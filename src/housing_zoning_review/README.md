# Monthly zoning-tax-lot reconciliation

Reconcile a verified broad discovery or dwelling-review package against NYC DCP's
published monthly Zoning Tax Lot Database (`fdkv-4t4z`). Preserve the parent under
parent/ and keep every lot. A source agreement is a record comparison, not a
professional entitlement or parcel-map interpretation.

```sh
python -m housing_zoning_review collect --parent runs/my-discovery-or-review --out runs/my-zoning-review
python -m housing_zoning_review verify --run runs/my-zoning-review
```

The fixed provider registry captures metadata before/after and exact BBL batches
for all upstream lots, with raw bytes, queries, attempts, timestamps and hashes.
Source schema/key type, query universe, row caps and update/version consistency
are checked. Failed, missing and duplicated rows remain separate review states.
Supply `--ca-file PATH` for a valid trusted CA bundle where required; TLS stays on.

The review compares all four recorded districts, up to three special districts,
overlays and limited-height signals. Missing/unstable records or differences move
the investigation path to special/unresolved review without overwriting the
parent's district values or its earlier housing/use observations. It does not
silently choose one vintage as legal truth. The source's published version and
metadata update time remain separate from retrieval dates.

The resulting ir.json retains earlier dwelling/public-context fields and can feed
[site goal search](../housing_site_search/README.md). packet.md/packet.html explain
coverage; zoning-records.json and receipts.json retain exact row references.
`finalize --run PATH` can validate a fully captured **unsealed** run after an
interruption; it performs no new collection and refuses completed manifests.

No spatial re-intersection, legal envelope, new development program, review
approval, availability or feasibility is inferred. Publisher source terms apply.

For a new compatible reviewed parent with the identical lot universe, reuse saved
raw capture without re-fetching: `replay --parent NEW_PARENT --capture CAPTURE
--out NEW_RUN`. The command recognizes supported capture bindings, validates raw
source/query hashes and paths, copies only retained evidence, and recomputes all
current interpretations. It does not certify the older analysis under a new
runtime or change its manifest. Retrieval timestamps remain original.
