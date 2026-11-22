# Kết quả đối chiếu trích dẫn với OpenAlex và Semantic Scholar

**Ngày:** 21/11/2026 · **Công cụ:** `scripts/verify_refs.py` (API công khai OpenAlex và Semantic Scholar; không gửi thông tin cá nhân) · **Dữ liệu:** `references/references.bib` (103 mục)

## Phạm vi và độ tin cậy

- Chỉ **56 mục có DOI** được tra theo DOI trên OpenAlex. Đây là kết quả đáng tin: DOI xác định duy nhất một bài. Chi tiết: `references/verification-doi-openalex.csv`.
- 37 mục là văn bản pháp luật, chuẩn, báo cáo, trang web (không phải bài báo) được đánh dấu `NOT_APPLICABLE`.
- 10 mục học thuật còn lại không có DOI trong danh mục nên chỉ tra theo tiêu đề. Kết quả tra tiêu đề (`references/verification-report.csv`) **không được dùng làm xác nhận**, vì dễ khớp nhầm bài khác.
- Semantic Scholar bị giới hạn tốc độ và thường không tìm thấy; chỉ dùng để tham khảo thêm, không quyết định kết luận.
- API không xác nhận được nội dung khẳng định (số liệu, mốc pháp lý). Kết quả này chỉ kiểm tra thư mục (tiêu đề, năm, DOI).

## Tổng hợp (56 mục có DOI)

| Kết quả | Số mục | Ghi chú |
|---|---|---|
| Khớp tiêu đề và năm | 40 | |
| Khớp tiêu đề, lệch năm | 7 | `ref_006`, `021`, `028`, `073`, `091`, `093`, `099`: năm online khác năm số tạp chí (ví dụ REDCap 2008/2009, Weiskopf 2012/2013). Cần quyết định theo quy ước APA, chưa phải lỗi chắc chắn. |
| Khớp một phần (khác cách viết/bản) | 2 | `ref_037` (tên đầy đủ hơn), `ref_056` (OpenAlex ghi bản Draft của Rev. 2) |
| **Không khớp, cần xử lý** | 6 | xem bên dưới |
| DOI không phân giải được trên OpenAlex | 1 | `ref_017` (DOI Zenodo; có thể là DOI phiên bản) |

## Các mục không khớp (cần Ben hoặc người audit xử lý, chưa tự sửa)

| Mục | Vấn đề | Đề xuất |
|---|---|---|
| `ref_045` Wilkinson 2019 | DOI trỏ tới bài *"Evaluating FAIR maturity through a scalable, automated, community-governed framework"*. | Đã sửa tiêu đề theo DOI (PR #21). |
| `ref_103` Lane 2020 | Crossref và PubMed 32864627: *"Risk of hydroxychloroquine alone and in combination with azithromycin in the treatment of rheumatoid arthritis: a multinational, retrospective study"*. | Đã sửa tiêu đề (PR #21). Còn phải đối chiếu số liệu ">950.000 người dùng HCQ, 14 cơ sở dữ liệu" ở Phụ lục A với bài gốc. |
| `ref_072` Clark (Bridge2AI) | bioRxiv: v6 (24/4/2026) tên *"AI-readiness criteria for biomedical data"*; v7 (17/11/2026) tên dài hơn (*…in functional genomics and clinical medicine*). OpenAlex ghi tiêu đề của một phiên bản khác. | Giữ tiêu đề v6, ghi rõ phiên bản khi trích. |
| `ref_067` Utrecht handbook | OpenAlex ghi tên sổ tay "Data Privacy Handbook" (mục đang ghi là chương). | Có thể chấp nhận; ghi rõ là chương |
| `ref_076`, `ref_085` | Khác ngôn ngữ/định dạng tiêu đề (tiếng Đức, tiếng Việt). | Có thể chấp nhận |

Lưu ý: các mục `ref_045` và `ref_103` cũng cho thấy rủi ro chung: tiêu đề trong danh mục 103 mục có thể được viết lại từ trí nhớ hoặc từ bản preprint. Các mục không có DOI (47 mục) cần audit thủ công.
