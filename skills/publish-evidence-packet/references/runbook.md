# publish-evidence-packet: execution reference

Working directory: repository root. This skill requires the checkout; it is not
a standalone installed bundle. Treat all example commands as examples; substitute
the user's actual paths/inputs. Read the relevant section below before execution.

## Canonical resources (read only as needed)

- [Module guide](../../../src/housing_workflow/README.md): commands, outputs and supported scope.
- [CLI implementation](../../../src/housing_workflow/__main__.py): existing executable entry point; run from the checkout root.
- [Request contract](../../../src/housing_workflow/request.schema.json): read before constructing new input.

## Detailed procedure and boundaries
# Prepare an information packet

The model build produces `packet.md`, self-contained `packet.html`, `ir.json`, `image-prompts.json`, `calculation-steps.csv`, source responses, receipts, request and a workflow snapshot. No hosted application or model service is required.

Before presenting:

```sh
python -m housing_workflow verify --run runs/my-investigation
```

Verification checks byte bindings, packet inventory, parcel/query identity, source pointers, calculation dependencies and regenerated projections. It cannot establish semantic completeness or professional acceptance. Identify failed sources, uncovered stages, unreviewed judgments and hypothetical assumptions alongside relevant conclusions.

Deliver a short summary and paths to the readable packet and JSON. The image brief binds displayed values to claims and the model hash; it permits a labeled area diagram/evidence card only. Geometry is unverified, so a photorealistic site design is not grounded by this output. Proposal writing and later image generation can consume the packet but must preserve its conditions and unresolved constraints.

This step writes local artifacts. It does not send email, submit a proposal, deploy a website or publish a claim to others. Public communication requires a separately authorized action and appropriate evidence for the specific claims.
