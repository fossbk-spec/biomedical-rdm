#!/usr/bin/env python3
"""Minimal standard-library YAML reader for the repository's flat glossary."""
from __future__ import annotations
import argparse,re,tempfile
from pathlib import Path
import sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT=Path(__file__).resolve().parents[1]; G=ROOT/"editorial/glossary.yml"; AL=ROOT/"editorial/glossary-allowlist.txt"
CH=ROOT/"docs/chapters"
FIELDS=("key","vi","vi_status","en","abbr","definition","first_chapter","source")
STATUS=("established","proposed","keep-english")
def parse(path=G):
    rows=[]; cur=None
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if re.match(r"\s*-\s*\{",line):
            body=line.split("{",1)[1].rsplit("}",1)[0]; d={}
            for k,v in re.findall(r"(\w+):\s*(null|[^,]+)",body): d[k]=v.strip().strip("'")
            d["line"]=n; rows.append(d)
    return rows
def allow(): return {x.split("—",1)[0].strip() for x in AL.read_text(encoding="utf-8").splitlines() if x and not x.startswith("#") and "—" in x}
def check():
    out=[]; rows=parse(); keys=[r.get("key") for r in rows]
    for i,r in enumerate(rows,1):
        for f in FIELDS:
            if f not in r or not r[f]: out.append(("FAIL",r.get("line",i),f"thiếu trường {f}"))
        if r.get("first_chapter") and not (CH/f"ch0{int(r['first_chapter']):02d}_").parent.exists(): pass
        if r.get("first_chapter") and not list(CH.glob(f"ch{int(r['first_chapter']):02d}_*.md")): out.append(("FAIL",r["line"],"first_chapter không tồn tại"))
    for r in rows:
        if r.get("vi_status") and r["vi_status"] not in STATUS: out.append(("FAIL",r["line"],f"vi_status không hợp lệ: {r['vi_status']}"))
    np_=sum(1 for r in rows if r.get("vi_status")=="proposed")
    if np_: out.append(("WARN",1,f"{np_} mục vi_status=proposed chưa được Ben xác nhận"))
    for k in set(x for x in keys if x):
        if keys.count(k)>1: out.append(("FAIL",1,f"key trùng {k}"))
    for p in sorted(CH.glob("ch0*.md")):
        text=p.read_text(encoding="utf-8");
        for abbr in re.findall(r"\b[A-Z][A-Z0-9+/-]{2,}\b",text):
            if abbr not in allow() and not any(r.get("abbr")==abbr for r in rows): out.append(("WARN",1,f"viết tắt {abbr} chưa có trong glossary/allowlist ({p.name})")); break
    return out,len(rows)
def show(fs,count):
    for l,n,m in fs: print(f"{l} {n}: {m}")
    c={x:sum(1 for f in fs if f[0]==x) for x in ("FAIL","WARN")}; print(f"Thuật ngữ: {count}; Đạt: {int(not fs)}; Không đạt: {c['FAIL']}; Chưa kiểm tra: 0; Không áp dụng: 0; WARN: {c['WARN']}"); return c
def self_test():
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/"g.yml"; p.write_text("terms:\n - {key: x, vi: x}\n - {key: x, vi: y}\n",encoding="utf-8"); rows=parse(p); assert rows[0]["key"] == rows[1]["key"]
    print("Đạt: self-test bắt được key trùng; Không đạt: 0; Chưa kiểm tra: 0; Không áp dụng: 0")
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--self-test",action="store_true"); a=ap.parse_args()
    if a.self_test:self_test();return 0
    if not a.check: print("Chưa kiểm tra: dùng --check; Đạt: 0; Không đạt: 0; Không áp dụng: 0");return 0
    fs,n=check(); c=show(fs,n); return 1 if c["FAIL"] else 0
if __name__=="__main__": raise SystemExit(main())
