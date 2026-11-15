---
name: discover-housing-sites
description: Discover and compare housing investigation candidates across a bounded NYC lot inventory using explicit exploratory FAR assumptions, public-use and application context, then hand shortlisted Bronx lots to deeper parcel analysis.
---

# Discover housing sites

Use this for an area search or a comparison of site-screening assumptions. For an
already selected lot, use [housing-investigation](../housing-investigation/SKILL.md).

Collect the geography, decision question, scenario assumptions and selection
criteria. The supplied probes are analyst experiments, not default planning policy.
If inputs are absent, explain the choices and help the user choose; preserve
uncertainty rather than inventing legal zoning changes or financial commitments.

Read [the execution reference](references/runbook.md) when running the module.
It covers collection, saved-source screening, sensitivity comparison and handoff.
Use the module CLI and a fresh local runs/ directory for each stage.

The baseline uses the larger of recorded residential and affordable residential
FAR only as a screening proxy. Do not claim the affordable branch applies, infer
vacancy from zero recorded homes, call home-equivalents buildable homes, or present
conditional rankings as approval probabilities or community-benefit scores.

Return coverage counts, shortlisted and held lots, reasons, exact assumptions and
missing diligence. A known-lot handoff preserves the discovery evidence and starts
with an evidence-only request; assumed FAR does not become a building program.
