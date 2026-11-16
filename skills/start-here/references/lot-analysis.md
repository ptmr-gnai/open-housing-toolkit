# Full lot analysis: from an area to a report

The standard chain when a user wants to find a site and take it all the way: area
search, one lot's records and ownership, schematic massing, financing scenarios,
an optional render, and the feasibility report. Every step uses an existing module
or `scripts/plan_lot.py`; do not hand-write polygons, underwriting JSON, comparison
tables or report HTML. Run from `~/open-housing-toolkit` with `.venv/bin/python`.
Use one project folder, `runs/NAME/` and new subfolders for each step. Values in the
examples are illustrative; use the user's. `BBL` means the ten digits.

## 0. Start the brief, before any work

The brief records the user's goal in their own words, what they gave you, and every
decision. The report's Brief, "How we got here" and decision log come from it, so
quote the user; don't paraphrase. Pick `--persona` from the user's own role
(`housing_agency`, `developer`, `community` or `other`); ask if unclear.

```sh
.venv/bin/python -m housing_feasibility brief start --persona housing_agency \
  --goal "USER'S GOAL, VERBATIM" --item "Area=about five blocks around Burnside Av (4)" --out runs/NAME/brief.json
# after each choice the user makes (steps: search, select, massing, financing, render, report, other):
.venv/bin/python -m housing_feasibility brief decide --brief runs/NAME/brief.json --step select \
  --proposed "WHAT YOU PROPOSED" --answer "THE USER'S ANSWER, VERBATIM"
```

Add a `brief provide --item "Label=value"` when the user hands over something new (a
photo, a budget, a constraint). Record at least the search area, the chosen site
(with the user's reason), the massing and the financing approvals.

Before step 3, show the user every assumption in one list and wait for a yes:
heights; ground-floor shop area; floor heights (15 ft ground, 10 ft upper); upper
floors as a share of the ground plate; apartment efficiency (0.8) and average size
(750 sf); land cost; hard cost per sf; rent per apartment per month; retail rent
($35/sf/yr); vacancy (5% / 10%); hard contingency (10%); soft costs (20% of hard);
mortgage interest (6.5%, other terms from the template); sponsor equity ($3M,
proposed). Pass their answer as `--approval-note` to both planning commands.

## 1. Find candidates (any borough)

"About five blocks" is roughly 400 m (`--radius-m 400`, an 800 m square). Collection
takes one to four minutes; run it in the background and tell the user it is working.

Station names follow the MTA list (149 St-Grand Concourse is "149 St-Hostos").
If `locate.py` says ambiguous, ask the user which option they mean.

```sh
.venv/bin/python scripts/locate.py area --station "Burnside Av" --routes 4 --radius-m 400 \
  --question "USER'S QUESTION" --out runs/NAME/request.json
.venv/bin/python -m housing_site_discovery collect --input runs/NAME/request.json --out runs/NAME/area-evidence
.venv/bin/python -m housing_site_discovery context --evidence runs/NAME/area-evidence --out runs/NAME/area-context
.venv/bin/python -m housing_site_discovery discover --evidence runs/NAME/area-evidence --context runs/NAME/area-context \
  --input runs/NAME/request.json --out runs/NAME/discovery
```

Open `discovery/packet.html`, then rank the lots worth discussing first:

```sh
.venv/bin/python scripts/plan_lot.py shortlist --discovery runs/NAME/discovery --top 8
```

It lists privately used nonhousing lots (stores, garages, industrial, offices,
vacant) by unused recorded residential floor area and station distance. It is a
browsing order, not a viability ranking (the report shows the same ranking and lists
every candidate in an appendix). Choosing the lot is a judgement you make with the user (frontage on a commercial street, flags, owner type). Copy addresses
and tax lots exactly. A recent sale (step 2) gives the money model a land-cost basis.

## 2. Research the chosen lot (Bronx for the full chain)

```sh
.venv/bin/python scripts/locate.py lookup "ADDRESS, Bronx"     # confirm BBL with the user
.venv/bin/python -m housing_workflow run --input runs/NAME/lot-request.json --out runs/NAME/evidence
.venv/bin/python -m housing_ownership --bbl BBL --run-id ownership --out runs/NAME   # -> runs/NAME/ownership
.venv/bin/python -m housing_geometry collect --bbl BBL --out runs/NAME/parcel
```

Write the lot request first:
`.venv/bin/python scripts/plan_lot.py lot-request --bbl BBL --question "WHY THIS LOT" --out runs/NAME/lot-request.json`.
Tell the user the zoning district, lot area, recorded FAR, existing building, the
latest deed and any conflict. For the ownership summary run
`.venv/bin/python scripts/plan_lot.py ownership --run runs/NAME/ownership`. A deed's
recorded amount is not a sale price; the DOF sale row is.

## 3. Sketch what could be built

Agree with the user one or two heights and how much ground-floor space is shops or
community use. Then, per height:

```sh
.venv/bin/python scripts/plan_lot.py massing --evidence runs/NAME/evidence --parcel-source runs/NAME/parcel \
  --stories 7 --ground-nonresidential-sf 12000 --upper-coverage 0.8 --out runs/NAME/plan-7
.venv/bin/python -m housing_workflow replay --from-run runs/NAME/evidence --input runs/NAME/plan-7/area-request.json --out runs/NAME/area-7
.venv/bin/python -m housing_geometry build --analysis runs/NAME/area-7 --parcel-source runs/NAME/parcel \
  --scenario runs/NAME/plan-7/geometry-scenario.json --out runs/NAME/massing-7
```

Add the `--approval-note` from the approval above. `program.json`
reports gross area, homes, and residential area ÷ lot area, which you compare with
the recorded FAR. On an irregular lot the ground plate is the largest rectangle that
fits; if the shops don't fit, the error says the maximum. Open `massing-7/packet.html`.

## 4. Test the money

No recent sale (no DOF row, or a deed amount of $0)? Propose a land value, say plainly
it is a test value, and record the user's answer; `--land-note` says so in every
scenario. `scenarios` writes one request per combination, `scenarios.json` (with the
`base_case`) and `assumptions.md`, the list the user approved, for the record.

```sh
.venv/bin/python scripts/plan_lot.py scenarios --program runs/NAME/plan-7/program.json --site-label "ADDRESS" \
  --land-usd 15000000 --land-note "Recorded sale, DATE (DOF/ACRIS)" --hard-cost-psf 450,525,600 \
  --rent-per-home-month 1800,2400,3000 --approval-note "Approved by the user on DATE." --out runs/NAME/scenarios-7
for f in runs/NAME/scenarios-7/[0-9]*.json; do
  .venv/bin/python -m housing_underwriting build --input "$f" --out "runs/NAME/underwriting/$(basename "$f" .json)"
done
.venv/bin/python scripts/plan_lot.py results --underwriting runs/NAME/underwriting   # cost, loan, gap, yield per scenario
```

## 5. Picture (needs a site photo or Street View screenshot)

`plan-7/render-scenario.json` already matches the massing's story count; confirm its
architectural treatment with the user. Write the scene from the user's photo and
follow [prepare-render-brief](../../prepare-render-brief/SKILL.md) with
`--scenario runs/NAME/plan-7/render-scenario.json --photo PATH --analysis runs/NAME/evidence/ir.json`,
then [render-site-concept](../../render-site-concept/SKILL.md) in Codex, or the
[runtime route](agent-runtimes.md) handoff in Claude Code.

## 6. The report

See [assemble-feasibility-report](../../assemble-feasibility-report/SKILL.md). The
base case is `base_case` from the `scenarios.json` of the height the user prefers
(the lower height if they have no preference); every scenario appears in sensitivity.

Every height's scenarios can share one `runs/NAME/underwriting` folder; the report and
`plan_lot.py results` group them by program. `prepared_by` names the agent and who
approved the inputs, e.g. "Codex, assumptions approved by the user".

```sh
.venv/bin/python -m housing_feasibility template --out runs/NAME/report-request.json   # then fill it in
.venv/bin/python -m housing_feasibility build --request runs/NAME/report-request.json --brief runs/NAME/brief.json \
  --evidence runs/NAME/evidence --underwriting runs/NAME/underwriting \
  --massing runs/NAME/massing-7 --massing runs/NAME/massing-9 --ownership runs/NAME/ownership \
  --discovery runs/NAME/discovery [--render runs/NAME/render] --out runs/NAME/report
```

Open `report/report.html` and summarise the yield on cost (year-1 net operating
income ÷ total cost), the remaining gap, the zoning check, the latest deed and the
top open items.
