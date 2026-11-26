---
id: ch04-vanbuuren2018-mice-imputation
citekey: vanbuuren2018flexible
title: "Flexible Imputation of Missing Data, Second Edition"
type: Textbook
chapter: ch04
year: 2018
doi: 10.1201/9780429492259
openalex_id: https://openalex.org/W2891381594
semantic_scholar_id: f93da53197823e8bfb4ae6020c2b29a09d327935
citations:
  openalex: 3276
  semantic_scholar: 254
  influential: 19
tags: ["Imputation (statistics)", "Missing data", "Computer science", "Information retrieval", "Machine learning"]
date_reviewed: 2026-11-25
---

# Hồ sơ Thẩm định Tài liệu: Flexible Imputation of Missing Data, Second Edition

> **Phân loại:** Textbook · **Chương áp dụng:** [Chương 4: Chất lượng dữ liệu và dữ liệu khuyết](file:///d:/Antigravity/biomedical-rdm/docs/chapters/ch04_*.md)  
> **Vai trò trong chuyên khảo:** Giáo trình tiêu chuẩn vàng thực hành thuật toán Gán đa bội chuỗi phương trình (MICE) cho các bộ dữ liệu y học phức tạp.

---

## 1. Siêu dữ liệu Học thuật (Academic Metadata)

| Thuộc tính | Chi tiết xác thực từ API |
|---|---|
| **Tác giả (Authors)** | Stef van Buuren |
| **Năm xuất bản (Year)** | 2018 |
| **Nhà xuất bản / Tạp chí (Venue)** | Chapman & Hall/CRC eBooks |
| **DOI** | [10.1201/9780429492259](https://doi.org/10.1201/9780429492259) |
| **OpenAlex ID** | [https://openalex.org/W2891381594](https://openalex.org/W2891381594) |
| **Semantic Scholar ID** | [f93da53197823e8bfb4ae6020c2b29a09d327935](https://www.semanticscholar.org/paper/f93da53197823e8bfb4ae6020c2b29a09d327935) |
| **Số lượt trích dẫn OpenAlex** | **3,276** trích dẫn |
| **Số lượt trích dẫn Semantic Scholar** | **254** trích dẫn (19 trích dẫn có ảnh hưởng sâu sắc) |
| **Lĩnh vực cốt lõi (Concepts)** | Imputation (statistics), Missing data, Computer science, Information retrieval, Machine learning |

---

## 2. Tóm tắt Học thuật (Abstract & Summary)

### Tóm tắt cốt lõi (TLDR)
> **Tóm lược:** Giáo trình tiêu chuẩn vàng thực hành thuật toán Gán đa bội chuỗi phương trình (MICE) cho các bộ dữ liệu y học phức tạp.

### Toàn văn Abstract (Nguyên văn từ tác giả)
Missing data pose challenges to real-life data analysis. Simple ad-hoc fixes, like deletion or mean imputation, only work under highly restrictive conditions, which are often not met in practice. Multiple imputation replaces each missing value by multiple plausible values. The variability between these replacements reflects our ignorance of the true (but missing) value. Each of the completed data set is then analyzed by standard methods, and the results are pooled to obtain unbiased estimates with correct confidence intervals. Multiple imputation is a general approach that also inspires novel solutions to old problems by reformulating the task at hand as a missing-data problem. This is the second edition of a popular book on multiple imputation, focused on explaining the application of methods through detailed worked examples using the MICE package as developed by the author. This new edition incorporates the recent developments in this fast-moving field. This class-tested book avoids mathematical and technical details as much as possible: formulas are accompanied by verbal statements that explain the formula in accessible terms. The book sharpens the reader’s intuition on how to think about missing data, and provides all the tools needed to execute a well-grounded quantitative analysis in the presence of missing data.

---

## 3. Đóng góp Phương pháp luận & Khái niệm then chốt

### Đóng góp nền tảng
Giáo trình tiêu chuẩn vàng thực hành thuật toán Gán đa bội chuỗi phương trình (MICE) cho các bộ dữ liệu y học phức tạp. Tài liệu này thiết lập các nguyên lý vững chắc, giúp định hình tiêu chuẩn thực hành và phương pháp luận nghiên cứu dữ liệu y sinh trên phạm vi toàn cầu.

### Các khái niệm cốt lõi cần nắm vững
- **Khái niệm chính:** Các định nghĩa và kiến trúc phương pháp luận được văn bản gốc bảo chứng.
- **Tiêu chuẩn dữ liệu:** Định vị mối liên hệ với các chuẩn thông tin y tế quốc tế và các yêu cầu quản lý thực nghiệm.
- **Tính khả thi:** Đảm bảo khả năng chuyển giao và áp dụng trong môi trường nghiên cứu lâm sàng.

---

## 4. Ánh xạ và Tích hợp vào Sách Chuyên khảo Biomedical RDM

### Vị trí và Phạm vi trong Chuyên khảo
- **Chương mục cụ thể:** Mục 4.3: Kỹ thuật gán đa bội (Multiple Imputation by Chained Equations - MICE)
- **Giai đoạn Vòng đời dữ liệu:** Giai đoạn 3 (Làm sạch) & Giai đoạn 5 (Phân tích tái lập)

### Ứng dụng Sư phạm & Luận điểm triển khai
Hướng dẫn chi tiết quy trình 3 giai đoạn của gán đa bội: (1) Tạo $m$ tập dữ liệu gán bằng chuỗi phương trình hồi quy có điều kiện đầy đủ (FCS) và Predictive Mean Matching (PMM); (2) Phân tích mô hình độc lập trên từng tập; (3) Hợp nhất kết quả theo quy tắc Rubin (Rubin's Rules).

### Cảnh báo Bẫy thực tế (Pitfalls & Misconceptions)
> [!WARNING] **Bẫy thực tế cần phòng tránh khi áp dụng:**  
> Chạy gán dữ liệu trên biến mục tiêu (target variable/outcome) mà không bao gồm biến outcome trong mô hình gán của các biến giải thích, vi phạm nguyên tắc thống kê.

---

## 5. Trích dẫn Chuẩn mực (Citations & References)

### Định dạng APA 7th Edition
```text
Stef van Buuren (2018). Flexible Imputation of Missing Data, Second Edition. *Chapman & Hall/CRC eBooks*. https://doi.org/10.1201/9780429492259
```

### Bản ghi BibTeX
```bibtex
@book{vanbuuren2018flexible,
  title = {{Flexible Imputation of Missing Data, Second Edition}},
  author = {Stef van Buuren},
  year = {2018},
  publisher = {Chapman & Hall/CRC eBooks},
  doi = {10.1201/9780429492259},
}
```
