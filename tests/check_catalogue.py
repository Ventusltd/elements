#!/usr/bin/env python3
"""Fail-closed checks of the committed catalogue against its pinned inputs.

Run from the repository root:  python tests/check_catalogue.py
Each check is shown failing on a broken copy before the real catalogue is allowed to pass:
a duplicated key, a function of 10 lines, and a line key the database does not hold.
"""
import copy, hashlib, json, struct, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
load = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))


def checks(cat, prov, register, families, keyset):
    out = []
    add = lambda name, ok: out.append((name, bool(ok)))
    keys = [x["key"] for x in cat["elements"]] + [x["key"] for x in cat["functions"]] + [x["key"] for x in cat["surfaces"]]
    add("every key in the catalogue is unique", len(keys) == len(set(keys)))
    add("every register block is an element", {f"block:{b['symbol']}" for b in register["blocks"]} == {e["key"] for e in cat["elements"]})
    add("apps are exactly the blocks of kind app", {e["key"] for e in cat["elements"] if e["kind"] == "app"} == {a["key"] for a in cat["apps"]})
    want = {f"family:{f['n']}" for f in families if f["lineCount"] > 10}
    add("functions are exactly the families with more than 10 lines", want == {f["key"] for f in cat["functions"]})
    add("no catalogued function has 10 lines or fewer", all(f["lines"] > 10 for f in cat["functions"]))
    add("every first and last line key exists in the numbered database",
        all(int(f["first_line"][5:]) in keyset and int(f["last_line"][5:]) in keyset for f in cat["functions"]))
    add("provenance counts equal the catalogue", prov["counts"]["elements"] == len(cat["elements"])
        and prov["counts"]["functions_over_10_lines"] == len(cat["functions"]) and prov["counts"]["apps"] == len(cat["apps"])
        and prov["counts"]["surfaces"] == len(cat["surfaces"]))
    return out


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
    b = pack["all-lines.bin"]
    keyset = set(struct.unpack(f"<{len(b)//4}I", b))
    families = json.loads(pack["families.json"])
    cat = {k: load(f"catalogue/{k}.json") for k in ("elements", "apps", "surfaces", "functions")}

    broken = copy.deepcopy(cat)
    broken["functions"][1]["key"] = broken["functions"][0]["key"]
    broken["functions"][2]["lines"] = 10
    broken["functions"][3]["first_line"] = "line:999999999"
    failed = [n for n, ok in checks(broken, prov, register, families, keyset) if not ok]
    must = {"every key in the catalogue is unique", "no catalogued function has 10 lines or fewer",
            "every first and last line key exists in the numbered database"}
    if not must <= set(failed):
        sys.exit(f"the broken fixture did not fail the checks it must: failed only {failed}")
    print(f"broken fixture fails as required: {len(failed)} checks")

    res = checks(cat, prov, register, families, keyset)
    bad = [n for n, ok in res if not ok]
    if bad:
        sys.exit("catalogue check FAILED:\n- " + "\n- ".join(bad))
    print(f"catalogue check PASS: {len(res)} checks · {len(cat['elements'])} elements · {len(cat['apps'])} apps · "
          f"{len(cat['surfaces'])} surfaces · {len(cat['functions'])} functions")


if __name__ == "__main__":
    main()
