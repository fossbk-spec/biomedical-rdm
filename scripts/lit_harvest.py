#!/usr/bin/env python3
"""Literature harvest and reference enrichment with OpenAlex and Semantic Scholar.

Two modes (see --help):
  enrich   look up every DOI in references/references.bib on both APIs and write
           docs/literature-review/api-enrichment.md (metadata only).
  harvest  run the topic queries in references/lit_search_config.json on both APIs,
           de-duplicate by DOI/title and write one .md per topic under
           docs/literature-review/harvest/ (metadata only, NOT screened).

Rules: read-only public APIs; keys are read from the environment
(OPENALEX_API_KEY, SEMANTIC_SCHOLAR_API_KEY) and are never printed or stored;
no e-mail or personal data is sent; no abstracts are copied (copyright);
nothing here edits references.bib or citation-audit.csv.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "references" / "references.bib"
CONFIG = ROOT / "references" / "lit_search_config.json"
CHAPTERS = ROOT / "docs" / "chapters"
OUT_ENRICH = ROOT / "docs" / "literature-review" / "api-enrichment.md"
OUT_HARVEST = ROOT / "docs" / "literature-review" / "harvest"
UA = "rdm-literature-review/1.0"
OA_KEY = os.environ.get("OPENALEX_API_KEY", "")
S2_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
OA_BASE = "https://api.openalex.org"
S2_BASE = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,year,venue,citationCount,influentialCitationCount,isOpenAccess,externalIds,publicationTypes,authors"
OA_SELECT = "id,doi,title,publication_year,cited_by_count,is_retracted,type,open_access,primary_location,authorships"


def http(url: str, headers: dict | None = None, data: bytes | None = None, tries: int = 8):
    for i in range(tries):
        req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, "Accept": "application/json", **(headers or {})},
                                     method="POST" if data is not None else "GET")
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(3 * (i + 1))
                continue
            return {"_error": f"HTTP {e.code}"}
        except Exception as e:  # network error
            if i < tries - 1:
                time.sleep(3 * (i + 1))
                continue
            return {"_error": type(e).__name__}
    return {"_error": "unknown"}


def oa(path: str, params: dict) -> dict:
    p = dict(params)
    if OA_KEY:
        p["api_key"] = OA_KEY
    return http(f"{OA_BASE}/{path}?" + urllib.parse.urlencode(p, safe=":|,"))


def s2_get(path: str, params: dict) -> dict:
    time.sleep(1.6)
    return http(f"{S2_BASE}/{path}?" + urllib.parse.urlencode(params), {"x-api-key": S2_KEY} if S2_KEY else None)


def s2_batch(ids: list[str]) -> list:
    out = []
    for i in range(0, len(ids), 100):
        time.sleep(1.6)
        d = http(f"{S2_BASE}/paper/batch?fields={S2_FIELDS}", {"x-api-key": S2_KEY, "Content-Type": "application/json"} if S2_KEY else {"Content-Type": "application/json"},
                 json.dumps({"ids": ids[i:i + 100]}).encode())
        out += d if isinstance(d, list) else [None] * len(ids[i:i + 100])
    return out


def norm_doi(d: str | None) -> str:
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", (d or "").strip().lower())


def norm_title(t: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def parse_bib() -> list[dict]:
    txt = BIB.read_text(encoding="utf-8").replace("\r\n", "\n")
    entries = []
    for m in re.finditer(r"@(\w+)\{(\w+),(.*?)\n\}\n", txt, re.S):
        f = {"type": m.group(1), "key": m.group(2)}
        for k, v in re.findall(r"\n\s*(\w+)\s*=\s*\{(.*?)\},?(?=\n|$)", m.group(3), re.S):
            f[k.lower()] = v.replace(r"\&", "&").replace(r"\_", "_").replace(r"\%", "%")
        entries.append(f)
    return entries


def chapter_usage() -> dict[str, list[str]]:
    use: dict[str, set] = {}
    for p in sorted(CHAPTERS.glob("ch0*.md")):
        n = re.match(r"ch(\d+)_", p.name)
        label = f"ch{n.group(1)}" if n else p.name
        for k in set(re.findall(r"ref_\d+", p.read_text(encoding="utf-8"))):
            use.setdefault(k, set()).add(label)
    return {k: sorted(v) for k, v in use.items()}


def first_author(authors: list[str]) -> str:
    if not authors:
        return ""
    a = authors[0].split()[-1] if authors[0] else ""
    return a + (" et al." if len(authors) > 1 else "")


def oa_source(w: dict) -> str:
    loc = w.get("primary_location") or {}
    return ((loc.get("source") or {}).get("display_name") or "")


def oa_authors(w: dict) -> list[str]:
    return [((a.get("author") or {}).get("display_name") or "") for a in (w.get("authorships") or [])]


def esc(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def mdlink_doi(doi: str) -> str:
    return f"[{doi}](https://doi.org/{doi})" if doi else ""


def enrich() -> int:
    entries = parse_bib()
    usage = chapter_usage()
    with_doi = [e for e in entries if e.get("doi")]
    no_doi = [e for e in entries if not e.get("doi")]
    dois = [norm_doi(e["doi"]) for e in with_doi]
    # OpenAlex in batches of 40
    oa_by_doi: dict[str, dict] = {}
    oa_errors = 0
    for i in range(0, len(dois), 40):
        chunk = dois[i:i + 40]
        d = oa("works", {"filter": "doi:" + "|".join("https://doi.org/" + x for x in chunk), "per-page": 50, "select": OA_SELECT})
        if "_error" in d:
            oa_errors += 1
            continue
        for w in d.get("results", []):
            oa_by_doi[norm_doi(w.get("doi"))] = w
    s2_list = s2_batch(["DOI:" + x for x in dois])
    s2_by_doi = {dois[i]: s2_list[i] for i in range(len(dois)) if i < len(s2_list) and s2_list[i]}
    today = dt.date.today().isoformat()
    rows = []
    flags = {"retracted": [], "oa_missing": [], "s2_missing": [], "year_diff": []}
    for e, d in zip(with_doi, dois):
        w, s = oa_by_doi.get(d), s2_by_doi.get(d)
        by = e.get("year", "")
        oy = str(w.get("publication_year")) if w else ""
        sy = str(s.get("year")) if s and s.get("year") else ""
        retr = bool(w and w.get("is_retracted"))
        if retr:
            flags["retracted"].append(e["key"])
        if not w:
            flags["oa_missing"].append(e["key"])
        if not s:
            flags["s2_missing"].append(e["key"])
        if by and ((oy and oy != by) or (sy and sy != by)):
            flags["year_diff"].append(e["key"])
        rows.append((e, d, w, s, oy, sy, retr))

    L = []
    L.append("# Làm giàu metadata tham khảo bằng OpenAlex và Semantic Scholar")
    L.append("")
    L.append(f"**Ngày chạy:** {today} · **Công cụ:** `scripts/lit_harvest.py enrich` · **Nguồn:** API công khai OpenAlex, Semantic Scholar (khóa đọc từ biến môi trường, không lưu) · **Dữ liệu:** `references/references.bib` ({len(entries)} mục, {len(with_doi)} có DOI)")
    L.append("")
    L.append("**Loại báo cáo:** EXPLORE, sơ bộ, chưa sàng lọc. **Chỉ là metadata:** số trích dẫn, cờ rút bài, loại tài liệu, trạng thái truy cập mở. Không xác nhận nội dung khẳng định trong sách và không đổi cột `status` trong `citation-audit.csv`. Số trích dẫn khác nhau giữa hai nguồn là bình thường (phạm vi chỉ mục khác nhau).")
    L.append("")
    L.append("## 1. Tóm tắt")
    L.append("")
    L.append("| Hạng mục | Số mục | Ghi chú |")
    L.append("|---|---:|---|")
    L.append(f"| Mục có DOI trong `.bib` | {len(with_doi)} | được tra theo DOI trên cả hai API |")
    L.append(f"| Mục không có DOI | {len(no_doi)} | không tra trong báo cáo này (văn bản pháp luật, chuẩn, báo cáo, trang web, hoặc chưa có DOI) |")
    L.append(f"| Tìm thấy trên OpenAlex | {len(with_doi) - len(flags['oa_missing'])} | |")
    L.append(f"| Tìm thấy trên Semantic Scholar | {len(with_doi) - len(flags['s2_missing'])} | |")
    L.append(f"| **Bị đánh dấu rút bài (OpenAlex `is_retracted`)** | {len(flags['retracted'])} | {', '.join('`' + k + '`' for k in flags['retracted']) or 'không'} |")
    L.append(f"| Năm khác giữa `.bib` và một API | {len(flags['year_diff'])} | thường là năm online và năm số tạp chí khác nhau; xem `references/VERIFICATION.md` |")
    if oa_errors:
        L.append(f"| Lô OpenAlex bị lỗi | {oa_errors} | cần chạy lại |")
    L.append("")
    L.append("**Lưu ý cho các mục rút bài:** bài Surgisphere (`ref_107`, `ref_108`) là bản thông báo rút bài (retraction notice) được dẫn có chủ ý trong case study; cờ rút bài ở đây có thể gắn với bài gốc bị rút chứ không phải thông báo. Cần xem từng dòng trước khi kết luận.")
    L.append("")
    L.append("## 2. Bảng chi tiết (theo khóa)")
    L.append("")
    L.append("| Khóa | Tác giả, năm (`.bib`) | Tiêu đề (`.bib`) | Chương dùng | OA: trích dẫn | OA: loại | OA: mở | OA: rút bài | S2: trích dẫn | S2: ảnh hưởng | Năm OA / S2 | DOI |")
    L.append("|---|---|---|---|---:|---|---|---|---:|---:|---|---|")
    for e, d, w, s, oy, sy, retr in rows:
        authors = [a.strip() for a in re.split(r"\sand\s|;", e.get("author", "")) if a.strip()] or [e.get("author", "")]
        au = (authors[0].split(",")[0] if authors else "") + (" et al." if len(authors) > 1 else "")
        L.append("| `{k}` | {au}, {y} | {t} | {ch} | {oc} | {ot} | {oo} | {orr} | {sc} | {si} | {yy} | {doi} |".format(
            k=e["key"], au=esc(au), y=e.get("year", ""), t=esc((e.get("title", ""))[:90]),
            ch=", ".join(usage.get(e["key"], [])) or "-",
            oc=w.get("cited_by_count", "") if w else "n/a", ot=esc(w.get("type", "")) if w else "",
            oo=((w.get("open_access") or {}).get("oa_status", "")) if w else "", orr="**RÚT BÀI**" if retr else ("không" if w else "n/a"),
            sc=s.get("citationCount", "") if s else "n/a", si=s.get("influentialCitationCount", "") if s else "n/a",
            yy=f"{oy or '-'} / {sy or '-'}", doi=mdlink_doi(d)))
    L.append("")
    L.append("## 3. Mục không có DOI trong `.bib` (không tra)")
    L.append("")
    L.append("| Khóa | Tác giả, năm | Tiêu đề | Chương dùng |")
    L.append("|---|---|---|---|")
    for e in no_doi:
        L.append(f"| `{e['key']}` | {esc((e.get('author') or '')[:40])}, {e.get('year', '')} | {esc((e.get('title') or '')[:100])} | {', '.join(usage.get(e['key'], [])) or '-'} |")
    L.append("")
    L.append("## 4. Giới hạn")
    L.append("")
    L.append("- Metadata tự động, chưa kiểm chứng nội dung; không dùng làm xác nhận trích dẫn.")
    L.append("- OpenAlex đánh dấu `is_retracted` dựa trên dữ liệu bên thứ ba; cần đối chiếu nguồn khi cờ bật.")
    L.append("- Số trích dẫn thay đổi theo thời gian; không đưa vào thân sách (thuộc lớp cập nhật).")
    OUT_ENRICH.parent.mkdir(parents=True, exist_ok=True)
    OUT_ENRICH.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"enrich: {len(with_doi)} DOI, OA found {len(with_doi) - len(flags['oa_missing'])}, S2 found {len(with_doi) - len(flags['s2_missing'])}, retracted {flags['retracted']}, year_diff {len(flags['year_diff'])}")
    return 0


def harvest() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    bib_dois = {norm_doi(e.get("doi")) for e in parse_bib() if e.get("doi")}
    bib_titles = {norm_title(e.get("title")) for e in parse_bib()}
    today = dt.date.today().isoformat()
    from_year = cfg.get("from_year", 2008)
    n_per = cfg.get("per_source", 25)
    OUT_HARVEST.mkdir(parents=True, exist_ok=True)
    index = []
    for topic in cfg["topics"]:
        recs: dict[str, dict] = {}
        counts = {"openalex": 0, "semantic_scholar": 0}
        err = []
        oa_q = topic.get("oa_query") or topic["query"]
        s2_q = topic.get("s2_query") or topic["query"]
        totals = {}
        d = oa("works", {"filter": f"title_and_abstract.search:{oa_q},from_publication_date:{from_year}-01-01,type:article|review|preprint|book-chapter",
                         "sort": "cited_by_count:desc", "per-page": n_per, "select": OA_SELECT})
        totals["openalex"] = (d.get("meta") or {}).get("count")
        if "_error" in d:
            err.append("OpenAlex " + d["_error"])
        for w in d.get("results", []) or []:
            counts["openalex"] += 1
            key = norm_doi(w.get("doi")) or "t:" + norm_title(w.get("title"))
            recs[key] = {"doi": norm_doi(w.get("doi")), "title": w.get("title") or "", "year": w.get("publication_year"),
                         "authors": oa_authors(w), "venue": oa_source(w), "oa_cited": w.get("cited_by_count"), "s2_cited": None,
                         "retracted": bool(w.get("is_retracted")), "open": (w.get("open_access") or {}).get("oa_status", ""),
                         "type": w.get("type", ""), "src": ["OpenAlex"]}
        s = s2_get("paper/search", {"query": s2_q, "limit": n_per, "year": f"{from_year}-", "fields": S2_FIELDS})
        totals["semantic_scholar"] = s.get("total") if isinstance(s, dict) else None
        if "_error" in s:
            err.append("Semantic Scholar " + s["_error"])
        for p in (s.get("data") or []):
            counts["semantic_scholar"] += 1
            doi = norm_doi((p.get("externalIds") or {}).get("DOI"))
            key = doi or "t:" + norm_title(p.get("title"))
            if key not in recs and "t:" + norm_title(p.get("title")) in recs:
                key = "t:" + norm_title(p.get("title"))
            if key in recs:
                recs[key]["s2_cited"] = p.get("citationCount")
                recs[key]["src"].append("Semantic Scholar")
            else:
                recs[key] = {"doi": doi, "title": p.get("title") or "", "year": p.get("year"),
                             "authors": [a.get("name", "") for a in (p.get("authors") or [])], "venue": p.get("venue") or "",
                             "oa_cited": None, "s2_cited": p.get("citationCount"), "retracted": False,
                             "open": "open" if p.get("isOpenAccess") else "", "type": ", ".join(p.get("publicationTypes") or []), "src": ["Semantic Scholar"]}
        ranked = sorted(recs.values(), key=lambda r: (-(max([c for c in (r["oa_cited"], r["s2_cited"]) if isinstance(c, int)] or [0])), r["title"]))
        both = sum(1 for r in ranked if len(r["src"]) == 2)
        in_bib = sum(1 for r in ranked if (r["doi"] and r["doi"] in bib_dois) or norm_title(r["title"]) in bib_titles)
        L = [f"# Harvest: {topic['title']}", "",
             "**Loại review:** EXPLORE, **sơ bộ, chưa sàng lọc**, không dùng để trích dẫn trong sách. Danh sách chỉ là ứng viên để Ben và người duyệt quyết định (Gate 1 và Gate 2 của `DrMayDay/.agents/workflows/literature-review.md` chưa được thực hiện).", "",
             f"**Ngày chạy:** {today} · **Chương liên quan:** {', '.join(topic.get('chapters', []))} · **Chuỗi OpenAlex (tiêu đề và tóm tắt):** `{oa_q}` · **Chuỗi Semantic Scholar:** `{s2_q}` · **Bộ lọc:** từ năm {from_year}; OpenAlex: article, review, preprint, book-chapter", "",
             "| Hạng mục | Số |", "|---|---:|",
             f"| OpenAlex: tổng số khớp / đã lấy | {totals.get('openalex')} / {counts['openalex']} |", f"| Semantic Scholar: tổng số khớp / đã lấy | {totals.get('semantic_scholar')} / {counts['semantic_scholar']} |",
             f"| Sau khử trùng lặp (theo DOI/tiêu đề) | {len(ranked)} |", f"| Có ở cả hai nguồn | {both} |",
             f"| Đã có trong `references.bib` | {in_bib} |"]
        if err:
            L.append(f"| Lỗi API | {'; '.join(err)} |")
        L += ["", "Sắp xếp theo số trích dẫn cao nhất trong hai nguồn (không phải mức liên quan hay chất lượng). Chỉ metadata; không sao chép tóm tắt.", "",
              "| # | Tác giả, năm | Tiêu đề | Nơi đăng | Loại | OA | Trích dẫn OA / S2 | Rút bài | Nguồn | Trong .bib | DOI |", "|---:|---|---|---|---|---|---|---|---|---|---|"]
        for i, r in enumerate(ranked, 1):
            inb = "có" if (r["doi"] and r["doi"] in bib_dois) or norm_title(r["title"]) in bib_titles else ""
            L.append("| {i} | {au}, {y} | {t} | {v} | {ty} | {op} | {oc} / {sc} | {rt} | {src} | {inb} | {doi} |".format(
                i=i, au=esc(first_author(r["authors"])), y=r["year"] or "", t=esc(r["title"][:110]), v=esc(r["venue"][:50]),
                ty=esc(r["type"][:20]), op=r["open"] or "", oc=r["oa_cited"] if r["oa_cited"] is not None else "-",
                sc=r["s2_cited"] if r["s2_cited"] is not None else "-", rt="**CÓ**" if r["retracted"] else "", src="+".join("OA" if x == "OpenAlex" else "S2" for x in r["src"]),
                inb=inb, doi=mdlink_doi(r["doi"])))
        L += ["", "## Giới hạn", "", "- Một chuỗi tìm kiếm cho mỗi chủ đề; chưa có MeSH, từ đồng nghĩa hay kiểm soát bởi người duyệt.", "- Xếp hạng theo trích dẫn thiên về bài cũ và bài của cộng đồng lớn; không phản ánh chất lượng.", "- Bài không có DOI được khử trùng lặp theo tiêu đề; có thể bỏ sót hoặc gộp nhầm."]
        fn = f"{topic['id']}.md"
        (OUT_HARVEST / fn).write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
        index.append((topic, counts, len(ranked), both, in_bib, err, totals))
        print(f"harvest {topic['id']}: OA {counts['openalex']}, S2 {counts['semantic_scholar']}, unique {len(ranked)}, both {both}, in_bib {in_bib}{' ERR ' + str(err) if err else ''}")
    I = ["# Harvest thử nghiệm (EXPLORE): chỉ mục các chủ đề", "",
         f"**Ngày chạy:** {today} · **Công cụ:** `scripts/lit_harvest.py harvest` · **Cấu hình:** `references/lit_search_config.json`", "",
         "Đây là bước thăm dò để chuẩn bị quy trình biên soạn chuyên khảo; **không phải review đã sàng lọc**. Chuỗi tìm kiếm chưa được Ben duyệt (Gate 1). Chỉ metadata; không có tóm tắt.", "",
         "| Chủ đề | Chương | OpenAlex (tổng / lấy) | Semantic Scholar (tổng / lấy) | Sau khử trùng lặp | Ở cả hai | Đã có trong .bib | Lỗi |", "|---|---|---:|---:|---:|---:|---:|---|"]
    for topic, c, u, b, ib, er, tot in index:
        I.append(f"| [{topic['title']}]({topic['id']}.md) | {', '.join(topic.get('chapters', []))} | {tot.get('openalex')} / {c['openalex']} | {tot.get('semantic_scholar')} / {c['semantic_scholar']} | {u} | {b} | {ib} | {'; '.join(er)} |")
    (OUT_HARVEST / "README.md").write_text("\n".join(I) + "\n", encoding="utf-8", newline="\n")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["enrich", "harvest"])
    a = ap.parse_args()
    if not OA_KEY or not S2_KEY:
        print("Cảnh báo: thiếu khóa API trong môi trường; giới hạn tốc độ sẽ chặt hơn.", file=sys.stderr)
    return enrich() if a.mode == "enrich" else harvest()


if __name__ == "__main__":
    raise SystemExit(main())
