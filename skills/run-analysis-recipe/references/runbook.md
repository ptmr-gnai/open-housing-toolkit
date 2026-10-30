# run-analysis-recipe: execution reference

Working directory: repository root. This skill requires the checkout; it is not
a standalone installed bundle. Treat all example commands as examples; substitute
the user's actual paths/inputs. Read the relevant section below before execution.

## Canonical resources (read only as needed)

- [Module guide](../../../src/housing_recipe/README.md): commands, outputs and supported scope.
- [CLI implementation](../../../src/housing_recipe/__main__.py): existing executable entry point; run from the checkout root.

## Detailed procedure and boundaries
Use for a housing practitioner investigating a known lot. Begin with a verified
`housing_workflow` run. Preserve that evidence and its original packet.

1. Copy `config/recipes/area-budget.json` and explain all edited assumptions. Methods are
   allowlisted and versioned; never substitute a net-area denominator into a gross-area method.
2. Build with `python -m housing_recipe build --from-run examples/parcel-investigation --recipe config/recipes/area-budget.json --out runs/recipe-base`.
3. Before changing a recipe, run `python -m housing_recipe impact --run runs/recipe-base --recipe config/recipes/area-budget-with-reserve.json`.
4. Build the changed recipe into a new directory. Inspect `trace.json`, `ir.json`,
   `calculation-steps.csv`, and `packet.html`. Verify with `python -m housing_recipe verify --run runs/recipe-base`.

Never edit a completed run in place, remove professional review gates, or claim
that a successful type check establishes appropriate methods, legal capacity,
physical fit, funded feasibility or complete agency process coverage. The current
recipe expresses numerical area methods, not arbitrary econometrics or judgments.
A new method needs code, semantic input/output types, validation and a new version.
Image prompts remain diagrams; no new streetscape generation is part of this skill.
