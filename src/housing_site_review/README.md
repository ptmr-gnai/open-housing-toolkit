# Historical dwelling-field review

A separate optional stage challenges the recorded-nonhousing classification with
DOB BIS/NOW, HPD multiple-dwelling registrations and affordable-production records
for **every recorded-nonhousing BBL** in a verified
broad discovery package. It preserves every original lot and classification,
adds review evidence, and leaves current occupancy unresolved.

```sh
python -m housing_site_review collect --discovery runs/my-discovery --out runs/my-dwelling-review
python -m housing_site_review verify --run runs/my-dwelling-review
```

Use Python 3.11+ and the editable checkout. Outputs must be new ignored runs/
folders or explicit external local paths. `--ca-file PATH` accepts a trusted TLS
bundle. `--max-requests` declares a finite HTTP budget (default 160, supported 4–500).
Source failures and the exhausted budget remain explicit unknowns. No API keys,
images, external messages or publication are part of this stage.

The live collector reuses the existing parcel module's DOB dataset IDs/fields
and adds the two HPD datasets in [sources.json](sources.json). Registration joins
derive BBL explicitly from numeric borough/block/lot; production uses numeric BBL.
The collector queries 25 tax lots per batch, retains raw responses and before/after
metadata, and splits capped responses until uncapped coverage or a single-lot cap.
A failed large batch can split into groups of five; failed small batches remain
unknown. Queries are bounded and unpaginated; unsorted responses below the cap
retain their exact bytes and do not require unstable offset paging. A 10-second
request timeout and modest request spacing limit an unresponsive source. HPD and
replayed NOW coverage are collected before live BIS gap repair. The metadata check verifies BBL type, required fields, source identity
and update stability. This detects some drift, not transactional consistency.

Top-level ir.json retains the discovery contract for downstream compositions.
Each reviewed lot adds dwelling_review:

- **positive_returned_housing_signal:** at least one returned unit field is positive or an HPD registration/program
  record is linked, with raw-byte pointer and available filing/program dates.
  An expired registration or planned project is still a historical association,
  not current occupancy.
- **no_positive_returned_housing_signal:** all four bounded source families completed
  under stable metadata and returned no positive numeric dwelling field. This is
  a literal returned-field result, **not proof that housing is absent**.
- **housing_signal_coverage_unknown:** no positive field was found but a query,
  metadata, budget or cap prevented the declared coverage.

Successful empty queries and successful returned rows have distinct per-source
statuses. Rows missing both numeric dwelling fields are counted explicitly.
Positive signals remain visible even when another source is incomplete.
Nonhousing membership is not erased by this stage; source disagreements and
historical/proposed units require practitioner reconciliation. An occupied home,
completed development or current lawful use is not inferred from a filing field.
Exact BBL joins can miss historical lot changes and unlinked or unrecorded housing.

Open packet.html/packet.md for counts and known-signal lots; signals.csv gives every
positive field observation and source pointer. All-lots.csv retains the full base
universe. The original verified discovery is under discovery/. Source receipts,
raw bytes, review.json, augmented ir.json and output manifests support offline
replay. Verify recomputes coverage, extracted signals, the retained universe and
all output projections. It does not prove source truth or full housing history.

The [case study](../../research/nonhousing-discovery/README.md) records the actual
coverage and failed requests, including retail sites whose zero PLUTO apartments
coexist with positive historical DOB dwelling fields. Optional downstream search
can require the explicit no-positive-returned condition while keeping unknown
and failed targets visible. This condition is not an occupancy clearance.

## Recover or replay a capture explicitly

```sh
python -m housing_site_review recover --capture runs/my-partial-review --out runs/my-recovered-review --ca-file /trusted/bundle.pem
python -m housing_site_review recover --capture runs/my-recovered-review --out runs/my-offline-review --offline
```

Recovery validates a recognized source-capture implementation and every original
file hash, preserves its original receipts/failures under imported/, reuses
successful exact-query responses with original URLs/times and fetches gaps. Old
row ordering remains recorded; only a complete uncapped returned universe can be
reused regardless of ordering. It recomputes all current coverage and outputs;
it does not assert that old derived packets verify under changed code.

Offline replay imports known captured responses including failures and makes no
HTTP calls. Missing requests remain unknown. Nested import metadata vintages are
resolved to the actual original capture; replay cannot freshen old evidence or
turn a mixed-vintage unknown into a clean negative. Traversal paths, source
symlinks, unknown capture implementations and changed original bytes are rejected.
The live iterations and failed query-shape probes remain separate local history.
