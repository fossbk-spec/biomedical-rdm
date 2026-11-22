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
1. Thiết kế & DMP → 2. Thu thập → 3. Làm sạch & kiểm tra
→ 4. Chuẩn hóa (CDISC / FHIR / OMOP) → 5. Bảo mật & khử định danh
→ 6. FAIR & AI-ready → 7. Kết thúc: lưu trữ / hủy an toàn
```

Quy tắc xuyên suốt: **quyết định càng sớm càng rẻ**. Một trường dữ liệu không định nghĩa ở bước 1 sẽ thành dữ liệu khuyết, không so sánh được, hoặc không dùng được cho AI ở bước 5–7. DMP không phải thủ tục hành chính — nó là bản hợp đồng về dữ liệu của cả nghiên cứu.

**Lớp kiểm soát xuyên suốt:** bảo mật, đạo đức và pháp lý áp dụng ở mọi giai đoạn của vòng đời dữ liệu, từ lập kế hoạch đến lưu trữ hoặc tiêu hủy; đây không phải một bước chỉ làm ở cuối.

| 7 bước của khóa học | 6 giai đoạn trong review §2.1 |
|---|---|
| Thiết kế & DMP | Lập kế hoạch |
| Thu thập | Thu thập |
| Làm sạch & kiểm tra | Xử lý và chuẩn hóa |
| Chuẩn hóa | Xử lý và chuẩn hóa |
| Phân tích | Bước 3–4: làm sạch, kiểm tra và chuẩn hóa để phân tích |
| Bảo mật & khử định danh | Áp dụng xuyên suốt |
| FAIR & AI-ready | Chia sẻ, công bố và tái sử dụng |
| Kết thúc: lưu trữ / hủy an toàn | Lưu trữ dài hạn hoặc tiêu hủy |

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
- A. Protocol nói nghiên cứu làm gì; DMP nói dữ liệu là gì, ở đâu, ai dùng và chia sẻ thế nào.
- B. DMP dài hơn protocol.
- C. DMP chỉ cần khi nghiên cứu có AI.
- D. Hai tài liệu này là một.
- **Đáp án: A.** Protocol trả lời câu hỏi nghiên cứu; DMP trả lời câu hỏi quản trị dữ liệu.

**1.2. Khi soạn DMSP, lựa chọn nào phù hợp với brief khóa học này?**
- A. Dùng mẫu NIH hiện hành (7 yếu tố) hoặc Horizon Europe và kiểm tra yêu cầu cụ thể.
- B. Luôn dùng một mẫu cũ có giới hạn trang cố định.
- C. Chỉ cần nêu tên kho, không cần mô tả dữ liệu.
- D. Chờ đến khi nghiên cứu kết thúc mới viết.
- **Đáp án: A.** Mẫu và yêu cầu cụ thể cần được kiểm tra theo nhà tài trợ; phụ lục mẫu ghi trạng thái kiểm chứng.

**1.3. Vì sao cần metadata?**
- A. Để ép mọi biến trong dataset về cùng một kiểu dữ liệu.
- B. Để thay thế từ điển dữ liệu.
- C. Để sau này vẫn hiểu dữ liệu được thu thập như thế nào, bởi ai, bằng công cụ nào.
- D. Chỉ cần cho dữ liệu mở.
- **Đáp án: C.** Không có metadata, dữ liệu mất ngữ cảnh và không tái sử dụng được.

**1.4. Tình huống:** Một nghiên cứu thu thập huyết áp nhưng có nhóm ghi “120/80”, nhóm ghi “120”, nhóm ghi “cao”. Lỗi này bắt nguồn từ bước nào?
- A. Bước phân tích.
- B. Bước lưu trữ.
- C. Không phải lỗi.
- D. Bước thu thập — không thống nhất từ điển dữ liệu và đơn vị trước khi thu thập.
- **Đáp án: D.** Lỗi định nghĩa biến phải sửa ở thiết kế, không sửa được triệt để ở phân tích.

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

**2.1. “Complete” trong phần “+” của ALCOA+ nghĩa là gì?**
- A. Dữ liệu phải đầy đủ, không thiếu trường bắt buộc và các bản ghi liên quan.
- B. Dữ liệu phải bao gồm cả những bản ghi đã bị hủy mà không cần lý do.
- C. Dữ liệu phải được nhập lại nhiều lần để chứng minh tính đầy đủ.
- D. Dữ liệu phải công khai.
- **Đáp án: A.**
- **Giải thích:** Workflow bắt đầu ở thiết kế và DMP, rồi thu thập, chuẩn hóa, FAIR/chia sẻ và kết thúc bằng lưu trữ hoặc hủy an toàn.

**2.2. Vì sao sửa dữ liệu phải để lại audit trail?**
- A. Để chứng minh rằng mọi thay đổi đều đã được phê duyệt trước khi thực hiện.
- B. Để truy vết được ai sửa, sửa gì, khi nào và vì sao — đó là yêu cầu của Original và Traceable.
- C. Để file lớn hơn.
- D. Không cần nếu sửa đúng.
- **Đáp án: B.**
- **Giải thích:** Quyết định thượng nguồn bị bỏ qua có thể làm thiếu metadata, không nhất quán biến và hạn chế khả năng chia sẻ về sau.

**2.3. RBQM khác kiểm tra 100% thủ công ở điểm nào?**
- A. RBQM không kiểm tra gì cả.
- B. RBQM chỉ dùng cho nghiên cứu AI.
- C. RBQM tập trung nguồn lực vào dữ liệu và quy trình rủi ro cao nhất.
- D. RBQM rẻ hơn vì bỏ qua lỗi.
- **Đáp án: C.**
- **Giải thích:** FHIR phục vụ trao đổi dữ liệu; OMOP phục vụ chuẩn hóa và phân tích dữ liệu quan sát.

**2.4. Tình huống:** Một điều dưỡng ghi nhiệt độ bệnh nhân vào giấy nháp cuối ca rồi hôm sau mới nhập vào hệ thống. Vi phạm nguyên tắc nào nhất?
- A. Accurate.
- B. Available.
- C. Không vi phạm gì.
- D. Contemporaneous — không ghi ngay lúc xảy ra.
- **Đáp án: D.** Ghi chậm làm tăng nguy cơ sai sót và mất bằng chứng gốc.

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
- A. Chuẩn hóa dữ liệu thử nghiệm lâm sàng để nộp cho cơ quan quản lý.
- B. Trao đổi dữ liệu giữa hai bệnh viện theo thời gian thực.
- C. Phân tích quần thể trên nhiều cơ sở dữ liệu.
- D. Lưu trữ ảnh y tế.
- **Đáp án: A.**

**3.2. FHIR R6 hiện tại ở trạng thái nào?**
- A. Đã ban hành và thay thế R4.
- B. Chưa ban hành, đang trong giai đoạn ballot.
- C. Đã bị hủy.
- D. Chỉ dùng ở Việt Nam.
- **Đáp án: B.** R4 là bản thực hành, R5 ban hành 26/03/2023, R6 chưa có bản chính thức.

**3.3. OMOP CDM mạnh nhất ở việc nào?**
- A. Ghi điện tâm đồ.
- B. Thay thế hồ sơ giấy.
- C. Phân tích quần thể trên dữ liệu quan sát từ nhiều nguồn khác nhau.
- D. Nộp hồ sơ thuốc mới.
- **Đáp án: C.**

**3.4. Tình huống:** Một bệnh viện muốn vừa chia sẻ dữ liệu khám chữa bệnh với bệnh viện khác, vừa phân tích xu hướng điều trị trên 5 năm. Cần chuẩn nào?
- A. Không cần chuẩn nào.
- B. Chỉ FHIR.
- C. Chỉ OMOP.
- D. FHIR để trao đổi, OMOP để phân tích — dùng cả hai, mỗi chuẩn một vai trò.
- **Đáp án: D.**
- **Giải thích:** Cơ chế khuyết có thể liên quan đến mức độ bệnh; cần ghi giả định, chọn phương pháp phù hợp và kiểm tra độ nhạy.

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

**4.1. Trong 5 chiều của Weiskopf & Weng, “plausibility” nghĩa là gì?**
- A. Dữ liệu hợp lý về mặt lâm sàng (ví dụ: tuổi không âm, huyết áp trong khoảng sinh lý).
- B. Dữ liệu đầy đủ.
- C. Dữ liệu mới nhất.
- D. Dữ liệu đúng chính tả.
- **Đáp án: A.**

**4.2. Dữ liệu khuyết loại MNAR khó nhất vì sao?**
- A. Vì khuyết quá nhiều.
- B. Vì nguyên nhân khuyết liên quan đến chính giá trị bị khuyết, nên không thể suy ra từ dữ liệu đã quan sát; cần phân tích độ nhạy.
- C. Vì không có phần mềm xử lý.
- D. Vì MNAR không xảy ra trong thực tế.
- **Đáp án: B.**

**4.3. Vì sao không nên dùng mean imputation?**
- A. Vì tính toán khó.
- B. Vì nó chỉ dùng cho dữ liệu lớn.
- C. Vì nó làm giảm phương sai giả tạo và bóp méo quan hệ giữa các biến.
- D. Vì mean imputation chỉ dùng được cho biến phân loại.
- **Đáp án: C.**

**4.4. Tình huống:** Bệnh nhân nặng thường không đo được một chỉ số xét nghiệm vì không lấy được mẫu. Đây là loại khuyết nào?
- A. MCAR.
- B. MAR.
- C. Không phải dữ liệu khuyết.
- D. MNAR — khả năng khuyết liên quan đến chính tình trạng bệnh (giá trị bị khuyết).
- **Đáp án: D.**

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

**5.1. Theo GDPR, dữ liệu giả danh (pseudonymised) có còn là dữ liệu cá nhân không?**
- A. Có — vẫn là dữ liệu cá nhân vì có thể tái định danh bằng khóa riêng.
- B. Không, đã ẩn danh hoàn toàn.
- C. Chỉ khi có tên.
- D. Chỉ ở Việt Nam.
- **Đáp án: A.**

**5.2. Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 có hiệu lực khi nào?**
- A. 01/01/2025.
- B. 01/01/2026.
- C. 01/07/2025.
- D. Chưa có hiệu lực.
- **Đáp án: B.** Nghị định 356/2025 hướng dẫn luật này và thay thế Nghị định 13/2023 từ cùng ngày.

**5.3. l-Diversity ra đời để khắc phục điểm yếu nào của k-anonymity?**
- A. k-Anonymity quá chậm.
- B. k-Anonymity không dùng được cho dữ liệu lớn.
- C. k-Anonymity không bảo vệ được khi giá trị nhạy cảm trong một nhóm thiếu đa dạng (ví dụ: cả nhóm cùng một chẩn đoán).
- D. k-Anonymity đã bị cấm.
- **Đáp án: C.**

**5.4. Tình huống:** Một nhóm muốn huấn luyện AI trên dữ liệu EHR nhưng không có ghi chép nào về nguồn gốc, phiên bản và quy trình làm sạch dữ liệu. Vấn đề lớn nhất là gì?
- A. Thiếu dữ liệu.
- B. Thiếu máy tính mạnh.
- C. Không có vấn đề gì.
- D. Thiếu Deep Provenance — không giải trình được mô hình, không tái lập được, và có thể vi phạm yêu cầu quản trị.
- **Đáp án: D.**

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
- A. Không — FAIR nghĩa là tìm được, truy cập được (có thể có kiểm soát), liên thông được và tái sử dụng được.
- B. Có, FAIR = mở hết.
- C. Chỉ đúng với dữ liệu không phải y tế.
- D. FAIR chỉ áp dụng cho ảnh.
- **Đáp án: A.**

**6.2. Bước cuối cùng trong FAIRification 7 bước là gì?**
- A. Thu thập dữ liệu.
- B. Xóa dữ liệu.
- C. Công bố bài báo.
- D. Đánh giá lại mức độ trưởng thành FAIR sau triển khai.
- **Đáp án: D.**

**6.3. Vì sao xóa file thông thường chưa đủ khi hủy dữ liệu nghiên cứu?**
- A. Vì file quá lớn.
- B. Vì luật cấm xóa file.
- C. Vì file vẫn có thể khôi phục được; cần hủy theo chuẩn như NIST SP 800-88 (Clear/Purge/Destroy).
- D. Không có lý do gì.
- **Đáp án: C.**

**6.4. Tình huống:** Một nhóm muốn chia sẻ dữ liệu bệnh nhân cho nhóm khác nhưng không muốn công khai. Cách làm đúng theo FAIR là gì?
- A. Không chia sẻ.
- B. Công khai toàn bộ lên mạng.
- C. Chỉ gửi qua email cá nhân.
- D. Công bố metadata để người khác tìm được, cho truy cập dữ liệu có kiểm soát theo thỏa thuận sử dụng dữ liệu.
- **Đáp án: D.**

---

<!-- page: course/final-quiz.md -->
# Quiz tổng hợp — Workflow (10 câu, làm sau 6 bài)

**Q1.** Sắp xếp đúng thứ tự workflow: (a) Chuẩn hóa, (b) Thiết kế & DMP, (c) Kết thúc/lưu trữ, (d) Thu thập, (e) FAIR & chia sẻ.
- A. b → d → a → e → c, theo tiến trình từ thiết kế đến lưu trữ.
- B. d → b → a → c → e, bắt đầu bằng thu thập trước khi hoàn thiện kế hoạch.
- C. b → a → d → e → c, đặt chuẩn hóa sớm hơn thu thập dữ liệu.
- D. a → b → d → e → c, đặt chuẩn hóa trước phần thiết kế.
- **Đáp án: A.**
- **Giải thích:** Workflow bắt đầu ở thiết kế và DMP, rồi thu thập, chuẩn hóa, FAIR/chia sẻ và kết thúc bằng lưu trữ hoặc hủy an toàn.

**Q2.** Một nghiên cứu không viết DMP, thu thập xong mới nghĩ đến việc chia sẻ dữ liệu. Hậu quả nào có khả năng xảy ra nhất?
- A. Có thể mất thêm thời gian, nhưng nhiều quyết định quản trị khác vẫn giữ nguyên.
- B. Thiếu metadata và biến không thống nhất, làm khó phê duyệt chia sẻ.
- C. Có ít hậu quả vì quyết định chia sẻ có thể đưa ra ở cuối nghiên cứu.
- D. Dữ liệu tự động trở nên FAIR vì đã được thu thập đầy đủ trong nghiên cứu.
- **Đáp án: B.**
- **Giải thích:** Quyết định thượng nguồn bị bỏ qua có thể làm thiếu metadata, không nhất quán biến và hạn chế khả năng chia sẻ về sau.

**Q3.** Bệnh viện A dùng FHIR để gửi dữ liệu cho bệnh viện B, rồi cả hai cùng phân tích trên OMOP CDM. Nhận định nào đúng?
- A. Phải chuyển sang CDISC trước, dù mục tiêu là trao đổi rồi phân tích quan sát.
- B. Dùng thừa chuẩn; một chuẩn thường đủ cho cả trao đổi và phân tích.
- C. Đúng vai trò: FHIR để trao đổi, OMOP để phân tích.
- D. FHIR và OMOP thường khó dùng chung trong một quy trình liên cơ sở.
- **Đáp án: C.**
- **Giải thích:** FHIR phục vụ trao đổi dữ liệu; OMOP phục vụ chuẩn hóa và phân tích dữ liệu quan sát.

**Q4.** Dữ liệu khuyết vì bệnh nhân nặng không lấy được mẫu xét nghiệm. Cách xử lý đúng nhất là gì?
- A. Xóa toàn bộ bệnh nhân đó để bộ dữ liệu không còn ô khuyết.
- B. Bỏ qua và không ghi lại nguyên nhân vì mẫu xét nghiệm chưa từng được lấy.
- C. Điền giá trị trung bình cho nhiều bệnh nhân để giữ kích thước mẫu.
- D. Xem xét MNAR, ghi giả định, chọn phương pháp và phân tích độ nhạy.
- **Đáp án: D.**
- **Giải thích:** Cơ chế khuyết có thể liên quan đến mức độ bệnh; cần ghi giả định, chọn phương pháp phù hợp và kiểm tra độ nhạy.

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
- **Đáp án: B.**
- **Giải thích:** k-anonymity giới hạn liên kết trực tiếp, nhưng không loại bỏ mọi nguy cơ tái định danh hoặc suy luận thuộc tính nhạy cảm.

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
