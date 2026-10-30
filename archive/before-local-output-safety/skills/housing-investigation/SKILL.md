---
name: housing-investigation
description: Investigate one Bronx parcel using public records, explicit scenario assumptions and a cited information packet. Use for an early site investigation or an area-budget scenario, with incomplete professional coverage made visible.
---

# Housing investigation

Investigate one supported Bronx parcel; use evidence-only output unless an area scenario was explicitly supplied.

## Inputs and preflight

Collect the BBL or unique address and decision question. For an offline tour, no site inputs are needed. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook for intake and the supported workflow. For live work, write the typed request, then follow collect → model → packet. The runbook also has a cached demo.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

## Validate and hand off

Verify the finished parcel run before handing its packet/IR to the user or a downstream module.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

Eligible next steps: [collect-parcel-evidence](../collect-parcel-evidence/SKILL.md) (live collection); [model-parcel-scenario](../model-parcel-scenario/SKILL.md) (model saved records); [publish-evidence-packet](../publish-evidence-packet/SKILL.md) (verify and present). Load only the requested branch.

## Limits

Current occupancy, title, zoning capacity, physical fit and financing remain unresolved.
