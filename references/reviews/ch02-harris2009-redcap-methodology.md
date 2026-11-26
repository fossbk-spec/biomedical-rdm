---
id: ch02-harris2009-redcap-methodology
citekey: harris2009redcap
title: "Research electronic data capture (REDCap)—A metadata-driven methodology and workflow process for providing translational research informatics support"
type: SoTA Paper
chapter: ch02
year: 2008
doi: 10.1016/j.jbi.2008.08.010
openalex_id: https://openalex.org/W2093274439
semantic_scholar_id: fef864e28d699f3bcdc66663e67edf6fd240e492
citations:
  openalex: 55153
  semantic_scholar: 48707
  influential: 2810
tags: ["Electronic data capture", "Workflow", "Metadata", "Computer science", "Translational research informatics", "Software deployment", "Software", "Translational research"]
date_reviewed: 2026-11-25
---

# Hồ sơ Thẩm định Tài liệu: Research electronic data capture (REDCap)—A metadata-driven methodology and workflow process for providing translational research informatics support

> **Phân loại:** SoTA Paper · **Chương áp dụng:** [Chương 2: Thu thập dữ liệu lâm sàng, ALCOA+ và REDCap](file:///d:/Antigravity/biomedical-rdm/docs/chapters/ch02_*.md)  
> **Vai trò trong chuyên khảo:** Công trình khai sinh kiến trúc phần mềm REDCap, định hình phương pháp thu thập dữ liệu nghiên cứu lâm sàng hướng metadata.

---

## 1. Siêu dữ liệu Học thuật (Academic Metadata)

| Thuộc tính | Chi tiết xác thực từ API |
|---|---|
| **Tác giả (Authors)** | Paul A. Harris, Robert Taylor, Robert J. Thielke, Jonathon Payne, Nathaniel Gonzalez, José G. Conde |
| **Năm xuất bản (Year)** | 2008 |
| **Nhà xuất bản / Tạp chí (Venue)** | Journal of Biomedical Informatics |
| **DOI** | [10.1016/j.jbi.2008.08.010](https://doi.org/10.1016/j.jbi.2008.08.010) |
| **OpenAlex ID** | [https://openalex.org/W2093274439](https://openalex.org/W2093274439) |
| **Semantic Scholar ID** | [fef864e28d699f3bcdc66663e67edf6fd240e492](https://www.semanticscholar.org/paper/fef864e28d699f3bcdc66663e67edf6fd240e492) |
| **Số lượt trích dẫn OpenAlex** | **55,153** trích dẫn |
| **Số lượt trích dẫn Semantic Scholar** | **48,707** trích dẫn (2810 trích dẫn có ảnh hưởng sâu sắc) |
| **Lĩnh vực cốt lõi (Concepts)** | Electronic data capture, Workflow, Metadata, Computer science, Translational research informatics, Software deployment, Software, Translational research |

---

## 2. Tóm tắt Học thuật (Abstract & Summary)

### Tóm tắt cốt lõi (TLDR)
> **TLDR (Semantic Scholar AI):** A brief description of the REDCap metadata-driven software toolset and detail concerning the capture and use of study-related metadata from scientific research teams are presented.

### Toàn văn Abstract (Nguyên văn từ tác giả)
REDCap is a novel workflow methodology and software solution designed for rapid development and deployment of electronic data capture tools to support clinical and translational research. We present: 1) a brief description of the REDCap metadata-driven software toolset; 2) detail concerning the capture and use of study-related metadata from scientific research teams; 3) measures of impact for REDCap; 4) details concerning a consortium network of domestic and international institutions collaborating on the project; and 5) strengths and limitations of the REDCap system. REDCap is currently supporting 286 translational research projects in a growing collaborative network including 27 active partner institutions.

---

## 3. Đóng góp Phương pháp luận & Khái niệm then chốt

### Đóng góp nền tảng
Công trình khai sinh kiến trúc phần mềm REDCap, định hình phương pháp thu thập dữ liệu nghiên cứu lâm sàng hướng metadata. Tài liệu này thiết lập các nguyên lý vững chắc, giúp định hình tiêu chuẩn thực hành và phương pháp luận nghiên cứu dữ liệu y sinh trên phạm vi toàn cầu.

### Các khái niệm cốt lõi cần nắm vững
- **Khái niệm chính:** Các định nghĩa và kiến trúc phương pháp luận được văn bản gốc bảo chứng.
- **Tiêu chuẩn dữ liệu:** Định vị mối liên hệ với các chuẩn thông tin y tế quốc tế và các yêu cầu quản lý thực nghiệm.
- **Tính khả thi:** Đảm bảo khả năng chuyển giao và áp dụng trong môi trường nghiên cứu lâm sàng.

---

## 4. Ánh xạ và Tích hợp vào Sách Chuyên khảo Biomedical RDM

### Vị trí và Phạm vi trong Chuyên khảo
- **Chương mục cụ thể:** Mục 2.3: Kiến trúc Metadata-driven và Hệ thống thu thập dữ liệu điện tử (EDC)
- **Giai đoạn Vòng đời dữ liệu:** Giai đoạn 2: Thu thập dữ liệu lâm sàng

### Ứng dụng Sư phạm & Luận điểm triển khai
Giải thích nguyên lý tách biệt giữa Siêu dữ liệu (Data Dictionary dạng bảng mã) và Dữ liệu thực tế (Entity-Attribute-Value), cho phép nhà nghiên cứu không chuyên về CNTT vẫn có thể tự xây dựng eCRF chuẩn mực và lưu vết kiểm toán (Audit Trail) tuân thủ 21 CFR Part 11.

### Cảnh báo Bẫy thực tế (Pitfalls & Misconceptions)
> [!WARNING] **Bẫy thực tế cần phòng tránh khi áp dụng:**  
> Sử dụng bảng tính Excel hoặc Google Sheets để thu thập dữ liệu bệnh nhân thay vì EDC chuyên dụng, vi phạm nghiêm trọng tính toàn vẹn dữ liệu ALCOA+ (không có audit trail, dễ ghi đè, không phân quyền vai trò).

---

## 5. Trích dẫn Chuẩn mực (Citations & References)

### Định dạng APA 7th Edition
```text
Paul A. Harris, Robert Taylor, Robert J. Thielke, Jonathon Payne, Nathaniel Gonzalez, & José G. Conde (2008). Research electronic data capture (REDCap)—A metadata-driven methodology and workflow process for providing translational research informatics support. *Journal of Biomedical Informatics*. https://doi.org/10.1016/j.jbi.2008.08.010
```

### Bản ghi BibTeX
```bibtex
@book{harris2009redcap,
  title = {{Research electronic data capture (REDCap)—A metadata-driven methodology and workflow process for providing translational research informatics support}},
  author = {Paul A. Harris and Robert Taylor and Robert J. Thielke and Jonathon Payne and Nathaniel Gonzalez and José G. Conde},
  year = {2008},
  publisher = {Journal of Biomedical Informatics},
  doi = {10.1016/j.jbi.2008.08.010},
}
```
