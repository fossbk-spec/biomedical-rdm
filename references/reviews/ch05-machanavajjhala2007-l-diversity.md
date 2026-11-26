---
id: ch05-machanavajjhala2007-l-diversity
citekey: machanavajjhala2007ldiversity
title: "L -diversity: Privacy beyond k -anonymity"
type: SoTA Paper
chapter: ch05
year: 2007
doi: 10.1145/1217299.1217302
openalex_id: https://openalex.org/W2134167315
semantic_scholar_id: 4c86fe689be77e5207b22743a0f47d1f2b42a303
citations:
  openalex: 4463
  semantic_scholar: 5804
  influential: 435
tags: ["Popularity", "Computer science", "Data publishing", "Anonymity", "Diversity (politics)", "k-anonymity", "Simple (philosophy)", "Internet privacy"]
date_reviewed: 2026-11-25
---

# Hồ sơ Thẩm định Tài liệu: L -diversity: Privacy beyond k -anonymity

> **Phân loại:** SoTA Paper · **Chương áp dụng:** [Chương 5: Bảo mật và khử định danh](file:///d:/Antigravity/biomedical-rdm/docs/chapters/ch05_*.md)  
> **Vai trò trong chuyên khảo:** Công trình phát triển mô hình ℓ-diversity nhằm giải quyết các lỗ hổng tấn công đồng nhất và tri thức nền tảng của k-anonymity.

---

## 1. Siêu dữ liệu Học thuật (Academic Metadata)

| Thuộc tính | Chi tiết xác thực từ API |
|---|---|
| **Tác giả (Authors)** | Ashwin Machanavajjhala, Daniel Kifer, Johannes E. Gehrke, Muthuramakrishnan Venkitasubramaniam |
| **Năm xuất bản (Year)** | 2007 |
| **Nhà xuất bản / Tạp chí (Venue)** | ACM Transactions on Knowledge Discovery from Data |
| **DOI** | [10.1145/1217299.1217302](https://doi.org/10.1145/1217299.1217302) |
| **OpenAlex ID** | [https://openalex.org/W2134167315](https://openalex.org/W2134167315) |
| **Semantic Scholar ID** | [4c86fe689be77e5207b22743a0f47d1f2b42a303](https://www.semanticscholar.org/paper/4c86fe689be77e5207b22743a0f47d1f2b42a303) |
| **Số lượt trích dẫn OpenAlex** | **4,463** trích dẫn |
| **Số lượt trích dẫn Semantic Scholar** | **5,804** trích dẫn (435 trích dẫn có ảnh hưởng sâu sắc) |
| **Lĩnh vực cốt lõi (Concepts)** | Popularity, Computer science, Data publishing, Anonymity, Diversity (politics), k-anonymity, Simple (philosophy), Internet privacy |

---

## 2. Tóm tắt Học thuật (Abstract & Summary)

### Tóm tắt cốt lõi (TLDR)
> **Tóm lược:** Công trình phát triển mô hình ℓ-diversity nhằm giải quyết các lỗ hổng tấn công đồng nhất và tri thức nền tảng của k-anonymity.

### Toàn văn Abstract (Nguyên văn từ tác giả)
Publishing data about individuals without revealing sensitive information about them is an important problem. In recent years, a new definition of privacy called k -anonymity has gained popularity. In a k -anonymized dataset, each record is indistinguishable from at least k − 1 other records with respect to certain identifying attributes. In this article, we show using two simple attacks that a k -anonymized dataset has some subtle but severe privacy problems. First, an attacker can discover the values of sensitive attributes when there is little diversity in those sensitive attributes. This is a known problem. Second, attackers often have background knowledge, and we show that k -anonymity does not guarantee privacy against attackers using background knowledge. We give a detailed analysis of these two attacks, and we propose a novel and powerful privacy criterion called ℓ-diversity that can defend against such attacks. In addition to building a formal foundation for ℓ-diversity, we show in an experimental evaluation that ℓ-diversity is practical and can be implemented efficiently.

---

## 3. Đóng góp Phương pháp luận & Khái niệm then chốt

### Đóng góp nền tảng
Công trình phát triển mô hình ℓ-diversity nhằm giải quyết các lỗ hổng tấn công đồng nhất và tri thức nền tảng của k-anonymity. Tài liệu này thiết lập các nguyên lý vững chắc, giúp định hình tiêu chuẩn thực hành và phương pháp luận nghiên cứu dữ liệu y sinh trên phạm vi toàn cầu.

### Các khái niệm cốt lõi cần nắm vững
- **Khái niệm chính:** Các định nghĩa và kiến trúc phương pháp luận được văn bản gốc bảo chứng.
- **Tiêu chuẩn dữ liệu:** Định vị mối liên hệ với các chuẩn thông tin y tế quốc tế và các yêu cầu quản lý thực nghiệm.
- **Tính khả thi:** Đảm bảo khả năng chuyển giao và áp dụng trong môi trường nghiên cứu lâm sàng.

---

## 4. Ánh xạ và Tích hợp vào Sách Chuyên khảo Biomedical RDM

### Vị trí và Phạm vi trong Chuyên khảo
- **Chương mục cụ thể:** Mục 5.2: Mô hình ℓ-diversity và t-closeness nâng cao
- **Giai đoạn Vòng đời dữ liệu:** Lớp ngang Bảo mật dữ liệu

### Ứng dụng Sư phạm & Luận điểm triển khai
Trình bày điều kiện $\ell$-diversity: trong mỗi nhóm tương đương thỏa mãn $k$-anonymity, các giá trị của thuộc tính nhạy cảm (như chẩn đoán HIV, ung thư, tâm thần) phải có ít nhất $\ell$ giá trị đa dạng, ngăn chặn kẻ tấn công suy đoán chắc chắn tình trạng bệnh lý của đối tượng.

### Cảnh báo Bẫy thực tế (Pitfalls & Misconceptions)
> [!WARNING] **Bẫy thực tế cần phòng tránh khi áp dụng:**  
> Áp dụng $\ell$-diversity mà không kiểm soát sự phân bố tổng thể (skewness), dẫn đến nguy cơ lộ dữ liệu nếu thuộc tính nhạy cảm chiếm tỷ lệ áp đảo trong quần thể (ví dụ 99% kết quả xét nghiệm âm tính).

---

## 5. Trích dẫn Chuẩn mực (Citations & References)

### Định dạng APA 7th Edition
```text
Ashwin Machanavajjhala, Daniel Kifer, Johannes E. Gehrke, & Muthuramakrishnan Venkitasubramaniam (2007). L -diversity: Privacy beyond k -anonymity. *ACM Transactions on Knowledge Discovery from Data*. https://doi.org/10.1145/1217299.1217302
```

### Bản ghi BibTeX
```bibtex
@book{machanavajjhala2007ldiversity,
  title = {{L -diversity: Privacy beyond k -anonymity}},
  author = {Ashwin Machanavajjhala and Daniel Kifer and Johannes E. Gehrke and Muthuramakrishnan Venkitasubramaniam},
  year = {2007},
  publisher = {ACM Transactions on Knowledge Discovery from Data},
  doi = {10.1145/1217299.1217302},
}
```
