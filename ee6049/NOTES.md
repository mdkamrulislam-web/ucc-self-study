# EE6049 Design of Analogue Integrated Circuits — guide notes

- **Page:** `ee6049/index.html` (title "EE6049 Study Guide")
- **Original artifact (main Claude account only):** https://claude.ai/artifact/QaHTtP87LvfGVPvWeGQYFf
- **Progress key:** `ee6049-guide-done-v1` → `l1`…`l13`
- **Last content update:** 30 Sep 2026 (artifact version 1790743253; synced 30 Sep 2026)

## Module facts used in the guide
- Exam: December 2026, 1.5 hours, answer 3 of 4, 70% of the module. Only the NMOS saturation equation is given.
- Labs: 30% (3 Cadence labs with worksheets 10%, op-amp design assignment 20%). Kamrul's lab sessions: Thu 8, 22, 29 Oct, 17:00–19:00, Elec Eng L3.
- Lectures: Tue 12:00 KANE_G06, Fri 09:00 ELECT_L2.

## Coverage (lectures 1–6, slides 1–146)

| Lecture | Date | Lessons |
|---|---|---|
| 1 | Tue 8 Sep | 1 The big picture |
| 2 | Fri 11 Sep | 2 Inside a MOSFET · 3 The I–V equation · 4 Which region is it in? · 5 Second-order effects |
| 3 (online) | Tue 15 Sep | 6 DC biasing · 7 The small-signal model |
| 4 | Fri 18 Sep | 8 Intrinsic gain · 9 CS stage: resistor load |
| 5 | Tue 22 Sep | 10 CS stage: diode load |
| 6 | Fri 25 Sep | 11 CS stage: current-source load · 12 CMOS inverter amplifier · 13 Two-port shortcut |
| 7 | Tue 29 Sep | *listed in the rail, not yet written up* |

Extras: interactive amplifier lab, 12 past-paper problems, formula sheet.

## Catch-up plan (`ee6049/catch-up.html`)

A separate page, not part of the guide (so an artifact re-import of `index.html` doesn't touch it). Linked from the hub under the Semester 1 cards. Written 4 Oct 2026 for Kamrul, who had watched Razavi *Electronics 1* Lec 29–30 but not yet worked through the course slides or problems.

- 11 days, 4–14 Oct 2026, ending at slide 178 (end of Section 11, common-gate). Each day pairs a Razavi lecture (start time, asides to skip) with Kamrul's own EE6049 lecture recording for the same slides (timestamped segments), plus the guide lesson and the end-of-section problem. Each "Try" comes before the recording segment that solves it.
- Recording segments used: 8 Sep 0:00–34:50 intro, 34:53– MOS basics · 11 Sep 0:00–27:10 structure→regions, 27:10–39:39 solutions 62–63, 40:11– second-order · 15 Sep 0:00–26:39 solutions 81–83, 26:39– small-signal · 18 Sep 8:39–30:00 solution 101, 30:00– CS stages · 22 Sep 0:00–17:40 solution 115, 17:40– diode loads · 25 Sep 0:00–29:05 recap + current-source load, 29:05–38:12 solution 139, 38:12– two-port · 29 Sep 0:00–16:00 y-parameter examples (146 circuit), 16:16– degeneration · 2 Oct 0:00–11:00 solution 161, 11:00–21:00 common-mode, 21:00– source follower.
- Razavi Lec ↔ section map used: 29–31 → S2 · 32 → S3 (CLM only) · 32–34 → S4 · 35–36 → S5 · 37 → S6–7 · none → S8 · 38 (+39 to 11:30) → S9 · 41 → S10 · 39 from 59:00 + 40 → S11. Lec 42–45 (op-amps as a black box) only touch S19, S24–27. Razavi Electronics 1 has nothing for S12–18 or S20–23.
- Ticks in `localStorage` key `ee6049-catchup-v3` (Lec 29–30 pre-ticked on first visit; v2 retired when the tasks were reshuffled). The hub does not read it.
- Uses the shared course resources: sample-problem solutions (slides 62 [+63], 81 [81–83], 101, 115, 126, 139, 146, 161, 171), the six whiteboard handouts, and the lab manual + Lab 1–3 worksheets + EDA quick start.
- Lab facts used (lab manual v1.0, 24 Sep 2026): Labs 1–2 = common-source NMOS, W/L 10/1 µm, 10 kΩ rppoly2 load, VDD 3.3 V, VIN 1 V DC, 1 pF load, AMS C35B4. Lab 1 worksheet: DC op point and headroom, ID from the square law, gain 20·log(gm/(gds+1/RL)), pole (gds+1/RL)/(2πCL), zero gm/(2πCgd), transient, DFT with HD2 ≈ Vp/(4(VGS−Vt)). Lab 2: sweeps, calculator, process corners. Lab 3: feedback amplifier, loop gain, phase margin, compensation (Sections 19–21). No worksheet answers in the guide or the plan.
- Also published as a private Claude artifact (main Claude account only): https://claude.ai/artifact/4vnwi3t35LYq5cMo7G9xA5. The repo copy is the one to edit.

## To do
- [ ] Write up lecture 7 (29 Sep) and later lectures
- [ ] Theory primer before Lab 1 (8 Oct) — no worksheet answers
