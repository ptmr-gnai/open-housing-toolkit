# Modular photo-referenced site concepts

This module takes a **scene and an explicitly assumed visual scenario** and compiles an image-provider-independent prompt. Collection and modeling are optional. It then attaches an externally generated image and a visual review, preserving the links between inputs, brief, invocation and output.

The executable commands use the Python standard library. Image generation is a separate provider/tool call performed by an agent using the skill or by a compatible provider adapter; the CLI does not pretend to include a free image service.

## Start without the analysis modules

From the repository root, Python 3.11+ recommended:

```sh
python -m housing_render prepare \
  --scene examples/site-concept/scene.json \
  --scenario examples/site-concept/scenario.json \
  --out runs/my-concept
```

This prepares a brief using the example's external conversation reference. To generate with your own photo, copy the scene/scenario JSON, identify the correct site and inputs, set reference availability to `local_file`, and add `--photo /path/to/site.jpg`. Local PNG/JPEG bytes are copied and hashed. An external conversation attachment must actually be available to the agent; this module cannot recover it from an address or pretend its bytes are locally bound.

Read `render-brief.json`, `prompt.txt` and `brief.md`. Give the agent [prepare-render-brief](../skills/prepare-render-brief/SKILL.md) and [render-site-concept](../skills/render-site-concept/SKILL.md). The latter describes the image-tool invocation and explicit review contract.

## Add analysis context when useful

```sh
python -m housing_render prepare \
  --scene examples/site-concept/scene.json \
  --scenario examples/site-concept/scenario.json \
  --analysis examples/parcel-investigation/ir.json \
  --out runs/concept-with-analysis
```

The adapter accepts canonical analysis JSON and requires the same tax lot. It retains selected cited parcel facts as context; it does not infer geometry or legal capacity from them. The earlier 40,000-sf/34-home-equivalent area budget is **not reconciled** to the six-story visual assumption. Each design parameter states its kind and rationale. Automatic conversion of agency workbooks, PDFs or other formats is future work.

The renderer CLI can run without the analysis package; a test exercises it with `housing_workflow/` absent. New packages bind the active rendering skills and their references. Current operational playbooks under `skills/` link shared resources and require the repository checkout; they are not standalone portable bundles. Retained examples are checked by the archived original verifier without rewriting their historical bindings.

## Generate, inspect and attach

The provider receives exactly the compiled prompt and declared reference assets. An invocation record has provider, prompt_sha256, brief_sha256, reference_id, reference_delivery, parameters, executed_at and execution_note. A review has reviewer_kind, summary and five checks: reference_setting, story_count, caption, invented_site_details, geometry_fidelity. See the committed real example for complete JSON shapes.

```sh
python -m housing_render attach --run runs/my-concept \
  --image generated.png --invocation invocation.json --review review.json
python -m housing_render verify --run runs/my-concept
```

Outputs include copied inputs, the optional analysis snapshot, render brief, exact prompt, image, invocation, review, generation receipt, readable packet and manifest. The receipt hashes the image, prompt, scenario, scene, optional analysis and review. Editing the brief stales the invocation. A different site is rejected. Prior generations cannot be overwritten; prepare a new run for revisions.

Review is an attributed visual inspection, not cryptographic proof of provider execution or professional acceptance. Exact image pixels are not reproducible from a stochastic generation call. Geometry fidelity remains unverified in this slice, even when the caption and apparent architectural scale look plausible.

## Real example and limits

[The generated example](../examples/site-concept/with-analysis/packet.md) used the user-supplied Street View attachment, six explicitly assumed stories and optional site-context facts from our parcel IR. The module compiled the prompt and it was submitted unchanged to image_gen.imagegen. Three recent conversation images were supplied to include the original screenshot; prior concepts were also in that context. Original-only conditioning cannot be independently audited.

The source screenshot's original bytes are not in the repository. Its attribution and visible June 2026 date are recorded as user-supplied metadata. The generated image is retained, but the source-byte binding is explicitly false. Reproduction of the source-conditioned call requires the original attachment. Other users can supply a local file to establish a source hash.

The visual is a replacement concept; it does not show an approved design or prove that the old structure can carry more floors. No footprint, height in feet, setbacks, area or lawful/current use is verified. GIS geometry, measured massing, automated imagery acquisition and city-twin adapters are future scene providers, not implemented capabilities. Source imagery/attribution are excluded from the project's blanket code/documentation licenses; see DATA-LICENSES.md.

```sh
python -m housing_render verify --run examples/site-concept/with-analysis
python -m housing_render verify --run examples/site-concept/standalone
python -m unittest discover -s housing_render/tests -v
```
