# Trạng thái dự án Biomedical RDM

**Phiên bản:** 1.1.0 · **Ngày:** 21/11/2026 (cập nhật sau PR #2–#4) · **Người nghiệm thu:** TS. Hoàng Quang Huy (Ben)
**Mục đích:** lưu trạng thái dự án để tiếp tục công việc mà không phải dựng lại ngữ cảnh.

## 1. Tóm tắt

Dự án có **hai repo công khai** của tài khoản `fossbk-spec`:

| Repo | Vai trò | Trạng thái (21/11/2026) |
|---|---|---|
| `biomedical-rdm` | **Repo gốc**, nguồn chân lý: literature review, danh mục tham khảo, nguồn khóa học | PR #1, #2, #3, #4 đã **merge** vào `main`; PR sửa script audit (nhánh `fix/audit-script-and-state`) đang cập nhật tài liệu này |
| `biomedical-rdm-course` | **Bản web** khóa học (VitePress, có Quarto song song), nội dung lấy từ repo gốc | PR #1–#4 đã **merge**; GitHub Pages đã bật: https://fossbk-spec.github.io/biomedical-rdm-course/ |

Ben đã chốt **giữ tách hai repo** (20/11/2026).

Đã làm: review độc lập hai PR đầu và thực hiện sửa; dựng `references.bib` (103 và 334 mục); đối chiếu thư mục bằng OpenAlex và Semantic Scholar; audit trang nguồn cho 47 mục không DOI; script `audit_references.py` (kiểm trích dẫn `[n]` ↔ 1..103 ↔ `.bib` ↔ CSV); QA pháp lý bằng nguồn chính thống (`docs/legal-verification.md`); `AGENTS.md` ở cả hai repo; plan pipeline v1.1.0; site khóa học với quiz tương tác. Còn một số mục chờ Ben (mục 6).

## 2. Nội dung repo gốc `biomedical-rdm`

- `docs/literature-review/index.md`: bản tổng hợp literature review (tổng hợp tường thuật có kiểm chứng, **không** phải systematic review theo PRISMA). Đã thêm front matter, sửa trích dẫn số cũ (`[19,185]`→`[38],[40]`; `[8,134,135]`→`[10],[28],[30]`), Phụ lục A còn 29 mục.
- `docs/literature-review/CHANGES.md`: mọi thay đổi so với file nguồn.
- `docs/course-source/rdm-mini-course-source.md` + `README.md`: **nguồn chân lý của khóa học**, 17 trang tách bằng marker `<!-- page: <path> -->`.
- `references/references.bib` (103 mục), `references/references-334.bib` (334 mục, chỉ tiêu đề + URL), `references/source-334-list.md` (danh mục thô), `references/citation-audit.csv` (103 dòng), `references/VERIFICATION.md`, `verification-doi-openalex.csv`, `verification-report.csv`.
- `scripts/build_bib.py` (`--check`), `scripts/verify_refs.py` (tra OpenAlex/Semantic Scholar), `scripts/audit_references.py` (kiểm nhất quán nội bộ, ghi `references/AUDIT-REPORT.md`), `scripts/audit_nodoi_pages.py` (kiểm trang nguồn cho mục không DOI, ghi `references/audit-nodoi-pages.csv`).
- `docs/DECISIONS.md`, `docs/INPUT-INVENTORY.md`, `docs/DATA-USE.md`, `docs/legal-verification.md`, `docs/plans/` (plan 10 ngày và plan pipeline v1.1.0), `docs/reviews/` (review hướng dẫn agent), `AGENTS.md`.
- `LICENSE` (CC BY 4.0 cho nội dung), `LICENSE-CODE` (MIT), `CONTRIBUTING.md`, `.gitignore`, `_quarto.yml`, `index.qmd`, `README.md`.

## 3. Nội dung repo khóa học `biomedical-rdm-course`

- Site VitePress với quiz tương tác (quy tắc đạt khớp ≥ 24/34 và ≥ 2/3 Q1–Q3), footer bản quyền; `AGENTS.md`, `docs/SITE-CHECKS.md` (VitePress build đạt).
- 7 module: M0 nhập môn (không quiz), M1–M6 (mỗi bài có trang bài giảng và trang quiz 4 câu), quiz cuối khóa 10 câu, glossary (33 thuật ngữ), syllabus, ROADMAP.
- **34 câu quiz**, phân bố đáp án A8/B8/C9/D9. Điều kiện đạt: ≥ 24/34 **và** đúng ít nhất 2/3 câu Q1–Q3. Giới hạn làm tối đa 2 lần chỉ là hướng dẫn tự học (site tĩnh không cưỡng chế).
- `scripts/sync_from_source.py [--check]`: đồng bộ từ `biomedical-rdm/docs/course-source/`. Lần kiểm cuối: 17 trang khớp.
- `LICENSE` CC BY 4.0, `CONTRIBUTING.md`, `docs/DECISIONS.md` (trỏ về repo gốc), `.gitignore`, `_quarto.yml` (`number-sections: false`).

## 4. Các quyết định đã chốt

| Quyết định | Căn cứ |
|---|---|
| Giữ tách hai repo | Ben, 20/11/2026 |
| Review tổng hợp là bản chính để xuất bản; hai `Literature_Review*.md` chỉ là nền | Plan §2 |
| M0 không có quiz; M1–M6 mỗi bài 4 câu; quiz cuối 10 câu; tổng 34 | Plan §2 |
| Điều kiện đạt: ≥ 24/34 và ≥ 2/3 câu Q1–Q3 | Plan §2 |
| Cho phép đảo thứ tự phương án A–D (không đổi nội dung) để chống đoán | Quyết định biên tập, 20/11/2026 |
| Sửa đề câu 2.1 (hỏi "Complete" trong phần `+` của ALCOA+) | Quyết định biên tập, 20/11/2026 |
| Bài 3: bỏ luồng FHIR→OMOP→SDTM, "9 cơ sở dữ liệu" của LEGEND-HTN, câu FHIR Bulk Data "nền tảng cho AI" | Quyết định biên tập, 20/11/2026 |
| Thêm "lớp kiểm soát xuyên suốt" + bảng đối chiếu 7 bước ↔ 6 giai đoạn (M0) | Quyết định biên tập, 20/11/2026 |
| FAIRification 7 bước theo review §7.2; Q9 viết lại | Quyết định biên tập, 20/11/2026 |
| Có 12 mục pending (không phải 9) | Quyết định biên tập, 20/11/2026 |
| Định nghĩa trạng thái: `VERIFIED`, `BIB_PENDING`, `CONTENT_PENDING`, `BLOCKED_INPUT` | `DECISIONS.md` |
| Thời lượng bài sửa thành ~2–3 phút đọc/bài | Quyết định biên tập, 20/11/2026 |
| `references.bib` 334 mục chỉ có tiêu đề/URL vì nguồn thiếu trường; không bịa thêm | `DECISIONS.md` |

## 5. Kết quả kiểm tra

- **Render:** `quarto render` (repo gốc) và `npm run build` (VitePress, repo khóa học) chạy được. Chưa kiểm tra lại sau mọi merge; chưa có CI.
- **Liên kết:** 0 hỏng nội bộ ở bản render đầu; chưa kiểm liên kết ngoài.
- **PII/secret:** không phát hiện trên cây làm việc của các nhánh PR (grep); chưa quét toàn bộ lịch sử git.
- **Audit nhất quán (`audit_references.py`):** 366 lần trích dẫn, đủ 103 mục, không thiếu/ngoài khoảng/trùng/mojibake. Chỉ kiểm cấu trúc, không xác nhận nội dung.
- **Đối chiếu OpenAlex/Semantic Scholar:** 56 mục có DOI: 40 khớp hoàn toàn, 7 lệch năm online/issue, 2 một phần, 6 không khớp, 1 DOI chưa phân giải.
- **Audit trang nguồn (47 mục không DOI):** chạy lại 21/11/2026 sau khi sửa lỗi biểu thức chính quy: MATCH 17, PARTIAL 9, MISMATCH 2, NOT_CHECKED 19; kết quả không ổn định giữa các lần chạy, chỉ là gợi ý.
- **QA pháp lý:** 14 văn bản đã đối chiếu nguồn chính thống: 11 xác nhận số hiệu/ngày, 1 xác nhận một phần ([66] TT 50/2025), 2 không tìm được nguồn chính thống ([64] Luật Dữ liệu, [82] QĐ 3218). Hai chi tiết đã kiểm lại độc lập: Luật 91/2025 gồm 05 chương, 39 điều; hạn 30/9/2025 và 31/12/2026 của TT 13/2025.
- **Đáp án quiz:** 34 câu, đáp án đúng, phân bố A8/B8/C9/D9.

## 6. Việc còn mở (chờ Ben hoặc người audit)

| # | Mục | Ghi chú |
|---|---|---|
| 1 | NIH NOT-OD-26-046: trạng thái ("thí điểm" hay "bắt buộc"; "thay thế" hay "cập nhật" NOT-OD-21-014) | Văn bản hiện mâu thuẫn; Quiz 1.2 phụ thuộc |
| 2 | Mốc FHIR R6 ballot và ICH E6(R3) Annex 2 | Nguồn dẫn hiện không chứa bằng chứng (`[35]`, `[4]`) |
| 3 | Chi tiết pháp lý chưa đối chiếu được | Mức lưu trữ 30/20 năm của TT 33/2025; thủ tục Cục A05/DPIA của Luật 91; toàn văn Luật Dữ liệu 60/2024, TT 50/2025, QĐ 3218 |
| 4 | `ref_045` (Wilkinson 2019) và `ref_103` (Lane 2020) | DOI trỏ tới bài có tiêu đề khác với tiêu đề đang ghi |
| 5 | Danh mục APA 334 mục đầy đủ | Danh mục hiện chỉ có tiêu đề + URL |
| 6 | Ethics/CITI/DUA trong M0 | Plan đổi M0 thành "nhập môn + hướng dẫn học"; handover còn mô tả M0 có đạo đức |
| 7 | Phạm vi đề cương `BIOMEDICAL_RDM_COURSE_SYLLABUS_v2.0.0` (chưa commit) | Sản phẩm mới (học phần 2 tín chỉ, lab, đồ án) hay kế hoạch tương lai của mini-course; đặt ở repo nào; dùng NĐ 13/2023 và TT 46/2018 đã hết hiệu lực |
| 8 | Audit thủ công 47 mục không DOI | Kết quả trang nguồn chỉ là gợi ý; xem `ref_034`, `ref_046`, `ref_018`, `ref_053` trong `DECISIONS.md` |
| 9 | Trạng thái pending | 15 `BIB_PENDING` + 3 chưa xác định + 85 `VERIFIED_UNAUDITED` (chưa audit độc lập) |
| 10 | Khẳng định đã biết nhưng chưa giải quyết | Khoảng tin cậy LEGEND-HTN gộp; lịch sử ALCOA/MHRA/EMA; ICH E8(R1) không có tham khảo; nguồn thứ cấp (CASRAI, Utrecht) làm căn cứ; ghi chú quy trình còn trong thân bài |
| 11 | Đáp án quiz theo thứ tự `ABCD` lặp lại | Phân bố đều nhưng dễ đoán; cần xáo lại ở `docs/course-source` rồi đồng bộ |
| 12 | Tài liệu hướng dẫn agent trong `docs/reviews/` | Quyết định nơi lưu và có nêu tên công cụ trong repo công khai hay không |

## 7. Bước tiếp theo đề xuất

1. Ben quyết các mục 1, 2, 5, 6, 7 ở §6; sửa các mục DOI sai (mục 4) sau khi đối chiếu bản gốc.
2. Đối chiếu nội dung các chi tiết pháp lý còn lại (mục 3) với văn bản gốc.
3. Audit thủ công 47 mục không DOI; cập nhật `citation-audit.csv` (`VERIFIED_UNAUDITED` → `VERIFIED`/`BIB_PENDING`/`CONTENT_PENDING`).
4. Xáo lại thứ tự đáp án quiz ở nguồn khóa học và đồng bộ.
5. Chạy lại `quarto render`, `npm run build`, `scripts/audit_references.py` và `sync_from_source.py --check` sau mỗi đợt merge.
6. Soạn các chương mới theo phạm vi đã chốt ở mục 7 của §6; review từng chương theo `AGENTS.md`.
