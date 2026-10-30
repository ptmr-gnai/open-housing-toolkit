# Independent live-lot trial record

A fresh worker received an isolated copy of the revised local repository and the
[practitioner brief](../../examples/live-lot-trial/brief.md). It received no project
history or recommended commands. The parent did not coach its first pass. The copy
excluded .git, so missing Git metadata in the report is a fixture limitation.

The report below is the unedited first-pass report. It exposed two defects that
were then fixed: wrong copied skill-reference content and demo-specific RER text.
The [published worked package](../../examples/live-lot-trial/README.md) preserves
its actual live evidence/area runs and rebuilds comparison/RER into fresh packages
with those corrections. First-pass temporary output paths refer to the original
worker workspace, not the corrected published output. No source photo, surveyed
geometry or provider-generated image was part of that first pass.

---

# Live practitioner trial: 1940 Jerome Avenue

Preparer: independent usability trial. Preparation date: 2026-10-30.
Repository: `/tmp/housing-live-lot-worker-29mp6f52`.
All new files are under `runs/live-jerome-trial/`, except this report and a temporary read-only guidance inspection export. No toolkit source code, existing examples or completed run artifacts were edited. No publication, submission or contact occurred. The requested task was executed against live public APIs, not the demo.

## Completed outputs

Root: `/tmp/housing-live-lot-worker-29mp6f52/runs/live-jerome-trial/`

- `evidence/packet.html` and `packet.md`: live parcel packet; `ir.json`, `receipts.json`, raw `sources/`, `execution.json`, `image-prompts.json`, calculation CSV and manifest.
- `area/packet.html`: independently editable typed area recipe, calculation CSV, trace and retained evidence.
- `comparison/packet.html`: requested 12/18-home hypothetical rental comparison; original upstream analysis and historical reference excerpt/receipt retained.
- `rer/packet.html`: index to `report-program_a.html` / `.md`, `report-program_b.html` / `.md`, `coverage.html` / `.md`, and typed `rer.json`. Incomplete drafts only.
- `review-visual.html`: separate local arithmetic/evidence visualization, created by `create-review-visual.py`. It is a supplementary report, not a toolkit-verified image or site design.
- `inputs/`: actual request JSONs and area recipe; `logs/01-live-run.log` through `08-rer-verify.log`: build/verification results.

## What the results mean

All four module builds and explicit verification commands passed. This establishes their implemented engineering checks, source bindings and deterministic arithmetic. It does not establish professional correctness, complete coverage or feasibility. A concrete stale-text defect below passed verification.

Live collection receipts show retrieval on 2026-10-30 around 02:23:05 UTC. All four adapters returned HTTP 200, valid exact-BBL results, with no recorded truncation:

| Source | Rows | Meaning |
| --- | ---: | --- |
| PLUTO | 1 | 26v2 tax-lot record |
| DOB BIS | 2 | Legacy filing/document rows, not two projects |
| DOB NOW | 38 | Filing rows, not 38 projects or completed buildings |
| HPD violations | 0 | Empty bounded exact-BBL query; not evidence of no violations, no housing or safety |

PLUTO records address **1940 JEROME AVENUE**, BBL **2028530012**, **115 residential units**, **117 total units**, **97,704 building sf**, **10,852 lot sf**, **13 floors**, building class **D7**, zoning descriptor **C4-4D**, special district **J**, environmental designation **E-442**. DOB NOW includes positive 115-unit signals. These recorded attributes materially challenge any vacant-lot premise, but do not establish actual/lawful occupancy, current tenancy, availability, title, site control, redevelopment rights or a reconciled filing history. Retrieval date is not a field-observation date.

The supplied hypothetical area budget yields `(15,000 − 1,500) × 0.8 = 10,800 residential net sf`, then `10,800 / 800 = 13.5 home-equivalents`. Residential gross allocation is 13,500 sf. The gross-to-recorded-lot quotient is approximately 1.3822 and is explicitly not zoning FAR. These test assumptions are not measured capacity, a permitted home count, surveyed design or reconciled evidence for either offer.

All offers are two-bedroom homes. Gross housing costs including supplied tenant utilities are $1,100 and $1,900 monthly. At the supplied 30% threshold, hypothetical annual incomes $48,600 and $97,200 give monthly budgets $1,215 and $2,430.

| Diagnostic | A | B |
| --- | ---: | ---: |
| Total hypothetical offers | 12 | 18 |
| $1,000 rent + $100 utilities | 8 | 4 |
| $1,800 rent + $100 utilities | 4 | 14 |
| Match $48,600 income profile's cost and exact-bedroom tests | 8 | 4 |
| Match $97,200 income profile's cost and exact-bedroom tests | 12 | 18 |

The profile populations overlap; their match counts must not be added. B has six more offers overall and four fewer lower-income diagnostic matches. A proposes 60 years for the eight lower-rent offers and 30 for the four higher-rent offers; B proposes 30 for all eighteen. Durations do not establish secured restrictions, fixed future rents or household-years served. No winner, eligibility finding, benefit causal estimate, net addition or commitment follows.

The comparison uses the existing coherent historical 2025 reference pack. Its receipt identifies the RER guide Table 3, printed page 6, internal July 1, 2025 stamp, extracted source PDF SHA256 `d3cb09347c351a0a52993758018b1b79296adc29ff934e28053f5cd6a949faf1`. The PDF is not bundled, and I did not independently retrieve/re-extract it. Verification checks retained excerpts/receipts, not original PDF authenticity or current applicability. This fits the requested historical 2025 diagnostic; the RER drafts explicitly flag its difference from preparation year 2026.

Each RER draft has 50 mapped slots: 3 filled metadata/caveats, 3 illustrative, 15 missing and 29 needing interpretation. These are diagnostic states, not a completeness percentage. Both fix official submission readiness to false, applicability to not determined, and professional review to pending.

## Failures, missing inputs and observed usability issues

1. **Actual output defect:** RER area-slot reason text says “not reconciled to this 24/36-home program” in `rer/coverage.md`, both per-program reports, corresponding HTML and typed slots. The actual supplied programs are **12 and 18**, correctly reflected in offer tables. The stale demo-specific explanation passed verification. I preserved those immutable artifacts and did not patch code or manifests. The visual and this report explicitly disclose it. Correct/rebuild before professional use.
2. Comparison and RER execution references contain copied geometry headings/procedures. Their canonical module READMEs and final build examples provide usable commands, so this did not block execution.
3. Input examples include generic cautions about “recorded zero homes”; some template limitations retain similar wording. Those are conditional generic cautions, not this parcel's recorded state. The actual record is 115 residential units. Read the live evidence summary alongside the later packets.
4. No current-use/leases, lawful occupancy reconciliation, title/site-control evidence, owner willingness, zoning interpretation, approvals, environmental studies, survey, layout, financing or program eligibility documentation was supplied or established. The modules retain these unknowns.
5. Official preparation lacks applicant/contact, qualifying land-use action and applicability determination, application consistency/stage, residential/nonresidential **ZSF**, program rules/AMI bands, official rents and income eligibility ranges, tenancy/sector/workforce/jobs, construction duration/person-years/workers, validated community geography, EDDE summary/full profiles/displacement context, and attributed applicant narrative. No gross-to-ZSF or cost-test-to-AMI conversion was invented.
6. The pinned form (2023) and guide (2025) differ on nonresidential reporting without identified tenants. Both are preserved; no legal interpretation was selected. Criteria has an unresolved printed-date placeholder. Source PDFs are external and were not freshly re-extracted here.
7. No site photo, surveyed footprint, floor/height assumptions or explicit massing scenario was supplied. No photo concept, surveyed massing, image generation, or photo substitution was attempted. The toolkit's verified diagram-only prompt was delivered. A separate HTML arithmetic diagram satisfies a visual communication role without depicting geometry; it was checked against supplied inputs and packet results, but no browser screenshot/layout inspection was performed.
8. `git status --short` failed because the supplied repository copy has no `.git` metadata. This prevented a git diff, not task execution. Python is 3.12.14. No dependency installation was needed.

## Exact task execution commands

Run from `/tmp/housing-live-lot-worker-29mp6f52`. The four JSON inputs were serialized with Python from documented example formats, replacing the parcel, counts, rationales, preparer/date and area values with the brief's supplied values; actual complete inputs remain in `inputs/`. No `demo` command was used.

```sh
python --version
python -m housing_workflow run --input runs/live-jerome-trial/inputs/parcel-request.json --out runs/live-jerome-trial/evidence > runs/live-jerome-trial/logs/01-live-run.log 2>&1
python -m housing_workflow verify --run runs/live-jerome-trial/evidence > runs/live-jerome-trial/logs/02-evidence-verify.log 2>&1
python -m housing_recipe build --from-run runs/live-jerome-trial/evidence --recipe runs/live-jerome-trial/inputs/area-recipe.json --out runs/live-jerome-trial/area > runs/live-jerome-trial/logs/03-area-build.log 2>&1
python -m housing_recipe verify --run runs/live-jerome-trial/area > runs/live-jerome-trial/logs/04-area-verify.log 2>&1
python -m housing_benefit build --analysis runs/live-jerome-trial/area --references examples/affordability-inputs/reference-source --input runs/live-jerome-trial/inputs/comparison-request.json --out runs/live-jerome-trial/comparison > runs/live-jerome-trial/logs/05-comparison-build.log 2>&1
python -m housing_benefit verify --run runs/live-jerome-trial/comparison > runs/live-jerome-trial/logs/06-comparison-verify.log 2>&1
python -m housing_rer build --comparison runs/live-jerome-trial/comparison --input runs/live-jerome-trial/inputs/rer-request.json --out runs/live-jerome-trial/rer > runs/live-jerome-trial/logs/07-rer-build.log 2>&1
python -m housing_rer verify --run runs/live-jerome-trial/rer > runs/live-jerome-trial/logs/08-rer-verify.log 2>&1
python runs/live-jerome-trial/create-review-visual.py
```

Every module command returned passed; explicit logs show the scoped states. The visualization script is itself retained for exact reproduction. All resulting materials are local review preparation only.
