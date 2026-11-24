# Làm giàu metadata tham khảo bằng OpenAlex và Semantic Scholar

**Ngày chạy:** 2026-11-24 · **Công cụ:** `scripts/lit_harvest.py enrich` · **Nguồn:** API công khai OpenAlex, Semantic Scholar (khóa đọc từ biến môi trường, không lưu) · **Dữ liệu:** `references/references.bib` (115 mục, 61 có DOI)

**Loại báo cáo:** EXPLORE, sơ bộ, chưa sàng lọc. **Chỉ là metadata:** số trích dẫn, cờ rút bài, loại tài liệu, trạng thái truy cập mở. Không xác nhận nội dung khẳng định trong sách và không đổi cột `status` trong `citation-audit.csv`. Số trích dẫn khác nhau giữa hai nguồn là bình thường (phạm vi chỉ mục khác nhau).

## 1. Tóm tắt

| Hạng mục | Số mục | Ghi chú |
|---|---:|---|
| Mục có DOI trong `.bib` | 61 | được tra theo DOI trên cả hai API |
| Mục không có DOI | 54 | không tra trong báo cáo này (văn bản pháp luật, chuẩn, báo cáo, trang web, hoặc chưa có DOI) |
| Tìm thấy trên OpenAlex | 56 | |
| Tìm thấy trên Semantic Scholar | 54 | |
| **Bị đánh dấu rút bài (OpenAlex `is_retracted`)** | 0 | không |
| Năm khác giữa `.bib` và một API | 14 | thường là năm online và năm số tạp chí khác nhau; xem `references/VERIFICATION.md` |

**Lưu ý cho các mục rút bài:** bài Surgisphere (`ref_107`, `ref_108`) là bản thông báo rút bài (retraction notice) được dẫn có chủ ý trong case study; cờ rút bài ở đây có thể gắn với bài gốc bị rút chứ không phải thông báo. Cần xem từng dòng trước khi kết luận.

## 2. Bảng chi tiết (theo khóa)

| Khóa | Tác giả, năm (`.bib`) | Tiêu đề (`.bib`) | Chương dùng | OA: trích dẫn | OA: loại | OA: mở | OA: rút bài | S2: trích dẫn | S2: ảnh hưởng | Năm OA / S2 | DOI |
|---|---|---|---|---:|---|---|---|---:|---:|---|---|
| `ref_006` | Harris, 2009 | Research electronic data capture (REDCap) — A metadata-driven methodology and workflow pro | ch02 | 55160 | article | bronze | không | 48672 | 2809 | 2008 / 2008 | [10.1016/j.jbi.2008.08.010](https://doi.org/10.1016/j.jbi.2008.08.010) |
| `ref_012` | Wilkinson, 2016 | The FAIR Guiding Principles for scientific data management and stewardship | ch01, ch06 | 22070 | data-paper | gold | không | 18078 | 725 | 2016 / 2016 | [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18) |
| `ref_016` | Wendelborn, 2023 | What is data stewardship? Towards a comprehensive understanding | - | 58 | article | bronze | không | 31 | 0 | 2023 / 2023 | [10.1016/j.jbi.2023.104337](https://doi.org/10.1016/j.jbi.2023.104337) |
| `ref_017` | Jetten, 2021 | Professionalising data stewardship in the Netherlands: Competences, training and education | ch01 | n/a |  |  | n/a | n/a | n/a | - / - | [10.5281/zenodo.4623713](https://doi.org/10.5281/zenodo.4623713) |
| `ref_021` | Jacobsen, 2020 | A generic workflow for the data FAIRification process | ch06 | 150 | article | diamond | không | 116 | 7 | 2019 / 2020 | [10.1162/dint_a_00028](https://doi.org/10.1162/dint_a_00028) |
| `ref_022` | DataCite Metadata Working Group., 2024 | DataCite Metadata Schema for the publication and citation of research data and other resea | ch06 | n/a |  |  | n/a | n/a | n/a | - / - | [10.14454/mzv1-5b55](https://doi.org/10.14454/mzv1-5b55) |
| `ref_023` | Villere, 2024 | Common Data Elements Repository | ch02 | 6 | article | green | không | 8 | 0 | 2024 / 2024 | [10.1080/02763869.2024.2323896](https://doi.org/10.1080/02763869.2024.2323896) |
| `ref_026` | Yamamoto, 2017 | A pragmatic method for transforming clinical research data from the research electronic da | ch02, ch03 | 46 | article | bronze | không | 34 | 0 | 2017 / 2017 | [10.1016/j.jbi.2017.05.003](https://doi.org/10.1016/j.jbi.2017.05.003) |
| `ref_028` | Weiskopf, 2013 | Methods and dimensions of electronic health record data quality assessment: Enabling reuse | ch04 | 1545 | review | hybrid | không | 1222 | 70 | 2012 / 2013 | [10.1136/amiajnl-2011-000681](https://doi.org/10.1136/amiajnl-2011-000681) |
| `ref_029` | Sheetz, 2014 | Evaluating source data verification as a quality control measure in clinical trials | ch02 | 57 | article | hybrid | không | 41 | 1 | 2014 / 2014 | [10.1177/2168479014554400](https://doi.org/10.1177/2168479014554400) |
| `ref_030` | Kahn, 2016 | A harmonized data quality assessment terminology and framework for the secondary use of el | ch04 | 870 | article | diamond | không | 619 | 27 | 2016 / 2016 | [10.13063/2327-9214.1244](https://doi.org/10.13063/2327-9214.1244) |
| `ref_031` | Rubin, 1976 | Inference and missing data | ch04 | 12981 | article | closed | không | n/a | n/a | 1976 / - | [10.1093/biomet/63.3.581](https://doi.org/10.1093/biomet/63.3.581) |
| `ref_032` | Sterne, 2009 | Multiple imputation for missing data in epidemiological and clinical research: Potential a | ch04 | 8596 | article | hybrid | không | 7406 | 229 | 2009 / 2009 | [10.1136/bmj.b2393](https://doi.org/10.1136/bmj.b2393) |
| `ref_033` | Baker, 2016 | 1,500 scientists lift the lid on reproducibility | ch01, ch04 | 5326 | other | closed | không | 3687 | 96 | 2016 / 2016 | [10.1038/533452a](https://doi.org/10.1038/533452a) |
| `ref_036` | Mandel, 2016 | SMART on FHIR: A standards-based, interoperable apps platform for electronic health record | ch03 | 1094 | article | hybrid | không | 797 | 45 | 2016 / 2016 | [10.1093/jamia/ocv189](https://doi.org/10.1093/jamia/ocv189) |
| `ref_037` | Mandl, 2020 | Push Button Population Health: The SMART/HL7 FHIR Bulk Data Access API | ch03 | 77 | article | gold | không | 65 | 0 | 2020 / 2020 | [10.1038/s41746-020-00358-4](https://doi.org/10.1038/s41746-020-00358-4) |
| `ref_039` | Overhage, 2012 | Validation of a common data model for active safety surveillance research | ch03 | 618 | article | bronze | không | 539 | 27 | 2012 / 2012 | [10.1136/amiajnl-2011-000376](https://doi.org/10.1136/amiajnl-2011-000376) |
| `ref_040` | Suchard, 2019 | Comprehensive comparative effectiveness and safety of first-line antihypertensive drug cla | ch03 | 402 | article | bronze | không | 314 | 6 | 2019 / 2019 | [10.1016/s0140-6736(19)32317-7](https://doi.org/10.1016/s0140-6736(19)32317-7) |
| `ref_041` | Queralt-Rosinach, 2022 | Applying the FAIR principles to data in a hospital: Challenges and opportunities in a pand | - | 78 | article | gold | không | 55 | 4 | 2022 / 2021 | [10.1186/s13326-022-00263-7](https://doi.org/10.1186/s13326-022-00263-7) |
| `ref_042` | Sinaci, 2020 | From raw data to FAIR data: The FAIRification workflow for health research | - | 142 | article | hybrid | không | 106 | 7 | 2020 / 2020 | [10.1055/s-0040-1713684](https://doi.org/10.1055/s-0040-1713684) |
| `ref_043` | Kasbohm, 2025 | Lessons learned from evaluating the NFDI4Health metadata schema for health studies using t | ch06 | 0 | preprint | green | không | 0 | 0 | 2025 / 2025 | [10.1101/2025.09.26.25336637](https://doi.org/10.1101/2025.09.26.25336637) |
| `ref_044` | Rocca-Serra, 2023 | The FAIR Cookbook — the essential resource for and by FAIR doers | ch06 | 84 | data-paper | gold | không | 66 | 0 | 2023 / 2023 | [10.1038/s41597-023-02166-3](https://doi.org/10.1038/s41597-023-02166-3) |
| `ref_045` | Wilkinson, 2019 | Evaluating FAIR maturity through a scalable, automated, community-governed framework | - | 233 | data-paper | gold | không | 183 | 9 | 2019 / 2019 | [10.1038/s41597-019-0184-5](https://doi.org/10.1038/s41597-019-0184-5) |
| `ref_047` | Taichman, 2017 | Data sharing statements for clinical trials: A requirement of the International Committee | - | 15 | editorial | gold | không | 1 | 0 | 2017 / 2017 | [10.3346/jkms.2017.32.7.1051](https://doi.org/10.3346/jkms.2017.32.7.1051) |
| `ref_049` | Mughal, 2025 | Compliance with results reporting at ClinicalTrials.gov before and after the 2017 FDAAA Fi | - | 4 | article | closed | không | 2 | 0 | 2025 / 2025 | [10.70542/rcj-japh-art-vr3aga](https://doi.org/10.70542/rcj-japh-art-vr3aga) |
| `ref_050` | Stuart, 2018 | Practical challenges for researchers in data sharing | - | n/a |  |  | n/a | n/a | n/a | - / - | [10.6084/m9.figshare.5975011](https://doi.org/10.6084/m9.figshare.5975011) |
| `ref_052` | Byrd, 2020 | Responsible, practical genomic data sharing that accelerates research | - | 181 | review | hybrid | không | 130 | 1 | 2020 / 2020 | [10.1038/s41576-020-0257-5](https://doi.org/10.1038/s41576-020-0257-5) |
| `ref_056` | Chandramouli, 2025 | Guidelines for media sanitization | - | 13 | report | gold | không | 1 | 0 | 2025 / 2025 | [10.6028/nist.sp.800-88r2](https://doi.org/10.6028/nist.sp.800-88r2) |
| `ref_059` | Raposo, 2025 | Can personal data be recycled? The reuse and repurposing of data under the EHDS | - | 4 | article | green | không | 2 | 0 | 2025 / 2025 | [10.1093/ijlit/eaae016](https://doi.org/10.1093/ijlit/eaae016) |
| `ref_061` | Sant, 2025 | Processing neuroimaging data for research purposes: Open Science, FAIR data, and the GDPR | - | 5 | article | hybrid | không | n/a | n/a | 2025 / - | [10.1093/idpl/ipaf020](https://doi.org/10.1093/idpl/ipaf020) |
| `ref_067` | Research Data Management Support., 2023 | K-anonymity, l-diversity and t-closeness | - | n/a |  |  | n/a | n/a | n/a | - / - | [10.5281/zenodo.8005847](https://doi.org/10.5281/zenodo.8005847) |
| `ref_068` | Sweeney, 2002 | k-Anonymity: A model for protecting privacy | ch05 | 10122 | article | green | không | 9318 | 663 | 2002 / 2002 | [10.1142/s0218488502001648](https://doi.org/10.1142/s0218488502001648) |
| `ref_069` | Machanavajjhala, 2007 | ℓ-Diversity: Privacy beyond k-anonymity | ch05 | 4430 | article | closed | không | 5803 | 435 | 2007 / 2006 | [10.1145/1217299.1217302](https://doi.org/10.1145/1217299.1217302) |
| `ref_070` | Dwork, 2008 | Differential privacy: A survey of results | ch05 | 4672 | conference-paper | closed | không | 4304 | 303 | 2008 / 2008 | [10.1007/978-3-540-79228-4_1](https://doi.org/10.1007/978-3-540-79228-4_1) |
| `ref_071` | Sadilek, 2021 | Privacy-first health research with federated learning | - | 285 | article | gold | không | 238 | 3 | 2021 / 2020 | [10.1038/s41746-021-00489-2](https://doi.org/10.1038/s41746-021-00489-2) |
| `ref_072` | Clark, 2024 | AI-readiness criteria for biomedical data | ch06 | 55 | preprint | green | không | 5 | 0 | 2024 / 2024 | [10.1101/2024.10.23.619844](https://doi.org/10.1101/2024.10.23.619844) |
| `ref_073` | Alderman, 2025 | Tackling algorithmic bias and promoting transparency in health datasets: The STANDING Toge | ch06 | 280 | article | gold | không | 189 | 5 | 2024 / 2024 | [10.1016/s2589-7500(24)00224-3](https://doi.org/10.1016/s2589-7500(24)00224-3) |
| `ref_074` | Gebru, 2021 | Datasheets for datasets | ch06 | 5581 | article | green | không | 4180 | 279 | 2021 / 2018 | [10.1145/3458723](https://doi.org/10.1145/3458723) |
| `ref_076` | Albashiti, 2024 | Die Datenintegrationszentren — Von der Konzeption in der Medizininformatik-Initiative zur | - | 24 | article | hybrid | không | 14 | 0 | 2024 / 2024 | [10.1007/s00103-024-03879-5](https://doi.org/10.1007/s00103-024-03879-5) |
| `ref_077` | Danciu, 2014 | Secondary use of clinical data: The Vanderbilt approach | - | 308 | article | bronze | không | 276 | 18 | 2014 / 2014 | [10.1016/j.jbi.2014.02.003](https://doi.org/10.1016/j.jbi.2014.02.003) |
| `ref_078` | Callahan, 2023 | The Stanford Medicine data science ecosystem for clinical and translational research | - | 49 | article | gold | không | 37 | 1 | 2023 / 2023 | [10.1093/jamiaopen/ooad054](https://doi.org/10.1093/jamiaopen/ooad054) |
| `ref_083` | Tran, 2022 | Digital health policy and programs for hospital care in Vietnam: Scoping review | - | 64 | review | gold | không | 33 | 0 | 2022 / 2021 | [10.2196/32392](https://doi.org/10.2196/32392) |
| `ref_084` | Tran, 2025 | Status of digital health technology adoption in 5 Vietnamese hospitals: Cross-sectional as | - | 16 | article | gold | không | 9 | 1 | 2025 / 2023 | [10.2196/53483](https://doi.org/10.2196/53483) |
| `ref_085` | Trịnh Văn Vinh., 2025 | Digital transformation in electronic medical record management towards a smart and sustain | - | 0 | article | closed | không | n/a | n/a | 2025 / - | [10.52163/yhc.v66i4.2905](https://doi.org/10.52163/yhc.v66i4.2905) |
| `ref_087` | Warnat-Herresthal, 2021 | Swarm Learning for decentralized and confidential clinical machine learning | - | 1112 | article | hybrid | không | 872 | 43 | 2021 / 2021 | [10.1038/s41586-021-03583-3](https://doi.org/10.1038/s41586-021-03583-3) |
| `ref_088` | Friedman, 2024 | Socio-technical infrastructure for a learning health system | - | 59 | article | gold | không | 43 | 2 | 2024 / 2024 | [10.1002/lrh2.10405](https://doi.org/10.1002/lrh2.10405) |
| `ref_089` | Dayan, 2021 | Federated learning for predicting clinical outcomes in patients with COVID-19 | - | 1199 | article | hybrid | không | 874 | 32 | 2021 / 2021 | [10.1038/s41591-021-01506-3](https://doi.org/10.1038/s41591-021-01506-3) |
| `ref_090` | Pati, 2022 | Federated learning enables big data for rare cancer boundary detection | - | 539 | article | gold | không | 427 | 14 | 2022 / 2022 | [10.1038/s41467-022-33407-5](https://doi.org/10.1038/s41467-022-33407-5) |
| `ref_091` | Heyndrickx, 2024 | MELLODDY: Cross-pharma federated learning at unprecedented scale unlocks benefits in QSAR | - | 226 | article | hybrid | không | 172 | 12 | 2023 / 2023 | [10.1021/acs.jcim.3c00799](https://doi.org/10.1021/acs.jcim.3c00799) |
| `ref_092` | Bakas, 2026 | Federated learning in healthcare: From research to real-world deployment | - | 40 | review | hybrid | không | 29 | 0 | 2026 / 2026 | [10.1146/annurev-bioeng-080125-041414](https://doi.org/10.1146/annurev-bioeng-080125-041414) |
| `ref_093` | Walonoski, 2018 | Synthea: An approach, method, and software mechanism for generating synthetic patients and | ch03 | 680 | article | hybrid | không | 544 | 33 | 2017 / 2017 | [10.1093/jamia/ocx079](https://doi.org/10.1093/jamia/ocx079) |
| `ref_096` | Chen, 2025 | Generating synthetic electronic health record data: A methodological scoping review with b | - | 39 | review | green | không | 22 | 0 | 2025 / 2024 | [10.1093/jamia/ocaf082](https://doi.org/10.1093/jamia/ocaf082) |
| `ref_098` | Williamson, 2020 | Factors associated with COVID-19-related death using OpenSAFELY | - | 7393 | article | bronze | không | 4821 | 240 | 2020 / 2020 | [10.1038/s41586-020-2521-4](https://doi.org/10.1038/s41586-020-2521-4) |
| `ref_099` | Friedman, 2015 | Toward a science of learning systems: A research agenda for the high-functioning Learning | - | 603 | article | hybrid | không | 451 | 19 | 2014 / 2014 | [10.1136/amiajnl-2014-002977](https://doi.org/10.1136/amiajnl-2014-002977) |
| `ref_102` | Harris, 2019 | The REDCap consortium: Building an international community of software platform partners | ch02 | 26161 | article | bronze | không | 21610 | 984 | 2019 / 2019 | [10.1016/j.jbi.2019.103208](https://doi.org/10.1016/j.jbi.2019.103208) |
| `ref_103` | Lane, 2020 | Risk of hydroxychloroquine alone and in combination with azithromycin in the treatment of | - | 293 | article | hybrid | không | 123 | 5 | 2020 / 2020 | [10.1016/s2665-9913(20)30276-9](https://doi.org/10.1016/s2665-9913(20)30276-9) |
| `ref_104` | Ziemann, 2016 | Gene name errors are widespread in the scientific literature | ch02 | 198 | article | gold | không | 170 | 3 | 2016 / 2016 | [10.1186/s13059-016-1044-7](https://doi.org/10.1186/s13059-016-1044-7) |
| `ref_105` | Begley, 2012 | Drug development: Raise standards for preclinical cancer research | ch01 | 3413 | article | bronze | không | 2643 | 58 | 2012 / 2012 | [10.1038/483531a](https://doi.org/10.1038/483531a) |
| `ref_106` | Freedman, 2015 | The economics of reproducibility in preclinical research | ch01 | 1197 | article | gold | không | 988 | 26 | 2015 / 2015 | [10.1371/journal.pbio.1002165](https://doi.org/10.1371/journal.pbio.1002165) |
| `ref_107` | Mehra, 2020 | Retraction—Hydroxychloroquine or chloroquine with or without a macrolide for treatment of | ch01 | n/a |  |  | n/a | 648 | 23 | - / 2020 | [10.1016/s0140-6736(20)31324-6](https://doi.org/10.1016/s0140-6736(20)31324-6) |
| `ref_108` | Mehra, 2020 | Retraction: Cardiovascular disease, drug therapy, and mortality in Covid-19 | ch01 | 518 | retraction | green | không | 427 | 14 | 2020 / 2020 | [10.1056/nejmc2021225](https://doi.org/10.1056/nejmc2021225) |

## 3. Mục không có DOI trong `.bib` (không tra)

| Khóa | Tác giả, năm | Tiêu đề | Chương dùng |
|---|---|---|---|
| `ref_001` | DAMA International., n.d. | DAMA-DMBOK® 3.0 project | - |
| `ref_002` | Healthcare Information and Management Sy, n.d. | Adoption Model for Analytics Maturity | ch01 |
| `ref_003` | European Commission., n.d. | Horizon Europe data management plan | ch01, ch06 |
| `ref_004` | International Council for Harmonisation., 2025 | ICH E6(R3) Guideline for Good Clinical Practice | ch01, ch02 |
| `ref_005` | National Institutes of Health., 2026 | Updated elements of an NIH Data Management and Sharing Plan | ch01 |
| `ref_007` | National Institutes of Health., 2020 | Final NIH Policy for Data Management and Sharing | ch01 |
| `ref_008` | National Institutes of Health., 2020 | Supplemental information to the NIH Policy for Data Management and Sharing: Elements of an NIH Data | ch01 |
| `ref_009` | HL7 International., 2023 | FHIR | ch03 |
| `ref_010` | HL7 International., n.d. | FHIR to OMOP Implementation Guide | ch03 |
| `ref_011` | Sachson, C., 2025 | Our journey | ch03, ch04 |
| `ref_013` | Society for Clinical Data Management., n.d. | GCDMP — Good Clinical Data Management Practices | ch02 |
| `ref_014` | DAMA International., 2017 | DAMA-DMBOK: Data Management Body of Knowledge | ch01, ch02 |
| `ref_015` | Association of American Medical Colleges, 2015 | Data governance in academic medicine | ch01 |
| `ref_018` | The Turing Way Community., n.d. | Data stewards: Overview | - |
| `ref_019` | CASRAI., n.d. | Horizon Europe FAIR Data Management Plan | - |
| `ref_020` | ,  | Expert Advisory Group on Data Access. (2017, August) | - |
| `ref_024` | U.S. Food and Drug Administration., 2024 | Electronic systems, electronic records, and electronic signatures in clinical investigations: Questi | ch02 |
| `ref_025` | CASRAI., n.d. | Castor EDC & lightweight EDC for IITs | ch02 |
| `ref_027` | Gurley, M. J., Warner, J., Bushmanova, Y, 2021 | REDCap2OMOP: A platform for ETLing REDCap projects into the OMOP CDM | ch02, ch03 |
| `ref_034` | CDISC, & HL7 International., 2021 | FHIR to CDISC Joint Mapping Implementation Guide | ch03 |
| `ref_035` | HL7 International., 2026 | Valueset-example-characteristic-codes | - |
| `ref_038` | Hripcsak, G., Duke, J. D., Shah, N. H.,, 2015 | Observational Health Data Sciences and Informatics (OHDSI): Opportunities for observational research | ch03, ch04 |
| `ref_046` | UNESCO., 2021 | UNESCO Recommendation on Open Science | - |
| `ref_048` | U.S. National Library of Medicine., [CẦN KIỂM CHỨNG] ngày cập nhật | Clinical trial reporting requirements | - |
| `ref_051` | National Center for Complementary and In, n.d. | Preferred repositories | - |
| `ref_053` | ,  | Vivli. (2018, July 20) | - |
| `ref_054` | ,  | Regulation (EU) No 536/2014 of the European Parliament and of the Council of 16 April 2014 on clinic | - |
| `ref_055` | Bộ Y tế., 2025 | Thông tư 33/2025/TT-BYT quy định thời hạn lưu trữ hồ sơ, tài liệu ngành y tế | - |
| `ref_057` | ,  | Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the prote | - |
| `ref_058` | ,  | Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the Eu | - |
| `ref_060` | ,  | Standards for Privacy of Individually Identifiable Health Information, 45 CFR §164.514 (U.S. Departm | - |
| `ref_062` | Quốc hội., 2025 | Luật Bảo vệ dữ liệu cá nhân | - |
| `ref_063` | Chính phủ., 2025 | Nghị định 356/2025/NĐ-CP hướng dẫn Luật Bảo vệ dữ liệu cá nhân | - |
| `ref_064` | Quốc hội., 2024 | Luật Dữ liệu | - |
| `ref_065` | Bộ Y tế., 2025 | Thông tư 13/2025/TT-BYT hướng dẫn triển khai hồ sơ bệnh án điện tử | - |
| `ref_066` | Bộ Y tế., 2025 | Thông tư 50/2025/TT-BYT quy định về thử thuốc trên lâm sàng | - |
| `ref_075` | CASRAI., 2026 | Trusted research environments & Five Safes framework | - |
| `ref_079` | Bộ Chính trị., 2024 | Nghị quyết 57-NQ/TW về đột phá phát triển khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số quố | ch05 |
| `ref_080` | Bộ Chính trị., 2025 | Nghị quyết 72-NQ/TW về một số giải pháp đột phá, tăng cường bảo vệ, chăm sóc và nâng cao sức khỏe nh | ch05 |
| `ref_081` | Thủ tướng Chính phủ., 2026 | Quyết định 1308/QĐ-TTg phê duyệt Chiến lược dữ liệu quốc gia giai đoạn 2026–2030, tầm nhìn đến năm 2 | ch05 |
| `ref_082` | Bộ Y tế., 2026 | Quyết định 3218/QĐ-BYT ban hành Quy chế quản lý, vận hành, sử dụng, khai thác, chia sẻ dữ liệu và bả | ch05 |
| `ref_086` | Pharma Group, KPMG, & Oxford University, 2025 | Roadmap to the future of clinical trials in Vietnam | - |
| `ref_094` | Wagner, Z., & Blacketer, C., 2024 | Evaluating Synthea: Comprehensive analysis of a leading synthesized medical record generator | - |
| `ref_095` | Hao, Y., He, H., & Ho, J. C., 2024 | LLMSYN: Generating synthetic electronic health records without patient-level data | - |
| `ref_097` | Goldacre, B., & Morley, J., 2022 | Better, broader, safer: Using health data for research and analysis | ch06 |
| `ref_100` | Trusted Research and Real-world Utilisat, n.d. | TRUST Platform: Home | - |
| `ref_101` | Ministry of Health and Welfare, Republic, n.d. | Overview of K-CURE Service | - |
| `ref_109` | European Medicines Agency., 2010 | Reflection paper on expectations for electronic source data and data transcribed to electronic data | ch02 |
| `ref_110` | Medicines and Healthcare products Regula, 2018 | Guidance on GxP data integrity | ch02 |
| `ref_111` | European Medicines Agency., 2023 | Guideline on computerised systems and electronic data in clinical trials | ch02 |
| `ref_112` | U.S. Food and Drug Administration., 1997 | 21 CFR Part 11 — Electronic Records; Electronic Signatures | ch02 |
| `ref_113` | European Parliament and Council of the E, 2016 | Regulation (EU) 2016/679 (General Data Protection Regulation) | ch05 |
| `ref_114` | European Parliament and Council of the E, 2025 | Regulation (EU) 2025/327 on the European Health Data Space | ch05 |
| `ref_115` | United States Department of Health and H, n.d. | 45 CFR 164.514 — Other requirements relating to uses and disclosures of protected health information | ch05 |

## 4. Giới hạn

- Metadata tự động, chưa kiểm chứng nội dung; không dùng làm xác nhận trích dẫn.
- OpenAlex đánh dấu `is_retracted` dựa trên dữ liệu bên thứ ba; cần đối chiếu nguồn khi cờ bật.
- Số trích dẫn thay đổi theo thời gian; không đưa vào thân sách (thuộc lớp cập nhật).
