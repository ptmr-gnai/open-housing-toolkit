---
name: start-here
description: Route a housing practitioner or coding agent to the right toolkit module, check prerequisites, and guide verified handoffs. Use for a first visit, a known-lot investigation, modeling, report preparation or imagery.
---

# Start here

Read [AGENTS.md](../../AGENTS.md). Work from a writable checkout with Python 3.11+.
Choose the user's task first; an independent module does not require the full tour.

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

For output locations and Mac/Windows status, read [storage and platforms](../../docs/storage-and-platforms.md).
The [active catalogue](../catalog.json) distinguishes current playbooks from frozen
historical instructions. Native host-menu installation is not implemented.
