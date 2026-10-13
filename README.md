# Source price feed

This repository collects literal public medicine listing facts from [russkaya-apteka.com](https://russkaya-apteka.com): source titles, source SKUs, source URLs, and displayed retail prices. Prices use the source's verified Egyptian-pound currency anchor and are stored as decimal strings. A missing price remains `null` with a reason.

The output is `data/prices.json`. It contains a sweep identifier, UTC observation times, the source origin, page counts, source records, and response receipts. Each receipt records the requested source URL, HTTP status, response size and SHA-256, and a limited set of response headers. The currency anchor has its own source record and receipt.

Only a complete validated sweep replaces the output. Validation failures leave the previous output intact and prevent the workflow's publication step from running.

## Run locally

Python 3 and its standard library are sufficient.

```sh
python3 -m unittest discover -s tests
python3 collector.py --mode probe
python3 collector.py --mode collect
```

`probe` checks the public source without persisting or publishing an output. `collect` checks the full listing sweep and atomically writes `data/prices.json` after validation succeeds.

## Scheduled collection

The workflow runs collection daily at 03:20 UTC. Manual runs offer `probe` (the default) and `collect`. Probe jobs have read-only repository permissions. Collection jobs can update repository contents, and the publication step receives only the workflow's standard `GITHUB_TOKEN`.

Publication updates only `data/prices.json` on `main` through GitHub's `createCommitOnBranch` API. The workflow reads the branch head, checks that it still matches the run's revision, and supplies `expectedHeadOid` for the atomic update. It checks the returned commit's GitHub signature. See [GitHub's commit API reference](https://docs.github.com/en/graphql/reference/commits#createcommitonbranch).

The data represents the source's observed listing facts at the recorded times. Titles and SKUs retain their source meaning; this feed does not add medicine identity matches or clinical information.
