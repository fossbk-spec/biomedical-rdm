# Nhật ký thay đổi hạ tầng: khung chương v2 — 27/11/2026

## Phạm vi

Thêm hỗ trợ khung chương hai tầng (v2) cho `scripts/check_structure.py` và ghi quy tắc ở `editorial/style-guide.md`. Không đổi chương nào; chưa chương nào có cờ `frame: v2`, nên kết quả kiểm tra các chương hiện có không đổi.

## Thay đổi

| Tệp | Thay đổi | Lý do |
|---|---|---|
| `scripts/check_structure.py` | Đọc cờ `frame: v2` từ `editorial/chapter-map.yml`; với chương có cờ, kiểm mục `Lời mở đầu`, `X.1.`–`X.5.` (tiền tố đúng, liên tục, nhãn tầng), `Tài liệu tham khảo`, và tiền tố `X.k.m.` của mục cấp 3; chương không có cờ giữ kiểm tra cũ | Quyết định M-03, Q3 (27/11/2026): chương nhập mới dùng khung X.1–X.5, ch01–ch03 chưa đổi vẫn qua kiểm tra |
| `scripts/check_structure.py` (self-test) | Thêm ba ca thử: đọc cờ, khung hợp lệ, khung sai | Bảo đảm kiểm tra bắt đúng lỗi |
| `editorial/style-guide.md` | Thêm mục "Khung chương v2 (hai tầng)" | Ghi quy tắc để người soạn và script cùng một nguồn |

## Đã thử

Chạy hàm kiểm khung v2 trên bản thảo v2 của ch04–ch09: không có lỗi. Ch03 (thiếu PART2) báo lỗi đúng như mong đợi: chỉ có mục 3.1, thiếu Tài liệu tham khảo. Ch01 và ch02 có lỗi caption từ kiểm tra cũ (số bảng/hình), không phải do khung.

## Chưa làm

Đặt cờ `frame: v2` cho từng chương trong PR nhập chương tương ứng (ch04 là PR kế tiếp).
