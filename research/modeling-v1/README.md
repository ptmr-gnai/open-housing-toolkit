# Rental-model improvement and reference checks

This slice improves the old area-only model by connecting an explicit rental
program to categorized development costs, annual operations, permanent debt and
unallocated capital. It is a standalone module and a financial template for
[goal-seeking site search](../../src/housing_site_search/README.md).

[Module guide](../../src/housing_underwriting/README.md) ·
[Sample inputs](../../config/underwriting/rental-60-base.json) ·
[Stanyan reference](../stanyan-methodology/README.md).

## Source basis

The retained HPD New Construction Finance term sheet (July 2025) has coverage and
income/expense screens on PDF page 6, and reserve and cash-flow structures on
page 8. The retained HDC New Construction document provides permanent-debt
conventions on page 2, leverage/coverage on page 4, and reserves/ongoing fees on
page 5. Exact URLs, retrieval time, hashes and source text extraction are in
sources.json and sources/. These are dated program references; the model does
not establish applicability, eligibility or that the documents govern a later
transaction. No automatic source amount or program award is assumed.

We reuse the separation of capital sources/uses, operations, reserves, debt and
coverage. Analysts supply thresholds and all financial amounts. Construction
cash-flow timing, LIHTC proceeds, full tax treatment, equity returns, agency
eligibility and financing commitments are outside this implementation.

Stanyan remains the principal known-case reference. Its existing benchmark and
source conflicts are preserved. Rental projections here do not import San
Francisco program rules into the Bronx or turn a known-case reconstruction into
a blind backtest. Homeownership/co-op project operations and buyer finance remain
separate budgets, as the 1337 Jerome input checklist already identifies.

## Verification

Behavioral tests cover full capital categories, support expiry, later-year cost
pressure, reserve treatment, combined leverage including subordinate debt,
missing appraisals, source status, zero-interest amortization, numerical bounds
and package replay/tampering. Twelve retained packages are indexed in [summary.json](cases/summary.json).
Run `python research/modeling-v1/validate.py` for offline verification.
See [results and limitations](report.md) and the connected
[site-search case study](../site-goal-search/README.md).

Code MIT; original prose CC BY 4.0. Source PDFs retain their agency terms and are
excluded from the project license.
