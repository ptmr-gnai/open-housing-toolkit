# Housing site search: transit-rental-targets

Which recorded nonhousing lots can accommodate an assumed 40/60/100-home area program under declared density, transit, operating and capital-gap targets?

1921 inventory lots retained; 457 recorded nonhousing lots; 2742 explicit program/price trials. Matches are conditional search results, not viable-site estimates.

Explicit finite scenario search, not an optimization proof, site recommendation, legal envelope or funded feasibility finding.

## Target outcomes

| Trial status | Count |
| --- | --- |
| does_not_match_declared_targets | 2742 |

| Lot status | Count |
| --- | --- |
| does_not_match_declared_targets | 457 |
| retained_other_current_use_queue | 1464 |

## Selected scenarios for inspection

No scenarios met all declared targets with sufficient target evidence. All failed/unknown trials remain in trials.csv.

Non-dominated on smaller required zoning FAR, smaller unallocated capital/home and more proposed homes, among matching scenarios only; no universal welfare weights.

## Exact targets and scaling

```json
{
  "basis": {
    "kind": "analyst_assumption",
    "rationale": "Analyst test of a transit-near rental search, not Jeremy-approved priorities, market underwriting, a zoning proposal or a recommendation. Every price/program/efficiency target is an explicit exploration choice.",
    "reference_ids": []
  },
  "detail_limit": 3,
  "id": "transit-rental-targets",
  "land_price_per_lot_sf_values": [
    "100",
    "200"
  ],
  "program_grid": {
    "gross_per_zoning_sf": "1",
    "homes": [
      40,
      60,
      100
    ],
    "net_efficiency": "0.85",
    "net_sf_per_home": "700",
    "residential_share_of_gross": "0.9"
  },
  "question": "Which recorded nonhousing lots can accommodate an assumed 40/60/100-home area program under declared density, transit, operating and capital-gap targets?",
  "scaling": {
    "below_line": {
      "asset-and-monitoring-fees": "per_home"
    },
    "expenses": {
      "administration": "per_home",
      "insurance": "per_home",
      "management": "per_home",
      "staff-and-maintenance": "per_home",
      "taxes": "per_home",
      "utilities": "per_home"
    },
    "fixed_capital": {
      "acquisition_closing": "per_home",
      "business_relocation": "per_lot_sf",
      "construction_interest": "per_home",
      "demolition": "per_lot_sf",
      "developer_fee": "per_home",
      "financing_fees": "per_home",
      "offsite_infrastructure": "per_lot_sf",
      "other": "per_home",
      "remediation": "per_lot_sf",
      "taxes_and_carry": "per_home"
    },
    "income": {
      "tenant-rent": "per_home"
    },
    "reference_lot_area_sf": "10000",
    "replacement_reserve": "per_home",
    "sources": {
      "sponsor-equity": "per_home"
    }
  },
  "targets": {
    "allowed_review_lanes": [
      "other_nonhousing_review"
    ],
    "allowed_zoning_paths": [
      "housing_permitted_by_general_use_rule",
      "rezoning_path",
      "special_or_unresolved_review"
    ],
    "max_monthly_scheduled_tenant_rent_usd": "2000",
    "max_required_zoning_far": "6",
    "max_station_straight_line_m": "800",
    "max_unallocated_capital_per_home_usd": "500000",
    "minimum_cashflow_usd": "0",
    "require_lot_point_outside_ibz": true,
    "require_no_active_linked_zap": true,
    "require_no_positive_returned_housing_signal": true,
    "tenant_rent_cap_scope": "year_one",
    "tenant_rent_stream_ids": [
      "tenant-rent"
    ]
  },
  "version": "1.0"
}
```

## Scope and unresolved work

- Broad nonhousing discovery stays unchanged; these are user/analyst-declared search filters.
- Desired whole-home programs imply required area; no FAR increment is required and no legally permitted unit count is inferred.
- Land prices, construction costs, rent, efficiency and all scaling are scenario assumptions, not automatically estimated from public records.
- Recorded-point station distance is not walking/job access; an outside-IBZ point does not resolve parcel-wide overlap or policy support.
- Dollar appraisal/debt caps and other debt service remain fixed scenario assumptions; all template funding statuses are downgraded to proposed for the new site/program.
- No result resolves occupancy, site control, parcel assembly, zoning applicability, physical fit, environmental clearance or investor returns.

[Broad discovery](discovery/packet.md) retains source records, all use queues and zoning paths. [Financial template](underwriting-template/packet.md) retains input bases and references. Every inventory lot remains in all-lots.csv; every modeled scenario remains in trials.csv/results.json.

Select explicit BBLs with the search handoff command. It verifies this package and uses the existing evidence-only parcel workflow; the model is not silently promoted to a lawful building program.
