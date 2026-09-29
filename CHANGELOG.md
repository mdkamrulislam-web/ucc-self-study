# Changelog

Dated log of working sessions. Newest first. Each entry: what changed, why, and anything left unfinished.

## 2026-09-29 — Hosting live

- Created public repo `mdkamrulislam-web/ucc-self-study` via the GitHub web UI (files uploaded folder by folder).
- GitHub Pages enabled: deploy from branch `main`, folder `/ (root)`; custom domain `study.whoiskamrul.com` picked up from `CNAME`.
- Cloudflare DNS (zone whoiskamrul.com): added `CNAME study → mdkamrulislam-web.github.io`, **DNS only** (grey cloud) so GitHub can issue the HTTPS certificate. The apex whoiskamrul.com is a Cloudflare Worker (`portfolio`) and was left untouched.
- A local copy of the repo is also in Google Drive: `UCC/Self-Study/ucc-self-study/` (not a git clone; GitHub is the source of truth).
- HTTPS certificate issued and **Enforce HTTPS** turned on. Verified live: hub, all four module pages, `CLAUDE.md` and the 404 page load at https://study.whoiskamrul.com.

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
