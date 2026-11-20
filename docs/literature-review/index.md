# Quản lý dữ liệu trong nghiên cứu y sinh: Yêu cầu từ thiết kế đề cương đến kết thúc nghiên cứu

# Biomedical Research Data Management: Requirements from Study Design to Research Completion

**Bản tổng hợp literature review — viết lại và hiệu đính từ bản Google Docs “Tổng Quan RDM Y Sinh” (60 trang, 25.133 từ, 334 tài liệu tham khảo) của TS. Hoàng Quang Huy.**
**Ngày hoàn thành:** 20/11/2026. **Ngày chốt mọi khẳng định về phiên bản chuẩn và văn bản pháp luật:** 20/11/2026. **Phạm vi:** 2015–2026.
**Nguồn:** toàn văn Google Docs đã trích xuất qua Google Docs API (`workspace/reviews/rdm-doc-2026-11-20/doc.txt`); bảng 334 tài liệu tham khảo chuẩn hóa APA (`workspace/your_files/rdm-334-tai-lieu-tham-khao-apa.md`); báo cáo nghiên cứu sâu ngày 19/11/2026 (`workspace/research_notes/biomedical-rdm-literature-review-20261119-1510/report.md`).

> **Năm hiệu đính quan trọng nhất so với bản Docs (chi tiết ở Phụ lục B):** (1) Thông tư 13/2025/TT-BYT — bệnh viện chậm nhất 30/9/2025, cơ sở khác chậm nhất 31/12/2026; (2) Nghị quyết 72-NQ/TW — khám miễn phí từ 2026 cho nhóm ưu tiên trước, các đối tượng còn lại từ 2028; (3) Tran và cộng sự về chính sách sức khỏe số Việt Nam là **2022**, *JMIR* 24(2), e32392, không phải 2025; (4) Luật 91/2025/QH15 hiệu lực 1/1/2026, Nghị định 356/2025 thay thế Nghị định 13/2023; (5) FHIR R6 chưa ban hành, OMOP CDM v5.4 là bản tham chiếu.

---

**Phần A — Tóm tắt, phương pháp tổng quan và vòng đời dữ liệu nghiên cứu**
**Part A — Abstract, Review Methods, and the Research Data Lifecycle**

Ngày chốt tài liệu và chuẩn: 20/11/2026. Số trích dẫn [n] là số trong danh mục Tài liệu tham khảo cuối bản tổng hợp này; chỉ các mục đã kiểm chứng đầy đủ mới được trích dẫn. Các mục còn ghi [CẦN KIỂM CHỨNG] trong bảng đó không được dùng làm trích dẫn, trừ ba trường hợp được ghi rõ cảnh báo trong văn bản ([1], [2], [3]).

---

## Tóm tắt

Bản tổng hợp này rà soát các yêu cầu quản lý dữ liệu trong nghiên cứu y sinh (biomedical research data management — RDM) xuyên suốt vòng đời nghiên cứu, trong phạm vi tài liệu 2015–2026. Đây là tổng hợp tường thuật có kiểm chứng nguồn gốc, không phải systematic review đầy đủ theo PRISMA: bài viết không trình bày lưu đồ PRISMA và không đưa ra số lượng bản ghi sàng lọc hay đưa vào, vì các số liệu đó không được lưu lại và không được bịa thêm. Bài viết hệ thống hóa vòng đời dữ liệu sáu giai đoạn — lập kế hoạch, thu thập, xử lý, phân tích, chia sẻ và lưu trữ dài hạn hoặc tiêu hủy — và chỉ ra rằng sai sót ở khâu lập kế hoạch khuếch đại chi phí làm sạch ở các giai đoạn sau và có thể làm mất giá trị tái sử dụng của toàn bộ tập dữ liệu. Quản trị dữ liệu được trình bày theo khung DAMA-DMBOK và mô hình HIMSS AMAM như công cụ tham chiếu và tự đánh giá, không phải chuẩn bắt buộc; vai trò Data Steward được phân tích qua ba hồ sơ bổ trợ: chính sách–tuân thủ, chuyên môn nghiên cứu và hạ tầng–kỹ thuật. Các mốc chuẩn đang chuyển đổi được hiệu đính theo ngày chốt 20/11/2026, đáng chú ý là FHIR R6 chưa ban hành và OMOP CDM v5.4 vẫn là bản tham chiếu. Kết quả cung cấp khung tham chiếu thống nhất cho các bệnh viện đại học khi xây dựng quy trình vận hành chuẩn về quản lý dữ liệu nghiên cứu y sinh.

**Từ khóa:** quản lý dữ liệu nghiên cứu; dữ liệu y sinh; vòng đời dữ liệu; nguyên tắc FAIR; quản trị dữ liệu; data steward.

## Abstract

This review examines the requirements of biomedical research data management (RDM) across the full research lifecycle, from study design to research completion, covering the literature from 2015 to 2026. It is a verified narrative synthesis, not a full PRISMA systematic review: it presents no PRISMA flow diagram and reports no numbers of records screened, excluded, or included, because those figures were not recorded in the source review and are not invented here. By checking the original texts of technical specifications, funder policies, and legal instruments, the review systematises a six-stage data lifecycle — planning, collection, processing, analysis, sharing, and long-term preservation or disposal — and shows that upstream errors, especially at the planning stage, amplify the cost of downstream data cleaning and can destroy the reuse value of an entire dataset. Data governance is presented through the DAMA-DMBOK reference framework and the HIMSS Adoption Model for Analytics Maturity (AMAM) as reference and self-assessment tools, not as mandatory standards, and the professionalisation of the Data Steward role is analysed through three complementary profiles: policy and compliance, research domain, and infrastructure. The review corrects several milestones for standards in transition as of 20 November 2026, notably that FHIR R6 has not yet been published, that OMOP CDM v5.4 remains the reference version, and that the Vietnamese legal milestones changed during 2025–2026. The result is a unified reference framework for university hospitals developing standard operating procedures for biomedical research data management.

**Keywords:** research data management; biomedical data; data lifecycle; FAIR principles; data governance; data steward.

---

## 1. Phương pháp tổng quan

### 1.1. Câu hỏi và phạm vi

Bản tổng hợp này trả lời câu hỏi: những yêu cầu nào về quản lý dữ liệu đặt ra cho nghiên cứu y sinh ở từng giai đoạn của vòng đời nghiên cứu, từ khi thiết kế đề cương đến khi kết thúc nghiên cứu. Phạm vi tài liệu là 2015–2026. Việc giữ tài liệu năm 2026 là quyết định có chủ đích, vì nhiều mốc cấu trúc rơi vào năm 2026: Phụ lục 2 của ICH E6(R3) về thử nghiệm phi truyền thống được thông qua Step 4 ngày 03/6/2026 [4], và Viện Y tế Quốc gia Hoa Kỳ (NIH) ban hành mẫu kế hoạch quản lý và chia sẻ dữ liệu (DMSP) tinh giản theo thông báo NOT-OD-26-046 ngày 25/02/2026 [5]. Ngày chốt là 20/11/2026; mọi khẳng định về phiên bản chuẩn hay hiệu lực văn bản đều được hiểu theo mốc đó. Phạm vi bao phủ y văn bình duyệt, đặc tả tiêu chuẩn chính thức, chính sách nhà tài trợ và cơ quan quản lý, và văn bản pháp luật về dữ liệu sức khỏe.

### 1.2. Nguồn và chiến lược tìm kiếm

Chiến lược tìm kiếm kế thừa từ bản tổng quan nguồn (Google Docs gốc, 60 trang, 12 mục) và được kiểm chứng lại theo từng nguồn gốc. Các cơ sở dữ liệu được rà soát gồm PubMed/MEDLINE, Scopus, Web of Science, IEEE Xplore và ACM Digital Library. Song song, bài viết truy vết trực tiếp văn bản gốc trên trang chính thức của tổ chức ban hành, vì các mốc phiên bản và hiệu lực thay đổi nhanh trong giai đoạn 2025–2026. Từ khóa bao quát tin học nghiên cứu lâm sàng, quản trị dữ liệu, dữ liệu FAIR, các chuẩn CDISC, HL7 FHIR và OMOP CDM/OHDSI, an toàn dữ liệu, và các kiến trúc phân tích bảo tồn quyền riêng tư (TRE, học liên kết, dữ liệu tổng hợp). Các công trình nền tảng trước năm 2015 có giá trị phương pháp luận bền vững được giữ lại làm ngoại lệ có chọn lọc; ví dụ nền tảng REDCap, công bố năm 2009 [6], vẫn là tài liệu gốc khi bàn về thu thập dữ liệu điện tử.

### 1.3. Tiêu chí lựa chọn và loại trừ

Tiêu chí lựa chọn ưu tiên: bài báo bình duyệt; khuyến nghị đồng thuận quốc tế; đặc tả tiêu chuẩn chính thức và hướng dẫn của cơ quan quản lý; chính sách nhà tài trợ và văn bản pháp quy của NIH, FDA, EMA, WHO cùng Quốc hội, Chính phủ và Bộ Y tế Việt Nam. Loại trừ: bài xã luận và quan điểm cá nhân thiếu căn cứ thực nghiệm, tài liệu thương mại của nhà cung cấp, và bản sao trùng lặp trên các kho không chính thức. Nguyên tắc xuyên suốt là ưu tiên nguồn gốc thay cho nguồn thứ cấp. Chẳng hạn, chính sách DMS của NIH được trích theo NOT-OD-21-013, hiệu lực 25/01/2023 [7], với sáu thành phần của DMSP theo NOT-OD-21-014 [8] và mẫu tinh giản theo NOT-OD-26-046 [5]; mẫu DMP của Horizon Europe được trích theo mẫu chính thức của Ủy ban châu Âu [3], với lưu ý năm và phiên bản của mẫu này còn ghi [CẦN KIỂM CHỨNG].

### 1.4. Thiết kế tổng hợp và giới hạn

Về thiết kế, đây là **tổng hợp tường thuật có kiểm chứng** (verified narrative synthesis), **không phải systematic review đầy đủ theo PRISMA**. Thứ nhất, bài viết không trình bày lưu đồ PRISMA và không đưa ra số lượng bản ghi sàng lọc, loại trừ hay đưa vào, vì bản tổng quan nguồn không lưu lại các số liệu đó. Thứ hai, bài viết không đánh giá rủi ro thiên lệch theo thang chuẩn cho từng nghiên cứu, mà thẩm định phản biện theo từng mốc, đối chiếu mỗi khẳng định về phiên bản chuẩn, ngày hiệu lực hay số liệu mạng lưới với văn bản gốc hoặc nguồn chính thức. Thứ ba, các chuẩn đang chuyển đổi được xử lý bằng quy tắc ghi ngày chốt: FHIR R5 (v5.0.0, 26/03/2023) là bản đặc tả hiện hành, FHIR R4 (4.0.1, 2019) vẫn là nền tảng triển khai chủ đạo, FHIR R6 chưa ban hành và đang ở vòng bỏ phiếu [9]; Hướng dẫn FHIR-to-OMOP v1.0.0 ánh xạ sang OMOP CDM v5.4 [10]; OMOP CDM v5.4 (9/2021) là bản tham chiếu, v6.0 không được tiếp tục, v5.5 còn mâu thuẫn giữa các nguồn thứ cấp [11]. Cuối cùng, hai tài liệu không được trích dẫn trong Phần A: mục 241 về suy giảm k-anonymity (Weatherhead và cộng sự, 2026), vì tên tác giả trùng lặp và chưa đối chiếu đầy đủ; và mục 196 (Inau và cộng sự, 2026), vì nội dung FAIRification chuyên biệt, để phần sau xem xét.

---

## 2. Vòng đời dữ liệu nghiên cứu y sinh

### 2.1. Sáu giai đoạn của vòng đời dữ liệu

Vòng đời dữ liệu nghiên cứu y sinh gồm sáu giai đoạn tương thuộc: (1) lập kế hoạch, (2) thu thập, (3) xử lý và chuẩn hóa, (4) phân tích, (5) chia sẻ và công bố, và (6) lưu trữ dài hạn hoặc tiêu hủy. Mỗi giai đoạn đặt ra một nhóm yêu cầu riêng, nhưng các yêu cầu đó liên kết với nhau qua các quyết định đã đưa ra ở thượng nguồn. Đặc tính then chốt của vòng đời này là hiệu ứng khuếch đại lỗi từ thượng nguồn. Một sai sót ở khâu lập kế hoạch — chẳng hạn không gắn mã thuật ngữ chuẩn cho biến lâm sàng hay thiếu điều khoản đồng thuận cho sử dụng thứ cấp — sẽ nhân lên chi phí làm sạch ở pha xử lý và có thể khiến toàn bộ tập dữ liệu mất giá trị tái sử dụng. Chính sách DMS của NIH thể hiện rõ logic này: DMSP nộp ngay trong hồ sơ xin tài trợ, tối đa hai trang với sáu thành phần, và kế hoạch đã phê duyệt là điều khoản ràng buộc [7], [8]. Nguyên tắc FAIR cũng chỉ thực hiện đầy đủ nếu được thiết kế từ đầu, vì tính tái sử dụng phụ thuộc vào siêu dữ liệu và giấy phép gắn ngay từ khâu lập kế hoạch [12]. Ở phía thực thi, Bộ thực hành quản lý dữ liệu lâm sàng tốt (GCDMP) của SCDM cung cấp khung vận hành xuyên suốt vòng đời, từ thiết kế biểu mẫu đến quản lý truy vấn và khóa cơ sở dữ liệu [13]. Vòng đời dữ liệu vì vậy là một đường ống liên tục, trong đó chất lượng mỗi giai đoạn là điều kiện tiên quyết cho giai đoạn tiếp theo.

### 2.2. Quản trị dữ liệu: DAMA-DMBOK và mô hình trưởng thành HIMSS AMAM

Quản trị dữ liệu (data governance) là hệ thống quyền quyết định, chính sách, tiêu chuẩn, trách nhiệm giải trình và cơ chế kiểm soát nhằm vận hành dữ liệu như một tài sản chiến lược có độ tin cậy cao; dữ liệu sức khỏe chịu đồng thời quy định đạo đức nghiên cứu, pháp luật bảo vệ dữ liệu cá nhân và yêu cầu của nhà tài trợ. ICH E6(R3) phản ánh bước chuyển này khi lần đầu tiên dành một mục riêng — Mục 4 của Phụ lục 1 — cho quản trị dữ liệu của nghiên cứu viên và nhà tài trợ, bao trùm toàn bộ vòng đời dữ liệu [4].

Bài viết dùng hai khung tham chiếu quốc tế — DAMA-DMBOK và HIMSS AMAM — với tư cách **khung tham chiếu, không phải chuẩn bắt buộc**. Khung DAMA-DMBOK đặt quản trị dữ liệu ở vị trí trục tâm điều phối mười miền tri thức vệ tinh: kiến trúc, mô hình hóa, lưu trữ–vận hành, an ninh, tích hợp–liên thông, tài liệu–nội dung, dữ liệu chủ–tham chiếu, kho dữ liệu–BI, siêu dữ liệu và chất lượng dữ liệu. Nội dung khung trong bài này dựa trên bản 2nd ed. đã xuất bản [14]; dự án DAMA-DMBOK 3.0, khởi động tháng 6/2025 theo trang dự án của DAMA International, chỉ được nêu như hướng phát triển về quản trị AI và đám mây [1] — ngày cập nhật và trạng thái của trang này còn ghi [CẦN KIỂM CHỨNG], nên các mở rộng của bản 3.0 không được dùng làm chuẩn bắt buộc. Các trung tâm y học hàn lâm thường triển khai cơ cấu quản trị ba tầng (điều hành, chiến lược, chiến thuật) [15]. Để đo lường tiến độ, các tổ chức có thể dùng mô hình trưởng thành phân tích HIMSS AMAM gồm tám cấp độ từ 0 đến 7, trong đó năng lực nghiên cứu và AI có quản trị chỉ thực sự hình thành từ cấp 5 trở lên [2]. Cần ghi rõ hai giới hạn: criteria sheet của HIMSS còn ghi [CẦN KIỂM CHỨNG] ngày ban hành, và HIMSS đã hiện đại hóa mô hình AMAM, nên mô tả các cấp 0–7 trong bài này theo bản criteria sheet cổ điển. AMAM vì vậy là thước tự đánh giá lộ trình trưởng thành, không phải ngưỡng tuân thủ bắt buộc.

### 2.3. Chuyên nghiệp hóa vai trò Data Steward

Khung quản trị chỉ vận hành được khi có con người đảm nhiệm vai trò quản trị dữ liệu một cách chuyên nghiệp. Data stewardship — khác với quản trị viên cơ sở dữ liệu CNTT thuần túy — bao hàm toàn bộ hoạt động lập kế hoạch và thực thi có trách nhiệm trên dữ liệu số trước, trong và sau dự án, bao phủ cả khía cạnh kỹ thuật, tổ chức và đạo đức [16]. Lộ trình quốc gia Hà Lan về chuyên nghiệp hóa data stewardship (Chương trình Khoa học Mở Quốc gia, NPOS) của Jetten và cộng sự (2021) xác định hồ sơ năng lực, chương trình đào tạo và lộ trình triển khai để đưa data stewardship thành nghề nghiệp được công nhận, thay vì công việc kiêm nhiệm [17]. Dựa trên lộ trình này, hệ sinh thái bệnh viện đại học cần tổ chức ba hồ sơ Data Steward bổ trợ lẫn nhau: *Policy Data Steward* (chính sách và tuân thủ) tham mưu quy chế dữ liệu cấp viện/trường và kiểm soát tuân thủ đạo đức, pháp luật bảo vệ dữ liệu cá nhân và chính sách nhà tài trợ; *Research/Domain Data Steward* (chuyên môn nghiên cứu) thường có trình độ thạc sĩ hoặc tiến sĩ y sinh, tư vấn kế hoạch quản lý dữ liệu, từ điển biến chuẩn hóa, khử định danh và lựa chọn kho công bố; *Infrastructure Data Steward* (hạ tầng và kỹ thuật) làm cầu nối với công nghệ thông tin và kỹ sư phần mềm nghiên cứu, xác định đặc tả kỹ thuật cho nền tảng thu thập dữ liệu điện tử, đường ống FHIR/OMOP và kho lưu trữ dài hạn [17]. The Turing Way mô tả tương tự data steward như vai trò hạ tầng nghiên cứu nhúng trong nhóm nghiên cứu, hỗ trợ nghiên cứu viên xuyên suốt vòng đời dữ liệu [18]. Điểm chung là data stewardship phải được tổ chức thành đội ngũ có năng lực phân tầng và lộ trình nghề nghiệp rõ ràng; nếu chỉ giao kiêm nhiệm hoặc chỉ đầu tư hạ tầng mà thiếu con người, các nguyên tắc FAIR sẽ khó đi vào thực tiễn [17], [12], [16].

---

*Tổng hợp từ Mục 3–4 của bản thảo gốc “Quản lý dữ liệu trong nghiên cứu y sinh: Yêu cầu từ thiết kế đề cương đến kết thúc nghiên cứu” (Google Docs, 60 trang), đối chiếu với các nguồn đã kiểm chứng trong nghiên cứu ngày 19/11/2026 và bảng tham khảo APA 334 mục. Số trích dẫn [n] là số trong danh mục Tài liệu tham khảo cuối bản tổng hợp này. Các mục còn ghi [CẦN KIỂM CHỨNG] trong bảng không được dùng làm căn cứ, hoặc được ghi rõ là chưa kiểm chứng.*

---

## §3. Thiết kế nghiên cứu và Kế hoạch quản lý dữ liệu (DMP)

### 3.1. Kế hoạch quản lý dữ liệu: từ yêu cầu của nhà tài trợ tới công cụ quản trị

Kế hoạch quản lý dữ liệu (DMP), hay Kế hoạch quản lý và chia sẻ dữ liệu (DMSP), đã trở thành điều kiện ràng buộc gắn với quyết định cấp kinh phí. Bước ngoặt quan trọng nhất là Chính sách Quản lý và Chia sẻ Dữ liệu của Viện Y tế Quốc gia Hoa Kỳ (NIH Data Management and Sharing Policy, NOT-OD-21-013), có hiệu lực ngày 25/01/2023 [7]. Chính sách này áp dụng cho mọi nghiên cứu do NIH tài trợ có phát sinh “dữ liệu khoa học” — dữ liệu đã ghi nhận, đủ chất lượng để xác thực và tái lập kết quả nghiên cứu — và loại trừ sổ tay phòng thí nghiệm, phân tích sơ bộ, phiếu CRF chưa xử lý hay mẫu sinh phẩm vật lý [7]. Mỗi hồ sơ xin tài trợ phải kèm một DMSP không quá hai trang, gồm sáu thành phần quy định trong thông báo bổ sung NOT-OD-21-014: (1) Loại dữ liệu; (2) Công cụ, phần mềm và/hoặc mã nguồn liên quan; (3) Tiêu chuẩn áp dụng; (4) Bảo quản, truy cập và mốc thời gian; (5) Các yếu tố hạn chế về truy cập, phân phối hoặc tái sử dụng; (6) Giám sát việc quản lý và chia sẻ dữ liệu [8]. Kế hoạch đã phê duyệt trở thành một điều khoản của quyết định tài trợ [7].

Dữ liệu phải được chia sẻ chậm nhất vào thời điểm công bố bài báo bình duyệt liên quan hoặc khi kết thúc thời gian tài trợ, tùy thời điểm nào đến trước — kể cả dữ liệu của các kết quả âm tính hoặc không được công bố [7]. Quy định này biến DMP thành cam kết có thời hạn ngay từ giai đoạn viết đề cương [8].

Ngày 25/02/2026, NIH ban hành Thông báo NOT-OD-26-046, thí điểm mẫu DMSP rút gọn thay bản sáu yếu tố văn xuôi cũ: hệ thống câu hỏi cam kết dạng Có/Không kèm bảng ánh xạ loại dữ liệu với kho lưu trữ và mục riêng cho dữ liệu hệ gen, bắt buộc với hồ sơ nộp từ ngày 25/05/2026 [5]. Chính sách DMS 2023 không đổi: phạm vi, nội dung thực chất và mốc chia sẻ giữ nguyên [5].

Ở châu Âu, chương trình Horizon Europe (2021–2027) yêu cầu quản lý dữ liệu theo nguyên tắc FAIR, với cam kết tóm tắt ở vòng đề xuất và DMP đầy đủ nộp chậm nhất vào tháng thứ sáu kể từ ngày ký hợp đồng, sau đó cập nhật định kỳ [19]. Nguyên tắc chỉ đạo là “mở tối đa có thể, đóng tối thiểu khi cần thiết” (*as open as possible, as closed as necessary*): dữ liệu được mở theo giấy phép CC BY hoặc CC0, siêu dữ liệu mở theo CC0, và mọi hạn chế — vì bảo vệ dữ liệu cá nhân theo GDPR, quyền sở hữu trí tuệ hay an ninh — đều phải được giải trình rõ ràng [19]. Mẫu DMP Horizon Europe [3] trong bảng tham khảo vẫn ghi [CẦN KIỂM CHỨNG] về năm và phiên bản, nên cần đối chiếu phiên bản hiện hành trước khi nộp [3]. Wellcome Trust áp dụng cùng triết lý: yêu cầu nộp kế hoạch quản lý dữ liệu ngay ở giai đoạn hồ sơ và gắn kết quả thực thi vào đánh giá các đợt xét duyệt tài trợ tiếp theo [20]. Điểm chung của ba nhà tài trợ là DMP không còn là sản phẩm phụ của đề cương mà là một đối tượng quản trị có vòng đời riêng: soạn thảo, phê duyệt, rà soát định kỳ và báo cáo tuân thủ [7] [19] [20].

### 3.2. Siêu dữ liệu, Phần tử dữ liệu chung và đề cương điện tử có cấu trúc

Một tập dữ liệu thiếu siêu dữ liệu ngữ cảnh sẽ nhanh chóng mất khả năng diễn giải và không thể được máy tính xử lý tự động [21]. Nguyên tắc FAIR — dữ liệu cần Tìm được (Findable), Truy cập được (Accessible), Tương tác được (Interoperable) và Tái sử dụng được (Reusable) — do Wilkinson và cộng sự công bố năm 2016, là khung tham chiếu nền tảng cho mọi quyết định về siêu dữ liệu ngay từ giai đoạn thiết kế [12]. FAIR là nguyên tắc, không phải tiêu chuẩn hay đặc tả kỹ thuật, nên mỗi dự án phải lựa chọn cụ thể chuẩn siêu dữ liệu, định danh bền vững và kho lưu trữ [12]. Quy trình FAIRification bảy bước trong ba pha của Jacobsen và cộng sự (2020) cung cấp trình tự thực hành cho việc này [21].

DataCite Metadata Schema là chuẩn dùng rộng rãi để gán định danh số lâu dài (DOI) và trích dẫn dữ liệu; phiên bản 4.6 (tháng 12/2024) duy trì sáu thuộc tính bắt buộc lõi — định danh, tác giả, tiêu đề, nhà xuất bản, năm xuất bản, loại tài nguyên — và bổ sung mở rộng cho y sinh học như liên kết mã định danh tài nguyên nghiên cứu (RRID) và DOI cho dự án [22]. Việc bổ sung siêu dữ liệu về sau thường tốn kém gấp nhiều lần so với ghi nhận ngay tại thời điểm thu thập [21] [22].

Ở tầng nội dung lâm sàng, Phần tử dữ liệu chung (Common Data Elements — CDE) là công cụ chuẩn hóa biến số trước khi thu thập. Kho CDE của NIH cung cấp định nghĩa biến và biểu mẫu chuẩn hóa để nhà nghiên cứu tích hợp ngay khi lập Từ điển dữ liệu (Data Dictionary), thay vì tự đặt tên biến và thang đo theo thói quen của từng nhóm [23]. Một từ điển dữ liệu chuẩn mực phải định nghĩa đồng bộ mã biến, mô tả lâm sàng, kiểu dữ liệu, khoảng giá trị, đơn vị chuẩn theo hệ UCUM, quy ước mã hóa giá trị khuyết và mã ánh xạ tới thuật ngữ quốc tế như LOINC, SNOMED CT hay thuật ngữ CDISC [23]. Việc thống nhất các yếu tố này ở giai đoạn thiết kế là điều kiện để dữ liệu đa trung tâm gộp lại được mà không cần làm sạch thủ công quy mô lớn [23] [21].

Giai đoạn 2025–2026 chứng kiến bước chuyển “chuẩn hóa từ thượng nguồn”: thay vì viết đề cương bằng văn bản tự do rồi diễn giải thủ công để dựng biểu mẫu thu thập điện tử và lập trình bảng dữ liệu, đề cương ngày càng được mã hóa ở dạng có cấu trúc, máy đọc được, để tự động sinh biểu mẫu thu thập chuẩn và khung ánh xạ dữ liệu nhất quán [4]. Hướng chuyển đổi này phù hợp với tinh thần hiện đại hóa của ICH E6(R3), trong đó quản trị dữ liệu và hệ thống máy tính hóa được nâng thành một chương độc lập [4]. Tuy nhiên, các mốc cụ thể về ICH M11 (CeSHarP), mô hình CDISC USDM và sáng kiến CDISC 360i trong bản thảo gốc chưa được kiểm chứng từ nguồn gốc (ich.org, cdisc.org) và cần đối chiếu trực tiếp với văn bản gốc trước khi trích dẫn.

---

## §4. Thu thập dữ liệu

### 4.1. Nền tảng thu thập dữ liệu điện tử (EDC/eCRF)

Chuyển từ phiếu giấy (CRF) sang nền tảng Thu thập Dữ liệu Điện tử (EDC/eCRF) giúp cắt giảm lỗi sao chép thủ công, kiểm tra tính hợp lệ tức thời tại điểm nhập liệu và ghi nhận tự động dấu vết kiểm toán (audit trail) [6]. REDCap là ví dụ kinh điển và được kiểm chứng tốt nhất: Harris và cộng sự (2009) mô tả REDCap như một phương pháp luận dựa trên siêu dữ liệu (metadata-driven), trong đó biểu mẫu thu thập được định nghĩa bằng siêu dữ liệu thay vì lập trình riêng cho từng nghiên cứu [6].

Lựa chọn EDC tối ưu đòi hỏi cân đối quy mô nghiên cứu, ngân sách, yêu cầu đệ trình pháp lý (FDA/EMA/PMDA) và năng lực thẩm định hệ thống máy tính hóa (CSV) của đơn vị chủ trì [4] [24]. Với thử nghiệm do nhà nghiên cứu khởi xướng quy mô vừa và nhỏ, các nền tảng EDC hạng nhẹ như Castor EDC triển khai nhanh với giao diện không cần lập trình, tích hợp sẵn đồng thuận điện tử (eConsent) và báo cáo kết quả do người bệnh tự báo cáo (ePRO) [25]. Ngược lại, thử nghiệm đa trung tâm quy mô lớn, có yêu cầu đệ trình dược phẩm, thường cần nền tảng doanh nghiệp với khả năng tùy biến sâu và tích hợp hệ thống quản lý thử nghiệm lâm sàng (CTMS) — đi kèm thời gian thiết lập dài hơn và nhu cầu đào tạo chuyên sâu hơn [4].

Một khía cạnh thường bị bỏ qua khi chọn EDC là khả năng chuyển đổi chuẩn về sau: dữ liệu REDCap có thể chuyển sang CDISC SDTM bằng REDCap2SDTM [26] và sang OMOP Common Data Model bằng REDCap2OMOP (Hội nghị OHDSI 2021) [27], tránh dữ liệu bị “khóa” trong định dạng riêng của nhà cung cấp [26] [27]. Về minh bạch số liệu, bản tổng hợp này không trích lại các con số quy mô do nhà cung cấp tự công bố hay các mức giá thương mại của REDCap, Castor EDC và Medidata Rave trong bản thảo gốc, vì các con số đó không kèm nguồn gốc có ngày đo kiểm chứng được [6] [25].

### 4.2. Từ ALCOA đến ALCOA++: toàn vẹn dữ liệu, ICH E6(R3) và 21 CFR Part 11

Toàn vẹn dữ liệu (Data Integrity) là thước đo nền tảng quyết định việc cơ quan quản lý chấp nhận hay bác bỏ bằng chứng từ một nghiên cứu lâm sàng [4]. Khung nguyên tắc ALCOA gốc gồm năm thuộc tính tập trung vào thời điểm tạo lập bản ghi: Quy trách nhiệm được (Attributable), Đọc được (Legible), Đồng thời (Contemporaneous), Nguyên bản hoặc bản sao chứng thực (Original) và Chính xác (Accurate) [4]. Năm yếu tố này được Stan W. Woollen thuộc Văn phòng Thực thi của FDA đặt ra từ đầu thập niên 1990 như một công cụ ghi nhớ trong các bài thuyết trình về GLP và giám sát nghiên cứu sinh học — và cần nhấn mạnh rằng ALCOA không nằm trong bất kỳ quy định pháp lý nào, kể cả 21 CFR Part 11, GLP, GMP hay GCP [4]. Khi hồ sơ điện tử phổ biến, ALCOA được mở rộng thành ALCOA+ với bốn yếu tố quản trị vòng đời — Đầy đủ (Complete), Nhất quán (Consistent), Bền vững (Enduring), Sẵn có (Available) — dùng trong hướng dẫn MHRA (2018) và các văn bản WHO, PIC/S, rồi thành ALCOA++ khi hướng dẫn EMA năm 2023 về hệ thống máy tính hóa bổ sung thuộc tính thứ mười, Truy vết được (Traceable) [4]. Dù tên gọi mở rộng, kỳ vọng thanh tra về thực chất không thay đổi [4]. Giới hạn nguồn: bảng tham khảo không có mục riêng đã kiểm chứng cho hướng dẫn MHRA 2018, WHO TRS 1033 hay hướng dẫn EMA 2023 — cần trích trực tiếp từ nguồn gốc trước khi nộp [4] [24].

ICH E6(R3) — Hướng dẫn Thực hành Lâm sàng Tốt phiên bản R3, được ICH thông qua ở Bước 4 ngày 06/01/2025 — gồm 11 nguyên tắc (R2 có 13) cùng Phụ lục 1 về thử nghiệm can thiệp và Phụ lục 2 về thử nghiệm phi tập trung, thực dụng và dữ liệu đời thực [4]. Điểm thay đổi quan trọng nhất là Mục 4 mới của Phụ lục 1 — chương độc lập đầu tiên về Quản trị dữ liệu cho Nghiên cứu viên và Nhà tài trợ — bao trùm bảo vệ làm mù (4.1), tám yếu tố vòng đời dữ liệu gồm siêu dữ liệu và audit trail (4.2), và tám yêu cầu đối với hệ thống máy tính hóa (4.3) [4]. Hướng dẫn cấm nhà tài trợ nắm quyền kiểm soát độc quyền dữ liệu và tự ý sửa dữ liệu khi thiếu căn cứ và đồng thuận trước bằng văn bản; yêu cầu thẩm định hệ thống dựa trên rủi ro, tập trung vào các chức năng trọng yếu như ngẫu nhiên hóa và thu thập tiêu chí chính; và chỉ cho phép kích hoạt hệ thống tại điểm nghiên cứu sau khi có đủ phê duyệt pháp lý và đạo đức [4]. Phụ lục 2 được ICH thông qua ở Bước 4 ngày 03/06/2026, hiệu lực tại EU từ ngày 15/01/2027 [4].

Quy định 21 CFR Part 11 của FDA về Hồ sơ điện tử và Chữ ký điện tử — ban hành ngày 20/03/1997, hiệu lực ngày 20/08/1997 — là khung pháp lý nền tảng xác định khi nào hồ sơ và chữ ký điện tử được coi là đáng tin cậy và tương đương với hồ sơ giấy và chữ ký viết tay [24]. Hướng dẫn Q&A cuối cùng của FDA về hệ thống điện tử, hồ sơ điện tử và chữ ký điện tử trong nghiên cứu lâm sàng (tháng 10/2024, thay thế hướng dẫn năm 2007) làm rõ rằng audit trail phải ghi đầy đủ mọi chỉnh sửa trên trường dữ liệu đã hoàn tất mà không che khuất giá trị cũ, và với Công nghệ Y tế Số như thiết bị đeo phải xác định rõ nguồn gốc dữ liệu (data originator) [24].

### 4.3. Đánh giá chất lượng dữ liệu và bước ngoặt quản trị chất lượng dựa trên rủi ro (RBQM)

Chất lượng dữ liệu cần được đo lường bằng khung đánh giá rõ ràng: Weiskopf và Weng (2013) tổng hợp năm chiều — đầy đủ, đúng đắn, đồng nhất, hợp lý và thời sự — trong đó ba chiều đầu là các thuộc tính gốc không thể quy giản [28].

Mô hình kiểm soát truyền thống dựa vào Kiểm chứng dữ liệu nguồn 100% (100% Source Data Verification — SDV) tại chỗ kết hợp Quản lý truy vấn dữ liệu theo quy trình chuẩn của SCDM [13]. Tuy nhiên, Sheetz và cộng sự (2014), trong nghiên cứu của TransCelerate BioPharma, cho thấy việc kiểm chứng toàn bộ không tương xứng với giá trị chất lượng thu được, tạo cơ sở cho bước chuyển sang Quản trị chất lượng dựa trên rủi ro (Risk-Based Quality Management — RBQM), gắn với tư duy Chất lượng từ thiết kế (Quality by Design) của ICH E8(R1) và ICH E6(R3) [4] [29].

Khung RBQM tái thiết quy trình qua bốn mắt xích: nhận diện các yếu tố trọng yếu với chất lượng (Critical-to-Quality — CtQ), thiết lập ngưỡng kiểm soát (Quality Tolerance Limits — QTLs) và bộ Chỉ số Rủi ro Chính (Key Risk Indicators — KRIs), báo cáo khi vượt ngưỡng chấp nhận, và phân tích nguyên nhân gốc kèm hành động khắc phục–phòng ngừa (CAPA) [4]. Giám sát thống kê trung tâm không loại bỏ mà tối ưu hóa giám sát tại chỗ: phát hiện sớm bất thường thống kê xuyên trung tâm để kích hoạt kiểm tra có mục tiêu tại những điểm có chỉ số hiệu năng suy giảm [4] [29]. Về bằng chứng định lượng, bản tổng hợp này không trích lại các con số về ngân sách giám sát, số lượng truy vấn hay mức tiết kiệm chi phí trong bản thảo gốc, vì các con số đó bắt nguồn từ các bài viết thị trường thứ cấp (trong đó có các mục intuitionlabs.ai đã được yêu cầu loại khỏi danh mục học thuật) và không có nguồn gốc độc lập, có ngày tháng để kiểm chứng.

*Thuộc bản tổng hợp literature review tiếng Việt "Quản lý dữ liệu trong nghiên cứu y sinh: Yêu cầu từ thiết kế đề cương đến kết thúc nghiên cứu". Phần này gồm §5 và §6 của bản tổng hợp.*

**Quy ước trích dẫn.** Số trong ngoặc vuông [n] là số thứ tự trong bảng 334 tài liệu tham khảo đã chuẩn hóa APA 7th (`rdm-334-tai-lieu-tham-khao-apa.md`). Các tài liệu ghi "(tài liệu bổ sung)" không nằm trong bảng 334 mục mà được bổ sung từ nghiên cứu kiểm chứng ngày 19–20/11/2026; trích dẫn đầy đủ của chúng được ghi ngay trong văn bản. **Ngày chốt thông tin: 20/11/2026.** Mọi khẳng định về phiên bản chuẩn được ghi theo trạng thái tại ngày này.

---

## §5. Làm sạch, dữ liệu khuyết và tái lập

Làm sạch dữ liệu, xử lý dữ liệu khuyết và khả năng tái lập là một chuỗi liên tục: chất lượng đầu vào chỉ có ý nghĩa khi được đo bằng khung tường minh; dữ liệu khuyết chỉ xử lý đúng khi cơ chế sinh ra nó đã được phân loại; và mọi quyết định chỉ có giá trị khi người khác tái dựng được từ dữ liệu thô và mã phân tích.

### 5.1. Chất lượng dữ liệu EHR: hai khung đánh giá bổ trợ nhau

Hồ sơ bệnh án điện tử (EHR) được sinh ra để phục vụ chăm sóc lâm sàng, không phải để phục vụ nghiên cứu; vì vậy tái sử dụng thứ cấp dữ liệu EHR phải bắt đầu bằng đánh giá chất lượng có hệ thống, thay vì mặc nhiên giả định dữ liệu đầy đủ và đúng [28]. Weiskopf và Weng (2013) xác định năm chiều chất lượng: *completeness* (hiện diện), *correctness* (đúng với thực tế), *concordance* (nhất quán giữa các nguồn), *plausibility* (hợp lý theo tri thức lâm sàng) và *currency* (kịp thời) [28]. Năm chiều này không gộp thành một điểm số duy nhất, bởi mỗi chiều phát hiện một loại lỗi khác nhau: một trường dữ liệu có thể đầy đủ nhưng vẫn sai — như huyết áp ghi đều đặn mà sai đơn vị đo — và mâu thuẫn giữa chẩn đoán, thuốc đã kê và xét nghiệm thường báo hiệu lỗi ánh xạ hoặc nhập liệu [28].

Khung hài hòa của Kahn và cộng sự (2016) bổ sung một ngôn ngữ đánh giá thống nhất, gồm ba nhóm: *conformance* (tuân thủ định dạng, quan hệ và quy tắc tính toán đã định), *completeness* và *plausibility* — trong đó plausibility gồm tính duy nhất và tính hợp lý theo thời gian [30]. Đóng góp phương pháp luận quan trọng nhất của khung này là phân biệt *verification* (kiểm tra nội bộ theo quy tắc định trước) với *validation* (đối chiếu với chuẩn bên ngoài độc lập): một bộ dữ liệu có thể vượt qua verification mà vẫn trượt validation, nên chỉ báo cáo một trong hai là chưa đủ [30]. Cả hai khung hội tụ ở nguyên tắc *fitness for use*: chất lượng chỉ có nghĩa khi gắn với mục đích phân tích cụ thể; cùng một bộ dữ liệu có thể đủ tốt cho mô tả dịch tễ nhưng không đủ tốt cho suy diễn nhân quả [134, 135].

Về vận hành, ba nguyên tắc rút ra là: đo chất lượng theo từng chiều trước khi phân tích; thực thi quy tắc làm sạch bằng mã có kiểm soát phiên bản, không ghi đè dữ liệu thô; và tách tập huấn luyện–kiểm thử trước khi ước lượng tham số làm sạch hay chuẩn hóa, để tránh rò rỉ dữ liệu [134, 135].

*Lưu ý [30]: nội dung khung đánh giá và DOI đã kiểm chứng; danh sách tác giả đầy đủ vẫn cần đối chiếu PMC5051581 để ghi đúng 20 tác giả đầu theo APA 7th trước khi nộp.*

### 5.2. Dữ liệu khuyết: phân loại cơ chế trước khi chọn phương pháp xử lý

Dữ liệu khuyết là thực tế phổ biến trong nghiên cứu y sinh, nhưng sai lầm thường gặp nhất không phải là có dữ liệu khuyết, mà là xử lý nó khi chưa xác định cơ chế sinh ra nó. Phân loại nền tảng của Rubin (1976) chia dữ liệu khuyết thành ba cơ chế: khuyết hoàn toàn ngẫu nhiên (MCAR) — xác suất khuyết độc lập với mọi dữ liệu; khuyết ngẫu nhiên có điều kiện (MAR) — xác suất khuyết phụ thuộc vào các biến đã quan sát nhưng độc lập với chính giá trị bị khuyết sau khi điều chỉnh theo các biến đó; và khuyết không ngẫu nhiên (MNAR) — xác suất khuyết phụ thuộc trực tiếp vào chính giá trị không đo được [31]. Trong thực tế, MCAR hiếm khi xảy ra; MNAR phổ biến trong EHR dưới dạng "sự hiện diện mang tính thông tin": xét nghiệm chỉ được chỉ định khi có nghi ngờ lâm sàng, nên việc thiếu xét nghiệm tự thân mang thông tin về sức khỏe ẩn của bệnh nhân.

Phân tích trên ca hoàn chỉnh làm mất lực thống kê và gây chệch ngay khi MCAR bị vi phạm; gán giá trị đơn bằng giá trị trung bình làm hẹp giả tạo sai số chuẩn và phá vỡ tương quan giữa các biến; còn mang giá trị quan sát cuối về trước (LOCF) có thể gây chệch theo cả hai chiều [32]. Sterne và cộng sự (2009) khuyến nghị đa gán giá trị (multiple imputation — MI) là chuẩn mực dưới MAR: tạo nhiều bộ dữ liệu đã gán, ước lượng độc lập rồi hợp nhất theo quy tắc Rubin, bảo toàn cả phương sai lấy mẫu lẫn độ bất định do gán gây ra [32].

Hai giới hạn thường bị bỏ qua: dữ liệu quan sát không thể phân biệt dứt khoát MAR với MNAR, nên dưới nghi ngờ MNAR bắt buộc phải phân tích độ nhạy dưới nhiều giả định về cơ chế khuyết; và mô hình gán phải được mô tả đầy đủ — gồm toàn bộ biến đưa vào mô hình và cách lập luận về cơ chế khuyết, tốt nhất bằng đồ thị nhân quả — chứ không thể chỉ ghi "đã dùng multiple imputation" [32]. Khi báo cáo, cần nêu tỷ lệ khuyết theo biến chính, cơ chế khuyết giả định và căn cứ, phương pháp xử lý đã chọn và lý do, cùng kết quả phân tích độ nhạy.

### 5.3. Khủng hoảng tái lập: hệ quả của những quyết định không được lưu vết

Chuỗi làm sạch — xử lý khuyết không chỉ là vấn đề kỹ thuật nội bộ, mà là một phần của cuộc khủng hoảng tái lập trong khoa học. Khảo sát của Baker (2016) trên 1.576 nhà khoa học cho thấy hơn 70% số người tham gia từng không thể tái lập thí nghiệm của một nhóm nghiên cứu khác, và 52% nhận định khoa học đang trải qua một cuộc khủng hoảng tái lập nghiêm trọng [33]. Con số này thường được quy cho cỡ mẫu nhỏ, áp lực công bố hay gian lận; nhưng có một nguyên nhân âm thầm hơn và trực tiếp liên quan tới mục này: các quyết định làm sạch và xử lý dữ liệu khuyết không được ghi lại đầy đủ. Khi các quyết định ấy chỉ tồn tại trong trí nhớ của người phân tích hoặc trong một bảng tính không có kiểm soát phiên bản, ngay cả chính nhóm nghiên cứu đó cũng khó tái dựng kết quả của mình sau vài tháng, huống chi một nhóm độc lập.

Vì vậy, khả năng tái lập là tiêu chí kiểm tra của toàn bộ §5: quy trình làm sạch đạt chuẩn là quy trình người khác chạy lại được từ dữ liệu thô, và cách xử lý khuyết đạt chuẩn là cách xử lý mà người khác đánh giá lại được giả định cơ chế của nó. Đầu tư cho lưu vết ở thượng nguồn luôn rẻ hơn truy vết ngược ở hạ nguồn, khi kết quả đã công bố và không ai còn nhớ một giá trị đã bị sửa như thế nào.

---

## §6. Chuẩn dữ liệu: CDISC, FHIR và OMOP bổ trợ nhau

### 6.1. Luận điểm trung tâm: ba chuẩn, ba chức năng, một kiến trúc

Một sai lầm kiến trúc phổ biến là xem CDISC, HL7 FHIR và OMOP CDM như các tiêu chuẩn loại trừ nhau để chọn lấy một chuẩn duy nhất. Đồng thuận tin học y sinh giai đoạn 2024–2026 khẳng định: ba hệ chuẩn đảm nhiệm ba chức năng bổ trợ, không cạnh tranh — FHIR phục vụ trao đổi lâm sàng thời gian thực; CDISC phục vụ thu thập, lập bảng và đệ trình pháp lý cho thử nghiệm lâm sàng can thiệp; và OMOP CDM phục vụ phân tích quần thể và nghiên cứu quan sát thứ cấp trên dữ liệu đời thực. Chọn một chuẩn duy nhất vì vậy là tự cắt bỏ một chức năng mà hai chuẩn còn lại mới đảm nhiệm được.

| Chiều so sánh | CDISC (CDASH / SDTM / ADaM) | HL7 FHIR (R4 / R5) | OMOP CDM (v5.4) |
|---|---|---|---|
| Mục đích cốt lõi | Thu thập, lập bảng, phân tích dữ liệu thử nghiệm lâm sàng để đệ trình | Trao đổi lâm sàng thời gian thực; kết nối ứng dụng với EHR | Nghiên cứu quan sát đa trung tâm, bằng chứng đời thực, cảnh giác dược |
| Mô hình dữ liệu | Bảng phẳng (SDTM), tập phân tích (ADaM), Define-XML | Tài nguyên mô-đun qua REST API | Bảng quan hệ chuẩn lấy bệnh nhân làm trung tâm |

Nguyên tắc chung nối ba hệ chuẩn lại là khả năng liên thông (Interoperable) trong bộ nguyên tắc FAIR: dữ liệu và siêu dữ liệu phải dùng ngôn ngữ chung, từ vựng chung và tham chiếu chuẩn để máy có thể đọc và kết hợp được [12]. FAIR là nguyên tắc, không phải tiêu chuẩn kỹ thuật; CDISC, FHIR và OMOP là ba phương tiện khác nhau để hiện thực hóa cùng một nguyên tắc đó trên ba tầng của vòng đời dữ liệu [12]. Hệ quả là các cầu nối chính thức giữa các chuẩn, như Hướng dẫn ánh xạ FHIR to CDISC (01/9/2021) giữa FHIR R4 với CDASH IG v2.1, SDTMIG v3.2 và LAB v1.0.1 [34].

### 6.2. HL7 FHIR: từ trao đổi lâm sàng tới nghiên cứu

HL7 FHIR thay chi phí tích hợp điểm-điểm của các chuẩn cũ (HL7 v2, C-CDA) bằng kiến trúc RESTful API hiện đại và các tài nguyên mô-đun. Về phiên bản tại ngày chốt 20/11/2026: R4 (4.0.1, 2019) vẫn là nền tảng triển khai và quy định chủ đạo; R5 (5.0.0), xuất bản 26/3/2023, là bản chính thức hiện tại (Standard for Trial Use) [9]; còn R6 chưa phát hành chính thức mà vẫn đang ở vòng bỏ phiếu (ballot 5, 17/7/2026), nên không được trình bày như phiên bản đã ổn định [35].

Bước ngoặt đưa FHIR từ chuẩn trao đổi thành nền tảng nghiên cứu là SMART on FHIR của Mandel và cộng sự (2016): nền tảng ứng dụng chuẩn hóa, liên thông cho hồ sơ bệnh án điện tử, trong đó ứng dụng được "viết một lần, chạy trên nhiều EHR" nhờ xác thực OAuth 2.0 và OpenID Connect [36]. Nhờ đó, ứng dụng nghiên cứu truy cập được dữ liệu lâm sàng có cấu trúc ngay tại nguồn — thay vì mỗi nhóm trích xuất thủ công rồi làm sạch lại từ đầu — với phân quyền và kiểm toán đầy đủ [36]. Mở rộng tiếp theo là FHIR Bulk Data Access của Mandl và cộng sự (2020): giao diện truy xuất quần thể ($export) cho phép xuất dữ liệu mức bệnh nhân của toàn bộ một quần thể, theo quy định ONC thi hành Đạo luật 21st Century Cures Act của Hoa Kỳ [37].

### 6.3. OMOP CDM và mạng lưới OHDSI: chuẩn phân tích quần thể

OMOP CDM do cộng đồng OHDSI phát triển áp dụng cấu trúc bảng quan hệ phẳng, thống nhất cả cú pháp lẫn ngữ nghĩa cho phân tích dữ liệu lớn. Nền tảng được đặt bởi hai công trình: Hripcsak và cộng sự (2015) mô tả OHDSI như một mạng lưới mở mà điều kiện tham gia là chuyển đổi dữ liệu về OMOP CDM — một mô hình thông tin "mạnh", biểu diễn dữ liệu chăm sóc sức khỏe nhất quán giữa các cơ sở [38]; và Overhage và cộng sự (2012) kiểm chứng bằng cách nạp dữ liệu từ 10 cơ sở dữ liệu quan sát vào các thể hiện OMOP CDM, cho thấy khả năng biểu diễn và hiệu năng phân tích chấp nhận được cho giám sát an toàn chủ động [39].

Về phiên bản, OMOP CDM v5.4 (tháng 9/2021) là bản tham chiếu có độ tương thích công cụ rộng nhất tại ngày chốt 20/11/2026; v6.0 đã không được tiếp tục; còn v5.5 vẫn mâu thuẫn giữa các nguồn thứ cấp trong năm 2026, nên bản tổng hợp không trình bày v5.5 như phiên bản đã ổn định [11]. Theo OHDSI, tính đến cuối năm 2025, mạng lưới có 4.833 cộng tác viên ở 88 quốc gia, 544 nguồn dữ liệu ở 54 quốc gia và 974 triệu hồ sơ bệnh nhân duy nhất [11]. Các con số này được kiểm chứng theo ấn phẩm *OHDSI 2025 Year in Review* (tháng 12/2025); trong bảng 334 mục, số liệu tương ứng được ghi tại mục [11] (*Our Journey* 2025).

Minh chứng kinh điển là nghiên cứu LEGEND-HTN của Suchard và cộng sự (2019): so sánh hiệu quả và an toàn các nhóm thuốc hạ áp đầu tay trên 4,9 triệu bệnh nhân, với 22.000 tỷ số nguy hại đã hiệu chuẩn điểm xu hướng [40]. Thiazide liên quan đến nguy cơ thấp hơn có ý nghĩa so với thuốc ức chế men chuyển (ACEi) về nhồi máu cơ tim cấp (HR 0,84), nhập viện do suy tim (HR 0,83) và đột quỵ (HR 0,83); KTC 95% của các ước lượng này nằm trong khoảng 0,74–0,95 [40]. Về phương pháp luận, LEGEND-HTN chạy theo mô hình phân tích phân tán — mã phân tích tới từng cơ sở, chạy tại chỗ, chỉ gửi về thống kê tổng hợp — nên nghiên cứu 4,9 triệu bệnh nhân không cần gom dữ liệu thô về một máy chủ trung tâm [19, 185].

### 6.4. Cầu nối FHIR-to-OMOP: nơi sự bổ trợ phải được kiểm toán

FHIR được tối ưu cho trao đổi từng hồ sơ, nên truy vấn quần thể lớn qua API có thể làm quá tải máy chủ lâm sàng — đó là lý do tồn tại của tầng phân tích OMOP, và là lý do cầu nối dưới đây phải là một đường ống có kiểm soát. Cột mốc hợp tác giữa HL7 và OHDSI là *FHIR to OMOP Implementation Guide* v1.0.0 (Informative), dựa trên FHIR R5 và ánh xạ lõi tài nguyên FHIR sang OMOP CDM v5.4; bản 2.0.0-ballot đang được xây dựng tính đến tháng 10/2026 [10]. Hướng dẫn này hệ thống hóa bốn dạng mất mát cấu trúc khi chuyển đổi từ chuẩn trao đổi sang chuẩn phân tích [10]: mất mát độ trung thực (mã bệnh chi tiết trên FHIR phải quy về khái niệm chuẩn OMOP rộng hơn); mất mát thông tin (chi tiết ngữ cảnh trên FHIR, như thời điểm chứng kiến cấp phát thuốc, không có cột tương ứng trong OMOP); mất mát quan hệ (liên kết chẩn đoán–thuốc bị tách vào các bảng CONDITION_OCCURRENCE và DRUG_EXPOSURE, chỉ phục hồi được bằng suy diễn thời gian); và mất mát độ chính xác và độ phân giải thời gian (OMOP yêu cầu ngày kết thúc dùng thuốc mà FHIR không có; dấu thời gian chính xác cao bị hạ cấp xuống ngày hoặc năm) [10].

Chuyển đổi FHIR-to-OMOP vì vậy không bao giờ là không mất mát và phải được đối soát định lượng — độ bao phủ trường ánh xạ, độ bao phủ khái niệm chuẩn, đối soát số dòng nạp, tỷ lệ suy giảm độ chính xác thời gian — với chủ sở hữu giải trình cho từng chỉ số, thay vì chỉ kiểm tra "đã chạy xong ETL". Điểm nối trở lại §5: đường ống chuyển đổi không có chỉ số đối soát cũng giống như quy trình làm sạch không có khung đánh giá chất lượng [8, 134, 135].

Kết lại, kiến trúc khuyến nghị là: FHIR ở tầng trao đổi lâm sàng, CDISC ở tầng thu thập và đệ trình thử nghiệm, OMOP ở tầng phân tích quần thể — và đầu tư vào các cầu nối có kiểm toán (FHIR-to-CDISC [34], FHIR-to-OMOP [10]) thay vì chọn một chuẩn duy nhất. Một bệnh viện đại học không cần bắt dữ liệu nói một thứ ngôn ngữ duy nhất; điều nó cần là dữ liệu nói được ba thứ ngôn ngữ đó một cách nhất quán và có kiểm chứng.

---

> Thuộc bản tổng hợp literature review tiếng Việt: *Quản lý dữ liệu trong nghiên cứu y sinh: Yêu cầu từ thiết kế đề cương đến kết thúc nghiên cứu*.
> Phần này gồm §7 và §8, viết trên nền Mục 7–8 của bản thảo gốc (Google Docs *Tổng Quan RDM Y Sinh*, 60 trang). Số trích dẫn [n] là số trong danh mục Tài liệu tham khảo cuối bản tổng hợp này. Các mục còn [CẦN KIỂM CHỨNG] không được dùng làm căn cứ, trừ trường hợp ghi rõ.

## §7. FAIR, FAIRification và khoa học mở

Nguyên tắc FAIR là trục nối giữa chia sẻ dữ liệu và quản lý giai đoạn kết thúc nghiên cứu: một bộ dữ liệu chỉ có thể được chia sẻ lại và lưu trữ dài hạn khi ngay từ đầu nó đã được mô tả, định danh và cấp phép để cả máy tính lẫn con người đều tìm thấy, truy cập, liên thông và tái sử dụng được.

### 7.1. Bốn trụ cột FAIR và ranh giới với dữ liệu mở

Khung nguyên tắc FAIR do Wilkinson và cộng sự đề xuất năm 2016 gồm bốn trụ cột — Tìm thấy được, Truy cập được, Liên thông được và Tái sử dụng được — triển khai thành 15 nguyên tắc thành phần có thể kiểm tra được bằng máy [12]. Điểm cốt lõi là *machine-actionability*: hệ thống máy tính tự động phát hiện, diễn giải và tái sử dụng dữ liệu cùng siêu dữ liệu của nó mà không cần can thiệp thủ công [12]. FAIR là một tập hợp nguyên tắc hướng dẫn, không phải một tiêu chuẩn hay đặc tả kỹ thuật [12].

Một nhận thức sai lệch phổ biến là đồng nhất FAIR với dữ liệu mở công khai. Thực tế, "FAIR không đồng nghĩa với Mở": dữ liệu bệnh nhân nhạy cảm hoàn toàn có thể đạt chuẩn FAIR nhờ siêu dữ liệu công khai giàu ngữ cảnh, định danh bền vững (DOI/URI) và giao thức truy cập có kiểm soát theo nguyên tắc A1 [12]. Kinh nghiệm từ đại dịch COVID-19 cho thấy tách bạch siêu dữ liệu công khai với dữ liệu lâm sàng được kiểm soát truy cập là điều kiện để vừa đạt FAIR vừa bảo vệ quyền riêng tư [41].

### 7.2. Quy trình FAIRification bảy bước

Jacobsen và cộng sự (2020) chuyển nguyên tắc thành thực hành bằng quy trình FAIRification gồm bảy bước, ba pha [21]: tiền-FAIRification — (1) xác định mục tiêu dựa trên đánh giá mức độ trưởng thành FAIR ban đầu, (2) phân tích cấu trúc dữ liệu, siêu dữ liệu hiện có và yêu cầu bảo vệ riêng tư; FAIRification — (3) định nghĩa mô hình ngữ nghĩa, (4) chuẩn hóa dữ liệu bằng bản thể học và từ vựng chuẩn, (5) làm giàu siêu dữ liệu và gắn định danh bền vững, (6) cấp phép tái sử dụng và lưu ký trên kho tin cậy; hậu-FAIRification — (7) đánh giá lại mức độ trưởng thành FAIR sau triển khai [21]. Quy trình này đã được thích ứng cho dữ liệu sức khỏe, trong đó tách biệt dữ liệu định danh và dữ liệu y khoa là điểm khác biệt chính [42].

Mô hình trưởng thành dữ liệu FAIR của Liên minh Dữ liệu Nghiên cứu (RDA) cung cấp bộ chỉ số đánh giá theo từng nguyên tắc thành phần, đã được vận dụng để đánh giá lược đồ siêu dữ liệu NFDI4Health tại Đức [43]. Ở cấp độ thực hành, *FAIR Cookbook* của Rocca-Serra và cộng sự (2023) tập hợp các "công thức" FAIRification cho khoa học sự sống, phát triển trong dự án FAIRplus [44]; Wilkinson và cộng sự (2019) đề xuất khung đánh giá trưởng thành FAIR tự động, đo được bằng máy và do cộng đồng quản trị [45].

### 7.3. Hệ sinh thái khoa học mở và lựa chọn kho lưu trữ

Khuyến nghị UNESCO về Khoa học Mở (11/2021, 193 quốc gia thành viên) là khung chuẩn quốc tế đầu tiên về khoa học mở [46]. ICMJE yêu cầu mọi bài báo thử nghiệm lâm sàng đính kèm Tuyên bố chia sẻ dữ liệu, công bố rõ phạm vi, thời điểm và điều kiện chia sẻ dữ liệu cá nhân đã khử định danh [47]. Tại Hoa Kỳ, đăng ký thử nghiệm và báo cáo kết quả trên ClinicalTrials.gov là nghĩa vụ pháp lý theo FDAAA 801 (hiệu lực từ 18/01/2017) [48]; tỷ lệ báo cáo đúng hạn trong 12 tháng đã tăng từ 8,3% (2010–2014) lên 23,2% (2017–2021) [49].

Rào cản lớn nhất đối với chia sẻ dữ liệu mang tính thực hành: khảo sát Springer Nature trên hơn 7.000 nhà nghiên cứu cho thấy 46% khó tổ chức dữ liệu ở dạng dễ dùng, 37% lúng túng về bản quyền và giấy phép, 33% không biết chọn kho lưu trữ và 26% thiếu thời gian [50]. NIH ưu tiên kho chuyên ngành trước kho của tổ chức và kho đa ngành [51]. Chính sách NIH yêu cầu Kế hoạch Quản lý và Chia sẻ Dữ liệu (DMSP) không quá hai trang, sáu thành phần, và chia sẻ dữ liệu chậm nhất vào thời điểm công bố hoặc khi kết thúc thời gian tài trợ [7].

Với dữ liệu hệ gen người, mô hình chia sẻ có trách nhiệm là lưu ký có kiểm soát truy cập qua dbGaP/EGA, thay vì mở công khai [52]. Với dữ liệu cá nhân của thử nghiệm lâm sàng, nền tảng Vivli (ra mắt 7/2018) cho phân tích dữ liệu trong môi trường an toàn thay vì tải về tự do [53]. Các kho đa ngành như Zenodo và Figshare cấp DOI vĩnh viễn cho tập dữ liệu và mã nguồn, với chế độ mở, hạn chế hoặc đóng tạm thời [51]. Nguyên tắc chung của các nhà tài trợ châu Âu là "mở ở mức tối đa có thể, đóng ở mức tối thiểu cần thiết", với siêu dữ liệu luôn mở [3].

### 7.4. Quản lý kết thúc nghiên cứu: lưu trữ dài hạn và tiêu hủy an toàn

Giai đoạn đóng nghiên cứu là điểm dễ phát sinh sai phạm nghiêm trọng. Bước chuyển căn bản trong ICH E6(R3) là mở rộng đối tượng lưu trữ từ "tài liệu thiết yếu" sang "hồ sơ thiết yếu", đưa siêu dữ liệu, nhật ký sự kiện và dấu vết kiểm toán vào phạm vi bảo quản bắt buộc, đồng thời đặt quản trị dữ liệu và hệ thống máy tính hóa thành một mục riêng (Annex 1 §4) [4]. Hệ quả là các bản xuất tĩnh dạng PDF hoặc CSV tách rời dữ liệu động khỏi audit trail không còn đáp ứng yêu cầu thanh tra [4].

Về thời hạn, Quy định (EU) số 536/2014, Điều 58, yêu cầu lưu trữ hồ sơ chính của thử nghiệm tối thiểu 25 năm sau khi thử nghiệm kết thúc [54]; mọi thử nghiệm đa quốc gia phải tuân theo quy tắc thời hạn dài nhất áp dụng được. Tại Việt Nam, Thông tư 33/2025/TT-BYT quy định bệnh án tử vong lưu 30 năm, bệnh án tâm thần, tai nạn lao động và tai nạn giao thông lưu 20 năm, và bộ quy trình chuẩn (SOP) thử nghiệm lâm sàng và khoa học công nghệ lưu 20 năm [55].

Hết thời hạn lưu trữ hoặc hoàn tất mục đích xử lý, dữ liệu nhạy cảm phải được tiêu hủy an toàn theo NIST SP 800-88 Revision 2 (26/9/2025, thay thế Rev. 1 năm 2014) [56]. Bản Rev. 2 phân định ba phương pháp làm sạch theo mức nỗ lực phục hồi của kẻ tấn công: Clear chống phục hồi thông thường; Purge ngăn chặn khôi phục ngay cả với thiết bị phòng thí nghiệm hiện đại nhưng vẫn giữ phương tiện tái sử dụng; Destroy là hủy hoại vật lý thiết bị [56]. Trong môi trường đám mây và ổ SSD/NVMe, xóa mật mã (Cryptographic Erase) bằng cách tiêu hủy toàn bộ khóa mã hóa thường là lựa chọn Purge khả thi duy nhất, với điều kiện mã hóa từ đầu và hủy hết bản sao lưu khóa [56]. Quy trình tiêu hủy chỉ hợp lệ khi hoàn tất Verification và Validation và lưu trữ Chứng chỉ tiêu hủy dữ liệu [56].

## §8. Bảo mật và pháp lý đa tầng

Bảo mật dữ liệu y sinh vận hành theo nhiều tầng bổ trợ nhau: luật bảo vệ dữ liệu cá nhân, luật y tế về bí mật bệnh án và các mô hình toán học định lượng rủi ro tái định danh. Mục này đối chiếu ba hệ thống — EU, Hoa Kỳ và Việt Nam — rồi trình bày các mô hình toán học nền tảng.

### 8.1. GDPR và Không gian Dữ liệu Y tế châu Âu (EHDS)

Quy định (EU) 2016/679 (GDPR) đặt dữ liệu sức khỏe vào nhóm dữ liệu cá nhân đặc biệt: Điều 9(1) cấm xử lý về nguyên tắc, trừ khi có căn cứ ngoại lệ như đồng ý tường minh (Điều 9(2)(a)) hoặc nghiên cứu khoa học kèm biện pháp bảo vệ phù hợp (Điều 9(2)(j) kết hợp Điều 89) [57]. Giả danh hóa (Điều 4(5)) là xử lý dữ liệu sao cho không còn gắn được với một chủ thể cụ thể nếu không có thông tin bổ sung lưu giữ riêng biệt. Dữ liệu giả danh vẫn là dữ liệu cá nhân: theo Recital 26, chỉ dữ liệu ẩn danh không thể đảo ngược bằng mọi phương tiện hợp lý mới thoát khỏi phạm vi điều chỉnh của GDPR; Điều 89(1) ưu tiên ẩn danh hóa khi mục đích nghiên cứu vẫn đạt được.

Quy định (EU) 2025/327 (EHDS) là tầng pháp lý thứ hai của EU, điều chỉnh sử dụng sơ cấp và tái sử dụng thứ cấp dữ liệu sức khỏe điện tử [58]. EHDS có hiệu lực 26/03/2025, áp dụng chung từ 26/03/2027, triển khai theo hai pha tới năm 2029 và 2031. Đối với nghiên cứu, EHDS chuyển từ ẩn danh hóa tĩnh sang cấp phép tái sử dụng: xin giấy phép từ cơ quan quản lý quyền truy cập dữ liệu y tế (HDAB), xử lý dữ liệu trong môi trường an toàn, chủ thể dữ liệu có quyền từ chối (opt-out); việc tái sử dụng vẫn phải tuân thủ GDPR [59].

### 8.2. HIPAA và sự bất tương xứng xuyên Đại Tây Dương

Quy tắc Quyền riêng tư HIPAA (45 CFR §164.514) quy định hai phương pháp khử định danh dữ liệu sức khỏe được bảo vệ (PHI) [60]. Safe Harbor yêu cầu loại bỏ 18 loại định danh — họ tên, địa lý nhỏ hơn bang, ngày tháng (trừ năm), tuổi trên 89, các số định danh cá nhân, định danh thiết bị, URL, địa chỉ IP, sinh trắc học, ảnh toàn mặt — và không có căn cứ để tin rằng phần dữ liệu còn lại vẫn định danh được cá nhân. Expert Determination yêu cầu chuyên gia đủ năng lực xác định rủi ro tái định danh là "rất nhỏ". Tập dữ liệu giới hạn (Limited Data Set) giữ lại ngày tháng và mã ZIP nhưng vẫn là PHI, chỉ được chia sẻ theo thỏa thuận sử dụng dữ liệu (DUA).

Nút thắt trong hợp tác đa quốc gia là sự bất tương xứng giữa chuẩn HIPAA và chuẩn GDPR: dữ liệu đã loại bỏ 18 định danh theo chuẩn HIPAA Safe Harbor — chẳng hạn ảnh cộng hưởng từ não đã xóa mặt hay hồ sơ giữ mã giả danh — vẫn là dữ liệu giả danh tại châu Âu, tức vẫn thuộc phạm vi điều chỉnh đầy đủ của GDPR [61]. Năng lực tái định danh của học máy làm lung lay giả định về "ẩn danh tuyệt đối", củng cố nhận định của Paul Ohm rằng dữ liệu có thể hữu ích hoặc ẩn danh hoàn hảo, nhưng không bao giờ đạt cả hai [59]. Khoảng trống này thúc đẩy cả EHDS lẫn pháp luật Việt Nam chuyển sang mô hình bảo vệ đa tầng [59].

### 8.3. Bước ngoặt pháp luật Việt Nam 2025–2026

Việt Nam đã hình thành hành lang pháp lý cấp Luật về dữ liệu trong giai đoạn 2025–2026. Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 (thông qua 26/6/2025, hiệu lực 01/01/2026) gồm 5 chương và 39 điều; dữ liệu về tình trạng sức khỏe thuộc nhóm dữ liệu cá nhân nhạy cảm, được bảo vệ ở cấp cao nhất [62]. Nghị định 356/2025/NĐ-CP hướng dẫn Luật này (ban hành 31/12/2025, hiệu lực 01/01/2026), đồng thời quy định Nghị định 13/2023/NĐ-CP hết hiệu lực từ ngày 01/01/2026 [63]. Như vậy, Nghị định 13/2023 chỉ điều chỉnh giai đoạn 01/7/2023–31/12/2025; trích dẫn Nghị định 13/2023 như văn bản đang có hiệu lực sau thời điểm này đều đã lỗi thời. Luật Dữ liệu số 60/2024/QH15 (hiệu lực từ 01/7/2025) đặt nền tảng cho quản trị dữ liệu quốc gia [64].

Luật 91/2025/QH15 yêu cầu đồng thuận tự nguyện cho từng mục đích xử lý cụ thể — sự im lặng không được coi là đồng ý — và quy định các trường hợp không cần đồng thuận như khẩn cấp, dịch bệnh nguy hiểm hoặc nghĩa vụ pháp lý [62]. Đối với nghiên cứu y sinh, luật yêu cầu lập Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân và Hồ sơ đánh giá tác động chuyển dữ liệu xuyên biên giới (khi chuyển dữ liệu ra ngoài biên giới) gửi Bộ Công an (Cục A05) [62]. Nghị định 356/2025/NĐ-CP bổ sung nghĩa vụ cho hệ thống trí tuệ nhân tạo: thông báo xử lý tự động, giải thích nguyên tắc thuật toán, bảo vệ dữ liệu suy luận từ AI có thể giúp định danh cá nhân, giám sát hai chiều và đánh giá tuân thủ định kỳ [63].

Ở tầng chuyên ngành, Thông tư 13/2025/TT-BYT hướng dẫn triển khai hồ sơ bệnh án điện tử (ban hành 06/06/2025, hiệu lực 21/07/2025), thay thế Thông tư 46/2018/TT-BYT [65]. Lộ trình cần trích chính xác: các bệnh viện chậm nhất ngày 30/09/2025, các cơ sở khác chậm nhất ngày 31/12/2026 — không viết gộp thành một hạn chung 31/12/2026 cho mọi bệnh viện [65]. Thông tư 50/2025/TT-BYT về thử thuốc trên lâm sàng (ban hành 31/12/2025, hiệu lực 27/02/2026) thay thế Thông tư 29/2018/TT-BYT [66].

### 8.4. Các mô hình toán học bảo vệ quyền riêng tư

Ẩn danh hóa dữ liệu dạng bảng phân chia ba loại biến: định danh trực tiếp (họ tên, số căn cước, mã bệnh án); bán định danh (tuổi, giới tính, địa chỉ cư trú, mốc thời gian khám); và thuộc tính nhạy cảm (chẩn đoán bệnh lý) [67]. Rủi ro nằm ở khả năng liên kết các biến bán định danh với nguồn dữ liệu bên ngoài: Sweeney (2000) chỉ ra 87% dân số Hoa Kỳ có thể bị định danh duy nhất chỉ từ ngày sinh, giới tính và mã ZIP 5 chữ số [67].

Mô hình k-anonymity (Sweeney, 2002) áp dụng tổng quát hóa và ẩn bớt để mỗi bản ghi không thể phân biệt với ít nhất k − 1 bản ghi khác trên tập biến bán định danh [68]. Giới hạn của nó là bất lực trước tấn công đồng nhất (mọi bệnh nhân trong cùng một nhóm đều mang cùng một chẩn đoán) và tấn công tri thức nền, đồng thời suy giảm tính hữu ích trên dữ liệu nhiều chiều [67]. Mô hình l-diversity (Machanavajjhala và cộng sự, 2007) yêu cầu mỗi lớp tương đương chứa ít nhất l giá trị thuộc tính nhạy cảm "đại diện tốt" nhằm chống tấn công đồng nhất [69]. Tuy nhiên l-diversity vẫn dễ bị khai thác qua tấn công lệch phân bố và tấn công tương đồng ngữ nghĩa [67]. Mô hình t-closeness ràng buộc khoảng cách phân bố của thuộc tính nhạy cảm trong mỗi nhóm so với phân bố toàn tập không vượt quá ngưỡng t [67].

Quyền riêng tư vi phân (Differential Privacy, DP) bảo vệ cơ chế truy vấn thay vì ẩn danh hóa tập dữ liệu: một cơ chế thỏa mãn DP khi thêm hay bớt một bản ghi cá nhân bất kỳ hầu như không làm thay đổi phân bố kết quả đầu ra, nhờ hiệu chuẩn nhiễu ngẫu nhiên theo độ nhạy truy vấn [70]. Sadilek và cộng sự (2021) chèn lớp DP trung tâm (ε = 0,165, δ = 10⁻⁵) vào mô hình học liên kết dự báo sống còn suy tim (n = 299) chỉ hạ nhẹ AUC từ 0,85 xuống 0,83 — vẫn cao hơn mức 0,82 của mô hình đơn cơ sở [71]. Dù vậy, trên quần thể bệnh hiếm hoặc cỡ mẫu nhỏ, độ nhạy truy vấn lớn buộc tăng nhiễu và gây suy giảm độ chính xác thống kê; DP thường được phối hợp với kiểm soát môi trường phân tích an toàn [70]. Thông điệp chung: không tồn tại mức ẩn danh "đủ tốt" cho mọi mục đích; ngưỡng bảo vệ phải được lựa chọn theo độ nhạy dữ liệu, cỡ mẫu và mô hình đe dọa từng nghiên cứu.

---

**Thuộc bản tổng hợp:** *Quản lý dữ liệu trong nghiên cứu y sinh: Yêu cầu từ thiết kế đề cương đến kết thúc nghiên cứu* (tổng quan tài liệu giai đoạn 2015–2026).
**Phạm vi phần này:** §9. Dữ liệu sẵn sàng cho AI và §10. Bối cảnh Việt Nam. Số trích dẫn [n] là số trong danh mục Tài liệu tham khảo cuối bản tổng hợp này; chỉ trích dẫn các mục đã kiểm chứng đầy đủ.

---

## 9. Dữ liệu sẵn sàng cho AI

Nghịch lý trung tâm của AI y tế là dữ liệu bệnh viện — dù đồ sộ — phần lớn chưa đủ chuẩn để huấn luyện mô hình đáng tin cậy, do khuyết dữ liệu, mã hóa thiếu nhất quán và thiên lệch quần thể. Nguyên tắc FAIR là điều kiện cần nhưng chưa đủ [12]. Vì vậy các chương trình lớn chuyển sang chuẩn “dữ liệu sẵn sàng cho AI”, trong đó chất lượng, nguồn gốc, tính giải trình và quản trị được kiểm chứng ngay từ khâu thiết kế.

### 9.1. Bảy tiêu chí AI-ready của Bridge2AI và kiểm soát thiên lệch

Sáng kiến Bridge2AI của NIH đề xuất bộ bảy tiêu chí nền tảng cho dữ liệu y sinh sẵn sàng cho AI [72]. **Lưu ý:** đây mới là bản preprint trên bioRxiv (v6, 24/4/2026), chưa qua bình duyệt trên tạp chí chính thức, vì vậy cần trích dẫn đúng tư cách preprint [72]. Bảy tiêu chí gồm: (1) **Tính FAIR** — tìm thấy, truy cập, liên thông, tái sử dụng [72][12]; (2) **Nguồn gốc sâu** — lần ngược tới phiên bản gốc [72]; (3) **Đặc trưng hóa sâu** — mô tả ngữ nghĩa, phân bố và thiên lệch đã biết [72]; (4) **Giải trình tiền mô hình** — bằng chứng đủ rõ để giải thích đầu ra thuật toán [72]; (5) **Đạo đức, pháp lý và quản trị** — đồng thuận phù hợp, DUA dạng máy đọc được, giám sát bởi con người [72]; (6) **Tính bền vững** — lưu trữ dài hạn trên kho tin cậy [72]; (7) **Tính khả toán** — đóng gói theo lược đồ chuẩn hóa [72].

Hai điểm có ý nghĩa thực hành trực tiếp. Thứ nhất, Bridge2AI khuyến nghị không dùng giấy phép CC0 cho dữ liệu y sinh, vì CC0 làm mất nguồn gốc và khả năng cưỡng chế tuân thủ pháp lý ở khâu hạ nguồn [72]. Thứ hai, năm chiều chất lượng của Weiskopf và Weng — đầy đủ, đúng đắn, đồng nhất, hợp lý, thời sự — là khung đo lường để một tập dữ liệu EHR được coi là đủ điều kiện tái sử dụng cho nghiên cứu và AI [28].

Kiểm soát thiên lệch là lớp yêu cầu bổ trợ cho Bridge2AI. Khuyến nghị đồng thuận STANDING Together (Alderman và cộng sự, *The Lancet Digital Health* 2025) thiết lập chuẩn minh bạch nhân khẩu học nhằm chống thiên lệch thuật toán và khắc phục “nghèo dữ liệu sức khỏe” [73]. Trong thực hành, yêu cầu này được chuẩn hóa qua Datasheets for Datasets (Gebru và cộng sự, 2021) [74] kết hợp với Model Cards báo cáo chỉ số phân biệt, độ hiệu chuẩn và giá trị dự báo tại đúng ngưỡng lâm sàng [73].

### 9.2. Kiến trúc tham chiếu: Biomedical Data Lakehouse

Kho dữ liệu quan hệ truyền thống không tích hợp mượt mà được dữ liệu đa phương thức, trong khi hồ dữ liệu thuần túy lại thiếu kỷ luật quản trị và toàn vẹn giao dịch. Mô hình Biomedical Data Lakehouse được đề xuất trong bản tổng hợp này như một kiến trúc hợp nhất, hỗ trợ song song SQL cho báo cáo và Python cho học sâu. **Cần ghi rõ:** đây là kiến trúc đề xuất của bản tổng hợp, chưa phải khung chuẩn đã kiểm chứng trong y văn; các thành phần — FHIR, OMOP CDM và hướng dẫn ánh xạ FHIR-to-OMOP — thì đã được kiểm chứng độc lập [9][10][11].

Nguyên lý thiết kế sống còn là tách biệt tuyệt đối tầng giao dịch lâm sàng với tầng phân tích AI. Dữ liệu từ hệ thống vận hành (HIS/LIS/PACS) được đưa qua đường ống ETL và khử định danh vào OMOP CDM, theo ánh xạ lõi của Hướng dẫn FHIR-to-OMOP (v1.0.0, dựa trên FHIR v5.0.0, ánh xạ sang OMOP CDM v5.4) [10][9]. Chuẩn hóa về OMOP CDM mở đường tham gia mạng lưới OHDSI (4.833 cộng tác viên, 88 quốc gia; 544 nguồn dữ liệu, 54 quốc gia; 974 triệu hồ sơ, theo *Our Journey 2025*) [11]. Feature Store chuẩn hóa biến đầu vào dùng chung và Model Registry lưu giữ phiên bản và hiệu năng kiểm định.

Lớp kiểm soát truy cập phân biệt kiến trúc này với một kho dữ liệu thông thường. Các mô hình AI không truy cập trực tiếp hệ thống nguồn mà chỉ đi qua lớp công cụ hẹp (narrow tools layer) áp đặt phân quyền, che trường nhạy cảm, neo tri thức bằng RAG và lưu vết truy vấn. Đối với dữ liệu nhạy cảm, mô hình “đưa thuật toán tới dữ liệu” được vận hành qua Môi trường Nghiên cứu Tin cậy (TRE) theo khung Five Safes [75]. Các hệ thống AI này vẫn chịu Mục 4 của ICH E6(R3) [4].

### 9.3. Quản trị dữ liệu và AI tại bệnh viện đại học

Hạ tầng kỹ thuật chỉ phát huy giá trị khi gắn liền với thiết chế quản trị đủ thẩm quyền. Kinh nghiệm quốc tế cho thấy cấu trúc hiệu quả nhất đặt quản trị dữ liệu và AI vào trục vận hành chính thức của bệnh viện đại học. Tại Đức, Sáng kiến Tin học Y tế đã thành lập các Trung tâm Tích hợp Dữ liệu (DICs) tại các bệnh viện đại học, chuẩn hóa dữ liệu chăm sóc thường quy theo bộ dữ liệu lõi dựa trên chuẩn HL7 FHIR [76]. Mô hình của Đại học Vanderbilt — kho bản sao khử định danh liên kết với ngân hàng mẫu sinh học [77] — và hệ sinh thái dữ liệu STARR của Stanford Medicine [78] là hai hình mẫu thường được đối chiếu.

Mỗi bệnh viện đại học cần thành lập Hội đồng Quản trị Dữ liệu và AI đa chuyên khoa — gồm lãnh đạo bệnh viện, giám đốc thông tin y tế, hội đồng đạo đức, công nghệ thông tin, pháp chế, Data Steward và đại diện người bệnh — để vận hành năm quy trình cốt lõi: kiểm soát truy cập, giám sát chất lượng dữ liệu và trôi dạt mô hình, quản trị siêu dữ liệu, thẩm định triển khai và phê duyệt chia sẻ dữ liệu, đi kèm thẩm quyền dừng khẩn cấp hệ thống AI gây rủi ro an toàn người bệnh.

Trụ cột nhân lực của toàn bộ thiết chế này là Data Steward, được tổ chức thành ba hồ sơ bổ trợ lẫn nhau: chính sách và tuân thủ (quy chế dữ liệu cấp viện, tuân thủ đạo đức và pháp luật, thỏa thuận sử dụng dữ liệu); chuyên môn nghiên cứu (kế hoạch quản lý dữ liệu, từ điển biến chuẩn hóa, khử định danh, biên mục siêu dữ liệu); và hạ tầng và kỹ thuật (đặc tả nền tảng thu thập dữ liệu điện tử, đường ống ETL sang FHIR/OMOP, kho lưu trữ dài hạn). Theo Jetten và cộng sự (2021) và *The Turing Way*, năng lực Data Steward là năng lực liên ngành, cần được công nhận bằng chức danh, khung năng lực và đào tạo chính quy [17][18].

---

## 10. Bối cảnh Việt Nam

### 10.1. Thể chế, pháp luật và chuyển đổi số y tế đến cuối năm 2026

Giai đoạn 2024–2026 đánh dấu bước chuyển thể chế mạnh mẽ cho dữ liệu y sinh tại Việt Nam. Nghị quyết 57-NQ/TW (22/12/2024) đặt mục tiêu đến năm 2030 đưa Việt Nam vào nhóm ba nước dẫn đầu Đông Nam Á về AI, dành ít nhất 3% tổng chi ngân sách hằng năm cho khoa học công nghệ và chuyển đổi số [79]. Nghị quyết 72-NQ/TW (09/09/2025) quy định từ năm 2026 người dân thuộc nhóm ưu tiên được khám sức khỏe định kỳ hoặc sàng lọc miễn phí tối thiểu mỗi năm một lần, các đối tượng còn lại được hưởng chính sách này từ năm 2028 (không phải “từ năm 2026 cho mọi người dân”), đồng thời lập sổ sức khỏe điện tử theo vòng đời [80]. Quyết định 1308/QĐ-TTg (18/7/2026) phê duyệt Chiến lược Dữ liệu Quốc gia 2026–2030, tầm nhìn đến năm 2045 [81].

Khung pháp lý cho dữ liệu y tế cũng được hoàn thiện ở cấp luật. Luật Dữ liệu 60/2024/QH15 (thông qua 30/11/2024, hiệu lực 01/7/2025) [64]. Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 (thông qua 26/6/2025, hiệu lực 01/01/2026) [62]. Nghị định 356/2025/NĐ-CP (ban hành 31/12/2025, hiệu lực 01/01/2026) hướng dẫn thi hành Luật này và quy định Nghị định 13/2023/NĐ-CP hết hiệu lực từ ngày 01/01/2026 [63]. Mọi đề tài y sinh dùng dữ liệu người bệnh từ đầu năm 2026 vì vậy phải thực thi cặp văn bản này [62][63].

Về hồ sơ bệnh án điện tử, Thông tư 13/2025/TT-BYT (ban hành 06/6/2025, hiệu lực 21/7/2025) thay thế Thông tư 46/2018/TT-BYT và ấn định lộ trình bắt buộc: bệnh viện triển khai chậm nhất ngày 30/9/2025, các cơ sở khám bệnh, chữa bệnh khác hoàn thành chậm nhất ngày 31/12/2026 [65]. Quyết định 3218/QĐ-BYT (14/10/2026) quy định vận hành Cổng dữ liệu sức khỏe của Bộ Y tế [82]. Tiến độ công bố triển khai EMR không đồng nghĩa với dữ liệu sẵn sàng cho nghiên cứu; các con số về EMR và thị trường y tế số chưa kiểm chứng đầy đủ nên không được nêu.

Tổng quan phạm vi của Tran và cộng sự về chính sách sức khỏe số cho chăm sóc bệnh viện tại Việt Nam (*Journal of Medical Internet Research* 24(2), e32392, 2022) [83]. **Cần hiệu đính dứt khoát:** công trình này là Tran và cộng sự 2022, *Journal of Medical Internet Research* 24(2), e32392, DOI 10.2196/32392, không phải 2025 và không phải *JMIR Formative Research* 9:e53483; mã e53483 thuộc về một bài báo khác [84]. Khảo sát của Trịnh Văn Vinh (2025) trên 125 cán bộ y tế và 10 quản lý tại các bệnh viện công ở Thành phố Hồ Chí Minh (tháng 3–4/2025) cũng ghi nhận thiếu đồng bộ hạ tầng và hạn chế liên thông [85].

### 10.2. Sáu khoảng trống mang tính hệ thống

**Thứ nhất, khoảng cách giữa công bố triển khai EMR và dữ liệu chuẩn hóa.** Bộ Y tế đã ghi nhận chất lượng dữ liệu tại một số cơ sở chưa đủ điều kiện thay thế hoàn toàn bệnh án giấy; khảo sát của Trịnh Văn Vinh (2025) xác nhận phân mảnh hệ thống và thiếu liên thông giữa các bệnh viện công [85]. Bộ chuẩn XML thanh toán bảo hiểm y tế thiếu ngữ nghĩa lâm sàng sâu.

**Thứ hai, suy giảm thử nghiệm lâm sàng và thiếu chuẩn CDISC/DMP bắt buộc.** Báo cáo tháng 5/2025 của Pharma Group, KPMG và OUCRU ghi nhận số thử nghiệm lâm sàng khởi sự mới giai đoạn 2018–2023 ở mức dưới 40 thử nghiệm mỗi năm [86]. Các quỹ khoa học trong nước và hội đồng đạo đức hiện chưa bắt buộc nộp DMP và chưa phổ cập bộ tiêu chuẩn CDISC.

**Thứ ba, thiếu hụt nhân lực Data Steward chuyên trách.** Quản trị dữ liệu nghiên cứu tại hầu hết bệnh viện đại học vẫn mang tính kiêm nhiệm giữa bác sĩ lâm sàng — thiếu chuyên môn kỹ thuật dữ liệu — và phòng công nghệ thông tin — tập trung vận hành hệ thống thông tin bệnh viện. Chưa có khung năng lực, chức danh nghề nghiệp hay chương trình đào tạo chính quy cho Data Steward; đây là nút thắt lớn nhất khiến nguyên tắc FAIR chậm đi vào thực tiễn [17][18].

**Thứ tư, thiếu kho dữ liệu quốc gia và môi trường phân tích tin cậy.** Việt Nam chưa có hạ tầng TRE cấp quốc gia hay môi trường nghiên cứu tin cậy theo khung Five Safes cho truy cập thứ cấp vào dữ liệu người bệnh [75]. Quyết định 3218/QĐ-BYT về Cổng dữ liệu sức khỏe (2026) là bước đi về mặt thể chế [82], nhưng cổng dữ liệu hành chính khác với kho dữ liệu nghiên cứu chuẩn hóa OMOP CDM và quy trình xét duyệt truy cập độc lập [11][10].

**Thứ năm, thiếu chính sách khoa học mở và động lực chia sẻ dữ liệu.** Chưa có khung pháp lý và học thuật đồng bộ khuyến khích chia sẻ dữ liệu có kiểm soát — mẫu DUA chuẩn liên viện, cơ chế bảo lưu quyền ưu tiên công bố — khiến tình trạng “cát cứ dữ liệu” giữa các khoa phòng và bệnh viện kéo dài [12]. Khoảng trống nằm ở động lực, công sức biên mục và chi phí lưu trữ, chứ không phải sự vắng mặt của chính sách.

**Thứ sáu, áp lực tuân thủ khung pháp lý dữ liệu cá nhân và AI mới.** Từ ngày 01/01/2026, mọi đề tài y sinh sử dụng dữ liệu người bệnh và phát triển AI phải tuân thủ Luật 91/2025/QH15 và Nghị định 356/2025/NĐ-CP [62][63]. Các quy trình đồng thuận, khử nhận dạng và đánh giá tác động phải được xây dựng song song với việc hoàn thiện bệnh án điện tử theo Thông tư 13/2025/TT-BYT [65]. Nguy cơ lớn nhất không phải là vi phạm cố ý mà là không tuân thủ do thiếu quy trình.

Một điểm cần khẳng định dứt khoát: **không có bằng chứng công bố nào về việc áp dụng CDISC, OMOP CDM hay HL7 FHIR tại các bệnh viện Việt Nam**. Không có nguồn bình duyệt hay văn bản chính thức nào mô tả việc triển khai các chuẩn này tại Việt Nam [83].

### 10.3. Lộ trình chiến lược đề xuất cho bệnh viện đại học Việt Nam, 2026–2035

Lộ trình bốn giai đoạn dưới đây mang tính khuyến nghị cho khối bệnh viện đại học nòng cốt giai đoạn 2026–2035; các chỉ tiêu trong bảng là mục tiêu khuyến nghị.

| Giai đoạn | Mục tiêu chiến lược | Quản trị, pháp lý và nhân lực | Hạ tầng và chuẩn dữ liệu |
|---|---|---|---|
| **Giai đoạn 1: Nền móng và tuân thủ (2026–2027)** | Hoàn tất bỏ bệnh án giấy; tuân thủ Luật 91/2025 [62][65] | Thành lập Hội đồng Quản trị Dữ liệu và AI; tuyển nhóm Data Steward đầu tiên; tích hợp DMP bắt buộc vào quy trình đạo đức [7][17] | Hoàn tất EMR đạt chuẩn Thông tư 13/2025 (bệnh viện 30/9/2025, cơ sở khác 31/12/2026) [65]; thu thập dữ liệu điện tử chuẩn |
| **Giai đoạn 2: Liên thông và chuẩn hóa (2027–2029)** | Phá vỡ phân mảnh hệ thống; vận hành Trung tâm Tích hợp Dữ liệu (DIC) [76] | Chính thức hóa DIC; mẫu đồng thuận rộng và DUA liên viện; đào tạo chuẩn CDISC/OMOP [18] | Tầng tích hợp HL7 FHIR R4; thí điểm ETL chuyển dữ liệu nhóm bệnh trọng điểm sang OMOP CDM v5.4 [10][9] |
| **Giai đoạn 3: Lakehouse, TRE và AI lâm sàng (2029–2032)** | Nền tảng AI-ready đa phương thức và phân tích bảo mật | Thẩm định quản trị AI theo Nghị định 356/2025 [63] | Triển khai Biomedical Data Lakehouse có Feature Store và Model Registry; dựng Môi trường Nghiên cứu Tin cậy (TRE) theo khung Five Safes [75] |
| **Giai đoạn 4: Mạng lưới quốc gia và hệ thống y tế học tập (2032–2035)** | Liên kết mạng lưới quốc tế và hệ thống y tế học tập | Hình thành Mạng lưới Dữ liệu Y sinh Quốc gia; công nhận đóng góp dữ liệu FAIR [11][12] | Mở rộng học liên kết và học bầy đàn (Swarm Learning) đa bệnh viện [87]; khép kín vòng phản hồi tri thức trở lại thực hành lâm sàng [88] |

Thứ tự ưu tiên phải được giữ đúng: tuân thủ và nhân lực trước, chuẩn hóa và liên thông sau, rồi mới đến AI lâm sàng và mạng lưới. Đảo ngược thứ tự sẽ lặp lại đúng nghịch lý đã nêu ở §9: dữ liệu nhiều nhưng không dùng được, mô hình chạy được nhưng không kiểm chứng được. Đích đến là một hệ thống y tế học tập [88]. Đối với Việt Nam, cửa sổ cơ hội nằm trong giai đoạn 2026–2029 [64][62][63][65].

---

**Thuộc bản tổng hợp:** *Quản lý dữ liệu trong nghiên cứu y sinh: Yêu cầu từ thiết kế đề cương đến kết thúc nghiên cứu* (bản tổng hợp literature review, 20/11/2026).
**Phạm vi phần này:** §11. Hướng tương lai; §12. Kết luận và khuyến nghị thực hành cho bệnh viện đại học Việt Nam; Phụ lục A (bảng landmark); Phụ lục B (bản nháp danh mục thay đổi so với bản Google Docs).
---

## 11. Hướng tương lai

Các mục trước mô tả RDM như kỷ luật của tuân thủ và liên thông. Hướng phát triển giai đoạn 2025–2030 đảo ngược một phần logic đó: thay vì di chuyển dữ liệu tới nhà nghiên cứu, các kiến trúc mới đưa thuật toán tới dữ liệu, giữ dữ liệu thô tại chỗ và chỉ cho tri thức đã tổng hợp rời khỏi kho [89]. Ba hướng hội tụ: học phân tán bảo tồn quyền riêng tư, dữ liệu tổng hợp, và môi trường nghiên cứu tin cậy trong một hệ thống y tế học tập. Cả ba đều đòi hỏi cao hơn ở các nền tảng đã trình bày — FHIR, CDISC, OMOP CDM và FAIR [12].

### 11.1. Học liên kết (Federated Learning) và Học bầy đàn (Swarm Learning)

Học liên kết (Federated Learning — FL) cho phép nhiều bệnh viện cùng huấn luyện một mô hình AI mà dữ liệu bệnh nhân thô không rời khỏi hạ tầng cục bộ: mỗi viện huấn luyện cục bộ và chỉ gửi lại bản cập nhật tham số [89]. Bằng chứng lớn nhất là dự án EXAM (Dayan và cộng sự, 2021): 20 cơ sở, 16.148 ca COVID-19 có triệu chứng, dự báo nhu cầu oxy trong 24 và 72 giờ với AUC trung bình trên 0,92 — tăng trung bình 16% AUC và 38% khả năng tổng quát hóa so với mô hình đơn cơ sở [89]. Ở bệnh hiếm, dự án FeTS (Pati và cộng sự, 2022) kết nối 71 trung tâm trên 6 châu lục với 6.314 bệnh nhân u nguyên bào thần kinh đệm [90]. MELLODDY (Heyndrickx và cộng sự, 2024) mở rộng FL sang 10 công ty dược [91].

Học bầy đàn (Swarm Learning — SL, Warnat-Herresthal và cộng sự, 2021) bỏ hẳn máy chủ trung tâm, dùng mạng ngang hàng qua chuỗi khối có cấp phép, và vượt trội mô hình đơn viện trên hơn 16.400 mẫu máu và hơn 95.000 ảnh X-quang ngực [87]. Tuy nhiên, FL không tự động bảo đảm quyền riêng tư: chia sẻ gradient vẫn tiềm ẩn nguy cơ tấn công suy ngược, nên cần thêm quyền riêng tư vi phân, mã hóa đồng cấu hoặc tính toán đa bên an toàn [92], như nghiên cứu của Sadilek và cộng sự (2021) [71]. Thách thức lớn nhất là tính dị biệt phi-IID giữa các bệnh viện; các biến thể FL cá thể hóa (FedProx, FedBN) được đề xuất nhưng chưa có đồng thuận về thuật toán tối ưu [92]. FL vì vậy đã chứng minh tính khả thi ở quy mô mạng lưới, chưa phải giải pháp đại trà khi bệnh viện chưa có dữ liệu chuẩn hóa và khung quản trị tương ứng.

### 11.2. Dữ liệu tổng hợp (Synthetic Data): tiềm năng và giới hạn trung thực lâm sàng

Dữ liệu tổng hợp mô phỏng cấu trúc và phân bố thống kê của hồ sơ bệnh án mà không ánh xạ tới cá nhân thật nào, hữu ích cho phát triển mã phân tích, kiểm thử API FHIR và đào tạo nhân lực y tế số [93]. Công cụ mã nguồn mở Synthea (Walonoski và cộng sự, 2018) tạo hồ sơ bệnh nhân dọc theo thời gian ở định dạng FHIR, C-CDA và CSV từ hướng dẫn lâm sàng và thống kê dịch tễ công khai [93].

Tuy vậy, độ trung thực lâm sàng của dữ liệu tổng hợp không đồng đều và phải được đo lường thay vì giả định. Poster đánh giá độc lập tại Hội nghị toàn cầu OHDSI 2024 đối chiếu Synthea với dữ liệu thực tế bang California báo cáo: tương đồng cao ở bệnh mạch vành (SMD 3,59%), trung bình ở tăng huyết áp (SMD 8,9%), nhưng sai lệch rất mạnh ở tỉ lệ nhập viện năm 2020 (SMD 33,64%), nên giá trị dự báo kết cục lâm sàng còn hạn chế [94]. Các mô hình sinh sâu, chẳng hạn LLMSYN (Hao và cộng sự, 2024) [95], cải thiện độ tương đồng phân bố; một tổng quan có bình duyệt (Chen và cộng sự, 2025) cũng ghi nhận nguy cơ suy luận thuộc tính và giới hạn độ tin cậy khoa học [96]. Dữ liệu tổng hợp cũng không tự động mang tính riêng tư — bộ sinh có thể ghi nhớ và rò rỉ bản ghi huấn luyện. Vì vậy, dữ liệu tổng hợp là công cụ hỗ trợ kỹ thuật và kiểm thử bước đầu, không thay thế thẩm định trên dữ liệu lâm sàng thực.

### 11.3. Môi trường Nghiên cứu Tin cậy (TRE) và khung Five Safes

Thay cho mô hình cũ sao chép và gửi tệp dữ liệu khử định danh cho từng nhà nghiên cứu, tiêu chuẩn quốc tế hiện nay hội tụ vào Môi trường Nghiên cứu Tin cậy (TRE/SDE), vận hành theo nguyên lý "dữ liệu không rời khỏi kho", dựa trên khung Five Safes — Safe People, Safe Projects, Safe Settings, Safe Data và Safe Outputs — tức thẩm tra nhà nghiên cứu, thẩm định đề cương, tính toán cô lập, tối thiểu hóa dữ liệu và kiểm soát tiết lộ thống kê đối với mọi kết quả xuất ra [75].

Goldacre Review (Goldacre và Morley, 2022) kiến nghị một số ít TRE dùng chung trở thành chuẩn mặc định cho mọi phân tích hồ sơ NHS khi có rủi ro quyền riêng tư, và Chính phủ Anh đã tiếp nhận định hướng này trong chiến lược *Data Saves Lives* (6/2022) [97]. Minh chứng vận hành là OpenSAFELY: phân tích 17.278.392 hồ sơ người trưởng thành liên kết với 10.926 ca tử vong do COVID-19 chỉ trong vài tuần, mà nhà nghiên cứu không bao giờ tiếp cận bảng dữ liệu thô; mọi mã phân tích đều công khai bắt buộc [98]. Không gian Dữ liệu Y tế Châu Âu (EHDS, Quy định (EU) 2025/327) có hiệu lực ngày 26/3/2025, áp dụng chung từ 26/3/2027 [58]. TRE vì vậy không phải một sản phẩm phần mềm mua sẵn, mà là một mô hình quản trị.

### 11.4. Hệ thống Y tế Học tập và hạ tầng dữ liệu quốc gia

Đích đến cao nhất là Hệ thống Y tế Học tập (LHS), nơi tương tác lâm sàng thường quy tạo sinh tri thức cải tiến điều trị theo vòng lặp P2D → D2K → K2P [99]. Friedman và cộng sự (2015) đặt nền móng cho khái niệm này [99]; Friedman và cộng sự (2024) khẳng định LHS là hạ tầng kỹ thuật–xã hội kết nối bốn trụ cột Con người, Công nghệ, Quy trình và Chính sách [88]. LHS vì vậy là đích đến, không phải điểm khởi đầu, của quản lý dữ liệu y sinh.

Ở tầng hạ tầng quốc gia, hai mô hình châu Á được nêu làm ví dụ tham chiếu (số liệu quy mô chi tiết chưa kiểm chứng đầy đủ): TRUST của Singapore, vận hành từ tháng 11/2022, áp dụng Five Safes và chuẩn hóa OMOP CDM [100] — các con số hơn 500 nhà nghiên cứu, 92 dự án, 48 bộ dữ liệu còn [CẦN KIỂM CHỨNG]; và K-CURE của Hàn Quốc, dự án của Bộ Y tế và Phúc lợi từ năm 2022 [101], với ngày đăng trang cổng còn [CẦN KIỂM CHỨNG]. Nền tảng chung là mạng lưới OMOP CDM: cuối năm 2025, OHDSI ghi nhận 4.833 cộng tác viên ở 88 quốc gia, 544 nguồn dữ liệu ở 54 quốc gia và 974 triệu hồ sơ bệnh nhân duy nhất [11].

---

## 12. Kết luận và khuyến nghị thực hành cho bệnh viện đại học Việt Nam

Tổng quan giai đoạn 2015–2026 cho thấy quản lý dữ liệu nghiên cứu y sinh là một kỷ luật cốt lõi, quyết định tính toàn vẹn khoa học và an toàn của AI y khoa. Bốn thông điệp là: thiết kế chất lượng từ thượng nguồn [4]; liên thông đa chuẩn [10], [38]; riêng tư kết hợp pháp lý mới với TRE và thuật toán phân tán [62], [63], [89], [75]; đích đến là hệ thống y tế học tập [99], [88].

Đối với Việt Nam, thuận lợi là hành lang pháp lý cấp Luật đã hoàn chỉnh [64], [62], [79], [80]; khoảng trống đã được đo lường: khảo sát 5 bệnh viện của Tran và cộng sự (2025) cho thấy không bệnh viện nào chia sẻ dữ liệu qua chuẩn HL7, và 2 trong 5 chưa có bệnh án điện tử hay kho dữ liệu lâm sàng [84]. Lưu ý: mục [83] là bài tổng quan năm 2022, không phải bài khảo sát 5 bệnh viện năm 2025 [84]. Trên nền đó, bản tổng hợp đề xuất 7 khuyến nghị cho năm học 2026–2027.

**KN1 — Bắt buộc DMP ngay từ đề cương (§3).** Mọi đề tài có sinh dữ liệu cần nộp kế hoạch quản lý và chia sẻ dữ liệu (DMSP) không quá 2 trang, 6 thành phần theo chính sách NIH (hiệu lực 25/1/2023) [7], cập nhật theo mẫu rút gọn ban hành 25/2/2026, bắt buộc với hồ sơ nộp từ 25/5/2026 [5]. Hội đồng đạo đức nên đưa DMSP vào checklist phê duyệt đề cương; chi phí quản lý dữ liệu cần được dự toán trong kinh phí đề tài.

**KN2 — Áp dụng FAIR có đo lường (§7).** FAIR của Wilkinson và cộng sự (2016) là nguyên tắc hướng dẫn, không phải tiêu chuẩn kỹ thuật [12]; bệnh viện cần quy trình FAIRification 7 bước của Jacobsen và cộng sự (2020) [21] và FAIR Cookbook [44], kèm chỉ số trưởng thành đo hằng năm. "Accessible" trong y tế không đồng nghĩa "mở công khai": dữ liệu nhạy cảm vẫn đạt FAIR khi siêu dữ liệu mở và dữ liệu được truy cập có kiểm soát qua TRE.

**KN3 — Kiến trúc đa chuẩn FHIR–CDISC–OMOP với kiểm toán ánh xạ (§4 và §6).** Bệnh viện nên chọn FHIR R4 (2019) làm chuẩn trao đổi lâm sàng, dùng SMART on FHIR [36] và API Bulk Data [37], đồng thời chuẩn hóa dữ liệu quan sát theo OMOP CDM v5.4. Hướng dẫn FHIR-to-OMOP (v1.0.0) là cầu nối giữa hai chuẩn [10]. Mọi ánh xạ phải được kiểm toán về mất mát ngữ nghĩa; thử nghiệm lâm sàng áp dụng ICH E6(R3) [4], ghi ngày chốt cho mọi tuyên bố về phiên bản chuẩn.

**KN4 — Đo lường chất lượng dữ liệu và bảo đảm tái lập (§5).** Chất lượng dữ liệu cần được đo theo 5 chiều của Weiskopf và Weng (2013) — đầy đủ, chính xác, nhất quán, hợp lý, kịp thời [28]. Dữ liệu khuyết phải được phân loại theo Rubin (1976) [31] và xử lý bằng multiple imputation (Sterne và cộng sự, 2009) [32]; không dùng điền giá trị trung bình hay mang giá trị cuối về trước. Khảo sát của Baker (2016) cho thấy hơn 70% nhà nghiên cứu không tái lập được thí nghiệm của nhóm khác [33] — bệnh viện cần yêu cầu nộp mã phân tích kèm dữ liệu trong kho lưu trữ và dùng nền tảng thu thập dữ liệu đã thẩm định như REDCap [6], [102].

**KN5 — Tuân thủ pháp lý theo Luật 91/2025 và Nghị định 356/2025 (§8 và §10).** Từ 1/1/2026, Nghị định 13/2023 đã hết hiệu lực; khung hiện hành là Luật 91/2025/QH15 [62] và Nghị định 356/2025/NĐ-CP [63], cùng Luật Dữ liệu 60/2024/QH15 [64]. Mọi tài liệu nội bộ còn trích dẫn Nghị định 13/2023 phải được sửa ngay. Bệnh viện cần bổ nhiệm cán bộ bảo vệ dữ liệu (DPO), lập hồ sơ đánh giá tác động cho từng nghiên cứu, và phân biệt rõ ẩn danh hóa, giả danh hóa và khử định danh [57]. Bệnh án điện tử [65] và thử nghiệm lâm sàng [66] cần khớp nối với các yêu cầu này ngay từ khâu thiết kế.

**KN6 — Thí điểm AI-ready theo mô hình "đưa thuật toán tới dữ liệu" (§9 và §11).** Bệnh viện nên bắt đầu bằng một thí điểm nhỏ có quản trị: chuẩn hóa dữ liệu theo OMOP CDM và chạy phân tích trong TRE nội bộ theo khung Five Safes [75] [97]. Chỉ khi hạ tầng sẵn sàng mới mở rộng sang học liên kết đa viện theo bằng chứng EXAM (+16% AUC, +38% khả năng tổng quát hóa) [89] và Swarm Learning [87]. Dữ liệu tổng hợp (Synthea [93]) chỉ dùng cho phát triển mã và đào tạo; mọi kết luận lâm sàng phải thẩm định lại trên dữ liệu thật [94], [96]. Mọi mô hình AI lâm sàng cần có Model Card và giám sát trôi dạt định kỳ, với bác sĩ là người ra quyết định cuối cùng.

**KN7 — Đầu tư vào con người và hạ tầng dùng chung, theo lộ trình tới hệ thống y tế học tập (§10 và §11).** Bệnh viện cần biên chế Data Steward chuyên trách [16] và một Trung tâm Tích hợp Dữ liệu (DIC). Lộ trình: 2026–2027 củng cố DMP, FAIR và chất lượng dữ liệu; 2027–2029 vận hành TRE nội bộ và tham gia mạng lưới OMOP/OHDSI [11]; từ 2029 mới mở rộng FL đa viện và khép kín vòng lặp LHS [99], [88]. Chỉ khi dữ liệu được quản lý như một tài sản có quản trị, bệnh viện đại học Việt Nam mới chuyển từ số hóa hồ sơ sang tạo sinh tri thức và bằng chứng lâm sàng có tầm vóc khu vực và quốc tế.

---

## Phụ lục A. Bảng 30 bài báo và văn bản landmark

*Bảng này chỉ gồm các nguồn đã kiểm chứng đầy đủ. Ký hiệu [n] là số mục trong danh mục 334 tài liệu tham khảo chuẩn hóa APA; ký hiệu (BSn) là tài liệu bổ sung ngoài danh mục 334, đã kiểm chứng đầy đủ ngày 19–20/11/2026 (xem danh sách tài liệu bổ sung cuối phần này). Không đưa vào bảng các mục còn [CẦN KIỂM CHỨNG] — cụ thể Kahn và cộng sự (2016) [30] (danh sách tác giả đầy đủ) và Sweeney (2002) [68] (DOI) — dù cả hai đều là công trình nền tảng; điều phối viên bổ sung sau khi đối chiếu PMC/PubMed.*

| Tác giả | Năm | Tạp chí / Nguồn | Đóng góp chính | DOI / Định danh |
|---|---|---|---|---|
| Wilkinson và cộng sự [12] | 2016 | *Scientific Data* | Nguyên tắc FAIR (F1–F4, A1–A2, I1–I3, R1); FAIR là nguyên tắc, không phải tiêu chuẩn | 10.1038/sdata.2016.18 |
| Jacobsen và cộng sự [21] | 2020 | *Data Intelligence* | Quy trình FAIRification 7 bước trong 3 pha | 10.1162/dint_a_00028 |
| Rocca-Serra và cộng sự [44] | 2023 | *Scientific Data* | FAIR Cookbook — công thức FAIRification cho khoa học sự sống (FAIRplus/ELIXIR) | 10.1038/s41597-023-02166-3 |
| Hripcsak và cộng sự [38] | 2015 | *Studies in Health Technology and Informatics* | Mô tả sáng lập OHDSI và OMOP CDM (kỷ yếu MEDINFO 2015, không phải *JAMIA*) | PMCID PMC4815923 |
| Overhage và cộng sự [39] | 2012 | *Journal of the American Medical Informatics Association* | Thẩm định OMOP CDM trên 10 cơ sở dữ liệu quan sát | 10.1136/amiajnl-2011-000376 |
| Suchard và cộng sự [40] | 2019 | *The Lancet* | LEGEND-HTN: hiệu quả và an toàn thuốc hạ áp đầu tay, 4,9 triệu bệnh nhân, 22.000 tỉ số nguy cơ đã hiệu chuẩn | 10.1016/S0140-6736(19)32317-7 |
| Lane và cộng sự [103] | 2020 | *The Lancet Rheumatology* | An toàn hydroxychloroquine ± azithromycin, 14 cơ sở dữ liệu, 6 quốc gia, >950.000 người dùng HCQ | 10.1016/S2665-9913(20)30276-9 |
| Mandel và cộng sự [36] | 2016 | *Journal of the American Medical Informatics Association* | SMART on FHIR — nền tảng ứng dụng thay thế được cho hồ sơ bệnh án điện tử | 10.1093/jamia/ocv189 |
| Mandl và cộng sự [37] | 2020 | *npj Digital Medicine* | FHIR Bulk Data Access API — xuất dữ liệu quần thể "push button" | 10.1038/s41746-020-00358-4 |
| HL7 International [10] | n.d. (v1.0.0) | *FHIR to OMOP Implementation Guide* | Ánh xạ lõi tài nguyên FHIR sang OMOP CDM v5.4 (bản Informative, dựa trên FHIR v5.0.0) | Không có DOI; hl7.org/fhir/uv/omop/ |
| Harris và cộng sự [6] | 2009 | *Journal of Biomedical Informatics* | REDCap — phương pháp luận thu thập dữ liệu dựa trên siêu dữ liệu | 10.1016/j.jbi.2008.08.010 |
| Harris và cộng sự [102] | 2019 | *Journal of Biomedical Informatics* | REDCap Consortium — cộng đồng quốc tế các đối tác nền tảng phần mềm | 10.1016/j.jbi.2019.103208 |
| Weiskopf & Weng [28] | 2013 | *Journal of the American Medical Informatics Association* | 5 chiều chất lượng dữ liệu EHR: completeness, correctness, concordance, plausibility, currency | 10.1136/amiajnl-2011-000681 |
| Rubin [31] | 1976 | *Biometrika* | Khung cơ chế dữ liệu khuyết MCAR / MAR / MNAR | 10.1093/biomet/63.3.581 |
| Sterne và cộng sự [32] | 2009 | *BMJ* | Multiple imputation: tiềm năng và cạm bẫy; không dùng mean imputation hay LOCF | 10.1136/bmj.b2393 |
| Baker [33] | 2016 | *Nature* | Khảo sát tái lập: >70% trong 1.500 nhà khoa học không tái lập được thí nghiệm của nhóm khác | 10.1038/533452a |
| Dayan và cộng sự [89] | 2021 | *Nature Medicine* | EXAM: học liên kết dự báo kết cục COVID-19, 20 cơ sở, 16.148 ca; +16% AUC, +38% khả năng tổng quát hóa | 10.1038/s41591-021-01506-3 |
| Pati và cộng sự [90] | 2022 | *Nature Communications* | FeTS: học liên kết phát hiện ranh giới u nguyên bào thần kinh đệm, 71 trung tâm, 6 châu lục, 6.314 bệnh nhân | 10.1038/s41467-022-33407-5 |
| Warnat-Herresthal và cộng sự [87] | 2021 | *Nature* | Swarm Learning: học máy lâm sàng phi tập trung, bảo mật; >16.400 mẫu máu, >95.000 X-quang ngực | 10.1038/s41586-021-03583-3 |
| Heyndrickx và cộng sự [91] | 2024 | *Journal of Chemical Information and Modeling* | MELLODDY: học liên kết liên dược phẩm, 10 công ty, >2,6 tỉ điểm dữ liệu, >21 triệu phân tử | 10.1021/acs.jcim.3c00799 |
| Sadilek và cộng sự [71] | 2021 | *npj Digital Medicine* | Nghiên cứu sức khỏe "privacy-first" bằng học liên kết | 10.1038/s41746-021-00489-2 |
| Walonoski và cộng sự [93] | 2018 | *Journal of the American Medical Informatics Association* | Synthea: sinh hồ sơ bệnh nhân tổng hợp chuẩn FHIR/C-CDA/CSV | 10.1093/jamia/ocx079 |
| Williamson và cộng sự [98] | 2020 | *Nature* | OpenSAFELY: yếu tố liên quan tử vong COVID-19 trên 17.278.392 hồ sơ người trưởng thành | 10.1038/s41586-020-2521-4 |
| Friedman và cộng sự [99] | 2015 | *Journal of the American Medical Informatics Association* | Chương trình nghiên cứu hệ thống y tế học tập (LHS); vòng lặp P2D → D2K → K2P | 10.1136/amiajnl-2014-002977 |
| Friedman và cộng sự [88] | 2024 | *Learning Health Systems* | Hạ tầng kỹ thuật–xã hội cho LHS: 4 trụ cột, 10 dịch vụ nền tảng dùng chung | 10.1002/lrh2.10405 |
| Goldacre & Morley [97] | 2022 | Bộ Y tế và Chăm sóc Xã hội Anh (DHSC) | *Better, broader, safer* (Goldacre Review): TRE trở thành chuẩn mặc định cho phân tích hồ sơ NHS | Không có DOI (báo cáo chính phủ) |
| Machanavajjhala và cộng sự [69] | 2007 | *ACM Transactions on Knowledge Discovery from Data* | ℓ-Diversity: quyền riêng tư vượt ra ngoài k-anonymity | 10.1145/1217299.1217302 |
| International Council for Harmonisation [4] | 2025 | *ICH E6(R3) Guideline for Good Clinical Practice* | GCP mới: 11 nguyên tắc; Phụ lục 1 §4 về quản trị dữ liệu và hệ thống máy tính hóa | Step 4, 6/1/2025 (database.ich.org) |
| National Institutes of Health [7] | 2020 (hiệu lực 2023) | *Final NIH Policy for Data Management and Sharing* (NOT-OD-21-013) | DMSP ≤2 trang, 6 thành phần; chia sẻ chậm nhất lúc công bố hoặc cuối thời gian tài trợ | NOT-OD-21-013 (grants.nih.gov) |
| Quốc hội Việt Nam [62] | 2025 | *Luật Bảo vệ dữ liệu cá nhân*, số 91/2025/QH15 | Luật chuyên ngành đầu tiên về bảo vệ dữ liệu cá nhân của Việt Nam; 5 chương, 39 điều | Thông qua 26/6/2025, hiệu lực 1/1/2026 |

## Phụ lục B. Danh mục thay đổi so với bản Google Docs

*Bản tổng hợp này viết lại từ bản Google Docs gốc “Tổng Quan RDM Y Sinh” (60 trang, 25.133 từ, 334 tài liệu tham khảo). Số [n] trong phụ lục này là số trong danh mục gốc 334 mục, không phải số trong danh mục tham khảo của bản tổng hợp. Ngày chốt mọi khẳng định về phiên bản chuẩn và văn bản pháp luật: 20/11/2026.*

### B.1. Đã sửa (hiệu đính thông tin sai hoặc lỗi thời trong bản gốc)

1. **Thông tư 13/2025/TT-BYT (số 17):** mục gốc dẫn tới bài viết trên HL7 Việt Nam, không phải văn bản gốc — đã thay bằng văn bản gốc; đồng thời sửa thời hạn: bệnh viện chậm nhất 30/9/2025, cơ sở khác chậm nhất 31/12/2026 (không gộp thành “hạn 31/12/2026 cho mọi bệnh viện”).
2. **Nghị quyết 72-NQ/TW (số 276):** khám sức khỏe định kỳ/sàng lọc miễn phí ít nhất 1 lần/năm từ 2026 cho nhóm ưu tiên trước, các đối tượng còn lại từ 2028; không viết “từ 2026 cho mọi người dân”.
3. **Tran và cộng sự (số 298):** bản gốc ghi là 2025, *JMIR Formative Research* 9:e53483 — đã sửa thành **Tran và cộng sự 2022**, *Journal of Medical Internet Research* 24(2), e32392, DOI 10.2196/32392, PMC8867296 / PMID 35138264. Mã e53483 thuộc một bài khác (khảo sát 5 bệnh viện năm 2025) — hai bài không được gộp (xem tài liệu tham khảo số 84).
4. **NIH NOT-OD-26-046 (số 40):** bổ sung thông báo cập nhật thành phần DMSP (phát hành 25/2/2026, thay NOT-OD-21-014, bắt buộc với hồ sơ nộp từ 25/5/2026); chính sách DMS 2023 không thay đổi.
5. **EHDS:** bổ sung văn bản Quy định (EU) 2025/327 gốc (hiệu lực 26/3/2025; áp dụng chung từ 26/3/2027; hai pha tới 2029 và 2031); các số 242 và 329 trong danh mục chỉ là tài liệu thứ cấp về EHDS, không thay văn bản gốc.
6. **ICH E6(R3) (số 3):** Nguyên tắc và Phụ lục 1 Step 4 ngày 6/1/2025 (EU hiệu lực 23/7/2025); Phụ lục 2 Step 4 ngày 3/6/2026 (EU hiệu lực 15/1/2027).
7. **Hripcsak và cộng sự (2015) (số 19):** đăng trên *Studies in Health Technology and Informatics* (kỷ yếu MEDINFO 2015), không phải *JAMIA*.
8. **Khung pháp lý Việt Nam:** Nghị định 13/2023/NĐ-CP chỉ còn hiệu lực tới 31/12/2025; từ 1/1/2026 khung hiện hành là Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 (số 16) và Nghị định 356/2025/NĐ-CP (số 54). Thông tư 46/2018/TT-BYT và Thông tư 29/2018/TT-BYT đã được thay thế lần lượt bởi Thông tư 13/2025/TT-BYT (số 17) và Thông tư 50/2025/TT-BYT (số 18).
9. **FHIR R6:** R6 chưa phát hành; đang ở vòng bỏ phiếu (ballot 5 tháng 7/2026), dự kiến hoàn tất 2026–2027. R4 (2019) vẫn là chuẩn triển khai thực tế chủ đạo; R5 phát hành 26/3/2023.
10. **Số liệu mạng lưới OHDSI (số 6):** cập nhật theo *OHDSI 2025 Year in Review* — 4.833 cộng tác viên ở 88 quốc gia; 544 nguồn dữ liệu ở 54 quốc gia; 974 triệu hồ sơ bệnh nhân duy nhất — thay cho con số cũ “hơn 80 nước / hàng tỉ bản ghi” không ghi nguồn.
11. **Số liệu REDCap (số 36):** con số quy mô trong bài phải ghi nguồn và ngày đo; link SCIRP trong danh mục gốc đã thay bằng DOI của nhà xuất bản. Bài Harris và cộng sự (2019) về REDCap Consortium được bổ sung (tài liệu tham khảo số 102).
12. **FHIR-to-OMOP IG (số 8):** v1.0.0 Informative (dựa trên FHIR v5.0.0), kiểm tra ngày 20/11/2026; ghi ngày truy cập khi nộp vì tài liệu không có DOI.
13. **Dayan 2021 (EXAM) (số 307) và Harris 2009 (số 36):** link ResearchGate/SCIRP trong danh mục gốc đã thay bằng DOI của nhà xuất bản.

### B.2. Đã bổ sung (tài liệu bản gốc nhắc tới nhưng danh mục chưa có, hoặc cần thiết cho bản tổng hợp)

1. **FAIR Cookbook** — Rocca-Serra và cộng sự (2023), *Scientific Data* 10:292, doi:10.1038/s41597-023-02166-3.
2. **Mandl và cộng sự (2020)** — FHIR Bulk Data, *npj Digital Medicine* 3:151, doi:10.1038/s41746-020-00358-4.
3. **Rubin (1976)** — cơ chế dữ liệu khuyết MCAR/MAR/MNAR, *Biometrika* 63(3):581–592.
4. **Sterne và cộng sự (2009)** — multiple imputation, *BMJ* 338:b2393.
5. **Baker (2016)** — khảo sát tái lập, *Nature* 533:452–454 (số 149 trong danh mục gốc).
6. **Lane và cộng sự (2020)** — nghiên cứu OHDSI COVID Study-a-thon đầu tiên, *The Lancet Rheumatology* 2:e698–e711 (số 189).
7. **Goldacre & Morley (2022)** — *Better, broader, safer* (Goldacre Review), DHSC Anh.
8. **Harris và cộng sự (2019)** — REDCap Consortium, *Journal of Biomedical Informatics* 95:103208.
9. **GDPR (EU) 2016/679** và **EHDS (EU) 2025/327** — văn bản gốc.
10. **Friedman và cộng sự (2015)** — chương trình nghiên cứu hệ thống y tế học tập, *JAMIA* 22(1):43–50.
11. **Heyndrickx và cộng sự (2024)** — MELLODDY, *Journal of Chemical Information and Modeling* 64(7):2331–2344.
12. **Wilkinson và cộng sự (2019)** — khung đánh giá trưởng thành FAIR, *Scientific Data* 6:174, doi:10.1038/s41597-019-0184-5.
13. **Quy định (EU) số 536/2014, Điều 58** — lưu trữ hồ sơ thử nghiệm tối thiểu 25 năm.
14. **HIPAA Privacy Rule, 45 CFR §164.514** — hai phương pháp khử định danh.
15. **Tran và cộng sự (2025)** — khảo sát áp dụng công nghệ sức khỏe số tại 5 bệnh viện Việt Nam, *JMIR Formative Research* 9:e53483 (tách rõ khỏi bài Tran 2022, số 298).
16. **DAMA International (2017)** — *DAMA-DMBOK* (2nd ed.), nguồn cho khung quản trị dữ liệu ở §2.

### B.3. Đã loại bỏ (khỏi danh mục trích dẫn học thuật)

1. **Số 1–2:** hai file nháp đầu vào (“Literature_Review.md” và “Literature_Review_Quan_ly_du_lieu_nghien_cuu_y_sinh.md”) — không phải nguồn trích dẫn.
2. **Các bài giải thích thứ cấp trên intuitionlabs.ai:** số 4, 5 (ICH E6(R3)), số 160 (CDISC), số 221 (checklist) — chỉ dùng để đọc hiểu; nguồn gốc xem ICH E6(R3) (số 3).
3. **Các bản trùng trên ResearchGate / Studocu / eScholarship / toolkit:** số 20 (Hripcsak 2015, gộp vào 19), 99 (Jacobsen 2020, gộp vào 194), 168 (Mandel 2016, gộp vào 161), 192 (toolkit Wilkinson 2016, gộp vào 191), 311 (Studocu Dayan 2021, gộp vào 307), 324 (ResearchGate Machanavajjhala 2007, gộp vào 244), 305 (ResearchGate Friedman 2024, gộp vào 333), 150 (trùng Baker 2016, gộp vào 149).
4. **Số 55 và 56:** bản trùng của Luật 91/2025/QH15 (gộp vào số 16) và Thông tư 50/2025/TT-BYT (gộp vào số 18).
5. **Số 10:** bản preprint bioRxiv của công trình AI-readiness (Bridge2AI) — gộp vào số 9 (bản v6, 24/4/2026).
6. **Số 186–187:** bài báo phổ thông/tin tức về LEGEND-HTN — không dùng làm trích dẫn học thuật; chỉ giữ số 185.
7. **Số 312:** hướng dẫn CASRAI về Swarm Learning (thứ cấp) — không thay bài gốc Warnat-Herresthal và cộng sự (2021) (số 313).
8. **Số 317:** preprint Research Square 2026 về sinh dữ liệu tổng hợp, chưa bình duyệt — không trích dẫn.

### B.4. Quyết định của điều phối viên về các điểm còn tồn đọng

1. **Phạm vi thời gian: 2015–2026, chốt 20/11/2026.** Các tài liệu 2026 được giữ khi là văn bản chính sách/chuẩn đang có hiệu lực (NOT-OD-26-046, ICH E6(R3) Annex 2, Bridge2AI preprint v6). Hai mục 196 (Inau và cộng sự, 2026) và 241 (Weatherhead và cộng sự, 2026) **không được trích dẫn trong bản tổng hợp này**: mục 241 do tên tác giả trùng lặp trong danh mục APA, chưa đối chiếu lại PMC13346167; mục 196 là trường hợp FAIRification chuyên biệt trong nghiên cứu đái tháo đường, không cần thiết cho luận điểm chung.
2. **Mục 233 (Murgia và cộng sự, 2025, về EHDS):** không được trích dẫn trong bản tổng hợp; luận điểm EHDS dựa trên văn bản gốc (EU) 2025/327.
3. **Kahn và cộng sự (2016) (số 135) và Sweeney (2002) (số 35):** vẫn được trích dẫn, nhưng danh sách tác giả đầy đủ của Kahn và DOI của Sweeney còn [CẦN KIỂM CHỨNG] — đối chiếu PMC5051581 và nhà xuất bản trước khi nộp. Cả hai đều không có trong Phụ lục A vì lý do này.
4. **Dayan và cộng sự (2021) (số 307):** danh sách tác giả đầy đủ còn [CẦN KIỂM CHỨNG]; trong bài chỉ dùng “Dayan và cộng sự”.
5. **Khoảng tin cậy của LEGEND-HTN (§6):** ba tỉ số nguy cơ được gộp chung khoảng 0,74–0,95 trong bản tổng hợp; khi nộp, ghi riêng từng khoảng theo bài gốc (Suchard và cộng sự, 2019).
6. **Số liệu TRUST/K-CURE (§11):** chỉ trình bày làm ví dụ tham chiếu; các con số quy mô chi tiết còn [CẦN KIỂM CHỨNG], không dùng làm kết luận.

## Ghi chú về trích dẫn và giới hạn của bản tổng hợp

- **Phạm vi và ngày chốt:** tổng quan tường thuật có kiểm chứng, phạm vi 2015–2026, chốt 20/11/2026. Đây không phải systematic review PRISMA đầy đủ: không có lưu đồ PRISMA và không có số lượng sàng lọc/loại/đưa vào đầy đủ (xem §1).
- **Tài liệu tham khảo được đánh số lại từ đầu** theo thứ tự xuất hiện trong bản tổng hợp này; số [n] trong thân bài là số của danh mục cuối bản tổng hợp, không phải số trong danh mục gốc 334 mục. Đối chiếu với danh mục gốc xem Phụ lục B.
- **Các mục còn [CẦN KIỂM CHỨNG]** trong danh mục cuối: [30], [48], [49], [61], [68], [89], [95], [100], [101]. Các mục này vẫn được trích dẫn vì nội dung chính đã kiểm chứng, nhưng một trường (thường là danh sách tác giả đầy đủ, DOI, số trang, hoặc ngày cập nhật của trang web) chưa xác minh xong — đối chiếu nguồn gốc trước khi nộp.
- **Bridge2AI (AI-readiness):** công trình của Clark và cộng sự hiện mới là bản preprint bioRxiv v6 (24/4/2026), chưa qua bình duyệt; trích dẫn đúng tư cách preprint.
- **DAMA-DMBOK và HIMSS AMAM** được trình bày là khung tham chiếu/công cụ tự đánh giá, không phải chuẩn bắt buộc. Nội dung DAMA dựa trên bản 2nd ed. đã xuất bản (2017); dự án DAMA-DMBOK 3.0 (khởi động 6/2025) chỉ nêu như hướng phát triển.
- **Không trích dẫn trong bản tổng hợp:** mục 196 và 241 trong danh mục gốc (xem B.4.1), mục 233 (Murgia và cộng sự, 2025), các mục 225–226 (tài liệu dự thảo/bảng tiếp thu ý kiến), và các bài thứ cấp trên intuitionlabs.ai.
- **Số liệu mạng lưới OHDSI** (4.833 cộng tác viên/88 nước; 544 nguồn/54 nước; 974 triệu hồ sơ) theo *OHDSI 2025 Year in Review*; số liệu REDCap phải ghi nguồn và ngày đo khi dùng.
- **Không có bằng chứng công bố về áp dụng CDISC/OMOP/FHIR tại bệnh viện Việt Nam** — bản tổng hợp trình bày điều này như khoảng trống, không suy ra đã áp dụng.

---

## Tài liệu tham khảo

*Danh mục này chỉ liệt kê các mục thực sự được trích dẫn trong bản tổng hợp, theo APA 7th, đánh số lại từ đầu theo thứ tự xuất hiện. Tổng số: **103 mục**, trong đó **9 mục còn [CẦN KIỂM CHỨNG]** ít nhất một trường (xem ghi chú cuối mỗi mục). Các tài liệu bổ sung ngoài danh mục gốc 334 mục được ghi chú trong Phụ lục B.*

1. DAMA International. (n.d.). *DAMA-DMBOK® 3.0 project*. https://dama.org/dama-dmbok-3-0-project/ (Truy cập ngày 20/11/2026)

2. Healthcare Information and Management Systems Society. (n.d.). *Adoption Model for Analytics Maturity* [Criteria sheet]. PALS Global. http://palsglobal.com/himss/ (Truy cập ngày 20/11/2026)

3. European Commission. (n.d.). *Horizon Europe data management plan* [Template]. https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e519589e89&appId=PPGMS (Truy cập ngày 20/11/2026)

4. International Council for Harmonisation. (2025). *ICH E6(R3) Guideline for Good Clinical Practice* (Step 4, 6 January 2025). https://database.ich.org/sites/default/files/ICH_E6%28R3%29_Step4_FinalGuideline_2025_0106.pdf

5. National Institutes of Health. (2026). *Updated elements of an NIH Data Management and Sharing Plan* (NOT-OD-26-046; released 25 February 2026). https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-046.html

6. Harris, P. A., Taylor, R., Thielke, R., Payne, J., Gonzalez, N., & Conde, J. G. (2009). Research electronic data capture (REDCap) — A metadata-driven methodology and workflow process for providing translational research informatics support. *Journal of Biomedical Informatics*, *42*(2), 377–381. https://doi.org/10.1016/j.jbi.2008.08.010

7. National Institutes of Health. (2020). *Final NIH Policy for Data Management and Sharing* (NOT-OD-21-013; effective 25 January 2023). https://grants.nih.gov/grants/guide/notice-files/NOT-OD-21-013.html

8. National Institutes of Health. (2020). *Supplemental information to the NIH Policy for Data Management and Sharing: Elements of an NIH Data Management and Sharing Plan* (NOT-OD-21-014; released 29 October 2020). https://grants.nih.gov/grants/guide/notice-files/NOT-OD-21-014.html

9. HL7 International. (2023). *FHIR* (Version 5.0.0) [Specification]. https://hl7.org/fhir/

10. HL7 International. (n.d.). *FHIR to OMOP Implementation Guide* (v1.0.0, Informative). http://hl7.org/fhir/uv/omop/

11. Sachson, C. (2025). *Our journey* (5th ed.). Observational Health Data Sciences and Informatics. https://www.ohdsi.org/wp-content/uploads/2025/10/OurJourney-2025.pdf

12. Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, *3*, 160018. https://doi.org/10.1038/sdata.2016.18

13. Society for Clinical Data Management. (n.d.). *GCDMP — Good Clinical Data Management Practices*. https://scdm.org/gcdmp/ (Truy cập ngày 20 tháng 11 năm 2026)

14. DAMA International. (2017). *DAMA-DMBOK: Data Management Body of Knowledge* (2nd ed.). Technics Publications.

15. Association of American Medical Colleges. (2015). *Data governance in academic medicine* [Webinar materials]. https://www.aamc.org/media/34986/download

16. Wendelborn, C., Anger, M., & Schickhardt, C. (2023). What is data stewardship? Towards a comprehensive understanding. *Journal of Biomedical Informatics*, *140*, 104337. https://doi.org/10.1016/j.jbi.2023.104337

17. Jetten, M., Grootveld, M., Mordant, A., Jansen, M., Bloemers, M., Miedema, M., & van Gelder, C. W. G. (2021). *Professionalising data stewardship in the Netherlands: Competences, training and education. Dutch roadmap towards national implementation of FAIR data stewardship* (Version 1.1). Zenodo. https://doi.org/10.5281/zenodo.4623713

18. The Turing Way Community. (n.d.). *Data stewards: Overview*. In *The Turing Way: A handbook for reproducible, ethical and collaborative research*. https://book.the-turing-way.org/collaboration/research-infrastructure-roles/data-steward/ (Truy cập ngày 20/11/2026)

19. CASRAI. (n.d.). *Horizon Europe FAIR Data Management Plan*. https://casrai.org/guides/horizon-europe-fair-data-management-plan (Truy cập ngày 20/11/2026)

20. Expert Advisory Group on Data Access. (2017, August). *Data management plans: Recommendations*. Wellcome. https://cms.wellcome.org/sites/default/files/data-management-plans.pdf

21. Jacobsen, A., Kaliyaperumal, R., Bonino da Silva Santos, L. O., Mons, B., Schultes, E., Roos, M., & Thompson, M. (2020). A generic workflow for the data FAIRification process. *Data Intelligence*, *2*(1–2), 56–65. https://doi.org/10.1162/dint_a_00028

22. DataCite Metadata Working Group. (2024). *DataCite Metadata Schema for the publication and citation of research data and other research outputs* (Version 4.6). DataCite e.V. https://doi.org/10.14454/mzv1-5b55

23. Villere, S. (2024). Common Data Elements Repository. *Medical Reference Services Quarterly*, *43*(2), 182–190. https://doi.org/10.1080/02763869.2024.2323896

24. U.S. Food and Drug Administration. (2024). *Electronic systems, electronic records, and electronic signatures in clinical investigations: Questions and answers* (Guidance for Industry). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/electronic-systems-electronic-records-and-electronic-signatures-clinical-investigations-questions

25. CASRAI. (n.d.). *Castor EDC & lightweight EDC for IITs*. https://casrai.org/guides/castor-edc-lightweight-edc-investigator-initiated-trials (Truy cập ngày 20 tháng 11 năm 2026)

26. Yamamoto, K., Ota, K., Akiya, I., & Shintani, A. (2017). A pragmatic method for transforming clinical research data from the research electronic data capture “REDCap” to Clinical Data Interchange Standards Consortium (CDISC) Study Data Tabulation Model (SDTM): Development and evaluation of REDCap2SDTM. *Journal of Biomedical Informatics*, *70*, 65–76. https://doi.org/10.1016/j.jbi.2017.05.003

27. Gurley, M. J., Warner, J., Bushmanova, Y., & Wehbe, F. (2021). *REDCap2OMOP: A platform for ETLing REDCap projects into the OMOP CDM*. OHDSI 2021 Symposium. https://www.ohdsi.org/wp-content/uploads/2021/09/65_REDCap2OMOP.pdf

28. Weiskopf, N. G., & Weng, C. (2013). Methods and dimensions of electronic health record data quality assessment: Enabling reuse for clinical research. *Journal of the American Medical Informatics Association*, *20*(1), 144–151. https://doi.org/10.1136/amiajnl-2011-000681

29. Sheetz, N., Wilson, B., Benedict, J., Huffman, E., Lawton, A., Travers, M., Nadolny, P., Young, S., Given, K., & Florin, L. (2014). Evaluating source data verification as a quality control measure in clinical trials. *Therapeutic Innovation & Regulatory Science*, *48*(6), 671–680. https://doi.org/10.1177/2168479014554400

30. Kahn, M. G., Callahan, T. J., Barnard, J., Bauck, A. E., Brown, J., Bruce, B. B., Desai, S., Downs, M., Fiechtner, C., Groeneveld, P. W., Kittel, C., Kitzmiller, R. R., & [CẦN KIỂM CHỨNG các tác giả còn lại — đối chiếu PMC5051581 để ghi đúng 20 tác giả đầu + et al.]. (2016). A harmonized data quality assessment terminology and framework for the secondary use of electronic health record data. *eGEMs*, *4*(1), 1244. https://doi.org/10.13063/2327-9214.1244 — **[CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.]**

31. Rubin, D. B. (1976). Inference and missing data. *Biometrika*, *63*(3), 581–592. https://doi.org/10.1093/biomet/63.3.581

32. Sterne, J. A. C., White, I. R., Carlin, J. B., Spratt, M., Royston, P., Kenward, M. G., Wood, A. M., & Carpenter, J. R. (2009). Multiple imputation for missing data in epidemiological and clinical research: Potential and pitfalls. *BMJ*, *338*, b2393. https://doi.org/10.1136/bmj.b2393

33. Baker, M. (2016). 1,500 scientists lift the lid on reproducibility. *Nature*, *533*(7604), 452–454. https://doi.org/10.1038/533452a — **[Ghi chú: chi tiết thư mục đã kiểm chứng; cờ [CẦN KIỂM CHỨNG] trong bảng APA chỉ liên quan tới ID ResearchGate và mục trùng 150 trong danh mục gốc.]**

34. CDISC, & HL7 International. (2021). *FHIR to CDISC Joint Mapping Implementation Guide* (Version 1.0). https://www.cdisc.org/standards/real-world-data/fhir-cdisc-joint-mapping-implementation-guide-v1-0 (Truy cập ngày 20 tháng 11 năm 2026)

35. HL7 International. (2026). *Valueset-example-characteristic-codes*. In *FHIR* (v6.0.0-ballot5). http://hl7.org/fhir/6.0.0-ballot5/valueset-example-characteristic-codes.html

36. Mandel, J. C., Kreda, D. A., Mandl, K. D., Kohane, I. S., & Ramoni, R. B. (2016). SMART on FHIR: A standards-based, interoperable apps platform for electronic health records. *Journal of the American Medical Informatics Association*, *23*(5), 899–908. https://doi.org/10.1093/jamia/ocv189

37. Mandl, K. D., Gottlieb, D., & Mandel, J. C. (2020). Push Button Population Health: The SMART/HL7 FHIR Bulk Data Access API. *npj Digital Medicine*, *3*, 151. https://doi.org/10.1038/s41746-020-00358-4

38. Hripcsak, G., Duke, J. D., Shah, N. H., Reich, C. G., Huser, V., Schuemie, M. J., Suchard, M. A., Park, R. W., Wong, I. C. K., Rijnbeek, P. R., van der Lei, J., Pratt, N., Norén, G. N., Li, Y.-C., Stang, P. E., Madigan, D., & Ryan, P. B. (2015). Observational Health Data Sciences and Informatics (OHDSI): Opportunities for observational researchers. *Studies in Health Technology and Informatics*, *216*, 574–578. https://pmc.ncbi.nlm.nih.gov/articles/PMC4815923/

39. Overhage, J. M., Ryan, P. B., Reich, C. G., Hartzema, A. G., & Stang, P. E. (2012). Validation of a common data model for active safety surveillance research. *Journal of the American Medical Informatics Association*, *19*(1), 54–60. https://doi.org/10.1136/amiajnl-2011-000376

40. Suchard, M. A., Schuemie, M. J., Krumholz, H. M., You, S. C., Chen, R., Pratt, N., Reich, C. G., Duke, J., Madigan, D., Hripcsak, G., & Ryan, P. B. (2019). Comprehensive comparative effectiveness and safety of first-line antihypertensive drug classes: A systematic, multinational, large-scale analysis. *The Lancet*, *394*(10211), 1816–1826. https://doi.org/10.1016/S0140-6736(19)32317-7

41. Queralt-Rosinach, N., Kaliyaperumal, R., Bernabé, C. H., Long, Q., Joosten, S. A., van der Wijk, H. J., Flikkenschild, E. L. A., Burger, K., Jacobsen, A., Mons, B., & Roos, M. (2022). Applying the FAIR principles to data in a hospital: Challenges and opportunities in a pandemic. *Journal of Biomedical Semantics*, *13*(1), Article 12. https://doi.org/10.1186/s13326-022-00263-7

42. Sinaci, A. A., Núñez-Benjumea, F. J., Gencturk, M., Jauer, M.-L., Deserno, T., Chronaki, C., Cangioli, G., Cavero-Barca, C., Rodríguez-Pérez, J. M., Pérez-Pérez, M. M., Laleci Erturkmen, G. B., Hernández-Pérez, T., Méndez-Rodríguez, E., & Parra-Calderón, C. L. (2020). From raw data to FAIR data: The FAIRification workflow for health research. *Methods of Information in Medicine*, *59*(S01), e21–e32. https://doi.org/10.1055/s-0040-1713684

43. Kasbohm, E., Inau, E. T., Zeleke, A. A., Shiferaw, K. B., Abaza, H., Clemens, V., Golebiewski, M., Gonzalez-Ocanto, M., Klopfenstein, S. A. I., Vorisek, C. N., Waltemath, D., & Schmidt, C. O. (2025). Lessons learned from evaluating the NFDI4Health metadata schema for health studies using the Research Data Alliance's FAIR data maturity model. *medRxiv*. https://doi.org/10.1101/2025.09.26.25336637

44. Rocca-Serra, P., Gu, W., Ioannidis, V., Abbassi-Daloii, T., Capella-Gutierrez, S., Chandramouliswaran, I., Splendiani, A., Burdett, T., Giessmann, R. T., Henderson, D., Batista, D., Emam, I., Gadiya, Y., Giovanni, L., Willighagen, E., Evelo, C., Gray, A. J. G., Gribbon, P., Juty, N., … Sansone, S.-A. (2023). The FAIR Cookbook — the essential resource for and by FAIR doers. *Scientific Data*, *10*, 292. https://doi.org/10.1038/s41597-023-02166-3

45. Wilkinson, M. D., Dumontier, M., Sansone, S.-A., Bonino da Silva Santos, L. O., Prieto, M., Batista, D., McQuilton, P., Kuhn, T., Rocca-Serra, P., Crosas, M., Schultes, E., & … (2019). Evaluating FAIR data maturity using the FAIR Data Maturity Model. *Scientific Data*, *6*, 174. https://doi.org/10.1038/s41597-019-0184-5

46. UNESCO. (2021). *UNESCO Recommendation on Open Science* (adopted 23 November 2021, 41st session of the General Conference). https://www.unesco.org/en/open-science/about

47. Taichman, D. B., Sahni, P., Pinborg, A., Peiperl, L., Laine, C., James, A., Hong, S.-T., Haileamlak, A., Gollogly, L., Godlee, F., Frizelle, F. A., Florenzano, F., Drazen, J. M., Bauchner, H., Baethge, C., & Backus, J. (2017). Data sharing statements for clinical trials: A requirement of the International Committee of Medical Journal Editors. *Journal of Korean Medical Science*, *32*(7), 1051–1053. https://doi.org/10.3346/jkms.2017.32.7.1051

48. U.S. National Library of Medicine. ([CẦN KIỂM CHỨNG] ngày cập nhật). *Clinical trial reporting requirements*. ClinicalTrials.gov. Retrieved November 20, 2026, from https://clinicaltrials.gov/policy/reporting-requirements — **[CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.]**

49. Mughal, Z., Fu, R., Luechtefeld, T., Chiswell, K., Kleinstreuer, N., Shaw, G., & Tidmarsh, G. F. (2025). Compliance with results reporting at ClinicalTrials.gov before and after the 2017 FDAAA Final Rule: A comparative analysis. *Journal of the Academy of Public Health*, *1*(1), [CẦN KIỂM CHỨNG số trang]. https://doi.org/10.70542/rcj-japh-art-vr3aga — **[CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.]**

50. Stuart, D., Baynes, G., Hrynaszkiewicz, I., Allin, K., Penny, D., Lucraft, M., & Astell, M. (2018). *Practical challenges for researchers in data sharing* [White paper]. Springer Nature. https://doi.org/10.6084/m9.figshare.5975011

51. National Center for Complementary and Integrative Health. (n.d.). *Preferred repositories*. https://www.nccih.nih.gov/grants/policies/data-management-and-sharing-policy/preferred-repositories

52. Byrd, J. B., Greene, A. C., Prasad, D. V., Jiang, X., & Greene, C. S. (2020). Responsible, practical genomic data sharing that accelerates research. *Nature Reviews Genetics*, *21*(10), 615–629. https://doi.org/10.1038/s41576-020-0257-5

53. Vivli. (2018, July 20). *Innovative global data-sharing platform Vivli launches with 2,500 clinical studies*. https://vivli.org/innovative-global-data-sharing-platform-vivli-launches-with-2500-clinical-studies/

54. Regulation (EU) No 536/2014 of the European Parliament and of the Council of 16 April 2014 on clinical trials on medicinal products for human use and repealing Directive 2001/20/EC. *Official Journal of the European Union*, L 158, 1–76. https://eur-lex.europa.eu/eli/reg/2014/536/oj

55. Bộ Y tế. (2025). *Thông tư 33/2025/TT-BYT quy định thời hạn lưu trữ hồ sơ, tài liệu ngành y tế* (ban hành 01/7/2025, hiệu lực 01/7/2025). https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Thong-tu-33-2025-TT-BYT-thoi-han-luu-tru-ho-so-tai-lieu-nganh-y-te-663505.aspx

56. Chandramouli, R., & Hibbard, E. A. (2025). *Guidelines for media sanitization* (NIST SP 800-88 Rev. 2). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-88r2

57. Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data (General Data Protection Regulation). *Official Journal of the European Union*, L 119, 1–88. https://eur-lex.europa.eu/eli/reg/2016/679/oj

58. Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the European Health Data Space and amending Directive 2011/24/EU and Regulation (EU) 2024/2847. *Official Journal of the European Union*, L, 2025/327. https://eur-lex.europa.eu/eli/reg/2025/327/oj

59. Raposo, V. L. (2025). Can personal data be recycled? The reuse and repurposing of data under the EHDS. *International Journal of Law and Information Technology*, *33*, Article eaae016. https://doi.org/10.1093/ijlit/eaae016

60. Standards for Privacy of Individually Identifiable Health Information, 45 CFR §164.514 (U.S. Department of Health and Human Services). https://www.ecfr.gov/current/title-45/section-164.514

61. Sant, M. M., & Bajada, C. J. (2025). Processing neuroimaging data for research purposes: Open Science, FAIR data, and the GDPR. *International Data Privacy Law*, *15*(3), 194–[CẦN KIỂM CHỨNG]. https://doi.org/10.1093/idpl/ipaf020 — **[CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.]**

62. Quốc hội. (2025). *Luật Bảo vệ dữ liệu cá nhân*, số 91/2025/QH15 (thông qua 26/6/2025, hiệu lực 1/1/2026).

63. Chính phủ. (2025). *Nghị định 356/2025/NĐ-CP hướng dẫn Luật Bảo vệ dữ liệu cá nhân* (ban hành 31/12/2025, hiệu lực 1/1/2026).

64. Quốc hội. (2024). *Luật Dữ liệu*, số 60/2024/QH15 (thông qua 30/11/2024, hiệu lực 1/7/2025).

65. Bộ Y tế. (2025). *Thông tư 13/2025/TT-BYT hướng dẫn triển khai hồ sơ bệnh án điện tử* (ban hành 6/6/2025, hiệu lực 21/7/2025).

66. Bộ Y tế. (2025). *Thông tư 50/2025/TT-BYT quy định về thử thuốc trên lâm sàng* (ban hành 31/12/2025, hiệu lực 27/2/2026).

67. Research Data Management Support. (2023). *K-anonymity, l-diversity and t-closeness*. In *Data Privacy Handbook* (v2023.11.24). Utrecht University. https://doi.org/10.5281/zenodo.8005847

68. Sweeney, L. (2002). k-Anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, *10*(5), 557–570. https://doi.org/10.1142/S0218488502001648 — **[CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.]**

69. Machanavajjhala, A., Kifer, D., Gehrke, J., & Venkitasubramaniam, M. (2007). ℓ-Diversity: Privacy beyond k-anonymity. *ACM Transactions on Knowledge Discovery from Data*, *1*(1), Article 3. https://doi.org/10.1145/1217299.1217302

70. Dwork, C. (2008). Differential privacy: A survey of results. In M. Agrawal, D. Du, Z. Duan, & A. Li (Eds.), *Theory and Applications of Models of Computation* (Lecture Notes in Computer Science, Vol. 4978, pp. 1–19). Springer. https://doi.org/10.1007/978-3-540-79228-4_1

71. Sadilek, A., Liu, L., Nguyen, D., Kamruzzaman, M., Serghiou, S., Rader, B., Ingerman, A., Mellem, S., Kairouz, P., Nsoesie, E. O., MacFarlane, J., Vullikanti, A., Marathe, M., Eastham, P., Brownstein, J. S., Aguera y Arcas, B., Howell, M. D., & Hernandez, J. (2021). Privacy-first health research with federated learning. *npj Digital Medicine*, *4*, 132. https://doi.org/10.1038/s41746-021-00489-2

72. Clark, T., Caufield, J. H., Parker, J. A., Al Manir, S., Amorim, E., Eddy, J., Gim, N., Gow, B., Goar, W., Haendel, M., Hansen, J. N., Harris, N., Hermjakob, H., Joachimiak, M., Jordan, G., Lee, I.-H., McWeeney, S. K., Nebeker, C., Nikolov, M., … Munoz-Torres, M. C. (2024). AI-readiness criteria for biomedical data. *bioRxiv*. https://doi.org/10.1101/2024.10.23.619844

73. Alderman, J. E., Palmer, J., Laws, E., McCradden, M. D., Ordish, J., Ghassemi, M., Pfohl, S. R., Rostamzadeh, N., Cole-Lewis, H., Glocker, B., Calvert, M., Pollard, T. J., Gill, J., Gath, J., Adebajo, A., Beng, J., Leung, C. H., Kuku, S., Farmer, L.-A., … Liu, X. (2025). Tackling algorithmic bias and promoting transparency in health datasets: The STANDING Together consensus recommendations. *The Lancet Digital Health*, *7*(1), e64–e88. https://doi.org/10.1016/S2589-7500(24)00224-3

74. Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM*, *64*(12), 86–92. https://doi.org/10.1145/3458723

75. CASRAI. (2026). *Trusted research environments & Five Safes framework*. https://casrai.org/guides/trusted-research-environments-five-safes-framework

76. Albashiti, F., Thasler, R., Wendt, T., Bathelt, F., Reinecke, I., & Schreiweis, B. (2024). Die Datenintegrationszentren — Von der Konzeption in der Medizininformatik-Initiative zur lokalen Umsetzung in einem Netzwerk Universitätsmedizin [Data integration centers—From a concept in the Medical Informatics Initiative to its local implementation in the Network of University Medicine]. *Bundesgesundheitsblatt – Gesundheitsforschung – Gesundheitsschutz*, *67*(6), 629–636. https://doi.org/10.1007/s00103-024-03879-5

77. Danciu, I., Cowan, J. D., Basford, M., Wang, X., Saip, A., Osgood, S., Shirey-Rice, J., Kirby, J., & Harris, P. A. (2014). Secondary use of clinical data: The Vanderbilt approach. *Journal of Biomedical Informatics*, *52*, 28–35. https://doi.org/10.1016/j.jbi.2014.02.003

78. Callahan, A., Ashley, E., Datta, S., Desai, P., Ferris, T. A., Fries, J. A., Halaas, M., Langlotz, C. P., Mackey, S., Posada, J. D., Pfeffer, M. A., & Shah, N. H. (2023). The Stanford Medicine data science ecosystem for clinical and translational research. *JAMIA Open*, *6*(3), ooad054. https://doi.org/10.1093/jamiaopen/ooad054

79. Bộ Chính trị. (2024). *Nghị quyết 57-NQ/TW về đột phá phát triển khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số quốc gia* (22/12/2024).

80. Bộ Chính trị. (2025). *Nghị quyết 72-NQ/TW về một số giải pháp đột phá, tăng cường bảo vệ, chăm sóc và nâng cao sức khỏe nhân dân* (9/9/2025).

81. Thủ tướng Chính phủ. (2026). *Quyết định 1308/QĐ-TTg phê duyệt Chiến lược dữ liệu quốc gia giai đoạn 2026–2030, tầm nhìn đến năm 2045* (ban hành 18/7/2026, hiệu lực kể từ ngày ký ban hành).

82. Bộ Y tế. (2026). *Quyết định 3218/QĐ-BYT ban hành Quy chế quản lý, vận hành, sử dụng, khai thác, chia sẻ dữ liệu và bảo đảm an ninh mạng Cổng dữ liệu sức khỏe của Bộ Y tế* (ban hành 14/10/2026, hiệu lực kể từ ngày ký, ban hành).

83. Tran, D. M., Thwaites, C. L., Van Nuil, J. I., McKnight, J., Luu, A. P., Paton, C., & Vietnam ICU Translational Applications Laboratory (VITAL). (2022). Digital health policy and programs for hospital care in Vietnam: Scoping review. *Journal of Medical Internet Research*, *24*(2), e32392. https://doi.org/10.2196/32392

84. Tran, D. M., et al. (2025). Status of digital health technology adoption in 5 Vietnamese hospitals: Cross-sectional assessment. *JMIR Formative Research*, *9*, e53483. https://doi.org/10.2196/53483

85. Trịnh Văn Vinh. (2025). Digital transformation in electronic medical record management towards a smart and sustainable healthcare system. *Vietnam Journal of Community Medicine*, *66*(4), 262–268. https://doi.org/10.52163/yhc.v66i4.2905

86. Pharma Group, KPMG, & Oxford University Clinical Research Unit. (2025). *Roadmap to the future of clinical trials in Vietnam*. https://assets.kpmg.com/content/dam/kpmgsites/vn/pdf/2025/05/roadmap-clinical-trials-in-vietnam-vi.pdf

87. Warnat-Herresthal, S., Schultze, H., Shastry, K. L., Manamohan, S., Mukherjee, S., Garg, V., Sarveswara, R., Händler, K., Pickkers, P., Aziz, N. A., Ktena, S., Tran, F., Bitzer, M., Ossowski, S., Casadei, N., Herr, C., Petersheim, D., Behrends, U., Kern, F., … Schultze, J. L. (2021). Swarm Learning for decentralized and confidential clinical machine learning. *Nature*, *594*(7862), 265–270. https://doi.org/10.1038/s41586-021-03583-3

88. Friedman, C. P., Lomotan, E. A., Richardson, J. E., & Ridgeway, J. L. (2024). Socio-technical infrastructure for a learning health system. *Learning Health Systems*, *8*(1), e10405. https://doi.org/10.1002/lrh2.10405

89. Dayan, I., Roth, H. R., Zhong, A., Harouni, A., Gentili, A., Abidin, A. Z., Liu, A., Costa, A. B., Wood, B. J., Tsai, C.-S., Wang, C.-H., Hsu, C.-N., Lee, C. K., Ruan, P., Xu, D., Wu, D., Huang, E., Kitamura, F. C., … Li, Q. (2021). Federated learning for predicting clinical outcomes in patients with COVID-19. *Nature Medicine*, *27*(10), 1735–1743. https://doi.org/10.1038/s41591-021-01506-3 — **[CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.]**

90. Pati, S., Baid, U., Edwards, B., Sheller, M., Wang, S.-H., Reina, G. A., Foley, P., Gruzdev, A., Karkada, D., Davatzikos, C., Sako, C., Ghodasara, S., Bilello, M., Mohan, S., Vollmuth, P., Brugnara, G., Preetha, C. J., Sahm, F., Maier-Hein, K., … Bakas, S. (2022). Federated learning enables big data for rare cancer boundary detection. *Nature Communications*, *13*, 7346. https://doi.org/10.1038/s41467-022-33407-5

91. Heyndrickx, W., et al. (2024). MELLODDY: Cross-pharma federated learning at unprecedented scale unlocks benefits in QSAR without compromising proprietary information. *Journal of Chemical Information and Modeling*, *64*(7), 2331–2344. https://doi.org/10.1021/acs.jcim.3c00799

92. Bakas, S., Li, X., Shah, P., & Roth, H. R. (2026). Federated learning in healthcare: From research to real-world deployment. *Annual Review of Biomedical Engineering*, *28*, 163–186. https://doi.org/10.1146/annurev-bioeng-080125-041414

93. Walonoski, J., Kramer, M., Nichols, J., Quina, A., Moesel, C., Hall, D., Duffett, C., Dube, K., Gallagher, T., & McLachlan, S. (2018). Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record. *Journal of the American Medical Informatics Association*, *25*(3), 230–238. https://doi.org/10.1093/jamia/ocx079

94. Wagner, Z., & Blacketer, C. (2024). *Evaluating Synthea: Comprehensive analysis of a leading synthesized medical record generator* [Conference poster]. OHDSI Global Symposium 2024, Collaborator Showcase #41. https://www.ohdsi.org/wp-content/uploads/2024/10/41-Wagner-Evaluating_Synthea-Clair-Blacketer.pdf

95. Hao, Y., He, H., & Ho, J. C. (2024). LLMSYN: Generating synthetic electronic health records without patient-level data. In K. Deshpande, M. Fiterau, S. Joshi, Z. C. Lipton, R. Ranganath, & I. Urteaga (Eds.), *Proceedings of the 9th Machine Learning for Healthcare Conference* (Vol. 252, pp. 1–27). PMLR. https://proceedings.mlr.press/v252/hao24a.html — **[CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.]**

96. Chen, X., Wu, Z., Shi, X., Cho, H., & Mukherjee, B. (2025). Generating synthetic electronic health record data: A methodological scoping review with benchmarking on phenotype data and open-source software. *Journal of the American Medical Informatics Association*, *32*(7), 1227–1240. https://doi.org/10.1093/jamia/ocaf082

97. Goldacre, B., & Morley, J. (2022). *Better, broader, safer: Using health data for research and analysis* (The Goldacre Review). UK Department of Health and Social Care.

98. Williamson, E. J., Walker, A. J., Bhaskaran, K., Bacon, S., Bates, C., Morton, C. E., Curtis, H. J., Mehrkar, A., Evans, D., Inglesby, P., Cockburn, J., McDonald, H. I., MacKenna, B., Tomlinson, L., Douglas, I. J., Rentsch, C. T., Mathur, R., Wong, A. Y. S., Grieve, R., … Goldacre, B. (2020). Factors associated with COVID-19-related death using OpenSAFELY. *Nature*, *584*(7821), 430–436. https://doi.org/10.1038/s41586-020-2521-4

99. Friedman, C. P., Rubin, J., Brown, J., Buntin, M., Corn, M., Etheredge, L., Gunter, C., Musen, M., Platt, R., Stead, W., Sullivan, K., & Van Houweling, D. (2015). Toward a science of learning systems: A research agenda for the high-functioning Learning Health System. *Journal of the American Medical Informatics Association*, *22*(1), 43–50. https://doi.org/10.1136/amiajnl-2014-002977

100. Trusted Research and Real-world Utilisation and Sharing Tech (TRUST). (n.d.). *TRUST Platform: Home*. https://www.trustplatform.sg/ — **[CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.]**

101. Ministry of Health and Welfare, Republic of Korea. (n.d.). *Overview of K-CURE Service*. https://k-cure.mohw.go.kr/portal/cmm/htm/engKcureService.do — **[CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.]**

102. Harris, P. A., et al. (2019). The REDCap consortium: Building an international community of software platform partners. *Journal of Biomedical Informatics*, *95*, 103208. https://doi.org/10.1016/j.jbi.2019.103208

103. Lane, J. C. E., Weaver, J., Kostka, K., Duarte-Salles, T., Abrahao, M. T. F., Alghoul, H., Alser, O., Alshammari, T. M., Biedermann, P., Banda, J. M., Burn, E., Casajust, P., Conover, M. M., Culhane, A. C., Davydov, A., DuVall, S. L., Dymshyts, D., Fernandez-Bertolin, S., Fišter, K., … Prieto-Alhambra, D. (2020). Safety of hydroxychloroquine, alone and in combination with azithromycin, in light of rapid wide-spread use for COVID-19: A multinational, network cohort and self-controlled case series study. *The Lancet Rheumatology*, *2*(11), e698–e711. https://doi.org/10.1016/S2665-9913(20)30276-9
