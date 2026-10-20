# Session budget reconciliation (2026-10-20 live session)

This document reconciles the two retained session ledgers and the three run
budgets from the 2026-10-20 live session. **Both original ledger files are
preserved unmodified.** No exact total for the whole session can be proved
from the ledgers alone; the gaps are identified openly below.

## Retained ledgers (originals, unmodified)

| File | Requests | Bytes charged | Elapsed | Notes |
|---|---|---|---|---|
| `runs/session-20261020T030707Z.budget.json` | 5 | 0 | 1.133 s | First docs batch; failed with a `TypeError` after requests were made and bodies received. Bodies were **discarded and never charged** (the bug fixed in this slice). |
| `runs/session-20261020T030812Z.budget.json` | 28 | 164,368 | 218.643 s | Successful session: docs re-fetch, discovery, manual probes, run 3. |

## Session 2 breakdown (28 requests / 164,368 bytes)

| Activity | Requests | Bytes |
|---|---|---|
| 5 documentation fetches (doc codes + 4 metadata) | 5 | 112,731 |
| 6 PLUTO discovery fetches (empty `[]` results) | 6 | 18 |
| 13 manual PLUTO probes (one-liners, bodies discarded) | 13 | 0 (not charged) |
| 4 run-3 fetches (PLUTO, ACRIS legals, DOF sales, doc codes re-fetch) | 4 | 27,615 |
| **Total** | **28** | **164,368** |

The doc-codes body (24,004 bytes) appears twice in the ledger: once in the
docs batch (03:08:12) and once in run 3 (03:11:51). Both are real, separate
requests (run 3's directory had no cached copy).

## First failed docs batch (session 1)

5 requests were made and 5 response bodies were received, then a `TypeError`
(`SessionBudget.charge() got an unexpected keyword argument 'bytes'`) aborted
the collection before the bodies were written or charged. The exact received
byte count **cannot be proved** (bodies discarded). It is bounded above by
112,731 bytes: the identical 5 URLs were re-fetched 65 seconds later in
session 2 and charged exactly that amount.

## Run budgets (separate from session ledgers)

| Run | Requests | Bytes | Elapsed |
|---|---|---|---|
| `run-20261020T020741Z-2028710002` | 5 | 60,765 | 2.963 s |
| `run-20261020T020834Z-2028430040` | 3 | 1,519 | 1.122 s |
| `run-20261020T031148Z-1012127503` | 4 | 51,619 | 2.999 s |

Runs 1 and 2 were executed in the earlier session **before the session
ledger existed**; they are accounted only by their run budgets, not by any
session file. Run 3 is accounted by both its run budget and session 2.

## Pre-ledger reconnaissance (not in any ledger)

Before the session ledger existed, the following live requests were made
during source discovery. They are **not recorded in any ledger file** and
their byte counts cannot be proved:

- 3 Socrata metadata probes (ACRIS parties / master / legals datasets)
- 1 `acris.nyc.gov` request (DNS failure)
- 1–2 ACRIS help-page fetches (JavaScript-only content)
- 1–2 requests locating the `7isb-wh4c` Document Control Codes dataset
- 1 initial fetch of the 126-row doc-codes dataset (later re-fetched in
  session 2 with a retained receipt)

Roughly 7–9 requests in total; exact count and bytes unknown.

## What can and cannot be asserted

- **Provable from ledgers:** session 1 = 5 requests / 0 bytes charged;
  session 2 = 28 requests / 164,368 bytes; runs 1–3 = 12 requests /
  113,903 bytes (run budgets).
- **Not provable:** exact bytes received by the failed session-1 batch
  (bounded by 112,731); all pre-ledger reconnaissance bytes; the 13 manual
  probe bodies (discarded, 0 bytes charged).
- **The later ledger alone does not cover the whole session.** It covers
  only the activity after 03:08:12Z. The failed batch, runs 1–2, and the
  pre-ledger reconnaissance are additional.
- No exact whole-session total is asserted here; inventing one would be
  false accounting.

## Forward fix

The corrected `SessionBudget.charge` persists before checking, the
`BoundedReader` charges received bytes per chunk (including partial and
error bodies), and `bounded_fetch` charges the session once per attempt with
the full received body. Future sessions using `--session-budget` will have
complete per-attempt accounting from the first request.
