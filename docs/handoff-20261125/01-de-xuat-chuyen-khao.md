# Đề xuất: biến Biomedical RDM thành sách chuyên khảo hoàn chỉnh

**Tác giả:** nhóm biên soạn · **Phiên bản:** 1.1.0 (thêm mục 13: quyết định của Ben) · **Ngày:** 24/11/2026
**Người quyết định:** TS. Hoàng Quang Huy (Ben)
**Căn cứ đã đọc:** `HDBS/QUY_TRINH_BIEN_SOAN_TEXTBOOK_CHUAN.md`, `HDBS/HUONG_DAN_TOAN_DIEN_BIEN_SOAN_TEXTBOOK.md`, `HDBS/AGENTS.md`, các mục lục của `HDBS/07` và `HDBS/08`; `HMYT/editorial/` (`HMYT_Quy_trinh_chinh_Living_Textbook_v2.0.md`, `review-policy.md`, `chapter-map.yml`, `TIEN_DO.md`), `HMYT/CLAUDE.md`; cấu trúc và số từ của `HMYT/chapters`; trạng thái `biomedical-rdm` (main @ 57b54b1 khi viết; đã lỗi thời, nay main @ aef5ae2, xem mục 15).
**Giới hạn:** `emr-book` trên máy chỉ có bản đã xuất bản (nhánh `gh-pages`, 8 chương + danh mục viết tắt + lời nói đầu); không có nguồn Markdown, nên tôi chỉ đọc cấu trúc xuất bản và danh sách script `HDBS/scripts/emr/`, **chưa đọc nội dung hay quy trình nội bộ của EMR**. Phần nào dựa vào EMR đều ghi rõ là suy ra từ cấu trúc.

## 1. Kết luận ngắn

Biomedical RDM hiện là **giáo trình tự học kèm mini-course** (khoảng 43.700 từ trong ch00–ch07 và phụ lục đã được theo dõi; 7 chương nội dung, 115 mục thư mục trong đó chỉ 103 đã xác minh định danh, quiz 39 + 34 câu). Chưa phải sách chuyên khảo. Khoảng cách chính không nằm ở số từ mà ở bốn việc: (1) chưa có lập luận xuyên suốt và khung khái niệm riêng của sách; (2) chưa có bộ chuẩn biên tập dùng chung (ký hiệu, thuật ngữ, chapter-map, quy tắc review); (3) tài liệu tham khảo mới được xác minh về định danh, chưa được đối chiếu với từng nhận định; (4) chưa có đường xuất bản bản in/PDF, phiên bản có thể trích dẫn và quy trình đính chính.

Đề xuất: **dùng lại bộ khung vận hành của HDBS và HMYT (đơn nguồn, trích dẫn đóng, chỉ thêm không bớt, lưu bản cũ trước khi sửa, một PR một chương, ba lớp kiểm định), nhưng không sao chép khung 16 mục của sách học máy** vì nó không khớp với nội dung quản trị dữ liệu. Làm theo 6 giai đoạn có cổng nghiệm thu, giữ mini-course và quiz là sản phẩm phái sinh.

## 2. Hiện trạng so với yêu cầu của một chuyên khảo

| Yêu cầu | Hiện trạng (kiểm trên repo) | Mức |
|---|---|---|
| Đơn nguồn Markdown, build tự động | Có: chương trong `docs/chapters`, web khóa học đồng bộ một chiều bằng script | Đạt |
| Trích dẫn đóng, kiểm bằng script | Có: `build_bib.py --check`, 115 mục. 103 `VERIFIED_UNAUDITED` (mới xác minh định danh), 9 `BIB_PENDING`, 3 `PENDING_UNDETERMINED` | Đạt một phần |
| Mỗi nhận định quan trọng có nguồn đã đối chiếu | Chưa: chưa có audit mức nhận định | Thiếu |
| Chống nội dung hết hạn | Có: `check_volatile.py`, quy tắc "cố định/cập nhật" | Đạt |
| Khung chương thống nhất | Chương theo mẫu giáo trình (mục tiêu, khái niệm, lý thuyết, case, lab, bài tập, tóm tắt, quiz); chưa phân loại theo vai trò chương | Một phần |
| Bộ chuẩn biên tập (ký hiệu, thuật ngữ Việt–Anh, phong cách, chapter-map, review-policy) | (Tại thời điểm viết chưa có; đã có `editorial/` sau PR #27, xem mục 15); thuật ngữ nằm rải rác | Thiếu |
| Lưu bản cũ và nhật ký thay đổi theo chương | Chỉ có `DECISIONS.md` và changelog phụ lục | Thiếu |
| Review độc lập (AI không ngữ cảnh, đồng nghiệp, chuyên gia ngoài) | Mới có review nội bộ của người soạn/bên thực hiện | Thiếu |
| Nội dung đang chờ xác minh | Luật Việt Nam, NIH, OMOP, EHDS (`CONTENT_PENDING`), ref_011, ref_103, preprint | Mở |
| Case study có thể công bố | Chờ quyết định về sự đồng ý | Mở |
| Lab chạy được và tái lập | Lab 2 chưa chạy sandbox | Mở |
| Xuất bản in/PDF, mục lục, chỉ mục, bảng/hình đánh số | Chưa; chỉ có web VitePress | Thiếu |
| Phiên bản trích dẫn được (DOI, license) | Chưa | Thiếu |
| Đính chính sau xuất bản | Chưa | Thiếu |

## 3. Những gì nên kế thừa, những gì không

**Kế thừa từ HDBS (quy trình chuẩn):**
- Đơn nguồn tri thức; kỷ luật phiên bản, cấm hậu tố `_final`.
- "Chỉ thêm, không bớt": lỗi khách quan sửa thẳng; quyết định nội dung hoặc sư phạm phải gắn cờ chờ tác giả.
- Nhãn minh bạch cho phần suy luận hoặc số minh họa; cấm tự bịa tài liệu tham khảo.
- Kiểm định hai lớp: cấu trúc, rồi nội dung và tính cập nhật, bắt buộc tra cứu pháp lý từ nguồn chính thức.
- Mức thẩm định mục lục 3 bậc (sai thực sự, lỗi thời, cần làm rõ) trước khi viết.
- Nguyên tắc nhánh và worktree riêng cho mỗi tác vụ, không làm trên `main` (`HDBS/AGENTS.md`); điều này RDM đang áp dụng.

**Kế thừa từ HMYT:**
- Thư mục `editorial/` làm nơi chứa chuẩn dùng chung: `glossary.yml`, `notation.md`, `style-guide.md`, `chapter-map.yml`, `review-policy.md`, `TIEN_DO.md`, đính chính `ERRATA_*.md`.
- Bốn trạng thái kiểm tra: Đạt, Không đạt, Chưa kiểm tra, Không áp dụng. Công cụ lỗi không được ghi là đạt. RDM đã theo tinh thần này ở policy `status`.
- Mẫu báo cáo phát hiện (mã, vị trí, nhận định, nguồn và phạm vi đã đọc: toàn văn, abstract hay metadata, mức độ, đề xuất, người đóng).
- Ba lớp kiểm định tách bạch: quy tắc, AI đối chiếu, chuyên gia duyệt. DOI hợp lệ chỉ xác nhận định danh, không chứng minh nhận định đúng.
- Chu trình sửa theo chương: nhánh riêng, một script thay thế có `assert count==1`, lưu bản cũ `archive/chNN/`, `editorial/changelog/chNN_<ngày>.md`, PR có CI. Bài học từ chuỗi PR của HMYT: PR xếp chồng khó review; nên gộp theo giai đoạn, mỗi PR một chương.
- Cảnh báo vận hành: không để hook cục bộ tự deploy từ worktree (sự cố 17/10 của HMYT); deploy RDM đang thủ công, giữ như vậy.

**Không sao chép:**
- Khung 16 mục (Algorithm, Data & Model Pipeline, Research Challenge, 40 câu Bloom mỗi chương) và ma trận trọng số của HMYT vốn thiết kế cho học máy. Với RDM, chương về pháp lý, DMP hay chuẩn dữ liệu không có "thuật toán" để mô tả. Thay bằng khung riêng ở mục 5.
- Chu trình "5 giờ/chương" gắn với hạn mức người soạn và Gemini viết Draft 1: RDM đã có nội dung; việc cần làm là nâng cấp và kiểm chứng, không viết mới hàng loạt. Gemini chỉ giữ vai trò kiểm trang nguồn mục không DOI (đã có) và tư vấn.
- Quy trình HMYT bản 2.0 tự ghi "Đề xuất triển khai; cần đối chiếu cấu hình" và có phần đa tác giả (CODEOWNERS, nhiều người duyệt). RDM hiện chỉ có Ben làm người duyệt. Chỉ áp dụng phần đa tác giả khi Ben chốt có đồng tác giả.

## 4. Vì sao "chuyên khảo" khác "giáo trình tự học"

Một chuyên khảo phải có (a) luận điểm và khung khái niệm riêng, (b) tổng hợp bằng chứng có hệ thống thay vì liệt kê, (c) nêu giới hạn và vùng chưa chắc chắn, (d) đối thoại với tài liệu tồn tại (khung FAIR, quy trình DMP, mô hình vòng đời dữ liệu), (e) tính tái lập. Với RDM y sinh, giá trị khác biệt có thể là **một khung quản trị dữ liệu nghiên cứu cho bối cảnh Việt Nam, gắn pháp lý, chuẩn dữ liệu y tế và dữ liệu sẵn sàng cho AI**. Đây là lập luận tôi đề xuất, cần Ben xác nhận hoặc thay; không có trong tài liệu hiện có nên tôi không tự khẳng định.

## 5. Kiến trúc sách đề xuất

### 5.1. Định vị
Định vị B của HDBS (chuyên khảo, không bị giới hạn khung giờ), chia sẻ nội dung nền với mini-course. Mục lục dưới đây là **phương án làm việc**, giữ đủ 7 chương hiện có và thêm chương nối khi có lý do nội dung; mỗi chương mới phải qua thẩm định mục lục 3 bậc trước khi viết.

| Phần | Chương (hiện có → đề xuất) | Ghi chú |
|---|---|---|
| I. Nền tảng | Ch1 Tổng quan và DMP; (mới, tùy chọn) vòng đời và khung quản trị | Khung khái niệm riêng của sách đặt ở đây |
| II. Thu thập dữ liệu | Ch2 Thu thập và REDCap | Ch2 dài nhất (~8.500 từ), cân nhắc tách |
| III. Chuẩn và chất lượng | Ch3 CDISC, FHIR, OMOP; Ch4 Chất lượng và dữ liệu khuyết | Ch4 phụ thuộc ch3 (DQD chạy trên OMOP CDM); phiên bản chuẩn đưa vào Sổ cập nhật |
| IV. Bảo mật, đạo đức, pháp lý | Ch5 Bảo mật và khử định danh; (mới, tùy chọn) quản trị và pháp lý Việt Nam | Gộp phần pháp lý rải rác thành một nơi dễ cập nhật |
| V. Chia sẻ, FAIR và AI | Ch6 FAIR và AI-ready | Tách phần AI-ready khỏi bài 5 mini-course theo `PROJECT-STATE` |
| VI. Tích hợp | Ch7 Hoàn thành và capstone; case study | Case study chỉ công bố khi có sự đồng ý |
| Phụ lục | Mẫu nhà tài trợ, lưu giữ, pháp lý, lab, thuật ngữ, ký hiệu, bảng tra | Phần cập nhật nằm phụ lục, thân chương chỉ nêu nguyên lý |

### 5.2. Khung chương cho chuyên khảo RDM (v1, để thử trên một chương)
1. Tóm tắt chương và các luận điểm chính (3–6 ý, đối chiếu được tới mục dưới).
2. Phạm vi, giả định và đối tượng.
3. Nền tảng khái niệm (định nghĩa, sơ đồ Mermaid có chú thích).
4. Nội dung cốt lõi theo vai trò chương (xem 5.3).
5. Bảng bằng chứng: nhận định, nguồn, loại nguồn, phạm vi đã đọc, mức độ chắc chắn.
6. Ví dụ minh họa và case study (nêu rõ giả định hay thật).
7. Lab/thực hành (tùy chọn, tái lập được).
8. Cạm bẫy và thực hành tốt.
9. Giới hạn và vấn đề mở.
10. Tóm tắt, câu hỏi tự kiểm tra (giữ quiz chống lộ đáp án), bài tập.
11. Thuật ngữ mới, tài liệu tham khảo.

### 5.3. Bốn vai trò chương (thay cho 5 archetype học máy)
| Vai trò | Ví dụ | Tỷ trọng gợi ý |
|---|---|---|
| Khung và quy trình | Ch1, Ch7 | Lập luận, quy trình, mẫu biểu |
| Kỹ thuật thực hành | Ch2, Ch4 | Quy trình dữ liệu, lab, cạm bẫy |
| Chuẩn và liên thông | Ch3 | Mô hình dữ liệu, ánh xạ, kiểm tra |
| Quản trị, pháp lý, đạo đức | Ch5, Ch6 | Quy định, rủi ro, quyết định có điều kiện |

Tỷ trọng chính xác nên chốt sau khi thử trên một chương, không áp số của HMYT.

## 6. Quy trình sản xuất đề xuất

### 6.1. Giai đoạn và cổng nghiệm thu
| GĐ | Nội dung | Sản phẩm | Cổng nghiệm thu |
|---|---|---|---|
| 0 | Quyết định định vị (mục 9), thẩm định mục lục 3 bậc | `docs/syllabus/` bản monograph v1.0, `editorial/chapter-map.yml` | Ben duyệt mục lục và phạm vi |
| 1 | Bộ chuẩn biên tập | `editorial/`: `style-guide.md`, `notation.md`, `glossary.yml`, `review-policy.md`, `TIEN_DO.md`; script `check_structure.py`, `check_glossary.py`, kiểm tham chiếu chéo | Script chạy trên cả 7 chương, báo cáo "đạt/không đạt/chưa kiểm tra" |
| 2 | Chương mẫu | 1 chương (đề xuất Ch1) viết lại theo khung 5.2, kèm archive, changelog | Ben duyệt khung; điều chỉnh khung trước khi nhân rộng |
| 3 | Nâng cấp từng chương, một PR mỗi chương | 6 chương còn lại theo thứ tự phụ thuộc: 1, 3, 2, 4, 5, 6, 7 | Mỗi chương: kiểm cấu trúc, trích dẫn, volatile, quiz đạt; audit mức nhận định hoàn tất |
| 4 | Xác minh nội dung chờ: pháp lý VN, NIH, OMOP, EHDS, ref_011, ref_103, preprint; chạy Lab 2 | Phụ lục pháp lý đã đối chiếu nguồn chính thức; lab có log chạy | Không còn `CONTENT_PENDING` trong thân sách |
| 5 | Review độc lập | Báo cáo AI không ngữ cảnh; 2–3 chuyên gia ngoài nhóm (Ben chọn) | Mọi phát hiện nghiêm trọng đã đóng hoặc ghi lý do |
| 6 | Xuất bản và đính chính | PDF/DOCX (Quarto hoặc Typst), web, bản có DOI và license, trang đính chính | Kiểm render thật các công thức và sơ đồ; tag phát hành |

### 6.2. Audit mức nhận định (điểm khác biệt quan trọng nhất so với hiện nay)
Với mỗi chương, lập bảng: nhận định có số liệu, quy định hoặc kết luận → nguồn → phạm vi đã đọc (toàn văn, abstract, metadata) → kết quả (đối chiếu được, không đối chiếu được, cần sửa). Chỉ nguồn đã đọc đủ mới đủ cơ sở kết luận; nguồn chỉ có abstract thì ghi giới hạn, theo `review-policy` của HMYT. Cột `status` của `citation-audit.csv` vẫn không đổi theo kiểm trang (policy hiện hành); bảng nhận định là tệp riêng.

### 6.3. Phân vai
- Ben: quyết định định vị, mục lục, case study, người duyệt chuyên môn, merge.
- người soạn: brief, thẩm định mục lục, review, audit nhận định, chốt chuẩn.
- bên thực hiện: triển khai script, viết lại chương theo brief, chạy kiểm tra.
- Gemini: chỉ kiểm trang nguồn mục không DOI và tư vấn, đã có trong repo.
- Mọi bản viết lại của AI qua PR; không ai merge chính PR của mình trừ khi Ben đã giao quyền (RDM hiện do Ben quyết).

## 7. Hạ tầng kiểm định cần thêm (script)
| Script | Kiểm gì | Ưu tiên |
|---|---|---|
| `check_structure.py` | Thứ tự mục, caption hình/bảng, mọi hình bảng được dẫn chiếu | Cao |
| `check_glossary.py` | Thuật ngữ trong thân chương khớp `glossary.yml`, viết tắt có chú giải lần đầu | Cao |
| `check_crossrefs.py` | Tham chiếu chương, mục, hình, bảng không gãy | Cao |
| `check_claims.py` | Mỗi dòng bảng bằng chứng có khóa tham khảo hợp lệ và trạng thái đọc | Trung bình |
| Kiểm render | Xuất PDF thật, kiểm công thức/sơ đồ không vỡ (HDBS cảnh báo lỗi glyph) | Cao trước GĐ6 |
| Bổ sung `check_volatile.py` | Mở rộng sang các mục mới | Thấp |

## 8. Xuất bản
- Giữ Quarto cho nguồn gốc (repo gốc đã dùng); thêm đầu ra PDF và DOCX, giữ VitePress cho web. HDBS `08` khuyến nghị Quarto cho giáo trình nhiều tác giả; chuyên khảo chính thức nên thêm JATS nếu qua nhà xuất bản.
- Mỗi bản phát hành gắn tag, có DOI (ví dụ qua kho lưu trữ có cấp DOI) và license; hai việc này cần Ben quyết định.
- Đính chính: bắt đầu bằng nhật ký nội bộ (Option A của HDBS `08`), nâng lên có thẩm định khi có bản in.

## 9. Quyết định cần Ben (chặn các giai đoạn sau)
1. **Định vị:** chuyên khảo độc lập cho nhà nghiên cứu y sinh, hay giáo trình nâng cao dùng trong đào tạo; có làm cả hai bản không?
2. **Quy mô:** giữ 7 chương và tinh luyện, hay thêm các chương nối ở mục 5.1 (khung quản trị, pháp lý Việt Nam, tái lập)?
3. **Ngôn ngữ:** chỉ tiếng Việt, hay song ngữ như HMYT (có chi phí duy trì cặp VI/EN rất lớn, HMYT đã gặp)?
4. **Tác giả:** một tác giả, hay có đồng tác giả và người phản biện nội bộ?
5. **Xuất bản:** tự xuất bản trực tuyến + PDF, hay qua nhà xuất bản; license (ví dụ CC BY) và DOI.
6. **Case study DrMayDay:** có công bố không, kèm sự đồng ý nào.
7. **Reviewer ngoài:** nhóm chuyên gia nào (y sinh, pháp lý, dữ liệu), thời hạn.
8. Số câu mỗi bài và quy tắc 24/34 của mini-course (đang chờ từ trước).

## 10. Rủi ro và cách giảm
| Rủi ro | Cách giảm |
|---|---|
| Phạm vi phình, không kết thúc | Cổng nghiệm thu từng giai đoạn; chương mới chỉ khi qua thẩm định mục lục |
| Nội dung pháp lý, chuẩn lỗi thời khi in | Giữ trong phụ lục cập nhật, thân chương nêu nguyên lý; ghi ngày đối chiếu |
| AI tạo nhận định khó kiểm | Bảng bằng chứng bắt buộc; chỉ nguồn đã đọc mới kết luận |
| PR xếp chồng khó review (bài học HMYT) | Một PR một chương, base `main` |
| Nội dung và mini-course lệch nhau | Giữ đồng bộ một chiều từ nguồn (đã có), thêm kiểm khớp khi sửa chương |
| Duy trì song ngữ | Quyết định ở mục 9.3 trước khi viết lại |
| Phụ thuộc một người duyệt | Thêm reviewer độc lập ở GĐ5 |

## 11. Bước tiếp theo đề xuất (không cần chờ mọi quyết định)
1. Ben trả lời mục 9.1–9.3 (ba câu quyết định cấu trúc).
2. Tôi lập `editorial/` v1 và `chapter-map.yml` từ nội dung hiện có (GĐ1), do bên thực hiện triển khai script kiểm.
3. Thử khung 5.2 trên Ch1 để đo công sức thật rồi mới ước lượng thời gian cho 6 chương còn lại. Tôi **chưa đưa ước lượng thời gian** vì chưa có số đo thử.

## Tài liệu tham chiếu nội bộ
- `HDBS/QUY_TRINH_BIEN_SOAN_TEXTBOOK_CHUAN.md` v1.0; `HDBS/HUONG_DAN_TOAN_DIEN_BIEN_SOAN_TEXTBOOK.md` v2.0; `HDBS/AGENTS.md`; `HDBS/08-nang-cap-chat-luong-va-lua-chon-trien-khai.md`.
- `HMYT/editorial/HMYT_Quy_trinh_chinh_Living_Textbook_v2.0.md`; `HMYT/editorial/review-policy.md`; `HMYT/editorial/chapter-map.yml`; `HMYT/editorial/TIEN_DO.md`.
- `biomedical-rdm/docs/PROJECT-STATE.md` v2.5.0; `docs/DECISIONS.md`; `docs/plans/RDM_Fixed_vs_Updatable_Content_Plan_v1.0.0_20261121.md`.

## 12. Phân tích bổ sung cho mục 9.1, 9.2, 9.4 (24/11/2026)

**9.3 đã chốt (Ben):** chỉ tiếng Việt. Hệ quả: bỏ chi phí duy trì cặp VI/EN; thuật ngữ Anh giữ trong `glossary.yml` và ghi lần đầu trong ngoặc; không cần script kiểm cặp ngôn ngữ.

**Số đo từ nội dung hiện có (đếm từ khóa trong `docs/chapters/ch00–ch07`):**
- Tái lập/reproducibility: 1 lần ở mỗi chương, riêng ch1 có 9.
- Quản trị dữ liệu/steward: tập trung ở ch1 (29), các chương khác 0–4.
- Luật/Nghị định: ch5 có 8 lần, còn lại 0–3; pháp lý chưa có chương riêng.
- Ngân hàng mẫu/biobank: 0 ở mọi chương. Genom/omics/DICOM/hình ảnh y: 0–3.
- Đối tượng của syllabus hiện tại: sinh viên BME/CNTT y tế/khoa học dữ liệu, bác sĩ, học viên cao học, nghiên cứu sinh, điều phối viên nghiên cứu lâm sàng.
Các số này chỉ cho biết chủ đề nào mỏng, không chứng minh chủ đề đó cần có chương riêng.

## 13. Quyết định của Ben (24/11/2026)

| Câu | Quyết định | Hệ quả cho kế hoạch |
|---|---|---|
| 9.1 Định vị | **Phương án C:** chuyên khảo là bản chính; quiz, lab, mini-course là lớp phái sinh | Một nguồn chân lý ở repo gốc; thêm kiểm khớp khi sửa chương để mini-course không lệch |
| 9.2 Quy mô | **Phương án 2:** 7 chương hiện có + 2 chương mới ("Quản trị và pháp lý Việt Nam", "Tái lập và phần mềm nghiên cứu") | Hai chương mới chỉ viết sau chương mẫu (GĐ2) và sau thẩm định mục lục 3 bậc |
| 9.3 Ngôn ngữ | Chỉ tiếng Việt | Không cần kiểm cặp VI/EN |
| 9.4 Tác giả | **Có đồng tác giả, bổ sung sau** | Chưa dựng `CODEOWNERS`; `chapter-map.yml` có sẵn trường `owner` (để trống) và `reviewers`; `editorial/review-policy.md` viết sẵn luồng đa người duyệt nhưng ghi "chưa áp dụng" cho đến khi có danh sách đồng tác giả |

**Còn chờ:** danh sách đồng tác giả và phân công chương; hình thức xuất bản, license và DOI; case study DrMayDay; reviewer ngoài; số câu mỗi bài và quy tắc 24/34 của mini-course.

## 14. Mô hình hai lớp nội dung (đề xuất của Ben, 24/11/2026; phân tích của người soạn)

**Nguyên tắc:** tách sách thành lớp **cốt lõi** (khái niệm, nguyên lý, phương pháp, sự kiện lịch sử; ít đổi) và lớp **cập nhật** (kết quả nghiên cứu hiện hành, tiêu chuẩn và phiên bản, quy định, mẫu nhà tài trợ, công cụ, URL; đổi thường xuyên). Đây là mở rộng của `docs/plans/RDM_Fixed_vs_Updatable_Content_Plan_v1.0.0_20261121.md` (mới áp dụng cho ch01 và 4 phụ lục `legal`, `funder-templates`, `retention`, `standards`), nâng lên thành nguyên tắc tổ chức cả cuốn.

**Điểm cần làm rõ khi áp dụng:** kết quả nghiên cứu có hai loại. Kết quả mang tính lịch sử (ví dụ khảo sát tái lập của Baker 2016, vụ Surgisphere) là sự kiện đã xảy ra, thuộc lớp cốt lõi. Kết quả mô tả hiện trạng hoặc "tốt nhất hiện nay" (benchmark, tỷ lệ áp dụng, hiệu năng công cụ, đánh giá của nguồn mới) thuộc lớp cập nhật.

### 14.1. Phân loại nội dung
- **Cốt lõi:** khái niệm, nguyên lý, phương pháp, logic lập luận, sự kiện lịch sử (ví dụ khảo sát tái lập Baker 2016, vụ Surgisphere).
- **Cập nhật:** văn bản pháp lý và chính sách, mẫu nhà tài trợ, phiên bản chuẩn và công cụ, URL, kết quả mô tả hiện trạng hoặc "tốt nhất hiện nay" (tỷ lệ áp dụng, benchmark, hiệu năng).

### 14.2. Mô hình đề xuất: Phần cốt lõi + Sổ cập nhật
- **Phần cốt lõi:** các chương, phát hành theo ấn bản (1.0, 2.0...), mỗi ấn bản có DOI.
- **Sổ cập nhật:** mỗi mục có `id`, chương liên quan, nhận định, nguồn, trạng thái (`VERIFIED`, `CONTENT_PENDING`...), `as_of`, `review_by`, người phụ trách. Năm nhóm: pháp lý và chính sách; mẫu nhà tài trợ; chuẩn và phiên bản công cụ; bằng chứng hiện hành; liên kết và URL.
- Thân chương chỉ viết khẳng định cố định và dẫn tới mục sổ bằng neo ổn định (dạng `[[upd:id]]`); mỗi chương có hộp "Cập nhật liên quan" kèm ngày chốt.
- Bản cập nhật định kỳ đánh số (ví dụ "Cập nhật 2027-1") kèm ghi chú thay đổi; cách trích dẫn là "ấn bản + ngày cập nhật".
- Quiz và mini-course chỉ dùng lớp cốt lõi; lab đọc mẫu từ sổ tại thời điểm thực hành.

### 14.3. Tác động tới các quyết định đang chờ
- Chương pháp lý Việt Nam chỉ dạy nguyên lý ổn định; danh sách văn bản cụ thể nằm trong sổ.
- Bảng bằng chứng mục 5 của ch01 (PR #28): gắn nhãn Cốt lõi hoặc Cập nhật cho từng dòng; dòng cập nhật chuyển sang sổ.
- `review-policy`: hai loại PR (sửa lớp cốt lõi cần tác giả hoặc chuyên gia duyệt; sửa sổ cập nhật cần nguồn chính thống kèm ngày, quy trình nhẹ hơn).
- Công cụ: mở rộng `check_volatile.py` quét `docs/syllabus/`, mục lục và thân chương; thêm `check_updates.py` (trường bắt buộc, neo trỏ đúng mục, `review_by` quá hạn).

### 14.4. Rủi ro và cách giảm
| Rủi ro | Cách giảm |
|---|---|
| Người đọc phải nhảy giữa hai lớp | Hộp "Cập nhật liên quan" trong mỗi chương |
| Bản in không cập nhật được | Ảnh chụp sổ ở ngày in, DOI và mã trỏ tới bản web |
| Phân loại sai (ví dụ ALCOA đến ALCOA++, FAIR mở rộng) | Lớp cốt lõi vẫn rà 2-3 năm |
| Công sức bảo trì sổ | Chu kỳ 6 tháng, người phụ trách từng nhóm, script báo mục quá hạn |
| Lệch giữa chương và sổ | Neo `[[upd:...]]` bắt buộc, script báo neo mất hoặc mục mồ côi |

### 14.5. Quyết định cần chốt (đề xuất mặc định của người soạn)
| Câu | Nội dung | Đề xuất |
|---|---|---|
| D1 | Tên hai phần | "Phần cốt lõi" và "Sổ cập nhật" |
| D2 | Chu kỳ rà lớp cập nhật | 6 tháng cố định, cộng rà ngay khi có văn bản hoặc phiên bản mới |
| D3 | Định dạng sổ | Dữ liệu có cấu trúc (YAML), sinh trang đọc được |
| D4 | Kết quả nghiên cứu hiện hành | Vào sổ, nhóm "bằng chứng hiện hành"; kết quả lịch sử ở lại thân chương |
| D5 | Bản in | Ảnh chụp sổ ở ngày in, DOI, mã trỏ tới bản web |
| D6 | Thứ tự làm | Dựng hạ tầng sổ (GĐ1b) trước khi nâng cấp ch03-ch07 |

## 15. Tổng hợp review độc lập của bên thực hiện và khuyến nghị đã hiệu đính (24/11/2026)

**Về độ tin cậy của hai báo cáo (bên thực hiện):** các phát hiện về vòng đời 7 giai đoạn, NIH 6 so với 7 yếu tố, thứ tự chương và vai trò ch00/ch07 được xác nhận. Sai sót đã sửa: baseline `57b54b1` và câu "chưa có `editorial/`" lỗi thời (nay `main` ở `aef5ae2`, đã có `editorial/` từ PR #27); số "48.700 từ" không tái lập (con số đó đã gồm 3 file chưa theo dõi của case study; số tái lập được là khoảng 43.700 từ); mục lục dự thảo đặt ch04 trước ch03 trong bảng nhưng ghi thứ tự đọc 3 trước 4; câu về tính đúng đắn khoa học vượt bằng chứng.

**Điểm bên thực hiện khác người soạn và quyết định chấp nhận:**
| Chủ đề | người soạn (trước) | bên thực hiện | Kết luận hiệu đính |
|---|---|---|---|
| Neo `[[upd:id]]` | Đề xuất làm neo | Quarto và VitePress đều không hỗ trợ; chưa có marker nào trong repo | **Chấp nhận bên thực hiện:** dùng liên kết Markdown chuẩn tới mục của Sổ cập nhật được sinh tự động (ví dụ `../updates/funder.md#nih-dmsp`), kiểm bằng script; không tạo cú pháp riêng |
| Chu kỳ rà (D2) | 6 tháng cố định | Theo rủi ro | **Chấp nhận:** pháp lý 3–6 tháng, chuẩn và công cụ 6 tháng, nội dung nền 12–24 tháng, cộng rà ngay khi nguồn đổi (`review_cycle_days` theo từng mục) |
| Schema sổ (D3) | 8 trường | Thêm trường | **Chấp nhận:** thêm `anchor`, `classification`, `source_type`, `source_url`, `evidence_scope`, `checked_at` (khác `as_of`), `jurisdiction`, `version`, `supersedes`, `blocking_reason`, `change_log`, `citation_key`; kèm JSON Schema và trang Markdown sinh tự động |
| Quy tắc phân loại | Hai mục | Thêm quy tắc | **Chấp nhận:** "nếu người đọc cần biết thông tin này còn đúng tại ngày nào thì nó phải có bản ghi cập nhật; nếu chỉ cần hiểu cơ chế hoặc lịch sử thì ở lớp cốt lõi"; ca biên (định nghĩa ổn định nhưng tên phiên bản đổi; quy trình ổn định nhưng công cụ đổi) tách đôi |
| Bản in (D5) | Ảnh chụp sổ | Cutoff, commit hash, manifest sổ, DOI của artifact cụ thể | **Chấp nhận** |
| Thứ tự làm (D6) | Dựng hạ tầng cho cả sách | Dựng tối thiểu trên ch01, thử render cả hai pipeline | **Chấp nhận:** làm pilot trên ch01 (chương mẫu) trước |
| Đánh số chương (Q-B) | B1 | Thêm phương án mã ổn định + số hiển thị sinh từ `chapter-map.yml`; đo 129 dòng `ch0N`, 58 dòng "Chương N", 18 dòng "Hình N" | **Giữ B1 nhưng nêu chi phí:** khoảng 200 dòng cần đổi; làm bằng script một lần trước khi nâng cấp tiếp. Phương án của bên thực hiện tránh đổi tên tệp nhưng làm số chương lệch mã; Ben quyết |
| Mục tiêu GĐ4 | "không còn CONTENT_PENDING" | Không nên là KPI | **Chấp nhận:** mục tiêu là mọi mục pending được giải quyết hoặc ghi rõ trong "Giới hạn và vấn đề mở" kèm lý do, không phải số 0 |
| Quy trình thiếu | | `check_claims.py` chưa tồn tại; `_quarto.yml` chỉ HTML; thiếu kiểm PDF/DOCX; reviewer cần tiêu chí độc lập, văn bản trả lời từng phát hiện | **Chấp nhận:** thêm cổng nghiệm thu `G-1…G-8` (baseline, schema sổ, audit thư mục, render Quarto và VitePress, đồng bộ khóa học, reviewer ký theo phạm vi, render PDF/DOCX có kiểm trực quan, errata) |

**Quyết định Ben cần chốt (xếp hạng):**
1. Định nghĩa vòng đời 7 giai đoạn (Q-A, đề xuất A1) và bảng ánh xạ giai đoạn ↔ chương.
2. Đánh số chương (Q-B): B1 (đổi số theo thứ tự đọc, ~200 dòng) hay mã ổn định và số hiển thị sinh tự động.
3. Vai trò ch00/ch07 (Q-C, đề xuất C1: lời nói đầu và chương tích hợp, quiz và capstone sang học liệu đi kèm).
4. Mô hình hai lớp: tên (D1), chu kỳ theo rủi ro (D2), schema và định dạng (D3), kết quả nghiên cứu (D4), bản in (D5), pilot trên ch01 (D6).
5. Reviewer bắt buộc cho chương pháp lý và tái lập; tiêu chí độc lập và xung đột lợi ích.
6. Các tệp chưa theo dõi trong clone chính (case study DrMayDay, DMPTool, quiz Gemini cũ): có thuộc dự án và sẽ vào sách không.
