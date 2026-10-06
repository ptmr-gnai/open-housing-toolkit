# Bounded requirement coverage component

Run from the repository root with Python and the repository development dependencies installed:

```sh
python research/requirement-coverage/build_coverage.py
python research/requirement-coverage/validate_coverage.py
python -m unittest discover -s research/requirement-coverage/tests -v
python research/requirement-coverage/coverage_check.py --case west169 --purpose evidence-pack
python research/requirement-coverage/coverage_check.py --case west169 --purpose submission-readiness-claim
```

The last command intentionally exits 2: actual evidence and semantic review are pending. Optional `--packet` and `--profile` JSON inputs bind to the packet and applicant components respectively. See `fixtures.py` for synthetic examples, never credentials.

`scan.py` independently enumerates source anchors; `registry.json` maps a partial, human-authored obligation inventory to them. `precommit.json` pins the baseline authored inventory and source manifest. `coverage_engine.py` checks source accounting, addendum operations and evidence/review state. `coverage_check.py` joins this with `research/eligibility-gates/` at export. `build_coverage.py` produces compact results and a manifest; `validate_coverage.py` checks hashes and rebuilds to compare every output byte.

Do not rerun `author.py` to bless a failed test or silently update the precommit. A changed source or interpretation needs an explicit reviewed baseline revision, preserving the old baseline and its reasons in Git. Source text, PDF hashes and quotes live in the eligibility source manifest; original West 169 inputs retain their repository paths.

Read [report.md](report.md) and [outputs/review-queue.md](outputs/review-queue.md) for scope. 150 review units, 33 obligations and six addendum operations do not establish completeness. All semantic review remains pending. The fixture workbook tests a container only. Code is MIT; original documentation follows the repository data license and agency sources retain upstream terms.
