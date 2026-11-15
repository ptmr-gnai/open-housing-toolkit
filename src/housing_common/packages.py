"""Small local package primitives shared by new independent modules. MIT."""
from pathlib import Path
import hashlib
import json
from .local_outputs import destination


def digest(data):return hashlib.sha256(data).hexdigest()
def load(path):return json.loads(Path(path).read_text())
def dumps(value):return json.dumps(value,sort_keys=True,indent=2,allow_nan=False)+'\n'
def save(path,value):Path(path).write_text(dumps(value))


def fresh(out):
    out=destination(out);out.mkdir(parents=True,exist_ok=False);return out
