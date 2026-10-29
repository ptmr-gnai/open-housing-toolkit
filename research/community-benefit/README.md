# Housing, transit and community-benefit research

[Read the research memo](report.md).

Broad orientation across 25 agency/research/tool references, with 9 candidate
method modules. This is not a systematic review, an implemented community-benefit
model, or professional validation. Two research agents and the lead contributed.

- `sources.json`: URLs, source types, uses, inspection extent and limitations.
- `retrievals.json`: five directly retrieved documents/pages with exact byte hashes.
  Source bytes are cached locally under ignored runs/ and are not publicly bundled.
- `methods.json`: explicitly unimplemented backlog and proposed impact-record fields.
- `validate.py`: reference/backlog metadata consistency; no semantic accuracy claim.

```sh
python research/community-benefit/validate.py
```

Start with a distributional benefits/harms comparison, supported by NYC's existing
reporting structure. Keep descriptive context, conditional program arithmetic,
behavioral projections, causal evidence, commitments and value judgments distinct.
No automatic maximal-benefit score is justified. No housing, transit-routing,
econometric or image-generation model was executed in this research slice.

The subsequent [implementation proposal](../../docs/specs/community-benefit.md)
turns this research into a bounded plan under the [project tenets](../../docs/tenets.md).
It remains proposed; the research catalogue is not an implemented benefit engine.

A later [conditional housing-cost slice](../../housing_benefit/README.md) implements
a bounded subset of the proposal. The research catalogue records its original
unimplemented backlog and is not the current capability index.
