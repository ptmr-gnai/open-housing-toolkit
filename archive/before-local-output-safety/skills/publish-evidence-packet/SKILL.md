---
name: publish-evidence-packet
description: Verify and present a portable information packet and its machine-readable image brief without upgrading evidence to professional clearance.
---

# Publish evidence packet

Verify and present an existing parcel packet and its machine-readable outputs.

## Inputs and preflight

A built parcel run containing inputs, sources, IR and packet exports. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook, run verify and inspect material assumptions, failed sources and unknowns.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

## Validate and hand off

Return actual absolute paths, source vintage, limitations and next questions. The diagram brief is optional.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

Eligible next steps: [run-analysis-recipe](../run-analysis-recipe/SKILL.md) (optional explicit area-method revision). Load only the requested branch.

## Limits

Presentation of local outputs is not email, public publishing or submission; a verified graph is not professional acceptance.
