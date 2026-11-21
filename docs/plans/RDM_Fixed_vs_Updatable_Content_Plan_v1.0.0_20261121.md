# Tách nội dung chương 1 — Phần cố định và phần cập nhật

**Phiên bản:** 1.1.0
**Áp dụng cho:** `docs/chapters/ch01_overview_and_dmp.md` và làm mẫu cho chương 2–6
**Ngày:** 21/11/2026  
**Người quyết định:** Ben

> Chương cần tách nội dung ít thay đổi (khái niệm, nguyên lý, phương pháp) khỏi nội dung hay thay đổi (pháp luật, mẫu tài trợ, thời hạn, phiên bản chuẩn, công cụ và URL). Thân chương chỉ trỏ tới phụ lục khi khẳng định có thể thay đổi.

## 1. Nguyên tắc tách

| Nội dung cố định | Nội dung cập nhật |
|---|---|
| Khái niệm, định nghĩa, nguyên lý, phương pháp và logic lập luận | Văn bản, phiên bản, mẫu biểu, số liệu, tên công cụ và đường link |
| Rà soát khi khung lý thuyết thay đổi, thường 2–3 năm | Rà soát sáu tháng một lần và ngay khi có văn bản/phiên bản mới |
| Giữ trong thân chương | Đặt trong phụ lục có ngày chốt, trạng thái, URL và ngày kiểm |

**Quy tắc vàng:** sự kiện lịch sử không cần ngày chốt. Một khẳng định có thể hết hạn phải có ngày chốt hoặc trỏ tới phụ lục có ngày chốt. Số minh họa phải được ghi rõ là minh họa, không phải số liệu đo được.

## 2. Phân loại chương 1

### 2.1. Giữ trong thân chương

- Mục tiêu học tập, khái niệm DMP/Protocol/CRF, vòng đời dữ liệu, nguyên lý lỗi thượng nguồn và khung quản trị.
- Ba vai trò Data Steward, maDMP và logic FAIR.
- Sự kiện lịch sử về khủng hoảng tái lập và Surgisphere, với trích dẫn đúng từ bibliography; các khẳng định chưa có bằng chứng giữ cờ kiểm chứng.
- Quiz chỉ hỏi khái niệm và quyết định tương đối ổn định; không hỏi chi tiết pháp lý, phiên bản, thời hạn hoặc con số dễ đổi.

### 2.2. Chuyển sang phụ lục

| Nội dung | Phụ lục | Trạng thái hiện tại |
|---|---|---|
| Căn cứ pháp lý Việt Nam/quốc tế và định hướng chính sách | [`legal`](../appendices/legal.md) | Chỉ mục có trong `docs/legal-verification.md` mới là `VERIFIED`; NQ 72-NQ/TW là định hướng chính sách |
| Mẫu nhà tài trợ và hướng dẫn FAIR | [`funder-templates`](../appendices/funder-templates.md) | NIH pilot bắt buộc từ 25/05/2026; Element 4/6 và giới hạn từ `CONTENT_PENDING` |
| Thời hạn lưu trữ và tiêu hủy | [`retention`](../appendices/retention.md) | Mốc 30/20 năm của TT 33/2025 `CONTENT_PENDING` cho tới khi đọc từng dòng phụ lục |
| Phiên bản chuẩn, vocabulary, công cụ và kho | [`standards`](../appendices/standards.md) | Các phiên bản chưa có bằng chứng đầy đủ giữ `CONTENT_PENDING`/`BIB_PENDING` |

## 3. Quy tắc nội dung cập nhật

### 3.1. NIH DMSP

- Ghi định dạng pilot và ghi rằng định dạng này bắt buộc từ 25/05/2026 theo thông tin đầu vào của đợt rà soát.
- Số mục, giới hạn từ và các giới hạn của Element 4/6 là `CONTENT_PENDING` cho tới khi đối chiếu thông tri gốc.
- NOT-OD-21-014 được mô tả là **cập nhật mẫu**, chưa xác nhận là bị thay thế; NOT-OD-26-100 phải được theo dõi riêng.

### 3.2. Pháp lý và tiêu chuẩn

- TT 13/2025 ghi hiệu lực 21/07/2025 khi dẫn đúng sổ kiểm chứng.
- TT 50/2025, TT 33/2025 và các chi tiết 30/20 năm giữ trạng thái kiểm chứng tương ứng; không suy rộng từ URL chưa có toàn văn chính thức.
- EHDS chỉ ghi các chi tiết đã có trong sổ kiểm chứng. NQ 72-NQ/TW nằm ở mục định hướng chính sách.
- NĐ 13/2023 được ghi là văn bản lịch sử, hết hiệu lực từ 01/01/2026 theo sổ kiểm chứng; khung hiện hành tham chiếu NĐ 356/2025.

### 3.3. Quiz và lab

- Quiz không kiểm tra chi tiết dễ thay đổi; nếu cần kiểm tra cập nhật, câu hỏi phải trỏ tới phụ lục và ghi ngày chốt.
- Lab đọc mẫu, cấu trúc hoặc thời hạn từ phụ lục tại thời điểm thực hành, không sao chép một phiên bản cũ vào thân chương.
- `funder-templates` bao gồm NIH, Horizon Europe và FAIR Cookbook; mỗi mục chưa kiểm chứng giữ trạng thái rõ ràng.

### 3.4. Bibliography

- `ref_001`–`ref_103` là bộ lõi khớp đánh số literature review.
- `ref_104+` là `chapter_only`, liên tục, không làm thay đổi 103 dòng lõi; mọi trích dẫn phải có khóa trong `.bib`.
- `VERIFIED_UNAUDITED` chỉ xác nhận metadata/đường dẫn đã đối chiếu, không xác nhận nội dung khoa học.

## 4. Trạng thái triển khai ch01

- Baseline triển khai: commit `434fb8c`.
- Đợt này cập nhật các DOI chapter-only, thay các cờ Begley/Freedman/Surgisphere khi đã có mục tương ứng, và giữ cờ cho số liệu Surgisphere chưa đối chiếu trực tiếp.
- Danh mục cuối chương phải được rà soát theo `.bib`; các chương 2–6 không thuộc phạm vi chỉnh sửa.

## 5. Cấu trúc và áp dụng

| Chương | Nội dung cố định | Nội dung cập nhật |
|---|---|---|
| Ch. 1 | DMP, vòng đời, quản trị, FAIR, bài học lịch sử | `legal`, `funder-templates`, `retention`, `standards` |
| Ch. 2 | ALCOA+, GCP, RBQM, nguyên lý EDC | ICH E6(R3), TT 50/2025, phiên bản công cụ |
| Ch. 3 | Vai trò CDISC/FHIR/OMOP và logic ánh xạ | Phiên bản chuẩn và vocabulary trong `standards` |
| Ch. 4 | Chiều chất lượng, missing data, khung Kahn | Phiên bản DQD và số liệu công cụ |
| Ch. 5 | Khử định danh, Five Safes, bảo mật | `legal` và `retention` |
| Ch. 6 | FAIR, FAIRification, AI-ready | FAIR Cookbook, DataCite và Horizon Europe |

## 6. Checklist nghiệm thu

- [ ] Thân chương chỉ chứa khẳng định cố định hoặc trỏ tới một slug phụ lục có ngày chốt.
- [ ] Bốn slug `legal`, `funder-templates`, `retention`, `standards` có cột trạng thái, URL và ngày kiểm.
- [ ] NĐ 13/2023 chỉ xuất hiện như văn bản lịch sử; không dùng như khung hiện hành.
- [ ] NIH pilot, ngày bắt buộc 25/05/2026, NOT-OD-21-014, NOT-OD-26-100 và các giới hạn Element 4/6 được ghi đúng trạng thái.
- [ ] TT 13/2025, TT 50/2025, TT 33/2025, EHDS và NQ 72-NQ/TW không bị gắn `VERIFIED` vượt quá sổ kiểm chứng.
- [ ] Quiz không hỏi chi tiết dễ đổi; lab lấy mẫu từ phụ lục.
- [ ] Các khóa `ref_104+` có `chapter_only`, không làm thay đổi bộ lõi 103.
- [ ] `appendices-CHANGELOG.md` ghi thay đổi và ngày kiểm.
