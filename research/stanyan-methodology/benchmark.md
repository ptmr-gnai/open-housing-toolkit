# Stanyan as the primary modeling reference

Stanyan is our **best available professional reference case pending a better
alternative**. Use its staged review process and documented budget structures to
guide development. Treat its numbers, exceptions and contradictions as evidence
to reconstruct and challenge. This policy does not establish industry-wide
superiority, transfer San Francisco rules to New York, or turn a known case into
a blind backtest.

The first executable slice is `benchmark.py`: three capital-budget summaries,
selected 2025 operating-budget categories and waterfall, a historical first-year
coverage screen, and independent changes to one assumption at a time. The prior
[case study](report.md), [Bronx comparison](bronx-comparison.md), source snapshots,
`case-data.json` and `checks.json` are preserved.

## Run the benchmark

From the repository root, Python 3.11+ and standard library only:

```sh
python research/stanyan-methodology/benchmark.py check
python research/stanyan-methodology/benchmark.py suite --out runs/stanyan-benchmark
python research/stanyan-methodology/benchmark.py verify --run runs/stanyan-benchmark
```

Open `runs/stanyan-benchmark/report.html` or `report.md`. The HTML has expandable
source-budget tables and calculation traces. No web server, notebook, API or
image provider is required. Existing destinations are refused. Source PDFs remain
in the matching repository checkout, bound by hash; a run is not a standalone
source archive. Run `verify` with that checkout.

The run includes copied inputs, `results.json`, a CSV of numerical changes, the
two readable reports, source/implementation bindings and a file manifest.
Verification recomputes all outputs, including the prose decision summaries;
rehashing an edited report does not make it a valid computed result.

To supply one different assumption, copy a scenario JSON into your local runs
folder, then:

```sh
python research/stanyan-methodology/benchmark.py run \
  --change runs/my-stanyan-change.json --out runs/my-stanyan-comparison
```

The change object has exactly `id`, `assumption`, `value` and `rationale`.
`value` is a finite decimal string between 0 and 10. Supported assumptions are
`operating_expense_multiplier` (2025 base expense categories), `losp_multiplier`
(2025 annual operating income), and `hard_cost_multiplier` (2023 hard costs).
Every diagnostic holds other inputs fixed. Monetary line items round to cents
before summation; ratios retain Decimal precision internally and display six
decimal places. New methods or sources require an explicit new implementation
and reference contract.

## Frozen reproduction targets

[reference-contract.json](reference-contract.json) defines fifteen selected
targets with source IDs and PDF pages. They cover three development totals,
capital source residuals, the 2023 land-excluding total, operating expenses,
effective gross income, NOI, cash flow, residual receipts, rounded debt coverage,
the historical LOSP schedule and its opening-year discrepancy.

This is a transcription-and-arithmetic reconstruction of selected public tables.
Expected totals were selected from the existing source study and its retained
PDFs. Matching them is not independent professional acceptance or validation of
the original Excel workbook. The model uses an explicit **-$1 EGI bridge** and
**+$1 NOI bridge** to reproduce the reported operating figures, while preserving
the displayed row arithmetic separately. These fixed source-reconciliation
amounts are retained in diagnostics; they are not financial resources.

An additional correction to the earlier prose: the source's opening-year LOSP
payment of **$236,794** is a reported number. Five-twelfths of the displayed annual
$568,307 is $236,794.58, or **$236,795 rounded to whole dollars**. The older
report's description of $236,794 as the rounded result was inaccurate. The
benchmark now shows the $1 discrepancy explicitly. The original `checks.json`
already computed $236,795 and remains unchanged. The source's displayed
calendar-year payments still sum exactly to $11,720,975; do not replace that
historical schedule with a hypothetical diagnostic's income stream.

## What the first diagnostics show

These are static analyst diagnostics, not agency-approved scenarios. Capital and
operations remain separate dated snapshots. In particular, a change to 2023
construction costs does not automatically size a new loan or revise 2025 debt
service; that linkage would require new financing and timing assumptions.

| Quantity | Reported-budget baseline | Base operating costs +10% | LOSP removed | 2023 hard costs +10% |
| --- | ---: | ---: | ---: | ---: |
| 2023 capital uses | $169,152,004.00 | Same | Same | $181,718,470.50 |
| Additional unallocated capital above original uses | $0 | $0 | $0 | $12,566,466.50 |
| 2025 base operating expenses | $2,575,541.00 | $2,833,095.10 | Same | Same |
| 2025 annual LOSP income | $568,307.00 | Same | $0 | Same |
| Year 1 debt-service coverage | 1.215942 | 0.969928 | 0.673098 | 1.215942 |
| Cash flow after scheduled hard debt | $226,071.00 | -$31,483.10 | -$342,236.00 | $226,071.00 |
| Additional annual income needed to meet the selected 1.15 screen | $0 | $188,519.15 | $499,272.05 | $0 |

The last row is a required-income calculation, not an available grant or a LOSP
award. The hard-cost diagnostic retains the original $1 capital source shortfall,
so total uses minus source rows is $12,566,467.50, one dollar above the incremental
cost. Requested or reported source amounts do not become committed simply
because they appear in a table.

The operating-cost change increases all eight source expense categories,
including services embedded in building operations. The separately funded PSH
services budget remains fixed and is added only once in the combined-scope
calculation. No automatic rent, operating subsidy or staffing-policy response is
assumed. A real re-underwriting exercise would consider those responses explicitly.

## Trace an assumption to the decision

For `operating_expense_multiplier = 1.10`, the trace is:

1. Eight base expense categories rise by a total of $257,554.10.
2. Total operating deductions increase by that amount; income, scheduled debt,
   replacement-reserve deposits and separate PSH services remain fixed.
3. NOI falls to $1,015,423.90 and cash flow after hard debt becomes negative.
4. Coverage falls below the historical first-year 1.15 screen.
5. The conditional summary changes from meeting that selected screen to requiring
   operating-cost/support review and re-underwriting. It still withholds a project
   feasibility finding.

`results.json` records each node's value, unit, kind, dependencies, method and
source locator. An impact report distinguishes all dependent nodes from those
whose numeric value actually changed. That distinction matters when, for example,
required additional income remains zero across a small cost change.

## Acceptance and limits

The implemented milestone is accepted technically when the fifteen reference
targets reproduce, the known source discrepancies remain visible, a declared
assumption propagates through relevant calculations and the conditional decision
summary, unrelated budgets remain unchanged, and a saved run verifies without
modifying the checkout. Counterexample tests cover incorrect reference targets,
unfunded shocks, duplicated services, unknown assumptions, output tampering and
overwrites, plus the previous study's evidence-boundary tests.

This does not reproduce the complete 20-year pro forma, original cell formulas,
all source statuses, executed capital/loan documents, tenant eligibility or legal
and physical feasibility. PBV growth and staffing conflicts remain unresolved.
Expert review is pending. A subsequent benchmark should use a frozen early packet
and predefined rubric on another case, including a documented changed/delayed
case. Any analyst exposure to later outcomes must be disclosed.

For Jerome, retain the three distinct budgets already identified in its brief:
development capital, ongoing co-op operations, and buyer financing/access. Stanyan
supplies a concrete software/evidence contract to learn from; Open Door inputs and
appropriate homeownership methods still need to be supplied and reviewed.
