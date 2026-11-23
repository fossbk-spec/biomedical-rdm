# Chính sách review Biomedical RDM

**Phiên bản:** 1.0.0  
**Ngày:** 24/11/2026  
**Mục đích:** Luồng review, điều kiện merge và trạng thái kiểm tra cho RDM.

## Phân luồng

| Thay đổi | Review tối thiểu |
|---|---|
| Chính tả/định dạng không đổi nghĩa | CI và Ben |
| Giải thích, bài tập, quiz | Người phụ trách chương và Ben; thêm chuyên môn nếu đổi nhận định |
| Công thức, số liệu, kết luận y khoa/pháp lý, nguồn | Reviewer chuyên môn phù hợp và Ben |
| Code, lab, pipeline | Reviewer kỹ thuật; thêm reviewer chuyên môn nếu đổi diễn giải |
| Glossary, notation, chapter-map hoặc thay đổi liên chương | Các chương bị ảnh hưởng và ban biên tập; hiện Ben là người duyệt |

## Điều kiện merge

Ben duyệt PR. Các script bắt buộc ghi rõ trong PR/CI: `check_structure.py`, `check_glossary.py`, `check_crossrefs.py`, `check_quizzes.py`, `check_volatile.py`, `build_bib.py`; khi thay bibliography chạy thêm `audit_references.py`. Không đánh dấu Đạt nếu công cụ chưa chạy hoặc chạy lỗi. Chưa dựng `CODEOWNERS`; `owner` và `reviewers` giữ null/rỗng cho đến khi có quyết định đồng tác giả.

## Bốn trạng thái

| Trạng thái | Ý nghĩa |
|---|---|
| Đạt | Đã chạy và đáp ứng tiêu chí |
| Không đạt | Có vi phạm hoặc điều kiện chưa đáp ứng |
| Chưa kiểm tra | Chưa chạy, thiếu dữ liệu, dịch vụ lỗi hoặc chưa đủ thời gian |
| Không áp dụng | Có lý do ghi nhận cho phạm vi thay đổi |

## Mẫu phát hiện

`Mã; vị trí file:dòng; nhận định; nguồn và ngày kiểm; phạm vi đã đọc; mức độ; đề xuất; người xử lý/quyết định/lý do đóng.`

## Đa tác giả

Luồng đa tác giả **chưa áp dụng cho đến khi có danh sách đồng tác giả**. Khi được kích hoạt, mỗi chương có owner và reviewer được ghi trong `chapter-map.yml`; thay đổi liên chương cần các reviewer bị ảnh hưởng.
