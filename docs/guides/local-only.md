# Local-only execution

Running the toolkit is permission to read its code/snapshots and create the user's
new local work. It is not permission to regenerate shipped artifacts, overwrite
examples, alter a source cache, commit, push, upload or publish results. A Git remote
is not authorization. An agent must receive explicit publication instructions for
that task before taking any such action.

## Normal use

The primary user workflow is Codex running on the user's Mac, with Codex's included
image tool when images are requested. No separate image-generation API, account or
hosted application is required by this toolkit. Save requests, downloaded/generated
images, reports and reviews in the user's local run folder.

From a checkout, a supported Python interpreter is enough for the offline tour.
No make target, research build or source refresh is a setup prerequisite. Use a
fresh runs/<name>/ folder (Git-ignored) or an explicitly chosen local folder outside
the checkout. The writers reject outputs inside shipped source/data directories,
including attempts to rebuild a saved example in place. Completed runs are not
reused for a new build; replay or revise into a fresh directory.

The output guard is a toolkit filesystem rule, not a sandbox for arbitrary shell
commands and not control over OS-level cloud-synced folders. Choose an unsynced
local folder when that is required. Git ignore rules help prevent accidental
staging; they are not encryption or access controls.

Using Codex's image tool does not authorize publishing an image. Retain the actual
generated file, prompt/reference bindings and review in the local run. Do not commit,
push or upload the resulting packet/assets unless the user explicitly requests it.
Public-data collection makes the requested source API calls and saves responses
locally; it does not publish the resulting analysis.

## Contributor commands

| Command | New output location | Shipped files |
| --- | --- | --- |
| make build / python research/legacy-probe/pipeline.py | New ignored runs/core-* directory | Read-only inputs; no replacement of outputs/ |
| make check | New ignored runs/check-* directory, core run and logs | Checked for byte/mtime changes |
| make research-check | Validator results on stdout; tests use fresh local scratch | Validators do not overwrite recorded validation JSON; checkout checked for changes |
| make release-check | New ignored runs/release-* directory; screenshots inside that run | No writes to shipped screenshots/reports |
| python validate.py LOCAL_RUN | Result on stdout | Does not write validation.json |
| python research/.../validate.py | Result on stdout for supported validators | No overwrite of recorded validation results |

Core lint/schema/replay/gate consumers accept a local --run path where applicable.
Browser checks require a local generated core run path and reject shipped outputs/.
Build/check commands do not change Git state, stage files or publish anything.
Checks fail if shipped file bytes or modification times change, even when the
rewritten bytes happen to be identical. Frozen research builders are historical
source, not supported user setup commands; use documented read-only validators.

## Maintainer source changes

An explicit request to change the toolkit's source is different from running an
analysis. Keep user-run data/results out of source commits. Curated example updates
require their own reviewed task; ordinary checks never update them. Existing
examples continue to verify against their recorded original code snapshots;
validation does not rewrite their manifests to conceal source changes. The pinned
historical conclusion experiment is validated in a fresh local copy with its
original source bytes; its generated outputs are not rebuilt.
