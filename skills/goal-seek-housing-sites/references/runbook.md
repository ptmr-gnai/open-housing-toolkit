# goal-seek-housing-sites: execution reference

Read the [search guide](../../../src/housing_site_search/README.md), the
[declared target request](../../../config/site-search/transit-rental-targets.json),
and the [rental-model guide](../../../src/housing_underwriting/README.md).

```sh
python -m housing_site_search build --discovery runs/my-broad-discovery --underwriting runs/my-rental-model --input config/site-search/transit-rental-targets.json --out runs/my-site-search
python -m housing_site_search verify --run runs/my-site-search
python -m housing_site_search handoff --run runs/my-site-search --bbl 2028310056 --out runs/my-search-handoff
python -m housing_site_search deepen --handoff runs/my-search-handoff --out runs/my-search-deep
```

The sample BBL is illustrative command syntax; select actual matching BBLs from
your verified search output. Broad discovery can hand off other explicitly chosen
nonhousing lots independently. A changed target/template/source requires a new run.
The search copies and verifies both upstream packages, retains every lot/trial,
and creates independent detailed underwriting packets for selected scenarios.
Input scaling is explicit. Dollar debt/appraisal caps remain fixed scenario
assumptions; no commitment is transferable to a new project through this search.

Inspect packet.html, trials.csv, all-lots.csv, results.json and detailed models/.
Choose alternatives with a practitioner, then use the existing evidence-only
handoff. Do not send emails, publish a proposal, infer a site is available or
create an image without the user's requested next step and required inputs.

## Reuse an explicit program in existing area/geometry work

After verifying the search and an existing same-BBL parcel evidence packet:

```sh
python -m housing_site_search area-handoff --run runs/my-site-search --trial SELECTED_SCENARIO_ID --parcel-evidence runs/my-parcel-evidence --out runs/my-area-handoff
python -m housing_site_search verify --run runs/my-area-handoff
```

The adapter preserves the full search and selected financial model, and calls the
existing parcel replay with explicit area assumptions. The resulting analysis/
can feed the [geometry module](../../../src/housing_geometry/README.md) with a
separately sourced polygon and author-supplied footprints/heights/use allocations.
This is an explicit analyst branch, not automatic model-to-building approval.

Compare revised targets or a revised financial template on the **exact same**
reviewed evidence:

```sh
python -m housing_site_search compare --left runs/my-site-search --right runs/my-revised-search --out runs/my-search-comparison
```

The comparison retains both inputs and all changed trial values/reasons. A changed
source packet must be investigated as a source change rather than silently
attributed to a modeling assumption.
