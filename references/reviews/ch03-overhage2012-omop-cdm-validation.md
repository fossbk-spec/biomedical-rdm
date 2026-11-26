---
id: ch03-overhage2012-omop-cdm-validation
citekey: overhage2012validation
title: "Validation of a common data model for active safety surveillance research"
type: SoTA Paper
chapter: ch03
year: 2012
doi: 10.1136/amiajnl-2011-000376
openalex_id: https://openalex.org/W34678172
semantic_scholar_id: 5c4cb597fc6b9dfd866b5edd2af485a61eb2f8bf
citations:
  openalex: 620
  semantic_scholar: 540
  influential: 27
tags: ["Observational study", "Computer science", "Data mining", "Scale (ratio)", "Systematic review", "Data science", "Database", "MEDLINE"]
date_reviewed: 2026-11-25
---

# Hồ sơ Thẩm định Tài liệu: Validation of a common data model for active safety surveillance research

> **Phân loại:** SoTA Paper · **Chương áp dụng:** [Chương 3: Chuẩn CDISC, FHIR và OMOP](file:///d:/Antigravity/biomedical-rdm/docs/chapters/ch03_*.md)  
> **Vai trò trong chuyên khảo:** Nghiên cứu chứng thực thực nghiệm tính khoa học và giá trị bảo toàn thông tin của mô hình OMOP CDM trên nhiều cơ sở dữ liệu lớn.

---

## 1. Siêu dữ liệu Học thuật (Academic Metadata)

| Thuộc tính | Chi tiết xác thực từ API |
|---|---|
| **Tác giả (Authors)** | J. Marc Overhage, Patrick B. Ryan, Christian Reich, Abraham G. Hartzema, Paul Stang |
| **Năm xuất bản (Year)** | 2012 |
| **Nhà xuất bản / Tạp chí (Venue)** | Journal of the American Medical Informatics Association |
| **DOI** | [10.1136/amiajnl-2011-000376](https://doi.org/10.1136/amiajnl-2011-000376) |
| **OpenAlex ID** | [https://openalex.org/W34678172](https://openalex.org/W34678172) |
| **Semantic Scholar ID** | [5c4cb597fc6b9dfd866b5edd2af485a61eb2f8bf](https://www.semanticscholar.org/paper/5c4cb597fc6b9dfd866b5edd2af485a61eb2f8bf) |
| **Số lượt trích dẫn OpenAlex** | **620** trích dẫn |
| **Số lượt trích dẫn Semantic Scholar** | **540** trích dẫn (27 trích dẫn có ảnh hưởng sâu sắc) |
| **Lĩnh vực cốt lõi (Concepts)** | Observational study, Computer science, Data mining, Scale (ratio), Systematic review, Data science, Database, MEDLINE |

---

## 2. Tóm tắt Học thuật (Abstract & Summary)

### Tóm tắt cốt lõi (TLDR)
> **TLDR (Semantic Scholar AI):** There was acceptable representation of the data from 10 observational databases in the OMOP CDM using the standardized terminologies selected, and a range of analytic methods was developed and executed with sufficient performance to be useful for active safety surveillance.

### Toàn văn Abstract (Nguyên văn từ tác giả)
OBJECTIVE: Systematic analysis of observational medical databases for active safety surveillance is hindered by the variation in data models and coding systems. Data analysts often find robust clinical data models difficult to understand and ill suited to support their analytic approaches. Further, some models do not facilitate the computations required for systematic analysis across many interventions and outcomes for large datasets. Translating the data from these idiosyncratic data models to a common data model (CDM) could facilitate both the analysts' understanding and the suitability for large-scale systematic analysis. In addition to facilitating analysis, a suitable CDM has to faithfully represent the source observational database. Before beginning to use the Observational Medical Outcomes Partnership (OMOP) CDM and a related dictionary of standardized terminologies for a study of large-scale systematic active safety surveillance, the authors validated the model's suitability for this use by example. VALIDATION BY EXAMPLE: To validate the OMOP CDM, the model was instantiated into a relational database, data from 10 different observational healthcare databases were loaded into separate instances, a comprehensive array of analytic methods that operate on the data model was created, and these methods were executed against the databases to measure performance. CONCLUSION: There was acceptable representation of the data from 10 observational databases in the OMOP CDM using the standardized terminologies selected, and a range of analytic methods was developed and executed with sufficient performance to be useful for active safety surveillance.

---

## 3. Đóng góp Phương pháp luận & Khái niệm then chốt

### Đóng góp nền tảng
Nghiên cứu chứng thực thực nghiệm tính khoa học và giá trị bảo toàn thông tin của mô hình OMOP CDM trên nhiều cơ sở dữ liệu lớn. Tài liệu này thiết lập các nguyên lý vững chắc, giúp định hình tiêu chuẩn thực hành và phương pháp luận nghiên cứu dữ liệu y sinh trên phạm vi toàn cầu.

### Các khái niệm cốt lõi cần nắm vững
- **Khái niệm chính:** Các định nghĩa và kiến trúc phương pháp luận được văn bản gốc bảo chứng.
- **Tiêu chuẩn dữ liệu:** Định vị mối liên hệ với các chuẩn thông tin y tế quốc tế và các yêu cầu quản lý thực nghiệm.
- **Tính khả thi:** Đảm bảo khả năng chuyển giao và áp dụng trong môi trường nghiên cứu lâm sàng.

---

## 4. Ánh xạ và Tích hợp vào Sách Chuyên khảo Biomedical RDM

### Vị trí và Phạm vi trong Chuyên khảo
- **Chương mục cụ thể:** Mục 3.3: Thẩm định quy trình ETL và Tính hợp lệ khoa học của Common Data Model
- **Giai đoạn Vòng đời dữ liệu:** Giai đoạn 4: Chuẩn hóa dữ liệu

### Ứng dụng Sư phạm & Luận điểm triển khai
Cung cấp bằng chứng thực nghiệm trả lời câu hỏi hoài nghi của các nhà nghiên cứu: liệu chuyển đổi dữ liệu sang một mô hình dùng chung có làm mất mát thông tin hoặc sai lệch kết quả nghiên cứu hay không.

### Cảnh báo Bẫy thực tế (Pitfalls & Misconceptions)
> [!WARNING] **Bẫy thực tế cần phòng tránh khi áp dụng:**  
> Thực hiện ETL từ cơ sở dữ liệu thô sang CDM mà không có quy trình kiểm tra đối chiếu (ETL reconciliation & validation) giữa số lượng bản ghi nguồn và bản ghi đích.

---

## 5. Trích dẫn Chuẩn mực (Citations & References)

### Định dạng APA 7th Edition
```text
J. Marc Overhage, Patrick B. Ryan, Christian Reich, Abraham G. Hartzema, & Paul Stang (2012). Validation of a common data model for active safety surveillance research. *Journal of the American Medical Informatics Association*. https://doi.org/10.1136/amiajnl-2011-000376
```

### Bản ghi BibTeX
```bibtex
@book{overhage2012validation,
  title = {{Validation of a common data model for active safety surveillance research}},
  author = {J. Marc Overhage and Patrick B. Ryan and Christian Reich and Abraham G. Hartzema and Paul Stang},
  year = {2012},
  publisher = {Journal of the American Medical Informatics Association},
  doi = {10.1136/amiajnl-2011-000376},
}
```
