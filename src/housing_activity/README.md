# Development-activity check

Before studying a candidate, check whether it is already being built. For a set of
NYC tax lots (an area search's candidates, or named BBLs), this module collects
recent records from four public datasets and classifies each lot:

| Status | Meaning |
| --- | --- |
| `active_development` | Full demolition, foundation, earth-work or excavation-support permit; a permit whose description names a new building; a new-building filing; or an HPD new-construction start, within the window |
| `site_preparation` | Only a construction-fence permit within the window |
| `none_found` | Nothing qualifying returned; not proof nothing is planned |
| `not_checked` | A source failed; the run is `partial` |

Sources ([sources.json](sources.json)): DOB NOW Approved Permits (`rbx6-tga4`),
DOB NOW Job Application Filings (`w9ak-ipjd`), legacy DOB Permit Issuance
(`ipu4-2q9a`) and HPD Affordable Housing Production (`hg8x-zxpr`). Each run also
counts each source's rows per borough and reports a source with none as a coverage
gap rather than treating its silence as "nothing found".

```sh
python -m housing_activity collect --discovery runs/NAME/discovery --out runs/NAME/activity
python -m housing_activity verify --run runs/NAME/activity
```

Every response is kept with a SHA-256 receipt; `verify` recomputes the
classification from them. The shortlist (`scripts/plan_lot.py shortlist --activity`)
lists active lots separately, and the feasibility report (`--activity`) shows the
check in its search block, the selected lot's permits in the Site section, and
active development as the first open item. Standard library only.

Why it exists: on November 16, 2026 a dry run selected 57 East Burnside Avenue, a
"one-story store" in PLUTO. A Street View image showed a fenced, cleared lot; DOB
NOW permits showed demolition signed off in May 2026 and excavation permitted in
September 2026. The existing lot research did not catch it because its DOB NOW
source holds Brooklyn rows only.
