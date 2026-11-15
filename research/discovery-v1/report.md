# Auto-lot discovery: two live Bronx case studies

## What we built and learned

Zero recorded homes is allowed and is the explicit setting in these probes.
Zero recorded residential FAR is also allowed: rezoning may introduce housing
where the recorded district currently provides none. Auto businesses and parking
uses remain candidates with current-use, lease and relocation questions.

The new `housing_discovery` module collects a bounded inventory, screens explicit
scenarios, applies a composable current-use focus, compares assumptions on the
same evidence, and hands selected lots to the existing parcel investigation
module. Each stage verifies independently. Failed context is unknown; it does not
become a reassuring zero. Every lot remains in the output with its reasons.

## Actual probe results

Sources were retrieved November 9, 2026. Geography uses PLUTO's recorded points
inside each bbox, not lot-polygon intersections, a walked catchment or all Bronx
lots. Jerome bbox: [-73.928, 40.834, -73.909, 40.848]. Hunts Point bbox:
[-73.895, 40.810, -73.879, 40.824]. These are analyst-selected test windows.

| Probe | Inventory | Broad private screen pool | Auto/parking screen pool |
| --- | ---: | ---: | ---: |
| Jerome, assumed FAR 6 | 1,921 | 88 | 40 |
| Hunts Point, assumed FAR 6 | 1,243 | 406 | 96 |

Both inventories passed primary and implemented context-coverage checks. The
collector retained 51 HTTP receipts for Jerome and 36 for Hunts Point. Coverage
means successful bounded collection under the stated queries, not complete
history or current occupancy. PLUTO rows report version 26v2.

Selection requires recorded lot area 2,500–60,000 sf, zero recorded homes and an
incremental zoning-area proxy of at least 5,000 sf. Active/on-hold linked ZAP
projects pause advancement. Public/institutional signals go to a separate mission.
The auto focus matches building-class prefix G **or** land-use code 10, while
retaining all original holds and every lot. These thresholds and the ten-row
shortlists are test choices, not endorsed policy.

The area proxy is lot area × max(0, assumed FAR − max(recorded residential FAR,
recorded affordable residential FAR)). It compares recorded residential zoning
capacity with a scenario. It does not estimate No-Action construction or net new
homes. Gross recorded building area is not substituted for zoning floor area.
The displayed home-equivalent conversion assumes gross/zoning ratio 1, residential
share 0.85, net efficiency 0.8 and average net home size 800 sf; it is conditional
arithmetic. An assumed FAR of 6 is not a proposed legally reconciled district.

## Real auto-related candidates

| Window / address | BBL | Class | Recorded zoning | Lot sf | Recorded homes | Recorded residential FAR | Area proxy at FAR 6, sf |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| Jerome / 1426 Cromwell Avenue | 2028570015 | G2 | C8-3 | 19,006 | 0 | 0 | 114,036 |
| Jerome / 1415 Cromwell Avenue | 2028720078 | G2 | C8-3 | 12,500 | 0 | 0 | 75,000 |
| Jerome / 1431 Cromwell Avenue | 2028720183 | G9 | C8-3 | 12,500 | 0 | 0 | 75,000 |
| Jerome / 1657 Jerome Avenue | 2028610001 | G5 | C8-3 | 10,000 | 0 | 0 | 60,000 |
| Hunts Point / Lafayette Avenue | 2027630335 | G7 | M1-2 | 55,000 | 0 | 0 | 330,000 |

Each row is traceable to retained PLUTO bytes using `pluto_reference` in its
screen IR. The top two Jerome rows and top Hunts Point row received deeper,
live evidence-only investigation. The handoff deliberately supplies no building
program: an exploratory discovery FAR does not establish physical fit.

- [1426 Cromwell](cases/jerome-deep/2028570015/packet.md): 8 legacy DOB rows;
  descriptions concern storage/warehouse and auto-repair use changes. Some are
  disapproved and some approved, so descriptions are historical signals rather
  than evidence of present lawful use. No DOB NOW or HPD violation rows returned.
- [1415 Cromwell](cases/jerome-deep/2028720078/packet.md): 8 legacy DOB rows,
  including a disapproved use-change application and signed-off maintenance work
  describing an existing storage garage. No DOB NOW or HPD violation rows returned.
- [Lafayette Avenue](cases/hunts-deep/2027630335/packet.md): 9 legacy DOB rows
  and 5 DOB NOW rows. Historical records include an auto-wrecking establishment
  and later plumbing/fence/curb-cut work. The ZAP join contains a withdrawn 1991
  disposition project. Neither those records nor their status resolve current
  operations, ownership intent or environmental requirements.

All four implemented parcel adapters returned successfully for each deeper run;
none reported row-cap truncation. Empty exact-BBL results do not establish no
housing, no activity or a complete history. The actual use, leases, title/control,
environment, applicable zoning, survey/envelope and financing remain unresolved.

## Mistakes the probes exposed

The initial private screen ranked a zero-apartment H4 hotel first at 1300
Sedgwick Avenue. That demonstrates why zero apartments alone cannot establish an
unoccupied site. Zero-unit hotel/housing-class records now pause for occupancy
review. This does not exclude auto businesses merely because they are operating.

The public review screen initially promoted park-zoned lots. Recorded PARK zoning
now pauses for a distinct parkland review. Infrastructure signals remain visible
under a separate public/institutional mission, with no inference of public title.

A later screen overcorrected by diverting every transportation/utility land-use
record to that mission. This incorrectly caught G-class auto properties such as
1426 Cromwell. The final method preserves those private auto candidates: a broad
transportation group alone does not establish infrastructure. The corrected auto
pools are **40 and 96**, replacing intermediate local results of 24 and 54.
Public-use records or other independent signals can still require separate review.

Collection also exposed a verification bug: serialized JSON reordered URL query
parameters. Equivalent URLs were rejected despite identical queries. Verification
now compares query semantics and still checks provider, predicates, selected
fields, pagination and coverage. Fully retained but unsealed collections can be
finalized without new HTTP calls; completed manifests cannot be rewritten.

The original screen source and selected results are retained in `iterations/`.
The current counterexample tests cover these failures, zero FAR and zero homes,
incomplete context, changed counts, ranks, comparisons and handoff boundaries.

## Sensitivity and the next investigation

Changing only the Jerome assumed FAR from 6 to 8 increases the broad private
screen pool from **88 to 193**. Two lots enter the ten-row shortlist: 2025300001
and 2025300025. The retained [comparison](cases/far-sensitivity.json) explains
changed values, ranks and reasons for every affected lot. Applying the auto focus
to the FAR-6 parent has its own [comparison](cases/auto-focus-comparison.json).
A separate public/institutional FAR-6 screen has 51 investigation candidates;
park-zoned lots remain held. None of these counts is a viable-site estimate.

The next useful work is to verify current auto/parking operations and ownership
intent for the few leads, reconcile zoning and special/environmental constraints,
and add surveyed parcel geometry, assemblage and pedestrian/transit access. Then
test explicit housing programs with complete development and operating budgets.
The [Stanyan benchmark](../stanyan-methodology/README.md) can guide the later
financial checklist; its San Francisco program cannot determine Bronx zoning or
site selection. Jeremy's review should test whether these leads match his search
intent and which practical constraints should change the screen.
