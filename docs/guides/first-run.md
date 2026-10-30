# First visit: practitioner and agent walkthrough

Give your coding agent this instruction:

> Read AGENTS.md and skills/start-here/SKILL.md. Run the offline walkthrough in a
> fresh directory, explain each stage and its limits, then help me choose the next
> task. Do not invent missing housing inputs.

First follow [checkout setup](setup.md) with Python 3.11+. This is a repository-based
workflow. From your activated, installed checkout:

```sh
python --version
python scripts/first_run.py --out runs/my-first-run
```

Use the activated environment from setup. No API key, image model or network
access is needed for replay after the editable install. Open
`runs/my-first-run/README.md`, then `runs/my-first-run/rer/packet.html`. On GitHub,
[the committed Markdown packet](../../examples/rer-preparation/packet.md) works
without running anything; HTML previews show source.

The walkthrough builds four modules in order, passing verified outputs downstream:
cached parcel evidence → editable area arithmetic → independently supplied
illustrative housing offers → incomplete RER preparation drafts. Read the earlier
packets as well as the final draft. The 24/36-home offers are not derived from the
34-home-equivalent area budget. Historical affordability references are not current
program rules. No feasibility, eligibility, optimal program or compliance is found.

## Codex and Claude Code

Both use the same modules and skills. Codex starts from AGENTS.md; Claude Code
starts from [CLAUDE.md](../../CLAUDE.md), which routes to the shared instructions.
For optional images, Codex uses its included image tool when available. Claude
Code currently prepares and exports a verified render brief without generating
an image. Neither path requires a separately configured image API key. The offline
walkthrough above needs no image tool in either environment.

Follow [task-specific preflight and the render branches](../../skills/start-here/references/agent-runtimes.md).
There is no automatic runtime detector; the agent checks its exposed tools and
required inputs. Image generation is not a prerequisite for the other modules.

For exact output locations, hosted-workspace behavior and current Mac/Windows
support, read [storage and platforms](storage-and-platforms.md).

## Reading the replay

Start with the short final RER index and coverage, then follow specific source or
calculation links instead of reading the long evidence packet line by line. Earlier
historical packet text such as "queried four NYC public datasets" describes the
retained collection, not a network call during replay. Newly built parcel/recipe
packets now state their execution mode and source dates in a short opening. Read
source receipts for actual retrieval dates. The RER request retains its supplied sample preparation
date (2026-10-29); it is not automatically replaced by today's date. For your own
work, create a new request with your actual preparer/date and rebuild.

## What to inspect

- Trace one cost result to its offer, utilities, hypothetical income and source.
- Compare Program A and B separately: more total homes does not mean more homes
  meeting this particular lower-income profile's test.
- In the RER map, find the missing EDDE information and unresolved guide/form
  interpretation. Five section headings do not make a completed official report.
- Tell us which input, method, output or next task differs from your actual work.
  A real internal packet or model can guide future adapters; it is not yet an
  automatically supported input format.

## Troubleshooting and independent modules

`Output already exists`: choose a new directory; completed runs are immutable.
`No module named ...`: work from the checkout root. Python below 3.11: choose a
newer interpreter. A stage failure stops the run, retains numbered logs and
steps.json, and produces no completed index. Inspect the failing log; do not
remove a verification step to continue. Retrying needs a new directory.

For live parcel collection, supplied program inputs, geometry or photos, use
[the coordinator's module map](../../skills/start-here/references/modules.md).
Those branches have their own inputs and optional dependencies. Nothing in the
walkthrough automatically requests images, sends emails or submits proposals.

## What a practitioner can supply next

EDDE means **Equitable Development Data Explorer**. Start with the
[official HPD overview](https://www.nyc.gov/site/hpd/services-and-information/equitable-data-development-explorer.page)
and the pinned RER instructions for the community summary and full profile.
Confirm the appropriate local geography with someone familiar with the project;
PUMA and community-district boundaries are not interchangeable. Retain any export,
its selected geography, indicator vintage and retrieval date for review. This is
manual acquisition guidance: the explorer's current export/API has not been
audited, and the RER module does not yet ingest those exports. They must not be
silently pasted into typed filled slots without a reviewed adapter.

## Readiness evidence

An [independent fresh-agent dry run](../reviews/first-time-agent-dry-run.md) completed
the sequence in an isolated checkout and a no-pip Python 3.12 virtual environment,
and confirmed an attempted overwrite left all previous files unchanged. Remaining
packet presentation issues are recorded there. This is AI execution/usability
evidence; a housing practitioner has not yet validated the approach or usefulness.
