# Changelog

Dated log of working sessions. Newest first. Each entry: what changed, why, and anything left unfinished.

## 2026-09-29 — Project set up

- Created the repo and the static site structure (`index.html` hub + one folder per module).
- Imported three existing guides from their Claude artifacts:
  - EE6049 Design of Analogue ICs (artifact version of 24 Sep; 11 lessons, lectures 1–5)
  - EE6041 Advanced DSP (24 Sep; 19 sections, lectures of 8, 9, 15 Sep)
  - CS6322 Optimisation (28 Sep; 15 lessons, notes 1–7)
- Added `tools/import_guide.py` (adds `noindex`, head `<title>`, "← Study hub" link; idempotent).
- EE6043 Design of Digital ICs: placeholder page, as no guide exists yet.
- Hub styled after the whoiskamrul.com "Amber IC" look; progress bars read each guide's `localStorage` ticks.
- `CNAME` set to `study.whoiskamrul.com`; `robots.txt` + `noindex` keep the site out of search engines.
- Tracking docs added: `README.md`, `CLAUDE.md`, `PROJECT_STATUS.md`, this file, per-module `NOTES.md`.
- **Unfinished at time of writing:** GitHub Pages and DNS setup (see the next entry once done).
