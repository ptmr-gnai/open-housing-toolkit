# Where things stand

November 2026. A plain summary for advisors and new contributors: what works,
what is good enough for now, and where practitioner judgement is needed next.

## The workflow in three stages

| Stage | Question | Status |
| --- | --- | --- |
| **1. Find candidate lots** | In a bounded NYC area, which lots are recorded as nonhousing, and what general zoning path applies to each? | **Working v1.** Works in all five boroughs; studied in depth on Jerome Avenue and Hunts Point (3,164 lots) and live-checked in Brooklyn. Good enough for a first pass. |
| **2. Investigate a lot** | What do public records say about one Bronx lot? | **Working.** Tested end to end on several live Bronx lots. Produces a cited evidence packet. |
| **3. Model scenarios** | Could a stated program and financing structure work on that lot? | **Experimental.** The arithmetic is checked; the assumptions are not. This is where expert judgement is needed. |
| **4. Feasibility report** | What does the whole analysis say, in a standard format? | **New (Nov 16).** Assembles verified packages into site, zoning, sources and uses, pro forma, debt, sensitivity, render and open items. Section layout open for practitioner review. |

Each stage runs on its own. An agent (Codex or Claude Code) can guide you through
any of them from [AGENTS.md](../AGENTS.md).

## 1. Find candidate lots

[Guide](guides/discover-sites.md). Give a bounding box and a question. The
toolkit pulls every recorded lot in the area from PLUTO and sorts it into four
groups: recorded housing, recorded nonhousing, conflicting housing signals, and
unknown current use. Nonhousing lots are grouped by general zoning path: housing
permitted in principle, rezoning needed, or special review. Optional stages add
subway-station distance, industrial business zones, Fast Tracker flags,
historical dwelling records (DOB, HPD) and monthly zoning records.

Example output: [Jerome Avenue discovery packet](../research/nonhousing-discovery/cases/jerome/packet.md).
A few-block area takes one to four minutes to collect live; `scripts/plan_lot.py shortlist` lists the lots worth discussing first.

What it does not know: current occupancy, owner intent, lot assembly, lawful
building envelope, environmental conditions or price. These are listed as
follow-up questions for every lot rather than used to silently drop lots.

## 2. Investigate a lot

[Guide](guides/investigate-a-lot.md) · [live-lot example](../examples/live-lot-trial/README.md).
Give a Bronx address or tax lot number (BBL). The packet cites PLUTO, DOB filings
and HPD records with retrieval receipts, and lists what is missing.

## 3. Model scenarios

Two pieces exist:

- A [rental underwriting model](../src/housing_underwriting/README.md) that
  separates development cost, operations, reserves, debt sizing and funding
  status, citing dated HPD and HDC term sheets.
- A [goal-seeking site search](../src/housing_site_search/README.md) that works
  backward from a target (for example, 60 homes under a rent cap) to the lots
  where that scenario could conditionally fit.

The arithmetic is tested. The inputs are not: land and construction costs, rents,
subsidy terms and thresholds are illustrative. In the retained Jerome case,
raising hard costs by 10% takes conditional matches from 61 to 0. That
sensitivity is the point: the model is only as good as its assumptions.

### Reference case: 730 Stanyan

To learn how professionals actually evaluate a project, we reconstructed a
public San Francisco case from its board memos and budgets:
[Stanyan case study](../research/stanyan-methodology/README.md). It shows how a
budget is compared across stages, how operating subsidy is kept separate from
construction capital, and how source disagreements are carried forward rather
than resolved by fiat. It is a known-case reconstruction, not a blind backtest,
and no expert has reviewed it yet.

## Open questions for practitioners

1. **Assumptions.** Which land, construction, rent and subsidy figures should a
   first-pass Bronx model use, and from what sources?
2. **Screening.** What makes a lot worth a closer look in practice? Which
   discovery filters would you trust, and which would you never apply?
3. **Reference cases.** Are there NYC projects with public, dated budgets
   (HPD or HDC closings, board packets) we could reconstruct and then backtest
   against? Stanyan is our only worked example and it is in San Francisco.
4. **Packet contents.** What would make an evidence packet useful to a
   practitioner, a community board or a nonprofit developer?

## Also in progress

- **Ownership evidence** is now merged: recorded deeds, mortgages and sales with
  parties and amounts for any lot outside Staten Island
  ([module](../src/housing_ownership/README.md)). It flags when the tax-roll owner
  lags the latest deed. Not a title opinion.
- Detailed history of fixes and remaining gaps: [papercut log](reference/papercuts.md).
