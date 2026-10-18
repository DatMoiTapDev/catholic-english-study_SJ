# Catholic English theo mẫu Unit 1

Phiên bản này sử dụng ba file Unit 1 do người học cung cấp làm mẫu về cấu trúc học liệu. Unit 1 được giữ nguyên byte. Unit 2–26 được biên soạn lại theo syllabus Catholic Vocabulary and Ecclesial Language, không phải tài liệu chính thức đã được giảng viên duyệt.

## Ba tài liệu cho mỗi unit

- `UnitN_Curriculum.pdf`: 8 phần theo mẫu, song ngữ Anh–Việt; 20 mục từ với IPA, từ loại, nghĩa, định nghĩa, ví dụ, collocation và mức ưu tiên; phân biệt khái niệm; mẫu câu; bài đọc; nói/viết; kiến thức mở rộng; gợi nhớ. Đáp án, rubric và transcript ở phụ lục cuối.
- `UnitN_Questions.pdf`: đề đầy đủ, có bài đọc và liên kết âm thanh; không có đáp án.
- `UnitN_Practice.docx`: đúng mã câu, câu hỏi, lựa chọn và bài đọc của đề PDF, có dòng viết và dàn ý nói, A4. A/B chung hàng đầu, C/D chung hàng sau.

Unit 2–26 có tổng 75 tài liệu mới. Unit 1 theo bản gốc có 16 nhiệm vụ /100, chưa có Listening. Các unit mới bổ sung Listening thành 19 nhiệm vụ /100, gồm Reading 10, Terminology 20, Grammar 10, Speaking 20, Writing 22, Critical Reading 8, Listening 10. Đây là phân bổ tự học, không phải trọng số thi của giảng viên.

## Cách học

Lộ trình B1+ hướng tới B2 theo mức học người dùng xác nhận. Giải thích tiếng Việt dễ hiểu, luyện bốn kỹ năng và mở rộng dần độ khó.

Nghe hai lượt trước khi mở transcript. Audio là MP3 thật, tổng hợp bằng Flite SLT, giọng Anh Mỹ. Với bài viết và nói, tự làm trước, sau đó đối chiếu ý cần có và rubric. Máy chỉ chấm trắc nghiệm (Unit 1 /10, Unit 2–26 /16). Các điểm còn lại do người học hoặc giáo viên nhập. Nội dung Công giáo và ngôn ngữ được tách thành các tiêu chí riêng. Phát âm không thể đánh giá từ kịch bản viết.

Bài chẩn đoán, 4 bài ôn và đề thi thử của phiên bản trước vẫn có định dạng riêng /34, được ghi rõ trong từng bài; chúng không nằm trong 75 file Unit 2–26. Chưa có cấu trúc hoặc trọng số thi chính thức.

## Sử dụng website và chạy local

Mỗi unit có đúng ba mục chính: Giáo trình / Đề bài / Luyện tập. Mỗi mục cho học trực tuyến và tải tài liệu tương ứng. Mục Luyện tập tải Word như mẫu mới; không tạo thêm tài liệu thứ tư cho mỗi unit.

Trên Windows, giải nén rồi mở `START_WINDOWS.bat`, hoặc chạy ở thư mục giải nén:

```
py -3 tools/package_downloads.py
py -3 -m http.server 8000 --directory dist --bind 127.0.0.1
```

Sau đó mở http://localhost:8000 . Có thể dùng `python` thay `py -3`; macOS/Linux dùng `python3`. Không mở trực tiếp index.html bằng file:// vì trình duyệt có thể chặn course.json. Không cần cài dependency frontend; các tài liệu và MP3 đã có sẵn.

## Dữ liệu cá nhân

Bài làm, điểm và ghi chú nằm trong localStorage; âm thanh ghi từ micro nằm trong IndexedDB trên thiết bị. Không có tài khoản hoặc đồng bộ, không gửi bài làm hay bản ghi lên máy chủ. Website là công khai; các tệp tài liệu được soạn sẵn cũng công khai.

Phiên bản mới dùng khóa lưu riêng và có thể tiếp nhận lịch sử phiên bản trước; các lượt cũ được ghi nhãn. Dùng Xuất sao lưu để tải JSON gồm bài làm và âm thanh. Nhập bản sao lưu thay dữ liệu hiện tại sau xác nhận. Giữ bản sao lưu riêng tư. Dùng chung hồ sơ trình duyệt thì có thể thấy bài làm của nhau.

Micro cần MediaRecorder, quyền micro và HTTPS hoặc localhost. Nếu không hoạt động, dùng ứng dụng ghi âm của thiết bị hoặc nói trực tiếp. Không có chấm phát âm, nói hoặc viết bằng AI. Bản ghi mới thay bản ghi cũ của cùng unit; tải bản ghi riêng nếu muốn lưu nhiều bản.

## Nội dung và quyền sử dụng

Chỉ có syllabus và ba file mẫu Unit 1, không có slide hay bài đọc được giảng viên chỉ định. Bài đọc Unit 2–26 là ngữ liệu tự biên soạn, có giải nghĩa tiếng Việt và nguồn để kiểm tra. Không coi phần tiếng Việt là bản dịch chính thức của văn kiện, Kinh Thánh hoặc phụng vụ. Không tự đặt kinh nguyện rồi gán địa vị chính thức.

Giữ ngày học gốc và thứ tự 26 buổi; Jesuit Vocabulary and Language gồm buổi 1 và 2 theo xác nhận của người học. Những chỗ chưa nhất quán của lịch syllabus được ghi chú trên website.

Tuân thủ chính sách AI-limited: không dùng AI thay bài suy tư cá nhân, kiểm tra từ vựng trên lớp hoặc nhiệm vụ được giảng viên đánh dấu hạn chế AI. Các tình huống giả định trong học liệu dùng để luyện ngôn ngữ, không ép tiết lộ trải nghiệm riêng.

## Mã nguồn và tạo lại tài liệu

- `dist/index.html`, `style.css`, `app.js`: giao diện tĩnh và tương tác.
- `dist/course.json`: dữ liệu học liệu dùng chung cho website, đề và phiếu.
- `dist/units/UnitN/`: ba file của từng unit và ZIP riêng.
- `dist/audio/`: âm thanh bài nghe; `dist/pdf/`: tài liệu chẩn đoán/ôn/thi thử riêng.
- `v2/topics.py`, `scenarios_vi.py`: nội dung biên soạn theo chủ đề và giải nghĩa tình huống.
- `v2/base-course.json`: dữ liệu tình huống và audio của phiên bản trước để phát triển bản mới.
- `v2/build_data.py`: kết hợp dữ liệu và đọc Unit 1 mẫu, tạo course.json. Dùng file Unit 1 ở thư mục upload khi có, hoặc bản đã đóng gói trong dist/units/Unit1.
- `v2/generate_documents.py`: sinh 50 PDF và 25 Word. Cần Python, reportlab, python-docx và font DejaVu ở đường dẫn ghi trong script.
- `v2/render_workbooks.py`: render Word bằng công cụ tài liệu của môi trường Codex, dành cho kiểm tra nội bộ.
- `v2/verify_documents.py`: kiểm tra câu hỏi, bài đọc, lựa chọn, biên trang và font; tạo ảnh rà soát.
- `v2/app-v1.js`, `frontend_additions.js`, `patch_frontend.py`: mã nền và phần mở rộng để dựng app.js mới.
- `v2/check_app.cjs`: kiểm tra dựng 96 mục, tính điểm, các liên kết tài liệu và sao lưu bằng Node.
- `v2/package_units.py`: đóng gói từng bộ và Unit 2–26.

## Kiểm tra đã thực hiện

Đã render cả 25 Word, đối chiếu đề–phiếu và kiểm tra vị trí chữ; kiểm tra trắc nghiệm hai cột và không tách câu/lựa chọn. Đã rà ảnh các tài liệu. Ba file Unit 1 được kiểm tra hash để bảo đảm giữ nguyên.

Đã kiểm tra logic tính điểm cho toàn bộ unit /100 và các bài riêng /34, liên kết tài liệu, escape dữ liệu và kiểm tra dữ liệu sao lưu. Không có công cụ control-browser cho Sites trong môi trường, nên chưa kiểm thử trực tiếp giao diện trình duyệt, quyền micro hoặc bố cục trên từng điện thoại.

## GitHub

Website đang hoạt động: https://catholic-english-study.calmgnome10.chatgpt.site

Repo chứa mã nguồn và assets.zip gồm PDF, Word, MP3 và font Montserrat tự lưu (giấy phép OFL trong dist/fonts). Chạy `python tools/package_downloads.py` để giải nén tài nguyên vào đúng thư mục. ZIP tải xuống là file sinh tự động: chạy `python tools/package_downloads.py` trước khi mở website. START_WINDOWS.bat đã tích hợp bước này. Không có tài khoản, khóa truy cập hoặc lịch sử học cá nhân trong repo.
