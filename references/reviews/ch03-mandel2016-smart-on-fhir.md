---
id: ch03-mandel2016-smart-on-fhir
citekey: mandel2016smart
title: "SMART on FHIR: a standards-based, interoperable apps platform for electronic health records"
type: SoTA Paper
chapter: ch03
year: 2016
doi: 10.1093/jamia/ocv189
openalex_id: https://openalex.org/W2276530525
semantic_scholar_id: 4744fe3b6182274f29f608cb6c820dd2a3be926a
citations:
  openalex: 1099
  semantic_scholar: 799
  influential: 45
tags: ["Interoperability", "Application programming interface", "Computer science", "Health care", "Consistency (knowledge bases)", "Interface (matter)", "Open standard", "Software engineering"]
date_reviewed: 2026-11-25
---

# Hồ sơ Thẩm định Tài liệu: SMART on FHIR: a standards-based, interoperable apps platform for electronic health records

> **Phân loại:** SoTA Paper · **Chương áp dụng:** [Chương 3: Chuẩn CDISC, FHIR và OMOP](file:///d:/Antigravity/biomedical-rdm/docs/chapters/ch03_*.md)  
> **Vai trò trong chuyên khảo:** Công trình thiết lập nền tảng ứng dụng tương tác trên hồ sơ bệnh án điện tử kết hợp chuẩn HL7 FHIR và xác thực OAuth2.

---

## 1. Siêu dữ liệu Học thuật (Academic Metadata)

| Thuộc tính | Chi tiết xác thực từ API |
|---|---|
| **Tác giả (Authors)** | Joshua C. Mandel, David Kreda, Kenneth D. Mandl, Isaac S. Kohane, Rachel Badovinac Ramoni |
| **Năm xuất bản (Year)** | 2016 |
| **Nhà xuất bản / Tạp chí (Venue)** | Journal of the American Medical Informatics Association |
| **DOI** | [10.1093/jamia/ocv189](https://doi.org/10.1093/jamia/ocv189) |
| **OpenAlex ID** | [https://openalex.org/W2276530525](https://openalex.org/W2276530525) |
| **Semantic Scholar ID** | [4744fe3b6182274f29f608cb6c820dd2a3be926a](https://www.semanticscholar.org/paper/4744fe3b6182274f29f608cb6c820dd2a3be926a) |
| **Số lượt trích dẫn OpenAlex** | **1,099** trích dẫn |
| **Số lượt trích dẫn Semantic Scholar** | **799** trích dẫn (45 trích dẫn có ảnh hưởng sâu sắc) |
| **Lĩnh vực cốt lõi (Concepts)** | Interoperability, Application programming interface, Computer science, Health care, Consistency (knowledge bases), Interface (matter), Open standard, Software engineering |

---

## 2. Tóm tắt Học thuật (Abstract & Summary)

### Tóm tắt cốt lõi (TLDR)
> **TLDR (Semantic Scholar AI):** This paper describes the creation of SMART on FHIR, relate the experience of the vendors and developers who built SMARTOnFHIR prototypes, and discusses some challenges in going from early industry prototyping to industry-wide production use.

### Toàn văn Abstract (Nguyên văn từ tác giả)
OBJECTIVE: In early 2010, Harvard Medical School and Boston Children's Hospital began an interoperability project with the distinctive goal of developing a platform to enable medical applications to be written once and run unmodified across different healthcare IT systems. The project was called Substitutable Medical Applications and Reusable Technologies (SMART). METHODS: We adopted contemporary web standards for application programming interface transport, authorization, and user interface, and standard medical terminologies for coded data. In our initial design, we created our own openly licensed clinical data models to enforce consistency and simplicity. During the second half of 2013, we updated SMART to take advantage of the clinical data models and the application-programming interface described in a new, openly licensed Health Level Seven draft standard called Fast Health Interoperability Resources (FHIR). Signaling our adoption of the emerging FHIR standard, we called the new platform SMART on FHIR. RESULTS: We introduced the SMART on FHIR platform with a demonstration that included several commercial healthcare IT vendors and app developers showcasing prototypes at the Health Information Management Systems Society conference in February 2014. This established the feasibility of SMART on FHIR, while highlighting the need for commonly accepted pragmatic constraints on the base FHIR specification. CONCLUSION: In this paper, we describe the creation of SMART on FHIR, relate the experience of the vendors and developers who built SMART on FHIR prototypes, and discuss some challenges in going from early industry prototyping to industry-wide production use.

---

## 3. Đóng góp Phương pháp luận & Khái niệm then chốt

### Đóng góp nền tảng
Công trình thiết lập nền tảng ứng dụng tương tác trên hồ sơ bệnh án điện tử kết hợp chuẩn HL7 FHIR và xác thực OAuth2. Tài liệu này thiết lập các nguyên lý vững chắc, giúp định hình tiêu chuẩn thực hành và phương pháp luận nghiên cứu dữ liệu y sinh trên phạm vi toàn cầu.

### Các khái niệm cốt lõi cần nắm vững
- **Khái niệm chính:** Các định nghĩa và kiến trúc phương pháp luận được văn bản gốc bảo chứng.
- **Tiêu chuẩn dữ liệu:** Định vị mối liên hệ với các chuẩn thông tin y tế quốc tế và các yêu cầu quản lý thực nghiệm.
- **Tính khả thi:** Đảm bảo khả năng chuyển giao và áp dụng trong môi trường nghiên cứu lâm sàng.

---

## 4. Ánh xạ và Tích hợp vào Sách Chuyên khảo Biomedical RDM

### Vị trí và Phạm vi trong Chuyên khảo
- **Chương mục cụ thể:** Mục 3.2: Chuẩn HL7 FHIR và Khả năng tương tác thời gian thực
- **Giai đoạn Vòng đời dữ liệu:** Giai đoạn 2 (Thu thập tích hợp từ EMR) và Giai đoạn 4 (Chuẩn hóa)

### Ứng dụng Sư phạm & Luận điểm triển khai
Minh họa cách một ứng dụng nghiên cứu y sinh có thể kết nối an toàn với hệ thống bệnh án điện tử (EHR/HIS) để trích xuất dữ liệu lâm sàng theo chuẩn Resource của FHIR (Patient, Observation, Condition) mà không cần can thiệp trực tiếp vào cơ sở dữ liệu gốc.

### Cảnh báo Bẫy thực tế (Pitfalls & Misconceptions)
> [!WARNING] **Bẫy thực tế cần phòng tránh khi áp dụng:**  
> Nhầm lẫn giữa mục đích của FHIR (tương tác dữ liệu lâm sàng thời gian thực ở mức độ từng giao dịch cá nhân) với OMOP CDM (tổng hợp dữ liệu thứ cấp quy mô lớn phục vụ phân tích dịch tễ học và nghiên cứu quan sát).

---

## 5. Trích dẫn Chuẩn mực (Citations & References)

### Định dạng APA 7th Edition
```text
Joshua C. Mandel, David Kreda, Kenneth D. Mandl, Isaac S. Kohane, & Rachel Badovinac Ramoni (2016). SMART on FHIR: a standards-based, interoperable apps platform for electronic health records. *Journal of the American Medical Informatics Association*. https://doi.org/10.1093/jamia/ocv189
```

### Bản ghi BibTeX
```bibtex
@book{mandel2016smart,
  title = {{SMART on FHIR: a standards-based, interoperable apps platform for electronic health records}},
  author = {Joshua C. Mandel and David Kreda and Kenneth D. Mandl and Isaac S. Kohane and Rachel Badovinac Ramoni},
  year = {2016},
  publisher = {Journal of the American Medical Informatics Association},
  doi = {10.1093/jamia/ocv189},
}
```
