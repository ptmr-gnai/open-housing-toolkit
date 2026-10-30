# Conditional housing-program comparison

Use an editable checkout; see [setup](../../docs/guides/setup.md).

First bounded implementation under the [community-benefit proposal](../../docs/reference/specs/community-benefit.md)
and [project tenets](../../docs/reference/tenets.md). It compares explicit rental offers for
hypothetical households. It does not estimate causal community benefit or decide
eligibility, availability, regulatory compliance or an overall preferred project.

## Try it

Python 3.11+, standard library only for build/replay/verify:

```sh
python -m housing_benefit demo --out runs/affordability-demo
python -m housing_benefit impact --run runs/affordability-demo --input examples/affordability-inputs/higher-utilities.json
python -m housing_benefit replay --from-run runs/affordability-demo --input examples/affordability-inputs/higher-utilities.json --out runs/affordability-utilities
python -m housing_benefit verify --run runs/affordability-utilities
```

Open `packet.html`. The offline demo uses the same real lot identity and verified
upstream source packet, with two **illustrative** programs. It does not derive those
programs from the area's zoning or the massing. No API key, network or AI model is
required. For an agent, use [the comparison skill](../../skills/compare-housing-programs/SKILL.md).

To build from explicit inputs:

```sh
python -m housing_benefit build --analysis examples/analysis-recipe/base --references examples/affordability-inputs/reference-source --input examples/affordability-inputs/request.json --out runs/my-comparison
```

A verified `housing_workflow` or `housing_recipe` run supplies site identity and
unresolved current-use context. Collection, geometry and rendering are not invoked.
The original upstream package is preserved in `analysis-run/`.

## What the demo establishes

| Quantity | Program A | Program B |
| --- | --- | --- |
| Explicit proposed homes | 24 | 36 |
| Two-bedroom homes with assumed $1,000 rent + $100 tenant utilities | 16 | 8 |
| Two-bedroom homes with assumed $1,800 rent + $100 tenant utilities | 8 | 28 |
| Proposed lower-rent restriction duration | 60 years | 30 years |
| Delivery / legally secured restriction | Unknown / not established | Unknown / not established |

The hypothetical four-person profile at the rounded **2025** 30%-AMI income
reference has $48,600 annual income. At the declared 30% housing-cost threshold,
its monthly budget is $1,215. The 60%-AMI reference is $97,200, with a $2,430 budget.
These are hypothetical profiles based on published rounded thresholds, not observed
households or exact program eligibility limits.

Program B offers 12 more homes but 8 fewer that meet the lower-income profile's
cost-and-exact-bedroom test. No winner is selected. The higher-utilities sensitivity
changes Program A's lower-rent gross cost to $1,250, exceeding $1,215 and changing
the affected count from 16 to zero. **Zero here is an explicit cost-test result,
not a conclusion of no community benefit.**

Counts do not account for program income caps, minimum incomes, assets, selection,
other eligibility rules, availability, suitability or actual delivery. Program
rents are assumptions and are not asserted to satisfy the reference table's AMI
program rules. Published rent references are retained as context only.

## Contracts and calculations

[Request schema](request.schema.json), [IR schema](ir.schema.json), frozen Claim
records, Kind/Unit enums and [versioned method signatures](methods.py) expose the
interfaces. Runtime checks enforce sums, unique IDs, source compatibility and graph
arithmetic beyond JSON Schema. Duplicate JSON keys and NaN/Infinity are rejected.

USD inputs are nonnegative decimal **strings**, not binary floats. Homes/bedrooms/
years are bounded integers; booleans and fractional homes are rejected. Exact
Decimal arithmetic evaluates:

- Gross monthly cost = supplied rent + supplied tenant-paid utilities.
- Annual cost = gross monthly cost × 12.
- Display burden = 100 × annual cost / hypothetical annual income (six decimals).
- Cost test = annual cost × 100 ≤ annual income × threshold percent, **before rounding**.
- Exact-bedroom test = offered bedrooms equals the profile's specified category.
- Profile count = sum of supplied home counts whose two tests are true.

The equality-bedroom convention is explicit, not an architectural or eligibility
standard. Duration is retained and compared in rows; no fixed-rent trajectory or
unit-years/household-years benefit is inferred. The declared threshold is a policy
assumption, not an optimized welfare criterion.

Every program quantity has a rationale and remains an assumption. Source facts
carry passage/field references; calculations carry method and dependency IDs.
Source reference income is a fact about the historical table; using it as the income
of a hypothetical household is a separate assumption. The IR fixes eligibility as
not determined, review as pending, ranking as null and causal benefit as not estimated.

## Source extraction and vintage discipline

The demo uses selected rows of NYC's Racial Equity Report guide, printed page 6,
Table 3, with a July 1, 2025 internal stamp. The table's income and rent figures are
rounded illustrative references. Both table years and the input price year must
match; no inflation or compatibility override is supported. We deliberately avoid
the live page's mixed 2026-income/2025-rent headings.

`reference-source/passages.txt` contains the two selected rows and table title.
`receipt.json` records the exact original PDF URL/hash, retrieval, printed page,
column mapping and extraction provenance. Offline validation hashes and parses the
excerpt. The external PDF is **not bundled**, and normal verification does not
re-extract it. This limitation is shown in every packet; hashes/receipts are not
provider-signed authenticity proofs or semantic acceptance.

Preparation was executed against the source PDF; to independently repeat it after
retrieving matching bytes, Poppler's `pdftotext` is needed for preparation only:

```sh
python scripts/prepare_benefit_reference.py --pdf PATH_TO_ORIGINAL.pdf --retrievals research/community-benefit/retrievals.json --out runs/reprepared-benefit-reference
```

The script checks the original retrieval hash, page, header, year, column layout
and selected rows. Upstream terms remain applicable. A citation does not establish
that NYC or any expert reviewed this implementation.

## Replay, impact and limits

Runs are immutable through the CLI. `verify` checks complete inventories, byte and
implementation bindings, source parsing, the upstream package, typed arithmetic
and exact output recomputation. `impact` previews direct changes and transitive
dependents before a new run. Changing duration does not artificially change a
cost-test count; it changes the assumption and packet row. Any changed input
regenerates the comparison artifacts. Old runs remain intact.

P0 supports only explicit illustrative rental offers, proposed restriction status,
and unresolved delivery/occupancy/no-action. An adapter for established occupancy,
known baselines, binding instruments, homeownership or agency program eligibility
requires a separate reviewed contract. The absence of these adapters is not a
clearance. No net-addition, displacement, transit-access, financial or causal-rent
claim is exported. Transit opportunity context and a broader benefit module remain
future work. Human professional review and first-time usability remain pending.
