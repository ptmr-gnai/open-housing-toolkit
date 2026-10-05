# Applicant eligibility gates and cross case checks

The missed applicant requirements are now represented in an executable, source-bound gate component. Testing a second Bronx solicitation exposed an important policy variation: an unmet experience threshold may have an explicit agency review route, while a different threshold remains strict. A universal unit-count cutoff would give misleading advice.

This slice demonstrates deterministic rule handling and evidence requests. It does not demonstrate automated discovery of all requirements, actual applicant eligibility, practitioner usefulness or professional approval.

## The two source cases

The original 97 West 169th Street assessment remains frozen. This new component uses its RFP and three addenda, plus the St Ann’s Avenue/East 142nd Street February 2015 RFP and two addenda. Seven original PDF/text pairs are retained or referenced with hashes, source ZIP lineage and dates.

| Requirement | 97 West 169th Street | St Ann’s Avenue and East 142nd Street |
| --- | --- | --- |
| Development experience | One qualifying mixed-use project with at least 60 residential units, completed as principal through new construction or substantial rehabilitation within seven years | Base criterion: qualifying new construction with at least 70 residential units within seven years, plus comparable scope |
| Experience that does not match development criterion | No specific alternative experience route modeled | Addendum 1 permits a summary justifying experienced-team status; acceptance remains unresolved agency judgment |
| Management experience | At least 60 residential units in NYC within seven years, with stated role/ownership conditions | At least 70 residential units in NYC within seven years; Addendum 2 explicitly refuses flexibility and evaluates information current at submission |
| General contractor | Team requirement clarified by addendum | Addendum 2 explicitly requires identification for the proposal |
| Completeness | Required tabs/forms and applicable clarifications, including absence of E-4 | Required forms; addendum tells respondents to disregard an obsolete multiple-site instruction |

Sources: 97 West 169th RFP PDF pages 17–19, 26–27; Addendum 1 page 3 and Addendum 3 page 2. St Ann’s RFP pages 18–22; Addendum 1 pages 3–4 and Addendum 2 page 3. Full exact-page passages are in the typed case declarations.

These are historical solicitations with 2019 and 2015 information cutoffs, not currently open opportunities. Hosted archive packaging postdates those deadlines; exact historical byte equivalence remains uncertified. The curator already saw later summaries during discovery. No later outcomes were used as rules or labels in this transfer test, but it is not an independent blind analyst assessment.

## What the pipeline now does

There are 22 authored gates across the cases, with 31 exact-page citations. Each includes a responsible role and concrete evidence request. Gates cover applicant experience, roles/capacity, financial capacity, adverse findings, proposal feasibility/conformance and submission obligations at an initial level.

The declarative DSL permits only typed Boolean, equality, unit-count, enumerated-value and calendar-window operations. Unit thresholds and lookback years are extracted from the cited passage and must equal the declared parameters. A matching quotation cannot accompany an invented threshold. Other interpretation remains authored and requires review.

Status meanings are scoped:

- **Pass:** accepted evidence matches the declared criterion; this is not HPD acceptance.
- **Unknown:** evidence is missing, unreviewed or incomplete, or the base rule is unmet but an explicit agency review route remains unresolved.
- **Fail:** a reviewed complete evidence scope shows the declared criterion is unmet, with no specific alternative route modeled. Agency discretion and overall selection remain separate.

The system records both base-rule status and effective status. It does not turn a development-experience justification into approval. Missing applicant records cannot prove failure. One matching project can satisfy an existential development test; two undersized projects cannot be added into one qualifying project. Management instead uses a reviewed unique-unit portfolio, with overlapping records left for evidence review.

Accepted review metadata binds credential facts, evidence bytes, requirement sources, engine, schema and release-policy version. Changed evidence, facts or rules require review again. Review attribution is attested metadata; identity and document entailment are not authenticated automatically.

## Tests that matter

All credential examples are explicitly synthetic. No real developer history or accepted advisor review was supplied.

| Synthetic evidence | 97 West 169th rule result | St Ann’s rule result |
| --- | --- | --- |
| Qualifying 60-unit development and NYC management history | Both experience rules match | Development remains unknown through justification route; NYC management criterion fails |
| Qualifying 70-unit new-construction and NYC management history | Both experience rules match | Both numeric/role/date experience predicates match; comparable scope and other requirements remain review obligations |
| Qualifying 70-unit substantial rehabilitation | Development predicate matches | New-construction base predicate fails; experience justification remains unresolved |
| Two 30-unit development projects and reviewed 60-unit management portfolio | Development fails; management predicate matches | Development remains unresolved through justification route; management fails |
| 10,000 managed units outside NYC | NYC management criterion fails | NYC management criterion fails |
| Missing roles, unreviewed assertions or incomplete history | Unknown; no promotion from missing evidence | Unknown; no promotion from missing evidence |

Even fixtures that mark every scoped gate as passing cannot make an actual submission-readiness claim. They are synthetic and the full form/attachment inventory has not been expanded and reviewed. Low-cost evidence gathering remains available.

The CLI recomputes from requirements and evidence before releasing an output; it does not trust a supplied readiness flag. An evidence pack is permitted with explicit unresolved status. A blocked readiness claim returns exit status 2, making backpressure machine-enforceable at this export boundary.

**Validation:** 26 behavioral/rejection tests pass. Tests cover source-specific thresholds and discretion, no project summing, missing evidence, stale reviews, changed source bytes, wrong-page citations, altered numeric rules, future/out-of-area experience, synthetic-to-actual relabeling, forged readiness flags and blocked CLI exit status. Output replay is byte-identical.

## What changed for the intended practitioner

The first assessment said, broadly, “organize due diligence and concept tests.” The new component first asks for a qualifying principal’s project history and a qualifying NYC management portfolio, with the exact source requirements. It can identify a team-change or agency-clarification question before a practitioner commissions more expensive design work.

That is a proposed improvement in decision order. Without an actual practitioner baseline or advisor feedback, time saved and decision quality remain unmeasured. The rules were curated by the project author; we have not shown that a fresh analyst reliably discovers the full inventory by itself.

## Next evidence needed

The remaining coverage gap is the detailed proposal inventory: each required form, attachment, applicable program/design obligation, and addendum correction needs its own evidence record and a completeness review. The next transfer test should focus on omissions and source conflicts, rather than unit counts or resemblance to a winning project.

For advisors, the concrete questions are whether these gate semantics preserve agency discretion correctly, whether the principal/managing-agent ownership conditions are interpreted correctly, and whether these evidence requests change the order of work for a small developer. Original source passages, rules, code, tests and outputs are included in the downloadable pack. The prior frozen assessment is unchanged.
