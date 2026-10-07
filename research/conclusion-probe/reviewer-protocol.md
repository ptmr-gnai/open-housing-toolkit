# Independent reproduction and challenge

This protocol is for someone who did not build the experiment. The reviewer does not need to endorse redevelopment. A reasoned rejection of the conclusion is useful feedback. The project author has not contacted or attributed answers to any reviewer.

## First judgment

Read `outputs/conclusion.md` before looking at the control outcomes. Record whether the proposed next investigation makes sense, what material constraint is absent, and which statement seems overstated. Distinguish historical filing activity from current use and straight-line station proximity from usable access. Is occupancy investigation the right next task, or should title, environmental obligations or another constraint come first?

## Reproduce

Extract the ZIP into a clean directory with Python 3.10+. No network or package installation is needed. Run `python research/conclusion-probe/validate_probe.py`, then `python -m unittest discover -s research/conclusion-probe/tests -v`. Record your environment, commands, outputs and any failure. Passing replay establishes reproducibility of these bytes and rules; it does not establish that the interpretation is correct.

## Trace and challenge

Trace three supporting claims from `outputs/baseline.json` into their source body and receipt: one historical filing passage, recorded residential units, and debt-support rent. Verify both the exact value and the strength of the interpretation. Sources live under `cache/`; row indices are zero-based. Do the eight unresolved checks include everything decisive for the proposed next action?

Make one documented assumption change using a copy of `probe.json` and the README command. Check that the expected calculations change and identify what should stay unresolved. Then inspect the contradiction and omission cases in `outputs/controls.json`. Those cases are synthetic, authored controls; they do not establish extraction recall or completeness.

Record a substantive disagreement with the interpretation or a reason it survives your challenge. Do not resolve disagreement by merely changing a readiness label or accepting a quote because it is present.

## Review record

Fill a copy of `review-template.json` with your name, relevant expertise, relationship to the build, packet fingerprint, commands, traced claims, assumption change, disagreements and disposition. Leave unperformed checks explicit. An attested identity does not authenticate the reviewer. A completed form is feedback to reconcile; it does not automatically approve a site, rule change or professional claim.
