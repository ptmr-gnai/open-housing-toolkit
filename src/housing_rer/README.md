# Guide-mapped RER preparation drafts

Use an editable checkout; see [setup](../../docs/guides/setup.md).

This module takes the verified housing-cost comparison and prepares **two separate
five-section drafts**, one per illustrative program, plus a source-to-implementation
map. It is the next bounded step under the [community-benefit proposal](../../docs/reference/specs/community-benefit.md)
and [project tenets](../../docs/reference/tenets.md).

It does not certify an RER, populate or submit the official fillable PDF, determine
legal applicability, or claim professional completeness. Missing data is a result
to act on, not a reason to invent content.

## Try it

Python 3.11+, standard library, offline:

```sh
python -m housing_rer demo --out runs/rer-draft
python -m housing_rer verify --run runs/rer-draft
```

Open `packet.html`, then the per-program draft and coverage links. GitHub entry:
[worked preparation packet](../../examples/rer-preparation/packet.md).
For an agent use [the skill](../../skills/prepare-rer-draft/SKILL.md).

Explicit build:

```sh
python -m housing_rer build --comparison examples/affordability-comparison --input examples/rer-inputs/request.json --out runs/my-rer-draft
```

`replay --from-run ... --out ...` preserves the comparison and draft inputs; an
optional `--input` changes supported preparation metadata. All outputs require a
new directory. Changing the upstream housing program requires its own verified
housing_benefit rebuild, then a new RER preparation run.

## What comes from the sources

The [pinned catalogue](guidance.json) records three official DCP resources:

- RER guide, internal July 1, 2025 stamp.
- RER form, June 9, 2023 stamp.
- Applicability criteria, with unresolved printed-date placeholders.

The [50-slot inventory](requirements.json) maps the cover and five report sections,
including conditional items, application consistency/versioning, affordability,
nonresidential area/jobs, construction employment, EDDE material and narrative
prompts. Each entry has source document SHA, PDF page, page-text hash and section
locator. These are manually interpreted instruction slots, not 50 independent
legal requirements or an exhaustive semantic-coverage certification. Six narrative
goals are prompts, not six automatic compliance tests. Full guide/form/criteria
interpretation and current applicability remain open to professional review.

The guide and form disagree about the nonresidential section without identified
tenants: the form skips the section, while the guide still requests area information.
We preserve both sources, keep area placeholders and suppress speculative job data.
We do not silently choose a legal interpretation. A supplied none-identified
assumption can make job/workforce reporting conditionally not applicable; no value
of zero jobs or finding of no existing businesses follows.

Our immutable rerun policy is an engineering choice. It does not override the
pinned guide's discussion of post-certification report updates. Version stage and
applicability remain unresolved.

## What is actually populated

- Draft preparer/date and the guide's final-setting caveat are populated slots.
- Project labels, summaries and total homes remain illustrative.
- Supplied rent offers appear in a candidate-input table. They are not filled
  official AMI-based rent ranges.
- Hypothetical profile incomes remain in the supplemental cost diagnostic. They
  cannot become program eligibility ranges or an AMI allocation.
- Prior gross-area quantities are candidate evidence only. They are not ZSF and
  are not established for the new programs; no conversion or job estimate is made.
- Community geography, EDDE summary, displacement context, complete profiles,
  program rules and applicant narrative are absent or need interpretation.
- References from 2025 are flagged against the 2026 preparation year, rather than
  silently presented as current-year reporting values.

The existing cost test is clearly outside the five official sections in a
supplemental appendix. The original comparison is preserved in `comparison-run/`.
Copied comparison claims retain that base path for resolving their original source
references; new slot bindings use explicit paths and JSON pointers.

## Status and contracts

[Request schema](request.schema.json), [IR schema](ir.schema.json), frozen Slot
records and the Status enum expose the supported interfaces. `filled` means a
slot contains content, not that the content or the overall report is compliant.
`illustrative`, `missing`, `needs_interpretation` and conditional `not_applicable`
remain separate. Unresolved slots retain null values. Status counts are diagnostic
counts, not an overall completeness percentage or a community-benefit score.

Every output fixes submission readiness to false and professional review/applicability
to pending/not determined. Input does not offer a switch to clear them. Current
adapters do not ingest EDDE exports, certify program rules or write an applicant's
fair-housing conclusions. Those are specific next integration/review tasks.

Runtime checks cover the independent minimum inventory, duplicate/missing slots,
source/page bindings, categorical distinctions, exact input pointers, upstream
verification, inventories and deterministic recomputation. They detect known omissions;
they cannot discover every missing requirement or validate professional interpretation.
No authoritative form default zero is imported as data.

## Source reproducibility boundary

Actual PDFs were retrieved and inspected during preparation. External PDFs are not
bundled. Ordinary offline replay verifies the pinned source metadata/page bindings,
not fresh extraction or the truth of the interpretation. To independently regenerate
the catalogue, retrieve matching PDFs plus retrieval records and use Poppler:

```sh
python scripts/prepare_rer_guidance.py --pdf-dir PATH_TO_PDFS_AND_RETRIEVALS --out runs/reprepared-rer-guidance.json
```

The directory contains guide.pdf, form.pdf, criteria.pdf and retrievals.json with
IDs, URLs, actual byte hashes/counts, retrieval times and status. The script checks
bytes and stamps, records Poppler version and page-text hashes. A changed source
requires explicit remapping; altering only a citation hash cannot clear the old map.
Source citations do not imply agency endorsement or expert acceptance.
