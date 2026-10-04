# EE6041 Advanced Signal Processing — guide notes

- **Page:** `ee6041/index.html` (title "EE6041 Advanced Signal Processing"; was "EE6041 LTI Systems")
- **Original artifact (main Claude account only):** https://claude.ai/artifact/JTnoT9E5GkcWsFp94eaK7i — frozen at 29 Sep 2026. From 30 Sep the guide is edited here directly; don't re-import it from the artifact.
- **Progress key:** `ee6041-lti-progress-v1` → `s1`…`s19` (LTI) and `z1`…`z15` (z-transform)
- **Last content update:** 30 Sep 2026, in the repo (sections 32–34 from the lectures of 29 and 30 Sep)
- **Note:** ~4.1 MB because KaTeX fonts are embedded as data URIs and every formula is pre-rendered. That's expected.

## Module facts
- Lecturer: Prof. Cantillon-Murphy. Seven topics in the module; the guide grows as each is taught.
- Lecture times and rooms: in the private `ucc-private` repo (`plan/class-timetable.md`).
- The guide has an "Assignment 1" section (explains the task; no answers).

## Coverage (topics 1–2 of 7)

| Topic · lecture | Date | Sections |
|---|---|---|
| LTI · 1 | 8 Sep | 1 Analogue to digital · 2 Sampling and digital frequency · 3 Linear and time-invariant · 4 The impulse response · 5 Convolution · 6 Causality |
| LTI · 2 | 9 Sep | 7 FIR and IIR · 8 Stability (BIBO) · 9 The DTFT · 10 Frequency response · 11 The moving average · 12 The ideal filter · 13 Filter specifications |
| LTI · 3 | 15 Sep | 14 Difference equations and block diagrams · 15 FIR vs IIR · 16 Linear phase · 17 The Type I derivation · 18 Group delay · 19 IIR vs FIR in action |
| Z-transform · 5 | 22 Sep | 20 Why poles and zeros · 21 A loop that runs away · 22 The z-transform · 23 Region of convergence · 24 The z-plane and the DTFT · 25 The table of pairs |
| Z-transform · 6 | 23 Sep | 26 Causal, anti-causal, two-sided · 27 The ROC decides the signal · 28 Properties · 29 Poles and zeros · 30 The inverse z-transform · 31 Stability from the z-plane |
| Z-transform · 7 | 29 Sep | 32 A double pole (the step convolved with itself) · 33 The system function (Z slides 24–28; its 30 Sep board example too) |
| Z-transform · 8 | 30 Sep | 34 The unit circle as the stability boundary (Z slides 29–36; "move the pole" demo) |

Extras: cheat sheet, common traps, exam-style practice, past exam questions, still to come.

## To do
- [ ] Z-transform slides 37–53 (frequency response from H(z), the geometric method, two FIR examples): next lectures, "into Fourier"
- [ ] Topics 3–7 as they are lectured
- [ ] Consider splitting into one page per topic if the file keeps growing (Kamrul asked on 29 Sep to keep it as one page)

## How this guide is built
Every formula is pre-rendered KaTeX (0.16.22, default options) and each lesson has `content-visibility:auto` with measured heights in `style="--cis-d:…;--cis-m:…"` (content box at 1280 px and 390 px wide). When adding a lesson, copy the markup of an existing one, render its TeX with KaTeX, add it to the rail and to the tick count, and measure its heights in a headless browser with `section.lesson{content-visibility:visible !important}` injected.

## Flags raised in the guide (lecture slips)
- 16 Sep: MIT-BIH mains called 50 Hz; it is 60 Hz (checked ECG100). "0.05 Hz" where the brief says 0.5 Hz.
- 22 Sep: "ROC inside the unit circle" for stability; the poles are inside, the ROC contains the circle.
- Z slide 3, row 9: sin ω0 printed in the denominator; should be cos ω0.
- 29 Sep: the two-sided board example drawn negative on the left and called not symmetric; it is x(n) = (1/2)^|n|.
