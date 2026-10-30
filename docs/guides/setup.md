# Set up the checkout once

Use Codex on your Mac with Python 3.11+. The toolkit now uses a standard src/
layout, so install the checkout in editable mode before running its Python modules.
The existing `python -m housing_…` commands stay the same.

From the repository root:

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
