---
name: build-grounded-massing
description: Build explicit assumed massing on a sourced real parcel and reconcile areas against a verified analysis packet.
---

Read docs/specs/geometry-grounding.md and housing_geometry/README.md. Install the
optional geometry dependency with `python -m pip install -r requirements-geometry.txt`.
Keep mapped boundaries, exploratory design choices and professional judgments distinct.

Use a verified housing_recipe or housing_workflow run with canonical gross-area
claims. Collect a Bronx parcel using `python -m housing_geometry collect --bbl
2028710002 --out runs/parcel-source`, or replay the retained example sources.

Supply a scenario JSON following the examples. Coordinates are local international
feet in the source-bound frame; never treat latitude/longitude as planar feet.
Footprints, heights and floor-use fractions must have explicit rationales. Do not
infer dimensions or a legal envelope from a street photograph.

Build into a new directory, verify, and inspect the total-area AND program-allocation
comparisons. A total match can coexist with a program mismatch. Read all unknown
review gates. Diagnostic SVG views can be inspected when mismatched; visual handoff
must stay blocked. A consistent result is eligible only as a schematic reference.

Do not invoke the current photo renderer as though it consumes this geometry contract.
No automatic geometry-conditioned image-generation adapter or fidelity review exists.
Preserve mesh, source bytes, assumptions, model bindings and the original analysis.
