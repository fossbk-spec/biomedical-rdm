# Danh mục tài liệu tham khảo của sách chuyên khảo Biomedical RDM

**Tác giả sách:** TS. Hoàng Quang Huy (Ben) · **Phiên bản:** 1.0.0 (dự thảo để duyệt) · **Ngày:** 26/11/2026
**Sinh từ:** `main` ở `69fc2ee`: `references/references.bib` (115 mục), `references/citation-audit.csv`, các khóa `ref_NNN` trong `docs/chapters/ch0*.md` và số `[n]` trong `docs/literature-review/index.md`.

**Đọc kỹ trước khi dùng:**
- Danh mục này là **bản trình bày lại của `references.bib`**; không thêm, không sửa nguồn nào. Định dạng dạng APA rút gọn do công cụ sinh, **chưa phải bản biên tập cuối**.
- Cột "Trạng thái" lấy nguyên từ `citation-audit.csv`: `VERIFIED_UNAUDITED` nghĩa là đã đối chiếu thư mục nhưng **chưa qua kiểm toán độc lập**; `BIB_PENDING` là còn thiếu trường thư mục. Không mục nào ở đây được coi là đã xác minh đầy đủ.
- Trường bị thiếu trong `references.bib` được ghi `[thiếu …]`, không được tự điền.
- Số `[n]` trùng số thứ tự trong `docs/literature-review/index.md` và `citation-audit.csv` (cột `source_number`).

## 1. Tóm tắt

| Chỉ tiêu | Số mục |
|---|---:|
| Tổng số mục trong `references.bib` | 115 |
| Đã đối chiếu, chưa kiểm toán (`VERIFIED_UNAUDITED`) | 102 |
| Thiếu trường thư mục, cần bổ sung (`BIB_PENDING`) | 10 |
| Chưa xác định (`PENDING_UNDETERMINED`) | 3 |
| Được trích bằng khóa `ref_NNN` trong ít nhất một chương hiện có | 61 |
| Chỉ xuất hiện trong bản tổng hợp literature review (không có khóa trong chương) | 54 |
| Thiếu tác giả hoặc năm trong `.bib` | 6 |
| Có DOI | 61 |

## 2. Danh mục theo thứ tự số `[n]`

**[1]** DAMA International. (n.d.). DAMA-DMBOK® 3.0 project. https://dama.org/dama-dmbok-3-0-project/

> `ref_001` · Thiếu trường thư mục, cần bổ sung · dùng ở: chỉ trong bản tổng hợp · cần xử lý: một trường thư mục bị đánh dấu trong văn bản nguồn

**[2]** Healthcare Information and Management Systems Society. (n.d.). Adoption Model for Analytics Maturity. http://palsglobal.com/himss/

> `ref_002` · Thiếu trường thư mục, cần bổ sung · dùng ở: Ch.1 · cần xử lý: một trường thư mục bị đánh dấu trong văn bản nguồn

**[3]** European Commission. (n.d.). Horizon Europe data management plan. https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e519589e89&appId=PPGMS

> `ref_003` · Thiếu trường thư mục, cần bổ sung · dùng ở: Ch.1, Ch.6 · cần xử lý: một trường thư mục bị đánh dấu trong văn bản nguồn

**[4]** International Council for Harmonisation. (2025). ICH E6(R3) Guideline for Good Clinical Practice. https://database.ich.org/sites/default/files/ICH_E6%28R3%29_Step4_FinalGuideline_2025_0106.pdf

> `ref_004` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1, Ch.2

**[5]** National Institutes of Health. (2026). Updated elements of an NIH Data Management and Sharing Plan. https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-046.html

> `ref_005` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1

**[6]** Harris, P. A., Taylor, R., Thielke, R., Payne, J., Gonzalez, N., & Conde, J. G. (2009). Research electronic data capture (REDCap) — A metadata-driven methodology and workflow process for providing translational research informatics support. *Journal of Biomedical Informatics*, 42, 377–381. https://doi.org/10.1016/j.jbi.2008.08.010

> `ref_006` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[7]** National Institutes of Health. (2020). Final NIH Policy for Data Management and Sharing. https://grants.nih.gov/grants/guide/notice-files/NOT-OD-21-013.html

> `ref_007` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1

**[8]** National Institutes of Health. (2020). Supplemental information to the NIH Policy for Data Management and Sharing: Elements of an NIH Data Management and Sharing Plan. https://grants.nih.gov/grants/guide/notice-files/NOT-OD-21-014.html

> `ref_008` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1

**[9]** HL7 International. (2023). FHIR. https://hl7.org/fhir/

> `ref_009` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.3

**[10]** HL7 International. (n.d.). FHIR to OMOP Implementation Guide. http://hl7.org/fhir/uv/omop/

> `ref_010` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.3

**[11]** Sachson, C. (2025). Our journey. Observational Health Data Sciences and Informatics. https://www.ohdsi.org/wp-content/uploads/2025/10/OurJourney-2025.pdf

> `ref_011` · Thiếu trường thư mục, cần bổ sung · dùng ở: Ch.3, Ch.4 · cần xử lý: tieu de: muc ghi "Our journey" (2025) trong khi van ban (ch03, muc 3.4) mo ta nhu The Book of OHDSI

**[12]** Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018. https://doi.org/10.1038/sdata.2016.18

> `ref_012` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1, Ch.6

**[13]** Society for Clinical Data Management. (n.d.). GCDMP — Good Clinical Data Management Practices. https://scdm.org/gcdmp/

> `ref_013` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[14]** DAMA International. (2017). DAMA-DMBOK: Data Management Body of Knowledge. Technics Publications.

> `ref_014` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1, Ch.2

**[15]** Association of American Medical Colleges. (2015). Data governance in academic medicine. https://www.aamc.org/media/34986/download

> `ref_015` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1

**[16]** Wendelborn, C., Anger, M., & Schickhardt, C. (2023). What is data stewardship? Towards a comprehensive understanding. *Journal of Biomedical Informatics*, 140, 104337. https://doi.org/10.1016/j.jbi.2023.104337

> `ref_016` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[17]** Jetten, M., Grootveld, M., Mordant, A., Jansen, M., Bloemers, M., Miedema, M., & van Gelder, C. W. G. (2021). Professionalising data stewardship in the Netherlands: Competences, training and education. Dutch roadmap towards national implementation of FAIR data stewardship. Zenodo. https://doi.org/10.5281/zenodo.4623713

> `ref_017` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1

**[18]** The Turing Way Community. (n.d.). Data stewards: Overview. In *The Turing Way: A handbook for reproducible, ethical and collaborative research*. https://book.the-turing-way.org/collaboration/research-infrastructure-roles/data-steward/

> `ref_018` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[19]** CASRAI. (n.d.). Horizon Europe FAIR Data Management Plan. https://casrai.org/guides/horizon-europe-fair-data-management-plan

> `ref_019` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[20]** [thiếu tác giả và năm trong .bib]. Expert Advisory Group on Data Access. (2017, August). *Data management plans: Recommendations*. https://cms.wellcome.org/sites/default/files/data-management-plans.pdf

> `ref_020` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[21]** Jacobsen, A., Kaliyaperumal, R., Bonino da Silva Santos, L. O., Mons, B., Schultes, E., Roos, M., & Thompson, M. (2020). A generic workflow for the data FAIRification process. *Data Intelligence*, 2, 56–65. https://doi.org/10.1162/dint_a_00028

> `ref_021` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.6

**[22]** DataCite Metadata Working Group. (2024). DataCite Metadata Schema for the publication and citation of research data and other research outputs. DataCite e. https://doi.org/10.14454/mzv1-5b55

> `ref_022` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.6

**[23]** Villere, S. (2024). Common Data Elements Repository. *Medical Reference Services Quarterly*, 43, 182–190. https://doi.org/10.1080/02763869.2024.2323896

> `ref_023` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[24]** U.S. Food and Drug Administration. (2024). Electronic systems, electronic records, and electronic signatures in clinical investigations: Questions and answers. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/electronic-systems-electronic-records-and-electronic-signatures-clinical-investigations-questions

> `ref_024` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[25]** CASRAI. (n.d.). Castor EDC & lightweight EDC for IITs. https://casrai.org/guides/castor-edc-lightweight-edc-investigator-initiated-trials

> `ref_025` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[26]** Yamamoto, K., Ota, K., Akiya, I., & Shintani, A. (2017). A pragmatic method for transforming clinical research data from the research electronic data capture “REDCap” to Clinical Data Interchange Standards Consortium (CDISC) Study Data Tabulation Model (SDTM): Development and evaluation of REDCap2SDTM. *Journal of Biomedical Informatics*, 70, 65–76. https://doi.org/10.1016/j.jbi.2017.05.003

> `ref_026` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2, Ch.3

**[27]** Gurley, M. J., Warner, J., Bushmanova, Y., & Wehbe, F. (2021). REDCap2OMOP: A platform for ETLing REDCap projects into the OMOP CDM. https://www.ohdsi.org/wp-content/uploads/2021/09/65_REDCap2OMOP.pdf

> `ref_027` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2, Ch.3

**[28]** Weiskopf, N. G., & Weng, C. (2013). Methods and dimensions of electronic health record data quality assessment: Enabling reuse for clinical research. *Journal of the American Medical Informatics Association*, 20, 144–151. https://doi.org/10.1136/amiajnl-2011-000681

> `ref_028` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.4

**[29]** Sheetz, N., Wilson, B., Benedict, J., Huffman, E., Lawton, A., Travers, M., Nadolny, P., Young, S., Given, K., & Florin, L. (2014). Evaluating source data verification as a quality control measure in clinical trials. *Therapeutic Innovation & Regulatory Science*, 48, 671–680. https://doi.org/10.1177/2168479014554400

> `ref_029` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[30]** Kahn, M. G., Callahan, T. J., Barnard, J., Bauck, A. E., Brown, J., Bruce, B. B., Desai, S., Downs, M., Fiechtner, C., Groeneveld, P. W., Kittel, C., Kitzmiller, R. R., & [CẦN KIỂM CHỨNG các tác giả còn lại — đối chiếu PMC5051581 để ghi đúng 20 tác giả đầu + et al.]. (2016). A harmonized data quality assessment terminology and framework for the secondary use of electronic health record data. *eGEMs*, 4, 1244. https://doi.org/10.13063/2327-9214.1244 (CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.)

> `ref_030` · Thiếu trường thư mục, cần bổ sung · dùng ở: Ch.4 · cần xử lý: một trường thư mục bị đánh dấu trong văn bản nguồn

**[31]** Rubin, D. B. (1976). Inference and missing data. *Biometrika*, 63, 581–592. https://doi.org/10.1093/biomet/63.3.581

> `ref_031` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.4

**[32]** Sterne, J. A. C., White, I. R., Carlin, J. B., Spratt, M., Royston, P., Kenward, M. G., Wood, A. M., & Carpenter, J. R. (2009). Multiple imputation for missing data in epidemiological and clinical research: Potential and pitfalls. *BMJ*, 338, b2393. https://doi.org/10.1136/bmj.b2393

> `ref_032` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.4

**[33]** Baker, M. (2016). 1,500 scientists lift the lid on reproducibility. *Nature*, 533, 452–454. https://doi.org/10.1038/533452a

> `ref_033` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1, Ch.4

**[34]** CDISC, & HL7 International. (2021). FHIR to CDISC Joint Mapping Implementation Guide. https://www.cdisc.org/standards/real-world-data/fhir-cdisc-joint-mapping-implementation-guide-v1-0

> `ref_034` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.3

**[35]** HL7 International. (2026). Valueset-example-characteristic-codes. In *FHIR*. http://hl7.org/fhir/6.0.0-ballot5/valueset-example-characteristic-codes.html

> `ref_035` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[36]** Mandel, J. C., Kreda, D. A., Mandl, K. D., Kohane, I. S., & Ramoni, R. B. (2016). SMART on FHIR: A standards-based, interoperable apps platform for electronic health records. *Journal of the American Medical Informatics Association*, 23, 899–908. https://doi.org/10.1093/jamia/ocv189

> `ref_036` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.3

**[37]** Mandl, K. D., Gottlieb, D., & Mandel, J. C. (2020). Push Button Population Health: The SMART/HL7 FHIR Bulk Data Access API. *npj Digital Medicine*, 3, 151. https://doi.org/10.1038/s41746-020-00358-4

> `ref_037` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.3

**[38]** Hripcsak, G., Duke, J. D., Shah, N. H., Reich, C. G., Huser, V., Schuemie, M. J., Suchard, M. A., Park, R. W., Wong, I. C. K., Rijnbeek, P. R., van der Lei, J., Pratt, N., Norén, G. N., Li, Y.-C., Stang, P. E., Madigan, D., & Ryan, P. B. (2015). Observational Health Data Sciences and Informatics (OHDSI): Opportunities for observational researchers. *Studies in Health Technology and Informatics*, 216, 574–578. https://pmc.ncbi.nlm.nih.gov/articles/PMC4815923/

> `ref_038` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.3, Ch.4

**[39]** Overhage, J. M., Ryan, P. B., Reich, C. G., Hartzema, A. G., & Stang, P. E. (2012). Validation of a common data model for active safety surveillance research. *Journal of the American Medical Informatics Association*, 19, 54–60. https://doi.org/10.1136/amiajnl-2011-000376

> `ref_039` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.3

**[40]** Suchard, M. A., Schuemie, M. J., Krumholz, H. M., You, S. C., Chen, R., Pratt, N., Reich, C. G., Duke, J., Madigan, D., Hripcsak, G., & Ryan, P. B. (2019). Comprehensive comparative effectiveness and safety of first-line antihypertensive drug classes: A systematic, multinational, large-scale analysis. *The Lancet*, 394, 1816–1826. https://doi.org/10.1016/s0140-6736(19)32317-7

> `ref_040` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.3

**[41]** Queralt-Rosinach, N., Kaliyaperumal, R., Bernabé, C. H., Long, Q., Joosten, S. A., van der Wijk, H. J., Flikkenschild, E. L. A., Burger, K., Jacobsen, A., Mons, B., & Roos, M. (2022). Applying the FAIR principles to data in a hospital: Challenges and opportunities in a pandemic. *Journal of Biomedical Semantics*, 13, Article. https://doi.org/10.1186/s13326-022-00263-7

> `ref_041` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[42]** Sinaci, A. A., Núñez-Benjumea, F. J., Gencturk, M., Jauer, M.-L., Deserno, T., Chronaki, C., Cangioli, G., Cavero-Barca, C., Rodríguez-Pérez, J. M., Pérez-Pérez, M. M., Laleci Erturkmen, G. B., Hernández-Pérez, T., Méndez-Rodríguez, E., & Parra-Calderón, C. L. (2020). From raw data to FAIR data: The FAIRification workflow for health research. *Methods of Information in Medicine*, 59, e21–e32. https://doi.org/10.1055/s-0040-1713684

> `ref_042` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[43]** Kasbohm, E., Inau, E. T., Zeleke, A. A., Shiferaw, K. B., Abaza, H., Clemens, V., Golebiewski, M., Gonzalez-Ocanto, M., Klopfenstein, S. A. I., Vorisek, C. N., Waltemath, D., & Schmidt, C. O. (2025). Lessons learned from evaluating the NFDI4Health metadata schema for health studies using the Research Data Alliance's FAIR data maturity model. *medRxiv*. https://doi.org/10.1101/2025.09.26.25336637

> `ref_043` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.6

**[44]** Rocca-Serra, P., Gu, W., Ioannidis, V., Abbassi-Daloii, T., Capella-Gutierrez, S., Chandramouliswaran, I., Splendiani, A., Burdett, T., Giessmann, R. T., Henderson, D., Batista, D., Emam, I., Gadiya, Y., Giovanni, L., Willighagen, E., Evelo, C., Gray, A. J. G., Gribbon, P., Juty, N., … Sansone, S.-A. (2023). The FAIR Cookbook — the essential resource for and by FAIR doers. *Scientific Data*, 10, 292. https://doi.org/10.1038/s41597-023-02166-3

> `ref_044` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.6

**[45]** Wilkinson, M. D., Dumontier, M., Sansone, S.-A., Bonino da Silva Santos, L. O., Prieto, M., Batista, D., McQuilton, P., Kuhn, T., Rocca-Serra, P., Crosas, M., Schultes, E., & …. (2019). Evaluating FAIR maturity through a scalable, automated, community-governed framework. *Scientific Data*, 6, 174. https://doi.org/10.1038/s41597-019-0184-5

> `ref_045` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[46]** UNESCO. (2021). UNESCO Recommendation on Open Science. https://www.unesco.org/en/open-science/about

> `ref_046` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[47]** Taichman, D. B., Sahni, P., Pinborg, A., Peiperl, L., Laine, C., James, A., Hong, S.-T., Haileamlak, A., Gollogly, L., Godlee, F., Frizelle, F. A., Florenzano, F., Drazen, J. M., Bauchner, H., Baethge, C., & Backus, J. (2017). Data sharing statements for clinical trials: A requirement of the International Committee of Medical Journal Editors. *Journal of Korean Medical Science*, 32, 1051–1053. https://doi.org/10.3346/jkms.2017.32.7.1051

> `ref_047` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[48]** U.S. National Library of Medicine. ([CẦN KIỂM CHỨNG] ngày cập nhật). Clinical trial reporting requirements. https://clinicaltrials.gov/policy/reporting-requirements (CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.)

> `ref_048` · Thiếu trường thư mục, cần bổ sung · dùng ở: chỉ trong bản tổng hợp · cần xử lý: một trường thư mục bị đánh dấu trong văn bản nguồn

**[49]** Mughal, Z., Fu, R., Luechtefeld, T., Chiswell, K., Kleinstreuer, N., Shaw, G., & Tidmarsh, G. F. (2025). Compliance with results reporting at ClinicalTrials.gov before and after the 2017 FDAAA Final Rule: A comparative analysis. *Journal of the Academy of Public Health*, 1. https://doi.org/10.70542/rcj-japh-art-vr3aga (CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.)

> `ref_049` · Thiếu trường thư mục, cần bổ sung · dùng ở: chỉ trong bản tổng hợp · cần xử lý: một trường thư mục bị đánh dấu trong văn bản nguồn

**[50]** Stuart, D., Baynes, G., Hrynaszkiewicz, I., Allin, K., Penny, D., Lucraft, M., & Astell, M. (2018). Practical challenges for researchers in data sharing. https://doi.org/10.6084/m9.figshare.5975011

> `ref_050` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[51]** National Center for Complementary and Integrative Health. (n.d.). Preferred repositories. https://www.nccih.nih.gov/grants/policies/data-management-and-sharing-policy/preferred-repositories

> `ref_051` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[52]** Byrd, J. B., Greene, A. C., Prasad, D. V., Jiang, X., & Greene, C. S. (2020). Responsible, practical genomic data sharing that accelerates research. *Nature Reviews Genetics*, 21, 615–629. https://doi.org/10.1038/s41576-020-0257-5

> `ref_052` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[53]** [thiếu tác giả và năm trong .bib]. Vivli. (2018, July 20). *Innovative global data-sharing platform Vivli launches with 2,500 clinical studies*. https://vivli.org/innovative-global-data-sharing-platform-vivli-launches-with-2500-clinical-studies/

> `ref_053` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[54]** [thiếu tác giả và năm trong .bib]. Regulation (EU) No 536/2014 of the European Parliament and of the Council of 16 April 2014 on clinical trials on medicinal products for human use and repealing Directive 2001/20/EC. *Official Journal of the European Union*, 158, L. https://eur-lex.europa.eu/eli/reg/2014/536/oj

> `ref_054` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[55]** Bộ Y tế. (2025). Thông tư 33/2025/TT-BYT quy định thời hạn lưu trữ hồ sơ, tài liệu ngành y tế. https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Thong-tu-33-2025-TT-BYT-thoi-han-luu-tru-ho-so-tai-lieu-nganh-y-te-663505.aspx

> `ref_055` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[56]** Chandramouli, R., & Hibbard, E. A. (2025). Guidelines for media sanitization. National Institute of Standards and Technology. https://doi.org/10.6028/nist.sp.800-88r2

> `ref_056` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[57]** [thiếu tác giả và năm trong .bib]. Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data (General Data Protection Regulation). *Official Journal of the European Union*, 119, L. https://eur-lex.europa.eu/eli/reg/2016/679/oj

> `ref_057` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[58]** [thiếu tác giả và năm trong .bib]. Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the European Health Data Space and amending Directive 2011/24/EU and Regulation (EU) 2024/2847. *Official Journal of the European Union*, 2025, L. https://eur-lex.europa.eu/eli/reg/2025/327/oj

> `ref_058` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[59]** Raposo, V. L. (2025). Can personal data be recycled? The reuse and repurposing of data under the EHDS. *International Journal of Law and Information Technology*, 33, Article. https://doi.org/10.1093/ijlit/eaae016

> `ref_059` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[60]** [thiếu tác giả và năm trong .bib]. Standards for Privacy of Individually Identifiable Health Information, 45 CFR §164.514 (U.S. Department of Health and Human Services). https://www.ecfr.gov/current/title-45/section-164.514

> `ref_060` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[61]** Sant, M. M., & Bajada, C. J. (2025). Processing neuroimaging data for research purposes: Open Science, FAIR data, and the GDPR. *International Data Privacy Law*, 15, 194. https://doi.org/10.1093/idpl/ipaf020 (CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.)

> `ref_061` · Thiếu trường thư mục, cần bổ sung · dùng ở: chỉ trong bản tổng hợp · cần xử lý: một trường thư mục bị đánh dấu trong văn bản nguồn

**[62]** Quốc hội. (2025). Luật Bảo vệ dữ liệu cá nhân.

> `ref_062` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[63]** Chính phủ. (2025). Nghị định 356/2025/NĐ-CP hướng dẫn Luật Bảo vệ dữ liệu cá nhân.

> `ref_063` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[64]** Quốc hội. (2024). Luật Dữ liệu.

> `ref_064` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[65]** Bộ Y tế. (2025). Thông tư 13/2025/TT-BYT hướng dẫn triển khai hồ sơ bệnh án điện tử.

> `ref_065` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[66]** Bộ Y tế. (2025). Thông tư 50/2025/TT-BYT quy định về thử thuốc trên lâm sàng.

> `ref_066` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[67]** Research Data Management Support. (2023). K-anonymity, l-diversity and t-closeness. In *Data Privacy Handbook*. https://doi.org/10.5281/zenodo.8005847

> `ref_067` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[68]** Sweeney, L. (2002). k-Anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, 10, 557–570. https://doi.org/10.1142/s0218488502001648 (CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.)

> `ref_068` · Thiếu trường thư mục, cần bổ sung · dùng ở: Ch.5 · cần xử lý: một trường thư mục bị đánh dấu trong văn bản nguồn

**[69]** Machanavajjhala, A., Kifer, D., Gehrke, J., & Venkitasubramaniam, M. (2007). ℓ-Diversity: Privacy beyond k-anonymity. *ACM Transactions on Knowledge Discovery from Data*, 1, Article. https://doi.org/10.1145/1217299.1217302

> `ref_069` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.5

**[70]** Dwork, C. (2008). Differential privacy: A survey of results. In *Theory and Applications of Models of Computation*. https://doi.org/10.1007/978-3-540-79228-4_1

> `ref_070` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.5

**[71]** Sadilek, A., Liu, L., Nguyen, D., Kamruzzaman, M., Serghiou, S., Rader, B., Ingerman, A., Mellem, S., Kairouz, P., Nsoesie, E. O., MacFarlane, J., Vullikanti, A., Marathe, M., Eastham, P., Brownstein, J. S., Aguera y Arcas, B., Howell, M. D., & Hernandez, J. (2021). Privacy-first health research with federated learning. *npj Digital Medicine*, 4, 132. https://doi.org/10.1038/s41746-021-00489-2

> `ref_071` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[72]** Clark, T., Caufield, J. H., Parker, J. A., Al Manir, S., Amorim, E., Eddy, J., Gim, N., Gow, B., Goar, W., Haendel, M., Hansen, J. N., Harris, N., Hermjakob, H., Joachimiak, M., Jordan, G., Lee, I.-H., McWeeney, S. K., Nebeker, C., Nikolov, M., … Munoz-Torres, M. C. (2024). AI-readiness criteria for biomedical data. *bioRxiv*. https://doi.org/10.1101/2024.10.23.619844

> `ref_072` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.6

**[73]** Alderman, J. E., Palmer, J., Laws, E., McCradden, M. D., Ordish, J., Ghassemi, M., Pfohl, S. R., Rostamzadeh, N., Cole-Lewis, H., Glocker, B., Calvert, M., Pollard, T. J., Gill, J., Gath, J., Adebajo, A., Beng, J., Leung, C. H., Kuku, S., Farmer, L.-A., … Liu, X. (2025). Tackling algorithmic bias and promoting transparency in health datasets: The STANDING Together consensus recommendations. *The Lancet Digital Health*, 7, e64–e88. https://doi.org/10.1016/s2589-7500(24)00224-3

> `ref_073` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.6

**[74]** Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM*, 64, 86–92. https://doi.org/10.1145/3458723

> `ref_074` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.6

**[75]** CASRAI. (2026). Trusted research environments & Five Safes framework. https://casrai.org/guides/trusted-research-environments-five-safes-framework

> `ref_075` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[76]** Albashiti, F., Thasler, R., Wendt, T., Bathelt, F., Reinecke, I., & Schreiweis, B. (2024). Die Datenintegrationszentren — Von der Konzeption in der Medizininformatik-Initiative zur lokalen Umsetzung in einem Netzwerk Universitätsmedizin [Data integration centers—From a concept in the Medical Informatics Initiative to its local implementation in the Network of University Medicine]. *Bundesgesundheitsblatt – Gesundheitsforschung – Gesundheitsschutz*, 67, 629–636. https://doi.org/10.1007/s00103-024-03879-5

> `ref_076` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[77]** Danciu, I., Cowan, J. D., Basford, M., Wang, X., Saip, A., Osgood, S., Shirey-Rice, J., Kirby, J., & Harris, P. A. (2014). Secondary use of clinical data: The Vanderbilt approach. *Journal of Biomedical Informatics*, 52, 28–35. https://doi.org/10.1016/j.jbi.2014.02.003

> `ref_077` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[78]** Callahan, A., Ashley, E., Datta, S., Desai, P., Ferris, T. A., Fries, J. A., Halaas, M., Langlotz, C. P., Mackey, S., Posada, J. D., Pfeffer, M. A., & Shah, N. H. (2023). The Stanford Medicine data science ecosystem for clinical and translational research. *JAMIA Open*, 6, ooad054. https://doi.org/10.1093/jamiaopen/ooad054

> `ref_078` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[79]** Bộ Chính trị. (2024). Nghị quyết 57-NQ/TW về đột phá phát triển khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số quốc gia.

> `ref_079` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.5

**[80]** Bộ Chính trị. (2025). Nghị quyết 72-NQ/TW về một số giải pháp đột phá, tăng cường bảo vệ, chăm sóc và nâng cao sức khỏe nhân dân.

> `ref_080` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.5

**[81]** Thủ tướng Chính phủ. (2026). Quyết định 1308/QĐ-TTg phê duyệt Chiến lược dữ liệu quốc gia giai đoạn 2026–2030, tầm nhìn đến năm 2045.

> `ref_081` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.5

**[82]** Bộ Y tế. (2026). Quyết định 3218/QĐ-BYT ban hành Quy chế quản lý, vận hành, sử dụng, khai thác, chia sẻ dữ liệu và bảo đảm an ninh mạng Cổng dữ liệu sức khỏe của Bộ Y tế.

> `ref_082` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.5

**[83]** Tran, D. M., Thwaites, C. L., Van Nuil, J. I., McKnight, J., Luu, A. P., Paton, C., & Vietnam ICU Translational Applications Laboratory (VITAL). (2022). Digital health policy and programs for hospital care in Vietnam: Scoping review. *Journal of Medical Internet Research*, 24, e32392. https://doi.org/10.2196/32392

> `ref_083` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[84]** Tran, D. M., et al. (2025). Status of digital health technology adoption in 5 Vietnamese hospitals: Cross-sectional assessment. *JMIR Formative Research*, 9, e53483. https://doi.org/10.2196/53483

> `ref_084` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[85]** Trịnh Văn Vinh. (2025). Digital transformation in electronic medical record management towards a smart and sustainable healthcare system. *Vietnam Journal of Community Medicine*, 66, 262–268. https://doi.org/10.52163/yhc.v66i4.2905

> `ref_085` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[86]** Pharma Group, KPMG, & Oxford University Clinical Research Unit. (2025). Roadmap to the future of clinical trials in Vietnam. https://assets.kpmg.com/content/dam/kpmgsites/vn/pdf/2025/05/roadmap-clinical-trials-in-vietnam-vi.pdf

> `ref_086` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[87]** Warnat-Herresthal, S., Schultze, H., Shastry, K. L., Manamohan, S., Mukherjee, S., Garg, V., Sarveswara, R., Händler, K., Pickkers, P., Aziz, N. A., Ktena, S., Tran, F., Bitzer, M., Ossowski, S., Casadei, N., Herr, C., Petersheim, D., Behrends, U., Kern, F., … Schultze, J. L. (2021). Swarm Learning for decentralized and confidential clinical machine learning. *Nature*, 594, 265–270. https://doi.org/10.1038/s41586-021-03583-3

> `ref_087` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[88]** Friedman, C. P., Lomotan, E. A., Richardson, J. E., & Ridgeway, J. L. (2024). Socio-technical infrastructure for a learning health system. *Learning Health Systems*, 8, e10405. https://doi.org/10.1002/lrh2.10405

> `ref_088` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[89]** Dayan, I., Roth, H. R., Zhong, A., Harouni, A., Gentili, A., Abidin, A. Z., Liu, A., Costa, A. B., Wood, B. J., Tsai, C.-S., Wang, C.-H., Hsu, C.-N., Lee, C. K., Ruan, P., Xu, D., Wu, D., Huang, E., Kitamura, F. C., … Li, Q. (2021). Federated learning for predicting clinical outcomes in patients with COVID-19. *Nature Medicine*, 27, 1735–1743. https://doi.org/10.1038/s41591-021-01506-3 (CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.)

> `ref_089` · Thiếu trường thư mục, cần bổ sung · dùng ở: chỉ trong bản tổng hợp · cần xử lý: một trường thư mục bị đánh dấu trong văn bản nguồn

**[90]** Pati, S., Baid, U., Edwards, B., Sheller, M., Wang, S.-H., Reina, G. A., Foley, P., Gruzdev, A., Karkada, D., Davatzikos, C., Sako, C., Ghodasara, S., Bilello, M., Mohan, S., Vollmuth, P., Brugnara, G., Preetha, C. J., Sahm, F., Maier-Hein, K., … Bakas, S. (2022). Federated learning enables big data for rare cancer boundary detection. *Nature Communications*, 13, 7346. https://doi.org/10.1038/s41467-022-33407-5

> `ref_090` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[91]** Heyndrickx, W., et al. (2024). MELLODDY: Cross-pharma federated learning at unprecedented scale unlocks benefits in QSAR without compromising proprietary information. *Journal of Chemical Information and Modeling*, 64, 2331–2344. https://doi.org/10.1021/acs.jcim.3c00799

> `ref_091` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[92]** Bakas, S., Li, X., Shah, P., & Roth, H. R. (2026). Federated learning in healthcare: From research to real-world deployment. *Annual Review of Biomedical Engineering*, 28, 163–186. https://doi.org/10.1146/annurev-bioeng-080125-041414

> `ref_092` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[93]** Walonoski, J., Kramer, M., Nichols, J., Quina, A., Moesel, C., Hall, D., Duffett, C., Dube, K., Gallagher, T., & McLachlan, S. (2018). Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record. *Journal of the American Medical Informatics Association*, 25, 230–238. https://doi.org/10.1093/jamia/ocx079

> `ref_093` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.3

**[94]** Wagner, Z., & Blacketer, C. (2024). Evaluating Synthea: Comprehensive analysis of a leading synthesized medical record generator. https://www.ohdsi.org/wp-content/uploads/2024/10/41-Wagner-Evaluating_Synthea-Clair-Blacketer.pdf

> `ref_094` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[95]** Hao, Y., He, H., & Ho, J. C. (2024). LLMSYN: Generating synthetic electronic health records without patient-level data. In *Proceedings of the 9th Machine Learning for Healthcare Conference*. https://proceedings.mlr.press/v252/hao24a.html (CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.)

> `ref_095` · Chưa xác định · dùng ở: chỉ trong bản tổng hợp · cần xử lý: undetermined from text flag

**[96]** Chen, X., Wu, Z., Shi, X., Cho, H., & Mukherjee, B. (2025). Generating synthetic electronic health record data: A methodological scoping review with benchmarking on phenotype data and open-source software. *Journal of the American Medical Informatics Association*, 32, 1227–1240. https://doi.org/10.1093/jamia/ocaf082

> `ref_096` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[97]** Goldacre, B., & Morley, J. (2022). Better, broader, safer: Using health data for research and analysis. UK Department of Health and Social Care.

> `ref_097` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.6

**[98]** Williamson, E. J., Walker, A. J., Bhaskaran, K., Bacon, S., Bates, C., Morton, C. E., Curtis, H. J., Mehrkar, A., Evans, D., Inglesby, P., Cockburn, J., McDonald, H. I., MacKenna, B., Tomlinson, L., Douglas, I. J., Rentsch, C. T., Mathur, R., Wong, A. Y. S., Grieve, R., … Goldacre, B. (2020). Factors associated with COVID-19-related death using OpenSAFELY. *Nature*, 584, 430–436. https://doi.org/10.1038/s41586-020-2521-4

> `ref_098` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[99]** Friedman, C. P., Rubin, J., Brown, J., Buntin, M., Corn, M., Etheredge, L., Gunter, C., Musen, M., Platt, R., Stead, W., Sullivan, K., & Van Houweling, D. (2015). Toward a science of learning systems: A research agenda for the high-functioning Learning Health System. *Journal of the American Medical Informatics Association*, 22, 43–50. https://doi.org/10.1136/amiajnl-2014-002977

> `ref_099` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[100]** Trusted Research and Real-world Utilisation and Sharing Tech (TRUST). (n.d.). TRUST Platform: Home. https://www.trustplatform.sg/ (CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.)

> `ref_100` · Chưa xác định · dùng ở: chỉ trong bản tổng hợp · cần xử lý: undetermined from text flag

**[101]** Ministry of Health and Welfare, Republic of Korea. (n.d.). Overview of K-CURE Service. https://k-cure.mohw.go.kr/portal/cmm/htm/engKcureService.do (CẦN KIỂM CHỨNG: một trường chưa xác minh đầy đủ trong bảng APA 334 mục; xem ghi chú của mục gốc trước khi nộp.)

> `ref_101` · Chưa xác định · dùng ở: chỉ trong bản tổng hợp · cần xử lý: undetermined from text flag

**[102]** Harris, P. A., et al. (2019). The REDCap consortium: Building an international community of software platform partners. *Journal of Biomedical Informatics*, 95, 103208. https://doi.org/10.1016/j.jbi.2019.103208

> `ref_102` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[103]** Lane, J. C. E., Weaver, J., Kostka, K., Duarte-Salles, T., Abrahao, M. T. F., Alghoul, H., Alser, O., Alshammari, T. M., Biedermann, P., Banda, J. M., Burn, E., Casajust, P., Conover, M. M., Culhane, A. C., Davydov, A., DuVall, S. L., Dymshyts, D., Fernandez-Bertolin, S., Fišter, K., … Prieto-Alhambra, D. (2020). Risk of hydroxychloroquine alone and in combination with azithromycin in the treatment of rheumatoid arthritis: a multinational, retrospective study. *The Lancet Rheumatology*, 2, e698–e711. https://doi.org/10.1016/s2665-9913(20)30276-9

> `ref_103` · Đã đối chiếu, chưa kiểm toán · dùng ở: chỉ trong bản tổng hợp

**[104]** Ziemann, M., Eren, Y., & El-Osta, A. (2016). Gene name errors are widespread in the scientific literature. *Genome Biology*, 17, 177. https://doi.org/10.1186/s13059-016-1044-7

> `ref_104` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[105]** Begley, C. G., & Ellis, L. M. (2012). Drug development: Raise standards for preclinical cancer research. *Nature*, 483, 531–533. https://doi.org/10.1038/483531a

> `ref_105` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1

**[106]** Freedman, L. P., Cockburn, I. M., & Simcoe, T. S. (2015). The economics of reproducibility in preclinical research. *PLoS Biology*, 13(6), e1002165. https://doi.org/10.1371/journal.pbio.1002165

> `ref_106` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1

**[107]** Mehra, M. R., Ruschitzka, F., & Patel, A. N. (2020). Retraction—Hydroxychloroquine or chloroquine with or without a macrolide for treatment of COVID-19: a multinational registry analysis. *The Lancet*, 395, 1820. https://doi.org/10.1016/S0140-6736(20)31324-6

> `ref_107` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1

**[108]** Mehra, M. R., Desai, S. S., Kuy, S., Henry, T. D., & Patel, A. N. (2020). Retraction: Cardiovascular disease, drug therapy, and mortality in Covid-19. *New England Journal of Medicine*, 382, 2582. https://doi.org/10.1056/NEJMc2021225

> `ref_108` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.1

**[109]** European Medicines Agency. (2010). Reflection paper on expectations for electronic source data and data transcribed to electronic data collection tools in clinical trials. https://www.ema.europa.eu/system/files/documents/regulatory-procedural-guideline/reflection-paper-expectations-electronic-source-data-data-transcribed-electronic-data-collection_en.pdf (VERIFIED_UNAUDITED; superseded by the 2023 EMA guideline.)

> `ref_109` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[110]** Medicines and Healthcare products Regulatory Agency. (2018). Guidance on GxP data integrity. https://www.gov.uk/government/publications/guidance-on-gxp-data-integrity (VERIFIED_UNAUDITED; published 9 March 2018.)

> `ref_110` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[111]** European Medicines Agency. (2023). Guideline on computerised systems and electronic data in clinical trials. https://www.ema.europa.eu/system/files/documents/regulatory-procedural-guideline/guideline_on_computerised_systems_and_electronic_data_in_clinical_trials_en.pdf (VERIFIED_UNAUDITED; final version adopted 7 March 2023.)

> `ref_111` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[112]** U.S. Food and Drug Administration. (1997). 21 CFR Part 11 — Electronic Records; Electronic Signatures. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11 (VERIFIED_UNAUDITED; eCFR checked 2026-11-21.)

> `ref_112` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.2

**[113]** European Parliament and Council of the European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). https://eur-lex.europa.eu/eli/reg/2016/679/oj (VERIFIED_UNAUDITED; EUR-Lex checked 2026-11-21.)

> `ref_113` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.5

**[114]** European Parliament and Council of the European Union. (2025). Regulation (EU) 2025/327 on the European Health Data Space. https://eur-lex.europa.eu/eli/reg/2025/327/oj (VERIFIED_UNAUDITED; EUR-Lex checked 2026-11-21; Article 105 dates recorded in legal appendix.)

> `ref_114` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.5

**[115]** United States Department of Health and Human Services. (n.d.). 45 CFR 164.514 — Other requirements relating to uses and disclosures of protected health information. https://www.ecfr.gov/current/title-45/section-164.514 (VERIFIED_UNAUDITED; eCFR checked 2026-11-21.)

> `ref_115` · Đã đối chiếu, chưa kiểm toán · dùng ở: Ch.5

## 3. Chỉ mục theo chương

Chỉ gồm các mục có khóa `ref_NNN` trong tệp chương hiện có. Chương 7, 8, 9 chưa viết nên chưa có.

- **Chương 1. Tổng quan RDM, vòng đời và DMP** (15 mục): [2], [3], [4], [5], [7], [8], [12], [14], [15], [17], [33], [105], [106], [107], [108]
- **Chương 2. Thu thập dữ liệu lâm sàng, ALCOA+ và REDCap** (16 mục): [4], [6], [13], [14], [23], [24], [25], [26], [27], [29], [102], [104], [109], [110], [111], [112]
- **Chương 3. CDISC, FHIR và OMOP** (12 mục): [9], [10], [11], [26], [27], [34], [36], [37], [38], [39], [40], [93]
- **Chương 4. Chất lượng dữ liệu và dữ liệu khuyết** (7 mục): [11], [28], [30], [31], [32], [33], [38]
- **Chương 5. Bảo mật và khử định danh** (10 mục): [68], [69], [70], [79], [80], [81], [82], [113], [114], [115]
- **Chương 6. FAIR, kho lưu trữ và dữ liệu sẵn sàng cho AI** (10 mục): [3], [12], [21], [22], [43], [44], [72], [73], [74], [97]

## 4. Việc còn mở

- 13 mục chưa ở trạng thái `VERIFIED_UNAUDITED`: [1], [2], [3], [11], [30], [48], [49], [61], [68], [89], [95], [100], [101].
- Chưa chạy kiểm toán độc lập (`scripts/audit_references.py` ghi nhận trạng thái; kiểm trang chỉ là đối chiếu, không đổi cột `status`).
- Chương 7, 8, 9 chưa có nguồn; chương 8 phải đi từ văn bản pháp luật chính thống (xem `docs/legal-verification.md`), không từ API học thuật.
- 334 mục của bản tổng hợp gốc nằm ở `references/references-334.bib`; chỉ 115 mục trong số đó đã vào danh mục đóng này.
