# Trạng thái dự án Biomedical RDM

**Phiên bản:** 2.0.0 · **Ngày:** 22/11/2026 (cập nhật sau PR #5–#14) · **Người nghiệm thu:** TS. Hoàng Quang Huy (Ben)
**Mục đích:** lưu trạng thái dự án để tiếp tục công việc mà không phải dựng lại ngữ cảnh.

## 1. Tóm tắt

Dự án có **hai repo công khai** của tài khoản `fossbk-spec`:

| Repo | Vai trò | Trạng thái (22/11/2026) |
|---|---|---|
| `biomedical-rdm` | **Repo gốc**, nguồn chân lý: literature review, danh mục tham khảo, nguồn khóa học, giáo trình (chương, phụ lục, syllabus) | `main`: PR #1–#4 đã merge. PR #5 (sửa script audit trang + trạng thái) mở, đã được gộp vào nhánh này. **PR #6 (draft)** là nhánh tích hợp giáo trình; các PR con #7–#14 đã merge vào nhánh PR #6, chưa vào `main` |
| `biomedical-rdm-course` | **Web khóa học** (VitePress, có Quarto song song); nội dung lấy từ repo gốc | `main`: PR #1–#4 đã merge. PR #5 (draft, bài học mở rộng) vẫn mở và sẽ bị thay bởi cơ chế đồng bộ mới |

Quyết định đã chốt: **giữ tách hai repo**; khóa học **đăng ở `biomedical-rdm-course`**, tài liệu lưu ở **repo gốc** (sửa ở repo gốc, đồng bộ một chiều sang repo khóa học). Khóa học là **miễn phí, tự học theo nhịp người đọc**, không phải học phần có tín chỉ.

## 2. Nội dung repo gốc `biomedical-rdm` (nhánh PR #6)

- **Giáo trình:** `docs/chapters/ch00_getting_started.md` (M0), `ch01`–`ch06` (6 chương đã sửa theo mẫu tách nội dung cố định/cập nhật), `ch07_completion_and_capstone.md` (quiz tổng hợp 10 câu, capstone tự đánh giá, bảng tự nghiệm thu); `docs/syllabus/BIOMEDICAL_RDM_FREE_SELF_PACED_SYLLABUS.md` (syllabus tự học, thay bản 2 tín chỉ v2.0.0; bản cũ còn trong lịch sử git). Tổng giáo trình + phụ lục + syllabus khoảng 44.000 từ.
- **Phụ lục cập nhật** (`docs/appendices/`, đặt tên theo slug, có `reviewed`/`next_review`, bảng Trạng thái/URL/Ngày kiểm): `legal`, `funder-templates`, `retention`, `standards`, `redcap-lab-notes`, `fhir-omop-lab-notes`, `privacy-lab-notes`, `quality-ai-lab-notes`, `appendices-CHANGELOG`; sổ kiểm chứng pháp lý `docs/legal-verification.md`.
- **Literature review:** `docs/literature-review/index.md` (tổng hợp tường thuật có kiểm chứng, **không** phải systematic review theo PRISMA; trích dẫn số `[n]`, 1..103) và `CHANGES.md`.
- **Nguồn khóa học mini:** `docs/course-source/rdm-mini-course-source.md` + `README.md` (17 trang tách bằng marker `<!-- page: <path> -->`; quiz cuối khóa 10 câu đã làm lại: đáp án phân bố A3/B2/C3/D2, câu khái niệm không phụ thuộc ngày/số hiệu).
- **Danh mục tham khảo:** `references/references.bib` **115 mục** = 103 mục lõi (`ref_001`–`ref_103`, khớp số `[n]` của literature review) + 12 mục riêng của chương (`ref_104`–`ref_115`, `used_in = chapter_only`); `references-334.bib` (334 mục, chỉ tiêu đề + URL); `citation-audit.csv` (115 dòng); `VERIFICATION.md`, `AUDIT-REPORT.md`, `audit-nodoi-pages.csv`.
- **Script:** `build_bib.py` (`--check`; 103 lõi + mục mở rộng), `verify_refs.py`, `audit_references.py`, `audit_nodoi_pages.py` (kiểm trang nguồn cho mục không DOI, tư vấn), `check_volatile.py` + `volatile_terms.txt` (cảnh báo khẳng định dễ hết hạn trong thân chương không trỏ phụ lục; quét ch00–ch07 và phụ lục).
- **Tài liệu quản trị:** `docs/DECISIONS.md`, `docs/PROJECT-STATE.md`, `docs/INPUT-INVENTORY.md`, `docs/DATA-USE.md`, `docs/plans/` (kế hoạch 10 ngày; kế hoạch tích hợp pipeline v1.1.0; kế hoạch tách nội dung cố định/cập nhật v1.1.0), `AGENTS.md`, `CONTRIBUTING.md`, `LICENSE` (CC BY 4.0), `LICENSE-CODE` (MIT), `_quarto.yml` (sách Quarto 22+ trang: chương, phụ lục, sổ kiểm chứng, tài liệu dự án), `index.qmd`, `README.md`.

## 3. Nội dung repo khóa học `biomedical-rdm-course` (main)

- 7 module mini (M0 không quiz; M1–M6 mỗi bài có trang bài học và quiz 4 câu), quiz tổng hợp 10 câu, glossary, syllabus (mini-course), roadmap; `scripts/sync_from_source.py [--check]` hiện chỉ đồng bộ 17 trang mini-course từ `course-source`.
- Hạn chế đã biết: thứ tự module mini-course (M5 = FAIR, M6 = bảo mật/AI) **chưa khớp** giáo trình (M5 = bảo mật/khử định danh, M6 = FAIR & AI-ready); chương, phụ lục và syllabus mới **chưa có** trên web; đang mở rộng cơ chế đồng bộ (xem §6).

## 4. Các quyết định đã chốt

| Quyết định | Căn cứ |
|---|---|
| Giữ tách hai repo; khóa học đăng ở repo khóa học, tài liệu ở repo gốc, đồng bộ một chiều | Ben, 20–21/11/2026 |
| Khóa học miễn phí, tự học theo nhịp người đọc; không tín chỉ, không điểm, không chứng nhận; lab tự chọn | Ben, 21/11/2026 |
| Mục tiêu tự đánh giá: ≥ 24/34 câu và đúng ≥ 2/3 câu Q1–Q3 của quiz tổng hợp (tự đánh giá, không ai ghi lại; làm lại không giới hạn) | Ben, 21/11/2026 |
| Tách nội dung cố định (thân chương) và nội dung cập nhật (phụ lục, ngày chốt, rà soát 6 tháng) | Ben, 21/11/2026 |
| Phụ lục đặt tên theo slug (không đánh chữ cái) để thêm phụ lục không phải đánh số lại | Review 21/11/2026 |
| Mục tham khảo riêng của chương dùng khóa `ref_104+`, chỉ thêm khi DOI/URL chính thống đọc được và metadata khớp; giữ trạng thái `VERIFIED_UNAUDITED` | Quyết định biên tập, 21/11/2026 |
| Thân chương không nêu số hiệu/ngày/số điều/phiên bản dễ đổi mà không trỏ phụ lục kèm ngày chốt; nội dung chưa kiểm giữ `[CẦN KIỂM CHỨNG]`/`CONTENT_PENDING` | `AGENTS.md`, review 21/11/2026 |
| Quiz không hỏi dữ kiện dễ đổi (ngày hiệu lực, số điều, giới hạn từ mẫu NIH, phiên bản chuẩn, mã concept) | Review 21/11/2026 |
| Trích dẫn số `[n]` (1..103) trong literature review; chương dùng khóa `[@ref_NNN]`, danh mục chương dựng từ `references.bib` | Ben, 21/11/2026 |
| Định nghĩa trạng thái: `VERIFIED`, `BIB_PENDING`, `CONTENT_PENDING`, `BLOCKED_INPUT`; hiện còn thêm `VERIFIED_UNAUDITED` (đã đối chiếu metadata, chưa audit độc lập) | `DECISIONS.md` |
| Case study dự án thực (DrMayDay) dùng nguyên bản, không ẩn danh, không chuyển file; **chưa đưa vào repo nào** | Ben, 21/11/2026 |
| Ba quyết định mặc định cho ch02–ch06 và nhóm syllabus (case study ghi minh họa; lab giữ trong chương; không dùng số/khẳng định chưa đọc ở nguồn) | Dùng tạm; chờ Ben xác nhận |

## 5. Kết quả kiểm tra

- **Render:** `quarto render` ở repo gốc: 25/25 trang, không cảnh báo, không trích dẫn chưa phân giải, không liên kết nội bộ hỏng (22/11/2026). Chưa kiểm hiển thị Mermaid trên trình duyệt; chưa chạy GitHub Pages cho repo gốc; chưa chạy lại `npm run build` ở repo khóa học sau các đợt merge giáo trình.
- **Script:** `build_bib.py --check` (115 mục), `audit_references.py` (cấu trúc), `check_volatile.py --check` (0 vi phạm), `git diff --check`: đạt.
- **Trạng thái danh mục** (`citation-audit.csv`, 115 dòng): 97 `VERIFIED_UNAUDITED` (gồm 12 mục riêng của chương), 15 `BIB_PENDING`, 3 `PENDING_UNDETERMINED`. **Chưa audit độc lập; không mục nào được coi là `VERIFIED` đầy đủ.**
- **Đối chiếu OpenAlex/Semantic Scholar** (chỉ thư mục): xem `references/VERIFICATION.md`; 12 mục riêng của chương đối chiếu Crossref/URL chính thống (21/11/2026).
- **Script lab đã chạy thử** (dữ liệu tổng hợp, môi trường tạm): Lab 3 (ETL FHIR→OMOP), Lab 4 (MICE), Lab 5 (khử định danh), Lab 6 (chia tập theo bệnh nhân). Kết quả ở các phụ lục `*-lab-notes`. Lab 2 (CSV REDCap) chưa chạy thử trên REDCap Sandbox. Trên Windows cần `PYTHONIOENCODING=utf-8` khi chạy script in tiếng Việt.

## 6. Việc còn mở

| # | Mục | Ghi chú |
|---|---|---|
| 1 | Quiz theo bài (4–5 câu/chương) trong repo gốc | Chỉ ch01 có; đang soạn quiz 5 câu cho từng chương. **Cần chốt số câu và quy tắc 34 câu** (24 theo bài + 10 tổng hợp) nếu tổng thay đổi |
| 2 | Đồng bộ chương, phụ lục, syllabus, quiz mới sang repo khóa học | Đang mở rộng `sync_from_source.py` (manifest, danh mục tham khảo, sidebar, khớp thứ tự M5/M6) |
| 3 | NIH: giới hạn 300 từ gắn với yếu tố nào; tên mẫu trên DMPTool production; điều kiện dùng mẫu cũ khi chuyển tiếp (NOT-OD-26-100) | Cần mở bản DOCX/trang NIH bằng trình duyệt; hiện `CONTENT_PENDING` |
| 4 | Pháp lý Việt Nam chưa đối chiếu | Điều 69 Luật KCB 15/2023; nghĩa vụ DPIA/DPO theo Luật 91/2025 và NĐ 356/2025; TT 50/2025; bảng 30/20 năm của TT 33/2025; QĐ 3218 |
| 5 | Mốc EHDS (2027/2029/2031/2035), ICH E6(R3) số mục Annex, FHIR R6 | Chưa tự đối chiếu độc lập; `CONTENT_PENDING` |
| 6 | Mã concept OMOP/SNOMED trong lab (kể cả đơn vị mmHg `8753` hay `8876`, concept bệnh mày đay) | Cần tra Athena bằng trình duyệt; script đặt `0` (chưa ánh xạ) |
| 7 | Nguồn gốc ALCOA (Woollen), DataCite, số quy tắc DQD thật | `CONTENT_PENDING` |
| 8 | Mục tham khảo cần xử lý | `ref_011` trong `.bib` là "Our journey" (2025), không phải "The Book of OHDSI"; `ref_045`, `ref_103` DOI/tiêu đề lệch; `ref_043`, `ref_072` là preprint; 15 `BIB_PENDING`; 3 URL trùng giữa mục cũ và mục mới |
| 9 | Audit độc lập 47 mục không DOI và chuyển `VERIFIED_UNAUDITED` → `VERIFIED` | Cần audit thủ công |
| 10 | Case study dự án thực (hai file + file DMPTool nháp) | Chưa đưa vào repo; nếu đăng công khai cần chủ nhiệm đề tài/bệnh viện đồng ý; còn lỗi nội dung đã nêu (giả danh ≠ "Zero-PII"; UAS7 thuộc miền QS của SDTM; căn cứ pháp lý chưa kiểm) |
| 11 | Ba quyết định mặc định cho ch02–ch06 và nhóm syllabus | Chờ Ben xác nhận |
| 12 | Danh mục APA 334 mục; Ethics/CITI/DUA ở mức nâng cao; tài liệu hướng dẫn agent trong `docs/reviews/` | Chưa quyết |
| 13 | GitHub Pages; workflow CI | Tài khoản làm việc không có quyền Workflows; Ben tự bật/thêm |
| 14 | Dọn nhánh và worktree đã merge | Chưa làm |
| 15 | Gộp PR #6 vào `main` | Chưa; điều kiện: các mục trên và quyết định của Ben |

## 7. Bước tiếp theo đề xuất

1. Hoàn tất quiz theo bài và đồng bộ sang repo khóa học; chạy `quarto render`, `npm run build`, `audit_references.py`, `check_volatile.py --check`, `sync_from_source.py --check` sau mỗi đợt.
2. Ben xác nhận các quyết định mặc định (mục 11) và quyết định số câu quiz (mục 1).
3. Người đọc nguồn chính thống xử lý các mục `CONTENT_PENDING` (mục 3–7) bằng trình duyệt; cập nhật phụ lục.
4. Audit độc lập danh mục (mục 8–9).
5. Khi đủ điều kiện, rà soát lần cuối và quyết định gộp PR #6 vào `main`; đóng PR #5 (nội dung đã gộp vào nhánh PR #6) và PR #5 của repo khóa học (bị thay bởi cơ chế đồng bộ).
