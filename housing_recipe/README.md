# Editable analysis recipes

The first user is a housing practitioner or member of the housing community with
domain knowledge. The hero task is: **here is a lot → evaluate it → model a
scenario → prepare a proposal-development packet and assets**. Area discovery is
an upstream extension. The practitioner chooses assumptions and methods and
remains responsible for interpretation. This numerical slice does not establish
that the complete professional process is known.

## Run the thin slice

From the repository root, Python 3.11+, standard library only, offline:

```sh
python -m housing_recipe build --from-run examples/parcel-investigation --recipe recipes/area-budget.json --out runs/recipe-base
python -m housing_recipe impact --run runs/recipe-base --recipe recipes/area-budget-with-reserve.json
python -m housing_recipe build --from-run runs/recipe-base --recipe recipes/area-budget-with-reserve.json --out runs/recipe-reserve
python -m housing_recipe build --from-run runs/recipe-base --recipe recipes/area-budget-gross-method.json --out runs/recipe-gross
python -m housing_recipe verify --run runs/recipe-reserve
```

Open `runs/recipe-reserve/packet.html`. Each output directory must be new. A live
lot can first be collected with `housing_workflow`; this module accepts its verified
run instead of repeating collection. Give an agent
[the recipe skill](../skills/current/run-analysis-recipe/SKILL.md).

## What changes, and what stays visible

- Base: (40,000 − 6,000) × 0.8 ÷ 800 = **34 home-equivalents**.
- Insert a step: reserve another assumed 4,000 gross sf before efficiency:
  (34,000 − 4,000) × 0.8 ÷ 800 = **30 home-equivalents**. This reserve is a
  deliberately selected sensitivity, not an architect's estimate. Check for
  double counting with efficiency.
- Replace a method: 34,000 residential gross sf ÷ assumed 1,000 gross sf per
  home-equivalent = **34 home-equivalents**. The result happens to match, but
  the method, denominator type and dependencies differ. That change stays visible.

No figure is a physically feasible or permitted unit count. Current use, title,
entitlement, physical fit, environment, finance, transit and process-coverage
review gates remain unknown. Method appropriateness is not machine certified.

## Contracts and deterministic backpressure

`recipe.json` declares recipe ID/revision, assumptions with rationales and semantic
types, selected source imports, method-version steps, dependencies, missing-input
policies and review gates. See [the schema](recipe.schema.json) and
[the method registry](methods.py). Runtime validation does not require jsonschema.

The executor orders steps by dependency, rejects cycles, duplicate/overwritten
claims, unknown methods, missing inputs, invalid arithmetic and incompatible
types. Gross sf and net sf are distinct types. Code execution and arbitrary
network URLs are not supported in recipe JSON. Additional methods require code,
explicit signatures, validation and a method version; JSON configuration alone
cannot implement a new econometric estimator.

Only the reviewed PLUTO recorded-lot-area import is supported in this slice.
Failed/missing PLUTO can skip the optional recorded-lot ratio, with a visible trace
entry; required area outputs cannot be skipped. Professional review gates cannot
be removed. Existing facts, citations, historical housing signals, unknowns and
judgments are retained. A source judgment depending on a replaced scenario blocks
execution pending explicit reconciliation.

`impact` previews changed nodes and their transitive dependents before rebuilding,
including changes to methods that leave the numeric answer unchanged. Every
recipe change requires regenerated IR, trace, packet, CSV and image brief. Editing
a completed run makes verification fail. A new run recomputes everything; this is
not an incremental execution/cache engine and does not automatically monitor files.

## Outputs and provenance

Each run contains a complete verified original `evidence-run/`, its source bytes,
`recipe.json`, `trace.json`, a new `ir.json`, CSV, Markdown/HTML packet, diagram-only
image brief, origin receipt and a hash inventory with implementation bindings.
The original request belongs to the retained evidence run; the new recipe is the
authoritative scenario input. `analysis_recipe` in the new IR binds its canonical
recipe SHA256 and revision. The new IR adds that field to the evidence IR shape;
use this module's verifier, not the original closed 0.2.0 evidence IR schema.

The original evidence packet is preserved unchanged, including its old scenario.
It is not the packet to use for the new scenario. Source bodies are duplicated at
the top level solely so relative citation links work in the new packet; verification
requires identical copies. The origin's parent-manifest hash records lineage,
not an independently authenticated assertion about a missing parent run.

The existing renderer can consume the new IR for site context, but numerical
area and physical massing remain unreconciled. This slice generates no new image.

## Boundaries

This makes the existing numerical modeling stage replaceable. It is not a general
agency workflow engine, an econometric library, a document importer, or professional
validation. New qualitative steps, source adapters, constraints and professional
judgments still require explicit contracts and implementation. Future expert
examples should guide those additions. Practitioner usability remains untested.
