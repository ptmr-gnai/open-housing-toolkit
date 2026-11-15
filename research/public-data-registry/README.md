# BetaNYC registry: tested source-discovery reuse

The [BetaNYC NY data registry MCP](https://github.com/BetaNYC/ny-data-registry-mcp)
is a useful upstream resource. It locates portals, datasets, fields and possible
join keys; publisher APIs still provide the actual data. We reuse its published
metadata rather than building a competing statewide harvester or assuming
matching column names prove a valid join.

On November 9, 2026 (local date), we downloaded its pinned `index-2026-11-05`
release and checked both compressed and uncompressed SHA-256 sums. The SQLite
contains 9,569 dataset rows and 185,352 column rows. Its metadata records schema1,
registry date2026-11-05 and last harvest2026-11-05T18:44:22.100Z. The110MB file
remains local under runs/; selected metadata, authored query results, public
publisher API samples, hashes and receipts are retained here.

## Useful findings

| Resource | What we actually checked | Use in this toolkit |
| --- | --- | --- |
| NYC DCP zoning-by-tax-lot `fdkv-4t4z` | Catalog fields, live metadata, then bounded queries for all3,164 Bronx lots | New monthly zoning-record reconciliation; current published version20260930, distinct from PLUTO26v2 and Fast Tracker25v2.1 |
| HPD multiple dwelling registrations `tesw-yqqr` | Catalog fields and live metadata; numeric borough/block/lot rather than a BBL column | Additional housing signal, with source-specific coverage; not a complete inventory of all housing |
| HPD affordable production by building `hg8x-zxpr` | Catalog BBL/BIN and program/date/unit columns | Additional funded-development context; program activity is not all housing, availability or completion |
| Buffalo zoning `5843-jknb` | Publisher metadata and one live source row | Candidate for a separately scoped non-NYC jurisdiction adapter; NYC legal rules do not transfer |
| Rochester city-owned real estate inventory | ArcGIS service/layer metadata and one live source row | Public-site discovery source; no full Rochester inventory or title/availability analysis performed |
| Syracuse vacant properties | ArcGIS service/layer metadata and one live source row | Vacancy-register source for comparison; a register label alone does not establish present vacancy or availability |

The three non-NYC source probes returned successfully. `sources/live/` preserves
exact requests, responses and results. These samples prove only that the stated
requests worked, not complete coverage or usefulness of every record.

The source index also identifies storefront reports, environmental planning
areas, other municipal zoning/parcel resources and NYC BBL-linked housing tables.
`metadata-queries.json` preserves three bounded, explicitly filtered query sets.
They are not an exhaustive enumeration of all available public data. Null API
endpoints, missing columns and licensing metadata stay null.

## Replay and integration

```sh
python research/public-data-registry/validate.py
python research/public-data-registry/validate.py --index runs/betanyc-registry-probe/ny-data-index.sqlite
```

The first command verifies retained file/source hashes, metadata shape and the
three live-sample receipts. It clearly reports that the large catalog replay was
not run. The second additionally checks the pinned index hash and replays the
three metadata queries. The downloaded index is not silently replaced.

For continued exploration use BetaNYC's maintained MCP tools (`find_sources`,
`search_datasets`, `get_dataset_columns`, `find_joinable`, `how_to_query`) rather
than copying its search/harvest engine. The tool is optional; current toolkit
collection needs no MCP server, Node package, global configuration change or API
key. We have not installed or connected the server for the user. A new publisher
adapter still needs a verified endpoint/schema, scope, pagination, source terms,
join semantics, raw receipts and explicit failure states.

Original toolkit code MIT/prose CC BY4.0. The upstream MIT tool license does not
relicense the indexed publishers' metadata, property data or map layers; those
remain subject to their source terms.
