---
id: ch04-blacketer2021-data-quality-dashboard
citekey: blacketer2021increasing
title: "Increasing trust in real-world evidence through evaluation of observational data quality"
type: SoTA Paper
chapter: ch04
year: 2021
doi: 10.1093/jamia/ocab132
openalex_id: https://openalex.org/W3183148060
semantic_scholar_id: fa827debc8b2ed9ff0b93f73a4ca5223e505defd
citations:
  openalex: 147
  semantic_scholar: 98
  influential: 5
tags: ["Data quality", "Computer science", "Observational study", "Standardization", "Data science", "Quality (philosophy)", "Automatic summarization", "Data mining"]
date_reviewed: 2026-11-25
---

# Hồ sơ Thẩm định Tài liệu: Increasing trust in real-world evidence through evaluation of observational data quality

> **Phân loại:** SoTA Paper · **Chương áp dụng:** [Chương 4: Chất lượng dữ liệu và dữ liệu khuyết](file:///d:/Antigravity/biomedical-rdm/docs/chapters/ch04_*.md)  
> **Vai trò trong chuyên khảo:** Công trình công bố công cụ tự động hóa Data Quality Dashboard (DQD) của OHDSI, hiện thực hóa Khung Kahn thành hơn 3.300 phép kiểm tra SQL tự động.

---

## 1. Siêu dữ liệu Học thuật (Academic Metadata)

| Thuộc tính | Chi tiết xác thực từ API |
|---|---|
| **Tác giả (Authors)** | Clair Blacketer, Frank DeFalco, Patrick B. Ryan, Peter R. Rijnbeek |
| **Năm xuất bản (Year)** | 2021 |
| **Nhà xuất bản / Tạp chí (Venue)** | Journal of the American Medical Informatics Association |
| **DOI** | [10.1093/jamia/ocab132](https://doi.org/10.1093/jamia/ocab132) |
| **OpenAlex ID** | [https://openalex.org/W3183148060](https://openalex.org/W3183148060) |
| **Semantic Scholar ID** | [fa827debc8b2ed9ff0b93f73a4ca5223e505defd](https://www.semanticscholar.org/paper/fa827debc8b2ed9ff0b93f73a4ca5223e505defd) |
| **Số lượt trích dẫn OpenAlex** | **147** trích dẫn |
| **Số lượt trích dẫn Semantic Scholar** | **98** trích dẫn (5 trích dẫn có ảnh hưởng sâu sắc) |
| **Lĩnh vực cốt lõi (Concepts)** | Data quality, Computer science, Observational study, Standardization, Data science, Quality (philosophy), Automatic summarization, Data mining |

---

## 2. Tóm tắt Học thuật (Abstract & Summary)

### Tóm tắt cốt lõi (TLDR)
> **TLDR (Semantic Scholar AI):** The Data Quality Dashboard is an open-source R package that reports potential quality issues in an OMOP CDM instance through the systematic execution and summarization of over 3,300 configurable data quality checks.

### Toàn văn Abstract (Nguyên văn từ tác giả)
OBJECTIVE: Advances in standardization of observational healthcare data have enabled methodological breakthroughs, rapid global collaboration, and generation of real-world evidence to improve patient outcomes. Standardizations in data structure, such as use of common data models, need to be coupled with standardized approaches for data quality assessment. To ensure confidence in real-world evidence generated from the analysis of real-world data, one must first have confidence in the data itself. MATERIALS AND METHODS: We describe the implementation of check types across a data quality framework of conformance, completeness, plausibility, with both verification and validation. We illustrate how data quality checks, paired with decision thresholds, can be configured to customize data quality reporting across a range of observational health data sources. We discuss how data quality reporting can become part of the overall real-world evidence generation and dissemination process to promote transparency and build confidence in the resulting output. RESULTS: The Data Quality Dashboard is an open-source R package that reports potential quality issues in an OMOP CDM instance through the systematic execution and summarization of over 3300 configurable data quality checks. DISCUSSION: Transparently communicating how well common data model-standardized databases adhere to a set of quality measures adds a crucial piece that is currently missing from observational research. CONCLUSION: Assessing and improving the quality of our data will inherently improve the quality of the evidence we generate.

---

## 3. Đóng góp Phương pháp luận & Khái niệm then chốt

### Đóng góp nền tảng
Công trình công bố công cụ tự động hóa Data Quality Dashboard (DQD) của OHDSI, hiện thực hóa Khung Kahn thành hơn 3.300 phép kiểm tra SQL tự động. Tài liệu này thiết lập các nguyên lý vững chắc, giúp định hình tiêu chuẩn thực hành và phương pháp luận nghiên cứu dữ liệu y sinh trên phạm vi toàn cầu.

### Các khái niệm cốt lõi cần nắm vững
- **Khái niệm chính:** Các định nghĩa và kiến trúc phương pháp luận được văn bản gốc bảo chứng.
- **Tiêu chuẩn dữ liệu:** Định vị mối liên hệ với các chuẩn thông tin y tế quốc tế và các yêu cầu quản lý thực nghiệm.
- **Tính khả thi:** Đảm bảo khả năng chuyển giao và áp dụng trong môi trường nghiên cứu lâm sàng.

---

## 4. Ánh xạ và Tích hợp vào Sách Chuyên khảo Biomedical RDM

### Vị trí và Phạm vi trong Chuyên khảo
- **Chương mục cụ thể:** Mục 4.1 & Mục 4.4: Tự động hóa kiểm soát chất lượng với công cụ Data Quality Dashboard
- **Giai đoạn Vòng đời dữ liệu:** Giai đoạn 3 (Làm sạch) & Giai đoạn 4 (Chuẩn hóa OMOP)

### Ứng dụng Sư phạm & Luận điểm triển khai
Hướng dẫn cài đặt và thực thi gói R DataQualityDashboard trên cơ sở dữ liệu OMOP CDM, xuất báo cáo HTML minh bạch tỷ lệ kiểm tra Đạt/Không đạt (Pass/Fail) làm bằng chứng kiểm toán chất lượng trước khi nộp đề tài hoặc gửi tạp chí.

### Cảnh báo Bẫy thực tế (Pitfalls & Misconceptions)
> [!WARNING] **Bẫy thực tế cần phòng tránh khi áp dụng:**  
> Không thiết lập ngưỡng chấp nhận lỗi (error thresholds) thực tế cho từng chuyên khoa, dẫn đến việc bị 'ngập lụt' trong hàng trăm cảnh báo vi phạm tính hợp lý mà không lọc được lỗi nghiêm trọng.

---

## 5. Trích dẫn Chuẩn mực (Citations & References)

### Định dạng APA 7th Edition
```text
Clair Blacketer, Frank DeFalco, Patrick B. Ryan, & Peter R. Rijnbeek (2021). Increasing trust in real-world evidence through evaluation of observational data quality. *Journal of the American Medical Informatics Association*. https://doi.org/10.1093/jamia/ocab132
```

### Bản ghi BibTeX
```bibtex
@book{blacketer2021increasing,
  title = {{Increasing trust in real-world evidence through evaluation of observational data quality}},
  author = {Clair Blacketer and Frank DeFalco and Patrick B. Ryan and Peter R. Rijnbeek},
  year = {2021},
  publisher = {Journal of the American Medical Informatics Association},
  doi = {10.1093/jamia/ocab132},
}
```
