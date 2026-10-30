# build-grounded-massing: execution reference

Working directory: repository root. This skill requires the checkout; it is not
a standalone installed bundle. Treat all example commands as examples; substitute
the user's actual paths/inputs. Read the relevant section below before execution.

## Canonical resources (read only as needed)

- [Module guide](../../../src/housing_geometry/README.md): commands, outputs and supported scope.
- [CLI implementation](../../../src/housing_geometry/__main__.py): existing executable entry point; run from the checkout root.

## Detailed procedure and boundaries
Read docs/specs/geometry-grounding.md and src/housing_geometry/README.md. Install the
optional geometry dependency with `python -m pip install -e ".[geometry]"`.
Keep mapped boundaries, exploratory design choices and professional judgments distinct.

Use a verified housing_recipe or housing_workflow run with canonical gross-area
claims. Collect a Bronx parcel using `python -m housing_geometry collect --bbl 2028710002 --out runs/parcel-source`, or replay the retained example sources.

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

## Explicit build and verify example

Using the retained parcel source and a deliberately assumed scenario:

```sh
python -m housing_geometry build --analysis examples/analysis-recipe/base --parcel-source examples/geometry-inputs/parcel-source --scenario examples/geometry-inputs/mixed-ground-allocation.json --out runs/my-massing
python -m housing_geometry verify --run runs/my-massing
```

This example assumes a mixed ground-floor use allocation. The module guide
describes the supported inputs and the separate allocation mismatch demonstration.
