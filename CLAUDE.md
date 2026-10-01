# CLAUDE.md — handoff for any session continuing this project

This file is for Claude (any account, any surface) or any person picking the project up. Read it fully, then `PROJECT_STATUS.md`, then the latest entries in `CHANGELOG.md`, before changing anything.

## What this project is

A static website of self-study guides for Kamrul's (Shuvo's) MEngSc in Electrical & Electronic Engineering at University College Cork, 2026–27. Each module gets one long, self-contained HTML guide written lesson by lesson as lectures happen. A hub page (`index.html`) links them.

- **Repo:** `github.com/mdkamrulislam-web/ucc-self-study` (public)
- **Hosting:** GitHub Pages from `main` / root, custom domain `study.whoiskamrul.com` (see `CNAME`)
- **DNS:** a `CNAME` record `study` → `mdkamrulislam-web.github.io` at the whoiskamrul.com DNS provider
- **Owner's portfolio:** whoiskamrul.com (the hub borrows its "Amber IC" look: amber/teal on near-black, Bebas Neue / Barlow / Fira Code)

## Source of truth

**The HTML in this repo is the source of truth.** The guides were first written as private Claude artifacts on Kamrul's main account (links in each `NOTES.md`). Those links only open for that account, so:

- If you *can* open the artifact and it is newer than the repo copy, download it and re-import it (workflow below).
- Otherwise edit the repo HTML directly. Don't rebuild a guide from scratch.
- After editing a guide in the repo, if you're on the main account you may republish it to its artifact so both match, but that's optional.
- **EE6041 is edited here directly (from 30 Sep 2026).** Its artifact is no longer updated and is older than the repo copy, so never sync or re-import EE6041 from the artifact.
- **CS1068 has no artifact: it was created in this repo (1 Oct 2026) and is only edited here.** Skip it when syncing. After editing it, run `python3 tools/check_examples.py cs1068/index.html` (see `cs1068/NOTES.md`).

## Writing and style rules (from Kamrul)

- **British English** throughout (optimisation, analogue, colour, modelling, behaviour).
- Guides are plain-English, **one idea per lesson**: each lesson opens with a highlighted "one idea" box, then builds the maths slowly, cites slide/note numbers, has worked examples, "check yourself" questions, and an exam-angle note.
- Each guide ends with past-paper / exam-style practice (solutions behind `<details>`), and a one-page cheat sheet.
- Progress ticks use `localStorage`; the hub reads them. Keep each guide's key stable:
  - EE6049 → `ee6049-guide-done-v1` (keys `l1`…`l13`)
  - EE6043 → `ee6043-guide-done-v1` (keys `l1`…`l13`)
  - EE6041 → `ee6041-lti-progress-v1` (keys `s1`…`s19`, `z1`…`z15`)
  - CS6322 → `cs6322-done` (keys `l1`…`l18`)
  - CS1068 → `cs1068-guide-done-v1` (keys `l1`…`l15`)
  If you add lessons, update `data-total` on that module's card in `index.html`.
- Labs: CS6322's lecturer asks that GenAI is not used for lab answers. Guides may explain ideas and check models, but never publish full lab solutions.
- CS1068 is stricter: in "Phase 1" students must not use AI to generate solutions, and GenAI is banned for the mid-term quiz and the programming assignment. Never put lab, practice-sheet, quiz or assignment answers in the guide, and hold back past-paper questions that overlap an open practice sheet until it closes.
- Don't put personal details (phone, email, student number, addresses) anywhere in this public repo.
- When showing code changes to Kamrul, show only the relevant changes and say where they go.

## Workflows

### Update a guide after new lectures
1. Get the new lecture slides/notes from Kamrul (they live in his Google Drive under `UCC/SEMESTER-1/...`).
2. Edit `<module>/index.html`: add lesson sections in the same markup pattern as existing ones, add them to the side rail/TOC, update the lesson counter total inside the guide.
3. Update the hub card in `index.html` (lesson count, coverage line, `data-total`) and the stats row (total lessons).
4. Update `<module>/NOTES.md` (coverage table, to-do), `PROJECT_STATUS.md`, and add a dated entry to `CHANGELOG.md`.
5. Test locally (`python3 -m http.server`), then commit and push to `main`.

### "Sync the website" (agreed workflow, 29 Sep 2026)
Guides are still edited in their own learning projects as Claude artifacts; the site does **not** update automatically. When Kamrul says "sync the website":
1. For each module, check **both** its artifact (URL in `<module>/NOTES.md`) **and** Drive `UCC/SEMESTER-1/COURSES/<module folder>/Claude outputs/` (a full `index.html`, or a git `.patch`/`.bundle` against this repo). Use whichever is newer; skip unchanged modules.
2. Save the new HTML and run `python3 tools/import_guide.py raw.html <module>`.
3. If lessons were added: update that card in `index.html` (`data-total`, lesson count, coverage line) and the hero "Lessons" stat.
4. Update `<module>/NOTES.md`, `PROJECT_STATUS.md`, `CHANGELOG.md`.
5. Push to `main`. With git access, just push. Without it (Cowork session), write the files to Drive `UCC/Self-Study/ucc-self-study/`, stage them, and upload through github.com → *Add file → Upload files* in Chrome, one folder per upload (scroll to the bottom and click **Commit changes** by coordinates; the ref-based click doesn't always submit).
6. Check https://study.whoiskamrul.com/<module>/ loads the new version.

Planned later: connect this repo to a Claude Code session so step 5 is a plain `git push`.

### Import a guide that was edited as a Claude artifact
```bash
# save the artifact's full HTML as raw.html first
python3 tools/import_guide.py raw.html ee6049   # writes ee6049/index.html
```
The script is idempotent: it adds `noindex`, a `<title>` in `<head>`, and the "← Study hub" link.

### Add a new module (e.g. EE6043, or Semester 2)
1. Create `<code>/index.html` (lower-case module code), following an existing guide's structure.
2. Run it through `tools/import_guide.py` (or add the hub link by hand).
3. Add/replace its card in `index.html`; for a new module add `<code>/NOTES.md` from the template in any existing `NOTES.md`.
4. Log it in `PROJECT_STATUS.md` and `CHANGELOG.md`.

### Deploy
Pushing to `main` is the deploy. GitHub Pages rebuilds in about a minute. If the custom domain ever breaks, check Settings → Pages (custom domain `study.whoiskamrul.com`, "Enforce HTTPS" on) and the DNS `CNAME` record.

## Session checklist (end of every working session)
- [ ] `CHANGELOG.md` has a dated entry: what changed, why, anything left half-done
- [ ] `PROJECT_STATUS.md` "Next steps" reflects reality
- [ ] Touched modules' `NOTES.md` updated
- [ ] Committed and pushed
