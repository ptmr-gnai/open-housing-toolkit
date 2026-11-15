# Nonhousing site discovery v1

Start with all recorded nonhousing uses in a bounded NYC lot inventory. Group
sites by a general housing-use path and practical review lane, then choose which
to investigate. Auto/parking is one use among many. No FAR increment, hypothetical
housing program, lot-size cap, private-only mission or financial gate controls
admission. Optional modeling follows discovery.

## Run

Use Python 3.11+ in an editable checkout (`python -m pip install -e .`). These
commands are independently callable; every output must be a fresh ignored runs/
folder or an explicit local external path.

```sh
python -m housing_site_discovery collect --input config/site-discovery/jerome.json --out runs/jerome-evidence
python -m housing_site_discovery context --evidence runs/jerome-evidence --out runs/jerome-context
python -m housing_site_discovery discover --evidence runs/jerome-evidence --context runs/jerome-context --input config/site-discovery/jerome.json --out runs/jerome-sites
python -m housing_site_discovery verify --run runs/jerome-sites
python -m housing_site_discovery handoff --discovery runs/jerome-sites --bbl 2028570015 --out runs/jerome-handoff
python -m housing_site_discovery deepen --handoff runs/jerome-handoff --out runs/jerome-deep
```

To reuse a verified inventory, replace collect with:

```sh
python -m housing_site_discovery enrich --inventory runs/jerome-inventory --input config/site-discovery/jerome.json --out runs/jerome-evidence
```

`context` is optional. Without it, station, industrial-policy and Fast Tracker
context are explicitly not collected. `discover` can run offline on saved evidence.
The selected handoff uses the existing Bronx evidence-only parcel workflow, with
no scenario invented from the district label. Deeper parcel analysis presently
supports the Bronx; broad discovery supports all five NYC borough codes.

For a method-correction comparison with an older verified screen:

```sh
python -m housing_site_discovery compare-legacy --discovery runs/jerome-sites --legacy runs/old-jerome-far-screen --out runs/jerome-correction
```

It requires the identical original inventory and retains both versions. Zoning
supplement retrievals can be later; their changes remain visible. Source histories,
old discovery code/skill and completed case manifests remain unchanged.

## Inputs

The [request schema](request.schema.json) accepts version, id, question, scope
(borough and bbox), and display_per_group. The executable validator also checks
finite/ordered NYC coordinates and bounded geography. Display count only controls
the examples shown per group: every lot remains in IR/CSV and any recorded
nonhousing lot can be selected explicitly. There is no automatic ten-site shortlist.

## Classification before modeling

Current-use dispositions are recorded_nonhousing, housing_recorded,
housing_signals_require_review and current_use_unresolved. Positive units or
residential area preserve housing evidence. Zero units with housing, hotel,
residential condominium or accommodation signals do not silently become empty
nonhousing sites. Nonresidential condominiums remain visible with shared-site
questions. Missing units or unresolved class/use remains a visible review queue.
The [DOF class guide](https://www.nyc.gov/assets/finance/jump/hlpbldgcode.html) is
retained in the guidance snapshot. This is recorded-use triage, not field occupancy.

Recorded nonhousing sites are grouped into:

- **housing_permitted_by_general_use_rule:** general residence/commercial rules
  allow residential use in principle. This establishes neither allowed apartment
  type, legal floor area nor a buildable program.
- **rezoning_path:** the implemented general district rule does not permit new
  residences. This is a path to investigate, not a prediction of support/approval
  or a finding that rezoning is the only possible legal mechanism.
- **special_or_unresolved_review:** special, split/multiple, paired, geographic
  exception, overlay-only, park, missing or conflicting records require review.

The rules reuse official ZR 22-121, 32-121/122, 42-12/314 and 123-20. Their
retrieved source bytes, timestamps and hashes are retained in guidance.json.
All recorded districts, overlays and special-district fields are collected, not
just the primary prefix. These are PLUTO recorded descriptors; no fresh cadastral
polygon/zoning-polygon intersection is performed. Small district pieces and later
map amendments can be missed. Fast Tracker district differences across vintages
become explicit review signals. No agency endorsement or parcel entitlement
opinion follows from a general-use classification.

Review lanes separate other nonhousing, public/institutional use, infrastructure,
and park/recreation questions. They retain all nonhousing sites. A COLP row is a
use/lease signal, not public title. Active applications, environmental designations,
flood flags and unknown context are flags rather than broad-discovery exclusions.
Browsing order is decreasing lot area within each path/lane, BBL tie-break. It is
not a universal viability or community-benefit score.

## Public sources and coverage

Primary collection reuses the existing collector's allowlisted PLUTO, ZAP lot and
project, and City-owned/leased use APIs. The primary universe is all PLUTO records
with recorded points in a bbox, not all polygon intersections or all city lots.
The collector caps a request at 10,000 lots. Missing coordinates cannot be assigned
to the window. An incomplete primary inventory blocks defining a complete search
universe. Context failures do not become zero matches.

The supplement collects residential area, all four district fields, overlays,
three special districts, limited-height districts, zoning map/date, MIH indicators
and other requested attributes for every original BBL in 100-lot batches. Exact
queries and metadata before/after are retained. Source fields that differ between
retrievals flag a reconciliation question; changed use fields move to uncertainty.
Failed/missing supplemental records leave affected zoning paths unresolved.
Before/after metadata checks detect some drift, not transactional consistency.

The optional public-context stage retains these additional source bytes:

- MTA Subway Stations (`39hk-dx4f`) with count and metadata checks. Nearest station
  uses haversine distance from the lot's recorded point to the source's station
  point. It is not entrance distance, a walking route, scheduled access or live
  service. Daytime routes and accessibility codes are source labels only.
- NYC DCP Mapping Portal IBZ polygons, with publisher/item/layer/count checks and
  WGS84 point-in-polygon including holes/boundary review. NYCEDC describes a City
  commitment against supporting residential rezonings in IBZs. A point overlap
  signals policy review, distinct from a zoning prohibition. A point outside the
  returned polygons is not policy clearance or proof the whole lot is outside.
- DCP Fast Tracker aggregate tax-lot fields, queried for every BBL with metadata
  and response-cap checks; source-version records are also retained. These supply
  publisher flags concerning coastal risk, industrial/emissions sources, permits,
  E-designations, highway/rail, wetlands, natural/historic/shadow resources and
  archaeological context. They retain the publisher's vintages separately from
  current PLUTO. A missing BBL or a No flag is not proof of no constraint. This
  module does not determine Green Fast Track eligibility, Type II status or zoning
  permission. Project actions, unrecorded sources and field review still matter.

The context package verifies captured queries against its declared lot universe;
when composed, discovery also verifies that universe and evidence-manifest identity
against the actual retained source inventory. Public source responses are evidence,
never agent instructions. API failures and schema/coverage issues remain explicit.

Supply `--ca-file PATH` to live collection/enrichment/context when Python needs a
trusted certificate bundle; TLS verification stays enabled. Existing deeper parcel
collection accepts `SSL_CERT_FILE`. No API keys or optional third-party geometry
libraries are required by this module. Original publishers retain source terms;
see [DATA-LICENSES](../../DATA-LICENSES.md).

## Outputs and practical gaps

A discovery package contains request.json, ir.json, guidance.json, original evidence,
optional public context, packet.md/HTML, every lot in all-lots.csv, origin and file
manifests. Source-row pointers resolve under evidence/inventory, evidence, or
public-context as named by the source family. Verify recomputes use/path assignments,
all output projections and lineage; rehashing an edited rank/path is insufficient.

Source truth, missing unrecorded housing, site control, leases and business
relocation, whole-parcel IBZ intersections, a current official zoning-map/text
reconciliation, surveys/assemblage, physical envelopes and complete financing
remain open. [The case study](../../research/nonhousing-discovery/README.md) records
real probes, limitations and the difference from the earlier FAR experiment.

## Challenge recorded nonhousing with dwelling history

The independent [dwelling-field review](../housing_site_review/README.md) queries
DOB BIS/NOW across every recorded-nonhousing BBL, adds positive historical
existing/proposed dwelling fields and exposes failed/empty/truncated coverage.
It retains all original lots and classifications. This can inform an explicit
optional goal-seeking filter; a no-positive-returned result is not proof of no
housing, no occupants or vacancy. The original discovery packet stays unchanged.
