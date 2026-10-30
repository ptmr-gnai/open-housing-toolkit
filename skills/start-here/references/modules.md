# Module and handoff map

All commands run from the checkout root. Use a fresh output directory. Follow the
linked skill for input collection, execution and verification.

| Need | Skill | Contracts / implementation / references |
| --- | --- | --- |
| Investigate a Bronx lot | [housing-investigation](../../housing-investigation/SKILL.md) | [workflow guide](../../../src/housing_workflow/README.md), [request schema](../../../src/housing_workflow/request.schema.json), [workflow](../../../config/workflows/parcel-investigation.json) |
| Edit area arithmetic | [run-analysis-recipe](../../run-analysis-recipe/SKILL.md) | [recipe guide](../../../src/housing_recipe/README.md), [base recipe](../../../config/recipes/area-budget.json) |
| Compare explicit housing offers | [compare-housing-programs](../../compare-housing-programs/SKILL.md) | [guide](../../../src/housing_benefit/README.md), [request schema](../../../src/housing_benefit/request.schema.json), [example inputs and reference pack](../../../examples/affordability-inputs/README.md) |
| Prepare RER drafts | [prepare-rer-draft](../../prepare-rer-draft/SKILL.md) | [guide](../../../src/housing_rer/README.md), [request schema](../../../src/housing_rer/request.schema.json), [pinned sources](../../../src/housing_rer/guidance.json), [instruction map](../../../src/housing_rer/requirements.json), [source-preparation script](../../../scripts/prepare_rer_guidance.py) |
| Build assumed geometry | [build-grounded-massing](../../build-grounded-massing/SKILL.md) | [guide](../../../src/housing_geometry/README.md), [spec](../../../docs/reference/specs/geometry-grounding.md) |
| Bring a photo and visual assumptions | [prepare-render-brief](../../prepare-render-brief/SKILL.md), then [render-site-concept](../../render-site-concept/SKILL.md) | [render guide](../../../src/housing_render/README.md), [examples](../../../examples/site-concept/README.md) |

For the supported Codex image-tool and Claude Code export paths, follow
[runtime routing and preflight](agent-runtimes.md) before the visual leaf skills.

## What actually connects

The walkthrough passes the newly verified parcel output to the recipe; the new
recipe output to the comparison as site context; and the new comparison to RER
preparation. Each downstream package retains its upstream inputs and hashes.
The comparison imports illustrative program inputs independently. It does not
calculate 24 or 36 homes from the area recipe. The RER adapter does not transform
that gross-area budget into ZSF or infer an AMI mix from cost-test results.

The geometry and photo-render modules remain independent branches. The retained
[geometry-reference image experiment](../../../examples/geometry-render/README.md)
and [street placement](../../../examples/street-placement/README.md) show actual
provider invocations, with unverified camera/metric fidelity. There is no general
mesh-to-photo registration adapter. Automatic Street View retrieval and arbitrary
agency-analysis ingestion are not implemented.

Skills keep operational instructions small and link to canonical code, schemas,
source catalogues and preparation scripts instead of copying them into each skill.
This requires the repository checkout; these directories are not independently
portable skill bundles. A distributable installer is future work.
