# Parcel investigation 2028710002

What do public records tell us about this Bronx lot, which housing signals need reconciliation, and what would the stated area budget imply?

**Partial playbook under development.** This packet preserves evidence and conditional arithmetic; it does not establish site availability, a lawful use, legal capacity, building fit or funded feasibility.

## What this run did

Queried four NYC public datasets for one tax lot, preserved the returned records, extracted typed facts, and applied an optional user-stated area budget. Professional interpretation is pending.

## Source coverage

| Source | Status | Returned rows | Truncated | Retrieved UTC |
| --- | --- | --- | --- | --- |
| pluto | ok | 1 | False | 2026-10-28T22:47:29.591267+00:00 |
| dob_bis | ok | 27 | False | 2026-10-28T22:47:29.592160+00:00 |
| dob_now | ok | 0 | False | 2026-10-28T22:47:29.592722+00:00 |
| hpd_violations | ok | 0 | False | 2026-10-28T22:47:29.593277+00:00 |

A failed request is missing evidence, not zero records. Counts describe returned rows, not unique projects. Empty exact-BBL results do not establish no housing, no violations or no activity.

## Recorded parcel facts

- Recorded address: 1240 EDWARD L GRANT HWY — [source](#pluto-0-address)
- Tax-lot BBL: 2028710002.00000000 — [source](#pluto-0-bbl)
- Recorded building area (sf): 26000 — [source](#pluto-0-bldgarea)
- Recorded building class: K1 — [source](#pluto-0-bldgclass)
- block: 2871 — [source](#pluto-0-block)
- borough: BX — [source](#pluto-0-borough)
- Recorded built FAR: 0.44000000000 — [source](#pluto-0-builtfar)
- Recorded environmental designation: E-442 — [source](#pluto-0-edesignum)
- Recorded irregular-lot flag: True — [source](#pluto-0-irrlotcode)
- landuse: 5 — [source](#pluto-0-landuse)
- latitude: 40.8376295 — [source](#pluto-0-latitude)
- longitude: -73.9218130 — [source](#pluto-0-longitude)
- lot: 2 — [source](#pluto-0-lot)
- Recorded lot area (sf): 59050 — [source](#pluto-0-lotarea)
- Recorded floor count: 1.0000000 — [source](#pluto-0-numfloors)
- Recorded overlay: C2-4 — [source](#pluto-0-overlay1)
- Recorded residential FAR (legal applicability unreviewed): 7.52000000000 — [source](#pluto-0-residfar)
- Recorded special district: J — [source](#pluto-0-spdist1)
- Recorded residential units: 0 — [source](#pluto-0-unitsres)
- Recorded total units: 4 — [source](#pluto-0-unitstotal)
- Dataset row version: 26v2 — [source](#pluto-0-version)
- Recorded primary zoning district: R9A — [source](#pluto-0-zonedist1)

## Historical housing signals requiring reconciliation

- Historical proposed dwelling units: 9; filing date 02/13/2003; HEREWITH FILING FOR MODIFICATIONS TO PLU  MBING AND MECHANICAL SYSTEMS A INDICATED ON PLANS.  NO CHANGE IN USE, E  GRESS, OR OCCUPANCY. — [source](#dob_bis-12-proposed_dwelling_units)

These fields describe historical existing/proposed units. They are not a current occupancy count and are not summed across documents or jobs. Their relationship to PLUTO and lawful/current use needs review.

## Scenario and calculation steps

Illustrative area budget, not a proposed or approved building

| Claim | Value | Unit | Basis |
| --- | --- | --- | --- |
| [gross_area_sf](#scenario-gross_area_sf) | 40000 | gross sf | Demonstration input chosen to exercise the workflow; not derived from zoning or verified drawings. |
| [nonresidential_gross_sf](#scenario-nonresidential_gross_sf) | 6000 | gross sf | Demonstration allocation to nonresidential uses; not a tenant commitment or displacement assessment. |
| [residential_net_efficiency](#scenario-residential_net_efficiency) | 0.8 | share | Hypothetical net residential share after circulation/support; no layout verified. |
| [average_net_home_sf](#scenario-average_net_home_sf) | 800 | net sf per home-equivalent | Hypothetical average home size; no unit mix or code compliance established. |
| [Residential gross area allocation](#scenario-residential_gross_sf) | 34000.0 | gross sf | 40000 − 6000 |
| [Residential net area allowance](#scenario-residential_net_sf) | 27200.0 | net sf | 34000.0 × 0.8 |
| [Area-budget home-equivalents](#scenario-home_equivalents) | 34.0 | home-equivalents; not a feasible unit count | 27200.0 ÷ 800 |
| [Proposed gross area / recorded lot area](#scenario-gross_to_recorded_lot_ratio) | 0.6773920406435224 | gross-to-lot ratio; NOT zoning FAR | 40000 ÷ 59050 |

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

Source: [pluto raw response](sources/pluto.json), JSON pointer `/`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

Bounded query; see truncation and source limits.

<a id="pluto-0-address"></a>

**pluto.0.address** [fact] pluto row 0 address: 1240 EDWARD L GRANT HWY (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/address`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bbl"></a>

**pluto.0.bbl** [fact] pluto row 0 bbl: 2028710002.00000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bbl`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgarea"></a>

**pluto.0.bldgarea** [fact] pluto row 0 bldgarea: 26000 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgarea`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-bldgclass"></a>

**pluto.0.bldgclass** [fact] pluto row 0 bldgclass: K1 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/bldgclass`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-block"></a>

**pluto.0.block** [fact] pluto row 0 block: 2871 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/block`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-borough"></a>

**pluto.0.borough** [fact] pluto row 0 borough: BX (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/borough`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-builtfar"></a>

**pluto.0.builtfar** [fact] pluto row 0 builtfar: 0.44000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/builtfar`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-edesignum"></a>

**pluto.0.edesignum** [fact] pluto row 0 edesignum: E-442 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/edesignum`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-irrlotcode"></a>

**pluto.0.irrlotcode** [fact] pluto row 0 irrlotcode: True (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/irrlotcode`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-landuse"></a>

**pluto.0.landuse** [fact] pluto row 0 landuse: 5 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/landuse`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-latitude"></a>

**pluto.0.latitude** [fact] pluto row 0 latitude: 40.8376295 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/latitude`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-longitude"></a>

**pluto.0.longitude** [fact] pluto row 0 longitude: -73.9218130 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/longitude`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lot"></a>

**pluto.0.lot** [fact] pluto row 0 lot: 2 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lot`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-lotarea"></a>

**pluto.0.lotarea** [fact] pluto row 0 lotarea: 59050 (square feet as recorded)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/lotarea`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-numfloors"></a>

**pluto.0.numfloors** [fact] pluto row 0 numfloors: 1.0000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/numfloors`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-overlay1"></a>

**pluto.0.overlay1** [fact] pluto row 0 overlay1: C2-4 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/overlay1`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-residfar"></a>

**pluto.0.residfar** [fact] pluto row 0 residfar: 7.52000000000 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/residfar`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-spdist1"></a>

**pluto.0.spdist1** [fact] pluto row 0 spdist1: J (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/spdist1`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitsres"></a>

**pluto.0.unitsres** [fact] pluto row 0 unitsres: 0 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitsres`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-unitstotal"></a>

**pluto.0.unitstotal** [fact] pluto row 0 unitstotal: 4 (units as recorded; source definition applies)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/unitstotal`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-version"></a>

**pluto.0.version** [fact] pluto row 0 version: 26v2 (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/version`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="pluto-0-zonedist1"></a>

**pluto.0.zonedist1** [fact] pluto row 0 zonedist1: R9A (source value)

Source: [pluto raw response](sources/pluto.json), JSON pointer `/0/zonedist1`; SHA256 `1ab74f2aecfbc62c5b9332b0c15960de316480140d344777be6374b445cb2179`. [Exact request](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24select=bbl%2Caddress%2Cborough%2Cblock%2Clot%2Clotarea%2Cbldgarea%2Cunitsres%2Cunitstotal%2Cbldgclass%2Clanduse%2Czonedist1%2Czonedist2%2Coverlay1%2Cspdist1%2Cspdist2%2Cirrlotcode%2Cresidfar%2Cbuiltfar%2Cnumfloors%2Cedesignum%2Clatitude%2Clongitude%2Cversion&%24order=bbl&%24limit=501).

<a id="dob_bis-returned_rows"></a>

**dob_bis.returned_rows** [calculation] dob_bis returned rows in this exact-BBL query: 27 (returned rows; not projects or total population)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

Bounded query; see truncation and source limits.

<a id="dob_bis-0-bbl"></a>

**dob_bis.0.bbl** [fact] dob_bis row 0 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-bin__"></a>

**dob_bis.0.bin__** [fact] dob_bis row 0 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-doc__"></a>

**dob_bis.0.doc__** [fact] dob_bis row 0 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-house__"></a>

**dob_bis.0.house__** [fact] dob_bis row 0 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job__"></a>

**dob_bis.0.job__** [fact] dob_bis row 0 job__: 200077120 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_description"></a>

**dob_bis.0.job_description** [fact] dob_bis row 0 job_description: INSTALL SPRINKLER SYSTEM FILED IN CONJU- NCTION WITH APPLICATION #200077 39. NO CHANGE TO EGRESS OR OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_status_descrp"></a>

**dob_bis.0.job_status_descrp** [fact] dob_bis row 0 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-job_type"></a>

**dob_bis.0.job_type** [fact] dob_bis row 0 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-latest_action_date"></a>

**dob_bis.0.latest_action_date** [fact] dob_bis row 0 latest_action_date: 08/28/1990 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-pre__filing_date"></a>

**dob_bis.0.pre__filing_date** [fact] dob_bis row 0 pre__filing_date: 08/23/1990 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-0-street_name"></a>

**dob_bis.0.street_name** [fact] dob_bis row 0 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/0/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bbl"></a>

**dob_bis.1.bbl** [fact] dob_bis row 1 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-bin__"></a>

**dob_bis.1.bin__** [fact] dob_bis row 1 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-doc__"></a>

**dob_bis.1.doc__** [fact] dob_bis row 1 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-house__"></a>

**dob_bis.1.house__** [fact] dob_bis row 1 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job__"></a>

**dob_bis.1.job__** [fact] dob_bis row 1 job__: 200077139 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_description"></a>

**dob_bis.1.job_description** [fact] dob_bis row 1 job_description: PARTITIONS, FLOORING, CEILING, STOREFRON  T STEEL, MASONRY AND ROOFING. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_status_descrp"></a>

**dob_bis.1.job_status_descrp** [fact] dob_bis row 1 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-job_type"></a>

**dob_bis.1.job_type** [fact] dob_bis row 1 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-latest_action_date"></a>

**dob_bis.1.latest_action_date** [fact] dob_bis row 1 latest_action_date: 09/13/1990 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-pre__filing_date"></a>

**dob_bis.1.pre__filing_date** [fact] dob_bis row 1 pre__filing_date: 08/23/1990 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-1-street_name"></a>

**dob_bis.1.street_name** [fact] dob_bis row 1 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/1/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-bbl"></a>

**dob_bis.2.bbl** [fact] dob_bis row 2 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-bin__"></a>

**dob_bis.2.bin__** [fact] dob_bis row 2 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-doc__"></a>

**dob_bis.2.doc__** [fact] dob_bis row 2 doc__: 02 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-house__"></a>

**dob_bis.2.house__** [fact] dob_bis row 2 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job__"></a>

**dob_bis.2.job__** [fact] dob_bis row 2 job__: 200077139 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_description"></a>

**dob_bis.2.job_description** [fact] dob_bis row 2 job_description: STRUCTUARAL PLANS FILED AS PART OF APPLICATION. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_status_descrp"></a>

**dob_bis.2.job_status_descrp** [fact] dob_bis row 2 job_status_descrp: APPLICATION PROCESSED - ENTIRE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-job_type"></a>

**dob_bis.2.job_type** [fact] dob_bis row 2 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-latest_action_date"></a>

**dob_bis.2.latest_action_date** [fact] dob_bis row 2 latest_action_date: 09/05/1990 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-pre__filing_date"></a>

**dob_bis.2.pre__filing_date** [fact] dob_bis row 2 pre__filing_date: 08/23/1990 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-2-street_name"></a>

**dob_bis.2.street_name** [fact] dob_bis row 2 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/2/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-bbl"></a>

**dob_bis.3.bbl** [fact] dob_bis row 3 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-bin__"></a>

**dob_bis.3.bin__** [fact] dob_bis row 3 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-doc__"></a>

**dob_bis.3.doc__** [fact] dob_bis row 3 doc__: 03 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-house__"></a>

**dob_bis.3.house__** [fact] dob_bis row 3 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job__"></a>

**dob_bis.3.job__** [fact] dob_bis row 3 job__: 200077139 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_status_descrp"></a>

**dob_bis.3.job_status_descrp** [fact] dob_bis row 3 job_status_descrp: APPLICATION PROCESSED - ENTIRE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-job_type"></a>

**dob_bis.3.job_type** [fact] dob_bis row 3 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-latest_action_date"></a>

**dob_bis.3.latest_action_date** [fact] dob_bis row 3 latest_action_date: 09/05/1990 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-pre__filing_date"></a>

**dob_bis.3.pre__filing_date** [fact] dob_bis row 3 pre__filing_date: 08/23/1990 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-3-street_name"></a>

**dob_bis.3.street_name** [fact] dob_bis row 3 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/3/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-bbl"></a>

**dob_bis.4.bbl** [fact] dob_bis row 4 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-bin__"></a>

**dob_bis.4.bin__** [fact] dob_bis row 4 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-doc__"></a>

**dob_bis.4.doc__** [fact] dob_bis row 4 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-house__"></a>

**dob_bis.4.house__** [fact] dob_bis row 4 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job__"></a>

**dob_bis.4.job__** [fact] dob_bis row 4 job__: 200116506 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_description"></a>

**dob_bis.4.job_description** [fact] dob_bis row 4 job_description: FILING TO CHANGE USE, ADD ADDITIONAL FL. AREA, &amp; OBTAIN NEW C.O. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_status_descrp"></a>

**dob_bis.4.job_status_descrp** [fact] dob_bis row 4 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-job_type"></a>

**dob_bis.4.job_type** [fact] dob_bis row 4 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-latest_action_date"></a>

**dob_bis.4.latest_action_date** [fact] dob_bis row 4 latest_action_date: 09/20/1991 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-pre__filing_date"></a>

**dob_bis.4.pre__filing_date** [fact] dob_bis row 4 pre__filing_date: 06/03/1991 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-4-street_name"></a>

**dob_bis.4.street_name** [fact] dob_bis row 4 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/4/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-bbl"></a>

**dob_bis.5.bbl** [fact] dob_bis row 5 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-bin__"></a>

**dob_bis.5.bin__** [fact] dob_bis row 5 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-doc__"></a>

**dob_bis.5.doc__** [fact] dob_bis row 5 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-house__"></a>

**dob_bis.5.house__** [fact] dob_bis row 5 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job__"></a>

**dob_bis.5.job__** [fact] dob_bis row 5 job__: 200276780 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_description"></a>

**dob_bis.5.job_description** [fact] dob_bis row 5 job_description: CONVERT AUTO SHOWROOM TO COMMUNITY ROOM AND ACCESSORY INDOOR PLAY AREA, OUTDOOR PLAY AREA AND PUBLIC PARKING LOT  FOR 50 CARS (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_status_descrp"></a>

**dob_bis.5.job_status_descrp** [fact] dob_bis row 5 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-job_type"></a>

**dob_bis.5.job_type** [fact] dob_bis row 5 job_type: A1 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-latest_action_date"></a>

**dob_bis.5.latest_action_date** [fact] dob_bis row 5 latest_action_date: 03/16/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-pre__filing_date"></a>

**dob_bis.5.pre__filing_date** [fact] dob_bis row 5 pre__filing_date: 12/07/1993 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-signoff_date"></a>

**dob_bis.5.signoff_date** [fact] dob_bis row 5 signoff_date: 03/16/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-5-street_name"></a>

**dob_bis.5.street_name** [fact] dob_bis row 5 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/5/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-bbl"></a>

**dob_bis.6.bbl** [fact] dob_bis row 6 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-bin__"></a>

**dob_bis.6.bin__** [fact] dob_bis row 6 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-doc__"></a>

**dob_bis.6.doc__** [fact] dob_bis row 6 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-house__"></a>

**dob_bis.6.house__** [fact] dob_bis row 6 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job__"></a>

**dob_bis.6.job__** [fact] dob_bis row 6 job__: 200651311 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_description"></a>

**dob_bis.6.job_description** [fact] dob_bis row 6 job_description: TO INSTALL (6) MODINE HEATERS.  NO CHANGE IN USE, EGRESS, OR OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_status_descrp"></a>

**dob_bis.6.job_status_descrp** [fact] dob_bis row 6 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-job_type"></a>

**dob_bis.6.job_type** [fact] dob_bis row 6 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-latest_action_date"></a>

**dob_bis.6.latest_action_date** [fact] dob_bis row 6 latest_action_date: 06/24/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-pre__filing_date"></a>

**dob_bis.6.pre__filing_date** [fact] dob_bis row 6 pre__filing_date: 12/18/2000 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-signoff_date"></a>

**dob_bis.6.signoff_date** [fact] dob_bis row 6 signoff_date: 06/24/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-6-street_name"></a>

**dob_bis.6.street_name** [fact] dob_bis row 6 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/6/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-bbl"></a>

**dob_bis.7.bbl** [fact] dob_bis row 7 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-bin__"></a>

**dob_bis.7.bin__** [fact] dob_bis row 7 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-doc__"></a>

**dob_bis.7.doc__** [fact] dob_bis row 7 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-house__"></a>

**dob_bis.7.house__** [fact] dob_bis row 7 house__: 1250 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job__"></a>

**dob_bis.7.job__** [fact] dob_bis row 7 job__: 200711453 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_description"></a>

**dob_bis.7.job_description** [fact] dob_bis row 7 job_description: Interior construction of laundromat. Install washing machines, dryers, plumbing fixtures, partitions, hung ceiling , boilers,  HVAC roof top units, and relocate existing sprinkler heads. No change to use egress or occupancy. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_status_descrp"></a>

**dob_bis.7.job_status_descrp** [fact] dob_bis row 7 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-job_type"></a>

**dob_bis.7.job_type** [fact] dob_bis row 7 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-latest_action_date"></a>

**dob_bis.7.latest_action_date** [fact] dob_bis row 7 latest_action_date: 06/24/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-pre__filing_date"></a>

**dob_bis.7.pre__filing_date** [fact] dob_bis row 7 pre__filing_date: 01/24/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-signoff_date"></a>

**dob_bis.7.signoff_date** [fact] dob_bis row 7 signoff_date: 06/24/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-7-street_name"></a>

**dob_bis.7.street_name** [fact] dob_bis row 7 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/7/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-bbl"></a>

**dob_bis.8.bbl** [fact] dob_bis row 8 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-bin__"></a>

**dob_bis.8.bin__** [fact] dob_bis row 8 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-doc__"></a>

**dob_bis.8.doc__** [fact] dob_bis row 8 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-house__"></a>

**dob_bis.8.house__** [fact] dob_bis row 8 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job__"></a>

**dob_bis.8.job__** [fact] dob_bis row 8 job__: 200723823 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job_description"></a>

**dob_bis.8.job_description** [fact] dob_bis row 8 job_description: SIZE:  7"-0" (H) X 71'-10"(W) + 10'-6"(H ) X 21'-0"(W) PROJECTION:  3'-0 WORDING: "CLEAN CITY" "SUPER LAUNDROMAT" (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job_status_descrp"></a>

**dob_bis.8.job_status_descrp** [fact] dob_bis row 8 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-job_type"></a>

**dob_bis.8.job_type** [fact] dob_bis row 8 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-latest_action_date"></a>

**dob_bis.8.latest_action_date** [fact] dob_bis row 8 latest_action_date: 04/22/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-pre__filing_date"></a>

**dob_bis.8.pre__filing_date** [fact] dob_bis row 8 pre__filing_date: 04/02/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-signoff_date"></a>

**dob_bis.8.signoff_date** [fact] dob_bis row 8 signoff_date: 04/22/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-8-street_name"></a>

**dob_bis.8.street_name** [fact] dob_bis row 8 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/8/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-bbl"></a>

**dob_bis.9.bbl** [fact] dob_bis row 9 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-bin__"></a>

**dob_bis.9.bin__** [fact] dob_bis row 9 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-doc__"></a>

**dob_bis.9.doc__** [fact] dob_bis row 9 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-house__"></a>

**dob_bis.9.house__** [fact] dob_bis row 9 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-job__"></a>

**dob_bis.9.job__** [fact] dob_bis row 9 job__: 200725037 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-job_description"></a>

**dob_bis.9.job_description** [fact] dob_bis row 9 job_description: 7'-0: (H) X 75'-5" (W) X 3'-0" (PROJECTI ON) WORDING: "CLEAN CITY" "SUPE  LAUNDROMAT" (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-job_status_descrp"></a>

**dob_bis.9.job_status_descrp** [fact] dob_bis row 9 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-job_type"></a>

**dob_bis.9.job_type** [fact] dob_bis row 9 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-latest_action_date"></a>

**dob_bis.9.latest_action_date** [fact] dob_bis row 9 latest_action_date: 04/22/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-pre__filing_date"></a>

**dob_bis.9.pre__filing_date** [fact] dob_bis row 9 pre__filing_date: 04/09/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-signoff_date"></a>

**dob_bis.9.signoff_date** [fact] dob_bis row 9 signoff_date: 04/22/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-9-street_name"></a>

**dob_bis.9.street_name** [fact] dob_bis row 9 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/9/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-bbl"></a>

**dob_bis.10.bbl** [fact] dob_bis row 10 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-bin__"></a>

**dob_bis.10.bin__** [fact] dob_bis row 10 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-doc__"></a>

**dob_bis.10.doc__** [fact] dob_bis row 10 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-house__"></a>

**dob_bis.10.house__** [fact] dob_bis row 10 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-job__"></a>

**dob_bis.10.job__** [fact] dob_bis row 10 job__: 200750393 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-job_description"></a>

**dob_bis.10.job_description** [fact] dob_bis row 10 job_description: TO INSTALL (2) FIRE ALARM SYSTEM.  NO CH  ANGE IN USE, EGRESS, OR OCCUPA Y. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-job_status_descrp"></a>

**dob_bis.10.job_status_descrp** [fact] dob_bis row 10 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-job_type"></a>

**dob_bis.10.job_type** [fact] dob_bis row 10 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-latest_action_date"></a>

**dob_bis.10.latest_action_date** [fact] dob_bis row 10 latest_action_date: 12/30/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-pre__filing_date"></a>

**dob_bis.10.pre__filing_date** [fact] dob_bis row 10 pre__filing_date: 09/04/2002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-signoff_date"></a>

**dob_bis.10.signoff_date** [fact] dob_bis row 10 signoff_date: 12/30/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-10-street_name"></a>

**dob_bis.10.street_name** [fact] dob_bis row 10 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/10/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-bbl"></a>

**dob_bis.11.bbl** [fact] dob_bis row 11 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-bin__"></a>

**dob_bis.11.bin__** [fact] dob_bis row 11 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-doc__"></a>

**dob_bis.11.doc__** [fact] dob_bis row 11 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-house__"></a>

**dob_bis.11.house__** [fact] dob_bis row 11 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-job__"></a>

**dob_bis.11.job__** [fact] dob_bis row 11 job__: 200774199 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-job_description"></a>

**dob_bis.11.job_description** [fact] dob_bis row 11 job_description: HEREWITH FILING FOR INTERIOR PARTITON MO DIFICATIONS AS INDICATED ON PLA S.  NO CHANGE IN USE, EGRESS OR OCCUPANC Y. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-job_status_descrp"></a>

**dob_bis.11.job_status_descrp** [fact] dob_bis row 11 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-job_type"></a>

**dob_bis.11.job_type** [fact] dob_bis row 11 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-latest_action_date"></a>

**dob_bis.11.latest_action_date** [fact] dob_bis row 11 latest_action_date: 10/18/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-pre__filing_date"></a>

**dob_bis.11.pre__filing_date** [fact] dob_bis row 11 pre__filing_date: 02/13/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-signoff_date"></a>

**dob_bis.11.signoff_date** [fact] dob_bis row 11 signoff_date: 10/18/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-11-street_name"></a>

**dob_bis.11.street_name** [fact] dob_bis row 11 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/11/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-bbl"></a>

**dob_bis.12.bbl** [fact] dob_bis row 12 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-bin__"></a>

**dob_bis.12.bin__** [fact] dob_bis row 12 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-doc__"></a>

**dob_bis.12.doc__** [fact] dob_bis row 12 doc__: 02 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-house__"></a>

**dob_bis.12.house__** [fact] dob_bis row 12 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-job__"></a>

**dob_bis.12.job__** [fact] dob_bis row 12 job__: 200774199 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-job_description"></a>

**dob_bis.12.job_description** [fact] dob_bis row 12 job_description: HEREWITH FILING FOR MODIFICATIONS TO PLU  MBING AND MECHANICAL SYSTEMS A INDICATED ON PLANS.  NO CHANGE IN USE, E  GRESS, OR OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-job_status_descrp"></a>

**dob_bis.12.job_status_descrp** [fact] dob_bis row 12 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-job_type"></a>

**dob_bis.12.job_type** [fact] dob_bis row 12 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-latest_action_date"></a>

**dob_bis.12.latest_action_date** [fact] dob_bis row 12 latest_action_date: 10/18/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-pre__filing_date"></a>

**dob_bis.12.pre__filing_date** [fact] dob_bis row 12 pre__filing_date: 02/13/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-proposed_dwelling_units"></a>

**dob_bis.12.proposed_dwelling_units** [fact] dob_bis row 12 proposed_dwelling_units: 9 (units as recorded; source definition applies)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/proposed_dwelling_units`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-signoff_date"></a>

**dob_bis.12.signoff_date** [fact] dob_bis row 12 signoff_date: 10/18/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-12-street_name"></a>

**dob_bis.12.street_name** [fact] dob_bis row 12 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/12/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-bbl"></a>

**dob_bis.13.bbl** [fact] dob_bis row 13 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-bin__"></a>

**dob_bis.13.bin__** [fact] dob_bis row 13 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-doc__"></a>

**dob_bis.13.doc__** [fact] dob_bis row 13 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-house__"></a>

**dob_bis.13.house__** [fact] dob_bis row 13 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-job__"></a>

**dob_bis.13.job__** [fact] dob_bis row 13 job__: 200797361 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-job_status_descrp"></a>

**dob_bis.13.job_status_descrp** [fact] dob_bis row 13 job_status_descrp: COMPLETED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-job_type"></a>

**dob_bis.13.job_type** [fact] dob_bis row 13 job_type: PA (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-latest_action_date"></a>

**dob_bis.13.latest_action_date** [fact] dob_bis row 13 latest_action_date: 03/22/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-pre__filing_date"></a>

**dob_bis.13.pre__filing_date** [fact] dob_bis row 13 pre__filing_date: 07/15/2003 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-signoff_date"></a>

**dob_bis.13.signoff_date** [fact] dob_bis row 13 signoff_date: 03/22/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-13-street_name"></a>

**dob_bis.13.street_name** [fact] dob_bis row 13 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/13/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-bbl"></a>

**dob_bis.14.bbl** [fact] dob_bis row 14 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-bin__"></a>

**dob_bis.14.bin__** [fact] dob_bis row 14 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-doc__"></a>

**dob_bis.14.doc__** [fact] dob_bis row 14 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-house__"></a>

**dob_bis.14.house__** [fact] dob_bis row 14 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-job__"></a>

**dob_bis.14.job__** [fact] dob_bis row 14 job__: 200827141 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-job_description"></a>

**dob_bis.14.job_description** [fact] dob_bis row 14 job_description: HEREWITH FILING FOR THE INSTALLATION OF A NEW RAMP.  NO CHANGE IN USE,EG RESS OR OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-job_status_descrp"></a>

**dob_bis.14.job_status_descrp** [fact] dob_bis row 14 job_status_descrp: PLAN EXAM - DISAPPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-job_type"></a>

**dob_bis.14.job_type** [fact] dob_bis row 14 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-latest_action_date"></a>

**dob_bis.14.latest_action_date** [fact] dob_bis row 14 latest_action_date: 02/23/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-pre__filing_date"></a>

**dob_bis.14.pre__filing_date** [fact] dob_bis row 14 pre__filing_date: 02/03/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-14-street_name"></a>

**dob_bis.14.street_name** [fact] dob_bis row 14 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/14/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-bbl"></a>

**dob_bis.15.bbl** [fact] dob_bis row 15 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-bin__"></a>

**dob_bis.15.bin__** [fact] dob_bis row 15 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-doc__"></a>

**dob_bis.15.doc__** [fact] dob_bis row 15 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-house__"></a>

**dob_bis.15.house__** [fact] dob_bis row 15 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-job__"></a>

**dob_bis.15.job__** [fact] dob_bis row 15 job__: 200853843 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-job_description"></a>

**dob_bis.15.job_description** [fact] dob_bis row 15 job_description: NON-ILLUMINATED NON ADVERTISISNG ACCESSO RY AWNING READING- COLUMBUS MEDICAL.  NO CHANGE IN USE,EGRE SS OR OCCUPANCY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-job_status_descrp"></a>

**dob_bis.15.job_status_descrp** [fact] dob_bis row 15 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-job_type"></a>

**dob_bis.15.job_type** [fact] dob_bis row 15 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-latest_action_date"></a>

**dob_bis.15.latest_action_date** [fact] dob_bis row 15 latest_action_date: 07/02/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-pre__filing_date"></a>

**dob_bis.15.pre__filing_date** [fact] dob_bis row 15 pre__filing_date: 05/03/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-15-street_name"></a>

**dob_bis.15.street_name** [fact] dob_bis row 15 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/15/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-bbl"></a>

**dob_bis.16.bbl** [fact] dob_bis row 16 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-bin__"></a>

**dob_bis.16.bin__** [fact] dob_bis row 16 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-doc__"></a>

**dob_bis.16.doc__** [fact] dob_bis row 16 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-house__"></a>

**dob_bis.16.house__** [fact] dob_bis row 16 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-job__"></a>

**dob_bis.16.job__** [fact] dob_bis row 16 job__: 200853852 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-job_description"></a>

**dob_bis.16.job_description** [fact] dob_bis row 16 job_description: NON ILLUMINATED NON ADVERTISING ACCESSORY AWNING          READING- COLUMBUS MEDICAL       NO CHANGE TO USE, EGRESS OR OCCUPANCY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-job_status_descrp"></a>

**dob_bis.16.job_status_descrp** [fact] dob_bis row 16 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-job_type"></a>

**dob_bis.16.job_type** [fact] dob_bis row 16 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-latest_action_date"></a>

**dob_bis.16.latest_action_date** [fact] dob_bis row 16 latest_action_date: 07/06/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-pre__filing_date"></a>

**dob_bis.16.pre__filing_date** [fact] dob_bis row 16 pre__filing_date: 05/03/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-16-street_name"></a>

**dob_bis.16.street_name** [fact] dob_bis row 16 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/16/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-bbl"></a>

**dob_bis.17.bbl** [fact] dob_bis row 17 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-bin__"></a>

**dob_bis.17.bin__** [fact] dob_bis row 17 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-doc__"></a>

**dob_bis.17.doc__** [fact] dob_bis row 17 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-house__"></a>

**dob_bis.17.house__** [fact] dob_bis row 17 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-job__"></a>

**dob_bis.17.job__** [fact] dob_bis row 17 job__: 200853861 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-job_description"></a>

**dob_bis.17.job_description** [fact] dob_bis row 17 job_description: NON ILLUMINATED NON ADVERTISING ACCESSORY AWNING        READING- COLUMBUS MEDICAL       NO CHANGE TO USE, EGRESS OR OCCUPANCY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-job_status_descrp"></a>

**dob_bis.17.job_status_descrp** [fact] dob_bis row 17 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-job_type"></a>

**dob_bis.17.job_type** [fact] dob_bis row 17 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-latest_action_date"></a>

**dob_bis.17.latest_action_date** [fact] dob_bis row 17 latest_action_date: 07/06/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-pre__filing_date"></a>

**dob_bis.17.pre__filing_date** [fact] dob_bis row 17 pre__filing_date: 05/03/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-17-street_name"></a>

**dob_bis.17.street_name** [fact] dob_bis row 17 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/17/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-bbl"></a>

**dob_bis.18.bbl** [fact] dob_bis row 18 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-bin__"></a>

**dob_bis.18.bin__** [fact] dob_bis row 18 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-doc__"></a>

**dob_bis.18.doc__** [fact] dob_bis row 18 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-house__"></a>

**dob_bis.18.house__** [fact] dob_bis row 18 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-job__"></a>

**dob_bis.18.job__** [fact] dob_bis row 18 job__: 200853870 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-job_description"></a>

**dob_bis.18.job_description** [fact] dob_bis row 18 job_description: NON ILLUMINATED NON ADVERTISING ACCESSORY AWNING          READING- COLUMBUS MEDICAL           NO CHANGE TO USE, EGRESS OR OCCUPANCY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-job_status_descrp"></a>

**dob_bis.18.job_status_descrp** [fact] dob_bis row 18 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-job_type"></a>

**dob_bis.18.job_type** [fact] dob_bis row 18 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-latest_action_date"></a>

**dob_bis.18.latest_action_date** [fact] dob_bis row 18 latest_action_date: 07/06/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-pre__filing_date"></a>

**dob_bis.18.pre__filing_date** [fact] dob_bis row 18 pre__filing_date: 05/03/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-18-street_name"></a>

**dob_bis.18.street_name** [fact] dob_bis row 18 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/18/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-bbl"></a>

**dob_bis.19.bbl** [fact] dob_bis row 19 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-bin__"></a>

**dob_bis.19.bin__** [fact] dob_bis row 19 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-doc__"></a>

**dob_bis.19.doc__** [fact] dob_bis row 19 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-house__"></a>

**dob_bis.19.house__** [fact] dob_bis row 19 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-job__"></a>

**dob_bis.19.job__** [fact] dob_bis row 19 job__: 200853889 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-job_description"></a>

**dob_bis.19.job_description** [fact] dob_bis row 19 job_description: NON ILLUMINATED NON ADVERTISING ACCESSORY AWNING            READING- 1240 EDWARD L GRANT HIGHWAY        NO CHANGE TO USE, EGRESS OR OCCUPANCY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-job_status_descrp"></a>

**dob_bis.19.job_status_descrp** [fact] dob_bis row 19 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-job_type"></a>

**dob_bis.19.job_type** [fact] dob_bis row 19 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-latest_action_date"></a>

**dob_bis.19.latest_action_date** [fact] dob_bis row 19 latest_action_date: 07/02/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-pre__filing_date"></a>

**dob_bis.19.pre__filing_date** [fact] dob_bis row 19 pre__filing_date: 05/03/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-19-street_name"></a>

**dob_bis.19.street_name** [fact] dob_bis row 19 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/19/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-bbl"></a>

**dob_bis.20.bbl** [fact] dob_bis row 20 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-bin__"></a>

**dob_bis.20.bin__** [fact] dob_bis row 20 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-doc__"></a>

**dob_bis.20.doc__** [fact] dob_bis row 20 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-house__"></a>

**dob_bis.20.house__** [fact] dob_bis row 20 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-job__"></a>

**dob_bis.20.job__** [fact] dob_bis row 20 job__: 200853898 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-job_description"></a>

**dob_bis.20.job_description** [fact] dob_bis row 20 job_description: NON ILLUMINATED NON ADVERTISING ACCESSORY AWNING           READING- COLUMBUS MEDICAL         NO CHANGE TO USE, EGRESS OR OCCUPANCY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-job_status_descrp"></a>

**dob_bis.20.job_status_descrp** [fact] dob_bis row 20 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-job_type"></a>

**dob_bis.20.job_type** [fact] dob_bis row 20 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-latest_action_date"></a>

**dob_bis.20.latest_action_date** [fact] dob_bis row 20 latest_action_date: 07/02/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-pre__filing_date"></a>

**dob_bis.20.pre__filing_date** [fact] dob_bis row 20 pre__filing_date: 05/03/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-20-street_name"></a>

**dob_bis.20.street_name** [fact] dob_bis row 20 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/20/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-bbl"></a>

**dob_bis.21.bbl** [fact] dob_bis row 21 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-bin__"></a>

**dob_bis.21.bin__** [fact] dob_bis row 21 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-doc__"></a>

**dob_bis.21.doc__** [fact] dob_bis row 21 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-house__"></a>

**dob_bis.21.house__** [fact] dob_bis row 21 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-job__"></a>

**dob_bis.21.job__** [fact] dob_bis row 21 job__: 200853941 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-job_description"></a>

**dob_bis.21.job_description** [fact] dob_bis row 21 job_description: NON ILLUMINATED NON ADVERTISING ACCESSORY AWNING           READING- COLUMBUS MEDICAL          NO CHANGE TO USE, EGRESS OR OCCUPANCY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-job_status_descrp"></a>

**dob_bis.21.job_status_descrp** [fact] dob_bis row 21 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-job_type"></a>

**dob_bis.21.job_type** [fact] dob_bis row 21 job_type: A3 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-latest_action_date"></a>

**dob_bis.21.latest_action_date** [fact] dob_bis row 21 latest_action_date: 07/06/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-pre__filing_date"></a>

**dob_bis.21.pre__filing_date** [fact] dob_bis row 21 pre__filing_date: 05/03/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-21-street_name"></a>

**dob_bis.21.street_name** [fact] dob_bis row 21 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/21/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-bbl"></a>

**dob_bis.22.bbl** [fact] dob_bis row 22 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-bin__"></a>

**dob_bis.22.bin__** [fact] dob_bis row 22 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-doc__"></a>

**dob_bis.22.doc__** [fact] dob_bis row 22 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-house__"></a>

**dob_bis.22.house__** [fact] dob_bis row 22 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-job__"></a>

**dob_bis.22.job__** [fact] dob_bis row 22 job__: 200858161 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-job_description"></a>

**dob_bis.22.job_description** [fact] dob_bis row 22 job_description: TO INSTALL FIRE ALARM SYSTEM.  NO CHANGE IN USE,EGRESS OR OCCUPANCY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-job_status_descrp"></a>

**dob_bis.22.job_status_descrp** [fact] dob_bis row 22 job_status_descrp: SIGNED OFF (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-job_type"></a>

**dob_bis.22.job_type** [fact] dob_bis row 22 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-latest_action_date"></a>

**dob_bis.22.latest_action_date** [fact] dob_bis row 22 latest_action_date: 12/29/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-pre__filing_date"></a>

**dob_bis.22.pre__filing_date** [fact] dob_bis row 22 pre__filing_date: 05/19/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-signoff_date"></a>

**dob_bis.22.signoff_date** [fact] dob_bis row 22 signoff_date: 12/29/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/signoff_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-22-street_name"></a>

**dob_bis.22.street_name** [fact] dob_bis row 22 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/22/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-bbl"></a>

**dob_bis.23.bbl** [fact] dob_bis row 23 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-bin__"></a>

**dob_bis.23.bin__** [fact] dob_bis row 23 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-doc__"></a>

**dob_bis.23.doc__** [fact] dob_bis row 23 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-house__"></a>

**dob_bis.23.house__** [fact] dob_bis row 23 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-job__"></a>

**dob_bis.23.job__** [fact] dob_bis row 23 job__: 200872608 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-job_description"></a>

**dob_bis.23.job_description** [fact] dob_bis row 23 job_description: HEREWITH FILING FOR THE INSTALLATION OF NEW RAMP NO CHANGE IN USE,EGRESS OR OCCUPAANCY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-job_status_descrp"></a>

**dob_bis.23.job_status_descrp** [fact] dob_bis row 23 job_status_descrp: PERMIT ISSUED - ENTIRE JOB/WORK (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-job_type"></a>

**dob_bis.23.job_type** [fact] dob_bis row 23 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-latest_action_date"></a>

**dob_bis.23.latest_action_date** [fact] dob_bis row 23 latest_action_date: 12/21/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-pre__filing_date"></a>

**dob_bis.23.pre__filing_date** [fact] dob_bis row 23 pre__filing_date: 08/02/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-23-street_name"></a>

**dob_bis.23.street_name** [fact] dob_bis row 23 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/23/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-bbl"></a>

**dob_bis.24.bbl** [fact] dob_bis row 24 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-bin__"></a>

**dob_bis.24.bin__** [fact] dob_bis row 24 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-doc__"></a>

**dob_bis.24.doc__** [fact] dob_bis row 24 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-house__"></a>

**dob_bis.24.house__** [fact] dob_bis row 24 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-job__"></a>

**dob_bis.24.job__** [fact] dob_bis row 24 job__: 200922369 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-job_description"></a>

**dob_bis.24.job_description** [fact] dob_bis row 24 job_description: TO INSTALL FIRE SUPPRESSION SYSTEM.  NO CHANGE IN USE, EGRESS OR OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-job_status_descrp"></a>

**dob_bis.24.job_status_descrp** [fact] dob_bis row 24 job_status_descrp: PERMIT ISSUED - PARTIAL JOB (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-job_type"></a>

**dob_bis.24.job_type** [fact] dob_bis row 24 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-latest_action_date"></a>

**dob_bis.24.latest_action_date** [fact] dob_bis row 24 latest_action_date: 12/07/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-pre__filing_date"></a>

**dob_bis.24.pre__filing_date** [fact] dob_bis row 24 pre__filing_date: 12/01/2004 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-24-street_name"></a>

**dob_bis.24.street_name** [fact] dob_bis row 24 street_name: EDWARD L GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/24/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-bbl"></a>

**dob_bis.25.bbl** [fact] dob_bis row 25 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-bin__"></a>

**dob_bis.25.bin__** [fact] dob_bis row 25 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-doc__"></a>

**dob_bis.25.doc__** [fact] dob_bis row 25 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-house__"></a>

**dob_bis.25.house__** [fact] dob_bis row 25 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-job__"></a>

**dob_bis.25.job__** [fact] dob_bis row 25 job__: 220464423 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-job_description"></a>

**dob_bis.25.job_description** [fact] dob_bis row 25 job_description: APPLICATION IS FILED FOR THE INSTALLATION OF HVAC UNIT ON THE ROOF AND ALSO OBTAIN EQUIPMENT USE PERMIT CARDS AFTER SIGN/OFF. NO CHANGE IN USE, EGRESS OR OCCUPANCY DUE TO SCOPE OF WORK. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-job_status_descrp"></a>

**dob_bis.25.job_status_descrp** [fact] dob_bis row 25 job_status_descrp: PLAN EXAM - APPROVED (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-job_type"></a>

**dob_bis.25.job_type** [fact] dob_bis row 25 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-latest_action_date"></a>

**dob_bis.25.latest_action_date** [fact] dob_bis row 25 latest_action_date: 06/19/2015 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-pre__filing_date"></a>

**dob_bis.25.pre__filing_date** [fact] dob_bis row 25 pre__filing_date: 06/18/2015 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-25-street_name"></a>

**dob_bis.25.street_name** [fact] dob_bis row 25 street_name: EDWARD GRANT HIGHWAY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/25/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-bbl"></a>

**dob_bis.26.bbl** [fact] dob_bis row 26 bbl: 2028710002 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/bbl`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-bin__"></a>

**dob_bis.26.bin__** [fact] dob_bis row 26 bin__: 2008638 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/bin__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-doc__"></a>

**dob_bis.26.doc__** [fact] dob_bis row 26 doc__: 01 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/doc__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-house__"></a>

**dob_bis.26.house__** [fact] dob_bis row 26 house__: 1240 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/house__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-job__"></a>

**dob_bis.26.job__** [fact] dob_bis row 26 job__: 240116815 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/job__`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-job_description"></a>

**dob_bis.26.job_description** [fact] dob_bis row 26 job_description: FILING TO CONVERT SCHOOL TO HALL. NO CHANGE IN USE, EGRESS AND OCCUPANCY. (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/job_description`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-job_status_descrp"></a>

**dob_bis.26.job_status_descrp** [fact] dob_bis row 26 job_status_descrp: APPLICATION PROCESSED - ENTIRE (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/job_status_descrp`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-job_type"></a>

**dob_bis.26.job_type** [fact] dob_bis row 26 job_type: A2 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/job_type`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-latest_action_date"></a>

**dob_bis.26.latest_action_date** [fact] dob_bis row 26 latest_action_date: 10/02/2015 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/latest_action_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-pre__filing_date"></a>

**dob_bis.26.pre__filing_date** [fact] dob_bis row 26 pre__filing_date: 10/02/2015 (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/pre__filing_date`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_bis-26-street_name"></a>

**dob_bis.26.street_name** [fact] dob_bis row 26 street_name: EDWARD L GRANT HWY (source value)

Source: [dob_bis raw response](sources/dob_bis.json), JSON pointer `/26/street_name`; SHA256 `6eabf3fdc65c337a84bf42236095688938c8990395831efab7873b1adbcec565`. [Exact request](https://data.cityofnewyork.us/resource/ic3t-wcy2.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob__%2Cdoc__%2Cjob_type%2Cjob_status_descrp%2Cpre__filing_date%2Clatest_action_date%2Csignoff_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin__%2Chouse__%2Cstreet_name&%24order=job__%2Cdoc__&%24limit=501).

<a id="dob_now-returned_rows"></a>

**dob_now.returned_rows** [calculation] dob_now returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [dob_now raw response](sources/dob_now.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/w9ak-ipjd.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cjob_filing_number%2Cjob_type%2Cfiling_status%2Cfiling_date%2Ccurrent_status_date%2Cexisting_dwelling_units%2Cproposed_dwelling_units%2Cjob_description%2Cbin%2Chouse_no%2Cstreet_name&%24order=job_filing_number&%24limit=501).

Bounded query; see truncation and source limits.

<a id="hpd_violations-returned_rows"></a>

**hpd_violations.returned_rows** [calculation] hpd_violations returned rows in this exact-BBL query: 0 (returned rows; not projects or total population)

Source: [hpd_violations raw response](sources/hpd_violations.json), JSON pointer `/`; SHA256 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`. [Exact request](https://data.cityofnewyork.us/resource/wvxf-dwi5.json?%24where=bbl%3D%272028710002%27&%24select=bbl%2Cviolationid%2Cinspectiondate%2Cclass%2Cviolationstatus%2Ccurrentstatus%2Cnovdescription%2Cbin&%24order=violationid&%24limit=501).

Bounded query; see truncation and source limits.

<a id="scenario-gross_area_sf"></a>

**scenario.gross_area_sf** [assumption] gross_area_sf: 40000 (gross sf)

Demonstration input chosen to exercise the workflow; not derived from zoning or verified drawings.

<a id="scenario-nonresidential_gross_sf"></a>

**scenario.nonresidential_gross_sf** [assumption] nonresidential_gross_sf: 6000 (gross sf)

Demonstration allocation to nonresidential uses; not a tenant commitment or displacement assessment.

<a id="scenario-residential_net_efficiency"></a>

**scenario.residential_net_efficiency** [assumption] residential_net_efficiency: 0.8 (share)

Hypothetical net residential share after circulation/support; no layout verified.

<a id="scenario-average_net_home_sf"></a>

**scenario.average_net_home_sf** [assumption] average_net_home_sf: 800 (net sf per home-equivalent)

Hypothetical average home size; no unit mix or code compliance established.

<a id="scenario-residential_gross_sf"></a>

**scenario.residential_gross_sf** [calculation] Residential gross area allocation: 34000.0 (gross sf)

Depends on: [scenario.gross_area_sf](#scenario-gross_area_sf), [scenario.nonresidential_gross_sf](#scenario-nonresidential_gross_sf).

User-stated area budget; not a verified design or entitlement.

<a id="scenario-residential_net_sf"></a>

**scenario.residential_net_sf** [calculation] Residential net area allowance: 27200.0 (net sf)

Depends on: [scenario.residential_gross_sf](#scenario-residential_gross_sf), [scenario.residential_net_efficiency](#scenario-residential_net_efficiency).

User-stated area budget; not a verified design or entitlement.

<a id="scenario-home_equivalents"></a>

**scenario.home_equivalents** [calculation] Area-budget home-equivalents: 34.0 (home-equivalents; not a feasible unit count)

Depends on: [scenario.residential_net_sf](#scenario-residential_net_sf), [scenario.average_net_home_sf](#scenario-average_net_home_sf).

User-stated area budget; not a verified design or entitlement.

<a id="scenario-gross_to_recorded_lot_ratio"></a>

**scenario.gross_to_recorded_lot_ratio** [calculation] Proposed gross area / recorded lot area: 0.6773920406435224 (gross-to-lot ratio; NOT zoning FAR)

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

<a id="review-housing_signals"></a>

**review.housing_signals** [judgment] Reconcile heterogeneous housing evidence: reconciliation_needed (unreviewed author policy)

Depends on: [dob_bis.12.proposed_dwelling_units](#dob_bis-12-proposed_dwelling_units), [pluto.0.unitsres](#pluto-0-unitsres).

DOB historical existing/proposed units and PLUTO recorded units are different observations. Preserve all positive signals; obtain approved plans, certificates and current-use evidence before concluding occupancy or displacement. No units are summed across filings.

<a id="review-next_diligence"></a>

**review.next_diligence** [judgment] Questions for practitioner review: Review current-use evidence, entitlement pathway, physical constraints and capital structure. (unreviewed author policy)

Depends on: [unknown.current_use](#unknown-current_use), [unknown.entitlement](#unknown-entitlement), [unknown.physical_fit](#unknown-physical_fit), [unknown.finance](#unknown-finance).

A checklist for discussion. Task cost, timing, actor resources and best ordering are not evaluated.

## Source limits and terms

- **pluto** — Tax-lot attributes may lag actual conditions. Zoning fields are recorded descriptors, not a legal entitlement analysis. Zero recorded residential units does not mean vacancy or no displacement. [Publisher dataset](https://data.cityofnewyork.us/d/64uk-42ks). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **dob_bis** — Legacy job/document rows, not unique projects or verified current use. Historical existing/proposed units are not current lawful dwellings. Exact-BBL queries miss unlinked filings and historical lot changes. [Publisher dataset](https://data.cityofnewyork.us/d/ic3t-wcy2). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **dob_now** — DOB NOW filing rows are not completed projects or a complete pipeline. Exact-BBL lookup only; missing rows do not establish no activity. [Publisher dataset](https://data.cityofnewyork.us/d/w9ak-ipjd). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
- **hpd_violations** — Recorded housing violation rows, not occupancy, executed evictions, or a displacement measure. Empty results do not prove no housing, no violations, or a safe building. [Publisher dataset](https://data.cityofnewyork.us/d/wvxf-dwi5). [Terms](https://opendata.cityofnewyork.us/overview/#termsofuse).
