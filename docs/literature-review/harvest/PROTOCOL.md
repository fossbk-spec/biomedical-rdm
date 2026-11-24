# Giao thức thăm dò literature review cho sách chuyên khảo Biomedical RDM

**Phiên bản:** 0.2.0 (dự thảo, chờ Gate 1) · **Ngày:** 24/11/2026 · **Người soạn:** Claude · **Người quyết định:** TS. Hoàng Quang Huy (Ben)
**Căn cứ quy trình:** `DrMayDay/.agents/workflows/literature-review.md` (Evisyn; Bước 0, Gate 1, Gate 2); báo cáo PRISMA-ScR cho scoping review.

## 1. Loại review và mục đích
- **Loại:** EXPLORE (Bước 0 của workflow). Sau khi Gate 1 được duyệt có thể nâng lên **SCOPING REVIEW** theo PRISMA-ScR (lập bản đồ bằng chứng cho từng chương), **không phải systematic review** (không có đăng ký protocol trước, không chấm nguy cơ sai lệch hay GRADE).
- **Mục đích:** (a) lập danh sách ứng viên tài liệu cho từng chương; (b) đo mức phủ của `references.bib`; (c) cung cấp đầu vào cho lớp "bằng chứng hiện hành" của Sổ cập nhật; (d) kiểm tra API nào phủ được loại nguồn nào.
- **Ràng buộc:** metadata only; không dùng bản ghi nào làm trích dẫn trước khi qua Gate 2; không sửa `references.bib` tự động.

## 2. Câu hỏi và khái niệm (dạng PCC cho scoping review)
- **Population (đối tượng):** nghiên cứu y sinh và lâm sàng, bao gồm thử nghiệm lâm sàng, nghiên cứu quan sát, dữ liệu hồ sơ sức khỏe điện tử.
- **Concept (khái niệm):** quản lý dữ liệu nghiên cứu: kế hoạch dữ liệu, thu thập và toàn vẹn dữ liệu, chuẩn hóa và liên thông, chất lượng và dữ liệu khuyết, khử định danh và bảo mật, FAIR và dữ liệu sẵn sàng cho AI, pháp lý và đạo đức chia sẻ, tái lập tính toán.
- **Context (bối cảnh):** mọi quốc gia; ưu tiên bằng chứng áp dụng được cho bối cảnh Việt Nam; dữ liệu pháp lý Việt Nam không tìm qua các cơ sở dữ liệu học thuật (mục 3).

## 3. Nguồn và vì sao
| Nguồn | Dùng cho | Hạn chế đã quan sát |
|---|---|---|
| OpenAlex (API, có khóa) | metadata, trích dẫn, cờ rút bài, loại tài liệu, mở truy cập; tìm Boolean trong tiêu đề và tóm tắt | không phủ DOI của kho dữ liệu (Zenodo, DataCite, figshare) |
| Semantic Scholar (Graph API, có khóa) | trích dẫn, trích dẫn có ảnh hưởng, tìm theo từ khóa | endpoint tìm kiếm không hỗ trợ Boolean; con số "tổng" không so sánh được với OpenAlex; giới hạn tốc độ (429) |
| **Chưa dùng:** PubMed (E-utilities), Europe PMC | độ phủ y sinh có MeSH | **đề xuất bổ sung ở Gate 1** để tránh thiên lệch cơ sở dữ liệu; Ben quyết |
| Nguồn chính thống (công báo, cổng văn bản pháp luật, NIH, EUR-Lex) | văn bản pháp lý, chính sách, mẫu | không qua API học thuật; xử lý theo `docs/legal-verification.md` |
| API của DataCite, Zenodo | DOI của kho dữ liệu | chưa dựng |

## 4. Tiêu chí chọn (áp dụng ở Gate 2; **chưa áp dụng**)
**Nhận:**
1. Năm công bố từ 2008 (khớp mốc chuẩn FAIR và các mô hình hiện hành); ngoại lệ có chủ đích cho tài liệu kinh điển (ghi lý do).
2. Ngôn ngữ: tiếng Anh; tiếng Việt khi là bằng chứng bối cảnh Việt Nam.
3. Loại: bài báo có bình duyệt, tổng quan, hướng dẫn hoặc báo cáo của tổ chức chuyên môn; preprint chỉ khi gắn nhãn và không có bản bình duyệt thay thế.
4. Nội dung thuộc một trong các khái niệm ở mục 2 và áp dụng cho nghiên cứu y sinh hoặc dữ liệu y tế.

**Loại:** không liên quan chủ đề (ví dụ nghiên cứu sức khỏe cộng đồng chỉ nhắc từ khóa); không có toàn văn hoặc metadata tối thiểu (DOI, tác giả, năm); bản sao trùng; bài bị rút (ghi lại, không dùng làm bằng chứng tích cực); phạm vi quá hẹp (một bệnh viện, một công cụ riêng) mà không có giá trị khái quát hóa.

## 5. Chuỗi tìm (xem `references/lit_search_config.json`, chờ duyệt)
- 17 chủ đề (t01–t16 và t12b), mỗi chủ đề một chuỗi OpenAlex Boolean (`title_and_abstract.search`) và một chuỗi từ khóa Semantic Scholar.
- **Lọc:** từ 2008; OpenAlex: article, review, preprint, book-chapter. Lấy 25 bản ghi đầu theo số trích dẫn giảm dần (OpenAlex) và 25 bản ghi đầu theo độ liên quan (Semantic Scholar).
- **Quy mô tổng số khớp trên OpenAlex** (xem `README.md`): từ 343 đến 35.325 mỗi chủ đề. Theo tổng số khớp OpenAlex: **dưới 1.000 (có thể sàng lọc hết trong một đợt):** t12b (343), t01 (346), t11 (502), t15 (536), t02 (614), t05 (761), t14 (862); **từ 1.000 đến 6.000 (cần thu hẹp chuỗi hoặc lấy mẫu có hệ thống):** t16 (1.523), t10 (2.124), t07 (2.934), t13 (3.544), t08 (3.878), t06 (5.130); **trên 10.000 (quá rộng, bắt buộc thu hẹp):** t03 (11.444), t12 (10.193), t09 (15.867), t04 (35.325). Con số "tổng" của Semantic Scholar không dùng được để so sánh (endpoint trả hàng trăm nghìn kết quả khớp lỏng).
- **Cảnh báo về xếp hạng:** sắp theo số trích dẫn có thể đưa lên các bài nhiều trích dẫn nhưng ít liên quan (ví dụ chủ đề Việt Nam t12b có bản ghi đầu bảng không liên quan). Sàng lọc phải dựa vào nội dung, không dựa vào thứ hạng.

## 6. Quy trình sàng lọc (đề xuất, sau Gate 1)
1. **Bước 3:** gộp và khử trùng lặp hai tầng (DOI chuẩn hóa; tiêu đề và tác giả và năm khi thiếu DOI), lưu `detected_in` để vẽ sơ đồ PRISMA-ScR. Đã có ở mức DOI/tiêu đề.
2. **Bước 4a, tiêu đề và tóm tắt:** hai người sàng độc lập trên mẫu (tối thiểu 20% hoặc 100 bản ghi cho mỗi chủ đề, lấy số lớn hơn), tính độ đồng thuận (Cohen's kappa); bất đồng giải quyết bằng thảo luận. AI chỉ hỗ trợ xếp hàng (gợi ý INCLUDE, EXCLUDE, UNCERTAIN kèm độ tin cậy); **toàn bộ UNCERTAIN và mẫu ngẫu nhiên 10% INCLUDE/EXCLUDE do người duyệt** (Gate 2).
3. **Bước 4b, toàn văn:** bản ghi qua 4a được đọc toàn văn trước khi dùng làm trích dẫn; nguồn chỉ có abstract không dùng để kết luận phương pháp hay khuyến nghị.
4. **Bước 5, trích xuất:** ma trận bằng chứng (loại nghiên cứu, bối cảnh, khuyến nghị, giới hạn); ghi phạm vi đã đọc.
5. **Cổng 3.5 (xác nhận khoảng trống):** tìm bài **phản bác** luận điểm của chương, không chỉ bài ủng hộ.
6. **Kết quả:** chỉ bản ghi qua toàn văn mới được đề xuất đưa vào `references.bib` (qua PR riêng, có `build_bib.py --check` và `audit_references.py`).
7. **Bản quyền:** không lưu tóm tắt trong repo công khai; lưu trích dẫn ngắn có nguồn khi cần.

## 7. Báo cáo (PRISMA-ScR)
Mỗi chủ đề ghi: ngày tìm, chuỗi tìm, nguồn, số khớp, số lấy về, số sau khử trùng lặp, số loại ở 4a (kèm lý do), số vào 4b, số cuối. Đã có một phần trong các file `t*.md`.

## 8. Giới hạn của bản dự thảo này
- Chuỗi tìm do một người (Claude) soạn, chưa có MeSH, chưa thử nghiệm độ nhạy với các bài "seed" đã biết; chưa tính độ nhạy và độ đặc hiệu.
- Chưa có người sàng thứ hai; chưa ai sàng lọc.
- Hai API chỉ lấy 25 bản ghi đầu; chưa phản ánh toàn bộ kết quả.
- Phụ thuộc cơ sở dữ liệu thương mại hoặc bên thứ ba cho số trích dẫn; dữ liệu đổi theo thời gian.
- Không có nguồn cho văn bản pháp luật Việt Nam; xử lý riêng.

## 9. Việc cần Ben duyệt (Gate 1)
1. Duyệt hoặc sửa 17 chuỗi tìm; thêm hoặc bỏ chủ đề.
2. Có bổ sung PubMed và Europe PMC không.
3. Có chấp nhận tiêu chí nhận/loại ở mục 4.
4. Ai là người sàng thứ hai (độc lập với Claude) và mẫu kiểm 20%.
5. Chủ đề rộng (trên 10.000: t03, t04, t09, t12; từ 1.000 đến 6.000: t06, t07, t08, t10, t13, t16): thu hẹp chuỗi hay lấy mẫu.
