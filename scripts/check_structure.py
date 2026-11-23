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
        m=re.search(r"\*\*(Hình|Bảng)\s+(\d+)\.(\d+)([a-z])?\.\s+.+?\*\*", line)
        if m: caps.append((m.group(1),int(m.group(2)),int(m.group(3)),m.group(4),n))
        elif re.search(r"\*\*(Hình|Bảng)\s+\d+[a-z]?\.\s", line): findings.append(("FAIL",n,"caption không theo dạng Hình/Bảng C.k (số chương.số thứ tự)"))
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
    mch=re.match(r"ch(\d+)_",path.name); chno=int(mch.group(1)) if mch else None
    seq={}
    for kind,c,k,sub,n in caps:
        token=f"{kind} {c}.{k}{sub or ''}"
        if chno is not None and c!=chno: findings.append(("FAIL",n,f"caption {token} có số chương {c}, file là chương {chno}"))
        if sub: findings.append(("WARN",n,f"caption {token} dùng tiểu hình; style-guide yêu cầu mỗi hình một số riêng"))
        body="\n".join(lines[:n-1]+lines[n:])
        if not re.search(rf"\b{re.escape(token)}\b",body): findings.append(("WARN",n,f"caption {token} không có dẫn chiếu trong thân"))
        seq.setdefault(kind,[]).append((k,n))
    for kind,vals in seq.items():
        ks=[v[0] for v in vals]
        if len(ks)!=len(set(ks)): findings.append(("FAIL",vals[0][1],f"trùng số {kind}"))
        elif ks!=list(range(1,len(ks)+1)): findings.append(("FAIL",vals[0][1],f"số thứ tự {kind} {ks} không liên tục từ 1"))
    for n,line in enumerate(lines,1):
        if any(x in line for x in ("[cite:", "TODO")):
            findings.append(("WARN",n,"dòng comment/rác của công cụ hoặc TODO còn sót"))
        elif any(x in line for x in ("CONTENT_PENDING", "BIB_PENDING", "[CẦN KIỂM CHỨNG")) and not line.lstrip().startswith(">"):
            findings.append(("INFO",n,"cờ chờ xác minh được giữ nguyên theo style-guide (không phải lỗi)"))
    return findings

def report(findings):
    counts={"FAIL":0,"WARN":0,"INFO":0}
    for level,n,msg in findings: counts[level]+=1; print(f"{level} {n}: {msg}")
    print(f"Đạt: {0 if findings else 1}; Không đạt: {counts['FAIL']}; Chưa kiểm tra: 0; Không áp dụng: 0; WARN: {counts['WARN']}; INFO: {counts['INFO']}")
    return counts

def self_test():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.md"
        p.write_text("# X\n## 1. A\n**Hình 1.1. x**\n", encoding="utf-8")
        assert any(x[0] == "WARN" for x in inspect(p)), "phải cảnh báo caption không dẫn chiếu"
        q = Path(d) / "ch02_x.md"
        q.write_text("# X\n## 1. A\n**Hình 5.1. x**\n**Hình 3a. y**\n", encoding="utf-8")
        assert sum(1 for x in inspect(q) if x[0] == "FAIL") >= 2, "phải báo sai số chương và sai dạng caption"
        r = Path(d) / "ch03_x.md"
        r.write_text("## 1. A\n", encoding="utf-8")
        assert any(x[0] == "FAIL" for x in inspect(r)), "phải báo thiếu tiêu đề"
    print("Đạt: self-test bắt được caption không dẫn chiếu, sai số chương/dạng caption và thiếu tiêu đề; Không đạt: 0; Chưa kiểm tra: 0; Không áp dụng: 0")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--self-test",action="store_true"); args=ap.parse_args()
    if args.self_test: self_test(); return 0
    if not args.check: print("Chưa kiểm tra: dùng --check để chạy trên chương; Không đạt: 0; Đạt: 0; Không áp dụng: 0"); return 0
    allf=[]
    for p in sorted(CHAPTERS.glob("ch0*.md")):
        fs=inspect(p); allf += [(p.relative_to(ROOT),n,l,m) for l,n,m in fs]; print(f"--- {p.name} ---"); report(fs)
    return 1 if any(x[2]=="FAIL" for x in allf) else 0
if __name__=="__main__": raise SystemExit(main())
