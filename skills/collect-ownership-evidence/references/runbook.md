# collect-ownership-evidence: execution reference

Working directory: repository root. Use `.venv/bin/python` after preflight.

## Canonical resources

- [Module guide](../../../src/housing_ownership/README.md): scope, outputs and non-claims.
- [Implementation](../../../src/housing_ownership/engine.py): budgets, sources and package builder.
- [Retained runs](../../../research/ownership-evidence/README.md): three live examples with replay check.

## Run

```sh
.venv/bin/python scripts/locate.py lookup "218 East 170 St, Bronx"   # address -> BBL
.venv/bin/python -m housing_ownership --bbl 2028310056 --run-id NAME
.venv/bin/python -m housing_ownership --replay runs/ownership/NAME     # no network
```

Output: `runs/ownership/NAME/package.json` with `records` (kind
`recorded_instrument` or `parcel_identity`; instruments carry
`doc_type_description`, `instrument_amount`, `dates`, `parties` with roles),
`conflicts`, `unknowns` and `non_claims`. `run.json` records the request budget.

## Reading the package

- Latest deed: the most recent `recorded_instrument` whose `instrument_family` is
  `deed`; `parties` give GRANTOR/SELLER and GRANTEE/BUYER.
- `instrument_amount` is the recorded amount on the instrument. Call it a recorded
  amount, not a price. Mortgage amounts are not outstanding balances.
- `conflicts` flags, for example, a PLUTO owner label that differs from the latest
  grantee; both stay visible.
- A run that is not `complete` had a failed source; say which and do not treat
  missing rows as empty.
