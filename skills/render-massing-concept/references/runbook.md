# render-massing-concept: execution reference

Working directory: repository root. Use `.venv/bin/python` after preflight.

- [Module guide](../../../src/housing_concept/README.md)
- [Implementation](../../../src/housing_concept/engine.py): prompt template, choices and review checks.

```sh
.venv/bin/python -m housing_concept prepare --massing runs/NAME/massing-7 --photo PHOTO.png \
  --provider "Google Street View" --capture-date "April 2026" --style brick \
  --ground-use shops_and_supermarket --out runs/NAME/concept-7
# generate one image with references in this order: inputs/reference.png, massing-3d.png, elevation.png,
# site-plan.png (all in runs/NAME/concept-7); prompt = the exact contents of runs/NAME/concept-7/prompt.txt.
# Count the window rows in the result before reviewing; a missing floor means generate again.
.venv/bin/python -m housing_concept review-template --out runs/NAME/concept-7-review.json   # fill in after looking
.venv/bin/python -m housing_concept attach --run runs/NAME/concept-7 --image GENERATED.png \
  --provider "Codex image_gen" --review runs/NAME/concept-7-review.json
.venv/bin/python -m housing_concept verify --run runs/NAME/concept-7
```

Choices: `--style` brick | light_masonry | metal_glass; `--ground-use` shops |
shops_and_supermarket | community. `prepare` lists the parcel edges; if the longest
edge is not the street side, pass `--frontage-edge N`. A second attempt goes in a new
folder (`concept-7b`); attach refuses a review whose story count or building removal
is not consistent.

Floor count off? Count the apartment window rows in the draft, then:

```sh
.venv/bin/python -m housing_concept correct --from runs/NAME/concept-7 --draft DRAFT.png --rows-seen 5 --out runs/NAME/concept-7b
```

Generate once more with the references it prints (photo, draft, 3D massing, elevation)
and `prompt.txt`. Still off: `attach ... --accept-issue "Shows 6 stories; the massing has 7"`.
