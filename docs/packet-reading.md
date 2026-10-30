# Read the packet without reading every claim

New parcel and area-recipe packets start with a deterministic extract of their
existing typed claims. It states evidence origin, raw-source retrieval dates,
PLUTO row vintage, failed/truncated sources, recorded parcel fields, supplied
assumptions, the conditional area result and unresolved input categories. Every
analytical statement links to its existing claim; details remain below.

The extract adds no professional interpretation or prioritized recommendation.
Recorded units do not establish actual/lawful occupancy; an area quotient does not
establish homes. A recently retrieved source may contain older observations.

Execution metadata lives in execution.json, separate from the analytical IR and
source receipts. Its [closed schema](../housing_workflow/execution.schema.json)
and frozen Python record distinguish live_collection, retained_snapshot_replay,
retained_snapshot_analysis and not_recorded. Modes describe the code path invoked,
not independent proof that a remote source is truthful or complete. Collection
records per-source failures; no recent date is used to infer a live collection.

Replay retains the original source manifest and checks source/receipt bytes against
it. Recipe runs bind the retained evidence manifest and state that the modeling
step did not collect new data. Existing historical packets retain their original
wording and source versions; rebuilding into a fresh run produces the new opening.

See [the independent live-lot trial](../examples/live-lot-trial/README.md) for a
new property and the boundaries between technical execution and usable proposal
materials. Cost-comparison and RER packets retain their existing specialized
summaries; this first revision improves the observed parcel/area-packet problem.
