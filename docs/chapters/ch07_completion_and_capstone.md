# HOÀN THÀNH KHÓA HỌC: QUIZ TỔNG HỢP WORKFLOW & BÀI TẬP CAPSTONE

> **Phần kết thúc:** Khóa học Quản lý dữ liệu nghiên cứu y sinh (Biomedical RDM)  
> **Nội dung:** Quiz Tổng hợp 10 câu + Bài tập Capstone tự đánh giá + Bảng tự nghiệm thu hoàn thành khóa học  
> **Thời gian gợi ý:** 45–60 phút  
> **Nguyên tắc:** Tự học, tự đánh giá, không chấm điểm, không nộp bài.

---

## PHẦN 1. QUIZ TỔNG HỢP WORKFLOW (10 CÂU HỎI TỰ ĐÁNH GIÁ)

Bài quiz này kiểm tra sự liên kết xuyên suốt quy trình 7 giai đoạn của dữ liệu y sinh. Hãy tự trả lời trước khi xem đáp án và giải thích chi tiết bên dưới mỗi câu:

---

### **Q1. Thứ tự chuẩn của Workflow Quản lý Dữ liệu Y sinh là gì?**
- A. Chuẩn hóa ➔ Thiết kế & DMP ➔ Lưu trữ ➔ Thu thập ➔ FAIR & Chia sẻ.
- B. Thiết kế & DMP ➔ Thu thập ➔ Chuẩn hóa ➔ FAIR & Chia sẻ ➔ Lưu trữ & Hủy an toàn.
- C. Thu thập ➔ Thiết kế & DMP ➔ Chuẩn hóa ➔ Lưu trữ ➔ FAIR & Chia sẻ.
- D. Chuẩn hóa ➔ Thu thập ➔ Thiết kế & DMP ➔ FAIR & Chia sẻ ➔ Lưu trữ.

> **Đáp án đúng: B.**  
> *Giải thích:* Quá trình quản trị dữ liệu luôn bắt đầu từ thượng nguồn (Thiết kế & DMP), tiếp theo là thu thập chuẩn ALCOA+, xử lý làm sạch, chuẩn hóa liên thông (CDISC/FHIR/OMOP), chia sẻ theo nguyên tắc FAIR, và kết thúc bằng lưu trữ bảo mật hoặc hủy an toàn.

---

### **Q2. Một nhóm nghiên cứu không lập DMP từ đầu, sau khi thu thập xong mới nghĩ đến việc chia sẻ dữ liệu lên kho mở. Hậu quả nào có nguy cơ cao nhất xảy ra?**
- A. Không có hậu quả gì, dữ liệu chỉ cần nén lại và tải lên.
- B. Thiếu metadata, định nghĩa biến không nhất quán, và quan trọng nhất: Thỏa thuận chấp thuận (Informed Consent) đã ký không có điều khoản cho phép chia sẻ dữ liệu thứ cấp, khiến dữ liệu bị cấm chia sẻ.
- C. Chỉ mất thêm khoảng 1 giờ để viết tệp README.
- D. Dữ liệu sẽ tự động đạt chuẩn FAIR.

> **Đáp án đúng: B.**  
> *Giải thích:* Hiệu ứng khuếch đại lỗi thượng nguồn (Upstream Error Amplification). Nếu không quy định điều khoản chia sẻ dữ liệu thứ cấp trong bản Informed Consent được Hội đồng Đạo đức (IRB) phê duyệt ngay từ đầu, bạn sẽ không có cơ sở pháp lý để công khai hoặc chia sẻ dữ liệu sau này.

---

### **Q3. Một đề tài nghiên cứu lâm sàng đa trung tâm: Bệnh viện A gửi dữ liệu bệnh án sang Bệnh viện B bằng chuẩn HL7 FHIR, sau đó dữ liệu cả hai viện được ánh xạ vào OMOP CDM để phân tích so sánh kết cục điều trị. Nhận định nào sau đây là chính xác?**
- A. Thiết kế này sai lầm và trùng lặp chuẩn, chỉ nên chọn một trong hai chuẩn.
- B. Thiết kế này hoàn toàn tối ưu và chuẩn mực: FHIR giải quyết bài toán giao tiếp thời gian thực giữa các hệ thống, còn OMOP CDM giải quyết bài toán phân tích quần thể đa trung tâm.
- C. FHIR và OMOP CDM không thể kết nối hoặc ánh xạ qua lại với nhau.
- D. Bắt buộc phải chuyển đổi sang CDISC SDTM trước thì mới phân tích được.

> **Đáp án đúng: B.**  
> *Giải thích:* Ba chuẩn dữ liệu lớn bổ trợ lẫn nhau, không triệt tiêu nhau: FHIR trao đổi liên thông, OMOP phân tích nghiên cứu quan sát, và CDISC nộp hồ sơ cho cơ quan quản lý.

---

### **Q4. Trong một nghiên cứu tim mạch, các bệnh nhân có tình trạng suy tim rất nặng thường không thể thực hiện nghiệm pháp đi bộ 6 phút để ghi nhận kết quả. Cơ chế dữ liệu khuyết ở đây là gì và xử lý thế nào?**
- A. MCAR (Khuyết hoàn toàn ngẫu nhiên); điền giá trị trung bình của cả nhóm vào các ô trống.
- B. MAR (Khuyết ngẫu nhiên); xóa bỏ toàn bộ các bệnh nhân nặng khỏi tập dữ liệu phân tích.
- C. MNAR (Khuyết không ngẫu nhiên vì lý do khuyết gắn liền với chính mức độ nặng của bệnh); cần mô hình hóa cơ chế khuyết và thực hiện phân tích độ nhạy (Sensitivity Analysis).
- D. Không phải là dữ liệu khuyết vì bệnh nhân từ chối làm xét nghiệm.

> **Đáp án đúng: C.**  
> *Giải thích:* Khi xác suất khuyết phụ thuộc vào chính giá trị của biến số hoặc mức độ trầm trọng của bệnh cảnh, đó là MNAR. Tuyệt đối không xóa bỏ tùy tiện hay điền mean imputation vì sẽ gây chệch nặng nề kết quả nghiên cứu.

---

### **Q5. Theo Thông tư 13/2025/TT-BYT của Bộ Y tế về Bệnh án Điện tử (EMR), mốc thời hạn bắt buộc hoàn thành triển khai EMR đối với các bệnh viện tại Việt Nam là khi nào?**
- A. Chậm nhất ngày 31/12/2026.
- B. Chậm nhất ngày 30/09/2025.
- C. Chậm nhất ngày 01/01/2030.
- D. Không quy định mốc thời hạn bắt buộc.

> **Đáp án đúng: B.**  
> *Giải thích:* Thông tư 13/2025/TT-BYT (thay thế Thông tư 46/2018/TT-BYT) quy định lộ trình bắt buộc hoàn thành triển khai bệnh án điện tử: các bệnh viện hoàn thành trước ngày 30/09/2025; các cơ sở khám chữa bệnh khác hoàn thành trước ngày 31/12/2026.

---

### **Q6. Một bộ dữ liệu nghiên cứu da liễu đạt chỉ số $k$-anonymity với $k = 5$. Kết luận nào sau đây là chuẩn xác nhất về mặt an toàn thông tin?**
- A. Bộ dữ liệu đã an toàn tuyệt đối và có thể công khai tự do mà không cần kiểm soát.
- B. Mỗi tổ hợp các thuộc tính bán định danh (quasi-identifiers) xuất hiện ít nhất 5 lần, giúp ngăn chặn việc liên kết định danh trực tiếp, nhưng vẫn có thể bị tấn công nếu thiếu đa dạng thuộc tính nhạy cảm ($l$-diversity) hoặc khi kẻ tấn công có tri thức nền phong phú.
- C. Bộ dữ liệu chỉ gồm đúng 5 người tham gia nghiên cứu.
- D. Dữ liệu đã đạt chuẩn mã hóa khóa công khai RSA.

> **Đáp án đúng: B.**  
> *Giải thích:* $k$-anonymity là rào chắn cơ bản chống liên kết đơn thuần, nhưng có điểm yếu là tính đồng nhất giá trị nhạy cảm (Homogeneity Attack), do đó cần bổ sung $l$-diversity và các cơ chế quản trị truy cập có kiểm soát.

---

### **Q7. Theo 7 tiêu chí của NIH Bridge2AI, để một bộ dữ liệu y sinh được công nhận là "Sẵn sàng cho Trí tuệ Nhân tạo (AI-Ready)", điều kiện tiên quyết nào sau đây là quan trọng nhất?**
- A. Bộ dữ liệu phải có dung lượng trên 10 Terabytes và định dạng bảng tính Excel.
- B. Dữ liệu phải có nguồn gốc sâu (Deep Provenance), mô tả đặc tính quần thể (Characterization), có giải trình trước mô hình, tuân thủ đạo đức/pháp lý và có khả năng tính toán tự động.
- C. Chỉ cần dữ liệu không có bất kỳ ô trống nào.
- D. Dữ liệu phải được bảo mật tuyệt đối, không chia sẻ cho bất kỳ ai.

> **Đáp án đúng: B.**  
> *Giải thích:* AI-ready trong y sinh không chỉ là kích thước lớn, mà là tính minh bạch, khả năng giải trình thuật toán, và vết nguồn gốc dữ liệu để tránh đưa "rác" vào mô hình học máy.

---

### **Q8. Sau khi đề tài thử nghiệm lâm sàng nghiệm thu, nhóm nghiên cứu xóa các tệp tin chứa dữ liệu gốc bằng lệnh Delete thông thường trên máy tính cá nhân. Thao tác này có đáp ứng tiêu chuẩn quản trị dữ liệu không?**
- A. Hoàn toàn đáp ứng vì dữ liệu đã nằm trong thùng rác (Recycle Bin).
- B. Không đáp ứng; việc tiêu hủy dữ liệu y sinh phải tuân thủ chuẩn NIST SP 800-88 Rev. 2 (Clear/Purge/Destroy), đảm bảo không thể phục hồi và bắt buộc phải lập Biên bản tiêu hủy an toàn.
- C. Chỉ cần format ổ đĩa một lần là đủ.
- D. Nghiên cứu lâm sàng không bao giờ được phép tiêu hủy dữ liệu.

> **Đáp án đúng: B.**  
> *Giải thích:* Lệnh xóa thông thường chỉ gỡ bỏ con trỏ tệp tin trong hệ điều hành, dữ liệu thô vẫn còn nguyên trên các cung từ ổ đĩa và có thể phục hồi dễ dàng bằng phần mềm thông dụng, tiềm ẩn rủi ro rò rỉ dữ liệu y tế nghiêm trọng.

---

### **Q9. Trong quy trình FAIRification 7 bước (Jacobsen et al., 2020), bước "Đánh giá mức độ FAIR" (Assess FAIRness) được thực hiện vào thời điểm nào?**
- A. Chỉ làm một lần duy nhất trước khi bắt đầu thu thập dữ liệu.
- B. Thực hiện ở bước cuối cùng của quy trình để đánh giá sản phẩm dữ liệu, và lặp lại định kỳ mỗi khi bộ dữ liệu có sự cập nhật hoặc thay đổi phiên bản.
- C. Không cần đánh giá nếu đã lưu trữ trên Zenodo.
- D. Do tạp chí khoa học tự động thực hiện, tác giả không cần quan tâm.

> **Đáp án đúng: B.**  
> *Giải thích:* Đánh giá mức độ FAIR là hoạt động thẩm định chất lượng cuối quy trình và có tính lặp lại (iterative) để duy trì tính liên thông và khả năng tái sử dụng bền vững của dữ liệu.

---

### **Q10. Một nhà nghiên cứu khẳng định: *"Dữ liệu của tôi đã đạt chuẩn FAIR, điều đó có nghĩa là tôi bắt buộc phải công khai toàn bộ dữ liệu thô của người bệnh lên mạng Internet để ai cũng có thể tải về"*. Luận điểm này đúng hay sai?**
- A. Đúng, vì chữ A trong FAIR là Accessible (Mở hoàn toàn cho cộng đồng).
- B. Sai; nguyên tắc FAIR không đồng nghĩa với Open Data vô điều kiện. Dữ liệu y tế nhạy cảm hoàn toàn có thể đạt chuẩn FAIR với siêu dữ liệu (metadata) công khai để người khác tìm thấy (Findable), nhưng quyền truy cập dữ liệu thô được kiểm soát nghiêm ngặt (Controlled Access qua DUA) để bảo vệ quyền riêng tư người bệnh.
- C. Đúng, vì các tổ chức tài trợ quốc tế cấm dữ liệu đóng.
- D. Sai, vì FAIR chỉ áp dụng cho tài liệu văn bản, không áp dụng cho dữ liệu bệnh nhân.

> **Đáp án đúng: B.**  
> *Giải thích:* Khẩu hiệu vàng của quản trị dữ liệu mở: *"Càng mở càng tốt, chỉ đóng khi cần thiết"* (As open as possible, as closed as necessary). Dữ liệu y tế bảo vệ người bệnh bằng cơ chế truy cập có kiểm soát (Controlled Access) nhưng vẫn tuân thủ đầy đủ 4 nguyên tắc FAIR.

---

## PHẦN 2. BÀI TẬP CAPSTONE TỰ ĐÁNH GIÁ (CAPSTONE SELF-ASSESSMENT)

### Tình huống giả định:
Bạn đóng vai trò là **Research Data Steward** hỗ trợ nhóm nghiên cứu thực hiện đề tài:  
*"Nghiên cứu ứng dụng Trí tuệ Nhân tạo đa phương thức hỗ trợ chẩn đoán và theo dõi bệnh nhân mày đay mạn tính (Chronic Urticaria) tại các bệnh viện đại học ở Việt Nam"*.  
- **Quy mô dự kiến:** 1.000 bệnh nhân, thu thập dữ liệu lâm sàng, ảnh tổn thương da, chỉ số xét nghiệm huyết thanh học và bảng câu hỏi chất lượng cuộc sống (UAS7, DLQI).

### Nhiệm vụ thực hành tự do của bạn:
Hãy tự soạn thảo một bộ hồ sơ **RDM Package** gồm 4 tài liệu sau (bằng tệp Markdown hoặc Word):
1. **Bản Kế hoạch Quản lý và Chia sẻ Dữ liệu (DMSP):** $\le 2$ trang, đầy đủ 6 thành tố cốt lõi (hoặc mẫu NOT-OD-26-046 tinh giản), chỉ định rõ kho lưu trữ dữ liệu (Zenodo).
2. **Từ điển Dữ liệu (Data Dictionary):** Định nghĩa ít nhất 10 biến số lâm sàng, chuẩn hóa định dạng, khoảng giá trị hợp lệ, và mã hóa từ vựng chuẩn (SNOMED CT, LOINC, ICD-10).
3. **Kế hoạch Bảo mật & Khử định danh:** Mô tả phương án loại bỏ các định danh HIPAA Safe Harbor, quy trình dịch chuyển ngày (Date Shifting) bảo toàn khoảng thời gian, và các bước xây dựng Hồ sơ Đánh giá tác động xử lý dữ liệu cá nhân (DPIA) theo Luật 91/2025/QH15 và Nghị định 356/2025/NĐ-CP.
4. **Kế hoạch FAIR & AI-Ready:** Mô tả phương án đóng gói dữ liệu kèm siêu dữ liệu mô tả nguồn gốc sâu (Deep Provenance) theo 7 tiêu chí Bridge2AI và lựa chọn giấy phép chia sẻ (CC BY 4.0 / Open Data License).

---

### Bảng Checklist Tự Đánh giá Bài tập Capstone (1 Trang)
*(Hãy tự tích chọn vào các ô dưới đây khi bạn hoàn thành sản phẩm của mình)*

- [ ] **Mục 1 — Bản DMSP ($\le 2$ trang):**
  - [ ] Nêu rõ loại dữ liệu (bảng lâm sàng, ảnh tổn thương sẩn phù có thước đo chuẩn, kết quả xét nghiệm).
  - [ ] Công cụ và mã nguồn phân tích được xác định (Python, R, REDCap) kèm cam kết công khai GitHub/Zenodo.
  - [ ] Chuẩn dữ liệu được áp dụng (OMOP CDM v5.4, SNOMED CT, LOINC).
  - [ ] Tên kho lưu trữ dữ liệu mở được chỉ định cụ thể (Zenodo Sandbox / Zenodo).
  - [ ] Nêu rõ người chịu trách nhiệm giám sát (PI và Data Steward).
- [ ] **Mục 2 — Từ điển Dữ liệu (Data Dictionary):**
  - [ ] Có đầy đủ tên biến, nhãn hiển thị, kiểu dữ liệu, đơn vị đo lường và danh mục mã hóa chuẩn.
  - [ ] Có quy tắc kiểm tra logic (Range check, Validation rule) để chặn lỗi nhập liệu ngay tại khâu thu thập.
- [ ] **Mục 3 — Bảo mật & Khử định danh:**
  - [ ] Loại bỏ toàn bộ 18 trường định danh trực tiếp theo chuẩn Safe Harbor.
  - [ ] Đối với dữ liệu ngày tháng: Áp dụng Date Shifting giữ nguyên số ngày giữa các lần khám và ghi rõ thuộc phương pháp Expert Determination / Limited Data Set (không nhầm với Safe Harbor tuyệt đối).
  - [ ] Dẫn chiếu đúng khung pháp lý hiện hành của Việt Nam: Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 và Nghị định 356/2025/NĐ-CP (thay thế Nghị định 13/2023/NĐ-CP).
- [ ] **Mục 4 — FAIR & Chuẩn AI-Ready:**
  - [ ] Bộ dữ liệu có tệp `README.md` mô tả đặc tính nhân khẩu học và nguồn gốc sâu (thiết bị chụp ảnh, ánh sáng chuẩn, quy trình tiền xử lý).
  - [ ] Lựa chọn giấy phép chia sẻ chuẩn mực (ví dụ: CC BY 4.0 cho dữ liệu tổng hợp / DUA cho dữ liệu truy cập có kiểm soát).

---

## PHẦN 3. BẢNG TỰ NGHIỆM THU HOÀN THÀNH KHÓA HỌC

Chúc mừng bạn đã hoàn thành hành trình học tập nghiên cứu dữ liệu y sinh! Hãy tự đối chiếu các tiêu chí dưới đây để ghi nhận kết quả cá nhân của bạn:

| Hạng mục học tập | Tiêu chí hoàn thành tự đánh giá | Tự xác nhận |
| :--- | :--- | :---: |
| **Đọc hiểu lý thuyết** | Đã hoàn thành việc đọc toàn bộ Module 0 đến Module 6 | [ ] Đã hoàn thành |
| **Quiz theo bài (M1–M6)** | Đã tự làm 24 câu hỏi kiểm tra và nắm vững lý do chọn đáp án đúng | [ ] Đã hoàn thành |
| **Quiz Tổng hợp Workflow** | Đạt ít nhất **24/34 câu hỏi** trên toàn khóa học, trong đó trả lời đúng ít nhất **2/3 câu Q1–Q3** | [ ] Đã hoàn thành |
| **Thực hành kỹ năng (Labs)** | Đã trải nghiệm các bài lab tự chọn (tối thiểu Lab 1 về DMPTool và Lab 2 về REDCap) | [ ] Đã hoàn thành |
| **Bài tập Capstone** | Đã tự thiết kế và đối chiếu đạt yêu cầu theo Bảng Checklist Capstone 1 trang | [ ] Đã hoàn thành |

> **Lời kết từ Ban Giảng huấn (iBME Lab, Đại học Bách khoa Hà Nội):**  
> Quản lý dữ liệu y sinh không phải là một công việc hành chính đơn thuần, mà là nền móng của sự liêm chính khoa học và đạo đức nghiên cứu y học. Kỹ năng bạn lĩnh hội từ khóa học này sẽ đồng hành cùng bạn trong từng công trình nghiên cứu, giúp các phát hiện khoa học của bạn luôn đáng tin cậy, có thể tái lập và đóng góp giá trị lâu dài cho sức khỏe cộng đồng.
