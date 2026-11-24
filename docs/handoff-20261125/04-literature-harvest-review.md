# Thăm dò literature review bằng OpenAlex và Semantic Scholar: kết quả và hệ quả cho quy trình biên soạn

**Tác giả:** nhóm biên soạn · **Phiên bản:** 1.1.0 (harvest v0.2 với chuỗi Boolean và giao thức Gate 1) · **Ngày:** 24/11/2026
**Người quyết định:** TS. Hoàng Quang Huy (Ben)
**Loại review:** EXPLORE (theo `DrMayDay/.agents/workflows/literature-review.md`, Bước 0): sơ bộ, chưa sàng lọc, không dùng để trích dẫn trong sách.
**Sản phẩm (nhánh `feat/lit-harvest-20261124`, worktree `biomedical-rdm-wt26`, commit cục bộ, chưa push):**
- `scripts/lit_harvest.py` (hai chế độ `enrich` và `harvest`), `references/lit_search_config.json` (16 chủ đề).
- `docs/literature-review/api-enrichment.md` (115 mục `.bib`, metadata từ hai API).
- `docs/literature-review/harvest/README.md`, `PROTOCOL.md` (giao thức Gate 1), và `t01…t16` cùng `t12b` (mỗi chủ đề một file).

## 1. Cách làm
- API công khai OpenAlex và Semantic Scholar, khóa đọc từ biến môi trường `OPENALEX_API_KEY` và `SEMANTIC_SCHOLAR_API_KEY`; khóa không in ra, không lưu vào file. **Không gửi e-mail hay thông tin cá nhân** (biến `OPENALEX_EMAIL` có sẵn nhưng không dùng, vì chưa được phép).
- **Chỉ lưu metadata** (tác giả, năm, tiêu đề, nơi đăng, DOI, số trích dẫn, trạng thái truy cập mở, cờ rút bài, mã định danh). **Không sao chép tóm tắt** vì bản quyền nhà xuất bản và vì repo công bố theo CC BY 4.0.
- `enrich`: tra theo DOI các mục trong `references/references.bib`. `harvest`: mỗi chủ đề một chuỗi tìm (từ năm 2008), 25 kết quả mỗi API, khử trùng lặp theo DOI rồi theo tiêu đề, xếp hạng theo số trích dẫn cao nhất trong hai nguồn.
- Không sửa `references.bib`, `citation-audit.csv` hay chương nào.

## 2. Kết quả enrich (115 mục `.bib`)
| Hạng mục | Số |
|---|---:|
| Có DOI | 61 |
| Không có DOI (không tra) | 54 |
| Tìm thấy trên OpenAlex | 56 |
| Tìm thấy trên Semantic Scholar | 54 |
| **Bị OpenAlex đánh dấu rút bài** | **0** |
| Năm khác giữa `.bib` và một API | 14 |

- **Mục có DOI nhưng không tìm thấy trên OpenAlex (5):** `ref_017` (Jetten, Zenodo), `ref_022` (DataCite), `ref_050` (Stuart, figshare), `ref_067` (Zenodo) và `ref_107` (thông báo rút bài Surgisphere). Bốn mục đầu là DOI của kho dữ liệu, không phải bài báo; muốn kiểm chúng cần API của nhà cấp DOI (DataCite, Zenodo), không phải hai API này.
- **Không có mục nào bị gắn `is_retracted`.** `ref_108` (thông báo rút bài Surgisphere thứ hai) được OpenAlex phân loại `type = retraction` (518 trích dẫn), tức đúng là thông báo, nên không bị gắn cờ; `ref_107` thì không có bản ghi OpenAlex, còn Semantic Scholar có bản ghi (648 trích dẫn, tiêu đề cần xem lại vì có thể là bài gốc). Đây là điều có chủ ý trong case study, nhưng nghĩa là **cờ rút bài của OpenAlex không thay thế việc kiểm tay**.
- 54 mục không có DOI gồm văn bản pháp luật, chuẩn, báo cáo, trang web; hai API không phủ được nhóm này.

## 3. Kết quả harvest v0.2 (17 chủ đề, chuỗi OpenAlex Boolean + Semantic Scholar từ khóa)
Bản v0.2 thay chuỗi từ khóa thường bằng chuỗi Boolean cho OpenAlex (`title_and_abstract.search`) và ghi tổng số khớp; thêm chủ đề t12b (Việt Nam) để đo độ phủ.
- **836 bản ghi duy nhất** sau khử trùng lặp, **16 bản ghi** đã có trong `references.bib` (0 đến 4 mỗi chủ đề). Chỉ **14** bản ghi xuất hiện ở cả hai API, nên hai API gần như bổ sung hơn là trùng lặp.
- **Tổng số khớp trên OpenAlex theo chủ đề:** từ 343 (t12b) đến 35.325 (t04). Dưới 1.000: t12b, t01, t11, t15, t02, t05, t14. Từ 1.000 đến 6.000: t16, t10, t07, t13, t08, t06. Trên 10.000: t03, t12, t09, t04. Con số "tổng" của Semantic Scholar (hàng trăm nghìn) không dùng được để so sánh.
- **Mức liên quan:** ở v0.1 tôi đã đọc tiêu đề 6 kết quả đầu của 5 chủ đề và thấy đúng chủ đề (ví dụ Kapoor 2023 về rò rỉ dữ liệu và tái lập đứng đầu t04). Ở v0.2 **chưa đọc lại**. Có một dấu hiệu lệch đã thấy: top t12b (Việt Nam) là một bài về công nghệ gây nghiện, không liên quan, vì xếp hạng theo số trích dẫn đưa bài nhiều trích dẫn nhưng ít liên quan lên đầu.
- **Chủ đề pháp lý:** hai API học thuật không phủ văn bản pháp luật Việt Nam (t12, t12b); lớp pháp lý phải đi từ nguồn chính thống.
- Semantic Scholar thỉnh thoảng trả 429; tôi tăng khoảng nghỉ và số lần thử lại, lần cuối đủ 17 chủ đề không lỗi.
- Galaxy xuất hiện ba lần (ba DOI khác nhau, ba bản cập nhật hằng năm); khử trùng lặp theo DOI không gộp chúng, đúng về dữ liệu nhưng cần chú ý khi sàng lọc.

## 4. Hệ quả cho quy trình biên soạn (đề xuất)
1. **Cần Gate 1 trước khi coi harvest là review thật.** Chuỗi tìm hiện do tôi tự đặt (một chuỗi mỗi chủ đề, không MeSH). Ben (và reviewer) duyệt chuỗi tìm trước; nếu không, giữ nhãn EXPLORE.
2. **Cần Gate 2 (sàng lọc) trước khi đưa bất kỳ bản ghi nào vào `references.bib`.** Hiện chỉ 16 trong 836 bản ghi đã có trong `.bib`, nên danh mục 115 mục hiện không phản ánh các bài được trích dẫn nhiều nhất; điều này không tự nó là lỗi (xếp hạng theo trích dẫn thiên về bài cũ), nhưng là lý do để chạy sàng lọc.
3. **Lớp cập nhật (Sổ cập nhật):** harvest và enrich nên được chạy lại theo chu kỳ (mỗi lần khoảng vài phút) để (a) phát hiện bài trong `.bib` bị rút, (b) phát hiện bằng chứng mới cho nhóm `evidence-current`, (c) ghi `checked_at`. Đề xuất đưa `lit_harvest.py enrich` vào chu trình `review_by` của `check_updates`.
4. **Nguồn theo loại:** bài báo thì dùng hai API (và PubMed, Europe PMC như workflow của DrMayDay); văn bản pháp luật, chuẩn, mẫu nhà tài trợ đi từ nguồn chính thống; DOI của kho dữ liệu dùng API của DataCite. Quy trình biên soạn nên ghi rõ nguồn nào cho loại nào.
5. **Bản quyền và công bố:** artifact của harvest chỉ chứa metadata; không lưu tóm tắt trong repo công khai.
6. **Phạm vi chuyên khảo:** harvest cho thấy các mảng có tài liệu phong phú (FAIR, FHIR/CDISC, khử định danh, tái lập tính toán), nên chương tái lập (ch08) có nền tài liệu tốt; chương pháp lý (ch06) cần nguồn khác và cần reviewer pháp lý (đã nêu trong kế hoạch).

## 5. Việc cần Ben quyết
1. Duyệt giao thức `docs/literature-review/harvest/PROTOCOL.md` và 17 chuỗi tìm trong `references/lit_search_config.json` (Gate 1); quyết bổ sung PubMed và Europe PMC; chọn người sàng thứ hai.
2. Cho phép (hoặc không) gửi `mailto` OpenAlex bằng e-mail của bạn để vào "polite pool"; hiện tôi **không gửi**.
3. (Đã làm theo yêu cầu "phương án khoa học và chính xác nhất": push nhánh và mở PR chỉ thêm file; chưa merge.)
4. Gate 2 (sàng lọc) **chưa chạy**, vì quy trình yêu cầu Gate 1 được duyệt trước và có người sàng thứ hai độc lập.

## 6. Giới hạn
- Một chuỗi tìm cho mỗi chủ đề; xếp hạng theo số trích dẫn, không phải mức liên quan hay chất lượng.
- Chưa sàng lọc, chưa đọc nội dung các bài; mức liên quan đánh giá qua tiêu đề của một số kết quả đầu.
- Số trích dẫn và cờ rút bài lấy từ dữ liệu của bên thứ ba, thay đổi theo thời gian.
- Chưa tra PubMed hoặc Europe PMC (workflow DrMayDay có hai nguồn này); Ben chỉ yêu cầu OpenAlex và Semantic Scholar.
- Chưa kiểm tra bản harvest bằng `check_*` của repo (chúng quét chương, phụ lục; `check_volatile` và `check_crossrefs` vẫn exit 0 sau khi thêm file).
