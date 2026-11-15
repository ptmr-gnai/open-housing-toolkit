# Stanyan versus the last substantive Bronx report

The comparison baseline is [1337 Jerome Avenue's October 4, 2026 brief](../jerome-brief/brief.md)
and [finance-inputs.json](../jerome-brief/finance-inputs.json), at repository commit
`6f2436a8` (full identity and exact file hashes in
[comparison-baseline.json](comparison-baseline.json)).
The October 30 [1940 Jerome usability trial](../../examples/live-lot-trial/README.md)
is newer but concerns a different parcel and a supplied hypothetical rental
comparison. It is considered below only as evidence of current toolkit capability.

**Jerome already has a sound evidence-and-unknowns structure. The substantive
next step is to turn its financial input contract and scenario questions into
linked, program-specific budgets.** Stanyan supplies a precedent for how to
organize that work and interrogate it. Its rental financing cannot fill Jerome's
missing co-op financial inputs.

## 1. Compare the tasks before comparing the answers

| Dimension | 1337 Jerome | 730 Stanyan | Implication |
| --- | --- | --- | --- |
| Point in process | 2026 community visioning / prospective procurement in the frozen brief | Selected sponsor, then 2020 predevelopment, 2022 preliminary gap, 2023 board financing and 2025 operations review | More detailed Stanyan evidence partly reflects maturity, not merely a superior modeling engine |
| Housing product | Affordable cooperative homeownership, Open Door | Affordable rental, tax-credit equity, vouchers and local operating support | Different buyer/resident cash flows, capital sources, restrictions and underwriting |
| Main comparison | Agency concepts of about 48 homes under current zoning and 60 under a possible rezoning | Successive 120-, 152- and 160-home schemes, cost containment and available local support | Neither sequence is a causal estimate of upzoning benefits |
| Starting authority | HPD concept and term sheet; no independent entitlement computation | Agency evaluations citing design submissions, funding processes and legal pathways | Attribute each claim; do not imply independent verification |
| Main result | Reviewable questions and unresolved requirements | Conditional funding decisions and later revised budgets | Match output to the next real decision |

The [425 Grand Concourse calibration](../grand-concourse-calibration/report.md)
already warned that area/cost definitions and legal pathways matter, and that
complete sources and uses were missing. Stanyan adds a richer public example of
the budgeting, review and revision process behind those categories.

## 2. What the Bronx report already gets right

The frozen Jerome brief distinguishes agency-estimated homes from calculated
FAR-area proxies; flags mapped zoning/MIH applicability; identifies a tax-lot versus
zoning-lot assumption; preserves an illustrative no-action alternative; separates
income-based housing budgets from actual sale prices and buyer access; and assigns
professional review owners. It explicitly keeps development capital, buyer
financing and co-op operations separate.

Its finance contract already asks for hard and soft costs, financing costs,
contingencies, reserves, unit/income mix, subsidy commitments, restricted sale
proceeds, maintenance, buyer borrowing and long-term stress. Those are useful
design choices to preserve. All 28 input categories are still null in the inspected
contract. No financial gap or affordable sale price can be responsibly recovered
from that file alone. [Baseline brief](../jerome-brief/brief.md),
[finance contract](../jerome-brief/finance-inputs.json).

We should therefore describe the missing work as **populating and executing the
contract with appropriate methods**, with expert review of those methods.
Stanyan does not justify replacing missing inputs with generic assumptions.

## 3. Methodological differences and concrete extensions

| Area | Current Bronx report / toolkit | Stanyan precedent | Proposed reusable extension |
| --- | --- | --- | --- |
| Decision record | Named next tasks and review gates | Funding request, prior conditions, disposition and subsequent conditions | Represent decision, authority, date, required evidence, deadline and disposition as linked records |
| Physical program | HPD 48/60 concepts; typed area arithmetic and separate assumed massing | Design-stage plans, use allocations, construction type, circulation, costed design revisions | Explicitly reconcile zoning area, gross area, usable residential area, amenities and shared space before financial yield claims |
| Cost estimate | Complete list of missing cost inputs | Estimator/design milestones, comparable costs, value engineering, contingencies and fees | Cost lines with scope, date, design maturity, payer, timing, source and review status |
| Funding | Subsidy maxima and null commitment inputs | Proposed, requested and committed sources; bridge and permanent takeout; failed applications | Versioned capital sources with amount, status, restrictions, conditions, timing and repayment |
| Household affordability | 33%-of-income co-op housing-cost ceilings | Tenant payment separated from landlord subsidy income | Jerome-specific buyer mortgage, maintenance, utilities, down payment and access branch |
| Long-run adequacy | Explicit request for maintenance escalation/stress | Annual expenses, reserves, differential growth, debt service and services budgets | Co-op annual operating/reserve schedule, maintenance trajectory and buyer stress; keep separate from development close |
| Community amenity | Agency goal, actual community preferences still missing | Space, shell, buildout, operator selection, lease and operating support | Amenity delivery record with named operator/funder and unresolved procurement status |
| Exceptions/conflicts | Explicit zoning interpretation and scope questions | Underwriting exceptions and contradictory text inside official records | Preserve source requirement, observed value, exception rationale, approving actor and unresolved discrepancy |
| Evidence quality | Provenance, hashes and source vintages | Real documents still contain inconsistent totals and definitions | Reconciliation findings with materiality, not silent edits or universal pass/fail |

Stanyan evidence for these precedents is detailed, with page references, in
[the case study](report.md). These are design proposals, not implemented
extensions to the production modules.

## 4. What a credible Jerome modeling exercise would do

Use the existing question: **do the approximately twelve additional homes in
HPD's rezoning concept justify the additional design, approval and financial
work?** The answer must be conditional on a supplied scenario and an attributed
choice about benefits, costs, time and buyer access.

### A. Freeze comparable program versions

Start with the agency's approximate 48/60-home alternatives, but label them
agency concepts pending envelope reconciliation. Record each unit/bedroom mix,
affordability tier, gross area, zoning area, community-space area, design maturity
and expected schedule separately. Use one consistent price date or an explicit
price-index conversion. Do not assume a 25% home increase means costs, fees,
subsidy and timing all rise 25%.

### B. Close the development-budget arithmetic

For each alternative, show acquisition/disposition obligations, demolition and
remediation, hard costs, soft costs, financing/carry, contingencies, developer
fees and capitalized reserves. Separate already-paid public expenditures from
new project cash needs. Require a source or declared assumption for each amount.

Then show restricted sales proceeds, public support by program, sponsor cash,
construction financing and its repayment path. Record application caps separately
from requested and committed funding. Bridge and takeout funding need time-aware
treatment. If necessary costs or revenues are absent, present the missingness
and a bounded conditional calculation rather than a financed-project conclusion.

### C. Solve buyer affordability with the correct program

Jerome's frozen Open Door term-sheet extraction uses a 33% total housing-cost
ceiling, a 30-year fixed-rate mortgage assumption, 5% down, maintenance and
shareholder utilities. For a supplied household and unit, the basic calculation is:

```text
monthly mortgage-payment capacity
  = permitted total monthly housing cost
    - maintenance
    - shareholder-paid utilities
    - other required housing charges if applicable

supportable mortgage principal
  = present value of that payment at the supplied rate and term

candidate purchase price
  = principal / (1 - down-payment share)
```

This is an illustrative calculation structure derived from the baseline's
program description, not a complete HPD pricing implementation. Match all charges
to actual program treatment to avoid counting taxes or insurance twice through
maintenance. Apply the market discount and other pricing constraints separately;
do not mistake this algebraic result for an approved sale price. Reject a negative
payment capacity rather than manufacture a negative-priced home.

Next test cash needed for down payment and closing, assets/credit, unit/household
matching and mortgage availability. Income targeting alone does not establish
access. Declared financing assistance may affect both capital and household
budgets; its treatment needs explicit program rules, not assumed double benefit.

### D. Test co-op operations and affordability over time

Specify operating costs, reserves, common debt, nonresidential income if supported,
maintenance allocations, escalation and sponsor/manager obligations. Evaluate
maintenance increases, cost shocks and buyer income/rate assumptions at relevant
dates. The baseline's minimum 2% annual maintenance increase is a program input,
not a guarantee that 2% is sufficient to meet costs or that buyers can sustain it.

This carries over Stanyan's practice of linking capital and operations while
respecting Jerome's ownership model. It does not import LOSP, LIHTC rental equity,
San Francisco AMI rules or a generic rental debt-coverage target into Open Door.

### E. Produce an attributed decision table

For each scenario show homes by target population, assumed physical program,
new public funding required and its status, total included public investment,
buyer cash requirements, monthly costs, long-run co-op adequacy, amenity-delivery
obligations, schedule and unresolved constraints. Keep objectives separate. An
analyst or community participant may prefer more homes, deeper affordability,
lower public cost or a particular amenity; the tool should expose those tradeoffs
and their attribution rather than invent a universal community-benefit ranking.

## 5. The next bounded experiment

**First reproduce a supplied professional budget and its decision-relevant
sensitivities. Then transfer the structure to Jerome.** This avoids requiring a
complete housing theory before learning something testable.

| Slice | Evidence / output | What counts as success |
| --- | --- | --- |
| Stanyan reconstruction, this study | Four frozen records, capital snapshots, selected Year 1 operating calculation, source conflicts | Every reported value has a dated page; arithmetic discrepancies remain visible; no claim of blind prediction |
| Next finance prototype | An isolated budget-comparison module with capital/operating domains and funding status; use Stanyan as an openly known fixture | Distinguish $153.252m land-excluding and $169.152m land-including budgets; preserve rounding residuals; never count operating subsidy as permanent construction capital |
| Next long-run exercise | Reconstruct selected years from the source worksheet, obtain original Excel if available, resolve PBV growth and staffing conflicts with a qualified reviewer | Formulas, time periods, loan repayment assumptions and exception decisions match the chosen dated source; unresolved conflicts block a fidelity claim |
| Jerome application | Practitioner-supplied Open Door cost, sales, maintenance and buyer-finance inputs; historical versions preserved | A reviewer can change an assumption and explain its effect on project gap, buyer access and ongoing co-op budget |
| Subsequent evaluation | A new case and frozen rubric, including a delayed/changed case | Evaluate missed constraints and useful decisions; separate known-case reconstruction from a genuinely withheld assessment |

The current [recipe engine](../../src/housing_recipe/README.md) provides typed
methods, dependencies and impact previews, but its implemented methods cover a
small area calculation and a reviewed PLUTO import. It is not already an agency
underwriting engine. The [benefit module](../../src/housing_benefit/README.md)
compares supplied rental offers against household cost/bedroom tests; it does not
derive financially viable rents or borrower eligibility. The newer live-lot trial
does not reconcile its independent offers to its assumed area budget.

A notebook could make the proposed experiment easier to inspect, but the core
methods should stay usable by the existing CLI and agent skills. No new notebook,
provider integration, usability rewrite or production financial method is added
by this case study. The immediate deliverable is a concrete professional precedent
and a precise comparison that can guide the next modeling implementation.
