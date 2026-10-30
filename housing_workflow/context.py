"""Typed execution context, separate from source observations and analytical claims. MIT."""
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
import re
from .contracts import digest, load, save


class EvidenceMode(str, Enum):
    LIVE = 'live_collection'
    REPLAY = 'retained_snapshot_replay'
    ANALYSIS = 'retained_snapshot_analysis'
    UNKNOWN = 'not_recorded'


@dataclass(frozen=True)
class ExecutionContext:
    mode: EvidenceMode
    source_manifest_sha256: str | None = None
    version: str = '0.1.0'

    def to_dict(self):
        return {**asdict(self), 'mode': self.mode.value}


def validate(value):
    if not isinstance(value, dict) or set(value) != {'version', 'mode', 'source_manifest_sha256'}:
        raise ValueError('Unsupported execution context fields')
    if value['version'] != '0.1.0':
        raise ValueError('Unsupported execution context version')
    try:
        mode = EvidenceMode(value['mode'])
    except (ValueError, TypeError) as exc:
        raise ValueError('Unsupported evidence mode') from exc
    bound = value['source_manifest_sha256']
    if mode in {EvidenceMode.REPLAY, EvidenceMode.ANALYSIS}:
        if not isinstance(bound, str) or not re.fullmatch('[0-9a-f]{64}', bound):
            raise ValueError('Retained execution needs a source manifest hash')
    elif bound is not None:
        raise ValueError('Live/unrecorded execution cannot claim a retained manifest')
    return ExecutionContext(mode, bound)


def read(folder):
    return validate(load(folder/'execution.json'))


def write(folder, mode, source=None):
    record = ExecutionContext(mode, digest((source/'manifest.json').read_bytes()) if source else None)
    validate(record.to_dict())
    save(folder/'execution.json', record.to_dict())
    return record


def validate_parcel(folder):
    context = read(folder)
    if context.mode == EvidenceMode.ANALYSIS:
        raise ValueError('Parcel execution cannot be a downstream analysis')
    if context.mode == EvidenceMode.REPLAY:
        manifest = folder/'replay-source-manifest.json'
        if digest(manifest.read_bytes()) != context.source_manifest_sha256:
            raise ValueError('Replay source manifest binding changed')
        source = load(manifest)
        paths = ['receipts.json'] + [str(p.relative_to(folder)) for p in sorted((folder/'sources').glob('*.json'))]
        for name in paths:
            if digest((folder/name).read_bytes()) != source['files'].get(name):
                raise ValueError('Replayed evidence differs from the retained source manifest: '+name)
    elif (folder/'replay-source-manifest.json').exists():
        raise ValueError('Replay source cannot be relabeled as live/unrecorded execution')
    return context
