#!/usr/bin/env python3
"""Doi chieu references/references.bib voi OpenAlex va Semantic Scholar.

Chi doc du lieu cong khai; khong gui thong tin ca nhan. Ket qua ghi vao
references/verification-report.csv. Khong tu sua .bib.
"""
import csv, difflib, json, re, sys, time, urllib.parse, urllib.request, urllib.error

UA = "rdm-reference-check/1.0"
BIB = "references/references.bib"
OUT = "references/verification-report.csv"


def parse_bib(path):
    txt = open(path, encoding="utf8").read().replace(chr(13) + chr(10), chr(10))
    entries = []
    for m in re.finditer(r"@(\w+)\{(\w+),(.*?)\n\}\n", txt, re.S):
        f = {}
        for k, v in re.findall(r"\n\s*(\w+)\s*=\s*\{(.*?)\},?(?=\n|$)", m.group(3), re.S):
            f[k.lower()] = v.replace(r"\&", "&").replace(r"\_", "_").replace(r"\%", "%")
        f["type"], f["key"] = m.group(1), m.group(2)
        entries.append(f)
    return entries


def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (429, 503):
                time.sleep(3 * (i + 1))
                continue
            return None
        except Exception:
            time.sleep(2)
    return None


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", (s or "").lower().replace("–", " ").replace("-", " ")).strip()


def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def openalex(e):
    if e.get("doi"):
        d = get("https://api.openalex.org/works/doi:" + urllib.parse.quote(e["doi"], safe="/()"))
        w = d
    else:
        d = get("https://api.openalex.org/works?per-page=3&search=" + urllib.parse.quote(e["title"][:200]))
        res = (d or {}).get("results") or []
        w = max(res, key=lambda x: sim(e["title"], x.get("title")), default=None)
    if not w:
        return None
    b = w.get("biblio") or {}
    if e.get("doi") and (w.get("doi") or "").lower().replace("https://doi.org/", "") != e["doi"].lower():
        return {"title": "[DOI_NOT_RESOLVED]", "year": "", "venue": "", "authors": "", "pages": "", "doi": ""}
    return {"title": w.get("title"), "year": w.get("publication_year"),
            "venue": ((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
            "authors": len(w.get("authorships") or []),
            "pages": "-".join(x for x in (b.get("first_page"), b.get("last_page")) if x),
            "doi": (w.get("doi") or "").replace("https://doi.org/", "")}


def s2(e):
    fields = "title,year,venue,authors,externalIds"
    if e.get("doi"):
        w = get("https://api.semanticscholar.org/graph/v1/paper/DOI:" + urllib.parse.quote(e["doi"], safe="/()") + "?fields=" + fields)
    else:
        d = get("https://api.semanticscholar.org/graph/v1/paper/search?limit=3&fields=" + fields + "&query=" + urllib.parse.quote(e["title"][:200]))
        res = (d or {}).get("data") or []
        w = max(res, key=lambda x: sim(e["title"], x.get("title")), default=None)
    if not w:
        return None
    return {"title": w.get("title"), "year": w.get("year"), "venue": w.get("venue"),
            "authors": len(w.get("authors") or []), "doi": (w.get("externalIds") or {}).get("DOI", "")}


def judge(e, r):
    if not r:
        return "NOT_FOUND"
    if r.get("title") == "[DOI_NOT_RESOLVED]":
        return "DOI_NOT_RESOLVED"
    ts = sim(e["title"], r.get("title"))
    ym = re.search(r"\d{4}", e.get("year", ""))
    yok = (not ym) or str(r.get("year")) == ym.group(0)
    if ts >= 0.9 and yok:
        return "MATCH"
    if ts >= 0.9:
        return "TITLE_MATCH_YEAR_DIFF"
    if ts >= 0.7:
        return "PARTIAL"
    return "MISMATCH" if e.get("doi") else "NO_RELIABLE_MATCH"


def main():
    es = parse_bib(BIB)
    rows = []
    for e in es:
        scholarly = e["type"] in ("article", "inproceedings", "book") or e.get("doi")
        if not scholarly:
            rows.append([e["key"], e["title"][:70], "", "", "", "NOT_APPLICABLE", "", "", "", "", "", "", "", ""])
            continue
        o = openalex(e); time.sleep(0.3)
        s = s2(e); time.sleep(1.2)
        rows.append([e["key"], e["title"][:70], e.get("year", ""), e.get("doi", ""), "doi" if e.get("doi") else "title-search",
                     judge(e, o), judge(e, s),
                     (o or {}).get("year", ""), (o or {}).get("authors", ""), (o or {}).get("pages", ""),
                     (s or {}).get("year", ""), (s or {}).get("authors", ""),
                     (o or {}).get("doi") or (s or {}).get("doi") or ""])
        print(rows[-1][0], rows[-1][5], rows[-1][6], flush=True)
    with open(OUT, "w", encoding="utf8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["key", "title", "bib_year", "bib_doi", "method", "openalex", "semantic_scholar",
                    "oa_year", "oa_n_authors", "oa_pages", "s2_year", "s2_n_authors", "doi_found"])
        w.writerows(rows)


if __name__ == "__main__":
    main()
