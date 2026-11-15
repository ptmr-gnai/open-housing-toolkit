# Public-source coverage

The collection is bounded. Fetched source families and successful joins are
listed separately from resources only located or deferred. Coverage refers to
implemented queries, not complete history, current occupancy or professional
clearance. Exact URLs, retrieval dates, source bodies and hashes are in case
receipts; later retrieval does not establish historical byte equivalence.

| Resource | What was actually retrieved/joined | Material limits |
| --- | --- | --- |
| PLUTO (64uk-42ks) |3,164 point-defined records; full implemented primary collection; supplemental residential area and all recorded district/overlay/special fields for every BBL | Recorded descriptors, not fresh parcel/zoning polygon intersections or current field survey; source version26v2 |
| ZAP (2iga-a6mk and hgx4-8ukb) | Bounded exact-BBL links and referenced project rows for every inventory lot | Historic identity changes/unlinked projects can be missed; application status is not construction or occupancy |
| City-Owned/Leased Property (fn4k-qyk2) | Bounded uses lookup for every inventory lot | Use/lease signal is not proof of public title, availability or site control |
| Official Zoning Resolution and DOF class guide | Seven source pages retained byte-for-byte for scoped general-use/current-use rules | Rules are incomplete parcel interpretation; special provisions, type/bulk conditions and effective maps need review |
| MTA Subway Stations (39hk-dx4f) | All 496 returned GTFS stop records, metadata and counts before/after; nearest point computed for each lot | Shared station IDs across platforms; no entrance/walking/live-service inference |
| DCP Mapping Portal IBZ polygons | Publisher organization, service item/layer, count, all returned WGS84 polygons and metadata checks; point overlap for every lot | Point overlap is not whole-parcel intersection; outside is not policy clearance |
| NYCEDC industrial policy page | Source HTML and retrieval receipt retained alongside IBZ context | Policy commitment is not a general legal prohibition; current support/process still requires review |
| DCP Fast Tracker lots | Exact-BBL batches across all3,164 lots;3,161returned;40 source-version rows | Some vintage data are older than current PLUTO; missing/unflagged is not eligibility or environmental clearance |
| DOB BIS (ic3t-wcy2) / NOW (w9ak-ipjd) | Four full parcel investigations plus broad 969-lot housing-signal review; raw rows, fields, metadata and coverage | Legacy job/document rows and NOW filings are not completed projects or current lawful housing; failures remain unknown |
| HPD violations (wvxf-dwi5) | Four exact-BBL deeper queries; zero returned rows | No occupancy clearance or complete-housing-coverage inference |
| HPD registrations (tesw-yqqr) / affordable production (hg8x-zxpr) | All 969 recorded-nonhousing lots queried in bounded exact-key batches, with metadata checks and raw receipts | Registration needs exact borough/block/lot derivation, not assumed BBL field; neither dataset covers all housing; zero rows do not rebut DOB signals |

## Additional useful resources and remaining adapters

- **DCP Zoning Tax Lot Database (fdkv-4t4z):** monthly recorded zoning-by-BBL data,
  found through the BetaNYC registry and implemented as a separately verified
  [reconciliation stage](../../src/housing_zoning_review/README.md). It can challenge PLUTO/Fast Tracker vintages; still not a
  complete legal interpretation or a fresh whole-parcel survey.
- **DCP Green Fast Tracker:** maintained public tool/source-layer catalogue. Its
  aggregate context is reused rather than rebuilding every environmental overlay.
  Process guidance still requires project-specific and field information; Type II
  treatment would not grant zoning permission. No claim is made that this is what
  the user meant by “clear zones.”
- **MapPLUTO parcel polygons/building footprints:** useful for exact spatial
  reconciliation, lot shape, assembly and geometry. Not collected as a complete
  new 3,164-parcel geometry layer here. Existing geometry module needs explicit
  source/survey inputs and cannot turn an area ratio into physical fit.
- **MTA schedules/entrances, pedestrian network and LEHD LODES:** station points
  are implemented; walking/service/job-access adapters remain separate work.
- **ACRIS/DOF sales and ownership:** useful for price/title/transaction diligence;
  existing source audit found working public records. No owner willingness,
  sale availability or automatic land valuation is inferred in this case.
- **HPD/HDC, HUD and Furman program/subsidy resources:** useful for financing and
  housing protections; current public datasets do not establish project eligibility,
  actual commitments or a financing award.

The [earlier ten-source audit](../source-audit/report.md) and
[community-benefit research](../community-benefit/report.md) remain the broader
resource base. These case queries reuse that work; they do not claim exhaustive
public-data coverage. Original publishers retain data/document terms.
