#!/usr/bin/env python3
"""Build the two BibTeX archives and audit the 103-to-334 mapping.

Only standard-library modules are used.  The input deliberately contains
incomplete bibliographic data; this script preserves that incompleteness.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "references" / "source-334-list.md"
INDEX = ROOT / "docs" / "literature-review" / "index.md"
AUDIT = ROOT / "references" / "citation-audit.csv"
OUT334 = ROOT / "references" / "references-334.bib"
OUT103 = ROOT / "references" / "references.bib"

EXTENSIONS = [
    (104, "article", {
        "title": "Gene name errors are widespread in the scientific literature",
        "author": "Ziemann, M., Eren, Y., & El-Osta, A.",
        "year": "2016", "journal": "Genome Biology", "volume": "17", "pages": "177",
        "doi": "10.1186/s13059-016-1044-7",
    }),
    (105, "article", {
        "title": "Drug development: Raise standards for preclinical cancer research",
        "author": "Begley, C. G., & Ellis, L. M.", "year": "2012", "journal": "Nature",
        "volume": "483", "pages": "531–533", "doi": "10.1038/483531a",
    }),
    (106, "article", {
        "title": "The economics of reproducibility in preclinical research",
        "author": "Freedman, L. P., Cockburn, I. M., & Simcoe, T. S.", "year": "2015",
        "journal": "PLoS Biology", "volume": "13", "number": "6", "pages": "e1002165",
        "doi": "10.1371/journal.pbio.1002165",
    }),
    (107, "article", {
        "title": "Retraction—Hydroxychloroquine or chloroquine with or without a macrolide for treatment of COVID-19: a multinational registry analysis",
        "author": "Mehra, M. R., Ruschitzka, F., & Patel, A. N.", "year": "2020",
        "journal": "The Lancet", "volume": "395", "pages": "1820",
        "doi": "10.1016/S0140-6736(20)31324-6",
    }),
    (108, "article", {
        "title": "Retraction: Cardiovascular disease, drug therapy, and mortality in Covid-19",
        "author": "Mehra, M. R., Desai, S. S., Kuy, S., Henry, T. D., & Patel, A. N.",
        "year": "2020", "journal": "New England Journal of Medicine", "volume": "382",
        "pages": "e102", "doi": "10.1056/NEJMc2021225",
    }),
]

EXCLUSIONS = {
    1: "draft input file, not a citation source",
    2: "draft input file, not a citation source",
    4: "secondary IntuitionLabs explainer; primary ICH source is #3",
    5: "secondary IntuitionLabs explainer; primary ICH source is #3",
    10: "duplicate Bridge2AI preprint; consolidated into #9",
    20: "duplicate Hripcsak copy; consolidated into #19",
    55: "duplicate Law 91/2025/QH15; consolidated into #16",
    56: "duplicate Circular 50/2025/TT-BYT; consolidated into #18",
    99: "duplicate ResearchGate copy; consolidated into the canonical source",
    150: "duplicate Baker (2016); consolidated into #149",
    160: "secondary IntuitionLabs explainer; primary CDISC source retained",
    168: "duplicate ResearchGate copy; consolidated into the canonical source",
    186: "popular/news article about LEGEND-HTN; not a scholarly source",
    187: "popular/news article about LEGEND-HTN; not a scholarly source",
    192: "secondary FAIR toolkit copy; canonical FAIR source retained",
    196: "not cited in the synthesis; unresolved specialized FAIRification case",
    221: "secondary IntuitionLabs clinical-trial checklist",
    225: "consultation/response table attachment; not a scholarly source",
    226: "draft legal-appendix attachment; not a scholarly source",
    233: "not cited; EHDS argument uses primary Regulation (EU) 2025/327",
    241: "not cited; unresolved duplicate-author K-anonymity item",
    305: "duplicate ResearchGate copy; consolidated into the canonical source",
    311: "duplicate Studocu copy; consolidated into the canonical source",
    312: "secondary CASRAI Swarm Learning guide; primary paper retained",
    317: "unreviewed Research Square preprint; not cited",
    324: "duplicate ResearchGate copy; consolidated into the canonical source",
}


def latex(value: str) -> str:
    """Escape BibTeX text while retaining UTF-8 characters."""
    value = value.replace("\\", r"\textbackslash{}")
    for char, escaped in [("&", r"\&"), ("%", r"\%"), ("_", r"\_"), ("#", r"\#")]:
        value = value.replace(char, escaped)
    return value.replace("{", r"\{").replace("}", r"\}")


def extract_url(text: str) -> str | None:
    match = re.search(r"https?://[^\s<>]+", text)
    if not match:
        return None
    return match.group(0).rstrip(".,;)")


def ids_from_url(url: str | None) -> dict[str, str]:
    if not url:
        return {}
    result: dict[str, str] = {}
    pmid = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", url, re.I)
    if pmid:
        result["pmid"] = pmid.group(1)
    pmcid = re.search(r"/articles/(PMC\d+)", url, re.I)
    if pmcid:
        result["pmcid"] = pmcid.group(1).upper()
    doi = re.search(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", url, re.I)
    if doi:
        result["doi"] = doi.group(0).rstrip(".,;)").lower()
    return result


def source_entries() -> list[dict]:
    entries = []
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^(\d+)\.\s+(.*)$", line)
        if not match:
            continue
        number, rest = int(match.group(1)), match.group(2).strip()
        url_match = re.search(r"(?:,\s*)?<([^>]+)>\s*$", rest)
        if url_match:
            url = url_match.group(1)
            title = rest[: url_match.start()].rstrip(" ,")
            if not title:
                title = url
        elif rest.startswith("http://") or rest.startswith("https://"):
            url, title = rest, rest
        else:
            url, title = None, rest
        entries.append({"number": number, "title": title, "url": url, **ids_from_url(url)})
    if [e["number"] for e in entries] != list(range(1, 335)):
        raise ValueError("source-334-list.md does not contain exactly numbered entries 1..334")
    return entries


def split_pending(raw: str) -> tuple[str, str | None]:
    notes = []
    for match in re.findall(r"\*\*\[([^\]]*CẦN KIỂM CHỨNG[^\]]*)\]\*\*", raw):
        notes.append(match)
    raw = re.sub(r"\s*—\s*\*\*\[[^\]]*CẦN KIỂM CHỨNG[^\]]*\]\*\*", "", raw)
    if "n.d." in raw:
        notes.append("năm là n.d.")
    return raw.strip(), ("; ".join(notes) if notes else None)


def parse_reference(line: str) -> dict:
    match = re.match(
        r"^(\d+)\.\s+(.*?)\s+\(((?:\d{4}|n\.d\.|[^()]*(?:CẦN KIỂM CHỨNG)[^()]*))\)\.\s+(.*)$",
        line,
    )
    if match:
        number = int(match.group(1))
        authors, year, rest = match.group(2), match.group(3), match.group(4)
    else:
        # Some legal instruments in the supplied list have no author/year
        # parenthetical.  Preserve the omission rather than inventing one.
        bare = re.match(r"^(\d+)\.\s+(.*)$", line)
        if not bare:
            raise ValueError(f"Cannot parse APA line: {line}")
        number, authors, year, rest = int(bare.group(1)), "", "", bare.group(2)
    rest, pending = split_pending(rest)
    url = extract_url(rest)
    if url:
        rest = rest[: rest.find(url)].rstrip(" .")
    rest = re.sub(r"\s*\(Truy cập[^)]*\)$", "", rest).strip()

    italics = list(re.finditer(r"\*([^*]+)\*", rest))
    title = ""
    journal = ""
    booktitle = ""
    publisher = ""
    if italics:
        first = italics[0]
        prefix = rest[: first.start()].strip()
        if prefix:
            if " In " in prefix:
                title = prefix.split(" In ", 1)[0].strip(" .")
            else:
                title = prefix.strip(" .")
            journal = first.group(1).strip()
        else:
            title = first.group(1).strip()
        remainder = rest[italics[0].end():].strip(" .")
        in_match = re.search(r"\bIn\s+(?:[^*]*\s+)?\*([^*]+)\*", remainder)
        if in_match:
            booktitle = in_match.group(1).strip()
        if " In " in prefix:
            journal = ""
            booktitle = first.group(1).strip()
        publisher_match = re.search(r"\)\.\s*([^.;]+)(?:\.|$)", remainder)
        if publisher_match:
            publisher = publisher_match.group(1).strip()
    else:
        title = rest.strip(" .")

    # If a title is followed by a journal in italics, parse volume/issue/pages.
    numeric = ""
    if journal:
        after = rest[italics[0].end():]
        numeric = after
    volume_match = re.search(r"(?:Vol\.\s*)?(\d+)\s*\(([^)]+)\)", numeric)
    if not volume_match:
        volume_match = re.search(r"(?:Vol\.\s*)?(\d+)", numeric)
    pages_match = re.search(r"(?:pp?\.\s*|,\s*)([eA-Za-z0-9]+(?:[–-][eA-Za-z0-9]+)?)", numeric)

    typ = "article" if journal else "misc"
    low = (title + " " + rest).lower()
    if " in *" in low or "proceedings" in low or "conference" in low:
        typ = "inproceedings"
    if publisher and not journal:
        typ = "book"
    if any(word in low for word in ["regulation (eu)", "luật ", "nghị định", "thông tư", "quyết định", "45 cfr"]):
        typ = "misc"
    fields = {"title": title}
    if authors:
        fields["author"] = authors
    if year:
        fields["year"] = year
    if journal:
        fields["journal"] = journal
    if booktitle:
        fields["booktitle"] = booktitle
    if publisher:
        fields["publisher"] = publisher
    if volume_match and journal:
        fields["volume"] = volume_match.group(1)
        if volume_match.lastindex and volume_match.lastindex >= 2:
            fields["number"] = volume_match.group(2)
    if pages_match and journal:
        fields["pages"] = pages_match.group(1)
    ids = ids_from_url(url)
    if "doi" in ids:
        fields["doi"] = ids["doi"]
    elif url:
        fields["url"] = url
    if pending:
        pending = re.sub(r"^CẦN KIỂM CHỨNG:\s*", "", pending)
        fields["note"] = "CẦN KIỂM CHỨNG: " + pending
    return {"number": number, "type": typ, "fields": fields, "pending": bool(pending), "url": url, **ids}


def reference_entries() -> list[dict]:
    lines = INDEX.read_text(encoding="utf-8").splitlines()
    start = next(i for i, line in enumerate(lines) if line.strip() == "## Tài liệu tham khảo")
    entries = [parse_reference(line) for line in lines[start + 1:] if re.match(r"^\d+\.\s+", line)]
    if [e["number"] for e in entries] != list(range(1, 104)):
        raise ValueError(f"expected 103 APA entries, got {len(entries)}")
    return entries


def bib_entry(key: str, typ: str, fields: dict[str, str], pending: bool = False) -> str:
    lines = [(f"@{typ}{{{key},")]
    for name, value in fields.items():
        lines.append(f"  {name} = {{{latex(value)}}},")
    lines[-1] = lines[-1].rstrip(",")
    lines.append("}")
    return ("% PENDING\n" if pending else "") + "\n".join(lines)


def write_334(entries: list[dict]) -> None:
    blocks = []
    for e in entries:
        note = f'source list #{e["number"]}; authors/year/venue absent in source list'
        if e["number"] in EXCLUSIONS:
            note += "; EXCLUDED: " + EXCLUSIONS[e["number"]]
        fields = {"title": e["title"]}
        for name in ("url", "pmid", "pmcid", "doi"):
            if e.get(name):
                fields[name] = e[name]
        fields["note"] = note
        blocks.append(bib_entry(f"src334_{e['number']:03d}", "misc", fields))
    OUT334.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")


def write_103(entries: list[dict]) -> None:
    blocks = []
    for e in entries:
        blocks.append(bib_entry(f"ref_{e['number']:03d}", e["type"], e["fields"], e["pending"]))
    for number, typ, fields in EXTENSIONS:
        blocks.append(bib_entry(f"ref_{number:03d}", typ, fields))
    OUT103.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def map_sources(refs: list[dict], sources: list[dict]) -> dict[int, int]:
    mapped = {}
    for ref in refs:
        candidates = []
        for src in sources:
            shared = any(ref.get(k) and src.get(k) and ref[k].lower() == src[k].lower() for k in ("doi", "pmid", "pmcid"))
            same_url = ref.get("url") and src.get("url") and ref["url"].rstrip("/").lower() == src["url"].rstrip("/").lower()
            title = ref["fields"].get("title", "")
            same_title = norm(title) and norm(title) == norm(src["title"])
            if shared or same_url or same_title:
                candidates.append(src["number"])
        if len(candidates) == 1:
            mapped[ref["number"]] = candidates[0]
    return mapped


def update_audit(mapping: dict[int, int]) -> None:
    with AUDIT.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
        fieldnames = list(rows[0]) if rows else ["source_number", "citation_key", "status", "missing_field", "used_in", "action"]
    rows = [row for row in rows if int(row["source_number"]) < 104]
    if "source334_number" not in fieldnames:
        fieldnames.append("source334_number")
    for row in rows:
        n = int(row["source_number"])
        row["citation_key"] = f"ref_{n:03d}"
        row["source334_number"] = str(mapping.get(n, ""))
    existing = {int(row["source_number"]) for row in rows}
    for number, _typ, _fields in EXTENSIONS:
        if number not in existing:
            rows.append({
                "source_number": str(number), "citation_key": f"ref_{number:03d}",
                "status": "VERIFIED_UNAUDITED", "missing_field": "",
                "used_in": "chapter_only", "action": "Metadata checked against Crossref; content audit remains open.",
                "source334_number": "", "page_check": "", "page_check_note": "",
            })
    with AUDIT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def replace_blocked_flag() -> None:
    text = INDEX.read_text(encoding="utf-8")
    flag = "[CẦN KIỂM CHỨNG: số 134 của danh mục 334 mục — BLOCKED_INPUT]"
    updated = text.replace(flag, "[28]")
    if updated == text and "[28]" not in text:
        raise ValueError("the blocked #134 flag was not found")
    INDEX.write_text(updated, encoding="utf-8")


def check_bib(path: Path, expected: int) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    structural = re.sub(r"\\[{}]", "", text)
    if structural.count("{") != structural.count("}"):
        raise ValueError(f"unbalanced braces in {path}")
    entries = re.findall(r"@\w+\{([^,]+),", text)
    if len(entries) != expected or len(set(entries)) != expected:
        raise ValueError(f"entry count/key uniqueness failed for {path}: {len(entries)}")
    for block in re.split(r"(?m)^@", text)[1:]:
        body = block[block.find("\n") :]
        body_structural = re.sub(r"\\[{}]", "", body)
        # The entry-opening brace is in the part before the first newline.
        # Include a virtual opening brace when checking the field body.
        body_structural = "{" + body_structural
        if body_structural.count("{") != body_structural.count("}"):
            raise ValueError(f"unbalanced entry in {path}")
        for line in body.splitlines():
            if line.strip() and not line.strip().startswith("%") and not line.strip().startswith("}") and "=" in line and not line.rstrip().endswith(","):
                # The last field is allowed to omit a comma only immediately before }.
                if not re.search(r"\}\s*$", line):
                    raise ValueError(f"missing comma in {path}: {line}")
    return len(entries), text.count("% PENDING")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check existing generated files only")
    args = parser.parse_args()
    if not args.check:
        sources = source_entries()
        refs = reference_entries()
        write_334(sources)
        write_103(refs)
        update_audit(map_sources(refs, sources))
        replace_blocked_flag()
    n334, _ = check_bib(OUT334, 334)
    # The canonical bibliography currently contains 103 core entries plus
    # chapter-only entries 104–112 added by approved chapter revisions.
    n103, pending = check_bib(OUT103, 112)
    sources = source_entries()
    counts = {k: sum(1 for e in sources if k in e) for k in ("pmid", "pmcid", "doi")}
    print(f"references-334.bib: {n334} entries; pmid={counts['pmid']} pmcid={counts['pmcid']} doi={counts['doi']}")
    print(f"references.bib: {n103} entries (103 core + {n103 - 103} chapter-only); pending={pending}")
    print(f"citation-audit.csv: source334_number mapping updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
