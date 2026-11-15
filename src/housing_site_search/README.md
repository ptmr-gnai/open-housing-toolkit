# Goal seeking over nonhousing sites

Start with a verified [broad discovery](../housing_site_discovery/README.md), then
add an explicit [rental underwriting template](../housing_underwriting/README.md)
and desired-program/search targets. Discovery remains useful without a model and
its universe is unchanged by the search. No auto-use or extra-FAR test is required.

```sh
python -m housing_site_search build --discovery runs/my-discovery --underwriting runs/my-rental-model --input config/site-search/transit-rental-targets.json --out runs/my-search
python -m housing_site_search verify --run runs/my-search
```

Open packet.html/packet.md. Every original lot remains in all-lots.csv; all modeled
program/price combinations, including failures and unknowns, remain in trials.csv
and results.json. Upstream source packets are copied and verified. Selected
scenarios have independently verified financial packets under models/. New outputs
use fresh local directories; never rewrite completed cases.

## Search from a desired program

The request declares a finite set of whole-home programs and assumed land prices.
For each recorded-nonhousing lot with known area:

```text
required residential net area = proposed homes × assumed net sf/home
required gross area = net area / net efficiency / residential share of gross
required zoning-area proxy = gross area / assumed gross-per-zoning-sf
required zoning FAR proxy = zoning-area proxy / recorded lot sf
```

The resulting program and gross area feed the supplied financial template. This
**inverts the question**: what would this stated program require on this lot?
The answer is conditional area arithmetic, not a layout, a zoning opinion or a
forecast of net added homes. Recorded residential FAR can be larger than the
required proxy; those sites remain in the search. A maximum scenario FAR is an
optional, explicitly declared search target rather than a general discovery gate.

All money is USD in the template's explicit price basis. Land price/sf values are
analyst assumptions, not automatically estimated market prices. The current
checked-in scenarios are method tests and are not Jeremy-approved objectives.

## Scale assumptions explicitly

Unit-rate capital lines already scale by gross area or homes. Every fixed capital
line except overridden land must separately declare fixed/per-home/per-gross-sf/
per-lot-sf scaling. Income, expenses, replacement reserves, below-line fees and
other source amounts each declare their scaling. Reference homes/gross area come
from the financial template; the request supplies reference lot area. There are
no implicit scale economies or site-specific relocation/remediation estimates.

Dollar appraisal/debt caps and other annual debt service remain fixed scenario
assumptions. Those values need reconciliation for a real project. All template
source statuses are downgraded to **proposed** when transferred to a different
site/program; no commitment is invented by scaling. Original template inputs and
source references remain available for comparison.

## Explicit goals, failures and unknowns

Targets can include allowed zoning paths and use-review lanes, maximum station
point distance, outside-IBZ point status, no active linked ZAP project, a required
FAR cap, maximum unallocated capital/home, maximum scheduled tenant rent/home and
minimum annual cash after modeled deductions. An explicit historical-housing-signal
target can require no positive signal across successfully queried DOB BIS, DOB NOW,
HPD registration and HPD affordable-production records; positive historical or
program signals trigger reconciliation, and missing review or
failed coverage stays unknown. A literal no-positive return is not proof of no
housing or occupants. Tenant-rent stream IDs and cap time scope (`year_one` or
`all_projection_years`) are explicit; both year-one and peak projected rent are
reported. The cap checks scheduled rent in the selected period, before vacancy;
operating support is not silently treated as tenant rent. This rent measure is an
average scheduled amount, not an income-eligibility or household affordability test.

Missing required station/IBZ/application evidence creates an unknown target.
Failed targets and unknowns are distinct; all lot/trial records remain visible.
No active rows in the retained join is a bounded query result, not a complete
pipeline finding. Outside an IBZ polygon refers to the recorded parcel point,
not a verified parcel-wide legal-policy intersection.

The search evaluates at most 25,000 declared lot/program/price combinations.
It does not prove a global optimum outside that finite grid. Matching scenarios
are compared on lower required FAR, lower unallocated capital/home and more
proposed homes. Non-dominated alternatives remain available without monetary
weights or a universal site score. A small displayed/detail selection is ordered
by capital gap/home, FAR, proposed homes and deterministic IDs for inspection.
It is not a recommendation or community-benefit ranking. Other meaningful
criteria remain in the source discovery and need practitioner review.

## Compose the next stage

```sh
python -m housing_site_search handoff --run runs/my-search --bbl SELECTED_MATCHING_BBL --out runs/my-handoff
python -m housing_site_search deepen --handoff runs/my-handoff --out runs/my-deep
```

The search verifies and delegates to the existing explicit evidence-only handoff.
It does not supply a legal building program or silently run imagery. Other
nonhousing lots can be selected through broad discovery even if they fail the
particular financial/search targets. Optional massing, housing-offer comparison,
RER and rendering remain independent toolkit stages with their own inputs.

The model does not resolve actual occupancy/leases, owner intent, title, shared
rights/assemblage, applicable zoning text/maps, physical layout, environmental
satisfaction, program eligibility, construction financing/timing or investor returns.
Passing all declared targets establishes a conditional scenario-search match only.

## Explicit program-to-area adapter

`area-handoff --run SEARCH --trial SCENARIO_ID --parcel-evidence VERIFIED_PARCEL
--out NEW_RUN` preserves the complete search and selected financial packet and
replays the existing same-BBL parcel evidence with the chosen area assumptions.
It verifies the area request and quantities against the selected trial. The new
analysis/ is an ordinary verified parcel/area package accepted by existing recipe
and geometry modules. The source's collection failures remain visible.

This branch requires explicit scenario selection and source evidence. A failed
search alternative can be examined diagnostically, with its original status
preserved; the adapter does not silently make it meet targets. Schematic parcel
containment and area agreement still do not establish legal height, floor plans,
construction system, context or financing. Flat cost/sf assumptions do not
automatically respond to a taller or more complex massing.

## Same-evidence sensitivity

`compare --left FIRST_SEARCH --right SECOND_SEARCH --out NEW_RUN` verifies both
packages, requires identical reviewed site evidence, and records changed trials,
values, target failures/unknowns and lot-set membership. Both full target requests
and financial templates remain visible. This exposes whether a different rent
cap scope, construction cost, capital-gap target or transit distance changes the
candidate set. Several changed inputs are not presented as a one-variable effect.
