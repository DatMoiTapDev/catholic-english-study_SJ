import json,pathlib,copy,re,shutil,subprocess
from docx import Document
from docx.oxml.ns import qn
from topics import TOPICS
from scenarios_vi import SCENARIOS_VI
P=pathlib.Path(__file__).resolve().parents[1];D=P/'dist';V=P/'v2'
# Keep the previous published data as the source of the distinct situational readings/audio.
basepath=V/'base-course.json'
if not basepath.exists():basepath.write_bytes(subprocess.check_output(['git','show','HEAD:dist/course.json'],cwd=P))
C=json.loads(basepath.read_text()); old=copy.deepcopy(C['lessons'])
base_defs=[
['A response to God involving trust and assent, not merely information.','A local community of the faithful in the Church.','Reverence and adoration directed to God.','People sharing life, responsibilities, and relationships in a setting.'],
['The sacred biblical writings received in the Church.','The good news of Christ or a particular Gospel book, according to context.','A selected section of a text considered with its context.','A numbered unit within a biblical chapter.'],
['One God in three distinct divine persons.','The Son becoming truly human without ceasing to be divine.','Christ rising from the dead, distinct from the Incarnation.','God’s gift and help, not simply elegance or manners.'],
['The lay faithful considered collectively.','A particular Church entrusted to the pastoral care of a bishop.','An ordained pastor with episcopal responsibility.','A form of ecclesial service, not a government department in this context.'],
['The sacrament of Christian rebirth and incorporation into Christ and the Church.','The sacrament that strengthens baptismal grace, not appointment confirmation.','The sacrament of Christ’s body and blood, central to Catholic life.','Restoration of communion; in context, the Sacrament of Penance.'],
['The altar in the liturgical space, distinct from the ambo.','The place for proclamation of the Word in the liturgy.','A sacred vessel used for the Eucharistic wine.','The priest’s outer vestment at Mass in the Roman Rite.'],
['The Church’s liturgical worship, not any gathering without distinction.','Preaching within a liturgical celebration.','Ecclesial sharing and unity, or receiving Holy Communion in context.','The concluding sending forth in the celebration.'],
['A living relationship with God expressed in various forms.','Prayer offered for others.','Prayer acknowledging gifts received from God.','Religious dedication or a particular devotional practice, depending on context.'],
['A call related to God and a way of life, broader than employment.','A process of learning and growth in a way of life.','A solemn commitment to God in religious life.','A person in the novitiate, distinct from a candidate.'],
['A member of the Society of Jesus, not any employee of a Jesuit institution.','Prayerful seeking of God’s guidance, not merely a preference.','A prayerful review of life, not an academic examination.','A being sent or a shared field of service in an ecclesial context.'],
['An ordained minister in the presbyterate, distinct from a deacon or bishop.','An ordained minister in the diaconate.','A religious title or family relationship; the title does not itself mean priest.','A person appointed to pastoral care in an institution or specified community.'],
['Relating to care of people in ecclesial life, not simply countryside.','Attentive support for a person’s process without taking control of it.','Someone offering service in a specified activity.','Respectful handling of private information, not public distribution.'],
['A proposition or position put forward for consideration.','Information or reasons offered to support a claim.','The origin of an idea or text that should be identified.','A faithful restatement in a genuinely new structure, still attributed.']]
american={'worship':'/ˈwɝːʃɪp/','scripture':'/ˈskrɪptʃɚ/','gospel':'/ˈɡɑːspəl/','verse':'/vɝːs/','incarnation':'/ˌɪnkɑːrˈneɪʃən/','confirmation':'/ˌkɑːnfɚˈmeɪʃən/','altar':'/ˈɔːltɚ/','ambo':'/ˈæmboʊ/','chasuble':'/ˈtʃæzəbəl/','liturgy':'/ˈlɪtɚdʒi/','homily':'/ˈhɑːməli/','prayer':'/prer/','intercession':'/ˌɪntɚˈseʃən/','devotion':'/dɪˈvoʊʃən/','vocation':'/voʊˈkeɪʃən/','formation':'/fɔːrˈmeɪʃən/','novice':'/ˈnɑːvɪs/','discernment':'/dɪˈsɝːnmənt/','brother':'/ˈbrʌðɚ/','pastoral':'/ˈpæstərəl/','volunteer':'/ˌvɑːlənˈtɪr/','confidentiality':'/ˌkɑːnfɪdenʃiˈæləti/','source':'/sɔːrs/','paraphrase':'/ˈpærəfreɪz/'}
intro_en='This lesson develops Catholic vocabulary through definitions, conceptual distinctions, and a bilingual reading. The aim is to understand what a term means, why a distinction matters, and how to use it with a particular reader or listener. Work at B1 with support first; use the extended language tasks when you can explain the core content accurately. B2 labels identify optional language practice, not a guaranteed course outcome.'
intro_vi='Bài này phát triển từ vựng Công giáo qua định nghĩa, phân biệt khái niệm và bài đọc song ngữ. Mục tiêu là hiểu từ có nghĩa gì, vì sao cần phân biệt và dùng với người đọc hoặc người nghe nào. Học phần lõi B1 có hỗ trợ trước; làm phần ngôn ngữ mở rộng khi đã giải thích đúng ý chính. B2 chỉ mức luyện thêm, không phải cam kết đầu ra.'
new=[]
def crit(label,max_,category,desc):return dict(label=label,max=max_,category=category,desc=desc)
def make_q(code,skill,type_,prompt,points,answer,explanation='',options=None,criteria=None):
 q=dict(code=code,skill=skill,type=type_,prompt=prompt,points=points,answer=answer,explanation=explanation,criteria=criteria or [])
 if options is not None:q['options']=options
 return q

def mc(code,skill,prompt,right,wrong,points,n):
 opts=[right]+wrong;shift=n%4;opts=opts[-shift:]+opts[:-shift] if shift else opts
 return make_q(code,skill,'mc',prompt,points,shift,'Chọn ý phù hợp với dữ kiện và phạm vi của bài; không thêm khẳng định ngoài văn bản.',options=opts)

for n,l in enumerate(old,1):
 u=(n-1)//2;t=TOPICS[u];l['format']=2;l['contentVersion']='unit1-form-v2';l['reference']=t['ref'];l['intro']=[intro_en,intro_vi];l['core']=t['core'];l['distinctions']=t['distinctions'];l['patterns']=t['grammar'];l['readingPairs']=t['core']+[(l['reading'],SCENARIOS_VI[n-1])];l['reading']='\n\n'.join(x[0] for x in l['readingPairs']);l['readingTitle']=l['title']+' Meaning and Use in Context';l['scenarioVi']=SCENARIOS_VI[n-1]
 for k,v in enumerate(l['vocab']):v['definition']=base_defs[u][k];v['ipa']=american.get(v['word'].lower(),v['ipa'])
 for raw in t['extra'].splitlines():
  word,ipa,pos,meaning,definition,example,collocation=raw.split('|');l['vocab'].append(dict(word=word,ipa=ipa,pos=pos,meaning=meaning,definition=definition,example=example,collocation=collocation))
 assert len(l['vocab'])==20
 for k,v in enumerate(l['vocab']):v['priority']='MUST KNOW' if k<10 else 'SHOULD KNOW' if k<15 else 'ADVANCED'
 l['extension']=[dict(theme='A distinction worth revisiting',en=t['distinctions'][n%4][1],vi=t['distinctions'][n%4][2],status='Proposed extension; not a new syllabus requirement'),dict(theme='Language and sources',en='A learning explanation can be accurate and useful without becoming an official Church text. Identify the source, distinguish quotation from explanation, and acknowledge what the source does not establish.',vi='Giải thích học tập có thể đúng và hữu ích mà không trở thành bản văn Giáo hội chính thức. Nêu nguồn, tách trích dẫn khỏi giải nghĩa và nhận giới hạn của nguồn.',status='Study method')]
 l['recall']=[x[0]+': '+x[1] for x in t['distinctions']]+[v['word']+': '+v['definition'] for v in l['vocab'][:6]]+['Use the term in a sentence for a specific listener.','Identify one claim that needs source verification.']
 oldqs=old[n-1]['questions'];rq=next(q for q in oldqs if q['code']=='R1');iq=next(q for q in oldqs if q['code']=='R2');lm=oldqs[0];ls=oldqs[1]
 main=t['core'][0][0].split('. ')[0].rstrip('.')+'.'
 qq=[mc('R01','Reading','Which statement best expresses the main focus of the first teaching paragraph?',main,['The paragraph gives only a timetable for an event.','The paragraph presents a newly authorised liturgical text.','The paragraph argues that terminology never depends on context.'],2,n),mc('R02','Reading',rq['prompt'],rq['answer'],['The speaker gives no reason for the action.','The action is required only to display advanced vocabulary.','The action replaces the need for any appropriate guidance.'],2,n+1),mc('R03','Reading',iq['prompt'],iq['answer'],['Because any confident answer is necessarily accurate.','Because practical examples are forbidden in English learning.','Because checking meaning is unnecessary once a word is familiar.'],2,n+2)]
 v=next(v for v in l['vocab'] if re.search(r'\b'+re.escape(v['word'])+r'\b',l['reading'],re.I))
 other=[x['definition'] for x in l['vocab'] if x['word']!=v['word']][:3]
 qq.append(mc('R04','Reading',f"In the reading, what does '{v['word']}' mean?",v['definition'],other,2,n+3))
 a,b,vi=t['distinctions'][0]
 qq.append(mc('R05','Reading',f"Which conclusion about {a} is NOT supported by the lesson?",'The two expressions can replace one another in every sentence.',[b,'Context helps determine which expression is appropriate.','A clear explanation should identify the relevant distinction.'],2,n+4))
 for k,(pair,meaning,vi) in enumerate(t['distinctions'],1):
  qq.append(make_q(f'V{k:02}','Terminology','short','In 40–70 English words, distinguish '+pair+'. Explain each meaning and give an appropriate example or use in context.',5,meaning+' '+vi,'Giữ đủ định nghĩa, điểm khác nhau và ví dụ. Không đánh giá chỉ theo việc giống câu mẫu.',criteria=[crit('Nội dung và nghĩa thuật ngữ',3,'catholic','3: đúng cả hai vế và phân biệt; 2: đúng cơ bản nhưng thiếu ý; 1: chỉ đúng một vế; 0: sai ý chính.'),crit('Ví dụ và ngôn ngữ',2,'language','2: ví dụ hợp nghĩa, diễn đạt rõ; 1: thiếu ví dụ hoặc còn lỗi gây mơ hồ; 0: chưa truyền được ý.')]))
 qq.append(make_q('G01','Grammar','short',f"Write one complete sentence about this lesson using '{t['grammar'][0][0]}'. Keep the meaning appropriate to the lesson.",4,t['grammar'][0][1],t['grammar'][0][2],criteria=[crit('Cấu trúc và nghĩa câu',4,'language','4: đúng cấu trúc, đủ câu và đúng bối cảnh; 2–3: có lỗi nhỏ; 1: dùng được một phần; 0: sai hoặc bỏ trống.')]))
 qq.append(make_q('G02','Grammar','short',f"Write one complete sentence using '{t['grammar'][1][0]}'. Use a concrete idea from the reading.",3,t['grammar'][1][1],t['grammar'][1][2],criteria=[crit('Cấu trúc và liên hệ bài đọc',3,'language','3: đúng cấu trúc và ý; 2: lỗi nhỏ; 1: chỉ đúng một phần; 0: sai hoặc bỏ trống.')]))
 qq.append(make_q('G03','Grammar','short',f"Extension: use '{t['grammar'][2][0]}' in a sentence that explains a distinction or limitation in the lesson. A clear correct sentence is more important than complexity.",3,t['grammar'][2][1],t['grammar'][2][2],criteria=[crit('Cấu trúc và độ chính xác',3,'language','3: câu rõ, đúng cấu trúc và nghĩa; 2: có lỗi nhỏ; 1: ý chưa rõ; 0: chưa đáp ứng.')]))
 sp='Explain the difference between '+t['distinctions'][0][0]+' to a visitor unfamiliar with Catholic terminology. Use one example from the situation in paragraph 3.'
 qq.append(make_q('S01','Speaking','speaking','Prepare for 2 minutes. Write a 100–130-word speaking script and rehearse aloud for 60–90 seconds. '+sp+' After speaking, answer: Which distinction or limit matters most for this listener?',12,'Dàn ý: chào và xác định người nghe → giải thích điểm chính → phân biệt hai từ dễ nhầm → ví dụ thực tế → mời hỏi. Dùng định nghĩa và ngữ cảnh trong bài, không tự nhận thẩm quyền chưa có.','Bản viết chỉ cho biết nội dung và ngôn ngữ. Độ dễ hiểu/phát âm chỉ nhận xét khi có bản ghi hoặc nghe trực tiếp.',criteria=[crit('Nội dung Công giáo và vai trò',3,'catholic','3: thuật ngữ và vai trò đúng; 2: thiếu một phân biệt; 1: có điểm cần kiểm tra; 0: sai ý quan trọng.'),crit('Nhiệm vụ và ngôn ngữ',9,'language','0–3 nhiệm vụ/độ dài; 0–3 tổ chức và phù hợp người nghe; 0–3 từ vựng-ngữ pháp. Phát âm không suy ra từ kịch bản viết.')]))
 qq.append(make_q('S02','Speaking','speaking',f"Write a 6-turn dialogue between a learner or volunteer and an English-speaking visitor based on the situation in paragraph 3. Include one clarification question, an explanation of a specialist term, and an appropriate next step. Prepare for 2 minutes and perform with a partner for 2–3 minutes.",8,'6 lượt gợi ý: khách hỏi → người học kiểm tra điều cần biết → khách làm rõ → giải thích từ có ví dụ → khách hỏi tiếp → trả lời hoặc giới thiệu đúng nguồn/người phụ trách.','Hội thoại cần có phản hồi qua lại, không phải hai bài độc thoại.',criteria=[crit('Nội dung và bối cảnh',2,'catholic','2: nghĩa từ và bước tiếp theo phù hợp; 1: còn mơ hồ; 0: sai hoặc vượt trách nhiệm.'),crit('Tương tác và tiếng Anh',6,'language','0–2 đủ sáu lượt; 0–2 đáp đúng lời nhau; 0–2 câu và từ dễ hiểu.')]))
 wp=next(q for q in oldqs if q['type']=='writing')['prompt'].split(' Use an appropriate')[0]
 qq.append(make_q('W01','Writing','writing',wp+' Write 150–180 words for the reader identified in the task. State your main point, explain a relevant Catholic distinction, give one concrete example, and include one accurate reference from '+t['ref']+'. A paraphrase is sufficient; do not invent a quotation. Allow 25 minutes.',22,'Dàn ý có thể dùng: mục đích với người đọc → điểm chính của chủ đề → phân biệt khái niệm → ví dụ trong tình huống → dẫn nguồn phù hợp với chính nhận định được nguồn hỗ trợ → kết luận hoặc việc tiếp theo. Dẫn nguồn không chỉ là thêm một tên văn kiện ở cuối đoạn.','Bài viết là giải thích hoặc giao tiếp thực tế, không phải bài suy tư cá nhân thay người học.',criteria=[crit('Nội dung và dùng nguồn',6,'catholic','0–3 đúng nghĩa và phân biệt; 0–2 nguồn hỗ trợ đúng nhận định; 0–1 không thêm dữ kiện hoặc vai trò sai.'),crit('Hoàn thành và ngôn ngữ',16,'language','0–4 mục đích/người đọc/độ dài; 0–4 tổ chức; 0–4 từ vựng; 0–4 ngữ pháp và dấu câu.')]))
 qq.append(make_q('C01','Critical reading','short',f"In 90–120 English words, explain why '{t['distinctions'][0][0]}' needs a distinction rather than one interchangeable definition. Refer to two details or examples from the reading, identify one possible misunderstanding, and state one limit of your explanation.",8,t['distinctions'][0][1]+' Use one teaching detail from paragraphs 1–2 and one situational detail from paragraph 3. Explain what each detail supports. Do not claim that one example proves every case.','Chấm lập luận dựa trên bài, không chấm mức độ người học bày tỏ niềm tin cá nhân.',criteria=[crit('Hiểu và lập luận nội dung',4,'catholic','0–2 phân biệt đúng; 0–1 nhận diện hiểu nhầm; 0–1 nêu giới hạn hợp lý.'),crit('Bằng chứng và diễn đạt',4,'language','0–2 dùng hai chi tiết có cơ sở; 0–2 mạch lạc, từ và câu rõ.')]))
 qq.append(make_q('L01','Listening','mc','Listen to the audio twice. '+lm['prompt'],3,lm['answer'],lm['explanation'],options=lm['options']))
 qq.append(make_q('L02','Listening','short','State two practical details from the audio. Do not add information that you cannot hear.',4,'. '.join(l['script'].split('. ')[:2]).rstrip('.')+'.','Mỗi chi tiết đúng được 2 điểm. Chấp nhận bất kỳ hai dữ kiện thực tế có trong audio, không chỉ hai dữ kiện gợi ý.',criteria=[crit('Hiểu thông tin nghe',4,'task','4: hai chi tiết đúng; 2: một chi tiết đúng; 0: chưa có chi tiết đúng; có thể cho 1 hoặc 3 khi đúng một phần.')]))
 qq.append(mc('L03','Listening',ls['prompt'],ls['answer'],['The audio does not provide this information.','Only after the activity has ended.','It must be announced publicly to every visitor.'],3,n+1))
 l['questions']=qq;l['totalPoints']=100;l['selfStudyMinutes']='120–150 phút học và 45–75 phút làm bài/ôn thêm';l['pdfs']=[f'Unit{n}_Curriculum.pdf',f'Unit{n}_Questions.pdf',f'Unit{n}_Practice.docx'];l['downloads']=[f'units/Unit{n}/'+x for x in l['pdfs']]
 assert len(qq)==19 and sum(q['points'] for q in qq)==100
 for q in qq:
  if q['type']!='mc':assert sum(x['max'] for x in q['criteria'])==q['points'],q
 new.append(l)
# Keep the supplied Unit 1 files byte-for-byte; only the online practice view is transcribed.
unit=new[0];unit['providedTemplate']=True;unit['audio']=None;unit['audioSeconds']=0;unit['questions']=[]
source_unit1=(P.parent/'upload') if (P.parent/'upload/Unit1_Practice.docx').exists() else (D/'units/Unit1')
doc=Document(source_unit1/'Unit1_Practice.docx');pending=None
for node in doc.element.body:
 if node.tag==qn('w:p'):
  text=''.join(node.itertext()) # XML itertext repeats some run text; use python-docx wrapper instead.
  from docx.text.paragraph import Paragraph
  text=Paragraph(node,doc).text
  m=re.match(r'([RVGSWC]\d{2})\s*\|\s*(.*?)\s*\((\d+) points\)\s*$',text)
  if m:
   code,prompt,pts=m.groups();skill={'R':'Reading','V':'Terminology','G':'Grammar','S':'Speaking','W':'Writing','C':'Critical reading'}[code[0]]
   pending=make_q(code,skill,'mc' if code[0]=='R' else 'speaking' if code[0]=='S' else 'writing' if code[0]=='W' else 'short',prompt,int(pts),'Xem nội dung giáo trình mẫu và tiêu chí ở cuối phiếu; các cách diễn đạt tương đương được chấp nhận.')
   unit['questions'].append(pending)
 elif node.tag==qn('w:tbl') and pending and pending['type']=='mc' and 'options' not in pending:
  from docx.table import Table
  pending['options']=[row.cells[1].text for row in Table(node,doc).rows];pending['answer']=[1,2,1,3,2][int(pending['code'][1:])-1];pending['explanation']='Đối chiếu bài Faith, Identity, and Life in the Church trong giáo trình Unit 1 do bạn cung cấp.'
assert len(unit['questions'])==16 and sum(q['points'] for q in unit['questions'])==100
for q in unit['questions']:
 if q['type']!='mc':
  p=q['points'];a=max(1,p//3)
  q['criteria']=[crit('Nội dung và thuật ngữ',a,'catholic','Dựa vào định nghĩa, phân biệt và nguồn trong giáo trình Unit 1.'),crit('Hoàn thành và tiếng Anh',p-a,'language','Dựa vào yêu cầu, số từ, mạch lạc, từ vựng và ngữ pháp; không suy ra phát âm từ bản viết.')]
unit['readingTitle']='Faith, Identity, and Life in the Church'
unit['reading']="""For many people, religion is closely connected with family traditions, cultural identity, and moral values. However, from a Catholic perspective, faith is more than belonging to a religious tradition. It is a personal and communal response to God, who reveals himself and invites human beings into a relationship with him.

Catholic faith involves both intellectual understanding and personal commitment. Believers are invited not only to accept the truths of the Christian faith but also to allow these truths to influence their decisions, relationships, and actions. In this sense, faith is not simply something people possess; it is also something they are called to live.

The Church plays an essential role in this journey. Although faith involves a personal response, it is not intended to remain an entirely private experience. Christians belong to a community in which they receive the sacraments, listen to the Word of God, participate in worship, and serve those in need. The Church therefore provides a setting in which faith is expressed, celebrated, and strengthened.

For Jesuit candidates, this understanding has particular significance. Their formation is not limited to acquiring religious knowledge or developing academic skills. It also involves learning how to pray, live in community, discern God's call, and grow in availability for service. These dimensions of formation are closely connected, even though each requires attention and effort.

Learning Catholic English can support this process. By becoming familiar with theological vocabulary and ecclesial expressions, candidates can engage more confidently with Catholic documents, communicate with members of the universal Church, and reflect on questions of faith with greater precision. Ultimately, learning a religious language should not be reduced to memorizing unfamiliar terms. Its deeper educational purpose is to help learners understand what the words mean, recognize the contexts in which they are used, and communicate responsibly about the beliefs and practices of the Church."""
for i,q in enumerate(unit['questions']):
 if q['code']=='V01':q['answer']='Faith includes a personal and communal response to God involving belief and trust; belief can name acceptance of a proposition. They overlap but are not interchangeable.'
 if q['code']=='V02':q['answer']='Church can refer to the community of believers; church may refer to a building. Example: The Church proclaims the Gospel. The church opens at six.'
 if q['code']=='V03':q['answer']='Prayer is expressed in several forms of relationship with God; worship emphasises reverence and adoration directed to God. They overlap without being identical labels in every context.'
 if q['code']=='V04':q['answer']='Catholics are Christians, but Christian does not always identify a person as Catholic. Catholic and Christian therefore cannot replace each other in every sentence.'
 if q['code']=='G01':q['answer']='Faith involves not merely accepting teachings but also trusting God.'
 if q['code']=='G02':q['answer']='Although prayer is personal, it has a communal dimension.'
 if q['code']=='G03':q['answer']='From a Catholic perspective, revelation is God’s self-communication and invitation into relationship with him.'
unit['readingPairs']=[]
for n in range(1,27):
 (D/'units'/f'Unit{n}').mkdir(parents=True,exist_ok=True)
for name in ['Curriculum.pdf','Questions.pdf','Practice.docx']:
 src=source_unit1/('Unit1_'+name);dst=D/'units/Unit1'/('Unit1_'+name)
 if src.resolve()!=dst.resolve():shutil.copyfile(src,dst)
C['lessons']=new;C['schemaVersion']=2;C['templateNote']='Unit 1 giữ nguyên ba file bạn cung cấp. Unit 2–26 theo cấu trúc song ngữ 8 phần; giữ mã R/V/G/S/W/C, bổ sung Listening L01–L03. Bài 2–26: 19 nhiệm vụ, 100 điểm đề xuất; không phải trọng số thi thật.'
C['sources']['girm6']={'title':'GIRM Chapter VI, 288–347','url':'https://www.usccb.org/prayer-and-worship/the-mass/general-instruction-of-the-roman-missal/girm-chapter-6'}
C['sources']['girm3']={'title':'GIRM Chapter III, Duties and Ministries','url':'https://www.usccb.org/prayer-and-worship/the-mass/general-instruction-of-the-roman-missal/girm-chapter-3'}
C['sources']['examen']={'title':'USA East Jesuits — The Daily Examen','url':'https://www.jesuitseast.org/spirituality/the-daily-examen/'}
C['sources']['magis']={'title':'Jesuit Formation — Magis and Cura personalis','url':'https://formation.jesuits.global/lessons/cis2025-patrick-goujon-sj-magis-and-cura-personalis/'}
C['sources']['gs']={'title':'Gaudium et Spes 1, 27','url':'https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19651207_gaudium-et-spes_en.html'}
(D/'course.json').write_text(json.dumps(C,ensure_ascii=False,indent=2))
print('Template transcription and 25 extended lessons ready')
