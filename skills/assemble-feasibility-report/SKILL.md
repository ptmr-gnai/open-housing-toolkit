---
name: assemble-feasibility-report
description: Assemble verified lot evidence, ownership, massing, underwriting scenarios and an optional render into one standard site feasibility report (site, zoning, sources and uses, operating pro forma, debt sizing, sensitivity, open items, sources). Use as the final step of a lot analysis or whenever the user asks for "the report".
---

# Assemble a feasibility report

The last step of a lot analysis. It writes no new numbers: it re-verifies each
package the earlier steps produced and lays them out in the sections practitioners
expect. Do not write your own report script, summary table or HTML; use this module.

## Inputs and preflight

Required: the run brief (the user's goal and decisions, started before any work
with `python -m housing_feasibility brief start`), a verified evidence package for
one lot and at least one verified underwriting package. Optional, all for the same lot: an ownership run, one or more
massing packages, a render package, and the area-search package the lot came from.
Python 3.11+ via `.venv/bin/python` from the repository root.

## Execute

Read [the execution reference](references/runbook.md) when running it. The CLI is
`python -m housing_feasibility` with `template`, `build` and `verify`. Write the
report request (title, base-case scenario id, date, who prepared it), then `build` into a new `runs/NAME/report` folder. `--underwriting`
and `--massing` accept a folder holding several packages.

## Validate and hand off

The report opens with the goal in the user's words, the path taken and the decisions,
then the findings; long lists (all candidates, every scenario, sources) sit in
appendices. The build verifies on completion; `verify` re-checks every input and
recomputes the report. Open `report.html` for the user and say in plain words: the base-case gap,
the gap range across scenarios, the zoning check, the latest deed and the top open
items. The report is the deliverable to share; `report.json` is the typed version
for other tools (slides, renders, comparisons).

## Limits

A funding gap is a diagnostic of the stated inputs, not a feasibility finding.
Zoning figures use recorded PLUTO descriptors, not a zoning determination.
Professional review is pending on every report.
