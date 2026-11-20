# Review: `andrej-karpathy-skills` và đề xuất áp dụng cho Biomedical RDM

**Ngày review:** 20/11/2026  
**Repo được review:** <https://github.com/forrestchang/andrej-karpathy-skills>  
**Repo duy trì hiện tại:** <https://github.com/multica-ai/andrej-karpathy-skills>  
**Phạm vi áp dụng đề xuất:** `biomedical-rdm` và `biomedical-rdm-course`

## 1. Kết luận

Repo đáng tham khảo và có thể áp dụng cho dự án Biomedical RDM, nhưng nên tích hợp có chọn lọc. Không nên sao chép nguyên `CLAUDE.md` hoặc phụ thuộc hoàn toàn vào plugin.

Khuyến nghị:

1. Giữ kế hoạch triển khai RDM và tài liệu quản trị của từng repo làm nguồn yêu cầu chính.
2. Dùng bốn nguyên tắc của `andrej-karpathy-skills` như lớp hướng dẫn hành vi.
3. Tạo hướng dẫn ngắn, riêng cho dự án trong `CLAUDE.md` và `AGENTS.md`.
4. Không để hướng dẫn chung ghi đè quy tắc kiểm chứng nguồn, an toàn dữ liệu, branch, PR và phê duyệt merge.
5. Kiểm tra context sau khi cài plugin; nếu skill không được tải, dùng file hướng dẫn trực tiếp trong repo.

**Đánh giá tổng thể:** 8/10 — nên dùng sau khi điều chỉnh theo dự án.

## 2. Bốn nguyên tắc cốt lõi

| Nguyên tắc | Ý nghĩa | Áp dụng trong Biomedical RDM |
|---|---|---|
| Think Before Coding | Nêu giả định, mâu thuẫn và điểm chưa rõ trước khi sửa | Không tự suy diễn tài liệu thiếu, trạng thái pháp lý hoặc phiên bản tiêu chuẩn |
| Simplicity First | Chọn giải pháp nhỏ nhất đáp ứng mục tiêu | Tránh tạo thêm module, tài liệu đặc tả hoặc automation ngoài phạm vi |
| Surgical Changes | Chỉ sửa nội dung liên quan trực tiếp tới nhiệm vụ | Không chỉnh lại literature review hoặc quiz ngoài yêu cầu hiện tại |
| Goal-Driven Execution | Xác định tiêu chí thành công và kiểm chứng | Kiểm đếm quiz, render Quarto, kiểm tra link, đối chiếu nguồn và quét secret |

## 3. Điểm mạnh

- Nội dung ngắn, dễ hiểu và tập trung vào các lỗi phổ biến của coding agent.
- Khuyến khích công khai giả định và mâu thuẫn thay vì âm thầm lựa chọn.
- Hạn chế overengineering và các thay đổi ngoài phạm vi.
- Chuyển yêu cầu chung thành tiêu chí có thể kiểm tra.
- Manifest plugin nhỏ và dùng giấy phép MIT.
- Bản audit bên thứ ba công bố không phát hiện script, hook, MCP, package thực thi hoặc vấn đề bảo mật.

Báo cáo audit tham khảo:

- <https://github.com/xiaolai/nlpm/issues/258>

Báo cáo này chỉ là bằng chứng hỗ trợ tại thời điểm audit, không thay thế việc kiểm tra phiên bản cụ thể trước khi cài đặt.

## 4. Hạn chế và rủi ro

### 4.1. Không phải workflow hoàn chỉnh

Bộ nguyên tắc không thay thế:

- kiểm chứng tài liệu tham khảo;
- phân loại `VERIFIED`, `BIB_PENDING`, `CONTENT_PENDING`;
- kiểm tra Quarto;
- kiểm tra link;
- kiểm tra dữ liệu bệnh nhân và secret;
- quản lý branch, pull request và phê duyệt merge;
- tiêu chí nghiệm thu riêng của khóa học.

### 4.2. Có thể khiến agent hỏi quá nhiều

Quy tắc “ask rather than guess” cần giới hạn cho các quyết định có ảnh hưởng đáng kể. Các lựa chọn nhỏ, có thể đảo ngược nên được xử lý bằng giả định được ghi rõ.

Quy tắc đề xuất:

> Nếu điểm chưa rõ có thể làm thay đổi phạm vi, nội dung khoa học, dữ liệu, kiến trúc hoặc kết quả nghiệm thu thì phải hỏi. Các lựa chọn nhỏ và có thể đảo ngược được xử lý bằng giả định có ghi rõ.

### 4.3. Không phải thay đổi nào cũng cần test-first

Đối với Markdown, chỉnh chính tả hoặc thay đổi cấu hình nhỏ, viết test trước có thể không cần thiết.

Quy tắc đề xuất:

> Xác định cách kiểm chứng trước khi thực hiện; dùng test tự động khi có giá trị thực tế.

Các cách kiểm chứng phù hợp với dự án:

- so sánh nội dung với file nguồn;
- kiểm đếm module và câu quiz;
- chạy `quarto render`;
- kiểm tra link nội bộ và link ngoài;
- kiểm tra YAML;
- quét secret và dữ liệu định danh;
- review diff.

### 4.4. Plugin bên thứ ba có thể không được tải vào context

Đã có báo cáo về trường hợp skill từ marketplace bên thứ ba được cài nhưng không xuất hiện trong context của Claude Code:

- <https://github.com/anthropics/claude-code/issues/27049>

Do đó, sau khi cài phải kiểm tra `/context`. Nếu skill không xuất hiện, dùng `CLAUDE.md` trong repo thay vì giả định plugin đang hoạt động.

### 4.5. Đường dẫn repo đã thay đổi

URL `forrestchang/andrej-karpathy-skills` hiện liên quan đến repo được duy trì dưới tổ chức `multica-ai`. Khi cài đặt hoặc sao chép file, cần xác nhận URL và commit cụ thể để tránh dùng tài liệu cũ.

## 5. Phương án áp dụng cho Biomedical RDM

### 5.1. Nguồn chỉ đạo theo thứ tự ưu tiên

1. Yêu cầu trực tiếp đã được phê duyệt cho nhiệm vụ hiện tại.
2. Tài liệu kế hoạch, quyết định và tiêu chí nghiệm thu của repo.
3. Quy định khoa học, pháp lý, an toàn dữ liệu và quản lý nguồn.
4. Hướng dẫn dự án trong `AGENTS.md` hoặc `CLAUDE.md`.
5. Nguyên tắc chung từ `andrej-karpathy-skills`.

Nếu có mâu thuẫn, nguồn có mức ưu tiên cao hơn được áp dụng và mâu thuẫn phải được ghi trong `docs/DECISIONS.md`.

### 5.2. Phân chia theo công cụ

| Công cụ | File đề xuất | Vai trò |
|---|---|---|
| Codex | `AGENTS.md` | Hướng dẫn triển khai, kiểm tra và thao tác repo |
| Claude Code | `CLAUDE.md` | Hướng dẫn review và triển khai bằng Claude |
| GitHub Copilot | `.github/copilot-instructions.md` | Chỉ bổ sung nếu dự án thực sự sử dụng Copilot |

Không cần duy trì ba bản nội dung dài. Nên có một phần nguyên tắc chung ngắn và các quy tắc riêng theo công cụ.

## 6. Nội dung rút gọn đề xuất

Nội dung sau có thể dùng làm phần chung trong `AGENTS.md` và `CLAUDE.md`:

```markdown
## Working principles

1. State assumptions that materially affect scope, scientific claims,
   repository structure, legal interpretation, or data handling.

2. Prefer the smallest implementation that satisfies the approved plan.
   Do not add modules, abstractions, automation, or content outside scope.

3. Keep changes surgical. Every changed file must trace to the current task.
   Record unrelated findings instead of fixing them silently.

4. Define verification before implementation. Use the appropriate evidence:
   source comparison, quiz counts, Quarto render, link checks, secret scanning,
   or tests.

5. Do not invent missing references, legal claims, version information, or
   research evidence. Do not remove verification warnings without evidence.
   Mark missing required inputs as BLOCKED_INPUT.

6. Treat privacy, ethics, security, and legal compliance as controls across
   the full research-data lifecycle.

7. Work on a branch, open a draft pull request, and do not merge without
   approval.

8. For reversible low-impact choices, proceed with a documented assumption.
   Ask before decisions that materially change scope, scientific meaning,
   data handling, architecture, or acceptance criteria.
```

## 7. Tiêu chí xác nhận hướng dẫn đang có tác dụng

- Diff chỉ chứa thay đổi liên quan đến nhiệm vụ.
- Agent nêu rõ các input còn thiếu và không tự dựng nguồn.
- Ít phát sinh cấu trúc hoặc tài liệu ngoài kế hoạch.
- Mỗi thay đổi có phương pháp kiểm chứng phù hợp.
- Không xóa cờ chưa kiểm chứng mà không có bằng chứng.
- Không có dữ liệu bệnh nhân, thông tin định danh hoặc secret trong repo.
- Pull request mô tả rõ phạm vi, kiểm thử, blocker và việc còn lại.
- Agent không tự merge trước khi được duyệt.

## 8. Quyết định đề xuất

**ADOPT WITH MODIFICATIONS**

Áp dụng các nguyên tắc hành vi, nhưng không cài plugin như một phụ thuộc bắt buộc của project. Trước mắt nên thêm hướng dẫn rút gọn vào `AGENTS.md` và `CLAUDE.md` trên branch riêng, review diff và kiểm tra bằng một nhiệm vụ thực tế trước khi đưa vào `main`.

## 9. Nguồn tham khảo

- Repo gốc: <https://github.com/forrestchang/andrej-karpathy-skills>
- Repo duy trì hiện tại: <https://github.com/multica-ai/andrej-karpathy-skills>
- Claude Code plugin discovery issue: <https://github.com/anthropics/claude-code/issues/27049>
- Audit tham khảo: <https://github.com/xiaolai/nlpm/issues/258>
