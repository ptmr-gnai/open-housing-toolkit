# discover-nonhousing-sites: execution reference

Read the [module guide](../../../src/housing_site_discovery/README.md) for inputs,
source coverage, classification limits and examples. Run in the editable checkout
with Python 3.11+, writing each stage to a fresh ignored runs/ directory.

```sh
python -m housing_site_discovery collect --input config/site-discovery/jerome.json --out runs/jerome-site-evidence
python -m housing_site_discovery discover --evidence runs/jerome-site-evidence --input config/site-discovery/jerome.json --out runs/jerome-sites
python -m housing_site_discovery verify --run runs/jerome-sites
```

For an existing verified inventory, replace collect with `enrich --inventory PATH
--input config/site-discovery/jerome.json --out runs/jerome-site-evidence`. This
collects the broader recorded-zoning fields and residential area, retaining both
retrievals and any disagreement. Supply `--ca-file PATH` with a valid trusted CA
bundle if required; TLS verification remains enabled.

Review packet.md/packet.html and all-lots.csv. Keep housing and unresolved use
queues visible. The three general zoning paths do not predict rezoning approval,
constructible homes or economics. Special/split districts, uncertain observations,
parks and infrastructure need their stated reviews. Do not call all manufacturing
labels housing-prohibited: paired and exception districts need separate handling.

Select the BBLs worth investigating; examples are not an automatic shortlist:

```sh
python -m housing_site_discovery handoff --discovery runs/jerome-sites --bbl 2028570015 --out runs/jerome-site-handoff
python -m housing_site_discovery deepen --handoff runs/jerome-site-handoff --out runs/jerome-site-deep
```

Deeper investigation uses the existing Bronx evidence-only workflow and supplies
no building program. Read [its skill](../../housing-investigation/SKILL.md) for
that branch. Broader discovery supports other NYC boroughs; the current deeper
parcel workflow supports the Bronx only. Collection, modeling and imagery remain
independent; no external publication or messages are part of this workflow.
