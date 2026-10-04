# EE6049 Design of Analogue Integrated Circuits — guide notes

- **Page:** `ee6049/index.html` (title "EE6049 Study Guide")
- **Original artifact (main Claude account only):** https://claude.ai/artifact/QaHTtP87LvfGVPvWeGQYFf
- **Progress key:** `ee6049-guide-done-v1` → `l1`…`l19`
- **Last content update:** 4 Oct 2026 (lessons 14–19 written in this repo; lessons 1–13 from artifact version 1790743253, synced 30 Sep 2026). The artifact is now older than the repo: edit the repo copy, don't re-import from the artifact.

## Module facts used in the guide
- Exam: December 2026, 1.5 hours, answer 3 of 4, 70% of the module. Only the NMOS saturation equation is given.
- Labs: 30% (3 Cadence labs with worksheets 10%, op-amp design assignment 20%).
- Lecture and lab times and rooms: in the private `ucc-private` repo (`plan/class-timetable.md`).

## Coverage (lectures 1–8, slides 1–171, plus read-ahead lessons for slides 172–233)

| Lecture | Date | Lessons |
|---|---|---|
| 1 | Tue 8 Sep | 1 The big picture |
| 2 | Fri 11 Sep | 2 Inside a MOSFET · 3 The I–V equation · 4 Which region is it in? · 5 Second-order effects |
| 3 (online) | Tue 15 Sep | 6 DC biasing · 7 The small-signal model |
| 4 | Fri 18 Sep | 8 Intrinsic gain · 9 CS stage: resistor load |
| 5 | Tue 22 Sep | 10 CS stage: diode load |
| 6 | Fri 25 Sep | 11 CS stage: current-source load · 12 CMOS inverter amplifier · 13 Two-port shortcut |
| 7 | Tue 29 Sep | 14 CS stage with degeneration |
| 8 | Fri 2 Oct | 15 Source follower (and the DC biasing / common-mode problem) |
| read ahead | not lectured yet (4 Oct) | 16 Common-gate stage · 17 Cascode stage · 18 Folded and regulated cascodes · 19 Current mirrors (Sections 11–14, slides 172–233) |

Extras: interactive amplifier lab, 12 past-paper problems (Lessons 1–13), formula sheet (Lessons 1–19).

## Course mapping (from the 4 Oct catch-up work)

The day-by-day EE6049 catch-up plan is personal, so it lives in the private `ucc-private` repo (`plan/ee6049-catch-up.html`), not on this site. The course facts behind it stay here because they help when writing lessons:

- Recording segments used: 8 Sep 0:00–34:50 intro, 34:53– MOS basics · 11 Sep 0:00–27:10 structure→regions, 27:10–39:39 solutions 62–63, 40:11– second-order · 15 Sep 0:00–26:39 solutions 81–83, 26:39– small-signal · 18 Sep 8:39–30:00 solution 101, 30:00– CS stages · 22 Sep 0:00–17:40 solution 115, 17:40– diode loads · 25 Sep 0:00–29:05 recap + current-source load, 29:05–38:12 solution 139, 38:12– two-port · 29 Sep 0:00–16:00 y-parameter examples (146 circuit), 16:16– degeneration · 2 Oct 0:00–11:00 solution 161, 11:00–21:00 common-mode, 21:00– source follower.
- Razavi Lec ↔ section map used: 29–31 → S2 · 32 → S3 (CLM only) · 32–34 → S4 · 35–36 → S5 · 37 → S6–7 · none → S8 · 38 (+39 to 11:30) → S9 · 41 → S10 · 39 from 59:00 + 40 → S11. Lec 42–45 (op-amps as a black box) only touch S19, S24–27. Razavi Electronics 1 has nothing for S12–18 or S20–23.
- Uses the shared course resources: sample-problem solutions (slides 62 [+63], 81 [81–83], 101, 115, 126, 139, 146, 161, 171), the six whiteboard handouts, and the lab manual + Lab 1–3 worksheets + EDA quick start.
- Lab facts used (lab manual v1.0, 24 Sep 2026): Labs 1–2 = common-source NMOS, W/L 10/1 µm, 10 kΩ rppoly2 load, VDD 3.3 V, VIN 1 V DC, 1 pF load, AMS C35B4. Lab 1 worksheet: DC op point and headroom, ID from the square law, gain 20·log(gm/(gds+1/RL)), pole (gds+1/RL)/(2πCL), zero gm/(2πCgd), transient, DFT with HD2 ≈ Vp/(4(VGS−Vt)). Lab 2: sweeps, calculator, process corners. Lab 3: feedback amplifier, loop gain, phase margin, compensation (Sections 19–21). No worksheet answers in the guide or the plan.

## To do
- [x] Lectures 7–8 written up (4 Oct), plus read-ahead lessons for Sections 11–14
- [ ] When the lectures reach Sections 11–14, check lessons 16–19 against what was said (recordings from 6 Oct on) and move them under their lecture dates in the rail
- [ ] Worked answers for problems 178, 190, 200, 207 and 227 are mine (no official solutions yet); compare them with the lecturer's when they appear
- [ ] Next: Sections 15–17 (mismatch, differential pairs) ahead of the lectures
- [ ] Theory primer before Lab 1 (8 Oct) — no worksheet answers
