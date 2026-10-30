# Investigate a lot

Give this guide to Codex or Claude Code with your Bronx address or tax-lot BBL and
a question. BBL is the ten-digit tax-lot identifier. The agent gathers your inputs, writes the existing module requests,
runs the supported steps, and returns a short cover note with linked packets.
This guide coordinates the existing tools; there is no new one-command live runner
or automatic converter for arbitrary agency documents.

No development build or regeneration is needed to use the checkout. Keep requests,
outputs and reviews local; do not commit, push or upload them unless explicitly
requested for this task. Shipped examples and source snapshots are read-only.

## Start with this

Copy this request and fill in the first two lines:

> Site: [Bronx address or BBL]
>
> Question: [What do I want to learn or compare?]
>
> Follow docs/investigate-a-lot.md. Collect live public records, preserve source
> dates and unknowns, and return a short cover note with links to the evidence.
> Ask for optional modeling inputs only if my question needs them. Keep working
> files under a fresh runs/ directory. Do not invent a building, program or photo.

A site and question are enough to start. No area or rental program is required.
For example, ask what the public records establish and what a practitioner would
need before evaluating a housing scenario.

## Inputs the agent may need

| Step | Inputs you supply | If absent |
| --- | --- | --- |
| Evidence | Address or BBL, question | Ask for them; resolve ambiguous addresses before collecting other data |
| Area model | Gross area, nonresidential allocation, net efficiency, average net home size, with rationales | Return evidence without inventing a home count |
| Rental offers | Unit mix, bedrooms, rents, utilities, proposed restriction durations, household profiles and price/reference year | Defer comparison; do not turn home-equivalents into units |
| NYC Racial Equity Report (RER) preparation | Verified comparison and preparer/date; identify missing professional evidence | Return incomplete drafts and missing-data states |
| Site image | Actual reference photo and explicit visual assumptions | Return available diagram/brief materials and name missing inputs; do not invent a site rendering |

Household profiles currently select supported income-reference rows. Arbitrary
household incomes and arbitrary reference years are not automatic adapters. The
agent must check compatibility instead of silently changing the user's inputs.
The current RER adapter maps supplied offers and preparation metadata; importing
EDDE community exports, certified program rules or applicant findings needs
additional reviewed adapters. Supplying those documents does not populate them automatically.

## Run in sequence, only as far as the inputs support

Use Python 3.11+ from the checkout root. The agent creates a fresh project folder
and its inputs/ directory **with parent directories** before writing requests.
Each module's output subdirectory must be new/empty. Write explicit rationales and
check schemas; copying example JSON does not make its wording true for a new site.

| Stage | Agent reads | Output / gate |
| --- | --- | --- |
| 1. Collect and explain the site | [Investigation skill](../skills/housing-investigation/SKILL.md) | Verified parcel packet; live/replay origin, dates, recorded building context and unknowns |
| 2. Apply supplied area assumptions, if needed | [Recipe skill](../skills/run-analysis-recipe/SKILL.md) | Verified area calculation and trace; no legal/physical capacity finding |
| 3. Compare supplied rental offers, if needed | [Comparison skill](../skills/compare-housing-programs/SKILL.md) | Verified independent cost-and-bedroom tests; no eligibility, delivery or winner |
| 4. Map a supplied comparison to reporting needs, if needed | [RER skill](../skills/prepare-rer-draft/SKILL.md) | Separate incomplete drafts and missing-data map; no official submission |

Verify each package before passing it downstream. Preserve partial evidence and
errors; a failure does not become zero records. Stop a blocked stage and explain
what is missing. Later independent modules can still run when their own documented
inputs and checks are satisfied; do not invent a successful handoff.

An area recipe is optional: the comparison accepts supported verified parcel or
recipe analysis. Independent offers are not derived from either analysis's area
quotient. A positive residential-unit record must remain visible when discussing
hypothetical offers; no existing-home loss or net addition is implied.

The supported visual branches have their own [runtime and input checks](../skills/start-here/references/agent-runtimes.md).
Codex can generate with its available image tool. Claude Code currently prepares
and exports a brief. Neither a missing image tool nor a missing photo blocks the
evidence packet. A diagram-only brief is not a completed image deliverable.

## Return one clear handoff

Write a reviewer-authored cover note using [this template](../templates/review-cover-note.md).
Keep it short and link each factual or numerical statement to a claim, source
passage or verified packet. Label interpretation as an attributed judgment.

The note must connect the recorded site context to the scenarios: what came from
public records, what was supplied as an assumption, and what remains unreconciled.
State which stages completed, were not requested or were blocked. Do not present
missing RER fields as a completed report, or an illustration as proof of fit.
The narrative cover note is not automatically verified by the module verifiers.

Return its **absolute path** and paths to the underlying packets/IR. Working outputs
stay local and are not automatically committed or published. For the primary Codex-on-Mac workflow, return the actual local folder path and
keep generated images with the same run. Offer a local ZIP if the user requests it.
See [storage and platforms](storage-and-platforms.md).

For a concrete case, the [1940 Jerome Avenue trial](../examples/live-lot-trial/README.md)
shows recorded residential development alongside independent hypothetical offers.
It demonstrates the supported workflow, not a feasible development proposal.
