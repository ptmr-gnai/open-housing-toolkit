# Ownership and transaction evidence

For one NYC tax lot (BBL), collect recorded instruments from ACRIS (deeds,
mortgages, agreements and other filings, with parties and amounts), DOF sales
rows and the PLUTO tax-roll row, then assemble a package of records with exact
source locators, conflicts and unknowns. Document types are classified with the
ACRIS Document Control Codes dataset, retained with the run.

```sh
python -m housing_ownership --bbl 2028310056
```

Output goes to `runs/ownership/<run-id>/`: raw response bodies with byte hashes,
source records with URLs and timestamps, `run.json` (budget accounting) and
`package.json` (records, conflicts, unknowns, non-claims). Replay without network:

```sh
python -m housing_ownership --replay runs/ownership/<run-id>
```

Collection is bounded (150 requests, 50 MiB, 90 minutes by default, sequential,
at most two retries, Retry-After honoured). A run is `complete` only when every
planned source returned successfully. Standard library only.

## What it does and does not establish

- Recorded grantees are parties to recorded instruments, not a current-owner
  conclusion. The PLUTO owner name is a tax-roll label that can lag a sale; a
  mismatch with the latest deed is reported as a conflict, not resolved.
- Instrument amounts are recorded amounts, never sale prices. DOF `sale_price`
  is the only sale-price field; condo rows are unit-level sales.
- ACRIS open data covers 1966 onward and excludes Staten Island. Absence of a
  record is not proof of absence. This is not a title opinion and does not
  establish beneficial ownership or site control.

Retained live runs and their replay check: [research/ownership-evidence](../../research/ownership-evidence/README.md).
Wider source list: [source catalog](../../docs/reference/source-catalog.md).
