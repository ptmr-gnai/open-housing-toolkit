# Massing-grounded concept renders

Turn a verified massing and a real site photo into a concept picture that shows the
modelled building, not a guess. `prepare` copies the massing and renders three
reference views of it for the image tool: `massing-3d.png` (the volume from across
the street, ground floor blue, apartment floors orange with one line per floor),
`elevation.png` (front elevation to scale; `elevation.svg` for people) and
`site-plan.png` (lot, footprints and street edge). It compiles `prompt.txt` from a
fixed template that tells the model what each reference is for and gives the
massing's numbers: stories, height, ground-floor height and width, upper-floor width
and setback. The only choices are a style and a ground-floor
use from short lists; there is no free-text field.

The image is generated outside the module (Codex `image_gen`) with the photo and the
three views as references, in that order, then attached with a review of five fixed
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

Tested November 16, 2026 on 68 East Burnside with Codex (`gpt-6.1-terra`): with the
three views the 7-story concept replaced the stores, kept the street, and showed the
correct six window rows; a 9-story test came out one floor short, which the
story-count review catches before attaching.

When a draft has the wrong floor count, `correct` makes a new attempt folder with a
fixed edit prompt (add or remove exactly N floors, change nothing else) and the draft
as a reference. If the count is still off, `attach --accept-issue` keeps the picture
with the issue recorded; the report states it under the picture and in open items.
