---
name: prepare-rer-draft
description: Prepare five-section RER drafts with an explicit source-to-implementation map, preserving missing and non-equivalent data.
---

# Prepare rer draft

Prepare incomplete five-section RER drafts from a verified housing-offer comparison.

## Inputs and preflight

Verified comparison package and a supported preparation request; do not invent missing professional data. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook, source catalogue and instruction map when applying the guide. Build separate drafts and inspect coverage.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

## Validate and hand off

Verify; return the index, both drafts and coverage, preserving missing and interpretation-needed states.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

## Limits

Do not infer AMI mix, ZSF, jobs, EDDE data or applicability. The cost diagnostic stays supplemental; no compliance finding.
