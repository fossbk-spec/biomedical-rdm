# Hướng dẫn sơ đồ, công thức và quiz cho sách/khóa học web (dùng lại cho các sách khác)

**Người nghiệm thu:** TS. Hoàng Quang Huy (Ben) · **Phiên bản:** 1.1.0 · **Ngày:** 22/11/2026
**Nguồn kinh nghiệm:** dự án Biomedical RDM (repo gốc `biomedical-rdm` dùng Quarto; web `biomedical-rdm-course` dùng VitePress, Pages từ nhánh `gh-pages`).
**Mục đích:** lưu các đề xuất để cập nhật vào quy trình biên soạn các sách khác (hmyt-book, ai4l-book, tdtk…).

## 1. Sơ đồ: khuyến nghị

**Định dạng nguồn: giữ Mermaid** (khối ```mermaid``` trong Markdown).
- Nguồn là văn bản: diff được trong PR, review được, sửa không cần công cụ vẽ.
- Quarto và GitHub dựng Mermaid sẵn, nên cùng một nguồn dùng được ở repo gốc và ở web (VitePress); không phát sinh bản vẽ lệch nhau.
- Hợp với nội dung hay đổi (chuẩn, luật, công cụ).

**Các lựa chọn khác và khi nào dùng**

| Lựa chọn | Khi nào | Ghi chú |
|---|---|---|
| Graphviz (dot) | Sơ đồ cây/đồ thị lớn cần bố cục tự động ổn định | Quarto hỗ trợ sẵn; kiểu dáng kém linh hoạt hơn |
| D2, PlantUML, Kroki | Chỉ khi có hàng chục sơ đồ phức tạp | Cần công cụ dựng riêng; thường không đáng cho ít sơ đồ |
| draw.io / SVG thiết kế tay | Vài hình then chốt (ví dụ vòng đời, khung khái niệm chính) | Lưu cả tệp nguồn (`.drawio`) và `.svg` trong repo; khó diff |
| Excalidraw, D3, Cytoscape | Không dùng | Khó diff, nặng, vượt nhu cầu |

**Quy tắc thiết kế (rút từ lỗi thực tế)**
1. Nhãn ngắn: mỗi nút tối đa 2–3 dòng ngắn; không nhồi danh sách dài vào nút. Sơ đồ ch05 từng cao khoảng 1.700 px và sơ đồ ch03 chỉ còn khoảng 40% khi vừa khung vì nhãn quá dài.
2. Tách sơ đồ lớn thành hai sơ đồ nhỏ thay vì một sơ đồ 4 tầng.
3. Mỗi sơ đồ có tiêu đề và mô tả bằng văn bản (hiển thị và dùng làm văn bản thay thế cho trình đọc màn hình).
4. Không đặt nội dung dễ hết hạn (số hiệu, ngày, phiên bản) trong nhãn sơ đồ; trỏ về phụ lục có ngày chốt.
5. Dùng màu có độ tương phản đủ ở cả chế độ sáng và tối; không dựa vào màu để truyền nghĩa.

## 2. Cách dựng trên web

**Hiện trạng (VitePress):** thành phần `Mermaid.vue` dựng ở trình duyệt với: thu nhỏ/phóng to (cũng Ctrl+cuộn), vừa khung, kéo để di chuyển, toàn màn hình (Esc), mở sơ đồ trong tab mới, tải SVG, xem mã nguồn, theo chế độ sáng/tối. Khối ```mermaid``` được thay bằng thành phần ở quy tắc `fence` của markdown-it.

**Đề xuất nâng cấp**
1. Dựng sẵn thành SVG khi build (`mermaid-cli`, cần trình duyệt không giao diện) thay vì dựng lúc chạy: tốt cho bản in/PDF, offline, không cần JavaScript, nhẹ hơn. Giữ các nút điều khiển.
2. Cân nhắc bố cục ELK cho sơ đồ rộng/phức tạp.
3. Kiểm thêm: điện thoại, Safari/Firefox, chế độ tối bằng ảnh chụp, in/xuất PDF (chưa kiểm ở RDM).

**Cạm bẫy đã gặp**
- Nhãn HTML (foreignObject) bị cắt chữ vì Mermaid đo bằng phông khác phông của trang. Cách sửa: `htmlLabels: false` ở **cấp gốc** của cấu hình (từ Mermaid 11, `flowchart.htmlLabels` đã lỗi thời) và đợi `document.fonts.ready`.
- Máy chủ `vitepress preview` lưu danh sách tệp lúc khởi động: build lại tệp có hash mới thì phải khởi động lại preview, nếu không trình duyệt nhận 404 và hiển thị bản cũ.
- Bộ nhớ đệm trình duyệt tự động hóa có thể giữ trang cũ: thêm tham số `?v=n` khi kiểm.

## 2.1. Quy tắc thiết kế sơ đồ Mermaid

Các quy tắc dưới đây là nguồn chân lý cho sơ đồ Mermaid trong giáo trình:

1. Chỉ dùng `<br/>` để xuống dòng; không dùng thẻ HTML khác. Nhấn mạnh tiêu đề bằng chữ IN HOA ngắn hoặc văn bản thường.
2. Nhãn nút tối đa 3 dòng ngắn (tiêu đề và tối đa 2 ý); mỗi dòng nên khoảng 32 ký tự trở xuống.
3. Không đưa số hiệu pháp luật, ngày, phiên bản chuẩn/công cụ hoặc dữ kiện dễ hết hạn vào nhãn; dùng nhãn trung tính và trỏ về phụ lục.
4. Nối nút với nút, không nối subgraph với subgraph; các bước quy trình phải có mũi tên theo thứ tự và nhãn cạnh ngắn.
5. Mỗi `classDef` phải khai báo `fill`, `stroke` và `color:#0D1117`. Dùng năm lớp màu ngữ nghĩa sau:

| Miền | `classDef` | Nền | Viền | Dùng cho |
|---|---|---|---|---|
| Pháp lý & đạo đức | `lawStyle` | `#E8EAF6` | `#283593` | Pháp luật, đạo đức, IRB |
| Kiến trúc & quản trị | `archStyle` | `#E0F2FE` | `#0277BD` | Five Safes, TRE, hạ tầng |
| Kỹ thuật & pipeline | `techStyle` | `#FFF3E0` | `#E65100` | ETL, khử định danh, kiểm tra |
| Toán học & tiêu chuẩn | `mathStyle` | `#E8F5E9` | `#2E7D32` | Riêng tư, FAIR, chuẩn |
| Cảnh báo & rủi ro | `warnStyle` | `#FFEBEE` | `#C62828` | Rò rỉ, lỗi, nguy cơ |

6. Mục tiêu kích thước tự nhiên ở 100% là rộng khoảng ≤ 950 px và cao khoảng ≤ 1000 px (số đo thực tế trên web); ưu tiên `TD` hoặc chia chuỗi rộng thành hai dòng.
7. Mỗi sơ đồ phải có tiêu đề hình và mô tả văn bản ngay dưới khối để làm văn bản thay thế; không sửa các đoạn văn khác chỉ để lặp lại sơ đồ.

### Lỗi bố cục và giới hạn kiểm chứng

Nối subgraph với subgraph có thể tạo khoảng trống hoặc kéo giãn khung trong một số trình dựng. Đây là quan sát phụ thuộc phiên bản và môi trường; hiện chưa tái hiện được trên Mermaid 12 trên web, nên quy tắc nối nút với nút được dùng như khuyến nghị thực hành. Các chuỗi một hàng dài và nhãn quá tải cũng dễ làm đảo thứ tự hoặc vượt khung.

Tỷ số tương phản của chữ `#0D1117` trên các nền lần lượt là: `#E8EAF6` **15,80:1**, `#E0F2FE` **16,49:1**, `#FFF3E0` **17,26:1**, `#E8F5E9` **16,82:1**, `#FFEBEE` **16,55:1**. Các tỷ số này đạt AA cho chữ thường theo ngưỡng 4,5:1; phép tính mới bao phủ chữ trong nút, chưa kiểm chế độ tối đầy đủ ở nhãn cạnh và tiêu đề subgraph.

Chưa có ảnh chụp hoặc tên công cụ IDE trong kho làm bằng chứng; kiểm chứng render trực tiếp vẫn cần ghi riêng khi thực hiện.

## 3. Công thức

- Dùng `markdown-it-mathjax3` (VitePress): công thức `$...$` và `$$...$$` được dựng sẵn khi build, cấu hình `isCustomElement` cho thẻ `mjx-*`; công thức khối cho phép cuộn ngang.
- Kiểm: số `mjx-container` khớp kỳ vọng, không còn cặp `$...$` thô, không có lỗi MathJax.
- Ký tự `$` tiền tệ phải thoát (`\$`) hoặc tránh dùng.

## 4. Quy tắc quiz (để lập quiz mới cho sách khác)

1. Số câu theo số phần lý thuyết chính của chương (tối đa 1 câu mỗi phần); quy tắc tự đánh giá tính theo tỷ lệ phần trăm, không cố định số câu.
2. Chỉ hỏi khái niệm ổn định; không hỏi số hiệu, ngày, số điều, phiên bản chuẩn, mã concept, số liệu kịch bản; mọi câu trả lời được từ chương.
3. Chống lộ đáp án: phân bố A–D đều (mỗi chữ khoảng 20–30%); đáp án đúng là phương án dài nhất tối đa 40% số câu và tỷ lệ độ dài đúng/sai ≤ 1,3; phương án sai không dùng từ tuyệt đối (luôn, chỉ, mọi, không bao giờ, hoàn toàn…) nhiều hơn đáp án đúng.
4. Kiểm bằng script (`check_quizzes.py`) và báo exit code thật. Bài học: lần đầu script chỉ tính chỉ số mà không thực thi ngưỡng nên báo PASS sai; phải thử cho ra vi phạm trên dữ liệu xấu trước khi tin kết quả PASS.
5. Quiz tổng hợp sửa ở nguồn chân lý (course-source) trước, bản chương mirror nguyên văn, kiểm so khớp từng dòng.

## 5. Quy trình triển khai web (VitePress + Pages từ `gh-pages`)

1. Sửa ở repo gốc → đồng bộ (`sync_from_source.py`, manifest) → `--check` → `npm run build`.
2. Loại trang nội bộ khỏi bản dựng (`srcExclude`: `AGENTS.md`, `README.md`, `CONTRIBUTING.md`).
3. Triển khai: build từ `main`, xóa sạch nhánh `gh-pages`, chép `dist` vào, thêm `.nojekyll`, commit "deploy: VitePress site <sha>", push; chờ run `pages-build-deployment` xong, kiểm các URL chính và mục mới trên trang công khai bằng `curl` hoặc trình duyệt (không giả User-Agent để vượt chặn bot).
4. Mỗi lần merge vào `main` không tự xuất bản; việc triển khai là bước riêng cần quyết định.

## 6. Việc áp dụng cho sách khác (checklist)
- [ ] Chọn Mermaid làm nguồn sơ đồ; viết nhãn ngắn; thêm tiêu đề/mô tả cho mỗi sơ đồ.
- [ ] Thêm thành phần Mermaid + MathJax vào theme web (sao chép `Mermaid.vue`, `mermaid.css`, cấu hình `markdown.config` và `vue.template.compilerOptions`).
- [ ] Kiểm dựng bằng trình duyệt: số sơ đồ dựng được, số công thức, không lỗi console.
- [ ] Dựng quiz theo quy tắc §4 và thêm script kiểm.
- [ ] Cân nhắc dựng sẵn SVG khi build nếu cần bản in/PDF.
