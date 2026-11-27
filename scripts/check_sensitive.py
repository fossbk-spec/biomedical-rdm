#!/usr/bin/env python3
"""Scan tracked files for AI-tool names and secret-like strings that must not appear in this public repository.

Rules (project policy): no credit to AI tools in repository files, and no keys or credentials.
Legitimate matches (an organisation name inside a bibliographic title, a script that calls a named API)
are listed per file in editorial/sensitive-allowlist.txt as `path-glob<TAB>regex`; a hit is allowed only
when its line matches the regex of an entry whose glob matches the file path.
Standard library only. Exit 1 on any unallowed hit.
"""
from __future__ import annotations
import argparse, fnmatch, re, subprocess, sys, tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
ALLOW = ROOT / "editorial" / "sensitive-allowlist.txt"
SKIP_PREFIXES = ("archive/", "references/")  # frozen copies and bibliographic data
SKIP_FILES = {"scripts/check_sensitive.py", "editorial/sensitive-allowlist.txt"}
NAMES = re.compile(r"\b(claude|codex|gemini|chatgpt|openai|anthropic|copilot)\b", re.I)
SECRETS = [
    ("khóa Google", re.compile(r"AIza[0-9A-Za-z_\-]{35}")),
    ("khóa dạng sk-", re.compile(r"\bsk-[A-Za-z0-9]{20,}")),
    ("token GitHub", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}")),
    ("khóa AWS", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("khóa riêng", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")),
    ("gán khóa API", re.compile(r"(?i)\bapi[_-]?key\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}['\"]")),
]
TEXT_EXT = {".md", ".py", ".yml", ".yaml", ".json", ".csv", ".txt", ".bib", ".qmd", ".html", ".mts", ".js", ".vue", ".cff", ".toml", ""}


def load_allow(path: Path = ALLOW) -> list[tuple[str, re.Pattern]]:
    out = []
    if not path.exists():
        return out
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        glob, _, rx = raw.partition("\t")
        out.append((glob.strip(), re.compile(rx.strip() or ".*")))
    return out


def scan_text(rel: str, text: str, allow: list[tuple[str, re.Pattern]]) -> list[tuple[int, str, str]]:
    hits = []
    allowed = [rx for g, rx in allow if fnmatch.fnmatch(rel, g)]
    for n, line in enumerate(text.splitlines(), 1):
        found = []
        for m in NAMES.finditer(line):
            found.append(("tên công cụ AI", m.group(0)))
        for label, rx in SECRETS:
            if rx.search(line):
                found.append((label, "(đã ẩn)"))
        if found and not any(rx.search(line) for rx in allowed):
            hits.extend((n, label, val) for label, val in found)
    return hits


def tracked_files() -> list[str]:
    out = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode("utf-8")
    return [f for f in out.split("\0") if f]


def run_check() -> int:
    allow = load_allow()
    bad = 0
    for rel in tracked_files():
        if rel in SKIP_FILES or rel.startswith(SKIP_PREFIXES) or Path(rel).suffix.lower() not in TEXT_EXT:
            continue
        p = ROOT / rel
        if not p.is_file():
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for n, label, val in scan_text(rel, text, allow):
            bad += 1
            print(f"FAIL {rel}:{n}: {label}: {val}")
    print(f"Không đạt: {bad}" if bad else "Đạt: không có tên công cụ AI hay chuỗi giống khóa ngoài danh sách cho phép")
    return 1 if bad else 0


def self_test() -> None:
    allow = [("docs/x.md", re.compile("OpenAIRE"))]
    assert scan_text("docs/y.md", "Viết bởi Claude", allow), "phải bắt tên công cụ AI"
    assert not scan_text("docs/x.md", "Zenodo, OpenAIRE", allow), "dòng nằm trong danh sách cho phép"
    assert scan_text("docs/x.md", "Gemini khác", allow), "danh sách chỉ cho phép dòng khớp biểu thức"
    assert scan_text("a.py", 'api_key = "abcdefghijklmnop1234"', []), "phải bắt gán khóa API"
    assert scan_text("a.py", "AIza" + "A" * 35, []), "phải bắt khóa Google"
    assert not scan_text("a.md", "Claudel et al. 2022", []), "họ tác giả không phải tên công cụ"
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "al.txt"
        f.write_text("# ghi chú\ndocs/*.md\tOpenAIRE\n", encoding="utf-8")
        assert len(load_allow(f)) == 1
    print("Đạt: self-test bắt tên công cụ AI, chuỗi giống khóa và tôn trọng danh sách cho phép; Không đạt: 0")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        return 0
    if a.check:
        return run_check()
    print("Dùng --self-test hoặc --check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
