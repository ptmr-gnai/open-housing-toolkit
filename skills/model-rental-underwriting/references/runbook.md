# model-rental-underwriting: execution reference

Read the [module guide](../../../src/housing_underwriting/README.md) and
[request schema](../../../src/housing_underwriting/request.schema.json).
The [sample request](../../../config/underwriting/rental-60-base.json) is an analyst
experiment, not a Bronx cost/rent estimate. All numerical input bases are explicit.

```sh
python -m housing_underwriting build --input config/underwriting/rental-60-base.json --out runs/rental-model
python -m housing_underwriting verify --run runs/rental-model
```

Repeat `--reference-source ID=/local/path` to retain declared source bytes.
Inspect packet.html/packet.md, annual.csv, results.json, trace.json and
references.json. The verifier recomputes arithmetic and projections; it does not
fetch newer sources or authenticate financing commitments. To change an input,
copy the request and rebuild into another new directory.

Use the [site-search skill](../../goal-seek-housing-sites/SKILL.md) for a bounded
search over a verified broad nonhousing inventory. Discovery is independently
useful and requires no financial scenario. For known-lot area/geometry work use
[analysis recipes](../../run-analysis-recipe/SKILL.md) and the
[geometry skill](../../build-grounded-massing/SKILL.md); no automatic physical-fit
or legal-envelope claim follows from this financial model.
