# Scene and scenario to a recorded illustration

The same scene/scenario templates prepare a brief [without analysis](standalone/brief.md) or [with the parcel IR and an actual generated image](with-analysis/packet.md).

- `scene.json` records the user-associated site, original Street View reference and unverified camera/parcel match.
- `scenario.json` records six stories and program/design choices as assumptions/preferences.
- `with-analysis/render-brief.json` binds those choices and five cited context facts to the compiled prompt.
- `with-analysis/invocation.json` records the actual image_gen tool parameters; `render-receipt.json` binds prompt, inputs, output and review.
- `with-analysis/review.json` records assistant visual inspection and its limits. It does not certify floor count or geometry.

The photograph is an external conversation reference, not a byte-bound source image in this repository. The prior generated concepts were also in the recent-image context, and original-only conditioning is unverified. The generated illustration carries Google source attribution. This example is not independently geographically or professionally validated, and its six-story assumption is not reconciled with the earlier area budget.
