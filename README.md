# Coaching License Lab

A single-page study and evidence tool for the U.S. Soccer coaching pathway, built for Freddy Adu: B License through the former-player waiver, then the A License.

The B is assessed on real coaching, not a written exam, so the tool centres on building evidence (game model, session plans, game plans, player plans, video reviews, portfolio), with a knowledge bank, flashcards and interview practice in support.

## What's in it

| Area | Pages |
|---|---|
| Course | Dashboard with the route drawn on a pitch, Route to the A, 24-week plan |
| Learn | 8 course modules (video slot, key points, diagrams), diagram gallery with lightbox |
| Build | Game model builder with a two-minute pitch, session planner, game day (half-time timer, review to next session), player plans |
| Practise | Video review logger and rubric, interview prep with timer, 60 knowledge questions, 36 flashcards |
| Prove | Portfolio by competency, feeding the readiness score on the dashboard |

All data saves in the browser (localStorage). Settings has export, import and reset.

## Repository layout

```
index.html            The app. Single source of truth for all questions, cards, prompts and plans.
images/               11 diagrams, 1600x900 PNG, rendered from diagrams-src/
diagrams-src/         Diagram sources (HTML + SVG) and the Barlow fonts (OFL)
video-scripts/        8 NotebookLM scripts (plain prose) and PRODUCTION.md (prompts, checklists)
exports/              Markdown exports generated from index.html. Don't edit by hand.
tools/check.py        Regression checks
tools/export.py       Regenerates exports/
tools/render_images.py Renders diagrams-src/ to images/ and fails on text overflow
UNCONFIRMED.md        What still needs checking against official U.S. Soccer documents
```

## Publish on GitHub Pages

1. Create a repository and push these files to `main`.
2. Settings → Pages → Deploy from a branch → `main` / root.
3. Custom domain: the `CNAME` file already contains `coaching.malickmanso.com`. At your DNS provider, add a `CNAME` record for `coaching` pointing to `<your-github-username>.github.io`. In Settings → Pages, confirm the custom domain shows, wait for the DNS check to pass, then tick "Enforce HTTPS".

## Personalise

Edit the `CONFIG` block at the top of the first `<script>` in `index.html`:

```js
coachName: "Freddy Adu",
aTrack: "Senior",            // or "Youth"
courseStart: "2027-01-11",   // first Monday of the B course
team: "Harbor FC U17",
videos: {1:"", 2:"", ...}    // YouTube IDs once videos are approved
```

The coach can also change name, track, start date and theme in the app's Settings. Demo content (game model, a session, two player plans, a video review) is seed data in `SEED`; Settings → "Reset to demo data" restores it.

## Videos

Scripts are in `video-scripts/`. Follow `video-scripts/PRODUCTION.md`: one notebook per video, the script as the main source, watch and transcript checks against the "Must hear" and "Reject if" lists, upload as **Unlisted**, then add the ID to `CONFIG.videos`.

## After every change

```bash
python tools/check.py           # syntax, question bank balance, images, video slots (needs Node.js)
python tools/export.py          # regenerate exports/
python tools/render_images.py   # only if a diagram changed (needs: pip install playwright && playwright install chromium)
```

Then open `index.html` at phone and desktop widths before pushing.

## Ground rules carried over from the PRINCE2 build

- Official documents are the referee. When the B Course Guide and rubric arrive, check content against them and update `UNCONFIRMED.md`.
- Correct answers are balanced across positions in storage, and options are shuffled at display (except order-dependent sets marked `fx:1`).
- Never bulk-replace a domain term; change each instance in context.
- Diagrams are drawn with code so every label is exact, and they all use the same Harbor FC scenario and numbers.
