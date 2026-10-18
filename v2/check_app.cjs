const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const root=path.join(__dirname,'..'),c=JSON.parse(fs.readFileSync(path.join(root,'dist/course.json'),'utf8'));
const sandbox={console,URL,Blob,Date,setTimeout,clearTimeout,localStorage:{setItem(){},getItem(){return null}},document:{querySelector(){return null}},navigator:{},location:{hash:''}};vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(path.join(root,'dist/app.js'),'utf8').replace(/init\(\);\s*$/,''),sandbox);sandbox.course=c;vm.runInContext('C=course; all=[...C.assessments,...C.lessons];',sandbox);
const run=s=>vm.runInContext(s,sandbox);let views=0,links=0;
for(const l of [...c.assessments,...c.lessons]){
 sandbox.lessonId=l.id;run('current=all.find(l=>l.id===lessonId)');
 for(const t of ['learn','tasks','practice']){
  sandbox.tabName=t;const out=run('tab=tabName;lesson(current)');assert(!out.includes('undefined'),l.id+' '+t);
  for(const m of out.matchAll(/(?:href|src)="((?:pdf|audio|units)\/[^"?#]+)"/g)){assert(fs.existsSync(path.join(root,'dist',m[1])),m[1]);links++}views++;
 }
 assert.equal(run('objective(current).score'),0);
 run("for(const q of current.questions)if(q.type==='mc')data(current.id)[q.code]=String(q.answer)");
 assert.equal(run('objective(current).score'),l.format===2?(l.providedTemplate?10:16):6);
 if(l.format===2){run("for(const q of current.questions.filter(q=>q.type!=='mc'))q.criteria.forEach((r,i)=>grades(current.id)[q.code+':'+i]=r.max)");assert.equal(run('score(current).total'),100);assert(run('score(current).complete'));assert.equal(run('score(current).autoMax'),l.providedTemplate?10:16)}
 else {run("for(const q of current.questions.filter(q=>q.type==='short'))grades(current.id)[q.code]=2;for(const skill of ['Speaking','Writing'])for(let i=0;i<5;i++)grades(current.id)[skill+'-'+i]=2");assert.equal(run('score(current).total'),34)}
 run("state.history.push({revision:current.format===2?2:1,id:current.id,at:new Date().toISOString(),score:score(current),answers:{...data(current.id)}})");
}
const progress=run('progressPage()');assert(progress.includes('/100 tổng'));assert(progress.includes('/34 tổng'));
sandbox.backup=JSON.parse(run("JSON.stringify({format:'CatholicEnglishBackup',version:1,state,recordings:[]})"));assert(run('validateBackup(backup).version')===1);
sandbox.bad=JSON.parse(JSON.stringify(sandbox.backup));sandbox.bad.state.history[0].score.graded='<img src=x onerror=alert(1)>';assert.throws(()=>run('validateBackup(bad)'));
assert.equal(run("esc('<img src=x>')"),'&lt;img src=x&gt;');
assert(run('home()').includes('Units_02_26_Theo_Mau_Unit1.zip'));assert(run('sourcesPage()').includes('19 nhiệm vụ'));
console.log(JSON.stringify({renderedViews:views,localAssetLinks:links,scoring:'26 units /100 and 6 prior assessments /34 passed',backup:'new and legacy history accepted; malformed rejected',browser:'not run, control-browser unavailable'}));
