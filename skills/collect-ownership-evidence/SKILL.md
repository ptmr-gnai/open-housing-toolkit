---
name: collect-ownership-evidence
description: Collect recorded deeds, mortgages, sales and tax-roll owner records for one NYC tax lot, with receipts, conflicts and unknowns. Use when a user asks who owns a lot, when it last sold, or what is recorded against it.
---

# Collect ownership evidence

For one NYC tax lot (BBL), gather ACRIS recorded instruments with parties and
amounts, DOF sales rows and the PLUTO tax-roll owner label. Works in Manhattan,
the Bronx, Brooklyn and Queens; ACRIS open data excludes Staten Island.

## Inputs and preflight

A ten-digit BBL (resolve an address with `scripts/locate.py lookup`), HTTPS access
and Python 3.11+ from the repository root. Each run writes a new folder.

## Execute

Read [the execution reference](references/runbook.md) when running it. Use the
existing module CLI; do not query ACRIS by hand when this module covers the need.

## Validate and hand off

Report the latest deed (date, recorded amount, grantor and grantee), any sale rows,
the tax-roll owner label and every conflict, in plain words, with the package path.
A tax-roll owner that differs from the latest deed grantee is reported, not resolved.
This evidence can inform a lot investigation or an acquisition-cost assumption;
the user approves any number used in a model.

## Limits

Not a title opinion. Recorded parties are not current ownership or site control.
Instrument amounts are not sale prices. Absence of a record is not proof of absence.
