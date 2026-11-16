---
name: check-development-activity
description: Check NYC tax lots for recent demolition, foundation, excavation, new-building and construction-fence permits and filings, so candidates already being developed are flagged before anyone studies them. Use right after an area search, or for one lot before a full analysis.
---

# Check development activity

Lot records (PLUTO) can lag reality by a year or more: a "one-story store" may
already be demolished with excavation underway. This check reads recent DOB and HPD
records for each lot and classifies it as active development, site preparation
(fence only), none found, or not checked.

## Inputs and preflight

A verified area-search package (checks its ranked candidates) or one or more BBLs.
HTTPS access; `.venv/bin/python` from the repository root.

## Execute

Read [the execution reference](references/runbook.md) when running it. Then rerun the
shortlist with `--activity` so lots already in development are listed separately.

## Validate and hand off

Tell the user how many candidates are already in development and name them with the
recorded permit and date. Report any coverage gap the package lists (a published
dataset with no rows for the borough). If the user still wants a held-back lot,
record that choice with `brief decide`; pass the package to the report with
`--activity`.

## Limits

A permit shows recorded activity, not what will be built. "None found" is not proof
that nothing is planned. Sidewalk sheds and scaffolds are ignored (facade work).
