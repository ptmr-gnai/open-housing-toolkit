# Cross-source dwelling review

512 recorded nonhousing lots reviewed. Every base inventory lot and its original classification remains retained.

| Returned-field review | Lots |
| --- | --- |
| housing_signal_coverage_unknown | 161 |
| no_positive_returned_housing_signal | 302 |
| positive_returned_housing_signal | 49 |

**Interpretation:** positive historical unit fields or HPD registration/program records require reconciliation. No positive returned signal does not establish no housing, no occupants, vacancy or a clean site.

## Source coverage

| Source | Per-lot query status | Lots |
| --- | --- | --- |
| hpd_registrations | query_complete_empty | 511 |
| hpd_registrations | query_complete_rows | 1 |
| hpd_production | query_complete_empty | 511 |
| hpd_production | query_complete_rows | 1 |
| dob_now | query_complete_empty | 374 |
| dob_now | query_complete_rows | 138 |
| dob_bis | failed | 165 |
| dob_bis | query_complete_empty | 113 |
| dob_bis | query_complete_rows | 234 |

## Positive returned signals

| BBL | Address | Returned housing signals |
| --- | --- | --- |
| 2027140004 | 948 TIFFANY STREET | 3 |
| 2027150053 | 989 WESTCHESTER AVENUE | 1 |
| 2027220063 | 877 SOUTHERN BOULEVARD | 9 |
| 2027240190 | 947 SOUTHERN BOULEVARD | 8 |
| 2027320025 | 854 SOUTHERN BOULEVARD | 2 |
| 2027370061 | 1102 BURNETT PLACE | 1 |
| 2027370065 | 1114 BURNETT PLACE | 2 |
| 2027370075 | 1127 LONGWOOD AVENUE | 1 |
| 2027370076 | 1125 LONGWOOD AVENUE | 2 |
| 2027370095 | 840 BARRY STREET | 4 |
| 2027370115 | 1141 LONGWOOD AVENUE | 1 |
| 2027380036 | BARRETTO STREET | 4 |
| 2027390015 | 1201 LAFAYETTE AVENUE | 6 |
| 2027400075 | 940 GARRISON AVENUE | 5 |
| 2027400100 | 1241 LAFAYETTE AVENUE | 4 |
| 2027420003 | 940 SOUTHERN BOULEVARD | 4 |
| 2027420030 | 980 SOUTHERN BOULEVARD | 1 |
| 2027430005 | 1014 SOUTHERN BOULEVARD | 2 |
| 2027430006 | 1026 SOUTHERN BOULEVARD | 2 |
| 2027490057 | 979 ALDUS STREET | 2 |
| 2027550058 | 941 LONGFELLOW AVENUE | 8 |
| 2027550107 | 955 WHITTIER STREET | 2 |
| 2027550131 | 970 LONGFELLOW AVENUE | 3 |
| 2027590042 | 1360 BRUCKNER BOULEVARD | 1 |
| 2027610001 | 870 HUNTS POINT AVENUE | 2 |
| 2027610006 | 878 HUNTS POINT AVENUE | 2 |
| 2027610169 | 1350 GARRISON AVENUE | 1 |
| 2027620020 | 823 FAILE STREET | 1 |
| 2027620280 | 1360 SENECA AVENUE | 4 |
| 2027630139 | 758 MANIDA STREET | 3 |
| 2027630343 | 755 WHITTIER STREET | 3 |
| 2027650067 | 621 TIFFANY STREET | 1 |
| 2027650098 | 625 CASANOVA STREET | 1 |
| 2027650099 | 623 CASANOVA STREET | 1 |
| 2027650123 | 650 TIFFANY STREET | 1 |
| 2027650138 | 1220 SPOFFORD AVENUE | 15 |
| 2027660522 | 665 HUNTS POINT AVENUE | 2 |
| 2027680091 | 538 CRAVEN STREET | 18 |
| 2027680097 | 1180 RANDALL AVENUE | 2 |
| 2027680105 | 531 TIFFANY STREET | 2 |
| 2027680117 | 515 TIFFANY STREET | 2 |
| 2027680171 | 1201 OAK POINT AVENUE | 4 |
| 2027680251 | 543 MANIDA STREET | 4 |
| 2027680360 | 1285 OAK POINT AVENUE | 4 |
| 2027690141 | 590 HUNTS POINT AVENUE | 1 |
| 2036210001 | 1400 STORY AVENUE | 1 |
| 2036460001 | 935 BRONX RIVER AVENUE | 3 |
| 2036470030 | 1430 BRUCKNER BOULEVARD | 4 |
| 2037090005 | 1425 BRUCKNER BOULEVARD | 1 |

See signals.csv and review.json for every exact source pointer, filing date/status and query coverage. Original packet and complete context remain under discovery/.

- Exact BBL or explicit borough/block/lot joins can miss historical lot changes, unlinked or unrecorded housing.
- Historical existing/proposed units and filing status do not establish current occupancy or completed/lawful housing.
- No positive returned signal is a literal query result; empty or missing numeric fields do not establish no housing.
- Before/after update metadata detects some drift; these APIs are not transactional snapshots.
