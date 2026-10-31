#!/usr/bin/env python3
"""Regenerate the markdown exports from index.html. Never edit exports/ by hand.
Usage: python tools/export.py   (needs Node.js)"""
from _data import load, ROOT

d, _ = load()
out = ROOT / "exports"; out.mkdir(exist_ok=True)
L = "ABCD"
QD = d["QDOMAINS"]

lines = ["# Question bank", "", "Generated from `index.html` by `tools/export.py`. Do not edit by hand.", ""]
for key, dom in QD.items():
    qs = [q for q in d["QUESTIONS"] if q["d"] == key]
    if not qs: continue
    lines += [f"## {dom['name']} ({len(qs)})", ""]
    for i, q in enumerate(qs, 1):
        lines.append(f"**{i}. {q['q']}**  ")
        lines += [f"{L[j]}. {o}  " for j, o in enumerate(q["o"])]
        lines += [f"*Answer: {L[q['a']]}. {q['e']}*", ""]
(out / "question-bank.md").write_text("\n".join(lines), encoding="utf-8")

lines = ["# Flashcards", "", "Generated from `index.html`. Do not edit by hand.", ""]
for key, dom in QD.items():
    cs = [c for c in d["CARDS"] if c["d"] == key]
    if not cs: continue
    lines += [f"## {dom['name']}", ""] + [f"- **{c['t']}**: {c['x']}" for c in cs] + [""]
(out / "flashcards.md").write_text("\n".join(lines), encoding="utf-8")

lines = ["# Interview prompts", "", "Generated from `index.html`. Do not edit by hand.", ""]
for key, dom in d["DOMAINS"].items():
    lines += [f"## {dom['name']}", ""] + [f"- {p['q']}" for p in d["PROMPTS"] if p["d"] == key] + [""]
(out / "interview-prompts.md").write_text("\n".join(lines), encoding="utf-8")

lines = ["# 24-week plan", "", "Generated from `index.html`. Do not edit by hand.", ""]
for i, w in enumerate(d["WEEKS"], 1):
    lines += [f"**Week {i}**"] + [f"- {t}" for t in w] + [""]
(out / "24-week-plan.md").write_text("\n".join(lines), encoding="utf-8")
print("Exports written to exports/")
