# Same lot, three explicit analysis recipes

All three packets retain the real public-source snapshot for Bronx lot
**2028710002**, recorded address **1240 Edward L Grant HWY**. No fresh collection,
professional acceptance, measured geometry or new image generation occurred.

| Run | Numerical method | Home-equivalents |
| --- | --- | --- |
| [Base packet](base/packet.md) | (40,000 − 6,000) gross sf × 0.8 ÷ 800 net sf/home | 34 |
| [Inserted reserve step](with-reserve/packet.md) | (40,000 − 6,000 − 4,000) gross sf × 0.8 ÷ 800 net sf/home | 30 |
| [Replacement gross method](gross-method/packet.md) | (40,000 − 6,000) gross sf ÷ 1,000 gross sf/home | 34 |

These are deliberately chosen arithmetic sensitivities. No result establishes a
permitted or physically feasible home count. All professional gates remain unknown.

Each directory has its own `recipe.json`, `trace.json`, `ir.json`, calculation CSV,
packet, diagram brief, full original `evidence-run/` and implementation/hash manifest.
The source packet's original area budget remains preserved inside `evidence-run/`;
use the top-level packet for the recipe's result.

```sh
python -m housing_recipe verify --run examples/analysis-recipe/base
python -m housing_recipe impact --run examples/analysis-recipe/base --recipe recipes/area-budget-with-reserve.json
python -m housing_recipe impact --run examples/analysis-recipe/base --recipe recipes/area-budget-gross-method.json
```

See the [recipe guide](../../housing_recipe/README.md). This is a numerical
extension test, not a practitioner comparison harness or a project backtest.
