# Harvest thử nghiệm (EXPLORE): chỉ mục các chủ đề

**Ngày chạy:** 2026-11-24 · **Công cụ:** `scripts/lit_harvest.py harvest` · **Cấu hình:** `references/lit_search_config.json` (phiên bản 0.4.1-protocol)

Đây là bước thăm dò để chuẩn bị quy trình biên soạn chuyên khảo; **không phải review đã sàng lọc**. Xem `PROTOCOL.md`. Chỉ metadata; không có tóm tắt.

**Số bản ghi duy nhất trên toàn bộ 17 chủ đề (khử trùng lặp liên chủ đề):** 2675. Tổng theo từng chủ đề không cộng được thành số nghiên cứu độc lập vì các chủ đề chồng lấn.

| Chủ đề | Chương chính | OpenAlex (tổng / lấy) | Semantic Scholar (lấy) | Europe PMC (tổng / lấy) | Sau khử trùng lặp | Từ 2 nguồn | Trong .bib (DOI) | Có thể (tiêu đề) | Lỗi |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| [Quản lý dữ liệu nghiên cứu y sinh](t01-rdm-biomedical.md) | ch01 | 770 / 125 | 25 | 163 / 25 | 156 | 14 | 3 | 0 |  |
| [Kế hoạch quản lý và chia sẻ dữ liệu (DMP, DMSP)](t02-dmp-funder.md) | ch01 | 1586 / 125 | 25 | 122 / 25 | 166 | 8 | 1 | 0 |  |
| [Quản trị dữ liệu và Data Steward](t03-governance-steward.md) | ch01 | 795 / 125 | 25 | 219 / 25 | 165 | 4 | 0 | 0 |  |
| [Khủng hoảng tái lập trong nghiên cứu y sinh](t04-reproducibility.md) | ch01 | 13823 / 125 | 25 | 6311 / 25 | 171 | 3 | 1 | 0 |  |
| [Toàn vẹn dữ liệu, ALCOA+ và giám sát theo rủi ro](t05-data-integrity-rbqm.md) | ch02 | 2659 / 125 | 25 | 1416 / 25 | 163 | 10 | 0 | 0 |  |
| [Thu thập dữ liệu điện tử (EDC, REDCap)](t06-edc-redcap.md) | ch02 | 6258 / 125 | 25 | 4199 / 25 | 160 | 14 | 3 | 0 |  |
| [Chuẩn dữ liệu y tế: CDISC, FHIR, OMOP](t07-standards.md) | ch03 | 9235 / 125 | 25 | 1203 / 25 | 171 | 4 | 3 | 1 |  |
| [Đánh giá chất lượng dữ liệu y tế](t08-data-quality.md) | ch04 | 1569 / 125 | 25 | 339 / 25 | 162 | 10 | 2 | 0 |  |
| [Dữ liệu khuyết và gán đa bội](t09-missing-data.md) | ch04 | 182265 / 125 | 25 | 13598 / 25 | 168 | 5 | 1 | 0 |  |
| [Khử định danh và rủi ro tái định danh](t10-deidentification.md) | ch05 | 25424 / 125 | 25 | 598 / 25 | 174 | 1 | 0 | 0 |  |
| [Môi trường nghiên cứu tin cậy và Five Safes](t11-tre-five-safes.md) | ch05 | 417 / 125 | 25 | 133 / 25 | 150 | 17 | 0 | 0 |  |
| [Bảo vệ dữ liệu cá nhân trong nghiên cứu y sinh (khái quát)](t12-data-protection-law.md) | ch06 | 2326 / 125 | 25 | 864 / 25 | 171 | 3 | 1 | 0 |  |
| [Bảo vệ dữ liệu và hồ sơ y tế ở Việt Nam (kiểm tra độ phủ)](t12b-vietnam-data-protection.md) | ch06 | 279 / 125 | 25 | - / 0 | 137 | 0 | 0 | 0 |  |
| [Đồng ý, đạo đức và chia sẻ dữ liệu y sinh](t13-consent-ethics-sharing.md) | ch06 | 2062 / 125 | 25 | 1393 / 25 | 165 | 8 | 1 | 0 |  |
| [Nguyên tắc FAIR và FAIR hóa](t14-fair.md) | ch07 | 7469 / 125 | 25 | 319 / 25 | 168 | 6 | 3 | 0 |  |
| [Dữ liệu sẵn sàng cho AI trong y sinh](t15-ai-ready.md) | ch07 | 6648 / 125 | 25 | 378 / 25 | 175 | 0 | 1 | 0 |  |
| [Tái lập tính toán và phần mềm nghiên cứu](t16-computational-reproducibility.md) | ch08 | 1997 / 125 | 25 | 772 / 25 | 165 | 8 | 0 | 0 |  |
