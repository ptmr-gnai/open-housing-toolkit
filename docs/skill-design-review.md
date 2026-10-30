# Skill design review and next revision

Reviewed 2026-10-30 against the sources below. This is an authoring review, not
confirmation that our skills work in every host. Existing bound leaf skills and
historical experiment receipts have not been rewritten.

## Guidance inspected

- [Anthropic: skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices):
  concise instructions, clear sequential checklists, validation before continuing,
  feedback loops, shallow reference links, declared dependencies and real-use testing.
- [OpenAI: build skills](https://learn.chatgpt.com/docs/build-skills):
  skills load progressively; descriptions should identify the task and its boundaries.
  Instructions, optional scripts and references form a reusable workflow.
- [OpenAI: plugin skill authoring](https://developers.openai.com/plugins/build/skills):
  focused user goals, explicit tool sequences and decision points; evaluate direct,
  indirect, incomplete, irrelevant and unsupported requests, including output quality.
- [Agent Skills specification](https://agentskills.io/specification):
  required name/description metadata, optional compatibility metadata, scripts,
  references and assets; reference files directly instead of long link chains.
- [Claude Code: skills](https://code.claude.com/docs/en/skills):
  project skill discovery uses `.claude/skills/`; root `skills/` is also a plugin
  layout. Our checkout currently uses explicit AGENTS.md/CLAUDE.md routing. Reading
  files through that route is not proof of native skill-menu discovery.

These are inspected documentation sections, not a comprehensive survey. They do
not prescribe a universal automatic chain-of-skills protocol. The following
architecture is our engineering recommendation.

## Proposed sequence contract

Keep one coordinator for intake and routing. Load a leaf skill only when its task
is selected; do not require reading every skill or running every module first.
Each leaf should expose this compact contract:

| Field | Required content |
| --- | --- |
| Trigger / scope | User goal and unsupported cases |
| Preflight | Execution capability, dependencies, real inputs, fresh output path |
| Inputs | Exact schemas, units, upstream package and verification command |
| Steps | Commands or tool actions in order, with explicit decision points |
| Outputs | Named files, actual absolute location, stage/status |
| Gate | Validator to run before the next consumer; no invented defaults |
| Recovery | What remains usable after failure; how to revise into a new run |
| Handoff | Next eligible skill and required artifacts; optional branches |
| Limits | Engineering validation versus professional interpretation |

Enforce fixed, fragile steps in code. Keep practitioner choices and explanation in
the skill. Our first-run runner already sequences verified packages and stops on
failure, but its fixed tour is not a general workflow engine. Its ledger and logs
are execution diagnostics; module manifests bind analytical inputs and outputs.

Resume from a verified package, not from an agent's recollection that a prior step
succeeded. A missing image tool yields a completed brief and deferred generation;
it must not produce fabricated invocation/review records. Missing program facts
remain missing rather than becoming inferred official fields.

## Gaps to address before describing skills as polished

1. Standardize the leaf contracts and provide complete input/output examples.
2. Make model-to-visual, optional geometry and report handoffs explicit in the
   coordinator; retain unsupported adapters as unsupported.
3. Package/discover skills in actual Codex and Claude Code hosts without duplicating
   canonical instructions. Decide checkout dependency versus portable bundles.
4. Test activation, branching, incomplete input, failure and resume in each host.
   A fresh AI walkthrough of the fixed tour does not cover these cases.
5. Declare and test platform support. See [storage and platforms](storage-and-platforms.md).

Changing existing leaf skills can invalidate module-bound examples. Apply revisions
with explicit rebuild/review rather than patching receipt hashes. This review is
not an implementation of those five improvements.
