# Goal-seeking nonhousing sites

A functional v1 connects broad discovery, housing-record review, monthly zoning
reconciliation, explicit search targets, rental finance, deeper parcel evidence
and the existing area/geometry modules. See [findings](report.md),
[practitioner guide](../../docs/guides/discover-sites.md), and
[financial case studies](../modeling-v1/README.md).

Run `python research/site-goal-search/validate.py` for read-only offline verification.
The five complete retained packages are indexed in [case-manifests.json](cases/case-manifests.json).
Four additional sensitivity records retain full input requests and expected outputs
for numerical replay; they are not presented as complete source packages.

Start with [Jerome baseline](cases/cost-comparison/left/packet.md),
[Hunts Point baseline](cases/hunts/packet.md),
[cost comparison](cases/cost-comparison/packet.md),
[deeper investigation](cases/deeper-evidence/packet.md), and
[selected-program area handoff](cases/area-handoff/packet.md).
The [geometry packet](cases/geometry/packet.md) is a schematic consistency case.

Code MIT; original prose CC BY 4.0. Retained public source material retains its
publisher terms. Packages intentionally preserve repeated input ancestry so each
handoff is independently verifiable; source bytes are not silently updated.

Folders named `imported/` preserve raw capture archives. Their old packet bytes
are retained as provenance; they are not independent current workflow packages,
and their historical relative back-links can refer to the original capture layout.
Use the verified current packets linked above for navigation and analysis.
