# Papercut log

GitHub publication preparation on 12 October 2026: the local checks previously
had no CI entry point for the retained research experiments. `make research-check`
and GitHub Actions now run those checks without live collection or model calls.
The root README now distinguishes executable prototypes, manual calibration and
unverified professional claims. A pattern scan of tracked files and reachable Git
history found no recognizable credentials; that scan is not a comprehensive audit.

The publication clean-checkout test caught an absolute-path dependency in the
frozen retrospective validator. A separate portable validator now binds the exact
recorded input root to the current checkout and checks the same bytes, rubric,
quotes and frozen outputs. Traversal, nested paths and matching basenames outside
the original boundary are rejected. The old code and access log remain unchanged.

Maintain this as work proceeds. A failure should become an executable check where
possible. Keep observations separate from proposed controls. This log records
failures encountered during probe one, not hypothetical advisor feedback.

| Papercut | Observed failure or cost | Cause | Deterministic control and state |
| --- | --- | --- | --- |
| Tool runtime differs from browser JavaScript | URLSearchParams was unavailable in tool orchestration | Assumed a browser global in a minimal JS runtime | Use explicit URL encoding or Python urllib.parse; request definitions are saved |
| Python HTTP dependency absent | requests import failed | Assumed an installed package | Use Python standard library; offline replay requires no third party package |
| Network permission differs from network policy | urllib request failed with Operation not permitted despite unrestricted egress policy | Command sandbox and destination policy are separate | Request only command-level network permission; retain proxy and TLS; replay never needs network |
| Stale source URL | MTA GitHub station URL returned 404 | Unverified repository path | Preserve failed source record; use authoritative MTA CSV; failed sources cannot support observed claims |
| Socrata BBL type mismatch | All initial challenge queries returned 400 | BBL numeric in PLUTO but text in DOB and HPD | Inspect metadata types before creating filters; quoted text queries now saved; negative query results require successful responses |
| Source dictionary vintage mismatch | Generic PLUTO dictionary was 22v1 while parcel data were 26v2 | Stable download URL did not imply current documentation | Mark mismatch; never use it to clear current zoning; metadata and source snapshots retained |
| Numeric rank selects civic facilities | School and police parcels ranked second and third | Capacity and zero recorded homes omitted existing public-service value | Preserve original rank; explicit challenge judgments reject ordinary redevelopment; add civic-use mission lens next |
| No homes is mistaken for no occupants | Lead has historical laundromat, medical and church/hall filings | Residential counts do not measure commercial/community occupancy | Current occupancy and leases stay unknown; no vacancy or availability inference permitted |
| Address alias splits a site | Police parcel uses River Avenue in PLUTO and East 169 Street in DOB | One lot can have multiple street addresses | Match BBL, preserve aliases; require BIN/address cross-check before pipeline clearance |
| Query row counts become project counts | DOB queries contain repeated documents or subsequent filings | Filings and projects have different grains | Label returned rows; no unique-project assertion or sum of proposed units |
| Zoning area becomes gross building area silently | Initial concept calculation used FAR area directly as gross sf | Two area definitions were conflated | Explicit gross_per_zoning_sf assumption and dependency node; legal capacity remains unknown |
| Markdown tables broken by paragraph joining | Blank lines appeared between every table row | Document join routine treated all lines as paragraphs | Remove blank row separators; artifact linter checks contiguous table rows |
| Changed claim kind breaks viewer | Window count became observed; viewer assumed every count had inputs | Renderer assumed one evidence shape | Optional inputs handled; schema and browser parity checks validate the viewer |
| Cached geography can silently mismatch a new mission | Changing station or enlarging radius could reuse old parcel window | DSL scope and collected query were not coupled | Validate station/route, exact bounding window and radius coverage; reject mismatches |
| New validation changed expected test error | Scope test failed after earlier station/route guard was added | Test fixture no longer reached the condition it meant to test | Make fixture valid up to the intended boundary; assert incomplete universe fails closed |
| Browser local navigation restricted | file URL was blocked by browser policy | Browser file access differs from executor access | Render authored HTML with setContent for tests; do not relax destination policies |
| Browser test reused global declarations | Second setContent raised Identifier data already declared | Same document context retained lexical declarations | Use separate page contexts for desktop and mobile |
| Map clipped southern candidates | Initial viewBox cropped several ranked points | Coordinate scale exceeded visible extent | Enlarge plot extent; browser check requires every shortlisted point inside bounds |
| Mobile evidence selector overflows | Long claim option widened the document | Intrinsic control width and grid min-content sizing | Bound select width, use border-box and zero child min-width; browser overflow check passes at 390 px |
| Source refresh can invalidate a review | Mutable source filenames can replace evidence under saved judgments | Live collection and reviewed snapshot share names | Hash check rejects mismatches; commit/cache snapshot before refresh; immutable refresh ledger added as release hardening |
| Releasing output without a hash match | Editing renderer after export invalidates code/output manifest | Save and release were separate informal steps | One release validation command must check source, code, configuration and output hashes; regenerate before release |
| Documentation can drift from parameters | Hardcoded scenario values would survive a changed DSL | Prose and numerical exports had separate inputs | Core numeric prose now rendered from IR/config; linter and sensitivity checks cover selected parameters |

## Engineering priorities

Prefer small named transformations, typed boundaries, fail-closed validation,
immutable evidence snapshots, reproducible builds, and a single source for
quantitative outputs. Do not turn an evidence-quality failure into a lower rank.
Reject the run or preserve an unknown. Keep professional judgments in a separate
review layer and never use a technical pass to imply feasibility approval.

The release gate is technical. The site action gate remains unresolved until
current uses, entitlement, ownership, environmental conditions, development
status, full economics and affordability inputs have been reviewed. The two
advisor dispositions remain pending.

## Source audit — 3 October 2026

76 request receipts and ten source families are recorded in
[the source audit](../research/source-audit/report.md).

| Papercut | Evidence | Deterministic response |
|---|---|---|
| HTTP 200 with Missing Key HTML | Census ACS sample | Separate semantic success from transport success; reject non-JSON API payload |
| HTTP 200 with JSON error | Guessed DEC services | Reject error objects; discover and inspect actual layer names |
| Working GIS service has wrong subject | DEC erm/erm exposes ecological/wetland layers | Do not promote GIS discovery to a verified cleanup source |
| DCP application shells and stale paths | ZAP shell; old agency URLs return 404 | Mark unparsed content; follow official indexes; no invented API contracts |
| Ambiguous tied geocoder confidence | Jerome fallback candidates share 0.8 | Exact address plus independent BBL/parcel corroboration |
| Mixed vintages on one page | HPD 2026 income / 2025 rent headings | Block derived rents pending explicit vintage reconciliation |
| Cross-project agency link | New Utrecht FAQ links Grand Concourse vision report | Validate document project/site identity |
| Record availability mistaken for current title | ACRIS lead returned latest document date 2023 | Preserve coverage dates; require native documents/current title review |
| New policy applicability | HPD 2026 guidance applies from October 1 consultations | Model effective date and project milestone explicitly |
| Proposal criteria mistaken for parcel metrics | HPD RFP threshold/team/finance requirements | Store requirement/evidence matrix and advisor dispositions |

Source audit validator checks retained byte integrity, ten-source cap, references,
structured API error rejection, parcel corroboration, ACRIS joins and feed validity.
Public document interpretation, licensing and professional feasibility remain
explicit review inputs; none are implied by a technical pass.

## Jerome advisor benchmark — 4 October 2026

| Papercut | Evidence or failure mode | Control |
|---|---|---|
| Agency estimates become claimed entitlements | HPD briefing supplies ~48/~60 homes and 175/185 ft | Label agency planning concepts; separate independently unresolved envelope |
| Generic R8A shortcuts ignore applicability | PLUTO MIH flags vs outside-MIH special height branch | Written branch/mapped-boundary reconciliation required; flag is not proof agency is wrong |
| Environmental exception dropped in earlier audit | HPD process p4 includes BCP/hazardous-material E exceptions and noise screening | Corrected audit Page/report; full scoped passage checked in case extraction |
| Correct quote but invented numerical value | A matching table passage could accompany an altered unit count | Numeric regex/currency-column extraction must equal authored value; rejection test |
| Wrong PDF page can appear credible | Whole-document quote search hides wrong locator | Match quotes within exact PDF page; rejection test |
| Reviews survive changed assumptions/interpretation | Earlier build left pending templates bound to older fingerprint | Fingerprint evidence/case/builder; update untouched templates, preserve and reject stale feedback |
| Rebuild erases supplied finance values | Completeness generator could replace filled inputs with nulls | Refuse rebuild when supplied inputs exist; require versioned sourcing |
| Two forms could represent one reviewer | Duplicate names across A/B slots | Separate slots and case-insensitive identity comparison; owner verifies attribution |
| Empty E query treated as clearance | Zero exact-BBL rows for 1337 Jerome | Environmental claim remains unknown; zero never satisfies professional gate |
| Program rent framework copied to co-op | Original probe's rental economics do not fit Open Door | Separate project sources/uses, buyer mortgage access, maintenance/reserves and resale rules |
| Timeline precision exceeds evidence | Webpage Fall 2026 vs briefing before year-end | Preserve both planning statements; final RFP controls binding deadlines |

The packet has 70 typed claims, 12 unresolved professional requirements, exact
source passage/field traces, pending independent A/B review forms and 13 rejection
and acceptance tests. Technical advisor-packet release passes; workflow acceptance,
agency proposal and development recommendation remain blocked pending evidence.

## Retrospective case search — 4 October 2026

| Papercut | Evidence | Control |
|---|---|---|
| Archive page appears empty | HPD designated-project records are loaded by rfp-filter.js from a CSV | Follow the official script/data provenance; do not interpret shell text as absence of records |
| Search results ignore query detail | Bing returned generic first-term results for specific case queries | Treat discovery as unreliable; use agency archive/documents for substantive claims |
| Printed issue date hides later PDF export | 351 Powers RFP printed August 2022, PDF creation/modification April 2024 | Reject strict date promotion until version reconciled; test metadata boundary |
| ZIP migration dates confuse document dates | 97 West 169 ZIP members dated 2021; PDF metadata 2018–2019 | Preserve packaging, printed issue and PDF metadata dates separately; no historical-byte certification |
| No archive result overinterpreted | Two specific Internet Archive URL checks returned no snapshot | Record the exact checked variants; do not assert no archival evidence exists anywhere |
| Known document exceeds collection cap | Powers RFP/CVR exceed 12 MiB | Retain failed attempts; explicit 64 MiB/two-worker exception with receipts |
| Original RFP disagrees on parcel ID | 97 West 169 p8 Block 2519 vs p9 Block 2509 | Flag contradiction; addendum evidence supports follow-up; do not silently fuse wrong parcel |
| Case finder already saw answers | Discovery archive and selection summaries disclose later outcomes | Fresh analyst context, input-only packet and allowlist; no claim of zero model prior knowledge |
| Agency summary confused with full proposal | Reference is a designation press release | Label missing submitted proposal/underwriting; test documentary reasoning separately from utility |
| Large binary discovery duplicates bloat Git | Alternative archives and later re-export PDFs | Keep receipts/metadata and selected input PDFs in Git; document local-only raw retention |

Recommended document exercise: 97 West 169th Street, with April 4, 2019 cutoff.
No experiment, expert assessment, time-savings estimate or construction-outcome
finding has been performed. Document integrity passes; strict historical replay
remains unverified.

## First retrospective assessment — 5 October 2026

| Papercut | Observed evidence | Control or next engineering change |
|---|---|---|
| Strong site narrative misses applicant eligibility | Frozen 97 West 169 assessment omitted RFP pp17–19 threshold framework and 60-unit/seven-year experience requirements | Add explicit applicant/submission pass/unknown/fail gates before claims of pursuit readiness; unknown credentials require evidence |
| Traceable quotes are mistaken for completeness | 24 claims and 82 exact-page quotes pass, but material team requirements are absent | Keep provenance validation separate from requirement coverage and professional utility; report omission rather than approve workflow |
| Evaluator has incorrect page locator | Precommitted rubric named Addendum2 p3 for contours; actual p2 | Preserve rubric hash; separate locator erratum; no post-output criterion change |
| Later reference invites answer matching | Agency selection announces 100 homes and specific health center | Freeze output before reveal; no score for unit/tenant/developer match; distinguish RFP requirements from independent discovery |
| Fresh context overclaimed as secure blinding | Analyst declares only input reads and no recalled outcome | Label instruction boundary, not OS sandbox; record curator exposure and model-prior limitation |
| Detailed provenance adds latency | Approximately 14-minute dispatched-to-freeze run, no human baseline | Bound first-pass scope and record run duration; no time-saved claim; future structured extraction and coverage checks |
| Available graphics left unreviewed | Analyst did not visually inspect addendum maps | Keep geometry and measured elevations unknown; require separate visual/map reconciliation before spatial conclusions |

The original analyst output is frozen at commit ae56d78. Evaluation records one
material missed criterion (applicant/submission review); no aggregate success score,
practitioner usefulness, professional approval or historical certification is claimed.

## Applicant gate transfer — 5 October 2026

| Papercut | Observed source or test | Engineering response |
|---|---|---|
| Universal threshold copied between projects | 97 West 169 requires 60 units; St Ann’s base criterion 70 | Bind parameters to exact case/document passage; reject source-value mismatch |
| Mechanical cutoff erases agency review route | St Ann’s Add1 p3 permits development experience justification | Preserve base fail separately; effective unknown pending agency review, no automatic approval |
| Development flexibility spreads to management | St Ann’s Add2 p3 explicitly rejects management flexibility/future credentials | Separate gates and authority passages; current-at-submission evidence required |
| Projects summed into a qualifying single project | Two 30-unit development fixtures vs one-project requirement | Existential witness per qualifying development project; no arbitrary sum |
| Management count treated as same one-project rule | Management concerns qualifying unit portfolio, not necessarily one building | Require reviewed unique-unit portfolio scope; duplicate-unit reconciliation remains evidence task |
| PDF table labels break phrase matching | 97 RFP p19 puts “Experience” between count and “residential units” in layout text | Retain original text; explicit scoped regex accepts documented interleaving; ambiguity rejects |
| Empty history is called ineligible | No actual applicant records supplied | Unknown unless complete evidence scope is reviewed and bound to exact record set |
| Review survives rule/fact/source changes | Mutation tests change evidence, facts or case assumptions | Bind reviews to payload/source and requirement+engine+schema+release-policy fingerprints |
| Caller invents ready flag | Injected submission_readiness_claim_allowed=true in profile | Export recomputes; no trust in caller-supplied readiness status |
| Synthetic fixture masquerades as credentials | Relabeled actual profile and removed synthetic flag | Check fixture path/content and block actual promotion; passing test records remain synthetic |
| Rule matching is mistaken for complete proposal readiness | All scoped synthetic gates pass, unexpanded full submission inventory | Separate coverage and actual-evidence blockers; evidence pack permitted, readiness claim exit 2 |
| Curated regression overclaimed as holdout analyst improvement | Curator previously saw second-case summary; manually authored gate inventory | Explicitly label source-driven transfer; no independent holdout, expert utility or automatic extraction claim |

22 gates / 31 source-page citations / seven PDFs / 26 tests. No real applicant
credentials, professional acceptance or certified historical replay were supplied.
The original assessment and its fingerprints remain unchanged.

## Requirement coverage — 6 October 2026

| Papercut | Observed evidence | Engineering response |
| --- | --- | --- |
| Obsolete form erases a live evidence obligation | West 169 Add3 p2 removes E4 format but retains commercial experience evidence | Separate artifact replacement from underlying conditional obligation |
| No experience treated as no form | St Ann’s RFP p23 requires forms marked “None” | Keep required form presence independent of applicant experience |
| Certification timing suppresses submission narrative | St Ann’s Add2 Q14 defers certificate; submission explains sustainability | Bind phase per obligation; retain softer requested material separately |
| Optional prefix lost at checkbox boundary | Optional staffing text precedes checkbox in the same block | Carry prefix context until next tab; regression test |
| Generic module names collide | Eligibility check import shadowed coverage/check modules | Rename coverage modules explicitly; verify CLI behavior |
| Source segments mistaken for atomic requirements | 150 segments include nested clauses and question start anchors | Publish bounded scanner scope; keep all semantic review pending |
| Accepted review copied between forms | Synthetic E1 acceptance could be reused for G without requirement binding | Bind artifact review to requirement ID and exact payload |
| False applicability silently waives required evidence | Unreviewed facts or facts without retained proof | Require scoped review and hash-checked applicability evidence |
| Global review queue confuses case release | Combined library contains two case inventories | Publish case-specific queues; global integrity still checked |
| Workbook presence mistaken for compliance | Minimal synthetic workbook passes container test | Separate container check from template and substantive review |
| Regression success mistaken for empirical improvement | Curated map and eleven known faults | Pin inventory before controls; no fresh holdout or utility claim |

27 coverage tests and deterministic replay pass. No actual proposal packet or
independent semantic review was supplied. Original analyst and eligibility artifacts
remain unchanged; the joined export delegates the old generic coverage placeholder
to this component while retaining eligibility blockers.

## One conclusion end to end — 7 October 2026

| Papercut | Observed behavior | Engineering response |
| --- | --- | --- |
| BBL strings contain decimal formatting | Synthetic mutation initially could not locate PLUTO's BBL with literal string equality | Reuse explicit BBL normalization; require unique fixed-site match |
| Environmental flags are actual Booleans | Numeric equality logic initially rejected true air/noise flags | Preserve Boolean facts; reject Boolean numerical assumptions separately |
| Hash checks alone do not describe semantic impact | A properly receipted revision can change the analysis basis | Show dependent claim changes and stale judgment fingerprint; preserve old snapshot |
| Failed-status receipt can bypass a successful-source hash branch | Controlled failed-status variant | Require successful status and matching digest for all four decisive source inputs |
| New receipt could masquerade as a real refresh | Synthetic revision with updated content hash | Require explicit synthetic lineage in this probe; reject actual relabeling |
| Different vintage treated as direct contradiction | Synthetic competing unit records with 26v2 versus 25v1 | Separate temporal reconciliation from same-context conflicting values; neither clears facts |
| Caller deletes a requirement and its graph edge | Occupancy/finance omission controls | Check independently pinned authored inventory, including graph reachability; no automatic unknown-requirement discovery claim |
| Model finance improvement overstates site readiness | $140/sf control closes modeled additional debt-support gap | Keep occupancy and all professional checks unknown; design/acquisition export exits 2 |
| Changed assumptions retain an old filename locator | A copied config differs from repository probe.json | Bind assumptions to the embedded config and its fingerprint |
| Self-replay mistaken for unfamiliar review | Clean extraction is performed by the same author | Publish reproduction/challenge protocol and pending reviewer form; independent human test remains open |

The experiment uses one fixed site, four source families and a 73-claim dependency
closure. Eleven precommitted cases include baseline and ten known controls; all
expected responses are observed. These counts establish scoped software behavior,
not completeness, site-selection quality, feasibility or practitioner utility.
Contradiction handling requires already-linked structured assertions. Exact quotes
and reproducibility still do not prove semantic entailment or professional judgment.

## Fresh agent assumptions review and real-project reference — 7 October 2026

| Papercut | Actual evidence | Response |
| --- | --- | --- |
| Selected passages omit a real housing signal | Cached DOB row 7 reports nine proposed units in a 2003 filing, signed off 2004 | Record as heterogeneous historical evidence; reconcile job/CO/use history without replacing PLUTO zero |
| Graph connection mistaken for a decision influence | Occupancy-first policy remains fixed when finance changes | Compare action cost/time/stop conditions; distinguish dependencies from an evaluated priority policy |
| Additional capital displayed without baseline contribution | Baseline non-debt $45.965m plus extra $45.651m | Expose $91.616m modeled total non-debt need; no full finance-closure interpretation |
| Same project has changing plan counts | 425 Grand Concourse 241 at selection, 277 at opening | Compare dated stages; do not reward matching delivered counts |
| Cost figures appear contradictory | NYSERDA Project Cost $121.943m vs HDC development $178m | Reconcile cost scope/dollar year before grading or calibration |
| Case endpoint returns login shell with HTTP 200 | ULI Knowledge Finder redirect/sign-in content | Mark no substantive case retrieval; do not promote finance table from shell |
| Public PDF retrieval fails | Government-hosted ULI mirror returns 403 | Retain failure; complete verified sources-and-uses remains unknown |
| AI replay counted as independent professional review | Fresh-context AI performs replay and critique in shared environment | Separate useful agent criticism from pending unfamiliar-human/professional acceptance |

Original experiment and known-control results are preserved. New primary references
are later reveal/calibration material, not historical analyst inputs. No new blind
backtest, private underwriting reconstruction or practitioner acceptance occurred.

## 425 Grand Concourse calibration on 7 October 2026

| Papercut | Observed failure or cost | Deterministic control and state |
| --- | --- | --- |
| Reference exposure undermines independence | Known outcomes were re-read before the early assessment commit | Explicit protocol deviation; this run is calibration only. Next withheld-case execution needs separate input and reference access. Git alone cannot prevent cognitive leakage. |
| PDF extraction emits an optional-content syntax warning | Addendum PDF still produced text, but warning could indicate missing visual content | Original PDF retained; text quotes checked. Image/map coverage and complete visual review remain pending. |
| PDF line-wrap hyphen changes quote matching | A selected east-west quotation failed exact normalized resolution | Shortened to an intact exact passage; validator rejects unresolved quotations rather than silently rewriting text. |
| Word and numeral disagree | RFP says thirty (35) years | Preserve contradictory literal wording and require clarification; never silently choose a value. |
| Same report has conflicting approximate areas | CPC reports 275,711 and 275,771 sf; use areas sum to 276,071 sf | Preserve source versions and scope; no fit or cost denominator clearance from these figures. |
| Outcome appears to violate base mix rule | Opening studio share is 16.25%; base cap is 15% | Exception-aware check returns needs-program-evidence. Approved final program is still missing. |
| Financial costs have unreconciled scope | HDC reports $178m; NYSERDA labels $121.943m Project Cost | Scope, price year and area definition required for comparison. Missing terms cannot generate an accuracy score. |
| Manual assessment can pass integrity while incomplete | 29 selected early claims do not audit all 157 RFP pages and forms | Explicit selected-claim scope; professional coverage acceptance remains pending. No automatic completeness pass. |
| Page attachment size ceiling | Complete calibration ZIP was 10,836,363 bytes, exceeding the 10 MiB upload limit | Split into source-PDF and analysis archives, each below the limit; combined extraction independently validates. |

## First integrated workflow on 28 October 2026

| Papercut | Observed failure or cost | Control and remaining boundary |
| --- | --- | --- |
| Repo entry point did not match an external user's expectations | An external tester reported trying the repo without getting it to work | One entry skill and `python -m housing_workflow demo --out runs/first-demo`, with a real-source example and explicit instructions to open local HTML. An external successful retry remains untested. |
| Workflow coverage was easy to confuse with a complete process | Earlier prototypes exposed many separate components | Versioned discrete workflow declares partial process status and uncovered stages in every IR/packet. This does not discover all missing professional steps. |
| Original housing signal was omitted | Historical proposed dwelling units were missed in earlier research | New model preserves every selected source field and surfaces all positive historical unit signals; actual live replay includes the nine-unit field without equating it to present housing. |
| Source address spelling differs | Initial 1337 Jerome Avenue lookup returned zero after normalizing AVENUE to AVE | Resolver queries explicit original/contracted/expanded forms and requires a unique result. Broader alias and address-history support remains absent; request BBL on ambiguity. |
| CSV line endings broke deterministic export verification | csv.writer used CRLF while read_text normalized it | Explicit LF line endings; byte-identical offline replay test passes. |
| Re-serializing an unchanged request changed model bindings | Request whitespace changed its SHA and downstream prompt hash | Exact request bytes are copied on unchanged replay; changed assumptions create a new request and model binding. |
| A documentation file accidentally entered a sample packet inventory | A README inside the run directory was not part of replay inputs | Example guide moved outside generated run packages; manifest/replay inventories now match. |
| Professional model depth remains thin | Current arithmetic is a user-stated area budget, not a design or underwriting model | Formula/dependency CSV and typed IR expose the limitation; legal/physical/finance stages remain unknown, and image output is restricted to a diagram brief. |

## Modular photo-concept slice

| Papercut | Observed failure or cost | Control and remaining boundary |
| --- | --- | --- |
| Attractive image had no model-to-prompt link | Earlier photo edit used manually chosen six-story/program/style instructions outside the executable workflow | Canonical scene/scenario → compiled prompt → actual invocation → image/review receipt. The new visual parameters remain explicit assumptions. |
| Global skill hashes coupled unrelated modules | Adding a rendering skill would stale every parcel packet | Parcel implementation bindings now follow only its own declared workflow skills. Renderer binds its own package/workflow/skills. Isolated-install and unrelated-skill tests pass. |
| Source screenshot unavailable as local bytes | Image tool can see the chat attachment, but no original source file exists in the workspace | External conversation reference is explicit and source byte binding is false. Local photo inputs are copied and hashed. The example cannot claim fully source-byte-reproducible conditioning. |
| Prior concepts also entered image context | Original photo required including three recent conversation images | Actual selector recorded; original-only conditioning is not independently verified. No assertion of source-pixel fidelity. |
| JSON key order changed compiled binding lists | Saving canonical inputs sorted keys and initial verify differed from preparation | Compile parameter bindings in sorted order; brief recomputation is deterministic. |
| Six-story caption could masquerade as a floor-count test | Recessed top is partly cropped in the generated example | Visual review leaves exact story count and geometry unverified. Caption presence is assessed separately. |
| Reusing an output could erase the experiment | A second attach could otherwise overwrite the first illustration | Existing generation is immutable through CLI; create a new run for revisions. |
