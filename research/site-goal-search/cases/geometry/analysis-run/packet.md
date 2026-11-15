# Parcel investigation 2028750045

Selected program area handoff for 2028750045. Which recorded nonhousing lots can accommodate an assumed 40/60/100-home area program under declared density, transit, operating and capital-gap targets? The source search status is matches_declared_targets. Treat all program dimensions as assumptions and retain the separate financial packet.

**Partial playbook under development.** This packet preserves evidence and conditional arithmetic; it does not establish site availability, a lawful use, legal capacity, building fit or funded feasibility.

## Read this first

**Evidence origin:** Cached replay. This step reused retained source responses; it did not query the APIs.

Execution metadata: [execution.json](execution.json). Raw-source retrieval dates: [receipts.json](receipts.json). Retrieval is not a field-observation date or a guarantee of current conditions.

**Source retrieval range (UTC):** 2026-11-10T02:55:44.417262+00:00 through 2026-11-10T02:55:44.417746+00:00.

**PLUTO row vintage:** 26v2 — [pluto row 0 version](#pluto-0-version).

**Coverage flags:** failed: dob_bis; no row-cap truncation recorded. Successful bounded queries are not proof of complete history.

### What these records support

- Recorded address: 1530 UNIVERSITY AVENUE — [pluto row 0 address](#pluto-0-address).
- Recorded lot area: 9750 — [pluto row 0 lotarea](#pluto-0-lotarea).
- Recorded residential units: 0 — [pluto row 0 unitsres](#pluto-0-unitsres).
- Recorded primary zoning: R7-1 — [pluto row 0 zonedist1](#pluto-0-zonedist1).

### Supplied assumptions and conditional result

- 54901.97 gross sf — [gross_area_sf](#scenario-gross_area_sf).
- 5490.197 gross sf — [nonresidential_gross_sf](#scenario-nonresidential_gross_sf).
- 0.85 share — [residential_net_efficiency](#scenario-residential_net_efficiency).
- 700.0 net sf per home-equivalent — [average_net_home_sf](#scenario-average_net_home_sf).
- Conditional area-budget result: 60.00001007142857 home-equivalents — [Area-budget home-equivalents](#scenario-home_equivalents). This does not establish feasible homes, zoning capacity or an affordable program.

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
| pluto | ok | 1 | False | 2026-11-10T02:55:44.417262+00:00 |
| dob_bis | failed | None | False | 2026-11-10T02:55:44.417607+00:00 |
| dob_now | ok | 5 | False | 2026-11-10T02:55:44.417746+00:00 |
| hpd_violations | ok | 0 | False | 2026-11-10T02:55:44.417720+00:00 |

A failed request is missing evidence, not zero records. Counts describe returned rows, not unique projects. Empty exact-BBL results do not establish no housing, no violations or no activity.

## Recorded parcel facts

- Recorded address: 1530 UNIVERSITY AVENUE — [source](#pluto-0-address)
- Tax-lot BBL: 2028750045.00000000 — [source](#pluto-0-bbl)
- Recorded building area (sf): 8840 — [source](#pluto-0-bldgarea)
- Recorded building class: K1 — [source](#pluto-0-bldgclass)
- block: 2875 — [source](#pluto-0-block)
- borough: BX — [source](#pluto-0-borough)
- Recorded built FAR: 0.91000000000 — [source](#pluto-0-builtfar)
- Recorded irregular-lot flag: True — [source](#pluto-0-irrlotcode)
- landuse: 5 — [source](#pluto-0-landuse)
- latitude: 40.8457975 — [source](#pluto-0-latitude)
- longitude: -73.9214564 — [source](#pluto-0-longitude)
- lot: 45 — [source](#pluto-0-lot)
- Recorded lot area (sf): 9750 — [source](#pluto-0-lotarea)
- Recorded floor count: 1.0000000 — [source](#pluto-0-numfloors)
- Recorded residential FAR (legal applicability unreviewed): 3.44000000000 — [source](#pluto-0-residfar)
- Recorded residential units: 0 — [source](#pluto-0-unitsres)
- Recorded total units: 5 — [source](#pluto-0-unitstotal)
- Dataset row version: 26v2 — [source](#pluto-0-version)
- Recorded primary zoning district: R7-1 — [source](#pluto-0-zonedist1)

## Historical housing signals requiring reconciliation

No positive dwelling-unit signal was extracted from the returned DOB rows. This does not establish absence of housing; review collection status, truncation and missing history.

## Scenario and calculation steps

2028750045-h60-p0

| Claim | Value | Unit | Basis |
| --- | --- | --- | --- |
| [gross_area_sf](#scenario-gross_area_sf) | 54901.97 | gross sf | Analyst scenario selected from verified finite search 2028750045-h60-p0. Area assumptions only; no lawful envelope, layout, availability or delivered-home finding. Financial model is retained separately. |
| [nonresidential_gross_sf](#scenario-nonresidential_gross_sf) | 5490.197 | gross sf | Analyst scenario selected from verified finite search 2028750045-h60-p0. Area assumptions only; no lawful envelope, layout, availability or delivered-home finding. Financial model is retained separately. Nonresidential share is 1 minus the explicit residential share of gross. |
| [residential_net_efficiency](#scenario-residential_net_efficiency) | 0.85 | share | Analyst scenario selected from verified finite search 2028750045-h60-p0. Area assumptions only; no lawful envelope, layout, availability or delivered-home finding. Financial model is retained separately. Declared net/residential-gross conversion, not a floor plan. |
| [average_net_home_sf](#scenario-average_net_home_sf) | 700.0 | net sf per home-equivalent | Analyst scenario selected from verified finite search 2028750045-h60-p0. Area assumptions only; no lawful envelope, layout, availability or delivered-home finding. Financial model is retained separately. Net sf per proposed home; the legacy area module reports fractional home-equivalents. |
| [Residential gross area allocation](#scenario-residential_gross_sf) | 49411.773 | gross sf | 54901.97 − 5490.197 |
| [Residential net area allowance](#scenario-residential_net_sf) | 42000.00705 | net sf | 49411.773 × 0.85 |
| [Area-budget home-equivalents](#scenario-home_equivalents) | 60.00001007142857 | home-equivalents; not a feasible unit count | 42000.00705 ÷ 700.0 |
| [Proposed gross area / recorded lot area](#scenario-gross_to_recorded_lot_ratio) | 5.630971282051282 | gross-to-lot ratio; NOT zoning FAR | 54901.97 ÷ 9750 |

Home-equivalents are an area quotient, not a verified count of homes. The gross-to-lot ratio is not zoning FAR. No rents, affordability eligibility, costs or financing commitments are inferred.

## Unknowns and next questions

- **dob_bis evidence unavailable**: TimeoutError: The read operation timed out
- **current_use**: Current occupancy, leases, lawful use and displacement implications are not established by these records.
- **title**: Title, site control and owner willingness have not been investigated.
- **entitlement**: Applicable zoning text, special districts, amendments, approvals and legal capacity are not determined.
- **physical_fit**: Survey, envelope, access, egress, layouts and geotechnical fit are not validated.
- **environment**: Environmental requirements, studies and satisfaction status have not been reconciled.
- **finance**: Complete development cost, affordability program, capital sources and commitments are not modeled.
- **transit**: Walked access, service reliability, accessibility and job access are not modeled.
- **process_coverage**: This is a partial playbook. The complete practitioner process and all material requirements are not known.
- **Questions for practitioner review — unreviewed judgment**: A checklist for discussion. Task cost, timing, actor resources and best ordering are not evaluated.

## Provenance register

Raw responses, retrieval receipts, request inputs, calculation steps and machine-readable claims are included alongside this packet. Retrieval dates are not field observation dates. Citations establish the selected value, not interpretation or complete coverage.

<a id="pluto-returned_rows"></a>

**pluto.returned_rows** [calculation] pluto returned rows in this exact-BBL query: 1 (returned rows; not projects or total population)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

Bounded query; see truncation and source limits.

<a id="pluto-0-address"></a>

**pluto.0.address** [fact] pluto row 0 address: 1530 UNIVERSITY AVENUE (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/address`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bbl"></a>

**pluto.0.bbl** [fact] pluto row 0 bbl: 2028750045.00000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bbl`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgarea"></a>

**pluto.0.bldgarea** [fact] pluto row 0 bldgarea: 8840 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgarea`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgclass"></a>

**pluto.0.bldgclass** [fact] pluto row 0 bldgclass: K1 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgclass`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-block"></a>

**pluto.0.block** [fact] pluto row 0 block: 2875 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/block`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-borough"></a>

**pluto.0.borough** [fact] pluto row 0 borough: BX (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/borough`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-builtfar"></a>

**pluto.0.builtfar** [fact] pluto row 0 builtfar: 0.91000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/builtfar`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-irrlotcode"></a>

**pluto.0.irrlotcode** [fact] pluto row 0 irrlotcode: True (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/irrlotcode`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-landuse"></a>

**pluto.0.landuse** [fact] pluto row 0 landuse: 5 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/landuse`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-latitude"></a>

**pluto.0.latitude** [fact] pluto row 0 latitude: 40.8457975 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/latitude`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-longitude"></a>

**pluto.0.longitude** [fact] pluto row 0 longitude: -73.9214564 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/longitude`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lot"></a>

**pluto.0.lot** [fact] pluto row 0 lot: 45 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lot`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lotarea"></a>

**pluto.0.lotarea** [fact] pluto row 0 lotarea: 9750 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lotarea`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-numfloors"></a>

**pluto.0.numfloors** [fact] pluto row 0 numfloors: 1.0000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/numfloors`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-residfar"></a>

**pluto.0.residfar** [fact] pluto row 0 residfar: 3.44000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/residfar`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitsres"></a>

**pluto.0.unitsres** [fact] pluto row 0 unitsres: 0 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitsres`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitstotal"></a>

**pluto.0.unitstotal** [fact] pluto row 0 unitstotal: 5 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitstotal`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-version"></a>

**pluto.0.version** [fact] pluto row 0 version: 26v2 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/version`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-zonedist1"></a>

**pluto.0.zonedist1** [fact] pluto row 0 zonedist1: R7-1 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/zonedist1`; SHA256 `f8c59a03e27a03950525c826ec483b94c6e6fa2b75328417d83b97972f2f6c14`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028750045&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="source-dob_bis-unknown"></a>

**source.dob_bis.unknown** [unknown] dob_bis evidence unavailable: None (unknown)

TimeoutError: The read operation timed out

<a id="dob_now-returned_rows"></a>

**dob_now.returned_rows** [calculation] dob_now returned rows in this exact-BBL query: 5 (returned rows; not projects or total population)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

Bounded query; see truncation and source limits.

<a id="dob_now-0-bbl"></a>

**dob_now.0.bbl** [fact] dob_now row 0 bbl: 2028750045 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/bbl`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-bin"></a>

**dob_now.0.bin** [fact] dob_now row 0 bin: 2008785 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/bin`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-current_status_date"></a>

**dob_now.0.current_status_date** [fact] dob_now row 0 current_status_date: 2022-07-13T13:39:59.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/current_status_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-existing_dwelling_units"></a>

**dob_now.0.existing_dwelling_units** [fact] dob_now row 0 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/existing_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-filing_date"></a>

**dob_now.0.filing_date** [fact] dob_now row 0 filing_date: 2022-05-09T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/filing_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-filing_status"></a>

**dob_now.0.filing_status** [fact] dob_now row 0 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/filing_status`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-house_no"></a>

**dob_now.0.house_no** [fact] dob_now row 0 house_no: 1530 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/house_no`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-job_description"></a>

**dob_now.0.job_description** [fact] dob_now row 0 job_description: replace 40' of gas piping in the cellar. no change, in use, egress or occupancy (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/job_description`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-job_filing_number"></a>

**dob_now.0.job_filing_number** [fact] dob_now row 0 job_filing_number: X00731819-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/job_filing_number`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-job_type"></a>

**dob_now.0.job_type** [fact] dob_now row 0 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/job_type`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-proposed_dwelling_units"></a>

**dob_now.0.proposed_dwelling_units** [fact] dob_now row 0 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/proposed_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-street_name"></a>

**dob_now.0.street_name** [fact] dob_now row 0 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/street_name`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-bbl"></a>

**dob_now.1.bbl** [fact] dob_now row 1 bbl: 2028750045 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/bbl`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-bin"></a>

**dob_now.1.bin** [fact] dob_now row 1 bin: 2008785 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/bin`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-current_status_date"></a>

**dob_now.1.current_status_date** [fact] dob_now row 1 current_status_date: 2022-06-21T12:27:41.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/current_status_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-existing_dwelling_units"></a>

**dob_now.1.existing_dwelling_units** [fact] dob_now row 1 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/existing_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-filing_date"></a>

**dob_now.1.filing_date** [fact] dob_now row 1 filing_date: 2022-06-17T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/filing_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-filing_status"></a>

**dob_now.1.filing_status** [fact] dob_now row 1 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/filing_status`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-house_no"></a>

**dob_now.1.house_no** [fact] dob_now row 1 house_no: 1530 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/house_no`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-job_description"></a>

**dob_now.1.job_description** [fact] dob_now row 1 job_description: replace 40' of gas piping in the cellar. no change, in use, egress or occupancy (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/job_description`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-job_filing_number"></a>

**dob_now.1.job_filing_number** [fact] dob_now row 1 job_filing_number: X00731819-P1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/job_filing_number`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-job_type"></a>

**dob_now.1.job_type** [fact] dob_now row 1 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/job_type`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-proposed_dwelling_units"></a>

**dob_now.1.proposed_dwelling_units** [fact] dob_now row 1 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/proposed_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-street_name"></a>

**dob_now.1.street_name** [fact] dob_now row 1 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/street_name`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-bbl"></a>

**dob_now.2.bbl** [fact] dob_now row 2 bbl: 2028750045 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/bbl`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-bin"></a>

**dob_now.2.bin** [fact] dob_now row 2 bin: 2008785 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/bin`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-current_status_date"></a>

**dob_now.2.current_status_date** [fact] dob_now row 2 current_status_date: 2022-07-13T13:39:51.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/current_status_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-existing_dwelling_units"></a>

**dob_now.2.existing_dwelling_units** [fact] dob_now row 2 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/existing_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-filing_date"></a>

**dob_now.2.filing_date** [fact] dob_now row 2 filing_date: 2022-07-12T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/filing_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-filing_status"></a>

**dob_now.2.filing_status** [fact] dob_now row 2 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/filing_status`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-house_no"></a>

**dob_now.2.house_no** [fact] dob_now row 2 house_no: 1530 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/house_no`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-job_description"></a>

**dob_now.2.job_description** [fact] dob_now row 2 job_description: replace 40' of gas piping in the cellar. no change, in use, egress or occupancy (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/job_description`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-job_filing_number"></a>

**dob_now.2.job_filing_number** [fact] dob_now row 2 job_filing_number: X00731819-P2 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/job_filing_number`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-job_type"></a>

**dob_now.2.job_type** [fact] dob_now row 2 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/job_type`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-proposed_dwelling_units"></a>

**dob_now.2.proposed_dwelling_units** [fact] dob_now row 2 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/proposed_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-street_name"></a>

**dob_now.2.street_name** [fact] dob_now row 2 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/street_name`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-bbl"></a>

**dob_now.3.bbl** [fact] dob_now row 3 bbl: 2028750045 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/bbl`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-bin"></a>

**dob_now.3.bin** [fact] dob_now row 3 bin: 2008785 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/bin`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-current_status_date"></a>

**dob_now.3.current_status_date** [fact] dob_now row 3 current_status_date: 2026-10-29T09:36:54.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/current_status_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-existing_dwelling_units"></a>

**dob_now.3.existing_dwelling_units** [fact] dob_now row 3 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/existing_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-filing_date"></a>

**dob_now.3.filing_date** [fact] dob_now row 3 filing_date: 2026-10-07T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/filing_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-filing_status"></a>

**dob_now.3.filing_status** [fact] dob_now row 3 filing_status: Plan Examiner Review (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/filing_status`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-house_no"></a>

**dob_now.3.house_no** [fact] dob_now row 3 house_no: 1530 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/house_no`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-job_description"></a>

**dob_now.3.job_description** [fact] dob_now row 3 job_description: REPLACE 2-HR FIRE DAMAGE ON PARTY WALL (EXP. 2) AND SISTER NEW 3 X 10 TO FIRE DAMAGE JOIST. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/job_description`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-job_filing_number"></a>

**dob_now.3.job_filing_number** [fact] dob_now row 3 job_filing_number: X01470163-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/job_filing_number`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-job_type"></a>

**dob_now.3.job_type** [fact] dob_now row 3 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/job_type`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-proposed_dwelling_units"></a>

**dob_now.3.proposed_dwelling_units** [fact] dob_now row 3 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/proposed_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-street_name"></a>

**dob_now.3.street_name** [fact] dob_now row 3 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/street_name`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-bbl"></a>

**dob_now.4.bbl** [fact] dob_now row 4 bbl: 2028750045 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/bbl`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-bin"></a>

**dob_now.4.bin** [fact] dob_now row 4 bin: 2008785 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/bin`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-current_status_date"></a>

**dob_now.4.current_status_date** [fact] dob_now row 4 current_status_date: 2026-10-28T20:07:16.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/current_status_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-existing_dwelling_units"></a>

**dob_now.4.existing_dwelling_units** [fact] dob_now row 4 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/existing_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-filing_date"></a>

**dob_now.4.filing_date** [fact] dob_now row 4 filing_date: 2026-10-06T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/filing_date`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-filing_status"></a>

**dob_now.4.filing_status** [fact] dob_now row 4 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/filing_status`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-house_no"></a>

**dob_now.4.house_no** [fact] dob_now row 4 house_no: 1534 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/house_no`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-job_description"></a>

**dob_now.4.job_description** [fact] dob_now row 4 job_description: SISTER NEW FIRE DAMAGE JOIST FROM FIRE AT 1530 UNIVERSITY AVENUE BRONX NY. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/job_description`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-job_filing_number"></a>

**dob_now.4.job_filing_number** [fact] dob_now row 4 job_filing_number: X01470733-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/job_filing_number`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-job_type"></a>

**dob_now.4.job_type** [fact] dob_now row 4 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/job_type`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-proposed_dwelling_units"></a>

**dob_now.4.proposed_dwelling_units** [fact] dob_now row 4 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/proposed_dwelling_units`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-street_name"></a>

**dob_now.4.street_name** [fact] dob_now row 4 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/street_name`; SHA256 `4dd29a5add4ed31f426bbdd44ea7199faee70d058504438dd118fcea9a82fd82`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="hpd_violations-returned_rows"></a>

**hpd_violations.returned_rows** [calculation] hpd_violations returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [hpd_violations raw response](sources/hpd_violations.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/wvxf-dwi5.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cviolationid%2Cinspectiondate%2Cclass%2Cviolationstatus%2Ccurrentstatus%2Cnovdescription%2Cbin&%24order=violationid&%24limit=501).

Bounded query; see truncation and source limits.

<a id="scenario-gross_area_sf"></a>

**scenario.gross_area_sf** [assumption] gross_area_sf: 54901.97 (gross sf)

Analyst scenario selected from verified finite search 2028750045-h60-p0. Area assumptions only; no lawful envelope, layout, availability or delivered-home finding. Financial model is retained separately.

<a id="scenario-nonresidential_gross_sf"></a>

**scenario.nonresidential_gross_sf** [assumption] nonresidential_gross_sf: 5490.197 (gross sf)

Analyst scenario selected from verified finite search 2028750045-h60-p0. Area assumptions only; no lawful envelope, layout, availability or delivered-home finding. Financial model is retained separately. Nonresidential share is 1 minus the explicit residential share of gross.

<a id="scenario-residential_net_efficiency"></a>

**scenario.residential_net_efficiency** [assumption] residential_net_efficiency: 0.85 (share)

Analyst scenario selected from verified finite search 2028750045-h60-p0. Area assumptions only; no lawful envelope, layout, availability or delivered-home finding. Financial model is retained separately. Declared net/residential-gross conversion, not a floor plan.

<a id="scenario-average_net_home_sf"></a>

**scenario.average_net_home_sf** [assumption] average_net_home_sf: 700.0 (net sf per home-equivalent)

Analyst scenario selected from verified finite search 2028750045-h60-p0. Area assumptions only; no lawful envelope, layout, availability or delivered-home finding. Financial model is retained separately. Net sf per proposed home; the legacy area module reports fractional home-equivalents.

<a id="scenario-residential_gross_sf"></a>

**scenario.residential_gross_sf** [calculation] Residential gross area allocation: 49411.773 (gross sf)

Depends on: [scenario.gross_area_sf](#scenario-gross_area_sf), [scenario.nonresidential_gross_sf](#scenario-nonresidential_gross_sf).

User-stated area budget; not a verified design or entitlement.

<a id="scenario-residential_net_sf"></a>

**scenario.residential_net_sf** [calculation] Residential net area allowance: 42000.00705 (net sf)

Depends on: [scenario.residential_gross_sf](#scenario-residential_gross_sf), [scenario.residential_net_efficiency](#scenario-residential_net_efficiency).

User-stated area budget; not a verified design or entitlement.

<a id="scenario-home_equivalents"></a>

**scenario.home_equivalents** [calculation] Area-budget home-equivalents: 60.00001007142857 (home-equivalents; not a feasible unit count)

Depends on: [scenario.residential_net_sf](#scenario-residential_net_sf), [scenario.average_net_home_sf](#scenario-average_net_home_sf).

User-stated area budget; not a verified design or entitlement.

<a id="scenario-gross_to_recorded_lot_ratio"></a>

**scenario.gross_to_recorded_lot_ratio** [calculation] Proposed gross area / recorded lot area: 5.630971282051282 (gross-to-lot ratio; NOT zoning FAR)

Depends on: [scenario.gross_area_sf](#scenario-gross_area_sf), [pluto.0.lotarea](#pluto-0-lotarea).

User-stated area budget; not a verified design or entitlement.

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

<a id="review-next_diligence"></a>

**review.next_diligence** [judgment] Questions for practitioner review: Review current-use evidence, entitlement pathway, physical constraints and capital structure. (unreviewed author policy)

Depends on: [unknown.current_use](#unknown-current_use), [unknown.entitlement](#unknown-entitlement), [unknown.physical_fit](#unknown-physical_fit), [unknown.finance](#unknown-finance).

A checklist for discussion. Task cost, timing, actor resources and best ordering are not evaluated.

## Source limits and terms

- **pluto** — Tax-lot attributes may lag actual conditions. Zoning fields are recorded descriptors, not a legal entitlement analysis. Zero recorded residential units does not mean vacancy or no displacement. [Publisher dataset](https://data.cityofnewyork.us/d/64uk-42ks). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **dob_bis** — Legacy job/document rows, not unique projects or verified current use. Historical existing/proposed units are not current lawful dwellings. Exact-BBL queries miss unlinked filings and historical lot changes. [Publisher dataset](https://data.cityofnewyork.us/d/ic3t-wcy2). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **dob_now** — DOB NOW filing rows are not completed projects or a complete pipeline. Exact-BBL lookup only; missing rows do not establish no activity. [Publisher dataset](https://data.cityofnewyork.us/d/w9ak-ipjd). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **hpd_violations** — Recorded housing violation rows, not occupancy, executed evictions, or a displacement measure. Empty results do not prove no housing, no violations, or a safe building. [Publisher dataset](https://data.cityofnewyork.us/d/wvxf-dwi5). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
