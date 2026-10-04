# Project status

_Last updated: 30 September 2026_

## Snapshot

| Module | Guide | Lessons | Covers | Last content update | State |
|---|---|---|---|---|---|
| EE6049 Design of Analogue ICs | `ee6049/` | 13 | Lectures 1–6 (8–25 Sep), slides 1–146; lecture 7 (29 Sep) not yet written up | 30 Sep 2026 | Live |
| EE6043 Design of Digital ICs | `ee6043/` | 13 | Lectures 1–3 (intro, Verilog parts 1–2) | 30 Sep 2026 | Live |
| EE6041 Advanced Signal Processing | `ee6041/` | 34 | Topics 1–2 of 7: LTI systems (8, 9, 15 Sep) and z-transform (22, 23, 29, 30 Sep; Z slides 1–36) | 30 Sep 2026 | Live |
| CS6322 Optimisation | `cs6322/` | 18 | Lecture notes 1–8 | 30 Sep 2026 | Live |
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
4. **EE6049** — write up lecture 7 (29 Sep) onwards; lab-related theory before the labs on 8, 22, 29 Oct (no lab answers).
5. **CS6322** — beyond notes 8 (local search / simulated annealing, genetic algorithms).
6. **Study plan** — `plan/semester-1-study-plan.md` is now the copy to edit (timetable, deadlines, rules).
7. Optional: a small "last updated" line on each hub card, generated from `NOTES.md`.

## Open decisions

- Syncing is manual for now (say "sync the website"); later connect the repo to a Claude Code session for direct pushes.

- Whether to also link the hub from the main portfolio at whoiskamrul.com.
- Whether EE6019 (research project) planning pages belong on this site. Currently out of scope.
