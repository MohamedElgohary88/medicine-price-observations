"""Portable stdlib tests; retained public page-one card facts, no live requests."""
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parent
CANDIDATE = ROOT / "collector.py" if (ROOT / "collector.py").exists() else ROOT.parent / "collector.py"
spec = importlib.util.spec_from_file_location("collector", CANDIDATE)
c = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = c
spec.loader.exec_module(c)

FIXTURE = '<h1>Medicines in Egypt</h1><div class="shop_products_outer"><img alt="Featured"><h3>Featured</h3></div><div class="products_showing"><p>Showing 33 of 5389 products</p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/glossy-crown-krem-dlia-piatok-s-mocevinoi-30-i-pantenolom-ot-suxosti-i-treshhin-50-g"><img alt="Glossy Crown Cream with 30% urea and panthenol for dry and cracked heels 50 g"></a><a data-product="22261"></a><div data-product-id="22261"></div><h3><a href="https://russkaya-apteka.com/en/products/glossy-crown-krem-dlia-piatok-s-mocevinoi-30-i-pantenolom-ot-suxosti-i-treshhin-50-g">Glossy Crown Cream with 30% urea and panthenol for dry and cracked heels 50 g</a></h3><p class="price-tooltip" title="9$ • 1€">110£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-kondicioner-dlia-volos-s-travianym-kompleksom-protiv-vypadeniia-i-pridaniia-bleska-300-ml"><img alt="Hebatt Sanus Hair Conditioner with herbal complex against hair loss and for enhanced shine 300 ml"></a><a data-product="22260"></a><div data-product-id="22260"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-kondicioner-dlia-volos-s-travianym-kompleksom-protiv-vypadeniia-i-pridaniia-bleska-300-ml">Hebatt Sanus Hair Conditioner with herbal complex against hair loss and for enhanced shine 300 ml</a></h3><p class="price-tooltip" title="9$ • 1€">320£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-kondicioner-s-proteinovym-kompleksom-i-keratinom-dlia-povrezdennyx-volos-300-ml"><img alt="Hebatt Sanus Hair Protein complex &amp; keratin conditioner for damaged hair 300 ml"></a><a data-product="22259"></a><div data-product-id="22259"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-kondicioner-s-proteinovym-kompleksom-i-keratinom-dlia-povrezdennyx-volos-300-ml">Hebatt Sanus Hair Protein complex &amp; keratin conditioner for damaged hair 300 ml</a></h3><p class="price-tooltip" title="9$ • 1€">320£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/gofit-kompleks-vitaminov-d3-i-k2-dlia-podderzki-kostei-i-immuniteta-30-tabletok"><img alt="GoFit D3 + K2 vitamin complex for bone and immune support 30 tablets"></a><a data-product="22258"></a><div data-product-id="22258"></div><h3><a href="https://russkaya-apteka.com/en/products/gofit-kompleks-vitaminov-d3-i-k2-dlia-podderzki-kostei-i-immuniteta-30-tabletok">GoFit D3 + K2 vitamin complex for bone and immune support 30 tablets</a></h3><p class="price-tooltip" title="9$ • 1€">245£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/gofit-vitaminy-gruppy-v-dlia-podderzki-nervnoi-sistemy-i-energii-30-tabletok"><img alt="GoFit B Complex vitamins B group for nervous system support and energy 30 tablets"></a><a data-product="22257"></a><div data-product-id="22257"></div><h3><a href="https://russkaya-apteka.com/en/products/gofit-vitaminy-gruppy-v-dlia-podderzki-nervnoi-sistemy-i-energii-30-tabletok">GoFit B Complex vitamins B group for nervous system support and energy 30 tablets</a></h3><p class="price-tooltip" title="9$ • 1€">195£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/xebatt-razogrevaiushhii-krem-dlia-mysc-i-sustavov-s-kolocintovym-maslom-150-g"><img alt="Hebatt Warming cream for muscles and joints with colocynth oil 150 g"></a><a data-product="22256"></a><div data-product-id="22256"></div><h3><a href="https://russkaya-apteka.com/en/products/xebatt-razogrevaiushhii-krem-dlia-mysc-i-sustavov-s-kolocintovym-maslom-150-g">Hebatt Warming cream for muscles and joints with colocynth oil 150 g</a></h3><p class="price-tooltip" title="9$ • 1€">320£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/oruoa-sprei-dlia-uxoda-za-polostiu-rta-i-gorlom-s-maslom-cernogo-tmina-i-romaskoi-60-ml"><img alt="Oruoua Oral and throat care spray with black seed oil and chamomile 60 ml"></a><a data-product="22255"></a><div data-product-id="22255"></div><h3><a href="https://russkaya-apteka.com/en/products/oruoa-sprei-dlia-uxoda-za-polostiu-rta-i-gorlom-s-maslom-cernogo-tmina-i-romaskoi-60-ml">Oruoua Oral and throat care spray with black seed oil and chamomile 60 ml</a></h3><p class="price-tooltip" title="9$ • 1€">125£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/oruoa-sprei-dlia-uxoda-za-polostiu-rta-s-ekstraktom-exinacei-60-ml"><img alt="Oruoua Oral care spray with echinacea extract 60 ml"></a><a data-product="22254"></a><div data-product-id="22254"></div><h3><a href="https://russkaya-apteka.com/en/products/oruoa-sprei-dlia-uxoda-za-polostiu-rta-s-ekstraktom-exinacei-60-ml">Oruoua Oral care spray with echinacea extract 60 ml</a></h3><p class="price-tooltip" title="9$ • 1€">125£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/oruoa-sprei-dlia-uxoda-za-polostiu-rta-s-ekstraktom-pliushha-i-timianom-60-ml"><img alt="Oruoua Oral care spray with ivy leaf extract and thyme 60 ml"></a><a data-product="22253"></a><div data-product-id="22253"></div><h3><a href="https://russkaya-apteka.com/en/products/oruoa-sprei-dlia-uxoda-za-polostiu-rta-s-ekstraktom-pliushha-i-timianom-60-ml">Oruoua Oral care spray with ivy leaf extract and thyme 60 ml</a></h3><p class="price-tooltip" title="9$ • 1€">125£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/oruoa-sprei-dlia-uxoda-za-polostiu-rta-s-propolisom-i-miatnym-vkusom-60-ml"><img alt="Oruoua Oral care spray with propolis and mint flavour 60 ml"></a><a data-product="22252"></a><div data-product-id="22252"></div><h3><a href="https://russkaya-apteka.com/en/products/oruoa-sprei-dlia-uxoda-za-polostiu-rta-s-propolisom-i-miatnym-vkusom-60-ml">Oruoua Oral care spray with propolis and mint flavour 60 ml</a></h3><p class="price-tooltip" title="9$ • 1€">100£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-sampun-s-proteinovym-kompleksom-i-keratinom-dlia-povrezdennyx-volos-300-ml"><img alt="Hebatt Sanus Hair Shampoo with protein complex and keratin for damaged hair 300 ml"></a><a data-product="22251"></a><div data-product-id="22251"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-sampun-s-proteinovym-kompleksom-i-keratinom-dlia-povrezdennyx-volos-300-ml">Hebatt Sanus Hair Shampoo with protein complex and keratin for damaged hair 300 ml</a></h3><p class="price-tooltip" title="9$ • 1€">320£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/epikotil-tenoksikam-20-mg-3-flakona-3-ampuly-po-2-ml"><img alt="Epicotil Tenoxicam 20 mg 3 vials + 3 ampoules 2 ml"></a><a data-product="22250"></a><div data-product-id="22250"></div><h3><a href="https://russkaya-apteka.com/en/products/epikotil-tenoksikam-20-mg-3-flakona-3-ampuly-po-2-ml">Epicotil Tenoxicam 20 mg 3 vials + 3 ampoules 2 ml</a></h3><p class="price-tooltip" title="9$ • 1€">48£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/kernel-vitamin-d3-4000-me-k2-pishhevaia-dobavka-dlia-podderzki-zdorovia-kostei-i-immunnoi-sistemy-60-tabletok"><img alt="Kernel Vitamin D3 4000 IU + K2 Dietary supplement for bone health and immune system support 60 tablets"></a><a data-product="22249"></a><div data-product-id="22249"></div><h3><a href="https://russkaya-apteka.com/en/products/kernel-vitamin-d3-4000-me-k2-pishhevaia-dobavka-dlia-podderzki-zdorovia-kostei-i-immunnoi-sistemy-60-tabletok">Kernel Vitamin D3 4000 IU + K2 Dietary supplement for bone health and immune system support 60 tablets</a></h3><p class="price-tooltip" title="9$ • 1€">320£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/kernel-kompleks-vitaminov-gruppy-b-s-folievoi-kislotoi-i-biotinom-pishhevaia-dobavka-dlia-podderzki-nervnoi-sistemy-60-kapsul"><img alt="Kernel Vitamin B Complex with folic acid and biotin Dietary supplement for nervous system support 60 capsules"></a><a data-product="22248"></a><div data-product-id="22248"></div><h3><a href="https://russkaya-apteka.com/en/products/kernel-kompleks-vitaminov-gruppy-b-s-folievoi-kislotoi-i-biotinom-pishhevaia-dobavka-dlia-podderzki-nervnoi-sistemy-60-kapsul">Kernel Vitamin B Complex with folic acid and biotin Dietary supplement for nervous system support 60 capsules</a></h3><p class="price-tooltip" title="9$ • 1€">295£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/kernel-cink-25-mg-pishhevaia-dobavka-dlia-podderzki-immunnoi-sistemy-60-kapsul"><img alt="Kernel Zinc 25 mg Dietary supplement for immune system support 60 capsules"></a><a data-product="22247"></a><div data-product-id="22247"></div><h3><a href="https://russkaya-apteka.com/en/products/kernel-cink-25-mg-pishhevaia-dobavka-dlia-podderzki-immunnoi-sistemy-60-kapsul">Kernel Zinc 25 mg Dietary supplement for immune system support 60 capsules</a></h3><p class="price-tooltip" title="9$ • 1€">275£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-sampun-dlia-volos-s-travianym-kompleksom-protiv-vypadeniia-i-dlia-bleska-300-ml"><img alt="Hebatt Sanus Hair Herbal shampoo for hair fall control and shine 300 ml"></a><a data-product="22246"></a><div data-product-id="22246"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-sampun-dlia-volos-s-travianym-kompleksom-protiv-vypadeniia-i-dlia-bleska-300-ml">Hebatt Sanus Hair Herbal shampoo for hair fall control and shine 300 ml</a></h3><p class="price-tooltip" title="9$ • 1€">320£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-ocishhaiushhaia-penka-dlia-umyvaniia-s-kollagenom-dlia-normalnoi-i-suxoi-kozi-200-ml"><img alt="Hebatt Collagen facial foam cleanser for normal to dry skin 200 ml"></a><a data-product="22245"></a><div data-product-id="22245"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-ocishhaiushhaia-penka-dlia-umyvaniia-s-kollagenom-dlia-normalnoi-i-suxoi-kozi-200-ml">Hebatt Collagen facial foam cleanser for normal to dry skin 200 ml</a></h3><p class="price-tooltip" title="9$ • 1€">320£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-omolazivaiushhaia-syvorotka-dlia-lica-s-kollagenom-50-ml"><img alt="Hebatt Collagen anti-ageing facial serum 50 ml"></a><a data-product="22244"></a><div data-product-id="22244"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-omolazivaiushhaia-syvorotka-dlia-lica-s-kollagenom-50-ml">Hebatt Collagen anti-ageing facial serum 50 ml</a></h3><p class="price-tooltip" title="9$ • 1€">390£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-collagen-ocishhaiushhii-gel-dlia-umyvaniia-kombinirovannoi-i-zirnoi-kozi-200-ml"><img alt="Hebatt Collagen Facial cleansing gel for combination and oily skin 200 ml"></a><a data-product="22243"></a><div data-product-id="22243"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-collagen-ocishhaiushhii-gel-dlia-umyvaniia-kombinirovannoi-i-zirnoi-kozi-200-ml">Hebatt Collagen Facial cleansing gel for combination and oily skin 200 ml</a></h3><p class="price-tooltip" title="9$ • 1€">320£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-sampun-protiv-perxoti-300-ml"><img alt="Hebatt Sanus Hair Anti-dandruff shampoo 300 ml"></a><a data-product="22242"></a><div data-product-id="22242"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-sanus-hair-sampun-protiv-perxoti-300-ml">Hebatt Sanus Hair Anti-dandruff shampoo 300 ml</a></h3><p class="price-tooltip" title="9$ • 1€">320£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/bikamreit-25-dlia-volos-i-nogtei-90-tabletok"><img alt="Bicamrate 25 For Hair &amp; nails 90 tablets"></a><a data-product="22241"></a><div data-product-id="22241"></div><h3><a href="https://russkaya-apteka.com/en/products/bikamreit-25-dlia-volos-i-nogtei-90-tabletok">Bicamrate 25 For Hair &amp; nails 90 tablets</a></h3><p class="price-tooltip" title="9$ • 1€">540£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-antivozrastnoi-krem-dlia-lica-s-morskim-kollagenom-i-gialuronovoi-kislotoi-protiv-morshhin-dlia-vsex-tipov-kozi-50-g"><img alt="Hebatt Anti-wrinkle face cream with marine collagen and hyaluronic acid for all skin types 50 g"></a><a data-product="22240"></a><div data-product-id="22240"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-antivozrastnoi-krem-dlia-lica-s-morskim-kollagenom-i-gialuronovoi-kislotoi-protiv-morshhin-dlia-vsex-tipov-kozi-50-g">Hebatt Anti-wrinkle face cream with marine collagen and hyaluronic acid for all skin types 50 g</a></h3><p class="price-tooltip" title="9$ • 1€">340£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/hebatt-glow-up-uvlazniaiushhii-losyon-dlia-suxoi-i-ocen-suxoi-cuvstvitelnoi-kozi-tela-250-ml"><img alt="Hebatt Glow Up Moisturizing body lotion for dry to very dry sensitive skin 250 ml"></a><a data-product="22239"></a><div data-product-id="22239"></div><h3><a href="https://russkaya-apteka.com/en/products/hebatt-glow-up-uvlazniaiushhii-losyon-dlia-suxoi-i-ocen-suxoi-cuvstvitelnoi-kozi-tela-250-ml">Hebatt Glow Up Moisturizing body lotion for dry to very dry sensitive skin 250 ml</a></h3><p class="price-tooltip" title="9$ • 1€">390£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/infinity-sprei-syvorotka-dezodorant-dlia-podmysek-s-zelenym-caem-200-ml"><img alt="Infinity Green tea underarm serum spray deodorant 200 ml"></a><a data-product="22238"></a><div data-product-id="22238"></div><h3><a href="https://russkaya-apteka.com/en/products/infinity-sprei-syvorotka-dezodorant-dlia-podmysek-s-zelenym-caem-200-ml">Infinity Green tea underarm serum spray deodorant 200 ml</a></h3><p class="price-tooltip" title="9$ • 1€">330£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/kernel-pishhevaia-dobavka-s-vitaminom-s-1000-mg-60-tabletok"><img alt="Kernel Vitamin C 1000 mg Dietary supplement 60 tablets"></a><a data-product="22237"></a><div data-product-id="22237"></div><h3><a href="https://russkaya-apteka.com/en/products/kernel-pishhevaia-dobavka-s-vitaminom-s-1000-mg-60-tabletok">Kernel Vitamin C 1000 mg Dietary supplement 60 tablets</a></h3><p class="price-tooltip" title="9$ • 1€">265£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/listerine-advanced-white-otbelivaiushhii-opolaskivatel-dlia-polosti-rta-osvezaiushhaia-miata-500-ml"><img alt="Listerine Advanced White whitening mouthwash, refreshing mint 500 ml"></a><a data-product="22236"></a><div data-product-id="22236"></div><h3><a href="https://russkaya-apteka.com/en/products/listerine-advanced-white-otbelivaiushhii-opolaskivatel-dlia-polosti-rta-osvezaiushhaia-miata-500-ml">Listerine Advanced White whitening mouthwash, refreshing mint 500 ml</a></h3><p class="price-tooltip" title="9$ • 1€">150£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/see-lit-osvetliaiushhii-rolikovyi-dezodorant-antiperspirant-svezest-48-casov-50-ml-x-2"><img alt="See Lit Whitening roll-on deodorant &amp; antiperspirant fresh 48h 50 ml x 2"></a><a data-product="22234"></a><div data-product-id="22234"></div><h3><a href="https://russkaya-apteka.com/en/products/see-lit-osvetliaiushhii-rolikovyi-dezodorant-antiperspirant-svezest-48-casov-50-ml-x-2">See Lit Whitening roll-on deodorant &amp; antiperspirant fresh 48h 50 ml x 2</a></h3><p class="price-tooltip" title="9$ • 1€">340£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/see-lit-osvetliaiushhii-rolikovyi-dezodorant-antiperspirant-saxarnaia-vata-48-casov-50-ml-x-2"><img alt="See Lit Whitening roll-on deodorant &amp; antiperspirant cotton candy 48h 50 ml x 2"></a><a data-product="22233"></a><div data-product-id="22233"></div><h3><a href="https://russkaya-apteka.com/en/products/see-lit-osvetliaiushhii-rolikovyi-dezodorant-antiperspirant-saxarnaia-vata-48-casov-50-ml-x-2">See Lit Whitening roll-on deodorant &amp; antiperspirant cotton candy 48h 50 ml x 2</a></h3><p class="price-tooltip" title="9$ • 1€">340£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/see-lit-osvetliaiushhii-rolikovyi-dezodorant-antiperspirant-proxladnyi-briz-48-casov-50-ml-x-2"><img alt="See Lit Whitening roll-on deodorant &amp; antiperspirant cool breeze 48h 50 ml x 2"></a><a data-product="22232"></a><div data-product-id="22232"></div><h3><a href="https://russkaya-apteka.com/en/products/see-lit-osvetliaiushhii-rolikovyi-dezodorant-antiperspirant-proxladnyi-briz-48-casov-50-ml-x-2">See Lit Whitening roll-on deodorant &amp; antiperspirant cool breeze 48h 50 ml x 2</a></h3><p class="price-tooltip" title="9$ • 1€">340£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/garnier-uvlazniaiushhii-krem-dlia-lica-s-vitaminom-c-dlia-vsex-tipov-kozi-85-ml"><img alt="Garnier Hydrating face cream with vitamin C for all skin types 85 ml"></a><a data-product="22231"></a><div data-product-id="22231"></div><h3><a href="https://russkaya-apteka.com/en/products/garnier-uvlazniaiushhii-krem-dlia-lica-s-vitaminom-c-dlia-vsex-tipov-kozi-85-ml">Garnier Hydrating face cream with vitamin C for all skin types 85 ml</a></h3><p class="price-tooltip" title="9$ • 1€">270£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/garnier-uvlazniaiushhii-krem-sorbet-dlia-lica-s-salicilovoi-kislotoi-dlia-vsex-tipov-kozi-85-ml"><img alt="Garnier Hydrating sorbet face cream with salicylic acid 85 ml"></a><a data-product="22230"></a><div data-product-id="22230"></div><h3><a href="https://russkaya-apteka.com/en/products/garnier-uvlazniaiushhii-krem-sorbet-dlia-lica-s-salicilovoi-kislotoi-dlia-vsex-tipov-kozi-85-ml">Garnier Hydrating sorbet face cream with salicylic acid 85 ml</a></h3><p class="price-tooltip" title="9$ • 1€">270£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/garnier-uvlazniaiushhii-krem-sorbet-dlia-lica-dlia-vsex-tipov-kozi-85-ml"><img alt="Garnier Hydrating sorbet face cream for all skin types 85 ml"></a><a data-product="22229"></a><div data-product-id="22229"></div><h3><a href="https://russkaya-apteka.com/en/products/garnier-uvlazniaiushhii-krem-sorbet-dlia-lica-dlia-vsex-tipov-kozi-85-ml">Garnier Hydrating sorbet face cream for all skin types 85 ml</a></h3><p class="price-tooltip" title="9$ • 1€">270£ <sup class="fa fa-info-circle"></sup></p></div><div class="shop_products_outer"><a href="https://russkaya-apteka.com/en/products/toriksava-120-mg-10-tabletok"><img alt="Torixava 120 mg 10 tablets"></a><a data-product="22228"></a><div data-product-id="22228"></div><h3><a href="https://russkaya-apteka.com/en/products/toriksava-120-mg-10-tabletok">Torixava 120 mg 10 tablets</a></h3><p class="price-tooltip" title="9$ • 1€">131£ <sup class="fa fa-info-circle"></sup></p></div><div class="pagination_column_shop"><ul><li class="active"><a>1</a></li><li><a href="https://russkaya-apteka.com/en/shop?page=164">164</a></li></ul></div>'

class ParserTests(unittest.TestCase):
    def test_retained_33_main_cards_ignore_featured_and_preserve_literal_titles(self):
        page = c.parse_listing(FIXTURE, 1)
        self.assertEqual((page["total"], page["max_page"], len(page["cards"])), (5389, 164, 33))
        first = page["cards"][0]
        self.assertEqual(first["source_sku"], "22261")
        self.assertEqual(first["price_egp"], "110")
        self.assertEqual(first["source_title"], "Glossy Crown Cream with 30% urea and panthenol for dry and cracked heels 50 g")
        self.assertTrue(any("50 g" in x["source_title"] for x in page["cards"]))


from datetime import datetime, timezone, timedelta
from email.message import Message
import hashlib
import io
import json
import tempfile
from unittest.mock import patch

NOW = datetime(2026, 10, 13, 8, 0, 0, tzinfo=timezone.utc)
ANCHOR_KEY = 'glossy-crown-krem-dlia-piatok-s-mocevinoi-30-i-pantenolom-ot-suxosti-i-treshhin-50-g'
ANCHOR_TITLE = 'Glossy Crown Cream with 30% urea and panthenol for dry and cracked heels 50 g'
ANCHOR_URL = 'https://russkaya-apteka.com/en/products/' + ANCHOR_KEY

def card(price='110£', sku='22261', title=ANCHOR_TITLE, key=ANCHOR_KEY):
    url='https://russkaya-apteka.com/en/products/'+key
    return f'<div class="shop_products_outer"><a href="{url}"><img alt="{title}"></a><a data-product="{sku}"></a><div data-product-id="{sku}"></div><h3><a href="{url}">{title}</a></h3><p class="price-tooltip" title="99$">{price}</p></div>'

def listing(cards=None, page=1, total=1, max_page=1):
    cards = [card()] if cards is None else cards
    return f'<h1>Medicines in Egypt</h1><div class="products_showing">Showing {len(cards)} of {total} products</div>'+''.join(cards)+f'<div class="pagination_column_shop"><li class="active"><a>{page}</a></li><a href="https://russkaya-apteka.com/en/shop?page={max_page}">{max_page}</a></div>'

def detail(price='110', currency='EGP'):
    product={'@type':'Product','name':ANCHOR_TITLE,'sku':'22261','offers':{'@type':'Offer','priceCurrency':currency,'price':price,'url':ANCHOR_URL}}
    return '<script type="application/ld+json">'+json.dumps(product)+'</script><h1>'+ANCHOR_TITLE+'</h1><h3>'+price+'£</h3>'

class StrictParserTests(unittest.TestCase):
    def test_current_price_ignores_old_price_and_tooltip_currency(self):
        self.assertEqual(c.parse_listing(listing([card('<del>300£</del>110.50£')]),1)['cards'][0]['price_egp'],'110.50')
    def test_zero_range_missing_and_wrong_currency_are_unpriced(self):
        for amount in ['0£','110-120£','110$','','£110','11.234£','1e2£']:
            with self.subTest(amount=amount):
                p=c.parse_listing(listing([card(amount)]),1)['cards'][0]
                self.assertIsNone(p['price_egp'])
                self.assertEqual(p['reason'],'price_missing_zero_ambiguous_or_wrong_currency')
    def test_title_disagreement_holds_price(self):
        p=c.parse_listing(listing().replace('<h3><a href="'+ANCHOR_URL+'">'+ANCHOR_TITLE, '<h3><a href="'+ANCHOR_URL+'">Changed 100 g'),1)['cards'][0]
        self.assertEqual(p['reason'],'card_title_disagrees')
        self.assertIsNone(p['price_egp'])
    def test_duplicate_sku_or_key_aborts(self):
        for cards in [[card(),card()], [card(),card(sku='2')], [card(),card(key='different')]]:
            with self.subTest(cards=cards):
                with self.assertRaises(c.RefreshError): c.parse_listing(listing(cards,total=2),1)
    def test_identity_extra_image_or_conflicting_sku_aborts(self):
        for suffix in ['<img alt="Other">','<b data-product-id="2"></b>']:
            with self.assertRaises(c.RefreshError): c.parse_listing(listing([card().replace('</h3>', '</h3>'+suffix)]),1)
    def test_page_title_count_and_scope_fail_closed(self):
        for html in [listing(page=2),listing().replace('Medicines in Egypt','Other'),listing().replace('Showing 1','Showing 2'),listing().replace('products_showing','unknown')]:
            with self.assertRaises(c.RefreshError): c.parse_listing(html,1)
    def test_detail_currency_identity_visible_price_and_duplicate_product(self):
        good=c.parse_listing(listing(),1)['cards'][0]
        self.assertEqual(c.parse_detail(detail(),good)['price_egp'],'110')
        for html in [detail(currency='USD'),detail().replace('<h3>110','<h3>120'),detail().replace('"sku": "22261"','"sku": "2"'),detail()+detail(),detail().replace('</h1>','</h1><h1>'+ANCHOR_TITLE+'</h1>')]:
            with self.assertRaises(c.RefreshError): c.parse_detail(html,good)
    def test_literal_dose_and_quantity_are_preserved(self):
        title='Medicine &amp; 30 mg 100 tablets'
        p=c.parse_listing(listing([card(title=title)]),1)['cards'][0]
        self.assertEqual(p['source_title'],'Medicine & 30 mg 100 tablets')

class Response:
    def __init__(self, body, url='https://russkaya-apteka.com/en/shop?page=1', headers=None, status=200):
        self.payload=body.encode(); self.status=status; self.url=url; self.headers=Message()
        for key,value in (headers or {'Date':'Tue, 13 Oct 2026 08:00:00 GMT','Content-Type':'text/html; charset=utf-8','Content-Length':str(len(self.payload))}).items(): self.headers[key]=value
    def geturl(self): return self.url
    def read(self,n): return self.payload[:n]
    def __enter__(self): return self
    def __exit__(self,*args): return None

class Opener:
    def __init__(self,response): self.response=response; self.request=None
    def open(self,request,timeout): self.request=request; return self.response

class NetworkTests(unittest.TestCase):
    def fetch(self, response):
        op=Opener(response)
        f=c.Fetcher(opener=op,now=lambda:NOW,sleep=lambda _:None)
        return f.fetch('https://russkaya-apteka.com/en/shop?page=1'),op
    def test_success_receipt_has_real_bytes_source_date_and_honest_agent(self):
        (html,r),op=self.fetch(Response(listing()))
        self.assertEqual(r.sha256,hashlib.sha256(html.encode()).hexdigest())
        self.assertEqual(r.response_bytes,len(html.encode()))
        self.assertEqual(r.public_metadata()['headers']['date'],'Tue, 13 Oct 2026 08:00:00 GMT')
        self.assertNotIn('Mozilla',op.request.get_header('User-agent'))
        self.assertEqual(op.request.get_header('Accept-encoding'),'identity')
    def test_redirect_foreign_url_and_http_fail(self):
        for response in [Response(listing(),url='https://example.com/'),Response(listing(),status=403)]:
            with self.assertRaises(c.RefreshError): self.fetch(response)
        with self.assertRaises(c.RefreshError): c.Fetcher().fetch('https://example.com/')
    def test_cache_stale_date_encoding_truncation_and_challenge_fail(self):
        for change in [{'Age':'1'},{'CF-Cache-Status':'HIT'},{'X-Cache':'STALE'},{'Date':'Tue, 13 Oct 2026 07:00:00 GMT'},{'Content-Encoding':'gzip'},{'Content-Length':'999999'},{'Content-Type':'application/json'}]:
            headers={'Date':'Tue, 13 Oct 2026 08:00:00 GMT','Content-Type':'text/html'};headers.update(change)
            with self.subTest(change=change):
                with self.assertRaises(c.RefreshError): self.fetch(Response(listing(),headers=headers))
        with self.assertRaises(c.RefreshError): self.fetch(Response('<title>Just a moment</title>'))
    def test_duplicate_headers_fail_and_polite_spacing(self):
        response=Response(listing());response.headers['Date']='Tue, 13 Oct 2026 08:00:00 GMT'
        with self.assertRaises(c.RefreshError): self.fetch(response)
        ticks=[0];pauses=[]
        def sleep(n): pauses.append(n);ticks[0]+=n
        f=c.Fetcher(opener=Opener(Response(listing())),now=lambda:NOW,monotonic=lambda:ticks[0],sleep=sleep)
        f.fetch('https://russkaya-apteka.com/en/shop?page=1');f.fetch('https://russkaya-apteka.com/en/shop?page=1')
        self.assertEqual(pauses,[2])

class FakeFetcher:
    def __init__(self,pages,anchor=None): self.pages=pages;self.anchor=anchor or detail();self.calls=[]
    def fetch(self,url):
        self.calls.append(url)
        if url==ANCHOR_URL: html=self.anchor
        else: html=self.pages[int(url.rsplit('=',1)[1])]
        payload=html.encode()
        return html,c.Receipt(url,NOW,hashlib.sha256(payload).hexdigest(),len(payload),{'date':'Tue, 13 Oct 2026 08:00:00 GMT','content-type':'text/html'})

class SweepTests(unittest.TestCase):
    def test_complete_sweep_dto_receipts_and_decimal_strings(self):
        f=FakeFetcher({1:listing(total=2,max_page=2),2:listing([card('22.50£','2','Medicine 22 mg 5 tablets','medicine')],2,2,2)})
        feed=c.collect(f,now=lambda:NOW)
        self.assertEqual(set(feed),{'schema','sweep_id','source_origin','generated_at','sweep_started_at','pages','currency_anchor'})
        self.assertEqual(feed['schema'],'source_price_feed_v1')
        self.assertEqual(feed['pages'][1]['cards'][0]['price_egp'],'22.50')
        self.assertEqual(feed['currency_anchor']['source_sku'],'22261')
        self.assertEqual(len(f.calls),3)
    def test_incomplete_unstable_duplicate_and_anchor_disagreement_never_replace_old_feed(self):
        sets=[{1:listing(total=2)}, {1:listing(total=2,max_page=2),2:listing([card('5£','2','Other','other')],2,3,2)}, {1:listing(total=2,max_page=2),2:listing(page=2,total=2,max_page=2)}]
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'data/prices.json';target.parent.mkdir();target.write_text('old')
            for pages in sets:
                with self.assertRaises(c.RefreshError): c.execute('collect',FakeFetcher(pages),target,now=lambda:NOW)
                self.assertEqual(target.read_text(),'old')
            with self.assertRaises(c.RefreshError):c.execute('collect',FakeFetcher({1:listing()},detail('120')),target,now=lambda:NOW)
            self.assertEqual(target.read_text(),'old')
    def test_probe_verifies_without_writing_feed(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'data/prices.json'
            result=c.execute('probe',FakeFetcher({1:listing()}),target,now=lambda:NOW)
            self.assertEqual(result['status'],'probe_verified')
            self.assertFalse(target.exists());self.assertFalse(target.parent.exists())
    def test_atomic_complete_json_write_and_size_gate(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'data/prices.json'
            c.atomic_write(target,{'ok':True})
            self.assertEqual(json.loads(target.read_text()),{'ok':True})
            with self.assertRaises(c.RefreshError):c.atomic_write(target,{'huge':'x'*4000000})
            self.assertEqual(json.loads(target.read_text()),{'ok':True})

class AdditionalSafetyTests(unittest.TestCase):
    def test_listing_link_cannot_stand_in_for_product_canonical_url(self):
        html=listing().replace(ANCHOR_URL,'https://russkaya-apteka.com/en/shop?page=1')
        with self.assertRaises(c.RefreshError):c.parse_listing(html,1)

    def test_foreign_link_in_main_card_is_ambiguous(self):
        html=listing().replace('<h3><a href="'+ANCHOR_URL+'">','<h3><a href="https://example.com/medicine">')
        with self.assertRaises(c.RefreshError):c.parse_listing(html,1)
    def test_unclosed_card_spanning_pagination_is_rejected(self):
        html=listing().replace('</p></div><div class="pagination_column_shop">','</p><div class="pagination_column_shop">')
        with self.assertRaises(c.RefreshError):c.parse_listing(html,1)
    def test_future_missing_date_nonzero_age_and_bounds_fail(self):
        for headers in [{'Content-Type':'text/html'}, {'Date':'Tue, 13 Oct 2026 08:02:00 GMT','Content-Type':'text/html'}, {'Date':'Tue, 13 Oct 2026 08:00:00 GMT','Content-Type':'text/html','Age':'-1'}, {'Date':'Tue, 13 Oct 2026 08:00:00 GMT','Content-Type':'text/html','Content-Length':'4000001'}]:
            with self.assertRaises(c.RefreshError):NetworkTests().fetch(Response(listing(),headers=headers))
    def test_duplicate_json_keys_and_wrong_offer_url_fail(self):
        good=c.parse_listing(listing(),1)['cards'][0]
        for html in [detail().replace('"sku": "22261"','"sku": "22261", "sku": "22261"'),detail().replace(ANCHOR_URL,'https://example.com')]:
            with self.assertRaises(c.RefreshError):c.parse_detail(html,good)
    def test_network_deadline_also_bounds_slow_drip_work(self):
        import time
        with self.assertRaises(c.RefreshError):
            with c.request_deadline(0.01):time.sleep(0.1)
    def test_total_budget_exhaustion_aborts_before_get(self):
        ticks=[0]
        f=c.Fetcher(opener=Opener(Response(listing())),now=lambda:NOW,monotonic=lambda:ticks[0])
        ticks[0]=1680
        with self.assertRaises(c.RefreshError):f.fetch('https://russkaya-apteka.com/en/shop?page=1')
    def test_capture_clock_regression_never_writes(self):
        later=NOW+timedelta(seconds=61)
        with self.assertRaises(c.RefreshError):c.collect(FakeFetcher({1:listing()}),now=lambda:later)


class PublisherTests(unittest.TestCase):
    def publisher(self):
        import ast, textwrap
        staging=ROOT / 'collect.yml'
        workflow=staging if staging.exists() else ROOT.parent / '.github/workflows/collect.yml'
        embedded=workflow.read_text().split("python3 - <<'PY'\n",1)[1].rsplit("          PY",1)[0]
        program=ast.parse(textwrap.dedent(embedded))
        program.body=[node for node in program.body if not isinstance(node, ast.Try)]
        namespace={}
        exec(compile(program,str(workflow),'exec'),namespace)
        return namespace
    def test_actual_publisher_sends_documented_committable_branch_shape(self):
        import base64, os
        publisher=self.publisher()
        calls=[]; head='a'*40
        def strict_api(query,variables):
            if query.lstrip().startswith('query'):
                return {'repository':{'ref':{'target':{'oid':head}}}}
            mutation=variables['input']
            # GitHub's CommittableBranch input has branchName; refName is invalid.
            self.assertEqual(mutation['branch'],{'repositoryNameWithOwner':'example/public-data','branchName':'main'})
            self.assertEqual(mutation['expectedHeadOid'],head)
            additions=mutation['fileChanges']['additions']
            self.assertEqual(len(additions),1)
            self.assertEqual(additions[0]['path'],'data/prices.json')
            self.assertEqual(json.loads(base64.b64decode(additions[0]['contents'])),document)
            calls.append(mutation)
            return {'createCommitOnBranch':{'commit':{'oid':'b'*40,'signature':{'isValid':True,'wasSignedByGitHub':True}}}}
        publisher['graphql']=strict_api
        document={'schema':'source_price_feed_v1','source_origin':'https://russkaya-apteka.com','pages':[{'page_number':1}]}
        with tempfile.TemporaryDirectory() as d:
            old=os.getcwd()
            try:
                os.chdir(d);Path('data').mkdir();Path('data/prices.json').write_text(json.dumps(document))
                with patch.dict(os.environ,{'GITHUB_REF':'refs/heads/main','GITHUB_REPOSITORY':'example/public-data','GITHUB_SHA':head},clear=True),patch('sys.stdout',new=io.StringIO()):
                    publisher['publish']()
            finally:os.chdir(old)
        self.assertEqual(len(calls),1)

if __name__ == "__main__":
    unittest.main()
