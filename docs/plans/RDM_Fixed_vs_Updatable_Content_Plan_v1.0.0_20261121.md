# Tách nội dung chương 1 — Phần cố định và phần cập nhật

**Áp dụng cho:** chương 1, `docs/chapters/ch01_overview_and_dmp.md`  
**Ngày:** 21/11/2026  
**Người quyết định:** Ben

## Quyết định

Giữ trong thân chương các khái niệm, nguyên lý, phương pháp và sự kiện lịch sử; chuyển văn bản pháp luật, mẫu tài trợ, thời hạn lưu trữ, phiên bản chuẩn, công cụ, kho và URL sang các phụ lục cập nhật. Mỗi phụ lục có ngày chốt và ngày rà soát tiếp theo.

Thân chương chỉ trỏ tới `docs/appendices/` khi một khẳng định có thể thay đổi. Phụ lục `legal` là bản đọc ngắn cho người học và trỏ về `docs/legal-verification.md`, là sổ kiểm chứng chi tiết. Nội dung NIH chưa đủ đối chiếu thông tri gốc phải giữ `CONTENT_PENDING` và cờ `[CẦN KIỂM CHỨNG]`.

## Phạm vi đợt này

- Tạo bốn phụ lục slug `legal`, `funder-templates`, `retention`, `standards` và changelog.
- Sửa thân chương 1 để bỏ khẳng định pháp lý/phiên bản hết hạn, ghi rõ số minh họa, dbGaP là kho truy cập có kiểm soát, và dùng mẫu từ phụ lục trong lab.
- Tạo kiểm tra tự động cho các thuật ngữ dễ hết hạn.
- Không sửa chương 2–6.

## Kiểm soát nội dung

Chỉ dùng khóa `[@ref_NNN]` có trong `references/references.bib`. Các chi tiết Begley, Freedman và Surgisphere chưa có mục tương ứng trong bibliography hiện tại nên được giữ như sự kiện cần đối chiếu, kèm cờ kiểm chứng; không thêm nguồn mới trong đợt này.

## Rà soát

Rà soát phụ lục mỗi sáu tháng và ngay khi có văn bản/phiên bản mới. Khóa học xuất bản ở `biomedical-rdm-course`; tài liệu nguồn lưu trong repo gốc.
