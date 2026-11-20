# Kế hoạch triển khai repo và mini-course Quản lý dữ liệu nghiên cứu y sinh

**Phiên bản:** 1.0.0  
**Ngày lập:** 20/11/2026  
**Thời gian thực hiện:** 23/11–04/12/2026, 10 ngày làm việc  
**Đơn vị triển khai:** Claude  
**Người nghiệm thu:** TS. Hoàng Quang Huy (Ben)  
**Repo dự kiến:** `fossbk-spec/biomedical-rdm`  

## 1. Mục tiêu và phạm vi

Tạo một repo công khai chứa:

1. Bản tổng hợp literature review về quản lý dữ liệu nghiên cứu y sinh.
2. Mini-course tiếng Việt gồm 6 bài lý thuyết, 24 câu quiz theo bài và 10 câu quiz tổng hợp.
3. Website Quarto có thể render và triển khai bằng GitHub Pages.
4. Tài liệu quản trị tối thiểu để duy trì, kiểm thử và cập nhật nội dung.

Đợt này không xây lab thực hành, video, peer review, capstone, chứng nhận, hệ thống tài khoản hay cơ chế lưu số lần làm quiz. Các nội dung đó chỉ được ghi trong roadmap.

## 2. Các quyết định đã chốt

Claude thực hiện theo các quyết định sau, không tự thay đổi:

- `tong-hop-literature-review-rdm-y-sinh.md` là bản tổng hợp chính để xuất bản.
- Hai file `Literature_Review*.md` chỉ là tài liệu nền/bản nháp; không xuất bản như các tổng quan độc lập.
- File `rdm-mini-course-ly-thuyet-quiz.md` là nguồn nội dung khóa học.
- Module M0 là phần nhập môn và hướng dẫn học, không có quiz trong đợt này.
- M1–M6 giữ nguyên 4 câu mỗi bài; quiz tổng hợp giữ nguyên 10 câu. Tổng cộng 34 câu.
- Điểm đạt toàn khóa là tối thiểu 24/34. Đồng thời học viên phải trả lời đúng ít nhất 2/3 câu Q1–Q3 của quiz tổng hợp.
- Giới hạn hai lần làm quiz tổng hợp chỉ là hướng dẫn tự học; site tĩnh chưa cưỡng chế được giới hạn này.
- Bảo mật, đạo đức và pháp lý được trình bày là lớp kiểm soát xuyên suốt toàn bộ vòng đời dữ liệu, dù vẫn có một module chuyên đề riêng.
- Không có dữ liệu bệnh nhân thật, thông tin định danh hoặc khóa bí mật trong repo.
- Không push trực tiếp vào `main`; mọi thay đổi đi qua branch và pull request.
- Không merge PR nếu chưa có Ben duyệt.

## 3. Điều kiện đầu vào

### 3.1. Bắt buộc để bắt đầu

- `tong-hop-literature-review-rdm-y-sinh.md`.
- `rdm-mini-course-ly-thuyet-quiz.md`.
- File kế hoạch này.
- Quyền tạo branch, commit và mở PR trong tài khoản `fossbk-spec`.

### 3.2. Bắt buộc trước khi hoàn thành Giai đoạn 1

- Danh mục APA 334 mục.
- Bảng 30 tài liệu landmark, nếu không dùng trực tiếp Phụ lục A của bản tổng hợp.
- Quyền hoặc phương án cấu hình GitHub Pages.

Nếu thiếu danh mục APA 334 mục, Claude vẫn được tạo skeleton và xử lý mini-course, nhưng phải ghi trạng thái `BLOCKED_INPUT` trong `docs/DECISIONS.md`. Claude không được tự tái tạo 334 mục từ trí nhớ và không được tuyên bố Giai đoạn 1 hoàn thành.

## 4. Quy tắc kiểm chứng tài liệu

Mỗi tài liệu tham khảo thuộc một trong ba trạng thái:

| Trạng thái | Ý nghĩa | Cách xử lý |
|---|---|---|
| `VERIFIED` | Nội dung và trường thư mục cần thiết đã xác minh | Có thể trích dẫn và xuất bản |
| `BIB_PENDING` | Nội dung chính đã xác minh nhưng còn thiếu một trường thư mục | Có thể giữ trong bản nháp với cảnh báo; không coi là hoàn thiện |
| `CONTENT_PENDING` | Khẳng định hoặc nguồn gốc chưa xác minh | Không dùng làm căn cứ; đưa vào danh sách cần xử lý |

Claude phải tạo `references/citation-audit.csv` với tối thiểu các cột: `source_number`, `citation_key`, `status`, `missing_field`, `used_in`, `action`.

Không được xóa cờ `[CẦN KIỂM CHỨNG]` nếu chưa có bằng chứng đối chiếu. Không dùng mục 196 và 241 của danh mục gốc cho đến khi kiểm chứng lại.

## 5. Kế hoạch 10 ngày làm việc

| Ngày | Mốc | Công việc chính | Đầu ra bắt buộc | Điều kiện hoàn thành |
|---|---|---|---|---|
| **23/11** | D1 — Khởi tạo và kiểm kê | Kiểm tra quyền repo; tạo branch; kiểm kê tất cả nguồn; ghi thiếu hụt và mâu thuẫn | `docs/DECISIONS.md`, `docs/INPUT-INVENTORY.md`, cây thư mục ban đầu | Mỗi đầu vào có trạng thái `AVAILABLE`, `MISSING` hoặc `BLOCKED` |
| **24/11** | D2 — Skeleton và quản trị | Tạo README, giấy phép CC BY 4.0/MIT, CONTRIBUTING, DATA-USE; cấu hình Quarto tối thiểu | Skeleton repo render được trang chủ | Không có dữ liệu thật, secret hoặc link nội bộ hỏng |
| **25/11** | D3 — Chuẩn hóa literature review | Đưa bản tổng hợp chính vào repo; tách metadata; đánh dấu bản nháp; lập CHANGES | `docs/literature-review/index.md`, `CHANGES.md` | Bản xuất bản khớp nguồn, ngoài các thay đổi có ghi log |
| **26/11** | D4 — Audit trích dẫn | Lập ánh xạ 103 mục, tạo citation key và BibTeX; phân loại ba trạng thái | `references/references.bib`, `references/citation-audit.csv` | Đủ 103 dòng audit; mọi mục pending có hành động cụ thể |
| **27/11** | D5 — Khung khóa học | Tạo M0, trang chủ, syllabus, workflow bảy bước và glossary | `course/index.md`, `syllabus.md`, M0, `glossary.md` | M0 không thêm quiz; thang điểm và đối tượng học rõ ràng |
| **30/11** | D6 — Module 1–3 | Chuyển Bài 1–3 và 12 câu quiz sang cấu trúc module | M1–M3 và quiz tương ứng | Nội dung, đáp án, giải thích khớp nguồn |
| **01/12** | D7 — Module 4–6 | Chuyển Bài 4–6 và 12 câu quiz; thể hiện lớp kiểm soát pháp lý xuyên suốt | M4–M6 và quiz tương ứng | Đủ 24 câu theo bài, không tự thêm câu mới |
| **02/12** | D8 — Quiz cuối và UX | Chuyển 10 câu cuối khóa; hoàn thiện điều hướng, trang lab/data roadmap | `final-quiz.md`, `labs/README.md`, `data/README.md` | Tổng đúng 34 câu; điều kiện đạt là 24/34 và đúng ≥2/3 Q1–Q3 |
| **03/12** | D9 — Kiểm thử | Render Quarto; kiểm tra link, trích dẫn, nội dung, bảo mật và cấu trúc | Báo cáo trong `docs/specs/test-plan.md` | Không lỗi render; link nội bộ đạt 100%; không có secret/PII |
| **04/12** | D10 — Bàn giao | Sửa lỗi còn lại; commit; push branch; mở PR; chuẩn bị báo cáo nghiệm thu | PR, checklist, link preview/Pages nếu có | PR có mô tả, giới hạn, mục chưa đạt và hướng xử lý; chưa merge |

## 6. Các cổng kiểm soát

### Gate A — cuối ngày 24/11

Chỉ tiếp tục phần xuất bản literature review khi:

- Nguồn chính được xác định rõ.
- Danh mục APA 334 mục đã có, hoặc thiếu hụt đã được ghi `BLOCKED_INPUT`.
- Repo không chứa dữ liệu bệnh nhân thật hoặc secret.

Nếu thiếu danh mục 334 mục, Claude tiếp tục phần mini-course song song và giữ phần danh mục ở trạng thái chưa nghiệm thu.

### Gate B — cuối ngày 27/11

Chỉ coi nội dung khoa học sẵn sàng tích hợp khi:

- 103 mục có dòng audit tương ứng.
- Các mục `CONTENT_PENDING` không được dùng làm căn cứ.
- Tất cả thay đổi so với nguồn có trong `CHANGES.md`.

### Gate C — cuối ngày 02/12

Khóa học đạt điều kiện kiểm thử khi:

- Có M0 và 6 bài học M1–M6.
- Có đúng 24 câu theo bài và 10 câu tổng hợp.
- Không có quiz M0.
- Không thêm hoặc viết lại khẳng định khoa học ngoài nguồn nếu chưa ghi quyết định.

### Gate D — ngày 04/12

Chỉ mở PR bàn giao khi:

- Quarto render không lỗi.
- Link nội bộ hoạt động 100%.
- Không phát hiện PII, dữ liệu bệnh nhân thật hoặc secret.
- Checklist ghi rõ mục đạt, chưa đạt, bị chặn và bằng chứng kiểm tra.

## 7. Cấu trúc repo tối giản

```text
biomedical-rdm/
├── README.md
├── LICENSE
├── LICENSE-CODE
├── CONTRIBUTING.md
├── _quarto.yml
├── docs/
│   ├── INPUT-INVENTORY.md
│   ├── DECISIONS.md
│   ├── DATA-USE.md
│   ├── literature-review/
│   │   ├── index.md
│   │   ├── references-334-apa.md
│   │   ├── references-30-landmark.md
│   │   └── CHANGES.md
│   └── specs/
│       ├── requirements.md
│       ├── architecture.md
│       ├── test-plan.md
│       ├── deployment.md
│       └── revision-guide.md
├── course/
│   ├── index.md
│   ├── syllabus.md
│   ├── module-0-intro/index.md
│   ├── module-1-dmp/{index.md,quiz.md}
│   ├── module-2-collection/{index.md,quiz.md}
│   ├── module-3-standards/{index.md,quiz.md}
│   ├── module-4-quality/{index.md,quiz.md}
│   ├── module-5-fair/{index.md,quiz.md}
│   ├── module-6-privacy-ai/{index.md,quiz.md}
│   ├── final-quiz.md
│   └── glossary.md
├── references/
│   ├── references.bib
│   └── citation-audit.csv
├── labs/README.md
└── data/README.md
```

Năm tài liệu đặc tả gọn ở trên thay cho bảy tài liệu SRS/SAD/SDD/UX riêng biệt. Mục tiêu là đủ quản trị và nghiệm thu, tránh tạo tài liệu trùng lặp cho một mini-course tĩnh.

## 8. Tiêu chí nghiệm thu cuối sprint

### Nội dung

- Bản tổng hợp chính được xuất bản và có log thay đổi.
- Các bản review ngắn được đánh dấu là tài liệu nền hoặc không đưa vào site.
- M0 và M1–M6 đầy đủ.
- Có đúng 34 câu; đáp án và giải thích khớp nguồn.
- Glossary có ít nhất 20 thuật ngữ.

### Tài liệu tham khảo

- Có audit cho toàn bộ 103 mục của bản tổng hợp.
- Không có `CONTENT_PENDING` được dùng làm căn cứ.
- Danh mục 334 mục giữ đúng số thứ tự nếu đã được cung cấp.
- Các trường chưa kiểm chứng còn nguyên cảnh báo.

### Kỹ thuật

- `quarto render` thành công.
- Tất cả link nội bộ hoạt động.
- Link ngoài được kiểm tra và ghi ngày kiểm tra.
- Không có PII, dữ liệu bệnh nhân thật hoặc secret.
- Repo có giấy phép phù hợp cho nội dung và code.

### Quy trình

- Mọi quyết định và ngoại lệ được ghi trong `DECISIONS.md`.
- Không push trực tiếp vào `main`.
- Có PR để Ben review; không tự merge.

## 9. Xử lý chậm tiến độ

Ưu tiên công việc theo thứ tự:

1. Tính đúng khoa học và trạng thái kiểm chứng.
2. Mini-course đủ nội dung và đúng 34 câu.
3. Render, link và an toàn dữ liệu.
4. Trang trí giao diện và tài liệu bổ trợ.

Nếu bị chậm, không cắt bước audit nguồn hoặc kiểm thử an toàn. Có thể hoãn giao diện nâng cao, bảng landmark riêng hoặc tối ưu SEO sang sprint sau. Mọi hạng mục hoãn phải ghi chủ sở hữu, lý do và ngày dự kiến trong `docs/DECISIONS.md`.

## 10. Báo cáo Claude phải gửi khi bàn giao

Claude báo cáo theo đúng mẫu:

1. URL repo, branch và PR.
2. URL preview hoặc GitHub Pages, nếu đã có quyền triển khai.
3. Số file tạo/sửa; số module; số câu quiz.
4. Kết quả Gate A–D: `PASS`, `PARTIAL`, `BLOCKED`.
5. Danh sách tài liệu `BIB_PENDING` và `CONTENT_PENDING`.
6. Các mục chưa hoàn thành, nguyên nhân, người cần xử lý và thời hạn đề xuất.
7. Xác nhận chưa merge PR và đang chờ Ben duyệt.

## 11. Prompt giao trực tiếp cho Claude

> Thực hiện kế hoạch trong file `RDM_Claude_Implementation_Plan_v1.0.0_20261120.md` theo lịch 23/11–04/12/2026. Đọc toàn bộ file trước khi sửa repo. Trước tiên kiểm kê nguồn và ghi `docs/INPUT-INVENTORY.md`; không tái tạo tài liệu còn thiếu từ trí nhớ. Dùng `tong-hop-literature-review-rdm-y-sinh.md` làm bản tổng hợp chính và `rdm-mini-course-ly-thuyet-quiz.md` làm nguồn khóa học. M0 không có quiz; M1–M6 có 24 câu và quiz tổng hợp có 10 câu, tổng 34 câu. Phân loại trích dẫn thành `VERIFIED`, `BIB_PENDING`, `CONTENT_PENDING`; không dùng `CONTENT_PENDING` làm căn cứ. Thực hiện theo Gate A–D, ghi mọi ngoại lệ vào `docs/DECISIONS.md`, chạy kiểm thử trước khi bàn giao. Làm việc trên branch riêng, mở PR và không merge trước khi Ben duyệt. Cuối mỗi ngày cập nhật ngắn: việc đã làm, bằng chứng kiểm tra, blocker và công việc ngày tiếp theo.

