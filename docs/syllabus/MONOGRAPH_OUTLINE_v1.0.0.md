# Mục lục chính thức của sách chuyên khảo Biomedical RDM

**Phiên bản:** 1.1.0 · **Ngày:** 25/11/2026 · **Người nghiệm thu:** TS. Hoàng Quang Huy (Ben)
**Trạng thái:** áp dụng các quyết định cấu trúc đã ghi ngày 25/11/2026 trong `docs/DECISIONS.md` (kể cả điều chỉnh chuyển chương Quản trị và pháp lý Việt Nam sang Chương 8); chờ Ben duyệt khi merge.
**Căn cứ:** `docs/handoff-20261125/02-tham-dinh-muc-luc.md` (mục 6), `docs/handoff-20261125/03-quy-cach-cu-the.md` (mục 1–3), `editorial/chapter-map.yml`, quyết định của Ben ngày 25/11/2026.

Tài liệu này là mục lục chính thức của **sách chuyên khảo**. Đề cương `BIOMEDICAL_RDM_FREE_SELF_PACED_SYLLABUS.md` cùng thư mục là đề cương của **khóa học tự học** (sản phẩm đi kèm), không thay thế tài liệu này.

## 1. Vòng đời dữ liệu dùng chung

Vòng đời dữ liệu nghiên cứu y sinh gồm bảy giai đoạn: (1) Thiết kế và kế hoạch quản lý dữ liệu; (2) Thu thập; (3) Xử lý và làm sạch; (4) Chuẩn hóa; (5) Phân tích và tái lập; (6) FAIR và chia sẻ; (7) Lưu trữ và hủy an toàn. Bốn lớp ngang áp dụng cho mọi giai đoạn: quản trị dữ liệu, bảo mật và quyền riêng tư, pháp lý và đạo đức, vai trò Data Steward.

Lời văn này dùng chung cho sách, đề cương, khóa học và quiz. Bản đồ giai đoạn ↔ chương nằm ở mục 4.2 của chương 1.

## 2. Mục lục

Số chương là **số chính thức**. Cột "Mã hiện tại" là `id` trong `editorial/chapter-map.yml` cho đến khi PR đổi số hoàn tất (`ch06` giữ nguyên số chương; chỉ `ch07` cũ chuyển sang học liệu đi kèm của `ch09`, nhường số `ch07` cho chương mới về Tái lập và `ch08` cho chương mới về Pháp lý).

| Phần | Chương | Mã hiện tại | Vai trò | Trạng thái |
|---|---|---|---|---|
| (Mở đầu) | Lời nói đầu và hướng dẫn đọc | viết mới | khung | cần viết (ch00 hiện là trang M0 của khóa học) |
| I. Nền tảng | 1. Tổng quan RDM, vòng đời và DMP | ch01 | khung | chương mẫu (khung 11 mục) |
| II. Thu thập dữ liệu | 2. Thu thập dữ liệu lâm sàng, ALCOA+ và REDCap | ch02 | thực hành | bản nháp, cần nâng cấp |
| III. Chuẩn và chất lượng | 3. CDISC, FHIR và OMOP | ch03 | chuẩn | bản nháp, cần nâng cấp |
| | 4. Chất lượng dữ liệu và dữ liệu khuyết | ch04 | thực hành | bản nháp, cần nâng cấp |
| IV. Bảo mật, chia sẻ và tái lập | 5. Bảo mật và khử định danh | ch05 | quản trị | bản nháp, cần nâng cấp |
| | 6. FAIR, kho lưu trữ và dữ liệu sẵn sàng cho AI | ch06 | quản trị | bản nháp, cần nâng cấp |
| | 7. Tái lập và phần mềm nghiên cứu | ch07 (`planned`) | thực hành | mới; cần nghiên cứu |
| V. Quản trị và pháp lý | 8. Quản trị và pháp lý Việt Nam | ch08 (`planned`) | quản trị | mới; cần nghiên cứu và reviewer pháp lý |
| VI. Tích hợp | 9. Tích hợp và tổng kết | viết mới (học liệu đi kèm ở `ch09_completion_and_capstone.md`) | khung | cần viết |
| Phụ lục | Mẫu nhà tài trợ, lưu giữ, chuẩn, pháp lý, lab, thuật ngữ, ký hiệu | `docs/appendices/`, `editorial/` | | giữ; sau này chuyển phần dễ lỗi thời sang Sổ cập nhật |

**Thứ tự đọc khuyến nghị:** 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9. Chương 3 đứng trước chương 4 dù giai đoạn 3 đứng trước giai đoạn 4, vì các bộ kiểm tra chất lượng như DQD chạy trên dữ liệu đã theo OMOP CDM. Các chương 5–7 đi liền mạch kỹ thuật–phương pháp quốc tế (bảo mật/khử định danh → FAIR/AI-ready → tái lập tính toán), sau đó Chương 8 đặt khung quản trị và tuân thủ pháp lý Việt Nam ngay trước Chương 9 tích hợp tổng kết (tách nguyên lý cố định ở thân chương và quy định dễ đổi sang Sổ cập nhật).

## 3. Tiên quyết

| Chương | Tiên quyết |
|---|---|
| 1 | không |
| 2 | 1 |
| 3 | 1, 2 |
| 4 | 1, 2, 3 |
| 5 | 1, 2 |
| 6 | 1, 3, 5 |
| 7 | 1, 4, 6 |
| 8 | 5, 6 |
| 9 | 1–8 |

Cột tiên quyết của các chương đang có đã khớp `chapter-map.yml`. Tiên quyết của chương 7 và 8 là dự kiến, theo mục lục; sẽ xác nhận khi viết.

## 4. Phạm vi và mục tiêu năng lực cấp chương

Mục tiêu năng lực chi tiết của các chương đang có nằm ở mục "Mục tiêu học tập" của chính chương và không lặp lại ở đây. Bảng dưới chỉ ghi phạm vi và điểm cần chốt.

| Chương | Phạm vi | Điểm cần chốt |
|---|---|---|
| 1 | Khủng hoảng tái lập, vòng đời, quản trị dữ liệu, Data Steward, DMP/DMSP | Mẫu NIH dạy trong chương (mẫu hiện hành, hoặc cả hai có phân biệt) |
| 2 | ALCOA+, GCP, EDC, REDCap | Chương dài nhất (8.490 từ); xét tách sau khi đọc nội dung |
| 3 | CDISC, FHIR, OMOP và vai trò bổ trợ của từng chuẩn | Phiên bản chuẩn và vocabulary chuyển vào Sổ cập nhật |
| 4 | Khung chất lượng dữ liệu, DQD, dữ liệu khuyết | Số liệu mô tả hiện trạng (số quy tắc DQD) ghi kèm ngày chốt |
| 5 | Bảo mật, khử định danh, khung quốc tế (HIPAA, GDPR, EHDS) | Phần pháp lý Việt Nam (mục 3.2–3.3) chuyển sang chương 8 |
| 6 | FAIR, FAIRification, kho lưu trữ, dữ liệu sẵn sàng cho AI | Công cụ và chỉ số trưởng thành chuyển vào Sổ cập nhật |
| 7 (mới) | Thực hành tái lập tính toán: môi trường, phiên bản, quy trình, mã nguồn | Chương 1 chỉ giữ động lực; chốt phạm vi để không chồng lấp chương 4 và 6 |
| 8 (mới) | Khung pháp lý và quản trị dữ liệu y tế tại Việt Nam | Đi từ văn bản chính thống, không từ API học thuật; tách nguyên lý cố định và Sổ cập nhật; cần reviewer pháp lý |
| 9 (mới) | Một bài toán tích hợp từ thiết kế đến chia sẻ, bám khung vòng đời | Quiz tổng hợp và capstone nằm ở học liệu đi kèm, không ở chương này |

Mục tiêu năng lực cho chương 7, 8, 9 sẽ viết khi chương được lập kế hoạch; chưa đề xuất ở đây để tránh hứa trước nội dung chưa nghiên cứu.

## 5. Sản phẩm sách và sản phẩm đi kèm

Trường `product` trong `editorial/chapter-map.yml`:
- `book`: các chương trong mục lục ở mục 2.
- `companion`: trang M0 của khóa học (ch00 hiện tại), Quiz tổng hợp và Checklist capstone (phần của ch07 hiện tại), mini-course 6 bài.

Các script kiểm quiz, mini-course và đồng bộ web đọc theo trường `product`.

## 6. Việc kế tiếp theo kế hoạch

1. PR riêng đổi số chương (`ch07` cũ sang `ch09` cho học liệu đi kèm, đồng bộ mã `ch07` Tái lập và `ch08` Pháp lý; `ch06` giữ nguyên số chương) cùng cập nhật web khóa học và chuyển hướng URL.
2. Dựng Sổ cập nhật, thử trên chương 1.
3. Nâng cấp lần lượt chương 3, 2, 4, 5, 6 theo mẫu chương 1.
4. Viết chương 7 và 8 sau khi có reviewer ngoài.

Chi tiết và cổng nghiệm thu: `docs/HANDOFF.md` mục 3 và `docs/handoff-20261125/03-quy-cach-cu-the.md` mục 5.
