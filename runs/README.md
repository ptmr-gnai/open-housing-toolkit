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

# offline tests (no network)
python3.12 -m unittest tests.test_parcel_evidence -v
```

Budget flags: `--budget-requests 150 --budget-bytes 52428800 --budget-seconds 5400`
(defaults are the proposed budget). Exhaustion stops the run cleanly; unfetched
sources become `source_missing` unknowns, never silent gaps.

## Packages

| Run | Parcel | Requests / bytes | Records | Notes |
| --- | --- | --- | --- | --- |
| `run-20261020T020741Z-2028710002` | 2028710002 (1240 Edward L Grant Hwy) | 5 / 60,765 B | 50 | 48 ACRIS instruments (4 deeds, 11 mortgages, 3 releases, 30 other), 1 DOF sale, 1 PLUTO row |
| `run-20261020T020834Z-2028430040` | 2028430040 (1426 Townsend Ave) | 3 / 1,519 B | 1 | PLUTO row only; ACRIS and DOF sales returned no rows (verified genuine: neighboring lots in block 2843 do have ACRIS rows) |

Package contents: `records` (each with exact `locators` into source rows),
`other_parcels` (parcels covered by the same ACRIS documents), `conflicts`
(owner-label and good-through-date mismatches, with evidence locators),
`unknowns` (coverage bounds, missing joins, unrecognized codes), and
`limitations`/`non_claims`.

## What works

- Deeds vs mortgages distinguished by ACRIS `doc_type` (keyword triage, raw
  code always preserved; unclassified codes are unknowns, not guesses).
- Two-phase ACRIS join (legals by BBL → master/parties by document_id) with
  byte-level provenance reused from `collect.py` (`root=` parameter).
- Cross-source corroboration observed in run 1: DOF sale 2020-12-10
  $13,797,661 matches the latest ACRIS deed (document date 2020-12-10, amount
  13797661.13).
- Empty results handled as recorded unknowns (run 2).
- Existing evidence untouched: pre/post snapshots in
  `before-live-runs.json` / `after-live-runs.json` show only
  `parcel_evidence.py` changed; `before-pipeline-repin.json` /
  `after-pipeline-repin.json` show the manifest re-pin changed only
  `outputs/manifest.json` (code-hash pin), all evidence files byte-identical.

## Concrete failures found and fixed

1. **BBL zero-padding**: ACRIS stores block/lot without zero padding; naive
   concatenation produced 9-digit "other parcel" BBLs. Fixed with
   `bbl_from_parts` normalization; caught by `test_other_parcels_from_same_records`.
2. **Coverage bound used latest deed, not latest document**: run 1 initially
   reported 2020-12-10; the audit's retained evidence shows 2023-02-10. Fixed
   to use the latest document of any family; replay now reports 2023-02-10.
3. **`validate.py` red after `collect.py` change**: the manifest pins code
   hashes; re-ran the deterministic pipeline to re-pin (only manifest changed).
4. **Party roles not identifiable**: the ACRIS parties dataset carries
   `party_type` codes (1, 2) with no verified role mapping. Not guessed;
   recorded as a `party_role` unknown. Owner-label conflict checks run only
   when a grantee is actually identified.

## What remains blocked / unknown

- **Grantor/grantee roles**: `party_type` code mapping unverified; party names
  are preserved with locators but roles are unknown.
- **Current ownership**: PLUTO `owner1` is null for both parcels in this run;
  no source in the plan identifies a current owner. Cached DOB BIS filings for
  the lead parcel (2000–2015) name several business names (e.g. NEW COVENANT
  CHURCH, 1240-50 PARKING LLC), but those are filing names, not ownership
  evidence.
- **Run 2 (2028430040)**: no ACRIS records in the 1966+ window and no DOF
  sales rows; pre-1966 history, lot mergers/splits, and alias coverage are
  unresolved.
- **Staten Island and pre-1966 records** are outside ACRIS coverage.
- **Native ACRIS document images** were not retrieved; index rows only.
- DOF sales dataset is the "NYC Citywide Annualized Calendar Sales Update"
  feed; the classic Property Sales dataset was not located during discovery.

## Checks

Full suite after the final edits: `pipeline.py`, `lint.py`, 31 unit tests,
`schema_check.py` (needs `.venv` with `requirements-dev.txt`), `validate.py`,
`replay_check.py` — all passing.
