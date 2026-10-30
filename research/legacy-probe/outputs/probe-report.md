# Bronx Housing Opportunity Probe One

**Disposition: investigate current uses and leases before commissioning design.** The lead is 1240 EDWARD L GRANT HWY (BBL 2028710002). This is a conditional research concept, not an available or approved development site.

The first probe demonstrates a reproducible screening and challenge process. Expert usefulness remains untested until the two advisors review it.

## What the screen found

The cached PLUTO window contains 2,323 lots; 881 have point coordinates within the assumed 650 metre straight line radius. 486 pass the numeric screen. 10 were shortlisted and 3 investigated. Counts: `screen.bounding_window_count`, `screen.within_radius_count`, `screen.eligible_count`.

Screen settings: lot area 2,500 to 60,000 square feet, positive recorded residential FAR, and at least 5,000 square feet of the proxy lotarea × residfar − bldgarea. Prioritize no recorded residential units, then descending proxy. These are research choices. The proxy is not legal buildable area and the radius is not walking or job access.

| Rank | Recorded address | BBL | Zoning | Lot area sf | Recorded homes | Distance m | Area gap proxy sf |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1240 EDWARD L GRANT HWY | 2028710002 | R9A | 59,050 | 0 | 434 | 418,056 |
| 2 | 1426 TOWNSEND AVENUE | 2028430040 | R8 | 55,000 | 0 | 165 | 237,895 |
| 3 | 1264 RIVER AVENUE | 2024890077 | R8A | 45,000 | 0 | 348 | 224,761 |
| 4 | 1211 GRANDVIEW PLACE | 2024650050 | R8 | 33,747 | 0 | 534 | 203,157 |
| 5 | RIVER AVENUE | 2024960064 | R9A | 27,000 | 0 | 642 | 203,040 |
| 6 | 1220 GERARD AVENUE | 2024800008 | R8 | 55,027 | 0 | 512 | 201,263 |
| 7 | 1355 CROMWELL AVENUE | 2028710085 | R9A | 25,654 | 0 | 240 | 187,918 |
| 8 | 1600 MACOMBS ROAD | 2028650134 | R8A | 30,879 | 0 | 647 | 185,892 |
| 9 | 1376 CROMWELL AVENUE | 2028640035 | R8A | 51,410 | 0 | 156 | 181,628 |
| 10 | 1203 JEROME AVENUE | 2025060062 | R9A | 25,375 | 0 | 581 | 158,251 |

Each row maps to `lot.<BBL>.<field>` in ir.json. The complete cached universe and exclusions are retained. No lot is inferred to be empty from its residential unit count.

## Three candidate challenges

### 1240 EDWARD L GRANT HWY

Recorded owner: 1240 EDWARD GRANT LLC (`lot.2028710002.ownername`); building class K1 (`lot.2028710002.bldgclass`).

**Research disposition:** Investigate current uses and leases before design.

Private ownership label and large area proxy justify a lead, but historical DOB filings describe a laundromat, medical signs and church/school/hall activity. PLUTO records retail use and E-442. Zero recorded homes does not imply an empty site. No new building rows observed in the exact-BBL queries; broader pipeline check remains unresolved. The E-designation source records hazardous-materials, air and noise requirements, including Phase I/II testing, HVAC fuel/stack limits and window attenuation or alternate ventilation; satisfaction status is not established.

Evidence: `lot.2028710002.ownername`, `lot.2028710002.bldgclass`, `lot.2028710002.retailarea`, `lot.2028710002.edesignum`, `check.2028710002.dob_bis.row.3.job_description`, `check.2028710002.dob_bis.row.1.job_description`, `check.2028710002.dob_bis.row.11.job_description`, `check.2028710002.dob_now.records`, `check.2028710002.e_designation.row.0.hazmat_code`, `check.2028710002.e_designation.row.0.air_code`, `check.2028710002.e_designation.row.0.noise_code`, `check.2028710002.e_designation.row.0.description`.

| Check | Returned rows | Meaning |
| --- | --- | --- |
| dob_bis | 21 | Exact BBL query only; not a clearance or complete project count |
| dob_now | 0 | Exact BBL query only; not a clearance or complete project count |
| hpd_violations | 0 | Exact BBL query only; not a clearance or complete project count |
| e_designation | 1 | Exact BBL query only; not a clearance or complete project count |

Filings may have multiple documents or subsequent submissions. Row counts are not unique projects. A zero-row query is an observed query result, not evidence that there is no activity, no violation, or no occupant.

### 1426 TOWNSEND AVENUE

Recorded owner: NYC DEPARTMENT OF EDUCATION (`lot.2028430040.ownername`); building class W1 (`lot.2028430040.bldgclass`).

**Research disposition:** Exclude from ordinary private redevelopment shortlist.

PLUTO records Education Department ownership and a school building class. DOB filings describe PS64 school improvements, including filings in 2026. A public-facility co-location proposal would be a different mission and would require an agency-led service plan; unused FAR alone does not justify housing redevelopment.

Evidence: `lot.2028430040.ownername`, `lot.2028430040.bldgclass`, `check.2028430040.dob_now.row.1.job_description`, `check.2028430040.dob_now.row.1.filing_date`, `check.2028430040.dob_bis.row.0.job_description`.

| Check | Returned rows | Meaning |
| --- | --- | --- |
| dob_bis | 26 | Exact BBL query only; not a clearance or complete project count |
| dob_now | 24 | Exact BBL query only; not a clearance or complete project count |
| hpd_violations | 0 | Exact BBL query only; not a clearance or complete project count |
| e_designation | unknown | Exact BBL query only; not a clearance or complete project count |

Filings may have multiple documents or subsequent submissions. Row counts are not unique projects. A zero-row query is an observed query result, not evidence that there is no activity, no violation, or no occupant.

### 1264 RIVER AVENUE

Recorded owner: NYC POLICE DEPARTMENT (`lot.2024890077.ownername`); building class Y2 (`lot.2024890077.bldgclass`).

**Research disposition:** Exclude from ordinary private redevelopment shortlist.

PLUTO records Police Department ownership; DOB NOW filings describe underground gasoline storage tank replacement and associated excavation work. Housing use requires a public-service replacement or co-location decision and environmental diligence. PLUTO and DOB use different street addresses on the same BBL; preserve the alias rather than treating it as another lot.

Evidence: `lot.2024890077.ownername`, `lot.2024890077.address`, `check.2024890077.dob_now.row.1.job_description`, `check.2024890077.dob_now.row.0.job_description`, `check.2024890077.dob_now.row.1.house_no`, `check.2024890077.dob_now.row.1.street_name`.

| Check | Returned rows | Meaning |
| --- | --- | --- |
| dob_bis | 1 | Exact BBL query only; not a clearance or complete project count |
| dob_now | 3 | Exact BBL query only; not a clearance or complete project count |
| hpd_violations | 0 | Exact BBL query only; not a clearance or complete project count |
| e_designation | unknown | Exact BBL query only; not a clearance or complete project count |

Filings may have multiple documents or subsequent submissions. Row counts are not unique projects. A zero-row query is an observed query result, not evidence that there is no activity, no violation, or no occupant.

## Lead site and first decision

The lead has recorded lot area 59,050 sf, building area 26,000 sf, residential FAR 7.52, and affordable residential FAR 9.02. Recorded zoning is R9A, overlay C2-4, special district code J, and environmental designation E-442. These fields are indicators for diligence, not a complete zoning or environmental opinion.

The scenario uses the recorded ordinary residential FAR as a transparent reference. It does not apply the affordable FAR, MIH requirements, special district modifications, lot geometry constraints, or verified floor area exemptions. Recorded building area and zoning floor area are different measures.

**First action:** establish what occupies the site today, which leases or community uses exist, and whether preservation, co-location, or redevelopment is even a relevant question. Historical owner names in filings differ from the current PLUTO label. This is time-varying evidence, not proof that a current owner or tenant has been identified.

## Two conditional housing scenarios

These model complete replacement housing concepts, not incremental additions to the existing building. Existing nonresidential services are not automatically preserved in the calculation. Neither scenario is a legal or architectural design.

| Scenario | Gross sf | Illustrative homes | Concept floors | Modeled cost excluding land | Monthly rent for debt coverage |
| --- | --- | --- | --- | --- | --- |
| A | 288,636 | 271 | 9 | $131,329,562 | $3,869 |
| B | 399,650 | 376 | 13 | $181,840,932 | $3,861 |

Scenario A uses 65 percent and B 90 percent of recorded FAR; assumed lot coverage is 55 percent for A and 55 percent for B. Net efficiency is 80 percent and average home size 850 net sf. The assumed gross to zoning area conversion is 1.00. Concept floors are area divided by an assumed footprint, rounded up; the last floor may be partial. Shape, setbacks, daylight, elevators, egress and height limits are unresolved.

Cost baseline: $350 per gross sf hard cost plus a 30 percent soft cost and contingency allowance. Debt baseline: 65 percent of modeled cost, 6.50 percent interest, 30 year amortization and 1.20 debt service coverage. Operations assume 5 percent vacancy and 35 percent operating expense share. All are editable hypothetical inputs, not sourced Bronx underwriting terms.

The rent figure covers the modeled debt at the assumed coverage ratio. It is not a market rent, AMI rent, full project break even rent, or equity return. Cost excludes site acquisition, demolition, remediation, relocation, construction financing carry, verified fees and reserves. No subsidy amount or financing commitment is inferred.

At the hypothetical $1,800 monthly all-unit rent test:

- Scenario A: baseline non-debt capital $45,965,347; additional non-debt capital needed to reduce modeled debt $45,651,124. Additional capital is not synonymous with public subsidy. Inputs and formula: `scenario.2028710002.A.additional_non_debt_capital`.

- Scenario B: baseline non-debt capital $63,644,326; additional non-debt capital needed to reduce modeled debt $63,096,524. Additional capital is not synonymous with public subsidy. Inputs and formula: `scenario.2028710002.B.additional_non_debt_capital`.

The 60 percent AMI objective remains a policy lens. No official rent schedule or utility allowance was verified, so the model does not call the hypothetical rent affordable at that income level.

## Unresolved gates and next actions

| Gate | Status | Next action |
| --- | --- | --- |
| legal entitlement | Unknown | Verify parcel geometry, zoning map, special Jerome rules, MIH applicability, permitted uses, bulk and affordability obligations. |
| current occupancy and leases | Unknown | Perform a site visit and establish current tenants, uses, leases and preservation needs. |
| owner willingness and title | Unknown | Check deed and mortgage history, parcel changes, title and willingness; no owner contact undertaken. |
| environment and geotechnical | Unknown | Resolve the E designation and obtain professional environmental and site diligence. |
| current development pipeline | Unknown | Cross-check block/lot, BIN and address aliases, permits and certificates; exact BBL filings alone are insufficient. |
| full cost and financing | Unknown | Obtain a quantity estimate, land and relocation assumptions, tax treatment, financing carry, reserves and actual program terms. |
| official affordability schedule | Unknown | Specify household sizes, unit mix, official income and rent limits, utility allowance and duration. |
| pedestrian and job access | Unknown | Route from entrances to relevant jobs and services; assess travel schedules, reliability, fares and accessibility. |

## What changed in the playbook

The naive numeric rank elevated a school and a police facility. The challenge stage corrected the decision without rewriting the original screen. Future missions should explicitly distinguish private redevelopment, public-service co-location, preservation and vacant-land development. A civic-use lens belongs before treating ranked capacity as an opportunity.

The private lead illustrates a second rule: absence of recorded homes does not eliminate displacement or service-loss questions. Current uses and leases should precede expensive design or promotional imagery.

## Advisor review

Both reviews are outstanding. Ask each advisor to choose reject, investigate or advance; identify material errors and missing constraints; estimate work saved; trace three claims; and change one assumption. Use docs/advisor-review.md and keep their judgments separate.

## Provenance and reproduction

Data snapshot: PLUTO version 26v2. Dataset metadata reports an August 24, 2026 update; source snapshots were retrieved during this probe. Field-level effective dates remain incomplete. The generic downloaded PLUTO dictionary is from 2022 and is not accepted as current 26v2 entitlement guidance.

Run `python pipeline.py` offline from the package. The resulting ir.json contains observed, derived, assumption, judgment and unknown claims; exact source queries and snapshot hashes; dependencies; and unresolved gates. The manifest hashes code, configuration, sources and outputs. See README.md for live collection, replay and validation.

No adviser has endorsed this output. No proposal, media post, owner contact or image has been published or sent.
