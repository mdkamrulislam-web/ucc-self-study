# Changelog

Dated log of working sessions. Newest first. Each entry: what changed, why, and anything left unfinished.

## 2026-10-04 — EE6049: catch-up plan page

- Later update: Kamrul wants to watch his own lecture recordings as well as Razavi. Every day now pairs a Razavi lecture with timestamped segments of the 8 Sep–2 Oct recordings (taken from the captions), with each problem placed before the recording segment that solves it. Plan extended by a day to Wed 14 Oct (about 2.5 hours a day); Lab 1 day kept light; new purple "Lecture" chip; steps and intro reworded. Storage key moved to `ee6049-catchup-v3` because tasks changed places.

- **EE6049:** new page `ee6049/catch-up.html`, a 10-day plan (4–13 Oct) from Razavi *Electronics 1* Lec 29–30 to slide 178 (end of Section 11, common-gate). Each day lists the Razavi lecture with its start time and the asides to skip, the slide range, the matching guide lesson and the end-of-section problem; class and Lab 1 times are on their days. Ticks in `localStorage` (`ee6049-catchup-v2`).
- Built from a read of the slides v1.1 (580 slides, 27 sections), the EE6049 captions for lectures 1–8, the EE4022 captions for lectures 10–12 and the Razavi Lec 29–45 transcripts in Drive. The Razavi-to-section map is in `ee6049/NOTES.md`.
- Kept separate from `ee6049/index.html` so an artifact re-import can't drop it. Hub: one link line under the Semester 1 cards (no change to lesson counts or stats).
- Left for later: guide lessons for Sections 9–11 (the plan's last three days use the captions instead).
- Same day, update: added the newly shared resources. Each problem now names its solution PDF (62 covers 63, 81 covers 81–83; none yet for 178), and the whiteboard handouts sit on their days (FET types, 2nd order effects, diode load, receiver line-up, common-mode problem, source follower). From the lab manual and worksheet: Thursday now has Lab 1 prep (slide 111, slides 295–297 and 304–315 for the pole and zero, the manual's Lab 1 chapter and the EDA quick start) and the circuit values; problems 81–83 moved from Wednesday to Friday; Monday 12 gained the 2 Oct common-mode section. New "The three labs" panel (Lab 3 needs Sections 19–21, likely ahead of the lectures). Ticks kept (same storage key).

## 2026-10-01 — CS1068: coverage re-check against all course material

- Re-read every slide of lectures 0.1–3.1 (text and slide images), both lab sheets, both practice sheets, Quizzes 2–3, the Canvas notices and all four past papers (the "Question Papers – Booklet" is the same four papers), and compared them with the guide.
- **CS1068:** added what was missing, no new lessons (still 15):
  - Start page: "How the lecturer wants you to learn" (the Golden Rule, the module goal, Phase 1, tips for success, the textbook, software, academic integrity and GenAI declarations).
  - Lesson 1: Lecture 0.2's sum-of-two-numbers algorithm; machine, assembly and high-level languages with the history list; why Python and the Python vs Java slide; pseudocode and flowchart definitions; the Gale–Shapley 4×4 example traced day by day (boys first and girls first) and the 3×3 lecture exercise in Check yourself. Answers verified with a script.
  - Lesson 2: Lecture 1.1's `average.py` with input; three kinds of error (syntax, runtime, logic).
  - Lesson 7: the Employee input example (2.1 slide 10). Lesson 10: "boolean expression".
  - Lesson 11: the Lecture 3.1 review chain (credit hours → student type) with a flowchart.
  - Lesson 13: slide 7's `add()` example, including the slide's own bug (prints `num1` twice), and Lecture 2.2 slide 22's plan-as-a-comment turned into Temp.py with the warnings. Lesson 15: slide 18's docstring template.
  - Cheat sheet: error kinds, boolean expression.
- `tools/check_examples.py`: 66 examples, all match. Phone widths 320/375/414 px have no page overflow; the new two-column tables wrap instead of scrolling.

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
