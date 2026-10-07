# One conclusion end to end

The fixed site is 1240 Edward L Grant Highway, BBL 2028710002. This experiment tests the October 3, 2026 cached evidence behind an occupancy-first investigation conclusion. It does not test candidate selection or establish current site facts, professional acceptance or feasibility.

Python 3.10+ and the standard library suffice. From the repository root:

```sh
python research/conclusion-probe/validate_probe.py
python -m unittest discover -s research/conclusion-probe/tests -v
python research/conclusion-probe/inspect_conclusion.py --purpose challenge-pack
python research/conclusion-probe/inspect_conclusion.py --purpose acquisition-or-design
```

The last command intentionally exits 2. A permitted investigation conclusion is explicitly provisional author judgment, suitable for challenge; it is not professional clearance.

Start with `outputs/conclusion.md`, then `outputs/baseline.json` and `outputs/trace.md`. The JSON graph distinguishes observed facts, derived calculations, assumptions, authored judgment and unknowns. Exact row/field passages, source receipts and version limits accompany facts. Assumptions resolve to the embedded configuration, including modified configs. Only concept A is included. The calculation functions are reused from the original pipeline; the original outputs and frozen retrospective runs are untouched.

`spec.json` and `precommit.json` were committed at 4a7176f before implementation and outcomes. The experiment author already knew the original site and its baseline calculations. Eleven cases include the unchanged baseline and ten known fault/sensitivity controls. They are regression controls, not a blind benchmark. Removing occupancy or finance checks is rejected against the authored pinned policy; this does not discover unknown requirements.

`conclusion_engine.py` forms the dependency closure and provisional disposition. `controls.py` makes explicitly synthetic source revisions in temporary copies, preserving parent hashes. It compares synthetic competing assertions only when already linked to this BBL and a supported field. It can withhold conflicting or differently dated claims; it does not extract contradictions from arbitrary prose or choose the authoritative winner. Existing calculations retain their stated primary-source basis and are marked blocked when a conflicting input affects them.

`run_probe.py` writes all output variants and an input/output manifest. `validate_probe.py` checks frozen input hashes and reruns to compare every output byte. Running `run_probe.py` overwrites this experiment’s outputs; use `--out /tmp/new-conclusion-run` for exploration. Never rewrite precommit to make a check pass.

To challenge a numerical assumption, copy `probe.json` to `work/config.json`, edit the value and rationale, and run:

```sh
python research/conclusion-probe/inspect_conclusion.py --config work/config.json --out work/rebuilt
```

Supply `--prior-basis` with the baseline fingerprint to demonstrate that the old interpretation basis becomes stale. The fresh interpretation remains unreviewed. Reviewers cannot supply a flag to clear unknown site requirements.

The ZIP includes original cached bodies/receipts, pinned configuration, arithmetic dependency, experiment code, outputs and a per-file digest manifest. It contains no paid-model or network dependency. Follow `reviewer-protocol.md` and retain real review answers in a distinct file. Technical replay by the author is complete; reproduction and substantive challenge by an unfamiliar human remain pending. Code is MIT; original documentation follows the repository license. Agency material retains upstream terms.
