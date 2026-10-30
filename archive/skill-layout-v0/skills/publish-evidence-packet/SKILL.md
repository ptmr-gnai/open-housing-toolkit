---
name: publish-evidence-packet
description: Verify and present a portable information packet and its machine-readable image brief without upgrading evidence to professional clearance.
---

# Prepare an information packet

The model build produces `packet.md`, self-contained `packet.html`, `ir.json`, `image-prompts.json`, `calculation-steps.csv`, source responses, receipts, request and a workflow snapshot. No hosted application or model service is required.

Before presenting:

```sh
python -m housing_workflow verify --run runs/my-investigation
```

Verification checks byte bindings, packet inventory, parcel/query identity, source pointers, calculation dependencies and regenerated projections. It cannot establish semantic completeness or professional acceptance. Identify failed sources, uncovered stages, unreviewed judgments and hypothetical assumptions alongside relevant conclusions.

Deliver a short summary and paths to the readable packet and JSON. The image brief binds displayed values to claims and the model hash; it permits a labeled area diagram/evidence card only. Geometry is unverified, so a photorealistic site design is not grounded by this output. Proposal writing and later image generation can consume the packet but must preserve its conditions and unresolved constraints.

This step writes local artifacts. It does not send email, submit a proposal, deploy a website or publish a claim to others. Public communication requires a separately authorized action and appropriate evidence for the specific claims.
