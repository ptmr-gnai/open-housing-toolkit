---
name: model-parcel-scenario
description: Build typed evidence claims and optional area-budget calculations from a saved parcel collection.
---

# Model a parcel scenario

```sh
python -m housing_workflow build --run runs/my-investigation
```

The typed IR distinguishes facts, assumptions, calculations, unknowns and unreviewed judgments. All selected fields in successful returned records become facts with source IDs, JSON pointers and version hashes. Historical positive existing/proposed dwelling-unit signals remain visible beside PLUTO; the model does not reconcile lawful or current occupancy automatically.

Optional scenario inputs are declared assumptions with rationales. Named deterministic operations calculate residential gross allocation, net area and home-equivalents. The proposed gross-area/recorded-lot-area quotient is explicitly NOT zoning FAR. No calculation infers permitted capacity, floor plans, rent, affordability, construction cost or financed viability.

No scenario is a supported path: produce evidence and unknowns without invented values. Source failures and truncated coverage stay visible. The model's diligence checklist is authored, unreviewed policy, not proof of the best next task. Complete practitioner process coverage remains unknown.

To change a supplied input, create a new request and use `replay --from-run ... --input ... --out ...`; the same-parcel evidence is retained. Code or adapter changes stale old packet validation and require an explicit versioned rebuild. Notebook/workbook interactivity is deferred; `calculation-steps.csv` and the dependency graph already expose calculation inputs and operations.
