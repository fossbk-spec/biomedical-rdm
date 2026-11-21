# Decision log

## 2026-11-21 — Tách nội dung cố định/cập nhật cho chương 1

- **Quyết định:** Giữ khái niệm, nguyên lý và phương pháp ổn định trong thân chương 1; chuyển pháp lý, mẫu tài trợ, thời hạn lưu trữ, phiên bản chuẩn, công cụ và URL vào `docs/appendices/`.
- **Người quyết định:** Ben.
- **Phạm vi:** Chương 2–6 không sửa trong đợt này. Khóa học đăng ở `biomedical-rdm-course`; tài liệu nguồn lưu ở repo gốc `biomedical-rdm`.
- **Rà soát:** Các phụ lục chốt ngày 21/11/2026 và rà soát tiếp theo ngày 21/05/2027; cờ `CONTENT_PENDING` và `[CẦN KIỂM CHỨNG]` được giữ nguyên khi chưa có bằng chứng đủ.

## 2026-11-21 — Phụ lục mẫu nhà tài trợ

- **Quyết định:** Đưa nội dung DMPTool vào `docs/appendices/funder-templates.md`; coi DMPTool là nguồn thứ cấp/hỗ trợ soạn thảo và giữ `CONTENT_PENDING` cho tên mẫu quan sát từ staging, điều kiện chuyển tiếp của mẫu cũ và mọi chi tiết chưa đối chiếu được.
- **Căn cứ:** Các yếu tố, giới hạn từ và mốc chuyển tiếp đã được đối chiếu với nguồn NIH chính thức; ngày kiểm 21/11/2026.
- **Người quyết định:** Ben.

## 2026-11-21 — Giữ dạng trích dẫn số trong canonical review

- **Quyết định:** Giữ `[n]` trong `docs/literature-review/index.md` cho đợt này; không đổi thân bài canonical và không tạo script chuyển đổi.
- **Lý do:** Thân bài hiện dùng số viết tay, Quarto không được cấu hình để nối `references.bib` với citekey, và yêu cầu hiện tại là audit tính toàn vẹn của hệ số 1..103. Giữ dạng hiện tại là thay đổi nhỏ nhất và không làm thay đổi nội dung khoa học.
- **Rủi ro:** Dạng `[n]` không nối tự động với `references.bib`, không dùng được reverse verifier/citekey workflow và có thể lệch khi chèn hoặc xóa tài liệu.
- **Chi phí/biện pháp giảm rủi ro:** Duy trì `scripts/audit_references.py` để đối chiếu thân bài, `references.bib` và `citation-audit.csv`; mọi lần đổi danh mục phải chạy audit và review diff. Việc chuyển sang `[@ref_NNN]` cần một đợt riêng, có dry-run, render và người duyệt.

## 2026-11-20 — Quyết định và trạng thái kiểm chứng

- Đưa nguồn khóa học vào repo gốc tại `docs/course-source/rdm-mini-course-source.md`. Đây là file nguồn chân lý; repo khóa học chỉ là bản render/web và được đồng bộ bằng `scripts/sync_from_source.py`.
- Ghi phiên bản nguồn của repo khóa học theo commit hash: `69c45b1a050205779056ad3e81b319d5def25695`.
- Ghi nhận các thay đổi khóa học so với `rdm-mini-course-ly-thuyet-quiz.md`: đảo thứ tự đáp án, sửa câu 2.1, sửa Bài 3, FAIRification theo §7.2, cảnh báo preprint/pending, thời lượng và lớp kiểm soát xuyên suốt.
- Phụ lục A hiện còn 29 hàng đủ điều kiện; loại Dayan [89] vì còn `BIB_PENDING`; tiêu đề và chú thích đã được sửa để không gây hiểu nhầm là 30 mục.

- Ben chốt giữ tách hai repo: `biomedical-rdm` cho nội dung nghiên cứu và `biomedical-rdm-course` cho khóa học.
- Có 12 mục pending theo cờ và ghi chú trong văn bản; chưa coi các mục này là đã kiểm chứng độc lập.
- `VERIFIED`: chỉ dùng khi mục tham khảo, ánh xạ trích dẫn và nội dung tuyên bố đã được đối chiếu với nguồn được cung cấp.
- `BIB_PENDING`: nội dung chính đã có căn cứ nhưng còn thiếu trường thư mục.
- `CONTENT_PENDING`: khẳng định hoặc căn cứ nội dung chưa được xác minh.
- `BLOCKED_INPUT`: thiếu input nguồn cần thiết, không được suy đoán hoặc tái tạo.
- Hoãn tạo `references.bib` cho đến sau audit trích dẫn; hiện chỉ tạo `references/citation-audit.csv`.
- Chuyển Ben xử lý: R-06 (NIH NOT-OD-26-046), R-04 (FHIR R6/ICH Annex 2), R-08 (pháp lý Việt Nam) và danh mục APA 334 mục.
- Vòng 3: `references/source-334-list.md` đã được cung cấp dưới dạng 334 tiêu đề + URL, không phải APA. Vì vậy “APA 334” vẫn `PARTIAL`; `references-334-apa.md` chưa có và vẫn là `BLOCKED_INPUT` cho bản APA đầy đủ.
- Đã tạo `references/references-334.bib` (334 mục) và `references/references.bib` (103 mục). Các trường còn thiếu trong BibTeX phản ánh nguồn đầu vào thiếu, không được suy đoán.
- Số 134 của danh mục 334 đã được xác nhận là Weiskopf & Weng, PubMed 22733976, và các cờ tương ứng trong bài đã đổi thành [28].


## 2026-11-20 — Repository separation

- **Decision:** Use `biomedical-rdm` for canonical research content and `biomedical-rdm-course` for learning materials.
- **Reason:** Research source governance and course publication have different release cycles.

## 2026-11-20 — Canonical review

- **Decision:** Publish `tong-hop-literature-review-rdm-y-sinh.md` as the canonical review.
- **Reason:** It identifies itself as a verified narrative synthesis and records its methodological limits.

## 2026-11-20 — Missing 334-entry list

- **Status:** BLOCKED_INPUT.
- **Decision:** Do not recreate the list from memory. Add it after the source file is supplied and audited.

## 2026-11-21 — Đối chiếu thư mục với OpenAlex và Semantic Scholar

- Ben yêu cầu dùng API OpenAlex và Semantic Scholar để xác nhận. Kết quả và giới hạn: `references/VERIFICATION.md`.
- Chỉ kết quả tra theo DOI (56 mục) được coi là xác nhận thư mục; 40 khớp hoàn toàn, 7 lệch năm online/issue, 6 không khớp cần xử lý (nổi bật: `ref_045`, `ref_103`).
- Chưa tự sửa `references.bib` hay thân bài. Trạng thái trong `citation-audit.csv` giữ nguyên; cột `action` đã ghi các mục cần đối chiếu.

## 2026-11-21 — Audit trang nguồn cho 47 mục không DOI

- Kết quả đối chiếu trang web (script `scripts/audit_nodoi_gemini.py`, Gemini chỉ so nội dung trang đã tải): `references/audit-nodoi-gemini.csv`. Đây là kiểm tra danh tính trang nguồn, không xác nhận nội dung khẳng định.
- `citation-audit.csv` thêm cột `page_check`, `page_check_note`. Chỉ chuyển `VERIFIED_UNAUDITED` → `BIB_PENDING` với 6 mục PARTIAL. Mục MATCH giữ `VERIFIED_UNAUDITED` (chưa đủ điều kiện `VERIFIED`); mục NOT_CHECKED/MISMATCH (trang chặn truy cập hoặc không có URL) cần audit thủ công.
## 2026-11-21 — Tách nội dung cố định/cập nhật cho chương 2

**Ngày:** 21/11/2026 · **Người quyết định:** Ben

- (a) Không dùng con số SDV; chỉ giữ kết luận định tính theo tóm tắt Sheetz 2014.
- (b) Hai case study là tình huống giả định minh họa; bỏ số liệu và hậu quả không có nguồn.
- (c) Giữ lab trong cùng file.

Ba quyết định trên là tạm thời, chờ Ben xác nhận.

## 2026-11-21 — Tách nội dung cố định/cập nhật cho chương 3

- **Quyết định:** Giữ trong thân chương các khái niệm ổn định về lớp miền SDTM, kiến trúc FHIR, mô hình person-centric của OMOP, logic ánh xạ `source_value`/`concept_id` và vai trò bổ trợ của ba chuẩn.
- **Chuyển phụ lục:** Phiên bản FHIR/OMOP/CDISC, yêu cầu tiếp nhận FDA/PMDA, URL, ngày kiểm, trạng thái Athena và chi tiết ETL được đưa vào `docs/appendices/standards.md` và `docs/appendices/fhir-omop-lab-notes.md`.
- **Quyết định tạm thời:** Bundle §5.2 là tình huống minh họa tự dựng; Synthea chỉ là gợi ý nguồn dữ liệu tổng hợp; concept chưa đọc trực tiếp từ Athena giữ `CONTENT_PENDING`.
- **Giới hạn:** R6, yêu cầu PMDA, và các concept `402407000`, `4180186`, `8753/8876` chưa được xác minh đầy đủ trong lượt này; không dùng chúng làm bằng chứng đã kiểm.

## 2026-11-21 — Tách nội dung cố định/cập nhật cho chương 5

- **Quyết định tạm thời:** Giữ trong thân chương các khái niệm ổn định về thuộc tính định danh, k-anonymity, l-diversity, dịch chuyển ngày và cảnh báo rằng Lab 5 không đạt Safe Harbor.
- **Chuyển phụ lục:** URL, ngày kiểm, trạng thái pháp lý, mốc EHDS, lưu trữ/hủy dữ liệu và kết quả chạy Lab 5 nằm ở `docs/appendices/legal.md`, `retention.md` và `privacy-lab-notes.md`.
- **Case study:** dùng nhãn tình huống giả định minh họa; không giữ số liệu, chế tài hoặc khẳng định chưa đọc được nguồn.
- **Giới hạn:** nguồn Five Safes, NIST SP 800-88 Rev. 2 và chi tiết Thông tư 33/2025/TT-BYT vẫn `CONTENT_PENDING`/`BIB_PENDING` cho đến khi đọc được nguồn tương ứng.
