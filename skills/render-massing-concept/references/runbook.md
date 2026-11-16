# render-massing-concept: execution reference

Working directory: repository root. Use `.venv/bin/python` after preflight.

- [Module guide](../../../src/housing_concept/README.md)
- [Implementation](../../../src/housing_concept/engine.py): prompt template, choices and review checks.

```sh
.venv/bin/python -m housing_concept prepare --massing runs/NAME/massing-7 --photo PHOTO.png \
  --provider "Google Street View" --capture-date "April 2026" --style brick \
  --ground-use shops_and_supermarket --out runs/NAME/concept-7
# generate one image: Image 1 = runs/NAME/concept-7/inputs/reference.png, Image 2 = runs/NAME/concept-7/elevation.png,
# prompt = the exact contents of runs/NAME/concept-7/prompt.txt
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
