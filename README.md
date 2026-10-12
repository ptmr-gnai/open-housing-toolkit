# Open Housing Toolkit

The Open Housing Opportunity Playbook research project.

An open source research project for investigating affordable housing opportunities:
find a site lead, challenge it, explore conditional scenarios, and assemble an
evidence pack that another person can reproduce and question. Facts, calculations,
assumptions, judgments and unknowns should stay distinguishable throughout the
pipeline. Agents can work with the files and executable checks.

**Status: early research prototype, open for feedback.** It is ready to share and
improve in public. It does not establish that a lot is available, a design fits,
a project is financed, or a proposal is ready to submit. Human housing expert
acceptance and practitioner usefulness remain untested. The components below are
separate experiments; they are not yet one integrated product.

## Start here

- [Project proposal](docs/proposal.md): the intended user, probe and open source approach.
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
