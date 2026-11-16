# Site feasibility report

Assemble the verified packages from a lot analysis into one standard-shaped report.
It opens with the brief (the user's goal in their words, what they provided), how we
got here (each step, its package and the decisions taken) and, when an area search
ran, the ranked candidates and why this site was chosen. Then: site facts, ownership and transactions, zoning, proposed
program and massing, development budget (sources and uses), operating pro forma,
debt sizing, sensitivity across scenarios, the visual concept, open items and a
source appendix. Standard library only.

```sh
python -m housing_feasibility brief start --goal "USER'S WORDS" --persona housing_agency --out runs/NAME/brief.json
python -m housing_feasibility brief decide --brief runs/NAME/brief.json --step select --proposed "..." --answer "..."
python -m housing_feasibility template --out runs/NAME/report-request.json
python -m housing_feasibility build --request runs/NAME/report-request.json --brief runs/NAME/brief.json \
  --evidence runs/NAME/evidence --underwriting runs/NAME/underwriting/BASE \
  [--underwriting ...] [--massing ...] [--ownership ...] [--render ...] [--discovery ...] \
  --out runs/NAME/report
python -m housing_feasibility verify --run runs/NAME/report
```

## Blocks

Each block appears only when its step ran: area search, ownership, massing, render.
Long lists go to appendices: every candidate, every financing scenario, every
decision, every source. The same layout serves an area-to-report run, a known-lot
run without a search, or a model-only run.

## How it stays honest

- The goal and decisions come from `brief.json`, which the agent starts before any
  work and appends to as the user decides; entries are never edited.
- Each input is copied into `inputs/` and re-verified by its own module
  (`housing_workflow`, `housing_underwriting`, `housing_geometry`, `housing_render`,
  `housing_ownership`) at build and at every `verify`. The area-search package is
  verified at build and kept as an extract bound to its manifest hash.
- The report adds no estimates. Values are copied from verified packages; the only
  calculations are labelled ones such as recorded lot area × recorded FAR and
  cost per home.
- All inputs must describe the same tax lot. Cross-checks are reported, not hidden:
  scenario gross area against massing, residential area against recorded FAR, render
  story count against massing.
- `report.json` is the typed contract for downstream uses (slides, comparisons,
  render prompts); `report.html` and `report.md` are deterministic projections of it.
- A report built by a different version of this module fails `verify`; rebuild into
  a new folder.

## Limits

Not an appraisal, zoning determination, title opinion, design, cost estimate or
financing commitment. Recorded FAR comes from PLUTO, not the Zoning Resolution text.
The section layout follows common development-memo practice and is open for
practitioner review.
