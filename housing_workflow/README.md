# One parcel from intake to evidence packet

This is the first integrated workflow in the Open Housing Toolkit. It is deliberately a partial playbook: the full professional process is not known and will develop through real use and review. It supports one Bronx tax lot, four public datasets and an optional user-stated area budget. The previously frozen research experiments remain unchanged.

## Try the worked example

From the repository root, Python 3.11+ recommended. The workflow itself needs only the standard library, no API key, model account or pip install.

```sh
python -m housing_workflow demo --out runs/first-demo
```

Open `runs/first-demo/packet.html` in a browser, or read `packet.md`. This replays committed real source responses, including their original retrieval dates. It is not live data collection. GitHub displays HTML source; download the run directory or generate the example locally to use the portable HTML.

An agent can start with [the entry skill](../skills/housing-investigation/SKILL.md). Example instruction:

> Read skills/housing-investigation/SKILL.md. Run the offline example first. Then ask me for a Bronx site and the question I want to investigate. Produce a cited information packet, keeping assumptions and unresolved professional questions visible.

## Investigate another site

Use the interactive intake or have an agent write the same structured request:

```sh
python -m housing_workflow init --out runs/my-inputs/request.json
python -m housing_workflow run --input runs/my-inputs/request.json --out runs/my-investigation
```

A BBL is the most reliable identity input. Exact address resolution accepts limited street-suffix variants; ambiguous/unmatched addresses stop and request a BBL. Examples, including a different live-tested parcel, are in `examples/`.

The agent can collect an optional scenario: total gross area, nonresidential gross allocation, residential net efficiency, and average net home size. Each needs a rationale. With no scenario, the same workflow produces records and questions without inventing a home count.

## Steps and outputs

The discrete workflow is [parcel-investigation.json](../workflows/parcel-investigation.json). Each skill maps to an independently callable stage:

```sh
python -m housing_workflow collect --input request.json --out runs/staged
python -m housing_workflow build --run runs/staged
python -m housing_workflow verify --run runs/staged
```

| Artifact | Purpose |
| --- | --- |
| request.json | User question, site input and explicitly explained assumptions |
| sources/*.json | Unchanged public API response bodies |
| receipts.json | Queries, dates, publishers, terms, hashes, failures and truncation |
| workflow.json | Versioned steps and explicit professional coverage gaps |
| ir.json | Typed facts, assumptions, calculations, unknowns, judgments and dependencies |
| calculation-steps.csv | Calculation values, formulas and dependencies for inspection or later workbook use |
| packet.md and packet.html | Readable evidence packet with a complete selected-field provenance register |
| image-prompts.json | Diagram/evidence-card prompt with claim IDs, values and a model hash |
| manifest.json | File inventory, source/artifact hashes and implementation bindings |

The local source router is [sources.json](sources.json) plus `router.py`: PLUTO, DOB BIS, DOB NOW and HPD violations. A future network proxy can implement the same contracts. It is not required for this slice. Exact-BBL matching, 501-row response caps and missing historical linkage limit coverage. A failed API call stays failed; it cannot generate a zero-row fact. API rows are not deduplicated projects.

The model preserves every selected field in successful returned records with a JSON pointer and source hash. It surfaces all positive historical existing/proposed dwelling-unit signals alongside PLUTO recorded units. It does not resolve which units exist now or are lawful. Retrieval dates are not observation dates.

## Inspect and change a calculation

The example assumes 40,000 gross sf, 6,000 nonresidential gross sf, 80% residential net efficiency, and 800 net sf per home-equivalent. The area budget is `(40,000 - 6,000) × 0.8 ÷ 800 = 34` home-equivalents. These are demonstration assumptions, not a proposed or physically verified building. The gross-area/recorded-lot-area quotient is not zoning FAR.

Copy the request to `runs/alternative-input.json`, change a value and explain why, then:

```sh
python -m housing_workflow replay --from-run runs/first-demo --input runs/alternative-input.json --out runs/alternative
```

The same evidence is retained and dependent calculations, packet text and image-brief values are recomputed. Changing the BBL requires new collection. New output directories preserve previous runs. Input/implementation changes stale old bindings rather than silently blessing old conclusions.

A step-through notebook/workbook is a later extension. The current JSON graph and CSV are inspectable inputs to it. The image brief currently permits a labeled diagram, not a site-specific building rendering: legal capacity and geometry remain unverified. No image is generated or proposal submitted by this workflow.

## What is not established

Current occupancy, leases, title/control, applicable zoning text, building fit, environmental conditions, affordable-housing finance and usable transit access remain unknown. The model's next-question checklist is an unreviewed authored policy, not an evaluated priority. The packet explicitly retains incomplete practitioner-process coverage. A useful partial packet is possible without claiming those questions are solved.

## Checks

```sh
python -m housing_workflow verify --run examples/parcel-investigation
python -m unittest discover -s housing_workflow/tests -v
```

Schema tests use the repository's existing `requirements-dev.txt`; replay and artifact verification do not. Checks cover version/parcel bindings, exact raw values, dependency arithmetic, deterministic replay, failed/truncated sources, omitted receipts, cross-parcel reuse, changed assumptions, stale prompts and output tampering. Passing these checks does not establish semantic completeness or practitioner usefulness.
