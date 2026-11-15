# Cross-source dwelling review

457 recorded nonhousing lots reviewed. Every base inventory lot and its original classification remains retained.

| Returned-field review | Lots |
| --- | --- |
| housing_signal_coverage_unknown | 185 |
| no_positive_returned_housing_signal | 204 |
| positive_returned_housing_signal | 68 |

**Interpretation:** positive historical unit fields or HPD registration/program records require reconciliation. No positive returned signal does not establish no housing, no occupants, vacancy or a clean site.

## Source coverage

| Source | Per-lot query status | Lots |
| --- | --- | --- |
| hpd_registrations | query_complete_empty | 452 |
| hpd_registrations | query_complete_rows | 5 |
| hpd_production | query_complete_empty | 454 |
| hpd_production | query_complete_rows | 3 |
| dob_now | query_complete_empty | 309 |
| dob_now | query_complete_rows | 148 |
| dob_bis | failed | 200 |
| dob_bis | query_complete_empty | 98 |
| dob_bis | query_complete_rows | 159 |

## Positive returned signals

| BBL | Address | Returned housing signals |
| --- | --- | --- |
| 2024630040 | 112 EAST 167 STREET | 37 |
| 2024660011 | 116 EAST 169 STREET | 7 |
| 2024660026 | 1275 GRAND CONCOURSE | 6 |
| 2024810023 | 1275 WALTON AVENUE | 8 |
| 2024960064 | RIVER AVENUE | 37 |
| 2025140040 | 1130 OGDEN AVENUE | 2 |
| 2025150138 | 1227 WOODYCREST AVENUE | 1 |
| 2025160012 | 1192 OGDEN AVENUE | 10 |
| 2025160051 | 1181 NELSON AVENUE | 2 |
| 2025160061 | 1171 NELSON AVENUE | 4 |
| 2025170001 | 75 WEST 168 STREET | 17 |
| 2025170026 | 96 WEST 169 STREET | 4 |
| 2025170027 | 94 WEST 169 STREET | 3 |
| 2025190025 | 1287 SHAKESPEARE AVENUE | 2 |
| 2025220057 | 1392 OGDEN AVENUE | 1 |
| 2025220105 | 1395 PLIMPTON AVENUE | 4 |
| 2025370007 | UNDERCLIFF AVENUE | 2 |
| 2027820001 | 353 EAST 169 STREET | 6 |
| 2027820013 | 1316 FINDLAY AVENUE | 15 |
| 2027820058 | 1329 TELLER AVENUE | 1 |
| 2027830020 | 1342 COLLEGE AVENUE | 14 |
| 2027830041 | 314 EAST 170 STREET | 2 |
| 2027840002 | 1408 COLLEGE AVENUE | 2 |
| 2027850002 | 273 EAST 169 STREET | 5 |
| 2028190029 | 178 MT EDEN PARKWAY | 6 |
| 2028200059 | 1509 MORRIS AVENUE | 2 |
| 2028200060 | 1507 MORRIS AVENUE | 2 |
| 2028210011 | 1526 GRAND CONCOURSE | 9 |
| 2028240034 | 155 EAST 173 STREET | 1 |
| 2028300035 | 220 EAST 170 STREET | 2 |
| 2028310056 | 218 EAST 170 STREET | 2 |
| 2028330037 | 161 EAST 170 STREET | 10 |
| 2028360035 | 105 ROCKWOOD STREET | 2 |
| 2028370009 | 1570 WALTON AVENUE | 2 |
| 2028400005 | 1328 JEROME AVENUE | 6 |
| 2028400065 | 152 MARCY PLACE | 6 |
| 2028420006 | 2 EAST 170 STREET | 2 |
| 2028420015 | 46 EAST 170 STREET | 1 |
| 2028420042 | 90 EAST 170 STREET | 2 |
| 2028420047 | 110 EAST 170 STREET | 2 |
| 2028420051 | 126 EAST 170 STREET | 2 |
| 2028430005 | 1412 JEROME AVENUE | 1 |
| 2028430012 | 1430 JEROME AVENUE | 2 |
| 2028430040 | 1426 TOWNSEND AVENUE | 2 |
| 2028430069 | 101 EAST 170 STREET | 4 |
| 2028450040 | 70 EAST MT EDEN AVENUE | 2 |
| 2028460021 | 1546 JEROME AVENUE | 1 |
| 2028490005 | 1712 JEROME AVENUE | 9 |
| 2028550028 | 1261 JEROME AVENUE | 1 |
| 2028560001 | 21 EAST CLARKE PLACE | 37 |
| 2028560011 | 1342 INWOOD AVENUE | 10 |
| 2028560019 | 1364 INWOOD AVENUE | 10 |
| 2028560023 | 1376 INWOOD AVENUE | 17 |
| 2028570001 | 1400 CROMWELL AVENUE | 2 |
| 2028577501 | 1477 MACOMBS ROAD | 2 |
| 2028580009 | 10 WEST 172 STREET | 6 |
| 2028580019 | 1477 JEROME AVENUE | 2 |
| 2028590051 | 1545 JEROME AVENUE | 8 |
| 2028650134 | 1600 MACOMBS ROAD | 74 |
| 2028710094 | 1361 CROMWELL AVENUE | 16 |
| 2028720082 | 1401 CROMWELL AVENUE | 2 |
| 2028720093 | 49 WEST 170 STREET | 2 |
| 2028720218 | 81 WEST 172 STREET | 2 |
| 2028760008 | 108 WEST 174 STREET | 2 |
| 2028760033 | 69 FEATHERBED LANE | 1 |
| 2028760064 | 1586 UNIVERSITY AVENUE | 4 |
| 2028760162 | 1676 NELSON AVENUE | 2 |
| 2028870009 | 1322 CLAY AVENUE | 1 |

See signals.csv and review.json for every exact source pointer, filing date/status and query coverage. Original packet and complete context remain under discovery/.

- Exact BBL or explicit borough/block/lot joins can miss historical lot changes, unlinked or unrecorded housing.
- Historical existing/proposed units and filing status do not establish current occupancy or completed/lawful housing.
- No positive returned signal is a literal query result; empty or missing numeric fields do not establish no housing.
- Before/after update metadata detects some drift; these APIs are not transactional snapshots.
