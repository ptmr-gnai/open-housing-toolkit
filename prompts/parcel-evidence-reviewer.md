# Parcel evidence reviewer

This is a future work prompt, not authorization to execute it now. Independently challenge a bounded parcel-evidence tool and its outputs on behalf of a human. The product is composable, independently callable agent tools with machine-readable evidence contracts first; reports and image generation are downstream. No dashboard, 3D engine or Valdrada dependency.

## Establish scope

Read repository instructions, README.md, CONTRIBUTING.md, the builder interface, frozen question set, benchmark, rubric and run manifest. Report actual review capabilities, evidence access, tool limitations and prior exposure before coding or testing. Separate build/offline tests from future live collection; original-source network verification requires separate explicit live-run authorization. Do not install dependencies or refresh evidence implicitly. A hash or passing replay proves integrity only, not truth or completeness.

Freeze acceptance criteria before review. Do not modify them, erase failures, regenerate baselines or weaken assertions to pass. Preserve old artifacts and record locator corrections as explicit errata. Keep independently verified facts separate from suggestions and unverified fixture leads.

## Independent checks

Trace material claims to original agency records and retained raw bytes, independently of builder summaries. Verify exact queries, hashes, record IDs, field/page locators and interpretation. Recompute selected outputs independently; avoid calling the same implementation as the only oracle. Check machine-readable schema, types, dependencies, conflicts, unknowns, source-level completeness, and offline replay.

Audit PLUTO identity/vintage; ACRIS BBL Legals → discovered document IDs → Master/Parties → all Legals; and DOF sales plus DOB/HPD when required by the frozen questions. Look for pagination gaps, repeated pages, unstable ordering, count drift, duplicate records, missing joins, silently truncated document/parcel expansion and API errors disguised as success. Counts must have scope and retrieval dates; changed snapshots cannot silently be combined as one complete result.

Check deed versus mortgage, grantor/grantee versus borrower/lender and other instrument-specific party roles. Use event and recording chronology, never document-ID sort as chronology. Package amounts are not per-lot sale prices. Challenge false entity merges, address/BBL ambiguity, unsupported beneficial-ownership links, stale assertions and conflict propagation. Distinguish event, recording, retrieval and dataset dates and good-through coverage. Empty results do not establish absence, title, occupancy or availability.

Known leads, requiring independent fixture-reference verification before expected-answer assertions; none is blind evaluation:
- 49 W 33 St, BBL 1008350009: deed 2014010700298001, dated 2013-12-30, recorded 2014-01-09, $13.35m; 2025 financing must not become a new sale.
- 97 W 169 St: provisional BBLs 2025190027 / 2025190032; RFP block 2519 versus 2509 identity conflict must remain explicit, not silently resolved.
- 1240 Edward L Grant Highway, BBL 2028710002: current occupancy unknown.

These cases do not prove current title, beneficial ownership or land availability. Review any geometry separately; reject invented imagery data. Check independently pinned question inventory to detect omissions. Label synthetic tests clearly; regression and synthetic success cannot establish holdout accuracy or practitioner acceptance. Record holdout exposure and preserve held-out results, including failures.

## Collection and reporting boundary

If explicitly authorized separately, constrain live verification to the approved scope and proposed ceilings: 150 HTTP requests including retries, 50 MiB response bytes, 90 minutes collection, maximum two concurrent requests and two transient retries per request respecting Retry-After. Account for all pagination and dynamic joins. Stop and report partial coverage at a limit. Report document-image work that would exceed the byte budget; do not expand it implicitly. No paid services, account creation, credentials, bypasses, private-data uploads or publishing.

## Deliverable checklist

- [ ] Capability/exposure report; frozen rubric identity and review scope.
- [ ] Independent claim/locator audit with original-source evidence and verified facts separated from suggestions.
- [ ] Findings by severity with affected questions/claims, reproducible failure, minimal suggested repair and independent retest.
- [ ] Pagination/count/join/role/chronology/identity/date/staleness/conflict checks, including labeled synthetic negatives and preserved failures.
- [ ] Independent output checks and offline replay results, with actual tests run distinguished from proposed tests.
- [ ] Bounded question coverage, correctness, locator validity, source completeness and costs; source count is not a metric. Unverified or omitted work remains explicit.
- [ ] Concrete pass/fail/blocked conclusion against unchanged criteria and exact remaining blockers; separate live-run authorization request if needed.
