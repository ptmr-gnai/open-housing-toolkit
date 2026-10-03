# Bronx housing raw materials: ten-source audit

Audited 3 October 2026. This is a source-readiness inventory and a small reconstruction of agency practice. It is not a feasibility study or an expert endorsement. Ten source families are listed; each can host many datasets. ACRIS uses NYC Open Data for its structured interface, so these are not ten independent API infrastructures.

## What the professional workflow requires

The goal is an open, reproducible path from a housing question to a reviewable opportunity brief: why this site, who benefits, what can be built, which approvals are needed, what it costs, and what evidence is still missing. A professional workflow includes data, program rules, legal documents, team qualifications, community priorities, drawings, financial assumptions, investigations and agency review.

We grounded the inventory in HPD's actual New Utrecht Library and Affordable Housing RFP pre-submission briefing, HPD's July 2026 design review process, its financing term sheets, the December 2025 CEQR framework, DCP's ULURP flowchart and Furman Center's established data products. These sources describe actual requirements; they do not prove that every agency analyst follows one identical workflow.

## Hardened shortlist

“Verified” means the stated request or download worked in this audit. It does not imply that every dataset, field, geographic region or authenticated interface has been verified.

| Source family | Raw materials and purpose | Tested access and limits |
|---|---|---|
| [NYC Open Data / Socrata](https://dev.socrata.com/docs/queries/) | PLUTO; DOB BIS/NOW; HPD violations and affordable production; E-designations; DOF sales. | **Queryable API.** No credential required for tested bounded query; app tokens/rate limits matter at scale. |
| [NYC DCP zoning and land-use resources](https://www.nyc.gov/assets/planning/download/pdf/applicants/applicant-portal/lur.pdf) | Zoning Resolution, special districts, ZoLa, ZAP, ULURP. | **Legal text + browser applications.** Public legal text verified; ZAP returned an application shell. No public ZAP API verified. |
| [DCP GeoSearch / Geosupport](https://geosearch.planninglabs.nyc/v2/search?text=1337%20JEROME%20AVENUE%20BRONX) | Address normalization and BBL/BIN resolution. | **Queryable API.** No credential required for tested search. Dedicated API documentation links attempted were unavailable. |
| [NYC DOF ACRIS](https://www.nyc.gov/site/finance/property/acris.page) | Deeds, mortgages, recorded instruments, parcel/document join. | **Records portal + Socrata API.** 48 lead-parcel legal rows joined to 48 master rows. Native images not retrieved. API transport is source 1. |
| [HPD / HDC development resources](https://www.nyc.gov/assets/hpd/downloads/pdfs/services/new-utrecht-rfp-pre-submission-conference-07012026.pdf) | Program term sheets, affordability, underwriting assumptions, design workbooks, RFP criteria, community vision. | **PDFs + XLSX + RFP pages.** Public documents and actual design workbook downloaded; no general underwriting API verified. |
| [MTA developer resources / NY State Open Data](https://www.mta.info/developers) | Stations, scheduled service, transfers, real-time feeds, performance data. | **GTFS download + Socrata API.** Public schedule ZIP and station API returned data. Bus Time account/key requirement documented; real-time not tested. |
| [US Census ACS / LEHD LODES](https://www.census.gov/data/developers/data-sets/acs-5year.html) | Households, rent burden, income, tenure; workplace/residence jobs and OD flows. | **Credentialed API + public bulk CSV.** ACS request returned HTTP 200 Missing Key HTML. NY 2023 workplace CSV gzip downloaded and parsed. |
| [HUD User income limits / FMR](https://www.huduser.gov/portal/dataset/fmr-api.html) | Official income limits, fair-market rents, geographic and program benchmarks. | **Credentialed API + published tables.** API registration and bearer token documented. Unauthenticated request returned 401; tables page accessible. |
| [NYS DEC GIS / cleanup resources](https://dec.ny.gov/environmental-protection/site-cleanup/brownfield-and-state-superfund-programs) | Environmental GIS discovery; brownfield/superfund process and records. Supplement NYC OER E-designation obligations. | **ArcGIS REST discovery + agency documents.** REST catalog and a GIS layer catalog returned valid JSON. Guessed cleanup endpoint failed; no remediation-site query verified. |
| [NYU Furman Center CoreData NYC](https://www.furmancenter.org/data-tools-resources/data-tools-core-data-dictionary/) | Existing industry data fusion: neighborhood indicators and subsidized-housing context. | **Published dictionary + XLSX download.** Dictionary read and 2026-05-05 neighborhood indicators workbook downloaded. No public API verified. |

## Integration contracts

### NYC Open Data / Socrata

Join keys: BBL, BIN; dataset-specific identifiers.

Entry point: `https://data.cityofnewyork.us/resource/{dataset_id}.json`. [Retained request URL](https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2028710002&%24limit=1).

Dataset coverage, dates and metadata must be checked separately. Production records are program activity, not all housing or necessarily completions.

### NYC DCP zoning and land-use resources

Join keys: BBL, district, zoning section, project ID.

Entry point: `https://zr.planning.nyc.gov/`. [Retained request URL](https://zr.planning.nyc.gov/article-xiv/chapter-1).

PLUTO FAR is a screening attribute, not an entitlement calculation. Resolve applicable text, geometry, effective dates and approvals.

### DCP GeoSearch / Geosupport

Join keys: Address, BBL, BIN, coordinates.

Entry point: `https://geosearch.planninglabs.nyc/v2/search?text={address}`. [Retained request URL](https://geosearch.planninglabs.nyc/v2/search?text=1240%20EDWARD%20L%20GRANT%20HWY%20BRONX).

Fallback matches and duplicate confidence scores require exact address and independent parcel checks; PAD and PLUTO versions differ.

### NYC DOF ACRIS

Join keys: Borough + block + lot -> document_id -> master/parties/images.

Entry point: `https://data.cityofnewyork.us/resource/8h5j-fqxa.json ; bnx9-e6tj.json`. [Retained request URL](https://data.cityofnewyork.us/resource/bnx9-e6tj.json?%24where=document_id+in+%28%272006071400444001%27%2C%272006071400444002%27%2C%272006071400444003%27%2C%272006071400444004%27%2C%272006071400444005%27%2C%272010122900666007%27%2C%272010122900666008%27%2C%272011102100750001%27%2C%272011102100750002%27%2C%272011102100750003%27%2C%272011102100750004%27%2C%272011102100750005%27%2C%272011111800148001%27%2C%272011111800262001%27%2C%272016080200145001%27%2C%272016080200145002%27%2C%272020121500488001%27%2C%272020121500488003%27%2C%272020121500488004%27%2C%272020121500488005%27%2C%272020121500488006%27%2C%272022020200871002%27%2C%272022020200871003%27%2C%272022020200871004%27%2C%272022020200871005%27%2C%272023032000888002%27%2C%272023032000888003%27%2C%272023032000888004%27%2C%27FT_2020007459302%27%2C%27FT_2030000780903%27%2C%27FT_2030007459103%27%2C%27FT_2090005518809%27%2C%27FT_2120007459312%27%2C%27FT_2160000763816%27%2C%27FT_2190005518819%27%2C%27FT_2230000780323%27%2C%27FT_2250005351025%27%2C%27FT_2350005350635%27%2C%27FT_2530007459253%27%2C%27FT_2540006421254%27%2C%27FT_2560000783156%27%2C%27FT_2570000783157%27%2C%27FT_2620000780962%27%2C%27FT_2700007509370%27%2C%27FT_2750006152475%27%2C%27FT_2760005200476%27%2C%27FT_2890005518189%27%2C%27FT_2940007459194%27%29&%24limit=1000).

NYC borough coverage excludes Staten Island; records from 1966 onward. Mixed good-through dates; retrieved latest document was 2023. Not a current title opinion.

### HPD / HDC development resources

Join keys: Program/version, site/BBL, household size, AMI/year, review milestone.

Entry point: `https://www.nyc.gov/site/hpd/services-and-information/term-sheets.page`. [Retained request URL](https://www.nyc.gov/assets/hpd/downloads/excel/NC-design-guidelines-workbook.xlsx).

Apply correct program and effective date, superseding addenda and agency assumptions. Design guidance is not a loan award or substitute for codes.

### MTA developer resources / NY State Open Data

Join keys: Stop/station ID, route/trip ID, service calendar.

Entry point: `https://rrgtfsfeeds.s3.amazonaws.com/gtfs_subway.zip`. [Retained request URL](https://rrgtfsfeeds.s3.amazonaws.com/gtfs_subway.zip).

Station distance is not door-to-door access. Respect feed validity, transfers, walking, accessibility, cancellations and service reliability.

### US Census ACS / LEHD LODES

Join keys: County/tract/block GEOID, year, ACS estimate + MOE.

Entry point: `https://api.census.gov/data/{year}/acs/acs5 ; https://lehd.ces.census.gov/data/lodes/LODES8/`. [Retained request URL](https://lehd.ces.census.gov/data/lodes/LODES8/ny/wac/ny_wac_S000_JT00_2023.csv.gz).

ACS sampling error and geography vintages; LODES jobs are not unique workers, coverage excludes some work, time lag. Borough-wide statistics cannot identify parcel occupants.

### HUD User income limits / FMR

Join keys: HUD area/entity ID, year, family/unit size.

Entry point: `https://www.huduser.gov/hudapi/public/fmr`. [Retained request URL](https://www.huduser.gov/portal/datasets/il.html).

FMR is not achievable rent, HPD restricted rent or project revenue. Match year, area, program and utility allowance; authenticated response not verified.

### NYS DEC GIS / cleanup resources

Join keys: Site/program ID, geometry, coordinates; BBL for NYC E-designations.

Entry point: `https://gisservices.dec.ny.gov/arcgis/rest/services?f=pjson`. [Retained request URL](https://gisservices.dec.ny.gov/arcgis/rest/services?f=pjson).

The discovered erm/erm service contains ecological/wetland layers, not cleanup sites. An empty map is never clearance. Need Phase I/II, noise/air and OER review as applicable.

### NYU Furman Center CoreData NYC

Join keys: Geography/type/year; building identifiers where provided.

Entry point: `https://www.furmancenter.org/data-tool/coredata-nyc/`. [Retained request URL](https://www.furmancenter.org/files/CoreData/Neighorhood_Indicators_CoreDataDownload_2026-05-05.xlsx).

Indicators vary in source/vintage. Subsidized-housing database generally multifamily and excludes expired subsidies. Use upstream sources for parcel/legal authority.

## Probe grounded in industry work

**A Bronx agency case, rather than an invented opportunity.** HPD's 1337 Jerome Avenue project page describes a 6,516-square-foot site, a vacant former City pest-control building, affordable homeownership through Open Door, community amenities, R8A with C2-4 in the Jerome Special District, and a possible rezoning. Its published phase is community visioning; an RFP is planned for Fall 2026. We have not treated it as an issued RFP or an unclaimed site.

GeoSearch returned an exact address candidate with BBL 2028560051 and BIN 2008295. PLUTO independently returned that address, 6,516-square-foot lot area, R8A/C2-4/J and an HPD owner label. The checks agree on parcel identity and agency-described lot/zoning attributes. PLUTO's owner label does not establish legal site control. Both GeoSearch and competing results had fallback confidence 0.8, so confidence alone would have selected ambiguously.

**A real proposal evaluation.** The New Utrecht July 1, 2026 agency briefing separates threshold criteria from competitive review. Thresholds include complete forms and requested documents, a specified equitable-ownership requirement, 100% affordable housing and compliance with project parameters. It then asks for community responsiveness, design, zoning assumptions, financing and operating assumptions, team experience, job outreach and continued library service. Its library-specific conditions must not be copied to the Bronx. The submission date has passed; this is a workflow reference. The briefing does not replace the RFP and later addenda, which were identified but not fully downloaded or reconciled.

**A design submission contract.** HPD's current process guide has workbook/waiver submission, design consultation, review pathway determination and later reviews. The 2026 guidance applies to projects submitted for Design Consultation on or after October 1, 2026. We downloaded and parsed the real XLSX workbook's sheet structure. The guide says all projects require a Phase I Environmental Site Assessment, regardless of review pathway. A public map cannot supply that investigation.

**Reproducible transit and employment inputs.** The MTA ZIP parsed as GTFS and contains station 412, 170 St. The feed declares validity May 26–October 31, 2026. We parsed all 108,030 rows of New York's 2023 LODES all-jobs workplace file; 3,435 Bronx workplace blocks sum to 340,785 jobs. That is a data plumbing check, not a current employment estimate, a count of employed residents, or a travel-time accessibility result. Travel-time routing and an econometric estimate were not performed.

**Title-record plumbing.** For the original lead parcel at 1240 Edward L Grant Highway, 48 ACRIS legal records joined one-to-one by document identifier to 48 master records. The latest returned document date was February 10, 2023, and good-through dates vary. Native document images, title exceptions, parties and present site control remain unverified.

## Agency and research references to read first

- [HPD: 1337 Jerome Avenue](https://www.nyc.gov/site/hpd/services-and-information/1337-jerome-ave-affordable-homeownership-rfp.page) — Bronx case; public purpose, program, zoning, community process and status.
- [HPD: New Utrecht RFP pre-submission briefing](https://www.nyc.gov/assets/hpd/downloads/pdfs/services/new-utrecht-rfp-pre-submission-conference-07012026.pdf) — Pages/slides 18–25: threshold criteria, appendices, team, drawings, financial assumptions and submission requirements.
- [HPD: New Construction Design Review Process, July 2026](https://www.nyc.gov/assets/hpd/downloads/pdfs/services/new-construction-design-review-process-guide.pdf) — Milestones, review pathways, evidence requirements and applicability.
- [HPD: New Construction Design Guidelines Workbook](https://www.nyc.gov/assets/hpd/downloads/excel/NC-design-guidelines-workbook.xlsx) — Actual structured submission material; downloaded and XML sheet structure checked.
- [HPD: NCF term sheet, July 2025](https://www.nyc.gov/assets/hpd/downloads/pdfs/services/hpd-ncf-term-sheet.pdf) — Example rental-program finance/eligibility requirements; not the Jerome homeownership program.
- [HPD: program term-sheet index](https://www.nyc.gov/site/hpd/services-and-information/term-sheets.page) — Select the applicable program, including Open Door for the published Jerome case.
- [HDC: Develop Affordable Housing](https://www.nychdc.com/develop) — HDC financing and linked term sheets; filename and hosting date alone do not establish effective date.
- [NYC OEC: CEQR Analysis Framework, December 2025](https://www.nyc.gov/assets/oec/technical-manual/02_Establishing_the_Analysis_Framework_2025.pdf) — Purpose and need, existing/future No-Action and With-Action conditions, reasonable worst-case development scenario.
- [DCP: ULURP flowchart](https://www.nyc.gov/assets/planning/download/pdf/applicants/applicant-portal/lur.pdf) — Actors and formal review steps; no specified pre-certification duration. PDF publication vintage not established.
- [NYC OER: E-designation process](https://www.nyc.gov/site/oer/remediation/e-designation.page) — Hazardous materials, air and noise obligations; approval and occupancy gates.
- [Furman Center: CoreData dictionary](https://www.furmancenter.org/data-tools-resources/data-tools-core-data-dictionary/) — Existing research data fusion, variable meanings and source context.

## Raw materials still missing

| Requirement | Public material available | Additional evidence required before stronger claims |
|---|---|---|
| Parcel and access | PLUTO, address/BIN, ACRIS index | Survey, current title/legal control, easements, access and encumbrances |
| Existing occupants and uses | Agency description, DOB/HPD records | Site visit, leases/occupancy verification, tenant protections and relocation obligations |
| Buildable envelope | Zoning text, parcel attributes, program guidance | Architect's code/zoning analysis, survey/geometry, special-district and approval determination |
| Environmental conditions | E-designations, agency process, GIS discovery | Phase I and any Phase II, geotechnical, noise/air studies, remediation and agency acceptance |
| Transit and neighborhood need | GTFS, ACS/LODES, Furman context | Valid walking/transit routing, accessibility/reliability assumptions, current community priorities |
| Project economics | Program term sheets, RFP finance assumptions, HUD benchmarks | Qualified cost estimate, operating/utility assumptions, financing/tax-credit quotes, subsidy eligibility and availability |
| Deliverable and execution | RFP criteria, design workbook, review milestones | Sponsor qualifications, professional drawings, signed submissions and actual agency/expert review |

The advisors should review this requirements matrix and one Bronx case before we build a larger ranking engine. Ask them to supply a redacted successful/failed opportunity memo or underwriting checklist, identify the most consequential missing input, and specify which claims they would refuse to sign. No advisor feedback has yet been obtained.

## Deterministic backpressure and papercuts

1. HTTP success is not data success: Census returned Missing Key HTML with HTTP 200; ArcGIS returned JSON errors with HTTP 200. Parse and check payload shape before promoting a claim. ACS and HUD authenticated API paths remain credential-blocked.
2. An application shell is not a process document: several DCP pages yielded JavaScript shells. Do not claim their full contents or an undocumented API were retrieved.
3. Resolve links from official indexes: guessed agency/GitHub URLs returned 404. The successful PDF/workbook paths were discovered through linked official pages.
4. Preserve field/table vintage: the HPD AMI page contains a 2026 income section and a 2025 rent section. Mixed vintages must block a derived rent claim until explicitly reconciled.
5. Cross-check project identity: a New Utrecht FAQ link pointed to a Grand Concourse visioning report. A working link is insufficient; compare site/project scope before ingesting.
6. Require address and BBL corroboration for fallback geocodes; never accept a tied confidence score as a unique identity.
7. Separate effective date, retrieval date and record coverage: current ACRIS transport does not prove current title; workbook applicability and addenda matter.
8. Discover ArcGIS layers by semantic name: the working DEC erm/erm service contained ecological/wetland layers, not remediation sites. Guessed cleanup endpoints failed; a cleanup-site query is still unverified.
9. Bound acquisition: 35-second per-request timeout, six workers, 12 MiB response budget, exact request receipts and SHA-256. Failed requests remain evidence, not silent omissions.
10. Separate public access from licensing: original code is MIT and original documentation CC BY 4.0; upstream data/document terms require dataset-level review before redistribution.

The local validator checks the ten-source cap, required registry fields, receipt existence, all retained response hashes and sizes, successful API payload shapes, the exact ACRIS identifier join, Jerome parcel/address corroboration and GTFS validity. Rejection fixtures cover HTML masquerading as an API response and JSON API errors. It does not validate legal entitlement, financial feasibility or document interpretation.

## Reproduction and next decision

Run `python research/source-audit/build_registry.py` then `python research/source-audit/validate.py` from the repository. For live refresh, run `audit.py` against the retained `requests-*.json` files first; upstream data will change. PDF text was extracted using `pdftotext -layout` for the final process/briefing documents; earlier extracted chapter text is a convenience layer, with original PDF bytes authoritative.

The next useful probe is a versioned opportunity brief for 1337 Jerome with explicit existing-condition, No-Action and possible rezoning scenarios, keyed to Open Door and community priorities. Do not calculate a housing yield or financing conclusion until the applicable zoning envelope, program rules and assumptions are reviewed. Success is advisor agreement that the brief exposes the right missing decisions and evidence—not a visually convincing building rendering.
