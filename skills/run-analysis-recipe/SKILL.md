---
name: run-analysis-recipe
description: Apply an editable, typed area-analysis recipe to a verified parcel investigation and inspect downstream impact.
---

# Run analysis recipe

Apply an editable typed area recipe to verified parcel evidence.

## Inputs and preflight

A verified parcel/recipe run and an explicit recipe with attributed assumptions. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook for build, impact preview and revision commands. Use versioned allowlisted methods and a fresh output.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

## Validate and hand off

Verify; inspect trace.json, IR, calculation CSV and packet before handing off.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

Eligible next steps: [compare-housing-programs](../compare-housing-programs/SKILL.md) (optional independently supplied program comparison); [build-grounded-massing](../build-grounded-massing/SKILL.md) (optional assumed geometry). Load only the requested branch.

## Limits

Unit semantics matter. This is area arithmetic, not an arbitrary econometric engine or feasibility finding.
