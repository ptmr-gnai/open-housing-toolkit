# Open Housing Toolkit

Open tools for housing practitioners and their coding agents: investigate a lot,
work through explicit scenarios, and prepare a cited review packet. Sources,
assumptions and calculations stay inspectable. Experts guide interpretation.

**Early research prototype.** It produces evidence and conditional analysis;
professional usefulness, feasibility and submission readiness remain unvalidated.

## Start here

**Have a lot?** Open [Investigate a lot](docs/investigate-a-lot.md). Give your Codex
or Claude Code agent a Bronx address or tax-lot identifier (BBL) and your question.
That guide covers the inputs, sequence, stopping points and final handoff.

**Want a quick tour first?** From a checkout with Python 3.11+:

```sh
python scripts/first_run.py --out runs/my-first-run
```

Open `runs/my-first-run/README.md`. The tour uses saved public records and needs
no API key, pip packages or image tool. [Setup and troubleshooting](docs/first-run.md).

New runs stay local. Shipped examples and source snapshots are read-only; setup
needs no development rebuild. Nothing is automatically committed, pushed or uploaded.
[Local-only execution and checks](docs/local-only.md).

## What you get

A short cover note answering your question, linked evidence and calculations,
machine-readable inputs/results, and explicit missing information. The agent
prepares that cover note; it is not a separate validated analytical module.
Without a supplied development scenario, the useful result is an evidence packet.
Photos and explicit visual assumptions enable optional image branches.

[See a real live-lot example](examples/live-lot-trial/README.md): evidence → area
model → independent rental offers → incomplete Racial Equity Report drafts.
The supplied offers are not derived from site capacity or established as fitting.

## Use the parts you need

The [module catalogue](docs/module-catalog.md) covers parcel collection, editable
area recipes, offer comparisons, RER preparation, assumed geometry and rendering.
They can be used independently. Codex uses its image tool when available; the
current Claude Code path prepares/exports the render brief.

For agents: [AGENTS.md](AGENTS.md) → [start-here](skills/start-here/SKILL.md).
For project principles and methods: [tenets](docs/tenets.md) ·
[community-benefit proposal](docs/specs/community-benefit.md).
For output storage and operating-system support: [storage and platforms](docs/storage-and-platforms.md).
