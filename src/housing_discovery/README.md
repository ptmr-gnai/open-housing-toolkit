# Housing discovery v1

Three independently callable stages: **collect a bounded lot inventory**, **screen
and compare explicit scenarios**, and **hand candidates to deeper parcel analysis**.
Use an editable checkout (`python -m pip install -e .`) with Python 3.11+.
Live collection uses public APIs; offline replay and screening use the standard
library. No LLM, API key, image provider or hosted proxy is needed.

## Run

```sh
python -m housing_discovery collect --input config/discovery/jerome-far6.json --out runs/jerome-inventory
python -m housing_discovery screen --inventory runs/jerome-inventory --input config/discovery/jerome-far6.json --out runs/jerome-far6
python -m housing_discovery screen --inventory runs/jerome-inventory --input config/discovery/jerome-far8.json --out runs/jerome-far8
python -m housing_discovery compare --left runs/jerome-far6 --right runs/jerome-far8 --out runs/jerome-sensitivity
python -m housing_discovery handoff --screen runs/jerome-far6 --top 3 --out runs/jerome-handoff
python -m housing_discovery deepen --handoff runs/jerome-handoff --out runs/jerome-deep
python -m housing_discovery verify --run runs/jerome-far6
```

Every destination must be new and under ignored runs/ or an explicit external local
folder. Completed sources and packets cannot be rebuilt in place. `deepen` makes
live calls through the existing Bronx parcel module and verifies each result. A
handoff alone makes no network requests. The supported deeper request is evidence
only: the assumed FAR is not silently converted to a building program.

The [request schema](request.schema.json) and executable input validator define
supported inputs. The checked-in settings are analyst probes, not default planning
policy. Alternate missions include public/institutional review and all lots with
flags. Thresholds, housing-unit caps and the treatment of active applications are
explicit user/analyst choices. Changing geography requires another collection.

## Sources and coverage

The [provider registry](providers.json) allowlists four public Socrata datasets:
PLUTO (`64uk-42ks`), ZAP lot links (`2iga-a6mk`), ZAP projects (`hgx4-8ukb`), and
City-owned/leased property uses (`fn4k-qyk2`). Raw responses, metadata, URLs,
retrieval times and failed attempts are retained. Metadata checks field presence
and join-key type. PLUTO is keyset-paged by numeric BBL, with counts and update
metadata before/after collection. This detects common truncation/drift, not all
possible concurrent changes; the API is not a transactional snapshot.

**Scope is all PLUTO records whose recorded points lie in the closed bbox.** This
is not a polygon-intersection inventory or a walked transit catchment. Unlocated
lots cannot be assigned to the bbox. The collector caps the primary inventory at
10,000 lots and the session at 100 HTTP attempts; incomplete primary collection
blocks ranked screening. Context is batch-queried for every collected BBL; failed,
missing or capped joins are unknown and hold advancement. Unknown application
statuses are not treated as inactive. Successful zero-row queries remain query
results, not proof that no historical or unlinked record exists.

If Python's trust store is incomplete, supply a valid trusted certificate bundle
with `collect --ca-file PATH` or `SSL_CERT_FILE` for live commands. TLS verification
is always enabled. Source terms remain the publishers':
https://opendata.cityofnewyork.us/overview/#termsofuse .

## The v1 numerical method

For each lot the baseline is the **larger recorded residential FAR or affordable
residential FAR**. This conservative recorded-field proxy avoids declaring extra
capacity by ignoring the affordable field, but does not establish either branch's
legal applicability. Missing fields remain unknown; a recorded FAR of zero is a
valid input, so industrial-use scenarios are not silently omitted.

```text
incremental zoning-area proxy = max(0, lotarea * (assumed FAR - baseline proxy))
home-equivalents = area proxy * gross/zoning conversion
                  * residential share * net efficiency / average net home size
```

All conversion/allocation/home-size values are explicit assumptions. Gross recorded
building area is not subtracted from zoning floor area. Rankings are by incremental
area proxy, BBL tie-break; they are not community-benefit or approval scores. The
method does not forecast No-Action development, model an applicable envelope,
calculate net new homes, resolve displacement, or establish funded feasibility.
The request's lot-size range and mission can substantially change results.

Public-property uses and institutional building/land-use classes are review
signals, not proof of public ownership or a service-replacement plan. COLP may
identify leased uses on privately owned property. Existing residential units remain
visible. Rent stabilization, housing subsidies, actual occupancy, title/control,
parcel assemblage, environmental satisfaction, pedestrian/job access and economics
are explicitly unresolved in v1. Flags for zoning, landmarks, floods or environmental
designations do not establish applicability, clearance or impossibility.

## Outputs and composition

Inventory: request.json, receipts.json, original sources/, inventory.json and
manifest. Screening: a copy of that inventory under evidence/, source-row pointers,
request/IR, packet.md, packet.html and **all-lots.csv**, including every held lot.
Every candidate has hold reasons, context references, assumptions and unresolved
fields. Comparison requires identical retained evidence and explains changed
values, rank, shortlist membership and reasons. Handoff retains the verified screen
and the exact supported deeper requests; deeper outputs retain both stages.

Verification checks source identities and queries, coverage, deterministic arithmetic,
all projections and implementation bindings. Rehashing an edited rank or packet
cannot pass recomputation. These checks do not prove source truth or professional
acceptance. The original research probes and their failures remain unchanged.

## Auto/parking focus

Zero recorded homes is allowed, including on lots with residential FAR zero.
For the auto/parking discovery question, use a verified screen as the parent:

```sh
python -m housing_discovery focus --screen runs/jerome-far6 --input config/discovery/focus/auto-parking.json --out runs/jerome-auto
python -m housing_discovery handoff --screen runs/jerome-auto --top 3 --out runs/jerome-auto-handoff
```

The user-requested use focus includes recorded building-class prefix G or land-use
code 10. It retains every lot and explains which fall outside the focus. The
parent's scenario and primary inventory stay unchanged. Existing auto businesses
remain investigation candidates; this is not a finding that they are empty or
can be relocated. A zero-apartment hotel/housing-class signal holds for occupancy
review under the zero-homes screen. Recorded PARK zoning is a separate review
hold; infrastructure uses enter the public/institutional review mission rather
than an ordinary private-redevelopment shortlist. Auto-class G lots in the broad
transportation land-use group remain private candidates unless another public-use
signal applies; the broad group alone does not make an auto business infrastructure.

`finalize --run PATH` can validate a fully captured but unsealed raw collection
after an interrupted finalization. It performs no new collection and refuses a
completed manifest. Never rewrite a completed inventory to refresh or repair it.
