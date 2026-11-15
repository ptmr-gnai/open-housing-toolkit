# Broad nonhousing discovery and source challenges

This case corrects the earlier auto/parking and extra-FAR experiment. Start with
all recorded nonhousing sites, classify their general zoning-use paths, then add
source context and optional modeling. Existing residential capacity is useful;
a site does not need an increment over an arbitrary assumed FAR to enter discovery.

- [Method and findings](report.md)
- [Public-source coverage and remaining resources](sources.md)
- [Broad discovery module](../../src/housing_site_discovery/README.md)
- [Cross-source dwelling review](../../src/housing_site_review/README.md)
- [Jerome discovery packet](cases/jerome/packet.md)
- [Hunts Point discovery packet](cases/hunts/packet.md)
- [Jerome four-source housing review](cases/reviews/jerome/packet.md)
- [Hunts Point four-source housing review](cases/reviews/hunts/packet.md)
- [Case counts and coverage](cases/findings.json)

The retained broad cases cover3,164 recorded lots, including969 classified as
recorded nonhousing and visible housing/uncertainty queues. The added four-source review finds 117
lots with returned housing-history/program/registration signals, 506 literal no-positive
returns and 346 coverage-unknown lots; these are not current-occupancy findings. They are bounded
recorded-point windows, not all Bronx land or a viable-site count. Four selected
lots also have independently verified deeper parcel investigations under cases/parcels.

Read-only offline replay: `python research/nonhousing-discovery/validate.py`.
New analyses and changed inputs go into fresh ignored runs/ folders; never rebuild
these source snapshots or rewrite manifests. Engineering checks do not establish
parcel entitlement, current occupancy, physical fit, financing or professional
acceptance. Earlier research/discovery-v1 remains unchanged as experimental history.

Code MIT; original documentation CC BY 4.0. Public-source snapshots retain publisher
terms; see [DATA-LICENSES](../../DATA-LICENSES.md).
