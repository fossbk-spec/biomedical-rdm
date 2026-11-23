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

## Hình, bảng, công thức và trích dẫn

- Caption dùng dạng `**Hình N. ...**` hoặc `**Bảng N. ...**`; nếu một nhóm có tiểu hình thì dùng `N.a`, `N.b`. Đánh số theo thứ tự xuất hiện trong chương.
- Mỗi hình/bảng phải được gọi trong thân văn bản bằng cụm `Hình N` hoặc `Bảng N`; không dùng caption làm dẫn chiếu duy nhất.
- Trích dẫn đóng dùng `[@key]`; `key` phải có trong `references/references.bib`. Không tạo nguồn từ trí nhớ.
- Đơn vị dùng SI khi phù hợp; viết số và đơn vị nhất quán, không trộn ký hiệu trong cùng một bảng. Ký hiệu toán học được giải thích tại lần đầu và ghi ở `notation.md` nếu xuất hiện trong chương.
- Viết tắt được giải thích lần đầu theo dạng tiếng Việt (English, ABBR), sau đó dùng nhất quán. Ngoại lệ phải có lý do trong `glossary-allowlist.txt`.

## Sơ đồ và quiz

Sơ đồ Mermaid phải có chú thích ngắn, không chứa dữ liệu bệnh nhân thật, và dùng quy tắc tại [`docs/guides/diagrams-math-quiz-web.md`](../docs/guides/diagrams-math-quiz-web.md). Quiz là sản phẩm phái sinh: không lộ đáp án trong tiêu đề/câu hỏi, giải thích bám nguồn chương, và tuân chính sách quiz đã ghi trong `docs/DECISIONS.md`.

Các điểm chưa đủ căn cứ để thành quy tắc chung ghi rõ **cần Ben xác nhận**, không tự suy diễn.
