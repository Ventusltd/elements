#!/usr/bin/env python3
"""Checks of the committed catalogue against its pinned inputs.

Run from the repository root:  python tests/check_catalogue.py

WHAT THIS PROVES. This file builds, independently of the builder, the complete row
for every entry from the pinned register copy and the pinned numbered database, and
requires each committed row to equal it exactly, field for field, with no extra and
no missing fields:
- functions: key, title, name, kind, lines, distinct_lines, first_line, last_line,
  block, block_in_register, category, repos, files, standalone, first_written,
  named_by_register_blocks, description (every value derived from families.json,
  lines.bin and the register);
- elements: key, number, symbol, title, description, kind, category, category_title,
  state, functions_inside, function_keys, functions_not_in_numbered_database, repos,
  live, files, first_written, depends_on, used_by (from the register; membership
  against families.json);
- apps: exactly the element rows of kind app, whole rows;
- surfaces: key, url, title, description, blocks;
- provenance: every count (elements, apps, surfaces, families_total,
  functions_over_10_lines, numbered_lines, highest_line_key) and the register's
  generated_utc and byte length, all with the same JSON types.
It also requires every line key of every catalogued function's sequence to be issued.

WHAT THIS DOES NOT PROVE. That the register or the numbered database are right;
that the register's depends_on and used_by edges are real (they are copied as the
register states them, and references to blocks the register does not hold are
counted and printed, not hidden); that keys were never reused historically; that
any surface is live or any function runs.

Before the real catalogue may pass, every deliberately broken copy below must fail,
including each unchecked-field case a peer review found.
"""
import copy, hashlib, json, struct, sys, urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
load = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))


def expected_rows(register, families, fam_lines):
    blocks = register["blocks"]
    by_sym = {b["symbol"]: b for b in blocks}
    cat_title = {c.get("id"): c.get("title") or c.get("id") for c in register.get("categories", []) if isinstance(c, dict)}
    named_by = defaultdict(list)
    for b in blocks:
        for fn in b.get("inside") or []:
            named_by[fn["family"]].append(b["symbol"])

    funcs = []
    for fam in families:
        if fam["lineCount"] <= 10:
            continue
        n, name = fam["n"], fam.get("name")
        seq = fam_lines[fam["lineOffset"]: fam["lineOffset"] + fam["lineCount"]]
        if fam["lineOffset"] < 0 or fam["lineOffset"] + fam["lineCount"] > len(fam_lines) or len(seq) != fam["lineCount"]:
            raise SystemExit(f"family {n} points outside lines.bin")
        blk = by_sym.get(fam["block"])
        distinct = len(set(seq))
        desc = (f"{fam['kind']} {name or '(name not yet known)'} · {fam['lineCount']} line occurrences, "
                f"{distinct} distinct line keys · sequence starts at line {seq[0]} and ends at line {seq[-1]} "
                f"(endpoints of the sequence, not a numeric range) · "
                + (f"in block {blk['symbol']} {blk['title']}" if blk else f"pack block {fam['block']} (not in the current register)")
                + f" · found in {fam['repos']} repositories and {fam['files']} files · "
                + ("self-contained" if fam.get("standalone") else "needs context")
                + (f" · first written {fam['first_written']}" if fam.get("first_written") else "")
                + " · description not yet written")
        funcs.append({
            "key": f"family:{n}", "title": f"#{n} {name}" if name else f"#{n} (name not yet known)", "name": name,
            "kind": fam["kind"], "lines": fam["lineCount"], "distinct_lines": distinct,
            "first_line": f"line:{seq[0]}", "last_line": f"line:{seq[-1]}",
            "block": f"block:{fam['block']}", "block_in_register": bool(blk), "category": fam.get("category"),
            "repos": fam["repos"], "files": fam["files"], "standalone": bool(fam.get("standalone")),
            "first_written": fam.get("first_written"),
            "named_by_register_blocks": [f"block:{s}" for s in named_by.get(n, [])], "description": desc,
            "_sequence": seq,
        })

    pack_ids = {f["n"] for f in families}
    sym = lambda d: d["symbol"] if isinstance(d, dict) else d
    elems = []
    for b in blocks:
        inside = b.get("inside") or []
        elems.append({
            "key": f"block:{b['symbol']}", "number": b["number"], "symbol": b["symbol"], "title": b["title"],
            "description": b.get("description") or "description not yet written", "kind": b["kind"],
            "category": b["category"], "category_title": cat_title.get(b["category"], b["category"]),
            "state": b.get("state"), "functions_inside": len(inside),
            "function_keys": [f"family:{fn['family']}" for fn in inside],
            "functions_not_in_numbered_database": [f"family:{fn['family']}" for fn in inside if fn["family"] not in pack_ids],
            "repos": b.get("repos") or [], "live": b.get("live") or [],
            "files": [{"repo": f["repo"], "path": f["path"], "commit": f.get("commit")} for f in b.get("files") or []],
            "first_written": b.get("first_written"),
            "depends_on": [f"block:{sym(d)}" for d in b.get("depends_on") or []],
            "used_by": [f"block:{sym(d)}" for d in b.get("used_by") or []],
        })
    apps = [e for e in elems if e["kind"] == "app"]
    surf = defaultdict(set)
    for b in blocks:
        for u in b.get("live") or []:
            surf[u.rsplit("/", 1)[0] + "/"].add(b["symbol"])
    surfs = [{"key": f"surface:{u}", "url": u, "title": u.split("://", 1)[-1],
              "description": f"served folder recorded as the live address of {len(s)} register blocks",
              "blocks": [f"block:{x}" for x in sorted(s)]} for u, s in sorted(surf.items())]
    known = {x["key"] for x in elems}
    refs = [(e["key"], field, r) for e in elems for field in ("depends_on", "used_by") for r in e[field] if r not in known]
    dangling = {"references": len(refs), "source_blocks": len({s for s, _, _ in refs}),
                "distinct_targets": sorted({r for _, _, r in refs}),
                "by_field": {f: sum(1 for _, g, _ in refs if g == f) for f in ("depends_on", "used_by")}}
    return {"functions": funcs, "elements": elems, "apps": apps, "surfaces": surfs}, dangling


def same(a, b):
    """Equality that also requires the same JSON type: True is not 1, 0 is not False."""
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    return a == b


def problems(cat, prov, exp, keyset):
    bad = []
    keys = [x["key"] for part in ("elements", "functions", "surfaces") for x in cat[part]]
    if len(keys) != len(set(keys)):
        bad.append("a key appears more than once")
    for part in ("functions", "elements", "apps", "surfaces"):
        want = {r["key"]: {k: v for k, v in r.items() if not k.startswith("_")} for r in exp[part]}
        got_list = cat[part]
        got = {}
        for r in got_list:
            if r.get("key") in got:
                bad.append(f"{part}: {r.get('key')} listed twice")
            got[r.get("key")] = r
        if len(got_list) != len(exp[part]):
            bad.append(f"{part}: {len(got_list)} rows, recomputed {len(exp[part])}")
        extra, missing = set(got) - set(want), set(want) - set(got)
        if extra or missing:
            bad.append(f"{part}: {len(extra)} extra keys, {len(missing)} missing keys")
        for k in set(got) & set(want):
            if not same(got[k], want[k]):
                fields = sorted(f for f in set(got[k]) | set(want[k]) if not same(got[k].get(f), want[k].get(f)) or (f in got[k]) != (f in want[k]))
                bad.append(f"{part} {k}: fields differ from the recomputed row: {fields}")
    for r in exp["functions"]:
        if any(key not in keyset for key in r["_sequence"]):
            bad.append(f"{r['key']}: a line key in its sequence is not issued")
    c = dict(prov["counts"])
    for field, want in exp["_counts"].items():
        if not same(c.get(field), want):
            bad.append(f"provenance counts.{field} is {c.get(field)!r}, recomputed {want!r}")
    for field, want in exp["_register"].items():
        if not same(prov["register"].get(field), want):
            bad.append(f"provenance register.{field} is {prov['register'].get(field)!r}, recomputed {want!r}")
    if "_apps_count" in cat:
        c["apps"] = cat["_apps_count"]
    if (c["elements"], c["apps"], c["surfaces"], c["functions_over_10_lines"]) != \
            (len(cat["elements"]), len(cat["apps"]), len(cat["surfaces"]), len(cat["functions"])):
        bad.append("provenance counts differ from the catalogue")
    return bad


def main():
    prov = load("catalogue/provenance.json")
    reg_bytes = (ROOT / prov["register"]["copy"]).read_bytes()
    if hashlib.sha256(reg_bytes).hexdigest() != prov["register"]["sha256"]:
        sys.exit("register copy does not match its recorded sha256")
    register = json.loads(reg_bytes)
    pack = {}
    for src in prov["numbered_database"]:
        b = urllib.request.urlopen(src["url"], timeout=120).read()
        if hashlib.sha256(b).hexdigest() != src["sha256"]:
            sys.exit(f"served bytes changed since the build: {src['url']}")
        pack[src["url"].rsplit("/", 1)[1]] = b
    u32 = lambda b: list(struct.unpack(f"<{len(b)//4}I", b))
    keyset = set(u32(pack["all-lines.bin"]))
    families = json.loads(pack["families.json"])
    meta = json.loads(pack["all-lines.meta.json"])
    exp, dangling = expected_rows(register, families, u32(pack["lines.bin"]))
    exp["_counts"] = {"elements": len(exp["elements"]), "apps": len(exp["apps"]), "surfaces": len(exp["surfaces"]),
                      "families_total": len(families), "functions_over_10_lines": len(exp["functions"]),
                      "numbered_lines": meta["lines"], "highest_line_key": meta["max"]}
    if meta["lines"] != len(keyset) or meta["max"] != max(keyset):
        sys.exit("all-lines.meta.json disagrees with all-lines.bin")
    exp["_register"] = {"generated_utc": register.get("generated_utc"), "bytes": len(reg_bytes)}
    cat = {k: load(f"catalogue/{k}.json") for k in ("elements", "apps", "surfaces", "functions")}

    def set_field(part, i, field, value):
        return lambda c: c[part][i].__setitem__(field, value)
    ra = next(i for i, e in enumerate(cat["elements"]) if e["kind"] == "app")
    mutations = [
        ("duplicate key", lambda c: c["functions"][1].__setitem__("key", c["functions"][0]["key"])),
        ("a foreign but issued first key", set_field("functions", 0, "first_line", "line:342795")),
        ("a false last key", set_field("functions", 0, "last_line", "line:27")),
        ("occurrences inflated", lambda c: c["functions"][0].__setitem__("lines", c["functions"][0]["lines"] + 100)),
        ("distinct lines changed", set_field("functions", 2, "distinct_lines", 1)),
        ("first key with a fake namespace", lambda c: c["functions"][0].__setitem__("first_line", "fake:" + c["functions"][0]["first_line"][5:])),
        ("function points at an unknown block", set_field("functions", 0, "block", "block:NOPE")),
        ("function description invented", set_field("functions", 0, "description", "invented")),
        ("function category invented", set_field("functions", 0, "category", "invented")),
        ("block_in_register inverted", lambda c: c["functions"][0].__setitem__("block_in_register", not c["functions"][0]["block_in_register"])),
        ("unknown family added", lambda c: c["functions"].append({**c["functions"][0], "key": "family:99999999"})),
        ("function dropped", lambda c: c["functions"].pop()),
        ("element lists family:0", set_field("elements", 0, "function_keys", ["family:0"])),
        ("element description changed", set_field("elements", 0, "description", "invented")),
        ("element depends_on invented", set_field("elements", 0, "depends_on", ["block:DOES-NOT-EXIST"])),
        ("element live invented", set_field("elements", 0, "live", ["https://example.invalid/"])),
        ("element files invented", set_field("elements", 0, "files", [{"repo": "example/invalid", "path": "invented.js", "commit": None}])),
        ("unknown block added", lambda c: c["elements"].append({**c["elements"][0], "key": "block:ZZZ"})),
        ("invented app prose", set_field("apps", 0, "description", "invented prose")),
        ("invented app title", set_field("apps", 0, "title", "invented title")),
        ("duplicate app with provenance count raised to match", lambda c: (c["apps"].append(c["apps"][0]), c.__setitem__("_apps_count", len(c["apps"])))),
        ("surface URL changed, key kept", set_field("surfaces", 0, "url", "https://example.invalid/")),
        ("surface description invented", set_field("surfaces", 0, "description", "invented")),
        ("surface key replaced by an unrelated URL", set_field("surfaces", 0, "key", "surface:https://example.test/other/")),
        ("fake key prefix", lambda c: c["surfaces"][0].__setitem__("key", "planet:" + c["surfaces"][0]["key"])),
        ("block_in_register True turned into 1", lambda c: c["functions"][0].__setitem__("block_in_register", int(c["functions"][0]["block_in_register"]))),
        ("standalone False turned into 0", lambda c: c["functions"][next(i for i, f in enumerate(c["functions"]) if f["standalone"] is False)].__setitem__("standalone", 0)),
        ("invented surface", lambda c: c["surfaces"].append({"key": "surface:https://example.invalid/", "url": "https://example.invalid/", "title": "x", "description": "x", "blocks": []})),
    ]
    prov_mutations = [
        ("families_total raised", lambda p: p["counts"].__setitem__("families_total", p["counts"]["families_total"] + 1)),
        ("numbered_lines raised", lambda p: p["counts"].__setitem__("numbered_lines", p["counts"]["numbered_lines"] + 1)),
        ("highest_line_key raised", lambda p: p["counts"].__setitem__("highest_line_key", p["counts"]["highest_line_key"] + 1)),
        ("register generated_utc changed", lambda p: p["register"].__setitem__("generated_utc", "2000-01-01T00:00:00Z")),
        ("register bytes changed", lambda p: p["register"].__setitem__("bytes", p["register"]["bytes"] + 1)),
    ]
    for name, mutate in mutations:
        broken = copy.deepcopy(cat)
        mutate(broken)
        if not problems(broken, prov, exp, keyset):
            sys.exit(f"a broken copy passed ({name}); the check proves nothing until it fails")
    for name, mutate in prov_mutations:
        broken_prov = copy.deepcopy(prov)
        mutate(broken_prov)
        if not problems(cat, broken_prov, exp, keyset):
            sys.exit(f"a broken provenance passed ({name}); the check proves nothing until it fails")
    print(f"{len(mutations) + len(prov_mutations)} broken copies each fail as required")

    bad = problems(cat, prov, exp, keyset)
    if bad:
        sys.exit("catalogue check FAILED:\n- " + "\n- ".join(bad[:40]))
    print(f"catalogue check PASS: complete rows equal the recomputed rows; {len(cat['elements'])} elements, "
          f"{len(cat['apps'])} apps, {len(cat['surfaces'])} surfaces, {len(cat['functions'])} functions")
    d = dangling
    print(f"disclosed, not failed: {d['references']} register references from {d['source_blocks']} blocks name "
          f"{len(d['distinct_targets'])} distinct targets absent from this register "
          f"(depends_on {d['by_field']['depends_on']}, used_by {d['by_field']['used_by']})")


if __name__ == "__main__":
    main()
