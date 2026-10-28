# Worked example with live public sources

28 October 2026 collection: BBL 2028710002, recorded address 1240 Edward L Grant Highway, Bronx. Four exact-BBL requests succeeded: one PLUTO row, 27 legacy DOB job/document rows, zero DOB NOW rows and zero HPD violation rows. Zero returned rows do not prove no activity or housing. These records are current retrieved snapshots, not a historical decision-date packet.

Read [packet.md](parcel-investigation/packet.md), [ir.json](parcel-investigation/ir.json) and [image-prompts.json](parcel-investigation/image-prompts.json). Run `python -m housing_workflow demo --out runs/first-demo` from the repository root to produce a portable local copy and open its HTML.

The model preserves PLUTO's recorded zero residential units and a 2003 filing's nine proposed dwelling units as different observations needing reconciliation. It does not claim nine present-day homes, vacancy or displacement. The optional 40,000-sf area budget is explicitly hypothetical and yields 34 home-equivalents, not verified capacity. No professional review is recorded.

A second live run resolved **1337 Jerome Avenue** to BBL **2028560051**, fetched the four parcel sources and produced an evidence-only packet with 35 claims. No development scenario was supplied and no home-equivalent count was invented. Read [that packet](jerome-evidence-only/packet.md) or replay it offline:

```sh
python -m housing_workflow replay --from-run examples/jerome-evidence-only --out runs/jerome
```

These examples test the executable path and reveal recorded signals. Neither is an independent backtest or a professionally reviewed development recommendation.
