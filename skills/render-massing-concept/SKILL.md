---
name: render-massing-concept
description: Make a photorealistic concept picture of a verified massing on a real site photo (e.g. a Street View screenshot), with the prompt compiled from the massing's numbers and a to-scale elevation drawing as the second reference. Use whenever a lot has a massing and the user wants a picture.
---

# Render a massing-grounded concept

The picture must show the building the model describes: same stories, height,
ground-floor width and upper-floor setback, replacing what is on the lot today.
This module compiles the prompt from a verified massing and renders three reference
views of it (3D from across the street, a to-scale front elevation, a site plan); you
only choose a style and a ground-floor use from short lists.

## Inputs and preflight

A verified massing package, the user's site photo or Street View screenshot (PNG or
JPEG) with its provider and date, an image tool (Codex `image_gen`), and
`.venv/bin/python` from the repository root.

## Execute

Read [the execution reference](references/runbook.md). Prepare, then generate ONE
image with the four reference images in the order `prepare` prints (photo, 3D
massing, elevation, site plan), passing `prompt.txt` exactly as written. Do not add to or rewrite the prompt. Fill in the review honestly
and attach. If the story count or the removal of the existing buildings is wrong,
generate again from the same prompt instead of editing the image or the prompt.

## Validate and hand off

`verify` checks the prompt and elevation against the massing and binds the image.
Pass the package to the report with `--render`. Anything you want to say about the
picture goes in an agent note (`housing_feasibility brief note`).

## Limits

An illustration, not a design: no survey, camera registration or zoning envelope.
A third-party photo stays out of shared bundles by default.
