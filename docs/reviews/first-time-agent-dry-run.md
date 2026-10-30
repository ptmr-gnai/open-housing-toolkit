# Open Housing Toolkit: first-time AI usability dry run

Date: 2026-10-30. This is an AI usability review, not a housing-method, legal, professional or human-practitioner validation. No source-checkout edits, network requests, secrets, optional dependencies or image generation were used. HTML was inspected as source/link structure, not rendered in a browser.

## Setup and exact commands

Source: `/workspace/bronx-housing-probe`; isolated copy: `/tmp/oht-first-time-323for7s`.
The copy included current tracked and nonignored untracked files, using:

```python
src = pathlib.Path('/workspace/bronx-housing-probe')
dst = pathlib.Path(tempfile.mkdtemp(prefix='oht-first-time-'))
paths = subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'], cwd=src).decode().split('\0')
for p in paths:
    if not p or set(pathlib.PurePosixPath(p).parts) & {'.git','runs','__pycache__'}:
        continue
    s, d = src / p, dst / p
    if s.is_file():
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(s, d)
```

Started with README.md and AGENTS.md, then read start-here, tenets, first-run walkthrough, the four leaf skills, module map, four module READMEs and parcel workflow. Commands below ran from the isolated copy root:

```sh
python --version
python scripts/first_run.py --out runs/first-time-dry-run
python scripts/check_onboarding.py
python scripts/first_run.py --out runs/first-time-dry-run
python -m venv --without-pip /tmp/oht-first-time-venv-323for7s
/tmp/oht-first-time-venv-323for7s/bin/python scripts/first_run.py --out runs/first-time-stdlib-venv
```

Interpreter: Python 3.12.14; initial executable `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python`. The clean venv also used Python 3.12.14 and had no pip or third-party installs. Python 3.11 was not independently exercised in this dry run. Needed: writable checkout, standard-library Python, and git only for copying this checkout. No Node, browser, Poppler or geometry libraries needed for the executed path. Optional source re-extraction would need matching external PDFs and Poppler; it was not performed.

`steps.json` records these exact eight internal commands, with `O=/tmp/oht-first-time-323for7s/runs/first-time-dry-run`, `R=/tmp/oht-first-time-323for7s`, and the interpreter above:

```sh
python -m housing_workflow demo --out "$O/parcel"
python -m housing_workflow verify --run "$O/parcel"
python -m housing_recipe build --from-run "$O/parcel" --recipe "$R/recipes/area-budget.json" --out "$O/recipe"
python -m housing_recipe verify --run "$O/recipe"
python -m housing_benefit build --analysis "$O/recipe" --references "$R/examples/affordability-inputs/reference-source" --input "$R/examples/affordability-inputs/request.json" --out "$O/comparison"
python -m housing_benefit verify --run "$O/comparison"
python -m housing_rer build --comparison "$O/comparison" --input "$R/examples/rer-inputs/request.json" --out "$O/rer"
python -m housing_rer verify --run "$O/rer"
```

## Results by task

| Task | Result | Observed evidence |
| --- | --- | --- |
| Find entry route using README/AGENTS | PASS | Clear fresh-directory command and coordinator skill; independent branches distinguished. |
| Build and verify four modules offline | PASS | All eight commands exit 0; index, steps ledger and numbered logs generated. |
| Run without installed packages | PASS | Fresh `venv --without-pip` completes the same eight commands. |
| Inspect outputs and explain quantities | PASS | Read index, packet summaries, comparison claim trace, both full RER drafts, coverage and typed status inventory. |
| Protect an existing output | PASS | Rerun exits 2: `Blocked: Output already exists; choose a new directory`; SHA256 inventories before/after match for all 130 files. |
| Local skill/resource links | PASS | Onboarding checker reports 11 skills and core routes; independent generated-package scan finds no missing file target among 4,680 Markdown/HTML local links. External URLs, every fragment and browser layout not validated. |
| Complete an RER | FAIL / explicitly out of scope | Both drafts remain incomplete and `official_submission_ready=false`. This is truthful behavior, not a walkthrough defect. |
| Professional correctness/usefulness | NOT TESTED | Technical success cannot establish either. |

## What the actual outputs mean

The lot is BBL 2028710002, recorded address 1240 EDWARD L GRANT HWY. Cached receipts show 2026-10-28 retrievals; PLUTO row version 26v2. Returned rows are PLUTO 1, DOB BIS 27, DOB NOW 0, HPD violations 0; no truncation shown. Zero exact-BBL returns do not prove no activity/violations. Historical proposed 9 dwelling units conflict with a simplistic vacancy reading of PLUTO residential units 0; current occupancy remains unresolved.

**34** is `(40,000 gross sf − 6,000 nonresidential gross sf) × 0.8 / 800 net sf per home-equivalent`. All four inputs are hypothetical. It is an area quotient, not zoning capacity or a feasible unit count.

**24 and 36** are independently supplied rental programs, not derived from 34 or reconciled to geometry. A offers 16 lower-rent plus 8 higher-rent two-bedroom homes; B offers 8 plus 28. Lower-rent gross cost is $1,000 rent + $100 utilities = $1,100/month; higher-rent cost is $1,900. A hypothetical four-person household uses the historical 2025 rounded 30%-AMI reference income $48,600: $48,600 × 30% / 12 = $1,215 budget. Both bins match exact two bedrooms; only $1,100 passes cost. Therefore **16 versus 8** homes meet this diagnostic. The income trace points to retained passage `30% AMI $34,000 $48,600 $850 $1,090`, Table 3 printed p.6, source PDF SHA256 `d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1`. Offline replay verifies the excerpt, not the external PDF. None establishes eligibility, availability, delivery, achieved benefit or a winner. Restriction years are proposed assumptions (A lower bin 60; other bins 30), not secured commitments.

Each RER draft has 50 mapped slots: 3 filled, 3 illustrative, 15 missing and 29 needing interpretation. These are diagnostic categories, not a completeness percentage. Missing examples include applicant contact, community geography, EDDE summary, displacement context, construction duration/person-years and full local/borough/city profiles. Interpretation remains needed for applicability, ZSF, AMI mix/program rules, income eligibility, narrative and the 2023 form/2025 guide nonresidential reporting divergence. The cost diagnostic stays supplemental. PDFs are not bundled and semantic coverage is manually curated/unreviewed.

## Handoffs and continuation

Parcel → recipe preserves sourced identity/evidence but adds assumed area arithmetic. Recipe → comparison passes site context, not a capacity constraint. Comparison → RER passes illustrative offers; it does not manufacture ZSF, official AMI categories, jobs, EDDE data or applicant interpretation. Geometry and images did not run.

A practitioner can now choose a specific Bronx lot and decision question, supply BBL/address, and use the investigation skill; evidence-only output is supported without a scenario. Confirm occupancy, title, zoning, fit, environment and finance with appropriate people/evidence. For modeling, copy the recipe/request, explain changed assumptions, preview impact and rebuild into a new directory. For program comparison supply explicit mixes/rents/utilities/durations/profiles in its contract. For RER, first establish applicable action/scope and obtain program definitions, community evidence and applicant interpretation; unsupported imports need adapters or separate professional work. The toolkit cannot currently complete those gaps by filling blanks or submit the official form.

## Friction and misleading wording

1. **Observed misleading packet sentence:** generated parcel packet says “Queried four NYC public datasets” under “What this run did,” even though this run only replayed retained responses. README/index are accurate, but a detached packet can imply fresh collection. Label replay origin in the packet itself.
2. **Observed reading overload:** parcel/recipe Markdown contain 2,212/2,218 lines; comparison contains 944. Reading them wholesale produced truncated tool output. Summaries help, but explicit targeted claim/source inspection instructions would help new agents.
3. **Observed stale-looking draft metadata:** first-run RER says prepared 2026-10-29 although run date was Oct30, because it retains supplied example `prepared_on`. Explain fixed demonstration metadata alongside source/price years so users do not mistake it for execution time.
4. **Missing continuation detail:** first-run asks users to find EDDE material without expanding EDDE or giving direct human acquisition/validation instructions in the immediate entry guides. It correctly states ingestion is unsupported. Add a short glossary and concrete manual next-step guidance.
5. **Minor presentation friction:** comparison repeats the identical “Program delivery and realization” unknown twice without visible program labels. Attribute each to A/B or combine.

No broken local file link or blocking instruction failure was observed on the exercised path. The absence of broken links, successful verifiers and clear disclaimers does not demonstrate skill quality, semantic completeness, professional acceptance or human usability. No live, optional, failure-mid-stage, browser or submission branch was tested.

## Parent remediation after this snapshot

The parent agent reports adding explanations to `docs/first-run.md`, the coordinator skill and generated index for retained queries, fixed example preparation date, targeted claim reading, and EDDE expansion/manual acquisition guidance with no export adapter. These address onboarding gaps 1–4 at entry points; this isolated dry run exercised the earlier copied snapshot, so those edits were not re-executed here. Existing leaf packets were preserved: packet-local “Queried” wording, long registers and duplicate delivery wording remain observable limitations. Reassess the updated entry text separately; do not infer its quality from the earlier successful execution.
