import concurrent.futures,pathlib,subprocess,sys
P=pathlib.Path(__file__).resolve().parents[1]
renderer='/root/.codex/skills/builtins/documents/render_docx.py'
def render(n):
 inp=P/f'dist/units/Unit{n}/Unit{n}_Practice.docx';out=P/f'qa-v2/docx/Unit{n}'
 out.mkdir(parents=True,exist_ok=True)
 r=subprocess.run([sys.executable,renderer,str(inp),'--output_dir',str(out),'--emit_pdf','--width','850','--height','1200'],capture_output=True,text=True)
 if r.returncode:raise RuntimeError(f'Unit {n}: '+r.stdout+r.stderr)
 print('Rendered Word Unit',n,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(render,range(2,27)))
