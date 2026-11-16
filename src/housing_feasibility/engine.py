"""Assemble verified toolkit packages into one standard-shaped feasibility report. MIT.

The report adds no new estimates. It copies each verified input package, re-runs that
module's verifier, and projects the typed results into the sections practitioners
expect (site, ownership, zoning, massing, development budget, operating pro forma,
sensitivity, render, open items, sources). `verify` recomputes everything.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil

from housing_common.local_outputs import ROOT, destination

VERSION = '1.2.0'
ROLES = ('evidence', 'ownership', 'activity', 'massing', 'underwriting', 'render')
REPOSITORY = 'https://github.com/ptmr-gnai/open-housing-toolkit'
WITHHELD = 'WITHHELD.json'


def toolkit_identity():
    """Which toolkit built this report, recorded at build (verify does not recompute it)."""
    import subprocess
    def git(*args):
        try:
            return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, timeout=10).stdout.strip() or None
        except (OSError, subprocess.SubprocessError):
            return None
    version = None
    pyproject = ROOT / 'pyproject.toml'
    if pyproject.exists():
        m = re.search(r'^version\s*=\s*"([^"]+)"', pyproject.read_text(), re.M)
        version = m.group(1) if m else None
    commit = git('rev-parse', 'HEAD')
    dirty = git('status', '--porcelain', '--', 'src', 'scripts', 'skills', 'config', 'pyproject.toml')
    return {'name': 'Open Housing Toolkit', 'repository': REPOSITORY, 'package_version': version,
            'git_commit': commit, 'uncommitted_toolkit_changes': bool(dirty) if commit else None,
            'report_module_version': VERSION}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def dumps(value):
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + '\n'


def save(path, value):
    Path(path).write_text(dumps(value))


def implementation():
    here = Path(__file__).parent
    paths = sorted(here.glob('*.py')) + sorted(here.glob('*.json'))
    return {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in paths}


def inventory(folder):
    folder = Path(folder)
    return {str(p.relative_to(folder)): digest(p.read_bytes())
            for p in sorted(folder.rglob('*'))
            if p.is_file() and p != folder / 'manifest.json' and '__pycache__' not in p.parts}


# ---------------------------------------------------------------- input verification

def verify_input(role, folder):
    """Run the owning module's own verifier on a retained copy."""
    folder = Path(folder)
    if role == 'evidence':
        from housing_workflow.engine import verify
        return verify(folder)
    if role == 'underwriting':
        from housing_underwriting.engine import verify
        return verify(folder)
    if role == 'massing':
        from housing_geometry.engine import verify
        return verify(folder)
    if role == 'render':
        from housing_render.engine import verify
        return verify(folder)
    if role == 'activity':
        from housing_activity.engine import verify
        return verify(folder)
    if role == 'ownership':
        from housing_ownership.engine import build_package
        if build_package(folder) != load(folder / 'package.json'):
            raise ValueError('Ownership package differs from its retained source records')
        package = load(folder / 'package.json')
        return {'status': 'passed', 'run_status': package['run_status'], 'records': len(package['records'])}
    raise ValueError('Unknown input role: ' + role)


def discovery_extract(folder, bbl, activity=None):
    """Keep the area search's summary and ranked candidates without copying the whole inventory."""
    from housing_site_discovery.engine import verify
    from .candidates import rank_with_activity
    folder = Path(folder)
    verify(folder)
    ir = load(folder / 'ir.json')
    lots = [lot for lot in ir['lots'] if lot['bbl'] == bbl]
    if len(lots) != 1:
        raise ValueError('Site %s is not in the discovery package' % bbl)
    lot = dict(lots[0])
    lot.pop('public_context', None)
    method, candidates, held, activity_summary = rank_with_activity(folder, activity)
    keep = ('question', 'scope', 'counts', 'order_method', 'admission_method', 'limits', 'request_id')
    return {'version': '1.1', 'retention': 'extract; full package referenced by manifest sha256',
            'package_manifest_sha256': digest((folder / 'manifest.json').read_bytes()),
            'package_name': folder.name, 'summary': {k: ir.get(k) for k in keep},
            'lot': lot, 'lot_csv_row': _csv_row(folder / 'all-lots.csv', bbl),
            'candidate_method': method, 'candidates': candidates, 'in_development': held,
            'activity': activity_summary}


def _csv_row(path, bbl):
    import csv
    if not path.exists():
        return None
    with path.open(newline='') as handle:
        for row in csv.DictReader(handle):
            if row.get('bbl') == bbl:
                return row
    return None


# ---------------------------------------------------------------- build / verify

def expand(paths):
    """Accept package folders or a parent folder holding several packages."""
    out = []
    for path in map(Path, paths):
        if path.is_dir() and not (path / 'manifest.json').exists():
            children = sorted(p for p in path.iterdir() if p.is_dir() and (p / 'manifest.json').exists())
            if not children:
                raise ValueError('No verified packages found in ' + str(path))
            out.extend(children)
        else:
            out.append(path)
    return out


def _slug(text):
    return re.sub(r'[^a-z0-9-]+', '-', text.lower()).strip('-')[:60] or 'item'


def build(request, out, evidence, underwriting, massing=(), ownership=None, render=None, discovery=None, brief=None, activity=None):
    """discovery: a verified discovery package folder, or a discovery-extract.json carried from an earlier report."""
    from .contracts import validate_request
    from .brief import validate as validate_brief
    validate_request(request)
    if brief is None:
        raise ValueError('A run brief is required (python -m housing_feasibility brief start ...)')
    brief_data = validate_brief(load(brief))
    out = destination(out)
    if out.exists() and any(out.iterdir()):
        raise ValueError('Output folder must be new or empty; reports are never overwritten')
    sources = {'evidence': [Path(evidence)], 'underwriting': expand(underwriting),
               'massing': expand(massing), 'ownership': [Path(ownership)] if ownership else [],
               'render': [Path(render)] if render else [], 'activity': [Path(activity)] if activity else []}
    for role, paths in sources.items():
        for path in paths:
            if not path.is_dir():
                raise ValueError('%s package not found: %s' % (role, path))
            if out.resolve().is_relative_to(path.resolve()):
                raise ValueError('Report folder cannot be inside an input package')
            verify_input(role, path)
    if not sources['underwriting']:
        raise ValueError('At least one verified underwriting package is required')
    out.mkdir(parents=True, exist_ok=True)
    names = {}
    for role, paths in sources.items():
        for path in paths:
            if role in ('evidence', 'ownership', 'render', 'activity'):
                target = out / 'inputs' / role
            else:
                target = out / 'inputs' / role / _slug(path.name)
                if target.exists():
                    raise ValueError('Two %s packages share the folder name %s' % (role, path.name))
            shutil.copytree(path, target, ignore=shutil.ignore_patterns('__pycache__'))
            names.setdefault(role, []).append(str(target.relative_to(out)))
    if discovery:
        bbl = load(out / 'inputs/evidence/ir.json')['resolved_bbl']
        if Path(discovery).is_file():
            extract = load(discovery)
            if extract.get('lot', {}).get('bbl') != bbl:
                raise ValueError('Discovery extract is for a different tax lot')
            save(out / 'inputs/discovery-extract.json', extract)
        else:
            save(out / 'inputs/discovery-extract.json', discovery_extract(Path(discovery), bbl, activity))
    save(out / 'request.json', request)
    save(out / 'inputs/brief.json', brief_data)
    save(out / 'inputs/toolkit.json', toolkit_identity())
    write_outputs(out)
    save(out / 'manifest.json', {'version': VERSION, 'module': 'feasibility-report',
                                 'implementation': implementation(), 'files': inventory(out),
                                 'validation_scope': 'Every input package re-verified by its own module; '
                                 'report sections recomputed from retained inputs. Not professional review.'})
    return verify(out)


def write_outputs(out):
    from .report import assemble
    from .present import markdown, html
    report = assemble(out)
    save(out / 'report.json', report)
    (out / 'report.md').write_text(markdown(report))
    (out / 'report.html').write_text(html(report, out))
    return report


def withheld_files(run):
    """Files a bundle deliberately left out (e.g. a third-party source photo), with their declared hashes."""
    path = Path(run).parent / WITHHELD
    if not path.exists():
        return {}
    data = load(path)
    return {item['path']: item['sha256'] for item in data.get('files', [])}


def verify(run):
    from .report import assemble
    from .present import markdown, html
    from .contracts import validate_report
    run = Path(run)
    manifest = load(run / 'manifest.json')
    if manifest.get('module') != 'feasibility-report' or manifest.get('version') != VERSION:
        raise ValueError('Not a feasibility report package (or one built by another report-module version)')
    if manifest['implementation'] != implementation():
        toolkit = load(run / 'inputs/toolkit.json') if (run / 'inputs/toolkit.json').exists() else {}
        raise ValueError('This report was built by a different version of the toolkit. Check out commit %s of %s and verify again.'
                         % (toolkit.get('git_commit') or 'unknown', toolkit.get('repository') or REPOSITORY))
    withheld = withheld_files(run)
    actual = inventory(run)
    for name, sha in withheld.items():
        if name in actual or manifest['files'].get(name) != sha:
            raise ValueError('Withheld-file list does not match the manifest: ' + name)
        actual[name] = sha
    if manifest['files'] != actual:
        raise ValueError('Report package files were added, removed or changed')
    checks = []
    for role in ROLES:
        base = run / 'inputs' / role
        if not base.exists():
            continue
        folders = [base] if role in ('evidence', 'ownership', 'render', 'activity') else sorted(p for p in base.iterdir() if p.is_dir())
        for folder in folders:
            rel = str(folder.relative_to(run))
            held = [n for n in withheld if n.startswith(rel + '/')]
            if held:
                checks.append({'package': rel, 'status': 'hashes_only', 'withheld': held})
                continue
            result = verify_input(role, folder)
            checks.append({'package': rel, 'status': result.get('status')})
    report = assemble(run, fallback_hashes=withheld)
    validate_report(report)
    if load(run / 'report.json') != report:
        raise ValueError('report.json differs from recomputation')
    if (run / 'report.md').read_text() != markdown(report) or (run / 'report.html').read_text() != html(report, run):
        raise ValueError('Report projection changed')
    h = report['headline']
    return {'status': 'passed', 'bbl': report['site']['bbl'], 'address': report['site']['address'],
            'inputs_verified': sum(1 for c in checks if c['status'] == 'passed'),
            'inputs_checked_by_hash_only': [c['package'] for c in checks if c['status'] == 'hashes_only'],
            'evidence_fingerprint': report['provenance']['evidence_fingerprint'], 'base_case': h['base_case_id'],
            'base_gap_usd': h['base_gap_usd'], 'gap_range_usd': h['gap_range_usd'],
            'open_items': len(report['open_items']), 'professional_review': 'pending',
            'report': str((run / 'report.html').resolve())}


def verify_html(html_path, run):
    """Confirm a report.html (e.g. the one that was emailed) matches a bundle exactly."""
    from .present import embedded_report
    embedded = embedded_report(Path(html_path).read_text())
    result = verify(run)
    if embedded != load(Path(run) / 'report.json'):
        raise ValueError('The HTML report does not match this bundle (different data or fingerprint)')
    return {**result, 'html_matches_bundle': True, 'html': str(html_path)}


BUNDLE_README = """# Evidence bundle: {title}

Produced by the Open Housing Toolkit ({repository}), toolkit commit {commit}.
Evidence fingerprint: {fingerprint}

For a person: open `report/report.html`. It is the whole report; this folder holds
the receipts behind it.

For an AI agent asked to review or continue this work:

1. What this is: a site feasibility report assembled from verified packages. Every
   figure comes from a public record (retained bytes with SHA-256 hashes) or an
   assumption the user approved (recorded in `report/inputs/brief.json`).
   `report/report.json` is the typed report; the same JSON is embedded in
   `report.html` (script id "report-data").
2. Verify it:
   git clone {repository} ~/open-housing-toolkit && cd ~/open-housing-toolkit
   git checkout {commit}
   python3 scripts/preflight.py
   .venv/bin/python -m housing_feasibility verify --run PATH/TO/THIS/BUNDLE/report
   .venv/bin/python -m housing_feasibility verify --run PATH/TO/THIS/BUNDLE/report --html PATH/TO/THE/report.html
   The second command confirms an emailed report matches this bundle.
3. Continue it (new heights, rents, a render):
   .venv/bin/python -m housing_feasibility continue --bundle PATH/TO/THIS/BUNDLE/report --out runs/NAME
   then follow skills/start-here/references/received-report.md in the toolkit.

{withheld_note}Contents: report/ (report.html, report.md, report.json, manifest.json, inputs/ with every
verified input package, the run brief and the toolkit identity).
"""


def bundle(run, out, include_source_photo=False):
    """Zip a verified report folder with a README for people and agents."""
    import zipfile
    run = Path(run)
    result = verify(run)
    report = load(run / 'report.json')
    out = Path(out)
    if out.exists():
        raise ValueError('Refusing to overwrite ' + str(out))
    withheld = []
    for photo in sorted((run / 'inputs/render/inputs').glob('reference.*')) if (run / 'inputs/render/inputs').exists() else []:
        if not include_source_photo:
            withheld.append({'path': str(photo.relative_to(run)), 'sha256': digest(photo.read_bytes()),
                             'reason': 'Source photo for the render (for example a Street View screenshot) may carry third-party rights; '
                                       'the generated concept image is included. Re-bundle with --include-source-photo if the user owns it.'})
    held = {w['path'] for w in withheld}
    toolkit = report['provenance']['toolkit']
    note = ''
    if withheld:
        note = ('Withheld: %s. The render package is therefore checked by file hashes only (WITHHELD.json); '
                'everything else is fully re-verified.\n\n' % ', '.join(sorted(held)))
    readme = BUNDLE_README.format(title=report['request']['title'], repository=toolkit['repository'],
                                  commit=toolkit.get('git_commit') or 'unknown',
                                  fingerprint=report['provenance']['evidence_fingerprint'], withheld_note=note)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('README.md', readme)
        if withheld:
            z.writestr(WITHHELD, dumps({'version': '1.0', 'files': withheld}))
        for path in sorted(run.rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts:
                rel = str(path.relative_to(run))
                if rel not in held:
                    z.write(path, 'report/' + rel)
    return {'status': 'bundled', 'bundle': str(out), 'bytes': out.stat().st_size,
            'evidence_fingerprint': report['provenance']['evidence_fingerprint'], 'withheld': sorted(held),
            'report_verified': result['status']}


def continue_from(bundle_run, out):
    """Start a new run from a verified report: reusable inputs plus the brief, marked as extending it."""
    from .brief import validate as validate_brief
    bundle_run = Path(bundle_run)
    verify(bundle_run)
    report = load(bundle_run / 'report.json')
    out = destination(out) if Path(out).resolve().is_relative_to(ROOT) else Path(out)
    if out.exists() and any(out.iterdir()):
        raise ValueError('Output folder must be new or empty')
    held = withheld_files(bundle_run)
    target = out / 'from-report'
    out.mkdir(parents=True, exist_ok=True)
    shutil.copytree(bundle_run / 'inputs', target, ignore=shutil.ignore_patterns('__pycache__', 'brief.json', 'toolkit.json'))
    brief = validate_brief(load(bundle_run / 'inputs/brief.json'))
    brief = dict(brief)
    brief['extends'] = list(brief.get('extends', [])) + [{'title': report['request']['title'],
                                                          'evidence_fingerprint': report['provenance']['evidence_fingerprint'],
                                                          'prepared_on': report['request']['prepared_on']}]
    save(out / 'brief.json', validate_brief(brief))
    reusable = {'evidence': 'from-report/evidence', 'ownership': 'from-report/ownership' if (target / 'ownership').exists() else None,
                'massing': [str(p.relative_to(out)) for p in sorted((target / 'massing').iterdir())] if (target / 'massing').exists() else [],
                'underwriting': 'from-report/underwriting',
                'render': 'from-report/render' if (target / 'render').exists() and not held else None,
                'discovery': 'from-report/discovery-extract.json' if (target / 'discovery-extract.json').exists() else None,
                'parcel_source': next((str(p.relative_to(out)) for p in sorted((target / 'massing').glob('*/parcel-source'))), None)
                if (target / 'massing').exists() else None}
    return {'status': 'ready', 'folder': str(out), 'brief': str(out / 'brief.json'), 'reusable_inputs': reusable,
            'base_case': report['request']['base_case'],
            'next': ['Ask whether the change replaces or adds to the original options, then record it: '
                     'housing_feasibility brief decide --brief {o}/brief.json --step massing --proposed ... --answer ...'.format(o=out),
                     'New height: scripts/plan_lot.py massing --evidence {o}/from-report/evidence --parcel-source {o}/{p} '
                     '--stories N ... --out {o}/plan-N; housing_workflow replay --from-run {o}/from-report/evidence '
                     '--input {o}/plan-N/area-request.json --out {o}/area-N; housing_geometry build --analysis {o}/area-N '
                     '--parcel-source {o}/{p} --scenario {o}/plan-N/geometry-scenario.json --out {o}/massing-N'.format(o=out, p=reusable['parcel_source'] or 'PARCEL'),
                     'New money: scripts/plan_lot.py scenarios --program {o}/plan-N/program.json ... --out {o}/scenarios-N; '
                     'housing_underwriting build for each into {o}/underwriting/ID'.format(o=out),
                     'Report: housing_feasibility build --brief {o}/brief.json --evidence {o}/from-report/evidence '
                     '--ownership {o}/from-report/ownership --discovery {o}/from-report/discovery-extract.json '
                     '--underwriting {o}/underwriting [--underwriting {o}/from-report/underwriting] '
                     '--massing {o}/massing-N [--massing {o}/from-report/massing] ...'.format(o=out)]}
