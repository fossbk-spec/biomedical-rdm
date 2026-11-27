# Quy cách cụ thể cho các quyết định chuyên khảo Biomedical RDM

**Tác giả:** nhóm biên soạn · **Phiên bản:** 1.0.0 · **Ngày:** 24/11/2026
**Người quyết định:** TS. Hoàng Quang Huy (Ben)
**Căn cứ:** `docs/handoff-20261125/01-de-xuat-chuyen-khao.md` (mục 13–15), `docs/handoff-20261125/02-tham-dinh-muc-luc.md`, review độc lập `docs/handoff-20261125/05-review-doc-lap-de-xuat.md`, số đo trên `main` @ aef5ae2.
**Giới hạn:** chưa ước lượng thời gian (chưa có số đo thử); chưa mở văn bản pháp lý và NIH gốc; chưa đọc đầy đủ nội dung ch06 và ch07 cũ nên bảng ánh xạ giai đoạn ↔ chương ở mục 1 cần Ben và bên thực hiện đối chiếu khi viết.

## 1. Q-A: định nghĩa vòng đời 7 giai đoạn (đề xuất cuối)

**Lời văn dùng chung (ch00, ch01, đề cương, quiz, mini-course):**
> Vòng đời dữ liệu nghiên cứu y sinh gồm bảy giai đoạn: (1) Thiết kế và kế hoạch quản lý dữ liệu; (2) Thu thập; (3) Xử lý và làm sạch; (4) Chuẩn hóa; (5) Phân tích và tái lập; (6) FAIR và chia sẻ; (7) Lưu trữ và hủy an toàn. Bốn lớp ngang áp dụng cho mọi giai đoạn: quản trị dữ liệu, bảo mật và quyền riêng tư, pháp lý và đạo đức, vai trò Data Steward.

**Bảng ánh xạ (mới, đặt trong ch01):**
| Giai đoạn / lớp | Chương chính (sau đánh số lại) |
|---|---|
| 1 Thiết kế và DMP | 1 |
| 2 Thu thập | 2 |
| 3 Xử lý và làm sạch | 4 |
| 4 Chuẩn hóa | 3 |
| 5 Phân tích và tái lập | 8 |
| 6 FAIR và chia sẻ | 7 |
| 7 Lưu trữ và hủy an toàn | 7 và phụ lục lưu giữ (cần bên thực hiện xác nhận nội dung ch06 cũ) |
| Lớp ngang: quản trị, Data Steward | 1 |
| Lớp ngang: bảo mật, khử định danh | 5 |
| Lớp ngang: pháp lý, đạo đức | 6 |

**Lý do thứ tự chương khác thứ tự giai đoạn** (ghi vào ch01): ch03 (chuẩn) đứng trước ch04 (chất lượng) vì DQD chạy trên OMOP CDM (`ch04...:123-129`).

**Việc phải sửa theo Q-A:** `ch00:23-28`, `docs/syllabus/...:46-52`, Quiz tổng hợp Q1 (bổ sung bước xử lý và làm sạch, kiểm lại đáp án), `docs/course-source/` (mini-course), `editorial/chapter-map.yml`.

## 2. Q-B: đánh số chương (đề xuất cuối: B1, chi phí thực tế thấp hơn ước lượng ban đầu)

Ước lượng "khoảng 200 dòng" của bên thực hiện tính mọi chuỗi `ch0N`. Khi phân tích riêng, **chỉ hai chương đổi số**:
| Hiện tại | Sau B1 | Ghi chú |
|---|---|---|
| ch01–ch05 | giữ nguyên | không đổi tên tệp, không đổi caption |
| (mới) | **ch06 Quản trị và pháp lý Việt Nam** | `planned` |
| ch06 FAIR và AI-ready | **ch07** | đổi tên tệp; ch06 cũ không có hình nên caption không đổi |
| (mới) | **ch08 Tái lập và phần mềm nghiên cứu** | `planned` |
| ch07 Hoàn thành và capstone | **ch09 Tích hợp và tổng kết** | tách quiz và capstone sang học liệu đi kèm (mục 3) |

**Đo thật:** tệp theo dõi chứa `ch06`/`ch07`/"Chương 6"/"Chương 7": `editorial/glossary.yml` (14 dòng), `editorial/chapter-map.yml` (8), `docs/PROJECT-STATE.md` (6), `scripts/check_quizzes.py` (5), `editorial/glossary-allowlist.txt` (4), `scripts/check_volatile.py` (2), `docs/DECISIONS.md` (2), `_quarto.yml` (2), `docs/quizzes/quiz_ch06.md` (1), cộng khoảng 6 tệp sinh tự động (`_site`, `.quarto`; không sửa). Repo khóa học: `scripts/sync_manifest.json` (2 dòng) và `.vitepress/config.mts` (2 dòng menu). **Khoảng 45 dòng thực chất.**
**Rủi ro riêng:** URL công khai của hai trang chương đổi (`/course/book/ch06` thành `/ch07` và `/ch07` thành `/ch09`); cần trang chuyển hướng hoặc ghi chú trên web.
**Cách làm:** một PR riêng, do bên thực hiện làm bằng `git mv` và script thay thế có `assert`, trước khi nâng cấp bất kỳ chương nào khác. Mini-course không đổi vì dùng "Bài N" riêng (`module-N-...`).
**Phương án khác (mã ổn định, số hiển thị sinh tự động):** tránh `git mv` nhưng số chương lệch mã, caption `Hình C.k` và tham chiếu "Chương N" phải đọc từ bảng ánh xạ; tôi không đề xuất.

## 3. Q-C: vai trò ch00 và ch07 cũ (đề xuất cuối: C1, bằng một trường trong `chapter-map.yml`)

Thêm trường `product: book | companion` vào `editorial/chapter-map.yml`:
| Tệp | `product` | Việc cụ thể |
|---|---|---|
| ch00 (Bắt đầu ở đây) | `companion` | giữ làm trang M0 của khóa học; sách có "Lời nói đầu và hướng dẫn đọc" viết mới (`book`) |
| ch07 cũ, phần Quiz tổng hợp và Checklist capstone | `companion` | giữ nguyên chữ, chuyển sang tên `ch09` hoặc thư mục companion khi chốt |
| ch09 mới (Tích hợp và tổng kết) | `book` | viết mới: một bài toán tích hợp từ thiết kế đến chia sẻ, bám khung vòng đời |

Quy tắc: script kiểm quiz, mini-course và đồng bộ web chỉ đọc theo `product`.

## 4. Mô hình hai lớp (D1–D6): quy cách kỹ thuật cụ thể

**Tên (D1):** "Phần cốt lõi" và "Sổ cập nhật".
**Vị trí:** `updates/` ở gốc repo gốc (cùng cấp `editorial/`).

```
updates/
  schema.json                 # JSON Schema cho mọi mục
  legal.yml                   # pháp lý, chính sách, lưu giữ (thay nội dung của appendices/legal.md và retention.md)
  funder.yml                  # mẫu và chính sách nhà tài trợ (thay appendices/funder-templates.md)
  standards.yml               # phiên bản chuẩn, vocabulary, công cụ (thay appendices/standards.md)
  evidence.yml                # bằng chứng hiện hành (kết quả mô tả hiện trạng, benchmark)
  links.yml                   # URL và công cụ cần theo dõi
  README.md
docs/updates/*.md             # trang đọc được, sinh tự động từ YAML (không sửa tay)
```
Các tệp `docs/appendices/legal.md`, `retention.md`, `funder-templates.md`, `standards.md` hiện có được **di trú** sang YAML ở bước pilot; trang đọc được sinh lại cùng slug để không gãy liên kết.

**Mỗi mục (D3):**
```yaml
- id: nih-dmsp-format
  anchor: nih-dmsp-format        # neo trong trang sinh ra
  chapter: [ch01]
  classification: regulation     # regulation | standard-version | funder-template | tool | evidence-current | link
  claim: "Mẫu DMSP của NIH hiện hành có 7 yếu tố (định dạng pilot)."
  source: "NIH, NOT-OD-26-046"
  source_type: official-notice   # official-notice | statute | standard | peer-reviewed | preprint | vendor | secondary
  source_url: "https://www.grants.nih.gov/grants/guide/notice-files/NOT-OD-26-046.html"
  evidence_scope: not-read       # full-text | abstract | metadata | secondary-summary | not-read
  status: CONTENT_PENDING        # giữ nguyên bộ trạng thái của repo
  as_of: 2026-05-25              # ngày nội dung có hiệu lực
  checked_at: 2026-11-24         # ngày repo kiểm
  review_cycle_days: 180
  review_by: 2027-05-23
  owner: null
  jurisdiction: US
  version: null
  supersedes: [nih-dmsp-21-014]
  blocking_reason: "Chưa đối chiếu văn bản gốc; giới hạn Element 4 và 6 chưa xác nhận"
  citation_key: ref_005
  change_log: []
```
`status` dùng bộ hiện có (`VERIFIED`, `CONTENT_PENDING`, `BIB_PENDING`, `BLOCKED_INPUT`); không dùng thay cột `status` của `citation-audit.csv`.

**Chu kỳ (D2):** mặc định theo `classification`: `regulation` 90–180 ngày; `funder-template` và `standard-version` và `tool` 180 ngày; `evidence-current` 180 ngày; `link` 365 ngày; nội dung ở lớp cốt lõi rà 12–24 tháng khi có thay đổi lớn của khung. Thêm trigger: rà ngay khi nguồn đổi.

**Liên kết từ chương (thay `[[upd:id]]`):** Markdown chuẩn, dạng `[NIH DMSP: mẫu hiện hành](../updates/funder.md#nih-dmsp-format)`. Mỗi chương có hộp "Cập nhật liên quan" liệt kê các mục dùng trong chương kèm `as_of`. Script đọc mọi liên kết trỏ vào `updates/` hoặc `docs/updates/` và đối chiếu `anchor`.

**Quy tắc phân loại (dùng trong style-guide):** "Nếu người đọc cần biết thông tin này còn đúng tại ngày nào thì nó phải có bản ghi trong sổ; nếu chỉ cần hiểu cơ chế hoặc lịch sử thì ở thân chương." Ca biên:
| Ca | Xử lý |
|---|---|
| Khái niệm ổn định nhưng tên hoặc phiên bản chuẩn đổi | Khái niệm ở thân chương; tên và phiên bản vào sổ `standards` |
| Kết quả lịch sử (Baker 2016, Surgisphere) | Thân chương, có trích dẫn |
| Con số mô tả hiện trạng (số quy tắc DQD, tỷ lệ áp dụng) | Sổ `evidence` hoặc `standards`; thân chương chỉ ghi nguyên lý |
| Văn bản pháp luật | Thân chương nêu nguyên lý; hiệu lực hiện tại, số hiệu và điều khoản vào sổ `legal` |
| Quy trình ổn định nhưng công cụ đổi (FAIRification 7 bước; FAIR Cookbook) | Quy trình ở thân chương; công cụ, chỉ số trưởng thành vào sổ |

**Script (D3, D6):**
- `scripts/check_updates.py`: kiểm schema; trường bắt buộc; `anchor` duy nhất; mọi liên kết từ chương trỏ tới `anchor` tồn tại; mục mồ côi (không chương nào dùng) → WARN; `review_by` quá hạn → WARN, quá hạn thêm 180 ngày → FAIL; `status: VERIFIED` mà `evidence_scope` là `metadata` hoặc `not-read` → FAIL.
- `scripts/gen_updates_pages.py`: sinh `docs/updates/*.md`.
- Mở rộng `check_volatile.py`: quét `docs/syllabus/`, tệp mục lục và mọi chương; số hiệu hoặc phiên bản dễ đổi ngoài sổ → WARN trước, FAIL sau khi pilot xong.

**Kết quả nghiên cứu (D4):** kết quả lịch sử ở thân chương; ước lượng hiện hành vào `evidence.yml` với `as_of`, phạm vi và trạng thái.
**Bản in (D5):** mỗi ấn bản kèm: ngày cắt, commit hash, manifest của `updates/` (mỗi tệp một hash), DOI của artifact (kho lưu trữ có cấp DOI) và hộp "Phiên bản và cập nhật" ghi cách trích dẫn "ấn bản + ngày cập nhật".
**Pilot (D6):** thực hiện đầy đủ trên **ch01** (chương mẫu, PR #28): đưa các mục NIH, ICH E6(R3), HIMSS AMAM, Horizon Europe, FAIR Cookbook vào sổ, đổi liên kết, chạy `check_updates.py`, render Quarto và VitePress để chắc liên kết và trang sinh hiển thị đúng. Chỉ khi pilot đạt mới mở rộng sang ch03–ch07.

## 5. Thứ tự PR đề xuất (không kèm ước lượng thời gian)
| Bước | PR | Người làm | Cổng nghiệm thu |
|---|---|---|---|
| 0 | #28 chương mẫu (hiện mở) | Ben duyệt | Ben chấp nhận khung 11 mục; bảng bằng chứng mục 5 được gắn `classification` |
| 1 | Chốt Q-A, Q-B, Q-C và mô hình hai lớp: viết `MONOGRAPH_OUTLINE_v1.0.0.md`, cập nhật `chapter-map.yml` (`product`, thứ tự, tiên quyết ch04 → ch03), sửa ch00, đề cương, Q1 | người soạn viết, bên thực hiện kiểm | `check_*` đạt; Ben duyệt |
| 2 | Đổi số chương (ch06 → ch07, ch07 → ch09) và URL web | bên thực hiện | script thay thế có `assert`; `quarto render`, build VitePress, kiểm liên kết |
| 3 | Hạ tầng Sổ cập nhật: `updates/`, `schema.json`, `check_updates.py`, generator, mở rộng `check_volatile.py` | bên thực hiện | self-test bắt được lỗi; pilot ch01 render ở cả hai pipeline |
| 4 | Nâng cấp ch03, ch02, ch04, ch05, ch07 (mỗi chương một PR, theo thứ tự đã chốt) | bên thực hiện làm, người soạn review | kiểm cấu trúc, trích dẫn, volatile, quiz, `check_updates`; audit nhận định có artifact |
| 5 | Viết ch06 (pháp lý) và ch08 (tái lập): chỉ sau khi có reviewer | bên thực hiện nháp, reviewer ngoài duyệt | reviewer pháp lý và kỹ thuật trả lời bằng văn bản từng phát hiện |
| 6 | Xác minh pháp lý, NIH, OMOP, EHDS từ văn bản gốc; chạy Lab 2 | người soạn và bên thực hiện, reviewer | mọi mục `CONTENT_PENDING` hoặc được giải quyết hoặc ghi rõ lý do trong "Giới hạn và vấn đề mở" |
| 7 | Review độc lập, xuất bản PDF/DOCX (kiểm trực quan trang mẫu có công thức, sơ đồ, bảng, font), DOI, license | Ben, reviewer | kiểm render thật; manifest phát hành |

## 6. Reviewer ngoài (tiêu chí cụ thể)
| Mảng | Chuyên môn cần | Phạm vi |
|---|---|---|
| Pháp lý | Người có chuyên môn pháp luật về dữ liệu cá nhân và y tế tại Việt Nam | ch06 và `updates/legal.yml` |
| Chuẩn dữ liệu | Người đã triển khai FHIR, OMOP hoặc CDISC trong dự án thật | ch03 và `updates/standards.yml` |
| Nghiên cứu lâm sàng | Người thực hiện thu thập dữ liệu bằng REDCap hoặc EDC (CRC, nhà nghiên cứu) | ch02, ch04, lab |
| Khoa học dữ liệu và tái lập | Người làm AI y tế và tái lập | ch07, ch08 |

**Độc lập:** không phải đồng tác giả, không cùng đơn vị với tác giả chính khi có thể, công bố xung đột lợi ích. **Sản phẩm:** văn bản trả lời từng phát hiện theo mẫu "mã, vị trí, nhận định, nguồn đã đọc, phạm vi (toàn văn hay chỉ abstract), mức độ, đề xuất, quyết định" (mẫu của HMYT `review-policy`). Ben chọn người; người soạn không đề cử tên.

## 7. Các tệp chưa theo dõi trong clone chính
| Tệp | Đề xuất |
|---|---|
| `docs/chapters/rdm-case-study-drmayday-workflow.md`, `rdm-dua-case-study-drmayday-vao-khoa-hoc.md` | Giữ chưa theo dõi cho tới khi Ben quyết định có công bố hay không (cần sự đồng ý); không đưa vào mục lục |
| `docs/chapters/rdm-phu-luc-b-bo-sung-dmptool-templates.md` | Là bản nháp kết quả kiểm DMPTool; có giá trị cho `updates/funder.md` (mẫu NIH 2026); nên được xử lý khi pilot sổ |
| `docs/quizzes/` (ngân hàng tạo tự động cũ), `docs/rdm-khoa-hoc-free-self-paced.md` | Đề xuất chuyển vào `archive/` hoặc xóa sau khi Ben xác nhận; hiện không thuộc kế hoạch |

## 8. Gói quyết định cần Ben duyệt (một lần)
1. Q-A: lời văn vòng đời và bảng ánh xạ (mục 1).
2. Q-B: B1, chỉ ch06 và ch07 đổi số, khoảng 45 dòng, một PR riêng (mục 2).
3. Q-C: trường `product` và các việc ở mục 3.
4. Mô hình hai lớp: D1–D6 với quy cách ở mục 4; cho phép dùng liên kết Markdown thay `[[upd:id]]`.
5. Thứ tự PR ở mục 5 và tiêu chí reviewer ở mục 6.
6. Xử lý tệp chưa theo dõi (mục 7).
