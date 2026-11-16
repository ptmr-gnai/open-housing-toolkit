# You received a feasibility report

Use this when a user hands you a report from this toolkit (an HTML file or PDF,
often with an `...-evidence.zip`) and asks what it is, whether to trust it, or to
take it further. Speak plainly; the user may not know what the toolkit is.

## 1. Explain it, from the report alone

The HTML carries the whole typed report as JSON in the script element whose id is
`report-data` (a PDF does not; ask for the HTML or the bundle). Read it and tell the
user, in a few lines:

- the goal (`brief.goal`, the requester's own words) and who it was prepared for;
- the selected site and why (`search.selected`), and what was tested (`process`);
- the findings: yield on cost, remaining gap, zoning check, latest deed (`headline`);
- the top open items, and that professional review is pending.

Say that every figure is either a public record (with a retrieval date and SHA-256
fingerprint) or an assumption the requester approved (`brief.decisions`), and that
you can check this if they have the evidence bundle.

## 2. Verify it (needs the bundle)

Unzip the bundle. Its `README.md` names the toolkit commit and the evidence
fingerprint; it should match the fingerprint printed in the report's "About this
report" section.

```sh
git clone https://github.com/ptmr-gnai/open-housing-toolkit.git ~/open-housing-toolkit   # if not installed
cd ~/open-housing-toolkit && git checkout COMMIT_FROM_README   # use a separate clone if this one has local work
python3 scripts/preflight.py
.venv/bin/python -m housing_feasibility verify --run PATH/BUNDLE/report --html PATH/report.html
```

`passed` means every input package re-verified with its own module, every figure
recomputed, and the HTML matches the bundle exactly. `inputs_checked_by_hash_only`
lists packages whose third-party source photo was withheld (see `WITHHELD.json`).
A failure names what differs; report it as found, don't repair it.

Verification shows the report is internally consistent and traceable. It does not
make the assumptions right; say which ones matter most (`brief.decisions`).

## 3. Continue it

When the user wants a variation (another height, different rents or costs, a
render, a different persona's view):

```sh
.venv/bin/python -m housing_feasibility continue --bundle PATH/BUNDLE/report --out runs/NAME
```

This copies the verified inputs to `runs/NAME/from-report/` and starts
`runs/NAME/brief.json` from the original brief, marked as extending it. Record what
the user wants changed with `brief decide`, build only the new pieces with
[full lot analysis](lot-analysis.md) steps 3–5 (the parcel geometry is in
`from-report/massing/*/parcel-source`), then build the report with the reusable
inputs plus the new packages; `--discovery` accepts `from-report/discovery-extract.json`.
The new report's "How we got here" names the report it continues.

To share the result, run `housing_feasibility bundle` and send the HTML with the zip.
