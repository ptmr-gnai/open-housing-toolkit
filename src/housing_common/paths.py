"""Resolve recorded legacy logical paths without rewriting historical source records. MIT."""
from pathlib import PurePosixPath
from .local_outputs import ROOT
LEGACY=ROOT/'research/legacy-probe'
LEGACY_FILES={'pipeline.py','collect.py','render.py','gates.py','probe.json','lint.py',
              'schema_check.py','validate.py','replay_check.py'}


def historical_file(name):
    path=PurePosixPath(str(name))
    if path.is_absolute() or '..' in path.parts:raise ValueError('Unsafe historical path')
    if path.parts and (path.parts[0] in {'cache','outputs','schemas'} or str(path) in LEGACY_FILES):
        return LEGACY/str(path)
    return ROOT/str(path)
