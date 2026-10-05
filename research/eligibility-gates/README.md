# Applicant and submission gate prototype

This adds a small typed requirements DSL and evaluator alongside the frozen earlier
probes. It does not rewrite the original analyst assessment, its tests or the root
housing IR. An integration adapter into a future unified IR remains work to do.

Requirements are curated from dated RFPs and addenda, not automatically discovered.
The compiler verifies byte provenance, exact-page quotations, numeric bindings,
closed JSON schema/operator types and vintage limits. Interpretation and coverage
remain review responsibilities. The second case is a source-driven cross-case
regression: the curator already saw later summaries, and no outcome labels are used.
It is not an independent held-out analyst assessment.

## Run

Python 3.11+ and `jsonschema` are required (the repository already lists it as a
validation dependency). From the repository root:

```
python research/eligibility-gates/build.py
python research/eligibility-gates/validate.py
python -m unittest discover -s research/eligibility-gates/tests -v
python research/eligibility-gates/check.py --case stanns --purpose evidence-pack
python research/eligibility-gates/check.py --case stanns --purpose submission-readiness-claim
```

The last command exits 2 when the claim is blocked; that is intended backpressure.
Optional `--profile path/to/profile.json` supplies credential/review evidence.
Credential paths are relative to the repository root; escape paths are rejected.
No actual applicant credentials or expert acceptance have been supplied.

`build.py` reads authored rules and labeled fixtures. It writes actual-unknown
snapshots and synthetic test outputs, never supplied profile files or reviews.
Replays require the same rules, code and sources; changed evidence or logic stales
previous accepted review bindings. Review attribution is attested metadata, not
cryptographically authenticated identity. An exact quote need not entail its claim.

## Semantics

- **pass:** accepted scoped evidence matches the declared criterion; no HPD approval
  or professional clearance implied.
- **unknown:** missing/unreviewed facts, incomplete history, or an unmet base rule
  with an unresolved agency review route.
- **fail:** an accepted complete evidence scope demonstrates the declared base rule
  is unmet and no source-backed alternative review route is modeled.

Missing records never imply failed eligibility. Development uses an individual
qualifying project; management uses a reviewed unique-unit portfolio for the period.
The seven-year window uses the historical submission deadline and inclusive calendar
years, an explicit convention needing confirmation at a material boundary.

The St Ann’s development addendum permits an experience justification; its later
management clarification refuses flexibility/current-at-submission substitution.
Base status and effective status are separate. The prototype never treats a
justification as automatic acceptance or eliminates this agency judgment.

Full proposal form/attachment and program/design requirements are not expanded yet.
Their coverage gate remains pending. All-pass synthetic cases still cannot generate
actual readiness claims. This prototype permits evidence gathering while blocking
premature claim promotion.

## Artifacts

- `cases/`: typed source-cited requirement declarations and assumptions.
- `sources.json`: seven original PDF/text hashes, dates and archive lineage.
- `sources/`: three retained St Ann’s PDFs and exact extracted text. First-case
  originals stay in `research/benchmark-case-search/inputs/`.
- `schemas/gates.schema.json`: closed declarative syntax; no code evaluation.
- `outputs/`: actual-unknown gate cards, labeled synthetic transfer checks, evidence
  requests and build manifest.
- `tests/`: behavioral and adversarial checks, separate from code-driven replay.

Original code is MIT; original prose follows the repository documentation license.
Agency PDFs retain upstream terms. Exact historical byte equivalence is uncertified;
the hosted source ZIPs were packaged after the historical deadlines.
