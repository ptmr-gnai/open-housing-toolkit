# Modules and research reference

Use [Investigate a lot](../guides/investigate-a-lot.md) for the main live workflow or
[First run](../guides/first-run.md) for the offline tour. This page keeps the detailed module
examples, earlier experiments and research notes available on demand. Commands
below run from the repository root, not this docs directory.

## Discover sites across an area

The [broad nonhousing module](../../src/housing_site_discovery/README.md) retains
all lots and groups nonhousing uses by general residential-use, rezoning and
special/unresolved paths. It requires no auto-use, size, extra-FAR or financing
admission gate. Public context includes station points, industrial policy zones
and DCP Fast Tracker records with source vintages.

[Practitioner guide](../guides/discover-sites.md) ·
[Discovery skill](../../skills/discover-nonhousing-sites/SKILL.md) ·
[Corrected case studies](../../research/nonhousing-discovery/README.md).
Separate [dwelling-signal review](../../src/housing_site_review/README.md) and
[monthly zoning-record reconciliation](../../src/housing_zoning_review/README.md)
carry conflicts and failed coverage into subsequent work.

The [goal-search module](../../src/housing_site_search/README.md) combines verified
site evidence with desired housing programs, explicit land/cost/rent assumptions
and public-context/financial targets. The [rental model](../../src/housing_underwriting/README.md)
projects operations, sizes constrained permanent debt and distinguishes modeled
funding gaps from actual commitments. Failed/unknown scenarios stay visible;
non-dominated alternatives are not site recommendations.

The earlier [explicit FAR-screen experiment](../../research/discovery-v1/README.md)
and its [skill](../../skills/discover-housing-sites/SKILL.md) remain unchanged for
replay and comparison. The [BetaNYC registry study](../../research/public-data-registry/README.md)
adds tested source-discovery resources, including non-NYC portals.

## Ownership and sale history

The [ownership module](../../src/housing_ownership/README.md) collects ACRIS recorded
instruments (deeds, mortgages, agreements) with parties and amounts, DOF sales rows
and the PLUTO tax-roll owner label for one lot outside Staten Island. It reports a
tax-roll owner that lags the latest deed as a conflict. Not a title opinion.
[Skill](../../skills/collect-ownership-evidence/SKILL.md) ·
[retained runs](../../research/ownership-evidence/README.md) ·
[source catalog](source-catalog.md).

## Development activity

The [activity module](../../src/housing_activity/README.md) checks candidates for
recent demolition, foundation, excavation, new-building and construction-fence
records (DOB NOW, legacy DOB, HPD), so lots already being developed are flagged
before anyone studies them. [Skill](../../skills/check-development-activity/SKILL.md).

## Massing-grounded concept renders

The [concept module](../../src/housing_concept/README.md) draws a to-scale front
elevation from a verified massing and compiles a fixed, numbers-only image prompt, so
a picture on a site photo shows the modelled building replacing what is there.
[Skill](../../skills/render-massing-concept/SKILL.md).

## Site feasibility report

The [feasibility report module](../../src/housing_feasibility/README.md) assembles a
lot's verified evidence, ownership, massing, underwriting scenarios and render into
one standard memo: site, zoning, sources and uses, operating pro forma, debt sizing,
sensitivity, open items and sources. It re-verifies every input and adds no new
estimates; `report.json` is the typed version for other tools.
[Skill](../../skills/assemble-feasibility-report/SKILL.md).

## Edit the analysis recipe

For a practitioner investigating a known lot, the numerical modeling stage can
now be edited independently of evidence collection and packet publication:

```sh
python -m housing_recipe build --from-run examples/parcel-investigation --recipe config/recipes/area-budget.json --out runs/recipe-base
python -m housing_recipe impact --run runs/recipe-base --recipe config/recipes/area-budget-with-reserve.json
```

[Recipe guide](../../src/housing_recipe/README.md) · [Agent skill](../../skills/run-analysis-recipe/SKILL.md) ·
[Worked packet](../../examples/analysis-recipe/base/packet.md).
The examples reproduce the current area model, insert a reserve step, and replace
the home-equivalent method. Typed method signatures, dependency checks and
required review gates provide engineering checks; professional acceptance remains
pending. The comparison harness remains deferred; the separate exploratory geometry
module is described below.

## Compare explicit housing programs

The first [conditional housing-cost module](../../src/housing_benefit/README.md) compares two
illustrative rental offers for hypothetical households, with strict money/unit types,
versioned methods, source-pinned historical references and a reviewable claim graph:

```sh
python -m housing_benefit demo --out runs/affordability-demo
```

[Base packet](../../examples/affordability-comparison/packet.md) ·
[Utility sensitivity](../../examples/affordability-utilities/packet.md) ·
[Agent skill](../../skills/compare-housing-programs/SKILL.md).
The larger offer has more homes but fewer that meet the lower-income profile's
cost-and-bedroom test. Eligibility, delivery, occupancy and the no-action baseline
are not determined; no winner or causal benefit estimate is produced. This is a
bounded implementation under the broader [community-benefit proposal](specs/community-benefit.md).

## Prepare a guide-mapped RER draft

The [RER preparation module](../../src/housing_rer/README.md) maps 50 scoped instruction slots
from the pinned City guide, form and criteria. It produces a separate five-section
draft for each illustrative program, with populated, illustrative, missing,
interpretation-needed and conditional not-applicable states.

```sh
python -m housing_rer demo --out runs/rer-draft
```

[Start with the worked packet](../../examples/rer-preparation/packet.md) ·
[Instruction map](../../examples/rer-preparation/coverage.md) ·
[Agent skill](../../skills/prepare-rer-draft/SKILL.md).
The cost diagnostic stays in a supplemental appendix. AMI classifications,
program eligibility, ZSF, community data, applicability and applicant interpretation
are not inferred from it. These are incomplete preparation drafts, not official
forms or compliance findings. A guide/form instruction divergence remains explicit.

## Ground a scenario in explicit geometry

The [geometry specification](specs/geometry-grounding.md) maps the evidence,
assumptions and professional interpretation needed to connect a real site to a
visual asset. The first [geometry module](../../src/housing_geometry/README.md) builds an
assumed massing on a sourced parcel polygon and checks its areas against a verified
analysis. It exports a plan, massing view, OBJ mesh, floor schedule and visual handoff.

The [worked examples](../../examples/grounded-massing/README.md) show why a total-area
match alone is insufficient: one matches 40,000 gross sf but disagrees on program
allocation. The second changes an explicit use-allocation assumption. Neither
establishes zoning, layouts, physical fit or financing. The geometry engine generates no AI image. A subsequent
[recorded image-generation experiment](../../examples/geometry-render/README.md) uses its
rasterized views; the existing photo renderer still does not consume this handoff.

## Use the rendering module independently

Bring a photo and an explicit visual scenario, with an optional analysis IR:

```sh
python -m housing_render prepare --scene examples/site-concept/scene.json --scenario examples/site-concept/scenario.json --out runs/my-concept
```

This prepares a provider-independent brief. An agent then calls an image provider
and attaches the output with an invocation and visual-review receipt. See the
[rendering guide](../../src/housing_render/README.md), [rendering skill](../../skills/render-site-concept/SKILL.md),
and [actual generated example](../../examples/site-concept/with-analysis/packet.md).
The example reference is an external chat attachment; supply your own local photo
to reproduce a source-byte-bound run. Collection and modeling are not required.

## Project resources

- [730 Stanyan methodology case study](../../research/stanyan-methodology/README.md):
  four dated agency reviews, capital and operating-budget reconciliation, source
  conflicts, and a comparison with the 1337 Jerome homeownership brief. This is a
  known-case reconstruction; its proposed financial extensions are not implemented
  production methods.
  The [executable research benchmark](../../research/stanyan-methodology/benchmark.md)
  reconstructs selected capital/operating budgets and traces one-assumption
  diagnostics. It is the current professional reference case; long-run underwriting
  and cross-program transfer remain unvalidated.
- [Project tenets](tenets.md): trust domain expertise, reuse established resources,
  empower practitioners and their agents, and keep the work inspectable.
- [Community-benefit proposal](specs/community-benefit.md): a bounded plan for
  applying existing resources to a practitioner-led scenario comparison.
- [Community-benefit research](../../research/community-benefit/report.md): agency frameworks,
  housing/transit evidence, candidate metrics and the boundaries between context,
  scenario arithmetic, causal effects and community priorities.
- [Original probe proposal](proposal.md): the initial experiment and open source
  approach, retained as project history. Current direction is set out above.
- [425 Grand Concourse calibration](../../research/grand-concourse-calibration/report.md):
  a real project challenges our zoning, physical and financing assumptions. This is
  an openly known case, not a blind prediction benchmark.
- [Fresh AI assumptions review](../../research/conclusion-probe/reviews/agent-assumptions-review.md):
  material omissions and modeling problems found despite passing engineering checks.
- [Source audit](../../research/source-audit/report.md): a bounded inventory of public
  data sources and agency workflows.
- [Papercut log](papercuts.md): observed failures, fixes and remaining gaps.

The original executable parcel probe is centered on 170 Street on the 4 line in
the Bronx. Read [its advisor brief](../../research/legacy-probe/outputs/advisor-brief.md) and open
`research/legacy-probe/outputs/advisor-explorer.html` locally. Its reports preserve the original model;
the later review calls for revisions to housing evidence, geometry, capital needs
and diligence priorities. Do not treat the original lead or scenarios as validated.

## Experiments

| Component | What works | What remains open |
| --- | --- | --- |
| [Parcel probe](../../research/legacy-probe/probe.json) | Cached public data, conditional scenarios, typed claims and offline replay | Legal and physical feasibility, current occupancy, complete economics |
| [Applicant eligibility](../../research/eligibility-gates/README.md) | Source-bound rules and scoped unknown/pass/fail states | Actual credentials and professional interpretation |
| [Requirement coverage](../../research/requirement-coverage/README.md) | Known omissions and addendum changes can block premature exports | Complete semantic coverage and unfamiliar-user testing |
| [One conclusion](../../research/conclusion-probe/README.md) | Source changes, stale judgments and conflicts propagate through a bounded graph | Discovery of omitted evidence and justification of the best next action |
| [Real project calibration](../../research/grand-concourse-calibration/README.md) | Dated quotations and comparison boundaries are reproducible | Independent forecast accuracy, complete underwriting and practitioner benefit |

## Local development checks

Normal user setup needs none of these commands. They are contributor checks,
reading frozen inputs and writing any new artifacts into ignored local scratch:

```sh
make build
make check
make research-check
make release-check
```

`make build` creates a new runs/core-* folder. `make check` creates a new runs/check-*
folder and validates there; research validators return results without overwriting
shipped validation records. The optional release check writes screenshots only in
its new runs/release-* folder. See [local-only execution](../guides/local-only.md).

## Source snapshots and live collection

Treat shipped research/legacy-probe/cache/ and examples/ as read-only. They preserve source bytes,
versions, interpretation limits and historical experiments. Use [Investigate a lot](../guides/investigate-a-lot.md)
for current live collection into a fresh local run. Do not run historical research
builders or refresh shipped snapshots as part of setup or an ordinary analysis.
The legacy collect.py command also writes a new local runs/collection-* folder;
it does not automatically rebind or update the frozen core analysis.

## Evidence and assumptions

ir.json records observed, derived, assumption, judgment, and unknown claims.
Observed claims point to source rows and fields. Derived claims declare dependencies
and formulas. Assumptions have units and rationale. Judgments explain selection or
rejection. Unknown gates stay unresolved. Sources and outputs have byte hashes.

The full bounded universe has 2,323 lots. The radius screen has 881 lots; 486 pass
the numeric rules, ten are shortlisted and three challenged. Those numbers are
snapshot results, not estimates for the borough or a count of developable sites.

The visual explorer is a selected view of the IR. Its sliders are local what-if
calculations using the same formulas; they do not overwrite the saved graph. To
retain a revised graph, rerun the JSON DSL. The map is a coordinate plot without
street routing or parcel boundaries. Massing is an abstract area diagram, not a
rendering of an approved or physically verified building.

## Limits and first finding

The simple capacity ranking elevated an Education Department parcel and a Police
Department parcel. Their development filings reinforce the need for a civic-use
lens before calling capacity an opportunity. The private lead has recorded retail
use, historical community and commercial filings, and E-designation requirements.
The next action is current occupancy and lease verification.

The conditional housing model uses a declared conversion between the recorded FAR
area proxy and gross building area. It is not a legal or architectural design.
Cost excludes land and several essential development costs. Rent for debt coverage
does not include an equity return. Additional non-debt capital is not a subsidy
estimate. Official AMI rents, transit job access, title, availability, and program
financing have not been verified. No site recommendation or causal econometric
finding follows from this probe.

MIT licensed code; original documentation CC BY 4.0. Public agency source
snapshots retain their publishers' terms; see [DATA-LICENSES.md](../../DATA-LICENSES.md).
The project license does not relicense those sources. Snapshot dates and source
URLs are part of the research record; later retrieval does not certify historical
byte equivalence.

## Contribute and continue

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for reproducing a result, challenging an
interpretation, and proposing a change. The next priorities are integrating the
review corrections into a versioned IR, testing a withheld real project, and
measuring usefulness with housing practitioners. Preserve failed experiments and
their assumptions so improvements can be assessed.

## Deterministic backpressure and papercuts

Run `make check` for syntax, artifact lint, ten behavioral tests, JSON Schema
validation and hash checks. Schema checks require the pyproject.toml dev extra. Run
`make release-check` to also check browser formula parity, sliders, trace links,
map containment, desktop/mobile layout, and byte-identical offline replay. The
optional browser checks require Node, Playwright and Chromium. Tests do not need
Internet destinations; the browser process may require sandbox socket permission.

`python gates.py advisor-review` allows a conditional review pack.
`python gates.py public-site-proposal` exits 2 while required site gates are
unresolved. This is an internal playbook control, not a request to send or publish.
Technical validation cannot substitute for professional feasibility review.

See docs/papercuts.md for observed failures, causes, controls and remaining gaps.

`make research-check` runs the retained research validators and test suites.
GitHub Actions runs `make check` and `make research-check` on pushes and pull
requests. Browser checks remain a separate optional local release check. Passing
CI verifies the implemented technical checks, not professional correctness.

The [425 Grand Concourse calibration](../../research/grand-concourse-calibration/report.md) compares 2015 solicitation conditions with later public project evidence. It preserves 42 quoted facts, unresolved definitions, a missed specific zoning mechanism and seven interpretation checks. This is an openly known case, not a blind prediction benchmark. Run its offline validator and tests using the instructions in that folder.
