# Source-bound exploratory geometry

Read the [specification](../docs/specs/geometry-grounding.md). This optional module
connects a real mapped parcel, explicit design assumptions and a verified analysis
packet. It produces a simple building volume and checks whether its area quantities
agree with the analysis. It does not determine a lawful or physically feasible design.

## Try the retained real-lot example

Python 3.11+, from the repository root:

```sh
python -m pip install -r requirements-geometry.txt
python -m housing_geometry build --analysis examples/analysis-recipe/base --parcel-source examples/geometry-inputs/parcel-source --scenario examples/geometry-inputs/all-nonresidential-ground.json --out runs/geometry-mismatch
python -m housing_geometry build --analysis examples/analysis-recipe/base --parcel-source examples/geometry-inputs/parcel-source --scenario examples/geometry-inputs/mixed-ground-allocation.json --out runs/geometry-allocation
python -m housing_geometry verify --run runs/geometry-allocation
```

Open `packet.html` in each directory. Build and verify are offline. For fresh DCP
source retrieval, use `python -m housing_geometry collect --bbl 2028710002 --out
runs/new-parcel-source`. Geometry source bytes change across retrievals; scenario
coordinates are bound to the exact parcel response SHA, not just a BBL or version.
A new source requires explicit coordinate-frame review/rebinding.

The first example totals 40,000 gross-floor-proxy sf, matching the model, but
allocates 7,500 nonresidential sf instead of 6,000: **visual handoff blocked**.
The second explicitly assumes 80% of the ground floor is nonresidential and 20%
residential. Its totals match, but this is an arithmetic sensitivity, not a working
mixed-use layout. Neither example derives a building from zoning, the photo or a
professional proposal. The dimensions were chosen algebraically to match the old
40,000-sf budget. All professional gates remain unknown.

## Inputs and supported scope

- A complete verified `housing_recipe` or `housing_workflow` run, with canonical
  gross-area, nonresidential gross-area and residential gross-area claims. No agency
  document importer or custom gross/net unit relabeling is supplied.
- DCP parcel response plus layer/item metadata and query/hash/retrieval receipts.
  One simple parcel ring only. Holes and multipart parcels block rather than disappear.
- A strict [scenario contract](scenario.schema.json): source geometry hash, BBL,
  exploratory origin, explicit closed convex floor footprints, floor-to-floor
  heights, fractional use allocations and rationales. All inputs are assumptions.

The local frame subtracts the source ring's minimum native X/Y and converts native
EPSG:2263 US survey feet to international feet. X east, Y north, Z up. The base
Z=0 is an assumed flat datum. No terrain elevation is implied. A formula and original
source coordinates are retained. Coordinates are not latitude/longitude.

Floor plates must be within the mapped parcel and upper plates within the previous
plate. Convex plates only in the current triangular mesh exporter. Technical bounds
(1–30 floors, 5–30-ft floor heights) are supported-input limits, not zoning rules.
No setbacks from legally interpreted lot lines, yards, lot coverage, permitted
height, easements, structures or adjacent buildings are checked.

## Outputs

- `geometry.json`: source facts, coordinate transform, assumed-floor bindings,
  calculated areas/mesh, analysis-linked comparisons, unknown review gates.
- `floor-schedule.csv`: gross/residential/nonresidential proxies and elevations.
- `massing.obj`: triangulated floor solids in local international feet. Floor-solid
  interfaces are retained; this is schematic, not a watertight fabrication/BIM model.
- `plan.svg`, `massing.svg`: deterministic schematic views. Plan is north up;
  axonometric camera is arbitrary and is not the user's Street View camera.
- Portable HTML/Markdown packet and versioned `visual-handoff.json`.
- Complete `analysis-run/`, `parcel-source/`, scenario and implementation/hash manifest.

The manifest binds Shapely/GEOS versions because geometry-library behavior is part
of the implementation. Install the pinned dependency; runtime changes require an
explicit rebuild. A build never overwrites a populated directory. Verification
recompiles all outputs and checks complete retained upstream packages.

## Reconciliation and backpressure

Gross polygon area is a declared proxy for scenario gross area. It is not zoning
floor area, net residential area or an architectural measurement. Floor shares are
arithmetic use allocations, not floor plans. No home count is inferred from the mesh.

Each comparison retains the original analysis claim ID, kind, rationale and IR hash.
Gross and two program-allocation checks run separately. A tolerance of at most 1 sf
is an authored numerical policy. A mismatch produces diagnostic outputs but suppresses
the handoff prompt. A match permits **schematic reference only**; zoning, survey,
access/egress/layout, structure/geotechnical, finance, existing context, photo-camera
registration and professional review all remain unknown.

The mapped polygon area differs from recorded LotArea. Both stay visible, as does
the prior analysis's source version. Equal Version labels are not certified release
equivalence. No recorded value is overwritten with a calculated geometry area.

## Rendering boundary

This module generates no AI image. The existing photo-concept module does not yet
consume the geometry handoff; its current prompts remain independent design assumptions.
A future adapter must deliver mesh/views/depth/masks as appropriate to the image
provider and record a fidelity review. A mesh in a JSON packet alone does not constrain
an image model. Photo registration and existing city context remain separate missing
inputs, and an attractive image cannot clear professional review gates.

The module uses Shapely for established polygon validity/containment operations.
Source data remains subject to NYC/DCP terms; see parcel-source/receipt.json and
[project source boundaries](../DATA-LICENSES.md). No Google image is used or copied
in this geometry example.
