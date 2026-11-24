#!/usr/bin/env python3
"""Literature harvest and reference enrichment (OpenAlex, Semantic Scholar, Europe PMC).

Modes:
  enrich    look up every DOI in references/references.bib on OpenAlex and Semantic
            Scholar and write docs/literature-review/api-enrichment.md (metadata only).
  harvest   run the topic queries in references/lit_search_config.json and write one
            .md per topic under docs/literature-review/harvest/ (metadata only, NOT
            screened). Retrieval design per topic (OpenAlex): if the total number of
            matches is small the whole result set is retrieved; otherwise the 25 most
            cited records plus a seeded random sample are retrieved, each record is
            labelled with how it was retrieved.
  seedtest  check how many references already in references.bib (used as seed
            papers) are retrieved by the topic queries of their chapter; writes
            docs/literature-review/harvest/SEED_TEST.md.

Rules: read-only public APIs; OpenAlex and Semantic Scholar keys are read from the
environment (OPENALEX_API_KEY, SEMANTIC_SCHOLAR_API_KEY), sent in HTTP headers, and
never printed or stored; no e-mail or personal data is sent; no abstracts are copied
(copyright); nothing here edits references.bib or citation-audit.csv.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import unicodedata
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
UA = "rdm-literature-review/1.1"
OA_KEY = os.environ.get("OPENALEX_API_KEY", "")
S2_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
OA_BASE = "https://api.openalex.org"
S2_BASE = "https://api.semanticscholar.org/graph/v1"
EPMC_BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest"
S2_FIELDS = "title,year,venue,citationCount,influentialCitationCount,isOpenAccess,externalIds,publicationTypes,authors"
OA_SELECT = "id,doi,title,publication_year,cited_by_count,is_retracted,type,open_access,primary_location,authorships"
OA_TYPES = "article|review|preprint|book-chapter|data-paper|report|book|conference-paper"


def http(url: str, headers: dict | None = None, data: bytes | None = None, tries: int = 8):
    for i in range(tries):
        req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, "Accept": "application/json", **(headers or {})},
                                     method="POST" if data is not None else "GET")
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                ra = e.headers.get("Retry-After") if e.headers else None
                wait = float(ra) if ra and ra.replace(".", "", 1).isdigit() else min(60, 2 ** (i + 1))
                time.sleep(wait + (i % 3) * 0.5)
                continue
            return {"_error": f"HTTP {e.code}"}
        except Exception as e:  # network error
            if i < tries - 1:
                time.sleep(min(60, 2 ** (i + 1)))
                continue
            return {"_error": type(e).__name__}
    return {"_error": "unknown"}


def oa(path: str, params: dict) -> dict:
    h = {"Authorization": "Bearer " + OA_KEY} if OA_KEY else None
    return http(f"{OA_BASE}/{path}?" + urllib.parse.urlencode(params, safe=":|,"), h)


def s2_get(path: str, params: dict) -> dict:
    time.sleep(3.0)
    return http(f"{S2_BASE}/{path}?" + urllib.parse.urlencode(params), {"x-api-key": S2_KEY} if S2_KEY else None)


def s2_batch(ids: list[str]) -> list:
    out = []
    for i in range(0, len(ids), 100):
        time.sleep(3.0)
        hdr = {"Content-Type": "application/json"}
        if S2_KEY:
            hdr["x-api-key"] = S2_KEY
        d = http(f"{S2_BASE}/paper/batch?fields={S2_FIELDS}", hdr, json.dumps({"ids": ids[i:i + 100]}).encode())
        out += d if isinstance(d, list) else [None] * len(ids[i:i + 100])
    return out


def epmc(query: str, page_size: int, sort: str | None = None) -> dict:
    p = {"query": query, "format": "json", "pageSize": page_size, "resultType": "lite"}
    if sort:
        p["sort"] = sort
    time.sleep(0.5)
    return http(f"{EPMC_BASE}/search?" + urllib.parse.urlencode(p))


def norm_doi(d: str | None) -> str:
    s = (d or "").strip().lower()
    s = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", s)
    return s.rstrip(".,;)")


def norm_title(t: str | None) -> str:
    s = unicodedata.normalize("NFKC", t or "").casefold()
    return re.sub(r"[\W_]+", " ", s, flags=re.UNICODE).strip()


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
    if not authors or not authors[0]:
        return ""
    return authors[0].split()[-1] + (" et al." if len(authors) > 1 else "")


def oa_source(w: dict) -> str:
    return (((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "")


def oa_authors(w: dict) -> list[str]:
    return [((a.get("author") or {}).get("display_name") or "") for a in (w.get("authorships") or [])]


def esc(s: str) -> str:
    s = (s or "").replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ").strip()
    return re.sub(r"([\[\]<>`*_])", r"\\\1", s)


def mdlink_doi(doi: str) -> str:
    return f"[{doi}](https://doi.org/{doi})" if doi else ""


# ----------------------------------------------------------------- enrich
def enrich() -> int:
    entries = parse_bib()
    usage = chapter_usage()
    with_doi = [e for e in entries if e.get("doi")]
    no_doi = [e for e in entries if not e.get("doi")]
    dois = [norm_doi(e["doi"]) for e in with_doi]
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
    L = ["# Làm giàu metadata tham khảo bằng OpenAlex và Semantic Scholar", "",
         f"**Ngày chạy:** {today} · **Công cụ:** `scripts/lit_harvest.py enrich` · **Nguồn:** API công khai OpenAlex (lọc theo DOI, trường `{OA_SELECT}`) và Semantic Scholar (`/paper/batch`, trường `{S2_FIELDS}`) · **Dữ liệu:** `references/references.bib` ({len(entries)} mục, {len(with_doi)} có DOI)", "",
         "**Loại báo cáo:** EXPLORE, sơ bộ, chưa sàng lọc. **Chỉ là metadata:** số trích dẫn, cờ rút bài, loại tài liệu, trạng thái truy cập mở. Không xác nhận nội dung khẳng định trong sách và không đổi cột `status` trong `citation-audit.csv`. Số trích dẫn khác nhau giữa hai nguồn là bình thường (phạm vi chỉ mục khác nhau).", "",
         "## 1. Tóm tắt", "", "| Hạng mục | Số mục | Ghi chú |", "|---|---:|---|",
         f"| Mục có DOI trong `.bib` | {len(with_doi)} | được tra theo DOI trên cả hai API |",
         f"| Mục không có DOI | {len(no_doi)} | không tra trong báo cáo này (văn bản pháp luật, chuẩn, báo cáo, trang web, hoặc chưa có DOI) |",
         f"| Tìm thấy trên OpenAlex | {len(with_doi) - len(flags['oa_missing'])} | không tìm thấy: {', '.join('`' + k + '`' for k in flags['oa_missing']) or 'không'} |",
         f"| Tìm thấy trên Semantic Scholar | {len(with_doi) - len(flags['s2_missing'])} | |",
         f"| **Bị đánh dấu rút bài (OpenAlex `is_retracted`)** | {len(flags['retracted'])} | {', '.join('`' + k + '`' for k in flags['retracted']) or 'không'} |",
         f"| Năm khác giữa `.bib` và một API | {len(flags['year_diff'])} | thường là năm online và năm số tạp chí khác nhau; xem `references/VERIFICATION.md` |"]
    if oa_errors:
        L.append(f"| Lô OpenAlex bị lỗi | {oa_errors} | cần chạy lại |")
    L += ["", "**Lưu ý về rút bài:** OpenAlex phân loại thông báo rút bài (`type = retraction`) khác với bài bị rút (`is_retracted`). Các thông báo rút bài được dẫn có chủ ý trong case study không bị gắn cờ; cờ này không thay thế việc kiểm tay.", "",
          "## 2. Bảng chi tiết (theo khóa)", "",
          "| Khóa | Tác giả, năm (`.bib`) | Tiêu đề (`.bib`) | Chương dùng | OA: trích dẫn | OA: loại | OA: mở | OA: rút bài | S2: trích dẫn | S2: ảnh hưởng | Năm OA / S2 | DOI |",
          "|---|---|---|---|---:|---|---|---|---:|---:|---|---|"]
    for e, d, w, s, oy, sy, retr in rows:
        authors = [a.strip() for a in re.split(r"\sand\s|;", e.get("author", "")) if a.strip()] or [e.get("author", "")]
        au = (authors[0].split(",")[0] if authors else "") + (" et al." if len(authors) > 1 else "")
        L.append("| `{k}` | {au}, {y} | {t} | {ch} | {oc} | {ot} | {oo} | {orr} | {sc} | {si} | {yy} | {doi} |".format(
            k=e["key"], au=esc(au), y=e.get("year", ""), t=esc((e.get("title", ""))[:90]), ch=", ".join(usage.get(e["key"], [])) or "-",
            oc=w.get("cited_by_count", "") if w else "n/a", ot=esc(w.get("type", "")) if w else "",
            oo=((w.get("open_access") or {}).get("oa_status", "")) if w else "", orr="**RÚT BÀI**" if retr else ("không" if w else "n/a"),
            sc=s.get("citationCount", "") if s else "n/a", si=s.get("influentialCitationCount", "") if s else "n/a",
            yy=f"{oy or '-'} / {sy or '-'}", doi=mdlink_doi(d)))
    L += ["", "## 3. Mục không có DOI trong `.bib` (không tra)", "", "| Khóa | Tác giả, năm | Tiêu đề | Chương dùng |", "|---|---|---|---|"]
    for e in no_doi:
        L.append(f"| `{e['key']}` | {esc((e.get('author') or '')[:40])}, {e.get('year', '')} | {esc((e.get('title') or '')[:100])} | {', '.join(usage.get(e['key'], [])) or '-'} |")
    L += ["", "## 4. Giới hạn", "", "- Metadata tự động, chưa kiểm chứng nội dung; không dùng làm xác nhận trích dẫn.",
          "- OpenAlex đánh dấu `is_retracted` dựa trên dữ liệu bên thứ ba; cần đối chiếu nguồn khi cờ bật.",
          "- Số trích dẫn thay đổi theo thời gian; không đưa vào thân sách (thuộc lớp cập nhật)."]
    OUT_ENRICH.parent.mkdir(parents=True, exist_ok=True)
    OUT_ENRICH.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"enrich: {len(with_doi)} DOI, OA found {len(with_doi) - len(flags['oa_missing'])}, S2 found {len(with_doi) - len(flags['s2_missing'])}, retracted {flags['retracted']}, year_diff {len(flags['year_diff'])}")
    return 0


# ----------------------------------------------------------------- harvest
def oa_filter(q: str, from_year: int, extra: str = "") -> str:
    return f"title_and_abstract.search:{q},from_publication_date:{from_year}-01-01,type:{OA_TYPES}{extra}"


def oa_record(w: dict, how: str) -> dict:
    return {"doi": norm_doi(w.get("doi")), "title": w.get("title") or "", "year": w.get("publication_year"), "authors": oa_authors(w),
            "venue": oa_source(w), "oa_cited": w.get("cited_by_count"), "s2_cited": None, "epmc_cited": None,
            "retracted": bool(w.get("is_retracted")), "open": (w.get("open_access") or {}).get("oa_status", ""), "type": w.get("type", ""),
            "src": ["OpenAlex"], "how": [how]}


def fetch_openalex(oa_q: str, cfg: dict, err: list) -> tuple[list[dict], int | None, str]:
    """Return (records, total_matches, retrieval_description)."""
    from_year = cfg.get("from_year", 2008)
    all_le = cfg.get("all_if_total_le", 200)
    sample_n = cfg.get("sample_n", 100)
    seed = cfg.get("sample_seed", 20261124)
    base = {"per-page": 100, "select": OA_SELECT}
    first = oa("works", {**base, "filter": oa_filter(oa_q, from_year), "sort": "cited_by_count:desc", "page": 1})
    if "_error" in first:
        err.append("OpenAlex " + first["_error"])
        return [], None, "lỗi"
    total = (first.get("meta") or {}).get("count") or 0
    if total <= all_le:
        results = list(first.get("results", []))
        page = 2
        while len(results) < total and page <= 5:
            d = oa("works", {**base, "filter": oa_filter(oa_q, from_year), "sort": "cited_by_count:desc", "page": page})
            if "_error" in d:
                err.append("OpenAlex " + d["_error"])
                break
            results += d.get("results", [])
            page += 1
        recs = [oa_record(w, "all") for w in results]
        return recs, total, f"toàn bộ {len(recs)}/{total} bản ghi khớp"
    recs = [oa_record(w, "top25-cited") for w in first.get("results", [])[:25]]
    sm = oa("works", {"select": OA_SELECT, "filter": oa_filter(oa_q, from_year), "sample": sample_n, "seed": seed, "per-page": min(100, sample_n)})
    if "_error" in sm:
        err.append("OpenAlex sample " + sm["_error"])
    else:
        recs += [oa_record(w, f"random{sample_n}-seed{seed}") for w in sm.get("results", [])]
    return recs, total, f"25 bản ghi nhiều trích dẫn nhất + mẫu ngẫu nhiên {sample_n} (seed {seed}) trên {total} bản ghi khớp"


def merge(recs: dict[str, dict], titles: dict[str, str], new: dict) -> None:
    tk = norm_title(new["title"])
    key = new["doi"] or ("t:" + tk)
    if new["doi"] not in recs and tk in titles:
        other = recs[titles[tk]]
        if (not new["doi"] or not other["doi"]) and abs((other.get("year") or 0) - (new.get("year") or 0)) <= 1:
            key = titles[tk]
    if key in recs:
        r = recs[key]
        for f in ("oa_cited", "s2_cited", "epmc_cited"):
            if r.get(f) is None and new.get(f) is not None:
                r[f] = new[f]
        r["src"] += [s for s in new["src"] if s not in r["src"]]
        r["how"] += [h for h in new["how"] if h not in r["how"]]
        r["doi"] = r["doi"] or new["doi"]
        r["retracted"] = r["retracted"] or new["retracted"]
        r["open"] = r["open"] or new["open"]
    else:
        recs[key] = new
        if tk:
            titles.setdefault(tk, key)


def harvest() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    bib = parse_bib()
    bib_dois = {norm_doi(e.get("doi")) for e in bib if e.get("doi")}
    bib_titles = {norm_title(e.get("title")) for e in bib}
    today = dt.date.today().isoformat()
    from_year = cfg.get("from_year", 2008)
    OUT_HARVEST.mkdir(parents=True, exist_ok=True)
    index = []
    global_keys: set[str] = set()
    for topic in cfg["topics"]:
        recs: dict[str, dict] = {}
        titles: dict[str, str] = {}
        counts = {"openalex": 0, "semantic_scholar": 0, "europe_pmc": 0}
        totals: dict[str, int | None] = {}
        err: list[str] = []
        oa_q = topic.get("oa_query") or topic["query"]
        s2_q = topic.get("s2_query") or topic["query"]
        ep_q = topic.get("epmc_query")
        oa_recs, totals["openalex"], retrieval = fetch_openalex(oa_q, cfg, err)
        for r in oa_recs:
            counts["openalex"] += 1
            merge(recs, titles, r)
        s = s2_get("paper/search", {"query": s2_q, "limit": 25, "year": f"{from_year}-", "fields": S2_FIELDS})
        if "_error" in s:
            err.append("Semantic Scholar " + s["_error"])
        totals["semantic_scholar"] = s.get("total")
        for p in (s.get("data") or []):
            counts["semantic_scholar"] += 1
            merge(recs, titles, {"doi": norm_doi((p.get("externalIds") or {}).get("DOI")), "title": p.get("title") or "", "year": p.get("year"),
                                 "authors": [a.get("name", "") for a in (p.get("authors") or [])], "venue": p.get("venue") or "",
                                 "oa_cited": None, "s2_cited": p.get("citationCount"), "epmc_cited": None, "retracted": False,
                                 "open": "open" if p.get("isOpenAccess") else "", "type": ", ".join(p.get("publicationTypes") or []),
                                 "src": ["Semantic Scholar"], "how": ["s2-relevance25"]})
        if ep_q:
            e = epmc(f"({ep_q}) AND (FIRST_PDATE:[{from_year}-01-01 TO 3000-12-31])", 25, "CITED desc")
            if "_error" in e:
                err.append("Europe PMC " + e["_error"])
            totals["europe_pmc"] = e.get("hitCount")
            for p in ((e.get("resultList") or {}).get("result") or []):
                counts["europe_pmc"] += 1
                au = [a.strip() for a in (p.get("authorString") or "").split(",") if a.strip()]
                merge(recs, titles, {"doi": norm_doi(p.get("doi")), "title": (p.get("title") or "").rstrip("."),
                                     "year": int(p["pubYear"]) if str(p.get("pubYear", "")).isdigit() else None,
                                     "authors": au, "venue": p.get("journalTitle") or "", "oa_cited": None, "s2_cited": None,
                                     "epmc_cited": p.get("citedByCount"), "retracted": False, "open": "open" if p.get("isOpenAccess") == "Y" else "",
                                     "type": ", ".join([x for x in [p.get("source"), p.get("pubType")] if x])[:30], "src": ["Europe PMC"], "how": ["epmc-cited25"]})
        ranked = sorted(recs.values(), key=lambda r: (-(max([c for c in (r["oa_cited"], r["s2_cited"], r["epmc_cited"]) if isinstance(c, int)] or [0])), r["title"]))
        both = sum(1 for r in ranked if len(r["src"]) >= 2)

        def inbib(r):
            if r["doi"] and r["doi"] in bib_dois:
                return "có (DOI)"
            if norm_title(r["title"]) in bib_titles:
                return "có thể (chỉ khớp tiêu đề)"
            return ""
        in_bib = sum(1 for r in ranked if inbib(r).startswith("có (DOI)"))
        in_bib_t = sum(1 for r in ranked if inbib(r).startswith("có thể"))
        for r in ranked:
            global_keys.add(r["doi"] or "t:" + norm_title(r["title"]))
        L = [f"# Harvest: {topic['title']}", "",
             "**Loại review:** EXPLORE, **sơ bộ, chưa sàng lọc**, không dùng để trích dẫn trong sách. Danh sách chỉ là ứng viên; Gate 2 (sàng lọc) chưa được thực hiện. Xem `PROTOCOL.md`.", "",
             f"**Ngày chạy:** {today} · **Chương liên quan:** {', '.join(topic.get('chapters', []))} (chương chính: {topic.get('primary_chapter', topic.get('chapters', [''])[0])})", "",
             "**Truy vấn thực tế (không gồm khóa API):**", "",
             f"- OpenAlex: `GET /works?filter=title_and_abstract.search:{oa_q},from_publication_date:{from_year}-01-01,type:{OA_TYPES}` · {retrieval}",
             f"- Semantic Scholar: `GET /paper/search?query={s2_q}&year={from_year}-&limit=25` (độ liên quan)"]
        if ep_q:
            L.append(f"- Europe PMC: `GET /search?query=({ep_q}) AND FIRST_PDATE:[{from_year}-01-01 TO 3000-12-31]&sort=CITED desc&pageSize=25`")
        L += ["", "| Hạng mục | Số |", "|---|---:|",
              f"| OpenAlex: tổng số khớp / đã lấy | {totals.get('openalex')} / {counts['openalex']} |",
              f"| Semantic Scholar: tổng số khớp (không so sánh được) / đã lấy | {totals.get('semantic_scholar')} / {counts['semantic_scholar']} |"]
        if ep_q:
            L.append(f"| Europe PMC: tổng số khớp / đã lấy | {totals.get('europe_pmc')} / {counts['europe_pmc']} |")
        L += [f"| Sau khử trùng lặp (DOI; thiếu DOI thì tiêu đề chuẩn hóa và năm ±1) | {len(ranked)} |", f"| Có ở từ hai nguồn trở lên | {both} |",
              f"| Đã có trong `references.bib` (khớp DOI) | {in_bib} |", f"| Có thể có trong `references.bib` (chỉ khớp tiêu đề, cần kiểm tay) | {in_bib_t} |"]
        if err:
            L.append(f"| Lỗi API | {'; '.join(err)} |")
        L += ["", "Sắp xếp theo số trích dẫn cao nhất trong các nguồn (không phải mức liên quan hay chất lượng). Cột \"Cách lấy\" cho biết bản ghi thuộc nhóm nhiều trích dẫn, mẫu ngẫu nhiên hay toàn bộ. Chỉ metadata; không sao chép tóm tắt.", "",
              "| # | Tác giả, năm | Tiêu đề | Nơi đăng | Loại | OA | Trích dẫn OA / S2 / EPMC | Rút bài | Nguồn | Cách lấy | Trong .bib | DOI |", "|---:|---|---|---|---|---|---|---|---|---|---|---|"]
        short = {"OpenAlex": "OA", "Semantic Scholar": "S2", "Europe PMC": "EPMC"}
        for i, r in enumerate(ranked, 1):
            c = lambda v: v if v is not None else "-"
            L.append("| {i} | {au}, {y} | {t} | {v} | {ty} | {op} | {oc} / {sc} / {ec} | {rt} | {src} | {how} | {inb} | {doi} |".format(
                i=i, au=esc(first_author(r["authors"])), y=r["year"] or "", t=esc(r["title"][:110]), v=esc(r["venue"][:50]), ty=esc(r["type"][:20]),
                op=r["open"] or "", oc=c(r["oa_cited"]), sc=c(r["s2_cited"]), ec=c(r["epmc_cited"]), rt="**CÓ**" if r["retracted"] else "",
                src="+".join(short[x] for x in r["src"]), how=esc(", ".join(r["how"])), inb=inbib(r), doi=mdlink_doi(r["doi"])))
        L += ["", "## Giới hạn", "", "- Chuỗi tìm do nhóm biên soạn đề xuất, chưa có MeSH; độ nhạy xem `SEED_TEST.md`.",
              "- Mẫu nhiều trích dẫn nhất thiên về bài cũ và cộng đồng lớn; mẫu ngẫu nhiên (nếu có) mới dùng được để ước lượng cơ cấu kết quả.",
              "- Bài thiếu DOI được gộp theo tiêu đề chuẩn hóa và năm; có thể bỏ sót hoặc gộp nhầm. Các chủ đề chồng lấn nên tổng theo chủ đề không phải số nghiên cứu độc lập."]
        (OUT_HARVEST / f"{topic['id']}.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
        index.append((topic, counts, len(ranked), both, in_bib, in_bib_t, err, totals))
        print(f"harvest {topic['id']}: OA {counts['openalex']}/{totals['openalex']}, S2 {counts['semantic_scholar']}, EPMC {counts['europe_pmc']}/{totals.get('europe_pmc')}, unique {len(ranked)}, multi-src {both}, in_bib {in_bib}(+{in_bib_t}){' ERR ' + str(err) if err else ''}")
    I = ["# Harvest thử nghiệm (EXPLORE): chỉ mục các chủ đề", "",
         f"**Ngày chạy:** {today} · **Công cụ:** `scripts/lit_harvest.py harvest` · **Cấu hình:** `references/lit_search_config.json` (phiên bản {cfg.get('version')})", "",
         "Đây là bước thăm dò để chuẩn bị quy trình biên soạn chuyên khảo; **không phải review đã sàng lọc**. Xem `PROTOCOL.md`. Chỉ metadata; không có tóm tắt.", "",
         f"**Số bản ghi duy nhất trên toàn bộ {len(index)} chủ đề (khử trùng lặp liên chủ đề):** {len(global_keys)}. Tổng theo từng chủ đề không cộng được thành số nghiên cứu độc lập vì các chủ đề chồng lấn.", "",
         "| Chủ đề | Chương chính | OpenAlex (tổng / lấy) | Semantic Scholar (lấy) | Europe PMC (tổng / lấy) | Sau khử trùng lặp | Từ 2 nguồn | Trong .bib (DOI) | Có thể (tiêu đề) | Lỗi |", "|---|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for topic, c, u, b, ib, ibt, er, tot in index:
        I.append(f"| [{topic['title']}]({topic['id']}.md) | {topic.get('primary_chapter', topic.get('chapters', [''])[0])} | {tot.get('openalex')} / {c['openalex']} | {c['semantic_scholar']} | {tot.get('europe_pmc', '-')} / {c['europe_pmc']} | {u} | {b} | {ib} | {ibt} | {'; '.join(er)} |")
    (OUT_HARVEST / "README.md").write_text("\n".join(I) + "\n", encoding="utf-8", newline="\n")
    return 0


# ----------------------------------------------------------------- seedtest
def seedtest() -> int:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    bib = {e["key"]: e for e in parse_bib()}
    usage = chapter_usage()
    by_ch: dict[str, list[str]] = {}
    for k, chs in usage.items():
        for c in chs:
            by_ch.setdefault(c, []).append(k)
    L = ["# Kiểm tra độ nhạy chuỗi tìm bằng tài liệu mẫu (seed test)", "",
         f"**Ngày chạy:** {dt.date.today().isoformat()} · **Cấu hình:** phiên bản {cfg.get('version')} · **Cách làm:** lấy các mục trong `references.bib` có DOI và có trên OpenAlex làm tài liệu mẫu; thông báo rút bài (`type = retraction`) và bài loại `other` (tin, bình luận) bị loại khỏi mẫu; một mẫu được coi là *bắt được* nếu thỏa ít nhất một chuỗi OpenAlex (`title_and_abstract.search`, từ {cfg.get('from_year', 2008)}) của các chương mà nó được dẫn (đã ánh xạ số chương hiện có sang số chương đề xuất).", "",
         "**Hạn chế:** tài liệu mẫu là danh mục hiện có, vốn được chọn theo cách khác; kết quả đo độ nhạy với danh mục này, không phải với toàn bộ y văn. Không dùng để suy ra độ đặc hiệu. Điều chỉnh chuỗi để bắt mẫu có nguy cơ quá khớp (overfitting); mọi lần điều chỉnh phải ghi lại.", "",
         "| Chương | Mẫu có DOI | Có trên OpenAlex | Bắt được | Độ nhạy | Không bắt được |", "|---|---:|---:|---:|---:|---|"]
    tot_e = tot_f = 0
    uniq_e: set[str] = set()
    uniq_f: set[str] = set()
    c2p = cfg.get("current_to_planned", {})
    for ch in sorted(by_ch):
        fy = cfg.get("from_year", 2008)
        all_seeds = [k for k in by_ch[ch] if bib.get(k, {}).get("doi")]
        old = [k for k in all_seeds if str(bib[k].get("year", "9999")).isdigit() and int(bib[k]["year"]) < fy]
        seeds = [k for k in all_seeds if k not in old]
        planned = set(c2p.get(ch, [ch]))
        topics = [t for t in cfg["topics"] if planned & set(t["chapters"])]
        if not seeds or not topics:
            continue
        dois = ["https://doi.org/" + norm_doi(bib[k]["doi"]) for k in seeds]
        d = oa("works", {"filter": "doi:" + "|".join(dois), "per-page": 100, "select": "id,doi,type"})
        inoa = {norm_doi(w["doi"]) for w in d.get("results", []) if w.get("type") not in ("retraction", "other")}
        found: set[str] = set()
        for t in topics:
            dd = oa("works", {"filter": oa_filter(t["oa_query"], cfg.get("from_year", 2008), ",doi:" + "|".join(dois)), "per-page": 100, "select": "id,doi"})
            found |= {norm_doi(w["doi"]) for w in dd.get("results", [])}
        elig = [k for k in seeds if norm_doi(bib[k]["doi"]) in inoa]
        hit = [k for k in elig if norm_doi(bib[k]["doi"]) in found]
        miss = [k for k in elig if k not in hit]
        tot_e += len(elig)
        tot_f += len(hit)
        uniq_e |= set(elig)
        uniq_f |= set(hit)
        sens = f"{100 * len(hit) / len(elig):.0f}%" if elig else "n/a"
        L.append(f"| {ch} (chuỗi: {', '.join(t['id'].split('-')[0] for t in topics)}) | {len(seeds)} | {len(elig)} | {len(hit)} | {sens} | {', '.join('`' + k + '`' for k in miss) or '-'}{('; ngoài cửa sổ năm: ' + ', '.join('`' + k + '`' for k in old)) if old else ''} |")
        print(f"seedtest {ch}: {len(hit)}/{len(elig)} missed {miss}")
    L += ["", f"**Tổng theo chương:** {tot_f}/{tot_e} ({100 * tot_f / max(tot_e, 1):.0f}%); một mẫu được dẫn ở nhiều chương được đếm ở mỗi chương.",
          f"**Tổng theo mẫu duy nhất:** {len(uniq_f)}/{len(uniq_e)} ({100 * len(uniq_f) / max(len(uniq_e), 1):.0f}%). Tiêu chí của giao thức: ≥ 80% (xem `PROTOCOL.md` mục 6)."]
    (OUT_HARVEST / "SEED_TEST.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"seedtest total per chapter {tot_f}/{tot_e}; unique {len(uniq_f)}/{len(uniq_e)}; missed unique: {sorted(uniq_e - uniq_f)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["enrich", "harvest", "seedtest"])
    a = ap.parse_args()
    if not OA_KEY or not S2_KEY:
        print("Cảnh báo: thiếu khóa API trong môi trường; giới hạn tốc độ sẽ chặt hơn.", file=sys.stderr)
    return {"enrich": enrich, "harvest": harvest, "seedtest": seedtest}[a.mode]()


if __name__ == "__main__":
    raise SystemExit(main())
