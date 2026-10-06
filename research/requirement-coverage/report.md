# Proposal requirement coverage and omission checks

6 October 2026. This slice adds an executable coverage and proposal-packet checker for the dated 97 West 169th Street and St Ann’s Avenue HPD solicitations. It catches omissions from a declared complete packet and attempts to silently drop requirements from the authored inventory. It also preserves requirements changed by addenda. Full semantic coverage remains pending.

The hypothesis was narrow: a source-linked inventory, checked against an independently enumerated source surface, can expose known omission failures and prevent an incomplete evidence pack from being promoted to submission readiness. We tested that engineering behavior with deliberate faults; we have not measured practitioner usefulness or automatic extraction accuracy.

## What the sources taught us

| Source | Consequence for the playbook |
| --- | --- |
| 97 West 169 RFP p28: Form G; pp16,28: Excel requirement | Removing Form G from a declared complete packet is detected. Removing it from the inventory is also detected against the pinned baseline. A filename alone does not establish compliant content. |
| 97 West 169 Addendum 3 p2 Q2 | Form E4 is obsolete, but relevant commercial management experience remains conditional evidence in the respondent’s preferred format. Deleting both would lose an obligation. |
| St Ann’s RFP p23 | Experience forms D1–D3 remain required even when the respondent must enter “None.” Lack of experience does not waive the forms. |
| St Ann’s Addendum 2 pp3–4 Q12,Q14; RFP p25 | Identify the general contractor in the proposal. Green Communities certification belongs after selection; the submission still explains its sustainability plan. The softer requested overlay material remains separately labeled. |
| St Ann’s Addendum 1 p4 Q18 | Disregard the former multiple-site instruction; do not force obsolete materials into a packet. |

Page numbers are PDF pages in the retained source files. Exact quotes and fingerprints accompany the machine-readable declarations and review queue.

## What is implemented

A separate scanner enumerates 150 text review units: 79 for West 169 and 71 for St Ann’s. These are checkbox/paragraph segments and addendum question-start anchors, not atomic requirements. The authored map contains 33 scoped obligations and six addendum operations. The inventory was pinned in Git before the omission tests.

Each scanned unit stays visible, whether mapped or awaiting expansion. The checker rejects missing anchors, broken mappings, stale source passages, silent baseline deletions or reclassifications, and unapplied addendum operations. Conditional waivers need reviewed applicability facts backed by retained, hash-checked evidence. File presence and accepted content review are separate states. Reviews bind to the precise requirement, payload and rule contract; they become stale when those change.

The export combines applicant eligibility with packet coverage. An evidence pack can be exported with unresolved states disclosed. A submission-readiness claim exits with code 2 while blockers remain. No actual proposal or applicant records were supplied, so actual completeness remains unknown rather than a claim that an applicant has missing documents.

## Validation and limits

All 27 coverage tests pass. Eleven deliberately constructed fault controls exercise omissions, obsolete requirements and phase changes. Output replay is byte-identical. These controls are known regression fixtures, not an independent benchmark or an estimate of recall/precision. Mock accepted reviews and workbook files are explicitly synthetic.

All 150 source review units await semantic review. Nested clauses, cardinality, signatures, field-level form requirements, cross-page continuations, graphics and referenced appendices are not fully expanded. The counts must not be used as a completeness percentage. Basic Excel container checks do not validate agency templates, formulas or substantive content. Review identity is attested, not authenticated. Historical archive packaging remains recorded; exact historical byte equivalence is uncertified.

The next useful slice is to fully expand and review one bounded submission tab, including its referenced forms and per-principal rules, then test omission controls at that finer level. Independent advisor review can challenge the obligation map when available. We still need a real practitioner task and baseline before claiming time savings or usefulness.
