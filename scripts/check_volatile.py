"""Check volatile chapter terms and appendix review dates."""
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


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    today = dt.date(2026, 11, 21)
    violations: list[str] = []
    terms = load_terms()
    chapter_paths = sorted((ROOT / "docs" / "chapters").glob("ch0[0-7]_*.md"))
    for path in chapter_paths:
        paragraphs = re.split(r"\n\s*\n", path.read_text(encoding="utf-8"))
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
