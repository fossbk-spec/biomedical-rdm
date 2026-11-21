#!/usr/bin/env python3
"""Audit goi y cho cac muc references.bib khong co DOI.

Script tu tai URL trong .bib (bang chung that), roi Gemini chi so sanh noi dung trang voi thu muc.
Gemini khong duoc tu tra cuu bang tri nho. Muc khong co URL hoac trang khong tai duoc -> NOT_CHECKED.

KET QUA CHI LA GOI Y, khong phai xac nhan. Khong sua .bib hay citation-audit.csv.
API key doc tu bien moi truong GEMINI_API_KEY (khong ghi vao file). Chi gui tieu de/URL/nam
cua tai lieu; khong gui thong tin ca nhan.
"""
import csv, json, os, re, sys, time, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(__file__))
from verify_refs import parse_bib

MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.1-flash-lite")
KEY = os.environ["GEMINI_API_KEY"]
OUT = "references/audit-nodoi-gemini.csv"
FIELDS = ["key", "bib_title", "bib_year", "bib_url", "url_resolves", "found_title", "found_authors",
          "found_year", "found_publisher", "found_doi", "found_url", "match", "notes"]

PROMPT = """Ban kiem chung thu muc. Duoi day la thong tin thu muc trong danh muc va NOI DUNG THAT cua trang URL (da tai ve). Chi dua vao noi dung trang; khong dung tri nho. Truong nao trang khong cho thay thi de rong.
THU MUC: title="{title}" year="{year}" author="{author}" type="{type}"
TRANG: final_url={furl} http_status={status}
<<<{text}>>>
Tra ve DUY NHAT mot JSON (khong markdown) voi khoa: found_title, found_authors, found_year, found_publisher, found_doi, match (MATCH neu trang dung la tai lieu nay, PARTIAL neu cung chu de nhung khac ban/tieu de/nam, MISMATCH neu la tai lieu khac, NOT_CHECKED neu trang khong du thong tin), notes (ngan, tieng Viet, neu lech thi noi lech o dau)."""


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 rdm-reference-check"})
        r = urllib.request.urlopen(req, timeout=30)
        ct = r.headers.get("Content-Type", "")
        raw = r.read(600000)
        if "html" not in ct and "text" not in ct:
            return r.status, r.geturl(), f"[khong phai HTML: {ct}]"
        t = raw.decode("utf-8", "replace")
        ti = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
        t = re.sub(r"<(script|style)[^>]*>.*?</>", " ", t, flags=re.S | re.I)
        t = re.sub(r"<[^>]+>", " ", t); t = re.sub(r"\s+", " ", t)
        return r.status, r.geturl(), "TITLE: " + (ti.group(1).strip() if ti else "") + " | " + t[:4000]
    except urllib.error.HTTPError as ex:
        return ex.code, url, ""
    except Exception as ex:
        return None, url, ""


def ask(e, status, furl, text):
    body = {"contents": [{"parts": [{"text": PROMPT.format(
        title=e.get("title", ""), year=e.get("year", ""), type=e["type"], author=e.get("author", ""),
        furl=furl, status=status, text=text)}]}], "generationConfig": {"temperature": 0}}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
    for i in range(4):
        try:
            req = urllib.request.Request(url, json.dumps(body).encode(), {
                "Content-Type": "application/json", "x-goog-api-key": KEY})
            r = json.load(urllib.request.urlopen(req, timeout=120))
            txt = "".join(p.get("text", "") for p in r["candidates"][0]["content"]["parts"])
            return json.loads(re.search(r"\{.*\}", txt, re.S).group(0))
        except urllib.error.HTTPError as ex:
            if ex.code in (429, 500, 503): time.sleep(10 * (i + 1)); continue
            return {"match": "ERROR", "notes": f"Gemini HTTP {ex.code}"}
        except Exception as ex:
            if i == 3: return {"match": "ERROR", "notes": str(ex)[:120]}
            time.sleep(5)
    return {"match": "ERROR", "notes": "Gemini het luot thu"}


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    es = [e for e in parse_bib("references/references.bib") if not e.get("doi")][:limit]
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, FIELDS); w.writeheader()
        for e in es:
            u = e.get("url", "")
            if not u:
                r, st = {"match": "NOT_CHECKED", "notes": "Khong co URL; can audit thu cong"}, ""
            else:
                st, furl, text = fetch(u)
                if not text:
                    r = {"match": "NOT_CHECKED", "notes": f"Khong tai duoc trang (status {st})"}
                else:
                    r = ask(e, st, furl, text)
            r["url_resolves"] = st
            row = {"key": e["key"], "bib_title": e.get("title", ""), "bib_year": e.get("year", ""), "bib_url": e.get("url", "")}
            row.update({k: r.get(k, "") for k in FIELDS if k in r})
            w.writerow(row); f.flush()
            print(e["key"], row.get("match"), flush=True)
            time.sleep(2)


if __name__ == "__main__":
    main()
