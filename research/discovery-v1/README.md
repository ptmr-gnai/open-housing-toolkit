# Discovery v1: auto and parking sites

Zero existing homes is compatible with rezoning for housing. This experiment
implements Jeremy's area-search question: find nonresidential lots worth a closer
look, preserve why each was selected, then investigate the strongest candidates.

The [case study](report.md) records live November 9, 2026 probes in two Bronx
windows, the first screen's mistakes, corrected auto-use selection, assumption
sensitivity and three deeper public-record investigations. These are exploratory
case studies, not forecasts or practitioner-accepted site recommendations.

- [Module and commands](../../src/housing_discovery/README.md)
- [Discovery skill](../../skills/discover-housing-sites/SKILL.md)
- [Jerome auto/parking shortlist](cases/jerome-deep/handoff/screen/packet.md)
- [Hunts Point auto/parking shortlist](cases/hunts-deep/handoff/screen/packet.md)
- [FAR sensitivity](cases/far-sensitivity.json)
- [Machine-readable findings](cases/findings.json)

Run `python research/discovery-v1/validate.py` for read-only offline verification.
The retained packages include raw source bytes and queries. To change a scenario,
screen the retained inventory into a **new runs/** directory; never rebuild these
cases in place. Each deep case contains the focus under `handoff/screen`, its
broader parent screen under `handoff/screen/parent`, and the primary inventory under
`handoff/screen/parent/evidence`. The FAR-8 case retains its own identical copy of
the Jerome inventory. Comparisons require that exact evidence identity.

`iterations/` preserves the first source implementation and selected findings,
including its errors. It is historical research, not an active module or verified
current shortlist. Intermediate local runs remain under ignored runs/.

Code MIT; original prose CC BY 4.0. Public source snapshots retain publisher terms;
see [DATA-LICENSES](../../DATA-LICENSES.md). No images were generated or published.
