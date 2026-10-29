# Community benefit from housing and transit-oriented development

Research date: 29 October 2026, America/New_York. Broad orientation, not a systematic
literature review, calibrated forecasting model or professional endorsement.

## Main finding

We have source-backed parcel facts, conditional area arithmetic, explicit geometry
and illustrative assets. We do **not** yet model community benefit. Public data can
support parts of that analysis, but cannot select community objectives or establish
causality by itself.

The useful starting question is: **what changes, for whom, compared with what
alternative, over what period, and on what evidence?** The first product should be
an inspectable comparison of benefits, harms, commitments and unknowns. A universal
"maximal community benefit" score is not justified by this research.

Two research agents examined housing/equity and transit/accessibility in parallel;
the lead examined agency reporting, appraisal discipline and community-led criteria.
We prioritize official guidance, authors' research and official tool documentation.
The [25-reference registry](sources.json) records inspection scope and limitations.
Five documents/pages also have [byte retrieval receipts](retrievals.json). Their
source bytes are cached locally under ignored runs/ and are not bundled publicly;
URLs, hashes and access notes do not guarantee continued source availability.
No private correspondence or advisor contact information is included.

## Existing professional foundations

**NYC already has a relevant packet structure.** The [Racial Equity Report guide][rer]
combines project affordability/jobs, community context and displacement mapping with
a fair-housing narrative. It distinguishes units, income bands, bedroom/household
sizes, rents and program. This is a useful reporting template; applicability and
compliance need separate review. Its jobs guidance also resists invented benefits:
unknown commercial tenants cannot justify speculative permanent-job claims, and
construction employment is reported in person-years, not permanent jobs.

The [EDDE overview][edde] and [city displacement-risk explanation][risk] provide
existing-community context. A neighborhood vulnerability index is not the probability
that a particular project will displace people. The live explorer's data exports
were not audited or integrated; its interactive site failed in the web reader.

[CEQR socioeconomic guidance][ceqr5] supplies a future-without-project comparison
and distinctions among direct/indirect residential and business displacement.
Regulatory significance screens do not answer whether a project benefits residents
or whether any displacement is acceptable. [Transportation guidance][ceqr16]
adds potential adverse effects on capacity, pedestrians, safety and other modes.
Neither chapter is a general welfare calculator.

The [Urban Institute TOD framework][tod] distinguishes planning/prioritization,
delivery tracking and outcome evaluation. We should preserve those stages. [ANHD's
community principles toolkit][anhd] supplies a process for communities to establish
criteria rather than infer their preferences from demographic data.

The [MHCLG appraisal guide][mhclg] is a useful methodological comparison: counterfactuals,
additionality, distribution, uncertainty, nonmonetized impacts and double-counting
checks. It applies to England; its parameters and policy weights are not NYC defaults.
[USDOT's BCA explanation][bca] similarly separates societal efficiency from financial
or economic-impact accounting. Property appreciation, construction spending and jobs
cannot simply be added to other benefits as independent welfare gains.

## What must stay distinct

| Evidence type | A defensible statement | What it does not establish |
| --- | --- | --- |
| Observed context | This neighborhood has a measured rent-burden distribution or a published displacement-risk index. | The marginal effect of this proposal. |
| Conditional project arithmetic | This supplied program includes a stated number of homes at specified income/rent bands and restriction durations. | Delivery, assignment to specific households, or local market-wide affordability. |
| Modeled exposure/access | Under pinned routes, calendars and walking assumptions, these destinations are reachable from this location. | Actual journeys, employment, reliability, crowding or disability access where unknown. |
| Behavioral projection | Under stated household/alternative-location assumptions, spending or travel could change by a modeled range. | A measured causal result. |
| Causal evidence | A particular intervention in a studied setting changed an outcome under an identified research design. | An automatically portable coefficient for a Bronx parcel. |
| Commitment/delivery record | A benefit is proposed, secured by an identified instrument, financed, delivered or observed. | That every earlier stage has already achieved the later outcome. |

These distinctions supplement the existing fact/assumption/calculation/judgment/unknown
claim types. They should not replace them with one vague confidence score.

Housing near an existing station does not itself improve the network. Its potential
contribution is making housing at that accessible location available to additional
households. Report housing-program quantities beside reachable opportunities; do
not multiply homes by jobs reachable and label the product new jobs.

Zoning permission, permitting, financing, completion and occupation are distinct
milestones. A proposed capacity is neither a forecast of construction nor an observed
benefit. Use an explicit future without the intervention, not today's conditions as
an automatic substitute. Report additions and losses, not just gross production.

## Candidate benefit and tradeoff dimensions

This table is a proposed toolkit design synthesis, not a claim that all methods are
already implemented or that agencies assign these dimensions identical importance.

| Dimension | Candidate measures and raw materials | Boundary or missing judgment |
| --- | --- | --- |
| Housing offer | Explicit new/removed/preserved homes; bedroom sizes; accessible units; tenure; population served; project plans and existing-use investigation | Our 34 home-equivalents are not a verified unit mix and cannot populate an affordability table. |
| Depth and durability of affordability | Gross rent including relevant utilities, income/household size, bedroom size, AMI band and year, program, restriction period and enforcement instrument | Regional AMI eligibility differs from affordability to nearby households; program-specific rules require review. |
| Existing community and direct losses | Occupied homes, protections, businesses, jobs/services, relocation and return provisions; records plus surveys/leases/interviews where necessary | PLUTO's zero residential count does not establish no occupants or no displacement. Unknown must not become zero. |
| Opportunity access | Scheduled travel time to jobs by wage/sector and to services; OSM walking network, transit entrances/GTFS, LODES and destinations | Fare, time of day, disability constraints, reliability and capacity matter. Reachability is not a job obtained. |
| Household budget | Housing plus transportation expenses for explicitly defined household profiles and alternative locations | Observed costs, modeled costs and illustrative assumptions differ; no assumption that existing residents' spending changes automatically. |
| Health and environmental conditions | Local exposure, safety, heat/flood context, operational/embodied emissions and transport activity | Historical context is not project-caused change. Emissions/VMT projections need behavioral and location counterfactuals. |
| Public resources and delivery | Subsidy, tax expenditure, public-land alternative use, ongoing support, schedule and delivery stage | Loan face value is not net subsidy; public, private and societal accounting differ. No invented delivery probability. |
| Community priorities and distribution | Who gains/loses, alternative viewpoints, binding versus proposed commitments, attributed criteria | No API can establish a community's consensus or appropriate weights. |

Separate existing residents, prospective residents, displaced people wherever they
move, businesses/service users, the regional housing market and public agencies.
A rise in neighborhood median income can reflect population replacement. It is not
proof that the original residents are better off. Any evaluation must identify its
population and avoid tracking only people who remain.

Our geometry uses a gross-floor-area proxy. The city's reporting also asks for
residential zoning square feet. These are different quantities; no automatic relabeling.

The RER guidance also identifies a public-data gap for new-construction market rents.
Licensed rental data, broker evidence or an explicitly supplied estimate may be needed.
A public-data-only pipeline must leave that input unresolved rather than substitute
a neighborhood median rent without explaining the mismatch.

## Transit: useful existing methods and tools

Cumulative opportunity access is a tractable descriptive method:

`access_i(T) = sum_j opportunities_j × indicator(travel_time_ij <= T)`

Choose and publish opportunity type, departure dates/windows, modes, walking/transfer
assumptions and multiple time budgets. Missing travel or accessibility data must
remain missing. An explicit network change can produce an access difference; adding
housing to an unchanged network changes housing allocation at that location instead.

[EPA Smart Location Mapping][epa] provides a useful precedent and historical benchmark;
the documented database release is 2021. [MTA's feed descriptions][mta] disclose
important coverage gaps: the Bronx bus feed alone omits Bx23/BxM routes, and static
feeds do not represent every temporary change. Pin actual feed bytes and service dates.

[r5py][r5py] is a plausible open-source routing adapter, not yet run here. [OpenTripPlanner's
documentation][otp] highlights unknown wheelchair-accessibility data. Opportunity
access and disability access are related but different requirements.

[HUD/DOT LAI v3][lai] is a household housing-plus-transport cost modeling precedent,
not current measured 2026 spending. [MTC's policy][mtc] demonstrates that agency TOD
work includes preservation/protection and station access. [CNT's calculator description][cnt]
is an adjacent product lead, but its full model and open-source status were not audited.

## Econometric evidence: useful, with different treatments

| Research | What it can inform | What not to do |
| --- | --- | --- |
| [Asquith/Mast/Reed, completed new housing][amr] | Evidence for local supply effects in the sampled rental markets. | Copy a reported rent effect into this site's forecast. |
| [Mast, moving chains][mast] | A regional mechanism linking new construction and subsequent household moves. | Treat a modeled chain as a measured local anti-displacement guarantee. |
| [Freemark, Chicago rail-area upzoning][freemark] | Permissions and delivered housing can diverge; study found no perceptible relative permitting increase over its horizon and higher property values. | Infer measured rent/displacement effects the study did not observe, or declare all upzoning ineffective. |
| [Moving to Opportunity][mto] | Neighborhood exposure can affect long-term outcomes; age, treatment and exposure duration matter. | Attribute voucher-experiment effects to this building or a station-distance score. |
| [Choice Neighborhoods evaluation][choice] | A practical evaluation combines resident and neighborhood outcomes, multiple data types and comparison methods. | Promise parcel-level outcomes from a program-specific retrospective study. |
| [TOD/gentrification systematic review][review] | Local conditions and research design complicate causal conclusions. | Assume either unavoidable displacement or guaranteed protection from TOD proximity alone. |

For a future causal module, define treatment and estimand first. Difference-in-differences,
event studies, synthetic controls, structural models and randomized evidence answer
different questions and require different assumptions. Selection, parallel trends,
spillovers, timing, missing movers and transportability need explicit review. No
causal estimator or validated Bronx effect coefficient was implemented in this work.

## Concrete provenance findings

- HPD's live AMI page has a **2026 income-table heading and 2025 rent-table heading**.
  We retrieved it directly and recorded its byte hash. A page-level retrieval date
  cannot make all tables the same vintage. Pin and reconcile table-level schedules.
- The RER filename/URL and internal date stamps differ. Preserve both instead of
  inventing a single publication date.
- An earlier HUD evaluation-status page lagged the subsequently published Choice
  report. Prefer the actual report/publication, with the page's inspection extent stated.
- Historical EPA/LAI inputs cannot be called current parcel conditions.
- UK appraisal's displacement of economic activity or supply elsewhere is not the
  same variable as involuntary displacement of existing residents. Name them separately.

## Recommended next thin slice, after this research

Build a **RER-inspired housing-program and opportunity comparison** for one site:

1. Accept two explicitly supplied housing programs and a time-specific no-action
   baseline. Require real or explicitly assumed unit mix, income/rent/utility rules,
   restriction duration and delivery status. Do not derive homes by rounding area.
2. Compare the offer by household/income/bedroom category. Show existing-community
   needs and direct-loss/occupancy coverage beside the offer, without a causal label.
3. Add a separate network-access context card using pinned transit/street/job inputs.
   Report additional homes at that access level conditional on delivery, without
   claiming improved network performance, lower regional rents or jobs obtained.
4. Produce a packet with explicit tradeoffs, unknowns, uncertainties and an attributed
   practitioner/community narrative. No aggregate optimum by default.

A useful counterexample is a larger proposal that offers more homes but fewer homes
affordable to a specified lower-income group. The output must expose the tradeoff.
Removing occupancy evidence must preserve unknown direct-displacement coverage.
Changing an AMI year, utility allowance, tenure, duration or transit window must
recompute or invalidate the dependent comparisons. These are proposed acceptance
experiments, not completed tests of a benefit engine.

The accompanying [candidate method catalogue](methods.json) is a researched backlog:
all entries are unimplemented. It records inputs, outputs and blocked interpretations
so future recipe modules can be built without silently promoting context into impact.

## What would justify an overall ranking later?

An attributed objective, defined beneficiary/geography/horizon, comparable alternatives,
valid metric definitions, sufficient evidence and reviewed weights. Keep distribution
and uncertainty visible, show sensitivity, and explain alternatives that are
nondominated on the declared dimensions. Missing harm data must not earn a zero-cost
score. Rendering quality must not affect analytical benefit assessment.

[rer]: https://www.nyc.gov/assets/planning/downloads/pdf/applicants/preparing-application/rer-instructions.pdf?r=1025a
[edde]: https://www.nyc.gov/site/hpd/services-and-information/equitable-data-development-explorer.page
[risk]: https://a816-dohbesp.nyc.gov/IndicatorPublic/data-features/displacement-risk/
[ceqr5]: https://www.nyc.gov/assets/oec/technical-manual/05_Socioeconomic_Conditions_2025.pdf
[ceqr16]: https://www.nyc.gov/assets/oec/technical-manual/16_Transportation_2025.pdf
[tod]: https://www.urban.org/sites/default/files/2025-12/Tracking%20Transit-Oriented%20Development%2020251209.pdf
[anhd]: https://landusetoolkit.anhd.org/wp-content/uploads/2023/10/ANHD_-_Community_Land_Use_Principles_Toolkit.pdf
[mhclg]: https://www.gov.uk/government/publications/the-mhclg-appraisal-guide/the-mhclg-appraisal-guide
[bca]: https://www.transportation.gov/grants/dot-navigator/what-is-a-benefit-cost-analysis
[epa]: https://www.epa.gov/smartgrowth/smart-location-mapping
[mta]: https://www.mta.info/developers
[r5py]: https://r5py.readthedocs.io/stable/user-guide/user-manual/travel-time-matrices.html
[otp]: https://docs.opentripplanner.org/en/latest/Accessibility/
[lai]: https://files.hudexchange.info/resources/documents/Location-Affordability-Index-Version-3-Data-and-Methodology.pdf
[mtc]: https://mtc.ca.gov/planning/land-use/transit-oriented-communities-toc-policy
[cnt]: https://cnt.org/node/504
[amr]: https://www.philadelphiafed.org/community-development/housing-and-neighborhoods/supply-shock-versus-demand-shock-the-local-effects-of-new-housing-in-low-income-areas
[mast]: https://research.upjohn.org/up_workingpapers/307/
[freemark]: https://www.urbanaffairsreview.com/uar-archive/2019/03/29/upzoning-chicago-impacts-of-a-zoning-reform-on-property-values-and-housing-construction
[mto]: https://opportunityinsights.org/paper/newmto/
[choice]: https://www.urban.org/research/publication/choice-neighborhoods
[review]: https://www.tandfonline.com/doi/full/10.1080/01441647.2019.1649316
