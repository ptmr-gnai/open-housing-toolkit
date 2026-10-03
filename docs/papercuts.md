# Papercut log

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
