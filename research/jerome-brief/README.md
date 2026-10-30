> Historical experiment. User setup/analysis must not run its build script or
> regenerate this snapshot. Use the read-only validator for inspection; use the
> current lot workflow for new work, with outputs in a fresh local runs/ folder.

# 1337 Jerome Avenue review benchmark

Start with brief.md and review-protocol.md. This reconstructs HPD's actual public
homeownership project for independent advisor critique. It is not an RFP response,
a bidder nomination, professional design, financing approval or causal estimate.

## Offline replay

Python 3.10+, standard library only for building and validation:

```sh
python research/jerome-brief/build.py
python research/jerome-brief/validate.py
python -m unittest discover -s research/jerome-brief/tests -v
```

From inside this directory, omit research/jerome-brief/ prefixes. The authoring
script author_case.py records the extraction definitions; do not rerun it over a
modified case.json. build.py binds that authored DSL to source bytes, performs the
supported named arithmetic and generates the brief, claim trace, requirement
matrix and financial input contract. It is not a zoning or underwriting compiler.

The case preserves existing, conditional No-Action, agency current-zoning and
agency potential-rezoning scenarios. Agency unit/height estimates remain agency
claims; only their differences and illustrative income budgets are calculated.
Every numerical passage uses a checked extraction contract. Unknowns remain null.

## Review forms and versioning

reviews/A.json and reviews/B.json are separate pending templates. Advisors may
reply in prose using review-protocol.md; a project owner or agent can transcribe
responses with attribution and confirm the transcription with the reviewer.
Fill names, expertise, review date, independent-first-pass attestation, disposition
and all answers. Mark questions outside expertise explicitly. Never manufacture
reviewer answers or signatures. Project owner must verify attribution: this code
does not authenticate identities or prove independent review occurred.

The fingerprint binds source receipts, source bytes, authored values/assumptions,
requirements, claim scopes, arithmetic and the builder's code (including rendered
interpretation and review questions). A modified packet invalidates old forms.
Untouched pending templates follow a new build; edited or completed reviews are
preserved and become stale. Material issue closure needs a corrected evidence
packet; merely changing an issue to closed is rejected. Supplied financial input
values also prevent a rebuild from silently replacing them with nulls.

```sh
python research/jerome-brief/validate.py --gate advisor_packet
python research/jerome-brief/validate.py --gate second_site_workflow
python research/jerome-brief/validate.py --gate agency_proposal
```

Allowed gates exit 0, blocked gates exit 2, technical failures exit 1. The present
snapshot allows expert review, blocks progression based on advisor acceptance
until real feedback exists, and blocks agency/development recommendations. The
professional gates are tied to this unresolved snapshot. Resolve them by creating
a new evidence-backed version, rather than changing their labels to resolved.

## Sources and licenses

cache/ contains original bytes, exact URL/timestamp/hash receipts, parsed HTML,
and PDF text extracted with pdftotext -layout. Failed acquisitions are retained.
The appendix URI attempted first returned 404; its resolved official link is a
separate receipt. No empty environmental query clears the site. The collector
refuses to overwrite the snapshot; follow-up request lists retain discovered URLs.

The collector imports ../source-audit/audit.py in the repository. The review ZIP
contains evidence and replay code, not that sibling live-collection dependency.
Use the full repository for future live collection. Network refresh requires a new
versioned snapshot and review reset; byte-identical replay uses no network/models.

Code MIT; original documentation CC BY 4.0 under repository licenses. Upstream
agency documents/data remain subject to their own terms. Retention for this review
does not establish blanket rights to redistribute upstream material publicly.
