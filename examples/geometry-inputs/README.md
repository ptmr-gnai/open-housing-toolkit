# Retained parcel geometry and exploratory scenario inputs

NYC DCP MapPLUTO polygon for BBL **2028710002**, recorded address
**1240 Edward L Grant HWY**. `parcel-source/` preserves exact response bytes,
layer and DCP_GIS item metadata, exact query, retrieval timestamps, version and SHA
receipts. Source terms remain NYC's; the polygon is a mapped tax lot, not a survey.

`all-nonresidential-ground.json` assumes a 75×100-ft ground plate and five
65×100-ft upper plates, 14-ft ground-floor height and 10-ft upper-floor heights.
Its footprint placement is an author choice near the mapped parcel centroid,
not a match to the photographed building. Its dimensions were selected to total
40,000 sf. This constructs a numerical consistency example, not a design prediction.

`mixed-ground-allocation.json` retains the same geometry and changes only the
ground-floor nonresidential fraction from 1 to 0.8, explicitly to reproduce the
model's 6,000-sf nonresidential allocation. This is not a tested mixed-use layout.

Footprint positions use the coordinate transform declared by the geometry module,
and bind the exact parcel response SHA. Read the individual rationales and
[specification](../../docs/specs/geometry-grounding.md).
