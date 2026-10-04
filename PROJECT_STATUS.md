# Project status

_Last updated: 4 October 2026_

## Snapshot

| Module | Guide | Lessons | Covers | Last content update | State |
|---|---|---|---|---|---|
| EE6049 Design of Analogue ICs | `ee6049/` | 13 | Lectures 1–6 (8–25 Sep), slides 1–146; lectures 7–8 (29 Sep, 2 Oct; slides 147–171) not yet written up. Plus `ee6049/catch-up.html`, a 4–13 Oct catch-up plan to slide 178 | 4 Oct 2026 | Live |
| EE6043 Design of Digital ICs | `ee6043/` | 13 | Lectures 1–3 (intro, Verilog parts 1–2) | 30 Sep 2026 | Live |
| EE6041 Advanced Signal Processing | `ee6041/` | 34 | Topics 1–2 of 7: LTI systems (8, 9, 15 Sep) and z-transform (22, 23, 29, 30 Sep; Z slides 1–36) | 30 Sep 2026 | Live |
| CS6322 Optimisation | `cs6322/` | 18 | Lecture notes 1–8 | 30 Sep 2026 | Live |
| CS1068 Introductory Programming in Python | `cs1068/` | 15 | Lectures 0.1–3.1 (to Functions); runnable examples, Quizzes 2–3, past-paper Q1s | 1 Oct 2026 | Live |
| Semester 2 (MEMS, Data Converters, Adv. Analogue IC, RF ICs) | — | — | — | — | Planned |

## Site infrastructure

| Item | State |
|---|---|
| GitHub repo `mdkamrulislam-web/ucc-self-study` | Created 29 Sep 2026, public |
| GitHub Pages (main, root) | Enabled 29 Sep 2026 |
| Custom domain `study.whoiskamrul.com` | Cloudflare `CNAME study → mdkamrulislam-web.github.io` (DNS only) added 29 Sep 2026. HTTPS enforced, site verified live |
| Search engines | Blocked (`robots.txt` + `noindex` on every page) |

## Next steps

1. **Sync after each guide update** — say "sync the website" (workflow in `CLAUDE.md`).
2. **EE6043** — FPGA architecture lecture next, then timing and power.
3. **EE6041** — z-transform slides 37–53 (frequency response) next, then topics 3–7. Edited directly in this repo now; its artifact is frozen.
4. **EE6049** — write up lectures 7–8 (Sections 9–10, slides 147–171) and Section 11 (common-gate, slides 172–178; EE4022 Lecture 11 captions are in Drive) so the catch-up plan's last three days have guide lessons; lab-related theory before the labs on 8, 22, 29 Oct (no lab answers). Retire or refresh `ee6049/catch-up.html` after 13 Oct.
5. **CS6322** — beyond notes 8 (local search / simulated annealing, genetic algorithms).
6. **CS1068** — lectures after 3.1 (loops next); after 7 Oct add 2025–26 Q1(iii) to practice; mid-term quiz revision before 28 Oct. Edited directly in this repo; run `tools/check_examples.py` after edits. No lab, practice or assignment answers.
7. Optional: a small "last updated" line on each hub card, generated from `NOTES.md`.

## Open decisions

- Syncing is manual for now (say "sync the website"); later connect the repo to a Claude Code session for direct pushes.

- Whether to also link the hub from the main portfolio at whoiskamrul.com.
- Whether EE6019 (research project) planning pages belong on this site. Currently out of scope.
