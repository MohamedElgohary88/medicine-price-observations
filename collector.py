#!/usr/bin/env python3
"""Read public supplier retail-price facts; publish only a verified complete sweep."""
from __future__ import annotations
import argparse
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from decimal import Decimal, InvalidOperation
from email.utils import parsedate_to_datetime
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import signal
import ssl
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import build_opener, HTTPSHandler, HTTPRedirectHandler, ProxyHandler, Request
import uuid

ORIGIN = 'https://russkaya-apteka.com'
MAX_BYTES = 4_000_000
HTTP_SECONDS = 8
SPACING_SECONDS = 2
BUDGET_SECONDS = 28 * 60
SAFE_HEADERS = {'date', 'age', 'cf-cache-status', 'x-cache', 'content-type',
                'cache-control', 'etag', 'last-modified'}
ANCHOR_KEY = 'glossy-crown-krem-dlia-piatok-s-mocevinoi-30-i-pantenolom-ot-suxosti-i-treshhin-50-g'
ANCHOR_SKU = '22261'
ANCHOR_TITLE = 'Glossy Crown Cream with 30% urea and panthenol for dry and cracked heels 50 g'

class RefreshError(Exception):
    """Stable public error codes; never raw HTTP bodies or exception details."""
    def __init__(self, code, http_status=None):
        self.code, self.http_status = code, http_status
        super().__init__(code)

def validate_source_url(url: str) -> None:
    if not isinstance(url, str):
        raise RefreshError('source_url_rejected')
    listing = re.fullmatch(re.escape(ORIGIN) + r'/en/shop[?]page=([1-9][0-9]{0,2})', url)
    detail = re.fullmatch(re.escape(ORIGIN) + r'/en/products/[a-z0-9][a-z0-9-]{0,999}', url)
    if not detail and not (listing and int(listing[1]) <= 500):
        raise RefreshError('source_url_rejected')


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise RefreshError('source_redirect_rejected', code)


@contextmanager
def request_deadline(seconds: float):
    """An absolute Unix deadline also bounds slow-drip DNS/TLS/body reads."""
    if not hasattr(signal, 'SIGALRM'):
        raise RefreshError('request_deadline_unavailable')
    def expired(signum, frame):
        raise RefreshError('source_request_timeout')
    old_handler = signal.signal(signal.SIGALRM, expired)
    old_timer = signal.setitimer(signal.ITIMER_REAL, seconds)
    started = time.monotonic()
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old_handler)
        if old_timer[0] or old_timer[1]:
            signal.setitimer(signal.ITIMER_REAL, max(0.000001, old_timer[0] - (time.monotonic() - started)), old_timer[1])


@dataclass(frozen=True)
class Receipt:
    source_url: str
    observed_at: datetime
    sha256: str
    response_bytes: int
    headers: dict

    def public_metadata(self) -> dict:
        return {'source_url': self.source_url, 'observed_at': self.observed_at.isoformat(),
                'http_status': 200, 'response_sha256': self.sha256,
                'response_bytes': self.response_bytes, 'headers': self.headers}


class Fetcher:
    def __init__(self, *, opener=None, now=None, monotonic=None, sleep=None):
        # No proxy, cookie jar, challenge handling, browser impersonation, or retry.
        self.opener = opener if opener is not None else build_opener(
            ProxyHandler({}), NoRedirect(), HTTPSHandler(context=ssl.create_default_context()))
        self.now = now or (lambda: datetime.now(timezone.utc))
        self.monotonic = monotonic or time.monotonic
        self.sleep = sleep or time.sleep
        self.deadline = self.monotonic() + BUDGET_SECONDS
        self.next_allowed = self.monotonic()

    def check_budget(self):
        if self.monotonic() >= self.deadline:
            raise RefreshError('source_time_budget_exceeded')

    def fetch(self, url: str) -> tuple[str, Receipt]:
        validate_source_url(url)
        self.check_budget()
        pause = self.next_allowed - self.monotonic()
        if pause > 0:
            self.sleep(pause)
        self.check_budget()
        request = Request(url, headers={
            'User-Agent': 'MedicinePriceObservations/1.0 (public retail price collector)', 'Accept': 'text/html',
            'Cache-Control': 'no-cache', 'Pragma': 'no-cache', 'Accept-Encoding': 'identity'})
        try:
            with request_deadline(min(HTTP_SECONDS, self.deadline - self.monotonic())), self.opener.open(request, timeout=HTTP_SECONDS) as response:
                if response.status != 200:
                    raise RefreshError('source_http_error', response.status)
                if response.geturl() != url:
                    raise RefreshError('source_redirect_rejected')
                headers = {key.lower(): value for key, value in response.headers.items()}
                # Ambiguous freshness/length/type headers cannot establish a receipt.
                for key in ('date', 'age', 'content-length', 'content-type', 'content-encoding', 'cf-cache-status', 'x-cache'):
                    if len(response.headers.get_all(key, [])) > 1:
                        raise RefreshError('source_headers_ambiguous')
                self._validate_headers(headers)
                payload = response.read(MAX_BYTES + 1)
                observed_at = self.now()
        except HTTPError as error:
            error.close()
            raise RefreshError('source_http_error', error.code) from None
        except (URLError, TimeoutError, OSError):
            raise RefreshError('source_network_error') from None
        finally:
            self.next_allowed = self.monotonic() + SPACING_SECONDS
        self.check_budget()
        self._validate_headers(headers, observed_at)
        if not 1 <= len(payload) <= MAX_BYTES:
            raise RefreshError('source_response_size_rejected')
        if headers.get('content-length') is not None and int(headers['content-length']) != len(payload):
            raise RefreshError('source_response_length_mismatch')
        try:
            html = payload.decode('utf-8', errors='strict')
        except UnicodeDecodeError:
            raise RefreshError('source_encoding_rejected') from None
        if re.search(r'<title>\s*(Just a moment|Attention Required)|id=[\"\x27](challenge-form|cf-chl-widget|cf-challenge-running)', html, re.I):
            raise RefreshError('source_challenge')
        receipt = Receipt(url, observed_at, hashlib.sha256(payload).hexdigest(), len(payload),
                          {key: value for key, value in headers.items() if key in SAFE_HEADERS})
        return html, receipt

    def _validate_headers(self, headers: dict, received_at: datetime | None = None):
        content_type = headers.get('content-type', '')
        if not re.match(r'^text/html(?:\s*;|$)', content_type, re.I):
            raise RefreshError('source_content_type_rejected')
        if headers.get('content-encoding', 'identity').lower() != 'identity':
            raise RefreshError('source_content_encoding_rejected')
        declared = headers.get('content-length')
        if declared is not None and (not re.fullmatch(r'[0-9]+', declared) or not 1 <= int(declared) <= MAX_BYTES):
            raise RefreshError('source_response_size_rejected')
        age = headers.get('age')
        if age is not None and (not re.fullmatch(r'[0-9]+', age) or int(age) > 0):
            raise RefreshError('cached_response_not_renewed')
        if any(re.search(r'HIT|STALE|UPDATING|REVALIDATED', headers.get(key, ''), re.I)
               for key in ('cf-cache-status', 'x-cache')):
            raise RefreshError('cached_response_not_renewed')
        try:
            source_date = parsedate_to_datetime(headers['date'])
            if source_date.tzinfo is None:
                raise ValueError
            age_seconds = ((received_at or self.now()) - source_date).total_seconds()
            if age_seconds < -60 or age_seconds > 120:
                raise ValueError
        except (KeyError, TypeError, ValueError, OverflowError):
            raise RefreshError('source_date_rejected') from None


@dataclass
class Node:
    tag: str
    attrs: dict
    order: int
    children: list = field(default_factory=list)

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.walk()

    def text(self, skip_old=False):
        if self.tag in {'script', 'style'} or skip_old and self.tag in {'del', 's', 'strike'}:
            return ''
        return ''.join(child.text(skip_old) if isinstance(child, Node) else child for child in self.children)

    def has_class(self, name):
        return name in self.attrs.get('class', '').split()


class Document(HTMLParser):
    """Bounded structural parser. Cards are scoped by ordered main-list markers."""
    VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self, html):
        if not isinstance(html, str) or len(html.encode('utf-8')) > MAX_BYTES:
            raise RefreshError('html_bound')
        super().__init__(convert_charrefs=True)
        self.root = Node('document', {}, -1)
        self.stack = [self.root]
        self.nodes = []
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        if len(self.nodes) >= 100_000 or len(self.stack) > 200:
            raise RefreshError('html_structure_bound')
        if len({key for key, _ in attrs}) != len(attrs):
            raise RefreshError('html_attributes_ambiguous')
        node = Node(tag, {key: value or '' for key, value in attrs}, len(self.nodes))
        self.nodes.append(node)
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, text):
        self.stack[-1].children.append(text)


def normalized(text):
    return ' '.join(text.split())


def amount(text, *, symbol=False):
    match = re.fullmatch(r'([0-9]{1,10}(?:[.][0-9]{1,2})?)' + (r'\s*£' if symbol else ''), normalized(text))
    if not match:
        return None
    value = match[1]
    return value if Decimal('0') < Decimal(value) < Decimal('10000000000') else None


def parse_listing(html, requested_page):
    if type(requested_page) is not int or not 1 <= requested_page <= 500:
        raise RefreshError('listing_page_bound')
    doc = Document(html)
    headings = [n for n in doc.nodes if n.tag == 'h1']
    starts = [n for n in doc.nodes if n.has_class('products_showing')]
    ends = [n for n in doc.nodes if n.has_class('pagination_column_shop')]
    if len(headings) != 1 or normalized(headings[0].text()) != 'Medicines in Egypt' or len(starts) != 1 or len(ends) != 1 or starts[0].order >= ends[0].order:
        raise RefreshError('listing_scope_or_title')
    showing = re.fullmatch(r'Showing\s+([0-9]+)\s+of\s+([0-9]+)\s+products', normalized(starts[0].text()))
    if not showing or not 1 <= int(showing[2]) <= 20_000:
        raise RefreshError('listing_total')
    pagination = list(ends[0].walk())
    active = [n for n in pagination if n.tag == 'li' and n.has_class('active')]
    if len(active) != 1 or normalized(active[0].text()) != str(requested_page):
        raise RefreshError('listing_page_identity')
    max_page = requested_page
    for n in pagination:
        if n.tag == 'a' and n.attrs.get('href', '').startswith(ORIGIN + '/en/shop'):
            match = re.fullmatch(re.escape(ORIGIN) + r'/en/shop[?]page=([1-9][0-9]{0,2})', n.attrs['href'])
            if not match or int(match[1]) > 500:
                raise RefreshError('listing_pagination_url')
            max_page = max(max_page, int(match[1]))
    main = [n for n in doc.nodes if starts[0].order < n.order < ends[0].order and n.has_class('shop_products_outer')]
    if not 1 <= len(main) <= 60 or len(main) != int(showing[1]):
        raise RefreshError('listing_card_count')
    keys, skus, cards = set(), set(), []
    for node in main:
        nodes = list(node.walk())
        if any(n is not node and n.has_class('shop_products_outer') for n in nodes):
            raise RefreshError('listing_card_nested')
        if any(n.order >= ends[0].order for n in nodes):
            raise RefreshError('listing_card_scope')
        urls = {n.attrs['href'] for n in nodes if n.tag == 'a' and n.attrs.get('href', '') not in {'', '#'}}
        ids = {n.attrs[key] for n in nodes for key in ('data-product','data-product-id') if key in n.attrs}
        images = [n for n in nodes if n.tag == 'img' and 'alt' in n.attrs]
        titles = [n for n in nodes if n.tag == 'h3']
        if len(urls) != 1 or len(ids) != 1 or len(images) != 1 or len(titles) != 1:
            raise RefreshError('listing_card_identity_ambiguous')
        url, sku = next(iter(urls)), next(iter(ids))
        if not url.startswith(ORIGIN + '/en/products/'):
            raise RefreshError('listing_card_canonical_url')
        validate_source_url(url)
        if not re.fullmatch(r'[0-9]+', sku):
            raise RefreshError('listing_card_identity_ambiguous')
        key = url.removeprefix(ORIGIN + '/en/products/')
        title = normalized(images[0].attrs['alt'])
        if not 1 <= len(title) <= 2000:
            raise RefreshError('listing_card_title_bound')
        if key in keys or sku in skus:
            raise RefreshError('listing_duplicate_key_or_sku')
        keys.add(key); skus.add(sku)
        prices = [n for n in nodes if n.tag == 'p' and n.has_class('price-tooltip')]
        price = amount(prices[0].text(skip_old=True), symbol=True) if len(prices) == 1 else None
        reason = None
        if normalized(titles[0].text()) != title:
            price, reason = None, 'card_title_disagrees'
        elif price is None:
            reason = 'price_missing_zero_ambiguous_or_wrong_currency'
        cards.append({'source_key': key, 'source_sku': sku, 'source_url': url,
                      'source_title': title, 'price_egp': price, 'reason': reason})
    return {'total': int(showing[2]), 'max_page': max_page,
            'page_number': requested_page, 'cards': cards}


def unique_json_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise RefreshError('detail_json_ambiguous')
        result[key] = value
    return result


def parse_detail(html, card):
    doc = Document(html)
    headings = [n for n in doc.nodes if n.tag == 'h1']
    if len(headings) != 1 or normalized(headings[0].text()) != card['source_title']:
        raise RefreshError('detail_title')
    products = []
    for n in doc.nodes:
        if n.tag == 'script' and n.attrs.get('type') == 'application/ld+json':
            try:
                raw = ''.join(s for s in n.children if isinstance(s, str))
                p = json.loads(raw, object_pairs_hook=unique_json_pairs, parse_float=Decimal)
            except (ValueError, InvalidOperation):
                raise RefreshError('detail_json_rejected') from None
            if isinstance(p, dict) and p.get('@type') == 'Product':
                products.append(p)
    if len(products) != 1:
        raise RefreshError('detail_product_identity')
    p = products[0]
    if p.get('sku') != card['source_sku'] or not isinstance(p.get('name'), str) or normalized(p['name']) != card['source_title']:
        raise RefreshError('detail_product_identity')
    offer = p.get('offers')
    if not isinstance(offer, dict) or offer.get('@type') != 'Offer' or offer.get('priceCurrency') != 'EGP' or offer.get('url') != card['source_url']:
        raise RefreshError('detail_offer_identity_currency')
    price = amount(str(offer.get('price', '')))
    visible = next((n for n in doc.nodes if n.tag == 'h3' and n.order > headings[0].order), None)
    visible_price = amount(visible.text(skip_old=True), symbol=True) if visible else None
    if price is None or visible_price is None or Decimal(price) != Decimal(visible_price):
        raise RefreshError('detail_visible_price')
    return {'currency': 'EGP', 'price_egp': price, 'source_key': card['source_key'],
            'source_sku': card['source_sku']}


def utc_now():
    return datetime.now(timezone.utc)


def verify_anchor(fetcher, card):
    html, receipt = fetcher.fetch(card['source_url'])
    detail = parse_detail(html, card)
    if card['price_egp'] is None or Decimal(detail['price_egp']) != Decimal(card['price_egp']):
        raise RefreshError('currency_anchor_price_changed')
    return {'source_key': card['source_key'], 'source_sku': card['source_sku'],
            'source_url': card['source_url'], 'source_title': card['source_title'],
            'currency': 'EGP', 'price_egp': detail['price_egp'],
            'receipt': receipt.public_metadata()}


def collect(fetcher, now=utc_now):
    started = now()
    pages, keys, skus = [], set(), set()
    total = max_page = None
    anchor = None
    number = 1
    while number == 1 or number <= max_page:
        html, receipt = fetcher.fetch(f'{ORIGIN}/en/shop?page={number}')
        parsed = parse_listing(html, number)
        if total is None:
            total, max_page = parsed['total'], parsed['max_page']
        elif total != parsed['total'] or max_page != parsed['max_page']:
            raise RefreshError('sweep_pagination_changed')
        for card in parsed['cards']:
            if card['source_key'] in keys or card['source_sku'] in skus:
                raise RefreshError('sweep_duplicate_key_or_sku')
            keys.add(card['source_key']); skus.add(card['source_sku'])
            if card['source_sku'] == ANCHOR_SKU:
                if card['source_key'] != ANCHOR_KEY or card['source_title'] != ANCHOR_TITLE or card['price_egp'] is None:
                    raise RefreshError('currency_anchor_identity_changed')
                anchor = card
        parsed['receipt'] = receipt.public_metadata()
        pages.append(parsed)
        print(json.dumps({'status': 'page_verified', 'page': number, 'cards': len(parsed['cards'])}), flush=True)
        number += 1
    if len(keys) != total or len(pages) != max_page:
        raise RefreshError('sweep_total_mismatch')
    if anchor is None:
        raise RefreshError('currency_anchor_missing')
    currency_anchor = verify_anchor(fetcher, anchor)
    ended = now()
    observed = [datetime.fromisoformat(p['receipt']['observed_at']) for p in pages]
    observed.append(datetime.fromisoformat(currency_anchor['receipt']['observed_at']))
    if ended < started or ended < max(observed) or any(t < started - timedelta(seconds=60) for t in observed):
        raise RefreshError('clock_changed')
    return {'schema': 'source_price_feed_v1', 'sweep_id': str(uuid.uuid4()),
            'source_origin': ORIGIN, 'generated_at': ended.isoformat(),
            'sweep_started_at': started.isoformat(), 'pages': pages,
            'currency_anchor': currency_anchor}


def atomic_write(path, feed):
    payload = (json.dumps(feed, ensure_ascii=False, separators=(',', ':'), allow_nan=False) + '\n').encode('utf-8')
    if not 1 <= len(payload) <= MAX_BYTES:
        raise RefreshError('feed_size_rejected')
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name('.prices.' + uuid.uuid4().hex + '.tmp')
    try:
        with temporary.open('xb') as stream:
            stream.write(payload); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, path)
    except OSError:
        raise RefreshError('feed_write_failed') from None
    finally:
        temporary.unlink(missing_ok=True)


def execute(mode, fetcher, output=Path('data/prices.json'), now=utc_now):
    if mode == 'probe':
        html, receipt = fetcher.fetch(ORIGIN + '/en/shop?page=1')
        parsed = parse_listing(html, 1)
        card = next((card for card in parsed['cards'] if card['price_egp'] is not None and card['reason'] is None), None)
        if card is None:
            raise RefreshError('probe_no_priced_card')
        anchor = verify_anchor(fetcher, card)
        return {'status': 'probe_verified', 'http_status': 200, 'source_sha256': receipt.sha256,
                'main_cards': len(parsed['cards']), 'total': parsed['total'],
                'max_page': parsed['max_page'], 'currency': anchor['currency'],
                'source_sku': card['source_sku']}
    if mode != 'collect':
        raise RefreshError('mode_rejected')
    feed = collect(fetcher, now=now)
    atomic_write(output, feed)
    return {'status': 'sweep_verified', 'pages': len(feed['pages']),
            'cards': sum(len(p['cards']) for p in feed['pages']), 'sweep_id': feed['sweep_id']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('probe', 'collect'), default='probe')
    args = parser.parse_args()
    try:
        result = execute(args.mode, Fetcher())
    except RefreshError as error:
        print(json.dumps({'status': 'failed', 'code': error.code, 'http_status': error.http_status}), flush=True)
        return 1
    except Exception:
        print(json.dumps({'status': 'failed', 'code': 'unexpected_failure'}), flush=True)
        return 1
    print(json.dumps(result), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
