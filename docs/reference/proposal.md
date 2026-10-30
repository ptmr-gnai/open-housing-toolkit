Test whether a free, open source, agent executable playbook can turn a small Bronx site search into a development concept that a housing professional finds useful. The first probe will screen ten lots, investigate three, and assemble one evidence backed pack. A justified rejection or request for further investigation counts as useful output; the probe does not need to manufacture a buildable opportunity.

The public data are inputs. The asset we are testing is a reusable process for selecting a lead, challenging it, simulating alternatives, and communicating a defensible next step. Jeremy Ney’s *The Opportunity Map* remains the project’s framing reference, without attributing this proposal to the author.

## Hypothesis and decision

An open playbook can reduce the time and expertise required to produce a credible first pass housing proposal by making professional judgment explicit, executable, and reviewable.

After the probe and feedback from the user’s two expert advisors, decide whether to deepen the workflow, narrow its use case, or stop. This first run can establish technical reproducibility and prepare review material. It cannot establish expert usefulness until the advisors respond.

## Scope of probe one

Use one existing Bronx subway station area as a bounded search rather than selecting a site from a borough wide score. The proposed initial setting is the 170 Street station on the 4 line and its surrounding parcels; confirm the station location from an authoritative source before running the screen. This is an experimental choice, not evidence that this area is the best housing opportunity.

The housing objective is additional family oriented rental housing with affordable units. Income targets, rent schedules, unit sizes, and financing are scenario inputs, not inferred commitments. Use an illustrative 60 percent AMI lens where useful and identify the household size and official schedule required before translating it into rents.

Retrieve the parcel universe within a declared geographic window, apply a transparent screen, select ten candidates, investigate three, and produce one pack. Preserve reasons for exclusions and selection. Include existing occupancy as a constraint; apparent unused floor area is not permission to displace residents or businesses.

## Workflow

| Stage | Required work | Reviewable output |
| --- | --- | --- |
| Seek | Confirm geography and data vintage; inspect parcels; apply transit, capacity, existing use, and ownership lenses | Full bounded universe, ten lot screen, explicit selection reasons |
| Challenge | Check identifiers, current recorded use, residential units, zoning, ownership indicators, development filings, housing stress, and contradictions | Three candidate dossiers with evidence and unresolved gates |
| Simulate | Compare existing conditions with two parameterized housing concepts; calculate area, unit counts, and operating feasibility sensitivities | Scenario tables, formulas, assumptions, and break even quantities |
| Package | Build a concise lead brief, source map, concept diagram, risks, and next actions | Advisor pack and derivative communication templates |
| Evaluate | Ask two advisors to review independently, then inspect provenance and replay a changed assumption | Review records, disagreements, corrections, and decision |

## Open source requirements

The playbook, transformation code, ranking rules, formulas, schemas, sample configuration, and reviewer protocol must be available in a downloadable source package. Use the MIT license for project code. Give original documentation a CC BY 4.0 notice. Upstream datasets retain their own terms; an open source code license does not relicense source data.

The first run will save the source package with the project. Public repository publication can follow when a destination is established. No paid model or private data should be required to reproduce the deterministic screen and scenario calculations. Agent judgment can suggest a candidate or interpretation, but must be preserved as an explicit, reviewable decision.

## Intermediate representation and domain specific language

Interpret IR as intermediate representation: a machine readable evidence and decision graph from which proposals and other outputs are rendered. The DSL is a declarative configuration for search scope, lenses, rules, scenario parameters, evidence requirements, and export gates. Start with JSON and a versioned schema; a new programming language is unnecessary.

Every material value or claim must be one of: observed source value, derived calculation, explicit assumption, expert judgment, or unknown. Do not convert missing evidence into zero, a cleared constraint, or a negative finding.

Each source record must include URL or exact API query, publisher, retrieved timestamp, source update metadata where exposed, cached file, content hash, upstream terms reference, and coverage limits. Each derived claim must reference input claims and a named formula or code step. Assumptions carry units, purpose, rationale, editable value or range, and sensitivity role. Decisions carry the applied rule, alternatives, reason, and unresolved gates.

Store the complete bounded universe as well as the shortlist. Preserve contradictory observations and missing joins. Record code and configuration hashes, source snapshot hashes, and output hashes in a run manifest. A reviewer must be able to change a declared assumption and trace which outputs change.

The DSL must distinguish screening proxies from verified entitlements. A numeric PLUTO FAR field cannot clear a zoning gate. Ownership labels do not establish willingness to sell. Zero recorded residential units do not establish vacancy. Scheduled station proximity does not establish reliable job access.

## Information pack

The lead pack must contain site identity; reasons for selection; existing conditions; current recorded zoning; a capacity proxy with explicit limits; two concept scenarios; cost and operating sensitivities; affordability questions; occupancy and displacement questions; development pipeline checks; conflicting evidence; and a prioritized next action list.

All numbers in the prose and tables must come from the same IR. Generate maps and massing diagrams deterministically from source coordinates and declared geometry assumptions. Image generation may later illustrate a reviewed concept; it must never establish legal capacity, architectural feasibility, or neighborhood conditions. In probe one, the concept diagram will be sufficient unless the evidence supports a more specific depiction.

Provide a proposal summary and a short media style draft as alternative views of the same facts, with gates that prevent unsupported claims about availability, approval, financing, displacement, and construction. Do not publish or send these outputs.

## Advisor protocol

The user has two expert advisors. Prepare a common review form; the user can share the material. No advisor contact is required to run this probe.

First, each advisor independently reads the brief and marks material errors, missing constraints, useful information, and the disposition: reject, investigate, or advance. Request an estimate of how much work the pack saves and what work remains. Record review time if the advisor is willing.

Second, reveal the evidence graph and executable configuration. Ask each advisor to trace three important claims and propose one changed assumption. Replay that change and ask whether the resulting differences make sense. Compare disagreements before revising the playbook.

## Success criteria

Technical acceptance requires that the cached run replays without network access; its ten lot screen can be regenerated; every material quantitative claim has an input path; unknowns remain explicit; scenario arithmetic passes checks; and changed assumptions propagate to dependent outputs.

Professional acceptance requires both advisor reviews. A useful lead should support a clear next decision without material hidden assumptions. A convincing rejection can pass. Report each advisor’s view separately rather than averaging away disagreement.

This probe has no causal econometric acceptance criterion. Causal analysis becomes relevant when a later decision requires evidence about an intervention’s effects.

## Deliverables and boundaries

Save this proposal before executing the probe. Then save the screening results, three dossiers, one lead pack, source cache and manifest, executable DSL and IR, source code, reproduction instructions, and advisor review template.

The probe will not represent any site as available, legally cleared, financially committed, or approved. Public records may be stale and are incomplete on occupants, leases, site conditions, and title. Those limits belong in the decision graph and next actions. Advisor feedback and verified development diligence remain outstanding after this first execution.

