#!/usr/bin/env python3
"""Build the elements catalogue from the estate's own permanent keys.

Nothing here invents a key. Every key already exists in a published source:

  block:<Sym>    an element: a block of the live block register
                 (https://ventusltd.github.io/stars/blocks/blocks.json), symbol unique.
                 Blocks whose kind is "app" are the register's defined apps.
  family:<n>     a function: the permanent function number of the numbered database
                 (families.json, n unique). Catalogued when its lineCount (line
                 occurrences) is MORE THAN 10; distinct_lines is reported beside it.
  line:<n>       a numbered line: the permanent line key (all-lines.bin, never reused).
                 Each function lists the first and last key OF ITS LINE SEQUENCE. These are
                 sequence endpoints, not numeric bounds: keys are issued in discovery
                 order, so the first key is often larger than the last, and a function may
                 repeat a key. "lines" counts occurrences; "distinct_lines" counts keys.
  surface:<url>  a served surface: the folder of a live address a block records, taken
                 verbatim from the register. The URL is its identity; it is not a new
                 number.

Titles and descriptions are the sources' own words. Where a source has no description,
the catalogue says what is known (kind, size, block, place counts, first written) and
says the description is not yet written. No prose is added that a source does not hold.

Inputs are fetched from their public addresses and pinned by sha256 in
catalogue/provenance.json. The register is copied into inputs/ because it changes;
the numbered database is referenced by address and digest.

Run from the repository root:  python build/build_catalogue.py
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import struct
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER_URL = "https://ventusltd.github.io/stars/blocks/blocks.json"
PACK_URL = "https://globalgrid2050.com/testcode/202609142202/data/"
PACK_FILES = ("all-lines.meta.json", "all-lines.bin", "families.json", "lines.bin")
MIN_LINES_EXCLUSIVE = 10


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def u32(b: bytes) -> list[int]:
    return list(struct.unpack(f"<{len(b) // 4}I", b))


def main() -> int:
    # --register <file> rebuilds from a committed register copy instead of the live one,
    # so a change to the builder can be separated from a change in the register.
    reg_arg = sys.argv[sys.argv.index("--register") + 1] if "--register" in sys.argv else None
    reg_raw = (ROOT / reg_arg).read_bytes() if reg_arg else fetch(REGISTER_URL)
    reg = json.loads(reg_raw.decode("utf-8"))
    pack = {n: fetch(PACK_URL + n) for n in PACK_FILES}
    meta = json.loads(pack["all-lines.meta.json"].decode("utf-8"))
    keyset = set(u32(pack["all-lines.bin"]))
    families = json.loads(pack["families.json"].decode("utf-8"))
    fam_lines = u32(pack["lines.bin"])
    if len(keyset) != meta["lines"]:
        raise SystemExit(f"all-lines.bin holds {len(keyset)} keys, meta says {meta['lines']}; refusing to build")

    blocks = reg["blocks"]
    by_sym = {b["symbol"]: b for b in blocks}
    if len(by_sym) != len(blocks):
        raise SystemExit("register symbols are not unique; refusing to build")
    cat_title = {}
    for c in reg.get("categories", []):
        if isinstance(c, dict):
            cat_title[c.get("id")] = c.get("title") or c.get("id")

    # which register blocks name each family (the register's own "inside" lists)
    named_by = defaultdict(list)
    for b in blocks:
        for fn in b.get("inside") or []:
            named_by[fn["family"]].append(b["symbol"])

    # ── functions: families with more than 10 numbered lines ──────────────────
    functions, seen = [], set()
    for fam in families:
        if fam["lineCount"] <= MIN_LINES_EXCLUSIVE:
            continue
        n = fam["n"]
        if n in seen:
            raise SystemExit(f"family {n} appears twice in families.json; refusing to build")
        seen.add(n)
        keys = fam_lines[fam["lineOffset"]: fam["lineOffset"] + fam["lineCount"]]
        missing = [k for k in keys if k not in keyset]
        if missing:
            raise SystemExit(f"family {n} names line keys absent from all-lines.bin: {missing[:5]}")
        blk = by_sym.get(fam["block"])
        name = fam.get("name")
        title = f"#{n} {name}" if name else f"#{n} (name not yet known)"
        distinct = len(set(keys))
        desc = (f"{fam['kind']} {name or '(name not yet known)'} · {fam['lineCount']} line occurrences, "
                f"{distinct} distinct line keys · sequence starts at line {keys[0]} and ends at line {keys[-1]} "
                f"(endpoints of the sequence, not a numeric range) · "
                + (f"in block {blk['symbol']} {blk['title']}" if blk else f"pack block {fam['block']} (not in the current register)")
                + f" · found in {fam['repos']} repositories and {fam['files']} files · "
                + ("self-contained" if fam.get("standalone") else "needs context")
                + (f" · first written {fam['first_written']}" if fam.get("first_written") else "")
                + " · description not yet written")
        functions.append({
            "key": f"family:{n}", "title": title, "name": name, "kind": fam["kind"],
            "lines": fam["lineCount"], "distinct_lines": distinct,
            "first_line": f"line:{keys[0]}", "last_line": f"line:{keys[-1]}",
            "block": f"block:{fam['block']}", "block_in_register": bool(blk),
            "category": fam.get("category"), "repos": fam["repos"], "files": fam["files"],
            "standalone": bool(fam.get("standalone")), "first_written": fam.get("first_written"),
            "named_by_register_blocks": [f"block:{s}" for s in named_by.get(n, [])],
            "description": desc,
        })

    # ── elements: every register block ────────────────────────────────────────
    pack_ids = {f["n"] for f in families}   # membership, not "above the highest": a gap in the numbering is also absent
    elements = []
    for b in blocks:
        inside = b.get("inside") or []
        elements.append({
            "key": f"block:{b['symbol']}", "number": b["number"], "symbol": b["symbol"],
            "title": b["title"], "description": b.get("description") or "description not yet written",
            "kind": b["kind"], "category": b["category"], "category_title": cat_title.get(b["category"], b["category"]),
            "state": b.get("state"), "functions_inside": len(inside),
            "function_keys": [f"family:{fn['family']}" for fn in inside],
            "functions_not_in_numbered_database": [f"family:{fn['family']}" for fn in inside if fn["family"] not in pack_ids],
            "repos": b.get("repos") or [], "live": b.get("live") or [],
            "files": [{"repo": f["repo"], "path": f["path"], "commit": f.get("commit")} for f in b.get("files") or []],
            "first_written": b.get("first_written"),
            "depends_on": [f"block:{d['symbol'] if isinstance(d, dict) else d}" for d in b.get("depends_on") or []],
            "used_by": [f"block:{d['symbol'] if isinstance(d, dict) else d}" for d in b.get("used_by") or []],
        })
    apps = [e for e in elements if e["kind"] == "app"]

    # ── surfaces: the folders of the live addresses the register records ──────
    # Identity rule, version 1, kept exactly as first published: the address text up to
    # its last "/", plus "/". It is not URL parsing: an address with no path, or with a
    # query or fragment containing "/", would give a wrong folder. None of the register's
    # addresses do today. A parsed-URL rule would be a new, versioned identity that keeps
    # these keys as aliases; it is not changed silently here.
    surf = defaultdict(list)
    for b in blocks:
        for u in b.get("live") or []:
            surf[u.rsplit("/", 1)[0] + "/"].append(b["symbol"])
    surfaces = [{"key": f"surface:{url}", "url": url, "title": url.split("://", 1)[-1],
                 "description": f"served folder recorded as the live address of {len(set(s))} register blocks",
                 "blocks": [f"block:{x}" for x in sorted(set(s))]} for url, s in sorted(surf.items())]

    # ── uniqueness across the whole catalogue ─────────────────────────────────
    all_keys = [x["key"] for x in elements] + [x["key"] for x in functions] + [x["key"] for x in surfaces]
    if len(all_keys) != len(set(all_keys)):
        raise SystemExit("a key appears twice across the catalogue; refusing to write")

    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = ROOT / "catalogue"
    out.mkdir(exist_ok=True)
    (ROOT / "inputs").mkdir(exist_ok=True)
    reg_name = f"blocks-{reg.get('generated_utc', 'unknown').replace(':', '').replace('.', '')}.json"
    (ROOT / "inputs" / reg_name).write_bytes(reg_raw)

    provenance = {
        "built_utc": now,
        "rule": {"elements": "every block of the live register", "apps": "register blocks whose kind is app",
                 "functions": f"families of the numbered database whose lineCount (line occurrences) is more than {MIN_LINES_EXCLUSIVE}; first_line and last_line are sequence endpoints, not numeric bounds",
                 "surfaces": "folders of the live addresses the register records"},
        "register": {"url": REGISTER_URL, "generated_utc": reg.get("generated_utc"), "sha256": sha(reg_raw),
                     "bytes": len(reg_raw), "copy": f"inputs/{reg_name}"},
        "numbered_database": [{"url": PACK_URL + n, "sha256": sha(pack[n]), "bytes": len(pack[n])} for n in PACK_FILES],
        "lines_source": meta.get("source"),
        "counts": {"elements": len(elements), "apps": len(apps), "surfaces": len(surfaces),
                   "families_total": len(families), "functions_over_10_lines": len(functions),
                   "numbered_lines": meta["lines"], "highest_line_key": meta["max"]},
    }
    w = lambda p, o: (out / p).write_text(json.dumps(o, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    w("provenance.json", provenance)
    w("elements.json", elements)
    w("apps.json", apps)
    w("surfaces.json", surfaces)
    w("functions.json", functions)
    write_markdown(provenance, elements, apps, surfaces, functions)
    print(json.dumps(provenance["counts"]))
    return 0


def cell(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def write_markdown(prov, elements, apps, surfaces, functions) -> None:
    c = prov["counts"]
    head = (f"Built {prov['built_utc']} from the block register generated {prov['register']['generated_utc']} "
            f"(sha256 `{prov['register']['sha256'][:12]}`) and the numbered database of {c['numbered_lines']:,} lines. "
            "Keys are the estate's permanent keys; none is invented. See catalogue/provenance.json.\n")
    md = ["# Catalogue of elements, apps and functions\n", head,
          "| what | key | count |", "|---|---|---|",
          f"| elements (register blocks) | `block:<Sym>` | {c['elements']} |",
          f"| apps (blocks of kind app) | `block:<Sym>` | {c['apps']} |",
          f"| served surfaces | `surface:<url>` | {c['surfaces']} |",
          f"| functions over 10 line occurrences | `family:<n>` | {c['functions_over_10_lines']} of {c['families_total']} |", "",
          "A function's first and last line keys are the ends of its line sequence, not a numeric range. "
          "Line occurrences count repeats; distinct lines count keys.", "",
          "- [Apps](APPS.md)", "- [Elements](ELEMENTS.md)", "- [Served surfaces](SURFACES.md)",
          "- Functions, by category: " + ", ".join(
              f"[{cat}](functions/{cat}.md)" for cat in sorted({f['category'] or 'other' for f in functions})), ""]
    (ROOT / "CATALOGUE.md").write_text("\n".join(md), encoding="utf-8")

    def table(rows, title):
        t = [f"# {title}\n", head, "| key | title | kind | category | state | functions | description |",
             "|---|---|---|---|---|---|---|"]
        for e in rows:
            t.append(f"| `{e['key']}` | {cell(e['title'])} | {e['kind']} | {cell(e['category_title'])} | "
                     f"{cell(e['state'])} | {e['functions_inside']} | {cell(e['description'])} |")
        return "\n".join(t) + "\n"
    (ROOT / "ELEMENTS.md").write_text(table(elements, "Elements"), encoding="utf-8")
    (ROOT / "APPS.md").write_text(table(apps, "Apps"), encoding="utf-8")

    s = ["# Served surfaces\n", head, "| key | blocks | description |", "|---|---|---|"]
    for x in surfaces:
        s.append(f"| `{x['key']}` | {', '.join('`'+b+'`' for b in x['blocks'])} | {cell(x['description'])} |")
    (ROOT / "SURFACES.md").write_text("\n".join(s) + "\n", encoding="utf-8")

    fdir = ROOT / "functions"
    fdir.mkdir(exist_ok=True)
    by_cat = defaultdict(list)
    for f in functions:
        by_cat[f["category"] or "other"].append(f)
    for cat, rows in by_cat.items():
        t = [f"# Functions over 10 lines · {cat}\n", head, f"{len(rows)} functions.\n",
             "| key | title | line occurrences | distinct lines | sequence starts | sequence ends | block | description |", "|---|---|---|---|---|---|---|---|"]
        for f in sorted(rows, key=lambda r: int(r["key"].split(":")[1])):
            t.append(f"| `{f['key']}` | {cell(f['title'])} | {f['lines']} | {f['distinct_lines']} | `{f['first_line']}` | `{f['last_line']}` | "
                     f"`{f['block']}` | {cell(f['description'])} |")
        (fdir / f"{cat}.md").write_text("\n".join(t) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
