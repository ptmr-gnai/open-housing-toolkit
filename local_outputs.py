"""Local-only output destinations; shipped checkout content is read-only. MIT."""
from pathlib import Path
import hashlib
import os
import tempfile

ROOT=Path(__file__).resolve().parent


def destination(path, root=ROOT):
    """Allow ignored runs/ within this checkout or an explicit external local path."""
    target=Path(path).resolve();base=Path(root).resolve()
    if target==base or (target.is_relative_to(base) and not target.is_relative_to(base/'runs')):
        raise ValueError('Shipped checkout files are read-only; choose a fresh path under runs/ or outside the checkout')
    return target


def new_run(prefix='run', root=ROOT):
    parent=destination(Path(root)/'runs',root)
    parent.mkdir(parents=True,exist_ok=True)
    return Path(tempfile.mkdtemp(prefix=prefix+'-',dir=parent))


def checkout_snapshot(root=ROOT):
    """Include content and mtime to detect even identical-byte rewrites; ignore local artifacts."""
    base=Path(root).resolve();result={}
    excluded={'.git','runs','__pycache__','.pytest_cache','.venv','node_modules'}
    for directory,dirs,files in os.walk(base):
        dirs[:]=[name for name in dirs if name not in excluded]
        for name in files:
            path=Path(directory)/name
            if not path.is_file():continue
            result[str(path.relative_to(base))]=(hashlib.sha256(path.read_bytes()).hexdigest(),path.stat().st_mtime_ns)
    return result


def assert_checkout_unchanged(before, root=ROOT):
    after=checkout_snapshot(root)
    changed=sorted(name for name in set(before)|set(after) if before.get(name)!=after.get(name))
    if changed:raise ValueError('Check modified shipped checkout content: '+', '.join(changed[:20]))
