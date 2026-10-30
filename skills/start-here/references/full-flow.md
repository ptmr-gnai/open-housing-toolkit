# Practitioner guide and full flow

Use this conversational route for first-time, uncertain, broad or “do the whole
flow” requests. It guides existing modules; it is not an automatic orchestration
engine or a promise of complete professional coverage. A direct expert request,
independent module request or explicit narrow evidence-only request keeps its own
scope. A bare address or BBL without an outcome is a guided request, not an
evidence-only instruction. Use what the user already supplied; do not repeat welcome, site, goal or inputs.
Ask one or two consequential questions at a time, continue independent work while
waiting, and explain progress and the next decision in ordinary language. When input
is needed, actually ask the question in the user-facing reply, not just list missing
fields or say the decision remains unclear. Offer plain-language choices or help choosing.

## Welcome and choose

For a newcomer, briefly welcome them: the toolkit can gather public site records,
explore conditional area scenarios, prepare diagrams and review/report packets, and
help prepare optional visual concepts. Ask whether this is a new project or a
continuation. If they already gave a site or asked for a specific output, acknowledge
it and skip questions already answered. Do not make a user learn module names or
lead with unexplained acronyms; offer details as the user chooses an outcome.

For a new project, accept a Bronx address or ten-digit BBL. Live parcel collection
currently supports one Bronx lot; do not promise automatic citywide site discovery.
Resolve the supplied site, confirm an ambiguous match before using it, and show the
resolved address and BBL when resolved. If the user supplies only a site, offer
the following short menu early in the first user-facing response and ask what they
want; allow multiple choices or “I'm not sure, help me choose”. Do not wait for
collection before presenting it. Do not ask for the address again. Explain choices in
plain language. Speak directly to the practitioner: show the menu itself, not
instructions describing what to ask, and end with an actual question such as
“Which would you like to explore? You can choose more than one, or say you are
unsure and I can help you choose.”

- **Understand a site:** a cited packet of available public records and gaps; it
  needs an identified supported lot and does not establish current use or title.
- **Explore scenarios:** compare conditional area assumptions with a calculation
  trace; it needs approved inputs and does not establish legal or buildable homes.
- **Rough shapes or layouts:** schematic assumed massing and diagrams where supported;
  these need parcel geometry and explicit dimensions, and are not verified designs.
- **Visual concept:** a brief, and an image only when the actual runtime supports it;
  it needs a real site reference and explicit assumptions and is not proof of fit.
- **Full exploratory packet:** work through relevant supported branches with a
  cited handoff, decisions and unresolved items; it is not an approval or feasibility
  finding.

Explain details when relevant, not as a long initial questionnaire. If unsure,
suggest starting with records and ask what decision they hope the work will inform;
it is fine not to know. Do not assume rental, ownership, or a development program.
For a returning project, locate the user's identified local run or ask for its path;
read its ledger, requests and artifacts, preserve previous versions, verify required
upstream packages, and resume pending decisions without repeating answered questions.
If the prior location or a needed package is unavailable, say what is missing.

## Preflight and progress

Quietly check the checkout, Python/setup, writable fresh output, available artifacts,
network for live work, and optional dependencies needed for selected branches. Read
[runtime routing](agent-runtimes.md); inspect the tools actually exposed by the host,
not its name alone. Explain the feasible plan and gaps before executing. Codex can
only offer actual image generation when an appropriate image tool is exposed and can
accept the needed reference; the current Claude route exports a verified brief. If
generation is unavailable and the user asks for an image, explicitly say that this
runtime cannot generate it, offer a verified brief for later use when its inputs are
available, and do not imply a brief is already complete. Ask for a real site photo or
a user-supplied Street View screenshot and the desired concept, one or two questions
at a time; do not introduce an unrequested design. Either asset can be a reference:
record its provenance and association with the site/view, check its actual availability
and rights as appropriate, and follow the render contract. It does not verify geometry,
camera alignment or fidelity. Never invent imagery, source assets or provider receipts.

Reserve a unique fresh local `runs/` project directory before writing anything:
create it exclusively, and if it already exists choose another name. Never write
into an existing run, including its inputs, to set up a new trial or project. Use a
human-readable `stage-status.md` as the continuity record. Record the user's intent and selected outcomes, site identity,
approved assumptions and rationales, supplied assets and provenance, artifact paths
and source dates, pending decisions, and the stage states below. Link actual requests,
receipts and packets rather than duplicating or altering their verified contents.
Do not store a guessed value as approved. If merely explaining capabilities with no
project yet, no project directory is required. Keep earlier runs and versions intact.

For a supported lot, follow [housing investigation](../../housing-investigation/SKILL.md)
to collect or replay, build and verify a fresh parcel packet. Report whether evidence
was live or replayed, its dates and coverage. Check identity and recorded existing use;
do not infer title, occupancy, legal capacity, financing or availability. Preserve
failed evidence and diagnostics. After evidence, continue the selected branches or
ask the focused question that unlocks the next one; do not silently end a whole flow.

## Guide the branches

Determine relevance with the practitioner, then read the appropriate leaf skill and
contract. Research inputs where a supported source or adapter permits it. If the user
says “I don't know”, explain the input, offer to research where supported or propose
clearly labeled hypothetical values with rationales for review. Obtain practitioner
approval before using proposed assumptions in calculations; silence is not approval.
Never present hypothetical values as facts. Explain each output and its limits as it
becomes relevant. Continue independent ready branches if another is blocked.

- **Area:** total gross area is the overall assumed floor area; nonresidential area is
  the share reserved for other uses; net efficiency is the share remaining for homes
  after shared/support space; average net home size is the assumed average interior
  area. Ask for or propose these with rationales, then use [area recipe](../../run-analysis-recipe/SKILL.md)
  when supported. Home-equivalents are an area quotient, not permitted homes.
- **Rental comparison:** only if relevant, request independent offers, mixes, rents,
  utilities, durations, profiles and coherent-year reference data. Follow
  [comparison](../../compare-housing-programs/SKILL.md). Do not infer eligibility,
  delivery or offers from area arithmetic, or substitute unrelated rental comparisons
  for homeownership. The toolkit does not automatically model ownership finance.
- **RER:** if relevant, follow [RER preparation](../../prepare-rer-draft/SKILL.md)
  with its verified comparison and preparation metadata. Incomplete drafts remain
  incomplete and applicability is not inferred.
- **Geometry and visual:** assess each independently. Follow
  [geometry](../../build-grounded-massing/SKILL.md) with its required geometry and
  explicit assumptions. For a photo concept follow [render preparation](../../prepare-render-brief/SKILL.md)
  and the runtime route. A brief is not a generated image or a verified design.

## Track, hand off and resume

Include evidence, area, rental comparison, RER, geometry and visual branches as
applicable, plus any user-specific objective the toolkit cannot support. For each
record **completed**, **awaiting input**, **declined**, **unsupported**, or **blocked**
(with specific reason), relevant paths and the exact next input or action. A prepared
brief is not a completed image. Mark a stage completed only after its actual gate;
relevance awaits input until clarified, or is declined when explicitly declined.
Do not invent successful dependencies. A stage's failure does not stop independent
ready branches.

At handoff provide a short cited cover note and ledger, what exists, source vintage,
meaningful limitations, the next useful decisions and how to resume. If awaiting an
answer, end the user-facing response with one or two direct questions, in plain
language, rather than only naming prerequisites in the ledger. Ask for the
minimum information that unlocks the next work; an unanswered question remains
awaiting input. On continuation inspect saved state and verify real upstream packages;
use fresh outputs for revisions. A partial handoff is not a completed whole flow.
Technical checks do not establish professional acceptance, legal entitlement,
eligibility, feasibility or submission readiness. Local preparation does not
implicitly authorize publication, submission or communication with others.
