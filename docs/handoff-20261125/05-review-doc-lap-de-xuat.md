## 1. Tóm tắt và khuyến nghị

1. Hai báo cáo có giá trị định hướng, nhưng chưa đủ tin cậy để dùng làm kế hoạch triển khai ngay.
2. Báo cáo thẩm định xác định đúng các mâu thuẫn lớn về vòng đời 7 giai đoạn, NIH DMSP và thứ tự chương.
3. Một số số liệu trong báo cáo đề xuất đã lỗi thời: báo cáo ghi baseline `57b54b1`, trong khi repo hiện tại là `aef5ae2`.
4. Báo cáo đề xuất vẫn mô tả repo như chưa có `editorial/`, dù thư mục này đã tồn tại trên `main`.
5. Phần hai lớp “cốt lõi + cập nhật” là hướng phù hợp, nhưng tiêu chí phân loại và schema sổ cập nhật chưa đủ chặt.
6. Neo `[[upd:id]]` hiện chưa được hỗ trợ bởi Quarto hoặc VitePress; chưa có marker nào trong repo.
7. Mục lục dự thảo có mâu thuẫn thứ tự: bảng đặt chương 4 trước chương 3, nhưng phần mô tả đọc lại đặt 3 trước 4.
8. Quy trình GD0–GD6 có cổng kiểm soát hợp lý nhưng thiếu các bước nghiệm thu bắt buộc cho bibliography, render, đồng bộ web và reviewer chuyên môn.
9. Không nên coi các kết luận pháp lý/NIH là đã xác minh đầy đủ; chính báo cáo thẩm định thừa nhận chưa mở văn bản gốc.
10. Khuyến nghị: chốt lại baseline, Q-A/Q-B/Q-C, schema cập nhật và tiêu chí nghiệm thu trước khi nâng cấp chương.

---

## 2. Bảng xác minh A

| Mã | Kết luận | Bằng chứng độc lập | Nhận xét |
|---|---|---|---|
| T1-1 | Đúng | `docs/chapters/ch00_getting_started.md:23-28`; `docs/chapters/ch01_overview_and_dmp.md:31-40` | Ch00 dùng G3 làm làm sạch/chất lượng, G5 FAIR, G6 pháp lý; ch01 dùng G5 phân tích/tái lập, G6 FAIR và pháp lý là lớp ngang. |
| T1-2 | Đúng | `docs/chapters/ch01_overview_and_dmp.md:20,154`; `docs/chapters/ch01_overview_and_dmp.md:254-265`; `docs/chapters/rdm-phu-luc-b-bo-sung-dmptool-templates.md:23-27` | Có đồng thời “7 yếu tố” hiện hành và “sáu thành tố” cũ. Cần phân biệt rõ theo thời điểm áp dụng. |
| T1-3 | Đúng một phần | `editorial/chapter-map.yml:5-11`; số đo thực tế: ch01–ch06 = 35.356 từ; appendices = 5.038 từ; tổng = 40.394 từ | Các số đo chương trong báo cáo đúng. Con số 38.300 trong syllabus đã lỗi thời. Con số 48.700 trong báo cáo đề xuất không tái lập được từ phạm vi hiện tại (`RDM_De_Xuat...:10`). |
| T1-4 | Đúng một phần | `editorial/chapter-map.yml:10`; `README.md:18`; `docs/syllabus/BIOMEDICAL_RDM_FREE_SELF_PACED_SYLLABUS.md:13` | Ch06 mang role `governance` nhưng nội dung chính là FAIR/AI-ready; license đã được ghi CC BY 4.0/MIT. Tuy nhiên nhận định “chưa có editorial” trong báo cáo đề xuất đã sai do dùng baseline cũ (`RDM_De_Xuat...:23-24`). |
| T3-1 | Đúng | `docs/chapters/ch04_quality_and_imputation.md:20,123-129`; `docs/chapters/ch03_standards_cdisc_fhir_omop.md:125-130` | Ch04 dùng DQD trên OMOP nhưng `chapter-map.yml` chưa khai báo ch04 phụ thuộc ch03. Đây là mâu thuẫn giữa nội dung và metadata. |
| T3-2 | Đúng | `docs/chapters/ch00_getting_started.md:1,21-28`; `docs/chapters/ch07_completion_and_capstone.md:1,10-16` | Ch00 là phần nhập môn khóa học; ch07 chủ yếu là quiz/capstone. Đề xuất coi chúng là phần mở đầu/phụ trợ là hợp lý. |
| T3-3 | Đúng một phần | `docs/chapters/ch05_privacy_and_deidentification.md:87-129`; đo lại đoạn này = 1.099 từ trên tổng 5.972 từ | Phần pháp lý hiện có đúng là phần nhỏ của ch05; chương pháp lý mới sẽ cần nội dung và reviewer mới. |
| T3-4 | Đúng một phần | `docs/chapters/ch01_overview_and_dmp.md:58-63`; `docs/chapters/ch04_quality_and_imputation.md:123-129`; `docs/chapters/ch06_fair_and_ai_ready.md:108-128` | Ranh giới tái lập đang chồng lấn. Các con số tần suất từ khóa trong báo cáo chưa tái lập đầy đủ bằng cùng một quy tắc đếm. |
| T3-5 | Đúng | `editorial/chapter-map.yml:5-11`; số đo thực tế ch02 = 8.490 từ, các chương còn lại = 2.403–5.972 từ | Ch02 dài đáng kể, nhưng chưa đủ bằng chứng để kết luận phải tách. |
| T3-6 | Đúng | `docs/syllabus/BIOMEDICAL_RDM_FREE_SELF_PACED_SYLLABUS.md:35-40`; `editorial/chapter-map.yml:12-13` | Đối tượng hiện tại gồm sinh viên, bác sĩ, người mới và điều phối viên; hai chương mới chưa có mục tiêu năng lực. |
| T3-7 | Đúng | `docs/chapters/ch07_completion_and_capstone.md:16-20` | Q1 có 5 mục, không biểu đạt rõ bước làm sạch/chất lượng. |

Các kiểm tra đã chạy:

- `check_structure.py --check`: exit 0, nhưng có WARN ở ch01–ch06.
- `check_crossrefs.py --check`: exit 0.
- `check_glossary.py --check`: exit 0, 9 nhóm WARN.
- `check_volatile.py --check`: exit 0, 0 vi phạm.
- `check_quizzes.py --check`: exit 0, 39 câu chương và 24 câu mini-course.
- `git diff --check`: exit 0.
- `audit_references.py`: exit 1 vì cố ghi `references/AUDIT-REPORT.md` trong môi trường chỉ đọc; không được coi là audit mới. Báo cáo audit hiện tại vẫn là bản cũ, `references/AUDIT-REPORT.md`.

---

## 3. Phát hiện mới

### Cao

| Mã | Vị trí | Bằng chứng | Khuyến nghị |
|---|---|---|---|
| N-01 | Baseline của báo cáo đề xuất | Báo cáo ghi `main @ 57b54b1` tại `RDM_De_Xuat...:5`; repo hiện tại là `aef5ae2`, có PR #27 mới hơn | Chạy lại toàn bộ review trên cùng một commit và ghi rõ phạm vi. |
| N-02 | Mô tả trạng thái repo | Báo cáo đề xuất nói chưa có `editorial/` tại `RDM_De_Xuat...:23-24`; thực tế có `editorial/chapter-map.yml`, `style-guide.md`, `notation.md`, `glossary.yml`, `review-policy.md` | Loại bỏ các kết luận dựa trên snapshot cũ. |
| N-03 | Mô hình hai lớp | `RDM_De_Xuat...:197-205` chưa quy định đủ cách xử lý định nghĩa, số liệu, phiên bản chuẩn, benchmark, ví dụ và nội dung có cả lịch sử lẫn hiện trạng | Bổ sung decision tree và trường bắt buộc cho từng loại claim. |
| N-04 | Neo cập nhật | Tìm kiếm toàn repo không có `[[upd:`; Quarto chỉ liệt kê Markdown tại `_quarto.yml:8-33`; VitePress chỉ cấu hình Markdown, MathJax và Mermaid tại `.vitepress/config.mts:1-15` | Không dùng `[[upd:id]]` trước khi có plugin/filter và test render cho cả hai pipeline. |
| N-05 | Ranh giới “đã xác minh” | Repo hiện có 103 `VERIFIED_UNAUDITED`, 9 `BIB_PENDING`, 3 `PENDING_UNDETERMINED`; báo cáo đề xuất dùng `VERIFIED`/`CONTENT_PENDING` nhưng chưa mô tả quan hệ giữa các trạng thái (`RDM_De_Xuat...:19-20,202`) | Giữ nguyên trạng thái hiện có; thêm `evidence_scope`, `checked_at`, `blocking_reason`, `source_type`, `source_url`, `supersedes`. |

### Trung bình

| Mã | Vị trí | Bằng chứng | Khuyến nghị |
|---|---|---|---|
| N-06 | Mục lục dự thảo | Bảng mục lục đặt ch02, ch04 trong Phần II rồi ch03 ở Phần III; phần cuối lại ghi thứ tự 1 → 2 → 3 → 4 (`RDM_Tham_Dinh...: mục 6`) | Chọn một thứ tự duy nhất và thể hiện cùng thứ tự trong bảng, `chapter-map.yml`, `_quarto.yml` và web. |
| N-07 | Số liệu thời lượng | Syllabus vẫn ghi khoảng 38.300 từ tại `docs/syllabus/BIOMEDICAL_RDM_FREE_SELF_PACED_SYLLABUS.md:69`, trong khi đo hiện tại là 40.394 từ cho chương + phụ lục | Bỏ số cứng hoặc sinh tự động từ manifest. |
| N-08 | Quy trình nghiệm thu | GD3–GD6 tại `RDM_De_Xuat...:100-109` không ghi rõ phải chạy `audit_references.py`, `quarto render`, đồng bộ khóa học và build VitePress | Bổ sung lệnh, điều kiện pass/fail và artifact lưu lại. |
| N-09 | Chất lượng reviewer | GD5 chỉ yêu cầu 2–3 chuyên gia ngoài nhưng chưa nêu tiêu chí độc lập, chuyên môn, xung đột lợi ích, phản hồi bắt buộc | Áp dụng yêu cầu reviewer không phải người viết từ quy trình HMYT. |
| N-10 | Bản in/DOI | `RDM_De_Xuat...:201-204,217` nói DOI cho từng phiên bản và “ảnh chụp sổ”, nhưng chưa định nghĩa snapshot hash, ngày cắt dữ liệu, phiên bản sổ và cách trích dẫn | Phát hành bản in kèm manifest/snapshot bất biến; DOI trỏ tới artifact cụ thể, không chỉ tới trang web động. |

### Thấp

| Mã | Vị trí | Bằng chứng | Khuyến nghị |
|---|---|---|---|
| N-11 | Thuật ngữ | `check_glossary.py --check` báo 26 thuật ngữ `vi_status=proposed` và các viết tắt CRC, OBJECTIVES, OUTCOMES, NAM, CAPSTONE | Xử lý trong PR editorial riêng, không gộp vào quyết định cấu trúc. |
| N-12 | Chương mẫu | `check_structure.py --check` báo thiếu số mục 6 ở ch01/ch04/ch06 và thiếu dẫn chiếu cho nhiều caption | Chốt quy tắc cấu trúc trước khi nhân rộng khung. |
| N-13 | Tệp chưa được theo dõi | `git status --short` cho thấy các tệp case study, quiz và syllabus mới đang untracked | Xác định rõ chúng có thuộc baseline review hay không trước khi dùng làm bằng chứng. |

---

## 4. Review B — mô hình hai lớp

### 4.1. Tiêu chí hiện tại

Tiêu chí trong `RDM_De_Xuat...:192-199` có nền tảng tốt:

- Cốt lõi: khái niệm, nguyên lý, phương pháp, logic, sự kiện lịch sử.
- Cập nhật: luật, chính sách, mẫu tài trợ, phiên bản chuẩn/công cụ, URL, benchmark và hiện trạng.

Điểm thiếu là chưa có quy tắc cho các trường hợp biên:

- Định nghĩa có thể ổn định nhưng tên/phiên bản của tiêu chuẩn thay đổi.
- Một kết quả lịch sử có thể nằm ở cốt lõi, nhưng con số/tỷ lệ cụ thể cần bản ghi cập nhật.
- Phương pháp có nguyên lý ổn định nhưng API, phần mềm hoặc phiên bản triển khai thay đổi.
- Quy định pháp lý có thể được trích dẫn lịch sử trong phần cốt lõi nhưng hiệu lực hiện tại phải nằm trong sổ cập nhật.
- Ví dụ minh họa có thể trở thành lỗi thời nếu dựa trên công cụ hoặc luật cụ thể.

Nên dùng quy tắc: “Nếu người đọc cần biết thông tin này còn đúng tại ngày nào, nó phải có bản ghi cập nhật; nếu chỉ cần hiểu cơ chế hoặc lịch sử, nó có thể ở cốt lõi.”

### 4.2. Mười ví dụ phân loại

| Ví dụ | Vị trí | Phân loại | Ghi chú |
|---|---|---|---|
| Protocol–DMP–CRF là ba loại tài liệu khác nhau | `ch01:17`, `ch01:140-147` | Cốt lõi | Khái niệm ổn định. |
| Bốn trụ cột FAIR | `ch06:68-80` | Cốt lõi | Nguyên lý nền tảng. |
| Vai trò FHIR, CDISC, OMOP | `ch03:14-19` | Cốt lõi | Mô hình chức năng, không phải phiên bản. |
| MCAR/MAR/MNAR và logic missing data | `ch04` | Cốt lõi | Phương pháp nền tảng. |
| OMOP CDM v5.4 | `ch03:127-130` | Cập nhật | Phiên bản cần ngày chốt và nguồn chính thức. |
| DQD có hơn 3.300 quy tắc | `ch04:125-129` | Cập nhật | Số lượng phụ thuộc phiên bản; hiện đã được đánh dấu minh họa/pending. |
| Mã concept Athena/SNOMED/LOINC | `ch03:329-334` | Cập nhật | Có thể thay đổi hoặc cần xác minh từng mã. |
| Luật 91/2025/QH15 và Nghị định 356/2025/NĐ-CP | `ch05`, `docs/appendices/legal.md` | Cập nhật | Phải kèm ngày kiểm tra, hiệu lực và nguồn chính thức. |
| NIH DMSP 7 yếu tố | `ch01:20`, `ch01:254-265` | Cập nhật | Phụ thuộc mẫu và thời điểm áp dụng. |
| FAIRification 7 bước | `ch06:108-128` | Cốt lõi + cập nhật | Quy trình là cốt lõi; tên công cụ, maturity indicator và benchmark là cập nhật. |

### 4.3. Schema sổ cập nhật

Các trường hiện có tại `RDM_De_Xuat...:202` là cần thiết nhưng chưa đủ. Nên bổ sung:

- `id`
- `chapter`
- `anchor`
- `claim`
- `classification`
- `source`
- `source_type`
- `source_url`
- `evidence_scope`
- `status`
- `checked_at`
- `as_of`
- `review_by`
- `owner`
- `jurisdiction`
- `version`
- `supersedes`
- `blocking_reason`
- `change_log`
- `citation_key`

`as_of` không thay thế `checked_at`: một trường là ngày nội dung có hiệu lực, trường kia là ngày repo kiểm tra.

### 4.4. Phụ lục và bibliography

Có ba vấn đề:

1. Kế hoạch hiện hành chỉ mới áp dụng rõ cho ch01 và bốn phụ lục tại `docs/plans/RDM_Fixed_vs_Updatable_Content_Plan_v1.0.0_20261121.md:20-56`; báo cáo đề xuất mở rộng cho toàn sách nhưng chưa định nghĩa migration.
2. `citation-audit.csv` là audit cấu trúc/metadata, không phải claim audit. `references/AUDIT-REPORT.md` cũng ghi rõ điều này.
3. Trạng thái trong `citation-audit.csv` không nên bị chuyển thành `VERIFIED` chỉ vì đã có bản ghi trong sổ cập nhật.

### 4.5. Quarto, VitePress và neo

Hiện chưa tương thích thực tế:

- `_quarto.yml:8-33` không có filter xử lý `[[upd:id]]`.
- VitePress `.vitepress/config.mts:1-15` không có markdown-it rule cho neo này.
- Không tìm thấy marker `[[upd:` trong repo.

Giải pháp an toàn hơn là dùng cú pháp Markdown chuẩn, ví dụ link tới trang/sổ cập nhật được sinh tự động. Nếu vẫn dùng neo riêng, phải có:

1. schema;
2. parser/filter Quarto;
3. markdown-it plugin VitePress;
4. test neo tồn tại;
5. test render không để lộ cú pháp thô;
6. cảnh báo mục mồ côi.

### 4.6. Rủi ro chưa được nêu

- Hai lớp có thể dẫn đến hai nguồn chân lý nếu bản cập nhật mâu thuẫn với chương.
- Sổ cập nhật có thể bị bỏ sót khi đổi tên chương hoặc anchor.
- Bản in và bản web có thể không cùng snapshot.
- Nội dung pháp lý có thể bị “đóng băng” nhầm vào lớp cốt lõi.
- Sổ cập nhật có thể chứa URL hỏng, dữ liệu nhạy cảm hoặc thông tin không được phép công khai.
- Không có quy tắc rollback khi một bản cập nhật bị xác định là sai.
- Chưa có ownership thực tế; `owner: null` trong `editorial/chapter-map.yml:5-13`.

---

## 5. Review C — D1–D6 và Q-A/Q-B/Q-C

| Quyết định | Đánh giá | Phương án thứ ba tốt hơn | Chi phí/ảnh hưởng |
|---|---|---|---|
| D1: tên hai lớp | Hợp lý. “Phần cốt lõi” và “Sổ cập nhật” dễ hiểu. | “Nội dung nền” + “Bản tin cập nhật” nếu ưu tiên độc giả phổ thông. | Thấp: chủ yếu đổi heading, glossary và template. |
| D2: chu kỳ 6 tháng | Quá cứng cho mọi loại dữ liệu. Luật/công cụ có thể cần rà ngay; nguyên lý có thể 12–24 tháng. | Chu kỳ theo rủi ro: pháp lý 3–6 tháng, công cụ/chuẩn 6 tháng, nội dung nền 12–24 tháng; có trigger khi nguồn đổi. | Trung bình: thêm trường `review_cycle_days` và trigger. |
| D3: YAML có cấu trúc | Phù hợp với repo hiện tại. | YAML + JSON Schema + trang Markdown sinh tự động. | Trung bình: thêm validator và generator. |
| D4: đưa kết quả hiện hành vào sổ | Đúng hướng nhưng “kết quả nghiên cứu” còn quá rộng. | Tách “bằng chứng lịch sử” và “ước lượng hiện hành”; chỉ loại sau có `as_of`, phạm vi và trạng thái. | Trung bình: phân loại lại claim trong ch01/ch04/ch06. |
| D5: bản in là snapshot | Hợp lý nhưng “ảnh chụp sổ” chưa đủ cho trích dẫn. | Bản in có cutoff date, commit hash, manifest sổ và DOI của artifact. | Cao khi xuất bản lần đầu; thấp cho các bản sau. |
| D6: dựng sổ trước ch03–ch07 | Hợp lý về kiến trúc. | Dựng schema tối thiểu trên ch01, thử render, rồi mới mở rộng. | Thấp–trung bình; giảm rủi ro xây sai hệ thống. |

### Q-A — vòng đời 7 giai đoạn

- A1 là phương án tốt nhất.
- A2 giữ được thứ tự cũ nhưng coi pháp lý là một bước độc lập, dễ làm sai bản chất “lớp ngang”.
- A3 tạo thêm thay đổi lớn mà chưa có lợi ích rõ.
- Khuyến nghị: chọn A1, nhưng ghi rõ “pháp lý, đạo đức, bảo mật và quản trị là lớp ngang”; đồng thời tách “phân tích/tái lập” khỏi “FAIR/chia sẻ” bằng bảng ánh xạ.

### Q-B — đánh số chương

- B1 có logic đọc tốt nhất nhưng chi phí migration cao.
- B2 ít thay đổi nhất nhưng giữ thứ tự đọc không tự nhiên.
- B3 giữ mã ổn định nhưng tạo chênh lệch giữa mã, số chương, caption và cross-reference.
- Phương án thứ ba: giữ mã định danh ổn định (`ch01`, `ch02`…) nhưng sinh số hiển thị từ `chapter-map.yml`, hoặc dùng phần/chương có tên thay vì buộc số hiển thị trùng mã.
- Đo sơ bộ phạm vi thay đổi trong repo hiện tại: 129 dòng khớp `ch0N`, 58 dòng khớp “Chương N”, 18 dòng khớp “Hình N”; ngoài ra còn glossary, notation, quiz, scripts và `_quarto.yml`. Con số này chưa bao gồm repo khóa học nếu phải đồng bộ thủ công.

### Q-C — vai trò ch00/ch07

- C1 phù hợp nhất với sách chuyên khảo và quyết định “sách là bản chính”.
- C2 giữ được trải nghiệm khóa học nhưng làm lẫn sách với học liệu.
- C3 làm mất hướng dẫn đọc và phần tích hợp.
- Phương án thứ ba: giữ ch00 và ch07 nhưng chuyển thành “Lời nói đầu/Hướng dẫn đọc” và “Tổng kết tích hợp”, không tính như chương nội dung chính.

---

## 6. Review D — mục lục và kiến trúc chương

Mục lục dự thảo có hướng hợp lý:

- Nền tảng → thu thập → chuẩn/liên thông → quản trị/pháp lý → FAIR/AI → tái lập → tích hợp.
- Ch02 không nên tách ngay chỉ vì dài 8.490 từ; trước hết cần xem có hai mục tiêu độc lập, hai nhóm người đọc hoặc hai chu trình thực hành hay không.
- Ch04 cần khai báo phụ thuộc ch03 nếu nội dung DQD/OMOP là điều kiện tiên quyết.
- Ch05 nên tập trung vào bảo mật, khử định danh và kiểm soát truy cập.
- Chương pháp lý mới cần ranh giới rõ với ch05: luật/chính sách và nghĩa vụ pháp lý, không lặp lại kỹ thuật khử định danh.
- Chương tái lập cần giới hạn vào môi trường, phiên bản, provenance, mã nguồn và quy trình; không lặp phần động lực ở ch01.

Các điểm cần bổ sung trong outline:

- mục tiêu năng lực cho ch08/ch09;
- dependency graph chính thức;
- quy tắc xử lý nội dung cập nhật trong từng chương;
- vị trí của phụ lục trong bản in và web;
- cách liên kết sách chính với quiz/lab/mini-course phái sinh;
- định nghĩa “chương tích hợp” khác gì so với capstone hiện tại.

---

## 7. Review E — quy trình GD0–GD6

### Điểm phù hợp

- Có cổng duyệt mục lục trước khi viết: `RDM_De_Xuat...:100-104`.
- Có chương mẫu trước khi nhân rộng: `:105`.
- Có PR theo chương: `:106`.
- Có xác minh pháp lý/NIH/OMOP/EHDS riêng: `:107`.
- Có review độc lập: `:108`.
- Có render thật trước xuất bản: `:109`.

Những điểm này phù hợp với HDBS và HMYT về single source, PR, review độc lập, kiểm tra render và không coi DOI là bằng chứng nội dung.

### Thiếu hoặc còn yếu

1. GD1 nói đến `check_claims.py` nhưng script này chưa tồn tại.
2. GD1 chưa chỉ rõ `audit_references.py`, `check_crossrefs.py`, `check_quizzes.py`, `quarto render` và build VitePress là điều kiện nào.
3. GD3 ghi “audit mức nhận định hoàn tất” nhưng chưa có format artifact, trạng thái và người ký xác nhận.
4. GD4 dùng cụm “không còn `CONTENT_PENDING` trong thân sách”, nhưng trạng thái pending có thể cần được giữ lại nếu chưa có nguồn gốc; không nên biến mục tiêu “không còn pending” thành KPI bắt buộc.
5. GD5 chưa yêu cầu reviewer chuyên môn trả lời bằng văn bản từng phát hiện.
6. GD6 yêu cầu PDF/DOCX/DOI/license nhưng `_quarto.yml` hiện chỉ cấu hình HTML; chưa có bằng chứng Typst/DOCX render hoạt động.
7. Quy trình HDBS có bước kiểm tra trực quan PDF để bắt lỗi glyph; đề xuất mới chỉ nói “kiểm render thật”, chưa nêu trang mẫu, công thức, Mermaid, bảng và font.
8. Quy trình HMYT yêu cầu phân biệt reviewer khoa học, kỹ thuật và người merge; đề xuất chưa gán rõ các vai trò này.

### Các bước nên thêm

- `G-1`: khóa commit baseline và inventory đầu vào.
- `G-2`: validate schema sổ cập nhật và kiểm tra neo.
- `G-3`: chạy bibliography structural audit.
- `G-4`: chạy Quarto render và build VitePress.
- `G-5`: kiểm tra đồng bộ repo khóa học.
- `G-6`: reviewer khoa học/pháp lý/kỹ thuật ký từng phạm vi.
- `G-7`: render PDF/DOCX, kiểm tra trực quan và tạo manifest release.
- `G-8`: ghi errata/changelog sau phát hành.

---

## 8. Review F — tính chính xác và trung thực

### Điểm đáng tin cậy

- Báo cáo thẩm định tự ghi rõ giới hạn: chưa mở văn bản pháp lý/NIH gốc và chưa kiểm chứng khoa học từng nhận định (`RDM_Tham_Dinh...` phần mở đầu).
- Báo cáo đề xuất cũng thừa nhận chưa có claim audit (`RDM_De_Xuat...:19-20,111-112`).
- `VERIFIED_UNAUDITED` được phân biệt với xác minh nội dung trong `docs/PROJECT-STATE.md:63`.

### Điểm cần chỉnh

1. Câu “không có phát hiện nào cho thấy nội dung 7 chương hiện tại sai về khoa học” trong báo cáo thẩm định là quá mạnh, vì cùng báo cáo nói chưa kiểm chứng khoa học từng nhận định. Nên viết: “Chưa đánh giá trong phạm vi review này.”
2. Các dòng “khớp” về luật/NIH trong báo cáo thẩm định chỉ nên là “khớp với hồ sơ kiểm tra hiện có”; không được coi là xác minh pháp lý mới.
3. `docs/legal-verification.md` có các trạng thái “XÁC NHẬN”, “XÁC NHẬN MỘT PHẦN” và “KHÔNG TÌM ĐƯỢC NGUỒN CHÍNH THỨC”, nhưng phần giải thích vẫn giới hạn theo từng chi tiết. Không được suy rộng thành xác nhận toàn bộ văn bản.
4. Báo cáo đề xuất ghi “115 tài liệu tham khảo” tại `:10`, nhưng trạng thái thực tế gồm 103 `VERIFIED_UNAUDITED`, 9 `BIB_PENDING`, 3 `PENDING_UNDETERMINED`; không nên trình bày như 115 tài liệu đã sẵn sàng.
5. Các tuyên bố pháp lý mới được đề cập trong báo cáo thẩm định phải tiếp tục giữ trạng thái “chưa kiểm tra” cho đến khi mở nguồn gốc; theo brief này không thực hiện web verification.

---

## 9. Danh sách quyết định Ben cần chốt

### Ưu tiên 1 — bắt buộc trước triển khai

1. Chốt định nghĩa vòng đời 7 giai đoạn và bảng ánh xạ giai đoạn–chương.
2. Chốt B1, B2 hay phương án mã ổn định/số hiển thị sinh tự động.
3. Chốt schema và quy tắc phân loại cốt lõi/cập nhật.
4. Chốt bản in là snapshot nào, cách gắn commit/hash/DOI và cách trích dẫn.
5. Chốt reviewer bắt buộc cho ch08 pháp lý, ch09 tái lập và các claim kỹ thuật.

### Ưu tiên 2 — cần chốt trước khi mở rộng chương

6. Vai trò cuối cùng của ch00/ch07.
7. Có tách ch02 hay không, sau khi đọc nội dung đầy đủ.
8. Chu kỳ review theo rủi ro thay cho “6 tháng cố định”.
9. Phạm vi build chính thức: HTML, PDF, DOCX, EPUB, JATS hay chỉ một số định dạng.
10. Quy tắc đồng bộ sách chính với quiz/lab/mini-course.

### Đề xuất khác với báo cáo hiện tại

- Không coi “6 tháng cố định” là chính sách chung.
- Không dùng `[[upd:id]]` trước khi có plugin và test.
- Không dùng trạng thái `VERIFIED` cho claim chỉ có metadata hoặc abstract.
- Không đặt mục tiêu “không còn `CONTENT_PENDING`” nếu chưa có nguồn gốc.
- Không mở rộng ch08/ch09 trước khi chốt baseline và dependency graph.
- Không coi số từ, số tài liệu hay số câu quiz là số liệu ổn định nếu chưa sinh tự động.

---

## 10. Điều chưa kiểm tra

- Chưa tra web hoặc mở văn bản pháp lý/NIH gốc, theo đúng brief.
- Chưa kiểm chứng nội dung khoa học của từng claim.
- Chưa chạy render PDF/DOCX/Typst vì repo hiện chưa có cấu hình hoàn chỉnh cho các đầu ra đó và review này chỉ đọc.
- Chưa chạy audit bibliography mới vì `scripts/audit_references.py` ghi đè `references/AUDIT-REPORT.md`; môi trường chỉ đọc trả exit code 1.
- Chưa kiểm tra đầy đủ repo khóa học bằng build thật; chỉ đọc `.vitepress/config.mts`.
- Chưa xác định các tệp untracked có thuộc baseline chính thức hay không.
- Chưa đánh giá toàn bộ 7 chương theo nội dung đầy đủ để quyết định tách ch02.
