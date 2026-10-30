---
name: compare-housing-programs
description: Compare two explicitly supplied housing offers for hypothetical households, preserving source versions, assumptions and unknowns.
---

# Compare housing programs

Compare explicitly supplied housing offers against hypothetical household cost-and-bedroom tests.

## Inputs and preflight

Verified site analysis, coherent-year reference pack, explicit integer mixes, rents, utilities, durations and profiles. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook and canonical request before building. For revisions, preview impact and replay into a new run.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

## Validate and hand off

Verify, then present overlapping profile tests separately. Optional next step: prepare-rer-draft with a supported draft request.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

Eligible next steps: [prepare-rer-draft](../prepare-rer-draft/SKILL.md) (optional report preparation). Load only the requested branch.

## Limits

Offers are independent assumptions, not derived unit capacity. No eligibility, availability, delivery, winner or causal benefit is established.
