# Rental underwriting: stanyan-separate-budget-control

Do the generic cost/operating calculations reproduce selected Stanyan source-table arithmetic while preserving dates and the reported one-dollar reconciliation difference? Do not interpret the artificial funding gap as a historical project shortfall.

Conditional rental-project underwriting diagnostic; no legal/physical feasibility, financing award or investor-return finding.

**Price basis:** Capital2023 USD; area schedule2022; full-year operations2025 USD. Selected arithmetic control across explicitly separate source budgets, not a unified underwriting forecast.

**Input basis:** Arithmetic control only. Capital2023, area2022 and full-year operations2025 remain separately dated. New primary debt is deliberately capped at zero; scheduled historical hard debt enters other annual debt service. No actual capital-gap or loan-terms reconstruction is claimed.

| Quantity | Value |
| --- | --- |
| Proposed homes (scenario, not validated layout) | 160 |
| Proposed gross area sf | 193739 |
| Total development cost | $169,152,004.00 |
| Maximum primary loan capacity under declared financing caps | $0.00 |
| Modeled primary loan limited to scenario funding need (uncommitted) | $0.00 |
| Declared other sources, committed + proposed | $0.00 |
| Unallocated capital after modeled loan and all declared sources | $169,152,004.00 |
| Capital not covered by committed sources | $169,152,004.00 |
| Balloon at loan maturity | $0.00 |

## Annual cash flow

| Year | Effective income | Operating expenses | Replacement reserve | NOI for coverage | Primary debt service | Other debt service | Required DSCR | DSCR | Maturity principal | Cash after all modeled deductions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025 | $3,946,019.00 | $2,593,041.00 | $80,000.00 | $1,272,978.00 | $0.00 | $1,046,907.00 | 1.15 | 1.215942 | $0.00 | $207,183.00 |

Replacement reserves are deducted from coverage NOI: True. The cash-flow calculation deducts them exactly once.

Debt sized against years 1–1; binding constraints: absolute_cap.

Coverage breach years: None under the supplied assumptions.

Cash-shortfall years (including modeled maturity obligations): None under supplied assumptions.

## Capital budget

| Category | Amount | Input measure |
| --- | --- | --- |
| land | $15,900,000.00 | fixed |
| acquisition_closing | $0.00 | fixed |
| demolition | $0.00 | fixed |
| remediation | $0.00 | fixed |
| hard_costs | $125,664,665.00 | fixed |
| hard_contingency | $0.00 | fixed |
| soft_costs | $23,143,948.00 | fixed |
| soft_contingency | $0.00 | fixed |
| offsite_infrastructure | $0.00 | fixed |
| construction_interest | $0.00 | fixed |
| financing_fees | $0.00 | fixed |
| developer_fee | $2,800,000.00 | fixed |
| initial_reserves | $1,643,391.00 | fixed |
| other | $0.00 | fixed |
| taxes_and_carry | $0.00 | fixed |
| business_relocation | $0.00 | fixed |

## Unresolved checks

- No combined loan-to-cost cap evaluated
- No loan-to-value cap or appraisal evaluated
- Entitlement, physical fit, existing occupancy and business relocation
- Land price/title/control and environmental scope
- Construction draws, interest carry timing, lease-up and conversion
- Tax-credit/program eligibility, tax treatment and actual commitments
- Subordinate loan repayment/balloons: only explicitly supplied annual debt service is included
- Investor return, exit value/taxes, refinancing and complete project feasibility

## Declared references

- [Board packet: Budget and Legislative Analyst report, File 23-0524 (2023-05-17)](https://sfgov.legistar.com/View.ashx?GUID=4F7996CD-ECE6-4F95-945E-69336BC233E7&ID=11989749&M=F): PDF page13 capital (2023), page14 operations (2025), page17 area schedule (2022), respectively. Separate dated snapshots; no current-project inference.
- [MOHCD LOSP contract funding evaluation (2025-05-02)](https://media.api.sf.gov/documents/Approved_730_Stanyan_Request_for_LOSP_Funding_Loan_Evaluation_-LC_5-2-25.pdf): PDF page13 capital (2023), page14 operations (2025), page17 area schedule (2022), respectively. Separate dated snapshots; no current-project inference.
- [MOHCD preliminary gap loan evaluation (2022-06-24)](https://sfmohcd.org/sites/default/files/Documents/MOH/Loan%20Committee/Approved%20730%20Stanyan%20Preliminary%20Gap%20Loan%20Eval%20-%20Loan%20Committee%206-24-2022.pdf): PDF page13 capital (2023), page14 operations (2025), page17 area schedule (2022), respectively. Separate dated snapshots; no current-project inference.

Source files, if supplied, are copied and hashed under sources/. Declared references without retained bytes are identified in references.json. Attribution and hashes do not establish a professional interpretation.

Full calculations and input bases: request.json, results.json, trace.json and annual.csv.
