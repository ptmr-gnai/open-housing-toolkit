"""Read-only public wrapper; original byte-bound validator is archived unchanged. MIT."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.validate_retrospective_portable import validate,legacy
validate_claims=legacy.validate_claims
check_frozen=legacy.check_frozen
digest=legacy.digest
norm=legacy.norm
if __name__=='__main__':print(json.dumps(validate(),indent=2))
