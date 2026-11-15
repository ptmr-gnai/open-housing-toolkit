# Set up the checkout once

The easiest way: ask Claude Code or Codex to "install
https://github.com/ptmr-gnai/open-housing-toolkit and let's start". The agent does
everything below.

To do it yourself on a Mac, from the repository root (any Python 3 can start it):

```sh
python3 scripts/preflight.py
```

It finds or installs Python 3.11+, creates `.venv`, installs the toolkit with
optional geometry support, fixes HTTPS certificate problems inside `.venv`, checks
live NYC data access and reports image options. Then use `.venv/bin/python` for
toolkit commands. The checkout is about 1.3 GB on disk, mostly retained research
cases (the download is about 80 MB).

## Manual setup

The toolkit uses a standard src/ layout, so install the checkout in editable mode
before running its Python modules. From the repository root, with Python 3.11+:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

For Codex commands in separate terminal sessions, use `.venv/bin/python` or activate
this environment in that session. Verify the setup:

```sh
python -c "import housing_workflow; print(housing_workflow.__file__)"
```

The path should point into this checkout's src/housing_workflow/ directory.
Setuptools/build tooling may be downloaded during installation; the base toolkit
has no third-party runtime dependencies. Setup creates ignored environment/package
metadata, not analytical results. It does not regenerate examples, refresh source
snapshots, commit, push or upload user data.

Then use [Investigate a lot](investigate-a-lot.md) or [the offline tour](first-run.md).
Outputs still go into fresh ignored runs/ folders or an explicit local destination.
No developer make target is a setup prerequisite. Codex's included image tool needs
no separate image-generation API setup in this workflow.

Optional geometry:

```sh
python -m pip install -e ".[geometry]"
```

Contributors who need schema/geometry checks:

```sh
python -m pip install -e ".[dev]"
```

Windows users should use WSL and its Linux environment; native Windows remains
unverified. A wheel-only deployment without the repository resources is not the
supported installation: keep this editable checkout and its config, skills,
examples and archived verification sources together.

## If live collection reports certificate errors

Live collection fetches public NYC data over HTTPS. Some macOS Python builds
(python.org installers, uv-managed Python) cannot verify those certificates and
fail with `CERTIFICATE_VERIFY_FAILED`. Lot discovery then reports 0 lots; the
errors are recorded in the run's `inventory/receipts.json`. Point Python at a
trusted bundle and rerun into a fresh folder:

```sh
python -m pip install certifi
export SSL_CERT_FILE="$(python -m certifi)"
```

Commands that accept `--ca-file` can take the same path instead. Saved examples,
the offline tour and all checks need no network access.
