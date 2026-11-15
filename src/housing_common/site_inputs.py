"""Allowlisted verified inputs for composable site-discovery review stages. MIT."""
from pathlib import Path
import importlib
import json

KINDS={'discovery':'housing_site_discovery.engine',
       'dwelling-review':'housing_site_review.engine',
       'zoning-review':'housing_zoning_review.engine'}


def verify(folder):
    folder=Path(folder)
    manifest=json.loads((folder/'manifest.json').read_text());kind=manifest.get('kind')
    if kind not in KINDS:raise ValueError('Expected a verified discovery or supported site-review stage')
    return importlib.import_module(KINDS[kind]).verify(folder)


def state(folder):
    folder=Path(folder);verify(folder)
    ir=json.loads((folder/'ir.json').read_text())
    if not isinstance(ir.get('lots'),list) or any('bbl' not in r or 'in_recorded_nonhousing_set' not in r for r in ir['lots']):
        raise ValueError('Site-review output does not preserve the discovery lot contract')
    return ir


def original_discovery(folder):
    """Locate retained broad evidence after verifying every supported transformation."""
    folder=Path(folder);verify(folder)
    for _ in range(10):
        kind=json.loads((folder/'manifest.json').read_text())['kind']
        if kind=='discovery':return folder
        if kind not in ['dwelling-review','zoning-review']:raise ValueError('Unsupported review ancestry')
        folder=folder/('discovery' if kind=='dwelling-review' else 'parent')
    raise ValueError('Site-review ancestry exceeds ten stages')
