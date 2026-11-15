# Parcel investigation 2028750045

Nonhousing discovery follow-up for 1530 UNIVERSITY AVENUE (2028750045), general zoning path housing_permitted_by_general_use_rule: reconcile current operations, historical housing signals, zoning exceptions, site control and unresolved constraints. No development program or vacancy finding is supplied.

**Partial playbook under development.** This packet preserves evidence and conditional arithmetic; it does not establish site availability, a lawful use, legal capacity, building fit or funded feasibility.

## Read this first

**Evidence origin:** Live collection was invoked for this run; inspect each source status below.

Execution metadata: [execution.json](execution.json). Raw-source retrieval dates: [receipts.json](receipts.json). Retrieval is not a field-observation date or a guarantee of current conditions.

**Source retrieval range (UTC):** 2026-11-10T03:48:47.836299+00:00 through 2026-11-10T03:48:47.836801+00:00.

**PLUTO row vintage:** 26v2 — [pluto row 0 version](#pluto-0-version).

**Coverage flags:** no adapter failures recorded; no row-cap truncation recorded. Successful bounded queries are not proof of complete history.

### What these records support

- Recorded address: 1530 UNIVERSITY AVENUE — [pluto row 0 address](#pluto-0-address).
- Recorded lot area: 9750 — [pluto row 0 lotarea](#pluto-0-lotarea).
- Recorded residential units: 0 — [pluto row 0 unitsres](#pluto-0-unitsres).
- Recorded primary zoning: R7-1 — [pluto row 0 zonedist1](#pluto-0-zonedist1).

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
| pluto | ok | 1 | False | 2026-11-10T03:48:47.836299+00:00 |
| dob_bis | ok | 26 | False | 2026-11-10T03:48:47.836708+00:00 |
| dob_now | ok | 5 | False | 2026-11-10T03:48:47.836764+00:00 |
| hpd_violations | ok | 0 | False | 2026-11-10T03:48:47.836801+00:00 |

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

<a id="dob_bis-returned_rows"></a>

**dob_bis.returned_rows** [calculation] dob_bis returned rows in this exact-BBL query: 26 (returned rows; not projects or total population)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

Bounded query; see truncation and source limits.

<a id="dob_bis-0-bbl"></a>

**dob_bis.0.bbl** [fact] dob_bis row 0 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-bin__"></a>

**dob_bis.0.bin__** [fact] dob_bis row 0 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-doc__"></a>

**dob_bis.0.doc__** [fact] dob_bis row 0 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-house__"></a>

**dob_bis.0.house__** [fact] dob_bis row 0 house__: 1546 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job__"></a>

**dob_bis.0.job__** [fact] dob_bis row 0 job__: 200263589 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_description"></a>

**dob_bis.0.job_description** [fact] dob_bis row 0 job_description: 1546-48 UNIVERSITY AV: CHANGE FROM TWO - STORES INTO EATING/DRINKING EST WITH ENTERTAINMENT &amp; MUSIC (U.G. 6A/6C)- PARTITIONS WORKS. 1542-44 UNIVERSITY AV.: STORE FRONT AND- MEZZ. PARTITIONS WORKS. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_status_descrp"></a>

**dob_bis.0.job_status_descrp** [fact] dob_bis row 0 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_type"></a>

**dob_bis.0.job_type** [fact] dob_bis row 0 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-latest_action_date"></a>

**dob_bis.0.latest_action_date** [fact] dob_bis row 0 latest_action_date: 06/26/2000 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-pre__filing_date"></a>

**dob_bis.0.pre__filing_date** [fact] dob_bis row 0 pre__filing_date: 07/22/1993 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-signoff_date"></a>

**dob_bis.0.signoff_date** [fact] dob_bis row 0 signoff_date: 06/26/2000 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/signoff_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-street_name"></a>

**dob_bis.0.street_name** [fact] dob_bis row 0 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bbl"></a>

**dob_bis.1.bbl** [fact] dob_bis row 1 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bin__"></a>

**dob_bis.1.bin__** [fact] dob_bis row 1 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-doc__"></a>

**dob_bis.1.doc__** [fact] dob_bis row 1 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-house__"></a>

**dob_bis.1.house__** [fact] dob_bis row 1 house__: 1546 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job__"></a>

**dob_bis.1.job__** [fact] dob_bis row 1 job__: 200272150 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_description"></a>

**dob_bis.1.job_description** [fact] dob_bis row 1 job_description: FILED HEREWITH TO PROPOSED RESTAURANT  - GU6 AT EXIST' STORE UG 6, MINOR PARTITIONS WORK, PL AND MG TO BE DONE AT 1ST FL. AS PER PLANS. NO CHANGE IN USE IN USE GROUP EGRESS OR OCC. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_status_descrp"></a>

**dob_bis.1.job_status_descrp** [fact] dob_bis row 1 job_status_descrp: PERMIT ISSUED - PARTIAL JOB (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_type"></a>

**dob_bis.1.job_type** [fact] dob_bis row 1 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-latest_action_date"></a>

**dob_bis.1.latest_action_date** [fact] dob_bis row 1 latest_action_date: 08/12/1994 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-pre__filing_date"></a>

**dob_bis.1.pre__filing_date** [fact] dob_bis row 1 pre__filing_date: 10/27/1993 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-street_name"></a>

**dob_bis.1.street_name** [fact] dob_bis row 1 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-bbl"></a>

**dob_bis.2.bbl** [fact] dob_bis row 2 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-bin__"></a>

**dob_bis.2.bin__** [fact] dob_bis row 2 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-doc__"></a>

**dob_bis.2.doc__** [fact] dob_bis row 2 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-house__"></a>

**dob_bis.2.house__** [fact] dob_bis row 2 house__: 1546 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job__"></a>

**dob_bis.2.job__** [fact] dob_bis row 2 job__: 200291512 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_description"></a>

**dob_bis.2.job_description** [fact] dob_bis row 2 job_description: REVISE USE OF 1ST. FL. FROM EATING AND -  DRINKING EST. UG 6 TO SOCIAL CLUB UG 6-F4. OBTAIN NEW C.O. NO WORK TO  BE DONE UNDER THIS APPL. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_status_descrp"></a>

**dob_bis.2.job_status_descrp** [fact] dob_bis row 2 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_type"></a>

**dob_bis.2.job_type** [fact] dob_bis row 2 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-latest_action_date"></a>

**dob_bis.2.latest_action_date** [fact] dob_bis row 2 latest_action_date: 09/16/1994 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-pre__filing_date"></a>

**dob_bis.2.pre__filing_date** [fact] dob_bis row 2 pre__filing_date: 09/09/1994 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-street_name"></a>

**dob_bis.2.street_name** [fact] dob_bis row 2 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-bbl"></a>

**dob_bis.3.bbl** [fact] dob_bis row 3 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-bin__"></a>

**dob_bis.3.bin__** [fact] dob_bis row 3 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-doc__"></a>

**dob_bis.3.doc__** [fact] dob_bis row 3 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-house__"></a>

**dob_bis.3.house__** [fact] dob_bis row 3 house__: 1546 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job__"></a>

**dob_bis.3.job__** [fact] dob_bis row 3 job__: 200300539 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_description"></a>

**dob_bis.3.job_description** [fact] dob_bis row 3 job_description: PROPOSED EATING/DRINKING EST. WITH ENTER  TAIMENT OR MUSIC UG 6 AT EXIST RESTAURANT UG 6. FIRE SP HEADS TO BE IN-  STALL NEW C.O. TO BE OBTAINED. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_status_descrp"></a>

**dob_bis.3.job_status_descrp** [fact] dob_bis row 3 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_type"></a>

**dob_bis.3.job_type** [fact] dob_bis row 3 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-latest_action_date"></a>

**dob_bis.3.latest_action_date** [fact] dob_bis row 3 latest_action_date: 12/20/1994 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-pre__filing_date"></a>

**dob_bis.3.pre__filing_date** [fact] dob_bis row 3 pre__filing_date: 12/14/1994 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-street_name"></a>

**dob_bis.3.street_name** [fact] dob_bis row 3 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-bbl"></a>

**dob_bis.4.bbl** [fact] dob_bis row 4 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-bin__"></a>

**dob_bis.4.bin__** [fact] dob_bis row 4 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-doc__"></a>

**dob_bis.4.doc__** [fact] dob_bis row 4 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-house__"></a>

**dob_bis.4.house__** [fact] dob_bis row 4 house__: 1546 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job__"></a>

**dob_bis.4.job__** [fact] dob_bis row 4 job__: 200305669 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_status_descrp"></a>

**dob_bis.4.job_status_descrp** [fact] dob_bis row 4 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_type"></a>

**dob_bis.4.job_type** [fact] dob_bis row 4 job_type: PA (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-latest_action_date"></a>

**dob_bis.4.latest_action_date** [fact] dob_bis row 4 latest_action_date: 02/09/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-pre__filing_date"></a>

**dob_bis.4.pre__filing_date** [fact] dob_bis row 4 pre__filing_date: 02/07/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-street_name"></a>

**dob_bis.4.street_name** [fact] dob_bis row 4 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-bbl"></a>

**dob_bis.5.bbl** [fact] dob_bis row 5 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-bin__"></a>

**dob_bis.5.bin__** [fact] dob_bis row 5 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-doc__"></a>

**dob_bis.5.doc__** [fact] dob_bis row 5 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-house__"></a>

**dob_bis.5.house__** [fact] dob_bis row 5 house__: 1546 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job__"></a>

**dob_bis.5.job__** [fact] dob_bis row 5 job__: 200344092 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_status_descrp"></a>

**dob_bis.5.job_status_descrp** [fact] dob_bis row 5 job_status_descrp: PLAN EXAM - APPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_type"></a>

**dob_bis.5.job_type** [fact] dob_bis row 5 job_type: PA (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-latest_action_date"></a>

**dob_bis.5.latest_action_date** [fact] dob_bis row 5 latest_action_date: 08/31/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-pre__filing_date"></a>

**dob_bis.5.pre__filing_date** [fact] dob_bis row 5 pre__filing_date: 08/17/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-street_name"></a>

**dob_bis.5.street_name** [fact] dob_bis row 5 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-bbl"></a>

**dob_bis.6.bbl** [fact] dob_bis row 6 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-bin__"></a>

**dob_bis.6.bin__** [fact] dob_bis row 6 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-doc__"></a>

**dob_bis.6.doc__** [fact] dob_bis row 6 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-house__"></a>

**dob_bis.6.house__** [fact] dob_bis row 6 house__: 1530 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job__"></a>

**dob_bis.6.job__** [fact] dob_bis row 6 job__: 200344109 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_description"></a>

**dob_bis.6.job_description** [fact] dob_bis row 6 job_description: INSTALL PLUMBING FIXTURES IN CONJUNCTION WITH 200263589. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_status_descrp"></a>

**dob_bis.6.job_status_descrp** [fact] dob_bis row 6 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_type"></a>

**dob_bis.6.job_type** [fact] dob_bis row 6 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-latest_action_date"></a>

**dob_bis.6.latest_action_date** [fact] dob_bis row 6 latest_action_date: 02/23/2000 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-pre__filing_date"></a>

**dob_bis.6.pre__filing_date** [fact] dob_bis row 6 pre__filing_date: 08/17/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-signoff_date"></a>

**dob_bis.6.signoff_date** [fact] dob_bis row 6 signoff_date: 02/23/2000 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/signoff_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-street_name"></a>

**dob_bis.6.street_name** [fact] dob_bis row 6 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-bbl"></a>

**dob_bis.7.bbl** [fact] dob_bis row 7 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-bin__"></a>

**dob_bis.7.bin__** [fact] dob_bis row 7 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-doc__"></a>

**dob_bis.7.doc__** [fact] dob_bis row 7 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-house__"></a>

**dob_bis.7.house__** [fact] dob_bis row 7 house__: 1530 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job__"></a>

**dob_bis.7.job__** [fact] dob_bis row 7 job__: 200345028 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_description"></a>

**dob_bis.7.job_description** [fact] dob_bis row 7 job_description: REPLACEMENT OF EXIST' HOOD. INSTALL EX - TINGUISHING SYSTEM. NO CHANGE I USE EGRESS OCC. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_status_descrp"></a>

**dob_bis.7.job_status_descrp** [fact] dob_bis row 7 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_type"></a>

**dob_bis.7.job_type** [fact] dob_bis row 7 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-latest_action_date"></a>

**dob_bis.7.latest_action_date** [fact] dob_bis row 7 latest_action_date: 02/23/2000 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-pre__filing_date"></a>

**dob_bis.7.pre__filing_date** [fact] dob_bis row 7 pre__filing_date: 08/22/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-signoff_date"></a>

**dob_bis.7.signoff_date** [fact] dob_bis row 7 signoff_date: 02/23/2000 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/signoff_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-street_name"></a>

**dob_bis.7.street_name** [fact] dob_bis row 7 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-bbl"></a>

**dob_bis.8.bbl** [fact] dob_bis row 8 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-bin__"></a>

**dob_bis.8.bin__** [fact] dob_bis row 8 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-doc__"></a>

**dob_bis.8.doc__** [fact] dob_bis row 8 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-house__"></a>

**dob_bis.8.house__** [fact] dob_bis row 8 house__: 1548 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job__"></a>

**dob_bis.8.job__** [fact] dob_bis row 8 job__: 200352812 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job_description"></a>

**dob_bis.8.job_description** [fact] dob_bis row 8 job_description: INSTALATION OF AWNING. (LA ZIMA RESTAURANT) 35' LONG 4' HEIGHT (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job_status_descrp"></a>

**dob_bis.8.job_status_descrp** [fact] dob_bis row 8 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job_type"></a>

**dob_bis.8.job_type** [fact] dob_bis row 8 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-latest_action_date"></a>

**dob_bis.8.latest_action_date** [fact] dob_bis row 8 latest_action_date: 11/17/1999 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-pre__filing_date"></a>

**dob_bis.8.pre__filing_date** [fact] dob_bis row 8 pre__filing_date: 11/08/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-signoff_date"></a>

**dob_bis.8.signoff_date** [fact] dob_bis row 8 signoff_date: 11/17/1999 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/signoff_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-street_name"></a>

**dob_bis.8.street_name** [fact] dob_bis row 8 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-bbl"></a>

**dob_bis.9.bbl** [fact] dob_bis row 9 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-bin__"></a>

**dob_bis.9.bin__** [fact] dob_bis row 9 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-doc__"></a>

**dob_bis.9.doc__** [fact] dob_bis row 9 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-house__"></a>

**dob_bis.9.house__** [fact] dob_bis row 9 house__: 1548 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-job__"></a>

**dob_bis.9.job__** [fact] dob_bis row 9 job__: 200355329 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-job_description"></a>

**dob_bis.9.job_description** [fact] dob_bis row 9 job_description: NEW HVAC SYSTEM WITH ASSOC. DUCT WORK, - STEEL DUNNAGE AND PLUMBING. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-job_status_descrp"></a>

**dob_bis.9.job_status_descrp** [fact] dob_bis row 9 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-job_type"></a>

**dob_bis.9.job_type** [fact] dob_bis row 9 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-latest_action_date"></a>

**dob_bis.9.latest_action_date** [fact] dob_bis row 9 latest_action_date: 05/23/1996 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-pre__filing_date"></a>

**dob_bis.9.pre__filing_date** [fact] dob_bis row 9 pre__filing_date: 12/05/1995 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-street_name"></a>

**dob_bis.9.street_name** [fact] dob_bis row 9 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-bbl"></a>

**dob_bis.10.bbl** [fact] dob_bis row 10 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-bin__"></a>

**dob_bis.10.bin__** [fact] dob_bis row 10 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-doc__"></a>

**dob_bis.10.doc__** [fact] dob_bis row 10 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-house__"></a>

**dob_bis.10.house__** [fact] dob_bis row 10 house__: 1534 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-job__"></a>

**dob_bis.10.job__** [fact] dob_bis row 10 job__: 200399988 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-job_description"></a>

**dob_bis.10.job_description** [fact] dob_bis row 10 job_description: STORE FRONT DOOR RELOCATION AND VEGETABL E AND FISH STORE WITH TAKE OUT FOOD. NO CHANGE IN USE, EGRESS, OR OCCUP ANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-job_status_descrp"></a>

**dob_bis.10.job_status_descrp** [fact] dob_bis row 10 job_status_descrp: PERMIT ISSUED - PARTIAL JOB (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-job_type"></a>

**dob_bis.10.job_type** [fact] dob_bis row 10 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-latest_action_date"></a>

**dob_bis.10.latest_action_date** [fact] dob_bis row 10 latest_action_date: 01/03/1997 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-pre__filing_date"></a>

**dob_bis.10.pre__filing_date** [fact] dob_bis row 10 pre__filing_date: 12/23/1996 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-street_name"></a>

**dob_bis.10.street_name** [fact] dob_bis row 10 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-bbl"></a>

**dob_bis.11.bbl** [fact] dob_bis row 11 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-bin__"></a>

**dob_bis.11.bin__** [fact] dob_bis row 11 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-doc__"></a>

**dob_bis.11.doc__** [fact] dob_bis row 11 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-house__"></a>

**dob_bis.11.house__** [fact] dob_bis row 11 house__: 1534 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-job__"></a>

**dob_bis.11.job__** [fact] dob_bis row 11 job__: 200400217 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-job_description"></a>

**dob_bis.11.job_description** [fact] dob_bis row 11 job_description: WORKS IN CONJUNCTION WITH JOB # 20039998 8. EXTINGUISHING SYSTEM. NO CHANGE IN USE OCCUPANCY OR EGRESS WITH APPLICATION. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-job_status_descrp"></a>

**dob_bis.11.job_status_descrp** [fact] dob_bis row 11 job_status_descrp: PERMIT ISSUED - PARTIAL JOB (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-job_type"></a>

**dob_bis.11.job_type** [fact] dob_bis row 11 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-latest_action_date"></a>

**dob_bis.11.latest_action_date** [fact] dob_bis row 11 latest_action_date: 08/13/1997 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-pre__filing_date"></a>

**dob_bis.11.pre__filing_date** [fact] dob_bis row 11 pre__filing_date: 12/26/1996 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-street_name"></a>

**dob_bis.11.street_name** [fact] dob_bis row 11 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-bbl"></a>

**dob_bis.12.bbl** [fact] dob_bis row 12 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-bin__"></a>

**dob_bis.12.bin__** [fact] dob_bis row 12 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-doc__"></a>

**dob_bis.12.doc__** [fact] dob_bis row 12 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-house__"></a>

**dob_bis.12.house__** [fact] dob_bis row 12 house__: 1546 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-job__"></a>

**dob_bis.12.job__** [fact] dob_bis row 12 job__: 200411642 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-job_status_descrp"></a>

**dob_bis.12.job_status_descrp** [fact] dob_bis row 12 job_status_descrp: PLAN EXAM - APPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-job_type"></a>

**dob_bis.12.job_type** [fact] dob_bis row 12 job_type: PA (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-latest_action_date"></a>

**dob_bis.12.latest_action_date** [fact] dob_bis row 12 latest_action_date: 07/21/1997 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-pre__filing_date"></a>

**dob_bis.12.pre__filing_date** [fact] dob_bis row 12 pre__filing_date: 02/24/1997 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-street_name"></a>

**dob_bis.12.street_name** [fact] dob_bis row 12 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-bbl"></a>

**dob_bis.13.bbl** [fact] dob_bis row 13 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-bin__"></a>

**dob_bis.13.bin__** [fact] dob_bis row 13 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-doc__"></a>

**dob_bis.13.doc__** [fact] dob_bis row 13 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-house__"></a>

**dob_bis.13.house__** [fact] dob_bis row 13 house__: 1530 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-job__"></a>

**dob_bis.13.job__** [fact] dob_bis row 13 job__: 200414453 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-job_description"></a>

**dob_bis.13.job_description** [fact] dob_bis row 13 job_description: KITCHEN EQUIPMENTS AND PLUMBING WORKS IN CONJUNCTION WITH JOB NO. 200263589 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-job_status_descrp"></a>

**dob_bis.13.job_status_descrp** [fact] dob_bis row 13 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-job_type"></a>

**dob_bis.13.job_type** [fact] dob_bis row 13 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-latest_action_date"></a>

**dob_bis.13.latest_action_date** [fact] dob_bis row 13 latest_action_date: 12/03/1999 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-pre__filing_date"></a>

**dob_bis.13.pre__filing_date** [fact] dob_bis row 13 pre__filing_date: 03/11/1997 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-signoff_date"></a>

**dob_bis.13.signoff_date** [fact] dob_bis row 13 signoff_date: 12/03/1999 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/signoff_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-street_name"></a>

**dob_bis.13.street_name** [fact] dob_bis row 13 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-bbl"></a>

**dob_bis.14.bbl** [fact] dob_bis row 14 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-bin__"></a>

**dob_bis.14.bin__** [fact] dob_bis row 14 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-doc__"></a>

**dob_bis.14.doc__** [fact] dob_bis row 14 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-house__"></a>

**dob_bis.14.house__** [fact] dob_bis row 14 house__: 1530 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-job__"></a>

**dob_bis.14.job__** [fact] dob_bis row 14 job__: 200446892 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-job_description"></a>

**dob_bis.14.job_description** [fact] dob_bis row 14 job_description: EXISTING CO 808-1926 UNDER NB-2714-1925 EXISTING STORE TO CHANGEDD INTO FISH MARKET AND VEGETABLE STORE PL AND MINOR PARTITION WORK. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-job_status_descrp"></a>

**dob_bis.14.job_status_descrp** [fact] dob_bis row 14 job_status_descrp: PLAN EXAM - APPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-job_type"></a>

**dob_bis.14.job_type** [fact] dob_bis row 14 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-latest_action_date"></a>

**dob_bis.14.latest_action_date** [fact] dob_bis row 14 latest_action_date: 04/23/1999 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-pre__filing_date"></a>

**dob_bis.14.pre__filing_date** [fact] dob_bis row 14 pre__filing_date: 04/22/1999 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-street_name"></a>

**dob_bis.14.street_name** [fact] dob_bis row 14 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-bbl"></a>

**dob_bis.15.bbl** [fact] dob_bis row 15 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-bin__"></a>

**dob_bis.15.bin__** [fact] dob_bis row 15 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-doc__"></a>

**dob_bis.15.doc__** [fact] dob_bis row 15 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-house__"></a>

**dob_bis.15.house__** [fact] dob_bis row 15 house__: 1534 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-job__"></a>

**dob_bis.15.job__** [fact] dob_bis row 15 job__: 200502884 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-job_description"></a>

**dob_bis.15.job_description** [fact] dob_bis row 15 job_description: Air Conditioning Installation. There will be no change in use egress or occupanc y (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-job_status_descrp"></a>

**dob_bis.15.job_status_descrp** [fact] dob_bis row 15 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-job_type"></a>

**dob_bis.15.job_type** [fact] dob_bis row 15 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-latest_action_date"></a>

**dob_bis.15.latest_action_date** [fact] dob_bis row 15 latest_action_date: 11/01/1999 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-pre__filing_date"></a>

**dob_bis.15.pre__filing_date** [fact] dob_bis row 15 pre__filing_date: 03/09/1998 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-signoff_date"></a>

**dob_bis.15.signoff_date** [fact] dob_bis row 15 signoff_date: 11/01/1999 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/signoff_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-street_name"></a>

**dob_bis.15.street_name** [fact] dob_bis row 15 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-bbl"></a>

**dob_bis.16.bbl** [fact] dob_bis row 16 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-bin__"></a>

**dob_bis.16.bin__** [fact] dob_bis row 16 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-doc__"></a>

**dob_bis.16.doc__** [fact] dob_bis row 16 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-house__"></a>

**dob_bis.16.house__** [fact] dob_bis row 16 house__: 1530 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-job__"></a>

**dob_bis.16.job__** [fact] dob_bis row 16 job__: 200637249 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-job_description"></a>

**dob_bis.16.job_description** [fact] dob_bis row 16 job_description: TO REPLACE EXISTING HVAC SPLIT SYSTEM WI TH NEW.NO CHANGE IN USE,OCCUPAN Y OR EGRESS (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-job_status_descrp"></a>

**dob_bis.16.job_status_descrp** [fact] dob_bis row 16 job_status_descrp: PERMIT ISSUED - PARTIAL JOB (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-job_type"></a>

**dob_bis.16.job_type** [fact] dob_bis row 16 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-latest_action_date"></a>

**dob_bis.16.latest_action_date** [fact] dob_bis row 16 latest_action_date: 11/08/2000 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-pre__filing_date"></a>

**dob_bis.16.pre__filing_date** [fact] dob_bis row 16 pre__filing_date: 08/30/2000 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-street_name"></a>

**dob_bis.16.street_name** [fact] dob_bis row 16 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-bbl"></a>

**dob_bis.17.bbl** [fact] dob_bis row 17 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-bin__"></a>

**dob_bis.17.bin__** [fact] dob_bis row 17 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-doc__"></a>

**dob_bis.17.doc__** [fact] dob_bis row 17 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-house__"></a>

**dob_bis.17.house__** [fact] dob_bis row 17 house__: 1548 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-job__"></a>

**dob_bis.17.job__** [fact] dob_bis row 17 job__: 200733821 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-job_description"></a>

**dob_bis.17.job_description** [fact] dob_bis row 17 job_description: INSTALL FIRE SUPPRESSION SYSTEM ONLY. NO CHANGE IN USE, EGRESS, OR OCC UPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-job_status_descrp"></a>

**dob_bis.17.job_status_descrp** [fact] dob_bis row 17 job_status_descrp: PERMIT ISSUED - PARTIAL JOB (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-job_type"></a>

**dob_bis.17.job_type** [fact] dob_bis row 17 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-latest_action_date"></a>

**dob_bis.17.latest_action_date** [fact] dob_bis row 17 latest_action_date: 06/07/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-pre__filing_date"></a>

**dob_bis.17.pre__filing_date** [fact] dob_bis row 17 pre__filing_date: 05/22/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-street_name"></a>

**dob_bis.17.street_name** [fact] dob_bis row 17 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-bbl"></a>

**dob_bis.18.bbl** [fact] dob_bis row 18 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-bin__"></a>

**dob_bis.18.bin__** [fact] dob_bis row 18 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-doc__"></a>

**dob_bis.18.doc__** [fact] dob_bis row 18 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-house__"></a>

**dob_bis.18.house__** [fact] dob_bis row 18 house__: 1534 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-job__"></a>

**dob_bis.18.job__** [fact] dob_bis row 18 job__: 200898092 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-job_description"></a>

**dob_bis.18.job_description** [fact] dob_bis row 18 job_description: INSTALLATION OF HVAC UNIT ON EXISTING DUNNAGE.  NO CHANGE IN USE, OCCUPANCY OR EGRESS UNDER THIS APPLICATION. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-job_status_descrp"></a>

**dob_bis.18.job_status_descrp** [fact] dob_bis row 18 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-job_type"></a>

**dob_bis.18.job_type** [fact] dob_bis row 18 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-latest_action_date"></a>

**dob_bis.18.latest_action_date** [fact] dob_bis row 18 latest_action_date: 12/21/2005 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-pre__filing_date"></a>

**dob_bis.18.pre__filing_date** [fact] dob_bis row 18 pre__filing_date: 11/17/2005 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-signoff_date"></a>

**dob_bis.18.signoff_date** [fact] dob_bis row 18 signoff_date: 12/21/2005 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/signoff_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-street_name"></a>

**dob_bis.18.street_name** [fact] dob_bis row 18 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-bbl"></a>

**dob_bis.19.bbl** [fact] dob_bis row 19 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-bin__"></a>

**dob_bis.19.bin__** [fact] dob_bis row 19 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-doc__"></a>

**dob_bis.19.doc__** [fact] dob_bis row 19 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-house__"></a>

**dob_bis.19.house__** [fact] dob_bis row 19 house__: 1548 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-job__"></a>

**dob_bis.19.job__** [fact] dob_bis row 19 job__: 201121106 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-job_description"></a>

**dob_bis.19.job_description** [fact] dob_bis row 19 job_description: RELOCATION OF THE EXISTING INTERIOR STAIR FROM FIRST FLOOR TO CELLAR FLO OR, AS PER DRAWINGS. "NO CHANGE IN USE,EGRESS OR OCCUPANCY". (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-job_status_descrp"></a>

**dob_bis.19.job_status_descrp** [fact] dob_bis row 19 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-job_type"></a>

**dob_bis.19.job_type** [fact] dob_bis row 19 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-latest_action_date"></a>

**dob_bis.19.latest_action_date** [fact] dob_bis row 19 latest_action_date: 05/04/2009 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-pre__filing_date"></a>

**dob_bis.19.pre__filing_date** [fact] dob_bis row 19 pre__filing_date: 04/26/2007 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-street_name"></a>

**dob_bis.19.street_name** [fact] dob_bis row 19 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-bbl"></a>

**dob_bis.20.bbl** [fact] dob_bis row 20 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-bin__"></a>

**dob_bis.20.bin__** [fact] dob_bis row 20 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-doc__"></a>

**dob_bis.20.doc__** [fact] dob_bis row 20 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-house__"></a>

**dob_bis.20.house__** [fact] dob_bis row 20 house__: 1530 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-job__"></a>

**dob_bis.20.job__** [fact] dob_bis row 20 job__: 220484394 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-job_description"></a>

**dob_bis.20.job_description** [fact] dob_bis row 20 job_description: RENOVATE EXISTING EATING AND DRINKING ESTABLISHMENT AS PER PLAN. NO CHANGE IN USE EGRESS OR OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-job_status_descrp"></a>

**dob_bis.20.job_status_descrp** [fact] dob_bis row 20 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-job_type"></a>

**dob_bis.20.job_type** [fact] dob_bis row 20 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-latest_action_date"></a>

**dob_bis.20.latest_action_date** [fact] dob_bis row 20 latest_action_date: 10/20/2015 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-pre__filing_date"></a>

**dob_bis.20.pre__filing_date** [fact] dob_bis row 20 pre__filing_date: 10/20/2015 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-street_name"></a>

**dob_bis.20.street_name** [fact] dob_bis row 20 street_name: UNIVERSITY AVE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-bbl"></a>

**dob_bis.21.bbl** [fact] dob_bis row 21 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-bin__"></a>

**dob_bis.21.bin__** [fact] dob_bis row 21 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-doc__"></a>

**dob_bis.21.doc__** [fact] dob_bis row 21 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-house__"></a>

**dob_bis.21.house__** [fact] dob_bis row 21 house__: 1534 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-job__"></a>

**dob_bis.21.job__** [fact] dob_bis row 21 job__: 220522931 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-job_status_descrp"></a>

**dob_bis.21.job_status_descrp** [fact] dob_bis row 21 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-job_type"></a>

**dob_bis.21.job_type** [fact] dob_bis row 21 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-latest_action_date"></a>

**dob_bis.21.latest_action_date** [fact] dob_bis row 21 latest_action_date: 03/30/2016 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-pre__filing_date"></a>

**dob_bis.21.pre__filing_date** [fact] dob_bis row 21 pre__filing_date: 03/25/2016 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-street_name"></a>

**dob_bis.21.street_name** [fact] dob_bis row 21 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-bbl"></a>

**dob_bis.22.bbl** [fact] dob_bis row 22 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-bin__"></a>

**dob_bis.22.bin__** [fact] dob_bis row 22 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-doc__"></a>

**dob_bis.22.doc__** [fact] dob_bis row 22 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-house__"></a>

**dob_bis.22.house__** [fact] dob_bis row 22 house__: 1546 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-job__"></a>

**dob_bis.22.job__** [fact] dob_bis row 22 job__: 220563156 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-job_status_descrp"></a>

**dob_bis.22.job_status_descrp** [fact] dob_bis row 22 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-job_type"></a>

**dob_bis.22.job_type** [fact] dob_bis row 22 job_type: PA (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-latest_action_date"></a>

**dob_bis.22.latest_action_date** [fact] dob_bis row 22 latest_action_date: 12/08/2016 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-pre__filing_date"></a>

**dob_bis.22.pre__filing_date** [fact] dob_bis row 22 pre__filing_date: 12/06/2016 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-street_name"></a>

**dob_bis.22.street_name** [fact] dob_bis row 22 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-bbl"></a>

**dob_bis.23.bbl** [fact] dob_bis row 23 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-bin__"></a>

**dob_bis.23.bin__** [fact] dob_bis row 23 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-doc__"></a>

**dob_bis.23.doc__** [fact] dob_bis row 23 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-house__"></a>

**dob_bis.23.house__** [fact] dob_bis row 23 house__: 1534 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-job__"></a>

**dob_bis.23.job__** [fact] dob_bis row 23 job__: 220576302 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-job_description"></a>

**dob_bis.23.job_description** [fact] dob_bis row 23 job_description: INSTALLING NEW FIRE SUPPRESSION SYSTEM ONLY.  NO OTHER WORK TO BE DONE.  NO CHANGE IN USE, EGRESS OR OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-job_status_descrp"></a>

**dob_bis.23.job_status_descrp** [fact] dob_bis row 23 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-job_type"></a>

**dob_bis.23.job_type** [fact] dob_bis row 23 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-latest_action_date"></a>

**dob_bis.23.latest_action_date** [fact] dob_bis row 23 latest_action_date: 01/20/2017 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-pre__filing_date"></a>

**dob_bis.23.pre__filing_date** [fact] dob_bis row 23 pre__filing_date: 12/29/2016 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-street_name"></a>

**dob_bis.23.street_name** [fact] dob_bis row 23 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-bbl"></a>

**dob_bis.24.bbl** [fact] dob_bis row 24 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-bin__"></a>

**dob_bis.24.bin__** [fact] dob_bis row 24 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-doc__"></a>

**dob_bis.24.doc__** [fact] dob_bis row 24 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-house__"></a>

**dob_bis.24.house__** [fact] dob_bis row 24 house__: 1542 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-job__"></a>

**dob_bis.24.job__** [fact] dob_bis row 24 job__: 220596647 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-job_description"></a>

**dob_bis.24.job_description** [fact] dob_bis row 24 job_description: RESPECTFULLY REQUEST TO DO MINOR CHANGES IN EATING AND DRINKING ESTABLISHMENT AS PER PLANS. NO CHANGE CERTIFICATE OF OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-job_status_descrp"></a>

**dob_bis.24.job_status_descrp** [fact] dob_bis row 24 job_status_descrp: PERMIT ISSUED - PARTIAL JOB (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-job_type"></a>

**dob_bis.24.job_type** [fact] dob_bis row 24 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-latest_action_date"></a>

**dob_bis.24.latest_action_date** [fact] dob_bis row 24 latest_action_date: 05/12/2017 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-pre__filing_date"></a>

**dob_bis.24.pre__filing_date** [fact] dob_bis row 24 pre__filing_date: 05/12/2017 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-street_name"></a>

**dob_bis.24.street_name** [fact] dob_bis row 24 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-bbl"></a>

**dob_bis.25.bbl** [fact] dob_bis row 25 bbl: 2028750045 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/bbl`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-bin__"></a>

**dob_bis.25.bin__** [fact] dob_bis row 25 bin__: 2008785 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/bin__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-doc__"></a>

**dob_bis.25.doc__** [fact] dob_bis row 25 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/doc__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-house__"></a>

**dob_bis.25.house__** [fact] dob_bis row 25 house__: 1548 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/house__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-job__"></a>

**dob_bis.25.job__** [fact] dob_bis row 25 job__: 220635249 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/job__`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-job_description"></a>

**dob_bis.25.job_description** [fact] dob_bis row 25 job_description: FILING TO INSTALL NEW FIRE SUPPRESSION SYSTEM.  NO OTHER WORK TO BE DONE.  NO CHANGE IN USE, EGRESS OR OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/job_description`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-job_status_descrp"></a>

**dob_bis.25.job_status_descrp** [fact] dob_bis row 25 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/job_status_descrp`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-job_type"></a>

**dob_bis.25.job_type** [fact] dob_bis row 25 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/job_type`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-latest_action_date"></a>

**dob_bis.25.latest_action_date** [fact] dob_bis row 25 latest_action_date: 05/14/2019 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/latest_action_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-pre__filing_date"></a>

**dob_bis.25.pre__filing_date** [fact] dob_bis row 25 pre__filing_date: 03/19/2018 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/pre__filing_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-signoff_date"></a>

**dob_bis.25.signoff_date** [fact] dob_bis row 25 signoff_date: 05/14/2019 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/signoff_date`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-street_name"></a>

**dob_bis.25.street_name** [fact] dob_bis row 25 street_name: UNIVERSITY AVENUE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/street_name`; SHA256 `e3b5424558ae750b01df4f1ab714bf7cc2fbf6df2cae7805d5b87b95c2b81fcd`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028750045%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

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
