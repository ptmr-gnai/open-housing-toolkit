# First visit: install, orient and guide

Use this when someone asks you to install the toolkit, says "let's start", or is
clearly new. Assume they know nothing about the workflow, coding or housing data
jargon. You do the technical work; they make the decisions.

## 1. Install and check (quietly)

1. Use `~/open-housing-toolkit`. If it does not exist, clone it:
   `git clone https://github.com/ptmr-gnai/open-housing-toolkit.git ~/open-housing-toolkit`.
   If it exists and its `origin` is this repository, reuse it: run
   `git pull --ff-only` only when `git status --porcelain` is empty, otherwise leave
   it as is. If it exists and is something else, ask the user where to install.
2. From that folder run `python3 scripts/preflight.py` (any Python 3 works; it finds
   or installs Python 3.11+, creates `.venv`, installs everything and fixes HTTPS
   certificate problems). Windows users need WSL. On exit code 1, relay the printed
   `USER ACTION NEEDED` line in plain words and wait. Never disable certificate checks.
3. Read `runs/preflight.json`. Afterwards run every toolkit command from that folder
   with `.venv/bin/python`.

Tell the user one line, such as "Installed and checked; everything is ready." Mention
only what limits their choices (no live data, no geometry, images). Do not narrate
package installs.

## 2. Orient

Say this in your own words, briefly:

> This is the Open Housing Toolkit. It helps you find New York City sites where
> housing could be built or might need a rezoning, research a specific lot from
> public records, sketch what could go there, and prepare building renders.
> Everything is cited and stays on your computer. Let me ask a couple of questions
> to get started.

If preflight says this agent cannot make images, add one sentence: "I can prepare
renders here; to generate the picture itself you'd open the prepared brief in Codex"
(or "...in an image tool later" when Codex was not found).

## 3. Ask two questions in one message

> 1. Do you already have a lot or address in mind, or would you like help finding
>    candidate sites?
> 2. What would you like to come away with? Pick any:
>    a. A list of candidate sites in an area, with how each is zoned (anywhere in NYC)
>    b. A research packet on one lot: what the public records say (Bronx lots for now)
>    c. A rough model of what could be built and whether the numbers might work
>    d. A picture: a 3D massing sketch or a render based on a site photo
>    e. Not sure yet: show me a two-minute example first

Skip anything the user already told you. Accept loose answers ("near the 4 train in
the Bronx", "something like a render") and confirm your reading.

## 4. Follow the matching route

**Find sites (a).** Ask where: an address, landmark or subway station, plus roughly
how far around it (default 400 m, about a five-minute walk each way). For a
neighbourhood or intersection, propose a central address or station and confirm.
If they already named a clear place, don't stall: say in one line the place and
size you'll search ("an 800 m square around the 170 St station on the 4") and offer
to widen or narrow it afterwards. Create the request:

```sh
.venv/bin/python scripts/locate.py area --station "170 St" --routes 4 --out runs/NAME/request.json
.venv/bin/python scripts/locate.py area "1337 Jerome Ave, Bronx" --radius-m 400 --out runs/NAME/request.json
```

Then run collect, context and discover from [Find sites](../../../docs/guides/discover-sites.md)
with `--input runs/NAME/request.json` and outputs under `runs/NAME/`. A small area
takes about a minute. If collect reports 0 lots, read `inventory/receipts.json`
before saying anything. Report: how many lots, how many are recorded as nonhousing,
how they split by zoning path, and three or four example sites in plain words,
copying each address and tax lot exactly from the packet. On a Mac, open the result
for them with `open runs/NAME/discovery/packet.html`; mention `all-lots.csv` as the
spreadsheet of every lot. Then offer: research one of these lots,
try another area, or test a housing goal ([goal search](../../goal-seek-housing-sites/SKILL.md)).

**Research one lot (b).** Resolve it with
`.venv/bin/python scripts/locate.py lookup "ADDRESS"` and confirm the address and
tax lot number (BBL). Bronx lots (BBL starting with 2) go to
[housing-investigation](../../housing-investigation/SKILL.md). For other boroughs,
explain that single-lot packets are Bronx-only today and offer a site search around
the lot instead, which covers it citywide.

**Model what could be built (c).** Explain that the arithmetic is checked but the
inputs (costs, rents, financing) are judgement calls the user or an advisor should
make. Follow the branches in the [practitioner guide](full-flow.md): propose clearly
labelled assumptions with reasons and get approval before calculating.

**A picture (d).** When the picture is for a specific lot, offer to research the lot
first (records, zoning, a schematic massing) so the building's height and size come
from what the lot allows rather than a guess; a quick standalone illustration is the
fallback if they just want a feel. Massing needs a researched Bronx lot and assumed dimensions:
[build-grounded-massing](../../build-grounded-massing/SKILL.md) (needs geometry from
preflight). A render needs a real site photo or Street View screenshot and a
description of the building: [prepare-render-brief](../../prepare-render-brief/SKILL.md),
then the [runtime route](agent-runtimes.md). In Codex with an image tool, generate it.
In Claude Code, prepare the brief and, when preflight found Codex, give the user a
sentence to paste into Codex opened on `~/open-housing-toolkit`:
"Generate the render for the prepared brief in runs/NAME following
skills/render-site-concept/SKILL.md."

No photo and the user doesn't want to get one? Offer a standalone illustration of
the described building, made with the host image tool (Codex) outside the
photo-based module. Caption it "Illustrative concept • Site fit unverified", check
the story count and other stated details against the image and regenerate if wrong,
and save the image with the exact prompt (`prompt.txt`) and a short note in
`runs/NAME/`. Say plainly that it shows the idea, not the real street or lot.

**Not sure (e).** Run `.venv/bin/python scripts/first_run.py --out runs/example-tour`,
then explain in four short bullets what each of its packets shows, and ask question 2 again.

## Style throughout

- Plain words. Explain any term the first time (BBL is the tax lot number; FAR is
  how much floor area zoning allows relative to lot size). Never lead with module names.
- After the opening, ask one or two questions at a time and end with a real question.
- Show results, not logs. For each result: what it is, the one limit that matters
  most, and the next choice. Open the main `packet.html` for them (`open PATH` on a
  Mac) instead of listing every file.
- Don't mention commands, module names, guide file paths, file formats or internal
  terms (SVG, mesh, IR, manifest, `housing_workflow`) unless asked. Say "the 3D sketch", "the research
  packet", "the site list".
- Keep each project in a new `runs/NAME/` folder. Never commit, push or upload.
- Do not invent sites, numbers, photos or images. Say what is unknown.
