---
name: build-grounded-massing
description: Build explicit assumed massing on a sourced real parcel and reconcile areas against a verified analysis packet.
---

# Build grounded massing

Build assumed schematic massing on a sourced parcel and reconcile program areas.

## Inputs and preflight

Verified analysis, supported parcel geometry, explicit footprint/heights/use assumptions and pinned geometry dependency. Use Python 3.11+ from the repository root. Preserve prior runs.

## Execute

Read the runbook and geometry guide before collection/build. Inspect both total and use-allocation comparisons.
Read [the execution reference](references/runbook.md) only when performing this task;
it contains commands, examples, contract links and recovery details. Use the existing
module CLI instead of reimplementing it in prose or adding a wrapper.

## Validate and hand off

Verify; keep handoff blocked on area mismatch. Retain SVG views, mesh, source geometry and unknowns.
Report what executed, actual output paths and unresolved inputs. If validation fails,
stop downstream execution, preserve evidence and diagnostics, correct inputs and
rebuild into a fresh run. Never bypass a gate or silently edit completed artifacts.

## Limits

Consistent arithmetic is only a schematic reference. The photo renderer does not consume this mesh contract.
