# Decision log

## 2026-11-21 — Giữ dạng trích dẫn số trong canonical review

- **Quyết định:** Giữ `[n]` trong `docs/literature-review/index.md` cho đợt này; không đổi thân bài canonical và không tạo script chuyển đổi.
- **Lý do:** Thân bài hiện dùng số viết tay, Quarto không được cấu hình để nối `references.bib` với citekey, và yêu cầu hiện tại là audit tính toàn vẹn của hệ số 1..103. Giữ dạng hiện tại là thay đổi nhỏ nhất và không làm thay đổi nội dung khoa học.
- **Rủi ro:** Dạng `[n]` không nối tự động với `references.bib`, không dùng được reverse verifier/citekey workflow và có thể lệch khi chèn hoặc xóa tài liệu.
- **Chi phí/biện pháp giảm rủi ro:** Duy trì `scripts/audit_references.py` để đối chiếu thân bài, `references.bib` và `citation-audit.csv`; mọi lần đổi danh mục phải chạy audit và review diff. Việc chuyển sang `[@ref_NNN]` cần một đợt riêng, có dry-run, render và người duyệt.
