# Open Housing Toolkit — Claude Code

Read [AGENTS.md](AGENTS.md), then [the start-here skill](skills/start-here/SKILL.md).
For "install this", "let's start" or a new user, follow
[first visit](skills/start-here/references/first-visit.md).
For other uncertain, broad or whole-flow requests follow the
[practitioner guide](skills/start-here/SKILL.md#practitioner-guide), including
conversational intake and resumable stage status. Use the shared repository skills and Python commands; no separate Claude plugin
installation is required for this checkout-based workflow.

For this project's current Claude Code path, image generation is unavailable.
Prepare and verify the render brief, prompt and accessible reference assets, then
hand the package back as `brief_prepared`. When preflight found Codex on this
computer, offer the user a ready sentence to paste into Codex to generate it. Do not
request an image API key, install an image integration, or invent a generation receipt. The other supported modules
work independently of image generation.

See [runtime routing and preflight](skills/start-here/references/agent-runtimes.md).

User-run inputs, outputs and reviews stay in fresh local runs/ folders or a chosen
external local folder. Never regenerate shipped data/examples or commit/push/upload
results unless the user explicitly requests that publication for this task.
