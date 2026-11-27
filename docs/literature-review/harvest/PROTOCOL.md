# Giao thức thăm dò literature review cho sách chuyên khảo Biomedical RDM

**Phiên bản:** 1.0.0 (Gate 1 phê duyệt có điều kiện, xem mục 10) · **Ngày:** 24/11/2026 · **Người quyết định:** TS. Hoàng Quang Huy (Ben); các quyết định Gate 1 dưới đây được đưa ra theo ủy quyền của Ben ngày 24/11/2026 sau một vòng review độc lập, ghi lại ở mục 10.
**Căn cứ quy trình:** `DrMayDay/.agents/workflows/literature-review.md` (Bước 0, Gate 1, Gate 2, Cổng 3.5) và danh mục kiểm PRISMA-ScR.
**Cập nhật v1.1 (26/11/2026, Gate 1 v1.1 đã được Ben duyệt cùng ngày):** xem mục 12; khi mục 12 khác các mục 1 và 7 thì theo mục 12.

## 1. Loại review và mục đích
- **Loại:** EXPLORE (Bước 0 của workflow); nâng lên **scoping review** theo PRISMA-ScR khi Gate 2 được thực hiện. **Không phải systematic review** (không đăng ký protocol trước, không chấm nguy cơ sai lệch, không GRADE).
- **Đăng ký protocol:** chưa đăng ký ở nơi công khai. Giao thức này là bản lưu trong kho mã nguồn (có lịch sử Git làm bằng chứng thời điểm); nếu nâng thành scoping review để công bố, đăng ký trên OSF trước khi sàng lọc.
- **Mục đích:** (a) lập danh sách ứng viên tài liệu theo chương; (b) đo mức phủ của `references.bib`; (c) đầu vào cho lớp "bằng chứng hiện hành" của Sổ cập nhật; (d) kiểm tra từng API phủ loại nguồn nào.
- **Ràng buộc:** chỉ metadata; bản ghi nào cũng không được trích dẫn trong sách trước khi qua Gate 2 và đọc toàn văn; không sửa `references.bib` tự động.

## 2. Câu hỏi và khái niệm (PCC)
- **Population:** nghiên cứu y sinh và lâm sàng (thử nghiệm lâm sàng, nghiên cứu quan sát, dữ liệu hồ sơ sức khỏe điện tử).
- **Concept:** quản lý dữ liệu nghiên cứu: kế hoạch dữ liệu, thu thập và toàn vẹn, chuẩn hóa và liên thông, chất lượng và dữ liệu khuyết, khử định danh và bảo mật, FAIR và dữ liệu sẵn sàng cho AI, pháp lý và đạo đức chia sẻ, tái lập tính toán.
- **Context:** mọi quốc gia; ưu tiên bằng chứng áp dụng được cho Việt Nam. Văn bản pháp luật Việt Nam không tìm qua cơ sở dữ liệu học thuật (mục 3).

## 3. Nguồn thông tin
| Nguồn | Dùng cho | Hạn chế đã quan sát |
|---|---|---|
| OpenAlex (API, khóa gửi trong header) | metadata, trích dẫn, cờ rút bài, mở truy cập; tìm Boolean trong tiêu đề và tóm tắt; lấy mẫu ngẫu nhiên có seed | không phủ DOI của kho dữ liệu (Zenodo, DataCite, figshare); loại tài liệu phân loại khác nhau (ví dụ bài FAIR của Wilkinson là `data-paper`) |
| Semantic Scholar (Graph API, khóa gửi trong header) | trích dẫn, trích dẫn có ảnh hưởng, tìm theo từ khóa | endpoint tìm kiếm không hỗ trợ Boolean; số "tổng" không so sánh được; giới hạn tốc độ (429) |
| **Europe PMC (REST, không cần khóa)** — *thêm theo quyết định G1-1* | độ phủ y sinh (có MEDLINE/PubMed và preprint), Boolean theo trường TITLE/ABSTRACT, trích dẫn | chỉ cho chủ đề y sinh; không phủ văn bản pháp luật |
| PubMed (E-utilities) trực tiếp | | **không dùng ở bước này**: Europe PMC đã lập chỉ mục MEDLINE/PubMed; NCBI khuyến nghị cung cấp e-mail liên hệ, mà dự án không gửi thông tin cá nhân; xem lại nếu cần MeSH |
| Nguồn chính thống (công báo, cổng văn bản pháp luật, NIH, EUR-Lex, eCFR) | văn bản pháp lý, chính sách, mẫu nhà tài trợ | đi theo `docs/legal-verification.md` |
| API DataCite, Zenodo | DOI của kho dữ liệu | chưa dựng |

## 4. Tiêu chí chọn (áp dụng ở Gate 2; chưa áp dụng)
**Định nghĩa dùng chung:**
- *Toàn văn*: tệp toàn văn bài báo hoặc báo cáo mà người sàng lọc đã mở và đọc phần phương pháp và kết quả; chỉ tóm tắt hoặc metadata không phải toàn văn.
- *Bản ghi trùng phiên bản*: cùng một công trình xuất hiện nhiều DOI (preprint và bản đăng, các bản cập nhật hằng năm như Galaxy); gom thành một nhóm, giữ bản đã bình duyệt hoặc bản chính thức mới nhất, ghi các bản còn lại làm phụ.
- *Preprint*: nhận có nhãn "preprint chưa bình duyệt"; loại nếu đã có bản bình duyệt thay thế.

**Nhận:**
1. Năm từ 2008. Tài liệu kinh điển trước 2008 (ví dụ Rubin 1976, Sweeney 2002, Machanavajjhala 2007) bổ sung thủ công qua danh mục, ghi lý do.
2. Ngôn ngữ: tiếng Anh; tiếng Việt khi là bằng chứng bối cảnh Việt Nam.
3. Loại (theo OpenAlex): article, review, preprint, book-chapter, data-paper, report, book, conference-paper. Loại `other` (tin, bình luận) và `retraction` không nhận làm bằng chứng (thông báo rút bài chỉ dẫn khi là chủ đề của case study).
4. Nội dung thuộc một khái niệm ở mục 2 và áp dụng cho nghiên cứu y sinh hoặc dữ liệu y tế (hoặc là nền tảng phương pháp không giới hạn lĩnh vực: FAIR, tái lập, datasheets).

**Loại, ghi mã lý do cho từng bản ghi:** `E1` không liên quan chủ đề; `E2` thiếu metadata tối thiểu (DOI hoặc tác giả hoặc năm) và không truy được; `E3` bản sao trùng; `E4` bài bị rút (ghi lại, không dùng làm bằng chứng tích cực); `E5` phạm vi quá hẹp (một cơ sở, một công cụ) và không khái quát; `E6` ngoài cửa sổ năm không có ngoại lệ; `E7` không có toàn văn truy cập được (chuyển sang hàng đợi tìm bản truy cập).

## 5. Chiến lược tìm và truy xuất
- 17 chủ đề (t01–t16 và t12b) trong `references/lit_search_config.json`: chuỗi OpenAlex Boolean (`title_and_abstract.search`), chuỗi từ khóa Semantic Scholar, chuỗi Europe PMC cho chủ đề y sinh. Mỗi file `t*.md` ghi truy vấn thực tế (không gồm khóa), ngày chạy và số khớp.
- **Thiết kế truy xuất (quyết định G1-4):** tổng khớp OpenAlex ≤ 200 thì lấy toàn bộ; lớn hơn thì lấy **25 bản ghi nhiều trích dẫn nhất cộng 100 bản ghi lấy mẫu ngẫu nhiên có seed cố định (20261124)**. Mẫu ngẫu nhiên dùng để ước lượng cơ cấu kết quả; nhóm nhiều trích dẫn dùng để không bỏ sót công trình trụ cột. Thêm 25 bản ghi của Semantic Scholar (độ liên quan) và 25 của Europe PMC (nhiều trích dẫn). Mỗi bản ghi mang nhãn "Cách lấy".
- **Quy mô theo tổng khớp OpenAlex** (xem `README.md`): từ vài trăm (t12b, t01, t03) đến hàng chục nghìn (t09 hơn 180.000; t10 hơn 25.000; t04 hơn 13.000). Chủ đề trên 10.000 chỉ được dùng ở mức mẫu; không tuyên bố đã bao quát.
- **Khử trùng lặp hai tầng:** DOI chuẩn hóa; nếu thiếu DOI thì tiêu đề chuẩn hóa (giữ chữ có dấu) cộng năm ±1, theo workflow. Khử trùng lặp liên chủ đề được báo ở `README.md`.
- **Xếp hạng theo trích dẫn không phải xếp hạng liên quan**; sàng lọc phải dựa trên nội dung. Đã thấy kết quả nhiễu ở các chủ đề dùng từ khóa hai nghĩa (ví dụ "safe haven" trong tài chính, "Vietnamese" là nhóm dân tộc); các chuỗi đã sửa ở v0.4.1 nhưng vẫn cần sàng lọc.

## 6. Độ nhạy chuỗi tìm (seed test) và điều kiện dừng (quyết định G1-6)
- **Phương pháp:** lấy các mục trong `references.bib` có DOI, có trên OpenAlex, loại `other` và `retraction`, làm tài liệu mẫu; kiểm xem có bị bắt bởi chuỗi của các chương mà nó được dẫn (ánh xạ số chương hiện có sang số chương đề xuất). Kết quả ghi ở `SEED_TEST.md`.
- **Tiêu chí:** độ nhạy theo mẫu duy nhất **≥ 80%**; tối đa **3 vòng** chỉnh chuỗi cho mỗi chủ đề; mỗi vòng ghi vào nhật ký (mục 11). Chỉnh chuỗi chỉ theo lý do khái niệm (từ đồng nghĩa, loại tài liệu, ràng buộc ngữ cảnh), không thêm từ chỉ để bắt một mẫu (tránh quá khớp).
- **Kết quả hiện tại:** xem `SEED_TEST.md`. Các mẫu bị bỏ sót đều có lý do giải thích được (tiêu đề và tóm tắt không chứa khái niệm, hoặc tài liệu kinh điển về quyền riêng tư không nhắc lĩnh vực y tế); không chỉnh chuỗi thêm để tránh quá khớp.
- **Bổ sung bắt buộc:** *truy vết trích dẫn* một vòng (OpenAlex `referenced_works` và `cited_by` của các bài đã qua Gate 2) để bù độ nhạy; dừng khi một vòng không thêm bản ghi đủ điều kiện nào.
- **Điều kiện dừng toàn bộ:** (i) độ nhạy mẫu ≥ 80% hoặc ngoại lệ có lý do; (ii) một vòng truy vết trích dẫn không thêm bản ghi mới đủ điều kiện; (iii) ghi lý do, ngày và truy vấn cuối cùng.

## 7. Quy trình sàng lọc (Gate 2; **chưa bắt đầu**)
1. **Bước 4a (tiêu đề và tóm tắt):** một mô hình AI độc lập (không phải mô hình đã soạn chuỗi tìm), **mù với quyết định của người soạn**, gán `INCLUDE`, `EXCLUDE` hoặc `UNCERTAIN`, kèm độ tin cậy, mã lý do loại và trích dẫn ngắn làm bằng chứng (tóm tắt chỉ đọc tạm, không lưu trong repo). Ghi tên mô hình, phiên bản, câu lệnh (prompt), ngày chạy và dữ liệu đầu vào.
2. **Con người duyệt (Ben hoặc người được Ben chỉ định):** toàn bộ `UNCERTAIN`, toàn bộ trường hợp độ tin cậy dưới 0,85, và **mẫu ngẫu nhiên 10% (tối thiểu 30 bản ghi mỗi chủ đề) của các quyết định tự động**. Mọi bất đồng giải quyết bằng quyết định của người duyệt.
3. **Độ đồng thuận:** Cohen's kappa **giữa quyết định của mô hình và của người duyệt trên mẫu 10%**, báo cáo mô tả. Không gọi đây là "sàng lọc kép bởi hai người"; nếu công bố, ghi rõ thiết kế một người cộng một AI, và xem lại nếu kappa dưới 0,6.
4. **Bước 4b (toàn văn):** bản ghi qua 4a được đọc toàn văn; nguồn chỉ có tóm tắt không dùng để kết luận phương pháp hay khuyến nghị.
5. **Bước 5 (trích xuất):** ma trận bằng chứng (loại nghiên cứu, bối cảnh, kết luận, giới hạn) và ghi phạm vi đã đọc.
6. **Cổng 3.5 (xác nhận khoảng trống):** tìm bài **phản bác** luận điểm của chương, không chỉ bài ủng hộ.
7. **Kết quả:** chỉ bản ghi qua toàn văn được đề xuất đưa vào `references.bib` bằng PR riêng (kèm `build_bib.py --check` và `audit_references.py`).
8. **Bản quyền:** không lưu tóm tắt trong repo công khai.

## 8. Dữ liệu và báo cáo (PRISMA-ScR)
- **Biến dữ liệu mỗi bản ghi:** DOI, tiêu đề, tác giả, năm, nơi đăng, loại, số trích dẫn (ngày lấy), trạng thái mở truy cập, cờ rút bài, nguồn phát hiện, cách lấy, quyết định, mã lý do, người quyết định.
- **Nhật ký lần chạy:** ngày, phiên bản cấu hình, tập lệnh và commit, số khớp và số lấy; lưu ở `README.md` và `SEARCH_LOG`.
- **Sơ đồ PRISMA-ScR:** số bản ghi nhận diện, sau khử trùng lặp, sau 4a, sau 4b, kết quả cuối, theo chủ đề.

## 9. Giới hạn
- Chuỗi tìm do một nhóm soạn, chưa có MeSH; độ nhạy đo bằng mẫu từ danh mục hiện có (không phải toàn bộ y văn), nên chưa biết độ đặc hiệu.
- Mẫu nhiều trích dẫn nhất thiên về bài cũ và cộng đồng lớn; mẫu ngẫu nhiên không thay thế sàng lọc.
- Cơ sở dữ liệu thương mại và bên thứ ba cung cấp số trích dẫn và cờ rút bài; dữ liệu đổi theo thời gian.
- Các chủ đề chồng lấn (t01 và t03, t05 và t08, t10 đến t13, t04 và t16) nên tổng theo chủ đề không phải số nghiên cứu độc lập; mỗi chủ đề có "chương chính".
- Văn bản pháp luật Việt Nam không có trong các API học thuật (t12 và t12b chỉ để đo độ phủ).

## 10. Nhật ký quyết định Gate 1 (24/11/2026)
Các quyết định đưa ra theo ủy quyền của Ben, sau review độc lập (review độc lập, tệp ghi ở kho riêng tư, kết luận "giữ HOLD cho tới khi sửa logic khử trùng lặp, xử lý khóa API, chốt thiết kế reviewer, làm rõ cỡ mẫu, thu hẹp truy vấn").
| Mã | Quyết định | Lý do |
|---|---|---|
| G1-1 | Thêm Europe PMC; không dùng PubMed trực tiếp ở bước này | độ phủ y sinh; Europe PMC không cần khóa hoặc e-mail; PubMed bị Europe PMC bao phủ |
| G1-2 | Tiêu chí mục 4 (có định nghĩa toàn văn, preprint, trùng phiên bản, mã lý do loại) | review nêu thiếu định nghĩa thao tác |
| G1-3 | Thiết kế sàng lọc một mô hình AI độc lập cộng người duyệt, kappa mô tả giữa mô hình và người; **không** gọi là sàng lọc kép | tránh mô tả sai thiết kế; thống nhất workflow và protocol |
| G1-4 | Thiết kế truy xuất: lấy toàn bộ nếu ≤ 200, ngược lại top 25 + mẫu ngẫu nhiên 100 (seed cố định) | sửa mâu thuẫn "20% hoặc 100 bản ghi" với 25 bản ghi mỗi nguồn |
| G1-5 | Thu hẹp chuỗi rộng (t03, t04, t09, t10, t12) bằng cụm danh pháp rõ nghĩa; ghi rõ vẫn rộng ở t09 và t10 | giảm nhiễu; không đủ thu hẹp thì dùng mẫu |
| G1-6 | Điều kiện dừng: độ nhạy mẫu ≥ 80%, tối đa 3 vòng chỉnh chuỗi, một vòng truy vết trích dẫn | review đề nghị saturation định trước |
| G1-7 | Ưu tiên tiếp theo cho chương: ch03 (chuẩn: HL7, LOINC, SNOMED CT, CDISC, OMOP), ch06 (pháp lý: nguồn chính thống), ch08 (tái lập: phần mềm, provenance) | khớp thứ tự nâng cấp chương |

**Điều kiện của phê duyệt có điều kiện:** (1) chỉ dùng ở mức EXPLORE cho tới khi người duyệt thực hiện Gate 2; (2) độ nhạy mẫu ≥ 80% hoặc ngoại lệ có lý do (xem mục 6); (3) kết quả sàng lọc không ảnh hưởng tới `references.bib` trước PR riêng.

## 11. Nhật ký vòng chỉnh chuỗi
| Phiên bản | Thay đổi chính | Lý do |
|---|---|---|
| 0.1 | Chuỗi từ khóa thường, một chuỗi mỗi chủ đề | thăm dò |
| 0.2 | Chuỗi Boolean OpenAlex; thêm t12b | tăng độ chính xác; đo độ phủ Việt Nam |
| 0.3 | Thêm từ đồng nghĩa; tách tầng khái niệm không giới hạn lĩnh vực (FAIR, datasheets); bổ sung loại tài liệu `data-paper`, `report`, `book` | seed test phát hiện bộ lọc loại tài liệu loại bài FAIR (OpenAlex phân loại `data-paper`) |
| 0.4 | OHDSI và OMOP không cần ràng buộc ngữ cảnh; thêm "common data elements"; thêm cụm "preclinical research" cho t04; thêm "health datasets" cho t15; thêm `conference-paper` | từ khóa duy nhất không cần ngữ cảnh; từ đồng nghĩa rõ nghĩa |
| 0.4.1 | Bỏ "safe haven" đơn lẻ (t11); thêm NOT cho t12b | kết quả nhiễu thấy trong harvest (tài chính, nhóm dân tộc) |

## 12. Cập nhật v1.1 (26/11/2026): quyết định và thiết kế Gate 2 (dự thảo)

### 12.1. Quyết định của Ben (26/11/2026, theo bộ câu hỏi duyệt)
- **Loại review:** scoping review theo PRISMA-ScR cho nhánh tài liệu học thuật, **cộng** sổ nguồn chính thống cho văn bản quy phạm (luật, chuẩn, hướng dẫn của nhà tài trợ; không tìm qua API học thuật, xem mục 3). Không gọi là systematic review.
- **Đăng ký protocol:** đăng ký trên OSF **trước khi bắt đầu sàng lọc Gate 2**. Trạng thái: chưa đăng ký; chờ tài khoản OSF và Ben duyệt nội dung giao thức.
- **Thứ tự chương cho Gate 2:** ch03 (chuẩn) → ch02 (thu thập) → ch04 (chất lượng) → ch05 (bảo mật) → ch06 (FAIR; trong ghi chú cũ gọi "ch07" theo cách đánh số trước khi #31 được merge). Ch07 (tái lập) và ch08 (pháp lý VN) làm sau; ch08 chỉ bắt đầu khi có reviewer pháp lý ngoài và đi từ nguồn chính thống.
- **Thiết kế sàng lọc tiêu đề và tóm tắt (thay mục 7 bước 1):** hai mô hình AI độc lập, mỗi mô hình sàng riêng và mù với quyết định của mô hình kia; người duyệt xử lý toàn bộ ca `UNCERTAIN`, ca độ tin cậy dưới 0,85, ca hai mô hình bất đồng, và mẫu ngẫu nhiên 10% (tối thiểu 30 bản ghi mỗi chủ đề) trong số bản ghi cả hai mô hình cùng loại. Báo cáo Cohen's kappa giữa hai mô hình và giữa mô hình với người duyệt (mô tả). Mô hình đề xuất: hai mô hình AI độc lập (tên và mã mô hình ghi ở kho riêng tư; không dùng grounding); tên mô hình phải kiểm bằng danh sách mô hình hiện hành ở ngày chạy.
- **Phân xử bất đồng giữa hai mô hình (quyết định theo phương án chặt chẽ nhất, 26/11/2026):** do **người duyệt** xử lý, không dùng mô hình AI làm người phân xử. Lý do: quyết định G1-3 đòi người sàng lọc độc lập với người soạn chuỗi tìm, và một mô hình thứ ba chỉ độc lập khi chưa từng soạn chuỗi tìm; không thể bảo đảm điều đó cho tác nhân soạn giao thức, vốn tham gia soạn giao thức. Ngoại lệ: dùng mô hình thứ ba chưa từng tham gia soạn chuỗi tìm nếu Ben đồng ý bằng văn bản; ghi tên mô hình và phiên bản vào nhật ký lần chạy.
- **Người duyệt hàng đợi:** Ben hoặc người Ben chỉ định; chuyên gia pháp lý ngoài cho ch08.
- **Dữ liệu:** chỉ lưu metadata và quyết định trong repo công khai; tóm tắt chỉ gửi cho mô hình trong lúc chạy và không lưu.

### 12.2. Câu hỏi nghiên cứu cấp chương, ch03 (dự thảo)
| Mã | Câu hỏi | Nhánh nguồn |
|---|---|---|
| RQ3.1 | CDISC, HL7 FHIR và OMOP CDM khác nhau thế nào về mục đích, kiến trúc, định dạng và từ vựng theo đặc tả chính thức? | chính thống |
| RQ3.2 | Hiện trạng phiên bản và yêu cầu nộp hồ sơ tại ngày tìm là gì (FHIR R4, R5, R6; SDTM và IG; OMOP v5.4; hướng dẫn của FDA, PMDA)? | chính thống |
| RQ3.3 | Bằng chứng nào cho thấy việc ánh xạ giữa các chuẩn (FHIR sang OMOP, FHIR sang CDISC, EHR sang OMOP) khả thi và những giới hạn về độ trung thực? | học thuật (t07) |
| RQ3.4 | Bằng chứng nào ủng hộ phân tích phân tán trên OMOP (nghiên cứu mạng lưới OHDSI) và giới hạn về kiểm soát tiết lộ? | học thuật (t07) |

Nhận định cụ thể của chương và nguồn cần để kiểm: `docs/literature-review/claims/ch03-claims.md`.

### 12.3. Nguồn chính thống dự kiến cho ch03 (chưa mở nguồn nào)
Đặc tả SDTM, SDTMIG và ADaM, ADaMIG của CDISC (ghi phiên bản); lịch sử phát hành và đặc tả FHIR trên hl7.org/fhir; đặc tả OMOP CDM v5.4 và tài liệu từ vựng của OHDSI; hướng dẫn kỹ thuật dữ liệu nghiên cứu của FDA và hướng dẫn tương ứng của PMDA. Mỗi nguồn được ghi vào sổ với ngày truy cập và phạm vi đã đọc.

### 12.4. Việc chờ Ben
1. Duyệt giao thức v1.1 và các câu hỏi RQ3.1 đến RQ3.4 (Gate 1 v1.1).
2. Xác nhận ngân sách API và hai mô hình sàng lọc (mục 12.1); việc phân xử do người duyệt.
3. Tạo hoặc chỉ định tài khoản OSF và đăng ký giao thức.
4. Chỉ định người duyệt hàng đợi Gate 2.
