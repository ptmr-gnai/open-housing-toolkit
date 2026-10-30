# Open Housing Toolkit

The Open Housing Opportunity Playbook research project.

An open source, modular toolkit for housing practitioners and the agents working
on their behalf. It brings existing data, housing resources and analytical methods
into workflows for research, scenario modeling and proposal materials. Sources,
assumptions and professional judgments stay visible so people can inspect, adapt
and correct the work.

We are learning the housing process in public. Our contribution is tooling that
helps people use established resources together; domain experts guide method
selection and interpretation. Read the [project tenets](docs/tenets.md) and the
[community-benefit proposal](docs/specs/community-benefit.md) for how we apply that
approach and what remains to be built and validated.

**Status: early research prototype, open for feedback.** It is ready to share and
improve in public. It does not establish that a lot is available, a design fits,
a project is financed, or a proposal is ready to submit. Human housing expert
acceptance and practitioner usefulness remain untested. The older components below remain
separate experiments. The new bounded workflow integrates one path; it is not a
complete professional process.

## Start here

**Try the example.** Give your agent [AGENTS.md](AGENTS.md) and the
[start-here skill](skills/start-here/SKILL.md), or run this from a checkout with
Python 3.11+:

```sh
python scripts/first_run.py --out runs/my-first-run
```

Open `runs/my-first-run/README.md`, then its linked packets. This offline tour needs
no pip install, API key or image provider. It chains cached evidence, an area recipe,
independently assumed housing offers and incomplete RER drafts. Offer counts are
not derived from site capacity. [First-run guide](docs/first-run.md).

**Investigate your lot.** Give your agent a Bronx address or BBL and the question
you want answered, and use [the parcel investigation skill](skills/housing-investigation/SKILL.md).
It can collect live public records without a development scenario. Supplied area
assumptions remain explicit; absent inputs remain missing.

[See the actual live-lot worker trial](examples/live-lot-trial/README.md): a new
worker collected records for a different property and ran evidence → area model →
independent offer comparison → RER preparation. Its packet opens with source dates,
recorded findings, assumptions and unresolved inputs. It is a workflow trial, not a
feasibility finding. [How to read the opening](docs/packet-reading.md).

Modules below can also be used independently. Geometry and image generation are
optional branches; the full professional housing process remains incomplete.

## Edit the analysis recipe

For a practitioner investigating a known lot, the numerical modeling stage can
now be edited independently of evidence collection and packet publication:

```sh
python -m housing_recipe build --from-run examples/parcel-investigation --recipe recipes/area-budget.json --out runs/recipe-base
python -m housing_recipe impact --run runs/recipe-base --recipe recipes/area-budget-with-reserve.json
```

[Recipe guide](housing_recipe/README.md) · [Agent skill](skills/run-analysis-recipe/SKILL.md) ·
[Worked packet](examples/analysis-recipe/base/packet.md).
The examples reproduce the current area model, insert a reserve step, and replace
the home-equivalent method. Typed method signatures, dependency checks and
required review gates provide engineering checks; professional acceptance remains
pending. The comparison harness remains deferred; the separate exploratory geometry
module is described below.

## Compare explicit housing programs

The first [conditional housing-cost module](housing_benefit/README.md) compares two
illustrative rental offers for hypothetical households, with strict money/unit types,
versioned methods, source-pinned historical references and a reviewable claim graph:

```sh
python -m housing_benefit demo --out runs/affordability-demo
```

[Base packet](examples/affordability-comparison/packet.md) ·
[Utility sensitivity](examples/affordability-utilities/packet.md) ·
[Agent skill](skills/compare-housing-programs/SKILL.md).
The larger offer has more homes but fewer that meet the lower-income profile's
cost-and-bedroom test. Eligibility, delivery, occupancy and the no-action baseline
are not determined; no winner or causal benefit estimate is produced. This is a
bounded implementation under the broader [community-benefit proposal](docs/specs/community-benefit.md).

## Prepare a guide-mapped RER draft

The [RER preparation module](housing_rer/README.md) maps 50 scoped instruction slots
from the pinned City guide, form and criteria. It produces a separate five-section
draft for each illustrative program, with populated, illustrative, missing,
interpretation-needed and conditional not-applicable states.

```sh
python -m housing_rer demo --out runs/rer-draft
```

[Start with the worked packet](examples/rer-preparation/packet.md) ·
[Instruction map](examples/rer-preparation/coverage.md) ·
[Agent skill](skills/prepare-rer-draft/SKILL.md).
The cost diagnostic stays in a supplemental appendix. AMI classifications,
program eligibility, ZSF, community data, applicability and applicant interpretation
are not inferred from it. These are incomplete preparation drafts, not official
forms or compliance findings. A guide/form instruction divergence remains explicit.

## Ground a scenario in explicit geometry

The [geometry specification](docs/specs/geometry-grounding.md) maps the evidence,
assumptions and professional interpretation needed to connect a real site to a
visual asset. The first [geometry module](housing_geometry/README.md) builds an
assumed massing on a sourced parcel polygon and checks its areas against a verified
analysis. It exports a plan, massing view, OBJ mesh, floor schedule and visual handoff.

The [worked examples](examples/grounded-massing/README.md) show why a total-area
match alone is insufficient: one matches 40,000 gross sf but disagrees on program
allocation. The second changes an explicit use-allocation assumption. Neither
establishes zoning, layouts, physical fit or financing. The geometry engine generates no AI image. A subsequent
[recorded image-generation experiment](examples/geometry-render/README.md) uses its
rasterized views; the existing photo renderer still does not consume this handoff.

## Use the rendering module independently

Bring a photo and an explicit visual scenario, with an optional analysis IR:

```sh
python -m housing_render prepare --scene examples/site-concept/scene.json --scenario examples/site-concept/scenario.json --out runs/my-concept
```

This prepares a provider-independent brief. An agent then calls an image provider
and attaches the output with an invocation and visual-review receipt. See the
[rendering guide](housing_render/README.md), [rendering skill](skills/render-site-concept/SKILL.md),
and [actual generated example](examples/site-concept/with-analysis/packet.md).
The example reference is an external chat attachment; supply your own local photo
to reproduce a source-byte-bound run. Collection and modeling are not required.

## Start here

- [Project tenets](docs/tenets.md): trust domain expertise, reuse established resources,
  empower practitioners and their agents, and keep the work inspectable.
- [Community-benefit proposal](docs/specs/community-benefit.md): a bounded plan for
  applying existing resources to a practitioner-led scenario comparison.
- [Community-benefit research](research/community-benefit/report.md): agency frameworks,
  housing/transit evidence, candidate metrics and the boundaries between context,
  scenario arithmetic, causal effects and community priorities.
- [Original probe proposal](docs/proposal.md): the initial experiment and open source
  approach, retained as project history. Current direction is set out above.
- [425 Grand Concourse calibration](research/grand-concourse-calibration/report.md):
  a real project challenges our zoning, physical and financing assumptions. This is
  an openly known case, not a blind prediction benchmark.
- [Fresh AI assumptions review](research/conclusion-probe/reviews/agent-assumptions-review.md):
  material omissions and modeling problems found despite passing engineering checks.
- [Source audit](research/source-audit/report.md): a bounded inventory of public
  data sources and agency workflows.
- [Papercut log](docs/papercuts.md): observed failures, fixes and remaining gaps.

The original executable parcel probe is centered on 170 Street on the 4 line in
the Bronx. Read [its advisor brief](outputs/advisor-brief.md) and open
`outputs/advisor-explorer.html` locally. Its reports preserve the original model;
the later review calls for revisions to housing evidence, geometry, capital needs
and diligence priorities. Do not treat the original lead or scenarios as validated.

## Experiments

| Component | What works | What remains open |
| --- | --- | --- |
| [Parcel probe](probe.json) | Cached public data, conditional scenarios, typed claims and offline replay | Legal and physical feasibility, current occupancy, complete economics |
| [Applicant eligibility](research/eligibility-gates/README.md) | Source-bound rules and scoped unknown/pass/fail states | Actual credentials and professional interpretation |
| [Requirement coverage](research/requirement-coverage/README.md) | Known omissions and addendum changes can block premature exports | Complete semantic coverage and unfamiliar-user testing |
| [One conclusion](research/conclusion-probe/README.md) | Source changes, stale judgments and conflicts propagate through a bounded graph | Discovery of omitted evidence and justification of the best next action |
| [Real project calibration](research/grand-concourse-calibration/README.md) | Dated quotations and comparison boundaries are reproducible | Independent forecast accuracy, complete underwriting and practitioner benefit |

## Reproduce without network or models

Requires Python 3.10 or later; the deterministic pipeline uses the standard library.

```sh
python pipeline.py
python -m unittest discover -s tests -v
python validate.py
```

This regenerates the IR, shortlist, three dossiers, report, brief, communication
draft, explorer and output manifest from cached public sources. No account, API
key, paid model, or network connection is needed for replay. It does not reproduce
the advisory expert judgments because they have not yet occurred; researcher
judgments are explicit in probe.json.

To save a changed assumption, copy probe.json to a new JSON file, edit its value
and rationale, and run:

```sh
python pipeline.py --config alternative.json --out sensitivity-output
```

Only version 0.1 supported formulas and ranking are executable. See
schemas/playbook.schema.json and pipeline.validate_config. This is a small
declarative DSL with named rules, not a general zoning compiler. Candidate review
judgments are tied to the cached evidence; rerun human review if sources change.

## Collection and source freshness

The current run includes exact URLs and timestamps in cache/*.source.json and
unchanged source bytes in cache/*.body. Source bodies are hashed before replay.
Metadata timestamps describe dataset updates, not the age of every parcel field.
The station CSV lacks an explicit vintage. PLUTO rows have version 26v2. The generic
dictionary fetched from NYC is 22v1; it is retained as a documented vintage mismatch,
not current zoning guidance.

Live collection uses collect.py and the source_*.json request definitions. It
requires network access. A successful cached source binding is reused by default;
`--refresh` explicitly replaces it and archives the previous body and source record.
A collection-attempt ledger records new requests. Commit reviewed snapshots before
refreshing and repeat professional review if their supporting evidence changes. Run bootstrap and discovery, then universe, then challenge and
environment source definitions in their documented order. Queries are generated
from a fixed window and BBLs for this probe. For a new station, regenerate the
window and candidate query definitions as well as changing the DSL; changing the
station alone cannot create a new source universe. Mismatched scope is rejected
by validation. Failed requests are recorded and cannot support observed claims.

```sh
python collect.py source_bootstrap.json
python collect.py source_discovery.json
python collect.py source_universe.json
python collect.py source_challenge.json
python collect.py source_rules.json
python collect.py source_environment.json
python collect.py source_environment_detail.json
```

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
snapshots retain their publishers' terms; see [DATA-LICENSES.md](DATA-LICENSES.md).
The project license does not relicense those sources. Snapshot dates and source
URLs are part of the research record; later retrieval does not certify historical
byte equivalence.

## Contribute and continue

See [CONTRIBUTING.md](CONTRIBUTING.md) for reproducing a result, challenging an
interpretation, and proposing a change. The next priorities are integrating the
review corrections into a versioned IR, testing a withheld real project, and
measuring usefulness with housing practitioners. Preserve failed experiments and
their assumptions so improvements can be assessed.

## Deterministic backpressure and papercuts

Run `make check` for syntax, artifact lint, ten behavioral tests, JSON Schema
validation and hash checks. Schema checks require requirements-dev.txt. Run
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

The [425 Grand Concourse calibration](research/grand-concourse-calibration/report.md) compares 2015 solicitation conditions with later public project evidence. It preserves 42 quoted facts, unresolved definitions, a missed specific zoning mechanism and seven interpretation checks. This is an openly known case, not a blind prediction benchmark. Run its offline validator and tests using the instructions in that folder.
