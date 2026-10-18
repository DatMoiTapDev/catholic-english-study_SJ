# Catholic English SJ

Website tự học tiếng Anh Công giáo theo syllabus, dành cho trình độ B1+ hướng tới B2: 26 bài, luyện bốn kỹ năng và tải học liệu để in.

## Xuất bản

Trong **Settings → Pages → Build and deployment**, chọn **Source: GitHub Actions** một lần. Workflow **Deploy GitHub Pages** sẽ tự chạy khi cập nhật nhánh `main`; cũng có thể chạy bằng **Actions → Deploy GitHub Pages → Run workflow**.

Địa chỉ sau khi triển khai thành công: https://DatMoiTapDev.github.io/catholic-english-study_SJ/

## Chạy trên máy

Cài Python 3, tải repo rồi mở `START_WINDOWS.bat`. Hoặc chạy:

```sh
python tools/package_downloads.py
python -m http.server 8000 --directory dist --bind 127.0.0.1
```

Mở http://localhost:8000. Script tự giải nén `assets.zip` và tạo các gói tải xuống.

## Cấu trúc

- `dist/`: giao diện và dữ liệu bài học.
- `assets.zip`: PDF, Word, MP3 và font Montserrat (OFL).
- `tools/`: chuẩn bị tài nguyên và gói tải xuống.
- `v2/`: mã biên soạn và kiểm tra học liệu.

Bài làm và bản ghi âm lưu trên trình duyệt; dùng xuất/nhập sao lưu để chuyển thiết bị. Học liệu bổ trợ tự biên soạn; bài nghe dùng giọng tổng hợp.
