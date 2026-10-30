---
name: prepare-render-brief
description: Convert an explicit visual scenario and supplied reference scene into a provider-independent building-render brief. Analysis is optional; collection and modeling modules are not required.
---

# Prepare render brief

Prepare a provider-independent concept brief from a scene, reference asset and explicit visual assumptions.

## Inputs and preflight

Supported scene/scenario inputs, fresh output and a resolved reference image for actual generation. Analysis is optional. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook for local-photo and conversation-reference paths. Prepare and verify the exact brief/prompt.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

Read [runtime branches](../../start-here/references/agent-runtimes.md) when selecting Codex generation versus Claude Code export.

## Validate and hand off

Codex with an exposed image tool can continue to render-site-concept when requested. Claude Code exports the complete brief package.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

Eligible next steps: [render-site-concept](../render-site-concept/SKILL.md) (only when image generation is requested and available). Load only the requested branch.

## Limits

No separate image API key is needed for either supported path. A prepared brief does not prove its external photo is available or geometry is reconciled.
