---
name: render-site-concept
description: Generate and review a concept image from a verified brief using Codex image access, then attach actual execution records. With the current Claude Code setup, export the prepared brief instead.
---

# Render site concept

Generate, inspect and attach a concept image from an existing verified render brief.

## Inputs and preflight

Prepared run, actual reference assets and Codex image-tool access. Claude Code currently exports the brief and defers generation. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook for invocation and review contracts before generating. Use the exact prompt and declared references; inspect the result.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

Read [runtime branches](../start-here/references/agent-runtimes.md) when selecting Codex generation versus Claude Code export.

## Validate and hand off

Attach the actual image, invocation and review, then verify. Return packet/image paths and inspection limits.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

## Limits

If the tool fails or is unavailable, preserve/export the prepared package. Never fabricate execution records or claim metric geometry fidelity.
