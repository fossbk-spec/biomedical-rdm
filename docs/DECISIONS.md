# Decision log

## 2026-11-22 — Quy tắc sơ đồ Mermaid

- **Quyết định:** Dùng nguồn Mermaid không HTML ngoài `<br/>`, nhãn gọn, không đưa dữ kiện dễ hết hạn vào nhãn, và trình bày các biện pháp song song khi chúng không phải quy trình tuần tự.
- **Người quyết định:** Ben.
- **Nguồn chân lý:** `docs/guides/diagrams-math-quiz-web.md`.

## 2026-11-22 — Xác nhận các quyết định mặc định và chấp nhận tạm thời các mục chưa kiểm

- **Quyết định:** Ben xác nhận các mặc định đã dùng cho ch02–ch06 và nhóm syllabus (case study ghi "tình huống giả định minh họa"; lab giữ trong cùng file với chương; không dùng số hay khẳng định chưa đọc được ở nguồn; quiz tổng hợp là câu khái niệm không dạy dữ kiện có ngày; capstone là tình huống giả định không dùng tên dự án thật). Các mục `CONTENT_PENDING` được chấp nhận tạm thời.
- **Người quyết định:** Ben.
- **Chi tiết:** PR #5 của hai repo đã đóng vì bị thay thế (PR #15 và cơ chế đồng bộ mới). Các nhánh `fix/…`, `feat/…`, `docs/…` đã merge của PR #7–#16 đã được xóa.

## 2026-11-21 — Khóa học miễn phí tự học: syllabus, M0, trang cuối khóa

- **Người quyết định:** Ben.
- **Quyết định mặc định tạm thời:** Dùng syllabus tự học, M0 và trang cuối khóa mới; bản v2.0.0 được thay và giữ trong lịch sử git. Quiz cuối gồm 10 câu khái niệm, không dạy dữ kiện pháp lý phụ thuộc ngày; capstone dùng tình huống giả định, không dùng tên dự án thật.
- **Trạng thái:** `CONTENT_PENDING` cho quiz 4 câu theo bài trên site khóa học; việc đối chiếu và tích hợp vào từng chương trong repo gốc chưa hoàn tất.

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
- `citation-audit.csv` thêm cột `page_check`, `page_check_note` (chỉ để tham khảo). **Cột `status` không đổi** do kiểm tra trang: kết quả này không đủ căn cứ để đổi trạng thái theo định nghĩa ở trên. Chỉ trang HTML được đối chiếu; PDF và trang chặn truy cập là `NOT_CHECKED` (script không trích xuất PDF). Sửa sau review của Codex: regex lọc script/style, chặn URL không phải http(s) hoặc IP nội bộ, điền `found_url`.
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

## 2026-11-21 — Tách nội dung cố định/cập nhật cho chương 4 và 6

- **Quyết định tạm thời:** Giữ trong thân chương các khái niệm ổn định về chất lượng dữ liệu, Rubin/MICE, FAIR, RO-Crate và Patient-Level Split; chuyển URL, trạng thái nguồn, phiên bản chuẩn và kết quả chạy lab vào phụ lục.
- **Case study/lab:** dùng tình huống minh họa; giữ lab trong chương; dữ liệu Lab 5 không được xem là đạt HIPAA Safe Harbor và không được đăng công khai trước khi kiểm tra tái định danh.
- **Giới hạn:** số DQD, tỷ lệ Q-01–Q-05 và ngưỡng Pass Rate trong chương chỉ là minh họa; `ref_043`/`ref_072` là preprint, `ref_003`/`ref_030` là `BIB_PENDING`, và `ref_011` là *Our Journey* (2025). Các nội dung chưa có bằng chứng giữ `CONTENT_PENDING`/`[CẦN KIỂM CHỨNG]`.

## 2026-11-22 — Gộp nhánh chương vào main: quy tắc audit trang nguồn

- Khi gộp PR #6 với `main` (đã có PR #21), giữ quy tắc của `main`: script và kết quả audit trang là `scripts/audit_nodoi_gemini.py` / `references/audit-nodoi-gemini.csv`; **cột `status` trong `citation-audit.csv` không đổi do kết quả đối chiếu trang** (chỉ cột `page_check`/`page_check_note`, để tham khảo).
- Bỏ lần chạy riêng trên nhánh chương (đổi tên sang `audit_nodoi_pages.py` và chuyển 6 mục PARTIAL sang `BIB_PENDING`) vì mâu thuẫn với quy tắc trên. **Người quyết định:** Ben.

## 2026-11-22 — Quiz theo chương: số câu theo nội dung; quy tắc tự đánh giá theo tỷ lệ

- **Người quyết định:** Ben.
- **Quyết định:** Quiz được tích hợp vào từng chương với số câu theo các phần lý thuyết chính, không cố định một số câu cho mọi chương; quiz tổng hợp giữ 10 câu.
- **Quy tắc tự đánh giá:** Tổng số câu là tổng số câu của sáu chương cộng 10 câu tổng hợp; mục tiêu là đúng ít nhất 70% tổng số câu và đúng ít nhất 2/3 câu Q1–Q3 của quiz tổng hợp. Đây là tự đánh giá, không ai ghi lại kết quả; làm lại không giới hạn.

## 2026-11-22 — Mini-course quiz theo cùng quy tắc

- Giữ 4 câu cho mỗi bài mini-course (3 câu khái niệm và 1 câu tình huống), tổng 24 câu; quiz tổng hợp giữ 10 câu.
- Mọi câu mini-course phải có giải thích đúng chủ đề cùng dòng với đáp án; không dùng dòng `- **Giải thích:**` riêng.
- Dùng cùng ngưỡng chống lộ đáp án: phân bố A/B/C/D của 24 câu là 6/6/6/6, mỗi bài dùng ít nhất ba chữ cái, tỷ lệ độ dài và từ tuyệt đối được script kiểm.
- Quy tắc tự đánh giá của mini-course vẫn là 24/34 và chờ Ben xác nhận số câu.
## 2026-11-24 — Quyết định vận hành cho Giai đoạn 1 chuyên khảo

- **Nguồn chân lý:** Sách chuyên khảo là bản chính; quiz, lab và mini-course là lớp phái sinh.
- **Phạm vi:** Giữ bảy chương hiện có và đăng ký hai chương mới `planned`: Quản trị và pháp lý Việt Nam; Tái lập và phần mềm nghiên cứu. Chỉ tiếng Việt; thuật ngữ Anh ghi lần đầu và quản lý trong `editorial/glossary.yml`.
- **Đồng tác giả:** Chưa dựng `CODEOWNERS`; `owner: null`, `reviewers: []`; luồng đa tác giả chưa áp dụng cho đến khi có danh sách đồng tác giả.
- **Bộ chuẩn và kiểm tra:** Tạo `editorial/` và ba script `check_structure.py`, `check_glossary.py`, `check_crossrefs.py`. Quy tắc chắc chắn là `FAIL`; quy tắc chưa chắc chắn hoặc phản ánh hiện trạng chương là `WARN`, không sửa chương trong GĐ1.
- **Bốn trạng thái:** Script phải báo Đạt, Không đạt, Chưa kiểm tra, Không áp dụng; không ghi Đạt khi chưa chạy. `citation-audit.csv` giữ nguyên cột `status`; script mới không đọc/sửa CSV.

## 2026-11-24 — Thử khung 11 mục trên Chương 1 (điểm cần Ben duyệt)

- **Quyết định làm việc:** Dùng Chương 1 làm chương mẫu GĐ2; tổ chức nội dung theo 11 mục của đề xuất, không sửa chương khác và chưa đồng bộ mini-course.
- **Giữ nguyên:** nội dung kỹ thuật, Surgisphere, Lab 1, quiz 5 câu và danh mục tham khảo; thêm archive và changelog để truy vết.
- **Bổ sung:** mục phạm vi, luận điểm cần tác giả xác nhận, bảng bằng chứng và mục giới hạn; bảng bằng chứng ghi `chưa đối chiếu` cho phạm vi đã đọc và trạng thái đối chiếu.
- **Cần Ben duyệt:** khung 11 mục có phù hợp với các chương còn lại không; luận điểm trung tâm về khung quản trị dữ liệu cho bối cảnh Việt Nam; các nhận định pending và bảng bằng chứng trước GĐ3/GĐ4.

## 2026-11-24 — Chuẩn hóa sau review GĐ1 (Ben chọn "theo gói đề xuất")

- **Đánh số hình/bảng theo chương** (`Hình C.k`, không tiểu hình `a`/`b`). Đã đổi 9 caption hình trong ch01, ch02, ch03, ch05; không nơi nào trong thân sách, mini-course, phụ lục hay guide dẫn "Hình N" nên không gãy tham chiếu. `check_structure.py` kiểm số chương và thứ tự; caption không có dẫn chiếu trong thân vẫn là `WARN` (xử lý ở GĐ3).
- **`notation.md` chỉ giữ ký hiệu có thật trong chương** (`k`, `m`, `θ̂ᵢ`, `θ̄`, `V̂ᵢ`, `Ū`, `B`, `T`). Đã bỏ `ℓ` và `ε` vì không xuất hiện trong thân bảy chương (bản v1.0.0 ghi sai), cùng các chữ cái chung và thông số lab.
- **`glossary.yml` có `vi_status`** (`established` 48, `proposed` 26, `keep-english` 14). Phân loại là đề xuất, Ben chưa rà; `check_glossary.py` cảnh báo số mục `proposed`.
- **Tên gọi "Chương N"** cho sách chuyên khảo: đổi `title` front matter của ch04 và ch06 từ "Bài N" sang "Chương N". Tên "Bài N" chỉ dùng cho mini-course. Tiêu đề ch04 và ch06 vẫn ở front matter (không có H1 trong thân), `check_structure.py` cảnh báo để thống nhất sau.

## 2026-11-24 — Gate 1 của harvest thăm dò (phê duyệt có điều kiện)

- Giao thức: `docs/literature-review/harvest/PROTOCOL.md` v1.0.0; quyết định G1-1…G1-7 ghi ở mục 10 của giao thức (thêm Europe PMC; tiêu chí nhận/loại có định nghĩa; thiết kế sàng lọc một mô hình AI độc lập cộng người duyệt, không gọi là sàng lọc kép; truy xuất toàn bộ nếu ≤ 200 hoặc top 25 cộng mẫu ngẫu nhiên có seed; điều kiện dừng theo độ nhạy ≥ 80%).
- Độ nhạy hiện tại theo seed test: 19/24 mẫu duy nhất (79%), dưới ngưỡng 80% một mẫu; các mẫu bị bỏ sót có lý do giải thích được (xem `SEED_TEST.md`), không chỉnh thêm chuỗi để tránh quá khớp; bù bằng truy vết trích dẫn ở Gate 2.
- Gate 2 (sàng lọc) chưa thực hiện; không bản ghi nào được thêm vào `references.bib`.
- Ghi chú vệ sinh: đã bỏ hai chỗ ghi công công cụ AI trong `editorial/style-guide.md` và `docs/DECISIONS.md`.

## 2026-11-25 — Quyết định cấu trúc chuyên khảo (theo ủy quyền của Ben, sau review độc lập)

Cơ sở và lý do: `docs/handoff-20261125/` (đề xuất, thẩm định mục lục, quy cách cụ thể, hai review độc lập). Chưa thực hiện ở mã nguồn; mỗi việc là một PR riêng.
- **Vòng đời:** bảy giai đoạn theo bản ch01 (Thiết kế và DMP; Thu thập; Xử lý và làm sạch; Chuẩn hóa; Phân tích và tái lập; FAIR và chia sẻ; Lưu trữ và hủy an toàn); quản trị, bảo mật, pháp lý và đạo đức, Data Steward là lớp ngang. Sửa ch00, đề cương và Q1 quiz tổng hợp cho khớp.
- **Đánh số chương:** ch06 quản trị và pháp lý Việt Nam (mới), ch07 FAIR và AI-ready (ch06 cũ), ch08 tái lập và phần mềm nghiên cứu (mới), ch09 tích hợp và tổng kết (ch07 cũ, tách quiz và capstone sang học liệu đi kèm). Một PR riêng, trước khi nâng cấp chương nào khác.
- **Trường `product: book | companion`** trong `editorial/chapter-map.yml`.
- **Hai lớp nội dung:** Phần cốt lõi + Sổ cập nhật (`updates/` gồm `legal`, `funder`, `standards`, `evidence`, `links` dạng YAML, `schema.json`, trang sinh tự động); liên kết Markdown chuẩn tới neo trong trang sinh, không dùng cú pháp neo riêng; chu kỳ rà theo loại; bản in kèm ngày cắt, commit, manifest và DOI của artifact. Thử đầy đủ trên ch01 trước khi mở rộng.
- **Không đặt mục tiêu "không còn `CONTENT_PENDING`"**; mục tiêu là mọi mục pending được giải quyết hoặc ghi rõ trong phần giới hạn kèm lý do.

## 2026-11-25 — Thực hiện bước 1: lời văn vòng đời, mục lục chính thức, bản đồ chương

- **Lời văn vòng đời bảy giai đoạn** áp dụng cho `ch00`, đề cương, mục 4.2 của `ch01`, nguồn mini-course (`docs/course-source/`) và Quiz tổng hợp Q1. Bảng "7 bước ↔ 6 giai đoạn trong review §2.1" của mini-course được thay bằng bảng giai đoạn ↔ bài học; bản tổng hợp literature review giữ nguyên sáu giai đoạn của riêng nó.
- **Quiz tổng hợp Q1** xếp sáu mục (thêm "Xử lý và làm sạch"), đáp án vẫn là A nên phân bố đáp án không đổi. Giai đoạn "Phân tích và tái lập" không đưa vào vì mini-course không có bài riêng cho giai đoạn này.
- **`docs/syllabus/MONOGRAPH_OUTLINE_v1.0.0.md`** là mục lục chính thức của sách (9 chương, tiên quyết, phạm vi). Đề cương tự học giữ làm tài liệu của khóa học.
- **`editorial/chapter-map.yml` v1.1.0:** thêm `product` và `target_id`, thêm ch00, tiên quyết của ch04 thêm ch03. Chưa đổi `id` hay tên tệp (PR riêng).
- **Việc kế tiếp bắt buộc:** đồng bộ web khóa học từ nguồn mini-course (sync PR ở `biomedical-rdm-course`), vì Q1 và M0 đã đổi.

## 2026-11-25 — Điều chỉnh đánh số chương: chuyển Quản trị và pháp lý Việt Nam sang Chương 8

- **Người quyết định:** Ben (25/11/2026).
- **Quyết định:** Chuyển chương mới **Quản trị và pháp lý Việt Nam** từ vị trí dự kiến Chương 6 sang **Chương 8** (ngay trước Chương 9 Tích hợp và tổng kết), giữ liền mạch mạch kỹ thuật–phương pháp quốc tế ở các chương 5–7 và áp dụng mô hình hai lớp (nguyên lý quản trị ở thân Chương 8; số hiệu, điều khoản và thời hạn vào Sổ cập nhật).
- **Đánh số chính thức sau điều chỉnh:** Chương 5 Bảo mật và khử định danh; **Chương 6** FAIR, kho lưu trữ và dữ liệu sẵn sàng cho AI (`ch06` giữ nguyên số); **Chương 7** Tái lập và phần mềm nghiên cứu (mới, `ch09` trong `chapter-map.yml` hiện tại); **Chương 8** Quản trị và pháp lý Việt Nam (mới, `ch08`); **Chương 9** Tích hợp và tổng kết (mới, thay vai trò sách của `ch07` cũ).
- **Hệ quả triển khai:** `ch06` không phải đổi tên tệp hay chuyển hướng URL công khai trên web khóa học; PR đổi số ở bước 2 chỉ chuyển `ch07` cũ sang `ch09` (học liệu đi kèm) và mở đường cho `ch07` mới. Đã cập nhật `MONOGRAPH_OUTLINE_v1.0.0.md` (v1.1.0), `editorial/chapter-map.yml` và bảng ánh xạ mục 4.2 của `ch01`.

## 2026-11-26 — Đối chiếu số liệu ref_103 với tóm tắt

- Số liệu ở Phụ lục A khớp tóm tắt bài Lane 2020 (PMID 32864627); mô tả được sửa để không gợi ý "an toàn" khi bài báo cáo tăng nguy cơ tim mạch. Phạm vi đã đọc: tóm tắt. Trạng thái `VERIFIED_UNAUDITED` của ref_103 không đổi; mô tả "OHDSI Study-a-thon" chưa đối chiếu.

## 2026-11-26 — Literature review P0: giao thức v1.1 và bản kê nhận định ch03 (dự thảo)

- **Ben duyệt Gate 1 v1.1, bốn câu hỏi RQ3.1 đến RQ3.4 và bản kê ch03 (26/11/2026).** Ben duyệt các lựa chọn: scoping review PRISMA-ScR kèm sổ nguồn chính thống; đăng ký OSF trước Gate 2; thứ tự ch03, ch02, ch04, ch05, ch06 (FAIR), rồi ch07 và ch08; sàng lọc bằng hai AI độc lập, mô hình phân xử và người duyệt.
- Giao thức cập nhật ở `docs/literature-review/harvest/PROTOCOL.md` mục 12; bản kê nhận định ch03 ở `docs/literature-review/claims/ch03-claims.md` (34 nhận định, 17 ưu tiên A, 27 chưa có trích dẫn).
- **Phân xử bất đồng giữa hai mô hình sàng lọc do người duyệt xử lý** (không dùng mô hình AI), vì G1-3 đòi độc lập với người soạn chuỗi tìm và không thể bảo đảm điều đó cho Claude. Ngoại lệ cần Ben đồng ý bằng văn bản. Chưa đăng ký OSF, chưa chạy Gate 2.

## 2026-11-26 — Gắn nhãn minh họa cho hai case study của ch03

- Ben duyệt (26/11/2026) PR nhỏ chỉ gắn nhãn "Tình huống giả định minh họa" cho hai case study ở mục 4 của ch03 (C3-32, C3-33). Các khẳng định mạnh C3-03, C3-16, C3-34 giữ nguyên chờ nguồn.
