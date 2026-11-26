---
id: ch07-wilkinson2019-fair-metrics
citekey: wilkinson2019evaluating
title: "Evaluating FAIR maturity through a scalable, automated, community-governed framework"
type: SoTA Paper
chapter: ch07
year: 2019
doi: 10.1038/s41597-019-0184-5
openalex_id: https://openalex.org/W2973839119
semantic_scholar_id: 2a989a03b696ec5c2730edd93a7e06e7c627d10e
citations:
  openalex: 236
  semantic_scholar: 183
  influential: 9
tags: ["Computer science", "Maturity (psychological)", "Scalability", "Resource (disambiguation)", "World Wide Web", "Data science", "Domain (mathematical analysis)", "Database"]
date_reviewed: 2026-11-25
---

# Hồ sơ Thẩm định Tài liệu: Evaluating FAIR maturity through a scalable, automated, community-governed framework

> **Phân loại:** SoTA Paper · **Chương áp dụng:** [Chương 7: FAIR, kho lưu trữ và dữ liệu sẵn sàng cho AI](file:///d:/Antigravity/biomedical-rdm/docs/chapters/ch07_*.md)  
> **Vai trò trong chuyên khảo:** Khung thiết kế và bộ chỉ số định lượng mức độ trưởng thành FAIR có thể kiểm tra tự động hóa quy mô lớn.

---

## 1. Siêu dữ liệu Học thuật (Academic Metadata)

| Thuộc tính | Chi tiết xác thực từ API |
|---|---|
| **Tác giả (Authors)** | Mark D. Wilkinson, Michel Dumontier, Susanna‐Assunta Sansone, Luiz Olavo Bonino da Silva Santos, Mario Prieto, Dominique Batista, Peter McQuilton, Tobias Kuhn, Philippe Rocca‐Serra, Mercè Crosas, Erik Schultes |
| **Năm xuất bản (Year)** | 2019 |
| **Nhà xuất bản / Tạp chí (Venue)** | Scientific Data |
| **DOI** | [10.1038/s41597-019-0184-5](https://doi.org/10.1038/s41597-019-0184-5) |
| **OpenAlex ID** | [https://openalex.org/W2973839119](https://openalex.org/W2973839119) |
| **Semantic Scholar ID** | [2a989a03b696ec5c2730edd93a7e06e7c627d10e](https://www.semanticscholar.org/paper/2a989a03b696ec5c2730edd93a7e06e7c627d10e) |
| **Số lượt trích dẫn OpenAlex** | **236** trích dẫn |
| **Số lượt trích dẫn Semantic Scholar** | **183** trích dẫn (9 trích dẫn có ảnh hưởng sâu sắc) |
| **Lĩnh vực cốt lõi (Concepts)** | Computer science, Maturity (psychological), Scalability, Resource (disambiguation), World Wide Web, Data science, Domain (mathematical analysis), Database |

---

## 2. Tóm tắt Học thuật (Abstract & Summary)

### Tóm tắt cốt lõi (TLDR)
> **TLDR (Semantic Scholar AI):** A scalable, automatable framework to evaluate digital resources that encompasses measurable indicators, open source tools, and participation guidelines, which come together to accommodate domain relevant community-defined FAIR assessments is proposed.

### Toàn văn Abstract (Nguyên văn từ tác giả)
Transparent evaluations of FAIRness are increasingly required by a wide range of stakeholders, from scientists to publishers, funding agencies and policy makers. We propose a scalable, automatable framework to evaluate digital resources that encompasses measurable indicators, open source tools, and participation guidelines, which come together to accommodate domain relevant community-defined FAIR assessments. The components of the framework are: (1) Maturity Indicators - community-authored specifications that delimit a specific automatically-measurable FAIR behavior; (2) Compliance Tests - small Web apps that test digital resources against individual Maturity Indicators; and (3) the Evaluator, a Web application that registers, assembles, and applies community-relevant sets of Compliance Tests against a digital resource, and provides a detailed report about what a machine "sees" when it visits that resource. We discuss the technical and social considerations of FAIR assessments, and how this translates to our community-driven infrastructure. We then illustrate how the output of the Evaluator tool can serve as a roadmap to assist data stewards to incrementally and realistically improve the FAIRness of their resources.

---

## 3. Đóng góp Phương pháp luận & Khái niệm then chốt

### Đóng góp nền tảng
Khung thiết kế và bộ chỉ số định lượng mức độ trưởng thành FAIR có thể kiểm tra tự động hóa quy mô lớn. Tài liệu này thiết lập các nguyên lý vững chắc, giúp định hình tiêu chuẩn thực hành và phương pháp luận nghiên cứu dữ liệu y sinh trên phạm vi toàn cầu.

### Các khái niệm cốt lõi cần nắm vững
- **Khái niệm chính:** Các định nghĩa và kiến trúc phương pháp luận được văn bản gốc bảo chứng.
- **Tiêu chuẩn dữ liệu:** Định vị mối liên hệ với các chuẩn thông tin y tế quốc tế và các yêu cầu quản lý thực nghiệm.
- **Tính khả thi:** Đảm bảo khả năng chuyển giao và áp dụng trong môi trường nghiên cứu lâm sàng.

---

## 4. Ánh xạ và Tích hợp vào Sách Chuyên khảo Biomedical RDM

### Vị trí và Phạm vi trong Chuyên khảo
- **Chương mục cụ thể:** Mục 7.1: Đo lường mức độ trưởng thành FAIR (FAIR Maturity Assessment)
- **Giai đoạn Vòng đời dữ liệu:** Giai đoạn 6: FAIR và Chia sẻ dữ liệu

### Ứng dụng Sư phạm & Luận điểm triển khai
Giới thiệu các công cụ tự động kiểm thử FAIR (như F-UJI, FAIR-Checker) để chấm điểm bộ dữ liệu nghiên cứu y sinh trước khi công bố lên các kho lưu trữ (Repositories như Zenodo, Figshare, PhysioNet).

### Cảnh báo Bẫy thực tế (Pitfalls & Misconceptions)
> [!WARNING] **Bẫy thực tế cần phòng tránh khi áp dụng:**  
> Tự đánh giá định tính chủ quan rằng dữ liệu của mình đã 'rất FAIR' mà không chạy qua các bộ kiểm tra tự động độc lập theo tiêu chuẩn RDA FAIR Data Maturity Model.

---

## 5. Trích dẫn Chuẩn mực (Citations & References)

### Định dạng APA 7th Edition
```text
Mark D. Wilkinson, Michel Dumontier, Susanna‐Assunta Sansone, Luiz Olavo Bonino da Silva Santos, Mario Prieto, Dominique Batista, ... Erik Schultes (2019). Evaluating FAIR maturity through a scalable, automated, community-governed framework. *Scientific Data*. https://doi.org/10.1038/s41597-019-0184-5
```

### Bản ghi BibTeX
```bibtex
@book{wilkinson2019evaluating,
  title = {{Evaluating FAIR maturity through a scalable, automated, community-governed framework}},
  author = {Mark D. Wilkinson and Michel Dumontier and Susanna‐Assunta Sansone and Luiz Olavo Bonino da Silva Santos and Mario Prieto and Dominique Batista and Peter McQuilton and Tobias Kuhn and Philippe Rocca‐Serra and Mercè Crosas and Erik Schultes},
  year = {2019},
  publisher = {Scientific Data},
  doi = {10.1038/s41597-019-0184-5},
}
```
