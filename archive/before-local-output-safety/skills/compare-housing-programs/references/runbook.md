# compare-housing-programs: execution reference

Working directory: repository root. Read this reference when performing this task.
Use fresh output directories and the user's actual paths and canonical inputs.

## Canonical resources

- [Module guide](../../../housing_benefit/README.md).
- [CLI implementation](../../../housing_benefit/__main__.py).
- [Request contract](../../../housing_benefit/request.schema.json).
- [Input/reference examples](../../../examples/affordability-inputs/README.md) and [reference preparation script](../../../scripts/prepare_benefit_reference.py).

## Detailed procedure and limits

Read housing_benefit/README.md and docs/tenets.md. The first slice is a conditional
housing-cost comparison, not a community-benefit forecast or eligibility assessment.

```sh
python -m housing_benefit demo --out runs/affordability-demo
python -m housing_benefit verify --run runs/affordability-demo
```

Collect explicit integer unit mixes, rents, tenant-paid utilities, restriction
durations and hypothetical household profiles. Never round home-equivalents into
units. Every program value needs its rationale. Reuse the input contract; arbitrary
spreadsheets, program rulebooks and legally secured commitments need later adapters.

Historical reference year must match the request price year. Do not mix current
income data with old rent tables. The demo uses selected 2025 guidance values and
is labeled historical. The source PDF is external, with hash, printed page and
selected passages; normal offline replay does not independently re-extract it.

Before an edit, preview `impact --run ... --input ...`. Rebuild with `replay
--from-run ... --input ... --out ...` into a new directory. Inspect separate total
homes, profile cost tests and restriction durations, with delivery, occupancy and
future no-action baseline unresolved. A missing input stays unknown. Read all
limitations before turning results into proposal prose or outreach assets.

Keep practitioner judgments attributable. The module does not choose a winner,
infer community priorities or clear professional review. Transit and image
modules are not called by this workflow.

## Build with supplied canonical inputs

```sh
python -m housing_benefit build --analysis runs/recipe-base --references examples/affordability-inputs/reference-source --input examples/affordability-inputs/request.json --out runs/my-comparison
python -m housing_benefit verify --run runs/my-comparison
```

For real work supply the user's canonical request, keeping rents, utilities,
restriction durations and household profiles attributed as assumptions. The
historical reference year is not a current-year applicability finding.
