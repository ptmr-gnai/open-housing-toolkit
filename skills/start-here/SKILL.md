---
name: start-here
description: Route a housing practitioner or coding agent to the right toolkit module, check prerequisites, and guide verified handoffs. Use for a first visit, a known-lot investigation, modeling, report preparation or imagery.
---

# Start here

Read [AGENTS.md](../../AGENTS.md). Work from an editable checkout with Python 3.11+; read [setup](../../docs/guides/setup.md) if not installed.
Choose the user's task first; an independent module does not require the full tour.
Default to a local user run: no shipped-data regeneration and no commits, pushes
or uploads. Setup does not require development builds/checks. Use fresh ignored
outputs and follow [the local-only policy](../../docs/guides/local-only.md).
A site-only address or BBL without an outcome needs the guided outcome menu, not
the narrow evidence shortcut. For first-time, site-only, uncertain, broad and
full-flow requests, follow [the practitioner guide](references/full-flow.md) and
keep its stage ledger. For an explicitly narrower live known-lot workflow, read [Investigate a lot](../../docs/guides/investigate-a-lot.md).
It collects the inputs and sequences existing modules. Return the linked cover-note
template as a reviewer-authored handoff; do not claim it is automatically verified.

1. **Preflight:** read [runtime branches](references/agent-runtimes.md) for the chosen
   task. Codex can use its included image tool; Claude Code currently exports a brief.
2. **Route:** read [the module map](references/modules.md) and load only the selected
   current leaf skill. Missing inputs remain missing; ask only what that task needs.
3. **Execute:** follow that skill's steps and load its execution reference when
   needed. Reuse the existing Python CLI/scripts and preserve all prior runs.
4. **Gate:** verify the actual package before handing it to the next module. Stop
   on validation failure; never use chat memory as proof of a completed stage.
5. **Return:** state what ran, absolute output paths, source vintage, assumptions,
   material gaps and next practitioner questions. Technical checks do not establish
   professional correctness, usefulness, feasibility or compliance.

For a first-time tour, read [the offline walkthrough](references/tour.md), then run
[the shared script](../../scripts/first_run.py) in a new directory. Do not preload
all leaf skills before a tour; the script enforces its fixed sequence.

For output locations and Mac/Windows status, read [storage and platforms](../../docs/guides/storage-and-platforms.md).
The [active catalogue](../catalog.json) distinguishes current playbooks from frozen
historical instructions. Native host-menu installation is not implemented.

## Practitioner guide

For a first-time, uncertain or broad request, read and follow the
[practitioner guide](references/full-flow.md). Welcome and teach in plain language,
use supplied information and guide the next decisions without repeating intake.
For a whole flow, continue beyond evidence, and record and resume applicable stages.
Independent and evidence-only requests keep their own scope.

## Full-flow requests

The [practitioner guide](references/full-flow.md) is the canonical full-flow route.
