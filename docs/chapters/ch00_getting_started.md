# MODULE 0. BẮT ĐẦU Ở ĐÂY: HƯỚNG DẪN TỰ HỌC & NGUYÊN TẮC CỐT LÕI

> **Tên khóa học:** Quản lý dữ liệu nghiên cứu y sinh (Biomedical Research Data Management - BioRDM)  
> **Hình thức:** Khóa học mở miễn phí, tự học theo nhịp (Free, Self-paced)  
> **Thời gian đọc:** Khoảng 15 phút  
> **Tác giả:** TS. Hoàng Quang Huy (Đại học Bách khoa Hà Nội, iBME Lab)

---

## 1. KHÓA HỌC NÀY HOẠT ĐỘNG NHƯ THẾ NÀO?

Chào mừng bạn đến với khóa học **Quản lý dữ liệu nghiên cứu y sinh (Biomedical RDM)**! Khóa học này được thiết kế dành cho sinh viên kỹ thuật y sinh, công nghệ thông tin y tế, các bác sĩ lâm sàng, điều phối viên nghiên cứu (CRC/CRA) và nhà khoa học dữ liệu mong muốn làm chủ kỹ năng quản trị dữ liệu nghiên cứu chuẩn quốc tế.

### Ba nguyên tắc tự học:
1. **Mở là học ngay, không cần chờ đợi:** Toàn bộ 6 module lý thuyết, 6 bài lab thực hành và các câu hỏi kiểm tra đều mở sẵn. Bạn có thể học tuần tự từ M0 đến M6 (khuyến nghị) hoặc truy cập trực tiếp vào chủ đề bạn đang cần giải quyết trong nghiên cứu của mình.
2. **Không áp lực điểm số:** Không có hạn nộp bài, không có điểm danh hay xếp loại qua/trượt. Các câu hỏi trắc nghiệm sau mỗi bài học cung cấp ngay đáp án đúng và phần giải thích khoa học chi tiết để bạn tự củng cố tri thức.
3. **Thực hành theo năng lực:** Các bài thực hành phòng máy (Labs) được thiết kế từ mức độ cơ bản (dùng công cụ web như DMPTool, giao diện REDCap) đến nâng cao (script Python/R trong Lab 4, 5, 6). Bạn có thể lựa chọn làm toàn bộ hoặc bỏ qua phần lập trình nếu chỉ tập trung vào vai trò quản lý chính sách.

---

## 2. XƯƠNG SỐNG QUY TRÌNH: WORKFLOW 7 GIAI ĐOẠN

Toàn bộ nội dung khóa học vận hành xoay quanh **vòng đời 7 giai đoạn** của dữ liệu y sinh:

```
1. Thiết kế & DMP ➔ 2. Thu thập dữ liệu (ALCOA+/EDC) ➔ 3. Làm sạch & Đánh giá chất lượng
➔ 4. Chuẩn hóa (CDISC / FHIR / OMOP) ➔ 5. FAIR & Chia sẻ kho lưu trữ
➔ 6. Bảo mật & Pháp lý (Luật 91/2025/QH15) ➔ 7. Kết thúc: Lưu trữ dài hạn & Hủy an toàn
```

Quy trình này phản ánh tư duy quản trị dữ liệu chủ động: **"Quyết định ở thượng nguồn càng sớm thì chi phí khắc phục ở hạ nguồn càng thấp"**. Một bản Kế hoạch Quản lý Dữ liệu (DMP) tốt ngay từ khâu viết đề cương sẽ giúp bạn tránh được thảm họa mất dữ liệu, bị từ chối bài báo hoặc vi phạm pháp luật bảo vệ quyền riêng tư người bệnh.

---

## 3. NGUYÊN TẮC ĐẠO ĐỨC & QUYỀN RIÊNG TƯ: NGUỒN DỮ LIỆU TRONG KHÓA HỌC

Trong nghiên cứu y sinh, dữ liệu luôn gắn liền với con người và sự tin tưởng của người bệnh. Khóa học tuân thủ tuyệt đối các nguyên tắc an toàn dữ liệu:

* **Không sử dụng dữ liệu bệnh nhân thật (Zero PII):** Tuyệt đối không có bất kỳ thông tin nhận dạng cá nhân hoặc dữ liệu bệnh án thật nào trong các bài tập và ví dụ của khóa học. Toàn bộ dữ liệu thực hành là **dữ liệu tổng hợp (Synthetic Data)** được sinh tự động bằng công cụ mã nguồn mở (như Synthea) hoặc ca bệnh giả định mô phỏng.
* **Chứng chỉ Đạo đức Nghiên cứu (CITI Program) & Thỏa thuận DUA:** Trong thực tế nghiên cứu, trước khi tiếp cận dữ liệu người bệnh, mọi nghiên cứu viên đều bắt buộc phải hoàn thành chứng chỉ đạo đức nghiên cứu (ví dụ: CITI Program về Biomedical Research / GCP) và ký Thỏa thuận Sử dụng Dữ liệu (Data Use Agreement - DUA). Khóa học sẽ hướng dẫn bạn cách xây dựng các tài liệu này một cách chuẩn mực.

---

## 4. CÁCH SỬ DỤNG QUIZ TỰ KIỂM TRA VÀ BÀI THỰC HÀNH (LABS)

### Cách dùng Quiz (34 câu hỏi tự đánh giá):
- Mỗi module từ M1 đến M6 có **4 câu hỏi trắc nghiệm** ở cuối bài, kèm đáp án và giải thích ngay bên dưới. Hãy đọc kỹ câu hỏi, tự chọn câu trả lời trước khi xem đáp án.
- Sau khi hoàn thành 6 module, bạn hãy làm **Quiz Tổng hợp 10 câu** ở trang Cuối khóa để kiểm tra sự liên kết giữa các giai đoạn trong quy trình.
- **Tiêu chuẩn tự đánh giá đạt yêu cầu:** Trả lời đúng từ **24/34 câu hỏi trở lên ($\ge 70\%$)**, trong đó đúng ít nhất 2 trong 3 câu đầu tiên (Q1–Q3) của bài quiz tổng hợp.

### Cách dùng Lab và Rubric /20:
- Mỗi chương cung cấp 1 bài thực hành cụ thể kèm dữ liệu mẫu và các bước chi tiết.
- Bảng Rubric /20 ở cuối mỗi bài lab là **thước đo tự kiểm tra (Self-Checklist)**: nếu bạn tự đánh giá mình đạt $\ge 16/20$ điểm, bạn đã hoàn toàn tự tin áp dụng kỹ năng đó vào dự án nghiên cứu thực tế của mình.
- Bài tập Capstone cuối khóa giúp bạn tự ghép nối toàn bộ các sản phẩm (DMP, biểu mẫu thu thập, đánh giá chất lượng, kế hoạch chia sẻ) thành một hồ sơ quản trị dữ liệu hoàn chỉnh.

Hãy bắt đầu hành trình của bạn với **Module 1: Tổng quan RDM, Vòng đời Dữ liệu và Kế hoạch DMP**!
