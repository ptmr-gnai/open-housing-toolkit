# Next steps

The working to-do list between sessions. Newest decisions first in each item; move an
item to [status](status.md) or the [papercut log](reference/papercuts.md) when it lands.
Last updated November 16, 2026, after the first packet went to Jeremy Ney.

## Priorities

1. **Backtest research: what got built, and from what.**
   A first prototype exists on branch `claude/dreamy-neumann-b4ee51` (commit `06994bf`,
   `research/backtest-built-projects/`): 33 typed Bronx lots, a Bronx-wide replay of
   today's screen, and a validator. Not merged or pushed. Next: review it, merge it,
   then widen it: pre-development lot conditions (archived PLUTO), sale before
   development, permits timeline, proposed vs. built units, program, and whether
   the screen would have ranked each lot. 57 East Burnside is case #1.

2. **Subsidy finder.**
   For a lot and program, what could it qualify for: federal (LIHTC 4% / 9%, HOME,
   HUD programs), state (NYS HCR programs), city (HPD term sheets, HDC bonds, 485-x,
   467-m, Mandatory Inclusionary / City of Yes affordability options). Encode the
   eligibility rules with sources. Apply it as a vector across the report: sources in
   the budget, the gap it could close, and the "why do this" case. Developer persona
   first; agencies care too.

3. **Equity, environmental and economic impact.**
   What a project could bring, not just what it costs: affordability and
   displacement risk (existing tenants and businesses, fair-housing opportunity
   areas), environmental conditions (E-designations, transit access, energy), and
   economic effects (retail kept or added, jobs, local business). A new report
   section once the inputs exist.

## Open threads

- **Feedback from Jeremy's contacts.** Turn answers into a rubric (what good looks
  like); record which workflow steps practitioners actually use.
- **Picture floor count.** The image model often draws one floor too few. Ideas:
  number the floors in the 3D massing view; camera-registered references from the
  Street View URL. Correction pass and `--accept-issue` already exist.
- **Occupied vs. cleared sites.** Show existing businesses and tenants as a signal
  in the shortlist; persona priorities (near transit, avoid displacing a grocery).
- **Pinned lot-evidence module.** Its DOB NOW source (`w9ak-ipjd`) currently
  publishes Brooklyn only and it never queries approved permits (`rbx6-tga4`); needs a
  versioned update. Also the geometry runbook's broken spec link and the render
  module's leftover "white-and-blue" prompt text (both pinned).
- **Report summary.** Decide whether the executive summary should keep leading with
  homes and gross area.
- **Cold-test isolation.** A separate HOME was not enough: Codex fell back to the
  real checkout. Use a separate macOS user or a sandbox for clean-room tests.
- **Later:** hosted interface for non-technical users, opt-in run traces for
  improvement, local inference.
