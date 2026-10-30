"""Check the pinned historical experiment in local scratch, never regenerate its outputs. MIT."""
from pathlib import Path
import json,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from local_outputs import new_run,checkout_snapshot,assert_checkout_unchanged


def main():
    workspace=new_run('historical-conclusion-check')
    for name in ['probe.json','schemas','cache','research/conclusion-probe']:
        source=ROOT/name;target=workspace/name;target.parent.mkdir(parents=True,exist_ok=True)
        if source.is_dir():shutil.copytree(source,target,ignore=shutil.ignore_patterns('__pycache__'))
        else:shutil.copyfile(source,target)
    for name in ['pipeline.py','gates.py']:
        shutil.copyfile(ROOT/'archive/historical-research/core'/name,workspace/name)
    before=checkout_snapshot(workspace)
    try:
        commands=[[sys.executable,'research/conclusion-probe/validate_probe.py'],
                  [sys.executable,'-m','unittest','discover','-s','research/conclusion-probe/tests','-v']]
        for command in commands:subprocess.run(command,cwd=workspace,check=True)
    finally:assert_checkout_unchanged(before,workspace)
    print(json.dumps({'status':'passed','historical_code':'original pinned bytes','local_workspace':str(workspace),'shipped_outputs_regenerated':False}))


if __name__=='__main__':main()
