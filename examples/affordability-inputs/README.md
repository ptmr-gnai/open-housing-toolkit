# Explicit illustrative rental programs and reference excerpts

These inputs exercise the [conditional comparison module](../../housing_benefit/README.md).
They are not professional housing proposals or verified plans for the linked real lot.

- `request.json`: Program A has 24 explicit two-bedroom homes; Program B has 36.
  A includes 16 lower-rent offers versus B's 8. Each input has an assumption rationale.
- `higher-utilities.json`: changes A's lower-rent tenant utilities from $100 to
  $250 monthly. The gross cost crosses the hypothetical lower-income profile's budget.
- `reference-source/`: selected 2025 income/rent rows from the NYC RER guide,
  original-document URL/hash, printed page, column mapping and extraction receipt.

The source PDF was checked during extraction but is not bundled. Normal offline
verification parses and hashes the selected excerpt; it does not independently
re-extract the PDF. The external re-extraction command and limits are in the guide.

All programs are illustrative initial rents expressed in 2025 USD, with proposed
restriction durations and unknown delivery. Profiles are hypothetical, using rounded
published income references. Cost/bedroom matching is not eligibility, availability,
regulatory compliance or a community-benefit estimate.

The retained real-site analysis is used for identity and unresolved current-use
context. These 24/36-home programs are not derived from or physically reconciled to
its 40,000-sf area budget or the separate building render. No geometry is updated.
