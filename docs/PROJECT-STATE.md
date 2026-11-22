# Trạng thái dự án Biomedical RDM

**Phiên bản:** 2.3.0 · **Ngày:** 22/11/2026 (cập nhật sau PR #18–#19, triển khai web, sửa hiển thị công thức và sơ đồ) · **Người nghiệm thu:** TS. Hoàng Quang Huy (Ben)
**Mục đích:** lưu trạng thái dự án để tiếp tục công việc mà không phải dựng lại ngữ cảnh.

## 1. Tóm tắt

Dự án có **hai repo công khai** của tài khoản `fossbk-spec`:

| Repo | Vai trò | Trạng thái (22/11/2026) |
|---|---|---|
| `biomedical-rdm` | **Repo gốc**, nguồn chân lý: literature review, danh mục tham khảo, nguồn khóa học, giáo trình (chương, phụ lục, syllabus, quiz), hướng dẫn dùng chung | `main`: PR #1–#4 đã merge; PR #5 đã đóng (nội dung gộp qua PR #15). **PR #6 (draft)** là nhánh tích hợp giáo trình; các PR con #7–#19 đã merge vào nhánh này, **chưa vào `main`**. Repo chưa bật Pages |
| `biomedical-rdm-course` | **Web khóa học** (VitePress); nội dung đồng bộ một chiều từ repo gốc | `main`: PR #1–#4, #6–#9 đã merge (#6 đồng bộ giáo trình, #7 loại trang `AGENTS`, #8 hiển thị công thức và sơ đồ, #9 đồng bộ quiz); PR #5 đã đóng. **Pages đã bật** (nhánh `gh-pages`, triển khai thủ công), bản công khai hiện là `a976252` tại https://fossbk-spec.github.io/biomedical-rdm-course/ |

Quyết định đã chốt: **giữ tách hai repo**; khóa học **đăng ở `biomedical-rdm-course`**, tài liệu lưu ở **repo gốc** (sửa ở repo gốc, đồng bộ một chiều sang repo khóa học). Khóa học là **miễn phí, tự học theo nhịp người đọc**, không phải học phần có tín chỉ.

## 2. Nội dung repo gốc `biomedical-rdm` (nhánh PR #6)

- **Giáo trình:** `docs/chapters/ch00_getting_started.md` (M0), `ch01`–`ch06` (6 chương đã sửa theo mẫu tách nội dung cố định/cập nhật), `ch07_completion_and_capstone.md` (quiz tổng hợp 10 câu, capstone tự đánh giá, bảng tự nghiệm thu); `docs/syllabus/BIOMEDICAL_RDM_FREE_SELF_PACED_SYLLABUS.md` (syllabus tự học, thay bản 2 tín chỉ v2.0.0; bản cũ còn trong lịch sử git). Tổng giáo trình + phụ lục + syllabus khoảng 44.000 từ.
- **Phụ lục cập nhật** (`docs/appendices/`, đặt tên theo slug, có `reviewed`/`next_review`, bảng Trạng thái/URL/Ngày kiểm): `legal`, `funder-templates`, `retention`, `standards`, `redcap-lab-notes`, `fhir-omop-lab-notes`, `privacy-lab-notes`, `quality-ai-lab-notes`, `appendices-CHANGELOG`; sổ kiểm chứng pháp lý `docs/legal-verification.md`.
- **Literature review:** `docs/literature-review/index.md` (tổng hợp tường thuật có kiểm chứng, **không** phải systematic review theo PRISMA; trích dẫn số `[n]`, 1..103) và `CHANGES.md`.
- **Nguồn khóa học mini:** `docs/course-source/rdm-mini-course-source.md` + `README.md` (17 trang tách bằng marker `<!-- page: <path> -->`; quiz cuối khóa 10 câu đã làm lại: đáp án phân bố A3/B2/C3/D2, câu khái niệm không phụ thuộc ngày/số hiệu).
- **Danh mục tham khảo:** `references/references.bib` **115 mục** = 103 mục lõi (`ref_001`–`ref_103`, khớp số `[n]` của literature review) + 12 mục riêng của chương (`ref_104`–`ref_115`, `used_in = chapter_only`); `references-334.bib` (334 mục, chỉ tiêu đề + URL); `citation-audit.csv` (115 dòng); `VERIFICATION.md`, `AUDIT-REPORT.md`, `audit-nodoi-gemini.csv`.
- **Script:** `build_bib.py` (`--check`; 103 lõi + mục mở rộng), `verify_refs.py`, `audit_references.py`, `audit_nodoi_gemini.py` (kiểm trang nguồn cho mục không DOI, tư vấn), `check_quizzes.py` (kiểm cấu trúc, số câu, phân bố đáp án, độ dài phương án và từ tuyệt đối của quiz ch01–ch07), `check_volatile.py` + `volatile_terms.txt` (cảnh báo khẳng định dễ hết hạn trong thân chương không trỏ phụ lục; quét ch00–ch07 và phụ lục).
- **Tài liệu quản trị:** `docs/DECISIONS.md`, `docs/PROJECT-STATE.md`, `docs/INPUT-INVENTORY.md`, `docs/DATA-USE.md`, `docs/plans/` (kế hoạch 10 ngày; kế hoạch tích hợp pipeline v1.1.0; kế hoạch tách nội dung cố định/cập nhật v1.1.0), `AGENTS.md`, `CONTRIBUTING.md`, `LICENSE` (CC BY 4.0), `LICENSE-CODE` (MIT), `_quarto.yml` (sách Quarto 22+ trang: chương, phụ lục, sổ kiểm chứng, tài liệu dự án), `index.qmd`, `README.md`.
- **Hướng dẫn dùng chung:** `docs/guides/diagrams-math-quiz-web.md` (giữ Mermaid làm nguồn sơ đồ, quy tắc thiết kế sơ đồ, công thức MathJax, quy tắc quiz chống lộ đáp án, quy trình triển khai web, checklist cho sách khác); bản dùng chung đã đồng bộ sang HDBS (`fossbk-spec/HDBS`, PR #6, `knowledge_base/GUIDE_DIAGRAMS_MATH_QUIZ_WEB.md`).
- **Quiz:** ch01–ch06 có mục `Quiz tự kiểm tra` (ch01 5, ch02 4, ch03 5, ch04 5, ch05 4, ch06 6 = 29 câu) và ch07 có quiz tổng hợp 10 câu: tổng 39 câu.

## 3. Nội dung repo khóa học `biomedical-rdm-course` (main)

- **Mini-course:** 7 module (M0 không quiz; M1–M6 mỗi bài có trang bài học và quiz 4 câu), quiz tổng hợp 10 câu, glossary, syllabus mini, roadmap. Thứ tự đã khớp giáo trình: M5 = bảo mật/khử định danh (`module-5-privacy`), M6 = FAIR và chia sẻ (`module-6-fair-ai`). Bài 5 mini-course (cũ M6) vẫn chứa cả phần AI-ready; syllabus đặt AI-ready ở M6 (chưa tách nội dung).
- **Giáo trình đầy đủ** (`course/book/`, 21 trang sinh bằng `sync_from_source.py` theo `scripts/sync_manifest.json`; không sửa tay): mục lục, syllabus tự học, ch00–ch07, 9 phụ lục kèm sổ kiểm chứng pháp lý, danh mục tham khảo (115 neo, kèm trạng thái từ `citation-audit.csv`). Trích dẫn `[@ref_NNN]` được đổi thành `[NNN]` có liên kết.
- **Hiển thị:** công thức LaTeX dựng bằng MathJax (`markdown-it-mathjax3`); sơ đồ Mermaid dựng bằng thành phần `Mermaid.vue` (nhãn SVG thuần, phóng to/thu nhỏ, vừa khung, kéo để di chuyển, toàn màn hình, tab mới, tải SVG, xem mã nguồn, theo chế độ sáng/tối). `AGENTS.md`, `README.md`, `CONTRIBUTING.md` không được dựng thành trang công khai.
- **Kiểm tra và triển khai:** `sync_from_source.py --check` (38 trang), `npm run build`; triển khai thủ công: build từ `main`, thay nội dung nhánh `gh-pages`, kiểm các URL chính sau khi Pages dựng xong. Merge vào `main` không tự xuất bản.

## 4. Các quyết định đã chốt

| Quyết định | Căn cứ |
|---|---|
| Giữ tách hai repo; khóa học đăng ở repo khóa học, tài liệu ở repo gốc, đồng bộ một chiều | Ben, 20–21/11/2026 |
| Khóa học miễn phí, tự học theo nhịp người đọc; không tín chỉ, không điểm, không chứng nhận; lab tự chọn | Ben, 21/11/2026 |
| Mục tiêu tự đánh giá của giáo trình: đúng ≥ 70% tổng số câu quiz (hiện 39 = 29 theo chương + 10 tổng hợp; số câu mỗi chương theo nội dung chương) và đúng ≥ 2/3 câu Q1–Q3 của quiz tổng hợp; tự đánh giá, không ai ghi lại, làm lại không giới hạn. Bộ quiz mini-course (34 câu) giữ quy tắc 24/34 riêng | Ben, 21–22/11/2026 |
| Tách nội dung cố định (thân chương) và nội dung cập nhật (phụ lục, ngày chốt, rà soát 6 tháng) | Ben, 21/11/2026 |
| Phụ lục đặt tên theo slug (không đánh chữ cái) để thêm phụ lục không phải đánh số lại | Review 21/11/2026 |
| Mục tham khảo riêng của chương dùng khóa `ref_104+`, chỉ thêm khi DOI/URL chính thống đọc được và metadata khớp; giữ trạng thái `VERIFIED_UNAUDITED` | Quyết định biên tập, 21/11/2026 |
| Thân chương không nêu số hiệu/ngày/số điều/phiên bản dễ đổi mà không trỏ phụ lục kèm ngày chốt; nội dung chưa kiểm giữ `[CẦN KIỂM CHỨNG]`/`CONTENT_PENDING` | `AGENTS.md`, review 21/11/2026 |
| Quiz không hỏi dữ kiện dễ đổi (ngày hiệu lực, số điều, giới hạn từ mẫu NIH, phiên bản chuẩn, mã concept) | Review 21/11/2026 |
| Trích dẫn số `[n]` (1..103) trong literature review; chương dùng khóa `[@ref_NNN]`, danh mục chương dựng từ `references.bib` | Ben, 21/11/2026 |
| Định nghĩa trạng thái: `VERIFIED`, `BIB_PENDING`, `CONTENT_PENDING`, `BLOCKED_INPUT`; hiện còn thêm `VERIFIED_UNAUDITED` (đã đối chiếu metadata, chưa audit độc lập) | `DECISIONS.md` |
| Case study dự án thực (DrMayDay) dùng nguyên bản, không ẩn danh, không chuyển file; **chưa đưa vào repo nào** | Ben, 21/11/2026 |
| Ba quyết định mặc định cho ch02–ch06 và nhóm syllabus: case study ghi "tình huống giả định minh họa"; lab giữ trong cùng file với chương; không dùng số/khẳng định chưa đọc ở nguồn. Nhóm syllabus: quiz cuối là câu khái niệm không dạy dữ kiện có ngày; capstone là tình huống giả định, không dùng tên dự án thật | Ben xác nhận, 22/11/2026 |
| Các mục `CONTENT_PENDING` được chấp nhận tạm thời; xử lý khi có người đọc nguồn chính thống | Ben, 22/11/2026 |
| Giữ Mermaid làm nguồn sơ đồ; quy tắc thiết kế (nhãn ngắn, tách sơ đồ lớn, có tiêu đề và mô tả); đề xuất dựng sẵn SVG khi build và vẽ tay vài hình then chốt; ghi vào hướng dẫn dùng chung và HDBS | Ben, 22/11/2026 |
| Triển khai bản web mới lên `gh-pages` dù còn mục `CONTENT_PENDING` | Ben, 22/11/2026 |
| Quiz chống lộ đáp án: phân bố A–D đều, đáp án đúng là phương án dài nhất tối đa 40% số câu, tỷ lệ độ dài ≤ 1,3, phương án sai không dùng từ tuyệt đối nhiều hơn đáp án đúng; script kiểm phải thực thi ngưỡng | Review 22/11/2026 |

## 5. Kết quả kiểm tra

- **Render (repo gốc):** `quarto render`: 25/25 trang, không cảnh báo, không trích dẫn chưa phân giải, không liên kết nội bộ hỏng (22/11/2026). Sách Quarto gồm ch00–ch07, phụ lục, sổ kiểm chứng và tài liệu dự án; `docs/guides/` không nằm trong sách.
- **Web (repo khóa học):** kiểm bằng trình duyệt trên bản preview và trên site công khai: 6/6 sơ đồ Mermaid dựng được (ch01 2, ch02 2, ch03 1, ch05 1), 67 công thức MathJax không lỗi, không còn cặp `$...$` thô; thử phóng to, toàn màn hình và Esc; trang quiz tổng hợp có 10 câu 4 phương án, chọn đáp án hiện kết quả đúng. Chưa kiểm điện thoại, Safari/Firefox, chế độ tối bằng ảnh chụp, in/xuất PDF.
- **Script:** `build_bib.py --check` (115 mục), `audit_references.py` (cấu trúc), `check_volatile.py --check` (0 vi phạm), `check_quizzes.py --check` (39 câu; đáp án A/B/C/D = 10/9/11/9; đáp án đúng là phương án dài nhất 9/39), `git diff --check origin/main`: 19 cảnh báo khoảng trắng cuối dòng/dòng trống cuối file (đa số là hai dấu cách ngắt dòng Markdown có chủ ý; có từ trước khi gộp, chưa dọn).
- **Trạng thái danh mục** (`citation-audit.csv`, 115 dòng): 103 `VERIFIED_UNAUDITED` (gồm 12 mục riêng của chương), 9 `BIB_PENDING`, 3 `PENDING_UNDETERMINED`. **Chưa audit độc lập; không mục nào được coi là `VERIFIED` đầy đủ.**
- **Đối chiếu OpenAlex/Semantic Scholar** (chỉ thư mục): xem `references/VERIFICATION.md`; 12 mục riêng của chương đối chiếu Crossref/URL chính thống (21/11/2026).
- **Script lab đã chạy thử** (dữ liệu tổng hợp, môi trường tạm): Lab 3 (ETL FHIR→OMOP), Lab 4 (MICE), Lab 5 (khử định danh), Lab 6 (chia tập theo bệnh nhân). Kết quả ở các phụ lục `*-lab-notes`. Lab 2 (CSV REDCap) chưa chạy thử trên REDCap Sandbox. Trên Windows cần `PYTHONIOENCODING=utf-8` khi chạy script in tiếng Việt.

## 6. Việc còn mở

| # | Mục | Ghi chú |
|---|---|---|
| 1 | Quiz 6 bài của mini-course (trong `course-source`) | Chưa kiểm cùng lỗi độ dài đáp án và từ tuyệt đối như quiz mới; hai quy tắc tự đánh giá đang song song (giáo trình: tỷ lệ; mini-course: 24/34) |
| 2 | Sơ đồ | Thiết kế lại 2–3 sơ đồ (ch03, ch05: nhãn quá dài, ch05 cao khoảng 1.700 px, ch03 chỉ còn khoảng 40% khi vừa khung); thêm tiêu đề và mô tả bằng văn bản; cân nhắc dựng sẵn SVG khi build (bản in/PDF/offline) |
| 3 | Kiểm hiển thị web | Điện thoại, Safari/Firefox, chế độ tối, in/xuất PDF |
| 4 | Mini-course Bài 5 chứa phần AI-ready | Syllabus đặt AI-ready ở M6; cần tách nội dung ở `course-source` |
| 5 | NIH: giới hạn 300 từ gắn với yếu tố nào; tên mẫu trên DMPTool production; điều kiện dùng mẫu cũ khi chuyển tiếp (NOT-OD-26-100) | Cần mở bản DOCX/trang NIH bằng trình duyệt; hiện `CONTENT_PENDING` |
| 6 | Pháp lý Việt Nam chưa đối chiếu | Điều 69 Luật KCB 15/2023; nghĩa vụ DPIA/DPO theo Luật 91/2025 và NĐ 356/2025; TT 50/2025; bảng 30/20 năm của TT 33/2025; QĐ 3218 |
| 7 | Mốc EHDS (2027/2029/2031/2035), ICH E6(R3) số mục Annex, FHIR R6 | Chưa tự đối chiếu độc lập; `CONTENT_PENDING` |
| 8 | Mã concept OMOP/SNOMED trong lab (kể cả đơn vị mmHg `8753` hay `8876`, concept bệnh mày đay) | Cần tra Athena bằng trình duyệt; script đặt `0` (chưa ánh xạ) |
| 9 | Nguồn gốc ALCOA (Woollen), DataCite, số quy tắc DQD thật | `CONTENT_PENDING` |
| 10 | Mục tham khảo cần xử lý | `ref_011` trong `.bib` là "Our journey" (2025), không phải "The Book of OHDSI"; `ref_045`, `ref_103` đã sửa tiêu đề theo DOI (PR #21), `ref_103` còn phải đối chiếu số liệu Phụ lục A; `ref_043`, `ref_072` là preprint; 9 `BIB_PENDING`; 3 URL trùng giữa mục cũ và mục mới |
| 11 | Audit độc lập 47 mục không DOI và chuyển `VERIFIED_UNAUDITED` → `VERIFIED` | Cần audit thủ công |
| 12 | Case study dự án thực (hai file + file DMPTool nháp, chỉ nằm trong thư mục làm việc cục bộ, chưa commit) | Chưa đưa vào repo; nếu đăng công khai cần chủ nhiệm đề tài/bệnh viện đồng ý; còn lỗi nội dung đã nêu (giả danh khác "Zero-PII"; UAS7 thuộc miền QS của SDTM; căn cứ pháp lý chưa kiểm) |
| 13 | Danh mục APA 334 mục; Ethics/CITI/DUA ở mức nâng cao; tài liệu hướng dẫn agent trong `docs/reviews/` | Chưa quyết |
| 14 | Lab 2 (CSV REDCap) chưa chạy thử trên REDCap Sandbox; một số phương án quiz hơi mơ hồ ("thường", "chủ yếu") | Chưa xử lý |
| 15 | Workflow CI; Pages cho repo gốc | Tài khoản làm việc không có quyền Workflows; Ben tự thêm. Repo khóa học triển khai thủ công |
| 16 | Gộp PR #6 vào `main` của repo gốc | Chưa; điều kiện: các mục trên và quyết định của Ben |
| 17 | HDBS: `KNOWLEDGE_BASE_PUBLISHING_PITFALLS_AND_FIXES.md` có hai bản giống hệt (gốc repo và `knowledge_base/`) | Chờ chủ repo HDBS quyết giữ bản nào |

## 7. Bước tiếp theo đề xuất

1. Thiết kế lại các sơ đồ phức tạp và thêm tiêu đề, mô tả (mục 2); kiểm hiển thị trên thiết bị khác (mục 3).
2. Kiểm quiz mini-course và thống nhất quy tắc tự đánh giá (mục 1); tách nội dung AI-ready (mục 4).
3. Người đọc nguồn chính thống xử lý các mục `CONTENT_PENDING` (mục 5–9) bằng trình duyệt; cập nhật phụ lục và đồng bộ lại web.
4. Audit độc lập danh mục (mục 10–11).
5. Sau mỗi đợt: chạy `quarto render`, `npm run build`, `audit_references.py`, `check_volatile.py --check`, `check_quizzes.py --check`, `sync_from_source.py --check`; triển khai lại `gh-pages` nếu nội dung web đổi.
6. Khi đủ điều kiện, rà soát lần cuối và quyết định gộp PR #6 vào `main`.
