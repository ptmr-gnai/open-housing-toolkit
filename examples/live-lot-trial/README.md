# Live-lot worker trial: 1940 Jerome Avenue

A fresh worker received the [practitioner brief](brief.md) and a repository copy,
without project history or commands. It collected actual current API responses,
built the supplied area budget and independent offers, and prepared review drafts.

**Start with the [live evidence packet](evidence/packet.md)** for its new short
opening: source origin, retrieval dates, recorded facts, supplied assumptions and
missing practitioner inputs. HTML is available locally at evidence/packet.html.

| Stage | Output | What it establishes |
| --- | --- | --- |
| Live evidence | [Packet](evidence/packet.md) · [execution metadata](evidence/execution.json) | Records for BBL 2028530012, collected 2026-10-30; sources and limits retained |
| Area recipe | [Packet](area/packet.md) · [trace](area/trace.json) | 13.5 home-equivalents from explicit assumptions; not building capacity |
| Independent offers | [Comparison](comparison/packet.md) | 12/18 total offers, 8/4 lower-income cost-and-bedroom matches; no winner or eligibility finding |
| RER preparation | [Index](rer/packet.md) · [coverage](rer/coverage.md) | Two incomplete five-section drafts; missing official data remains missing |

PLUTO 26v2 records **115 residential units**, not zero. Current/lawful occupancy,
tenancy, availability and development rights remain unverified. This test is not a
vacant-site recommendation. No comparison of existing versus proposed home losses,
net additions, financing or displacement was performed. The hypothetical programs
are independent of the area quotient and are not established as fitting this site.

The 2025 income/reference inputs are deliberately historical diagnostic inputs;
live 2026 retrievals do not make them current program rules. Source retrieval dates
are not observation dates for every field.

## What the independent first pass found

The worker completed all four stages, but correctly identified two defects that
passed the then-current checks: unrelated copied geometry text in two execution
references, and a demo-specific “24/36-home” explanation in new 12/18-home RER drafts.
Both are fixed. Evidence and area outputs here preserve its original verified
bytes. Comparison and RER were rebuilt into new packages after those corrections;
original first-pass artifacts were not edited to make them pass.

Read [the unedited first-pass report and protocol](../../docs/reviews/live-lot-worker.md).
Its temporary output paths refer to the original worker workspace. The same worker
then performed a clearly separated [follow-up check](../../docs/reviews/live-lot-corrected-followup.md)
on the corrected package; that was not another cold trial. It also produced
an optional HTML arithmetic visual there; that was not provider-generated imagery
or a toolkit-verified design artifact.

No site photograph, surveyed footprint, heights or massing scenario was supplied.
No site rendering, measured geometry, image-provider execution or official report
submission is claimed. The evidence package exports a labeled diagram-only prompt.
Expert review and substantive data remain necessary before a proposal or benefit
assessment is possible.

## Reproduce from retained sources

From the checkout root, using fresh output directories:

```sh
python -m housing_workflow verify --run examples/live-lot-trial/evidence
python -m housing_recipe verify --run examples/live-lot-trial/area
python -m housing_benefit verify --run examples/live-lot-trial/comparison
python -m housing_rer verify --run examples/live-lot-trial/rer
```

Replaying the evidence into a new run labels it cached replay, not new collection.
Use its request JSON with the `run` command to request genuinely new API responses.
Complete requests and the recipe are under inputs/. Upstream source terms apply;
these retained public-source bytes are not covered by the code license.
