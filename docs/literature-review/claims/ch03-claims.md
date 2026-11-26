# Bản kê nhận định cần bằng chứng: Chương 3 (CDISC, FHIR, OMOP)

**Phiên bản:** 0.1 (đã duyệt cùng Gate 1 v1.1, 26/11/2026; vẫn là bản kê, chưa kiểm chứng nguồn nào) · **Ngày:** 26/11/2026 · **Chương:** `docs/chapters/ch03_standards_cdisc_fhir_omop.md`
**Mục đích:** liệt kê các nhận định của chương có số liệu, phiên bản, quy định, mô tả kỹ thuật hoặc kết luận thực tế, kèm nguồn hiện có và nguồn cần để kiểm. Đây là đầu vào cho Gate 2 và cho bảng bằng chứng của chương.

## Phạm vi đã đọc và giới hạn
- **Đã đọc:** mục 3 (Cơ sở lý thuyết và chuẩn mực ngành, gồm 3.1–3.5) và mục 4 (Nghiên cứu tình huống) của chương, ngày 26/11/2026.
- **Chưa đọc:** mục 1–2 (mục tiêu, bản đồ khái niệm), mục 5 (Lab 3 và script ETL), mục 6 (thảo luận) và các câu quiz. Các khóa `ref_026`, `ref_027`, `ref_093` xuất hiện ở các phần chưa đọc này.
- **Không phải kiểm chứng.** Bản kê chỉ nêu nhận định nào cần nguồn nào; chưa mở nguồn chính thống nào. Cột "Nguồn cần để kiểm" là loại nguồn dự kiến, không phải kết luận rằng nguồn đó xác nhận nhận định.
- Trạng thái trích dẫn lấy từ `references/citation-audit.csv` ngày 26/11/2026. Tất cả khóa của chương đang là `VERIFIED_UNAUDITED`: chưa có khóa nào được audit độc lập.

## Ưu tiên
- **A:** nhận định có phiên bản, ngày, quy định hoặc con số cụ thể, hoặc khẳng định mạnh; sai sẽ làm sai nội dung dạy. Làm trước.
- **B:** mô tả kỹ thuật hoặc nhận định chung cần nguồn; sai sót ít gây hại nhưng vẫn cần dẫn.
- **C:** mô tả khái niệm hoặc ví dụ dễ kiểm.

## Bảng nhận định

| ID | Mục | Nhận định (tóm tắt trung thành) | Loại | Trích dẫn hiện có (trạng thái) | Nguồn cần để kiểm | Ưu tiên |
|---|---|---|---|---|---|---|
| C3-01 | 3.1 | Dữ liệu y tế được thu thập bởi "hàng nghìn" hệ thống phần mềm độc quyền | số lượng mơ hồ | không có | khảo sát hoặc thống kê thị trường hệ thống thông tin y tế; hoặc viết lại không nêu số | B |
| C3-02 | 3.1 | Hai cấp bất đồng: cấu trúc (SQL, JSON, DICOM, XML) và ngữ nghĩa (ICD-10, viết tắt, mã nội bộ, LOINC) | khái niệm | không có | tài liệu định nghĩa các mức liên thông (ví dụ HL7, IEEE) | C |
| C3-03 | 3.1 | Thiếu chuẩn mở thì chi phí tích hợp và phân tích đa trung tâm "tăng theo cấp số nhân" | khẳng định định lượng | không có | không có nguồn; nên bỏ "cấp số nhân" hoặc dẫn nghiên cứu chi phí liên thông | A |
| C3-04 | 3.2 | CDISC là hiệp hội cung cấp các mô hình và hướng dẫn dùng trong nghiên cứu lâm sàng | định nghĩa | không có | trang tổ chức CDISC | C |
| C3-05 | 3.2 | Yêu cầu định dạng khi nộp hồ sơ phụ thuộc loại hồ sơ, cơ quan tiếp nhận và hướng dẫn hiện hành | quy định (đã rào đón) | không có | hướng dẫn kỹ thuật dữ liệu nghiên cứu của FDA, hướng dẫn của PMDA, catalog chuẩn tương ứng | A |
| C3-06 | 3.2.1 | SDTM tổ chức dữ liệu thành các miền (domain); các lớp: Special-Purpose, Interventions, Events, Findings, Findings About | cấu trúc chuẩn, theo phiên bản | không có | SDTM và SDTMIG của CDISC (ghi rõ phiên bản) | A |
| C3-07 | 3.2.1 | DM là miền special-purpose; AE là Events; VS và LB là Findings; CM là Interventions | cấu trúc chuẩn | không có | SDTMIG (phiên bản áp dụng) | A |
| C3-08 | 3.2.1 | `STUDYID`, `USUBJID`, `DOMAIN` là biến định danh thường dùng; cách ghép `USUBJID` do đặc tả nghiên cứu quy định | cấu trúc chuẩn | không có | SDTMIG | B |
| C3-09 | 3.2.1 | `--SEQ` không bắt buộc cho mọi miền (DM không dùng); `--TESTCD` và `--TEST` thuộc nhóm Findings | cấu trúc chuẩn | không có; có cờ `[CẦN KIỂM CHỨNG: phiên bản IG]` | SDTMIG | A |
| C3-10 | 3.2.2 | ADaM phục vụ phân tích thống kê, thêm biến phái sinh; `ADSL` có một dòng cho mỗi đối tượng | cấu trúc chuẩn | không có | ADaM và ADaMIG của CDISC | B |
| C3-11 | 3.3 | FHIR ra đời để khắc phục sự cồng kềnh, khó triển khai của HL7 v2 và v3 | lịch sử, thiết kế | `ref_009` (`VERIFIED_UNAUDITED`; mục tham khảo là trang đặc tả "FHIR") | trang tổng quan FHIR và bài mô tả nguồn gốc FHIR | B |
| C3-12 | 3.3.1 | FHIR dựa trên HTTP, RESTful API, định dạng JSON hoặc XML | mô tả kỹ thuật | không có | đặc tả FHIR | C |
| C3-13 | 3.3.1 | "Hiện có hơn 150 tài nguyên chuẩn" | con số, theo phiên bản | không có | danh mục tài nguyên của từng phiên bản FHIR (R4, R5) | A |
| C3-14 | 3.3.1 | Ví dụ tài nguyên: `Patient`, `Encounter`, `Condition`, `Observation`, `MedicationRequest` | mô tả kỹ thuật | không có | đặc tả FHIR | C |
| C3-15 | 3.3.1 | FHIR cho phép mở rộng và hồ sơ hóa; không dùng tỷ lệ 80/20 như định lượng phổ quát | mô tả kỹ thuật | không có; có cờ `[CẦN KIỂM CHỨNG]` | đặc tả FHIR (extensibility, profiling) | B |
| C3-16 | 3.3.2 | R4 (4.0.1, 2019) có các tài nguyên cốt lõi ở mức Normative và "là tiêu chuẩn thực tế trong hầu hết các hệ thống bệnh viện trên thế giới" | phiên bản và khẳng định mạnh | không có | trang phát hành R4 của HL7; khảo sát mức độ áp dụng. Vế "hầu hết trên thế giới" nhiều khả năng cần giảm nhẹ | A |
| C3-17 | 3.3.2 | R5 (5.0.0) ban hành ngày 26/03/2023 | ngày phát hành | không có (chỉ trỏ phụ lục) | lịch sử phát hành trên hl7.org/fhir | A |
| C3-18 | 3.3.2 | Trạng thái R6 thay đổi theo lịch HL7; mô tả R6 giữ `CONTENT_PENDING` | trạng thái phát hành | không có; cờ `CONTENT_PENDING` | hl7.org/fhir (ballot, lịch phát hành), ngày kiểm | A |
| C3-19 | 3.3.3 | SMART on FHIR là khung ủy quyền OAuth2 cho ứng dụng bên thứ ba tích hợp vào EHR mà không đổi mã lõi | mô tả kỹ thuật | `ref_036` (`VERIFIED_UNAUDITED`) | bài gốc SMART on FHIR (toàn văn) và đặc tả SMART App Launch | B |
| C3-20 | 3.3.3 | FHIR Bulk Data API cho phép trích xuất dữ liệu hàng loạt ở quy mô quần thể | mô tả kỹ thuật | `ref_037` (`VERIFIED_UNAUDITED`; kiểm trang: tiêu đề `PARTIAL`, thiếu chữ "Application Programming Interface" trong bản ghi) | bài gốc và đặc tả Bulk Data Access | B |
| C3-21 | 3.4 | OMOP CDM do cộng đồng OHDSI quản lý và phát triển | mô tả tổ chức | `ref_011`, `ref_038`. **Mâu thuẫn:** văn bản nói `ref_011` giữ `BIB_PENDING`, nhưng sổ ghi `VERIFIED_UNAUDITED`, và kiểm trang chưa kiểm được | trang OHDSI, bài Hripcsak 2015; đối chiếu lại `ref_011` | A |
| C3-22 | 3.4.1 | Chương dùng CDM v5.4 làm minh họa; phiên bản và mốc phát hành chốt theo đặc tả OMOP | phiên bản | không có (có liên kết đặc tả) | trang đặc tả CDM v5.4 | A |
| C3-23 | 3.4.1 | Mô tả các bảng và cột: `person`, `observation_period`, `visit_occurrence`, `condition_occurrence`, `drug_exposure` (`days_supply`, `dose_unit_source_value`), `measurement` | cấu trúc chuẩn, theo phiên bản | không có; có cảnh báo "đối chiếu đúng phiên bản trước khi ETL" | đặc tả OMOP CDM v5.4, từng bảng và cột | A |
| C3-24 | 3.4.2 | Mã địa phương được ánh xạ về khái niệm chuẩn: chẩn đoán về SNOMED CT; thuốc về RxNorm hoặc RxNorm Extension; xét nghiệm về LOINC | quy tắc từ vựng | không có | tài liệu từ vựng chuẩn hóa OMOP (The Book of OHDSI, ATHENA) | A |
| C3-25 | 3.4.3 | OHDSI gửi mã phân tích đến các cơ sở, mỗi nơi chạy cục bộ; chỉ kết quả được phép chia sẻ mới gửi về; không mặc định kết quả không thể nhận dạng; `ref_039` chỉ dùng cho kiểm định CDM | mô tả mô hình (đã rào đón) | `ref_039` (`VERIFIED_UNAUDITED`), `ref_038` | The Book of OHDSI (nghiên cứu mạng lưới), tài liệu kiểm soát tiết lộ | B |
| C3-26 | 3.4.3 | LEGEND-HTN là ví dụ có trích dẫn; cỡ mẫu và mô tả triển khai chỉ dùng sau khi đọc bài gốc | ví dụ (đã rào đón) | `ref_040` (`VERIFIED_UNAUDITED`); cờ `[CẦN KIỂM CHỨNG]` | bài Suchard 2019 (toàn văn) | B |
| C3-27 | 3.5 | Mục đích CDISC: nộp hồ sơ nghiên cứu lâm sàng cho cơ quan quản lý (FDA, PMDA) | quy định | không có | hướng dẫn của FDA và PMDA về dữ liệu nộp theo chuẩn | A |
| C3-28 | 3.5 | Định dạng: CDISC dùng XPT (SAS Transport v5), Dataset-XML, JSON; FHIR dùng JSON, XML, Turtle; OMOP dùng PostgreSQL, SQL Server, BigQuery, Oracle | mô tả kỹ thuật | không có | tài liệu từng chuẩn | B |
| C3-29 | 3.5 | Từ vựng: CDISC dùng CDISC CT, MedDRA, WHODrug; FHIR ràng buộc qua ValueSets (SNOMED, LOINC, ICD-10); OMOP bắt buộc ánh xạ về Standard Concepts | mô tả kỹ thuật | không có | tài liệu từng chuẩn | B |
| C3-30 | 3.5 | Có hướng dẫn ánh xạ FHIR sang CDISC; OMOP nhận dữ liệu từ nhiều nguồn sau ETL | tương thích | `ref_034`, `ref_010` (`VERIFIED_UNAUDITED`; hai mục là tài liệu hướng dẫn triển khai) | hai hướng dẫn triển khai (toàn văn) | B |
| C3-31 | 3.5 | Nên hỏi "dữ liệu phục vụ mục đích gì": FHIR cho kết nối EHR thời gian thực, CDISC cho hồ sơ thuốc mới, OMOP cho phân tích đa cơ sở | luận điểm của tác giả | không có | tổng quan về liên thông và các chuẩn; nếu không có thì ghi rõ đây là tổng hợp của tác giả | A |
| C3-32 | 4 | Tình huống 1: viện châu Âu lưu toàn bộ dữ liệu dưới dạng FHIR JSON, truy vấn tra cứu tốt nhưng phân tích tốn chi phí; khắc phục bằng ETL sang OMOP | kịch bản | không có; có câu "hiệu năng thực tế phải đo trên dữ liệu cụ thể" | không phải sự kiện có nguồn: gắn nhãn minh họa, hoặc thay bằng ca có nguồn | A |
| C3-33 | 4 | Tình huống 2: ba bệnh viện mã hóa khác nhau biến "tình trạng hút thuốc", gộp không qua từ điển chuẩn thì phân loại sai | kịch bản | không có | như C3-32 | A |
| C3-34 | 4 | Dùng SNOMED CT và quy tắc ánh xạ OMOP/CDISC là biện pháp "sống còn" ngăn sai lệch | khẳng định mạnh | không có | nguồn về trôi dạt ngữ nghĩa khi ánh xạ; hoặc giảm nhẹ "sống còn" | B |

## Tổng hợp
- **34 nhận định** (đếm từ bảng bằng script ngày 26/11/2026). Ưu tiên A: 17 (C3-03, 05, 06, 07, 09, 13, 16, 17, 18, 21, 22, 23, 24, 27, 31, 32, 33). Ưu tiên B: 13 (C3-01, 08, 10, 11, 15, 19, 20, 25, 26, 28, 29, 30, 34). Ưu tiên C: 4 (C3-02, 04, 12, 14).
- **27 trong 34 nhận định không có trích dẫn nào** gắn trực tiếp; 7 nhận định có khóa trích dẫn (C3-11, 19, 20, 21, 25, 26, 30).
- **Không có trích dẫn nào cho toàn bộ mục 3.2 (CDISC).** Mọi mô tả SDTM và ADaM ở C3-04 đến C3-10 hiện không được dẫn nguồn nào, trong khi chúng phụ thuộc phiên bản của SDTMIG và ADaMIG.
- **Chương dựa nhiều vào phụ lục chuẩn thay vì nguồn gốc.** C3-13, C3-17, C3-22, C3-23 trỏ về `docs/appendices/standards.md`; phụ lục đó cần được xác minh từ nguồn chính thống.
- **Mâu thuẫn giữa văn bản và sổ:** `ref_011` (C3-21).
- **Hai kịch bản (C3-32, C3-33)** được trình bày như tình huống thật nhưng không có nguồn; theo quy tắc minh bạch nguồn gốc cần gắn nhãn minh họa.

## Việc kế tiếp
1. Ben duyệt bản kê này và các câu hỏi nghiên cứu của chương 3 trong giao thức v1.1.
2. Lập sổ nguồn chính thống cho các nhận định loại "chuẩn và phiên bản" (C3-05, 06, 07, 09, 10, 13, 16, 17, 18, 22, 23, 24, 27, 28, 29): các nguồn này đọc trực tiếp ở CDISC, HL7, OHDSI, FDA, PMDA, không tìm qua API học thuật.
3. Các nhận định dạng mô tả có trích dẫn (C3-11, 19, 20, 21, 25, 26, 30) đi vào Gate 2 và đọc toàn văn.
