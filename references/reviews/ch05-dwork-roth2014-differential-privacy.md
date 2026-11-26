---
id: ch05-dwork-roth2014-differential-privacy
citekey: dwork2014algorithmic
title: "The Algorithmic Foundations of Differential Privacy"
type: Monograph / Textbook
chapter: ch05
year: 2014
doi: 10.1561/0400000042
openalex_id: https://openalex.org/W4205228770
semantic_scholar_id: 0023582fde36430c7e3ae81611a14e558c8f4bae
citations:
  openalex: 11470
  semantic_scholar: 10679
  influential: 1872
tags: ["Differential privacy", "Computer science", "Differential (mechanical device)", "Internet privacy", "Computer security", "Engineering", "Data mining", "Aerospace engineering"]
date_reviewed: 2026-11-25
---

# Hồ sơ Thẩm định Tài liệu: The Algorithmic Foundations of Differential Privacy

> **Phân loại:** Monograph / Textbook · **Chương áp dụng:** [Chương 5: Bảo mật và khử định danh](file:///d:/Antigravity/biomedical-rdm/docs/chapters/ch05_*.md)  
> **Vai trò trong chuyên khảo:** Chuyên khảo kinh điển đặt nền móng toán học và lý thuyết thuật toán cho Bảo mật vi sai (Differential Privacy - DP).

---

## 1. Siêu dữ liệu Học thuật (Academic Metadata)

| Thuộc tính | Chi tiết xác thực từ API |
|---|---|
| **Tác giả (Authors)** | Cynthia Dwork, Aaron Roth |
| **Năm xuất bản (Year)** | 2014 |
| **Nhà xuất bản / Tạp chí (Venue)** | Foundations and Trends® in Theoretical Computer Science |
| **DOI** | [10.1561/0400000042](https://doi.org/10.1561/0400000042) |
| **OpenAlex ID** | [https://openalex.org/W4205228770](https://openalex.org/W4205228770) |
| **Semantic Scholar ID** | [0023582fde36430c7e3ae81611a14e558c8f4bae](https://www.semanticscholar.org/paper/0023582fde36430c7e3ae81611a14e558c8f4bae) |
| **Số lượt trích dẫn OpenAlex** | **11,470** trích dẫn |
| **Số lượt trích dẫn Semantic Scholar** | **10,679** trích dẫn (1872 trích dẫn có ảnh hưởng sâu sắc) |
| **Lĩnh vực cốt lõi (Concepts)** | Differential privacy, Computer science, Differential (mechanical device), Internet privacy, Computer security, Engineering, Data mining, Aerospace engineering |

---

## 2. Tóm tắt Học thuật (Abstract & Summary)

### Tóm tắt cốt lõi (TLDR)
> **TLDR (Semantic Scholar AI):** The preponderance of this monograph is devoted to fundamental techniques for achieving differential privacy, and application of these techniques in creative combinations, using the query-release problem as an ongoing example.

### Toàn văn Abstract (Nguyên văn từ tác giả)
The problem of privacy-preserving data analysis has a long history spanning multiple disciplines. As electronic data about individuals becomes increasingly detailed, and as technology enables ever more powerful collection and curation of these data, the need increases for a robust, meaningful, and mathematically rigorous definition of privacy, together with a computationally rich class of algorithms that satisfy this definition. Differential Privacy is such a definition. After motivating and discussing the meaning of differential privacy, the preponderance of this monograph is devoted to fundamental techniques for achieving differential privacy, and application of these techniques in creative combinations, using the query-release problem as an ongoing example. A key point is that, by rethinking the computational goal, one can often obtain far better results than would be achieved by methodically replacing each step of a non-private computation with a differentially private implementation. Despite some astonishingly powerful computational results, there are still fundamental limitations — not just on what can be achieved with differential privacy but on what can be achieved with any method that protects against a complete breakdown in privacy. Virtually all the algorithms discussed herein maintain differential privacy against adversaries of arbitrary computational power. Certain algorithms are computationally intensive, others are efficient. Computational complexity for the adversary and the algorithm are both discussed. We then turn from fundamentals to applications other than queryrelease, discussing differentially private methods for mechanism design and machine learning. The vast majority of the literature on differentially private algorithms considers a single, static, database that is subject to many analyses. Differential privacy in other models, including distributed databases and computations on data streams is discussed. Finally, we note that this work is meant as a thorough introduction to the problems and techniques of differential privacy, but is not intended to be an exhaustive survey — there is by now a vast amount of work in differential privacy, and we can cover only a small portion of it.

---

## 3. Đóng góp Phương pháp luận & Khái niệm then chốt

### Đóng góp nền tảng
Chuyên khảo kinh điển đặt nền móng toán học và lý thuyết thuật toán cho Bảo mật vi sai (Differential Privacy - DP). Tài liệu này thiết lập các nguyên lý vững chắc, giúp định hình tiêu chuẩn thực hành và phương pháp luận nghiên cứu dữ liệu y sinh trên phạm vi toàn cầu.

### Các khái niệm cốt lõi cần nắm vững
- **Khái niệm chính:** Các định nghĩa và kiến trúc phương pháp luận được văn bản gốc bảo chứng.
- **Tiêu chuẩn dữ liệu:** Định vị mối liên hệ với các chuẩn thông tin y tế quốc tế và các yêu cầu quản lý thực nghiệm.
- **Tính khả thi:** Đảm bảo khả năng chuyển giao và áp dụng trong môi trường nghiên cứu lâm sàng.

---

## 4. Ánh xạ và Tích hợp vào Sách Chuyên khảo Biomedical RDM

### Vị trí và Phạm vi trong Chuyên khảo
- **Chương mục cụ thể:** Mục 5.3: Bảo mật vi sai (Differential Privacy) trong chia sẻ dữ liệu y tế
- **Giai đoạn Vòng đời dữ liệu:** Giai đoạn 5 (Phân tích) và Giai đoạn 6 (Chia sẻ dữ liệu thống kê)

### Ứng dụng Sư phạm & Luận điểm triển khai
Giải thích định nghĩa toán học $(\varepsilon, \delta)$-DP: kết quả phân tích thống kê hầu như không thay đổi dù một cá nhân cụ thể có tham gia hay không tham gia vào bộ dữ liệu; cách tiêm nhiễu Laplace/Gaussian tương ứng với độ nhạy toàn cục (global sensitivity).

### Cảnh báo Bẫy thực tế (Pitfalls & Misconceptions)
> [!WARNING] **Bẫy thực tế cần phòng tránh khi áp dụng:**  
> Coi bảo mật vi sai là 'giải pháp vạn năng' không có đánh đổi; trên thực tế, giảm $\varepsilon$ để tăng bảo mật sẽ làm tăng nhiễu, có thể phá hủy độ chính xác của các phân tích dịch tễ trên mẫu nhỏ hoặc bệnh hiếm.

---

## 5. Trích dẫn Chuẩn mực (Citations & References)

### Định dạng APA 7th Edition
```text
Cynthia Dwork & Aaron Roth (2014). The Algorithmic Foundations of Differential Privacy. *Foundations and Trends® in Theoretical Computer Science*. https://doi.org/10.1561/0400000042
```

### Bản ghi BibTeX
```bibtex
@book{dwork2014algorithmic,
  title = {{The Algorithmic Foundations of Differential Privacy}},
  author = {Cynthia Dwork and Aaron Roth},
  year = {2014},
  publisher = {Foundations and Trends® in Theoretical Computer Science},
  doi = {10.1561/0400000042},
}
```
