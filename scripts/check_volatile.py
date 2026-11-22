"""Check volatile chapter terms, Mermaid labels, and appendix review dates.

Usage:
    python scripts/check_volatile.py --check

With ``--check``, exit status 1 means that a violation was found. Mermaid
blocks in chapters ch01--ch06 are checked for HTML other than ``<br/>`` and
for volatile terms listed in ``scripts/volatile_terms.txt``. The built-in
self-test proves that a deliberately bad sample is detected.
"""
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TERMS = ROOT / "scripts" / "volatile_terms.txt"
APPENDICES = ROOT / "docs" / "appendices"


def load_terms() -> list[str]:
    return [x.strip() for x in TERMS.read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")]


def scan_mermaid(text: str, terms: list[str], path: Path) -> list[str]:
    violations: list[str] = []
    blocks = re.findall(r"```mermaid\s*\n(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)
    allowed_years = ("Sweeney 2002", "Machanavajjhala 2007", "Dwork 2008")
    allowed_stable_terms = {"ALCOA++", "CDISC SDTM", "k-anonymity", "l-diversity", "Five Safes"}
    for number, block in enumerate(blocks, 1):
        html_hits = re.findall(r"<(?!br\s*/?>)[^>]+>", block, flags=re.IGNORECASE)
        if html_hits:
            violations.append(f"{path.relative_to(ROOT)} Mermaid block {number}: HTML tag(s) other than <br/>: {', '.join(sorted(set(html_hits)))}")
        stable_block = block
        for allowed in allowed_years:
            stable_block = stable_block.replace(allowed, "")
        hits = [term for term in terms if term not in allowed_stable_terms and re.search(term, stable_block, re.IGNORECASE)]
        if hits:
            violations.append(f"{path.relative_to(ROOT)} Mermaid block {number}: {', '.join(hits)}")
    return violations


def self_test(terms: list[str]) -> bool:
    sample = 'flowchart TD\n  A["<b>Luật 91/2025</b>"]'
    return bool(scan_mermaid(f"```mermaid\n{sample}\n```", terms, ROOT / "docs" / "chapters" / "ch01_test.md"))


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    today = dt.date(2026, 11, 21)
    violations: list[str] = []
    terms = load_terms()
    if not self_test(terms):
        print("SELF-TEST: FAILED (sample violation was not detected)")
        return 2
    print("SELF-TEST: passed (sample Mermaid violation detected)")
    chapter_paths = sorted((ROOT / "docs" / "chapters").glob("ch0[0-7]_*.md"))
    for path in chapter_paths:
        text = path.read_text(encoding="utf-8")
        if path.name.startswith(("ch01_", "ch02_", "ch03_", "ch04_", "ch05_", "ch06_")):
            violations.extend(scan_mermaid(text, terms, path))
        paragraphs = re.split(r"\n\s*\n", text)
        paragraphs = [p for p in paragraphs if "\n## " in p or p.lstrip().startswith("## ")]
        for number, paragraph in enumerate(paragraphs, 1):
            hits = [term for term in terms if re.search(term, paragraph, re.IGNORECASE)]
            if hits and not re.search(r"appendices/", paragraph, re.IGNORECASE):
                violations.append(f"{path.relative_to(ROOT)} paragraph {number}: {', '.join(hits)}")
    appendix_paths = []
    for path in sorted(APPENDICES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not re.match(r"^---\s*(?:\r?\n|$)", text):
            continue
        appendix_paths.append(path)
        match = re.search(r"^next_review:\s*(\d{4}-\d{2}-\d{2})\s*$", text, re.MULTILINE)
        if not match:
            violations.append(f"{path.relative_to(ROOT)}: missing next_review")
        elif dt.date.fromisoformat(match.group(1)) < today:
            violations.append(f"{path.relative_to(ROOT)}: next_review {match.group(1)} is overdue")
    for item in violations:
        print(f"VOLATILE: {item}")
    print(f"Checked {len(chapter_paths)} chapters and {len(appendix_paths)} front-matter appendices; {len(violations)} violation(s).")
    return 1 if args.check and violations else 0


if __name__ == "__main__":
    sys.exit(main())
