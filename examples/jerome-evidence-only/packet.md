# Parcel investigation 2028560051

What do these public records establish about this different Bronx parcel, and what questions remain?

**Partial playbook under development.** This packet preserves evidence and conditional arithmetic; it does not establish site availability, a lawful use, legal capacity, building fit or funded feasibility.

## What this run did

Queried four NYC public datasets for one tax lot, preserved the returned records, extracted typed facts, and applied an optional user-stated area budget. Professional interpretation is pending.

## Source coverage

| Source | Status | Returned rows | Truncated | Retrieved UTC |
| --- | --- | --- | --- | --- |
| address_resolution | ok | 1 | False | 2026-10-28T22:50:35.806255+00:00 |
| pluto | ok | 1 | False | 2026-10-28T22:50:36.396392+00:00 |
| dob_bis | ok | 0 | False | 2026-10-28T22:50:36.397202+00:00 |
| dob_now | ok | 0 | False | 2026-10-28T22:50:36.397753+00:00 |
| hpd_violations | ok | 0 | False | 2026-10-28T22:50:36.398357+00:00 |

A failed request is missing evidence, not zero records. Counts describe returned rows, not unique projects. Empty exact-BBL results do not establish no housing, no violations or no activity.

## Recorded parcel facts

- Recorded address: 1337 JEROME AVENUE — [source](#pluto-0-address)
- Tax-lot BBL: 2028560051.00000000 — [source](#pluto-0-bbl)
- Recorded building area (sf): 6250 — [source](#pluto-0-bldgarea)
- Recorded building class: O1 — [source](#pluto-0-bldgclass)
- block: 2856 — [source](#pluto-0-block)
- borough: BX — [source](#pluto-0-borough)
- Recorded built FAR: 0.96000000000 — [source](#pluto-0-builtfar)
- Recorded irregular-lot flag: True — [source](#pluto-0-irrlotcode)
- landuse: 5 — [source](#pluto-0-landuse)
- latitude: 40.8389423 — [source](#pluto-0-latitude)
- longitude: -73.9190648 — [source](#pluto-0-longitude)
- lot: 51 — [source](#pluto-0-lot)
- Recorded lot area (sf): 6516 — [source](#pluto-0-lotarea)
- Recorded floor count: 1.0000000 — [source](#pluto-0-numfloors)
- Recorded overlay: C2-4 — [source](#pluto-0-overlay1)
- Recorded residential FAR (legal applicability unreviewed): 6.02000000000 — [source](#pluto-0-residfar)
- Recorded special district: J — [source](#pluto-0-spdist1)
- Recorded residential units: 0 — [source](#pluto-0-unitsres)
- Recorded total units: 1 — [source](#pluto-0-unitstotal)
- Dataset row version: 26v2 — [source](#pluto-0-version)
- Recorded primary zoning district: R8A — [source](#pluto-0-zonedist1)

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

Source: [pluto raw response](sources/pluto.json), JSON pointer `/`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

Bounded query; see truncation and source limits.

<a id="pluto-0-address"></a>

**pluto.0.address** [fact] pluto row 0 address: 1337 JEROME AVENUE (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/address`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bbl"></a>

**pluto.0.bbl** [fact] pluto row 0 bbl: 2028560051.00000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bbl`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgarea"></a>

**pluto.0.bldgarea** [fact] pluto row 0 bldgarea: 6250 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgarea`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgclass"></a>

**pluto.0.bldgclass** [fact] pluto row 0 bldgclass: O1 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgclass`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-block"></a>

**pluto.0.block** [fact] pluto row 0 block: 2856 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/block`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-borough"></a>

**pluto.0.borough** [fact] pluto row 0 borough: BX (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/borough`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-builtfar"></a>

**pluto.0.builtfar** [fact] pluto row 0 builtfar: 0.96000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/builtfar`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-irrlotcode"></a>

**pluto.0.irrlotcode** [fact] pluto row 0 irrlotcode: True (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/irrlotcode`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-landuse"></a>

**pluto.0.landuse** [fact] pluto row 0 landuse: 5 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/landuse`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-latitude"></a>

**pluto.0.latitude** [fact] pluto row 0 latitude: 40.8389423 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/latitude`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-longitude"></a>

**pluto.0.longitude** [fact] pluto row 0 longitude: -73.9190648 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/longitude`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lot"></a>

**pluto.0.lot** [fact] pluto row 0 lot: 51 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lot`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lotarea"></a>

**pluto.0.lotarea** [fact] pluto row 0 lotarea: 6516 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lotarea`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-numfloors"></a>

**pluto.0.numfloors** [fact] pluto row 0 numfloors: 1.0000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/numfloors`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-overlay1"></a>

**pluto.0.overlay1** [fact] pluto row 0 overlay1: C2-4 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/overlay1`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-residfar"></a>

**pluto.0.residfar** [fact] pluto row 0 residfar: 6.02000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/residfar`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-spdist1"></a>

**pluto.0.spdist1** [fact] pluto row 0 spdist1: J (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/spdist1`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitsres"></a>

**pluto.0.unitsres** [fact] pluto row 0 unitsres: 0 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitsres`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitstotal"></a>

**pluto.0.unitstotal** [fact] pluto row 0 unitstotal: 1 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitstotal`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-version"></a>

**pluto.0.version** [fact] pluto row 0 version: 26v2 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/version`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-zonedist1"></a>

**pluto.0.zonedist1** [fact] pluto row 0 zonedist1: R8A (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/zonedist1`; SHA256 `249e3d933782fc75356441aed36ecc3aa2b48f1861bb6016dd55d836744a1624`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028560051&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="dob_bis-returned_rows"></a>

**dob_bis.returned_rows** [calculation] dob_bis returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028560051%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

Bounded query; see truncation and source limits.

<a id="dob_now-returned_rows"></a>

**dob_now.returned_rows** [calculation] dob_now returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028560051%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

Bounded query; see truncation and source limits.

<a id="hpd_violations-returned_rows"></a>

**hpd_violations.returned_rows** [calculation] hpd_violations returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [hpd_violations raw response](sources/hpd_violations.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/wvxf-dwi5.json?%24where=bbl%3D%272028560051%27&%24select=bbl%2Cviolationid%2Cinspectiondate%2Cclass%2Cviolationstatus%2Ccurrentstatus%2Cnovdescription%2Cbin&%24order=violationid&%24limit=501).

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

- **address_resolution** — Tax-lot attributes may lag actual conditions. Zoning fields are recorded descriptors, not a legal entitlement analysis. Zero recorded residential units does not mean vacancy or no displacement. [Publisher dataset](https://data.cityofnewyork.us/d/64uk-42ks). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **pluto** — Tax-lot attributes may lag actual conditions. Zoning fields are recorded descriptors, not a legal entitlement analysis. Zero recorded residential units does not mean vacancy or no displacement. [Publisher dataset](https://data.cityofnewyork.us/d/64uk-42ks). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **dob_bis** — Legacy job/document rows, not unique projects or verified current use. Historical existing/proposed units are not current lawful dwellings. Exact-BBL queries miss unlinked filings and historical lot changes. [Publisher dataset](https://data.cityofnewyork.us/d/ic3t-wcy2). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **dob_now** — DOB NOW filing rows are not completed projects or a complete pipeline. Exact-BBL lookup only; missing rows do not establish no activity. [Publisher dataset](https://data.cityofnewyork.us/d/w9ak-ipjd). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **hpd_violations** — Recorded housing violation rows, not occupancy, executed evictions, or a displacement measure. Empty results do not prove no housing, no violations, or a safe building. [Publisher dataset](https://data.cityofnewyork.us/d/wvxf-dwi5). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
