# Nhật ký thay đổi

## Thay đổi trong đợt 2026-11-20

- Đưa toàn bộ nguồn khóa học đã sửa vào `docs/course-source/rdm-mini-course-source.md`; repo `biomedical-rdm` là nguồn gốc, còn repo khóa học là bản render/web.
- Các thay đổi của khóa học so với `rdm-mini-course-ly-thuyet-quiz.md`: đảo thứ tự đáp án; sửa câu 2.1; sửa Bài 3; thống nhất FAIRification theo §7.2; thêm cảnh báo preprint/pending; hiệu chỉnh thời lượng; và mô tả lớp bảo mật, đạo đức, pháp lý xuyên suốt.
- Phụ lục A còn 29 hàng đủ điều kiện; đã loại Dayan [89] vì còn `BIB_PENDING` và thêm chú thích ngay dưới bảng.

- Thêm YAML front matter gồm tiêu đề, phụ đề, tác giả, ngày và phiên bản; bỏ H1 tiếng Anh trùng lặp để phụ đề nhận diện trong bản render.
- Thay đường dẫn `workspace/...` bằng mô tả nguồn chung, không làm mất các ghi chú biên tập còn lại trong thân bài.
- Chuẩn hóa quy ước trích dẫn và lời dẫn Phụ lục A theo danh mục cuối bài 103 mục.
- Sửa các ánh xạ chắc chắn `[19,185]` thành `[38], [40]` và `[135]` thành `[30]`; giữ phần ánh xạ số 134 bằng cờ `[CẦN KIỂM CHỨNG: số 134 của danh mục 334 mục — BLOCKED_INPUT]`.
- Sửa câu bị cụt ở §6.1 ở mức tối thiểu; loại `[89]` khỏi bảng Phụ lục A.

## Vòng 3 — danh mục nguồn và BibTeX

- Đã nhận `references/source-334-list.md`: 334 mục chỉ gồm tiêu đề (có thể bị cắt ngắn) và URL, không phải APA. “APA 334” vẫn `PARTIAL`; bản APA đầy đủ là `BLOCKED_INPUT` vì chưa có `references-334-apa.md`.
- Đã tạo `references/references-334.bib` và `references/references.bib`; các trường BibTeX chưa hoàn thiện là do nguồn cung cấp thiếu, không phải metadata được suy đoán.
- Đã xác nhận mục 134 là Weiskopf & Weng, PubMed 22733976; thay cờ `BLOCKED_INPUT` bằng trích dẫn [28] tại các vị trí tương ứng.

## Ghi chú quy trình vẫn còn trong thân bài

Các ghi chú về ngày chốt, giới hạn phương pháp, các mục `[CẦN KIỂM CHỨNG]`, tài liệu bổ sung, mục bị loại khỏi thân bài, các tuyên bố cần đối chiếu và các giới hạn nguồn được giữ nguyên theo yêu cầu. Chúng không được xem là xác nhận kiểm chứng độc lập.

Các đường dẫn nguồn nội bộ đã được thay ở dòng nguồn đầu bài; các nội dung biên tập khác vẫn chờ Ben quyết định nếu cần viết lại ở đợt sau.

## Đối chiếu thư mục (2026-11-21)

- Thêm `scripts/verify_refs.py`, `references/verification-doi-openalex.csv`, `references/verification-report.csv` và `references/VERIFICATION.md`. Không sửa nội dung thân bài; các sai lệch được ghi để người audit xử lý.

## Đối chiếu số liệu ref_103 (2026-11-26)

- Phụ lục A, dòng Lane và cộng sự [103]: sửa mô tả cho khớp tóm tắt bài gốc (PMID 32864627, Europe PMC). Số liệu giữ nguyên và đã khớp: 14 nguồn dữ liệu, 6 quốc gia (Đức, Nhật, Hà Lan, Tây Ban Nha, Anh, Mỹ), 956.374 người dùng HCQ. Bỏ chữ "An toàn" đứng một mình vì bài báo cáo tăng nguy cơ tim mạch khi dùng dài hạn và khi thêm azithromycin. Phạm vi đã đọc: tóm tắt; chưa đọc toàn văn.
