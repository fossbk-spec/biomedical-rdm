# Chuẩn biên tập Biomedical RDM

**Phiên bản:** 1.0.0  
**Ngày:** 24/11/2026  
**Mục đích:** Quy ước biên tập dùng chung cho sách chuyên khảo và các sản phẩm phái sinh.

## Phạm vi và nguồn

Sách chuyên khảo là nguồn chân lý; quiz, lab và mini-course là lớp phái sinh. Chỉ tiếng Việt được dùng trong thân sách. Thuật ngữ tiếng Anh ghi lần đầu trong ngoặc và quản lý tập trung trong `glossary.yml`. Quy tắc cố định/cập nhật xem [`docs/plans/RDM_Fixed_vs_Updatable_Content_Plan_v1.0.0_20261121.md`](../docs/plans/RDM_Fixed_vs_Updatable_Content_Plan_v1.0.0_20261121.md).

## Giọng văn và cấu trúc

- Viết rõ, trung tính, có chủ thể; phân biệt dữ kiện, khuyến nghị, ví dụ giả định và điểm chưa chắc chắn.
- Mỗi chương có đúng một tiêu đề cấp 1; tiêu đề cấp 2 đánh số liên tục (`## 1.`, `## 2.`...). Tiêu đề cấp 3 dùng cho phân mục (`### 3.1.`).
- Không đổi ý nghĩa khoa học, pháp lý hoặc phạm vi của chương chỉ vì lý do văn phong. Nội dung chưa kiểm chứng giữ nguyên cờ `[CẦN KIỂM CHỨNG]`, `CONTENT_PENDING`, `BIB_PENDING` hoặc `BLOCKED_INPUT`.
- Số liệu, phiên bản, ngày hiệu lực, URL và quy định có thể thay đổi phải nêu ngày kiểm và đặt ở phần cập nhật/phụ lục theo kế hoạch cố định/cập nhật.

## Khung chương v2 (hai tầng)

Chương có cờ `frame: v2` trong `editorial/chapter-map.yml` dùng khung hai tầng thay cho khung 11 mục (Ben duyệt 27/11/2026). Chương không có cờ giữ khung cũ. `scripts/check_structure.py` kiểm theo cờ này.

- Mục không đánh số: `## Lời mở đầu` (đầu chương) và `## Tài liệu tham khảo` (sau mục X.5).
- Mục cấp 2 đánh số `## X.1.` đến `## X.5.`, X là số chương, liên tục, không thiếu và không thêm. `X.1.` mang nhãn `[Cơ sở]`; `X.2.` đến `X.4.` mang nhãn `[Nâng cao & Case Study]`; `X.5.` là tổng kết, thảo luận, thuật ngữ mới.
- Mục cấp 3 đánh số `X.k.m.` phải thuộc đúng mục `X.k.`; tiêu đề cấp 3 không đánh số được phép.
- Nhật ký thay đổi chỉ ở `editorial/changelog/`, không đặt trong thân chương.
- Quiz giữ định dạng của kho (`scripts/check_quizzes.py`).

## Hình, bảng, công thức và trích dẫn

- Caption dùng dạng `**Hình C.k. ...**` hoặc `**Bảng C.k. ...**`, trong đó `C` là số chương và `k` là số thứ tự trong chương (ví dụ `Hình 2.3`). Không dùng tiểu hình `a`/`b`; mỗi hình có số riêng. Đánh số theo thứ tự xuất hiện trong chương (quyết định của Ben, 24/11/2026).
- Tên gọi: dùng "Chương N" cho sách chuyên khảo; tên "Bài N" chỉ dùng cho mini-course.
- Mỗi hình/bảng phải được gọi trong thân văn bản bằng cụm `Hình C.k` hoặc `Bảng C.k`; không dùng caption làm dẫn chiếu duy nhất.
- Trích dẫn đóng dùng `[@key]`; `key` phải có trong `references/references.bib`. Không tạo nguồn từ trí nhớ.
- Đơn vị dùng SI khi phù hợp; viết số và đơn vị nhất quán, không trộn ký hiệu trong cùng một bảng. Ký hiệu toán học được giải thích tại lần đầu và ghi ở `notation.md` nếu xuất hiện trong chương.
- Viết tắt được giải thích lần đầu theo dạng tiếng Việt (English, ABBR), sau đó dùng nhất quán. Ngoại lệ phải có lý do trong `glossary-allowlist.txt`.

## Thuật ngữ và glossary

Mỗi mục trong `glossary.yml` có `vi_status`: `established` (thuật ngữ tiếng Việt thông dụng), `proposed` (bản dịch đề xuất, chờ Ben xác nhận) hoặc `keep-english` (tên chuẩn hoặc tên riêng dùng nguyên tiếng Anh trong sách; trường `vi` chỉ là diễn giải tham khảo). Phân loại ban đầu là đề xuất, chưa được Ben rà.

## Sơ đồ và quiz

Sơ đồ Mermaid phải có chú thích ngắn, không chứa dữ liệu bệnh nhân thật, và dùng quy tắc tại [`docs/guides/diagrams-math-quiz-web.md`](../docs/guides/diagrams-math-quiz-web.md). Quiz là sản phẩm phái sinh: không lộ đáp án trong tiêu đề/câu hỏi, giải thích bám nguồn chương, và tuân chính sách quiz đã ghi trong `docs/DECISIONS.md`.

Các điểm chưa đủ căn cứ để thành quy tắc chung ghi rõ **cần Ben xác nhận**, không tự suy diễn.
