<!-- page: course/syllabus.md -->
# Đề cương khóa học

## Đối tượng

Sinh viên kỹ thuật y sinh, bác sĩ và nghiên cứu viên mới bắt đầu. Không yêu cầu lập trình.

## Thời lượng

Khoảng 2–3 phút đọc mỗi bài và làm quiz (tổng khoảng 1 giờ).

## Cấu trúc

- M0: Nhập môn và cách học, không có quiz.
- M1–M6: Sáu bài lý thuyết, mỗi bài có 4 câu quiz.
- Quiz cuối khóa: 10 câu về workflow và tình huống.

## Đánh giá

Tổng số 34 câu. Học viên đạt khi đúng ít nhất 24/34 câu và đúng ít nhất 2 trong 3 câu Q1–Q3 của quiz cuối khóa. Học viên nên làm quiz tổng hợp tối đa 2 lần như một hướng dẫn tự học; phiên bản site tĩnh không cưỡng chế và không lưu lịch sử lượt làm.

<!-- page: course/module-0-intro/index.md -->
# Nhập môn và cách học

**Mục tiêu duy nhất của phần này:** sau khi học xong, bạn nắm được **workflow quản lý dữ liệu từ thiết kế đề cương đến kết thúc nghiên cứu** và trả lời được “ở bước này phải làm gì, vì sao, và làm sai thì hậu quả gì”.

**Đối tượng:** sinh viên BME, bác sĩ và nghiên cứu viên mới bắt đầu. Không cần biết lập trình.
**Thời lượng:** khoảng 2–3 phút đọc mỗi bài + quiz (tổng khoảng 1 giờ), 6 bài.
**Nguồn:** tổng hợp từ bản *Tổng hợp literature review — RDM Y Sinh* (20/11/2026). Có 103 mục tham khảo, trong đó một số đang chờ kiểm chứng (xem Roadmap).
**Phạm vi:** chỉ lý thuyết và quiz. Lab, video, dữ liệu mẫu và chứng nhận sẽ bổ sung sau.

---

## Workflow tổng thể — 7 giai đoạn cần nhớ

```
1. Thiết kế & DMP → 2. Thu thập → 3. Xử lý & làm sạch
→ 4. Chuẩn hóa (CDISC / FHIR / OMOP) → 5. Phân tích & tái lập
→ 6. FAIR & chia sẻ → 7. Lưu trữ & hủy an toàn
```

Quy tắc xuyên suốt: **quyết định càng sớm càng rẻ**. Một trường dữ liệu không định nghĩa ở bước 1 sẽ thành dữ liệu khuyết, không so sánh được, hoặc không dùng được cho AI ở các giai đoạn sau. DMP không phải thủ tục hành chính — nó là bản hợp đồng về dữ liệu của cả nghiên cứu.

**Bốn lớp ngang:** quản trị dữ liệu; bảo mật và quyền riêng tư; pháp lý và đạo đức; vai trò Data Steward. Cả bốn áp dụng ở mọi giai đoạn của vòng đời dữ liệu, từ lập kế hoạch đến lưu trữ hoặc tiêu hủy; đây không phải một bước chỉ làm ở cuối.

| Giai đoạn / lớp ngang | Bài học trong khóa này |
|---|---|
| 1. Thiết kế & DMP | Bài 1 |
| 2. Thu thập | Bài 2 |
| 3. Xử lý & làm sạch | Bài 4 |
| 4. Chuẩn hóa | Bài 3 |
| 5. Phân tích & tái lập | Bài 4 (phần tái lập); chưa có bài riêng trong khóa này |
| 6. FAIR & chia sẻ | Bài 5 |
| 7. Lưu trữ & hủy an toàn | Bài 5 (kết thúc nghiên cứu) |
| Lớp ngang: quản trị, Data Steward | Bài 1 |
| Lớp ngang: bảo mật, pháp lý, đạo đức | Bài 6 |

---

<!-- page: course/module-1-dmp/index.md -->
# Bài 1 — Thiết kế nghiên cứu và Kế hoạch quản lý dữ liệu (DMP)

**Mục tiêu:** viết được DMP theo mẫu NIH hiện hành (7 yếu tố) hoặc Horizon Europe cho một nghiên cứu giả định; phân biệt được DMP, protocol và CRF.

## Nội dung chính

Lớp kiểm soát bảo mật, đạo đức và pháp lý áp dụng xuyên suốt mọi giai đoạn của vòng đời dữ liệu.

Một nghiên cứu bắt đầu bằng câu hỏi lâm sàng, nhưng dữ liệu bắt đầu bằng **Data Management Plan (DMP)** — tài liệu mô tả dữ liệu nào sẽ thu thập, ở định dạng nào, lưu ở đâu, ai được truy cập, chia sẻ ra sao, và lưu bao lâu.

Nhà tài trợ lớn yêu cầu DMP từ lúc nộp hồ sơ. Khi soạn thảo, dùng **mẫu NIH hiện hành (7 yếu tố) hoặc Horizon Europe**; xem `../appendices/funder-templates.md` để biết phạm vi và trạng thái kiểm chứng. Horizon Europe nhấn mạnh nguyên tắc “mở tối đa có thể, đóng tối thiểu khi cần thiết”.

Ba thứ thường bị nhầm với nhau:

- **Protocol (đề cương):** nghiên cứu *làm gì, vì sao, trên ai*.
- **DMP:** dữ liệu *là gì, ở đâu, ai dùng, chia sẻ thế nào*.
- **CRF / eCRF:** biểu mẫu *thu thập từng trường dữ liệu* của từng người tham gia.

Trước khi thu thập, cần thống nhất ba thứ: **từ điển dữ liệu** (mỗi biến nghĩa là gì, đơn vị nào, giá trị nào hợp lệ), **Common Data Elements (CDE)** — các biến chuẩn dùng chung để so sánh giữa các nghiên cứu, và **metadata** — dữ liệu mô tả dữ liệu (ai thu thập, khi nào, bằng công cụ nào, phiên bản nào). Không có metadata, dữ liệu sau 2 năm sẽ không ai hiểu nổi, kể cả chính người thu thập.

**Điểm cần nhớ:** DMP có vòng đời riêng — soạn thảo, phê duyệt, rà soát định kỳ, cập nhật khi protocol thay đổi. DMP viết xong rồi cất tủ là DMP chết.

<!-- page: course/module-1-dmp/quiz.md -->
# Quiz — Bài 1

**1.1. DMP khác protocol ở điểm nào?**
- A. Protocol nói nghiên cứu làm gì; DMP nói dữ liệu được quản trị ra sao trong nghiên cứu.
- B. Protocol và DMP mô tả nội dung tương tự, nhưng khác cách trình bày trong quản trị dữ liệu.
- C. DMP mô tả kế hoạch phân tích, còn protocol mô tả cách lưu trữ dữ liệu ở từng giai đoạn.
- D. DMP phù hợp khi nghiên cứu có dữ liệu mở hoặc dùng công cụ AI trong một số trường hợp.
- **Đáp án: A.** Protocol tập trung vào câu hỏi và quy trình nghiên cứu; DMP tập trung vào dữ liệu, người dùng và chia sẻ.

**1.2. Vì sao cần lập DMP/DMSP trước khi thu thập dữ liệu?**
- A. Để có thể bỏ qua việc thống nhất biến nếu biểu mẫu đã có sẵn.
- B. Để thống nhất dữ liệu cần thu, metadata, lưu trữ và chia sẻ trước khi quyết định thượng nguồn.
- C. Để thay thế protocol bằng một tài liệu ngắn hơn và dễ phê duyệt hơn.
- D. Để chọn kho lưu trữ trước, còn chất lượng dữ liệu tính sau khi thu thập.
- **Đáp án: B.** Lập kế hoạch sớm giúp các quyết định về biến, metadata, lưu trữ và chia sẻ nhất quán từ đầu.

**1.3. Vì sao cần metadata?**
- A. Để biến các trường dữ liệu thành cùng một kiểu và cùng một đơn vị khi phân tích.
- B. Để thay thế trực tiếp từ điển dữ liệu và nhật ký xử lý trong nghiên cứu.
- C. Để giữ lại ngữ cảnh về cách dữ liệu được thu thập, mô tả và sử dụng.
- D. Để dữ liệu cần metadata khi được công bố công khai hoặc chia sẻ có kiểm soát.
- **Đáp án: C.** Metadata giúp người khác hiểu dữ liệu và đánh giá khả năng tái sử dụng sau này.

**1.4. Tình huống:** Một nghiên cứu ghi huyết áp bằng “120/80”, “120” hoặc “cao”. Cách phòng lỗi phù hợp nhất là gì?
- A. Chọn một cách ghi sau khi phân tích để bảng dữ liệu ngắn hơn và dễ đọc hơn.
- B. Giữ nguyên các cách ghi vì chúng đều phản ánh một lần đo.
- C. Chuyển các giá trị sang văn bản để giữ lại thông tin ban đầu trong bảng.
- D. Thống nhất định nghĩa biến, từ điển dữ liệu và đơn vị trước khi thu thập.
- **Đáp án: D.** Chuẩn hóa biến và đơn vị ở bước thiết kế giúp dữ liệu nhất quán ngay khi được thu thập.

---

<!-- page: course/module-2-collection/index.md -->
# Bài 2 — Thu thập dữ liệu: ALCOA+, GCP và EDC

**Mục tiêu:** giải thích được ALCOA+; phân biệt được thu thập tốt và thu thập chỉ “đủ dùng”.

## Nội dung chính

Lớp kiểm soát bảo mật, đạo đức và pháp lý áp dụng xuyên suốt mọi giai đoạn của vòng đời dữ liệu.

Dữ liệu nghiên cứu lâm sàng phải đáng tin trước tòa, trước hội đồng đạo đức và trước tạp chí. Khung cổ điển là **ALCOA** — Attributable (quy được cho ai), Legible (đọc được), Contemporaneous (ghi ngay lúc xảy ra), Original (bản gốc), Accurate (chính xác). **ALCOA+** thêm Complete (đầy đủ), Consistent (nhất quán), Enduring (bền vững), Available (truy xuất được). Một số hướng dẫn thêm Traceable (truy vết được) thành ALCOA++.

**ICH E6(R3) Good Clinical Practice** (Step 4, 06/01/2025) là chuẩn GCP hiện hành, với 11 nguyên tắc. Annex 1 có mục mới về data governance và hệ thống máy tính — điều mà bản R2 không có. Thu thập hiện nay chủ yếu qua **EDC (Electronic Data Capture)** như REDCap: biểu mẫu điện tử có kiểm tra giá trị ngay khi nhập, có audit trail ghi ai sửa gì, khi nào.

Ba sai lầm phổ biến ở bước này:

1. **Ghi sau, ghi hộ, ghi lại từ trí nhớ** — vi phạm Contemporaneous và Attributable.
2. **Sửa dữ liệu không để lại dấu vết** — vi phạm Original và Traceable; mọi sửa đổi phải có lý do và audit trail.
3. **Kiểm tra chất lượng 100% thủ công** — tốn kém mà không tăng chất lượng tương xứng; xu hướng hiện nay là **Risk-Based Quality Management (RBQM)**: tập trung kiểm tra vào dữ liệu và quy trình rủi ro cao nhất.

**Điểm cần nhớ:** dữ liệu tốt không phải dữ liệu không có lỗi, mà là dữ liệu mà mọi lỗi đều được phát hiện, ghi lại và xử lý có thể truy vết.

<!-- page: course/module-2-collection/quiz.md -->
# Quiz — Bài 2

**2.1. “Complete” trong ALCOA+ nghĩa là gì?**
- A. Dữ liệu được nhập lại nhiều lần để chứng minh không có sai sót trong bản ghi.
- B. Dữ liệu đầy đủ các trường bắt buộc và bản ghi liên quan cần thiết.
- C. Dữ liệu được công khai để người dùng có thể kiểm tra tính đầy đủ của bộ dữ liệu.
- D. Dữ liệu giữ lại những bản ghi đã được xác nhận là đúng và có liên quan.
- **Đáp án: B.** “Complete” nhấn mạnh việc giữ đủ thông tin và bản ghi liên quan, không chỉ giữ các giá trị đẹp.

**2.2. Vì sao sửa dữ liệu phải để lại audit trail?**
- A. Để xác nhận các thay đổi đều làm tăng số lượng bản ghi trong tệp và nhật ký.
- B. Để cho phép ghi đè giá trị cũ khi có người sửa dữ liệu trong hệ thống.
- C. Để truy vết ai sửa, sửa gì, khi nào và vì sao trong suốt vòng đời dữ liệu.
- D. Để thay thế việc kiểm tra chất lượng bằng một nhật ký thay đổi.
- **Đáp án: C.** Audit trail giữ bằng chứng về thay đổi và hỗ trợ các thuộc tính Original, Traceable của dữ liệu.

**2.3. RBQM khác kiểm tra 100% thủ công ở điểm nào?**
- A. RBQM kiểm tra các trường dữ liệu với cùng một mức độ trong từng nghiên cứu.
- B. RBQM không cần quy trình phát hiện và xử lý sai lệch dữ liệu.
- C. RBQM thường dùng khi nghiên cứu có hệ thống thu thập dữ liệu điện tử.
- D. RBQM tập trung nguồn lực vào dữ liệu và quy trình có rủi ro cao hơn.
- **Đáp án: D.** RBQM ưu tiên kiểm soát theo rủi ro thay vì phân bổ cùng một mức kiểm tra cho mọi phần.

**2.4. Tình huống:** Một điều dưỡng ghi nhiệt độ vào giấy nháp cuối ca rồi hôm sau nhập hệ thống. Vi phạm nguyên tắc nào nhất?
- A. Contemporaneous, vì dữ liệu không được ghi ngay khi sự việc xảy ra.
- B. Available, vì dữ liệu trên giấy không thể được lưu trữ lâu dài.
- C. Original, vì dữ liệu điện tử không thể được xem là bản ghi gốc.
- D. Accurate, vì giá trị nhập sau sẽ có sai số so với bản ghi nháp.
- **Đáp án: A.** Ghi chậm làm tăng nguy cơ sai sót và làm yếu bằng chứng về thời điểm quan sát.

---

<!-- page: course/module-3-standards/index.md -->
# Bài 3 — Chuẩn dữ liệu: CDISC, FHIR và OMOP bổ trợ nhau

**Mục tiêu:** nói được mỗi chuẩn dùng để làm gì, và vì sao không chọn chỉ một chuẩn.

**Lớp kiểm soát bảo mật, đạo đức và pháp lý áp dụng xuyên suốt mọi giai đoạn của vòng đời dữ liệu.**

## Nội dung chính

Ba chuẩn lớn nhất thường bị hiểu là đối thủ của nhau. Thực ra chúng bổ trợ nhau, mỗi chuẩn giải một bài toán khác:

- **CDISC (đặc biệt SDTM):** chuẩn để **nộp hồ sơ** cho cơ quan quản lý. Dữ liệu thử nghiệm lâm sàng được chuyển thành dạng bảng chuẩn để FDA/EMA đọc được.
- **FHIR (HL7):** chuẩn để **trao đổi lâm sàng theo thời gian thực** giữa các hệ thống bệnh viện. FHIR R4 (2019) là bản dùng trong thực hành; R5 ban hành 26/03/2023; **R6 chưa ban hành, đang trong giai đoạn ballot**.
- **OMOP CDM (OHDSI):** mô hình dữ liệu chung để **phân tích quần thể** trên nhiều cơ sở dữ liệu. OMOP CDM v5.4 (09/2021) là bản tham chiếu. Mạng lưới OHDSI cuối 2025: 4.833 cộng tác viên ở 88 quốc gia, 544 nguồn dữ liệu ở 54 quốc gia, 974 triệu hồ sơ bệnh nhân duy nhất.

Ba chức năng này bổ trợ nhau: CDISC/SDTM phục vụ nộp hồ sơ, FHIR phục vụ trao đổi lâm sàng, còn OMOP CDM phục vụ phân tích quần thể. Nghiên cứu LEGEND-HTN (Suchard và cộng sự, 2019) minh họa phân tích phân tán trên 4,9 triệu bệnh nhân; mã phân tích được chạy tại từng cơ sở và chỉ gửi thống kê tổng hợp.

SMART on FHIR là lớp ứng dụng chạy trên FHIR: ứng dụng bên thứ ba đọc/ghi dữ liệu EHR qua API chuẩn. FHIR Bulk Data API hỗ trợ xuất dữ liệu quần thể hàng loạt.

**Điểm cần nhớ:** hỏi “nên dùng CDISC hay FHIR hay OMOP?” là hỏi sai. Hỏi đúng là: “dữ liệu này cần đi đâu — nộp hồ sơ, trao đổi lâm sàng, hay phân tích quần thể?”

<!-- page: course/module-3-standards/quiz.md -->
# Quiz — Bài 3

**3.1. CDISC SDTM dùng chủ yếu để làm gì?**
- A. Trao đổi dữ liệu lâm sàng giữa các hệ thống đang vận hành trong thực hành.
- B. Phân tích quần thể từ dữ liệu quan sát của nhiều cơ sở khác nhau.
- C. Chuẩn hóa dữ liệu thử nghiệm lâm sàng để nộp cho cơ quan quản lý.
- D. Lưu trữ ảnh y tế cùng thông tin chẩn đoán của người bệnh.
- **Đáp án: C.** SDTM tổ chức dữ liệu thử nghiệm lâm sàng theo cấu trúc phục vụ việc nộp hồ sơ.

**3.2. FHIR và OMOP có vai trò khác nhau thế nào?**
- A. FHIR dùng để phân tích quần thể, còn OMOP dùng để trao đổi lâm sàng giữa các hệ thống.
- B. FHIR và OMOP đều là mô hình phân tích nên có thể thay thế cho nhau trong một workflow.
- C. FHIR dùng để nộp hồ sơ, còn OMOP dùng để ghi dữ liệu tại điểm chăm sóc trong bệnh viện.
- D. FHIR hỗ trợ trao đổi lâm sàng, còn OMOP hỗ trợ chuẩn hóa và phân tích dữ liệu.
- **Đáp án: D.** Hai chuẩn giải quyết hai nhu cầu khác nhau và có thể cùng xuất hiện trong một workflow.

**3.3. OMOP CDM mạnh nhất ở việc nào?**
- A. Phân tích quần thể trên dữ liệu quan sát đã được chuẩn hóa từ nhiều nguồn.
- B. Ghi nhận thông tin khám chữa bệnh trực tiếp giữa các bệnh viện.
- C. Chuẩn bị hồ sơ thử nghiệm lâm sàng theo cấu trúc nộp cho cơ quan quản lý và đánh giá.
- D. Lưu trữ hình ảnh y tế nguyên bản cùng toàn bộ tín hiệu máy đo.
- **Đáp án: A.** OMOP tạo mô hình chung để các cơ sở có thể phân tích dữ liệu quan sát theo cách tương thích.

**3.4. Tình huống:** Một bệnh viện muốn trao đổi dữ liệu với nơi khác và phân tích xu hướng điều trị. Cách chọn chuẩn phù hợp là gì?
- A. Dùng CDISC cho trao đổi và bỏ qua mô hình phân tích vì dữ liệu đã được gửi đi theo quy trình.
- B. Dùng FHIR cho trao đổi và OMOP cho phân tích, mỗi chuẩn đảm nhiệm một vai trò.
- C. Dùng OMOP cho trao đổi thời gian thực và FHIR cho mọi phân tích dài hạn.
- D. Dùng một chuẩn cho cả trao đổi lâm sàng và phân tích quần thể.
- **Đáp án: B.** FHIR phục vụ trao đổi lâm sàng, còn OMOP phục vụ chuẩn hóa và phân tích quần thể.

---

<!-- page: course/module-4-quality/index.md -->
# Bài 4 — Chất lượng dữ liệu, dữ liệu khuyết và tái lập

**Mục tiêu:** đánh giá được chất lượng dữ liệu theo 5 chiều; xử lý đúng dữ liệu khuyết.

## Nội dung chính

Lớp kiểm soát bảo mật, đạo đức và pháp lý áp dụng xuyên suốt mọi giai đoạn của vòng đời dữ liệu.

Dữ liệu EHR tái sử dụng cho nghiên cứu thường bẩn theo những cách có hệ thống. Khung của Weiskopf & Weng (2013) đánh giá chất lượng theo 5 chiều: **completeness (đầy đủ), correctness (đúng), concordance (nhất quán giữa các nguồn), plausibility (hợp lý), currency (cập nhật)**. Khung hài hòa của Kahn và cộng sự (2016) **[CẦN KIỂM CHỨNG thư mục]** bổ sung phân biệt **verification** (dữ liệu có đúng định dạng và quy tắc không) và **validation** (dữ liệu có đúng với thực tế không).

Dữ liệu khuyết không phải một loại. Theo Rubin (1976):

- **MCAR (Missing Completely At Random):** khuyết hoàn toàn ngẫu nhiên — ít gây chệch nhất.
- **MAR (Missing At Random):** khuyết có thể dự đoán được từ dữ liệu đã quan sát — dùng được multiple imputation.
- **MNAR (Missing Not At Random):** khuyết liên quan đến chính giá trị bị khuyết — không thể phân biệt được từ dữ liệu, cần phân tích độ nhạy.

Quy tắc thực hành (Sterne và cộng sự, 2009): **multiple imputation là cách khuyến nghị khi MAR; không dùng mean imputation hay last observation carried forward** vì chúng bóp méo phương sai và quan hệ giữa các biến. Mọi cách xử lý dữ liệu khuyết phải được ghi lại trong protocol phân tích trước khi nhìn kết quả.

Cuối cùng là tái lập: khảo sát của Baker (2016) trên 1.500 nhà khoa học cho thấy hơn 70% không tái lập được thí nghiệm của nhóm khác. Dữ liệu tốt mà không có code, phiên bản dữ liệu và môi trường phân tích đi kèm thì vẫn không tái lập được.

**Điểm cần nhớ:** câu hỏi đầu tiên khi thấy dữ liệu khuyết không phải “điền gì vào?”, mà là “vì sao nó khuyết?”.

<!-- page: course/module-4-quality/quiz.md -->
# Quiz — Bài 4

**4.1. Trong các chiều chất lượng dữ liệu, “plausibility” nghĩa là gì?**
- A. Dữ liệu có đủ số dòng và đủ trường theo thiết kế nghiên cứu.
- B. Dữ liệu được cập nhật gần thời điểm phân tích và còn giá trị sử dụng.
- C. Dữ liệu có cùng giá trị khi đối chiếu giữa các nguồn thu thập.
- D. Dữ liệu hợp lý về mặt lâm sàng và không mâu thuẫn với giới hạn đã biết.
- **Đáp án: D.** Plausibility xem dữ liệu có hợp lý trong bối cảnh thực tế hay không, chẳng hạn tuổi không âm.

**4.2. Dữ liệu khuyết loại MNAR khó nhất vì sao?**
- A. Vì nguyên nhân khuyết có thể liên quan đến chính giá trị không quan sát được.
- B. Vì dữ liệu MNAR khó diễn giải trong nghiên cứu y sinh nếu thiếu thông tin bổ sung.
- C. Vì các phương pháp xử lý dữ liệu khuyết có thể cho kết quả khác nhau.
- D. Vì MNAR thường xảy ra khi dữ liệu được lưu trong một hệ thống cũ.
- **Đáp án: A.** Khi cơ chế khuyết gắn với giá trị bị khuyết, dữ liệu quan sát khó đủ để suy ra cơ chế.

**4.3. Vì sao không nên dùng mean imputation như một cách mặc định?**
- A. Vì giá trị trung bình khó tính được từ dữ liệu số có phân phối lệch trong một số trường hợp.
- B. Vì cách này có thể làm giảm phương sai và bóp méo quan hệ giữa các biến.
- C. Vì mean imputation thường phù hợp với biến phân loại và không dùng cho biến số.
- D. Vì điền trung bình có thể làm giảm số lượng quan sát còn lại trong phân tích.
- **Đáp án: B.** Điền cùng một giá trị cho nhiều ô có thể làm dữ liệu trông ổn định hơn thực tế.

**4.4. Tình huống:** Bệnh nhân nặng thường không đo được một xét nghiệm vì không lấy được mẫu. Đây là loại khuyết nào?
- A. MCAR, vì việc lấy mẫu không liên quan đến tình trạng bệnh của người bệnh.
- B. MAR, vì dùng các giá trị đã quan sát có thể giúp xác định nhiều nguyên nhân.
- C. MNAR, vì khả năng khuyết có thể liên quan đến chính tình trạng bệnh.
- D. Không phải dữ liệu khuyết, vì xét nghiệm chưa từng được thực hiện trên mẫu đó.
- **Đáp án: C.** Cơ chế khuyết có thể liên quan đến mức độ bệnh; cần ghi giả định và phân tích độ nhạy.

---

<!-- page: course/module-5-privacy/index.md -->
# Bài 5 — Bảo mật, pháp lý và dữ liệu sẵn sàng cho AI

**Mục tiêu:** kể được các lớp pháp lý áp dụng ở Việt Nam và quốc tế; biết khi nào dữ liệu “đủ tốt cho AI”.

## Nội dung chính

Lớp kiểm soát bảo mật, đạo đức và pháp lý áp dụng xuyên suốt mọi giai đoạn của vòng đời dữ liệu.

Bảo mật dữ liệu y sinh có nhiều lớp, không chỉ một luật:

- **Quốc tế:** GDPR (EU 2016/679) — dữ liệu giả danh vẫn là dữ liệu cá nhân; dữ liệu sức khỏe là dữ liệu đặc biệt. EHDS (EU 2025/327) — có hiệu lực 26/03/2025, áp dụng từ 26/03/2027. HIPAA (Mỹ) — Safe Harbor (loại 18 định danh) hoặc Expert Determination.
- **Việt Nam:** Luật Bảo vệ dữ liệu cá nhân **91/2025/QH15** (hiệu lực 01/01/2026); Nghị định **356/2025/NĐ-CP** (31/12/2025) hướng dẫn luật này và thay thế Nghị định 13/2023 từ 01/01/2026; Luật Dữ liệu 60/2024/QH15; Thông tư 13/2025/TT-BYT về bệnh án điện tử (bệnh viện chậm nhất 30/09/2025, cơ sở khác chậm nhất 31/12/2026); Thông tư 50/2025/TT-BYT về thử thuốc trên lâm sàng (hiệu lực 27/02/2026); Nghị quyết 72-NQ/TW (09/09/2025) về khám sức khỏe định kỳ miễn phí và sổ sức khỏe điện tử.

Về kỹ thuật ẩn danh: **k-anonymity** (Sweeney, 2002) **[CẦN KIỂM CHỨNG thư mục]** — mỗi tổ hợp quasi-identifier xuất hiện ít nhất k lần; **l-diversity** (Machanavajjhala và cộng sự, 2007) — khắc phục điểm yếu của k-anonymity khi giá trị nhạy cảm thiếu đa dạng; **differential privacy** — thêm nhiễu có kiểm soát để bảo vệ cá nhân trong kết quả tổng hợp. Không có kỹ thuật nào là tuyệt đối — k-anonymity vẫn có thể bị tấn công nếu biết thêm thông tin nền.

Dữ liệu “sẵn sàng cho AI” không chỉ là dữ liệu sạch. Theo Bridge2AI (**preprint chưa bình duyệt**), cần 7 tiêu chí: FAIR, Deep Provenance (nguồn gốc sâu), Characterization (mô tả đặc tính), Pre-Model Explainability, Ethics/Legal/Governance, Sustainability, Computability. Dữ liệu không có nguồn gốc rõ ràng thì mô hình AI huấn luyện trên đó cũng không thể giải trình được.

**Điểm cần nhớ:** pháp lý là sàn, không phải trần. Tuân thủ luật là điều kiện cần; quản trị tốt — ai truy cập, vì mục đích gì, ghi lại ra sao — mới là điều kiện đủ.

<!-- page: course/module-5-privacy/quiz.md -->
# Quiz — Bài 5

**5.1. Dữ liệu giả danh (pseudonymised) khác dữ liệu ẩn danh ở điểm nào?**
- A. Dữ liệu giả danh vẫn có thể gắn lại với cá nhân qua thông tin tách riêng.
- B. Dữ liệu giả danh không còn cách nào gắn lại với một cá nhân cụ thể trong thực tế.
- C. Dữ liệu ẩn danh thường giữ khóa liên kết để nhóm nghiên cứu dùng lại.
- D. Hai cách xử lý khác nhau ở tên gọi, không khác về khả năng nhận diện.
- **Đáp án: A.** Giả danh giảm nhận diện trực tiếp nhưng vẫn có khả năng liên kết; ẩn danh hướng tới không thể liên kết hợp lý.

**5.2. Khi nào một bộ dữ liệu được xem là đã ẩn danh theo nghĩa khái niệm?**
- A. Khi tên và số hồ sơ được thay bằng mã do nhóm nghiên cứu tự đặt.
- B. Khi không còn khả năng liên kết hợp lý dữ liệu với một cá nhân cụ thể.
- C. Khi dữ liệu được lưu trong một kho riêng và không chia sẻ cho bên ngoài.
- D. Khi người quản trị hệ thống giữ riêng cách nối mã với thông tin nhận diện.
- **Đáp án: B.** Ẩn danh khác giả danh ở chỗ không còn đường liên kết hợp lý tới cá nhân.

**5.3. l-Diversity khắc phục điểm yếu nào của k-anonymity?**
- A. Khó khăn khi lưu các bản ghi trong nhiều tệp dữ liệu khác nhau.
- B. Việc các nhóm dữ liệu có quá nhiều biến nhận diện trực tiếp.
- C. Việc giá trị nhạy cảm trong một nhóm thiếu đa dạng dù nhóm có cùng mẫu nhận diện.
- D. Việc không thể dùng dữ liệu đã khử nhận diện cho phân tích thống kê.
- **Đáp án: C.** l-Diversity chú ý đến sự đa dạng của thuộc tính nhạy cảm trong mỗi nhóm tương đồng.

**5.4. Tình huống:** Một nhóm muốn huấn luyện AI nhưng không ghi chép nguồn gốc, phiên bản hay quy trình làm sạch dữ liệu. Vấn đề chính là gì?
- A. Bộ dữ liệu quá nhỏ để dùng cho mô hình học máy.
- B. Hệ thống máy tính chưa đủ mạnh để lưu các tệp dữ liệu nghiên cứu.
- C. Dữ liệu có thể được chia sẻ khi dữ liệu EHR được quản trị theo điều kiện phù hợp.
- D. Thiếu provenance làm giảm khả năng giải trình và tái lập quy trình dữ liệu.
- **Đáp án: D.** Không có nguồn gốc và lịch sử xử lý, khó đánh giá dữ liệu cũng như giải thích kết quả mô hình.

---

<!-- page: course/module-6-fair-ai/index.md -->
# Bài 6 — FAIR, chia sẻ và kết thúc nghiên cứu

**Mục tiêu:** áp dụng được 4 nguyên tắc FAIR; biết khi nào chia sẻ, khi nào đóng, và kết thúc nghiên cứu thế nào.

## Nội dung chính

Lớp kiểm soát bảo mật, đạo đức và pháp lý áp dụng xuyên suốt mọi giai đoạn của vòng đời dữ liệu.

**FAIR** (Wilkinson và cộng sự, 2016) gồm 4 nguyên tắc: **Findable (tìm được), Accessible (truy cập được), Interoperable (liên thông được), Reusable (tái sử dụng được)**. FAIR không có nghĩa là “mở hết”: dữ liệu sức khỏe thường FAIR nhưng **không mở công khai** — metadata mở để người khác tìm được, còn dữ liệu thì truy cập có kiểm soát.

Quy trình **FAIRification 7 bước** (Jacobsen và cộng sự, 2020) gồm ba pha: tiền-FAIRification — (1) xác định mục tiêu dựa trên đánh giá FAIR ban đầu, (2) phân tích cấu trúc dữ liệu, metadata và yêu cầu riêng tư; FAIRification — (3) định nghĩa mô hình ngữ nghĩa, (4) chuẩn hóa bằng bản thể học và từ vựng chuẩn, (5) làm giàu metadata và gắn định danh bền vững, (6) cấp phép tái sử dụng và lưu ký trên kho tin cậy; hậu-FAIRification — (7) đánh giá lại mức độ trưởng thành FAIR sau triển khai. Sách công thức thực hành là FAIR Cookbook (Rocca-Serra và cộng sự, 2023).

Kết thúc nghiên cứu không phải là “xong thì thôi”. Cần có:

- **Báo cáo kết quả** (đăng ký ClinicalTrials.gov, chia sẻ dữ liệu theo tuyên bố đã cam kết).
- **Lưu trữ (archiving):** dữ liệu, metadata, code và tài liệu lưu theo thời hạn quy định — ở Việt Nam, Thông tư 33/2025/TT-BYT quy định thời hạn lưu trữ hồ sơ, tài liệu y tế.
- **Hủy an toàn (secure destruction):** khi hết hạn lưu trữ, hủy theo NIST SP 800-88 Rev. 2 (Clear / Purge / Destroy) — xóa thông thường không đủ.

**Điểm cần nhớ:** một nghiên cứu chỉ hoàn thành khi dữ liệu của nó có thể được tìm lại, hiểu lại và kiểm tra lại sau nhiều năm.

<!-- page: course/module-6-fair-ai/quiz.md -->
# Quiz — Bài 6

**6.1. FAIR có nghĩa là dữ liệu phải công khai không?**
- A. Có, vì dữ liệu đạt FAIR khi người dùng tải được toàn bộ tệp theo chính sách truy cập.
- B. Không, dữ liệu có thể FAIR với metadata mở và quyền truy cập dữ liệu được kiểm soát.
- C. FAIR phù hợp với dữ liệu không chứa thông tin sức khỏe hoặc thông tin nhạy cảm.
- D. Có, dữ liệu đạt FAIR khi đã được đăng trên một kho dữ liệu công cộng.
- **Đáp án: B.** FAIR yêu cầu khả năng tìm, truy cập theo điều kiện, liên thông và tái sử dụng; không buộc mở hết.

**6.2. Bốn nguyên tắc FAIR nhấn mạnh những khả năng nào của dữ liệu?**
- A. Dữ liệu phải được lưu cục bộ, mã hóa, sao lưu và giữ nguyên bản.
- B. Dữ liệu phải được công khai, tải xuống, phân tích và dùng lại không hạn chế.
- C. Dữ liệu phải tìm được, truy cập được, liên thông được và tái sử dụng được.
- D. Dữ liệu phải có kích thước lớn, nhiều biến, ít ô trống và một định dạng chung.
- **Đáp án: C.** FAIR mô tả cách dữ liệu được tìm thấy, truy cập, kết hợp và dùng lại có trách nhiệm.

**6.3. Vì sao xóa file thông thường chưa đủ khi hủy dữ liệu nghiên cứu?**
- A. Vì các tệp nghiên cứu phải được giữ lại theo chính sách để phục vụ tái sử dụng.
- B. Vì xóa file làm hỏng thiết bị lưu trữ và các tệp khác trên thiết bị đó.
- C. Vì việc hủy dữ liệu liên quan đến thủ tục giấy tờ và việc ghi chép của nhóm nghiên cứu về thiết bị lưu trữ.
- D. Vì dữ liệu có thể còn khôi phục được; cần quy trình hủy phù hợp với thiết bị và chính sách.
- **Đáp án: D.** Xóa thông thường chưa chứng minh dữ liệu không thể khôi phục, nên cần quy trình hủy an toàn phù hợp.

**6.4. Tình huống:** Một nhóm muốn chia sẻ dữ liệu bệnh nhân nhưng không muốn công khai. Cách làm nào phù hợp với FAIR?
- A. Chia sẻ metadata để dữ liệu được tìm thấy, rồi cấp quyền truy cập theo điều kiện.
- B. Không mô tả dữ liệu để tránh người khác biết dữ liệu đang tồn tại.
- C. Công khai toàn bộ dữ liệu vì FAIR yêu cầu tài nguyên phải được mở.
- D. Gửi tệp qua kênh cá nhân mà không cần thỏa thuận hoặc kiểm soát truy cập.
- **Đáp án: A.** Dữ liệu nhạy cảm vẫn có thể FAIR khi được mô tả rõ và truy cập theo quy trình được kiểm soát.

---

<!-- page: course/final-quiz.md -->
# Quiz tổng hợp — Workflow (10 câu, làm sau 6 bài)

**Q1.** Sắp xếp đúng thứ tự các giai đoạn: (a) Chuẩn hóa, (b) Thiết kế & DMP, (c) Lưu trữ & hủy an toàn, (d) Thu thập, (e) FAIR & chia sẻ, (f) Xử lý & làm sạch.
- A. b → d → f → a → e → c, theo tiến trình từ thiết kế đến lưu trữ.
- B. d → b → f → a → c → e, bắt đầu bằng thu thập trước khi hoàn thiện kế hoạch.
- C. b → a → d → f → e → c, đặt chuẩn hóa sớm hơn thu thập dữ liệu.
- D. a → b → d → f → e → c, đặt chuẩn hóa trước phần thiết kế.
- **Đáp án: A.** Vòng đời bắt đầu ở thiết kế và DMP, rồi thu thập, xử lý và làm sạch, chuẩn hóa, FAIR/chia sẻ và kết thúc bằng lưu trữ hoặc hủy an toàn. Giai đoạn phân tích và tái lập không có bài riêng trong khóa này nên không đưa vào câu hỏi.

**Q2.** Một nghiên cứu không viết DMP, thu thập xong mới nghĩ đến việc chia sẻ dữ liệu. Hậu quả nào có khả năng xảy ra nhất?
- A. Có thể mất thêm thời gian, nhưng nhiều quyết định quản trị khác vẫn giữ nguyên.
- B. Thiếu metadata và biến không thống nhất, làm khó phê duyệt chia sẻ.
- C. Có ít hậu quả vì quyết định chia sẻ có thể đưa ra ở cuối nghiên cứu.
- D. Dữ liệu tự động trở nên FAIR vì đã được thu thập đầy đủ trong nghiên cứu.
- **Đáp án: B.** Quyết định thượng nguồn bị bỏ qua có thể làm thiếu metadata, không nhất quán biến và hạn chế khả năng chia sẻ về sau.

**Q3.** Bệnh viện A dùng FHIR để gửi dữ liệu cho bệnh viện B, rồi cả hai cùng phân tích trên OMOP CDM. Nhận định nào đúng?
- A. Phải chuyển sang CDISC trước, dù mục tiêu là trao đổi rồi phân tích quan sát.
- B. Dùng thừa chuẩn; một chuẩn thường đủ cho cả trao đổi và phân tích.
- C. Đúng vai trò: FHIR để trao đổi, OMOP để phân tích.
- D. FHIR và OMOP thường khó dùng chung trong một quy trình liên cơ sở.
- **Đáp án: C.** FHIR phục vụ trao đổi dữ liệu; OMOP phục vụ chuẩn hóa và phân tích dữ liệu quan sát.

**Q4.** Dữ liệu khuyết vì bệnh nhân nặng không lấy được mẫu xét nghiệm. Cách xử lý đúng nhất là gì?
- A. Xóa toàn bộ bệnh nhân đó để bộ dữ liệu không còn ô khuyết.
- B. Bỏ qua và không ghi lại nguyên nhân vì mẫu xét nghiệm chưa từng được lấy.
- C. Điền giá trị trung bình cho nhiều bệnh nhân để giữ kích thước mẫu.
- D. Xem xét MNAR, ghi giả định, chọn phương pháp và phân tích độ nhạy.
- **Đáp án: D.** Cơ chế khuyết có thể liên quan đến mức độ bệnh; cần ghi giả định, chọn phương pháp phù hợp và kiểm tra độ nhạy.

**Q5.** Khi xử lý dữ liệu cá nhân trong nghiên cứu, nguyên tắc nào phù hợp nhất?
- A. Chủ yếu áp dụng văn bản có tại thời điểm viết đề cương, ít rà soát về sau.
- B. Có thể bỏ qua ngày hiệu lực nếu tên văn bản đã ghi trong DMP của nghiên cứu.
- C. Đối chiếu văn bản hiện hành và ngày hiệu lực áp dụng cho bối cảnh nghiên cứu.
- D. Chủ yếu tuân theo chính sách phần mềm thu thập dữ liệu, ít căn cứ khác.
- **Đáp án: C.** Tên văn bản không đủ để xác định nghĩa vụ; cần kiểm tra văn bản hiện hành, ngày hiệu lực và phạm vi áp dụng.

**Q6.** Một dataset đạt k-anonymity với k=5. Điều này đảm bảo điều gì?
- A. Dữ liệu đã được mã hóa và nhiều khóa liên kết đã bị loại bỏ.
- B. Mỗi quasi-identifier xuất hiện ít nhất 5 lần; vẫn còn nguy cơ từ thông tin nền.
- C. Không ai có thể tái định danh bằng bất kỳ cách nào, kể cả liên kết nguồn khác.
- D. Dữ liệu được phép công khai mà không cần xét duyệt hoặc kiểm soát truy cập.
- **Đáp án: B.** k-anonymity giới hạn liên kết trực tiếp, nhưng không loại bỏ mọi nguy cơ tái định danh hoặc suy luận thuộc tính nhạy cảm.

**Q7.** Nhận định nào mô tả đầy đủ hơn yêu cầu để dữ liệu y sinh sẵn sàng cho AI?
- A. Dữ liệu cần lớn, sạch và ở định dạng bảng tính phổ biến để mô hình đọc được.
- B. Dữ liệu chủ yếu cần có nhiều biến và ít ô trống, không cần provenance.
- C. AI-ready cần FAIR, provenance, giải trình, quản trị và khả năng tính toán.
- D. Dữ liệu nên được giữ kín để tránh rủi ro, không cần khả năng tái sử dụng.
- **Đáp án: C.** AI-ready là yêu cầu đa chiều về khả năng tìm thấy, hiểu, giải trình, quản trị và tính toán, không chỉ là dung lượng hoặc độ sạch.

**Q8.** Nghiên cứu kết thúc, nhóm xóa file dữ liệu bằng cách xóa thông thường trong hệ điều hành. Đủ chưa?
- A. Chưa chắc; xóa thông thường chưa đồng nghĩa khử hoặc hủy an toàn.
- B. Đủ trong nhiều trường hợp vì tệp không còn hiển thị trong thư mục.
- C. Không cần hủy, cứ giữ dữ liệu mãi mãi bất kể chính sách lưu giữ.
- D. Cần quan tâm khi dataset có kích thước lớn hoặc nhiều tệp.
- **Đáp án: A.** Cần có quy trình khử hoặc hủy phù hợp với loại lưu trữ, chính sách và yêu cầu áp dụng; xóa thông thường chưa đủ để kết luận an toàn.

**Q9.** Trong workflow FAIRification 7 bước, đánh giá FAIR được dùng như thế nào?
- A. Đánh giá bước 1 để tìm khoảng cách và bước 7 để kiểm tra cải thiện.
- B. Thường đánh giá một lần ở bước 7, sau khi đã hoàn tất nhiều thay đổi.
- C. Chủ yếu đánh giá khi dữ liệu được công khai và không còn hạn chế.
- D. Đánh giá FAIR thay thế cho việc lập kế hoạch và quản trị ở bước 1.
- **Đáp án: A.** Đánh giá ban đầu định hướng kế hoạch, còn đánh giá lại ở bước 7 kiểm tra mức cải thiện và kết quả đạt được.

**Q10.** Một học viên nói: “Dữ liệu của tôi đã FAIR nên tôi công khai toàn bộ lên mạng.” Sai ở đâu?
- A. Không sai, vì nhiều dữ liệu FAIR được công khai trên mạng.
- B. FAIR chủ yếu áp dụng cho dữ liệu mở và không áp dụng cho dữ liệu sức khỏe.
- C. Phải công khai mới gọi là FAIR, bất kể ràng buộc đạo đức hay pháp lý.
- D. FAIR không đồng nghĩa mở hết; dữ liệu sức khỏe có thể kiểm soát truy cập.
- **Đáp án: D.** FAIR yêu cầu khả năng tìm thấy, truy cập được theo điều kiện, liên thông và tái sử dụng; không buộc dữ liệu nhạy cảm phải mở công khai.

**Cách tính điểm:** mỗi câu 1 điểm, tổng 34 câu (24 câu theo bài + 10 câu tổng hợp). Đạt khi ≥ 24/34 **và đúng ít nhất 2/3 câu Q1–Q3** của quiz tổng hợp. Học viên nên làm quiz tổng hợp tối đa 2 lần như hướng dẫn tự học; site tĩnh không cưỡng chế giới hạn này.

---

<!-- page: course/glossary.md -->
# Thuật ngữ

| Thuật ngữ | Định nghĩa ngắn |
|---|---|
| ALCOA+ | Các nguyên tắc bảo đảm tính toàn vẹn dữ liệu. |
| CDISC | Hệ tiêu chuẩn dữ liệu cho nghiên cứu và thử nghiệm lâm sàng. |
| CDE | Phần tử dữ liệu chung được định nghĩa để dùng nhất quán. |
| CRF | Biểu mẫu thu thập dữ liệu nghiên cứu. |
| Data dictionary | Tài liệu định nghĩa biến, kiểu dữ liệu, đơn vị và giá trị hợp lệ. |
| DMP | Kế hoạch quản lý dữ liệu trong toàn bộ vòng đời nghiên cứu. |
| DMSP | Kế hoạch quản lý và chia sẻ dữ liệu. |
| DUA | Thỏa thuận sử dụng dữ liệu. |
| EDC | Hệ thống thu thập dữ liệu điện tử. |
| eCRF | CRF điện tử. |
| FAIR | Findable, Accessible, Interoperable, Reusable. |
| FHIR | Tiêu chuẩn HL7 trao đổi dữ liệu y tế qua tài nguyên và API. |
| GDPR | Quy định bảo vệ dữ liệu chung của Liên minh châu Âu. |
| Metadata | Dữ liệu mô tả nguồn gốc, cấu trúc và ngữ cảnh của dữ liệu. |
| MNAR | Dữ liệu khuyết phụ thuộc vào chính giá trị bị khuyết. |
| OMOP CDM | Mô hình dữ liệu chung cho nghiên cứu quan sát. |
| Pseudonymisation | Thay định danh trực tiếp bằng mã nhưng vẫn có khả năng tái liên kết. |
| RBQM | Quản trị chất lượng dựa trên rủi ro. |
| REDCap | Nền tảng thu thập và quản lý dữ liệu nghiên cứu. |
| Reproducibility | Khả năng tái tạo kết quả bằng dữ liệu và quy trình đã mô tả. |
| audit trail | Dấu vết ghi lại ai sửa gì, khi nào và vì sao. |
| quasi-identifier | Tổ hợp thuộc tính có thể dùng để liên kết và phân biệt bản ghi. |
| k-anonymity | Mỗi tổ hợp quasi-identifier xuất hiện ít nhất k lần. |
| l-diversity | Yêu cầu đa dạng giá trị nhạy cảm trong mỗi nhóm k-anonymity. |
| differential privacy | Kỹ thuật thêm nhiễu có kiểm soát vào kết quả tổng hợp. |
| MCAR | Dữ liệu khuyết hoàn toàn ngẫu nhiên. |
| MAR | Dữ liệu khuyết có thể dự đoán từ dữ liệu đã quan sát. |
| imputation | Phương pháp xử lý hoặc ước lượng giá trị bị khuyết. |
| SDTM | Mô hình dữ liệu CDISC để nộp dữ liệu thử nghiệm lâm sàng. |
| GCP | Thực hành tốt trong nghiên cứu lâm sàng. |
| provenance | Thông tin về nguồn gốc, phiên bản và quá trình hình thành dữ liệu. |
| Safe Harbor | Phương pháp HIPAA loại bỏ 18 nhóm định danh theo danh sách quy định. |
| protocol | Đề cương mô tả nghiên cứu làm gì, vì sao và trên ai. |

<!-- page: ROADMAP.md -->
## Những gì chưa có trong phần này (bổ sung sau)

- Lab thực hành (Synthea, SQL/FHIR/OMOP mẫu) — theo mô hình PhysioNet/MIT Critical Data.
- Video/script bài giảng — theo mẫu Coursera.
- Bài tập peer review và capstone — viết DMP + kế hoạch FAIR cho một nghiên cứu giả định.
- Chứng nhận hoàn thành và rubric chấm.
- Cập nhật 12 mục [CẦN KIỂM CHỨNG] còn lại trong bản tổng hợp (xem citation-audit ở biomedical-rdm) trước khi dùng làm tài liệu chính thức.
