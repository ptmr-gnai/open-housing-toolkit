# Parcel investigation 2028530012

Investigate 1940 Jerome Avenue using current public data; preserve unknown occupancy, availability and legal developability. Support independent illustrative program comparison and practitioner review.

**Partial playbook under development.** This packet preserves evidence and conditional arithmetic; it does not establish site availability, a lawful use, legal capacity, building fit or funded feasibility.

## Read this first

**Evidence origin:** Analysis of retained source snapshots. This modeling step did not query the APIs.

Execution metadata: [execution.json](execution.json). Raw-source retrieval dates: [receipts.json](receipts.json). Retrieval is not a field-observation date or a guarantee of current conditions.

**Source retrieval range (UTC):** 2026-10-30T02:23:05.529664+00:00 through 2026-10-30T02:23:05.532401+00:00.

**PLUTO row vintage:** 26v2 — [pluto row 0 version](#pluto-0-version).

**Coverage flags:** no adapter failures recorded; no row-cap truncation recorded. Successful bounded queries are not proof of complete history.

### What these records support

- Recorded address: 1940 JEROME AVENUE — [pluto row 0 address](#pluto-0-address).
- Recorded lot area: 10852 — [pluto row 0 lotarea](#pluto-0-lotarea).
- Recorded residential units: 115 — [pluto row 0 unitsres](#pluto-0-unitsres).
- Recorded primary zoning: C4-4D — [pluto row 0 zonedist1](#pluto-0-zonedist1).
- Historical positive dwelling-unit signals need reconciliation: [115 units as recorded](#dob_now-0-proposed_dwelling_units), [115 units as recorded](#dob_now-1-proposed_dwelling_units), [115 units as recorded](#dob_now-2-proposed_dwelling_units). This is not a present occupancy count; see the full signal section.

### Supplied assumptions and conditional result

- 15000 gross sf — [gross_area_sf](#scenario-gross_area_sf).
- 1500 gross sf — [nonresidential_gross_sf](#scenario-nonresidential_gross_sf).
- 0.8 share — [residential_net_efficiency](#scenario-residential_net_efficiency).
- 800 net sf per home-equivalent — [average_net_home_sf](#scenario-average_net_home_sf).
- Conditional area-budget result: 13.5 home-equivalents — [Area-budget home-equivalents](#scenario-home_equivalents). This does not establish feasible homes, zoning capacity or an affordable program.

### What remains unresolved / inputs to continue

- Current-use, lease and lawful-occupancy evidence — [current_use](#unknown-current_use).
- Title, site control and owner intent — [title](#unknown-title).
- Applicable zoning and approvals — [entitlement](#unknown-entitlement).
- Survey, envelope and layout evidence — [physical_fit](#unknown-physical_fit).
- Environmental requirements and studies — [environment](#unknown-environment).
- Program rules, costs and financing — [finance](#unknown-finance).
- Walked access, service and job-access evidence — [transit](#unknown-transit).

These are unresolved input categories, not a ranked action plan. [The discussion checklist](#review-next_diligence) is an unreviewed author judgment.

Detailed source coverage, calculations and the complete claim register follow. This summary is an extract of the same claims; it adds no professional clearance.

## Source coverage

| Source | Status | Returned rows | Truncated | Retrieved UTC |
| --- | --- | --- | --- | --- |
| pluto | ok | 1 | False | 2026-10-30T02:23:05.529664+00:00 |
| dob_bis | ok | 2 | False | 2026-10-30T02:23:05.530823+00:00 |
| dob_now | ok | 38 | False | 2026-10-30T02:23:05.531403+00:00 |
| hpd_violations | ok | 0 | False | 2026-10-30T02:23:05.532401+00:00 |

A failed request is missing evidence, not zero records. Counts describe returned rows, not unique projects. Empty exact-BBL results do not establish no housing, no violations or no activity.

## Recorded parcel facts

- Recorded address: 1940 JEROME AVENUE — [source](#pluto-0-address)
- Tax-lot BBL: 2028530012.00000000 — [source](#pluto-0-bbl)
- Recorded building area (sf): 97704 — [source](#pluto-0-bldgarea)
- Recorded building class: D7 — [source](#pluto-0-bldgclass)
- block: 2853 — [source](#pluto-0-block)
- borough: BX — [source](#pluto-0-borough)
- Recorded built FAR: 9.00000000000 — [source](#pluto-0-builtfar)
- Recorded environmental designation: E-442 — [source](#pluto-0-edesignum)
- Recorded irregular-lot flag: True — [source](#pluto-0-irrlotcode)
- landuse: 4 — [source](#pluto-0-landuse)
- latitude: 40.8509022 — [source](#pluto-0-latitude)
- longitude: -73.9095908 — [source](#pluto-0-longitude)
- lot: 12 — [source](#pluto-0-lot)
- Recorded lot area (sf): 10852 — [source](#pluto-0-lotarea)
- Recorded floor count: 13.0000000 — [source](#pluto-0-numfloors)
- Recorded residential FAR (legal applicability unreviewed): 6.02000000000 — [source](#pluto-0-residfar)
- Recorded special district: J — [source](#pluto-0-spdist1)
- Recorded residential units: 115 — [source](#pluto-0-unitsres)
- Recorded total units: 117 — [source](#pluto-0-unitstotal)
- Dataset row version: 26v2 — [source](#pluto-0-version)
- Recorded primary zoning district: C4-4D — [source](#pluto-0-zonedist1)

## Historical housing signals requiring reconciliation

- Historical proposed dwelling units: 115; filing date 2026-06-03T00:00:00.000; HUB CONSULTATION MEETING HELD AND ACCEPTED ON 8/8/2022. PROPOSE NEW 13-STORY PLUS CELLAR MIXED-USE BUILDING. OBTAIN NEW C OF O. THIS PROJECT IS MANDATORY INCLUSIONARY, 100% LOW INCOME HOUSING, AND QUALITY HOUSING. — [source](#dob_now-0-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2022-08-22T00:00:00.000; HUB CONSULTATION MEETING HELD AND ACCEPTED ON 8/8/2022. PROPOSE NEW 13-STORY PLUS CELLAR MIXED-USE BUILDING. OBTAIN NEW C OF O. THIS PROJECT IS MANDATORY INCLUSIONARY, 100% LOW INCOME HOUSING, AND QUALITY HOUSING. — [source](#dob_now-1-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2024-02-29T00:00:00.000; Subsequent application for proposed SOE Work filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-2-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2024-04-25T00:00:00.000; Propose Underpinning the adjacent buildings, 1934 and 1946 Jerome Avenue filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-3-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2024-09-03T00:00:00.000; Subsequent application for proposed SOE Work filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-4-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2024-09-03T00:00:00.000; Propose Underpinning the adjacent buildings, 1934 and 1946 Jerome Avenue filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-5-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2026-03-03T00:00:00.000; PROPOSE STRUCTURAL SCOPE OF WORKS IN CONJUNCTION WITH NB # X00787559-I1. — [source](#dob_now-6-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2026-04-10T00:00:00.000; Subsequent application for proposed Mechanical Scope of Work filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-7-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2022-11-01T00:00:00.000; Subsequent application for proposed Mechanical Scope of Work filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-8-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2022-11-02T00:00:00.000; Subsequent application for Plumbing Scope of Work filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-9-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2022-11-01T00:00:00.000; Subsequent application for Sprinkler and Standpipe System filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-10-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2022-11-03T00:00:00.000; PROPOSED FOUNDATAION SCOPE OF WORKS IN CONJUNCTION WITH NB # X00787559-I1. — [source](#dob_now-11-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2022-10-24T00:00:00.000; PROPOSE STRUCTURAL SCOPE OF WORKS IN CONJUNCTION WITH NB # X00787559-I1. — [source](#dob_now-12-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2023-01-24T00:00:00.000; Subsequent application for proposed SOE Work filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-13-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2023-01-24T00:00:00.000; Propose Underpinning the adjacent buildings, 1934 and 1946 Jerome Avenue filed in conjunction with NB-GC # X00787559-I1. — [source](#dob_now-14-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2023-04-21T00:00:00.000; Propose Partial Foundation Work for a new 13-story residential building filed in conjunction with NB # X00787559-I1. — [source](#dob_now-15-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2023-12-19T00:00:00.000; Proposed installation of a temporary combined class I fire standpipe system in conjunction with NB # X00787559-I1. — [source](#dob_now-16-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2024-04-19T00:00:00.000; HEAVY DUTY SIDEWALK SHED DURING NB CONST, FILED SEP. SIDEWALK SHED SHALL COMPLY WITH CH #33 OF THE NYC BC. NO CHANGE IN USE, OCCUPANCY OR EGRESS UNDER THIS APPLICATION. DOT PERMITS BY OTHERS FOR SHED INSTALLED ON SIDEWALK/ROADWAY — [source](#dob_now-21-proposed_dwelling_units)
- Historical existing dwelling units: 1; filing date 2024-08-12T00:00:00.000; Installation of a temporary roof protection per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application — [source](#dob_now-22-existing_dwelling_units)
- Historical proposed dwelling units: 1; filing date 2024-08-12T00:00:00.000; Installation of a temporary roof protection per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application — [source](#dob_now-22-proposed_dwelling_units)
- Historical existing dwelling units: 1; filing date 2025-02-13T00:00:00.000; Installation of a temporary roof protection per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application — [source](#dob_now-23-existing_dwelling_units)
- Historical proposed dwelling units: 1; filing date 2025-02-13T00:00:00.000; Installation of a temporary roof protection per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application — [source](#dob_now-23-proposed_dwelling_units)
- Historical existing dwelling units: 1; filing date 2024-08-08T00:00:00.000; Installation of a temporarily heavy-duty sidewalk shed per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. — [source](#dob_now-24-existing_dwelling_units)
- Historical proposed dwelling units: 1; filing date 2024-08-08T00:00:00.000; Installation of a temporarily heavy-duty sidewalk shed per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. — [source](#dob_now-24-proposed_dwelling_units)
- Historical existing dwelling units: 1; filing date 2025-02-21T00:00:00.000; Installation of a temporarily heavy-duty sidewalk shed per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. — [source](#dob_now-25-existing_dwelling_units)
- Historical proposed dwelling units: 1; filing date 2025-02-21T00:00:00.000; Installation of a temporarily heavy-duty sidewalk shed per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. — [source](#dob_now-25-proposed_dwelling_units)
- Historical existing dwelling units: 1; filing date 2025-08-13T00:00:00.000; Installation of a temporarily heavy-duty sidewalk shed per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. — [source](#dob_now-26-existing_dwelling_units)
- Historical proposed dwelling units: 1; filing date 2025-08-13T00:00:00.000; Installation of a temporarily heavy-duty sidewalk shed per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. — [source](#dob_now-26-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2024-07-25T00:00:00.000; Installation of a temporary construction fence per plan submitted.  Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. — [source](#dob_now-27-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2025-09-05T00:00:00.000; Installation of a temporary construction fence per plan submitted.  Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. — [source](#dob_now-28-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2024-09-23T00:00:00.000; EQUIPMENT USE: DUAL 7000# CAPACITY PERSONNEL/MATERIAL HOISTS DURING NB CONST, FILED SEP. HOISTS SHALL COMPLY WITH CH #33 OF THE NYC BC. NO CHANGE IN USE, OCCUPANCY OR EGRESS UNDER THIS APPLICATION. ELEVATOR APPLICATION SUBMITTED SEPARATELY — [source](#dob_now-29-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2024-12-02T00:00:00.000; EQUIPMENT USE: DUAL 7000# CAPACITY PERSONNEL/MATERIAL HOISTS DURING NB CONST, FILED SEP. HOISTS SHALL COMPLY WITH CH #33 OF THE NYC BC. NO CHANGE IN USE, OCCUPANCY OR EGRESS UNDER THIS APPLICATION. ELEVATOR APPLICATION SUBMITTED SEPARATELY — [source](#dob_now-30-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2025-02-21T00:00:00.000; EQUIPMENT USE: DUAL 7000# CAPACITY PERSONNEL/MATERIAL HOISTS DURING NB CONST, FILED SEP. HOISTS SHALL COMPLY WITH CH #33 OF THE NYC BC. NO CHANGE IN USE, OCCUPANCY OR EGRESS UNDER THIS APPLICATION. ELEVATOR APPLICATION SUBMITTED SEPARATELY — [source](#dob_now-31-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2024-12-05T00:00:00.000; INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. — [source](#dob_now-32-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2025-03-25T00:00:00.000; INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. — [source](#dob_now-33-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2025-03-31T00:00:00.000; INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. — [source](#dob_now-34-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2025-05-13T00:00:00.000; INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. — [source](#dob_now-35-proposed_dwelling_units)
- Historical proposed dwelling units: 115; filing date 2025-12-08T00:00:00.000; INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. — [source](#dob_now-36-proposed_dwelling_units)

These fields describe historical existing/proposed units. They are not a current occupancy count and are not summed across documents or jobs. Their relationship to PLUTO and lawful/current use needs review.

## Scenario and calculation steps

Illustrative area budget, not a proposed or approved building

| Claim | Value | Unit | Basis |
| --- | --- | --- | --- |
| [gross_area_sf](#scenario-gross_area_sf) | 15000 | gross sf | Practitioner brief test assumption; not measured capacity or surveyed design. |
| [nonresidential_gross_sf](#scenario-nonresidential_gross_sf) | 1500 | gross sf | Practitioner brief test assumption; not measured capacity or surveyed design. |
| [residential_net_efficiency](#scenario-residential_net_efficiency) | 0.8 | share | Practitioner brief test assumption; not measured capacity or surveyed design. |
| [average_net_home_sf](#scenario-average_net_home_sf) | 800 | net sf per home-equivalent | Practitioner brief test assumption; not measured capacity or surveyed design. |
| [Residential gross area allocation](#scenario-residential_gross_sf) | 13500.0 | gross sf | 15000 − 1500 |
| [Residential net area allowance](#scenario-residential_net_sf) | 10800.0 | net sf | 13500.0 × 0.8 |
| [Area-budget home-equivalents](#scenario-home_equivalents) | 13.5 | home-equivalents; not a feasible unit count | 10800.0 ÷ 800 |
| [Proposed gross area / recorded lot area](#scenario-gross_to_recorded_lot_ratio) | 1.3822336896424623 | gross-to-lot ratio; NOT zoning FAR | 15000 ÷ 10852 |

Home-equivalents are an area quotient, not a verified count of homes. The gross-to-lot ratio is not zoning FAR. No rents, affordability eligibility, costs or financing commitments are inferred.

## Unknowns and next questions

- **current_use**: Current occupancy, leases, lawful use and displacement implications are not established by these records.
- **title**: Title, site control and owner willingness have not been investigated.
- **entitlement**: Applicable zoning text, special districts, amendments, approvals and legal capacity are not determined.
- **physical_fit**: Survey, envelope, access, egress, layouts and geotechnical fit are not validated.
- **environment**: Environmental requirements, studies and satisfaction status have not been reconciled.
- **finance**: Complete development cost, affordability program, capital sources and commitments are not modeled.
- **transit**: Walked access, service reliability, accessibility and job access are not modeled.
- **process_coverage**: This is a partial playbook. The complete practitioner process and all material requirements are not known.
- **Reconcile heterogeneous housing evidence — unreviewed judgment**: DOB historical existing/proposed units and PLUTO recorded units are different observations. Preserve all positive signals; obtain approved plans, certificates and current-use evidence before concluding occupancy or displacement. No units are summed across filings.
- **Questions for practitioner review — unreviewed judgment**: A checklist for discussion. Task cost, timing, actor resources and best ordering are not evaluated.

## Provenance register

Raw responses, retrieval receipts, request inputs, calculation steps and machine-readable claims are included alongside this packet. Retrieval dates are not field observation dates. Citations establish the selected value, not interpretation or complete coverage.

<a id="pluto-returned_rows"></a>

**pluto.returned_rows** [calculation] pluto returned rows in this exact-BBL query: 1 (returned rows; not projects or total population)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

Bounded query; see truncation and source limits.

<a id="pluto-0-address"></a>

**pluto.0.address** [fact] pluto row 0 address: 1940 JEROME AVENUE (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/address`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bbl"></a>

**pluto.0.bbl** [fact] pluto row 0 bbl: 2028530012.00000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bbl`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgarea"></a>

**pluto.0.bldgarea** [fact] pluto row 0 bldgarea: 97704 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgarea`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgclass"></a>

**pluto.0.bldgclass** [fact] pluto row 0 bldgclass: D7 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgclass`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-block"></a>

**pluto.0.block** [fact] pluto row 0 block: 2853 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/block`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-borough"></a>

**pluto.0.borough** [fact] pluto row 0 borough: BX (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/borough`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-builtfar"></a>

**pluto.0.builtfar** [fact] pluto row 0 builtfar: 9.00000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/builtfar`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-edesignum"></a>

**pluto.0.edesignum** [fact] pluto row 0 edesignum: E-442 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/edesignum`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-irrlotcode"></a>

**pluto.0.irrlotcode** [fact] pluto row 0 irrlotcode: True (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/irrlotcode`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-landuse"></a>

**pluto.0.landuse** [fact] pluto row 0 landuse: 4 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/landuse`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-latitude"></a>

**pluto.0.latitude** [fact] pluto row 0 latitude: 40.8509022 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/latitude`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-longitude"></a>

**pluto.0.longitude** [fact] pluto row 0 longitude: -73.9095908 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/longitude`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lot"></a>

**pluto.0.lot** [fact] pluto row 0 lot: 12 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lot`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lotarea"></a>

**pluto.0.lotarea** [fact] pluto row 0 lotarea: 10852 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lotarea`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-numfloors"></a>

**pluto.0.numfloors** [fact] pluto row 0 numfloors: 13.0000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/numfloors`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-residfar"></a>

**pluto.0.residfar** [fact] pluto row 0 residfar: 6.02000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/residfar`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-spdist1"></a>

**pluto.0.spdist1** [fact] pluto row 0 spdist1: J (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/spdist1`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitsres"></a>

**pluto.0.unitsres** [fact] pluto row 0 unitsres: 115 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitsres`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitstotal"></a>

**pluto.0.unitstotal** [fact] pluto row 0 unitstotal: 117 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitstotal`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-version"></a>

**pluto.0.version** [fact] pluto row 0 version: 26v2 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/version`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-zonedist1"></a>

**pluto.0.zonedist1** [fact] pluto row 0 zonedist1: C4-4D (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/zonedist1`; SHA256 `3f796e67c20dc5588b48f6e61dddf4ac9baed9162380f1c8dc3cd7dda6a589a9`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028530012&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="dob_bis-returned_rows"></a>

**dob_bis.returned_rows** [calculation] dob_bis returned rows in this exact-BBL query: 2 (returned rows; not projects or total population)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

Bounded query; see truncation and source limits.

<a id="dob_bis-0-bbl"></a>

**dob_bis.0.bbl** [fact] dob_bis row 0 bbl: 2028530012 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bbl`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-bin__"></a>

**dob_bis.0.bin__** [fact] dob_bis row 0 bin__: 2129813 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bin__`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-doc__"></a>

**dob_bis.0.doc__** [fact] dob_bis row 0 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/doc__`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-house__"></a>

**dob_bis.0.house__** [fact] dob_bis row 0 house__: 1940 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/house__`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job__"></a>

**dob_bis.0.job__** [fact] dob_bis row 0 job__: 220755485 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job__`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_description"></a>

**dob_bis.0.job_description** [fact] dob_bis row 0 job_description: CONDO SUBDIVISION FOR LOT#12. THERE WILL BE A TOTAL OF TWO (2) CONDO TAX LOTS. RELATED APPLICATION #X00787559-I1. TAX LOT 1101 FOR RESIDENTIAL USE ON CEL, ROF, AND 001-013 FLOORS. TAX LOT 1102 FOR COMMERCIAL USE ON CEL AND 001 FLOOR. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_description`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_status_descrp"></a>

**dob_bis.0.job_status_descrp** [fact] dob_bis row 0 job_status_descrp: COMPLETED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_status_descrp`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_type"></a>

**dob_bis.0.job_type** [fact] dob_bis row 0 job_type: SC (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_type`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-latest_action_date"></a>

**dob_bis.0.latest_action_date** [fact] dob_bis row 0 latest_action_date: 11/12/2025 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/latest_action_date`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-pre__filing_date"></a>

**dob_bis.0.pre__filing_date** [fact] dob_bis row 0 pre__filing_date: 10/21/2025 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/pre__filing_date`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-street_name"></a>

**dob_bis.0.street_name** [fact] dob_bis row 0 street_name: JEROME AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/street_name`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bbl"></a>

**dob_bis.1.bbl** [fact] dob_bis row 1 bbl: 2028530012 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bbl`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bin__"></a>

**dob_bis.1.bin__** [fact] dob_bis row 1 bin__: 2129813 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bin__`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-doc__"></a>

**dob_bis.1.doc__** [fact] dob_bis row 1 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/doc__`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-house__"></a>

**dob_bis.1.house__** [fact] dob_bis row 1 house__: 1940 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/house__`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job__"></a>

**dob_bis.1.job__** [fact] dob_bis row 1 job__: 240339406 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job__`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_description"></a>

**dob_bis.1.job_description** [fact] dob_bis row 1 job_description: PROPOSE BUILDER'S PAVEMENT PLAN FOR A TOTAL STREET FRONTAGE OF 126.68 LF FILED IN CONJUNCTION WITH NB # X00787559-I1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_description`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_status_descrp"></a>

**dob_bis.1.job_status_descrp** [fact] dob_bis row 1 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_status_descrp`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_type"></a>

**dob_bis.1.job_type** [fact] dob_bis row 1 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_type`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-latest_action_date"></a>

**dob_bis.1.latest_action_date** [fact] dob_bis row 1 latest_action_date: 12/19/2023 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/latest_action_date`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-pre__filing_date"></a>

**dob_bis.1.pre__filing_date** [fact] dob_bis row 1 pre__filing_date: 11/09/2022 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/pre__filing_date`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-street_name"></a>

**dob_bis.1.street_name** [fact] dob_bis row 1 street_name: JEROME AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/street_name`; SHA256 `d1761b7955d1cbc5011ba3ae4e6f3e3861f6d51bbe2750a5419e62cdbe6583b0`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_now-returned_rows"></a>

**dob_now.returned_rows** [calculation] dob_now returned rows in this exact-BBL query: 38 (returned rows; not projects or total population)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

Bounded query; see truncation and source limits.

<a id="dob_now-0-bbl"></a>

**dob_now.0.bbl** [fact] dob_now row 0 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-bin"></a>

**dob_now.0.bin** [fact] dob_now row 0 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-current_status_date"></a>

**dob_now.0.current_status_date** [fact] dob_now row 0 current_status_date: 2026-07-24T13:28:17.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-filing_date"></a>

**dob_now.0.filing_date** [fact] dob_now row 0 filing_date: 2026-06-03T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-filing_status"></a>

**dob_now.0.filing_status** [fact] dob_now row 0 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-house_no"></a>

**dob_now.0.house_no** [fact] dob_now row 0 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-job_description"></a>

**dob_now.0.job_description** [fact] dob_now row 0 job_description: HUB CONSULTATION MEETING HELD AND ACCEPTED ON 8/8/2022. PROPOSE NEW 13-STORY PLUS CELLAR MIXED-USE BUILDING. OBTAIN NEW C OF O. THIS PROJECT IS MANDATORY INCLUSIONARY, 100% LOW INCOME HOUSING, AND QUALITY HOUSING. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-job_filing_number"></a>

**dob_now.0.job_filing_number** [fact] dob_now row 0 job_filing_number: X00787559-A1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-job_type"></a>

**dob_now.0.job_type** [fact] dob_now row 0 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-proposed_dwelling_units"></a>

**dob_now.0.proposed_dwelling_units** [fact] dob_now row 0 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-street_name"></a>

**dob_now.0.street_name** [fact] dob_now row 0 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-bbl"></a>

**dob_now.1.bbl** [fact] dob_now row 1 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-bin"></a>

**dob_now.1.bin** [fact] dob_now row 1 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-current_status_date"></a>

**dob_now.1.current_status_date** [fact] dob_now row 1 current_status_date: 2026-07-24T13:27:06.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-filing_date"></a>

**dob_now.1.filing_date** [fact] dob_now row 1 filing_date: 2022-08-22T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-filing_status"></a>

**dob_now.1.filing_status** [fact] dob_now row 1 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-house_no"></a>

**dob_now.1.house_no** [fact] dob_now row 1 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-job_description"></a>

**dob_now.1.job_description** [fact] dob_now row 1 job_description: HUB CONSULTATION MEETING HELD AND ACCEPTED ON 8/8/2022. PROPOSE NEW 13-STORY PLUS CELLAR MIXED-USE BUILDING. OBTAIN NEW C OF O. THIS PROJECT IS MANDATORY INCLUSIONARY, 100% LOW INCOME HOUSING, AND QUALITY HOUSING. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-job_filing_number"></a>

**dob_now.1.job_filing_number** [fact] dob_now row 1 job_filing_number: X00787559-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-job_type"></a>

**dob_now.1.job_type** [fact] dob_now row 1 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-proposed_dwelling_units"></a>

**dob_now.1.proposed_dwelling_units** [fact] dob_now row 1 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-street_name"></a>

**dob_now.1.street_name** [fact] dob_now row 1 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-bbl"></a>

**dob_now.2.bbl** [fact] dob_now row 2 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-bin"></a>

**dob_now.2.bin** [fact] dob_now row 2 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-current_status_date"></a>

**dob_now.2.current_status_date** [fact] dob_now row 2 current_status_date: 2024-04-30T18:16:29.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-filing_date"></a>

**dob_now.2.filing_date** [fact] dob_now row 2 filing_date: 2024-02-29T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-filing_status"></a>

**dob_now.2.filing_status** [fact] dob_now row 2 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-house_no"></a>

**dob_now.2.house_no** [fact] dob_now row 2 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-job_description"></a>

**dob_now.2.job_description** [fact] dob_now row 2 job_description: Subsequent application for proposed SOE Work filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-job_filing_number"></a>

**dob_now.2.job_filing_number** [fact] dob_now row 2 job_filing_number: X00787559-P1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-job_type"></a>

**dob_now.2.job_type** [fact] dob_now row 2 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-proposed_dwelling_units"></a>

**dob_now.2.proposed_dwelling_units** [fact] dob_now row 2 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-street_name"></a>

**dob_now.2.street_name** [fact] dob_now row 2 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-bbl"></a>

**dob_now.3.bbl** [fact] dob_now row 3 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-bin"></a>

**dob_now.3.bin** [fact] dob_now row 3 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-current_status_date"></a>

**dob_now.3.current_status_date** [fact] dob_now row 3 current_status_date: 2024-05-02T17:32:59.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-filing_date"></a>

**dob_now.3.filing_date** [fact] dob_now row 3 filing_date: 2024-04-25T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-filing_status"></a>

**dob_now.3.filing_status** [fact] dob_now row 3 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-house_no"></a>

**dob_now.3.house_no** [fact] dob_now row 3 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-job_description"></a>

**dob_now.3.job_description** [fact] dob_now row 3 job_description: Propose Underpinning the adjacent buildings, 1934 and 1946 Jerome Avenue filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-job_filing_number"></a>

**dob_now.3.job_filing_number** [fact] dob_now row 3 job_filing_number: X00787559-P2 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-job_type"></a>

**dob_now.3.job_type** [fact] dob_now row 3 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-proposed_dwelling_units"></a>

**dob_now.3.proposed_dwelling_units** [fact] dob_now row 3 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-street_name"></a>

**dob_now.3.street_name** [fact] dob_now row 3 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-bbl"></a>

**dob_now.4.bbl** [fact] dob_now row 4 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-bin"></a>

**dob_now.4.bin** [fact] dob_now row 4 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-current_status_date"></a>

**dob_now.4.current_status_date** [fact] dob_now row 4 current_status_date: 2024-09-05T20:56:33.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-filing_date"></a>

**dob_now.4.filing_date** [fact] dob_now row 4 filing_date: 2024-09-03T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-filing_status"></a>

**dob_now.4.filing_status** [fact] dob_now row 4 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-house_no"></a>

**dob_now.4.house_no** [fact] dob_now row 4 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-job_description"></a>

**dob_now.4.job_description** [fact] dob_now row 4 job_description: Subsequent application for proposed SOE Work filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-job_filing_number"></a>

**dob_now.4.job_filing_number** [fact] dob_now row 4 job_filing_number: X00787559-P3 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-job_type"></a>

**dob_now.4.job_type** [fact] dob_now row 4 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-proposed_dwelling_units"></a>

**dob_now.4.proposed_dwelling_units** [fact] dob_now row 4 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-street_name"></a>

**dob_now.4.street_name** [fact] dob_now row 4 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-bbl"></a>

**dob_now.5.bbl** [fact] dob_now row 5 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-bin"></a>

**dob_now.5.bin** [fact] dob_now row 5 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-current_status_date"></a>

**dob_now.5.current_status_date** [fact] dob_now row 5 current_status_date: 2024-09-06T20:35:43.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-filing_date"></a>

**dob_now.5.filing_date** [fact] dob_now row 5 filing_date: 2024-09-03T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-filing_status"></a>

**dob_now.5.filing_status** [fact] dob_now row 5 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-house_no"></a>

**dob_now.5.house_no** [fact] dob_now row 5 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-job_description"></a>

**dob_now.5.job_description** [fact] dob_now row 5 job_description: Propose Underpinning the adjacent buildings, 1934 and 1946 Jerome Avenue filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-job_filing_number"></a>

**dob_now.5.job_filing_number** [fact] dob_now row 5 job_filing_number: X00787559-P4 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-job_type"></a>

**dob_now.5.job_type** [fact] dob_now row 5 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-proposed_dwelling_units"></a>

**dob_now.5.proposed_dwelling_units** [fact] dob_now row 5 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-5-street_name"></a>

**dob_now.5.street_name** [fact] dob_now row 5 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/5/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-bbl"></a>

**dob_now.6.bbl** [fact] dob_now row 6 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-bin"></a>

**dob_now.6.bin** [fact] dob_now row 6 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-current_status_date"></a>

**dob_now.6.current_status_date** [fact] dob_now row 6 current_status_date: 2026-03-29T18:18:13.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-filing_date"></a>

**dob_now.6.filing_date** [fact] dob_now row 6 filing_date: 2026-03-03T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-filing_status"></a>

**dob_now.6.filing_status** [fact] dob_now row 6 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-house_no"></a>

**dob_now.6.house_no** [fact] dob_now row 6 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-job_description"></a>

**dob_now.6.job_description** [fact] dob_now row 6 job_description: PROPOSE STRUCTURAL SCOPE OF WORKS IN CONJUNCTION WITH NB # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-job_filing_number"></a>

**dob_now.6.job_filing_number** [fact] dob_now row 6 job_filing_number: X00787559-P6 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-job_type"></a>

**dob_now.6.job_type** [fact] dob_now row 6 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-proposed_dwelling_units"></a>

**dob_now.6.proposed_dwelling_units** [fact] dob_now row 6 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-6-street_name"></a>

**dob_now.6.street_name** [fact] dob_now row 6 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/6/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-bbl"></a>

**dob_now.7.bbl** [fact] dob_now row 7 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-bin"></a>

**dob_now.7.bin** [fact] dob_now row 7 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-current_status_date"></a>

**dob_now.7.current_status_date** [fact] dob_now row 7 current_status_date: 2026-05-03T18:45:45.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-filing_date"></a>

**dob_now.7.filing_date** [fact] dob_now row 7 filing_date: 2026-04-10T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-filing_status"></a>

**dob_now.7.filing_status** [fact] dob_now row 7 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-house_no"></a>

**dob_now.7.house_no** [fact] dob_now row 7 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-job_description"></a>

**dob_now.7.job_description** [fact] dob_now row 7 job_description: Subsequent application for proposed Mechanical Scope of Work filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-job_filing_number"></a>

**dob_now.7.job_filing_number** [fact] dob_now row 7 job_filing_number: X00787559-P7 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-job_type"></a>

**dob_now.7.job_type** [fact] dob_now row 7 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-proposed_dwelling_units"></a>

**dob_now.7.proposed_dwelling_units** [fact] dob_now row 7 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-7-street_name"></a>

**dob_now.7.street_name** [fact] dob_now row 7 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/7/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-bbl"></a>

**dob_now.8.bbl** [fact] dob_now row 8 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-bin"></a>

**dob_now.8.bin** [fact] dob_now row 8 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-current_status_date"></a>

**dob_now.8.current_status_date** [fact] dob_now row 8 current_status_date: 2026-05-03T18:48:06.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-filing_date"></a>

**dob_now.8.filing_date** [fact] dob_now row 8 filing_date: 2022-11-01T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-filing_status"></a>

**dob_now.8.filing_status** [fact] dob_now row 8 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-house_no"></a>

**dob_now.8.house_no** [fact] dob_now row 8 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-job_description"></a>

**dob_now.8.job_description** [fact] dob_now row 8 job_description: Subsequent application for proposed Mechanical Scope of Work filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-job_filing_number"></a>

**dob_now.8.job_filing_number** [fact] dob_now row 8 job_filing_number: X00787559-S1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-job_type"></a>

**dob_now.8.job_type** [fact] dob_now row 8 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-proposed_dwelling_units"></a>

**dob_now.8.proposed_dwelling_units** [fact] dob_now row 8 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-8-street_name"></a>

**dob_now.8.street_name** [fact] dob_now row 8 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/8/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-bbl"></a>

**dob_now.9.bbl** [fact] dob_now row 9 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-bin"></a>

**dob_now.9.bin** [fact] dob_now row 9 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-current_status_date"></a>

**dob_now.9.current_status_date** [fact] dob_now row 9 current_status_date: 2025-10-17T21:33:20.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-filing_date"></a>

**dob_now.9.filing_date** [fact] dob_now row 9 filing_date: 2022-11-02T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-filing_status"></a>

**dob_now.9.filing_status** [fact] dob_now row 9 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-house_no"></a>

**dob_now.9.house_no** [fact] dob_now row 9 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-job_description"></a>

**dob_now.9.job_description** [fact] dob_now row 9 job_description: Subsequent application for Plumbing Scope of Work filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-job_filing_number"></a>

**dob_now.9.job_filing_number** [fact] dob_now row 9 job_filing_number: X00787559-S2 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-job_type"></a>

**dob_now.9.job_type** [fact] dob_now row 9 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-proposed_dwelling_units"></a>

**dob_now.9.proposed_dwelling_units** [fact] dob_now row 9 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-9-street_name"></a>

**dob_now.9.street_name** [fact] dob_now row 9 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/9/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-bbl"></a>

**dob_now.10.bbl** [fact] dob_now row 10 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-bin"></a>

**dob_now.10.bin** [fact] dob_now row 10 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-current_status_date"></a>

**dob_now.10.current_status_date** [fact] dob_now row 10 current_status_date: 2026-01-22T18:57:20.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-filing_date"></a>

**dob_now.10.filing_date** [fact] dob_now row 10 filing_date: 2022-11-01T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-filing_status"></a>

**dob_now.10.filing_status** [fact] dob_now row 10 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-house_no"></a>

**dob_now.10.house_no** [fact] dob_now row 10 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-job_description"></a>

**dob_now.10.job_description** [fact] dob_now row 10 job_description: Subsequent application for Sprinkler and Standpipe System filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-job_filing_number"></a>

**dob_now.10.job_filing_number** [fact] dob_now row 10 job_filing_number: X00787559-S3 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-job_type"></a>

**dob_now.10.job_type** [fact] dob_now row 10 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-proposed_dwelling_units"></a>

**dob_now.10.proposed_dwelling_units** [fact] dob_now row 10 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-10-street_name"></a>

**dob_now.10.street_name** [fact] dob_now row 10 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/10/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-bbl"></a>

**dob_now.11.bbl** [fact] dob_now row 11 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-bin"></a>

**dob_now.11.bin** [fact] dob_now row 11 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-current_status_date"></a>

**dob_now.11.current_status_date** [fact] dob_now row 11 current_status_date: 2026-04-13T18:10:03.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-filing_date"></a>

**dob_now.11.filing_date** [fact] dob_now row 11 filing_date: 2022-11-03T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-filing_status"></a>

**dob_now.11.filing_status** [fact] dob_now row 11 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-house_no"></a>

**dob_now.11.house_no** [fact] dob_now row 11 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-job_description"></a>

**dob_now.11.job_description** [fact] dob_now row 11 job_description: PROPOSED FOUNDATAION SCOPE OF WORKS IN CONJUNCTION WITH NB # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-job_filing_number"></a>

**dob_now.11.job_filing_number** [fact] dob_now row 11 job_filing_number: X00787559-S4 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-job_type"></a>

**dob_now.11.job_type** [fact] dob_now row 11 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-proposed_dwelling_units"></a>

**dob_now.11.proposed_dwelling_units** [fact] dob_now row 11 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-11-street_name"></a>

**dob_now.11.street_name** [fact] dob_now row 11 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/11/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-bbl"></a>

**dob_now.12.bbl** [fact] dob_now row 12 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-bin"></a>

**dob_now.12.bin** [fact] dob_now row 12 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-current_status_date"></a>

**dob_now.12.current_status_date** [fact] dob_now row 12 current_status_date: 2026-03-31T17:22:34.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-filing_date"></a>

**dob_now.12.filing_date** [fact] dob_now row 12 filing_date: 2022-10-24T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-filing_status"></a>

**dob_now.12.filing_status** [fact] dob_now row 12 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-house_no"></a>

**dob_now.12.house_no** [fact] dob_now row 12 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-job_description"></a>

**dob_now.12.job_description** [fact] dob_now row 12 job_description: PROPOSE STRUCTURAL SCOPE OF WORKS IN CONJUNCTION WITH NB # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-job_filing_number"></a>

**dob_now.12.job_filing_number** [fact] dob_now row 12 job_filing_number: X00787559-S5 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-job_type"></a>

**dob_now.12.job_type** [fact] dob_now row 12 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-proposed_dwelling_units"></a>

**dob_now.12.proposed_dwelling_units** [fact] dob_now row 12 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-12-street_name"></a>

**dob_now.12.street_name** [fact] dob_now row 12 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/12/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-bbl"></a>

**dob_now.13.bbl** [fact] dob_now row 13 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-bin"></a>

**dob_now.13.bin** [fact] dob_now row 13 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-current_status_date"></a>

**dob_now.13.current_status_date** [fact] dob_now row 13 current_status_date: 2024-09-05T20:57:15.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-filing_date"></a>

**dob_now.13.filing_date** [fact] dob_now row 13 filing_date: 2023-01-24T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-filing_status"></a>

**dob_now.13.filing_status** [fact] dob_now row 13 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-house_no"></a>

**dob_now.13.house_no** [fact] dob_now row 13 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-job_description"></a>

**dob_now.13.job_description** [fact] dob_now row 13 job_description: Subsequent application for proposed SOE Work filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-job_filing_number"></a>

**dob_now.13.job_filing_number** [fact] dob_now row 13 job_filing_number: X00787559-S6 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-job_type"></a>

**dob_now.13.job_type** [fact] dob_now row 13 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-proposed_dwelling_units"></a>

**dob_now.13.proposed_dwelling_units** [fact] dob_now row 13 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-13-street_name"></a>

**dob_now.13.street_name** [fact] dob_now row 13 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/13/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-bbl"></a>

**dob_now.14.bbl** [fact] dob_now row 14 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-bin"></a>

**dob_now.14.bin** [fact] dob_now row 14 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-current_status_date"></a>

**dob_now.14.current_status_date** [fact] dob_now row 14 current_status_date: 2024-09-06T20:35:53.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-filing_date"></a>

**dob_now.14.filing_date** [fact] dob_now row 14 filing_date: 2023-01-24T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-filing_status"></a>

**dob_now.14.filing_status** [fact] dob_now row 14 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-house_no"></a>

**dob_now.14.house_no** [fact] dob_now row 14 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-job_description"></a>

**dob_now.14.job_description** [fact] dob_now row 14 job_description: Propose Underpinning the adjacent buildings, 1934 and 1946 Jerome Avenue filed in conjunction with NB-GC # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-job_filing_number"></a>

**dob_now.14.job_filing_number** [fact] dob_now row 14 job_filing_number: X00787559-S7 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-job_type"></a>

**dob_now.14.job_type** [fact] dob_now row 14 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-proposed_dwelling_units"></a>

**dob_now.14.proposed_dwelling_units** [fact] dob_now row 14 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-14-street_name"></a>

**dob_now.14.street_name** [fact] dob_now row 14 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/14/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-bbl"></a>

**dob_now.15.bbl** [fact] dob_now row 15 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-bin"></a>

**dob_now.15.bin** [fact] dob_now row 15 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-current_status_date"></a>

**dob_now.15.current_status_date** [fact] dob_now row 15 current_status_date: 2026-01-13T18:33:25.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-filing_date"></a>

**dob_now.15.filing_date** [fact] dob_now row 15 filing_date: 2023-04-21T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-filing_status"></a>

**dob_now.15.filing_status** [fact] dob_now row 15 filing_status: Filing Withdrawn (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-house_no"></a>

**dob_now.15.house_no** [fact] dob_now row 15 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-job_description"></a>

**dob_now.15.job_description** [fact] dob_now row 15 job_description: Propose Partial Foundation Work for a new 13-story residential building filed in conjunction with NB # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-job_filing_number"></a>

**dob_now.15.job_filing_number** [fact] dob_now row 15 job_filing_number: X00787559-S8 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-job_type"></a>

**dob_now.15.job_type** [fact] dob_now row 15 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-proposed_dwelling_units"></a>

**dob_now.15.proposed_dwelling_units** [fact] dob_now row 15 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-15-street_name"></a>

**dob_now.15.street_name** [fact] dob_now row 15 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/15/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-bbl"></a>

**dob_now.16.bbl** [fact] dob_now row 16 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-bin"></a>

**dob_now.16.bin** [fact] dob_now row 16 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-current_status_date"></a>

**dob_now.16.current_status_date** [fact] dob_now row 16 current_status_date: 2025-09-04T14:08:27.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-filing_date"></a>

**dob_now.16.filing_date** [fact] dob_now row 16 filing_date: 2023-12-19T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-filing_status"></a>

**dob_now.16.filing_status** [fact] dob_now row 16 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-house_no"></a>

**dob_now.16.house_no** [fact] dob_now row 16 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-job_description"></a>

**dob_now.16.job_description** [fact] dob_now row 16 job_description: Proposed installation of a temporary combined class I fire standpipe system in conjunction with NB # X00787559-I1. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-job_filing_number"></a>

**dob_now.16.job_filing_number** [fact] dob_now row 16 job_filing_number: X00787559-S9 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-job_type"></a>

**dob_now.16.job_type** [fact] dob_now row 16 job_type: New Building (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-proposed_dwelling_units"></a>

**dob_now.16.proposed_dwelling_units** [fact] dob_now row 16 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-16-street_name"></a>

**dob_now.16.street_name** [fact] dob_now row 16 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/16/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-bbl"></a>

**dob_now.17.bbl** [fact] dob_now row 17 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-bin"></a>

**dob_now.17.bin** [fact] dob_now row 17 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-current_status_date"></a>

**dob_now.17.current_status_date** [fact] dob_now row 17 current_status_date: 2024-07-31T16:42:22.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-filing_date"></a>

**dob_now.17.filing_date** [fact] dob_now row 17 filing_date: 2023-06-29T10:59:27.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-filing_status"></a>

**dob_now.17.filing_status** [fact] dob_now row 17 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-house_no"></a>

**dob_now.17.house_no** [fact] dob_now row 17 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-job_description"></a>

**dob_now.17.job_description** [fact] dob_now row 17 job_description: full demolition of one story structure, using hand held and mechanical means to assist. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-job_filing_number"></a>

**dob_now.17.job_filing_number** [fact] dob_now row 17 job_filing_number: X00862805-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-job_type"></a>

**dob_now.17.job_type** [fact] dob_now row 17 job_type: Full Demolition (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-17-street_name"></a>

**dob_now.17.street_name** [fact] dob_now row 17 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/17/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-bbl"></a>

**dob_now.18.bbl** [fact] dob_now row 18 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-bin"></a>

**dob_now.18.bin** [fact] dob_now row 18 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-current_status_date"></a>

**dob_now.18.current_status_date** [fact] dob_now row 18 current_status_date: 2024-07-31T16:42:32.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-filing_date"></a>

**dob_now.18.filing_date** [fact] dob_now row 18 filing_date: 2024-04-03T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-filing_status"></a>

**dob_now.18.filing_status** [fact] dob_now row 18 filing_status: Full Demolition Signed-off (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-house_no"></a>

**dob_now.18.house_no** [fact] dob_now row 18 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-job_description"></a>

**dob_now.18.job_description** [fact] dob_now row 18 job_description: full demolition of one story structure, using hand held and mechanical means to assist. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-job_filing_number"></a>

**dob_now.18.job_filing_number** [fact] dob_now row 18 job_filing_number: X00862805-P1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-job_type"></a>

**dob_now.18.job_type** [fact] dob_now row 18 job_type: Full Demolition (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-18-street_name"></a>

**dob_now.18.street_name** [fact] dob_now row 18 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/18/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-bbl"></a>

**dob_now.19.bbl** [fact] dob_now row 19 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-bin"></a>

**dob_now.19.bin** [fact] dob_now row 19 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-current_status_date"></a>

**dob_now.19.current_status_date** [fact] dob_now row 19 current_status_date: 2024-07-31T16:42:36.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-filing_date"></a>

**dob_now.19.filing_date** [fact] dob_now row 19 filing_date: 2024-05-17T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-filing_status"></a>

**dob_now.19.filing_status** [fact] dob_now row 19 filing_status: Full Demolition Signed-off (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-house_no"></a>

**dob_now.19.house_no** [fact] dob_now row 19 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-job_description"></a>

**dob_now.19.job_description** [fact] dob_now row 19 job_description: mechanical equipment to be used in accordance with approved demolition plans (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-job_filing_number"></a>

**dob_now.19.job_filing_number** [fact] dob_now row 19 job_filing_number: X00862805-S1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-job_type"></a>

**dob_now.19.job_type** [fact] dob_now row 19 job_type: Full Demolition (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-19-street_name"></a>

**dob_now.19.street_name** [fact] dob_now row 19 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/19/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-bbl"></a>

**dob_now.20.bbl** [fact] dob_now row 20 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-bin"></a>

**dob_now.20.bin** [fact] dob_now row 20 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-current_status_date"></a>

**dob_now.20.current_status_date** [fact] dob_now row 20 current_status_date: 2024-07-31T16:42:43.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-filing_date"></a>

**dob_now.20.filing_date** [fact] dob_now row 20 filing_date: 2024-04-16T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-filing_status"></a>

**dob_now.20.filing_status** [fact] dob_now row 20 filing_status: Full Demolition Signed-off (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-house_no"></a>

**dob_now.20.house_no** [fact] dob_now row 20 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-job_description"></a>

**dob_now.20.job_description** [fact] dob_now row 20 job_description: installation of construction fence to protect site, during full demolition (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-job_filing_number"></a>

**dob_now.20.job_filing_number** [fact] dob_now row 20 job_filing_number: X00862805-S2 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-job_type"></a>

**dob_now.20.job_type** [fact] dob_now row 20 job_type: Full Demolition (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-20-street_name"></a>

**dob_now.20.street_name** [fact] dob_now row 20 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/20/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-bbl"></a>

**dob_now.21.bbl** [fact] dob_now row 21 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-bin"></a>

**dob_now.21.bin** [fact] dob_now row 21 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-current_status_date"></a>

**dob_now.21.current_status_date** [fact] dob_now row 21 current_status_date: 2024-10-01T19:35:57.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-existing_dwelling_units"></a>

**dob_now.21.existing_dwelling_units** [fact] dob_now row 21 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-filing_date"></a>

**dob_now.21.filing_date** [fact] dob_now row 21 filing_date: 2024-04-19T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-filing_status"></a>

**dob_now.21.filing_status** [fact] dob_now row 21 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-house_no"></a>

**dob_now.21.house_no** [fact] dob_now row 21 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-job_description"></a>

**dob_now.21.job_description** [fact] dob_now row 21 job_description: HEAVY DUTY SIDEWALK SHED DURING NB CONST, FILED SEP. SIDEWALK SHED SHALL COMPLY WITH CH #33 OF THE NYC BC. NO CHANGE IN USE, OCCUPANCY OR EGRESS UNDER THIS APPLICATION. DOT PERMITS BY OTHERS FOR SHED INSTALLED ON SIDEWALK/ROADWAY (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-job_filing_number"></a>

**dob_now.21.job_filing_number** [fact] dob_now row 21 job_filing_number: X01036441-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-job_type"></a>

**dob_now.21.job_type** [fact] dob_now row 21 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-proposed_dwelling_units"></a>

**dob_now.21.proposed_dwelling_units** [fact] dob_now row 21 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-21-street_name"></a>

**dob_now.21.street_name** [fact] dob_now row 21 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/21/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-bbl"></a>

**dob_now.22.bbl** [fact] dob_now row 22 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-bin"></a>

**dob_now.22.bin** [fact] dob_now row 22 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-current_status_date"></a>

**dob_now.22.current_status_date** [fact] dob_now row 22 current_status_date: 2026-03-12T18:27:29.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-existing_dwelling_units"></a>

**dob_now.22.existing_dwelling_units** [fact] dob_now row 22 existing_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-filing_date"></a>

**dob_now.22.filing_date** [fact] dob_now row 22 filing_date: 2024-08-12T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-filing_status"></a>

**dob_now.22.filing_status** [fact] dob_now row 22 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-house_no"></a>

**dob_now.22.house_no** [fact] dob_now row 22 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-job_description"></a>

**dob_now.22.job_description** [fact] dob_now row 22 job_description: Installation of a temporary roof protection per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-job_filing_number"></a>

**dob_now.22.job_filing_number** [fact] dob_now row 22 job_filing_number: X01081403-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-job_type"></a>

**dob_now.22.job_type** [fact] dob_now row 22 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-proposed_dwelling_units"></a>

**dob_now.22.proposed_dwelling_units** [fact] dob_now row 22 proposed_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-22-street_name"></a>

**dob_now.22.street_name** [fact] dob_now row 22 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/22/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-bbl"></a>

**dob_now.23.bbl** [fact] dob_now row 23 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-bin"></a>

**dob_now.23.bin** [fact] dob_now row 23 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-current_status_date"></a>

**dob_now.23.current_status_date** [fact] dob_now row 23 current_status_date: 2025-02-13T16:05:18.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-existing_dwelling_units"></a>

**dob_now.23.existing_dwelling_units** [fact] dob_now row 23 existing_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-filing_date"></a>

**dob_now.23.filing_date** [fact] dob_now row 23 filing_date: 2025-02-13T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-filing_status"></a>

**dob_now.23.filing_status** [fact] dob_now row 23 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-house_no"></a>

**dob_now.23.house_no** [fact] dob_now row 23 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-job_description"></a>

**dob_now.23.job_description** [fact] dob_now row 23 job_description: Installation of a temporary roof protection per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-job_filing_number"></a>

**dob_now.23.job_filing_number** [fact] dob_now row 23 job_filing_number: X01081403-P1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-job_type"></a>

**dob_now.23.job_type** [fact] dob_now row 23 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-proposed_dwelling_units"></a>

**dob_now.23.proposed_dwelling_units** [fact] dob_now row 23 proposed_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-23-street_name"></a>

**dob_now.23.street_name** [fact] dob_now row 23 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/23/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-bbl"></a>

**dob_now.24.bbl** [fact] dob_now row 24 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-bin"></a>

**dob_now.24.bin** [fact] dob_now row 24 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-current_status_date"></a>

**dob_now.24.current_status_date** [fact] dob_now row 24 current_status_date: 2026-02-18T21:30:45.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-existing_dwelling_units"></a>

**dob_now.24.existing_dwelling_units** [fact] dob_now row 24 existing_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-filing_date"></a>

**dob_now.24.filing_date** [fact] dob_now row 24 filing_date: 2024-08-08T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-filing_status"></a>

**dob_now.24.filing_status** [fact] dob_now row 24 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-house_no"></a>

**dob_now.24.house_no** [fact] dob_now row 24 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-job_description"></a>

**dob_now.24.job_description** [fact] dob_now row 24 job_description: Installation of a temporarily heavy-duty sidewalk shed per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-job_filing_number"></a>

**dob_now.24.job_filing_number** [fact] dob_now row 24 job_filing_number: X01086372-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-job_type"></a>

**dob_now.24.job_type** [fact] dob_now row 24 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-proposed_dwelling_units"></a>

**dob_now.24.proposed_dwelling_units** [fact] dob_now row 24 proposed_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-24-street_name"></a>

**dob_now.24.street_name** [fact] dob_now row 24 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/24/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-bbl"></a>

**dob_now.25.bbl** [fact] dob_now row 25 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-bin"></a>

**dob_now.25.bin** [fact] dob_now row 25 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-current_status_date"></a>

**dob_now.25.current_status_date** [fact] dob_now row 25 current_status_date: 2025-02-26T01:48:06.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-existing_dwelling_units"></a>

**dob_now.25.existing_dwelling_units** [fact] dob_now row 25 existing_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-filing_date"></a>

**dob_now.25.filing_date** [fact] dob_now row 25 filing_date: 2025-02-21T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-filing_status"></a>

**dob_now.25.filing_status** [fact] dob_now row 25 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-house_no"></a>

**dob_now.25.house_no** [fact] dob_now row 25 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-job_description"></a>

**dob_now.25.job_description** [fact] dob_now row 25 job_description: Installation of a temporarily heavy-duty sidewalk shed per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-job_filing_number"></a>

**dob_now.25.job_filing_number** [fact] dob_now row 25 job_filing_number: X01086372-P1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-job_type"></a>

**dob_now.25.job_type** [fact] dob_now row 25 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-proposed_dwelling_units"></a>

**dob_now.25.proposed_dwelling_units** [fact] dob_now row 25 proposed_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-25-street_name"></a>

**dob_now.25.street_name** [fact] dob_now row 25 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/25/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-bbl"></a>

**dob_now.26.bbl** [fact] dob_now row 26 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-bin"></a>

**dob_now.26.bin** [fact] dob_now row 26 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-current_status_date"></a>

**dob_now.26.current_status_date** [fact] dob_now row 26 current_status_date: 2025-08-15T16:08:17.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-existing_dwelling_units"></a>

**dob_now.26.existing_dwelling_units** [fact] dob_now row 26 existing_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-filing_date"></a>

**dob_now.26.filing_date** [fact] dob_now row 26 filing_date: 2025-08-13T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-filing_status"></a>

**dob_now.26.filing_status** [fact] dob_now row 26 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-house_no"></a>

**dob_now.26.house_no** [fact] dob_now row 26 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-job_description"></a>

**dob_now.26.job_description** [fact] dob_now row 26 job_description: Installation of a temporarily heavy-duty sidewalk shed per plan submitted. Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-job_filing_number"></a>

**dob_now.26.job_filing_number** [fact] dob_now row 26 job_filing_number: X01086372-P2 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-job_type"></a>

**dob_now.26.job_type** [fact] dob_now row 26 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-proposed_dwelling_units"></a>

**dob_now.26.proposed_dwelling_units** [fact] dob_now row 26 proposed_dwelling_units: 1 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-26-street_name"></a>

**dob_now.26.street_name** [fact] dob_now row 26 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/26/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-bbl"></a>

**dob_now.27.bbl** [fact] dob_now row 27 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-bin"></a>

**dob_now.27.bin** [fact] dob_now row 27 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-current_status_date"></a>

**dob_now.27.current_status_date** [fact] dob_now row 27 current_status_date: 2026-05-14T15:29:34.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-existing_dwelling_units"></a>

**dob_now.27.existing_dwelling_units** [fact] dob_now row 27 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-filing_date"></a>

**dob_now.27.filing_date** [fact] dob_now row 27 filing_date: 2024-07-25T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-filing_status"></a>

**dob_now.27.filing_status** [fact] dob_now row 27 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-house_no"></a>

**dob_now.27.house_no** [fact] dob_now row 27 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-job_description"></a>

**dob_now.27.job_description** [fact] dob_now row 27 job_description: Installation of a temporary construction fence per plan submitted.  Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-job_filing_number"></a>

**dob_now.27.job_filing_number** [fact] dob_now row 27 job_filing_number: X01086384-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-job_type"></a>

**dob_now.27.job_type** [fact] dob_now row 27 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-proposed_dwelling_units"></a>

**dob_now.27.proposed_dwelling_units** [fact] dob_now row 27 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-27-street_name"></a>

**dob_now.27.street_name** [fact] dob_now row 27 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/27/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-bbl"></a>

**dob_now.28.bbl** [fact] dob_now row 28 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-bin"></a>

**dob_now.28.bin** [fact] dob_now row 28 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-current_status_date"></a>

**dob_now.28.current_status_date** [fact] dob_now row 28 current_status_date: 2025-09-08T16:00:17.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-existing_dwelling_units"></a>

**dob_now.28.existing_dwelling_units** [fact] dob_now row 28 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-filing_date"></a>

**dob_now.28.filing_date** [fact] dob_now row 28 filing_date: 2025-09-05T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-filing_status"></a>

**dob_now.28.filing_status** [fact] dob_now row 28 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-house_no"></a>

**dob_now.28.house_no** [fact] dob_now row 28 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-job_description"></a>

**dob_now.28.job_description** [fact] dob_now row 28 job_description: Installation of a temporary construction fence per plan submitted.  Work shall comply with 2022 building codes chapter 33. No change in use, egress and/or occupancy with this application. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-job_filing_number"></a>

**dob_now.28.job_filing_number** [fact] dob_now row 28 job_filing_number: X01086384-P1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-job_type"></a>

**dob_now.28.job_type** [fact] dob_now row 28 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-proposed_dwelling_units"></a>

**dob_now.28.proposed_dwelling_units** [fact] dob_now row 28 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-28-street_name"></a>

**dob_now.28.street_name** [fact] dob_now row 28 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/28/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-bbl"></a>

**dob_now.29.bbl** [fact] dob_now row 29 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-bin"></a>

**dob_now.29.bin** [fact] dob_now row 29 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-current_status_date"></a>

**dob_now.29.current_status_date** [fact] dob_now row 29 current_status_date: 2025-11-18T18:28:43.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-existing_dwelling_units"></a>

**dob_now.29.existing_dwelling_units** [fact] dob_now row 29 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-filing_date"></a>

**dob_now.29.filing_date** [fact] dob_now row 29 filing_date: 2024-09-23T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-filing_status"></a>

**dob_now.29.filing_status** [fact] dob_now row 29 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-house_no"></a>

**dob_now.29.house_no** [fact] dob_now row 29 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-job_description"></a>

**dob_now.29.job_description** [fact] dob_now row 29 job_description: EQUIPMENT USE: DUAL 7000# CAPACITY PERSONNEL/MATERIAL HOISTS DURING NB CONST, FILED SEP. HOISTS SHALL COMPLY WITH CH #33 OF THE NYC BC. NO CHANGE IN USE, OCCUPANCY OR EGRESS UNDER THIS APPLICATION. ELEVATOR APPLICATION SUBMITTED SEPARATELY (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-job_filing_number"></a>

**dob_now.29.job_filing_number** [fact] dob_now row 29 job_filing_number: X01111863-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-job_type"></a>

**dob_now.29.job_type** [fact] dob_now row 29 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-proposed_dwelling_units"></a>

**dob_now.29.proposed_dwelling_units** [fact] dob_now row 29 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-29-street_name"></a>

**dob_now.29.street_name** [fact] dob_now row 29 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/29/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-bbl"></a>

**dob_now.30.bbl** [fact] dob_now row 30 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-bin"></a>

**dob_now.30.bin** [fact] dob_now row 30 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-current_status_date"></a>

**dob_now.30.current_status_date** [fact] dob_now row 30 current_status_date: 2024-12-03T14:07:30.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-existing_dwelling_units"></a>

**dob_now.30.existing_dwelling_units** [fact] dob_now row 30 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-filing_date"></a>

**dob_now.30.filing_date** [fact] dob_now row 30 filing_date: 2024-12-02T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-filing_status"></a>

**dob_now.30.filing_status** [fact] dob_now row 30 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-house_no"></a>

**dob_now.30.house_no** [fact] dob_now row 30 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-job_description"></a>

**dob_now.30.job_description** [fact] dob_now row 30 job_description: EQUIPMENT USE: DUAL 7000# CAPACITY PERSONNEL/MATERIAL HOISTS DURING NB CONST, FILED SEP. HOISTS SHALL COMPLY WITH CH #33 OF THE NYC BC. NO CHANGE IN USE, OCCUPANCY OR EGRESS UNDER THIS APPLICATION. ELEVATOR APPLICATION SUBMITTED SEPARATELY (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-job_filing_number"></a>

**dob_now.30.job_filing_number** [fact] dob_now row 30 job_filing_number: X01111863-P1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-job_type"></a>

**dob_now.30.job_type** [fact] dob_now row 30 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-proposed_dwelling_units"></a>

**dob_now.30.proposed_dwelling_units** [fact] dob_now row 30 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-30-street_name"></a>

**dob_now.30.street_name** [fact] dob_now row 30 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/30/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-bbl"></a>

**dob_now.31.bbl** [fact] dob_now row 31 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-bin"></a>

**dob_now.31.bin** [fact] dob_now row 31 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-current_status_date"></a>

**dob_now.31.current_status_date** [fact] dob_now row 31 current_status_date: 2025-02-24T19:44:10.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-existing_dwelling_units"></a>

**dob_now.31.existing_dwelling_units** [fact] dob_now row 31 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-filing_date"></a>

**dob_now.31.filing_date** [fact] dob_now row 31 filing_date: 2025-02-21T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-filing_status"></a>

**dob_now.31.filing_status** [fact] dob_now row 31 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-house_no"></a>

**dob_now.31.house_no** [fact] dob_now row 31 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-job_description"></a>

**dob_now.31.job_description** [fact] dob_now row 31 job_description: EQUIPMENT USE: DUAL 7000# CAPACITY PERSONNEL/MATERIAL HOISTS DURING NB CONST, FILED SEP. HOISTS SHALL COMPLY WITH CH #33 OF THE NYC BC. NO CHANGE IN USE, OCCUPANCY OR EGRESS UNDER THIS APPLICATION. ELEVATOR APPLICATION SUBMITTED SEPARATELY (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-job_filing_number"></a>

**dob_now.31.job_filing_number** [fact] dob_now row 31 job_filing_number: X01111863-P2 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-job_type"></a>

**dob_now.31.job_type** [fact] dob_now row 31 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-proposed_dwelling_units"></a>

**dob_now.31.proposed_dwelling_units** [fact] dob_now row 31 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-31-street_name"></a>

**dob_now.31.street_name** [fact] dob_now row 31 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/31/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-bbl"></a>

**dob_now.32.bbl** [fact] dob_now row 32 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-bin"></a>

**dob_now.32.bin** [fact] dob_now row 32 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-current_status_date"></a>

**dob_now.32.current_status_date** [fact] dob_now row 32 current_status_date: 2026-05-28T18:00:55.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-existing_dwelling_units"></a>

**dob_now.32.existing_dwelling_units** [fact] dob_now row 32 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-filing_date"></a>

**dob_now.32.filing_date** [fact] dob_now row 32 filing_date: 2024-12-05T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-filing_status"></a>

**dob_now.32.filing_status** [fact] dob_now row 32 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-house_no"></a>

**dob_now.32.house_no** [fact] dob_now row 32 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-job_description"></a>

**dob_now.32.job_description** [fact] dob_now row 32 job_description: INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-job_filing_number"></a>

**dob_now.32.job_filing_number** [fact] dob_now row 32 job_filing_number: X01127777-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-job_type"></a>

**dob_now.32.job_type** [fact] dob_now row 32 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-proposed_dwelling_units"></a>

**dob_now.32.proposed_dwelling_units** [fact] dob_now row 32 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-32-street_name"></a>

**dob_now.32.street_name** [fact] dob_now row 32 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/32/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-bbl"></a>

**dob_now.33.bbl** [fact] dob_now row 33 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-bin"></a>

**dob_now.33.bin** [fact] dob_now row 33 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-current_status_date"></a>

**dob_now.33.current_status_date** [fact] dob_now row 33 current_status_date: 2025-03-27T13:56:07.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-existing_dwelling_units"></a>

**dob_now.33.existing_dwelling_units** [fact] dob_now row 33 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-filing_date"></a>

**dob_now.33.filing_date** [fact] dob_now row 33 filing_date: 2025-03-25T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-filing_status"></a>

**dob_now.33.filing_status** [fact] dob_now row 33 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-house_no"></a>

**dob_now.33.house_no** [fact] dob_now row 33 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-job_description"></a>

**dob_now.33.job_description** [fact] dob_now row 33 job_description: INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-job_filing_number"></a>

**dob_now.33.job_filing_number** [fact] dob_now row 33 job_filing_number: X01127777-P1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-job_type"></a>

**dob_now.33.job_type** [fact] dob_now row 33 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-proposed_dwelling_units"></a>

**dob_now.33.proposed_dwelling_units** [fact] dob_now row 33 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-33-street_name"></a>

**dob_now.33.street_name** [fact] dob_now row 33 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/33/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-bbl"></a>

**dob_now.34.bbl** [fact] dob_now row 34 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-bin"></a>

**dob_now.34.bin** [fact] dob_now row 34 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-current_status_date"></a>

**dob_now.34.current_status_date** [fact] dob_now row 34 current_status_date: 2025-04-01T19:02:35.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-existing_dwelling_units"></a>

**dob_now.34.existing_dwelling_units** [fact] dob_now row 34 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-filing_date"></a>

**dob_now.34.filing_date** [fact] dob_now row 34 filing_date: 2025-03-31T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-filing_status"></a>

**dob_now.34.filing_status** [fact] dob_now row 34 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-house_no"></a>

**dob_now.34.house_no** [fact] dob_now row 34 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-job_description"></a>

**dob_now.34.job_description** [fact] dob_now row 34 job_description: INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-job_filing_number"></a>

**dob_now.34.job_filing_number** [fact] dob_now row 34 job_filing_number: X01127777-P2 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-job_type"></a>

**dob_now.34.job_type** [fact] dob_now row 34 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-proposed_dwelling_units"></a>

**dob_now.34.proposed_dwelling_units** [fact] dob_now row 34 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-34-street_name"></a>

**dob_now.34.street_name** [fact] dob_now row 34 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/34/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-bbl"></a>

**dob_now.35.bbl** [fact] dob_now row 35 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-bin"></a>

**dob_now.35.bin** [fact] dob_now row 35 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-current_status_date"></a>

**dob_now.35.current_status_date** [fact] dob_now row 35 current_status_date: 2025-05-14T16:30:30.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-existing_dwelling_units"></a>

**dob_now.35.existing_dwelling_units** [fact] dob_now row 35 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-filing_date"></a>

**dob_now.35.filing_date** [fact] dob_now row 35 filing_date: 2025-05-13T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-filing_status"></a>

**dob_now.35.filing_status** [fact] dob_now row 35 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-house_no"></a>

**dob_now.35.house_no** [fact] dob_now row 35 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-job_description"></a>

**dob_now.35.job_description** [fact] dob_now row 35 job_description: INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-job_filing_number"></a>

**dob_now.35.job_filing_number** [fact] dob_now row 35 job_filing_number: X01127777-P3 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-job_type"></a>

**dob_now.35.job_type** [fact] dob_now row 35 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-proposed_dwelling_units"></a>

**dob_now.35.proposed_dwelling_units** [fact] dob_now row 35 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-35-street_name"></a>

**dob_now.35.street_name** [fact] dob_now row 35 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/35/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-bbl"></a>

**dob_now.36.bbl** [fact] dob_now row 36 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-bin"></a>

**dob_now.36.bin** [fact] dob_now row 36 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-current_status_date"></a>

**dob_now.36.current_status_date** [fact] dob_now row 36 current_status_date: 2025-12-09T20:24:03.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-existing_dwelling_units"></a>

**dob_now.36.existing_dwelling_units** [fact] dob_now row 36 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/existing_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-filing_date"></a>

**dob_now.36.filing_date** [fact] dob_now row 36 filing_date: 2025-12-08T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-filing_status"></a>

**dob_now.36.filing_status** [fact] dob_now row 36 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-house_no"></a>

**dob_now.36.house_no** [fact] dob_now row 36 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-job_description"></a>

**dob_now.36.job_description** [fact] dob_now row 36 job_description: INSTALLATION OF TEMPORARY PIPE SCAFFOLD AS PER PLANS. NO CHANGE IN USE, EGRESS OR OCCUPANCY. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-job_filing_number"></a>

**dob_now.36.job_filing_number** [fact] dob_now row 36 job_filing_number: X01127777-P4 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-job_type"></a>

**dob_now.36.job_type** [fact] dob_now row 36 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-proposed_dwelling_units"></a>

**dob_now.36.proposed_dwelling_units** [fact] dob_now row 36 proposed_dwelling_units: 115 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/proposed_dwelling_units`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-36-street_name"></a>

**dob_now.36.street_name** [fact] dob_now row 36 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/36/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-bbl"></a>

**dob_now.37.bbl** [fact] dob_now row 37 bbl: 2028530012 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/bbl`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-bin"></a>

**dob_now.37.bin** [fact] dob_now row 37 bin: 2129813 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/bin`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-current_status_date"></a>

**dob_now.37.current_status_date** [fact] dob_now row 37 current_status_date: 2026-08-20T15:56:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/current_status_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-filing_date"></a>

**dob_now.37.filing_date** [fact] dob_now row 37 filing_date: 2025-04-21T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/filing_date`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-filing_status"></a>

**dob_now.37.filing_status** [fact] dob_now row 37 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/filing_status`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-house_no"></a>

**dob_now.37.house_no** [fact] dob_now row 37 house_no: 1940 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/house_no`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-job_description"></a>

**dob_now.37.job_description** [fact] dob_now row 37 job_description: INSTALLATION OF 53.46 KW SOLAR ENERGY SYSTEM ON ROOF. NO CHANGE OF OCCUPANCY, USE OR EGRESS. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/job_description`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-job_filing_number"></a>

**dob_now.37.job_filing_number** [fact] dob_now row 37 job_filing_number: X01211421-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/job_filing_number`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-job_type"></a>

**dob_now.37.job_type** [fact] dob_now row 37 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/job_type`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-37-street_name"></a>

**dob_now.37.street_name** [fact] dob_now row 37 street_name: JEROME AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/37/street_name`; SHA256 `4c16570cefb62406a3d59c8f47f9f5d658b60def961ace1e1263cda613719694`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="hpd_violations-returned_rows"></a>

**hpd_violations.returned_rows** [calculation] hpd_violations returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [hpd_violations raw response](sources/hpd_violations.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/wvxf-dwi5.json?%24where=bbl%3D%272028530012%27&%24select=bbl%2Cviolationid%2Cinspectiondate%2Cclass%2Cviolationstatus%2Ccurrentstatus%2Cnovdescription%2Cbin&%24order=violationid&%24limit=501).

Bounded query; see truncation and source limits.

<a id="unknown-current_use"></a>

**unknown.current_use** [unknown] current_use: None (unknown)

Current occupancy, leases, lawful use and displacement implications are not established by these records.

<a id="unknown-title"></a>

**unknown.title** [unknown] title: None (unknown)

Title, site control and owner willingness have not been investigated.

<a id="unknown-entitlement"></a>

**unknown.entitlement** [unknown] entitlement: None (unknown)

Applicable zoning text, special districts, amendments, approvals and legal capacity are not determined.

<a id="unknown-physical_fit"></a>

**unknown.physical_fit** [unknown] physical_fit: None (unknown)

Survey, envelope, access, egress, layouts and geotechnical fit are not validated.

<a id="unknown-environment"></a>

**unknown.environment** [unknown] environment: None (unknown)

Environmental requirements, studies and satisfaction status have not been reconciled.

<a id="unknown-finance"></a>

**unknown.finance** [unknown] finance: None (unknown)

Complete development cost, affordability program, capital sources and commitments are not modeled.

<a id="unknown-transit"></a>

**unknown.transit** [unknown] transit: None (unknown)

Walked access, service reliability, accessibility and job access are not modeled.

<a id="unknown-process_coverage"></a>

**unknown.process_coverage** [unknown] process_coverage: None (unknown)

This is a partial playbook. The complete practitioner process and all material requirements are not known.

<a id="review-housing_signals"></a>

**review.housing_signals** [judgment] Reconcile heterogeneous housing evidence: reconciliation_needed (unreviewed author policy)

Depends on: [dob_now.0.proposed_dwelling_units](#dob_now-0-proposed_dwelling_units), [dob_now.1.proposed_dwelling_units](#dob_now-1-proposed_dwelling_units), [dob_now.2.proposed_dwelling_units](#dob_now-2-proposed_dwelling_units), [dob_now.3.proposed_dwelling_units](#dob_now-3-proposed_dwelling_units), [dob_now.4.proposed_dwelling_units](#dob_now-4-proposed_dwelling_units), [dob_now.5.proposed_dwelling_units](#dob_now-5-proposed_dwelling_units), [dob_now.6.proposed_dwelling_units](#dob_now-6-proposed_dwelling_units), [dob_now.7.proposed_dwelling_units](#dob_now-7-proposed_dwelling_units), [dob_now.8.proposed_dwelling_units](#dob_now-8-proposed_dwelling_units), [dob_now.9.proposed_dwelling_units](#dob_now-9-proposed_dwelling_units), [dob_now.10.proposed_dwelling_units](#dob_now-10-proposed_dwelling_units), [dob_now.11.proposed_dwelling_units](#dob_now-11-proposed_dwelling_units), [dob_now.12.proposed_dwelling_units](#dob_now-12-proposed_dwelling_units), [dob_now.13.proposed_dwelling_units](#dob_now-13-proposed_dwelling_units), [dob_now.14.proposed_dwelling_units](#dob_now-14-proposed_dwelling_units), [dob_now.15.proposed_dwelling_units](#dob_now-15-proposed_dwelling_units), [dob_now.16.proposed_dwelling_units](#dob_now-16-proposed_dwelling_units), [dob_now.21.proposed_dwelling_units](#dob_now-21-proposed_dwelling_units), [dob_now.22.existing_dwelling_units](#dob_now-22-existing_dwelling_units), [dob_now.22.proposed_dwelling_units](#dob_now-22-proposed_dwelling_units), [dob_now.23.existing_dwelling_units](#dob_now-23-existing_dwelling_units), [dob_now.23.proposed_dwelling_units](#dob_now-23-proposed_dwelling_units), [dob_now.24.existing_dwelling_units](#dob_now-24-existing_dwelling_units), [dob_now.24.proposed_dwelling_units](#dob_now-24-proposed_dwelling_units), [dob_now.25.existing_dwelling_units](#dob_now-25-existing_dwelling_units), [dob_now.25.proposed_dwelling_units](#dob_now-25-proposed_dwelling_units), [dob_now.26.existing_dwelling_units](#dob_now-26-existing_dwelling_units), [dob_now.26.proposed_dwelling_units](#dob_now-26-proposed_dwelling_units), [dob_now.27.proposed_dwelling_units](#dob_now-27-proposed_dwelling_units), [dob_now.28.proposed_dwelling_units](#dob_now-28-proposed_dwelling_units), [dob_now.29.proposed_dwelling_units](#dob_now-29-proposed_dwelling_units), [dob_now.30.proposed_dwelling_units](#dob_now-30-proposed_dwelling_units), [dob_now.31.proposed_dwelling_units](#dob_now-31-proposed_dwelling_units), [dob_now.32.proposed_dwelling_units](#dob_now-32-proposed_dwelling_units), [dob_now.33.proposed_dwelling_units](#dob_now-33-proposed_dwelling_units), [dob_now.34.proposed_dwelling_units](#dob_now-34-proposed_dwelling_units), [dob_now.35.proposed_dwelling_units](#dob_now-35-proposed_dwelling_units), [dob_now.36.proposed_dwelling_units](#dob_now-36-proposed_dwelling_units), [pluto.0.unitsres](#pluto-0-unitsres).

DOB historical existing/proposed units and PLUTO recorded units are different observations. Preserve all positive signals; obtain approved plans, certificates and current-use evidence before concluding occupancy or displacement. No units are summed across filings.

<a id="review-next_diligence"></a>

**review.next_diligence** [judgment] Questions for practitioner review: Review current-use evidence, entitlement pathway, physical constraints and capital structure. (unreviewed author policy)

Depends on: [unknown.current_use](#unknown-current_use), [unknown.entitlement](#unknown-entitlement), [unknown.physical_fit](#unknown-physical_fit), [unknown.finance](#unknown-finance).

A checklist for discussion. Task cost, timing, actor resources and best ordering are not evaluated.

<a id="scenario-gross_area_sf"></a>

**scenario.gross_area_sf** [assumption] gross_area_sf: 15000 (gross sf)

Practitioner brief test assumption; not measured capacity or surveyed design.

<a id="scenario-nonresidential_gross_sf"></a>

**scenario.nonresidential_gross_sf** [assumption] nonresidential_gross_sf: 1500 (gross sf)

Practitioner brief test assumption; not measured capacity or surveyed design.

<a id="scenario-residential_net_efficiency"></a>

**scenario.residential_net_efficiency** [assumption] residential_net_efficiency: 0.8 (share)

Practitioner brief test assumption; not measured capacity or surveyed design.

<a id="scenario-average_net_home_sf"></a>

**scenario.average_net_home_sf** [assumption] average_net_home_sf: 800 (net sf per home-equivalent)

Practitioner brief test assumption; not measured capacity or surveyed design.

<a id="scenario-residential_gross_sf"></a>

**scenario.residential_gross_sf** [calculation] Residential gross area allocation: 13500.0 (gross sf)

Depends on: [scenario.gross_area_sf](#scenario-gross_area_sf), [scenario.nonresidential_gross_sf](#scenario-nonresidential_gross_sf).

User-stated area budget; not a verified design or entitlement.

<a id="scenario-residential_net_sf"></a>

**scenario.residential_net_sf** [calculation] Residential net area allowance: 10800.0 (net sf)

Depends on: [scenario.residential_gross_sf](#scenario-residential_gross_sf), [scenario.residential_net_efficiency](#scenario-residential_net_efficiency).

User-stated area budget; not a verified design or entitlement.

<a id="scenario-home_equivalents"></a>

**scenario.home_equivalents** [calculation] Area-budget home-equivalents: 13.5 (home-equivalents; not a feasible unit count)

Depends on: [scenario.residential_net_sf](#scenario-residential_net_sf), [scenario.average_net_home_sf](#scenario-average_net_home_sf).

User-stated area budget; not a verified design or entitlement.

<a id="scenario-gross_to_recorded_lot_ratio"></a>

**scenario.gross_to_recorded_lot_ratio** [calculation] Proposed gross area / recorded lot area: 1.3822336896424623 (gross-to-lot ratio; NOT zoning FAR)

Depends on: [scenario.gross_area_sf](#scenario-gross_area_sf), [pluto.0.lotarea](#pluto-0-lotarea).

User-stated area budget; not a verified design or entitlement.

## Source limits and terms

- **pluto** — Tax-lot attributes may lag actual conditions. Zoning fields are recorded descriptors, not a legal entitlement analysis. Zero recorded residential units does not mean vacancy or no displacement. [Publisher dataset](https://data.cityofnewyork.us/d/64uk-42ks). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **dob_bis** — Legacy job/document rows, not unique projects or verified current use. Historical existing/proposed units are not current lawful dwellings. Exact-BBL queries miss unlinked filings and historical lot changes. [Publisher dataset](https://data.cityofnewyork.us/d/ic3t-wcy2). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **dob_now** — DOB NOW filing rows are not completed projects or a complete pipeline. Exact-BBL lookup only; missing rows do not establish no activity. [Publisher dataset](https://data.cityofnewyork.us/d/w9ak-ipjd). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **hpd_violations** — Recorded housing violation rows, not occupancy, executed evictions, or a displacement measure. Empty results do not prove no housing, no violations, or a safe building. [Publisher dataset](https://data.cityofnewyork.us/d/wvxf-dwi5). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).

## Analysis recipe

Analysis recipe: parcel-area-budget revision 1; SHA256 be800f8bc1639b8cb7ce95c588de5895fdeb00f6d3ff02ce6c014c955b54a56c. Professional review pending.

See recipe.json and trace.json for assumptions, versioned methods, execution order and review gates. The retained evidence-run contains the original source packet; its prior scenario has been replaced in this packet.
