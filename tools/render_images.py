#!/usr/bin/env python3
"""Render every diagram in diagrams-src/ to images/<name>.png at 1600x900.

Diagrams are drawn with HTML and SVG so every label is exact text.
The script also fails if any text overflows its box or the canvas.

Usage:  pip install playwright && playwright install chromium
        python tools/render_images.py            # all diagrams
        python tools/render_images.py game-model # one diagram
"""
import asyncio, pathlib, sys
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "diagrams-src", ROOT / "images"

CHECK = """() => {
  const probs = [];
  const de = document.documentElement;
  if (de.scrollWidth > 1600 || de.scrollHeight > 900) probs.push(`canvas ${de.scrollWidth}x${de.scrollHeight}`);
  const w = document.querySelector('.watch');
  if (w && w.getBoundingClientRect().bottom > 901) probs.push('watch strip pushed below the canvas');
  document.querySelectorAll('.box, .watch .items div, .hd p').forEach((el, i) => {
    if (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1)
      probs.push(`overflow in ${el.className || el.tagName} #${i}: "${el.textContent.trim().slice(0, 50)}"`);
  });
  return probs;
}"""

async def main(only):
    OUT.mkdir(exist_ok=True)
    files = sorted(p for p in SRC.glob("*.html") if not only or p.stem in only)
    bad = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1600, "height": 900})
        for f in files:
            await page.goto(f.as_uri())
            await page.evaluate("document.fonts.ready")
            await page.wait_for_timeout(150)
            probs = await page.evaluate(CHECK)
            await page.screenshot(path=str(OUT / f"{f.stem}.png"))
            print(("FAIL " if probs else "ok   ") + f.stem + ("".join("\n     - " + x for x in probs)))
            bad += bool(probs)
        await browser.close()
    sys.exit(1 if bad else 0)

asyncio.run(main(set(sys.argv[1:])))
