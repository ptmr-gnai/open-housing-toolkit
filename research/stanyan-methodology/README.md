# 730 Stanyan methodology case study

Prepared November 9, 2026. Start with [the case study](report.md), then
[the comparison with the Bronx report](bronx-comparison.md).

**Executable benchmark:** [run the budget reconstruction and assumption-change
comparisons](benchmark.md). Stanyan is our primary best available professional
reference case pending a better alternative. The first slice reproduces fifteen
selected targets and traces three independent one-assumption diagnostics to
conditional decision summaries.

This is a known-case reconstruction of public agency work, with later outcomes
already exposed. It is not a blind backtest, a new underwriting approval, or an
implementation of San Francisco rules in the NYC toolkit. No expert review of
this study has occurred. Usability changes are deferred pending the Jeremy meeting.

The primary Bronx baseline is the **October 4, 2026, 1337 Jerome Avenue brief**,
not the October 30 trial on 1940 Jerome Avenue. Exact paths, roles, hashes and
the inspected repository commit are in [comparison-baseline.json](comparison-baseline.json).

## What is included

- [Report](report.md): four decision stages, financing, operations, tradeoffs,
  source conflicts and what the methodology teaches us.
- [Bronx comparison](bronx-comparison.md): what already exists, what is absent,
  what transfers across programs, and a bounded next modeling experiment.
- [Case data](case-data.json): attributed budget snapshots, selected Year 1
  operating inputs and the LOSP disbursement schedule.
- [Sources](sources.json): exact public URLs, retrieval dates, document dates,
  raw PDF hashes, per-page extraction hashes and review scope. Original PDFs and
  per-page text are retained under sources/. Original Excel formulas, full legal
  due diligence and realized costs/outcomes are not reconstructed.
- [Reconciliation results](checks.json): recomputed arithmetic and explicitly
  retained discrepancies. Source discrepancies are findings, not passing balances.

## Reproduce the bounded checks

From the repository root, standard-library Python 3.11+; no network, image API or
spreadsheet package is needed:

```sh
python research/stanyan-methodology/validate.py
python -m unittest discover -s research/stanyan-methodology/tests -v
```

The validator reads only. It checks source and baseline identities, selected
numeric page anchors, stage/date/domain boundaries and the saved arithmetic.
Tests challenge later-evidence leakage, double-counted homes and moving operating
subsidy into construction funding. They do not certify source completeness,
professional correctness, legal applicability or actual delivery.

To independently extract PDFs, use PyMuPDF and
`page.get_text('text', sort=False)` as recorded in sources.json. Text hashes
are tied to the recorded extraction version; other versions may yield different
text. Inspect cited pages visually before interpreting tables. Complete original
response PDFs are retained, so reproducing the source snapshot does not require
re-downloading changing public URLs.

## Rights and scope

Original analysis is covered by the repository's documentation license. Source
PDFs and extracted public-agency text remain subject to their publishers' rights;
MIT/CC licenses do not relicense them. See [DATA-LICENSES.md](../../DATA-LICENSES.md).
Public recommendation/approval records do not establish funds were disbursed,
that conditions were fulfilled, or that projected services and outcomes occurred.
