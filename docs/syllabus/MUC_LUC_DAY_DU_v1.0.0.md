# Mục lục đầy đủ của sách chuyên khảo Biomedical RDM

**Tác giả sách:** TS. Hoàng Quang Huy (Ben) · **Phiên bản:** 1.0.0 (dự thảo để duyệt) · **Ngày:** 26/11/2026
**Sinh từ:** `main` ở `69fc2ee`: `docs/syllabus/MONOGRAPH_OUTLINE_v1.0.0.md`, `editorial/chapter-map.yml`, tiêu đề các tệp trong `docs/chapters/` và `docs/appendices/`.
**Quy ước:** số chương là số chính thức theo `MONOGRAPH_OUTLINE_v1.0.0.md`; "Mã hiện tại" là tên tệp chương hiện có trong repo. Tiêu đề mục con **giữ nguyên như trong tệp chương** (chưa chỉnh), nên các chương 2–6 còn theo cấu trúc cũ và sẽ đổi theo khung 11 mục khi nâng cấp. Chương 7, 8, 9 và Lời nói đầu chưa được viết: chỉ ghi phạm vi đã chốt, không bịa mục con.

## 1. Tổng quan cấu trúc

| Phần | Chương | Mã hiện tại | Số từ hiện tại | Trạng thái |
|---|---|---|---:|---|
| (Mở đầu) | Lời nói đầu và hướng dẫn đọc | viết mới | — | cần viết |
| I. Nền tảng | 1. Tổng quan RDM, vòng đời và DMP | ch01 | 6529 | chương mẫu (khung 11 mục) |
| II. Thu thập dữ liệu | 2. Thu thập dữ liệu lâm sàng, ALCOA+ và REDCap | ch02 | 8490 | bản nháp, cần nâng cấp |
| III. Chuẩn và chất lượng | 3. CDISC, FHIR và OMOP | ch03 | 5935 | bản nháp, cần nâng cấp |
|  | 4. Chất lượng dữ liệu và dữ liệu khuyết | ch04 | 4897 | bản nháp, cần nâng cấp |
| IV. Bảo mật, chia sẻ và tái lập | 5. Bảo mật và khử định danh | ch05 | 5972 | bản nháp, cần nâng cấp |
|  | 6. FAIR, kho lưu trữ và dữ liệu sẵn sàng cho AI | ch06 | 5301 | bản nháp, cần nâng cấp |
| | 7. Tái lập và phần mềm nghiên cứu | chưa có tệp | — | mới; cần nghiên cứu |
| V. Quản trị và pháp lý | 8. Quản trị và pháp lý Việt Nam | chưa có tệp | — | mới; cần nghiên cứu và reviewer pháp lý |
| VI. Tích hợp | 9. Tích hợp và tổng kết | chưa có tệp (phần capstone nằm ở ch07 cũ, học liệu đi kèm) | — | cần viết |
| Phụ lục | Phụ lục A–… (mục 4 dưới đây) | `docs/appendices/` | — | giữ; phần dễ lỗi thời sẽ chuyển vào Sổ cập nhật |

**Thứ tự đọc khuyến nghị:** 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9. **Tiên quyết:** 1: không; 2: 1; 3: 1, 2; 4: 1–3; 5: 1, 2; 6: 1, 3, 5; 7: 1, 4, 6 (dự kiến); 8: 5, 6 (dự kiến); 9: 1–8.

## 2. Mục lục chi tiết

### Lời nói đầu và hướng dẫn đọc

Chưa viết. `ch00_getting_started.md` hiện là trang M0 của khóa học (sản phẩm đi kèm), không thuộc sách.

### Chương 1. Tổng quan RDM, vòng đời và DMP

Tệp: `docs/chapters/ch01_overview_and_dmp.md` · 6529 từ · chương mẫu (khung 11 mục)

- 1. TÓM TẮT CHƯƠNG VÀ CÁC LUẬN ĐIỂM CHÍNH
  - Luận điểm cần tác giả xác nhận
- 2. PHẠM VI, GIẢ ĐỊNH VÀ ĐỐI TƯỢNG
  - Mục tiêu học tập và khung năng lực (Learning Objectives)
- 3. NỀN TẢNG KHÁI NIỆM
- 4. NỘI DUNG CỐT LÕI
  - 4.1. Khủng hoảng khả năng tái lập và sự ra đời của RDM y sinh
  - 4.2. Vòng đời dữ liệu y sinh & Nguyên lý khuếch đại lỗi thượng nguồn
  - 4.3. Khung Quản trị Dữ liệu Y tế (Data Governance Frameworks)
  - 4.4. Chuyên nghiệp hóa nhân lực: Mô hình 3 hồ sơ Data Steward [@ref_017]
  - 4.5. Kế hoạch Quản lý và Chia sẻ Dữ liệu (DMP / DMSP)
- 5. BẢNG BẰNG CHỨNG
- 6. VÍ DỤ VÀ CASE STUDY
  - Case Study minh họa: Sự việc rút bài liên quan đến cơ sở dữ liệu Surgisphere (2020)
- 7. THỰC HÀNH (LAB 1 DMPTOOL, TÙY CHỌN)
  - Bài thực hành tự chọn: Soạn thảo DMSP chuẩn NIH trên DMPTool
- 8. CẠM BẪY VÀ THỰC HÀNH TỐT
- 9. GIỚI HẠN VÀ VẤN ĐỀ MỞ
- 10. TÓM TẮT, CÂU HỎI TỰ KIỂM TRA VÀ THẢO LUẬN
- Quiz tự kiểm tra — Bài 1 (5 câu hỏi)
  - Câu hỏi thảo luận tình huống
- 11. THUẬT NGỮ MỚI VÀ TÀI LIỆU THAM KHẢO

### Chương 2. Thu thập dữ liệu lâm sàng, ALCOA+ và REDCap

Tệp: `docs/chapters/ch02_collection_and_redcap.md` · 8490 từ · bản nháp, cần nâng cấp

- 1. MỤC TIÊU HỌC TẬP VÀ KHUNG NĂNG LỰC (LEARNING OBJECTIVES)
- 2. BẢN ĐỒ KHÁI NIỆM (CONCEPT MAP)
- 3. CƠ SỞ LÝ THUYẾT VÀ CHUẨN MỰC NGÀNH
  - 3.1. Khủng hoảng toàn vẹn dữ liệu tại nguồn và Sự sụp đổ của "Văn hóa Bảng tính"
  - 3.2. Khung toàn vẹn dữ liệu: ALCOA, ALCOA+ và ALCOA++
  - 3.3. Các Chuẩn mực Quốc tế Điều chỉnh Hoạt động Thu thập Dữ liệu
  - 3.4. Hệ thống Thu thập Dữ liệu Điện tử (EDC) và Nền tảng REDCap
- 4. NGHIÊN CỨU TÌNH HUỐNG VÀ BÀI HỌC THẤT BẠI (FAILURE ANALYSIS)
  - Case Study 1: Tình huống giả định minh họa — rủi ro bảng tính Excel
  - Case Study 2: Tình huống giả định minh họa — tài khoản và audit trail
- Quiz tự kiểm tra — Bài 2 (4 câu hỏi)
- 5. HƯỚNG DẪN THỰC HÀNH PHÒNG MÁY - LAB TÙY CHỌN
  - 5.1. Bối cảnh Nghiên cứu và Đề bài
  - 5.2. Các Bước Triển Khai Chi Tiết
  - 5.3. Mẫu Tệp Dữ Liệu Từ Điển Cốt Lõi (Raw CSV Snippet)
  - 5.4. Rubric Tự Đánh Giá Kết Quả Thực Hành Lab (Thang điểm 20)
- 6. CÂU HỎI THẢO LUẬN VÀ BÀI TẬP TÌNH HUỐNG (DISCUSSION & EXERCISES)
  - 6.1. Câu hỏi Thảo luận trên Lớp
  - 6.2. Bài tập Tình huống Nâng cao (Mini-Case Study)
- 7. TÀI LIỆU THAM KHẢO CHUẨN (REFERENCES)

### Chương 3. CDISC, FHIR và OMOP

Tệp: `docs/chapters/ch03_standards_cdisc_fhir_omop.md` · 5935 từ · bản nháp, cần nâng cấp

- 1. MỤC TIÊU HỌC TẬP VÀ KHUNG NĂNG LỰC (LEARNING OBJECTIVES)
- 2. BẢN ĐỒ KHÁI NIỆM (CONCEPT MAP)
- 3. CƠ SỞ LÝ THUYẾT VÀ CHUẨN MỰC NGÀNH
  - 3.1. Thách thức phân mảnh và Bất đồng Ngữ nghĩa trong Y tế
  - 3.2. CDISC: Chuẩn mực Đệ trình Nghiên cứu Lâm sàng Quy chuẩn
  - 3.3. HL7 FHIR: Chuẩn mực Trao đổi Dữ liệu Lâm sàng Thế hệ Mới
  - 3.4. OMOP CDM và Mạng lưới OHDSI: Chuẩn hóa Phân tích Dữ liệu Thế giới thực
  - 3.5. Ma trận So sánh Ba Chuẩn và Tính Bổ trợ Lẫn nhau
- 4. NGHIÊN CỨU TÌNH HUỐNG VÀ BÀI HỌC THẤT BẠI (FAILURE ANALYSIS)
  - Case Study 1: Tình huống giả định minh họa — sai lầm khi ép một chuẩn làm nhiệm vụ không phù hợp
  - Case Study 2: Tình huống giả định minh họa — trôi dạt ngữ nghĩa (Semantic Drift) khi ánh xạ không chuẩn
- Quiz tự kiểm tra — Bài 3 (5 câu hỏi)
- 5. HƯỚNG DẪN THỰC HÀNH PHÒNG MÁY - LAB 3 (2 GIỜ)
  - 5.1. Bối cảnh Nghiên cứu và Đề bài
  - 5.2. Cấu trúc Dữ liệu Đầu vào (Sample FHIR JSON Bundle)
  - 5.3. Bảng Ánh xạ Đối chiếu Cấu trúc (Mapping Specification)
  - 5.4. Script Python Thực hành Chuyển đổi (ETL Script)
  - 5.5. Rubric Tự Đánh Giá Kết Quả Thực Hành Lab 3 (Thang điểm 20)
- 6. CÂU HỎI THẢO LUẬN VÀ BÀI TẬP TÌNH HUỐNG (DISCUSSION & EXERCISES)
  - 6.1. Câu hỏi Thảo luận trên Lớp
  - 6.2. Bài tập Tình huống Nâng cao (Real-World Pipeline Challenge)
- 7. TÀI LIỆU THAM KHẢO CHUẨN (REFERENCES)

### Chương 4. Chất lượng dữ liệu và dữ liệu khuyết

Tệp: `docs/chapters/ch04_quality_and_imputation.md` · 4897 từ · bản nháp, cần nâng cấp

- 1. MỤC TIÊU HỌC TẬP (LEARNING OUTCOMES)
- 2. BẢN ĐỒ KHÁI NIỆM (CONCEPT MAP)
- 3. LÝ THUYẾT (THEORY)
  - 3.1. Các Chiều Chất Lượng Dữ liệu EHR — Weiskopf & Weng (2013)
  - 3.2. Khung Đánh giá Chất lượng Dữ liệu Kahn et al. (2016) — 3 Trục
  - 3.3. OHDSI Data Quality Dashboard (DQD)
  - 3.4. Phân loại Cơ chế Dữ liệu Khuyết — Rubin (1976)
  - 3.5. Multiple Imputation by Chained Equations (MICE)
- 4. TÌNH HUỐNG THỰC TẾ (CASE STUDY 1)
- 5. THỰC HÀNH (LAB 4) — TÙY CHỌN
  - 5.1. Mục tiêu Lab
  - 5.2. Cài đặt Môi trường
  - 5.3. Script Python — Phân tích Chất lượng Dữ liệu & MICE Đúng Chuẩn
  - 5.4. Checklist Tự Đánh Giá (không chấm điểm)
- 6. CÂU HỎI THẢO LUẬN VÀ BÀI TẬP TÌNH HUỐNG
  - 6.1. Câu hỏi Thảo luận
  - 6.2. Bài tập Tình huống Nâng cao (Clinical Audit Scenario)
- 7. TÓM TẮT TRỌNG TÂM (KEY TAKEAWAYS)
- Quiz tự kiểm tra — Bài 4 (5 câu hỏi)
- 9. TÀI LIỆU THAM KHẢO (REFERENCES)

### Chương 5. Bảo mật và khử định danh

Tệp: `docs/chapters/ch05_privacy_and_deidentification.md` · 5972 từ · bản nháp, cần nâng cấp

- 1. MỤC TIÊU HỌC TẬP VÀ KHUNG NĂNG LỰC (LEARNING OBJECTIVES)
- 2. BẢN ĐỒ KHÁI NIỆM (CONCEPT MAP)
- 3. CƠ SỞ LÝ THUYẾT VÀ CHUẨN MỰC NGÀNH
  - 3.1. Nghịch lý Bảo mật và Chia sẻ Dữ liệu Y sinh học
  - 3.2. Khung Pháp lý Quốc tế về Dữ liệu Y tế
  - 3.3. Khung Pháp lý và Đạo đức Nghiên cứu Y tế tại Việt Nam
  - 3.4. Các Mô hình Kỹ thuật Khử định danh và Ẩn danh Toán học
  - 3.5. Kiến trúc Môi trường Nghiên cứu Tin cậy (TREs) và Khung Five Safes
- 4. NGHIÊN CỨU TÌNH HUỐNG VÀ BÀI HỌC THẤT BẠI (FAILURE ANALYSIS)
  - Case Study 1: Minh họa tấn công liên kết
  - Case Study 2: Tình huống giả định minh họa về chia sẻ dữ liệu
- Quiz tự kiểm tra — Bài 5 (4 câu hỏi)
- 5. HƯỚNG DẪN THỰC HÀNH PHÒNG MÁY - LAB 5 (2 GIỜ)
  - 5.1. Bối cảnh Nghiên cứu và Đề bài
  - 5.2. Mẫu Dữ Liệu Lâm Sàng Thô Định Danh (`csu_raw_identifiable_lab5.csv`)
  - 5.3. Script Python Đường Ống Khử Định Danh (`deidentify_csu_lab5.py`)
  - 5.4. Rubric tự đối chiếu kết quả thực hành Lab 5 (20 điểm)
- 6. CÂU HỎI THẢO LUẬN VÀ BÀI TẬP TÌNH HUỐNG (DISCUSSION & EXERCISES)
  - 6.1. Câu hỏi Thảo luận trên Lớp
  - 6.2. Bài tập Tình huống Nâng cao (Hospital Data Governance Audit)
- 7. TÀI LIỆU THAM KHẢO CHUẨN (REFERENCES)

### Chương 6. FAIR, kho lưu trữ và dữ liệu sẵn sàng cho AI

Tệp: `docs/chapters/ch06_fair_and_ai_ready.md` · 5301 từ · bản nháp, cần nâng cấp

- 1. MỤC TIÊU HỌC TẬP (LEARNING OUTCOMES)
- 2. BẢN ĐỒ KHÁI NIỆM (CONCEPT MAP)
- 3. CƠ SỞ LÝ THUYẾT
  - 3.1. Nguyên tắc FAIR trong Nghiên cứu Y Sinh học
  - 3.2. Phân biệt FAIR Data và Open Data trong Y tế
  - 3.3. Quy trình FAIRification 7 bước (Jacobsen et al. 2020)
  - 3.4. Hệ sinh thái Kho lưu trữ Dữ liệu Số Y Sinh học
  - 3.5. Chuẩn Đóng gói Đối tượng Nghiên cứu: RO-Crate
  - 3.6. Dữ liệu Sẵn sàng cho AI (AI-Ready Datasets)
- 4. NGHIÊN CỨU TÌNH HUỐNG (CASE STUDIES)
  - Case Study 1: Thảm họa Rò rỉ Dữ liệu (Data Leakage) trong Chẩn đoán X-quang Phổi
  - Case Study 2: Dữ liệu AI thiếu Đa dạng (Dataset Bias) trong Nhận diện Melanoma
- 5. THỰC HÀNH (LAB 6) — TÙY CHỌN
  - 5.1. Bối cảnh và Nhiệm vụ
  - 5.2. Cấu trúc Thư mục Gói Dữ liệu (RO-Crate)
  - 5.3. Tệp Siêu dữ liệu Máy đọc được (`ro-crate-metadata.json`)
  - 5.4. Script Python Phân chia Dữ liệu An toàn cho AI (`train_test_split_safe.py`)
  - 5.5. Các Bước Xuất bản trên Zenodo Sandbox
  - 5.6. Checklist Tự Đánh Giá (không chấm điểm)
- 6. CÂU HỎI THẢO LUẬN VÀ BÀI TẬP TÌNH HUỐNG
  - 6.1. Câu hỏi Thảo luận
  - 6.2. Bài tập Tình huống Nâng cao (Capstone Checklist)
- 7. TÓM TẮT TRỌNG TÂM (KEY TAKEAWAYS)
- Quiz tự kiểm tra — Bài 6 (6 câu hỏi)
- 9. TÀI LIỆU THAM KHẢO (REFERENCES)

### Chương 7. Tái lập và phần mềm nghiên cứu (chưa viết)

Phạm vi đã chốt: thực hành tái lập tính toán (môi trường, phiên bản, quy trình, mã nguồn). Chương 1 chỉ giữ động lực; cần chốt phạm vi để không chồng lấp chương 4 và 6. Mục con chưa lập.

### Chương 8. Quản trị và pháp lý Việt Nam (chưa viết)

Phạm vi đã chốt: khung pháp lý và quản trị dữ liệu y tế tại Việt Nam; đi từ văn bản chính thống; tách nguyên lý cố định và Sổ cập nhật; phần pháp lý Việt Nam của chương 5 (mục 3.2–3.3) sẽ chuyển sang chương này; cần reviewer pháp lý. Mục con chưa lập.

### Chương 9. Tích hợp và tổng kết (chưa viết)

Phạm vi đã chốt: một bài toán tích hợp từ thiết kế đến chia sẻ, bám khung vòng đời bảy giai đoạn. Quiz tổng hợp và capstone nằm ở học liệu đi kèm, không ở chương này. Mục con chưa lập.

## 3. Học liệu đi kèm (không thuộc mục lục sách)

- Trang M0 của khóa học: `docs/chapters/ch00_getting_started.md`.
- Quiz tổng hợp và checklist capstone: phần của `docs/chapters/ch07_completion_and_capstone.md` (mã cũ; chương sách tương ứng là chương 9 viết mới).
- Quiz theo chương, mini-course 6 bài, đề cương khóa học `docs/syllabus/BIOMEDICAL_RDM_FREE_SELF_PACED_SYLLABUS.md`.

## 4. Phụ lục

| Phụ lục | Tệp | Tiêu đề trong tệp |
|---|---|---|
| case-study-drmayday | `docs/appendices/case-study-drmayday.md` | Phụ lục: Case Study — Quản trị dữ liệu cho dự án DrMayDay (mày đay, Bệnh viện Da liễu Trung ương) |
| fhir-omop-lab-notes | `docs/appendices/fhir-omop-lab-notes.md` | Ghi chú lab FHIR–OMOP cho chương 3 |
| funder-templates | `docs/appendices/funder-templates.md` | Phụ lục cập nhật: Yêu cầu và mẫu nhà tài trợ |
| legal | `docs/appendices/legal.md` | Phụ lục cập nhật: Pháp lý và định hướng chính sách |
| privacy-lab-notes | `docs/appendices/privacy-lab-notes.md` | Ghi chú Lab 5: khử định danh minh họa |
| quality-ai-lab-notes | `docs/appendices/quality-ai-lab-notes.md` | Ghi chú Lab 4 và Lab 6: chất lượng, FAIR và AI |
| redcap-lab-notes | `docs/appendices/redcap-lab-notes.md` | Ghi chú lab REDCap |
| retention | `docs/appendices/retention.md` | Phụ lục cập nhật: Thời hạn lưu trữ |
| standards | `docs/appendices/standards.md` | Phụ lục cập nhật: Chuẩn, công cụ và kho |

Ngoài ra: nhật ký thay đổi phụ lục `docs/appendices/appendices-CHANGELOG.md`; thuật ngữ `editorial/glossary.yml`; ký hiệu `editorial/notation.md`; sổ kiểm chứng pháp lý `docs/legal-verification.md`.

## 5. Danh mục tài liệu tham khảo

Xem `references/DANH_MUC_THAM_KHAO_v1.0.0.md` (sinh cùng lượt với tệp này).
