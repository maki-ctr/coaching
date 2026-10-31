"""Shared helper: read the data arrays out of index.html (the single source of truth)."""
import json, pathlib, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent

def load():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    scripts = re.findall(r"<script>([\s\S]*?)</script>", html)
    data_js = next(s for s in scripts if "const QUESTIONS" in s)
    js = data_js + "\nprocess.stdout.write(JSON.stringify({CONFIG,QUESTIONS,CARDS,PROMPTS,DIAGRAMS,MODULES,DOMAINS,QDOMAINS,WEEKS}));"
    out = subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout
    return json.loads(out), scripts
