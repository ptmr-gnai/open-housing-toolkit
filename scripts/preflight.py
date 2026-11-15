#!/usr/bin/env python3
"""Install and check the toolkit for a first-time user. MIT.

Run from the repository root with any Python 3 (macOS ships 3.9):

    python3 scripts/preflight.py           # set up if needed, then check
    python3 scripts/preflight.py --check   # check only; install nothing

It finds or installs Python 3.11+, creates .venv, installs the toolkit, fixes
HTTPS certificate verification inside .venv when the system bundle fails, checks
live NYC data access, and reports which optional abilities this computer has
(geometry, image rendering through Codex). It writes runs/preflight.json and
prints a plain summary. It never commits, pushes or uploads anything.

Exit codes: 0 ready, 1 the user must do one thing (printed), 2 unexpected error.
Keep this file compatible with Python 3.9 so it can bootstrap a newer Python.
"""
import argparse
import glob
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV = ROOT / '.venv'
MIN = (3, 11)
PROBE_URL = 'https://data.cityofnewyork.us/api/views/64uk-42ks.json'


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def version_of(python):
    try:
        out = run([python, '-c', 'import sys;print("%d.%d" % sys.version_info[:2])'], timeout=20)
        major, minor = out.stdout.strip().split('.')
        return int(major), int(minor)
    except Exception:
        return None


def venv_python():
    path = VENV / 'bin' / 'python'
    return str(path) if path.exists() else None


def find_python():
    """Return (path, how) for a Python >= 3.11, or (None, reason)."""
    candidates = [sys.executable]
    for name in ['python3.13', 'python3.12', 'python3.11', 'python3']:
        found = shutil.which(name)
        if found:
            candidates.append(found)
    for pattern in ['/opt/homebrew/bin/python3.1[1-9]', '/usr/local/bin/python3.1[1-9]',
                    '/Library/Frameworks/Python.framework/Versions/3.1[1-9]/bin/python3',
                    os.path.expanduser('~/.local/share/uv/python/cpython-3.1[1-9]*/bin/python3')]:
        candidates += sorted(glob.glob(pattern), reverse=True)
    uv = shutil.which('uv')
    if uv:
        out = run([uv, 'python', 'find', '>=3.11'], timeout=60)
        if out.returncode == 0 and out.stdout.strip():
            candidates.append(out.stdout.strip())
    for c in candidates:
        v = version_of(c)
        if v and v >= MIN:
            return c, 'found Python %d.%d' % v
    return None, 'no Python 3.11+ found'


def install_python():
    """Try user-level installers that need no administrator password."""
    uv = shutil.which('uv')
    if uv:
        out = run([uv, 'python', 'install', '3.12'], timeout=900)
        if out.returncode == 0:
            return find_python()
    brew = shutil.which('brew')
    if brew:
        out = run([brew, 'install', 'python@3.12'], timeout=1800)
        if out.returncode == 0:
            return find_python()
    return None, 'could not install Python automatically'


def ensure_venv(python, log):
    vp = venv_python()
    if vp and (version_of(vp) or (0, 0)) >= MIN:
        log.append('Reused existing .venv')
        return vp
    if VENV.exists():
        # An old or broken environment: move it aside rather than deleting it.
        backup = ROOT / ('.venv-old-%d' % os.getpid())
        VENV.rename(backup)
        log.append('Moved an older .venv to ' + backup.name)
    out = run([python, '-m', 'venv', str(VENV)], timeout=300)
    if out.returncode:
        raise RuntimeError('Could not create .venv: ' + out.stderr[-800:])
    log.append('Created .venv')
    return venv_python()


def pip_install(vp, log):
    base = run([vp, '-m', 'pip', 'install', '--quiet', '--disable-pip-version-check',
                '-e', '.', 'certifi'], cwd=ROOT, timeout=1800)
    if base.returncode:
        raise RuntimeError('Toolkit install failed: ' + (base.stderr or base.stdout)[-1200:])
    log.append('Installed the toolkit into .venv')
    geo = run([vp, '-m', 'pip', 'install', '--quiet', '--disable-pip-version-check',
               '-e', '.[geometry]'], cwd=ROOT, timeout=1800)
    log.append('Installed optional geometry support' if geo.returncode == 0
               else 'Optional geometry support did not install (building shapes unavailable)')


def https_status(vp):
    """'ok', 'certificate' or 'offline: ...' for the default HTTPS setup in .venv."""
    code = ('import urllib.request,sys\n'
            'try:\n'
            '    urllib.request.urlopen(sys.argv[1],timeout=20).read(64);print("ok")\n'
            'except Exception as e:\n'
            '    print("certificate" if "CERTIFICATE_VERIFY_FAILED" in str(e) else "offline: "+str(e)[:160])\n')
    return run([vp, '-c', code, PROBE_URL], timeout=60).stdout.strip() or 'offline: no response'


def fix_certificates(vp, log):
    """Point .venv at certifi's bundle via sitecustomize, so every module works."""
    site = run([vp, '-c', 'import sysconfig;print(sysconfig.get_paths()["purelib"])']).stdout.strip()
    target = Path(site) / 'sitecustomize.py'
    target.write_text('# Written by scripts/preflight.py: the system CA bundle failed HTTPS checks.\n'
                      'import os\n'
                      'try:\n'
                      '    import certifi\n'
                      '    os.environ.setdefault("SSL_CERT_FILE", certifi.where())\n'
                      'except ImportError:\n'
                      '    pass\n')
    log.append('Fixed HTTPS certificate checks inside .venv (certifi bundle)')


def agent_runtime():
    if os.environ.get('CLAUDECODE') or any(k.startswith('CLAUDE_CODE') for k in os.environ):
        return 'claude-code'
    if any(k.startswith('CODEX') for k in os.environ):
        return 'codex'
    return 'unknown'


def codex_on_computer():
    places = [shutil.which('codex'), '/Applications/Codex.app',
              '/Applications/ChatGPT.app/Contents/Resources/codex-cli']
    return [p for p in places if p and os.path.exists(p)]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--check', action='store_true', help='check only; install nothing')
    args = ap.parse_args()
    log, needs = [], []
    report = {'checkout': str(ROOT), 'platform': platform.platform(), 'agent': agent_runtime()}

    vp = venv_python()
    if not args.check:
        python, how = find_python()
        if not python:
            log.append('No Python 3.11+ found; trying a user-level install')
            python, how = install_python()
        if not python:
            needs.append('Install Python 3.12 from https://www.python.org/downloads/macos/ '
                         '(download and double-click the installer), then run this again.')
        else:
            log.append(how)
            vp = ensure_venv(python, log)
            pip_install(vp, log)
    report['python'] = vp and '%d.%d' % (version_of(vp) or (0, 0))
    report['installed'] = bool(vp) and run([vp, '-c', 'import housing_site_discovery, housing_workflow'],
                                            cwd=ROOT).returncode == 0
    if vp and not report['installed'] and not needs:
        needs.append('The toolkit is not installed in .venv; run python3 scripts/preflight.py without --check.')

    if vp and report['installed']:
        status = https_status(vp)
        if status == 'certificate' and not args.check:
            fix_certificates(vp, log)
            status = https_status(vp)
        report['live_nyc_data'] = status
        report['geometry'] = run([vp, '-c', 'import shapely'], cwd=ROOT).returncode == 0
        tour = run([vp, '-c', 'import housing_workflow, housing_recipe, housing_benefit, housing_rer'], cwd=ROOT)
        report['offline_tour'] = tour.returncode == 0

    codex = codex_on_computer()
    report['codex_on_computer'] = codex
    if report['agent'] == 'codex':
        report['images'] = 'Codex: can generate images when its image tool is available in this session.'
    elif codex:
        report['images'] = ('This agent cannot generate images, but Codex is installed on this computer: '
                            'render briefs prepared here can be opened in Codex to generate the image.')
    else:
        report['images'] = ('This agent cannot generate images and Codex was not found. Render briefs '
                            '(a ready-to-use image prompt) can still be prepared for later.')
    report['log'], report['user_action_needed'] = log, needs
    report['ready'] = bool(report.get('installed')) and not needs

    (ROOT / 'runs').mkdir(exist_ok=True)
    (ROOT / 'runs' / 'preflight.json').write_text(json.dumps(report, indent=2) + '\n')

    print('Open Housing Toolkit preflight')
    for line in log:
        print('  - ' + line)
    print('Ready: ' + ('yes' if report['ready'] else 'no'))
    print('Python environment: ' + (str(VENV) if vp else 'missing'))
    if 'live_nyc_data' in report:
        live = report['live_nyc_data']
        print('Live NYC public data: ' + ('reachable' if live == 'ok' else live))
        print('Building shapes (geometry): ' + ('available' if report['geometry'] else 'not installed'))
    print('Images: ' + report['images'])
    for item in needs:
        print('USER ACTION NEEDED: ' + item)
    print('Details: runs/preflight.json. Run toolkit commands with .venv/bin/python.')
    return 0 if report['ready'] else 1


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:  # report plainly; the agent relays it
        print('Preflight error: %s' % exc, file=sys.stderr)
        raise SystemExit(2)
