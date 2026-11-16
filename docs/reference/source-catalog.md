# Source catalog

Reference list of canonical public sources for NYC parcel and property research.
It is a **candidate catalog, not an acquisition list**. Each module fetches only
the sources declared in its own code and records them in its run receipts; a
source moves from candidate to wired-in when a module actually fetches it.
Written October 2026 alongside the [ownership module](../../src/housing_ownership/README.md);
the newer lot-discovery sources are listed in
[public-source coverage](../../research/nonhousing-discovery/sources.md).

Status key: **wired-in** = fetched by the current evidence pipeline;
**candidate** = identified, not yet acquired.

ID key: **confirmed** = verified against the toolkit's own run URLs or a live
search; **re-verify** = from domain knowledge, confirm the Socrata ID before
wiring in; **valdrada** = ID verified against the Valdrada project's fetch code
(see the Valdrada section below).

## Wired-in

| Source | ID / endpoint | Publisher | Role | ID |
| --- | --- | --- | --- | --- |
| PLUTO | `64uk-42ks` | NYC Dept. of City Planning | Parcel identity, owner label (derivative), geometry | confirmed |
| ACRIS Real Property Legals | `8h5j-fqxa` | NYC ACRIS (Open Data mirror) | Recorded instrument legal descriptions | confirmed |
| ACRIS Master | `bnx9-e6tj` | NYC ACRIS (Open Data mirror) | Instrument index rows | confirmed |
| ACRIS Parties | `636b-3b5g` | NYC ACRIS (Open Data mirror) | Grantor/grantee party rows | confirmed |
| DOF Property Sales | `w2pb-icbu` | NYC Dept. of Finance | Reported sale price and date | confirmed |
| DOB NOW job metadata | `w9ak-ipjd` | NYC Dept. of Buildings | Filing metadata only | confirmed |
| DOB legacy BIS job filings | `ic3t-wcy2` | NYC Dept. of Buildings | Legacy filings; not DOB NOW coverage | confirmed |
| HPD violations metadata | `wvxf-dwi5` | NYC HPD | Metadata only, not yet a fetched feed | confirmed |
| E-designation metadata | `hxm3-23vy` | NYC Dept. of City Planning | Environmental designation metadata | confirmed |
| MTA Stations | GitHub raw + `data.ny.gov` | MTA New York City Transit | Station reference coordinates | confirmed |

## Candidates by domain

### Title / recorded instruments (completeness gap)

| Source | ID / endpoint | Publisher | Why it matters | ID |
| --- | --- | --- | --- | --- |
| ACRIS primary system | `nycacris.org` | NYC ACRIS | The system of record. The Open Data mirror is a subset (1966+, Staten Island excluded, no document images), so "empty mirror" is weaker than "empty primary." | n/a |
| NYC API portal | `api-portal.nyc.gov` | NYC (Azure API Mgmt) | Official gateway for ACRIS and other city APIs. | n/a |

### Ownership / assessment (current-owner gap)

| Source | ID / endpoint | Publisher | Why it matters | ID |
| --- | --- | --- | --- | --- |
| **DOF Property Tax Roll** | `8y4t-faws` | NYC Dept. of Finance | **Official current owner of record + assessed value.** Highest-value addition: replaces the `current_owner: unknown` gap with a sourced claim. | confirmed |
| NYC Tax Map | `dof.nyc.gov` | NYC Dept. of Finance | Canonical lot geometry; interactive, no API. | n/a |

### Zoning / entitlements

| Source | ID / endpoint | Publisher | Why it matters | ID |
| --- | --- | --- | --- | --- |
| ZoLa zoning & land-use map | `zola.planning.nyc.gov` | NYC Dept. of City Planning | Official zoning map; GeoJSON/shapefile download. | n/a |
| DCP Lot Boundaries | DCP resources | NYC Dept. of City Planning | Lot geometry (GeoJSON/shapefile). | n/a |
| DCP Building Footprints | DCP resources | NYC Dept. of City Planning | Building geometry. | n/a |
| Zoning Resolution | `zr.planning.nyc.gov` | NYC Dept. of City Planning | Law text; toolkit already cites one section. | n/a |
| DCP Special Districts | DCP resources | NYC Dept. of City Planning | Overlay district rules. | n/a |

### Construction / compliance

| Source | ID / endpoint | Publisher | Why it matters | ID |
| --- | --- | --- | --- | --- |
| **DOB Building Permits** | `3n4p-7z4t` | NYC Dept. of Buildings | Canonical permit/units record. The backtest found a 2003 DOB filing recording 9 units the graph missed; permits are the authoritative source, not NOW metadata. | confirmed |
| DOB Violations | `235p-7d6h` | NYC Dept. of Buildings | Open-violation signal. | re-verify |
| DOB NOW full filings | `a810-dobnow.nyc.gov` | NYC Dept. of Buildings | Full filings; toolkit currently pulls catalog metadata only. | n/a |

### Housing / rental

| Source | ID / endpoint | Publisher | Why it matters | ID |
| --- | --- | --- | --- | --- |
| HPD Rental Registration DB | (confirm ID) | NYC HPD | Canonical registered units/owners. | re-verify |
| HPD HMC Complaints | `33f7-nh35` | NYC HPD | Condition signal. | re-verify |
| NYC Housing Court (HCR) | HCR data portal | NYC Admin. Trials | Eviction / housing-court records. | n/a |

### Context / environmental

| Source | ID / endpoint | Publisher | Why it matters | ID |
| --- | --- | --- | --- | --- |
| FEMA NFHL | `fema.gov/flood-maps/national-flood-hazard-layer` | FEMA | Flood hazard. | n/a |
| LPC Landmarks | LPC datasets | NYC Landmarks Pres. Comm. | Designated landmarks. | n/a |
| NYC 311 | `311` dataset | NYC 311 | Service-request signal. | n/a |
| US Census TIGER / ACS | census.gov | US Census Bureau | Geography + demographics. | n/a |

### Entity resolution (state)

| Source | ID / endpoint | Publisher | Why it matters | ID |
| --- | --- | --- | --- | --- |
| NY State DOS Corporate Records | `nydos.ny.gov` (web; no clean public API) | NY State Dept. of State | Deed grantees are often LLCs/corporations; DOS resolves the entity behind a grantee — needed before any "current owner" claim is meaningful. | n/a |

### Commercial (not public; cross-checks only)

CoreLogic, Attom Data Solutions (deeds), Zillow/Redfin (listings). Paid, not
part of a public-reproducibility story. Useful as independent cross-checks only.

## From Valdrada provenance

Source: [mkturkcan/valdrada](https://github.com/mkturkcan/valdrada), a city-scale
NYC digital twin (WebGL renderer + traffic/pedestrian sim) compiled entirely
from public municipal records. Its `client/DATA_SOURCES.md` is a fully
provenanced table of every ingested dataset. All Socrata IDs below are verified
against Valdrada's fetch code; non-Socrata endpoints are as documented in its
`DATA_SOURCES.md`. None are wired into this toolkit yet — recorded here so their
value to property research can be assessed. Valdrada is a rendering/simulation
project, so several of its sources bear on physical/site context rather than on
ownership or title; the rendering-only asset libraries are listed last and do
not bear on property research.

### Building / physical

| Source | ID / endpoint | Publisher | What it gives us | ID |
| --- | --- | --- | --- | --- |
| **Building Footprints (BUILDING)** | `5zhs-2jue` | NYC Dept. of City Planning | Footprint polygon, `height_roof`, `ground_elevation`, `construction_year`, `bin`, `mappluto_bbl`. Grounds massing/unit-count in real geometry instead of FAR×area; joins to BBL. | valdrada |
| **NYC 3D Building Model (DoITT)** | `maps.nyc.gov/download/3dmodel/DA_WISE_GML.zip` (CityGML LOD2) | NYC Dept. of City Planning | Real roof forms / massing. Heavy; Valdrada uses it for landmarks only. | doc |
| **FISP facade filings (LL11)** | `xubg-57si` | NYC Dept. of Buildings | Real facade material per building (masonry/terra cotta/stone/concrete/curtain wall). Mandatory for buildings >6 stories → condition + renovation signal. | valdrada |
| **Microsoft Global ML Footprints** | `minedbuildings.z5.web.core.windows.net/global-buildings/` (ODbL) | Microsoft | Gap-fill footprints + estimated heights where DOITT is missing. | doc |
| **Drinking-water tank inspections** | (BIN list) | NYC DEP | Rooftop tanks → physical / roof-load signal. | doc |
| **Green-roof inventory** | Treglia et al., The Nature Conservancy 2016 | TNC | Green-roof footprints per BIN. | doc |
| **Roofpedia** | Wu & Biljecki, Landscape & Urban Planning 214, 2021 | academic | Detected green + solar roofs per BIN. | doc |
| **NYSERDA distributed solar** | NYSERDA | NY State | Rooftop solar locations + module counts. | doc |

### Site / ground / access

| Source | ID / endpoint | Publisher | What it gives us | ID |
| --- | --- | --- | --- | --- |
| **Street Centerlines (CSCL)** | `inkn-q76z` | NYC DOT | Street width, lane counts, direction, speed, bike lanes, per-vertex ramp elevation → frontage + access. | valdrada |
| **Planimetric: Sidewalk** | `52n9-sdep` | NYC DOT | Walk polygons → site/open-space geometry. | valdrada |
| **Planimetric: Roadbed** | `i36f-5ih7` | NYC DOT | Roadbed polygons. | valdrada |
| **Planimetric: Median** | `ees7-4ufv` | NYC DOT | Median polygons. | valdrada |
| **Planimetric: Parking Lot** | `7cgt-uhhz` | NYC DOT | Parking-lot polygons. | valdrada |
| **Planimetric: Public Plazas** | `ue2e-9jm2` | NYC DOT | Plaza polygons. | valdrada |
| **Planimetric: Open Space** | `y6ja-fw4f`, `b7j8-z8a7` | NYC DOT | Open-space polygons. | valdrada |
| **Parks Properties** | `enfh-gkve` | NYC Parks | Park polygons → adjacency + open space. | valdrada |
| **Borough Boundaries** | `gthc-hcne` | NYC | Land polygons → base geography / water mask. | valdrada |
| **Railroad Lines (Planimetric)** | `anc7-97cy` | NYC DOT | Rail centerlines + feature code (at-grade/elevated/viaduct/open cut) → rail proximity/noise. | valdrada |
| **MTA Subway Entrances (2024)** | `i9wp-a4ja` (data.ny.gov) | MTA | Entrance stair positions — more precise pedestrian access than station points. | valdrada |
| **Bus Stop Shelters** | `t4f2-8md7` | NYC DOT | Shelter positions/orientation. | valdrada |
| **Bus Lanes – Local Streets** | `ycrg-ses3` | NYC DOT | Red-lane segments. | valdrada |
| **DOT Bicycle Parking (CityRacks)** | `592z-n7dk` | NYC DOT | Bike-rack positions. | valdrada |
| **LinkNYC Kiosks** | `s4kf-3yrf` | NYC DOT | Kiosk positions. | valdrada |
| **NYCDEP Citywide Hydrants** | `5bgh-vtsn` | NYC DEP | Hydrant positions. | valdrada |
| **2015 Street Tree Census** | `uvpi-gqnh` | NYC Parks | Street-tree species + size. | valdrada |
| **Forestry Tree Points** | `hn5i-inap` | NYC Parks | Current street trees (updated daily). | valdrada |

### Terrain / environmental

| Source | ID / endpoint | Publisher | What it gives us | ID |
| --- | --- | --- | --- | --- |
| **NYC 2017 LiDAR bare-earth DEM** | `7sc8-jtbz` (15.6 GB) | NYC | 1 ft citywide terrain → grading, flood, cut/fill. Large; defer. | valdrada |
| **USGS 3DEP 1 m / 1/3-arc DEM** | National Map API (`tnmaccess.nationalmap.gov`) | USGS | Public-domain elevation, incl. NJ backdrop. | doc |
| **NOAA ENC** | `encdirect.noaa.gov` | NOAA | Water depth / chart coverage → waterfront sites only. | doc |
| **USGS NAIP orthoimagery** | `imagery.nationalmap.gov` | USGS | Aerial imagery (tree crowns, site context). | doc |
| **NYS ITS orthoimagery** | `orthos.its.ny.gov` (2022–25 mosaic) | NY State | Recent aerials. | doc |

### Gap-fill / cross-check

| Source | ID / endpoint | Publisher | What it gives us | ID |
| --- | --- | --- | --- | --- |
| **OSM building footprints + `building:colour`** | Overpass API (ODbL) | OpenStreetMap | Footprints DOITT lacks + literal facade colours. | doc |
| **OSM land polygons** | `osmdata.openstreetmap.de` (ODbL) | OpenStreetMap | Coastline land polygons. | doc |

### Evaluated and rejected by Valdrada

- **Google Street View** — ideal for facade appearance; licensing prohibits extraction.
- **Mapillary** (CC-BY-SA) — viable for facade colour via API + segmentation; not implemented.
- **LPC designation reports** — facade material exists but only in unstructured PDFs.

### Asset libraries (rendering only; not property data)

Valdrada also ingests CC0/CC-BY texture, model and animation libraries that do
not bear on property research: Poly Haven and ambientCG (PBR textures, HDRI
skies), CARLA 0.9/0.10 (vehicles, pedestrians, props), Objaverse/Sketchfab
(photogrammetry scans), Microsoft Rocketbox (avatars), 100STYLE (locomotion),
Google Fonts (sign typefaces), ez-tree (parametric trees). Recorded for
completeness of the provenance; not candidates for this toolkit.

## Notes

- The ACRIS Open Data mirror vs. the ACRIS primary system is a real coverage
  difference. Record it as a limitation rather than treating the mirror as the
  whole of record.
- None of these sources establish title. They are evidence feeds. The DOF tax
  roll gets closest to a defensible "current owner," but unrecorded interests
  still require the ACRIS primary plus DOS entity resolution.
- Socrata IDs are stable but should be re-verified once before a source is
  wired in. Rows marked **re-verify** have not been confirmed against a live
  endpoint.
- When a source is promoted to acquisition, add its publisher's terms to
  `DATA-LICENSES.md`.
- The Valdrada-provenance section is a candidate inventory, not an endorsement:
  Valdrada is a rendering/simulation project, so its sources were chosen for
  visual fidelity, not for property research. Assess each against the four
  verification questions (right source, accurate extraction, correct
  interpretation, sufficient coverage) before wiring any in. ODbL sources
  (OpenStreetMap, Microsoft Global ML footprints) carry attribution and
  share-alike obligations on any published derived work.
