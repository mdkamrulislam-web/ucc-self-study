# EE6019: scope questions for Prof. Emanuel Popovici

*Open chip-development flow using open-source tools. Draft, 30 September 2026 (revised after reading the Drive folder).*

## What I have understood so far

- **21 Sep email:** you suggested starting with Bo Yang's thesis, and mentioned two other directions: in-memory computing and AI, and "a completely open flow for digital and use tinytapeouts".
- **24 Sep options note:** I proposed four directions from the thesis. Option C combined the open flow (Yosys, ABC, LibreLane, Tiny Tapeout on SKY130 or IHP SG13G2) with reliability-driven synthesis from Chapter 3.
- **25 Sep meeting:** you said the project is now the open flow: survey the free alternatives to Cadence and Synopsys, install the flow, and build an ASIC with it. You also said the group hopes to make chips for students next year using this flow, so this project would be the first one through it, and you would send a website/link with more detail. Weekly Friday log entries will feed the logbook in the report.

*(My notes on the meeting come from an automatic transcript that is hard to follow in places, so please correct anything I have misread.)*

The questions below are what I still need to pin down. Each has a suggested default in *italics* so you can simply agree or change it.

---

## 1. Goal and audience

1. Is the main deliverable a **documented, reusable flow that next year's students can follow**, with my own chip as the first worked example?
   *Default: yes. The flow and its documentation are the core; a tapeout-ready design proves it works.*
2. You mentioned building a chip "using both those open flows". Which two flows did you mean? My assumption is LibreLane and OpenROAD-flow-scripts, the two main open RTL-to-GDS flows; is that right?
3. Could you send the website/link you mentioned in the meeting, so I start from the same material?
4. Should any of the thesis work carry over (for example Option C's reliability-aware synthesis as a research contribution on top of the flow), or is the flow the whole project now?
   *Default: flow first; add a reliability or PPA comparison study only if time allows, since it gives the report a research angle.*

## 2. Tapeout

5. Is an actual **Tiny Tapeout** submission expected during the project, or is a verified, tapeout-ready GDS enough?
6. If submitting, which shuttle should we aim for, and is there a budget for the tile(s)? Shuttle deadlines will set the whole schedule.
7. For next year's student chips, are you thinking of Tiny Tapeout tiles for each student, a shared multi-project chip, or an IHP MPW run?

## 3. PDK choice

The realistic open PDKs are SkyWater SKY130 and IHP SG13G2 (GF180MCU is a third).

| | **SKY130** (SkyWater, 130 nm) | **IHP SG13G2** (IHP, 130 nm SiGe BiCMOS) |
|---|---|---|
| Open ecosystem | Most mature: most examples, tutorials, student projects | Younger but growing fast; actively maintained by IHP |
| Tool support | LibreLane/OpenLane, OpenROAD, Magic, KLayout, Netgen, ngspice, Xschem | LibreLane and OpenROAD-flow-scripts, KLayout-based DRC/LVS, ngspice, Xschem |
| Getting chips made | Tiny Tapeout still runs SKY130 shuttles (listed closing 30 Nov 2026 and May 2027) | Tiny Tapeout IHP shuttle TTIHP27a (closing March 2027); IHP also offers free MPW runs for research and education |
| Good for | Learning and teaching, lots of reference material | A live fabrication route in Europe; SiGe HBTs for analogue/RF |

*Shuttle dates are from the Tiny Tapeout chips page (tinytapeout.com/chips), checked 30 Sep 2026.*

8. Do you have a preference, or existing links with IHP or another fab?
9. Is the scope **digital only** (RTL to GDS), or should the flow also cover analogue design?
   *Default: digital only, as in your email.*
10. Should the flow work on more than one PDK?
   *Default: bring the flow up on SKY130 first (most examples), then move to IHP SG13G2 and target the TTIHP27a shuttle closing in March 2027.*

## 4. Tools and flow

11. Am I free to choose the toolchain (Yosys, ABC, LibreLane or OpenROAD-flow-scripts, Verilator or Icarus with cocotb, KLayout, Magic, Netgen)?
12. How far should the flow go: simulation, synthesis, place and route, static timing, DRC, LVS, gate-level simulation?
13. How should students install it? For example a Docker or Nix container, a lab machine or server image, or a GitHub template with CI that runs the flow.
14. What should the example design be? Something from the group's research, a small processor or peripheral, or my own choice?

## 5. Deliverables, timeline and practicalities

15. Beyond the report and the logbook, which of these do you want: a public repository, student lab handouts, a demo/presentation, a paper (for example on open-source EDA in teaching)?
16. What are the fixed dates for the interim report, final submission and presentation? My outline plan aims to finish by the end of April 2027.
17. Which machine should I use: my laptop, a lab PC, or remote access to a server? (You mentioned my account would be set up.)
18. Is there anyone I should coordinate with, such as another student or group member already using open tools?

---

### Proposed next step

Once you have answered these, I will write a one-page project plan with milestones (tool set-up, first design through the flow, verification and sign-off, student documentation, tapeout submission) and send it for your approval.
