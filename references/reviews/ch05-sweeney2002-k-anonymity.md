---
id: ch05-sweeney2002-k-anonymity
citekey: sweeney2002kanonymity
title: "k-ANONYMITY: A MODEL FOR PROTECTING PRIVACY"
type: SoTA Paper
chapter: ch05
year: 2002
doi: 10.1142/s0218488502001648
openalex_id: https://openalex.org/W2159024459
semantic_scholar_id: 62ce35108ef0a816ba1929223f511c976079a300
citations:
  openalex: 10212
  semantic_scholar: 9323
  influential: 664
tags: ["Anonymity", "Computer security", "k-anonymity", "Computer science", "Internet privacy", "Identification (biology)", "Software deployment", "Data Protection Act 1998"]
date_reviewed: 2026-11-25
---

# Hồ sơ Thẩm định Tài liệu: k-ANONYMITY: A MODEL FOR PROTECTING PRIVACY

> **Phân loại:** SoTA Paper · **Chương áp dụng:** [Chương 5: Bảo mật và khử định danh](file:///d:/Antigravity/biomedical-rdm/docs/chapters/ch05_*.md)  
> **Vai trò trong chuyên khảo:** Công trình đặt nền tảng cho mô hình k-anonymity và chứng minh thực nghiệm cuộc tấn công liên kết (linking attack) tái định danh hồ sơ y tế.

---

## 1. Siêu dữ liệu Học thuật (Academic Metadata)

| Thuộc tính | Chi tiết xác thực từ API |
|---|---|
| **Tác giả (Authors)** | Latanya Sweeney |
| **Năm xuất bản (Year)** | 2002 |
| **Nhà xuất bản / Tạp chí (Venue)** | International Journal of Uncertainty Fuzziness and Knowledge-Based Systems |
| **DOI** | [10.1142/s0218488502001648](https://doi.org/10.1142/s0218488502001648) |
| **OpenAlex ID** | [https://openalex.org/W2159024459](https://openalex.org/W2159024459) |
| **Semantic Scholar ID** | [62ce35108ef0a816ba1929223f511c976079a300](https://www.semanticscholar.org/paper/62ce35108ef0a816ba1929223f511c976079a300) |
| **Số lượt trích dẫn OpenAlex** | **10,212** trích dẫn |
| **Số lượt trích dẫn Semantic Scholar** | **9,323** trích dẫn (664 trích dẫn có ảnh hưởng sâu sắc) |
| **Lĩnh vực cốt lõi (Concepts)** | Anonymity, Computer security, k-anonymity, Computer science, Internet privacy, Identification (biology), Software deployment, Data Protection Act 1998 |

---

## 2. Tóm tắt Học thuật (Abstract & Summary)

### Tóm tắt cốt lõi (TLDR)
> **TLDR (Semantic Scholar AI):** The solution provided in this paper includes a formal protection model named k-anonymity and a set of accompanying policies for deployment and examines re-identification attacks that can be realized on releases that adhere to k- anonymity unless accompanying policies are respected.

### Toàn văn Abstract (Nguyên văn từ tác giả)
Consider a data holder, such as a hospital or a bank, that has a privately held collection of person-specific, field structured data. Suppose the data holder wants to share a version of the data with researchers. How can a data holder release a version of its private data with scientific guarantees that the individuals who are the subjects of the data cannot be re-identified while the data remain practically useful? The solution provided in this paper includes a formal protection model named k-anonymity and a set of accompanying policies for deployment. A release provides k-anonymity protection if the information for each person contained in the release cannot be distinguished from at least k-1 individuals whose information also appears in the release. This paper also examines re-identification attacks that can be realized on releases that adhere to k-anonymity unless accompanying policies are respected. The k-anonymity protection model is important because it forms the basis on which the real-world systems known as Datafly, μ-Argus and k-Similar provide guarantees of privacy protection.

---

## 3. Đóng góp Phương pháp luận & Khái niệm then chốt

### Đóng góp nền tảng
Công trình đặt nền tảng cho mô hình k-anonymity và chứng minh thực nghiệm cuộc tấn công liên kết (linking attack) tái định danh hồ sơ y tế. Tài liệu này thiết lập các nguyên lý vững chắc, giúp định hình tiêu chuẩn thực hành và phương pháp luận nghiên cứu dữ liệu y sinh trên phạm vi toàn cầu.

### Các khái niệm cốt lõi cần nắm vững
- **Khái niệm chính:** Các định nghĩa và kiến trúc phương pháp luận được văn bản gốc bảo chứng.
- **Tiêu chuẩn dữ liệu:** Định vị mối liên hệ với các chuẩn thông tin y tế quốc tế và các yêu cầu quản lý thực nghiệm.
- **Tính khả thi:** Đảm bảo khả năng chuyển giao và áp dụng trong môi trường nghiên cứu lâm sàng.

---

## 4. Ánh xạ và Tích hợp vào Sách Chuyên khảo Biomedical RDM

### Vị trí và Phạm vi trong Chuyên khảo
- **Chương mục cụ thể:** Mục 5.2: Mô hình k-anonymity và Các kỹ thuật làm mờ (Generalization/Suppression)
- **Giai đoạn Vòng đời dữ liệu:** Lớp ngang Bảo mật; Giai đoạn 6 (Chia sẻ dữ liệu)

### Ứng dụng Sư phạm & Luận điểm triển khai
Giảng dạy khái niệm nhóm tương đương (equivalence class): mỗi bản ghi bệnh nhân phải có các thuộc tính bán định danh giống hệt với ít nhất $k-1$ bệnh nhân khác trong bộ dữ liệu; cách áp dụng kỹ thuật làm mờ phân cấp (ví dụ tuổi gộp nhóm 5 năm, địa chỉ rút gọn về cấp tỉnh/huyện).

### Cảnh báo Bẫy thực tế (Pitfalls & Misconceptions)
> [!WARNING] **Bẫy thực tế cần phòng tránh khi áp dụng:**  
> Lầm tưởng đạt được $k$-anonymity là đã bảo vệ an toàn tuyệt đối thuộc tính nhạy cảm; không lường trước được nguy cơ tấn công đồng nhất (homogeneity attack) khi tất cả $k$ bệnh nhân trong nhóm đều có chung một chẩn đoán bệnh.

---

## 5. Trích dẫn Chuẩn mực (Citations & References)

### Định dạng APA 7th Edition
```text
Latanya Sweeney (2002). k-ANONYMITY: A MODEL FOR PROTECTING PRIVACY. *International Journal of Uncertainty Fuzziness and Knowledge-Based Systems*. https://doi.org/10.1142/s0218488502001648
```

### Bản ghi BibTeX
```bibtex
@book{sweeney2002kanonymity,
  title = {{k-ANONYMITY: A MODEL FOR PROTECTING PRIVACY}},
  author = {Latanya Sweeney},
  year = {2002},
  publisher = {International Journal of Uncertainty Fuzziness and Knowledge-Based Systems},
  doi = {10.1142/s0218488502001648},
}
```
