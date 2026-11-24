# Kiểm tra độ nhạy chuỗi tìm bằng tài liệu mẫu (seed test)

**Ngày chạy:** 2026-11-24 · **Cấu hình:** phiên bản 0.4.1-protocol · **Cách làm:** lấy các mục trong `references.bib` có DOI và có trên OpenAlex làm tài liệu mẫu; thông báo rút bài (`type = retraction`) và bài loại `other` (tin, bình luận) bị loại khỏi mẫu; một mẫu được coi là *bắt được* nếu thỏa ít nhất một chuỗi OpenAlex (`title_and_abstract.search`, từ 2008) của các chương mà nó được dẫn (đã ánh xạ số chương hiện có sang số chương đề xuất).

**Hạn chế:** tài liệu mẫu là danh mục hiện có, vốn được chọn theo cách khác; kết quả đo độ nhạy với danh mục này, không phải với toàn bộ y văn. Không dùng để suy ra độ đặc hiệu. Điều chỉnh chuỗi để bắt mẫu có nguy cơ quá khớp (overfitting); mọi lần điều chỉnh phải ghi lại.

| Chương | Mẫu có DOI | Có trên OpenAlex | Bắt được | Độ nhạy | Không bắt được |
|---|---:|---:|---:|---:|---|
| ch01 (chuỗi: t01, t02, t03, t04) | 7 | 3 | 1 | 33% | `ref_012`, `ref_105` |
| ch02 (chuỗi: t05, t06) | 6 | 6 | 4 | 67% | `ref_023`, `ref_104` |
| ch03 (chuỗi: t07) | 6 | 6 | 5 | 83% | `ref_040` |
| ch04 (chuỗi: t08, t09) | 4 | 3 | 3 | 100% | -; ngoài cửa sổ năm: `ref_031` |
| ch05 (chuỗi: t10, t11) | 1 | 1 | 0 | 0% | `ref_070`; ngoài cửa sổ năm: `ref_068`, `ref_069` |
| ch06 (chuỗi: t13, t14, t15) | 8 | 7 | 7 | 100% | - |

**Tổng theo chương:** 20/26 (77%); một mẫu được dẫn ở nhiều chương được đếm ở mỗi chương.
**Tổng theo mẫu duy nhất:** 19/24 (79%). Tiêu chí của giao thức: ≥ 80% (xem `PROTOCOL.md` mục 6).
