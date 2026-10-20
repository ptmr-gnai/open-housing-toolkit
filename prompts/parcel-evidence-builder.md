# Parcel evidence builder

This is a future work prompt, not authorization to execute it now. Build composable, independently callable agent tools acting on behalf of humans. Start with machine-readable evidence contracts; reports and image generation are downstream consumers. No dashboard, 3D engine, or Valdrada dependency.

## Before implementation

Read repository instructions, README.md, CONTRIBUTING.md, collect.py, pipeline.py, schemas/, replay_check.py, research/source-audit/, and research/conclusion-probe/. Report actual available capabilities, existing reusable components, gaps, environment constraints, and proposed files before coding. Do not claim a capability merely because a source or script exists. Reuse unchanged raw bytes, receipts, hashes, typed claims, dependency/conflict propagation and offline replay patterns. Existing collect.py defaults (four workers and unbounded response reads) do not enforce the limits below; implement and test enforcement before any live run.

Separate build/offline testing from future live collection. Explicit human authorization of a specific live run and budget is required separately. Do not install dependencies, run live collection, or refresh frozen snapshots by implication of this prompt.

## Smallest useful contract

Add a fixed-BBL evidence module with inputs: parcel ID (validated borough/block/lot, preserving identity ambiguity), bounded question set, and explicit request/byte/time budget. Return versioned machine-readable claims and source locators, exact queries/record IDs/rows/fields/pages where available, raw-byte hashes and receipts, event dates, recording dates, retrieval timestamps, dataset vintage/update/coverage dates, typed parcel-document-party relationships and roles, dependencies, conflicts, explicit unknowns and source-level completeness. Keep facts, calculations, assumptions and judgments distinct. Missing or failed evidence is never zero, clearance or absence.

Use PLUTO for parcel context; ACRIS Legals for the BBL, then dynamically join discovered document IDs to Master and Parties and back to all Legals for every associated parcel. Bound and account for each expansion; preserve unmatched IDs, duplicate rows and truncated joins. Use DOF sales, and existing DOB/HPD sources only as questions require. Verify current source schemas, role definitions, coverage and pagination rather than trusting old endpoint assumptions. Do not turn an instrument amount into a per-lot price.

## Frozen evaluation and repair loop

Before hillclimbing, freeze questions, benchmark inputs, acceptance criteria, budget and scoring definitions in a versioned manifest. Include a separately withheld case with documented curator/model exposure; the known cases below are regressions, never blind evaluation. Verify fixture references independently before asserting expected answers. Preserve originals, hashes, failures and locator errata; never rewrite criteria or baselines to pass.

Iterate collect → independent challenge → minimal repair → offline replay using invariant criteria. Evaluate bounded question coverage, correctness, locator validity, source-level completeness, costs and reproducibility; source count is not a success metric. Report missing questions and joins, unsupported claims, stale/conflicting evidence and holdout limitations without inflated coverage claims. Freeze changes before evaluating the holdout; record exposure and do not relabel a tuned case as withheld.

Known leads to verify, not prevalidated expected answers:
- 49 W 33 St, BBL 1008350009: deed 2014010700298001, dated 2013-12-30, recorded 2014-01-09, $13.35m; distinguish 2025 financing from a new sale.
- 97 W 169 St: provisional BBLs 2025190027 and 2025190032; RFP block 2519 versus 2509 identity conflict. Preserve the conflict and both references; do not silently resolve it.
- 1240 Edward L Grant Highway, BBL 2028710002: current occupancy remains unknown.

These cases do not prove current title, beneficial ownership or land availability. Geometry is optional and separately reviewed. Never invent imagery data or infer measurements from illustrative images.

## Future live-run boundary

Proposed upper limits, requiring separate explicit authorization: 150 total HTTP requests including retries and join/pagination calls, 50 MiB total response bytes, 90 minutes collection, at most two concurrent requests, at most two transient retries per request respecting Retry-After. Enforce streaming byte limits and elapsed-time limits; stop with partial results and a ledger when exhausted. Record requests, bytes, retries, elapsed time, failures and skipped work. If document-image work exceeds the byte budget, report the estimate/blocker and leave it pending rather than expanding the budget. No paid services, account creation, credentials, bypasses, private-data uploads or publishing.

## Deliverable checklist

- [ ] Capability/gap report and minimal implementation with documented independently callable interface.
- [ ] Versioned input/output schemas, frozen benchmark/rubric, verified fixture references and separate holdout protocol.
- [ ] Offline tests for joins, budget stops, errors, conflicting/stale evidence and typed unknowns; synthetic cases explicitly labeled.
- [ ] Hash-preserved evidence bundle, source completeness ledger, failures and offline replay instructions/results.
- [ ] Results by question: correctness, coverage, valid locators, completeness, costs and limitations; distinguish verified facts from suggestions.
- [ ] Separate proposed live-run request with scope and budget; no live execution until explicitly authorized.
