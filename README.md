# UCC MEngSc Study Hub

Plain-English, lesson-by-lesson study guides for my MEngSc in Electrical & Electronic Engineering at University College Cork (2026–27), published as a static website.

**Live site:** https://study.whoiskamrul.com (GitHub Pages, custom subdomain of whoiskamrul.com)

| Module | Title | Guide | Status |
|---|---|---|---|
| EE6049 | Design of Analogue ICs | [`ee6049/`](ee6049/) | Live · lectures 1–5 |
| EE6043 | Design of Digital ICs | [`ee6043/`](ee6043/) | Placeholder |
| EE6041 | Advanced DSP | [`ee6041/`](ee6041/) | Live · lectures of 8, 9, 15 Sep |
| CS6322 | Optimisation | [`cs6322/`](cs6322/) | Live · notes 1–7 |

## Start here (continuing on another computer or Claude account)

1. Read **[`CLAUDE.md`](CLAUDE.md)** — context and working rules for whoever (or whichever Claude) picks this up.
2. Read **[`PROJECT_STATUS.md`](PROJECT_STATUS.md)** — what's done, what's next, open decisions.
3. Skim **[`CHANGELOG.md`](CHANGELOG.md)** — a dated log of every working session.
4. Each module folder has a **`NOTES.md`** with coverage, sources and the to-do list for that guide.

## Repository layout

```
index.html            Hub page (module cards, progress bars, semester 2 plan)
ee6049/index.html     EE6049 guide (self-contained HTML)
ee6049/NOTES.md       Tracking notes for that guide
ee6041/  cs6322/      Same pattern
ee6043/index.html     "Coming soon" placeholder
tools/import_guide.py Prepares a guide HTML for the site (noindex, <title>, hub link)
CNAME                 Custom domain for GitHub Pages
.nojekyll             Serve files as-is (no Jekyll build)
robots.txt, 404.html  Keep out of search engines; friendly not-found page
```

## Run locally

Every page is plain HTML with inline CSS/JS (only Google Fonts load from outside).

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```

## Updating a guide

See the "Update a guide" workflow in [`CLAUDE.md`](CLAUDE.md). In short: edit `<module>/index.html`, run `python3 tools/import_guide.py <file> <module>` if it came fresh from a Claude artifact, update that module's `NOTES.md`, `PROJECT_STATUS.md` and `CHANGELOG.md`, then commit and push. GitHub Pages redeploys automatically within a minute or two.

---
Personal study notes, not official UCC material.
