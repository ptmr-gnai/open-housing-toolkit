# Massing-grounded concept renders

Turn a verified massing and a real site photo into a concept picture that shows the
modelled building, not a guess. `prepare` copies the massing, projects its floors
onto the street frontage to draw a to-scale front elevation (`elevation.png` for the
image tool, `elevation.svg` for people) and compiles `prompt.txt` from a fixed
template filled with the massing's numbers: stories, height, ground-floor height and
width, upper-floor width and setback. The only choices are a style and a ground-floor
use from short lists; there is no free-text field.

The image is generated outside the module (Codex `image_gen`) with the photo as
Image 1 and the elevation as Image 2, then attached with a review of five fixed
checks (story count, existing buildings removed, shape matches the elevation,
context preserved, caption and credit). `verify` recomputes the prompt and drawing
from the massing and binds the image, references and review by hash.

```sh
python -m housing_concept prepare --massing runs/NAME/massing-7 --photo PHOTO.png --provider "Google Street View" \
  --capture-date "April 2026" --style brick --ground-use shops --out runs/NAME/concept-7
python -m housing_concept attach --run runs/NAME/concept-7 --image IMAGE.png --provider "Codex image_gen" --review REVIEW.json
python -m housing_concept verify --run runs/NAME/concept-7
```

The feasibility report accepts the package as `--render` and shows the elevation next
to the picture. Why it exists: the photo-only renderer (`housing_render`) took only a
story count from the massing, and an agent-written prompt produced new floors stacked
on top of the existing one-story stores.
