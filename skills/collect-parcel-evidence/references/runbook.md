# collect-parcel-evidence: execution reference

Working directory: repository root. This skill requires the checkout; it is not
a standalone installed bundle. Treat all example commands as examples; substitute
the user's actual paths/inputs. Read the relevant section below before execution.

## Canonical resources (read only as needed)

- [Module guide](../../../housing_workflow/README.md): commands, outputs and supported scope.
- [CLI implementation](../../../housing_workflow/__main__.py): existing executable entry point; run from the checkout root.
- [Request contract](../../../housing_workflow/request.schema.json): read before constructing new input.

## Detailed procedure and boundaries
# Collect parcel evidence

Read `housing_workflow/sources.json` for the four supported APIs, field selections, publishers and limits. `housing_workflow/router.py` is a local adapter router, not a hosted proxy. It accepts no user-supplied API URL. Public access can still fail or throttle.

```sh
python -m housing_workflow collect --input request.json --out runs/my-investigation
```

Intake requires a BBL or unique exact PLUTO Bronx address. Address abbreviation normalization is limited; ask for the BBL on failure rather than guessing. Four exact-BBL queries fetch PLUTO, DOB BIS, DOB NOW and HPD violations. Responses are capped at 501 rows; more than 500 is flagged as truncated. Missing historical lot linkage remains unresolved even below the cap. These are filing/document/violation rows, not deduplicated projects.

Inspect `receipts.json`: status, requested parcel, exact URL, retrieval date, body path, SHA256, returned rows, truncation and source limitations. Raw bodies stay in `sources/`. HTTP 200 alone is insufficient; structured error objects and mismatched parcels are rejected. Failed calls remain failed evidence, not empty successful datasets. Review surviving source coverage before continuing; a packet can be partial.

Do not refresh a previous run in place. The saved snapshots support offline replay and later contradiction analysis. Live retrieval does not recreate a historical decision-date packet. Upstream source terms are separate from the toolkit license.
