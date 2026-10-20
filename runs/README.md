# Parcel evidence runs

Bounded public ownership/transaction evidence for individual parcels, collected
by `parcel_evidence.py` under the 150-request / 50 MiB / 90-minute budget.
Each run directory is self-contained: raw source bodies (byte-hashed), source
records with exact URLs and timestamps, a request ledger, `run.json` (budget
accounting) and `package.json` (structured evidence).

**These packages are not title opinions.** They do not establish beneficial
ownership, current site control, or complete title research.

## Run

```sh
# collect one parcel (live; writes runs/<run-id>/)
python3.12 parcel_evidence.py --bbl 2028710002

# rebuild a package from an existing run (no requests)
python3.12 parcel_evidence.py --replay runs/run-20261020T020741Z-2028710002

# collect the ACRIS Document Control Codes mapping + dataset metadata receipts
# (runs/docs/; idempotent — cached receipts are reused without new requests)
python3.12 parcel_evidence.py --collect-docs

# discover candidate BBLs for an address (PLUTO prefix match; selection aid only)
python3.12 parcel_evidence.py --discover-address "150 WEST 82ND STREET" --borough 1

# offline tests (no network)
python3.12 -m unittest tests.test_parcel_evidence -v
```

Budget flags: `--budget-requests 150 --budget-bytes 52428800 --budget-seconds 5400`
(defaults are the proposed budget). Exhaustion stops the run cleanly; unfetched
sources become `source_missing` unknowns, never silent gaps.

`--session-budget <file>` accumulates a session-wide ledger (requests, bytes,
elapsed time, per-attempt entries) across documentation collection, discovery
and runs, so the 150/50 MiB/90 min cap covers the whole live session, not just
one run. Retries count as requests; error bodies count as bytes.

## Packages

| Run | Parcel | Requests / bytes | Records | Notes |
| --- | --- | --- | --- | --- |
| `run-20261020T020741Z-2028710002` | 2028710002 (1240 Edward L Grant Hwy) | 5 / 60,765 B | 50 | 48 ACRIS instruments (4 deeds, 11 mortgages, 3 releases, 30 other), 1 DOF sale, 1 PLUTO row |
| `run-20261020T020834Z-2028430040` | 2028430040 (1426 Townsend Ave) | 3 / 1,519 B | 1 | PLUTO row only; ACRIS and DOF sales returned no rows (verified genuine: neighboring lots in block 2843 do have ACRIS rows) |
| `run-20261020T031148Z-1012127503` | 1012127503 (150 West 82nd St, Manhattan) | 4 / 51,619 B | 41 | 40 DOF unit sales (same BBL/BIN 1032037), 1 PLUTO row; ACRIS legal empty in the 1966+ window (recorded as `acris_empty` unknown) |

Package contents: `records` (each with exact `locators` into source rows),
`other_parcels` (parcels covered by the same ACRIS documents), `conflicts`
(owner-label and good-through-date mismatches, with evidence locators),
`unknowns` (coverage bounds, missing joins, empty results, unrecognized codes),
`date_bounds` (earliest/latest document dates, dataset last-modified,
retrieval range), `truncation` (per-source limit vs row count),
`mapping_provenance` (which control-code dataset/rows drive the
doc_type→family and party_type→role mappings, with receipt + sha256),
`ownership_evidence` (`recorded_grantees` from recorded instruments, and
`current_owner.status = "unknown"` with the reason a current-owner conclusion
was not made), and `limitations`/`non_claims`.

## What works

- **Verified ACRIS mappings with retained receipts.** `doc_type` → instrument
  family and `party_type` → party role now use the NYC DOF "ACRIS - Document
  Control Codes" dataset (`7isb-wh4c`, 126 rows), fetched with receipts
  (`runs/docs/`): exact URLs, timestamps, sha256, and the official field
  descriptions from the master/parties dataset metadata. The keyword fallback
  is still present for codes missing from the mapping and is flagged per
  record.
- **Recorded grantee evidence vs current-owner conclusions.** Packages carry
  `ownership_evidence.recorded_grantees` (parties of recorded instruments,
  with roles from the control-code mapping) and an explicit
  `current_owner.status = "unknown"` with the reason. No package claims
  current ownership.
- **Instrument amounts are never sale prices.** ACRIS `document_amt` is
  recorded as `instrument_amount` with a note; DOF `sale_price` is the only
  sale-price field. Stated in `non_claims`.
- **Bounded fetch with retries.** Per-request byte cap, ≤2 retries per
  request, Retry-After honored (capped), exponential backoff, error bodies
  retained and byte-charged, retries counted in the ledger. A failed source
  yields a `failed` record + `source_missing` unknown, never a silent gap or
  a `complete` run.
- **Session budget ledger.** `--session-budget` accumulates requests/bytes/time
  across docs + discovery + runs; exhaustion raises `BudgetExceeded` and the
  run is marked incomplete.
- Deeds vs mortgages distinguished by ACRIS `doc_type` (control-code class,
  raw code always preserved; unclassified codes are unknowns, not guesses).
- Two-phase ACRIS join (legals by BBL → master/parties by document_id) with
  byte-level provenance reused from `collect.py` (`root=` parameter).
- Cross-source corroboration observed in run 1: DOF sale 2020-12-10
  $13,797,661 matches the latest ACRIS deed (document date 2020-12-10, amount
  13797661.13).
- Empty results handled as recorded unknowns (runs 2 and 3).
- Generalization: run 3 is a Manhattan condo (borough 1) vs the two Bronx
  parcels; different BBL padding, unit-level DOF sales, and an empty ACRIS
  window were all handled without code changes.
- Existing evidence untouched: `git diff b7f5de8` on the two earlier run
  directories is empty; `before-repin-*.json` / `after-repin-*.json` show each
  manifest re-pin changed only `outputs/manifest.json` (code-hash pin), all
  evidence files byte-identical.

## Concrete failures found and fixed

1. **BBL zero-padding**: ACRIS stores block/lot without zero padding; naive
   concatenation produced 9-digit "other parcel" BBLs. Fixed with
   `bbl_from_parts` normalization; caught by `test_other_parcels_from_same_records`.
2. **Coverage bound used latest deed, not latest document**: run 1 initially
   reported 2020-12-10; the audit's retained evidence shows 2023-02-10. Fixed
   to use the latest document of any family; replay now reports 2023-02-10.
3. **`validate.py` red after code changes**: the manifest pins code hashes;
   re-ran the deterministic pipeline to re-pin (only manifest changed).
4. **Party roles not identifiable**: the ACRIS parties dataset carries
   `party_type` codes with no verified role mapping in the Socrata metadata.
   Resolved this slice by locating the NYC DOF Document Control Codes dataset
   (`7isb-wh4c`), which pairs each `doc_type` with its party-role slots;
   receipts retained in `runs/docs/`.
5. **Session ledger keyword bug**: `bounded_fetch` charged the session ledger
   with `bytes=` while `SessionBudget.charge` takes `nbytes=`, so the first
   live docs run failed all 5 fetches after the requests were made. Fixed;
   regression test `test_session_charged_requests_and_bytes`. The failed
   attempt is preserved in `session-20261020T030707Z.budget.json`.
6. **PLUTO discovery field/format**: `borough` is a text code (`MN`/`BX`/…),
   not a digit, and street names are full ("WEST 82ND STREET", not
   "W 82ND ST"). Discovery now queries `borocode` with a prefix `like`;
   the probe history is recorded in the session ledger.

## What remains blocked / unknown

- **Current ownership**: PLUTO `owner1` is null for all three parcels; no
  source in the plan identifies a current owner. Cached DOB BIS filings for
  the lead parcel (2000–2015) name several business names (e.g. NEW COVENANT
  CHURCH, 1240-50 PARKING LLC), but those are filing names, not ownership
  evidence.
- **Run 2 (2028430040)**: no ACRIS records in the 1966+ window and no DOF
  sales rows; pre-1966 history, lot mergers/splits, and alias coverage are
  unresolved.
- **Run 3 (1012127503)**: no ACRIS legal rows in the 1966+ window (recorded
  as `acris_empty`); the 40 DOF unit sales are reported prices, not deed
  evidence.
- **Staten Island and pre-1966 records** are outside ACRIS coverage.
- **Native ACRIS document images** were not retrieved; index rows only.
- DOF sales dataset is the "NYC Citywide Annualized Calendar Sales Update"
  feed; the classic Property Sales dataset was not located during discovery.
- The control-code mapping is a point-in-time snapshot (receipts in
  `runs/docs/`); if DOF revises the dataset, re-run `--collect-docs` and
  compare sha256.

## Session budget accounting (2026-10-20 live session)

`runs/session-20261020T030812Z.budget.json`: 28 requests / 164,368 bytes /
218.65 s against the 150 / 50 MiB / 5400 s cap. Entries: 5 documentation
fetches, 6 discovery fetches, 13 manual PLUTO probes (each labeled), and the
run-3 collection (4 requests). `runs/session-20261020T030707Z.budget.json`
records the 5 failed attempts from the ledger-keyword bug (requests were made;
bodies were not byte-charged).

## Checks

Full suite after the final edits: `pipeline.py`, `lint.py`, 54 unit tests,
`schema_check.py` (needs `.venv` with `requirements-dev.txt`), `validate.py`,
`replay_check.py` — all passing.
