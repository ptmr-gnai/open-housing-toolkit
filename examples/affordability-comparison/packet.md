# Conditional housing-program comparison: 2028710002

How do these two explicit rental offers differ for the stated hypothetical households, without choosing an overall winner?

**Illustrative programs; professional review pending. No overall ranking.**

Prices and reference schedules: **2025**, historical. No current-year or future-rent forecast.

The profiles are hypothetical households at published rounded income reference values. Counts below mean only that the stated cost threshold and exact bedroom category match. They are **not** counts of eligible households, available homes or achieved benefits.

## Stated objective

Expose total-home, household-cost and proposed-duration tradeoffs. No community preference or optimal project is inferred. — supplied by Open Housing Toolkit demonstration; unreviewed

## Explicit offers and profile comparisons

| Program | Total proposed homes | Hypothetical four-person household at 30% AMI reference | Hypothetical four-person household at 60% AMI reference | Delivery |
| --- | --- | --- | --- | --- |
| Program A — smaller, more lower-rent offers | 24 | 16 | 24 | unknown |
| Program B — larger, fewer lower-rent offers | 36 | 8 | 36 | unknown |

These counts describe supplied offers. No known no-action baseline establishes net additions or an effect caused by intervention.

## The visible tradeoff

Program B — larger, fewer lower-rent offers minus Program A — smaller, more lower-rent offers: **12 total proposed homes**.

- Hypothetical four-person household at 30% AMI reference: -8 homes meeting the diagnostic conditions.
- Hypothetical four-person household at 60% AMI reference: 12 homes meeting the diagnostic conditions.

These are separate dimensions. The module does not choose a winner or infer community preferences.

## Household profiles

| Profile | Hypothetical annual income USD | Household size | Exact bedrooms | Monthly budget USD |
| --- | --- | --- | --- | --- |
| Hypothetical four-person household at 30% AMI reference | 48600.00 | 4 | 2 | 1215.00 |
| Hypothetical four-person household at 60% AMI reference | 97200.00 | 4 | 2 | 2430.00 |

Budget = annual income × stated threshold / 100 / 12. Threshold: 30.00%. Burden percentages are displayed to six decimal places. Tests use the exact inequality before rounding.

## Offer assumptions, restrictions and cost tests

| Program / bin | Homes | Bedrooms | Rent USD/month | Utilities USD/month | Gross USD/month | Proposed restriction years | Commitment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Program A — smaller, more lower-rent offers / lower_rent | 16 | 2 | 1000.00 | 100.00 | 1100.00 | 60 | proposed |
| Program A — smaller, more lower-rent offers / higher_rent | 8 | 2 | 1800.00 | 100.00 | 1900.00 | 30 | proposed |
| Program B — larger, fewer lower-rent offers / lower_rent | 8 | 2 | 1000.00 | 100.00 | 1100.00 | 30 | proposed |
| Program B — larger, fewer lower-rent offers / higher_rent | 28 | 2 | 1800.00 | 100.00 | 1900.00 | 30 | proposed |

Restriction duration is a proposed input, not a promise of fixed rents over that period, a legal certification, or a forecast of household-years served. The exact-bedroom rule is a scoped comparison convention, not a suitability or eligibility determination.

| Program / bin | Profile | Housing cost burden % | Cost test | Bedroom test | Both |
| --- | --- | --- | --- | --- | --- |
| program_a / lower_rent | lower_income | 27.160494 | True | True | True |
| program_a / lower_rent | higher_income | 13.580247 | True | True | True |
| program_a / higher_rent | lower_income | 46.913580 | False | True | False |
| program_a / higher_rent | higher_income | 23.456790 | True | True | True |
| program_b / lower_rent | lower_income | 27.160494 | True | True | True |
| program_b / lower_rent | higher_income | 13.580247 | True | True | True |
| program_b / higher_rent | lower_income | 46.913580 | False | True | False |
| program_b / higher_rent | higher_income | 23.456790 | True | True | True |

## Unknowns and limits

- **Future without-intervention baseline**: Future no-action development has not been established. Program differences are not net additions or causal benefits.
- **Existing occupancy and direct losses**: Existing occupants, businesses, protections and direct losses remain unresolved. Recorded zero homes cannot clear displacement.
- **Transit opportunity access**: No network-access result imported or calculated in this slice. Station proximity is not job access.
- **Program delivery and realization**: Illustrative program only; no finance, construction or delivery evidence.
- **Program delivery and realization**: Illustrative program only; no finance, construction or delivery evidence.

- Hypothetical household profiles, not observed beneficiaries; no eligibility or availability determination.
- Cost threshold and exact bedroom match are diagnostic criteria, not an agency affordability or compliance certification.
- All program quantities and restriction durations are explicit assumptions; restrictions are proposed, delivery unknown.
- No established future no-action baseline; no project-attributable benefit, net new homes or causal rent/displacement estimate.
- Existing occupancy and direct losses unresolved; zero recorded homes does not establish no displacement.
- No transit-access, public-resource, financing, geometric-fit or emissions model executed by this module.
- Historical reference values in the declared price year, not a current rent forecast or inflation-adjusted projection.

## Reference and implementation scope

Foundation: [NYC Racial Equity Report submission guide](https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a), Table 3, printed page 6; document stamp 7/1/25 | Subject to Change. The table contains rounded illustrative references. Rents shown there are context, not calculated regulatory rent ceilings or utility-adjusted program limits.

Original PDF SHA256: `d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1`. It is externally available and not bundled. The selected excerpt was checked against that PDF at preparation; ordinary offline replay parses the retained passages and receipt without re-extracting the external PDF. Source interpretation and current applicability still need review.

Rent and income table vintages must match each other and the request price year. No compatibility override or inflation adapter is implemented.

## Complete claim register

Each source fact has a passage/field reference; assumptions have rationales; derived claims have versioned methods and input IDs. All source excerpt, request and analysis bytes are bound in the manifest. Citations and byte checks do not establish complete coverage or professional acceptance.

### site.bbl

[fact] Site identity from verified upstream analysis: 2028710002 status

Reference: `{
  "file": "analysis-run/ir.json",
  "pointer": "/resolved_bbl",
  "sha256": "95d339d015994ab13b1b723f6e36ababccb0c83d1c5826e87c5ddd1784d8bee9"
}`

### reference.ami30_income_one

[fact] Historical rounded annual_income_usd at 30% AMI: 34000.00 USD per year

Reference: `{
  "excerpt_file": "reference-source/passages.txt",
  "excerpt_sha256": "ec02efd171c803c2e1429868471b602739a4e68e7a448dec99cb3ef1230dcbc4",
  "extraction_method": "nyc-rer-table3-selected-rows@1",
  "page": 6,
  "quote": "30% AMI $34,000 $48,600 $850 $1,090",
  "source_pdf_sha256": "d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1",
  "table": "3",
  "url": "https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a"
}`

### reference.ami30_income_four

[fact] Historical rounded annual_income_usd at 30% AMI: 48600.00 USD per year

Reference: `{
  "excerpt_file": "reference-source/passages.txt",
  "excerpt_sha256": "ec02efd171c803c2e1429868471b602739a4e68e7a448dec99cb3ef1230dcbc4",
  "extraction_method": "nyc-rer-table3-selected-rows@1",
  "page": 6,
  "quote": "30% AMI $34,000 $48,600 $850 $1,090",
  "source_pdf_sha256": "d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1",
  "table": "3",
  "url": "https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a"
}`

### reference.ami30_rent_studio

[fact] Historical rounded reference_monthly_rent_usd at 30% AMI: 850.00 USD per month

Reference: `{
  "excerpt_file": "reference-source/passages.txt",
  "excerpt_sha256": "ec02efd171c803c2e1429868471b602739a4e68e7a448dec99cb3ef1230dcbc4",
  "extraction_method": "nyc-rer-table3-selected-rows@1",
  "page": 6,
  "quote": "30% AMI $34,000 $48,600 $850 $1,090",
  "source_pdf_sha256": "d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1",
  "table": "3",
  "url": "https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a"
}`

### reference.ami30_rent_two

[fact] Historical rounded reference_monthly_rent_usd at 30% AMI: 1090.00 USD per month

Reference: `{
  "excerpt_file": "reference-source/passages.txt",
  "excerpt_sha256": "ec02efd171c803c2e1429868471b602739a4e68e7a448dec99cb3ef1230dcbc4",
  "extraction_method": "nyc-rer-table3-selected-rows@1",
  "page": 6,
  "quote": "30% AMI $34,000 $48,600 $850 $1,090",
  "source_pdf_sha256": "d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1",
  "table": "3",
  "url": "https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a"
}`

### reference.ami60_income_one

[fact] Historical rounded annual_income_usd at 60% AMI: 68000.00 USD per year

Reference: `{
  "excerpt_file": "reference-source/passages.txt",
  "excerpt_sha256": "ec02efd171c803c2e1429868471b602739a4e68e7a448dec99cb3ef1230dcbc4",
  "extraction_method": "nyc-rer-table3-selected-rows@1",
  "page": 6,
  "quote": "60% AMI $68,000 $97,200 $1,700 $2,190",
  "source_pdf_sha256": "d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1",
  "table": "3",
  "url": "https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a"
}`

### reference.ami60_income_four

[fact] Historical rounded annual_income_usd at 60% AMI: 97200.00 USD per year

Reference: `{
  "excerpt_file": "reference-source/passages.txt",
  "excerpt_sha256": "ec02efd171c803c2e1429868471b602739a4e68e7a448dec99cb3ef1230dcbc4",
  "extraction_method": "nyc-rer-table3-selected-rows@1",
  "page": 6,
  "quote": "60% AMI $68,000 $97,200 $1,700 $2,190",
  "source_pdf_sha256": "d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1",
  "table": "3",
  "url": "https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a"
}`

### reference.ami60_rent_studio

[fact] Historical rounded reference_monthly_rent_usd at 60% AMI: 1700.00 USD per month

Reference: `{
  "excerpt_file": "reference-source/passages.txt",
  "excerpt_sha256": "ec02efd171c803c2e1429868471b602739a4e68e7a448dec99cb3ef1230dcbc4",
  "extraction_method": "nyc-rer-table3-selected-rows@1",
  "page": 6,
  "quote": "60% AMI $68,000 $97,200 $1,700 $2,190",
  "source_pdf_sha256": "d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1",
  "table": "3",
  "url": "https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a"
}`

### reference.ami60_rent_two

[fact] Historical rounded reference_monthly_rent_usd at 60% AMI: 2190.00 USD per month

Reference: `{
  "excerpt_file": "reference-source/passages.txt",
  "excerpt_sha256": "ec02efd171c803c2e1429868471b602739a4e68e7a448dec99cb3ef1230dcbc4",
  "extraction_method": "nyc-rer-table3-selected-rows@1",
  "page": 6,
  "quote": "60% AMI $68,000 $97,200 $1,700 $2,190",
  "source_pdf_sha256": "d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1",
  "table": "3",
  "url": "https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a"
}`

### policy.cost_threshold_percent

[assumption] Illustrative housing-cost threshold: 30.00 percent

Illustrative housing-cost-burden convention, not eligibility or a sufficient measure of household welfare.

### review.no_action

[unknown] Future without-intervention baseline: None status

Future no-action development has not been established. Program differences are not net additions or causal benefits.

### review.occupancy

[unknown] Existing occupancy and direct losses: None status

Existing occupants, businesses, protections and direct losses remain unresolved. Recorded zero homes cannot clear displacement.

Reference: `{
  "file": "analysis-run/ir.json",
  "sha256": "95d339d015994ab13b1b723f6e36ababccb0c83d1c5826e87c5ddd1784d8bee9",
  "upstream_claim": "unknown.current_use"
}`

### review.access

[unknown] Transit opportunity access: None status

No network-access result imported or calculated in this slice. Station proximity is not job access.

### profile.lower_income.annual_income_usd

[assumption] Hypothetical annual household income: 48600.00 USD per year

Inputs: reference.ami30_income_four.

Hypothetical annual income equal to the rounded historical published threshold, not an observed household or eligibility finding.

### profile.lower_income.bedrooms

[assumption] Exact bedroom category for this comparison: 2 bedrooms

Hypothetical annual income equal to the rounded historical published threshold, not an observed household or eligibility finding.

### profile.lower_income.monthly_budget

[calculation] Illustrative monthly housing-cost budget: 1215.00 USD per month

Inputs: profile.lower_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.monthly_budget@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### profile.higher_income.annual_income_usd

[assumption] Hypothetical annual household income: 97200.00 USD per year

Inputs: reference.ami60_income_four.

Hypothetical annual income equal to the rounded historical published threshold, not an observed household or eligibility finding.

### profile.higher_income.bedrooms

[assumption] Exact bedroom category for this comparison: 2 bedrooms

Hypothetical annual income equal to the rounded historical published threshold, not an observed household or eligibility finding.

### profile.higher_income.monthly_budget

[calculation] Illustrative monthly housing-cost budget: 2430.00 USD per month

Inputs: profile.higher_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.monthly_budget@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.declared_homes

[assumption] Explicit proposed program total: 24 homes

Sum of explicit illustrative offer bins; not a feasible or approved unit count.

### program.program_a.delivery

[unknown] Program delivery and realization: None status

Illustrative program only; no finance, construction or delivery evidence.

### program.program_a.commitment

[assumption] Restriction commitment status: proposed status

Only an illustrative proposed offer. No binding legal instrument or achieved affordability certified.

### program.program_a.lower_rent.homes

[assumption] homes: 16 homes

Illustrative explicit two-bedroom program count, not derived from area or a verified plan.

### program.program_a.lower_rent.monthly_rent_usd

[assumption] monthly_rent_usd: 1000.00 USD per month

Assumed initial monthly contract rent in 2025 USD; no certified program income cap or rent ceiling.

### program.program_a.lower_rent.tenant_utilities_usd

[assumption] tenant_utilities_usd: 100.00 USD per month

Assumed monthly tenant-paid utilities, not an official utility allowance or measured bill.

### program.program_a.lower_rent.restriction_years

[assumption] restriction_years: 60 years

Assumed proposed restriction duration; no binding instrument, rent trajectory or delivery established.

### program.program_a.lower_rent.bedrooms

[assumption] Proposed bedroom category: 2 bedrooms

Explicit illustrative offer category, not a reviewed floor plan or household-suitability determination.

### program.program_a.lower_rent.gross_monthly_cost

[calculation] Rent plus assumed tenant-paid utilities: 1100.00 USD per month

Inputs: program.program_a.lower_rent.monthly_rent_usd, program.program_a.lower_rent.tenant_utilities_usd.

Method: `housing.gross_monthly_cost@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.lower_rent.annual_cost

[calculation] Annualized housing cost: 13200.00 USD per year

Inputs: program.program_a.lower_rent.gross_monthly_cost.

Method: `housing.annualize@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.lower_rent.for_lower_income.burden_percent

[calculation] Illustrative housing-cost burden: 27.160494 percent

Inputs: program.program_a.lower_rent.annual_cost, profile.lower_income.annual_income_usd.

Method: `housing.cost_burden_percent@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.lower_rent.for_lower_income.cost_test

[calculation] Annual cost at or below stated income threshold: True boolean

Inputs: program.program_a.lower_rent.annual_cost, profile.lower_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.within_threshold@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.lower_rent.for_lower_income.bedroom_test

[calculation] Exact bedroom category matches: True boolean

Inputs: program.program_a.lower_rent.bedrooms, profile.lower_income.bedrooms.

Method: `housing.bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.lower_rent.for_lower_income.cost_and_bedroom_test

[calculation] Both diagnostic conditions met; not eligibility: True boolean

Inputs: program.program_a.lower_rent.for_lower_income.cost_test, program.program_a.lower_rent.for_lower_income.bedroom_test.

Method: `housing.cost_and_bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.lower_rent.for_higher_income.burden_percent

[calculation] Illustrative housing-cost burden: 13.580247 percent

Inputs: program.program_a.lower_rent.annual_cost, profile.higher_income.annual_income_usd.

Method: `housing.cost_burden_percent@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.lower_rent.for_higher_income.cost_test

[calculation] Annual cost at or below stated income threshold: True boolean

Inputs: program.program_a.lower_rent.annual_cost, profile.higher_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.within_threshold@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.lower_rent.for_higher_income.bedroom_test

[calculation] Exact bedroom category matches: True boolean

Inputs: program.program_a.lower_rent.bedrooms, profile.higher_income.bedrooms.

Method: `housing.bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.lower_rent.for_higher_income.cost_and_bedroom_test

[calculation] Both diagnostic conditions met; not eligibility: True boolean

Inputs: program.program_a.lower_rent.for_higher_income.cost_test, program.program_a.lower_rent.for_higher_income.bedroom_test.

Method: `housing.cost_and_bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.homes

[assumption] homes: 8 homes

Illustrative explicit two-bedroom program count, not derived from area or a verified plan.

### program.program_a.higher_rent.monthly_rent_usd

[assumption] monthly_rent_usd: 1800.00 USD per month

Assumed initial monthly contract rent in 2025 USD; no certified program income cap or rent ceiling.

### program.program_a.higher_rent.tenant_utilities_usd

[assumption] tenant_utilities_usd: 100.00 USD per month

Assumed monthly tenant-paid utilities, not an official utility allowance or measured bill.

### program.program_a.higher_rent.restriction_years

[assumption] restriction_years: 30 years

Assumed proposed restriction duration; no binding instrument, rent trajectory or delivery established.

### program.program_a.higher_rent.bedrooms

[assumption] Proposed bedroom category: 2 bedrooms

Explicit illustrative offer category, not a reviewed floor plan or household-suitability determination.

### program.program_a.higher_rent.gross_monthly_cost

[calculation] Rent plus assumed tenant-paid utilities: 1900.00 USD per month

Inputs: program.program_a.higher_rent.monthly_rent_usd, program.program_a.higher_rent.tenant_utilities_usd.

Method: `housing.gross_monthly_cost@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.annual_cost

[calculation] Annualized housing cost: 22800.00 USD per year

Inputs: program.program_a.higher_rent.gross_monthly_cost.

Method: `housing.annualize@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.for_lower_income.burden_percent

[calculation] Illustrative housing-cost burden: 46.913580 percent

Inputs: program.program_a.higher_rent.annual_cost, profile.lower_income.annual_income_usd.

Method: `housing.cost_burden_percent@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.for_lower_income.cost_test

[calculation] Annual cost at or below stated income threshold: False boolean

Inputs: program.program_a.higher_rent.annual_cost, profile.lower_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.within_threshold@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.for_lower_income.bedroom_test

[calculation] Exact bedroom category matches: True boolean

Inputs: program.program_a.higher_rent.bedrooms, profile.lower_income.bedrooms.

Method: `housing.bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.for_lower_income.cost_and_bedroom_test

[calculation] Both diagnostic conditions met; not eligibility: False boolean

Inputs: program.program_a.higher_rent.for_lower_income.cost_test, program.program_a.higher_rent.for_lower_income.bedroom_test.

Method: `housing.cost_and_bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.for_higher_income.burden_percent

[calculation] Illustrative housing-cost burden: 23.456790 percent

Inputs: program.program_a.higher_rent.annual_cost, profile.higher_income.annual_income_usd.

Method: `housing.cost_burden_percent@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.for_higher_income.cost_test

[calculation] Annual cost at or below stated income threshold: True boolean

Inputs: program.program_a.higher_rent.annual_cost, profile.higher_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.within_threshold@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.for_higher_income.bedroom_test

[calculation] Exact bedroom category matches: True boolean

Inputs: program.program_a.higher_rent.bedrooms, profile.higher_income.bedrooms.

Method: `housing.bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.higher_rent.for_higher_income.cost_and_bedroom_test

[calculation] Both diagnostic conditions met; not eligibility: True boolean

Inputs: program.program_a.higher_rent.for_higher_income.cost_test, program.program_a.higher_rent.for_higher_income.bedroom_test.

Method: `housing.cost_and_bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.sum_homes

[calculation] Sum of explicit offer bins: 24 homes

Inputs: program.program_a.lower_rent.homes, program.program_a.higher_rent.homes.

Method: `housing.sum_homes@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.for_lower_income.cost_test_homes

[calculation] Homes meeting cost threshold and exact bedroom category; not eligibility: 16 homes

Inputs: program.program_a.lower_rent.homes, program.program_a.lower_rent.for_lower_income.cost_and_bedroom_test, program.program_a.higher_rent.homes, program.program_a.higher_rent.for_lower_income.cost_and_bedroom_test.

Method: `housing.selected_homes@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_a.for_higher_income.cost_test_homes

[calculation] Homes meeting cost threshold and exact bedroom category; not eligibility: 24 homes

Inputs: program.program_a.lower_rent.homes, program.program_a.lower_rent.for_higher_income.cost_and_bedroom_test, program.program_a.higher_rent.homes, program.program_a.higher_rent.for_higher_income.cost_and_bedroom_test.

Method: `housing.selected_homes@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.declared_homes

[assumption] Explicit proposed program total: 36 homes

Sum of explicit illustrative offer bins; not a feasible or approved unit count.

### program.program_b.delivery

[unknown] Program delivery and realization: None status

Illustrative program only; no finance, construction or delivery evidence.

### program.program_b.commitment

[assumption] Restriction commitment status: proposed status

Only an illustrative proposed offer. No binding legal instrument or achieved affordability certified.

### program.program_b.lower_rent.homes

[assumption] homes: 8 homes

Illustrative explicit two-bedroom program count, not derived from area or a verified plan.

### program.program_b.lower_rent.monthly_rent_usd

[assumption] monthly_rent_usd: 1000.00 USD per month

Assumed initial monthly contract rent in 2025 USD; no certified program income cap or rent ceiling.

### program.program_b.lower_rent.tenant_utilities_usd

[assumption] tenant_utilities_usd: 100.00 USD per month

Assumed monthly tenant-paid utilities, not an official utility allowance or measured bill.

### program.program_b.lower_rent.restriction_years

[assumption] restriction_years: 30 years

Assumed proposed restriction duration; no binding instrument, rent trajectory or delivery established.

### program.program_b.lower_rent.bedrooms

[assumption] Proposed bedroom category: 2 bedrooms

Explicit illustrative offer category, not a reviewed floor plan or household-suitability determination.

### program.program_b.lower_rent.gross_monthly_cost

[calculation] Rent plus assumed tenant-paid utilities: 1100.00 USD per month

Inputs: program.program_b.lower_rent.monthly_rent_usd, program.program_b.lower_rent.tenant_utilities_usd.

Method: `housing.gross_monthly_cost@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.lower_rent.annual_cost

[calculation] Annualized housing cost: 13200.00 USD per year

Inputs: program.program_b.lower_rent.gross_monthly_cost.

Method: `housing.annualize@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.lower_rent.for_lower_income.burden_percent

[calculation] Illustrative housing-cost burden: 27.160494 percent

Inputs: program.program_b.lower_rent.annual_cost, profile.lower_income.annual_income_usd.

Method: `housing.cost_burden_percent@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.lower_rent.for_lower_income.cost_test

[calculation] Annual cost at or below stated income threshold: True boolean

Inputs: program.program_b.lower_rent.annual_cost, profile.lower_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.within_threshold@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.lower_rent.for_lower_income.bedroom_test

[calculation] Exact bedroom category matches: True boolean

Inputs: program.program_b.lower_rent.bedrooms, profile.lower_income.bedrooms.

Method: `housing.bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.lower_rent.for_lower_income.cost_and_bedroom_test

[calculation] Both diagnostic conditions met; not eligibility: True boolean

Inputs: program.program_b.lower_rent.for_lower_income.cost_test, program.program_b.lower_rent.for_lower_income.bedroom_test.

Method: `housing.cost_and_bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.lower_rent.for_higher_income.burden_percent

[calculation] Illustrative housing-cost burden: 13.580247 percent

Inputs: program.program_b.lower_rent.annual_cost, profile.higher_income.annual_income_usd.

Method: `housing.cost_burden_percent@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.lower_rent.for_higher_income.cost_test

[calculation] Annual cost at or below stated income threshold: True boolean

Inputs: program.program_b.lower_rent.annual_cost, profile.higher_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.within_threshold@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.lower_rent.for_higher_income.bedroom_test

[calculation] Exact bedroom category matches: True boolean

Inputs: program.program_b.lower_rent.bedrooms, profile.higher_income.bedrooms.

Method: `housing.bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.lower_rent.for_higher_income.cost_and_bedroom_test

[calculation] Both diagnostic conditions met; not eligibility: True boolean

Inputs: program.program_b.lower_rent.for_higher_income.cost_test, program.program_b.lower_rent.for_higher_income.bedroom_test.

Method: `housing.cost_and_bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.homes

[assumption] homes: 28 homes

Illustrative explicit two-bedroom program count, not derived from area or a verified plan.

### program.program_b.higher_rent.monthly_rent_usd

[assumption] monthly_rent_usd: 1800.00 USD per month

Assumed initial monthly contract rent in 2025 USD; no certified program income cap or rent ceiling.

### program.program_b.higher_rent.tenant_utilities_usd

[assumption] tenant_utilities_usd: 100.00 USD per month

Assumed monthly tenant-paid utilities, not an official utility allowance or measured bill.

### program.program_b.higher_rent.restriction_years

[assumption] restriction_years: 30 years

Assumed proposed restriction duration; no binding instrument, rent trajectory or delivery established.

### program.program_b.higher_rent.bedrooms

[assumption] Proposed bedroom category: 2 bedrooms

Explicit illustrative offer category, not a reviewed floor plan or household-suitability determination.

### program.program_b.higher_rent.gross_monthly_cost

[calculation] Rent plus assumed tenant-paid utilities: 1900.00 USD per month

Inputs: program.program_b.higher_rent.monthly_rent_usd, program.program_b.higher_rent.tenant_utilities_usd.

Method: `housing.gross_monthly_cost@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.annual_cost

[calculation] Annualized housing cost: 22800.00 USD per year

Inputs: program.program_b.higher_rent.gross_monthly_cost.

Method: `housing.annualize@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.for_lower_income.burden_percent

[calculation] Illustrative housing-cost burden: 46.913580 percent

Inputs: program.program_b.higher_rent.annual_cost, profile.lower_income.annual_income_usd.

Method: `housing.cost_burden_percent@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.for_lower_income.cost_test

[calculation] Annual cost at or below stated income threshold: False boolean

Inputs: program.program_b.higher_rent.annual_cost, profile.lower_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.within_threshold@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.for_lower_income.bedroom_test

[calculation] Exact bedroom category matches: True boolean

Inputs: program.program_b.higher_rent.bedrooms, profile.lower_income.bedrooms.

Method: `housing.bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.for_lower_income.cost_and_bedroom_test

[calculation] Both diagnostic conditions met; not eligibility: False boolean

Inputs: program.program_b.higher_rent.for_lower_income.cost_test, program.program_b.higher_rent.for_lower_income.bedroom_test.

Method: `housing.cost_and_bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.for_higher_income.burden_percent

[calculation] Illustrative housing-cost burden: 23.456790 percent

Inputs: program.program_b.higher_rent.annual_cost, profile.higher_income.annual_income_usd.

Method: `housing.cost_burden_percent@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.for_higher_income.cost_test

[calculation] Annual cost at or below stated income threshold: True boolean

Inputs: program.program_b.higher_rent.annual_cost, profile.higher_income.annual_income_usd, policy.cost_threshold_percent.

Method: `housing.within_threshold@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.for_higher_income.bedroom_test

[calculation] Exact bedroom category matches: True boolean

Inputs: program.program_b.higher_rent.bedrooms, profile.higher_income.bedrooms.

Method: `housing.bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.higher_rent.for_higher_income.cost_and_bedroom_test

[calculation] Both diagnostic conditions met; not eligibility: True boolean

Inputs: program.program_b.higher_rent.for_higher_income.cost_test, program.program_b.higher_rent.for_higher_income.bedroom_test.

Method: `housing.cost_and_bedroom_match@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.sum_homes

[calculation] Sum of explicit offer bins: 36 homes

Inputs: program.program_b.lower_rent.homes, program.program_b.higher_rent.homes.

Method: `housing.sum_homes@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.for_lower_income.cost_test_homes

[calculation] Homes meeting cost threshold and exact bedroom category; not eligibility: 8 homes

Inputs: program.program_b.lower_rent.homes, program.program_b.lower_rent.for_lower_income.cost_and_bedroom_test, program.program_b.higher_rent.homes, program.program_b.higher_rent.for_lower_income.cost_and_bedroom_test.

Method: `housing.selected_homes@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### program.program_b.for_higher_income.cost_test_homes

[calculation] Homes meeting cost threshold and exact bedroom category; not eligibility: 36 homes

Inputs: program.program_b.lower_rent.homes, program.program_b.lower_rent.for_higher_income.cost_and_bedroom_test, program.program_b.higher_rent.homes, program.program_b.higher_rent.for_higher_income.cost_and_bedroom_test.

Method: `housing.selected_homes@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### comparison.total_homes_difference

[calculation] Second program minus first: explicit total homes: 12 homes

Inputs: program.program_b.declared_homes, program.program_a.declared_homes.

Method: `housing.difference@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### comparison.for_lower_income.cost_test_homes_difference

[calculation] Second minus first: homes meeting diagnostic conditions: -8 homes

Inputs: program.program_b.for_lower_income.cost_test_homes, program.program_a.for_lower_income.cost_test_homes.

Method: `housing.difference@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.

### comparison.for_higher_income.cost_test_homes_difference

[calculation] Second minus first: homes meeting diagnostic conditions: 12 homes

Inputs: program.program_b.for_higher_income.cost_test_homes, program.program_a.for_higher_income.cost_test_homes.

Method: `housing.difference@1`.

Conditional arithmetic for explicitly supplied profiles and offers; not eligibility or achieved welfare.
