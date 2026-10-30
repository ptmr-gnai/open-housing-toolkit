---
name: collect-parcel-evidence
description: Fetch bounded public parcel records with source receipts, exact identity and byte provenance.
---

# Collect parcel evidence

Collect public records for an identified Bronx parcel with source receipts and raw bytes.

## Inputs and preflight

A request matching the parcel schema, a fresh run directory and HTTPS access for live queries. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook before live collection. Run the collection command; inspect identity, adapter status, truncation and receipt bindings.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

## Validate and hand off

Pass the saved request, receipts and source directory to model-parcel-scenario. Preserve failed-source states.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

Eligible next steps: [model-parcel-scenario](../model-parcel-scenario/SKILL.md) (consume the retained collection). Load only the requested branch.

## Limits

No returned rows does not establish no activity; HTTP success alone does not establish valid evidence.
