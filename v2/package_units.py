from pathlib import Path
import json,zipfile
P=Path(__file__).resolve().parents[1];D=P/'dist';C=json.loads((D/'course.json').read_text())
for l in C['lessons']:
 folder=D/'units'/f'Unit{l["number"]}'
 with zipfile.ZipFile(folder/f'Unit{l["number"]}_Bo_3_file.zip','w',zipfile.ZIP_DEFLATED) as z:
  for path in l['downloads']:z.write(D/path,Path(path).name)
with zipfile.ZipFile(D/'Units_02_26_Theo_Mau_Unit1.zip','w',zipfile.ZIP_DEFLATED) as z:
 for l in C['lessons'][1:]:
  for path in l['downloads']:z.write(D/path,Path(path).relative_to('units'))
  z.write(D/l['audio'],l['audio'])
 z.writestr('README.txt','Unit 2–26 theo cấu trúc Unit 1 do người học cung cấp. Mỗi unit: Curriculum.pdf, Questions.pdf, Practice.docx. Listening bổ sung dùng audio/02.mp3 tới audio/26.mp3. B1 là giả định đầu vào, B2 chỉ phần luyện mở rộng. Đây là học liệu tự học, không phải cấu trúc thi chính thức. Bản Word có thể in trực tiếp trên A4; đáp án và transcript chỉ trong phụ lục giáo trình.\n')
# Old per-lesson PDFs are no longer linked; keep only diagnostic/review/mock PDFs.
for f in (D/'pdf').glob('Bai_*.pdf'):
 id=f.name.split('_')[1]
 if id.isdigit() and 1<=int(id)<=26:f.unlink()
print('26 individual bundles; 75 new documents in the Unit 2–26 bundle')
