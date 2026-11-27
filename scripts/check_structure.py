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
CHAPTER_MAP = ROOT / "editorial" / "chapter-map.yml"
LAYER_BASIC, LAYER_ADV = "[Cơ sở]", "[Nâng cao & Case Study]"

def frame_of(chno: int | None, map_path: Path = CHAPTER_MAP) -> str:
    """Return 'v2' when chapter-map.yml marks the chapter with `frame: v2`, else 'v1'."""
    if chno is None or not map_path.exists():
        return "v1"
    for line in map_path.read_text(encoding="utf-8").splitlines():
        if re.search(rf"\bid:\s*ch{chno:02d}\b", line):
            return "v2" if re.search(r"\bframe:\s*v2\b", line) else "v1"
    return "v1"

def check_frame_v2(h2: list[tuple[int, str]], h3: list[tuple[int, str]], chno: int | None) -> list[tuple[str, int, str]]:
    """Frame v2: optional `Lời mở đầu`, sections X.1.–X.5. (X = chapter number), `Tài liệu tham khảo`, optional quiz."""
    out: list[tuple[str, int, str]] = []
    if chno is None:
        return [("FAIL", 1, "khung v2 cần tên tệp dạng chNN_...")]
    heads = [(n, line[3:].strip()) for n, line in h2]
    nums = []
    for n, text in heads:
        m = re.match(r"(\d+)\.(\d+)\.\s", text)
        if m:
            nums.append((n, int(m.group(1)), int(m.group(2)), text))
    for n, x, k, text in nums:
        if x != chno:
            out.append(("FAIL", n, f"mục '{text[:40]}' có tiền tố chương {x}, tệp là chương {chno}"))
    ks = [k for _n, x, k, _t in nums if x == chno]
    if ks != [1, 2, 3, 4, 5]:
        out.append(("FAIL", nums[0][0] if nums else 1, f"khung v2 yêu cầu mục cấp 2 {chno}.1.–{chno}.5. liên tục; hiện có {ks}"))
    for n, x, k, text in nums:
        if k == 1 and LAYER_BASIC not in text:
            out.append(("WARN", n, f"mục {x}.{k}. thiếu nhãn {LAYER_BASIC}"))
        if k in (2, 3, 4) and LAYER_ADV not in text:
            out.append(("WARN", n, f"mục {x}.{k}. thiếu nhãn {LAYER_ADV}"))
    titles = [t.lower() for _n, t in heads]
    if not any(t.startswith("lời mở đầu") for t in titles):
        out.append(("WARN", 1, "khung v2 thiếu mục 'Lời mở đầu'"))
    if not any(t.startswith("tài liệu tham khảo") for t in titles):
        out.append(("FAIL", 1, "khung v2 thiếu mục 'Tài liệu tham khảo'"))
    for n, text in heads:
        if text.lower().startswith(("lời mở đầu", "tài liệu tham khảo")) and re.match(r"\d", text):
            out.append(("FAIL", n, "mục 'Lời mở đầu' và 'Tài liệu tham khảo' không đánh số"))
    cur = None
    for n, line in sorted(h2 + h3):
        text = line.lstrip("#").strip()
        if line.startswith("## "):
            m = re.match(r"(\d+)\.(\d+)\.\s", text)
            cur = (int(m.group(1)), int(m.group(2))) if m else None
        else:
            m = re.match(r"(\d+)\.(\d+)\.(\d+)\.\s", text)
            if m and cur and (int(m.group(1)), int(m.group(2))) != cur:
                out.append(("FAIL", n, f"mục '{text[:40]}' không khớp mục cấp 2 {cur[0]}.{cur[1]}."))
    return out

def inspect(path: Path) -> list[tuple[str, int, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    findings=[]; fenced=False; h1=[]; h2=[]; h3=[]; caps=[]
    for n,line in enumerate(lines,1):
        if line.strip().startswith("```"): fenced=not fenced; continue
        if fenced: continue
        if re.match(r"^# ", line): h1.append(n)
        if re.match(r"^## ", line): h2.append((n,line))
        if re.match(r"^### ", line): h3.append((n,line))
        m=re.search(r"\*\*(Hình|Bảng)\s+(\d+)\.(\d+)([a-z])?\.\s+.+?\*\*", line)
        if m: caps.append((m.group(1),int(m.group(2)),int(m.group(3)),m.group(4),n))
        elif re.search(r"\*\*(Hình|Bảng)\s+\d+[a-z]?\.\s", line): findings.append(("FAIL",n,"caption không theo dạng Hình/Bảng C.k (số chương.số thứ tự)"))
    fm_title = bool(lines and lines[0].strip() == "---" and any(re.match(r"^title:\s*\S", l) for l in lines[1:12]))
    if len(h1) > 1 or (len(h1) == 0 and not fm_title):
        findings.append(("FAIL", 1, f"có {len(h1)} tiêu đề cấp 1 và {'có' if fm_title else 'không có'} title ở front matter; yêu cầu đúng một nguồn tiêu đề"))
    elif len(h1) == 0:
        findings.append(("WARN", 1, "tiêu đề nằm ở front matter (title:), không có H1 trong thân; các chương khác dùng H1, cần thống nhất"))
    mch=re.match(r"ch(\d+)_",path.name); chno=int(mch.group(1)) if mch else None
    if frame_of(chno) == "v2":
        findings += check_frame_v2(h2, h3, chno)
    else:
        nums=[]
        for n,line in h2:
            m=re.match(r"^##\s+(\d+)\.",line)
            if m: nums.append((n,int(m.group(1))))
        expected=list(range(1,len(nums)+1))
        if [x[1] for x in nums] != expected: findings.append(("WARN", nums[0][0] if nums else 1, f"số mục cấp 2 là {[x[1] for x in nums]}, không liên tục"))
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
        mp = Path(d) / "map.yml"
        mp.write_text("chapters:\n  - {id: ch04, frame: v2}\n  - {id: ch05, status: draft}\n", encoding="utf-8")
        assert frame_of(4, mp) == "v2" and frame_of(5, mp) == "v1" and frame_of(9, mp) == "v1", "phải đọc cờ frame từ chapter-map"
        good = [(3, "## Lời mở đầu")] + [(10 * k, f"## 4.{k}. T {LAYER_BASIC if k == 1 else LAYER_ADV if k < 5 else ''}") for k in range(1, 6)] + [(99, "## Tài liệu tham khảo")]
        assert not [x for x in check_frame_v2(good, [(11, "### 4.1.1. A"), (21, "### 4.2.1. B"), (22, "### Ghi chú")], 4) if x[0] == "FAIL"], "khung v2 hợp lệ không được báo FAIL"
        bad = [(3, "## 4.1. A"), (4, "## 4.3. B"), (5, "## 5.2. C")]
        fails = [x for x in check_frame_v2(bad, [(6, "### 4.1.2. D"), (7, "### 4.3.1. E")], 4) if x[0] == "FAIL"]
        assert len(fails) >= 3, "phải báo sai tiền tố, thiếu/không liên tục mục, thiếu Tài liệu tham khảo"
    print("Đạt: self-test bắt được caption không dẫn chiếu, sai số chương/dạng caption, thiếu tiêu đề và sai khung v2; Không đạt: 0; Chưa kiểm tra: 0; Không áp dụng: 0")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--self-test",action="store_true"); args=ap.parse_args()
    if args.self_test: self_test(); return 0
    if not args.check: print("Chưa kiểm tra: dùng --check để chạy trên chương; Không đạt: 0; Đạt: 0; Không áp dụng: 0"); return 0
    allf=[]
    for p in sorted(CHAPTERS.glob("ch0*.md")):
        fs=inspect(p); allf += [(p.relative_to(ROOT),n,l,m) for l,n,m in fs]; print(f"--- {p.name} ---"); report(fs)
    return 1 if any(x[2]=="FAIL" for x in allf) else 0
if __name__=="__main__": raise SystemExit(main())
