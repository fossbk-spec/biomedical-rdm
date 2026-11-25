# Bàn giao để tiếp tục trên máy khác

**Ngày:** 25/11/2026 · **Người nghiệm thu:** TS. Hoàng Quang Huy (Ben)
**Mục đích:** một điểm vào duy nhất để tiếp tục dự án (biến Biomedical RDM thành sách chuyên khảo) mà không phải dựng lại ngữ cảnh. Trạng thái chi tiết hơn: `docs/PROJECT-STATE.md`; nhật ký quyết định: `docs/DECISIONS.md`.

## 1. Đang ở đâu (đối chiếu bằng `git log` và `gh pr list` trước khi dựa vào)

| Hạng mục | Trạng thái |
|---|---|
| Repo gốc `fossbk-spec/biomedical-rdm` | `main` đã gồm: quiz mini-course làm lại (#25), PROJECT-STATE v2.5 (#26), bộ chuẩn biên tập `editorial/` và script `check_structure/glossary/crossrefs` (#27), chương mẫu ch01 (#28), harvest thăm dò và giao thức Gate 1 (#29) |
| Repo web `fossbk-spec/biomedical-rdm-course` | `main` ở `9966bbc`; Pages (`gh-pages`) triển khai từ `9966bbc`; quiz 34 câu hiển thị đủ giải thích, quy tắc đạt 24/34 đã chạy đúng |
| PR mở | Nhánh bàn giao này (nếu chưa merge); không còn PR nào khác |
| Chưa theo dõi trong clone chính (**không nằm trên GitHub, cần chép tay sang máy mới nếu muốn**) | `docs/chapters/rdm-case-study-drmayday-workflow.md`, `rdm-dua-case-study-drmayday-vao-khoa-hoc.md`, `rdm-phu-luc-b-bo-sung-dmptool-templates.md`, `docs/quizzes/` (ngân hàng quiz cũ), `docs/rdm-khoa-hoc-free-self-paced.md`. Case study chờ quyết định về sự đồng ý công bố; chưa đưa vào repo |

## 2. Các quyết định đã chốt

**Ben chốt trực tiếp:** sách chuyên khảo là bản chính, quiz/lab/mini-course là lớp phái sinh; 7 chương hiện có + 2 chương mới (quản trị và pháp lý Việt Nam; tái lập và phần mềm nghiên cứu); chỉ tiếng Việt; có đồng tác giả (bổ sung sau); tách nội dung thành lớp cốt lõi và lớp cập nhật; số câu mini-course giữ 4 mỗi bài (chờ xác nhận lại).

**Quyết định theo ủy quyền của Ben ngày 24–25/11/2026** ("làm theo phương án khoa học và chính xác nhất", "review độc lập rồi quyết định"). Chi tiết và lý do trong `docs/handoff-20261125/`:
- **Q-A, vòng đời 7 giai đoạn** (bản chuẩn của ch01; pháp lý, bảo mật, quản trị, Data Steward là lớp ngang): `03-quy-cach-cu-the.md` mục 1.
- **Q-B, đánh số chương** (điều chỉnh bởi Ben ngày 25/11/2026: giữ FAIR là ch06, tái lập thành ch07, **chuyển Quản trị và pháp lý Việt Nam thành ch08**, tích hợp thành ch09; chỉ `ch07` cũ chuyển sang `ch09`, `ch06` giữ nguyên số và URL).
- **Q-C, ch00 và ch07 cũ thuộc học liệu đi kèm** (`product: companion` trong `chapter-map.yml`): mục 3.
- **Mô hình hai lớp**: Phần cốt lõi + Sổ cập nhật (`updates/*.yml` + `schema.json` + trang sinh tự động; liên kết Markdown chuẩn, không dùng cú pháp neo riêng; chu kỳ rà theo loại: pháp lý 90–180 ngày, mẫu, chuẩn, công cụ, bằng chứng 180 ngày, URL 365 ngày): mục 4.
- **Gate 1 của harvest** (phê duyệt có điều kiện): `docs/literature-review/harvest/PROTOCOL.md` mục 10.
- **Chưa thực hiện bất kỳ quyết định cấu trúc nào ở mã nguồn** (đổi số chương, dựng `updates/`, viết `MONOGRAPH_OUTLINE`): mới là kế hoạch.

## 3. Việc kế tiếp (thứ tự đề xuất, mỗi việc một nhánh và một PR)

1. Ghi các quyết định cấu trúc ở mục 2 vào `docs/DECISIONS.md`; viết `docs/syllabus/MONOGRAPH_OUTLINE_v1.0.0.md` (mục lục chính thức 9 chương, tiên quyết, mục tiêu năng lực cấp chương); cập nhật `editorial/chapter-map.yml` (trường `product`, thứ tự, tiên quyết ch04 → ch03); sửa lời văn vòng đời ở ch00, đề cương và Q1 của quiz tổng hợp.
2. PR riêng đổi số chương (`ch07` cũ → `ch09`, đồng bộ `ch07` Tái lập và `ch08` Pháp lý; `ch06` giữ nguyên) bằng `git mv` cộng script thay thế có `assert`; cập nhật web khóa học (`scripts/sync_manifest.json`, menu VitePress), kèm chuyển hướng URL.
3. Dựng Sổ cập nhật: `updates/`, `schema.json`, `check_updates.py`, sinh trang, mở rộng `check_volatile.py` quét đề cương và mục lục; thử trên ch01 và render cả Quarto lẫn VitePress.
4. Nâng cấp ch03 trước (HL7, LOINC, SNOMED CT, CDISC, OMOP), rồi ch02, ch04, ch05, ch06; mỗi chương một PR theo mẫu ch01 (khung 11 mục, lưu `archive/chNN/`, `editorial/changelog/`).
5. Viết ch07 (tái lập) và ch08 (pháp lý) chỉ sau khi có reviewer ngoài; pháp lý đi từ nguồn chính thống, không từ API học thuật.
6. Harvest Gate 2 (sàng lọc): cần xác nhận mô hình AI độc lập làm người sàng và người duyệt hàng đợi; chưa bắt đầu.
7. Việc Ben cần quyết còn mở: các điểm đã đánh dấu ở ch01 (khối "Luận điểm cần tác giả xác nhận", 5 luận điểm, 4 cạm bẫy, nhãn Cốt lõi/Cập nhật cho bảng bằng chứng); 26 thuật ngữ `vi_status: proposed`; xử lý tệp chưa theo dõi (mục 1); reviewer ngoài (pháp lý, chuẩn dữ liệu, nghiên cứu lâm sàng, khoa học dữ liệu); số câu mini-course và quy tắc 24/34; hình thức xuất bản, DOI.

## 4. Quy tắc làm việc (không đổi)
- Vai trò: người điều phối viết brief và review; bên thực hiện viết mã và nội dung theo brief; Ben quyết định. Chỉ merge khi Ben bảo.
- **Không ghi tên công cụ AI** trong commit, PR, README, tệp repo hay web (đã dọn ở PR #29).
- Mỗi tác vụ một nhánh và một worktree; không làm trên `main`; không đẩy trực tiếp lên `main`.
- Không bịa nguồn, DOI, số hiệu hay ngày; giữ `[CẦN KIỂM CHỨNG]`, `CONTENT_PENDING`, `BIB_PENDING`; kiểm trang không đổi cột `status` của `citation-audit.csv`.
- Mọi kiểm tra: `scripts/check_*.py --check`, `build_bib.py --check`, `audit_references.py` (rồi `git checkout -- references/AUDIT-REPORT.md` nếu bị sinh lại), `git diff --check`; ghi exit code thật.

## 5. Dựng lại môi trường trên máy mới
```bash
git clone git@github.com:fossbk-spec/biomedical-rdm.git
git clone git@github.com:fossbk-spec/biomedical-rdm-course.git   # nếu cần sửa web
# Python 3.12+ (chỉ thư viện chuẩn cho scripts), Quarto, Node (VitePress cho repo web)
export OPENALEX_API_KEY=...            # chỉ cho scripts/lit_harvest.py
export SEMANTIC_SCHOLAR_API_KEY=...    # khóa không được ghi vào tệp hay repo
python scripts/check_structure.py --check   # kiểm tra nền
```
- Đẩy qua SSH (`git@github.com:`); HTTPS dễ treo vì trình quản lý thông tin xác thực.
- Chạy bên thực hiện không tương tác: sandbox cho phép ghi trong worktree riêng, đầu vào rỗng (`< /dev/null`), ghi báo cáo ra tệp; thông báo "hoàn tất" của tác vụ nền có thể đến sớm, hãy chờ tệp báo cáo xuất hiện (Windows Bash không có `pgrep`; dùng vòng `until [ -s <tệp> ]`). Lệnh cụ thể nằm trong ghi chú cục bộ của người điều phối.
- Triển khai web: build từ `main` của repo web, thay nội dung nhánh `gh-pages` bằng thư mục build, commit "deploy: VitePress site <sha>", đẩy; kiểm trang công khai (trình duyệt có thể giữ cache bản cũ).
- Harvest: `python scripts/lit_harvest.py enrich|harvest|seedtest` (Semantic Scholar giới hạn tốc độ nên mất khoảng 10 phút; kết quả ghi trong `docs/literature-review/harvest/`).

## 6. Tài liệu trong `docs/handoff-20261125/`
| Tệp | Nội dung |
|---|---|
| `01-de-xuat-chuyen-khao.md` | Đề xuất biến RDM thành chuyên khảo; quyết định đã chốt (mục 13), mô hình hai lớp (mục 14), tổng hợp review độc lập (mục 15) |
| `02-tham-dinh-muc-luc.md` | Thẩm định mục lục 3 mức (mâu thuẫn vòng đời, NIH 6 so với 7 yếu tố, thứ tự chương); mục lục dự thảo |
| `03-quy-cach-cu-the.md` | Quy cách cụ thể cho Q-A, Q-B, Q-C và Sổ cập nhật; thứ tự PR; tiêu chí reviewer |
| `04-literature-harvest-review.md` | Báo cáo harvest và hệ quả cho quy trình (bản trước khi sửa lần cuối: số liệu mới nhất ở `docs/literature-review/harvest/`) |
| `05-review-doc-lap-de-xuat.md` | Review độc lập các phương án (xác minh phát hiện, phản biện) |
| `06-review-doc-lap-harvest.md` | Review độc lập mã nguồn, chuỗi tìm và giao thức harvest |

Các tệp này là bản sao đã bỏ tên công cụ để lưu trong repo công khai; bản gốc nằm ở thư mục làm việc cục bộ của máy cũ.
