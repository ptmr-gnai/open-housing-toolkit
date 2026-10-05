# Document assessment run

This is a bounded retrospective assessment of an HPD solicitation, not an economic
feasibility model, certified historical backtest, or independent professional review.

## Stage boundaries

1. `rubric.json` and input fingerprints in `precommit.json` were committed before
   the fresh analyst context started. The curator already knew the later outcome;
   the analyst received only the controlled input folder and task. Prior model
   knowledge and undeclared reads cannot be ruled out by this instruction boundary.
2. The analyst writes `assessment.md`, `claims.json`, and `access-log.json`.
3. `validate.py` checks unchanged inputs/rubric, claim source allowlist, exact-page
   quote presence, dependency references/cycles, declared reads, and frozen bytes.
   It does not prove that the quote entails the claim, that the claim ledger covers
   every prose assertion, or that a quoted number was interpreted correctly.
4. `freeze.py` refuses overwrite and records output hashes. Commit that receipt and
   original output before the evaluator opens the later agency reference in this run.
5. Evaluation lives in separate artifacts. No post-reveal rewriting of the original
   assessment. Any future corrected assessment must use a distinct version/run.

The rubric has a separately recorded locator erratum. This does not change any
criterion. Claims of actual user usefulness, time savings, historical certification,
professional approval, financing readiness, or construction delivery remain blocked.

## Checks

From the repository root:

```
python research/retrospective-run/validate.py
python -m unittest discover -s research/retrospective-run/tests -v
python -m unittest discover -s research/benchmark-case-search/tests -v
```

Do not re-run `freeze.py` on a completed run. The frozen case-input manifest still
says `prepared_not_run`: it describes the packet at preparation time. The separate
run receipt and report carry the experiment status without changing the inputs.

Read `report.md` for the result and limits. Advisors remain needed to judge whether
the information improves an actual next decision.
