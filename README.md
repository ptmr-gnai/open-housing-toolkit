# Open Housing Toolkit

Open tools for housing practitioners and their coding agents: find candidate
lots, investigate a lot, work through explicit scenarios, and prepare a cited
review packet. Sources, assumptions and calculations stay inspectable. Experts
guide interpretation.

**Early research prototype.** It produces evidence and conditional analysis;
professional usefulness, feasibility and submission readiness remain unvalidated.

## What it does

| Stage | Question | Status | Start |
| --- | --- | --- | --- |
| 1. Find candidate lots | Which lots in an area are recorded as nonhousing, and what zoning path applies? | Working v1 | [Find sites](docs/guides/discover-sites.md) |
| 2. Investigate a lot | What do public records say about this Bronx lot? | Working | [Investigate a lot](docs/guides/investigate-a-lot.md) |
| 3. Model scenarios | Could a stated program and financing work here? | Experimental: needs expert assumptions | [Status](docs/status.md#3-model-scenarios) |

**[Where things stand, and open questions for practitioners →](docs/status.md)**

## Start here

[Set up the checkout once](docs/guides/setup.md). The editable install makes the
modules in src/ available to the existing Python commands; it does not rebuild data.

**Searching for sites?** Open [Find sites](docs/guides/discover-sites.md). Give your
agent an area and a question; it lists every recorded nonhousing lot with its general
zoning path and the follow-up questions each one raises.

**Have a lot?** Open [Investigate a lot](docs/guides/investigate-a-lot.md). Give your Codex
or Claude Code agent a Bronx address or tax-lot identifier (BBL) and your question.
That guide covers the inputs, sequence, stopping points and final handoff.

**Want a quick tour first?** From a checkout with Python 3.11+:

```sh
python scripts/first_run.py --out runs/my-first-run
```

Open `runs/my-first-run/README.md`. The tour uses saved public records and needs
no API key, optional dependencies or image tool after setup. [Setup and troubleshooting](docs/guides/first-run.md).

New runs stay local. Shipped examples and source snapshots are read-only; setup
needs no development rebuild. Nothing is automatically committed, pushed or uploaded.
[Local-only execution and checks](docs/guides/local-only.md).

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

The [module catalogue](docs/reference/module-catalog.md) covers area lot discovery,
parcel collection, rental underwriting, goal-seeking site search, editable
area recipes, offer comparisons, RER preparation, assumed geometry and rendering.
They can be used independently. Codex uses its image tool when available; the
current Claude Code path prepares/exports the render brief.

For agents: [AGENTS.md](AGENTS.md) → [start-here](skills/start-here/SKILL.md).
For project principles and methods: [tenets](docs/reference/tenets.md) ·
[community-benefit proposal](docs/reference/specs/community-benefit.md).
For output storage and operating-system support: [storage and platforms](docs/guides/storage-and-platforms.md).

Repository map: [code, configuration, research and local runs](docs/reference/repository-layout.md).
