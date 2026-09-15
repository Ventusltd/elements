#!/usr/bin/env python3
"""Checks of the committed catalogue against its pinned inputs.

Run from the repository root:  python tests/check_catalogue.py

What this proves, and only this: every entry in catalogue/*.json equals what this
file recomputes, independently of the builder, from the pinned register copy and
the pinned numbered database. It recomputes each function's key, name, kind, line
occurrences, distinct lines, sequence start and end keys and block from
families.json and lines.bin; each element's title, description, kind, category and
function keys from the register; the apps as the blocks of kind app; the surfaces
from the register's live addresses. Missing entries, extra entries and any changed
field fail.

It does not prove the sources are right, that descriptions are complete, or that a
function runs.

Before the real catalogue may pass, twenty deliberately broken copies must each
fail, including every corruption a peer review showed the earlier seven-check
version let through.
"""
import copy, hashlib, json, struct, sys, urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
load = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))


def expected(register, families, fam_lines):
    blocks = register["blocks"]
    exp_f = {}
    for fam in families:
        if fam["lineCount"] <= 10:
            continue
        seq = fam_lines[fam["lineOffset"]: fam["lineOffset"] + fam["lineCount"]]
        exp_f[f"family:{fam['n']}"] = {
            "name": fam.get("name"), "kind": fam["kind"], "lines": fam["lineCount"], "distinct_lines": len(set(seq)),
            "first_line": f"line:{seq[0]}", "last_line": f"line:{seq[-1]}", "block": f"block:{fam['block']}",
        }
    exp_e = {f"block:{b['symbol']}": {
        "title": b["title"], "kind": b["kind"], "category": b["category"],
        "description": b.get("description") or "description not yet written",
        "function_keys": [f"family:{x['family']}" for x in b.get("inside") or []],
    } for b in blocks}
    exp_apps = sorted(f"block:{b['symbol']}" for b in blocks if b["kind"] == "app")
    surf = defaultdict(set)
    for b in blocks:
        for u in b.get("live") or []:
            surf[u.rsplit("/", 1)[0] + "/"].add(f"block:{b['symbol']}")
    exp_s = {f"surface:{u}": sorted(v) for u, v in surf.items()}
    return exp_f, exp_e, exp_apps, exp_s


def problems(cat, prov, exp, keyset):
    exp_f, exp_e, exp_apps, exp_s = exp
    bad = []
    keys = [x["key"] for x in cat["elements"]] + [x["key"] for x in cat["functions"]] + [x["key"] for x in cat["surfaces"]]
    if len(keys) != len(set(keys)):
        bad.append("a key appears more than once")
    for x in keys:
        if not (x.startswith("block:") or x.startswith("family:") or x.startswith("surface:")):
            bad.append(f"unknown key prefix: {x}")
    got_f = {f["key"]: f for f in cat["functions"]}
    if set(got_f) != set(exp_f):
        bad.append(f"function keys differ: {len(set(got_f) - set(exp_f))} extra, {len(set(exp_f) - set(got_f))} missing")
    for k, e in exp_f.items():
        g = got_f.get(k)
        if not g:
            continue
        for field, want in e.items():
            if g.get(field) != want:
                bad.append(f"{k}.{field} is {g.get(field)!r}, recomputed {want!r}")
    got_e = {e["key"]: e for e in cat["elements"]}
    if set(got_e) != set(exp_e):
        bad.append(f"element keys differ: {len(set(got_e) - set(exp_e))} extra, {len(set(exp_e) - set(got_e))} missing")
    for k, e in exp_e.items():
        g = got_e.get(k)
        if g:
            for field, want in e.items():
                if g.get(field) != want:
                    bad.append(f"{k}.{field} differs from the register")
    got_apps = [a["key"] for a in cat["apps"]]
    if sorted(got_apps) != exp_apps:
        bad.append(f"apps are {sorted(got_apps)}, register kind app gives {exp_apps}")
    for a in cat["apps"]:
        if a != got_e.get(a["key"]):
            bad.append(f"app {a['key']} differs from its element entry")
    got_s = {s["key"]: sorted(s["blocks"]) for s in cat["surfaces"]}
    if got_s != exp_s:
        bad.append(f"surfaces differ: {len(set(got_s) - set(exp_s))} extra, {len(set(exp_s) - set(got_s))} missing, or blocks changed")
    c = dict(prov["counts"])
    if "_apps_count" in cat:   # a mutated copy whose provenance app count was raised to match
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
    exp = expected(register, json.loads(pack["families.json"]), u32(pack["lines.bin"]))
    cat = {k: load(f"catalogue/{k}.json") for k in ("elements", "apps", "surfaces", "functions")}

    f0 = cat["functions"][0]
    other_key = next(k for k in sorted(keyset) if f"line:{k}" != f0["first_line"])
    mutations = [
        ("duplicate key", lambda c: c["functions"][1].__setitem__("key", c["functions"][0]["key"])),
        ("first line replaced by another issued key", lambda c: c["functions"][0].__setitem__("first_line", f"line:{other_key}")),
        ("line count changed", lambda c: c["functions"][2].__setitem__("lines", c["functions"][2]["lines"] + 1)),
        ("distinct line count changed", lambda c: c["functions"][2].__setitem__("distinct_lines", 1)),
        ("fake key prefix", lambda c: c["surfaces"][0].__setitem__("key", "planet:" + c["surfaces"][0]["key"])),
        ("invented surface", lambda c: c["surfaces"].append({"key": "surface:https://example.invalid/", "blocks": []})),
        ("unknown family added", lambda c: c["functions"].append({**c["functions"][0], "key": "family:99999999"})),
        ("unknown block added", lambda c: c["elements"].append({**c["elements"][0], "key": "block:ZZZ"})),
        ("duplicate app with matching tally", lambda c: c["apps"].__setitem__(1, c["apps"][0])),
        ("function dropped with matching tally", lambda c: (c["functions"].pop(), None)),
        ("element description changed", lambda c: c["elements"][0].__setitem__("description", "invented")),
        # the exact cases a peer review found passing the earlier seven checks
        ("a foreign but issued first key", lambda c: c["functions"][0].__setitem__("first_line", "line:342795")),
        ("a false last key", lambda c: c["functions"][0].__setitem__("last_line", "line:27")),
        ("occurrences inflated", lambda c: c["functions"][0].__setitem__("lines", c["functions"][0]["lines"] + 100)),
        ("first key with a fake namespace", lambda c: c["functions"][0].__setitem__("first_line", "fake:" + c["functions"][0]["first_line"][5:])),
        ("function points at an unknown block", lambda c: c["functions"][0].__setitem__("block", "block:NOPE")),
        ("element lists family:0", lambda c: c["elements"][0].__setitem__("function_keys", ["family:0"])),
        ("surface key replaced by an unrelated URL", lambda c: c["surfaces"][0].__setitem__("key", "surface:https://example.test/other/")),
        ("invented app prose", lambda c: c["apps"][0].__setitem__("description", "invented prose")),
        ("duplicate app with provenance count raised to match", lambda c: (c["apps"].append(c["apps"][0]), c.__setitem__("_apps_count", len(c["apps"])))),
    ]
    for name, mutate in mutations:
        broken = copy.deepcopy(cat)
        mutate(broken)
        if not problems(broken, prov, exp, keyset):
            sys.exit(f"a broken copy passed ({name}); the check proves nothing until it fails")
    print(f"{len(mutations)} broken copies each fail as required")

    bad = problems(cat, prov, exp, keyset)
    if bad:
        sys.exit("catalogue check FAILED:\n- " + "\n- ".join(bad[:40]))
    print(f"catalogue check PASS: every field recomputed from the pinned inputs; {len(cat['elements'])} elements, "
          f"{len(cat['apps'])} apps, {len(cat['surfaces'])} surfaces, {len(cat['functions'])} functions")


if __name__ == "__main__":
    main()
