# Minimal-context worker trial

A brand-new worker received no conversation history or recommended starting file.
It received an isolated copy of the current local working tree, not the previously
published GitHub revision. The supplied copy intentionally excluded .git and ignored
runs. Its reported lack of Git metadata is a test-fixture limitation, not a problem
with a normal clone. The parent did not coach it during execution.

Exact task:

> Here is a repository: /tmp/housing-cold-start-1v1kcuwb
> You are seeing it for the first time. Figure out what it does and try using it,
> following whatever instructions you find. Do not edit the repository's source
> files, publish anything or contact anyone. Report what you tried, what worked,
> where you got stuck, and what you think the results mean. Save your report to
> /tmp/housing-cold-start-review.md.

The report below is the worker's output. It tests the offline introduction, not
native host discovery, alternate module branches or practitioner usefulness.

---

# First-visit review: Open Housing Toolkit

Reviewed 2026-10-30 in `/tmp/housing-cold-start-1v1kcuwb`, using Python 3.12.14.

## What it does

This is a repository-based research prototype for housing practitioners and agents. It combines cached NYC parcel records, typed evidence and assumptions, editable area calculations, explicit hypothetical housing-offer comparisons, and preparation of incomplete Racial Equity Report (RER) drafts. It also documents independent geometry and image-concept branches. It is neither a hosted application nor a complete development-feasibility or regulatory-compliance system.

Its distinguishing feature is inspectable handoffs: raw records, retrieval receipts, inputs, claim graphs, versions, and manifests travel with the results. The documentation repeatedly distinguishes engineering consistency from domain correctness and practitioner acceptance.

## What I tried

I followed `AGENTS.md` → `skills/start-here/SKILL.md`, then read the project tenets, runtime preflight, module map, offline-tour instructions, and human first-run guide. I selected the documented general-introduction route rather than inventing a real project. Python and a writable checkout were available; this route required no pip installation, API credentials, image provider, or live collection.

I ran:

```sh
python scripts/first_run.py --out runs/cold-start-review
```

It completed in about three seconds. All eight child commands returned zero: parcel demo/verify, recipe build/verify, benefit-comparison build/verify, and RER build/verify. Execution commands and logs are retained in `runs/cold-start-review/steps.json` and numbered log files. The run contains 130 files.

I read the generated index, parcel and recipe Markdown packets, the comparison's tables and provenance entries, the RER index, and the instruction-coverage map. I used the Markdown outputs; I did not visually inspect the HTML in a browser.

I also ran:

```sh
python scripts/check_onboarding.py
```

It passed checks for 11 active skills, linked resources/routes, and 10 frozen skill hashes. This is link/routing integrity, not semantic validation of the playbooks.

Finally I retried the first-run command against the existing output directory. It exited 2 with `Blocked: Output already exists; choose a new directory`. SHA-256 hashes of all 130 generated files were identical before and after that attempted overwrite. The protection worked as documented.

## What worked and what the results mean

- **Getting started:** The explicit agent entry point and one-command tour were sufficient. I installed nothing and encountered no execution failure on the main route.
- **Parcel evidence:** The sample concerns BBL 2028710002, recorded as 1240 Edward L Grant Hwy. Retained source receipts are dated 2026-10-28; PLUTO identifies row version 26v2. Returned data include one PLUTO row, 27 DOB BIS rows, and zero DOB NOW/HPD violation rows. The packet correctly warns that zero returned records do not establish absence. PLUTO records zero residential units while a historical DOB filing mentions nine proposed dwelling units; the packet preserves that reconciliation question rather than asserting vacancy.
- **Area arithmetic:** `(40,000 gross sf − 6,000 nonresidential gross sf) × 0.8 / 800 net sf` gives 34 home-equivalents. These are declared demonstration assumptions, not legal capacity or a layout-verified unit count. The area/lot ratio is explicitly distinguished from zoning FAR.
- **Offer comparison:** Program A assumes 24 two-bedroom homes (16 at $1,000 rent and eight at $1,800); B assumes 36 (eight and 28 respectively). Each has $100 monthly utilities. At hypothetical annual income $48,600, the stated 30% threshold gives a $1,215 monthly budget. Thus $1,100 gross monthly cost passes and $1,900 fails, producing 16 versus eight matching homes. At $97,200 annual income, the $2,430 budget admits both bins, producing 24 versus 36. I checked this arithmetic against the displayed assumptions and traced the income reference to the retained passage from the pinned 2025 City guide. This establishes a conditional cost-and-bedroom diagnostic only. The two profiles overlap; their counts must not be added together. The offers are independent of the 34-home-equivalent area model.
- **RER preparation:** Two separate illustrative drafts and a 50-slot-per-program instruction map are produced. Missing EDDE/community data, applicant details, applicability, AMI/program interpretation, zoning area, and construction information remain visible. A 2023 form versus 2025 guide disagreement about nonresidential reporting is retained explicitly. The sample preparation date stays 2026-10-29 rather than silently becoming the execution date. Offline verification binds retained guidance metadata; it does not re-fetch or validate the external source PDFs or their interpretation.

Useful entry files:

- `/tmp/housing-cold-start-1v1kcuwb/runs/cold-start-review/README.md`
- `/tmp/housing-cold-start-1v1kcuwb/runs/cold-start-review/comparison/packet.md`
- `/tmp/housing-cold-start-1v1kcuwb/runs/cold-start-review/rer/packet.html`
- `/tmp/housing-cold-start-1v1kcuwb/runs/cold-start-review/rer/coverage.md`

## Where I got stuck or found friction

There was no blocker to completing the documented offline tour. The real stopping point is turning the sample into a substantive project decision: the run does not resolve occupancy/leases, title and site control, zoning applicability, physical fit, environmental obligations, financing, delivery, or the relevant community evidence. It cannot select a winning program or support submission.

A few first-visit frictions remain:

1. The README presents many experiments and entry points. The short start-here route helps, but without it the scope is harder to prioritize.
2. Generated parcel and recipe packets say they “Queried four NYC public datasets,” even though this execution replayed cached records. The top-level index and first-run guide explain the distinction, but a detached packet could still imply fresh collection.
3. The claim registers are long. The short index and coverage map are useful entry points; following individual claims is more manageable than reading every entry sequentially.
4. The example spans 2025 reference prices, 2026 source receipts, and supplied sample preparation metadata. The boundaries are documented, but a new user must attend to all three rather than treating the newest timestamp as current applicability.
5. `git status --short` failed because this supplied directory has no Git metadata. This did not affect the workflow, but I could not use Git to establish a clean checkout.

I did not test live collection, alternate assumptions, geometry, image generation, browser interaction, the legacy pipeline, the full developer test suites, or practitioner usefulness. Those remain untested here, not demonstrated failures.

## Preservation and overall assessment

I did not edit repository source files, publish anything, or contact anyone. Before execution I recorded hashes for 1,207 preexisting files outside `runs/` and Python bytecode directories. After execution all those files were unchanged, and no additional non-run/non-bytecode files appeared. New workflow artifacts are confined to the fresh `runs/cold-start-review` directory; Python may also create normal `__pycache__` files.

The documented offline onboarding works in this environment and yields a reproducible, readable chain of bounded research artifacts. The strongest result is a clear account of what the supplied records and assumptions support, and what they leave unresolved. Passing verification supports that implemented chain's technical consistency; it does not show that a development fits, that the inputs are professionally sufficient, or that a housing practitioner would find the workflow useful in real work.
