---
name: model-parcel-scenario
description: Build typed evidence claims and optional area-budget calculations from a saved parcel collection.
---

# Model parcel scenario

Build typed claims and optional area arithmetic from a saved parcel collection.

## Inputs and preflight

Saved source responses and receipts; scenario values only if supplied with rationales. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook and build the model. Keep historical dwelling-unit signals and source gaps visible. No supplied scenario means evidence-only output.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

## Validate and hand off

Hand the run to publish-evidence-packet for final verification and presentation.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

Eligible next steps: [publish-evidence-packet](../publish-evidence-packet/SKILL.md) (verify and present the built package). Load only the requested branch.

## Limits

Home-equivalents are an area quotient, not permitted or feasible homes. No automatic occupancy reconciliation.
