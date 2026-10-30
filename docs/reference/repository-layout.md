# Repository map

| Location | Purpose |
| --- | --- |
| src/housing_workflow/ | Known-lot evidence collection and packets |
| src/housing_recipe/ | Editable typed area arithmetic |
| src/housing_benefit/ | Explicit housing-offer comparisons |
| src/housing_rer/ | Incomplete RER preparation and instruction coverage |
| src/housing_geometry/ | Assumed, source-bound schematic massing |
| src/housing_render/ | Render briefs, image attachment and review |
| src/housing_common/ | Local-output safeguards, historical verification and path mapping |
| skills/<name>/ | Skill entry, on-demand references and canonical script links |
| config/workflows/ and config/recipes/ | Versioned composition and model configuration |
| docs/guides/, docs/reference/, docs/templates/ | Setup/use, supporting detail and handoff templates |
| examples/ | Curated read-only worked packages |
| research/ | Bounded research experiments and their evidence |
| research/legacy-probe/ | Original station-screening probe, its scripts, cache and reports |
| archive/ | Exact original source used for historical verification; not user entry points |
| scripts/ and tests/ | Contributor checks and organized module/integration tests |
| runs/ | Ignored local inputs, artifacts and diagnostics |

Use [setup](../guides/setup.md) once, then the existing `python -m housing_…`
commands. The src layout requires an editable checkout; there is no top-level
package shim or automatic user-data regeneration. Dependency extras live in
pyproject.toml. The existing make targets remain the contributor interface.

Legacy direct commands now use paths such as
`python research/legacy-probe/pipeline.py`. Their inputs are relative to that legacy
probe directory. Fresh output destinations still follow the shared local-only
policy and default to ignored runs/ at the checkout root.

Old snapshot records can name logical paths such as cache/ or pipeline.py. Those
recorded strings and hashes are preserved. Read-only compatibility checks map to
the moved data or use the exact archived code in isolated local scratch. They never
rewrite a snapshot to make the new layout look like the original execution.

Existing local runs are not migrated or committed as source. Old ignored artifacts
that occupied former legacy locations are preserved under runs/organization-local-preserved/.
New analyses, images and reviews remain local; this reorganization does not authorize
commits, uploads or publication of them.
