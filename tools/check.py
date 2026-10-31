#!/usr/bin/env python3
"""Regression checks. Run after every change:  python tools/check.py   (needs Node.js)"""
import collections, pathlib, re, subprocess, sys
from _data import load, ROOT

fails = []
def check(ok, msg):
    print(("ok   " if ok else "FAIL ") + msg)
    if not ok: fails.append(msg)

d, scripts = load()

# 1. JavaScript syntax of every script block
for i, s in enumerate(scripts):
    r = subprocess.run(["node", "--check", "-"], input=s, capture_output=True, text=True)
    check(r.returncode == 0, f"script block {i+1} parses" + ("" if r.returncode == 0 else ": " + r.stderr.strip()[:200]))

Q = d["QUESTIONS"]
check(len(Q) >= 60, f"{len(Q)} questions present")
check(all(0 <= q["a"] < len(q["o"]) for q in Q), "every answer index points to an option")
check(all(len(set(q["o"])) == len(q["o"]) for q in Q), "no duplicate options within a question")
check(all(q["d"] in d["QDOMAINS"] for q in Q), "every question has a valid domain")

# 2. Answer-position balance (stored order). The app also shuffles options at display.
cnt = collections.Counter(q["a"] for q in Q)
spread = max(cnt.values()) - min(cnt.values())
check(spread <= 3, f"answer positions balanced {dict(sorted(cnt.items()))}")
run = mx = 1
for a, b in zip(Q, Q[1:]):
    run = run + 1 if a["a"] == b["a"] else 1; mx = max(mx, run)
check(mx <= 3, f"longest same-position run is {mx}")
letter_refs = [q["q"][:40] for q in Q if re.search(r"\b(option|answer) [A-D]\b|\(([a-d])\)", q["e"])]
check(not letter_refs, "no explanation refers to options by letter")

# 3. Content counts
check(len(d["CARDS"]) >= 30, f"{len(d['CARDS'])} flashcards")
check(len(d["PROMPTS"]) >= 25, f"{len(d['PROMPTS'])} interview prompts")
check(len(d["WEEKS"]) == 24 and all(len(w) == 3 for w in d["WEEKS"]), "24 weeks with 3 tasks each")

# 4. Diagrams and modules
for g in d["DIAGRAMS"]:
    check((ROOT / "images" / f"{g['id']}.png").exists(), f"image exists: {g['id']}.png")
    check((ROOT / "diagrams-src" / f"{g['id']}.html").exists(), f"diagram source exists: {g['id']}.html")
mods = {m["n"] for m in d["MODULES"]}
check(all(g["mod"] in mods for g in d["DIAGRAMS"]), "every diagram belongs to a module")
check(all(str(m) in d["CONFIG"]["videos"] for m in mods), "every module has a video slot in CONFIG.videos")
for m in sorted(mods):
    check(any((ROOT / "video-scripts").glob(f"{m:02d}-*.txt")), f"video script exists for module {m}")

print("\n" + ("All checks passed." if not fails else f"{len(fails)} check(s) failed."))
sys.exit(1 if fails else 0)
