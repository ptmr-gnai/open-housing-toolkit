"""Write-once analyst artifact receipt before reference comparison. MIT."""
import datetime,json,pathlib,subprocess
from validate import digest,validate
P=pathlib.Path(__file__).resolve().parent
if (P/'freeze.json').exists():raise SystemExit('Already frozen; no overwrite permitted')
result=validate()
r={'frozen_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'precommit_git':subprocess.check_output(['git','rev-parse','HEAD'],cwd=P,text=True).strip(),'files':{name:digest(P/name) for name in ['assessment.md','claims.json','access-log.json']},'rubric_sha256':digest(P/'rubric.json'),'validator_sha256':digest(P/'validate.py'),'freeze_code_sha256':digest(P/'freeze.py'),'input_precommit_sha256':digest(P/'precommit.json'),'technical_validation':result,'curator_already_exposed_to_outcomes':True,'analyst_context':'fresh input-only context; declared access auditable; no OS sandbox or guarantee against model prior knowledge','later_reference_read_in_this_run':'not yet; compare only after freeze commit'}
(P/'freeze.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
