# Kế hoạch pipeline Literature Review — Biomedical RDM

**Phiên bản:** 1.1.0  
**Ngày:** 21/11/2026  
**Phạm vi:** trạng thái hiện tại của nhánh `chore/refs-workflow-20261121`, xuất phát từ `main`.

## 1. Mục tiêu và ranh giới

Mục tiêu của đợt này là làm cho quy trình kiểm tra thư mục tham khảo, QA pháp lý và render có thể lặp lại, có bằng chứng và không làm thay đổi nội dung khoa học canonical trong `docs/literature-review/index.md`.

Các nguyên tắc bất biến:

- Không bịa nguồn, DOI, số hiệu, ngày tháng hoặc nhận định pháp lý.
- Không xóa cờ `[CẦN KIỂM CHỨNG]` và không tự sửa thân bài hay `.bib` trong các bước kiểm tra.
- Dùng trạng thái `VERIFIED`, `BIB_PENDING`, `CONTENT_PENDING`, `BLOCKED_INPUT` cho hồ sơ tham khảo khi cần; đây là trạng thái kiểm chứng của tài liệu, không phải trạng thái của VERA.
- Tham khảo VERA/DrMayDay về provenance và gate, không áp dụng nguyên vẹn tên gate hay quy trình của các dự án đó.

## 2. Đầu vào đã biết

- `docs/literature-review/index.md` có 103 số trích dẫn canonical và danh mục BibTeX `references/references.bib`.
- `references/citation-audit.csv` có các dòng `ref_001` đến `ref_103`; một số dòng còn `BIB_PENDING` hoặc `VERIFIED_UNAUDITED`.
- `scripts/verify_refs.py` là bộ tra cứu OpenAlex/Semantic Scholar; không dùng nó như bộ kiểm tra nhất quán giữa thân bài, CSV và BibTeX.
- `docs/PROJECT-STATE.md` được đề xuất ở một pull request riêng (chưa merge tại thời điểm viết); mọi việc mở trong kế hoạch này được xác nhận từ các file đang có trên `main`.

## 3. Các bước thực hiện

### B1 — Chốt phạm vi và provenance

Đọc `docs/DECISIONS.md`, các file review và inventory hiện hành; lập danh sách đầu vào, file sẽ đổi và file tuyệt đối không đổi. Nếu cần tái dùng harvester của DrMayDay, chỉ copy phần cần thiết theo hợp đồng provenance của `evisyn/PROVENANCE.md`, ghi commit nguồn và lý do copy. Không tạo `harvest_metadata.py` mới.

### B2 — Audit ánh xạ trích dẫn

Chạy `python scripts/audit_references.py`. Script kiểm tra số `[n]` và `[n, m]` trong phần thân/Phụ lục A sau khi loại danh mục tham khảo và Phụ lục B; đối chiếu với 1..103, `references.bib` và `citation-audit.csv`; phát hiện mục chưa được trích, trùng DOI/URL/tiêu đề, mojibake/ký tự lạ và số ngoài khoảng. Báo cáo ghi tại `references/AUDIT-REPORT.md`; chỉ lỗi ánh xạ thiếu, thiếu mục nguồn và số ngoài khoảng mới làm script thoát mã 1.

### B3 — QA pháp lý có nguồn chính thống

Tạo `docs/legal-verification.md` cho các mục [54], [55], [57]–[58], [60], [62]–[66], [79]–[82]. Mỗi dòng ghi số hiệu, ngày ban hành, ngày hiệu lực, URL nguồn chính thống, ngày tra cứu, trạng thái và chi tiết đã đối chiếu. Chỉ ghi nội dung xác nhận được; các điểm khác với review chỉ liệt kê, không sửa `index.md`.

Khung pháp lý Việt Nam dùng Nghị định 356/2025/NĐ-CP cho giai đoạn từ 01/01/2026; không dùng Nghị định 13/2023/NĐ-CP như văn bản hiện hành.

### B4 — Quyết định dạng trích dẫn

Giữ dạng số `[n]` trong đợt này để bảo toàn thân bài canonical. Ghi lý do, rủi ro và chi phí trong `docs/DECISIONS.md`; audit nội bộ ở B2 thay thế kiểm tra reverse citekey. Không tạo hoặc chạy chuyển đổi citation trong đợt này.

### B5 — Gate phát hành và bàn giao

Chạy audit, `python scripts/verify_refs.py` theo đúng vai trò tra cứu metadata, và `quarto render`. Kiểm tra diff, cờ kiểm chứng, secret/PII và trạng thái file. Bàn giao báo cáo gồm lỗi thật, khác biệt pháp lý, quyết định B4 và việc còn mở. Không commit, push, merge hoặc tự phê duyệt.

## 4. Tiêu chí nghiệm thu

- `scripts/audit_references.py` dùng thư viện chuẩn, chạy từ thư mục repo với đường dẫn tương đối, tạo báo cáo tiếng Việt có ngày và trả mã 1 khi có lỗi ánh xạ bắt buộc.
- Audit báo cáo riêng các phát hiện không làm thay đổi file nguồn; không tự sửa `index.md` hoặc `references.bib`.
- `docs/legal-verification.md` có đủ 14 mục yêu cầu, URL chính thống hoặc ghi rõ không tìm được, ngày tra cứu và giới hạn tra cứu.
- `docs/DECISIONS.md` ghi quyết định giữ `[n]` và hệ quả kỹ thuật.
- Render Quarto hoàn tất với kết quả thật được ghi lại; `verify_refs.py` chỉ được mô tả là tra OpenAlex/Semantic Scholar.
- Không có file mới nào ghi tên công cụ AI, khóa API, secret hoặc PII.

## 5. Việc mở thật sự

- Người duyệt xem các lỗi audit và quyết định sửa thân bài/BibTeX nếu cần.
- Người có thẩm quyền xác nhận các chi tiết pháp lý chưa đọc được từ nguồn chính thống hoặc cung cấp bản văn gốc.
- Cập nhật `docs/PROJECT-STATE.md` sau khi pull request tương ứng được merge, theo kết quả của kế hoạch này.
