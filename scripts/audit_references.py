#!/usr/bin/env python3
"""Audit numbered citations, BibTeX and citation-audit.csv for Biomedical RDM."""

from __future__ import annotations

import csv
import re
import sys
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "literature-review" / "index.md"
BIB = ROOT / "references" / "references.bib"
CSV = ROOT / "references" / "citation-audit.csv"
REPORT = ROOT / "references" / "AUDIT-REPORT.md"
EXPECTED = set(range(1, 104))
NUMBER_RE = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
ENTRY_RE = re.compile(r"^@[^\{]+\{(ref_(\d{3})),", re.MULTILINE)
FIELD_RE = re.compile(r"^\s*(doi|url|title)\s*=\s*\{(.*?)\}\s*,?\s*$", re.IGNORECASE | re.MULTILINE)
MOJIBAKE = ("Ã", "Â", "â€", "ï¿½", "�", ".tnum")


def md_lines(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items) if items else "- Không phát hiện."


def citation_numbers() -> tuple[list[int], list[str]]:
    text = INDEX.read_text(encoding="utf-8")
    if "## Phụ lục B." in text:
        text = text.split("## Phụ lục B.", 1)[0]
    if "## Tài liệu tham khảo" in text:
        text = text.split("## Tài liệu tham khảo", 1)[0]
    malformed: list[str] = []
    numbers: list[int] = []
    for match in NUMBER_RE.finditer(text):
        values = [int(x.strip()) for x in match.group(1).split(",")]
        numbers.extend(values)
        if any(value not in EXPECTED for value in values):
            malformed.append(match.group(0))
    return numbers, malformed


def bib_entries() -> tuple[set[int], dict[str, list[str]], list[str]]:
    text = BIB.read_text(encoding="utf-8")
    entries = {int(number) for _, number in ENTRY_RE.findall(text)}
    fields: dict[str, list[str]] = defaultdict(list)
    for block in re.split(r"(?=^@)", text, flags=re.MULTILINE):
        key_match = re.search(r"^@[^\{]+\{(ref_\d{3}),", block)
        if not key_match:
            continue
        key = key_match.group(1)
        for field, value in FIELD_RE.findall(block):
            normalized = re.sub(r"\s+", " ", value).strip().lower()
            if normalized:
                fields[f"{field.lower()}::{normalized}"].append(key)
    strange: list[str] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if any(marker in line for marker in MOJIBAKE):
            strange.append(f"dòng {line_no}: dấu hiệu mojibake/ký tự thay thế")
        if any(unicodedata.category(ch) in {"Cc", "Cf"} and ch not in "\t\r\n" for ch in line):
            strange.append(f"dòng {line_no}: ký tự điều khiển/định dạng ẩn")
    return entries, fields, strange


def csv_entries() -> tuple[set[int], list[str]]:
    with CSV.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    numbers: set[int] = set()
    malformed: list[str] = []
    for row in rows:
        raw = (row.get("source_number") or "").strip()
        try:
            numbers.add(int(raw))
        except ValueError:
            malformed.append(raw or "<trống>")
    return numbers, malformed


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    cited, out_of_range = citation_numbers()
    cited_set = set(cited)
    bib, fields, strange = bib_entries()
    audit, audit_malformed = csv_entries()

    missing_bib = sorted(EXPECTED - bib)
    missing_csv = sorted(EXPECTED - audit)
    missing_cited_bib = sorted(cited_set - bib)
    missing_cited_csv = sorted(cited_set - audit)
    uncited = sorted(EXPECTED - cited_set)
    duplicates: list[str] = []
    for field, keys in sorted(fields.items()):
        if len(set(keys)) > 1:
            kind, value = field.split("::", 1)
            duplicates.append(f"{kind}: `{value}` → {', '.join(sorted(set(keys)))}")

    required_errors = []
    if missing_cited_bib or missing_cited_csv:
        required_errors.append("(a) có trích dẫn trong thân bài không có mục tương ứng")
    if missing_bib or missing_csv:
        required_errors.append("(b) thiếu mục 1..103 trong references.bib hoặc citation-audit.csv")
    if out_of_range:
        required_errors.append("(f) có số trích dẫn ngoài khoảng 1..103")

    report = f"""# Báo cáo audit tham khảo

**Ngày chạy:** {date.today().isoformat()}  
**Phạm vi:** `docs/literature-review/index.md` sau khi loại danh mục tham khảo và Phụ lục B; đối chiếu 1..103.

## Kết quả tổng quát

- Số lần xuất hiện trích dẫn đã quét: **{len(cited)}**
- Số trích dẫn khác nhau: **{len(cited_set)}**
- Mã thoát dự kiến: **{"1 — có lỗi bắt buộc" if required_errors else "0 — không có lỗi bắt buộc"}**

## (a) Trích dẫn thân bài không có mục tương ứng

{md_lines([f'BibTeX thiếu: {missing_cited_bib}' if missing_cited_bib else 'BibTeX: không thiếu.', f'CSV thiếu: {missing_cited_csv}' if missing_cited_csv else 'CSV: không thiếu.'])}

## (b) Mục 1..103 trong nguồn đối chiếu

{md_lines([f'BibTeX thiếu: {missing_bib}' if missing_bib else 'BibTeX đủ 1..103.', f'CSV thiếu: {missing_csv}' if missing_csv else 'CSV đủ 1..103.', f'Dòng CSV không đọc được: {audit_malformed}' if audit_malformed else 'Không có dòng CSV lỗi.'])}

## (c) Mục không được trích trong thân bài

{md_lines([', '.join(map(str, uncited))] if uncited else [])}

## (d) Trùng DOI/URL/tiêu đề

{md_lines(duplicates)}

## (e) Mojibake/ký tự lạ trong `.bib`

{md_lines(strange)}

## (f) Số trích dẫn ngoài khoảng

{md_lines(out_of_range)}

## Ghi chú

Đây là báo cáo cấu trúc, không xác nhận nội dung khoa học, tính đúng của DOI/URL hay hiệu lực pháp lý. Không tự sửa thân bài, BibTeX hoặc CSV.
"""
    REPORT.write_text(report, encoding="utf-8", newline="\n")
    print(report)
    return 1 if required_errors else 0


if __name__ == "__main__":
    sys.exit(main())
