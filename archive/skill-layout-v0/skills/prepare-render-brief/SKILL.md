---
name: prepare-render-brief
description: Convert an explicit visual scenario and supplied reference scene into a provider-independent building-render brief. Analysis is optional; collection and modeling modules are not required.
---

# Prepare a site-concept render brief

Use `housing_render` independently from the parcel-analysis workflow. Read `workflows/site-concept.json`. Requires Python 3.11+ recommended, no pip dependencies. See `examples/site-concept/scene.json` and `scenario.json` for the strict canonical contracts; validation rejects missing or extra fields. The current visual parameters are explicit assumptions/preferences, not inferred legal capacity.

```sh
python -m housing_render prepare --scene scene.json --scenario scenario.json --out runs/concept
```

For a local photo set reference availability to `local_file` and add `--photo /path/to/site.jpg`. The module copies and hashes the image. For a reference available only in the conversation, declare `conversation_attachment`; its original bytes are unavailable to the executable module and no source hash may be invented. Before generating, the agent must actually resolve the declared attachment. Ask for it again only if it is no longer available.

Optionally add `--analysis /path/to/ir.json`. The adapter reads canonical claim IDs and references for site context and requires the same parcel. This does not certify the imported analysis, and it does not reconcile its area budget with an assumed story count/footprint. Existing analysis can be skipped completely. Automated agency-document conversion is future work.

Inspect `render-brief.json`, `prompt.txt`, and `brief.md`. The prompt is compiled from scene/scenario fields; do not add unrecorded design instructions at generation time. To change a scenario, save a new input and prepare a new run. The versioned workflow is partial and records missing geometry, approvals, occupancy and funding.
