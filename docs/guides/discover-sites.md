# Discover nonhousing sites and test housing goals

Ask your agent a question such as “Find nonhousing sites near Bronx transit where
housing could be built, and distinguish existing residential permission from a
rezoning.” Start with [setup](setup.md) once. Give a bounded geography or let the
agent help define one. Auto/parking lots are one use among retail, warehouses,
vacant land and other recorded nonhousing uses.

The [nonhousing discovery skill](../../skills/discover-nonhousing-sites/SKILL.md)
collects the area and preserves all lots. It separates housing, recorded
nonhousing, conflicting housing signals and missing current-use data. General
zoning paths are housing permitted in principle, rezoning, or special/unresolved
review. Those are investigation categories, not feasibility findings.

**What you get:** a packet listing every lot in the area, the nonhousing lots
grouped by zoning path with their size, station distance and review flags, and
a CSV of all lots. See the [Jerome Avenue example](../../research/nonhousing-discovery/cases/jerome/packet.md)
(1,921 lots, 457 recorded nonhousing). A few-block area collects live in about a
minute; a neighborhood takes longer. If collection returns 0 lots with certificate errors,
see [setup](setup.md#if-live-collection-reports-certificate-errors).

## Collect public evidence

```sh
python -m housing_site_discovery collect --input config/site-discovery/jerome.json --out runs/area-evidence
python -m housing_site_discovery context --evidence runs/area-evidence --out runs/area-context
python -m housing_site_discovery discover --evidence runs/area-evidence --context runs/area-context --input config/site-discovery/jerome.json --out runs/area-discovery
```

The request's bbox uses recorded parcel points. It is not a cadastral intersection
or walked transit catchment. PLUTO, zoning fields, ZAP projects and City-owned/
leased uses retain their raw records. The optional public-context stage adds
actual station-point proximity, industrial-business-zone polygons and DCP Fast
Tracker publisher context with its own source versions. Industrial policy and
Fast Tracker screening do not grant zoning permission or environmental clearance.

Review source differences before narrowing the search. PLUTO can report zero
homes where historical DOB records contain dwelling signals. Monthly zoning tax
lot records can differ from older source vintages. Separate review stages preserve
those conflicts instead of erasing records or calling failed queries empty:

```sh
python -m housing_site_review collect --discovery runs/area-discovery --out runs/area-dwelling-review
python -m housing_zoning_review collect --parent runs/area-dwelling-review --out runs/area-zoning-review
```

Each stage has `verify --run PATH`. A valid trusted CA bundle may be needed on
some local Python installations; use the documented `--ca-file` option. All
outputs stay in fresh local directories and completed results remain unchanged.
See the [source-discovery study](../../research/public-data-registry/README.md) for
additional publisher resources and the optional BetaNYC MCP locator.

## Add explicit modeling and goals

Discovery needs no assumed FAR or financial program. When ready, supply desired
home counts, price/rent/cost assumptions and search targets. The agent should
explain those choices rather than silently adopting the checked-in analyst probes.

```sh
python -m housing_underwriting build --input config/underwriting/rental-60-lower-rent.json --out runs/rental-template
python -m housing_site_search build --discovery runs/area-zoning-review --underwriting runs/rental-template --input config/site-search/transit-rental-targets.json --out runs/area-target-search
```

The [rental model](../../src/housing_underwriting/README.md) separates development
cost, annual operations/reserves, debt limits and funding status. The
[search](../../src/housing_site_search/README.md) works backward from desired
programs to required area and explicit financial needs. Targets can include
station-point distance, zoning path, policy/housing-signal review, scheduled rent,
annual cash flow and unallocated capital/home. Specify whether a rent cap applies
to year1 or every projection year. Land prices and cost/rent values are scenario
inputs, not automatically verified market estimates.

Every failed/unknown trial remains visible. Non-dominated alternatives expose
tradeoffs; the module provides no universal site/community-benefit score.
Inspect the selected detailed financial packets and the broad source evidence.
A conditional match still needs current occupancy/leases, owner intent, title,
parcel assembly, applicable zoning maps/text, survey/layout, environmental work
and financing review.

## Investigate selected lots

```sh
python -m housing_site_search handoff --run runs/area-target-search --bbl SELECTED_MATCHING_BBL --out runs/selected-handoff
python -m housing_site_search deepen --handoff runs/selected-handoff --out runs/selected-deep
```

The handoff verifies and uses the existing Bronx parcel workflow in evidence-only
mode. Broader discovery can hand off other explicitly selected nonhousing lots
independently of any particular financial target. A model is not silently turned
into a lawful building program. Area recipes, housing-offer comparisons, RER,
geometry and imagery remain optional existing stages with their own inputs and
verification. No email, acquisition or publication is automatic.
