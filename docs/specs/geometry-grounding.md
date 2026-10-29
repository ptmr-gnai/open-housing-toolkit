# Geometry grounding: connect a real site, an explicit scenario and visual assets

Status: thin vertical slice specification, 29 October 2026. The intended user is
a housing practitioner investigating a known lot and developing a proposal packet.
Professional workflow completeness and usefulness are not yet established.

## Problem and goal

The current area recipe and photo-based illustration describe separate assumptions.
A prompt asking for six stories does not establish footprint, floor area, boundaries
or fidelity to the analytical scenario. A persuasive image can hide that gap.

Build an inspectable bridge: **source evidence → interpreted constraints/objectives
→ proposed scenario → dimensioned geometry → area reconciliation → visual brief
→ generated asset → fidelity review**. A discrepancy feeds back into the scenario
and model. Geometry is an intermediate representation, not evidence of feasibility.

The immediate goal is a reproducible, dimensioned building volume on a mapped real
parcel, with calculated floor areas compared to a verified analysis run. Source
facts, design assumptions, calculations and unverified judgments remain separate.
The immediate deliverables are a massing view, plan, machine-readable geometry,
interchange mesh, floor schedule, reconciliation report and a geometry-bound visual
handoff. A new photorealistic image is not required for this step.

## What grounds what

| Grounding requirement | Required inputs | Current state / acceptance boundary |
| --- | --- | --- |
| Right site | BBL, mapped polygon, address match, source version; eventually survey | Query one mapped tax lot by exact BBL; match analysis BBL. Mapping is not a surveyed legal boundary. |
| Existing surroundings | Neighbor footprints/heights, terrain, dated imagery | Not available in this slice. Do not invent existing-building or street context. |
| Explicit proposed shape | Footprints, floor heights, floor count, upper-floor changes, coordinate frame | Practitioner-supplied or declared design assumptions; never extracted from a single photo by assertion. |
| Agreement with analysis | Floor areas, program allocation, target gross area, common definitions | Sum modeled floor polygons; compare to scenario.gross_area_sf. Gross polygon area is a simplified floor-plate proxy, not zoning floor area or a code-compliant measured schedule. |
| Program agreement | Residential/nonresidential floor areas and analysis allocations | Compare floor-use allocations, without inferring layouts, efficiency or homes from the mesh. |
| Zoning plausibility | Districts, overlays, text, special rules, approval pathway, versioned interpretation | Remains unknown; geometry does not silently convert recorded FAR into legal capacity. |
| Physical plausibility | Survey, access, egress, plans, structure, geotechnical/site constraints | Remains unknown. Polygon containment is only a mapped-geometry test. |
| Financial/program plausibility | Unit mix, agency requirements, cost and financing models | Remains unknown; preserve upstream limits. |
| Visual fidelity | Mesh, coordinate frame, camera, imagery, materials, output review | Produce schematic view and an explicit handoff, not automatic photo conditioning or a geometry-fidelity certificate. |

## Three scenario origins

1. Practitioner-supplied proposed design: retain author and source.
2. Scenario generated under interpreted constraints: retain interpretations and method.
3. Exploratory scenario: retain every design assumption and its rationale.

P0 implements only the third. These statuses must not collapse into an undifferentiated
"realistic" label. A precise mesh of an assumed design is still an assumed design.

## First vertical slice

Use BBL 2028710002, the same lot as the analysis example. Collect and retain one
NYC DCP MapPLUTO polygon plus service/item metadata and query/version/hash receipts.
Reject missing/duplicate/wrong-parcel/invalid-CRS/truncated geometry. Support one
simple closed ring only initially; reject holes and multipart rather than drop them.

Use native EPSG:2263 planar coordinates, translated to a local origin and converted
from US survey feet to international feet by an explicit factor. Never treat
longitude/latitude as feet. Preserve the reversible coordinate transform and original
source coordinates. Existing numeric "sf" values lack survey-unit precision; compare
under a declared numerical tolerance, without claiming survey accuracy.

Accept an explicitly assumed replacement footprint as local XY vertices, floor
heights, repeated floor plates, use labels and an upper-floor footprint change.
No existing structure is being certified for vertical extension. No street frontage
or photo camera is inferred. The design must be contained in the mapped parcel;
upper plates must be contained in the preceding plate in this limited slice.

For the demonstration, select dimensions algebraically to match the existing
40,000 gross-sf scenario: one 7,500-sf ground floor and five 6,500-sf upper floors.
This is a constructed consistency example, NOT an independently derived design or
proof that 40,000 sf fits professional constraints. Program allocation intentionally
gets a separate check against the 6,000 nonresidential-sf analysis assumption: an
all-nonresidential ground floor creates a visible mismatch even though total gross
area matches. Do not adjust the analysis behind the scenes to force a pass.

Generate floor-by-floor areas/heights, an OBJ mesh, site-plan and axonometric SVGs,
portable HTML/Markdown packet, typed IR and JSON visual handoff. Link every derived
area to its floor polygon and compare gross and residential/nonresidential allocation
against the source analysis. Bind geometry, scenario, analysis and source hashes.

## Deterministic backpressure

- Strict input contracts, numeric bounds, polygon validity and non-overwriting runs.
- Reject self-intersections, missing units, unsupported geometry, parcel mismatch,
  footprints crossing boundaries, unsupported uses and unsafe file references.
- Explicit area-definition compatibility. No automatic comparison of zoning FAR,
  net residential area or total building area to a gross-floor proxy.
- Numeric reconciliation tolerance is an authored policy, not a professional standard.
- Mismatches produce a diagnostic packet and block a positive visual handoff. An
  assumed massing can be viewed for investigation even when unreconciled.
- Zoning/physical/finance/context/photo-camera review stays unknown even on a numeric
  match. "Consistent within tolerance" is never named "feasible" or "approved".
- Changing source bytes, shape, floor count, height, area target or implementation
  invalidates the prior run. Verification recomputes mesh, reports and exports.

## Acceptance experiments

1. Replay the same retained inputs in a new directory with byte-identical outputs.
2. Construct the above 40,000-sf example: gross matches, allocation mismatch is flagged.
3. Supply explicit mixed ground-floor use allocation to match 6,000 nonresidential
   sf and 34,000 residential sf, without changing the old analysis. Declare that
   allocation is arithmetic, not an architectural layout.
4. Change a footprint dimension/floor count; geometry, floor schedule and comparisons
   must update, with a mismatch blocking a positive visual handoff.
5. Reject wrong BBL, geographic CRS, invalid/outside polygons, missing provenance,
   altered output and rehashed stale geometry.

## Modularity and future work

New housing_geometry module consumes a verified housing_recipe or housing_workflow
run and retained parcel geometry. It does not modify those modules or old experiments.
The P0 adapter expects their canonical gross-area scenario claims; a universal
agency-model importer is P1. The visual handoff is standalone and versioned; it is
not automatically accepted by the current photo-concept renderer. That adapter,
geometry/depth/mask conditioning and fidelity review are subsequent work.

Later: surveys, more polygon types, neighboring buildings/terrain, camera registration,
constraint-derived scenarios with professional interpretations, layout/egress/structure,
affordability/finance and approved program checks. Valdrada or other scene tools can
be optional context adapters. Expert review must determine whether these contracts
represent useful professional work; integrity tests cannot decide that.

## Source references

- NYC DCP MapPLUTO service: https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/arcgis/rest/services/MAPPLUTO/FeatureServer/0
- DCP_GIS item metadata: https://www.arcgis.com/home/item.html?id=1564ace0b4f44318ac39920737f9bd07
- NYC source terms: https://www.nyc.gov/home/terms-of-use.page

Live retrieval must record service metadata and returned feature Version. Do not
assume that another endpoint called MapPLUTO has the same release; discovery found
an official gazetteer endpoint whose description still references 2018 inputs.
