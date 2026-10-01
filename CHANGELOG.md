# Changelog

Dated log of working sessions. Newest first. Each entry: what changed, why, and anything left unfinished.

## 2026-10-01 — CS1068 Introductory Programming in Python added

- New module, set up from a Claude Code session in the CS1068 project; source material was the project's shared files (slides 0.1–3.1, lab and practice sheets, Quizzes 2–3, Canvas notices, Winter 2022–23 to 2025–26 papers).
- **CS1068:** new guide `cs1068/index.html`, 15 lessons (problem → program, first program, variables, types, operators, casting, input, print, f-strings, if, elif, nested/and-or-not, defining functions, return vs print, docstrings and built-ins), plus a Python playground, Quizzes 2–3 explained, labs and deadlines (no answers), exam practice (four past-paper Q1 openers with solutions, three exam-style questions), still to come and a cheat sheet. Progress key `cs1068-guide-done-v1` (`l1`–`l15`).
- Every example runs in the browser through Pyodide 0.26.4 (CDN, loaded on first use). Added `tools/check_examples.py`, which runs every example in Python and checks the output shown on the page (59 examples, all match).
- Hub: CS1068 card; stats 5 guides, 93 lessons, 5 modules. README, CLAUDE.md, PROJECT_STATUS, `cs1068/NOTES.md` updated.
- Held back: 2025–26 Q1(iii) overlaps Practice 3 (due 7 Oct); add it after that date.

## 2026-09-30 — Sync: CS6322 notes 8, EE6041 sections 32–34 pushed

- Found the updates in Drive `UCC/SEMESTER-1/COURSES/<module>/Claude outputs/`, not in the artifacts (all four artifacts were unchanged), so the first check of the day missed them.
- **EE6041:** applied the learning project's commit (bundle/patch `ee6041-sections-32-34`), see the entry below.
- **CS6322:** 15 → 18 lessons from notes 8 (16 Branch and bound · 17 Greedy algorithms · 18 Dynamic programming). Imported the Drive `Claude outputs/index.html` with `tools/import_guide.py`. Keys `l16`–`l18` share `cs6322-done`.
- Hub: CS6322 card 18 lessons, notes 1–8; stats 78 lessons. README, CLAUDE.md, PROJECT_STATUS, `cs6322/NOTES.md` updated.
- **Sync rule change:** check each module's Drive `Claude outputs/` folder as well as its artifact; the newer one wins. EE6049 and EE6043 had nothing new.

## 2026-09-30 — EE6041: lectures of 29 and 30 September

- **EE6041:** 31 → 34 sections, written straight into `ee6041/index.html` (the guide is no longer edited as an artifact, so it must not be re-synced from one).
  - 32 A double pole: the step convolved with itself, (z/(z−1))² ↔ (n+1)u(n).
  - 33 The system function: H(z) from a difference equation and back (Z slides 24–28, the 30 Sep board example).
  - 34 The unit circle as the stability boundary (Z slides 29–36), with a "move the pole" demo and the s-plane link z = e^{sT}.
  - Notes from the two lectures added to sections 30 and 31; cheat sheet, traps, "still to come", hero and module overview updated; tick keys `z13`–`z15` added.
- Hub: EE6041 card 34 sections, 8–30 Sep; stats 75 lessons. README, CLAUDE.md (EE6041 keys and edit-here rule), NOTES.md, PROJECT_STATUS updated.

## 2026-09-30 — First sync

- Checked all four artifacts against the repo. Synced three; CS6322 unchanged (version 28 Sep).
- **EE6049:** 11 → 13 lessons (lectures 1–6; new: CMOS inverter amplifier, two-port shortcut; 12 practice problems).
- **EE6043:** new guide replaces the placeholder — 13 lessons, lectures 1–3; progress key `ee6043-guide-done-v1`.
- **EE6041:** 19 → 31 sections (added z-transform, lectures of 22 and 23 Sep, plus an Assignment 1 section); renamed "Advanced Signal Processing". New keys `z1`–`z12` share the existing storage key.
- Hub: EE6043 card now live with a progress bar; card counts and descriptions updated; stats now 4 guides, 72 lessons.
- NOTES.md for the three modules, README and PROJECT_STATUS updated.

## 2026-09-29 — Sync workflow agreed

- Decision: guides stay in their learning projects; the site is updated on request ("sync the website"). Steps documented in `CLAUDE.md`. Later: connect the repo to a Claude Code session for direct pushes.

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
