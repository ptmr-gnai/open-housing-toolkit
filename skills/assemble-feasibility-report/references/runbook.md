# assemble-feasibility-report: execution reference

Working directory: repository root. Use `.venv/bin/python` after preflight.

## Canonical resources

- [Module guide](../../../src/housing_feasibility/README.md): sections, inputs and checks.
- [Request schema](../../../src/housing_feasibility/request.schema.json) and
  [brief schema](../../../src/housing_feasibility/brief.schema.json).
- [Implementation](../../../src/housing_feasibility/report.py): every section and formula.

## Run

```sh
.venv/bin/python -m housing_feasibility template --out runs/NAME/report-request.json
# edit: title, base_case (an underwriting request id), prepared_on, prepared_by
.venv/bin/python -m housing_feasibility build --request runs/NAME/report-request.json --brief runs/NAME/brief.json \
  --evidence runs/NAME/evidence \
  --underwriting runs/NAME/underwriting \
  --massing runs/NAME/massing-6 \
  --ownership runs/NAME/ownership \
  --render runs/NAME/render \
  --discovery runs/AREA/discovery \
  --out runs/NAME/report
.venv/bin/python -m housing_feasibility verify --run runs/NAME/report
```

`--underwriting` takes a package or a folder of packages (repeatable); every one
appears in the sensitivity table and the base case drives the budget and pro forma. Repeat `--massing` for
each height option. Every package must be for the same tax lot; the build stops
otherwise. The output folder must be new.

The whole chain that produces these inputs: [full lot analysis](../../start-here/references/lot-analysis.md).

## Outputs

- `report.html`: the memo. Open it for the user (`open runs/NAME/report/report.html`).
- `report.md`: the same content as text.
- `report.json`: typed sections (`brief`, `process`, `headline`, `site`, `search`, `ownership`,
  `zoning`, `massing`, `development_budget`, `operating_pro_forma`, `debt_sizing`,
  `sensitivity`, `program_reconciliation`, `render`, `open_items`, `sources`, `inputs`).
- `inputs/`: verified copies of every package used; `manifest.json` binds all bytes.

## Checks to read before handing off

- `program_reconciliation`: each scenario's gross area should match a massing.
- `zoning.massing_comparison`: residential area against recorded FAR.
- `render.story_status`: the render's story count should match a massing.
Report any mismatch to the user instead of hiding it.
