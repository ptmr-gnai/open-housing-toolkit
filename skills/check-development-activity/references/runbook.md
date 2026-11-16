# check-development-activity: execution reference

Working directory: repository root. Use `.venv/bin/python` after preflight.

## Canonical resources

- [Module guide](../../../src/housing_activity/README.md): sources, rules and limits.
- [Source registry](../../../src/housing_activity/sources.json): datasets, fields and signal rules.

## Run

```sh
.venv/bin/python -m housing_activity collect --discovery runs/NAME/discovery --out runs/NAME/activity
.venv/bin/python -m housing_activity collect --bbl 2031780001 --out runs/NAME/activity-lot   # one lot
.venv/bin/python -m housing_activity verify --run runs/NAME/activity
.venv/bin/python scripts/plan_lot.py shortlist --discovery runs/NAME/discovery --activity runs/NAME/activity
```

About 30 seconds for an area of 60–70 candidates. `--since-years` (default 3) sets
the look-back; `--as-of` fixes the end date. `--all-nonhousing` checks every
recorded-nonhousing lot instead of only ranked candidates.

## Outputs

`activity.json` (per lot: `status`, `latest`, `signals` with date, record and a
locator into the retained response), `packet.md`, `receipts.json` and every raw
response under `sources/`. `coverage_gaps` lists sources that published no rows for
the borough (in November 2026 the DOB NOW job-filings dataset held Brooklyn only).
