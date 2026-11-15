# Find nonhousing land, then identify its housing path

## The correction

Jeremy's question is broader than auto lots: which nonhousing sites could support
housing, with what zoning path and practical constraints? Auto, parking, retail,
office, warehouse, vacant land and public/institutional uses all matter. A site
with substantial existing residential capacity remains relevant even if a FAR 6
scenario adds no capacity. The previous experiment's auto/extra-FAR selection was
not an answer to this broad question.

The separate housing_site_discovery module preserves the earlier code and cases.
It collects all recorded nonhousing in the bounded inventory, identifies general
use paths, keeps all other current-use dispositions visible, and supports explicit
follow-up. Modeling is optional and follows discovery. It admits no site based on
assumed extra FAR, lot-size thresholds, private-only mission or financing.

## Two real source windows

| Window | All recorded lots | Recorded nonhousing | General housing-use permission | General rezoning path | Special/unresolved |
| --- | ---: | ---: | ---: | ---: | ---: |
| Jerome | 1,921 | 457 | 221 | 22 | 214 |
| Hunts Point | 1,243 | 512 | 90 | 44 | 378 |

The two analyst-selected bboxes are [-73.928,40.834,-73.909,40.848] and
[-73.895,40.810,-73.879,40.824]. Scope is source points in those windows, not lot
polygon intersection, pedestrian catchments or all borough land. All source times
and exact queries are retained. Both PLUTO 26v2 inventories and their supplemental
records passed implemented collection checks.

General use permission means residential use is allowed in principle under the
implemented general district table. It establishes no apartment type, floor area,
envelope, construction program or actual entitlement. Special/split/paired and
exception records require separate review. The source-based rules reuse ZR 22-121,
32-121/122, 42-12/314 and 123-20; their dated bytes are retained. Parks, infrastructure
and public/institutional uses have separate review lanes and remain visible.

The method-correction comparisons retain both old dispositions and new paths.
There are 369 Jerome and 112 Hunts Point recorded-nonhousing lots previously held
by the earlier FAR 6 screen. These are new investigation entries, not extra homes
or an estimate of deliverable housing. Original and changed classifications can
be inspected in the retained comparison JSONs.

## Public context changes what is worth investigating

The added MTA station dataset contains 496 GTFS stop records. Some station IDs are
shared across platforms, so the collector preserves GTFS identities instead of
mistaking valid platform records for duplicate stations. The nearest source
station point is within 500 straight-line metres for 377 Jerome and 210 Hunts Point
recorded-nonhousing lots. These are descriptive point distances, not walking,
entrance, live-service, accessibility or job-access results.

DCP's hosted industrial-business-zone polygons contain the recorded points of
349 Hunts Point nonhousing lots and none in the Jerome window. NYCEDC describes
a City commitment not to support residential rezonings in IBZs; that policy signal
is distinct from a zoning prohibition. A point outside the polygons does not
resolve whole-parcel overlap or policy support.

DCP Fast Tracker returned context for 1,919/1,921 Jerome and 1,242/1,243 Hunts Point
BBLs. The missing condo/billing BBLs remain unknown. The 40 retained source-version
rows identify MapPLUTO 25v2.1 and varying older permit/natural/historic sources,
separate from the current PLUTO 26v2 inventory. Publisher flags cover emissions,
industrial uses, coastal risk, E-designations, highways/railways, wetlands,
historic/archaeological and shadow resources. No flags, missing rows or a successful
API request do not establish Green Fast Track eligibility or environmental clearance.
Project actions, unmapped sources, updated rules and field review still matter.

## Four selected parcel investigations

| Lot | Why it is informative | Deeper result |
| --- | --- | --- |
| 218 East 170 Street, 2028310056 | Retail class K2, 13,000 sf, R8, recorded residential FAR 6.02/affordable FAR7.2. The extra-FAR 6 screen held it, though housing is allowed in principle. Closest source B/D station point 131.5 m. | 23 legacy DOB and 6 NOW rows. NOW filing X01297915-I1 reports existing/proposed 5 dwellings despite PLUTO 0. Historical field signal requires reconciliation. |
| 925 Hunts Point Avenue, 2027350020 | Retail class K6, 20,101 sf, C4-5X, recorded FAR 5/6. Another existing-capacity site held by the prior increment gate. Closest source 6 station point 98.9 m. | 65 legacy DOB and 71 NOW rows. Multiple legacy filings report existing/proposed 2 dwellings, some signed off; another proposes 1. These are not verified present homes. |
| 1426 Cromwell Avenue, 2028570015 | G2 auto-repair class, C8-3, 19,006 sf, zero recorded residential FAR; general rezoning-path example. | 8 legacy DOB rows concerning storage/auto-repair changes; no positive numeric dwelling signal in this bounded deeper return. Current business/lease/use remains unresolved. |
| Lafayette Avenue, 2027630335 | G7 parking class, M1-2, 55,000 sf, Special Hunts Point, inside returned IBZ polygons. | 9 legacy and 5 NOW rows, including historical auto-wrecking and later site work. General district alone misses important special/policy questions. |

The four original source-bound parcel packets are retained under cases/parcels.
Their calls returned without adapter failures or row-cap truncation. No HPD
violation rows returned. Successful empty results do not establish no housing or
no activity. Evidence-only handoffs supplied no invented building program.

The two non-auto examples are consequential counterexamples: PLUTO use fields can
look like nonhousing while another official dataset reports dwelling-unit history.
The response is to preserve and investigate the signal, rather than silently
calling the site vacant or substituting historical filings for current occupancy.

## Broader dwelling-field challenge

The independent housing_site_review stage queries DOB BIS/NOW plus HPD registration and affordable-production sources for every
recorded-nonhousing BBL. It retains the complete discovery universe and adds exact
historical existing/proposed dwelling-field observations and per-source coverage.
Successful empty, returned rows, missing numeric fields, failures and caps remain
distinct. A literal no-positive-returned result is not housing-absence proof. HPD registration
uses exact numeric borough/block/lot keys; programme records use numeric BBL.

The first collection attempted all 969 lots and found 109 lots with positive returned
fields. Some 25-BBL BIS batches timed out; those affected lots remained unknown,
while DOB NOW completed across all 969. The failed requests and first capture are
preserved locally. The recovery probes tested single/five-lot predicates and ordering. Some unsorted
queries returned rapidly, while live BIS remained intermittent, so recovery used
bounded timeouts and preserved residual unknowns. HPD and cached NOW were
prioritized to prevent an unresponsive BIS source from consuming their budget.
Successful retained requests were replayed with original queries, dates and hashes;
all original failures remain in the imported history. A final offline replay adds
path-safety checks and preserves nested metadata vintages without new HTTP calls.

The final four-source review retains **117 positive-signal lots**, **506 literal
no-positive-return lots**, and **346 coverage-unknown lots** across the 969 recorded
nonhousing sites. Jerome counts are 68/204/185; Hunts Point 49/302/161. These are
returned-record review states, not counts of current homes or developable sites.
All 969 NOW, registration and affordable-production lookups completed; the
remaining coverage gaps are BIS. Raw source/status details are in the review cases.

The HPD joins returned six registration rows and four production rows across nine
unique lots. For 1322 Clay Avenue (2028870009), the first complete DOB-only queries
found no positive fields but HPD returned a registration that expired in 2015.
That is a dated reconciliation question, not proof of current housing. For 823 Faile
Street (2027620020), a registration runs through 2027 while current PLUTO classifies
the site as religious use with zero homes. These cases demonstrate why one field
or one source cannot settle the current-use question.

## What the prototype establishes

Broad discovery, official recorded-use rules, station/industrial/context lookups,
old/new method comparison and explicit deeper handoffs now run independently and
compose through verified packets. The original scenario screen remains a later,
optional experiment. The site universe stays visible through added reviews and
numerical goal seeking.

A current legal map/text reconciliation, actual occupancy and leases, title/control,
shared rights and assemblage, a surveyed physical envelope, environmental
satisfaction, project-specific economics and practitioner priorities remain open.
These are reviewable leads and exposed source conflicts, not site recommendations.
