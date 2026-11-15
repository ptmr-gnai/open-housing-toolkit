# discover-housing-sites: execution reference

Run from the editable repository checkout with Python 3.11+. Read the
[module guide](../../../src/housing_discovery/README.md) and use the
[request schema](../../../src/housing_discovery/request.schema.json) when authoring
inputs. [Jerome probe settings](../../../config/discovery/jerome-far6.json) are a
worked experiment, not endorsed zoning or selection policy.

## Inventory and screening

```sh
python -m housing_discovery collect --input config/discovery/jerome-far6.json --out runs/jerome-inventory
python -m housing_discovery screen --inventory runs/jerome-inventory --input config/discovery/jerome-far6.json --out runs/jerome-screen
python -m housing_discovery verify --run runs/jerome-screen
```

Live collection uses allowlisted public Socrata APIs: PLUTO, ZAP parcel links,
ZAP project metadata and City-owned/leased property uses. It records raw responses,
queries, metadata, timestamps and failures. A valid trusted CA bundle may be passed
with `collect --ca-file PATH`; never disable TLS verification. A failed/truncated
context query remains missing evidence. An incomplete primary inventory blocks
ranking. The geography is defined by source points in a bbox, not intersecting lot
polygons or a walked transit catchment.

Open packet.html/packet.md and all-lots.csv. Every inventory lot has a disposition,
including those held by size, recorded homes, mission, pipeline or missing inputs.
Public and institutional uses are a distinct configurable review mission. Display
known environmental and special-district flags without treating them as clearance
or automatic impossibility. Rent stabilization, subsidies, owner intent, physical
fit and economics remain unresolved in v1.

## Compare and hand off

Screen the same inventory with another explicit request, then:

```sh
python -m housing_discovery compare --left runs/jerome-screen --right runs/jerome-other-screen --out runs/jerome-comparison
python -m housing_discovery handoff --screen runs/jerome-screen --top 3 --out runs/jerome-handoff
```

Comparisons require the exact same retained inventory. The handoff includes the
verified screen and supported evidence-only requests for selected Bronx BBLs.
For live deeper collection, read the [housing-investigation skill](../../housing-investigation/SKILL.md)
and run `python -m housing_discovery deepen --handoff runs/jerome-handoff --out runs/jerome-deep`.
This invokes the existing parcel module, preserves discovery lineage, and verifies
each output. Other borough inventories can be screened but the present deeper
parcel workflow supports only the Bronx. No acquisition, image, publication or
external message is implied by a discovery run.

For the auto-lot use case, preserve the scenario and apply the explicit
[auto/parking focus](../../../config/discovery/focus/auto-parking.json):
`python -m housing_discovery focus --screen runs/jerome-screen --input config/discovery/focus/auto-parking.json --out runs/jerome-auto`.
Zero recorded homes and residential FAR zero are allowed. Auto-related business
uses are candidates with occupancy/lease questions; they are not cleared sites.
