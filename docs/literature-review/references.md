# Danh mục tài liệu nền tảng và đề xuất bổ sung theo 9 chương chuyên khảo

**Ngày lọc:** 25/11/2026 · **Căn cứ mục lục:** `docs/syllabus/MONOGRAPH_OUTLINE_v1.0.0.md` (v1.1.0, đã chuyển Quản trị và pháp lý Việt Nam sang Chương 8)  
**Phạm vi & giới hạn:** Đây là danh mục định hướng biên soạn cho 9 chương chuyên khảo, đã đối chiếu với `references/references.bib`, `references/citation-audit.csv`, `docs/legal-verification.md` và tra cứu định danh xuất bản phẩm (ISBN/DOI) ngày 25/11/2026. Tài liệu này **không thay thế** thư mục đóng `references/references.bib`. Mọi nguồn mới chỉ được phép trích dẫn chính thức trong thân sách sau khi audit toàn văn và cấp khóa `ref_116+` trong `references/references.bib`.

## Quy ước phân loại trong danh mục

- **Đã có trong `references.bib`:** ghi kèm khóa `[@ref_NNN]` và giữ nguyên trạng thái từ `references/citation-audit.csv` (`VERIFIED_UNAUDITED` hoặc `BIB_PENDING`) và `docs/legal-verification.md`.
- **Đề xuất bổ sung mới (`Chưa có trong .bib`):** chỉ giữ lại các đầu sách, chuẩn, working paper và bài báo đã xác minh được tiêu đề, năm, nhà xuất bản/tạp chí, ISBN hoặc DOI thật; gắn nhãn `CHỜ AUDIT TOÀN VĂN` trước khi cấp `ref_NNN`.

---

## Chương 1. Tổng quan RDM, Vòng đời và Kế hoạch Quản lý Dữ liệu (DMP)

### Textbook & khung tham chiếu
- **Shortliffe, E. H., & Cimino, J. J. (Eds.), với Co-Editor Chiang, M. F. (2021).** *Biomedical Informatics: Computer Applications in Health Care and Biomedicine* (5th ed.). Springer International Publishing. ISBN `978-3-030-58720-8` / `978-3-030-58721-5`. — *Mới; đã xác minh định danh, chờ audit nội dung.*
- **DAMA International. (2017).** *DAMA-DMBOK: Data Management Body of Knowledge* (2nd ed.). Technics Publications. — *Đã có trong `.bib`: `[@ref_014]` (`VERIFIED_UNAUDITED`; lưu ý `[@ref_001]` cho DAMA-DMBOK 3.0 đang `BIB_PENDING`).*

### Bài báo nền tảng & chính sách
- **Wilkinson, M. D., et al. (2016).** The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018. `doi:10.1038/sdata.2016.18`. — *Đã có trong `.bib`: `[@ref_012]` (`VERIFIED_UNAUDITED`).*
- **Baker, M. (2016).** 1,500 scientists lift the lid on reproducibility. *Nature*, 533(7604), 452–454. `doi:10.1038/533452a`. — *Đã có trong `.bib`: `[@ref_033]` (`VERIFIED_UNAUDITED`).*
- **Michener, W. K. (2015).** Ten simple rules for creating a good data management plan. *PLOS Computational Biology*, 11(10), e1004525. `doi:10.1371/journal.pcbi.1004525`. — *Mới; đã xác minh DOI/tiêu đề, chờ audit nội dung.*

---

## Chương 2. Thu thập dữ liệu lâm sàng, ALCOA+ và Nền tảng REDCap

### Textbook & hướng dẫn thực hành
- **Prokscha, S. (2024).** *Practical Guide to Clinical Data Management* (4th ed.). CRC Press / Taylor & Francis. ISBN `9781032495583` / `9781040042113`. — *Mới; đã hiệu đính năm xuất bản (2024, không phải 2023; cập nhật dự thảo/xu hướng ICH E6(R3), chưa bao phủ bản Step 4 ngày 06/01/2025).*
- **Society for Clinical Data Management (SCDM). (n.d.).** *GCDMP — Good Clinical Data Management Practices*. URL: `https://scdm.org/gcdmp/`. — *Đã có trong `.bib`: `[@ref_013]` (`VERIFIED_UNAUDITED`).*

### Bài báo & hướng dẫn quy chuẩn
- **Harris, P. A., et al. (2009).** Research electronic data capture (REDCap) — A metadata-driven methodology and workflow process for providing translational research informatics support. *Journal of Biomedical Informatics*, 42(2), 377–381. `doi:10.1016/j.jbi.2008.08.010`. — *Đã có trong `.bib`: `[@ref_006]` (`VERIFIED_UNAUDITED`).*
- **Harris, P. A., et al. (2019).** The REDCap consortium: Building an international community of software platform partners. *Journal of Biomedical Informatics*, 95, 103208. `doi:10.1016/j.jbi.2019.103208`. — *Đã có trong `.bib`: `[@ref_102]` (`VERIFIED_UNAUDITED`).*
- **International Council for Harmonisation (ICH). (2025).** *ICH E6(R3) Guideline for Good Clinical Practice* (Step 4 Final Guideline, 06/01/2025). — *Đã có trong `.bib`: `[@ref_004]` (`VERIFIED_UNAUDITED`; chi tiết số mục/phụ lục trong chương vẫn giữ cờ chờ đối chiếu).*

---

## Chương 3. Chuẩn dữ liệu y sinh: CDISC, HL7 FHIR và OHDSI OMOP CDM

### Sách & tài liệu chuẩn mực
- **OHDSI Community. (2019, bản trực tuyến cập nhật liên tục).** *The Book of OHDSI: Observational Health Data Sciences and Informatics*. ISBN `978-1088855195`. — *Mới; chưa có trong `.bib` (lưu ý `[@ref_011]` trong `.bib` hiện là Sachson, 2025, Our journey).*
- **Holland, C., & Shostak, J. (2016/2020).** *Implementing CDISC Using SAS: An End-to-End Guide* (2nd ed.). SAS Press. — *Mới (đề xuất thay thế mục Hume et al. 2020 không xác nhận được sự tồn tại); chờ tác giả duyệt và kiểm chứng ISBN.*

### Bài báo nền tảng & đặc tả kỹ thuật
- **Bender, D., & Sartipi, K. (2013).** HL7 FHIR: An agile and RESTful approach to healthcare information exchange. *2013 IEEE 26th International Symposium on Computer-Based Medical Systems (CBMS)*, 326–331. `doi:10.1109/CBMS.2013.6627810`. — *Mới; đã hiệu đính phân loại từ "textbook" sang bài báo hội nghị.*
- **Mandel, J. C., et al. (2016).** SMART on FHIR: A standards-based, interoperable apps platform for electronic health records. *JAMIA*, 23(5), 899–908. `doi:10.1093/jamia/ocv189`. — *Đã có trong `.bib`: `[@ref_036]` (`VERIFIED_UNAUDITED`).*
- **Hripcsak, G., et al. (2015).** Observational Health Data Sciences and Informatics (OHDSI): Opportunities for observational researchers. *Studies in Health Technology and Informatics*, 216, 574–578. — *Đã có trong `.bib`: `[@ref_038]` (`VERIFIED_UNAUDITED`).*
- **HL7 International & OHDSI (Vulcan Accelerator). (2026).** *FHIR to OMOP Implementation Guide v1.0.0* (Informative Release, 30/04/2026). URL: `http://hl7.org/fhir/uv/omop/`. — *Đã có trong `.bib`: `[@ref_010]` (`VERIFIED_UNAUDITED`, trong `.bib` đang ghi `n.d.`, đã đối chiếu ngày công bố v1.0.0 là 30/04/2026).*

---

## Chương 4. Khung chất lượng dữ liệu và Xử lý dữ liệu khuyết

### Textbook kinh điển
- **Little, R. J. A., & Rubin, D. B. (2019).** *Statistical Analysis with Missing Data* (3rd ed.). John Wiley & Sons. ISBN `978-0470526798`. — *Mới; đã xác minh định danh, chờ audit nội dung (hiện `.bib` mới có bài Rubin 1976 `[@ref_031]`).*
- **van Buuren, S. (2018).** *Flexible Imputation of Missing Data* (2nd ed.). Chapman & Hall/CRC. ISBN `978-1138588318`. — *Mới; đã xác minh định danh, chờ audit nội dung.*

### Bài báo nền tảng & công cụ đánh giá
- **Kahn, M. G., et al. (2016).** A harmonized data quality assessment terminology and framework for the secondary use of electronic health record data. *eGEMs*, 4(1), 1244. `doi:10.13063/2327-9214.1244`. — *Đã có trong `.bib`: `[@ref_030]` (`BIB_PENDING`: thiếu danh sách đầy đủ tác giả).*
- **Weiskopf, N. G., & Weng, C. (2013).** Methods and dimensions of electronic health record data quality assessment: Enabling reuse for clinical research. *JAMIA*, 20(1), 144–151. `doi:10.1136/amiajnl-2011-000681`. — *Đã có trong `.bib`: `[@ref_028]` (`VERIFIED_UNAUDITED`).*
- **Blacketer, C., DeFalco, F. J., Ryan, P. B., & Rijnbeek, P. R. (2021).** Increasing trust in real-world evidence through evaluation of observational data quality. *JAMIA*, 28(10), 2251–2257. `doi:10.1093/jamia/ocab132`. — *Mới; đã hiệu đính đúng tiêu đề bài báo gốc.*

---

## Chương 5. Bảo vệ dữ liệu, Quyền riêng tư và Kỹ thuật khử định danh

### Textbook & chuyên khảo nền tảng
- **El Emam, K. (2013).** *Guide to the De-Identification of Personal Health Information*. CRC Press / Auerbach Publications. ISBN `9781466579064`. — *Mới; đã xác minh định danh, chờ audit nội dung.*
- **Dwork, C., & Roth, A. (2014).** *The Algorithmic Foundations of Differential Privacy*. *Foundations and Trends in Theoretical Computer Science*, 9(3–4), 211–407. `doi:10.1561/0400000042`. — *Mới; ghi đúng dạng chuyên khảo tạp chí (hiện `.bib` mới có Dwork 2008 `[@ref_070]`).*

### Bài báo & khung truy cập an toàn
- **Sweeney, L. (2002).** k-Anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, 10(5), 557–570. `doi:10.1142/s0218488502001648`. — *Đã có trong `.bib`: `[@ref_068]` (`BIB_PENDING`).*
- **Machanavajjhala, A., et al. (2007).** $\ell$-Diversity: Privacy beyond k-anonymity. *ACM Transactions on Knowledge Discovery from Data*, 1(1), Article 3. `doi:10.1145/1217299.1217302`. — *Đã có trong `.bib`: `[@ref_069]` (`VERIFIED_UNAUDITED`).*
- **Desai, T., Ritchie, F., & Welpton, R. (2016).** *Five Safes: designing data access for research*. Economics Working Paper Series 1601, University of the West of England, Bristol. — *Mới; đã hiệu đính tiêu đề và cơ quan phát hành (hiện `.bib` chỉ có trang thứ cấp CASRAI `[@ref_075]`).*

---

## Chương 6. FAIR, Kho lưu trữ và Dữ liệu sẵn sàng cho AI

### Tài liệu đã bình duyệt & báo cáo chính thức
- **Wilkinson, M. D., et al. (2019).** Evaluating FAIR maturity through a scalable, automated, community-governed framework. *Scientific Data*, 6, 174. `doi:10.1038/s41597-019-0184-5`. — *Đã có trong `.bib`: `[@ref_045]` (`VERIFIED_UNAUDITED`).*
- **Gebru, T., et al. (2021).** Datasheets for datasets. *Communications of the ACM*, 64(12), 86–92. `doi:10.1145/3458723`. — *Đã có trong `.bib`: `[@ref_074]` (`VERIFIED_UNAUDITED`).*
- **Goldacre, B., & Morley, J. (2022).** *Better, broader, safer: Using health data for research and analysis* (The Goldacre Review). UK Department of Health and Social Care. — *Đã có trong `.bib`: `[@ref_097]` (`VERIFIED_UNAUDITED`).*

### Preprint đang theo dõi (chưa bình duyệt — giữ cờ cảnh báo)
- **Clark, T. W., et al. (Bridge2AI Standards Working Group, 2024/2026).** AI-readiness criteria for biomedical data. *bioRxiv*, `doi:10.1101/2024.10.23.619844`. — *Đã có trong `.bib`: `[@ref_072]` (`VERIFIED_UNAUDITED`; đã hiệu đính tác giả đầu là `Clark, T.`, lưu ý là **preprint chưa bình duyệt**, bản v6 giữ tiêu đề ngắn và v7 có tiêu đề mở rộng).*

---

## Chương 7. Tính tái lập và Phần mềm nghiên cứu y sinh

### Sách & báo cáo nền tảng
- **National Academies of Sciences, Engineering, and Medicine (NASEM). (2019).** *Reproducibility and Replicability in Science*. The National Academies Press. `doi:10.17226/25303`. — *Mới; đã xác minh DOI/tiêu đề, chờ audit nội dung.*
- **Stodden, V., Leisch, F., & Peng, R. D. (Eds.). (2014).** *Implementing Reproducible Research*. Chapman & Hall/CRC. ISBN `9781466561595`, `doi:10.1201/b16868`. — *Mới; đã xác minh ISBN/DOI, chờ audit nội dung.*

### Công cụ quy trình & chuẩn phần mềm nghiên cứu
- **Di Tommaso, P., Chatzou, M., Floden, E. W., Prieto Barja, P., Palumbo, E., & Notredame, C. (2017).** Nextflow enables reproducible computational workflows. *Nature Biotechnology*, 35(4), 316–319. `doi:10.1038/nbt.3820`. — *Mới; đã hiệu đính đúng tiêu đề (`workflows`, không phải `pipelines`).*
- **Barker, M., et al. (2022).** Introducing the FAIR Principles for research software. *Scientific Data*, 9, 622. `doi:10.1038/s41597-022-01710-x`. — *Đã xác minh DOI/tiêu đề; mới, chờ cấp `ref_NNN` và audit nội dung.*

---

## Chương 8. Quản trị và Pháp lý dữ liệu y tế tại Việt Nam

*(Quyết định 25/11/2026: chuyển thành Chương 8, ngay trước Chương 9 Tích hợp; thân chương chỉ nêu nguyên lý quản trị, toàn bộ số hiệu điều khoản và thời hạn lưu trữ cập nhật qua phụ lục / Sổ cập nhật `updates/legal.yml` từ văn bản chính thống.)*

### Văn bản quy phạm pháp luật Việt Nam (kèm trạng thái kiểm chứng hiện có)
- **Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15** (hiệu lực 01/01/2026): `[@ref_062]` (`VERIFIED_UNAUDITED`; [legal-verification.md](../legal-verification.md) xác nhận 05 chương 39 điều, **chưa** coi chi tiết Cục A05/DPIA/DPO là đã đối chiếu toàn văn).
- **Nghị định số 356/2025/NĐ-CP** (hiệu lực 01/01/2026): `[@ref_063]` (`VERIFIED_UNAUDITED`; chi tiết nghĩa vụ DPIA/DPO chờ đối chiếu toàn văn).
- **Thông tư 13/2025/TT-BYT** (lộ trình hồ sơ bệnh án điện tử): `[@ref_065]` (`VERIFIED_UNAUDITED` trong `.bib`; [legal.md](../appendices/legal.md) giữ `CONTENT_PENDING` vì chưa đọc toàn văn nguồn Bộ Y tế, đã xác nhận mốc 30/09/2025 và 31/12/2026 qua Cổng TTĐT Chính phủ).
- **Thông tư 33/2025/TT-BYT** (thời hạn lưu trữ hồ sơ, tài liệu ngành y tế): `[@ref_055]` (`VERIFIED_UNAUDITED`; [legal-verification.md](../legal-verification.md) xác nhận hiệu lực từ 01/07/2025, các mức 30/20 năm còn `CONTENT_PENDING` chờ đối chiếu từng dòng phụ lục).
- **Thông tư 50/2025/TT-BYT** (thử thuốc trên lâm sàng): `[@ref_066]` (`VERIFIED_UNAUDITED` trong `.bib`; [legal-verification.md](../legal-verification.md) ghi `XÁC NHẬN MỘT PHẦN — chưa có toàn văn chính thức`).
- **Luật Dữ liệu số 60/2024/QH15**: `[@ref_064]` (`VERIFIED_UNAUDITED` trong `.bib`; [legal-verification.md](../legal-verification.md) ghi `KHÔNG TÌM ĐƯỢC NGUỒN CHÍNH THỐNG`, không suy rộng nội dung khi chưa có bản toàn văn).
- **Luật Khám bệnh, chữa bệnh số 15/2023/QH15** (Điều 69): chưa có trong `.bib`; [legal.md](../appendices/legal.md) đã có URL trang văn bản chính phủ nhưng chi tiết Điều 69 vẫn thuộc nhóm chưa đối chiếu ở `docs/PROJECT-STATE.md` (`CONTENT_PENDING`).

### Nghiên cứu thực địa tại Việt Nam
- **Tran, D. M., et al. (2025).** Status of digital health technology adoption in 5 Vietnamese hospitals: Cross-sectional assessment. *JMIR Formative Research*, 9, e53483. `doi:10.2196/53483`. — *Đã có trong `.bib`: `[@ref_084]` (`VERIFIED_UNAUDITED`).*
- **Trịnh Văn Vinh. (2025).** Digital transformation in electronic medical record management towards a smart and sustainable healthcare system. *Vietnam Journal of Community Medicine*, 66(4), 262–268. `doi:10.52163/yhc.v66i4.2905`. — *Đã có trong `.bib`: `[@ref_085]` (`VERIFIED_UNAUDITED`).*

---

## Chương 9. Tích hợp hệ thống và Tổng kết

- **Institute of Medicine (IOM / NAM), Smith, M., Saunders, R., Stuckhardt, L., & McGinnis, J. M. (Eds.). (2012).** *Best Care at Lower Cost: The Path to Continuously Learning Health Care in America*. The National Academies Press. `doi:10.17226/13444`. — *Mới; đã xác minh DOI/tiêu đề, chờ audit nội dung.*
- **Friedman, C. P., et al. (2015).** Toward a science of learning systems: A research agenda for the high-functioning Learning Health System. *JAMIA*, 22(1), 43–50. `doi:10.1136/amiajnl-2014-002977`. — *Đã có trong `.bib`: `[@ref_099]` (`VERIFIED_UNAUDITED`).*
- **Williamson, E. J., et al. (2020).** Factors associated with COVID-19-related death using OpenSAFELY. *Nature*, 584(7821), 430–436. `doi:10.1038/s41586-020-2521-4`. — *Đã có trong `.bib`: `[@ref_098]` (`VERIFIED_UNAUDITED`).*

---

## Nhật ký lọc và hiệu đính so với bản nháp ngày 25/11/2026

| Mục trong bản nháp cũ | Xử lý | Lý do |
|---|---|---|
| Dòng truy vấn tìm kiếm, mở đầu hội thoại, liên kết `file:///d:/...`, sơ đồ Mermaid lỗi quy tắc, Phần 2 cũ | **Đã loại bỏ** | Không phù hợp tài liệu repo; Phần 2 đã được Ben chốt chuyển Chương Pháp lý sang Chương 8 tại `MONOGRAPH_OUTLINE_v1.0.0.md` v1.1.0 |
| `Hume, S., et al. (2020). Exploring CDISC Standards...` | **Đã loại bỏ** | Không xác nhận được sự tồn tại của sách qua tra cứu; thay bằng đề xuất kiểm chứng *Holland & Shostak (2016/2020)* |
| `Prokscha, S. (2023)` | **Sửa năm → 2024** | Ấn bản 4 phát hành 2024; ghi rõ chưa bao phủ bản Step 4 ICH E6(R3) 01/2025 |
| `Bender & Sartipi (2013)` dưới mục Textbook | **Chuyển mục** | Là bài báo hội nghị IEEE CBMS 2013 (`doi:10.1109/CBMS.2013.6627810`) |
| `HL7 International (2024) FHIR to OMOP v1.0.0` | **Sửa năm → 2026** | Bản v1.0.0 công bố ngày 30/04/2026 |
| `Blacketer et al. (2021)` | **Sửa tiêu đề** | Tiêu đề gốc: *Increasing trust in real-world evidence through evaluation of observational data quality* |
| `Desai, Ritchie, Welpton (2016)` | **Sửa tiêu đề & nơi xuất bản** | *Five Safes: designing data access for research* (UWE Bristol Working Paper 1601) |
| `Clark, K. et al. (Bridge2AI, 2024)` dưới mục bình duyệt | **Sửa tác giả & phân loại** | Tác giả đầu là `Clark, T. W.`; giữ nguyên là **preprint `bioRxiv` chưa bình duyệt** |
| `Di Tommaso et al. (2017)` | **Sửa tiêu đề** | Đúng là *…reproducible computational workflows* (`workflows`, không phải `pipelines`) |
| Đánh số chương Ch. 6–8 | **Sắp lại theo v1.1.0** | Ch. 6 = FAIR & AI-Ready; Ch. 7 = Tái lập & phần mềm; Ch. 8 = Quản trị & Pháp lý VN |
