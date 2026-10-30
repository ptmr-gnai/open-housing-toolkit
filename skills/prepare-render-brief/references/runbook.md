# prepare-render-brief: execution reference

Working directory: repository root. This skill requires the checkout; it is not
a standalone installed bundle. Treat all example commands as examples; substitute
the user's actual paths/inputs. Read the relevant section below before execution.

## Canonical resources (read only as needed)

- [Module guide](../../../src/housing_render/README.md): commands, outputs and supported scope.
- [CLI implementation](../../../src/housing_render/__main__.py): existing executable entry point; run from the checkout root.
- [Scene example](../../../examples/site-concept/scene.json) and [scenario example](../../../examples/site-concept/scenario.json): formats only; not facts about a new site.
- [Actual invocation example](../../../examples/site-concept/with-analysis/invocation.json) and [review example](../../../examples/site-concept/with-analysis/review.json): record actual execution, never copy invented facts.

## Detailed procedure and boundaries
# Prepare a site-concept render brief

Use `housing_render` independently from the parcel-analysis workflow. Read `config/workflows/site-concept.json`. Requires Python 3.11+ recommended, no pip dependencies. See `examples/site-concept/scene.json` and `scenario.json` for the strict canonical contracts; validation rejects missing or extra fields. The current visual parameters are explicit assumptions/preferences, not inferred legal capacity.

```sh
python -m housing_render prepare --scene scene.json --scenario scenario.json --out runs/concept
```

For a local photo set reference availability to `local_file` and add `--photo /path/to/site.jpg`. The module copies and hashes the image. For a reference available only in the conversation, declare `conversation_attachment`; its original bytes are unavailable to the executable module and no source hash may be invented. Before generating, the agent must actually resolve the declared attachment. Ask for it again only if it is no longer available.

Optionally add `--analysis /path/to/ir.json`. The adapter reads canonical claim IDs and references for site context and requires the same parcel. This does not certify the imported analysis, and it does not reconcile its area budget with an assumed story count/footprint. Existing analysis can be skipped completely. Automated agency-document conversion is future work.

Inspect `render-brief.json`, `prompt.txt`, and `brief.md`. The prompt is compiled from scene/scenario fields; do not add unrecorded design instructions at generation time. To change a scenario, save a new input and prepare a new run. The versioned workflow is partial and records missing geometry, approvals, occupancy and funding.
