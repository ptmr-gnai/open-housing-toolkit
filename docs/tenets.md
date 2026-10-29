# Project tenets

The Open Housing Toolkit helps housing practitioners and their agents gather data,
apply established methods, investigate scenarios and prepare useful materials.
Practitioners bring the domain knowledge, objectives and professional judgment.
The toolkit makes more of that work accessible, repeatable and inspectable.

This project is being built from a software and agent-tooling perspective while we
learn the housing process. We do not claim to know that entire process. We build
trust by showing our sources and limits, incorporating expert corrections, and
learning whether people can use the work successfully.

## 1. Trust domain expertise; keep practitioners in charge

Housing practitioners determine which methods apply, interpret the results and
make professional judgments. Our contribution is to help them and their agents
carry out the work. Domain expertise includes agency, development, planning,
research and community experience; different kinds of expertise answer different
questions.

**In practice:** name the basis for each interpretation and its review status.
Preserve expert disagreement and supporting evidence. A cited expert is not an
endorsement of our implementation, and a disagreement is a question to resolve
openly rather than silently overwrite.

## 2. Use what exists before inventing a method

Start with the best available, applicable agency guidance, established research,
community resources and maintained tools. We are not setting out to replace
housing experts' methods with our own. The primary innovation is in access,
composition, automation and reproducibility.

**In practice:** explain what we reuse, why it fits, its version and limitations,
and what we changed. Prefer adapters to duplicating maintained tools. Any new or
substantially changed domain method is a separately labeled experiment requiring
expert evaluation; it cannot quietly become the default.

## 3. Be honest about what we know

We are learning in public. A complete-looking workflow can still omit important
professional steps. Technical integrity, domain correctness and practical usefulness
are separate questions.

**In practice:** distinguish working components, proposals and experiments. Name
uncovered work and pending reviews. Claim expert review only for the actual scope
reviewed. Citing an agency document does not establish compliance, approval or agency
endorsement.

## 4. Empower people and the agents working for them

The first user has housing domain knowledge and a task to accomplish. The user
sets the question and objectives; agents can gather evidence, execute methods,
explain changes and prepare materials on that user's behalf.

**In practice:** expose skills and discrete workflows with clear inputs and outputs.
Make assumptions editable and methods replaceable. Support bringing an existing
analysis into a module as its contract permits. Document unsupported imports rather
than implying every agency model can already be ingested.

## 5. Make the work inspectable and correctable

Trust requires more than footnotes. A practitioner should be able to locate a
supporting passage or field, understand a calculation, change an assumption and
see the consequences.

**In practice:** retain source identity, dates, versions, units, coverage and hashes
where source bytes are available. Bind derived claims to inputs and methods.
Keep source retrieval dates separate from observation dates. Preserve contradictions,
corrections and earlier runs. Missing source bytes or incomplete provenance remain
explicit limitations.

## 6. Keep evidence, assumptions and interpretation distinct

Observed conditions, conditional scenario arithmetic, forecasts and causal effects
are different. None becomes another simply because an agent writes confident prose.
Professional judgment and community priorities must remain attributable.

**In practice:** carry typed facts, assumptions, calculations, judgments and unknowns
through the model and every output. Preserve uncertainty and missingness. An
unknown is not zero, a cleared constraint or an absence of harm.

## 7. Ask who benefits, who bears costs, and compared with what

Community benefit has a population, geography, alternative and time horizon.
Current residents, prospective residents, businesses and the wider city can have
different interests. A community does not have a single preference that an API can infer.

**In practice:** show benefits and harms separately, with attributed objectives and
tradeoffs. Use established community-led processes to inform priorities. Publish
any ranking criteria and sensitivity. Do not default to an unexplained universal
benefit score or assume more floor area settles the question.

## 8. Build checks that expose problems early

Use classic engineering principles: explicit contracts, versioned methods,
reproducible calculations, isolated changes and validation at interfaces. Checks
should detect consequential failures rather than merely make a demonstration pass.

**In practice:** reject incompatible units, stale dependencies and unsupported
methods; flag conflicting observations; propagate changed inputs. Allow diagnostic
packets to explain missing evidence while withholding claims that evidence cannot
support. Keep semantic completeness and professional acceptance distinct from tests.

## 9. Judge the work by usefulness and faithful communication

A justified rejection, an exposed contradiction or a well-formed next question can
be a successful result. An attractive render is a communication asset with its own
fidelity limits.

**In practice:** observe real users, compare against professional work when available,
record papercuts and retain failures. Ask whether results support a real decision.
Do not use image quality, citation counts or passing tests as substitutes for that
assessment. Carry assumptions and unresolved issues into proposal and outreach assets.

## 10. Keep the toolkit open, modular and portable

People should be able to inspect, adapt and use individual components, with their
own agents and infrastructure. The components should also work together through
explicit contracts.

**In practice:** publish code, schemas, methods, sample configurations and relevant
review findings. Respect upstream data and imagery terms; open code does not make
all inputs redistributable. Public examples need not expose a practitioner's private
working data. Preserve useful experimental history and improve entry points as the
project matures.

## How we apply these tenets now

The [community-benefit proposal](specs/community-benefit.md) uses NYC reporting
resources and published housing/transit work as its foundation. Its first bounded
[housing-cost comparison](../housing_benefit/README.md) is implemented with illustrative
programs; broader benefit methods and professional validation remain pending. The current parcel,
recipe, geometry and image experiments show our work and its limitations.

These tenets guide implementation choices and review. Changes to them should explain
the reason and supporting experience. They do not establish a new approval requirement
for routine work already authorized by a user.
