# Where outputs live and which platforms are supported

Normal user runs never regenerate shipped reports, examples or source snapshots.
The [local-only policy](local-only.md) covers both analysis and contributor checks.

## Local paths and storage

Every module takes an explicit `--out` argument; nothing is automatically uploaded
to GitHub, a cloud bucket or an agency system. The first-run command:

```sh
python scripts/first_run.py --out runs/my-first-run
```

creates this tree beneath the checkout when run from its root:

```text
open-housing-toolkit/runs/my-first-run/
  README.md        # links into the stage packets
  steps.json       # commands, exit statuses and log paths
  01-...log        # numbered execution logs
  parcel/          # packet.html/md, IR, inputs, source receipts and bytes
  recipe/          # area model, trace, packet and retained evidence
  comparison/      # explicit offers, cost results, packet and retained inputs
  rer/             # two draft reports, coverage, typed IR and retained comparison
```

`runs/` is Git-ignored. This avoids accidental normal commits; it is not access
control or encryption, and deliberately forced commits/uploads remain possible.
Runs duplicate upstream inputs for inspectability and portability. Preserve the
whole stage package rather than moving only its HTML or JSON.

The first-run script prints absolute completion paths. Relative `--out` paths
resolve from the shell's current directory; examples assume the repository root.
Inside the checkout, that script allows output only under `runs/`; outside the
checkout it accepts a new absolute directory. Paths with spaces should be quoted.
The first-run directory must not already exist. Individual module commands require
new/empty directories as specified by their validators.

A render is independent: for example `--out runs/site-concept` saves the prepared
brief, inputs and prompt there. After actual generation and attachment, that same
package also contains the copied image, actual invocation, review and receipt.
An image provider may first return a temporary file; it must be saved/attached
before claiming it is retained. No-tool export produces no generated image.

In a hosted coding-agent session, these paths belong to the hosted workspace,
not automatically to the person's Mac or PC. Download/copy the complete desired
package to retain it outside that environment. Local sessions write on the
computer hosting that checkout. Workspace persistence depends on the host.

## Platform status

The core walkthrough uses Python 3.11+, pathlib and subprocess argument lists;
it needs no Make, Bash, pip packages or image API. Optional geometry and source
PDF preparation have separate dependencies. Image-tool access is a host capability,
not something the operating system alone guarantees.

| Platform | Evidence / present recommendation |
| --- | --- |
| Linux | Exercised locally and in GitHub CI, including the composed walkthrough. |
| macOS | The macOS Python 3.11 offline walkthrough and onboarding-link check passed in [GitHub CI](https://github.com/ptmr-gnai/open-housing-toolkit/actions/runs/40980198211/job/123818053996). This checks the core composed path without optional dependencies, not the Codex/Claude UI, live APIs or visual branches. |
| Native Windows | Not supported as verified today. Exact-byte provenance can be broken by Git checkout newline conversion, default text encoding and platform-translated output newlines. |
| Windows via WSL | Recommended path to the Linux environment; use a checkout created inside WSL with Python 3.11+. Not yet separately exercised on a Windows/WSL machine. |

On macOS, Python may be named `python3`:

```sh
python3 scripts/first_run.py --out runs/my-first-run
```

On Windows, run the Linux commands inside WSL; keep that checkout in WSL's Linux
filesystem. A native Windows `py -3` invocation alone does not address byte-format
issues. No install-time or platform support claim is inferred just from Python's
portability.

Native Windows work needs explicit UTF-8/LF authoring and export behavior, raw
source preservation, cross-platform manifest paths, reviewed rebuilds of bound
examples, and real Windows CI. Existing code includes `write_text` defaults and
byte comparisons of regenerated text, so documentation-only fixes cannot establish
support. Never normalize raw evidence or rehash receipts to conceal conversion.
