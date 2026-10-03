import json,pathlib
P=pathlib.Path(__file__).resolve().parent;registry=json.loads((P/'registry.json').read_text());ledger={x['id']:x for x in json.loads((P/'access-ledger.json').read_text())}
def link(id,label):return f"[{label}]({ledger[id]['url']})"
t='''# Bronx housing raw materials: ten-source audit

Audited 3 October 2026. This is a source-readiness inventory and a small reconstruction of agency practice. It is not a feasibility study or an expert endorsement. Ten source families are listed; each can host many datasets. ACRIS uses NYC Open Data for its structured interface, so these are not ten independent API infrastructures.

## What the professional workflow requires

The goal is an open, reproducible path from a housing question to a reviewable opportunity brief: why this site, who benefits, what can be built, which approvals are needed, what it costs, and what evidence is still missing. A professional workflow includes data, program rules, legal documents, team qualifications, community priorities, drawings, financial assumptions, investigations and agency review.

We grounded the inventory in HPD's actual New Utrecht Library and Affordable Housing RFP pre-submission briefing, HPD's July 2026 design review process, its financing term sheets, the December 2025 CEQR framework, DCP's ULURP flowchart and Furman Center's established data products. These sources describe actual requirements; they do not prove that every agency analyst follows one identical workflow.

## Hardened shortlist

“Verified” means the stated request or download worked in this audit. It does not imply that every dataset, field, geographic region or authenticated interface has been verified.

| Source family | Raw materials and purpose | Tested access and limits |
|---|---|---|
'''
for s in registry['sources']:
 t+=f"| {link(s['documentation_receipt'],s['name'])} | {s['raw_materials']} | **{s['interface']}.** {s['access']} |\n"
t+='\n## Integration contracts\n\n'
for s in registry['sources']:
 t+=f"### {s['name']}\n\nJoin keys: {s['join_keys']}.\n\nEntry point: `{s['endpoint']}`. [Retained request URL]({ledger[s['probe_receipt']]['url']}).\n\n{ s['limitations'] }\n\n"
t+='''## Probe grounded in industry work

**A Bronx agency case, rather than an invented opportunity.** HPD's 1337 Jerome Avenue project page describes a 6,516-square-foot site, a vacant former City pest-control building, affordable homeownership through Open Door, community amenities, R8A with C2-4 in the Jerome Special District, and a possible rezoning. Its published phase is community visioning; an RFP is planned for Fall 2026. We have not treated it as an issued RFP or an unclaimed site.

GeoSearch returned an exact address candidate with BBL 2028560051 and BIN 2008295. PLUTO independently returned that address, 6,516-square-foot lot area, R8A/C2-4/J and an HPD owner label. The checks agree on parcel identity and agency-described lot/zoning attributes. PLUTO's owner label does not establish legal site control. Both GeoSearch and competing results had fallback confidence 0.8, so confidence alone would have selected ambiguously.

**A real proposal evaluation.** The New Utrecht July 1, 2026 agency briefing separates threshold criteria from competitive review. Thresholds include complete forms and requested documents, a specified equitable-ownership requirement, 100% affordable housing and compliance with project parameters. It then asks for community responsiveness, design, zoning assumptions, financing and operating assumptions, team experience, job outreach and continued library service. Its library-specific conditions must not be copied to the Bronx. The submission date has passed; this is a workflow reference. The briefing does not replace the RFP and later addenda, which were identified but not fully downloaded or reconciled.

**A design submission contract.** HPD's current process guide has workbook/waiver submission, design consultation, review pathway determination and later reviews. The 2026 guidance applies to projects submitted for Design Consultation on or after October 1, 2026. We downloaded and parsed the real XLSX workbook's sheet structure. The guide says all projects require a Phase I Environmental Site Assessment, regardless of review pathway. A public map cannot supply that investigation.

**Reproducible transit and employment inputs.** The MTA ZIP parsed as GTFS and contains station 412, 170 St. The feed declares validity May 26–October 31, 2026. We parsed all 108,030 rows of New York's 2023 LODES all-jobs workplace file; 3,435 Bronx workplace blocks sum to 340,785 jobs. That is a data plumbing check, not a current employment estimate, a count of employed residents, or a travel-time accessibility result. Travel-time routing and an econometric estimate were not performed.

**Title-record plumbing.** For the original lead parcel at 1240 Edward L Grant Highway, 48 ACRIS legal records joined one-to-one by document identifier to 48 master records. The latest returned document date was February 10, 2023, and good-through dates vary. Native document images, title exceptions, parties and present site control remain unverified.

## Agency and research references to read first

'''
for id,label,desc in [('hpd_jerome_official','HPD: 1337 Jerome Avenue','Bronx case; public purpose, program, zoning, community process and status.'),('hpd_rfp_conference_pdf','HPD: New Utrecht RFP pre-submission briefing','Pages/slides 18–25: threshold criteria, appendices, team, drawings, financial assumptions and submission requirements.'),('hpd_design_process_pdf','HPD: New Construction Design Review Process, July 2026','Milestones, review pathways, evidence requirements and applicability.'),('hpd_design_workbook','HPD: New Construction Design Guidelines Workbook','Actual structured submission material; downloaded and XML sheet structure checked.'),('hpd_ncf_pdf','HPD: NCF term sheet, July 2025','Example rental-program finance/eligibility requirements; not the Jerome homeownership program.'),('hpd_term_sheets','HPD: program term-sheet index','Select the applicable program, including Open Door for the published Jerome case.'),('hdc_develop','HDC: Develop Affordable Housing','HDC financing and linked term sheets; filename and hosting date alone do not establish effective date.'),('ceqr_framework_pdf','NYC OEC: CEQR Analysis Framework, December 2025','Purpose and need, existing/future No-Action and With-Action conditions, reasonable worst-case development scenario.'),('dcp_ulurp_pdf','DCP: ULURP flowchart','Actors and formal review steps; no specified pre-certification duration. PDF publication vintage not established.'),('oer_e','NYC OER: E-designation process','Hazardous materials, air and noise obligations; approval and occupancy gates.'),('furman_dictionary','Furman Center: CoreData dictionary','Existing research data fusion, variable meanings and source context.')]:
 t+=f"- {link(id,label)} — {desc}\n"
t+='''
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
'''
(P/'report.md').write_text(t)
print(len(t))
