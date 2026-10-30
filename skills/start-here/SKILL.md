---
name: start-here
description: Guide a first-time housing practitioner or agent through the toolkit, run its offline walkthrough, explain the outputs, and route to independent parcel, modeling, reporting or visual skills.
---

# Start here

Use when someone wants to try the toolkit, investigate a lot, or choose a module.
Read [AGENTS.md](../../AGENTS.md) and [the tenets](../../docs/tenets.md).
This skill is the coordinator; it does not replace the leaf skills or their checks.

## 1. Establish execution capability

Work from the repository root with Python 3.11+. If no checkout exists:

```sh
git clone https://github.com/ptmr-gnai/open-housing-toolkit.git
cd open-housing-toolkit
```

If shell execution is unavailable, offer the [readable worked packet](../../examples/rer-preparation/packet.md)
and explain that nothing has been executed. Do not claim an installed plugin or
silently install optional geometry/image tools.

## 2. Run a first result

For an initial tour, read the four leaf skills in sequence:

1. [Parcel investigation](../housing-investigation/SKILL.md).
2. [Analysis recipe](../run-analysis-recipe/SKILL.md).
3. [Housing-program comparison](../compare-housing-programs/SKILL.md).
4. [RER preparation](../prepare-rer-draft/SKILL.md).

Then run the shared [walkthrough script](../../scripts/first_run.py):

```sh
python scripts/first_run.py --out runs/my-first-run
```

Choose a new directory if it already exists. The script runs cached evidence →
editable area recipe → explicitly supplied illustrative offers → five-section RER
preparation, verifying every stage before continuing. It performs no live collection
or image generation. Partial failures retain logs and stop downstream execution;
there is no success index until all stages pass. Read `README.md` in the output,
then `rer/packet.html`, both program drafts and coverage. Read the earlier stage
packets as needed by tracing individual claims; they are long. Explain that earlier
"queried" wording describes retained collection and that the sample preparation date
is supplied metadata, not today's date. See [the reading guide](../../docs/first-run.md).
GitHub previews of HTML display source; use local HTML or Markdown.

Explain three observations before suggesting a real-site run:

- The base area recipe yields 34 **home-equivalents**, not a feasible unit count.
- The independently assumed 24- and 36-home offers yield 16 versus 8 homes meeting
  one hypothetical lower-income household's cost-and-bedroom test. These counts
  do not establish eligibility, delivery or the best program. Offers are not
  reconciled to the earlier area budget or geometry.
- The RER outputs are incomplete drafts. Read actual missing/interpretation-needed
  slots; do not claim compliance from the five headings or verification.

## 3. Route the user's work

Read [the module and handoff map](references/modules.md). Ask only for missing
inputs needed for the chosen task; a first offline tour needs no housing inputs.
For a real investigation, collect the lot BBL/address and question before choosing
assumptions. Use evidence-only output if no scenario was supplied. Existing analysis
or photos can enter supported modules independently; arbitrary agency formats need
an adapter and must not be presented as already supported.

Read the selected leaf skill, its linked module README and canonical contracts.
Preserve unknowns and unsupported handoffs. Geometry and image generation are
optional branches: do not run them just because the investigation succeeded.

## 4. Return a useful handoff

Report the actual commands executed, paths to readable packets and typed IR,
source vintage, assumptions, material gaps and next practitioner questions.
Technical success and professional usefulness are separate. Invite feedback about
which step differs from actual practice; record friction in the papercut log without
publishing private inputs. Never invent an expert endorsement or send outreach.
