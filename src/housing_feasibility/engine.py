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

VERSION = '1.1.0'
ROLES = ('evidence', 'ownership', 'massing', 'underwriting', 'render')


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
    if role == 'ownership':
        from housing_ownership.engine import build_package
        if build_package(folder) != load(folder / 'package.json'):
            raise ValueError('Ownership package differs from its retained source records')
        package = load(folder / 'package.json')
        return {'status': 'passed', 'run_status': package['run_status'], 'records': len(package['records'])}
    raise ValueError('Unknown input role: ' + role)


def discovery_extract(folder, bbl):
    """Keep the area search's summary and ranked candidates without copying the whole inventory."""
    from housing_site_discovery.engine import verify
    from .candidates import rank
    folder = Path(folder)
    verify(folder)
    ir = load(folder / 'ir.json')
    lots = [lot for lot in ir['lots'] if lot['bbl'] == bbl]
    if len(lots) != 1:
        raise ValueError('Site %s is not in the discovery package' % bbl)
    lot = dict(lots[0])
    lot.pop('public_context', None)
    method, candidates = rank(folder)
    keep = ('question', 'scope', 'counts', 'order_method', 'admission_method', 'limits', 'request_id')
    return {'version': '1.1', 'retention': 'extract; full package referenced by manifest sha256',
            'package_manifest_sha256': digest((folder / 'manifest.json').read_bytes()),
            'package_name': folder.name, 'summary': {k: ir.get(k) for k in keep},
            'lot': lot, 'lot_csv_row': _csv_row(folder / 'all-lots.csv', bbl),
            'candidate_method': method, 'candidates': candidates}


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


def build(request, out, evidence, underwriting, massing=(), ownership=None, render=None, discovery=None, brief=None):
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
               'render': [Path(render)] if render else []}
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
            if role in ('evidence', 'ownership', 'render'):
                target = out / 'inputs' / role
            else:
                target = out / 'inputs' / role / _slug(path.name)
                if target.exists():
                    raise ValueError('Two %s packages share the folder name %s' % (role, path.name))
            shutil.copytree(path, target, ignore=shutil.ignore_patterns('__pycache__'))
            names.setdefault(role, []).append(str(target.relative_to(out)))
    if discovery:
        bbl = load(out / 'inputs/evidence/ir.json')['resolved_bbl']
        save(out / 'inputs/discovery-extract.json', discovery_extract(Path(discovery), bbl))
    save(out / 'request.json', request)
    save(out / 'inputs/brief.json', brief_data)
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


def verify(run):
    from .report import assemble
    from .present import markdown, html
    from .contracts import validate_report
    run = Path(run)
    manifest = load(run / 'manifest.json')
    if manifest.get('module') != 'feasibility-report' or manifest.get('version') != VERSION:
        raise ValueError('Not a feasibility report package')
    if manifest['implementation'] != implementation():
        raise ValueError('Report was built by a different version of the report module; rebuild it into a new folder')
    if manifest['files'] != inventory(run):
        raise ValueError('Report package files were added, removed or changed')
    checks = []
    for role in ROLES:
        base = run / 'inputs' / role
        if not base.exists():
            continue
        folders = [base] if role in ('evidence', 'ownership', 'render') else sorted(p for p in base.iterdir() if p.is_dir())
        for folder in folders:
            result = verify_input(role, folder)
            checks.append({'package': str(folder.relative_to(run)), 'status': result.get('status')})
    report = assemble(run)
    validate_report(report)
    if load(run / 'report.json') != report:
        raise ValueError('report.json differs from recomputation')
    if (run / 'report.md').read_text() != markdown(report) or (run / 'report.html').read_text() != html(report, run):
        raise ValueError('Report projection changed')
    h = report['headline']
    return {'status': 'passed', 'bbl': report['site']['bbl'], 'address': report['site']['address'],
            'inputs_verified': len(checks), 'base_case': h['base_case_id'],
            'base_gap_usd': h['base_gap_usd'], 'gap_range_usd': h['gap_range_usd'],
            'open_items': len(report['open_items']), 'professional_review': 'pending',
            'report': str((run / 'report.html').resolve())}
