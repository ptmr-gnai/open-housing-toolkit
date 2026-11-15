# Rental underwriting diagnostics

This module connects an explicit rental program to a categorized capital budget,
annual operating projection, permanent-debt limits and unallocated capital. It is
an independent, offline component of the toolkit; it does not require discovery,
a notebook, an image provider or an API key. Python 3.11+ and the editable checkout
are sufficient.

```sh
python -m housing_underwriting build --input config/underwriting/rental-60-base.json --out runs/my-underwriting
python -m housing_underwriting verify --run runs/my-underwriting
```

Each destination must be new. Open packet.html or packet.md; annual.csv carries
all projection years, results.json all derived values, and trace.json explains
step dependencies. Inputs remain editable in a copied JSON request; rebuild into
another directory. Existing packages are never refreshed in place.

## Inputs and attribution

The checked-in requests are **illustrative analyst scenarios**, not empirical
cost/rent estimates, official program offers or financing commitments. Every
program, cost, income, expense, debt and source section carries an input basis and
rationale. Reported inputs must cite declared references. Links alone are not
source-byte verification. To retain documents, repeat
`--reference-source REFERENCE_ID=/local/path`; references.json distinguishes
retained bytes from link-only citations. Verification hashes and recomputes the
package without re-fetching source URLs. Source truth, relevance and applicability
still require review.

Currency/rates/areas are finite decimal **strings**; homes, years and horizons are
integers. All amounts use USD and the explicit price basis. A whole proposed home
count is a scenario input, not a validated unit layout. Gross area is distinct from
zoning floor area and net residential area. The module does not infer a program
from zoning FAR.

Every supported capital category is required, with fixed, per-proposed-home or per-gross-sf
rates: land, acquisition closing, demolition, remediation, hard costs and their
contingency, soft costs and their contingency, offsite infrastructure, construction
interest, taxes/insurance and other carrying costs, business relocation/lease
termination, financing fees, developer fee, initial reserves and other. An explicit
zero has a rationale; missing costs cannot silently become zero. This declared category coverage is not
proof that every material project cost has been identified. An aggregate
source budget can allocate a category to another row, but that mapping must be
explained rather than double counted.

## Methods

Capital lines round to cents before summation. Each annual income stream has its
own loss rate, growth and active start/end years. Expired operating support does
not continue implicitly. Expense rows, replacement deposits and below-line fees
have separate escalation. Growth is measured from year-one prices, including for
a stream that starts later. Replacement reserve treatment in coverage NOI is an
explicit choice; the cash waterfall deducts the deposit exactly once.

Permanent primary debt is the smallest capacity under:

- The lowest allowed annual service over the declared sizing years while the
  primary loan is outstanding, using the explicit per-year coverage schedule (or
  uniform floor), divided by
  the monthly-payment mortgage constant, after other supplied debt service.
- An optional **combined** loan-to-cost cap, subtracting declared subordinate
  loan principal before sizing the primary loan.
- An optional **primary** loan-to-value cap using an explicitly supplied appraisal.
- An optional absolute primary-loan cap.
- The scenario funding need after all declared other sources. The separate maximum
  loan-capacity figure remains visible; available capacity does not force
  unnecessary borrowing or debt service when other scenario funds cover uses.

Principal rounds down to cents. Coverage checks use unrounded principal-level
service to avoid a false failure caused by displaying annual payments to cents;
DSCR and cash flow use the displayed annual service. Zero-interest amortization
is supported. A fully amortizing loan can be paid off before the projection ends; subsequent
years have no primary debt service. When no scheduled debt remains, DSCR and its
covenant test are N/A; a later operating cash deficit remains a separate cash
shortfall, not an expired-loan covenant breach. A balloon loan cannot project beyond maturity
without a separate refinancing model. Remaining principal is deducted from cash
in the maturity year if that year is in the projection and is also shown as
unresolved balloon/refinancing risk. The separate before-maturity-payment and scheduled ending balances reconcile
the obligation with the modeled repayment; zero scheduled debt after maturity is
not proof that a negative-cash project actually repaid its loan. No refinancing
proceeds or cash carry-forward
are invented. The cash target is annual, not a cumulative reserve-funding model.
No fee, construction draw or tax treatment is implied by the chosen interest rate.

Debt sizing is not a lender commitment. Other source amounts retain their
**declared** committed/proposed status; verification does not authenticate that
status. The capital gap after modeled debt and all declared sources differs from
capital not covered by committed sources. Neither amount is an available subsidy.
Subordinate financing only has the annual service explicitly supplied in the debt
input; deferred principal, shared residual receipts and repayment waterfalls still
need separate modeling.

## Established references and limits

The dated [HPD/HDC source study](../../research/modeling-v1/README.md) explains the
published budget and coverage structures we reuse. Their thresholds are not
universal defaults or proof of qualification. The [Stanyan reference](../../research/stanyan-methodology/README.md)
remains a separate historical reconstruction, including its source disagreements.
San Francisco rules and operating subsidies do not become Bronx program inputs.

This module does not reproduce an agency Excel workbook, resolve construction
cash timing, calculate LIHTC proceeds or tax eligibility, model an equity return,
underwrite a co-op buyer, forecast delivery, or establish legal/physical feasibility.
Missing LTC/LTV appraisal checks remain visible. Passing the selected DSCR screen
is one conditional calculation, not a project recommendation.
