#!/usr/bin/env python3
"""Check chapter structure without modifying chapters."""
from __future__ import annotations
import argparse, re, tempfile
from pathlib import Path
import sys
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "docs" / "chapters"
STATUSES = ("Đạt", "Không đạt", "Chưa kiểm tra", "Không áp dụng")

def inspect(path: Path) -> list[tuple[str, int, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    findings=[]; fenced=False; h1=[]; h2=[]; caps=[]
    for n,line in enumerate(lines,1):
        if line.strip().startswith("```"): fenced=not fenced; continue
        if fenced: continue
        if re.match(r"^# ", line): h1.append(n)
        if re.match(r"^## ", line): h2.append((n,line))
        m=re.search(r"\*\*(Hình|Bảng)\s+(\d+)([a-z])?\.\s+.+?\*\*", line)
        if m: caps.append((m.group(1),int(m.group(2)),m.group(3),n))
    fm_title = bool(lines and lines[0].strip() == "---" and any(re.match(r"^title:\s*\S", l) for l in lines[1:12]))
    if len(h1) > 1 or (len(h1) == 0 and not fm_title):
        findings.append(("FAIL", 1, f"có {len(h1)} tiêu đề cấp 1 và {'có' if fm_title else 'không có'} title ở front matter; yêu cầu đúng một nguồn tiêu đề"))
    elif len(h1) == 0:
        findings.append(("WARN", 1, "tiêu đề nằm ở front matter (title:), không có H1 trong thân; các chương khác dùng H1, cần thống nhất"))
    nums=[]
    for n,line in h2:
        m=re.match(r"^##\s+(\d+)\.",line)
        if m: nums.append((n,int(m.group(1))))
    expected=list(range(1,len(nums)+1))
    if [x[1] for x in nums] != expected: findings.append(("WARN", nums[0][0] if nums else 1, f"số mục cấp 2 là {[x[1] for x in nums]}, không liên tục"))
    for kind,num,sub,n in caps:
        token=f"{kind} {num}{sub or ''}"
        body="\n".join(lines[:n-1]+lines[n:])
        if not re.search(rf"\b{re.escape(token)}\b",body): findings.append(("WARN",n,f"caption {token} không có dẫn chiếu trong thân"))
    grouped={}
    for kind,num,sub,n in caps: grouped.setdefault(kind,[]).append((num,sub,n))
    for kind,vals in grouped.items():
        bare=[v[0] for v in vals if not v[1]]
        if len(bare)!=len(set(bare)): findings.append(("FAIL",vals[0][2],f"trùng số {kind}"))
    for n,line in enumerate(lines,1):
        if any(x in line for x in ("[cite:", "TODO", "CONTENT_PENDING")) and not line.lstrip().startswith(">"):
            findings.append(("WARN",n,"dòng comment/rác hoặc cờ pending ngoài block được phép"))
    return findings

def report(findings):
    counts={"FAIL":0,"WARN":0}
    for level,n,msg in findings: counts[level]+=1; print(f"{level} {n}: {msg}")
    print(f"Đạt: {0 if findings else 1}; Không đạt: {counts['FAIL']}; Chưa kiểm tra: 0; Không áp dụng: 0; WARN: {counts['WARN']}")
    return counts

def self_test():
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/"x.md"; p.write_text("# X\n## 1. A\n**Hình 1. x**\n",encoding="utf-8")
        assert any(x[0]=="WARN" for x in inspect(p))
    print("Đạt: self-test bắt được caption không được dẫn chiếu; Không đạt: 0; Chưa kiểm tra: 0; Không áp dụng: 0")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--self-test",action="store_true"); args=ap.parse_args()
    if args.self_test: self_test(); return 0
    if not args.check: print("Chưa kiểm tra: dùng --check để chạy trên chương; Không đạt: 0; Đạt: 0; Không áp dụng: 0"); return 0
    allf=[]
    for p in sorted(CHAPTERS.glob("ch0*.md")):
        fs=inspect(p); allf += [(p.relative_to(ROOT),n,l,m) for l,n,m in fs]; print(f"--- {p.name} ---"); report(fs)
    return 1 if any(x[2]=="FAIL" for x in allf) else 0
if __name__=="__main__": raise SystemExit(main())
