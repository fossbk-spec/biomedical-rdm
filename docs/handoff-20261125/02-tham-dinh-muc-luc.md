# Thẩm định mục lục và đề cương sách chuyên khảo Biomedical RDM

**Tác giả:** nhóm biên soạn · **Phiên bản:** 1.0.0 · **Ngày:** 24/11/2026
**Người quyết định:** TS. Hoàng Quang Huy (Ben)
**Phương pháp:** thẩm định 3 mức của HDBS (`QUY_TRINH_BIEN_SOAN_TEXTBOOK_CHUAN.md` mục 4.2): Mức 1 sai hoặc mâu thuẫn nội bộ; Mức 2 lỗi thời hoặc dễ hết hạn; Mức 3 cần làm rõ.
**Đối tượng đã đọc:** `docs/syllabus/BIOMEDICAL_RDM_FREE_SELF_PACED_SYLLABUS.md` (v1.0.0, 21/11/2026), `editorial/chapter-map.yml`, tiêu đề và nội dung liên quan của ch00–ch07 (main @ aef5ae2), `docs/appendices/`, `docs/legal-verification.md`, `docs/course-source/README.md`, `docs/plans/RDM_Fixed_vs_Updatable_Content_Plan_v1.0.0_20261121.md`.
**Giới hạn:** đây là thẩm định cấu trúc, mâu thuẫn nội bộ và dữ kiện dễ hết hạn. **Không phải** kiểm chứng khoa học từng nhận định (việc của GĐ3–GĐ4). Tra cứu pháp lý và chính sách NIH bằng tìm kiếm web ngày 24/11/2026: tôi chỉ đọc tóm tắt kết quả tìm kiếm, **chưa mở văn bản gốc**; đối chiếu bản gốc vẫn cần làm ở GĐ4.

## 1. Kết luận

Mục lục làm việc 7 + 2 chương **chưa thể chốt ngay**. Có **4 phát hiện Mức 1** làm sai nền của cuốn sách (một trong số đó ảnh hưởng cả ch00, ch01, đề cương và quiz), và **3 quyết định cấu trúc** cần Ben chốt trước khi nâng cấp 6 chương còn lại. Việc đánh giá tính đúng đắn khoa học của từng nhận định nằm ngoài phạm vi thẩm định này (thuộc GĐ3–GĐ4); các phát hiện dưới đây là về cấu trúc, mâu thuẫn nội bộ và dữ kiện dễ hết hạn.

## 2. Phát hiện Mức 1 (mâu thuẫn nội bộ, phải sửa)

| Mã | Vị trí | Phát hiện | Bằng chứng | Đề xuất |
|---|---|---|---|---|
| **T1-1** | ch00, đề cương, ch01 | **Có hai định nghĩa khác nhau của "vòng đời 7 giai đoạn"**, là xương sống của cả sách. Bản ch00/đề cương: 1 Thiết kế và DMP, 2 Thu thập, 3 Làm sạch và chất lượng, 4 Chuẩn hóa, **5 FAIR và chia sẻ, 6 Bảo mật và pháp lý (Luật 91/2025/QH15)**, 7 Lưu trữ và hủy. Bản ch01 (Hình 1.1): G1–G4 giống, **G5 Phân tích và tái lập, G6 FAIR và chia sẻ**, G7 Lưu trữ và hủy; bảo mật/pháp lý là **lớp ngang** (nút "PHÁP LÝ & ĐẠO ĐỨC" nối vào cả vòng đời), không phải một giai đoạn | `docs/chapters/ch00_getting_started.md:23-28`; `docs/syllabus/...SYLLABUS.md:46-52`; `docs/chapters/ch01_overview_and_dmp.md` (Hình 1.1, nhãn G1–G7) | Chốt **một** định nghĩa (xem quyết định Q-A). Đề xuất bản ch01 |
| **T1-2** | ch01 mục 4.5 và các nơi khác | **NIH DMSP: sách dạy đồng thời "7 yếu tố hiện hành" và "sáu thành tố bắt buộc".** Mục tiêu học tập, Lab 1, capstone và đề cương nói "mẫu hiện hành 7 yếu tố"; mục "Sáu thành tố bắt buộc của NIH DMSP (≤ 2 trang)" vẫn dạy mẫu 6 thành tố theo NOT-OD-21-014. Phụ lục B (bản nháp) gọi mẫu 6 thành tố là "mẫu cũ" | `ch01_overview_and_dmp.md:20` (7 yếu tố) và `:154` (Sáu thành tố bắt buộc); `docs/syllabus/...:38,59,92`; `docs/chapters/rdm-phu-luc-b-bo-sung-dmptool-templates.md:23-27` | Nếu giữ cả hai mẫu thì tiêu đề phải ghi rõ "mẫu trước 25/05/2026" và "mẫu hiện hành"; hoặc đưa mẫu cũ vào phụ lục. Để GĐ4 đối chiếu bản gốc NIH |
| **T1-3** | đề cương | **Số liệu mô tả khối lượng đã lỗi thời.** Đề cương ghi "Chương 1–6 và phụ lục khoảng 38.300 từ"; đo hiện tại bằng `wc -w` trên main: ch01–ch06 = 4.761 + 8.490 + 5.935 + 4.897 + 5.972 + 5.301 = 35.356 từ, cộng 5.038 từ phụ lục = 40.394 từ (trước khi PR #28 làm ch01 thành 6.297 từ). Thời gian đọc "4–6 giờ" tính từ số này | `docs/syllabus/...:69`; số đo `wc -w` ngày 24/11/2026 | Đề cương chuyên khảo không nên nêu số từ; nếu cần, sinh tự động từ `chapter-map.yml` |
| **T1-4** | `chapter-map.yml` (cũng thiếu tiên quyết ch04 → ch03), đề xuất chuyên khảo của tôi | **Vai trò chương và tiên quyết do bên thực hiện đề xuất chưa được đối chiếu với nội dung**; ví dụ ch06 ghi vai trò `governance` nhưng nội dung chính là FAIR và dữ liệu AI-ready (kỹ thuật + quản trị). Một lỗi trong đề xuất chuyên khảo của tôi: mục 9.5 nói license "cần Ben quyết định", nhưng README và đề cương **đã ghi CC BY 4.0** (nội dung) và **MIT** (mã nguồn) | `editorial/chapter-map.yml`; `README.md:18`; `docs/syllabus/...:13` | Rà `role` và `prerequisites` sau khi chốt thứ tự chương; hỏi Ben xác nhận license cho bản chuyên khảo |

## 3. Phát hiện Mức 2 (dữ kiện dễ hết hạn)

`scripts/check_volatile.py` chỉ quét chương và phụ lục, **không quét `docs/syllabus/`**. Đề cương hiện chứa các dữ kiện dễ đổi:

| Vị trí (đề cương) | Dữ kiện | Kiểm hôm nay (24/11/2026) | Xử lý |
|---|---|---|---|
| dòng 51, 63 | Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 | Khớp: được Quốc hội thông qua 26/06/2025, hiệu lực 01/01/2026, gồm 5 chương 39 điều (kết quả tìm kiếm và `legal-verification.md` mục [62]) | Không nên đặt số hiệu luật trong đề cương; chuyển vào phụ lục pháp lý |
| dòng 63, 111 | Nghị định 356/2025/NĐ-CP | Khớp: ký 31/12/2025, hiệu lực 01/01/2026, thay Nghị định 13/2023/NĐ-CP | Như trên |
| dòng 63 | Thông tư 13/2025/TT-BYT; 33/2025/TT-BYT; 50/2025/TT-BYT | Đã ghi trong `legal-verification.md`; [66] chỉ xác nhận một phần (thiếu toàn văn chính thức) | Giữ ở phụ lục, ghi trạng thái |
| dòng 38, 59, 92 | NIH "7 yếu tố hiện hành" | Theo tìm kiếm: NOT-OD-26-046 (25/02/2026) áp dụng cho hồ sơ có hạn nộp từ 25/05/2026, 7 yếu tố; có NOT-OD-26-100 (29/07/2026) về chuyển tiếp. Repo đã nhắc cả hai trong `funder-templates.md` | Như T1-2 |
| dòng 63 | EHDS, GDPR | EHDS Reg. (EU) 2025/327 đã đối chiếu ở `legal-verification.md` [58] | Giữ ở phụ lục |
| dòng 64 | "7 tiêu chí NIH Bridge2AI" | Nguồn là preprint chưa bình duyệt (ch06 đã ghi cờ) | Không đưa vào đề cương; giữ trong chương kèm cờ |
| dòng 14, 102 | "103 mục lõi, 115 mục tổng" | Khớp số mục hiện tại, nhưng 115 mục chưa phải đã sẵn sàng: 103 `VERIFIED_UNAUDITED` (mới xác minh định danh), 9 `BIB_PENDING`, 3 `PENDING_UNDETERMINED` | Sinh tự động hoặc bỏ; không ghi như "115 tài liệu đã xác minh" |

**Phát hiện mới ngoài repo** (từ tìm kiếm, chưa đọc văn bản gốc): Nghị định 330/2026/NĐ-CP (xử phạt hành chính về an ninh mạng và bảo vệ dữ liệu cá nhân, ban hành khoảng 19/08/2026) và Quyết định 2623/QĐ-TTg (kế hoạch triển khai luật, 29/11/2025). Cả hai thuộc phạm vi ch08 (pháp lý) và chưa có trong `legal-verification.md`; cần tra bản gốc trước khi dùng.

Đề xuất: (1) bỏ số hiệu văn bản khỏi đề cương và mục lục; (2) mở rộng `check_volatile.py` quét `docs/syllabus/` và tệp mục lục.

## 4. Phát hiện Mức 3 (cần làm rõ)

| Mã | Phát hiện | Bằng chứng | Đề xuất |
|---|---|---|---|
| **T3-1** | **Thứ tự chương không trùng thứ tự giai đoạn**: giai đoạn 3 là chất lượng, giai đoạn 4 là chuẩn hóa, nhưng ch03 là chuẩn, ch04 là chất lượng. Có lý do: ch04 dùng OHDSI DQD chạy trên OMOP CDM (ch04: mục 3.3, dòng 123–129) nên cần học chuẩn trước; ch03 gần như không phụ thuộc ch04 (1 lần nhắc) | `ch04_quality_and_imputation.md:20,123-129`; số đếm từ khóa ch03 | Giữ thứ tự chương, nhưng **nói rõ**: "thứ tự chương theo phụ thuộc kiến thức, không theo thứ tự giai đoạn"; thêm bảng ánh xạ giai đoạn ↔ chương trong ch01 |
| **T3-2** | **Ch00 và ch07 là học liệu của khóa học, không phải chuyên khảo.** Ch00 là "bắt đầu ở đây, hướng dẫn tự học"; ch07 là quiz tổng hợp và capstone. Ch07 hiện 2.403 từ, gần như toàn quiz | `ch00_getting_started.md:1`; `ch07_completion_and_capstone.md:1,16` | Ch00 thành "Lời nói đầu và hướng dẫn đọc" (phần đầu sách); quiz và capstone chuyển thành học liệu đi kèm; sách cần một **chương tổng kết và tích hợp** thật (bài toán tích hợp từ thiết kế đến chia sẻ) |
| **T3-3** | **Ch08 (pháp lý VN) phần lớn là viết mới, không phải di chuyển.** Nội dung pháp lý trong ch05 (mục 3.2 và 3.3) chỉ khoảng 1.099 từ (18% của 5.972 từ). Ch05 nhắc luật 7 lần, các chương khác 0–3 lần | đếm trên `ch05...:87-129` và số đếm từ khóa | Ch08 cần nghiên cứu mới và reviewer pháp lý; không nên hứa ngày hoàn thành trước khi có nguồn và người duyệt |
| **T3-4** | **Ranh giới ch09 (tái lập) chồng lấp**: ch01 mục 3.1 (khủng hoảng tái lập), ch04 (phân chia, rò rỉ), ch06 (FAIR) đều chạm tái lập. Ch01 nhắc "tái lập" 9 lần, các chương khác 0–1 | số đếm từ khóa | Chốt phạm vi ch09 là **thực hành tái lập tính toán** (môi trường, phiên bản, quy trình, mã nguồn); ch01 chỉ giữ động lực |
| **T3-5** | **Ch02 dài 8.490 từ**, gấp 1,4–1,8 lần chương khác (4.761–5.972) | `wc -w` | Chưa đề xuất tách; xét lại ở GĐ3 sau khi đọc nội dung (REDCap, ALCOA+, GCP, lab) |
| **T3-6** | **Đối tượng và mục tiêu năng lực của đề cương nhắm sinh viên và người học tự học**, trong khi quyết định C hướng tới nhà nghiên cứu và điều phối viên. Chưa có mục tiêu năng lực cho ch08, ch09 | `docs/syllabus/...:12,35-40` | Viết mục tiêu năng lực cấp chương trong chuyên khảo; giữ đề cương cũ làm tài liệu của khóa học |
| **T3-7** | **Quiz tổng hợp Q1 chỉ xếp 5 mục** (thiết kế, thu thập, chuẩn hóa, FAIR, kết thúc); không nêu làm sạch/chất lượng nên không phân biệt hai định nghĩa vòng đời ở T1-1 | `ch07...:16-20` | Rà lại Q1 sau khi chốt Q-A |

## 5. Các quyết định cần Ben

**Q-A. Định nghĩa chuẩn của vòng đời 7 giai đoạn (T1-1).**
| Phương án | Nội dung | Nhận xét |
|---|---|---|
| **A1 (đề xuất)** | Bản ch01: G1 Thiết kế và DMP, G2 Thu thập, G3 Xử lý và làm sạch, G4 Chuẩn hóa, G5 Phân tích và tái lập, G6 FAIR và chia sẻ, G7 Lưu trữ và hủy; bảo mật/pháp lý/đạo đức là lớp ngang | Mô tả đúng bản chất (pháp lý áp vào mọi giai đoạn); khớp ch09 (tái lập) mới; cần sửa ch00, đề cương, quiz Q1, `check` trong mini-course |
| A2 | Bản ch00/đề cương: bảo mật và pháp lý là giai đoạn 6, FAIR là 5 | Giữ thứ tự chương gần hơn (privacy trước FAIR), nhưng coi pháp lý như một bước riêng dễ gây hiểu sai; không có chỗ cho tái lập |
| A3 | 8 giai đoạn hợp nhất | Quá nhiều thay đổi cho cả sách và mini-course |

**Q-B. Đánh số chương khi thêm ch08 (pháp lý) và ch09 (tái lập).**
| Phương án | Nội dung | Nhận xét |
|---|---|---|
| **B1 (đề xuất)** | Đánh số lại theo thứ tự đọc một lần, trước khi nâng cấp các chương: 1 Tổng quan, 2 Thu thập, 3 Chuẩn, 4 Chất lượng, 5 Bảo mật và khử định danh, **6 Quản trị và pháp lý VN**, **7 FAIR và AI-ready**, **8 Tái lập**, 9 Tích hợp và tổng kết | Số chương khớp thứ tự đọc; tốn công một lần (đổi tên tệp, `chapter-map`, glossary `first_chapter`, caption `Hình C.k`, đồng bộ web); mini-course không đổi vì dùng "Bài N" riêng |
| B2 | Giữ ch01–ch07, thêm ch08, ch09 ở cuối; sắp xếp thứ tự đọc bằng "Phần" | Không đổi gì ngay, nhưng số chương không khớp thứ tự đọc (pháp lý là chương 8 nhưng đọc sau ch05) |
| B3 | Giữ mã `chNN` như định danh cố định, hiển thị số chương theo thứ tự đọc | Mã và số chương lệch nhau, dễ nhầm trong tham chiếu và caption |

**Q-C. Vai trò của ch00 và ch07 (T3-2).** C1 (đề xuất): ch00 thành "Lời nói đầu và hướng dẫn đọc", ch07 chuyển quiz và capstone sang học liệu đi kèm, sách có chương tích hợp mới. C2: giữ nguyên ch00 và ch07 như chương của sách. C3: bỏ hẳn hai chương này khỏi chuyên khảo.

**Cần xác nhận thêm:** mẫu NIH dạy trong ch01 (T1-2): chỉ mẫu hiện hành, hay cả hai có phân biệt rõ; license CC BY 4.0 + MIT có giữ cho bản chuyên khảo không.

## 6. Mục lục đề xuất (dự thảo, theo A1, B1, C1; chờ Ben duyệt)

| Phần | Chương | Vai trò | Nguồn nội dung hiện có | Trạng thái |
|---|---|---|---|---|
| (Mở đầu) | Lời nói đầu và hướng dẫn đọc | khung | ch00 (đã bỏ phần tự học) | cần viết lại |
| I. Nền tảng | 1. Tổng quan RDM, vòng đời, DMP | khung | ch01 | **chương mẫu (PR #28)** |
| II. Thu thập dữ liệu | 2. Thu thập dữ liệu lâm sàng, ALCOA+, REDCap | thực hành | ch02 | cần nâng cấp |
| III. Chuẩn và chất lượng | 3. CDISC, FHIR, OMOP | chuẩn | ch03 | cần nâng cấp |
| | 4. Chất lượng và dữ liệu khuyết | thực hành | ch04 (khai báo tiên quyết ch03) | cần nâng cấp |
| IV. Quản trị, bảo mật, pháp lý | 5. Bảo mật và khử định danh | quản trị | ch05 (bỏ mục 3.2–3.3 sang chương 6) | cần nâng cấp |
| | 6. Quản trị và pháp lý Việt Nam | quản trị | **mới** (nền: ch05 mục 3.2–3.3, `legal.md`) | cần nghiên cứu và reviewer pháp lý |
| V. Chia sẻ và AI | 7. FAIR, kho lưu trữ, dữ liệu AI-ready | chuẩn/quản trị | ch06 | cần nâng cấp |
| | 8. Tái lập và phần mềm nghiên cứu | thực hành | **mới** (nền: ch01 mục 3.1, ch04, ch06) | cần nghiên cứu |
| VI. Tích hợp | 9. Tích hợp và tổng kết | khung | ch07 (phần capstone), bài toán tích hợp mới | cần viết |
| Phụ lục | Mẫu nhà tài trợ, lưu giữ, chuẩn, pháp lý, lab, thuật ngữ, ký hiệu | | `docs/appendices/`, `editorial/` | giữ, ghi ngày cập nhật |

Thứ tự đọc khuyến nghị: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 (3 trước 4 do phụ thuộc DQD/OMOP; 5 trước 6; 6 trước 7 vì chia sẻ phải qua kiểm soát pháp lý). Bảng ánh xạ giai đoạn ↔ chương được thêm vào chương 1.

## 7. Việc làm tiếp (khi Ben chốt Q-A, Q-B, Q-C)
1. Sửa ch00, đề cương và `chapter-map.yml` theo Q-A và Q-C; thêm bảng ánh xạ giai đoạn ↔ chương vào ch01.
2. Nếu chọn B1: một PR riêng đổi số và tên chương (git mv, tham chiếu, caption, glossary, `chapter-map`), trước khi nâng cấp chương nào khác.
3. Ghi `docs/syllabus/MONOGRAPH_OUTLINE_v1.0.0.md` (mục lục chính thức, mục tiêu năng lực cấp chương, tiên quyết, phạm vi từng chương).
4. Mở rộng `check_volatile.py` quét `docs/syllabus/` và tệp mục lục.
5. Giao bên thực hiện nâng cấp ch03 theo thứ tự đã chốt (sau khi duyệt chương mẫu).

## 8. Điều chưa kiểm
- Chưa đọc văn bản gốc của luật, nghị định, thông báo NIH; chỉ dựa tóm tắt kết quả tìm kiếm và tệp `legal-verification.md` của repo.
- Chưa đọc toàn bộ nội dung từng chương; mô tả vai trò chương dựa trên tiêu đề, số đo và đọc có chọn lọc.
- Chưa kiểm mini-course (6 bài) theo mục lục mới; việc đó làm sau khi chốt Q-A, Q-B.
- Chưa đánh giá ch02 (dài nhất) để biết có nên tách.

## Nguồn tìm kiếm ngày 24/11/2026 (chưa mở văn bản gốc)
- Luật 91/2025/QH15: [Hà Tĩnh](https://hatinh.gov.vn/vi/bai-viet/luat-bao-ve-du-lieu-ca-nhan-chinh-thuc-co-hieu-luc-thi-hanh-tu-ngay-112026), [Thư viện pháp luật](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Luat-Bao-ve-du-lieu-ca-nhan-2025-91-2025-QH15-625628.aspx).
- Nghị định 356/2025/NĐ-CP: [EY Vietnam](https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/nghi-dinh-so-356-2025-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-va-bien-phap-thi-hanh-luat-bao-ve-du-lieu-ca-nhan), [CSDL quốc gia về văn bản pháp luật](https://vbpl.moj.gov.vn/TW/Lists/vbpq/Attachments/187276/ND.356.2025.doc).
- NIH NOT-OD-26-046: [thông báo NIH](https://www.grants.nih.gov/grants/guide/notice-files/NOT-OD-26-046.html), [NIH Extramural Nexus](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/04/2026-pilot-data-management-and-sharing-plan-format-available).

## 9. Hiệu đính sau review độc lập của bên thực hiện (24/11/2026)
bên thực hiện xác minh lại các phát hiện T1-1…T3-7: 8 phát hiện Đúng, 4 Đúng một phần, không phát hiện nào Sai. Các chỉnh sửa đã áp dụng vào báo cáo này: (1) bỏ câu khẳng định "không có phát hiện nào cho thấy nội dung sai về khoa học" (vượt bằng chứng); (2) mục lục dự thảo sắp lại các phần cho khớp thứ tự đọc (ch03 và ch04 cùng Phần III; trước đó bảng đặt ch04 trước ch03); (3) ghi `chapter-map.yml` còn thiếu tiên quyết ch04 → ch03; (4) nói rõ 115 mục thư mục chưa phải đã sẵn sàng. Các kết luận pháp lý và NIH ở mục 3 chỉ có nghĩa "khớp với hồ sơ kiểm tra hiện có và tóm tắt tìm kiếm"; chưa phải xác minh nguồn gốc. Chi tiết review xem `docs/handoff-20261125/05-review-doc-lap-de-xuat.md` và mục 15 của đề xuất chuyên khảo.
