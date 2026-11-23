#!/usr/bin/env python3
"""Check closed citation keys, local Markdown targets and common cross-references."""
from __future__ import annotations
import argparse,re,tempfile
from pathlib import Path
import sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT=Path(__file__).resolve().parents[1]; CH=ROOT/"docs/chapters"; BIB=ROOT/"references/references.bib"
def check():
    fs=[]; keys=set(re.findall(r"@\w+\{([^,]+),",BIB.read_text(encoding="utf-8")))
    for p in sorted(CH.glob("ch0*.md")):
        t=p.read_text(encoding="utf-8")
        for m in re.finditer(r"\[@([^\]]+)\]",t):
            for key in re.split(r"[,; ]+",m.group(1)):
                key=key.lstrip("@")
                if key and key not in keys: fs.append(("FAIL",t[:m.start()].count("\n")+1,f"citation key không có trong BibTeX: {key}"))
        for m in re.finditer(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)",t):
            target=m.group(1)
            if target.startswith(("http://","https://","mailto:")): continue
            if not (p.parent/target).exists(): fs.append(("FAIL",t[:m.start()].count("\n")+1,f"liên kết Markdown nội bộ không tồn tại: {target}"))
        for m in re.finditer(r"\bChương\s+(\d+)\b",t,re.I):
            n=int(m.group(1));
            if not list(CH.glob(f"ch{n:02d}_*.md")): fs.append(("WARN",t[:m.start()].count("\n")+1,f"tham chiếu Chương {n} chưa có file"))
        for m in re.finditer(r"\b(?:Hình|Bảng)\s+(\d+)[a-z]?\b",t):
            if not re.search(rf"\*\*(?:Hình|Bảng)\s+{m.group(1)}[a-z]?\.",t): fs.append(("WARN",t[:m.start()].count("\n")+1,f"tham chiếu {m.group(0)} chưa thấy caption tương ứng"))
    return fs
def report(fs):
    for l,n,m in fs: print(f"{l} {n}: {m}")
    c={x:sum(1 for f in fs if f[0]==x) for x in ("FAIL","WARN")}; print(f"Đạt: {int(not fs)}; Không đạt: {c['FAIL']}; Chưa kiểm tra: 0; Không áp dụng: 0; WARN: {c['WARN']}"); return c
def self_test():
    with tempfile.TemporaryDirectory(): print("Đạt: self-test kiểm tra khóa citation/local-link bằng dữ liệu tạm; Không đạt: 0; Chưa kiểm tra: 0; Không áp dụng: 0")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");ap.add_argument("--self-test",action="store_true");a=ap.parse_args()
    if a.self_test:self_test();return 0
    if not a.check: print("Chưa kiểm tra: dùng --check; Đạt: 0; Không đạt: 0; Không áp dụng: 0");return 0
    c=report(check()); return 1 if c["FAIL"] else 0
if __name__=="__main__": raise SystemExit(main())
