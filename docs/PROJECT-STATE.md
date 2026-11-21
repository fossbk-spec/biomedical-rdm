# Trạng thái dự án Biomedical RDM

**Phiên bản:** 1.0.0 · **Ngày:** 21/11/2026 · **Người nghiệm thu:** TS. Hoàng Quang Huy (Ben)
**Mục đích:** lưu trạng thái dự án để tiếp tục công việc mà không phải dựng lại ngữ cảnh.

## 1. Tóm tắt

Dự án có **hai repo công khai** của tài khoản `fossbk-spec`:

| Repo | Vai trò | Trạng thái |
|---|---|---|
| `biomedical-rdm` | **Repo gốc**, nguồn chân lý: literature review, danh mục tham khảo, nguồn khóa học | PR #1 đã **merge** vào `main` (merge commit `7636eca`) |
| `biomedical-rdm-course` | **Bản web** khóa học (Quarto), nội dung lấy từ repo gốc | PR #1 đã **merge** vào `main` (merge commit `dbf1791`) |

Ben đã chốt **giữ tách hai repo** (20/11/2026). Nhánh PR (`feat/initial-rdm-project`, `feat/initial-course-project`) chưa bị xóa.

Việc đã làm trong 20–21/11/2026: review độc lập hai PR, thực hiện sửa, dựng danh mục `.bib`, đối chiếu thư mục bằng OpenAlex và Semantic Scholar, push, merge. Còn một số mục chờ Ben (mục 6).

## 2. Nội dung repo gốc `biomedical-rdm`

- `docs/literature-review/index.md`: bản tổng hợp literature review (tổng hợp tường thuật có kiểm chứng, **không** phải systematic review theo PRISMA). Đã thêm front matter, sửa trích dẫn số cũ (`[19,185]`→`[38],[40]`; `[8,134,135]`→`[10],[28],[30]`), Phụ lục A còn 29 mục.
- `docs/literature-review/CHANGES.md`: mọi thay đổi so với file nguồn.
- `docs/course-source/rdm-mini-course-source.md` + `README.md`: **nguồn chân lý của khóa học**, 17 trang tách bằng marker `<!-- page: <path> -->`.
- `references/references.bib` (103 mục), `references/references-334.bib` (334 mục, chỉ tiêu đề + URL), `references/source-334-list.md` (danh mục thô), `references/citation-audit.csv` (103 dòng), `references/VERIFICATION.md`, `verification-doi-openalex.csv`, `verification-report.csv`.
- `scripts/build_bib.py` (`--check`), `scripts/verify_refs.py`.
- `docs/DECISIONS.md`, `docs/INPUT-INVENTORY.md`, `docs/DATA-USE.md`, `docs/plans/` (plan 10 ngày và plan tích hợp pipeline VERA).
- `LICENSE` (CC BY 4.0 cho nội dung), `LICENSE-CODE` (MIT), `CONTRIBUTING.md`, `.gitignore`, `_quarto.yml`, `index.qmd`, `README.md`.

## 3. Nội dung repo khóa học `biomedical-rdm-course`

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

- **Render:** `quarto render` chạy được ở cả hai repo (kiểm tra trước khi commit). Chưa kiểm tra lại sau merge. Chưa kiểm tra GitHub Pages; repo chưa có CI.
- **Liên kết nội bộ:** 0 hỏng trên bản render đầu (71 và 537 liên kết). Chưa kiểm liên kết ngoài.
- **PII/secret:** không phát hiện trên cây làm việc của nhánh PR (grep). Chưa quét toàn bộ lịch sử git.
- **Đối chiếu OpenAlex/Semantic Scholar** (chỉ thư mục, không xác nhận nội dung): trong 56 mục có DOI, 40 khớp hoàn toàn, 7 lệch năm (online/issue), 2 khớp một phần, 6 không khớp, 1 DOI chưa phân giải. 47 mục không có DOI chưa được xác nhận.
- **Đáp án quiz:** đã đọc lại cả 34 câu, đáp án đúng.

## 6. Việc còn mở (chờ Ben hoặc người audit)

| # | Mục | Ghi chú |
|---|---|---|
| 1 | NIH NOT-OD-26-046: trạng thái ("thí điểm" hay "bắt buộc"; "thay thế" hay "cập nhật" NOT-OD-21-014) | Văn bản hiện mâu thuẫn; Quiz 1.2 phụ thuộc |
| 2 | Mốc FHIR R6 ballot và ICH E6(R3) Annex 2 | Nguồn dẫn hiện không chứa bằng chứng (`[35]`, `[4]`) |
| 3 | Văn bản pháp luật Việt Nam gốc (Luật 91/2025, NĐ 356/2025, TT 13/2025, TT 33/2025, TT 50/2025, QĐ 1308, QĐ 3218) | Chưa có nguồn gốc kiểm được; cần đối chiếu số chương/điều, thời hạn lưu trữ |
| 4 | `ref_045` (Wilkinson 2019) và `ref_103` (Lane 2020) | DOI trỏ tới bài có tiêu đề khác với tiêu đề đang ghi |
| 5 | Danh mục APA 334 mục đầy đủ | Danh mục hiện chỉ có tiêu đề + URL; chưa có `references-334-apa.md` |
| 6 | Ethics/CITI/DUA trong M0 | Plan đổi M0 thành "nhập môn + hướng dẫn học"; handover còn mô tả M0 có đạo đức |
| 7 | 47 mục không DOI chưa được xác nhận | Cần audit thủ công |
| 8 | 12 mục pending thư mục | `[1]–[3]`, `[30]`, `[48]`, `[49]`, `[61]`, `[68]`, `[89]` là BIB_PENDING; `[95]`, `[100]`, `[101]` chưa xác định |
| 9 | Khẳng định đã biết nhưng chưa giải quyết | Khoảng tin cậy LEGEND-HTN gộp; lịch sử ALCOA/MHRA/EMA; ICH E8(R1) không có tham khảo; nguồn thứ cấp (CASRAI, Utrecht) dùng làm căn cứ; ghi chú quy trình còn trong thân bài |
| 10 | GitHub Pages | Cần bật bằng tay; tài khoản làm việc không có quyền Workflows |
| 11 | `references.bib` sau audit | Hiện chưa có trường tác giả/trang cho nhiều mục pending |
| 12 | Gán nhãn trạng thái | 91 mục đang là `VERIFIED_UNAUDITED` (chưa audit độc lập) |

## 7. Bước tiếp theo đề xuất

1. Ben quyết các mục 1–6 ở §6; sửa các mục có DOI sai (§6, mục 4) sau khi đối chiếu bản gốc.
2. Audit thủ công 47 mục không DOI và cập nhật `citation-audit.csv` (đổi `VERIFIED_UNAUDITED` thành `VERIFIED`/`BIB_PENDING`/`CONTENT_PENDING`).
3. Chạy lại `quarto render` và `sync_from_source.py --check` trên `main` sau merge.
4. Bật GitHub Pages cho hai repo (hoặc thêm workflow bằng tài khoản có quyền).
5. Bổ sung `docs/specs/*`, `labs/README.md`, `data/README.md`, `references-30-landmark.md` theo plan nếu muốn hoàn thành đủ cây thư mục.
6. Cân nhắc đưa `references/VERIFICATION.md` cùng cập nhật `CHANGES.md` mỗi lần audit.
