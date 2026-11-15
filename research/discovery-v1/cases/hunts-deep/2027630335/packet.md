# Parcel investigation 2027630335

Discovery follow-up for LAFAYETTE AVENUE (2027630335): reconcile public records, existing-use and historical housing signals, pipeline and the unresolved inputs behind this conditional discovery candidate. Do not infer vacancy, availability, rezoning eligibility or financial feasibility.

**Partial playbook under development.** This packet preserves evidence and conditional arithmetic; it does not establish site availability, a lawful use, legal capacity, building fit or funded feasibility.

## Read this first

**Evidence origin:** Live collection was invoked for this run; inspect each source status below.

Execution metadata: [execution.json](execution.json). Raw-source retrieval dates: [receipts.json](receipts.json). Retrieval is not a field-observation date or a guarantee of current conditions.

**Source retrieval range (UTC):** 2026-11-09T20:02:51.165519+00:00 through 2026-11-09T20:02:51.165945+00:00.

**PLUTO row vintage:** 26v2 — [pluto row 0 version](#pluto-0-version).

**Coverage flags:** no adapter failures recorded; no row-cap truncation recorded. Successful bounded queries are not proof of complete history.

### What these records support

- Recorded address: LAFAYETTE AVENUE — [pluto row 0 address](#pluto-0-address).
- Recorded lot area: 55000 — [pluto row 0 lotarea](#pluto-0-lotarea).
- Recorded residential units: 0 — [pluto row 0 unitsres](#pluto-0-unitsres).
- Recorded primary zoning: M1-2 — [pluto row 0 zonedist1](#pluto-0-zonedist1).

### Supplied assumptions and conditional result

- No area assumptions were supplied. Evidence-only output does not invent a development program.

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
| pluto | ok | 1 | False | 2026-11-09T20:02:51.165741+00:00 |
| dob_bis | ok | 9 | False | 2026-11-09T20:02:51.165519+00:00 |
| dob_now | ok | 5 | False | 2026-11-09T20:02:51.165945+00:00 |
| hpd_violations | ok | 0 | False | 2026-11-09T20:02:51.165907+00:00 |

A failed request is missing evidence, not zero records. Counts describe returned rows, not unique projects. Empty exact-BBL results do not establish no housing, no violations or no activity.

## Recorded parcel facts

- Recorded address: LAFAYETTE AVENUE — [source](#pluto-0-address)
- Tax-lot BBL: 2027630335.00000000 — [source](#pluto-0-bbl)
- Recorded building area (sf): 0 — [source](#pluto-0-bldgarea)
- Recorded building class: G7 — [source](#pluto-0-bldgclass)
- block: 2763 — [source](#pluto-0-block)
- borough: BX — [source](#pluto-0-borough)
- Recorded built FAR: 0.00000000000 — [source](#pluto-0-builtfar)
- Recorded environmental designation: E-210 — [source](#pluto-0-edesignum)
- Recorded irregular-lot flag: True — [source](#pluto-0-irrlotcode)
- landuse: 10 — [source](#pluto-0-landuse)
- latitude: 40.8164530 — [source](#pluto-0-latitude)
- longitude: -73.8846697 — [source](#pluto-0-longitude)
- lot: 335 — [source](#pluto-0-lot)
- Recorded lot area (sf): 55000 — [source](#pluto-0-lotarea)
- Recorded residential FAR (legal applicability unreviewed): 0.00000000000 — [source](#pluto-0-residfar)
- Recorded special district: HP — [source](#pluto-0-spdist1)
- Recorded residential units: 0 — [source](#pluto-0-unitsres)
- Recorded total units: 0 — [source](#pluto-0-unitstotal)
- Dataset row version: 26v2 — [source](#pluto-0-version)
- Recorded primary zoning district: M1-2 — [source](#pluto-0-zonedist1)

## Historical housing signals requiring reconciliation

No positive dwelling-unit signal was extracted from the returned DOB rows. This does not establish absence of housing; review collection status, truncation and missing history.

## Scenario and calculation steps

No scenario supplied; the workflow produced evidence without inventing assumptions or a home count.

## Unknowns and next questions

- **No development scenario supplied**: Evidence gathering is useful without inventing a building program.
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

Source: [pluto raw response](sources/pluto.json), JSON pointer `/`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

Bounded query; see truncation and source limits.

<a id="pluto-0-address"></a>

**pluto.0.address** [fact] pluto row 0 address: LAFAYETTE AVENUE (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/address`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bbl"></a>

**pluto.0.bbl** [fact] pluto row 0 bbl: 2027630335.00000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bbl`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgarea"></a>

**pluto.0.bldgarea** [fact] pluto row 0 bldgarea: 0 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgarea`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgclass"></a>

**pluto.0.bldgclass** [fact] pluto row 0 bldgclass: G7 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgclass`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-block"></a>

**pluto.0.block** [fact] pluto row 0 block: 2763 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/block`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-borough"></a>

**pluto.0.borough** [fact] pluto row 0 borough: BX (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/borough`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-builtfar"></a>

**pluto.0.builtfar** [fact] pluto row 0 builtfar: 0.00000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/builtfar`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-edesignum"></a>

**pluto.0.edesignum** [fact] pluto row 0 edesignum: E-210 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/edesignum`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-irrlotcode"></a>

**pluto.0.irrlotcode** [fact] pluto row 0 irrlotcode: True (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/irrlotcode`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-landuse"></a>

**pluto.0.landuse** [fact] pluto row 0 landuse: 10 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/landuse`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-latitude"></a>

**pluto.0.latitude** [fact] pluto row 0 latitude: 40.8164530 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/latitude`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-longitude"></a>

**pluto.0.longitude** [fact] pluto row 0 longitude: -73.8846697 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/longitude`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lot"></a>

**pluto.0.lot** [fact] pluto row 0 lot: 335 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lot`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lotarea"></a>

**pluto.0.lotarea** [fact] pluto row 0 lotarea: 55000 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lotarea`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-residfar"></a>

**pluto.0.residfar** [fact] pluto row 0 residfar: 0.00000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/residfar`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-spdist1"></a>

**pluto.0.spdist1** [fact] pluto row 0 spdist1: HP (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/spdist1`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitsres"></a>

**pluto.0.unitsres** [fact] pluto row 0 unitsres: 0 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitsres`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitstotal"></a>

**pluto.0.unitstotal** [fact] pluto row 0 unitstotal: 0 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitstotal`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-version"></a>

**pluto.0.version** [fact] pluto row 0 version: 26v2 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/version`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-zonedist1"></a>

**pluto.0.zonedist1** [fact] pluto row 0 zonedist1: M1-2 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/zonedist1`; SHA256 `fdf019b5875b5d73da69b932c2d08c0663ef6e4b86b76f3fd2e03df4d388e2ba`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2027630335&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="dob_bis-returned_rows"></a>

**dob_bis.returned_rows** [calculation] dob_bis returned rows in this exact-BBL query: 9 (returned rows; not projects or total population)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

Bounded query; see truncation and source limits.

<a id="dob_bis-0-bbl"></a>

**dob_bis.0.bbl** [fact] dob_bis row 0 bbl: 2027630335 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bbl`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-bin__"></a>

**dob_bis.0.bin__** [fact] dob_bis row 0 bin__: 2130759 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bin__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-doc__"></a>

**dob_bis.0.doc__** [fact] dob_bis row 0 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/doc__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-house__"></a>

**dob_bis.0.house__** [fact] dob_bis row 0 house__: 1340 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/house__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job__"></a>

**dob_bis.0.job__** [fact] dob_bis row 0 job__: 200301477 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_description"></a>

**dob_bis.0.job_description** [fact] dob_bis row 0 job_description: OBTAINING NEW CERTIFICATE OF OCCUPANCY F  OR AUTO WRECKING ESTABLISHMENT AND ERECTING DISMANTLING SHED. SUPERSEDE CO 22024,9105 &amp; 25559 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_description`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_status_descrp"></a>

**dob_bis.0.job_status_descrp** [fact] dob_bis row 0 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_status_descrp`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_type"></a>

**dob_bis.0.job_type** [fact] dob_bis row 0 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_type`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-latest_action_date"></a>

**dob_bis.0.latest_action_date** [fact] dob_bis row 0 latest_action_date: 05/30/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/latest_action_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-pre__filing_date"></a>

**dob_bis.0.pre__filing_date** [fact] dob_bis row 0 pre__filing_date: 12/21/1994 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/pre__filing_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-signoff_date"></a>

**dob_bis.0.signoff_date** [fact] dob_bis row 0 signoff_date: 05/30/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/signoff_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-street_name"></a>

**dob_bis.0.street_name** [fact] dob_bis row 0 street_name: LAFAYETTE AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/street_name`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bbl"></a>

**dob_bis.1.bbl** [fact] dob_bis row 1 bbl: 2027630335 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bbl`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bin__"></a>

**dob_bis.1.bin__** [fact] dob_bis row 1 bin__: 2130759 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bin__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-doc__"></a>

**dob_bis.1.doc__** [fact] dob_bis row 1 doc__: 02 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/doc__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-house__"></a>

**dob_bis.1.house__** [fact] dob_bis row 1 house__: 1340 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/house__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job__"></a>

**dob_bis.1.job__** [fact] dob_bis row 1 job__: 200301477 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_description"></a>

**dob_bis.1.job_description** [fact] dob_bis row 1 job_description: ADDING PLUMBING WORK TYPE. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_description`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_status_descrp"></a>

**dob_bis.1.job_status_descrp** [fact] dob_bis row 1 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_status_descrp`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_type"></a>

**dob_bis.1.job_type** [fact] dob_bis row 1 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_type`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-latest_action_date"></a>

**dob_bis.1.latest_action_date** [fact] dob_bis row 1 latest_action_date: 05/30/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/latest_action_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-pre__filing_date"></a>

**dob_bis.1.pre__filing_date** [fact] dob_bis row 1 pre__filing_date: 02/06/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/pre__filing_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-signoff_date"></a>

**dob_bis.1.signoff_date** [fact] dob_bis row 1 signoff_date: 05/30/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/signoff_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-street_name"></a>

**dob_bis.1.street_name** [fact] dob_bis row 1 street_name: LAFAYETTE AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/street_name`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-bbl"></a>

**dob_bis.2.bbl** [fact] dob_bis row 2 bbl: 2027630335 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/bbl`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-bin__"></a>

**dob_bis.2.bin__** [fact] dob_bis row 2 bin__: 2130759 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/bin__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-doc__"></a>

**dob_bis.2.doc__** [fact] dob_bis row 2 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/doc__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-house__"></a>

**dob_bis.2.house__** [fact] dob_bis row 2 house__: 1340 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/house__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job__"></a>

**dob_bis.2.job__** [fact] dob_bis row 2 job__: 200820914 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_status_descrp"></a>

**dob_bis.2.job_status_descrp** [fact] dob_bis row 2 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_status_descrp`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_type"></a>

**dob_bis.2.job_type** [fact] dob_bis row 2 job_type: DM (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_type`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-latest_action_date"></a>

**dob_bis.2.latest_action_date** [fact] dob_bis row 2 latest_action_date: 04/29/2005 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/latest_action_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-pre__filing_date"></a>

**dob_bis.2.pre__filing_date** [fact] dob_bis row 2 pre__filing_date: 12/16/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/pre__filing_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-signoff_date"></a>

**dob_bis.2.signoff_date** [fact] dob_bis row 2 signoff_date: 04/29/2005 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/signoff_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-street_name"></a>

**dob_bis.2.street_name** [fact] dob_bis row 2 street_name: LAFAYETTE AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/street_name`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-bbl"></a>

**dob_bis.3.bbl** [fact] dob_bis row 3 bbl: 2027630335 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/bbl`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-bin__"></a>

**dob_bis.3.bin__** [fact] dob_bis row 3 bin__: 2130759 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/bin__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-doc__"></a>

**dob_bis.3.doc__** [fact] dob_bis row 3 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/doc__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-house__"></a>

**dob_bis.3.house__** [fact] dob_bis row 3 house__: 1340 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/house__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job__"></a>

**dob_bis.3.job__** [fact] dob_bis row 3 job__: 200983668 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_status_descrp"></a>

**dob_bis.3.job_status_descrp** [fact] dob_bis row 3 job_status_descrp: PLAN EXAM - APPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_status_descrp`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_type"></a>

**dob_bis.3.job_type** [fact] dob_bis row 3 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_type`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-latest_action_date"></a>

**dob_bis.3.latest_action_date** [fact] dob_bis row 3 latest_action_date: 07/13/2005 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/latest_action_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-pre__filing_date"></a>

**dob_bis.3.pre__filing_date** [fact] dob_bis row 3 pre__filing_date: 07/13/2005 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/pre__filing_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-street_name"></a>

**dob_bis.3.street_name** [fact] dob_bis row 3 street_name: LAFAYETTE AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/street_name`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-bbl"></a>

**dob_bis.4.bbl** [fact] dob_bis row 4 bbl: 2027630335 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/bbl`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-bin__"></a>

**dob_bis.4.bin__** [fact] dob_bis row 4 bin__: 2130759 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/bin__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-doc__"></a>

**dob_bis.4.doc__** [fact] dob_bis row 4 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/doc__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-existing_dwelling_units"></a>

**dob_bis.4.existing_dwelling_units** [fact] dob_bis row 4 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/existing_dwelling_units`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-house__"></a>

**dob_bis.4.house__** [fact] dob_bis row 4 house__: 743 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/house__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job__"></a>

**dob_bis.4.job__** [fact] dob_bis row 4 job__: 201085921 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_status_descrp"></a>

**dob_bis.4.job_status_descrp** [fact] dob_bis row 4 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_status_descrp`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_type"></a>

**dob_bis.4.job_type** [fact] dob_bis row 4 job_type: NB (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_type`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-latest_action_date"></a>

**dob_bis.4.latest_action_date** [fact] dob_bis row 4 latest_action_date: 11/23/2010 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/latest_action_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-pre__filing_date"></a>

**dob_bis.4.pre__filing_date** [fact] dob_bis row 4 pre__filing_date: 10/27/2006 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/pre__filing_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-proposed_dwelling_units"></a>

**dob_bis.4.proposed_dwelling_units** [fact] dob_bis row 4 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/proposed_dwelling_units`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-street_name"></a>

**dob_bis.4.street_name** [fact] dob_bis row 4 street_name: WHITTIER STREET (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/street_name`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-bbl"></a>

**dob_bis.5.bbl** [fact] dob_bis row 5 bbl: 2027630335 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/bbl`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-bin__"></a>

**dob_bis.5.bin__** [fact] dob_bis row 5 bin__: 2130759 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/bin__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-doc__"></a>

**dob_bis.5.doc__** [fact] dob_bis row 5 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/doc__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-house__"></a>

**dob_bis.5.house__** [fact] dob_bis row 5 house__: 743 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/house__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job__"></a>

**dob_bis.5.job__** [fact] dob_bis row 5 job__: 210025300 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_description"></a>

**dob_bis.5.job_description** [fact] dob_bis row 5 job_description: FILING FOR APPROVAL OF BUILDERS PAVEMENT PLAN (BPP) FILING IN CONJUNCTIO N WITH APPLICATIO 201085921  LINEAR FT 200.0 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_description`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_status_descrp"></a>

**dob_bis.5.job_status_descrp** [fact] dob_bis row 5 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_status_descrp`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_type"></a>

**dob_bis.5.job_type** [fact] dob_bis row 5 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_type`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-latest_action_date"></a>

**dob_bis.5.latest_action_date** [fact] dob_bis row 5 latest_action_date: 10/06/2008 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/latest_action_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-pre__filing_date"></a>

**dob_bis.5.pre__filing_date** [fact] dob_bis row 5 pre__filing_date: 11/30/2007 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/pre__filing_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-street_name"></a>

**dob_bis.5.street_name** [fact] dob_bis row 5 street_name: WHITTIER STREET (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/street_name`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-bbl"></a>

**dob_bis.6.bbl** [fact] dob_bis row 6 bbl: 2027630335 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/bbl`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-bin__"></a>

**dob_bis.6.bin__** [fact] dob_bis row 6 bin__: 2130759 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/bin__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-doc__"></a>

**dob_bis.6.doc__** [fact] dob_bis row 6 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/doc__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-house__"></a>

**dob_bis.6.house__** [fact] dob_bis row 6 house__: 743 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/house__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job__"></a>

**dob_bis.6.job__** [fact] dob_bis row 6 job__: 220519954 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_description"></a>

**dob_bis.6.job_description** [fact] dob_bis row 6 job_description: RESTORATION OF 8' &amp; 10' PERIMETER CHAIN LINK FENCE AT THE PROPERTY, AND RESOLVE PENDING ECB VIOLATION 34832691L (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_description`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_status_descrp"></a>

**dob_bis.6.job_status_descrp** [fact] dob_bis row 6 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_status_descrp`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_type"></a>

**dob_bis.6.job_type** [fact] dob_bis row 6 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_type`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-latest_action_date"></a>

**dob_bis.6.latest_action_date** [fact] dob_bis row 6 latest_action_date: 03/17/2016 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/latest_action_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-pre__filing_date"></a>

**dob_bis.6.pre__filing_date** [fact] dob_bis row 6 pre__filing_date: 03/10/2016 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/pre__filing_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-street_name"></a>

**dob_bis.6.street_name** [fact] dob_bis row 6 street_name: WHITTIER STREET (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/street_name`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-bbl"></a>

**dob_bis.7.bbl** [fact] dob_bis row 7 bbl: 2027630335 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/bbl`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-bin__"></a>

**dob_bis.7.bin__** [fact] dob_bis row 7 bin__: 2130759 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/bin__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-doc__"></a>

**dob_bis.7.doc__** [fact] dob_bis row 7 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/doc__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-existing_dwelling_units"></a>

**dob_bis.7.existing_dwelling_units** [fact] dob_bis row 7 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/existing_dwelling_units`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-house__"></a>

**dob_bis.7.house__** [fact] dob_bis row 7 house__: 743 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/house__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job__"></a>

**dob_bis.7.job__** [fact] dob_bis row 7 job__: 220735079 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_status_descrp"></a>

**dob_bis.7.job_status_descrp** [fact] dob_bis row 7 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_status_descrp`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_type"></a>

**dob_bis.7.job_type** [fact] dob_bis row 7 job_type: DM (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_type`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-latest_action_date"></a>

**dob_bis.7.latest_action_date** [fact] dob_bis row 7 latest_action_date: 07/15/2021 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/latest_action_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-pre__filing_date"></a>

**dob_bis.7.pre__filing_date** [fact] dob_bis row 7 pre__filing_date: 10/09/2020 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/pre__filing_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-signoff_date"></a>

**dob_bis.7.signoff_date** [fact] dob_bis row 7 signoff_date: 07/15/2021 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/signoff_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-street_name"></a>

**dob_bis.7.street_name** [fact] dob_bis row 7 street_name: WHITTIER STREET (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/street_name`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-bbl"></a>

**dob_bis.8.bbl** [fact] dob_bis row 8 bbl: 2027630335 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/bbl`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-bin__"></a>

**dob_bis.8.bin__** [fact] dob_bis row 8 bin__: 2130759 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/bin__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-doc__"></a>

**dob_bis.8.doc__** [fact] dob_bis row 8 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/doc__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-house__"></a>

**dob_bis.8.house__** [fact] dob_bis row 8 house__: 1340 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/house__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job__"></a>

**dob_bis.8.job__** [fact] dob_bis row 8 job__: 240287505 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job__`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job_description"></a>

**dob_bis.8.job_description** [fact] dob_bis row 8 job_description: FILING HEREWITH ALTERATION I FOR PARKING LOT IMPROVEMENTS AND TO AMEND CO (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job_description`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job_status_descrp"></a>

**dob_bis.8.job_status_descrp** [fact] dob_bis row 8 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job_status_descrp`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job_type"></a>

**dob_bis.8.job_type** [fact] dob_bis row 8 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job_type`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-latest_action_date"></a>

**dob_bis.8.latest_action_date** [fact] dob_bis row 8 latest_action_date: 11/30/2022 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/latest_action_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-pre__filing_date"></a>

**dob_bis.8.pre__filing_date** [fact] dob_bis row 8 pre__filing_date: 09/23/2020 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/pre__filing_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-signoff_date"></a>

**dob_bis.8.signoff_date** [fact] dob_bis row 8 signoff_date: 11/30/2022 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/signoff_date`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-street_name"></a>

**dob_bis.8.street_name** [fact] dob_bis row 8 street_name: LAFAYETTE AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/street_name`; SHA256 `f04b853e2d6d604430b92d74cf591e2c156e72c2453bd0cca3437095249a1cb9`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_now-returned_rows"></a>

**dob_now.returned_rows** [calculation] dob_now returned rows in this exact-BBL query: 5 (returned rows; not projects or total population)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

Bounded query; see truncation and source limits.

<a id="dob_now-0-bbl"></a>

**dob_now.0.bbl** [fact] dob_now row 0 bbl: 2027630335 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/bbl`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-bin"></a>

**dob_now.0.bin** [fact] dob_now row 0 bin: 2130759 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/bin`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-current_status_date"></a>

**dob_now.0.current_status_date** [fact] dob_now row 0 current_status_date: 2022-05-19T14:12:40.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/current_status_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-existing_dwelling_units"></a>

**dob_now.0.existing_dwelling_units** [fact] dob_now row 0 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/existing_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-filing_date"></a>

**dob_now.0.filing_date** [fact] dob_now row 0 filing_date: 2021-01-08T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/filing_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-filing_status"></a>

**dob_now.0.filing_status** [fact] dob_now row 0 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/filing_status`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-house_no"></a>

**dob_now.0.house_no** [fact] dob_now row 0 house_no: 1340 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/house_no`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-job_description"></a>

**dob_now.0.job_description** [fact] dob_now row 0 job_description: Filing herewith site plumbing plans for the installation of new on-site inlets, conveyance piping and a pipe detention system. Application filed in conjunction with Alteration type I application #240287505. No change in use, egress, or occupancy. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/job_description`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-job_filing_number"></a>

**dob_now.0.job_filing_number** [fact] dob_now row 0 job_filing_number: X00444055-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/job_filing_number`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-job_type"></a>

**dob_now.0.job_type** [fact] dob_now row 0 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/job_type`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-proposed_dwelling_units"></a>

**dob_now.0.proposed_dwelling_units** [fact] dob_now row 0 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/proposed_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-0-street_name"></a>

**dob_now.0.street_name** [fact] dob_now row 0 street_name: LAFAYETTE AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/0/street_name`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-bbl"></a>

**dob_now.1.bbl** [fact] dob_now row 1 bbl: 2027630335 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/bbl`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-bin"></a>

**dob_now.1.bin** [fact] dob_now row 1 bin: 2130759 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/bin`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-current_status_date"></a>

**dob_now.1.current_status_date** [fact] dob_now row 1 current_status_date: 2022-05-19T14:12:59.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/current_status_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-existing_dwelling_units"></a>

**dob_now.1.existing_dwelling_units** [fact] dob_now row 1 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/existing_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-filing_date"></a>

**dob_now.1.filing_date** [fact] dob_now row 1 filing_date: 2021-04-15T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/filing_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-filing_status"></a>

**dob_now.1.filing_status** [fact] dob_now row 1 filing_status: Approved (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/filing_status`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-house_no"></a>

**dob_now.1.house_no** [fact] dob_now row 1 house_no: 1340 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/house_no`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-job_description"></a>

**dob_now.1.job_description** [fact] dob_now row 1 job_description: Filing herewith site plumbing plans for the installation of new on-site inlets, conveyance piping and a pipe detention system. Application filed in conjunction with Alteration type I application #240287505. No change in use, egress, or occupancy. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/job_description`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-job_filing_number"></a>

**dob_now.1.job_filing_number** [fact] dob_now row 1 job_filing_number: X00444055-P1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/job_filing_number`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-job_type"></a>

**dob_now.1.job_type** [fact] dob_now row 1 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/job_type`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-proposed_dwelling_units"></a>

**dob_now.1.proposed_dwelling_units** [fact] dob_now row 1 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/proposed_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-1-street_name"></a>

**dob_now.1.street_name** [fact] dob_now row 1 street_name: LAFAYETTE AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/1/street_name`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-bbl"></a>

**dob_now.2.bbl** [fact] dob_now row 2 bbl: 2027630335 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/bbl`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-bin"></a>

**dob_now.2.bin** [fact] dob_now row 2 bin: 2120378 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/bin`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-current_status_date"></a>

**dob_now.2.current_status_date** [fact] dob_now row 2 current_status_date: 2021-07-12T16:34:23.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/current_status_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-existing_dwelling_units"></a>

**dob_now.2.existing_dwelling_units** [fact] dob_now row 2 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/existing_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-filing_date"></a>

**dob_now.2.filing_date** [fact] dob_now row 2 filing_date: 2021-01-19T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/filing_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-filing_status"></a>

**dob_now.2.filing_status** [fact] dob_now row 2 filing_status: Permit Entire (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/filing_status`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-house_no"></a>

**dob_now.2.house_no** [fact] dob_now row 2 house_no: 743 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/house_no`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-job_description"></a>

**dob_now.2.job_description** [fact] dob_now row 2 job_description: Filing herewith plans for the installation of a temporary construction fence. No change in use, egress, or occupancy. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/job_description`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-job_filing_number"></a>

**dob_now.2.job_filing_number** [fact] dob_now row 2 job_filing_number: X00453887-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/job_filing_number`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-job_type"></a>

**dob_now.2.job_type** [fact] dob_now row 2 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/job_type`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-proposed_dwelling_units"></a>

**dob_now.2.proposed_dwelling_units** [fact] dob_now row 2 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/proposed_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-2-street_name"></a>

**dob_now.2.street_name** [fact] dob_now row 2 street_name: WHITTIER STREET (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/2/street_name`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-bbl"></a>

**dob_now.3.bbl** [fact] dob_now row 3 bbl: 2027630335 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/bbl`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-bin"></a>

**dob_now.3.bin** [fact] dob_now row 3 bin: 2130759 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/bin`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-current_status_date"></a>

**dob_now.3.current_status_date** [fact] dob_now row 3 current_status_date: 2022-05-19T14:13:12.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/current_status_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-existing_dwelling_units"></a>

**dob_now.3.existing_dwelling_units** [fact] dob_now row 3 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/existing_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-filing_date"></a>

**dob_now.3.filing_date** [fact] dob_now row 3 filing_date: 2021-04-09T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/filing_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-filing_status"></a>

**dob_now.3.filing_status** [fact] dob_now row 3 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/filing_status`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-house_no"></a>

**dob_now.3.house_no** [fact] dob_now row 3 house_no: 1340 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/house_no`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-job_description"></a>

**dob_now.3.job_description** [fact] dob_now row 3 job_description: Hereby filing plans for the installation of a 30' Curb Cut. No change in use. egress. or occupancy. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/job_description`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-job_filing_number"></a>

**dob_now.3.job_filing_number** [fact] dob_now row 3 job_filing_number: X00498433-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/job_filing_number`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-job_type"></a>

**dob_now.3.job_type** [fact] dob_now row 3 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/job_type`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-proposed_dwelling_units"></a>

**dob_now.3.proposed_dwelling_units** [fact] dob_now row 3 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/proposed_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-3-street_name"></a>

**dob_now.3.street_name** [fact] dob_now row 3 street_name: LAFAYETTE AVENUE (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/3/street_name`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-bbl"></a>

**dob_now.4.bbl** [fact] dob_now row 4 bbl: 2027630335 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/bbl`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-bin"></a>

**dob_now.4.bin** [fact] dob_now row 4 bin: 2120378 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/bin`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-current_status_date"></a>

**dob_now.4.current_status_date** [fact] dob_now row 4 current_status_date: 2021-07-14T19:28:19.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/current_status_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-existing_dwelling_units"></a>

**dob_now.4.existing_dwelling_units** [fact] dob_now row 4 existing_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/existing_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-filing_date"></a>

**dob_now.4.filing_date** [fact] dob_now row 4 filing_date: 2021-06-03T00:00:00.000 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/filing_date`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-filing_status"></a>

**dob_now.4.filing_status** [fact] dob_now row 4 filing_status: LOC Issued (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/filing_status`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-house_no"></a>

**dob_now.4.house_no** [fact] dob_now row 4 house_no: 743 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/house_no`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-job_description"></a>

**dob_now.4.job_description** [fact] dob_now row 4 job_description: Installation of temporary sidewalk shed per plan submitted. Work shall comply with 2014 building codes chapter 33. No change in use, egress and/or occupancy with this application. (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/job_description`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-job_filing_number"></a>

**dob_now.4.job_filing_number** [fact] dob_now row 4 job_filing_number: X00532898-I1 (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/job_filing_number`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-job_type"></a>

**dob_now.4.job_type** [fact] dob_now row 4 job_type: Alteration (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/job_type`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-proposed_dwelling_units"></a>

**dob_now.4.proposed_dwelling_units** [fact] dob_now row 4 proposed_dwelling_units: 0 (units as recorded; source definition applies)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/proposed_dwelling_units`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="dob_now-4-street_name"></a>

**dob_now.4.street_name** [fact] dob_now row 4 street_name: WHITTIER STREET (source value)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/4/street_name`; SHA256 `fa091b6c417d95fbee8f96d8431eaf892167adad7e43bbcfc08a9ff78c133e16`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

<a id="hpd_violations-returned_rows"></a>

**hpd_violations.returned_rows** [calculation] hpd_violations returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [hpd_violations raw response](sources/hpd_violations.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/wvxf-dwi5.json?%24where=bbl%3D%272027630335%27&%24select=bbl%2Cviolationid%2Cinspectiondate%2Cclass%2Cviolationstatus%2Ccurrentstatus%2Cnovdescription%2Cbin&%24order=violationid&%24limit=501).

Bounded query; see truncation and source limits.

<a id="scenario-unspecified"></a>

**scenario.unspecified** [unknown] No development scenario supplied: None (unknown)

Evidence gathering is useful without inventing a building program.

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
