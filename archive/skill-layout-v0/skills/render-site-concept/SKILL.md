---
name: render-site-concept
description: Generate an illustrative building concept from a prepared render brief, then attach the image and an explicit visual-review receipt using any compatible image provider.
---

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
