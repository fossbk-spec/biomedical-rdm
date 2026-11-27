# Nhật ký thay đổi hạ tầng: quét tên công cụ AI và chuỗi giống khóa — 27/11/2026

## Phạm vi

Thêm `scripts/check_sensitive.py` và bước CI tương ứng để chặn tái phát sinh tên công cụ AI và chuỗi giống khóa trong kho công khai (quy tắc dự án: không ghi tên công cụ AI vào kho công khai; không đưa khóa hay thông tin xác thực). Không đổi chương.

## Thay đổi

| Tệp | Thay đổi |
|---|---|
| `scripts/check_sensitive.py` | Quét các tệp văn bản được theo dõi (bỏ `archive/` và `references/`); báo lỗi với tên công cụ AI và sáu dạng chuỗi giống khóa; chỉ cho phép dòng khớp danh sách cho phép; có `--self-test` |
| `editorial/sensitive-allowlist.txt` | Lượt khớp hợp lệ: OpenAIRE ở ch06 và các bảng harvest, một nhan đề bài báo và một họ tác giả ở harvest, script `audit_nodoi_gemini.py` (mã gọi một API cụ thể) và các dòng nhắc tên tệp/nhánh lịch sử ở `DECISIONS.md`, `PROJECT-STATE.md` |
| `.github/workflows/ci.yml` | Thêm bước chạy self-test và kiểm tra |

## Phụ thuộc

PR này xếp chồng lên PR "Bỏ tên công cụ AI khỏi tài liệu công khai" (#50): nếu chưa có #50, kiểm tra sẽ báo các tệp mà #50 sửa.

## Giới hạn

Không quét lịch sử git và thông điệp commit; không quét tệp nhị phân. Danh sách chặn là các tên cố định; tên mới phải thêm vào script.
