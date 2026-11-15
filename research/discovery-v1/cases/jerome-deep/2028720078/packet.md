# Parcel investigation 2028720078

Discovery follow-up for 1415 CROMWELL AVENUE (2028720078): reconcile public records, existing-use and historical housing signals, pipeline and the unresolved inputs behind this conditional discovery candidate. Do not infer vacancy, availability, rezoning eligibility or financial feasibility.

**Partial playbook under development.** This packet preserves evidence and conditional arithmetic; it does not establish site availability, a lawful use, legal capacity, building fit or funded feasibility.

## Read this first

**Evidence origin:** Live collection was invoked for this run; inspect each source status below.

Execution metadata: [execution.json](execution.json). Raw-source retrieval dates: [receipts.json](receipts.json). Retrieval is not a field-observation date or a guarantee of current conditions.

**Source retrieval range (UTC):** 2026-11-09T20:02:54.148014+00:00 through 2026-11-09T20:02:54.148424+00:00.

**PLUTO row vintage:** 26v2 — [pluto row 0 version](#pluto-0-version).

**Coverage flags:** no adapter failures recorded; no row-cap truncation recorded. Successful bounded queries are not proof of complete history.

### What these records support

- Recorded address: 1415 CROMWELL AVENUE — [pluto row 0 address](#pluto-0-address).
- Recorded lot area: 12500 — [pluto row 0 lotarea](#pluto-0-lotarea).
- Recorded residential units: 0 — [pluto row 0 unitsres](#pluto-0-unitsres).
- Recorded primary zoning: C8-3 — [pluto row 0 zonedist1](#pluto-0-zonedist1).

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
| pluto | ok | 1 | False | 2026-11-09T20:02:54.148123+00:00 |
| dob_bis | ok | 8 | False | 2026-11-09T20:02:54.148014+00:00 |
| dob_now | ok | 0 | False | 2026-11-09T20:02:54.148255+00:00 |
| hpd_violations | ok | 0 | False | 2026-11-09T20:02:54.148424+00:00 |

A failed request is missing evidence, not zero records. Counts describe returned rows, not unique projects. Empty exact-BBL results do not establish no housing, no violations or no activity.

## Recorded parcel facts

- Recorded address: 1415 CROMWELL AVENUE — [source](#pluto-0-address)
- Tax-lot BBL: 2028720078.00000000 — [source](#pluto-0-bbl)
- Recorded building area (sf): 25000 — [source](#pluto-0-bldgarea)
- Recorded building class: G2 — [source](#pluto-0-bldgclass)
- block: 2872 — [source](#pluto-0-block)
- borough: BX — [source](#pluto-0-borough)
- Recorded built FAR: 2.00000000000 — [source](#pluto-0-builtfar)
- Recorded environmental designation: E-442 — [source](#pluto-0-edesignum)
- Recorded irregular-lot flag: False — [source](#pluto-0-irrlotcode)
- landuse: 7 — [source](#pluto-0-landuse)
- latitude: 40.8414624 — [source](#pluto-0-latitude)
- longitude: -73.9196906 — [source](#pluto-0-longitude)
- lot: 78 — [source](#pluto-0-lot)
- Recorded lot area (sf): 12500 — [source](#pluto-0-lotarea)
- Recorded floor count: 2.0000000 — [source](#pluto-0-numfloors)
- Recorded residential FAR (legal applicability unreviewed): 0.00000000000 — [source](#pluto-0-residfar)
- Recorded residential units: 0 — [source](#pluto-0-unitsres)
- Recorded total units: 1 — [source](#pluto-0-unitstotal)
- Dataset row version: 26v2 — [source](#pluto-0-version)
- Recorded primary zoning district: C8-3 — [source](#pluto-0-zonedist1)
- Recorded second zoning district: R7-1 — [source](#pluto-0-zonedist2)

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

Source: [pluto raw response](sources/pluto.json), JSON pointer `/`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

Bounded query; see truncation and source limits.

<a id="pluto-0-address"></a>

**pluto.0.address** [fact] pluto row 0 address: 1415 CROMWELL AVENUE (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/address`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bbl"></a>

**pluto.0.bbl** [fact] pluto row 0 bbl: 2028720078.00000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bbl`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgarea"></a>

**pluto.0.bldgarea** [fact] pluto row 0 bldgarea: 25000 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgarea`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgclass"></a>

**pluto.0.bldgclass** [fact] pluto row 0 bldgclass: G2 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgclass`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-block"></a>

**pluto.0.block** [fact] pluto row 0 block: 2872 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/block`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-borough"></a>

**pluto.0.borough** [fact] pluto row 0 borough: BX (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/borough`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-builtfar"></a>

**pluto.0.builtfar** [fact] pluto row 0 builtfar: 2.00000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/builtfar`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-edesignum"></a>

**pluto.0.edesignum** [fact] pluto row 0 edesignum: E-442 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/edesignum`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-irrlotcode"></a>

**pluto.0.irrlotcode** [fact] pluto row 0 irrlotcode: False (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/irrlotcode`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-landuse"></a>

**pluto.0.landuse** [fact] pluto row 0 landuse: 7 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/landuse`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-latitude"></a>

**pluto.0.latitude** [fact] pluto row 0 latitude: 40.8414624 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/latitude`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-longitude"></a>

**pluto.0.longitude** [fact] pluto row 0 longitude: -73.9196906 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/longitude`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lot"></a>

**pluto.0.lot** [fact] pluto row 0 lot: 78 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lot`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lotarea"></a>

**pluto.0.lotarea** [fact] pluto row 0 lotarea: 12500 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lotarea`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-numfloors"></a>

**pluto.0.numfloors** [fact] pluto row 0 numfloors: 2.0000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/numfloors`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-residfar"></a>

**pluto.0.residfar** [fact] pluto row 0 residfar: 0.00000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/residfar`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitsres"></a>

**pluto.0.unitsres** [fact] pluto row 0 unitsres: 0 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitsres`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitstotal"></a>

**pluto.0.unitstotal** [fact] pluto row 0 unitstotal: 1 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitstotal`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-version"></a>

**pluto.0.version** [fact] pluto row 0 version: 26v2 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/version`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-zonedist1"></a>

**pluto.0.zonedist1** [fact] pluto row 0 zonedist1: C8-3 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/zonedist1`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-zonedist2"></a>

**pluto.0.zonedist2** [fact] pluto row 0 zonedist2: R7-1 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/zonedist2`; SHA256 `3187de9fff30c6dd64647d5883c356b0e179504b54b994662c02e22bd6b4162b`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028720078&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="dob_bis-returned_rows"></a>

**dob_bis.returned_rows** [calculation] dob_bis returned rows in this exact-BBL query: 8 (returned rows; not projects or total population)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

Bounded query; see truncation and source limits.

<a id="dob_bis-0-bbl"></a>

**dob_bis.0.bbl** [fact] dob_bis row 0 bbl: 2028720078 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bbl`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-bin__"></a>

**dob_bis.0.bin__** [fact] dob_bis row 0 bin__: 2008663 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bin__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-doc__"></a>

**dob_bis.0.doc__** [fact] dob_bis row 0 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/doc__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-house__"></a>

**dob_bis.0.house__** [fact] dob_bis row 0 house__: 1415 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/house__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job__"></a>

**dob_bis.0.job__** [fact] dob_bis row 0 job__: 200163296 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_description"></a>

**dob_bis.0.job_description** [fact] dob_bis row 0 job_description: CHANGE 1ST FLOOR STORAGE GARAGE USE TO CONTRACTOR'S ESTABLISHMENT &amp; WHO LESALE ESTABLISHMENTS; CHANGE 2ND FL. ST ORAGE GARAGE USE TO AUTO BODY SHOP USE; OBTAIN NEW C.O.; INSTALL NEW GAS-FIRED S PACE HEATERS IN EACH ESTABLISHMENT; INS ALL NEW CONCRETE BLOCK &amp; DRYWALL PARTITI ONS. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_description`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_status_descrp"></a>

**dob_bis.0.job_status_descrp** [fact] dob_bis row 0 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_status_descrp`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_type"></a>

**dob_bis.0.job_type** [fact] dob_bis row 0 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_type`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-latest_action_date"></a>

**dob_bis.0.latest_action_date** [fact] dob_bis row 0 latest_action_date: 10/23/1991 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/latest_action_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-pre__filing_date"></a>

**dob_bis.0.pre__filing_date** [fact] dob_bis row 0 pre__filing_date: 10/08/1991 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/pre__filing_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-street_name"></a>

**dob_bis.0.street_name** [fact] dob_bis row 0 street_name: CROMWELL AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/street_name`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bbl"></a>

**dob_bis.1.bbl** [fact] dob_bis row 1 bbl: 2028720078 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bbl`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bin__"></a>

**dob_bis.1.bin__** [fact] dob_bis row 1 bin__: 2008663 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bin__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-doc__"></a>

**dob_bis.1.doc__** [fact] dob_bis row 1 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/doc__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-house__"></a>

**dob_bis.1.house__** [fact] dob_bis row 1 house__: 1415 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/house__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job__"></a>

**dob_bis.1.job__** [fact] dob_bis row 1 job__: 201058470 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_description"></a>

**dob_bis.1.job_description** [fact] dob_bis row 1 job_description: EXISTING STORAGE GARAGE NO CHANGE TO USEOCCUPANCY OR EGRESS. NEW LAYER O F ROOFING ON EXISTING ROOF EXISTING CONCRETE FLOOR SLABS AND CEMENT  FIREPROOFIN G AT FIRST AND SECOND FLOOR SHALL BE PATCHED AND REPLACED WHERE NEEDED. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_description`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_status_descrp"></a>

**dob_bis.1.job_status_descrp** [fact] dob_bis row 1 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_status_descrp`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_type"></a>

**dob_bis.1.job_type** [fact] dob_bis row 1 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_type`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-latest_action_date"></a>

**dob_bis.1.latest_action_date** [fact] dob_bis row 1 latest_action_date: 03/02/2011 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/latest_action_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-pre__filing_date"></a>

**dob_bis.1.pre__filing_date** [fact] dob_bis row 1 pre__filing_date: 06/09/2006 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/pre__filing_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-signoff_date"></a>

**dob_bis.1.signoff_date** [fact] dob_bis row 1 signoff_date: 03/02/2011 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/signoff_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-street_name"></a>

**dob_bis.1.street_name** [fact] dob_bis row 1 street_name: CROMWELL AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/street_name`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-bbl"></a>

**dob_bis.2.bbl** [fact] dob_bis row 2 bbl: 2028720078 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/bbl`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-bin__"></a>

**dob_bis.2.bin__** [fact] dob_bis row 2 bin__: 2008663 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/bin__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-doc__"></a>

**dob_bis.2.doc__** [fact] dob_bis row 2 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/doc__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-house__"></a>

**dob_bis.2.house__** [fact] dob_bis row 2 house__: 1415 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/house__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job__"></a>

**dob_bis.2.job__** [fact] dob_bis row 2 job__: 201075102 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_description"></a>

**dob_bis.2.job_description** [fact] dob_bis row 2 job_description: REVISED SCHEDULE B FOR CORRECTEDFIXTURE COUNT AND REVISED DRAWING P-1 TO REVISE FIXTURE LOCATIONNO CHANGE IN USE OCCUPANCY OR EGRESS (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_description`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_status_descrp"></a>

**dob_bis.2.job_status_descrp** [fact] dob_bis row 2 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_status_descrp`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_type"></a>

**dob_bis.2.job_type** [fact] dob_bis row 2 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_type`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-latest_action_date"></a>

**dob_bis.2.latest_action_date** [fact] dob_bis row 2 latest_action_date: 03/02/2011 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/latest_action_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-pre__filing_date"></a>

**dob_bis.2.pre__filing_date** [fact] dob_bis row 2 pre__filing_date: 08/31/2006 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/pre__filing_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-signoff_date"></a>

**dob_bis.2.signoff_date** [fact] dob_bis row 2 signoff_date: 03/02/2011 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/signoff_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-street_name"></a>

**dob_bis.2.street_name** [fact] dob_bis row 2 street_name: CROMWELL AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/street_name`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-bbl"></a>

**dob_bis.3.bbl** [fact] dob_bis row 3 bbl: 2028720078 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/bbl`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-bin__"></a>

**dob_bis.3.bin__** [fact] dob_bis row 3 bin__: 2008663 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/bin__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-doc__"></a>

**dob_bis.3.doc__** [fact] dob_bis row 3 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/doc__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-house__"></a>

**dob_bis.3.house__** [fact] dob_bis row 3 house__: 1415 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/house__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job__"></a>

**dob_bis.3.job__** [fact] dob_bis row 3 job__: 201091040 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_description"></a>

**dob_bis.3.job_description** [fact] dob_bis row 3 job_description: EXISTING STORAGE NEW CEILING HUNG GASMETERS WITH NEW FLUES MISC. PATC WORK RELATED TO HANGING HEATING UNITS &amp;RUNNING GAS PIPE. REINSTALL GAS SERV. ONE NEW CEILING HUNG AIR CONDITIONER. NOCHANGE IN USE, EGRESS OR OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_description`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_status_descrp"></a>

**dob_bis.3.job_status_descrp** [fact] dob_bis row 3 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_status_descrp`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_type"></a>

**dob_bis.3.job_type** [fact] dob_bis row 3 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_type`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-latest_action_date"></a>

**dob_bis.3.latest_action_date** [fact] dob_bis row 3 latest_action_date: 03/07/2011 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/latest_action_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-pre__filing_date"></a>

**dob_bis.3.pre__filing_date** [fact] dob_bis row 3 pre__filing_date: 11/21/2006 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/pre__filing_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-signoff_date"></a>

**dob_bis.3.signoff_date** [fact] dob_bis row 3 signoff_date: 03/07/2011 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/signoff_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-street_name"></a>

**dob_bis.3.street_name** [fact] dob_bis row 3 street_name: CROMWELL AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/street_name`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-bbl"></a>

**dob_bis.4.bbl** [fact] dob_bis row 4 bbl: 2028720078 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/bbl`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-bin__"></a>

**dob_bis.4.bin__** [fact] dob_bis row 4 bin__: 2008663 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/bin__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-doc__"></a>

**dob_bis.4.doc__** [fact] dob_bis row 4 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/doc__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-house__"></a>

**dob_bis.4.house__** [fact] dob_bis row 4 house__: 1415 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/house__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job__"></a>

**dob_bis.4.job__** [fact] dob_bis row 4 job__: 201092539 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_description"></a>

**dob_bis.4.job_description** [fact] dob_bis row 4 job_description: Herewith filing for a new sprinkler system and a new four-inch sprinkler water service (water service piping).  There is no change in use, egress or occupancy under this application. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_description`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_status_descrp"></a>

**dob_bis.4.job_status_descrp** [fact] dob_bis row 4 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_status_descrp`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_type"></a>

**dob_bis.4.job_type** [fact] dob_bis row 4 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_type`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-latest_action_date"></a>

**dob_bis.4.latest_action_date** [fact] dob_bis row 4 latest_action_date: 08/24/2012 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/latest_action_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-pre__filing_date"></a>

**dob_bis.4.pre__filing_date** [fact] dob_bis row 4 pre__filing_date: 11/29/2006 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/pre__filing_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-signoff_date"></a>

**dob_bis.4.signoff_date** [fact] dob_bis row 4 signoff_date: 08/24/2012 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/signoff_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-street_name"></a>

**dob_bis.4.street_name** [fact] dob_bis row 4 street_name: CROMWELL AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/street_name`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-bbl"></a>

**dob_bis.5.bbl** [fact] dob_bis row 5 bbl: 2028720078 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/bbl`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-bin__"></a>

**dob_bis.5.bin__** [fact] dob_bis row 5 bin__: 2008663 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/bin__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-doc__"></a>

**dob_bis.5.doc__** [fact] dob_bis row 5 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/doc__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-house__"></a>

**dob_bis.5.house__** [fact] dob_bis row 5 house__: 1415 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/house__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job__"></a>

**dob_bis.5.job__** [fact] dob_bis row 5 job__: 201106329 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_description"></a>

**dob_bis.5.job_description** [fact] dob_bis row 5 job_description: EXISTING STORAGE GARAGE NO CHANGE TO USEOR OCCUPANCY OR EGRESS.NEW OIL SEPARATOR &amp; TRECH DRAIN INSTALLATION NEWTAIL PIPE EXHAUST SYSTEM AND VENTILATION WORK. RELATED WALL AND FLOOR REQUIREDPATCH WORK. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_description`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_status_descrp"></a>

**dob_bis.5.job_status_descrp** [fact] dob_bis row 5 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_status_descrp`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_type"></a>

**dob_bis.5.job_type** [fact] dob_bis row 5 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_type`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-latest_action_date"></a>

**dob_bis.5.latest_action_date** [fact] dob_bis row 5 latest_action_date: 04/26/2013 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/latest_action_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-pre__filing_date"></a>

**dob_bis.5.pre__filing_date** [fact] dob_bis row 5 pre__filing_date: 02/07/2007 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/pre__filing_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-street_name"></a>

**dob_bis.5.street_name** [fact] dob_bis row 5 street_name: CROMWELL AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/street_name`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-bbl"></a>

**dob_bis.6.bbl** [fact] dob_bis row 6 bbl: 2028720078 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/bbl`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-bin__"></a>

**dob_bis.6.bin__** [fact] dob_bis row 6 bin__: 2008663 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/bin__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-doc__"></a>

**dob_bis.6.doc__** [fact] dob_bis row 6 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/doc__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-house__"></a>

**dob_bis.6.house__** [fact] dob_bis row 6 house__: 1415 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/house__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job__"></a>

**dob_bis.6.job__** [fact] dob_bis row 6 job__: 201130196 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_description"></a>

**dob_bis.6.job_description** [fact] dob_bis row 6 job_description: THIS APPLICATION IS TO ADDRESS THEDETAILS OF THE VENTILATION FOR THE GARAGE AND AUTOMOTIVE REPAIRS, INCONJUNCTION WITH ALT 201106329. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_description`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_status_descrp"></a>

**dob_bis.6.job_status_descrp** [fact] dob_bis row 6 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_status_descrp`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_type"></a>

**dob_bis.6.job_type** [fact] dob_bis row 6 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_type`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-latest_action_date"></a>

**dob_bis.6.latest_action_date** [fact] dob_bis row 6 latest_action_date: 12/22/2014 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/latest_action_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-pre__filing_date"></a>

**dob_bis.6.pre__filing_date** [fact] dob_bis row 6 pre__filing_date: 06/07/2007 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/pre__filing_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-signoff_date"></a>

**dob_bis.6.signoff_date** [fact] dob_bis row 6 signoff_date: 12/22/2014 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/signoff_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-street_name"></a>

**dob_bis.6.street_name** [fact] dob_bis row 6 street_name: CROMWELL AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/street_name`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-bbl"></a>

**dob_bis.7.bbl** [fact] dob_bis row 7 bbl: 2028720078 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/bbl`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-bin__"></a>

**dob_bis.7.bin__** [fact] dob_bis row 7 bin__: 2008663 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/bin__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-doc__"></a>

**dob_bis.7.doc__** [fact] dob_bis row 7 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/doc__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-house__"></a>

**dob_bis.7.house__** [fact] dob_bis row 7 house__: 1415 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/house__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job__"></a>

**dob_bis.7.job__** [fact] dob_bis row 7 job__: 220008943 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job__`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_description"></a>

**dob_bis.7.job_description** [fact] dob_bis row 7 job_description: APPLICATION IS FILED FOR CONVERSION OF EXISTING AUTOMOTIVE STORAGE GARAGE TO AUTO REPAIR &amp; AUTO BODY FACILITY.  NO CHANGE IN EGRESS, BULK.  NO WORK FILED UNDER THIS APPLICATION (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_description`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_status_descrp"></a>

**dob_bis.7.job_status_descrp** [fact] dob_bis row 7 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_status_descrp`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_type"></a>

**dob_bis.7.job_type** [fact] dob_bis row 7 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_type`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-latest_action_date"></a>

**dob_bis.7.latest_action_date** [fact] dob_bis row 7 latest_action_date: 11/13/2013 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/latest_action_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-pre__filing_date"></a>

**dob_bis.7.pre__filing_date** [fact] dob_bis row 7 pre__filing_date: 05/28/2009 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/pre__filing_date`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-street_name"></a>

**dob_bis.7.street_name** [fact] dob_bis row 7 street_name: CROMWELL AVE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/street_name`; SHA256 `d7404eca16b2ff5e1a61886e10bf0d2e17adf54703bca451a99c3a021ceed171`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_now-returned_rows"></a>

**dob_now.returned_rows** [calculation] dob_now returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

Bounded query; see truncation and source limits.

<a id="hpd_violations-returned_rows"></a>

**hpd_violations.returned_rows** [calculation] hpd_violations returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [hpd_violations raw response](sources/hpd_violations.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/wvxf-dwi5.json?%24where=bbl%3D%272028720078%27&%24select=bbl%2Cviolationid%2Cinspectiondate%2Cclass%2Cviolationstatus%2Ccurrentstatus%2Cnovdescription%2Cbin&%24order=violationid&%24limit=501).

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
