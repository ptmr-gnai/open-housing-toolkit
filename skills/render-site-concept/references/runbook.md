# render-site-concept: execution reference

Working directory: repository root. This skill requires the checkout; it is not
a standalone installed bundle. Treat all example commands as examples; substitute
the user's actual paths/inputs. Read the relevant section below before execution.

## Canonical resources (read only as needed)

- [Module guide](../../../src/housing_render/README.md): commands, outputs and supported scope.
- [CLI implementation](../../../src/housing_render/__main__.py): existing executable entry point; run from the checkout root.
- [Scene example](../../../examples/site-concept/scene.json) and [scenario example](../../../examples/site-concept/scenario.json): formats only; not facts about a new site.
- [Actual invocation example](../../../examples/site-concept/with-analysis/invocation.json) and [review example](../../../examples/site-concept/with-analysis/review.json): record actual execution, never copy invented facts.

## Detailed procedure and boundaries
# Render and inspect a site concept

Start with an existing `housing_render` run; data collection is not required. Run `python -m housing_render verify --run runs/concept` and read its `render-brief.json`. Resolve the declared reference image. A conversation attachment is usable by a conversation image tool but cannot be claimed locally byte-bound.

Give the image provider exactly the brief's `prompt`. For the image_gen tool use `referenced_image_paths` for a local photo. For conversation-only images use the smallest `num_last_images_to_include` that includes the original supplied photograph; extra recent generated images are not source evidence. Inspect an unseen local image before editing it. Preserve attribution. Do not invent street numbers or upgrade assumptions to verified geometry.

Record the actual provider, parameter object, execution time, reference selection, prompt SHA256 and render-brief SHA256 in an invocation JSON. Do not print base64 image data. Save the provider output as a file. Do not claim that a stochastic generator can reproduce identical pixels from a prompt.

Visually inspect the generated image and write a review JSON covering exactly: reference_setting, story_count, caption, invented_site_details, geometry_fidelity. Each check has id, status (consistent_by_inspection, issue_observed, not_verified) and note. Identify reviewer_kind as assistant_visual_inspection or human_visual_inspection. Geometry fidelity stays not_verified. A caption saying six stories does not prove six floors were rendered; describe visible evidence and ambiguity.

```sh
python -m housing_render attach --run runs/concept --image output.png --invocation invocation.json --review review.json
python -m housing_render verify --run runs/concept
```

This copies the generated asset and binds it to the brief, scenario, scene, optional imported analysis, actual invocation and review. A review is an attributed attestation, not cryptographic proof of execution or professional acceptance. Preserve outputs with issues; create a new run for a revision rather than rewriting the earlier result.

Local artifact creation does not authorize sending emails or submitting proposals. Rendering an assumed concept does not clear site availability, occupancy, zoning, building fit or finance.
