# Kết quả đối chiếu trích dẫn với OpenAlex và Semantic Scholar

**Ngày:** 21/11/2026 · **Công cụ:** `scripts/verify_refs.py` (API công khai OpenAlex và Semantic Scholar; không gửi thông tin cá nhân) · **Dữ liệu:** `references/references.bib` (103 mục)

## Phạm vi và độ tin cậy

- Chỉ **56 mục có DOI** được tra theo DOI trên OpenAlex. Đây là kết quả đáng tin: DOI xác định duy nhất một bài. Chi tiết: `references/verification-doi-openalex.csv`.
- 37 mục là văn bản pháp luật, chuẩn, báo cáo, trang web (không phải bài báo) được đánh dấu `NOT_APPLICABLE`.
- 10 mục học thuật còn lại không có DOI trong danh mục nên chỉ tra theo tiêu đề. Kết quả tra tiêu đề (`references/verification-report.csv`) **không được dùng làm xác nhận**, vì dễ khớp nhầm bài khác.
- Semantic Scholar bị giới hạn tốc độ và thường không tìm thấy; chỉ dùng để tham khảo thêm, không quyết định kết luận.
- API không xác nhận được nội dung khẳng định (số liệu, mốc pháp lý). Kết quả này chỉ kiểm tra thư mục (tiêu đề, năm, DOI).

## Tổng hợp (56 mục có DOI)

| Kết quả | Số mục | Ghi chú |
|---|---|---|
| Khớp tiêu đề và năm | 40 | |
| Khớp tiêu đề, lệch năm | 7 | `ref_006`, `021`, `028`, `073`, `091`, `093`, `099`: năm online khác năm số tạp chí (ví dụ REDCap 2008/2009, Weiskopf 2012/2013). Cần quyết định theo quy ước APA, chưa phải lỗi chắc chắn. |
| Khớp một phần (khác cách viết/bản) | 2 | `ref_037` (tên đầy đủ hơn), `ref_056` (OpenAlex ghi bản Draft của Rev. 2) |
| **Không khớp, cần xử lý** | 6 | xem bên dưới |
| DOI không phân giải được trên OpenAlex | 1 | `ref_017` (DOI Zenodo; có thể là DOI phiên bản) |

## Các mục không khớp (cần Ben hoặc người audit xử lý, chưa tự sửa)

| Mục | Vấn đề | Đề xuất |
|---|---|---|
| `ref_045` Wilkinson 2019 | DOI trỏ tới bài *"Evaluating FAIR maturity through a scalable, automated, community-governed framework"*. | Đã sửa tiêu đề theo DOI (PR #21). |
| `ref_103` Lane 2020 | Crossref và PubMed 32864627: *"Risk of hydroxychloroquine alone and in combination with azithromycin in the treatment of rheumatoid arthritis: a multinational, retrospective study"*. | Đã sửa tiêu đề (PR #21). Còn phải đối chiếu số liệu ">950.000 người dùng HCQ, 14 cơ sở dữ liệu" ở Phụ lục A với bài gốc. |
| `ref_072` Clark (Bridge2AI) | bioRxiv: v6 (24/4/2026) tên *"AI-readiness criteria for biomedical data"*; v7 (17/11/2026) tên dài hơn (*…in functional genomics and clinical medicine*). OpenAlex ghi tiêu đề của một phiên bản khác. | Giữ tiêu đề v6, ghi rõ phiên bản khi trích. |
| `ref_067` Utrecht handbook | OpenAlex ghi tên sổ tay "Data Privacy Handbook" (mục đang ghi là chương). | Có thể chấp nhận; ghi rõ là chương |
| `ref_076`, `ref_085` | Khác ngôn ngữ/định dạng tiêu đề (tiếng Đức, tiếng Việt). | Có thể chấp nhận |

Lưu ý: các mục `ref_045` và `ref_103` cũng cho thấy rủi ro chung: tiêu đề trong danh mục 103 mục có thể được viết lại từ trí nhớ hoặc từ bản preprint. Các mục không có DOI (47 mục) cần audit thủ công.

## Đối chiếu DOI bổ sung cho chương 1 (21/11/2026)

Lệnh dự kiến dùng trong môi trường có mạng: `python -c "... requests.get('https://api.crossref.org/works/' + doi) ..."`. Sandbox không kết nối được trực tiếp tới `api.crossref.org`, nên kết quả dưới đây được ghi từ Crossref Metadata Search/Crossmark và các trang xuất bản hoặc PubMed được mở cùng ngày. Đây là kiểm tra metadata, không phải xác nhận toàn bộ nội dung khoa học.

| Khóa | DOI | Kết quả Crossref | Đối chiếu |
|---|---|---|---|
| `ref_104` | `10.1186/s13059-016-1044-7` | KHỚP | Ziemann, Eren, El-Osta; *Gene name errors are widespread in the scientific literature*; 2016; *Genome Biology* 17:177. |
| `ref_105` | `10.1038/483531a` | KHỚP | Begley và Ellis; *Nature* 483:531–533; 2012. |
| `ref_106` | `10.1371/journal.pbio.1002165` | KHỚP | Freedman, Cockburn, Simcoe; *PLoS Biology* 13(6):e1002165; 2015. |
| `ref_107` | `10.1016/S0140-6736(20)31324-6` | KHỚP | Thông báo rút bài Lancet, 2020; DOI và tiêu đề khớp. |
| `ref_108` | `10.1056/NEJMc2021225` | KHỚP | Thông báo rút bài NEJM, 2020; DOI và tiêu đề khớp. |

`ref_104`–`ref_108` được đánh dấu `VERIFIED_UNAUDITED`; hai DOI của bài gốc Surgisphere được nhận diện trong tra cứu nhưng không được thêm vì chưa hoàn tất kiểm tra trực tiếp qua Crossref trong môi trường này.

Kiểm tra bổ sung (21/11/2026, gọi trực tiếp `api.crossref.org`): bốn DOI `ref_105`–`ref_108` đều phân giải, tiêu đề/tác giả/năm khớp. Sửa `ref_108`: số trang đúng là `382:2582` (không phải `e102`, là số của bài gốc). Với `ref_104`, trang nhà xuất bản Genome Biology xác nhận 18 tạp chí, 2005–2015, 704 bài (19,6% số bài có danh sách gen Excel). Đây là đối chiếu metadata, chưa phải audit nội dung độc lập.

## Đối chiếu nguồn chương 2 — 21/11/2026

| Khóa | URL | Kết quả và giới hạn |
|---|---|---|
| `ref_109` | https://www.ema.europa.eu/system/files/documents/regulatory-procedural-guideline/reflection-paper-expectations-electronic-source-data-data-transcribed-electronic-data-collection_en.pdf | Đọc được tài liệu EMA 2010; trang ghi tài liệu đã được thay thế bởi hướng dẫn 2023. Không dùng để khẳng định nguồn gốc lịch sử của ALCOA. |
| `ref_110` | https://www.gov.uk/government/publications/guidance-on-gxp-data-integrity | Đọc được trang GOV.UK/MHRA; công bố 09/03/2018. Không suy rộng lịch sử ALCOA ngoài nội dung tài liệu. |
| `ref_111` | https://www.ema.europa.eu/system/files/documents/regulatory-procedural-guideline/guideline_on_computerised_systems_and_electronic_data_in_clinical_trials_en.pdf | Đọc được hướng dẫn EMA 2023; bản cuối được thông qua 07/03/2023 và có mục ALCOA++/audit trail. |
| `ref_112` | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11 | Đọc được eCFR ngày 21/11/2026; xác nhận Part 11 là quy định về hồ sơ/chữ ký điện tử và các kiểm soát liên quan. |
| REDCap resources | https://projectredcap.org/resources/ | Đọc được trang tài nguyên chính thức ngày 21/11/2026; không dùng tài liệu này để khẳng định chi tiết cơ chế De-Identified hay audit trail của mọi phiên bản REDCap. |

Chưa tìm được nguồn chính thống trực tiếp để xác nhận phát biểu lịch sử “Stan Woollen đặt ra ALCOA”; cờ `[CẦN KIỂM CHỨNG: nguồn gốc ALCOA]` được giữ trong chương.

## Đối chiếu bổ sung `ref_116`–`ref_133` — 25/11/2026

Các mục `chapter_only` bổ sung (`ref_116`–`ref_133`) được đối chiếu định danh thư mục (tiêu đề, tác giả/chủ biên, năm xuất bản, nhà xuất bản/tạp chí, ISBN/DOI/URL) qua tìm kiếm web trên trang nhà xuất bản, Crossref/DOI, PubMed/PMC, RePEc và cổng văn bản chính phủ ngày 25/11/2026. Tất cả được giữ trạng thái `VERIFIED_UNAUDITED` (chỉ kiểm định danh, chưa đọc và kiểm chứng toàn văn từng khẳng định khoa học/pháp lý).

| Khóa | Định danh chính | Kết quả đối chiếu ngày 25/11/2026 |
|---|---|---|
| `ref_116` | `doi:10.1007/978-3-030-58721-5` / ISBN `978-3-030-58720-8` | Khớp Shortliffe, Cimino & Chiang (2021), 5th ed., Springer. |
| `ref_117` | `doi:10.1371/journal.pcbi.1004525` | Khớp Michener (2015), *PLOS Computational Biology* 11(10):e1004525. |
| `ref_118` | ISBN `978-1-032-49558-3` | Khớp Prokscha (2024), 4th ed., CRC Press (hiệu đính năm từ 2023 sang 2024). |
| `ref_119` | ISBN `978-1-088-85519-5` / `ohdsi.github.io/TheBookOfOhdsi/` | Khớp *The Book of OHDSI* (2019, bản trực tuyến cập nhật liên tục). |
| `ref_120` | ISBN `978-1-64295-244-5` | Khớp Holland & Shostak (2016, Revised 2nd ed.), SAS Institute (thay cho mục Hume et al. 2020 không tồn tại). |
| `ref_121` | `doi:10.1109/CBMS.2013.6627810` | Khớp Bender & Sartipi (2013), bài báo hội nghị IEEE CBMS 2013, tr. 326–331 (không phải textbook). |
| `ref_122` | ISBN `978-0-470-52679-8` | Khớp Little & Rubin (2019), 3rd ed., Wiley. |
| `ref_123` | ISBN `978-1-138-58831-8` | Khớp van Buuren (2018), 2nd ed., Chapman & Hall/CRC. |
| `ref_124` | `doi:10.1093/jamia/ocab132` | Khớp Blacketer et al. (2021), *JAMIA* 28(10):2251–2257 (hiệu đính đúng tiêu đề bài báo gốc). |
| `ref_125` | ISBN `978-1-4665-7906-4` | Khớp El Emam (2013), CRC Press / Auerbach Publications. |
| `ref_126` | `doi:10.1561/0400000042` | Khớp Dwork & Roth (2014), *Foundations and Trends in Theoretical Computer Science* 9(3–4):211–407. |
| `ref_127` | `ideas.repec.org/p/uwe/wpaper/20161601.html` | Khớp Desai, Ritchie & Welpton (2016), UWE Bristol Working Paper 1601 (hiệu đính tiêu đề và đơn vị phát hành). |
| `ref_128` | `doi:10.17226/25303` | Khớp NASEM (2019), *Reproducibility and Replicability in Science*. |
| `ref_129` | ISBN `978-1-4665-6159-5` / `doi:10.1201/b16868` | Khớp Stodden, Leisch & Peng (2014), Chapman & Hall/CRC. |
| `ref_130` | `doi:10.1038/nbt.3820` | Khớp Di Tommaso et al. (2017), *Nature Biotechnology* 35(4):316–319 (hiệu đính `workflows`, không phải `pipelines`). |
| `ref_131` | `doi:10.1038/s41597-022-01710-x` | Khớp Barker et al. (2022), *Scientific Data* 9:622. |
| `ref_132` | `vanban.chinhphu.vn/?classid=1&docid=207396&pageid=27160` | Trang văn bản Chính phủ cho Luật 15/2023/QH15 (ghi nhận từ phụ lục pháp lý 21/11/2026); Điều 69 cần đối chiếu toàn văn. |
| `ref_133` | `doi:10.17226/13444` | Khớp IOM (2012), *Best Care at Lower Cost*, The National Academies Press. |
