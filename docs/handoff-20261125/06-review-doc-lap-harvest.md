## 1. Tóm tắt 10 dòng

1. Kết luận Gate 1: **CHƯA NÊN PHÊ DUYỆT**, nên giữ trạng thái EXPLORE.
2. Cấu hình có 17 chủ đề; Boolean OpenAlex hiện nhìn chung hợp lệ, chưa thấy lỗi ngoặc hoặc ưu tiên AND/OR.
3. Logic khử trùng lặp chưa đáp ứng workflow vì không dùng đồng thời DOI, tác giả và năm.
4. Có rủi ro lộ OpenAlex API key qua query URL.
5. t12b cho kết quả nhiễu rõ rệt; từ khóa `Vietnam` bắt nhiều nghiên cứu Chiến tranh Việt Nam và y tế không liên quan.
6. Giao thức đã nêu PCC, tiêu chí nhận/loại, Gate 1/2/3.5 và metadata-only, nhưng còn thiếu đặc tả vận hành.
7. Mẫu “20% hoặc 100 bản ghi, lấy số lớn hơn” không khả thi khi mỗi API chỉ lấy 25 bản ghi.
8. Cohen’s kappa chỉ phù hợp cho hai bộ quyết định độc lập; AI không nên được mô tả như người sàng lọc thứ hai.
9. Các con số 836, 16 và 14 trong báo cáo có thể tái lập từ các file harvest; báo cáo lại ghi sai số chủ đề ở một chỗ.
10. Khuyến nghị thêm PubMed/Europe PMC cho phần y-sinh, thu hẹp t03/t04/t09/t12, rồi mới mở Gate 2.

## 2. Phát hiện

### Cao

| ID | Phát hiện, bằng chứng, đề xuất |
|---|---|
| H-01 | **Khử trùng lặp có thể tạo bản ghi trùng hoặc gộp nhầm.** `scripts/lit_harvest.py:244-282` dùng DOI hoặc tiêu đề đã chuẩn hóa; không dùng tác giả/năm khi thiếu DOI. Ngoài ra, nếu OpenAlex có DOI nhưng Semantic Scholar chỉ có tiêu đề thì hai bản ghi có thể không được gộp; chiều ngược lại lại được xử lý ở dòng 270-272. `norm_title()` tại dòng 92-94 còn loại bỏ toàn bộ ký tự ngoài ASCII, dễ làm hỏng tiêu đề tiếng Việt. Đề xuất dùng khóa DOI chuẩn hóa; nếu thiếu DOI, dùng fuzzy title + first author + year, phù hợp workflow tại `literature-review.md:67-71`. |
| H-02 | **API key OpenAlex được gửi trong URL.** `scripts/lit_harvest.py:66-70` thêm `api_key` vào query string. Dù key không được ghi file, URL có thể xuất hiện trong proxy/server/request logs. Đề xuất chuyển key sang header `Authorization`, hoặc tối thiểu ghi rõ rủi ro và bảo đảm không log URL. AGENTS yêu cầu không đưa secrets/credentials vào artefact (`AGENTS.md:17`). |
| H-03 | **Cỡ mẫu hiện tại không đủ để thực hiện tiêu chí screening đã viết.** Mỗi nguồn chỉ lấy 25 bản ghi (`scripts/lit_harvest.py:239-251`, `:262-267`), nhưng PROTOCOL yêu cầu tối thiểu `20% hoặc 100 bản ghi cho mỗi chủ đề` (`PROTOCOL.md:40-43`). Với 50 bản ghi sau hợp nhất, “100” không thể đạt nếu không mở rộng truy xuất. Cần quyết định rõ: lấy toàn bộ 50, tăng `per_source`, hoặc đổi ngưỡng trước Gate 1. |
| H-04 | **t12b là truy vấn nhiễu và không thích hợp cho kết luận pháp lý.** `references/lit_search_config.json:32-33`; kết quả đầu tiên gồm nghiên cứu “Vietnam Experience Study”, combat injuries, anxiety và các bài không liên quan (`t12b-vietnam-data-protection.md:19-33`). Đây là bằng chứng trực tiếp rằng `Vietnam` không đủ để đại diện cho pháp luật Việt Nam. Đề xuất bổ sung cụm pháp lý/chính sách như “personal data protection law”, “electronic medical record”, “privacy”, tên văn bản Việt Nam; đồng thời dùng nguồn chính phủ cho kết luận pháp lý. |

### Trung bình

| ID | Phát hiện, bằng chứng, đề xuất |
|---|---|
| M-01 | **Báo cáo người soạn tự mâu thuẫn về số chủ đề.** Báo cáo ghi “16 chủ đề” tại `docs/handoff-20261125/04-literature-harvest-review.md:7`, nhưng cùng báo cáo ghi 17 ở dòng 31; cấu hình thực tế có 17 topic, từ t01–t16 và t12b. Sửa số liệu trước khi dùng báo cáo làm hồ sơ review. |
| M-02 | **Các con số tổng hợp chính đúng, nhưng phạm vi ý nghĩa cần ghi rõ hơn.** Đối chiếu các file `t*.md`: tổng số dòng kết quả duy nhất là **836**; tổng `có ở cả hai nguồn` là **14**; tổng `đã có trong .bib` là **16**. Các số này khớp báo cáo tại `docs/handoff-20261125/04-literature-harvest-review.md:31-34`. Tuy nhiên, đây là hợp nhất của tối đa 25 kết quả mỗi nguồn/chủ đề, không phải toàn bộ kết quả truy vấn. |
| M-03 | **`in_bib` có thể khớp sai theo tiêu đề.** `scripts/lit_harvest.py:282` và `:295` coi bản ghi là có trong bibliography nếu tiêu đề chuẩn hóa giống nhau, không kiểm tra tác giả/năm. Cần đổi nhãn thành `possible_bib_match` cho trường hợp chỉ khớp tiêu đề, hoặc yêu cầu DOI/tác giả/năm xác nhận. |
| M-04 | **Giao thức còn thiếu một số thành phần PRISMA-ScR vận hành.** PROTOCOL đã có mục tiêu/PCC, nguồn, chiến lược, tiêu chí và quy trình charting (`PROTOCOL.md:6-14`, `:25-50`). Nhưng chưa nêu rõ tình trạng đăng ký protocol, mẫu biểu đã hiệu chuẩn, biến dữ liệu được định nghĩa đầy đủ, cách ghi lý do loại từng bản ghi, và lịch sử các lần chạy. PRISMA-ScR yêu cầu mô tả nguồn thông tin, chiến lược tìm kiếm, chọn nguồn và quy trình charting; xem [checklist PRISMA-ScR của EQUATOR](https://equator-network.org/reporting-guidelines/prisma-scr/PRISMA-ScR-checklist.pdf). |
| M-05 | **AI và reviewer thứ hai chưa nhất quán giữa workflow và protocol.** Workflow nêu một mô hình AI cụ thể, tự động phân loại theo confidence và người kiểm 5–10% hàng đợi (`literature-review.md:73-81`); PROTOCOL lại mô tả hai người đọc độc lập và AI chỉ hỗ trợ xếp hạng (`PROTOCOL.md:40-43`). Cần chọn một thiết kế duy nhất, ghi model/version, prompt, ngày chạy, dữ liệu đầu vào và quy tắc adjudication. AI-vs-người soạn có thể đo mức đồng thuận mô tả, nhưng không nên gọi là dual-human screening. Hướng dẫn Cochrane khuyến nghị hai reviewer độc lập cho một phần bản ghi và chỉ chuyển sang single screening khi đồng thuận đủ cao ([Cochrane rapid-review guidance](https://www.bmj.com/content/384/bmj-2023-076335?s=09)). |
| M-06 | **Thiên lệch bao phủ thuật ngữ còn đáng kể.** Ví dụ: t04 thiếu “replication crisis”, “reproducible science”; t05 thiếu “ALCOA+”, audit trail, GCP; t07 thiếu HL7, LOINC, SNOMED CT; t09 thiếu MCAR/MAR/MNAR, missingness; t10 thiếu pseudonymization/anonymisation; t16 thiếu container, workflow provenance, software citation. Cần seed testing và kiểm tra độ nhạy trước Gate 1. |
| M-07 | **Các chủ đề chồng lấn nhưng chưa có quy tắc phân luồng.** Chồng lấn rõ giữa t01/t03, t05/t08, t06/t07/t08, t10/t11/t12/t13, t04/t16 và t12/t12b. Nếu không ghi “primary topic” hoặc quy tắc gán nhiều chủ đề, tổng số theo chủ đề sẽ không thể diễn giải như tổng số nghiên cứu độc lập. |
| M-08 | **Báo cáo ghi nhận nguồn/ngày nhưng chưa ghi đủ provenance cho từng lần xác minh.** `api-enrichment.md:3-5` có ngày chạy và tên hai API, nhưng không có endpoint/query cụ thể, phiên bản schema hay snapshot ID. Đây là metadata exploration, không phải claim verification; cần giữ phân biệt này theo `AGENTS.md:10` và `AGENTS.md:24`. |
| M-09 | **Ghi tên công cụ AI trong artefact.** `PROTOCOL.md:3` ghi “Người soạn: người soạn”; báo cáo ghi tác giả người soạn tại dòng 3 và nhiều chỗ khác. Brief yêu cầu không ghi tên công cụ AI; AGENTS cũng cấm credit AI tools trong các artefact công bố (`AGENTS.md:17`). Nên đổi sang mô tả trung tính hoặc bỏ trường tác giả. |

### Thấp

| ID | Phát hiện, bằng chứng, đề xuất |
|---|---|
| L-01 | `esc()` chỉ thoát dấu `|` và newline (`scripts/lit_harvest.py:133-135`). DOI hoặc nội dung tiêu đề chứa ký tự đặc biệt Markdown khác có thể làm bảng/link hỏng. Nên thêm kiểm tra render Markdown hoặc hàm escape đầy đủ. |
| L-02 | `norm_doi()` chỉ loại tiền tố `https://doi.org/` (`scripts/lit_harvest.py:88-90`), chưa xử lý `doi:`, dấu chấm/câu cuối hoặc khoảng trắng đặc biệt. Có thể làm giảm tỷ lệ match DOI. |
| L-03 | Retry HTTP dùng thời gian cố định (`scripts/lit_harvest.py:53-62`, `:73-84`), không dùng `Retry-After` hoặc exponential backoff có jitter. Đây là rủi ro vận hành khi Semantic Scholar trả 429, không phải lỗi số liệu hiện tại. |

## 3. Kiểm tra số liệu

| Hạng mục | Kết quả kiểm tra |
|---|---:|
| Số topic trong `lit_search_config.json` | 17 |
| Bản ghi trong `references.bib`/audit | 115 |
| Mục có DOI | 61 |
| OpenAlex tìm thấy | 56 |
| Semantic Scholar tìm thấy | 54 |
| Tổng bản ghi harvest sau hợp nhất | 836 |
| Có ở cả hai nguồn | 14 |
| Đã có trong `references.bib` | 16 |
| OpenAlex totals theo README | Khớp các số tại `PROTOCOL.md:37` và `harvest/README.md:9-25` |
| Số liệu sai rõ ràng | “16 chủ đề” tại báo cáo dòng 7; đúng phải là 17 |

Không phát hiện code nào ghi vào `references/references.bib` hoặc `references/citation-audit.csv`; docstring và luồng thực thi đều chỉ đọc các file này (`scripts/lit_harvest.py:5-14`, `:96-104`, `:141-177`).

## 4. Khuyến nghị Gate 1, theo thứ hạng

1. **PubMed và Europe PMC: NÊN BỔ SUNG.** Thêm cho các chủ đề y-sinh/lâm sàng, đặc biệt t01, t04–t11, t13–t16; không dùng chúng thay cho nguồn pháp lý chính thức ở t12/t12b. Ghi chi phí là API công khai, nhưng phải đặt rate limit và lưu lịch sử truy vấn.
2. **Tiêu chí nhận/loại: CHƯA ĐỦ ĐỂ PHÊ DUYỆT.** Cần chốt định nghĩa “full text”, xử lý preprint, loại tài liệu, ngôn ngữ, bản rút bài, trùng bản cập nhật, và lý do loại theo từng bản ghi.
3. **Reviewer thứ hai: CHẤP NHẬN AI CHỈ NHƯ KIỂM TRA ĐỘC LẬP BỔ TRỢ.** Dùng một model khác người soạn, chạy mù với quyết định của người soạn; Ben kiểm tra toàn bộ UNCERTAIN và hàng đợi nghi ngờ. Nếu cần Cohen’s kappa có ý nghĩa phương pháp luận, nên có reviewer người thứ hai; không gọi AI là người reviewer.
4. **Thu hẹp truy vấn >10.000: BẮT BUỘC.**
   - t03: ưu tiên `"data steward"`/`"data stewardship"` và thêm bối cảnh nghiên cứu y-sinh thay vì `data governance` quá rộng.
   - t04: dùng `"reproducibility crisis"`/`"replication crisis"`/`"reproducible research"` kết hợp biomedical/preclinical/clinical.
   - t09: giữ `missing data`/`multiple imputation` nhưng bắt buộc clinical trial/EHR/clinical research và thêm missingness.
   - t12: thêm `privacy law`, `personal data`, `health data`, `medical research` và tách nhánh GDPR khỏi truy vấn chung.
5. **Ưu tiên nâng cấp tiếp theo:** ch03 để bổ sung chuẩn thuật ngữ/định dạng (HL7, LOINC, SNOMED CT, CDISC, OMOP); ch06 phải chuyển trọng tâm sang nguồn pháp lý chính thức; ch08 bổ sung phần mềm, provenance và khả năng tái lập tính toán.
6. **Điều kiện dừng/saturation: NÊN BẮT BUỘC.** Ghi trước ngưỡng theo từng chủ đề, ví dụ hai vòng mở rộng liên tiếp không phát hiện bản ghi đủ điều kiện mới, hoặc đã thu hồi hết seed papers và biến thể thuật ngữ đã định trước. Mọi lần dừng phải ghi lý do, ngày và truy vấn.

## 5. Điều chưa kiểm được

- Không chạy lại API OpenAlex/Semantic Scholar, nên chưa xác nhận được tính nhạy của truy vấn và totals hiện tại theo dữ liệu trực tuyến.
- Không kiểm tra được 429, response schema và việc API key có bị ghi trong network/proxy logs.
- Không chạy `quarto render` vì đây là review chỉ đọc và render có thể tạo/ghi artefact.
- Không xác minh nội dung khoa học, DOI, tình trạng rút bài hoặc hiệu lực pháp lý của từng nguồn; các file hiện chỉ là metadata/explore.
- Không đánh giá được chất lượng màn hình Gate 2 vì chưa có dữ liệu screening, lý do loại, evidence matrix hoặc adjudication log.

**Kết luận:** PR #29 có nền tảng tốt cho một harvest EXPLORE, nhưng nên giữ **Gate 1: CONDITIONAL HOLD / chưa phê duyệt** cho đến khi sửa logic khử trùng lặp, xử lý API key, chốt thiết kế reviewer, làm rõ cỡ mẫu và thu hẹp các truy vấn rộng/nhiễu.