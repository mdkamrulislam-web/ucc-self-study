# Project status

_Last updated: 29 September 2026_

## Snapshot

| Module | Guide | Lessons | Covers | Last content update | State |
|---|---|---|---|---|---|
| EE6049 Design of Analogue ICs | `ee6049/` | 11 | Lectures 1–5 (8–22 Sep), slides 1–131; lecture 6 (25 Sep) not yet written up | 24 Sep 2026 | Live |
| EE6043 Design of Digital ICs | `ee6043/` | 0 | — | — | Placeholder |
| EE6041 Advanced DSP | `ee6041/` | 19 | Lectures of 8, 9, 15 Sep (LTI systems, slides 1–47) | 24 Sep 2026 | Live |
| CS6322 Optimisation | `cs6322/` | 15 | Lecture notes 1–7 | 28 Sep 2026 | Live |
| Semester 2 (MEMS, Data Converters, Adv. Analogue IC, RF ICs) | — | — | — | — | Planned |

## Site infrastructure

| Item | State |
|---|---|
| GitHub repo `mdkamrulislam-web/ucc-self-study` | Created 29 Sep 2026, public |
| GitHub Pages (main, root) | Enabled 29 Sep 2026 |
| Custom domain `study.whoiskamrul.com` | Cloudflare `CNAME study → mdkamrulislam-web.github.io` (DNS only) added 29 Sep 2026. HTTPS enforced, site verified live |
| Search engines | Blocked (`robots.txt` + `noindex` on every page) |

## Next steps

1. **EE6043 Design of Digital ICs guide** — biggest gap. Needs the lecture slides from `UCC/SEMESTER-1/` on Google Drive. Build in the same format; replace the placeholder and update the hub card (badge → Live, add `data-store`/`data-total`, progress bar markup).
2. **EE6041** — extend beyond the 15 Sep lecture as new lectures arrive.
3. **EE6049** — write up lecture 6 (25 Sep) and onwards; add lab-related theory before the labs on 8, 22, 29 Oct (no lab answers).
4. **CS6322** — extend beyond notes 7 (metaheuristics, greedy, dynamic programming are still to come per the Winter 2025 paper).
5. Optional: a small "last updated" line on each hub card, generated from `NOTES.md`.

## Open decisions

- Syncing is manual for now (say "sync the website"); later connect the repo to a Claude Code session for direct pushes.

- Whether to also link the hub from the main portfolio at whoiskamrul.com.
- Whether EE6019 (research project) planning pages belong on this site. Currently out of scope.
