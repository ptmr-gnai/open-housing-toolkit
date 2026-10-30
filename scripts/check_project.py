"""Build/check in a new ignored local run; shipped files must remain untouched. MIT."""
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from local_outputs import new_run,checkout_snapshot,assert_checkout_unchanged
import pipeline


def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['check','release']);args=p.parse_args()
    before=checkout_snapshot();run=new_run(args.mode);out=run/'core';steps=[]
    print('Local check workspace: '+str(run),flush=True)
    try:
        pipeline.export(pipeline.build(ROOT/'probe.json'),out,ROOT/'probe.json')
        commands=[[sys.executable,'lint.py','--run',str(out)],
                  [sys.executable,'-m','unittest','discover','-s','tests','-v'],
                  [sys.executable,'schema_check.py','--run',str(out)],
                  [sys.executable,'validate.py',str(out)],
                  [sys.executable,'replay_check.py','--run',str(out)]]
        if args.mode=='release':commands += [['node','tests/check_explorer.cjs',str(out)]]
        for i,command in enumerate(commands,1):
            result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
            log=f'{i:02d}.log';(run/log).write_text(result.stdout+result.stderr)
            steps.append({'command':command,'returncode':result.returncode,'log':log})
            (run/'steps.json').write_text(json.dumps(steps,indent=2)+'\n')
            if result.returncode:raise ValueError('Check failed; inspect '+str(run/log))
        if args.mode=='release':
            manifest=pipeline.read_json(out/'manifest.json')
            for name in ['preview-desktop.png','preview-mobile.png']:manifest['output_sha256'][name]=pipeline.digest(out/name)
            pipeline.write_json(out/'manifest.json',manifest)
            import validate
            validate.validate(out)
    finally:
        assert_checkout_unchanged(before)
    print(json.dumps({'status':'passed','local_workspace':str(run),'shipped_files_written':False}))


if __name__=='__main__':
    try:main()
    except (ValueError,OSError) as exc:
        print(str(exc),file=sys.stderr);raise SystemExit(2)
