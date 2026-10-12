# Contributing

Start by reproducing the result you want to challenge. Python 3.11 or later is
recommended for the complete set of experiments.

```sh
python -m pip install -r requirements-dev.txt
make check
make research-check
```

Offline replay uses committed public-source snapshots. Live collection is a
separate operation; preserve an old snapshot and its receipts before refreshing
it. Do not overwrite a frozen experiment or regenerate a baseline merely to make
a failed test pass.

Useful issues identify a concrete claim, source passage, assumption, omitted
requirement or practitioner task. Include the artifact path, relevant source
version, why the issue changes the conclusion, and how a correction could be
checked. A passing citation check does not prove the interpretation is right.

For code changes, keep facts, calculations, assumptions, judgments and unknowns
distinct. Record units, dates, provenance and dependencies. Missing evidence must
not silently become zero, eligibility, legal clearance or committed funding. Add
a meaningful failure case when changing an evidence boundary or release gate.

For research changes, save a new version and retain the original finding. Keep
input packets separate from later comparison evidence. Disclose outcome exposure,
definitions and limitations. Unknowns are not automatic successes, and matching a
real project's home count does not establish feasibility.

Do not submit private applicant records, credentials or confidential advisor
material. Reference public sources and their terms; project code is MIT and
original documentation is CC BY 4.0 as described in DATA-LICENSES.md.
