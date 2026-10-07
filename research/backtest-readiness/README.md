# Assumptions review and real-project backtest readiness

The fresh-context AI review is at `../conclusion-probe/reviews/agent-assumptions-review.md`. Its disposition is revise; it does not provide human expert acceptance. `review-disposition.json` preserves the reviewed baseline fingerprint, verified omitted DOB record, and the full modeled non-debt capital calculation. Original experiment outputs remain unchanged.

`cache/` and `receipts.json` retain a bounded October 7 acquisition of later real-project references. These files are **reveal/calibration evidence**, not contemporaneous analyst inputs. 425 Grand Concourse is already known to the curator, so it is not a blind holdout. `report.md` defines what to test next and which comparisons remain unsupported.

Nine requests were recorded. Eight returned bytes; the ULI case URL returned a login shell, and the award page only links to the case. The government PDF mirror returned 403. Neither the login shell nor the award page supplies the detailed finance table. A search-indexed third-party copy was observed but not promoted into verified financial inputs. Do not treat HTTP 200 or a mirrored search result as recovered underwriting.

Sources are retained with exact URLs, timestamps, hashes and text transformations. Current pages can report historical milestones without proving exact pre-cutoff byte equivalence. Project descriptions also mix planned and retrospective wording. The opening announcement is evidence of the publicly reported opening, not a financial audit, final rent roll, resident-outcome study or complete submitted proposal.

Run `python research/backtest-readiness/validate.py` from the repository root to verify source/derived-text hashes, required source anchors, review evidence and recorded arithmetic. Python standard library only. This is a receipt/interpretation-boundary check, not a test of backtest performance. `manifest.json` binds the separate review, disposition, plan and reference files. Retain the original failure record when implementing a new model version.
