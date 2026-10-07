# Supporting facts and assumptions

All rows belong to the conclusion dependency closure. Source strings are exact values, not interpretations.

| Claim | Kind | Value | Exact locator or dependency |
| --- | --- | --- | --- |
| assumption.amortization_years | assumption | 30 | "/assumptions/amortization_years/value" |
| assumption.annual_interest | assumption | 0.065 | "/assumptions/annual_interest/value" |
| assumption.avg_net_unit_sf | assumption | 850 | "/assumptions/avg_net_unit_sf/value" |
| assumption.debt_ltc | assumption | 0.65 | "/assumptions/debt_ltc/value" |
| assumption.dscr | assumption | 1.2 | "/assumptions/dscr/value" |
| assumption.gross_per_zoning_sf | assumption | 1.0 | "/assumptions/gross_per_zoning_sf/value" |
| assumption.hard_cost_per_gsf | assumption | 350 | "/assumptions/hard_cost_per_gsf/value" |
| assumption.monthly_rent_test | assumption | 1800 | "/assumptions/monthly_rent_test/value" |
| assumption.net_efficiency | assumption | 0.8 | "/assumptions/net_efficiency/value" |
| assumption.opex_share_egi | assumption | 0.35 | "/assumptions/opex_share_egi/value" |
| assumption.soft_contingency_share | assumption | 0.3 | "/assumptions/soft_contingency_share/value" |
| assumption.vacancy_share | assumption | 0.05 | "/assumptions/vacancy_share/value" |
| conclusion.next_step | judgment | "investigate_current_uses_and_leases" | ["judgment.investigation_priority", "resident.recorded_units", "finance.model_gap", "station.Station ID", "station.Stop Name", "station.Daytime Routes", "lot.2028710002.address", "lot.2028710002.bbl", "lot.2028710002.version", "lot.2028710002.ownername", "lot.2028710002.bldgclass", "lot.2028710002.zonedist1", "lot.2028710002.edesignum", "lot.2028710002.distance_m", "scenario.2028710002.A.gross_sf", "scenario.2028710002.A.units", "scenario.2028710002.A.ex_land_cost", "scenario.2028710002.A.debt_support_rent_month", "environment.0.hazmat_code", "environment.0.air_code", "environment.0.noise_code", "environment.0.description", "gate.legal_entitlement", "gate.current_occupancy_and_leases", "gate.owner_willingness_and_title", "gate.environment_and_geotechnical", "gate.current_development_pipeline", "gate.full_cost_and_financing", "gate.official_affordability_schedule", "gate.pedestrian_and_job_access"] |
| environment.0.air_code | observed | true | {"row": 0, "field": "air_code"} |
| environment.0.description | observed | "Air Quality - HVAC fuel limited to natural gas;Exhaust stack location limitations;Hazardous Materials* Phase I and Phase II Testing Protocol;Window Wall Attenuation & Alternate Ventilation" | {"row": 0, "field": "description"} |
| environment.0.hazmat_code | observed | true | {"row": 0, "field": "hazmat_code"} |
| environment.0.noise_code | observed | true | {"row": 0, "field": "noise_code"} |
| finance.model_gap | derived | true | ["scenario.2028710002.A.additional_non_debt_capital"] |
| gate.current_development_pipeline | unknown | null | "/required_gates/4" |
| gate.current_occupancy_and_leases | unknown | null | "/required_gates/1" |
| gate.environment_and_geotechnical | unknown | null | "/required_gates/3" |
| gate.full_cost_and_financing | unknown | null | "/required_gates/5" |
| gate.legal_entitlement | unknown | null | "/required_gates/0" |
| gate.official_affordability_schedule | unknown | null | "/required_gates/6" |
| gate.owner_willingness_and_title | unknown | null | "/required_gates/2" |
| gate.pedestrian_and_job_access | unknown | null | "/required_gates/7" |
| history.1.doc__ | observed | "01" | {"row": 1, "field": "doc__"} |
| history.1.job__ | observed | "240116815" | {"row": 1, "field": "job__"} |
| history.1.job_description | observed | "FILING TO CONVERT SCHOOL TO HALL. NO CHANGE IN USE, EGRESS AND OCCUPANCY." | {"row": 1, "field": "job_description"} |
| history.1.pre__filing_date | observed | "10/02/2015" | {"row": 1, "field": "pre__filing_date"} |
| history.11.doc__ | observed | "01" | {"row": 11, "field": "doc__"} |
| history.11.job__ | observed | "200853843" | {"row": 11, "field": "job__"} |
| history.11.job_description | observed | "NON-ILLUMINATED NON ADVERTISISNG ACCESSO RY AWNING READING- COLUMBUS MEDICAL.  NO CHANGE IN USE,EGRE SS OR OCCUPANCY" | {"row": 11, "field": "job_description"} |
| history.11.pre__filing_date | observed | "05/03/2004" | {"row": 11, "field": "pre__filing_date"} |
| history.3.doc__ | observed | "01" | {"row": 3, "field": "doc__"} |
| history.3.job__ | observed | "200711453" | {"row": 3, "field": "job__"} |
| history.3.job_description | observed | "Interior construction of laundromat. Install washing machines, dryers, plumbing fixtures, partitions, hung ceiling , boilers,  HVAC roof top units, and relocate existing sprinkler heads. No change to use egress or occupancy." | {"row": 3, "field": "job_description"} |
| history.3.pre__filing_date | observed | "01/24/2002" | {"row": 3, "field": "pre__filing_date"} |
| judgment.investigation_priority | judgment | "Occupancy and lease facts precede design spending in this bounded research workflow; independent practitioner acceptance pending." | ["history.1.job_description", "history.1.pre__filing_date", "history.1.job__", "history.1.doc__", "history.3.job_description", "history.3.pre__filing_date", "history.3.job__", "history.3.doc__", "history.11.job_description", "history.11.pre__filing_date", "history.11.job__", "history.11.doc__", "lot.2028710002.retailarea", "gate.current_occupancy_and_leases"] |
| lot.2028710002.address | observed | "1240 EDWARD L GRANT HWY" | {"row": 1940, "field": "address"} |
| lot.2028710002.bbl | observed | "2028710002.00000000" | {"row": 1940, "field": "bbl"} |
| lot.2028710002.bldgclass | observed | "K1" | {"row": 1940, "field": "bldgclass"} |
| lot.2028710002.distance_m | derived | 434.07933676398704 | ["lot.2028710002.latitude", "lot.2028710002.longitude", "station.GTFS Latitude", "station.GTFS Longitude"] |
| lot.2028710002.edesignum | observed | "E-442" | {"row": 1940, "field": "edesignum"} |
| lot.2028710002.latitude | observed | 40.8376295 | {"row": 1940, "field": "latitude"} |
| lot.2028710002.longitude | observed | -73.921813 | {"row": 1940, "field": "longitude"} |
| lot.2028710002.lotarea | observed | 59050.0 | {"row": 1940, "field": "lotarea"} |
| lot.2028710002.ownername | observed | "1240 EDWARD GRANT LLC" | {"row": 1940, "field": "ownername"} |
| lot.2028710002.residfar | observed | 7.52 | {"row": 1940, "field": "residfar"} |
| lot.2028710002.retailarea | observed | 26000.0 | {"row": 1940, "field": "retailarea"} |
| lot.2028710002.unitsres | observed | 0.0 | {"row": 1940, "field": "unitsres"} |
| lot.2028710002.version | observed | "26v2" | {"row": 1940, "field": "version"} |
| lot.2028710002.zonedist1 | observed | "R9A" | {"row": 1940, "field": "zonedist1"} |
| resident.recorded_units | derived | "recorded_zero_does_not_establish_vacancy" | ["lot.2028710002.unitsres", "lot.2028710002.version"] |
| scenario.2028710002.A.additional_non_debt_capital | derived | 45651124.19742605 | ["scenario.2028710002.A.illustrative_loan", "scenario.2028710002.A.rent_supported_debt"] |
| scenario.2028710002.A.annual_debt_constant | derived | 0.07584816281915584 | ["assumption.annual_interest", "assumption.amortization_years"] |
| scenario.2028710002.A.annual_debt_service | derived | 6474718.901003876 | ["scenario.2028710002.A.illustrative_loan", "scenario.2028710002.A.annual_debt_constant"] |
| scenario.2028710002.A.debt_support_rent_month | derived | 3869.141969914323 | ["scenario.2028710002.A.target_noi", "scenario.2028710002.A.units", "assumption.vacancy_share", "assumption.opex_share_egi"] |
| scenario.2028710002.A.ex_land_cost | derived | 131329562.00000003 | ["scenario.2028710002.A.gross_sf", "assumption.hard_cost_per_gsf", "assumption.soft_contingency_share"] |
| scenario.2028710002.A.far_share | assumption | 0.65 | "/scenarios/0/far_share" |
| scenario.2028710002.A.gross_sf | derived | 288636.4 | ["scenario.2028710002.A.zoning_area_proxy_sf", "assumption.gross_per_zoning_sf"] |
| scenario.2028710002.A.illustrative_loan | derived | 85364215.30000003 | ["scenario.2028710002.A.ex_land_cost", "assumption.debt_ltc"] |
| scenario.2028710002.A.net_sf | derived | 230909.12000000002 | ["scenario.2028710002.A.gross_sf", "assumption.net_efficiency"] |
| scenario.2028710002.A.rent_supported_debt | derived | 39713091.102573976 | ["scenario.2028710002.A.rent_test_noi", "assumption.dscr", "scenario.2028710002.A.annual_debt_constant"] |
| scenario.2028710002.A.rent_test_noi | derived | 3614598.0 | ["scenario.2028710002.A.units", "assumption.monthly_rent_test", "assumption.vacancy_share", "assumption.opex_share_egi"] |
| scenario.2028710002.A.target_noi | derived | 7769662.681204651 | ["scenario.2028710002.A.annual_debt_service", "assumption.dscr"] |
| scenario.2028710002.A.units | derived | 271 | ["scenario.2028710002.A.net_sf", "assumption.avg_net_unit_sf"] |
| scenario.2028710002.A.zoning_area_proxy_sf | derived | 288636.4 | ["lot.2028710002.lotarea", "lot.2028710002.residfar", "scenario.2028710002.A.far_share"] |
| station.Daytime Routes | observed | "4" | {"row": 387, "column": "Daytime Routes"} |
| station.GTFS Latitude | observed | 40.840075 | {"row": 387, "column": "GTFS Latitude"} |
| station.GTFS Longitude | observed | -73.917791 | {"row": 387, "column": "GTFS Longitude"} |
| station.Station ID | observed | "387" | {"row": 387, "column": "Station ID"} |
| station.Stop Name | observed | "170 St" | {"row": 387, "column": "Stop Name"} |
