---
reviewed: 2026-11-27
next_review: 2027-05-25
---

# Nhật ký thay đổi phụ lục

| Ngày | Thay đổi | Trạng thái | URL nguồn | Ngày kiểm | Người quyết định |
|---|---|---|---|---|---|
| 2026-11-21 | Tách nội dung cập nhật của chương 1 thành `legal`, `funder-templates`, `retention`, `standards`; giữ cờ chưa kiểm chứng. | VERIFIED | [Sổ kiểm chứng](../legal-verification.md) | 2026-11-21 | Ben |
| 2026-11-21 | Tách nội dung cập nhật chương 2; bổ sung phụ lục `redcap-lab-notes` (ghi chú lab REDCap); cập nhật `standards` (REDCap2SDTM/OMOP, Castor). | VERIFIED | [redcap-lab-notes](redcap-lab-notes.md) | 2026-11-21 | Ben |
| 2026-11-21 | Bổ sung các dòng pháp lý, nhà tài trợ, lưu trữ và chuẩn từ bộ phụ lục chữ cái; các chi tiết chưa có bằng chứng đầy đủ giữ `CONTENT_PENDING`/`BIB_PENDING`. | CONTENT_PENDING | [Sổ kiểm chứng](../legal-verification.md) | 2026-11-21 | Ben |
| 2026-11-21 | Cập nhật phụ lục pháp lý/chuẩn cho chương 2 và thêm ghi chú lab REDCap; các chi tiết cấu hình/mã ánh xạ chưa đối chiếu giữ `CONTENT_PENDING`. | CONTENT_PENDING | [Phụ lục pháp lý](legal.md); [Phụ lục standards](standards.md); [Ghi chú lab](redcap-lab-notes.md) | 2026-11-21 | Ben |
| 2026-11-21 | Bổ sung phụ lục chuẩn và ghi chú lab cho chương 3: trạng thái FHIR/OMOP/CDISC/FDA/PMDA, giới hạn concept mapping và kết quả chạy ETL minh họa. | CONTENT_PENDING | [Phụ lục standards](standards.md); [Ghi chú FHIR–OMOP](fhir-omop-lab-notes.md) | 2026-11-21 | Ben |
| 2026-11-21 | Cập nhật pháp lý và lưu trữ cho chương 5; thêm ghi chú Lab 5 với trạng thái nguồn, cảnh báo seed và kết quả chạy dữ liệu tổng hợp. | CONTENT_PENDING | [Phụ lục pháp lý](legal.md); [Phụ lục lưu trữ](retention.md); [Ghi chú Lab 5](privacy-lab-notes.md) | 2026-11-21 | Ben |
| 2026-11-21 | Cập nhật phụ lục `funder-templates`: bổ sung định dạng NIH 2026 gồm 7 yếu tố, trạng thái nguồn NIH/DMPTool và cảnh báo tên mẫu production; cập nhật thời hạn lưu giữ HHS/NIH, giữ các cờ chưa kiểm chứng. | VERIFIED_UNAUDITED/CONTENT_PENDING | [Phụ lục nhà tài trợ](funder-templates.md); [Phụ lục lưu trữ](retention.md) | 2026-11-21 | Ben |
| 2026-11-21 | Bổ sung ghi chú Lab 4/6; chốt trạng thái nguồn DQD, RO-Crate, DataCite và Zenodo; ghi rõ số DQD minh họa và giới hạn preprint. | CONTENT_PENDING | [Ghi chú Lab 4/6](quality-ai-lab-notes.md); [Phụ lục standards](standards.md) | 2026-11-21 | Ben |
| 2026-11-25 | Bổ sung phụ lục `case-study-drmayday` (case study dự án thật DrMayDay, v2): vòng đời 7 giai đoạn áp vào dự án, SOP chụp ảnh + gán nhãn, dataset theo mô hình, QC trước huấn luyện, sơ đồ pipeline 8 chặng; sửa 3 lỗi (giả danh hóa, UAS7 miền QS, căn cứ Luật 91/2025 + NĐ 356/2025). | VERIFIED_UNAUDITED | [Phụ lục case study DrMayDay](case-study-drmayday.md) | 2026-11-25 | Ben |
| 2026-11-26 | Đối chiếu nguồn cho phụ lục `case-study-drmayday`: đọc văn bản gốc Luật 91/2025 (Điều 21–23, 38–39), Nghị định 356/2025 (Điều 39, 42), Thông tư 33/2025 (Điều 1–2, Phụ lục STT 15/39/40/44); chạy lại kiểm thử rule engine ở repo dự án; hạ trạng thái các mục chưa kiểm chứng (TCVN 14423, guideline 2026, tên đơn vị nhận DPIA). Thêm mức 10 năm cho bệnh án nội trú/ngoại trú. | VERIFIED_UNAUDITED | [Sổ kiểm chứng](../legal-verification.md); [Phụ lục case study](case-study-drmayday.md) | 2026-11-26 | Ben (chờ duyệt PR) |
| 2026-11-27 | Đối chiếu bổ sung `legal`: đọc bản PDF gốc Quyết định 1308/QĐ-TTg (18/07/2026) và nâng lên `VERIFIED_UNAUDITED`; tách dòng chung Nghị quyết 57/QĐ 1308/QĐ 3218 thành từng dòng; thêm Nghị định 102/2025/NĐ-CP (quản lý dữ liệu y tế) ở `CONTENT_PENDING`; ghi lệch năm với bản thảo v2. | VERIFIED_UNAUDITED / CONTENT_PENDING | [Sổ kiểm chứng](../legal-verification.md) | 2026-11-27 | Ben |
