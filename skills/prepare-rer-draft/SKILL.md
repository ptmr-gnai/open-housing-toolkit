---
name: prepare-rer-draft
description: Prepare five-section RER drafts with an explicit source-to-implementation map, preserving missing and non-equivalent data.
---

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
