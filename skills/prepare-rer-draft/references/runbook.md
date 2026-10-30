# prepare-rer-draft: execution reference

Working directory: repository root. Read this reference when performing this task.
Use fresh output directories and the user's actual paths and canonical inputs.

## Canonical resources

- [Module guide](../../../housing_rer/README.md).
- [CLI implementation](../../../housing_rer/__main__.py).
- [Request contract](../../../housing_rer/request.schema.json).
- [Pinned guidance](../../../housing_rer/guidance.json), [instruction map](../../../housing_rer/requirements.json) and [source-preparation script](../../../scripts/prepare_rer_guidance.py). Source preparation is separate from ordinary offline runtime.

## Detailed procedure and limits

Use for a practitioner reviewing how a housing-program comparison maps to NYC's
pinned RER guide and form. Read housing_rer/README.md and docs/tenets.md first.

```sh
python -m housing_rer demo --out runs/rer-draft
python -m housing_rer verify --run runs/rer-draft
```

Read packet.md, the two separate program drafts, and coverage.md. Keep official
form fields distinct from the supplemental cost diagnostic. Never infer AMI mix
from which hypothetical household can afford an offer. Never relabel gross area as
ZSF or use an unrelated prior area scenario to invent jobs.

Application classification, EDDE geography/profile, program eligibility and the
applicant narrative remain unresolved. Missing values stay null, not template zeroes.
The guide/form nonresidential instruction divergence must remain visible. A declared
none-identified tenant assumption can suppress job reporting; it is not a finding
of no jobs or no businesses. Six narrative-goal prompts are not six legal pass/fail tests.

Use build with a complete verified housing_benefit run and the typed draft request.
Create a new run for revisions. Cite source versions and exact review scope; technical
verification is not a finding of compliance, submission readiness or professional
endorsement. This module does not fill or submit the official City PDF.

## Build from the actual upstream package

```sh
python -m housing_rer build --comparison runs/my-comparison --input examples/rer-inputs/request.json --out runs/my-rer
python -m housing_rer verify --run runs/my-rer
```

For user work supply the actual preparation metadata instead of the example date.
EDDE exports, program certification and applicant narrative remain unsupported
inputs requiring reviewed adapters or separate practitioner work.
