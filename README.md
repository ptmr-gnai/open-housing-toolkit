# Open Housing Opportunity Playbook

Probe one: 170 Street on the 4 line, Bronx. A local open source prototype for
finding a site lead, challenging it, simulating conditional concepts, and preparing
material for two independent expert reviewers.

Start with outputs/advisor-brief.md, then open outputs/advisor-explorer.html in a
browser. The complete report is outputs/probe-report.md. The proposal is
docs/proposal.md. Both expert reviews remain outstanding.

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

MIT licensed code; original documentation CC BY 4.0. Upstream terms and attribution
remain separate; see DATA-LICENSES.md. A local Git repository records this work;
there is no public remote repository yet.

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
