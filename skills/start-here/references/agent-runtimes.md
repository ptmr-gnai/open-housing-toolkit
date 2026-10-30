# Supported coding-agent paths and preflight

These are the two supported project configurations, not universal claims about
all installations of either product. Read this before starting the selected task.
No shell command can reliably establish which image tools an agent has.

| Runtime | Analysis / packets | Optional image request |
| --- | --- | --- |
| Codex with its included image tool | Shared Python modules and skills | Prepare → invoke available image tool → inspect → attach → verify |
| Claude Code, current project configuration | Same modules and skills | Prepare → verify → export; image generation is deferred |

Neither path needs a separately configured image-provider API key for the work
supported here. The toolkit does not supply an image API client. Codex's tool is a
host capability, not a Python dependency or a secret to discover in the environment.

Primary workflow: Codex on the user's Mac with its included image tool. No
separate image API setup or hosted application is required. Save generated images
and their prompt/reference/review records in the local run; do not publish them.

## Task-specific preflight

1. Identify the requested outcome. A rendering-only request does not require the
   parcel, recipe, comparison or RER tour. Ask only for necessary missing inputs.
2. Confirm a writable checkout, repository root, Python 3.11+ and a fresh output
   directory. Do not overwrite previous runs.
3. For live collection, establish HTTPS access and a BBL or unique supported
   address. Offline replay needs no network. A failed API request is not zero data.
4. For geometry, check/install the pinned optional dependency as appropriate to the
   user's task. Geometry is not required merely to prepare a photo concept.
5. For a render, obtain the supported scene/scenario inputs and resolve the actual
   reference image. Prefer a local PNG/JPEG to bind source bytes. The repository's
   conversation-attachment example does not provide a reusable source photograph.
   Missing assets require supplied assets; do not substitute an unrelated example.
6. Route by the agent runtime. In Codex, confirm the image tool is actually exposed
   and supports the required references. In Claude Code, take the export path.
   If the Codex tool is unexpectedly unavailable, explicitly tell the user that
   image generation is unavailable here and offer the export fallback when its inputs
   exist. If no photo was supplied, ask for a real site photo or a supplied Street
   View screenshot and the intended concept; do not invent a design or a prepared brief. Do not request credentials to compensate.

Before running, state the selected task, prerequisites found/missing, route and
expected output. This is an agent-observed preflight, not an implemented automatic
capability detector. No additional permission question is needed for already
requested local preparation or generation.

## Render branch: common preparation

Read [prepare-render-brief](../../prepare-render-brief/SKILL.md). Supply the scene
and explicit scenario; analysis context is optional. Prepare into a fresh directory
and run `python -m housing_render verify --run YOUR_RUN`. Inspect `brief.md`,
`prompt.txt` and `render-brief.json`. A valid brief can exist without an accessible
conversation photo; verify that asset separately before promising generation.

## Codex: generate when requested

Read [render-site-concept](../../render-site-concept/SKILL.md) and the current host
image-tool instructions. Use the exact compiled prompt and declared reference,
inspect an unseen local image first, and use the host-supported reference mechanism.
Do not assume a particular tool name or argument schema exists in every Codex host.
Record the actual invocation, inspect the output and attach it using the module's
receipt/review contract. Do not reuse a previous image as a fresh generation or
invent provider metadata. A provider failure preserves the prepared brief; report
that failure without claiming a generated image.

## Claude Code: export without generation

Stop after successful preparation/verification. Deliver the complete prepared run
folder, not just a copied prompt: inputs, accessible reference, brief, workflow and
manifest retain their bindings. Name the three readable/useful entry files:
`brief.md`, `prompt.txt`, `render-brief.json`. State `stage: brief_prepared`,
`generation: deferred`, `reason: no image tool in current Claude Code path` in the
handoff explanation. These explanation fields do not change the module's IR schema.
Do not create image, invocation, review or generation-receipt placeholders.

A person can take the package to Codex with image access and resume at verify →
render → inspect → attach. Any external-only reference must also be supplied.
An external image application can use the prompt, but an image alone does not
reconstruct a trustworthy execution record. Record only known settings/actions;
never fabricate them to satisfy the attachment validator.

The prepared run is already a useful successful deliverable. Geometry users can
also retain deterministic plan/massing SVGs without any image-generation service.
Exact camera registration, metric image fidelity, zoning and feasibility remain
unverified regardless of runtime.
