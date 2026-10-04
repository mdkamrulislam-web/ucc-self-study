# EE6019 Project Plan: An Open Chip-Development Flow

First written 30 Sep 2026 as a Claude Doc and copied here on 4 Oct 2026. This file is now the copy to edit.

## Summary

By the end of April 2027, deliver a documented, open-source digital chip flow (RTL to GDS) that next year's UCC students can install and follow, proven by taking one small design of my own to a verified, tapeout-ready layout and, if a shuttle and budget allow, a Tiny Tapeout submission.

The end date is firm: my work placement starts on 10 May 2027, so nothing in this plan can slip past April.

- **Main deliverable:** the flow itself, as a public repository with a pinned tool environment, one-command runs, and a step-by-step student guide.
- **Proof it works:** my design passes simulation, synthesis, place and route, timing, DRC and LVS with no errors.
- **Research angle:** a short survey of open tools against Cadence and Synopsys, and one measured comparison (for example two PDKs, or two flows) written up in the report.
- **Done means:** a student who has never used the tools can follow the guide from a clean machine to a GDS in one lab session, and Prof. Popovici has signed off the report and logbook.

## What Prof. Popovici asked for

The ask has moved from Bo Yang's thesis to an open flow: survey the free alternatives to Cadence and Synopsys, install an open flow, and build an ASIC with it. Sources are the 21 Sep email, my 24 Sep options note, and the 25 Sep group meeting transcript (my part runs from about 20:05 to 21:10).

| Point | Where | How sure |
| --- | --- | --- |
| Look at the open tools that replace Cadence or Synopsys, then install the flow and build an ASIC | Transcript 20:05 to 20:43 | Clear in meaning, garbled words ("open floor", "bill the Asian") |
| The group wants to make chips for students next year using this flow; my project is the first one through it | Transcript 20:44 | Clear |
| I may get to build a chip myself "using both those open flows" | Transcript 21:08 | Unclear which two flows he means |
| He will send a website link with more detail | Transcript 20:05 and 21:08 | Clear; not received yet |
| "A completely open flow for digital and use tinytapeouts" | 21 Sep email | Clear (quoted in my notes) |
| Weekly log, ideally each Friday, feeds the logbook in the final report; record mistakes and how they were fixed | Transcript 9:35 to 11:29 | Clear |
| Every project needs a short risk assessment | Transcript 6:09 | Clear |
| A lab account will be set up for remote log-in | Transcript 23:55 | Probably said to another student; check |

The rest of the transcript (FPGA place and route, PCB design, option pricing, smart glasses) is about other students' projects and is left out of this plan.

## Scope and deliverables

The scope is a digital RTL-to-GDS flow; analogue design is out unless Prof. Popovici asks for it.

| Deliverable | What it is | Where it lives | Needed by |
| --- | --- | --- | --- |
| Open-tool survey | Each flow stage mapped to its commercial tool and its open replacement, with maturity notes | Report chapter 2 | End of Oct 2026 |
| Reproducible environment | One pinned container (the first-run thread already uses IIC-OSIC-TOOLS 2026.09) plus install notes for lab PCs | openFlowForChipDev repo | Mid Oct 2026 |
| Reference flow | Makefile targets for simulate, synthesise, place and route, timing, DRC, LVS, gate-level simulation; PDK chosen by one setting | openFlowForChipDev repo | Nov 2026 |
| Worked example | A small design taken through every stage, with the reports kept | openFlowForChipDev repo | Nov 2026 (counter), Mar 2027 (real design) |
| My demonstrator design | A useful block, verified and tapeout-ready; submitted to Tiny Tapeout if approved | Repo, then shuttle | Mar 2027 |
| Student guide | Lab-style handouts: install, first run, reading the reports, fixing DRC and timing errors | Repo docs, later a website | Apr 2027 |
| Report, logbook, presentation | EE6019 submission, with weekly Friday logs and the risk assessment | UCC submission | Dates to confirm |

Out of scope unless asked: analogue or mixed-signal design, FPGA flows, PCB design, and the reliability-synthesis work from the thesis (kept as an optional extension).

## Tool chain and PDK

Build the flow on LibreLane (the successor to OpenLane 2) inside one pinned container, keep the PDK a single setting, and run the same design through OpenROAD-flow-scripts as the second flow for comparison.

| Stage | Open tool | Commercial equivalent |
| --- | --- | --- |
| RTL simulation and testbench | Icarus Verilog or Verilator, with cocotb | Cadence Xcelium, Synopsys VCS |
| Lint | Verilator lint | Synopsys SpyGlass |
| Synthesis | Yosys with ABC | Synopsys Design Compiler, Cadence Genus |
| Floorplan, placement, clock tree, routing | OpenROAD (driven by LibreLane or ORFS) | Cadence Innovus, Synopsys IC Compiler II |
| Parasitics and static timing | OpenRCX, OpenSTA | Cadence Tempus, Synopsys PrimeTime |
| DRC | Magic and KLayout (KLayout decks for IHP) | Siemens Calibre |
| LVS | Netgen (SKY130), KLayout (IHP) | Siemens Calibre |
| Gate-level simulation | Icarus Verilog with the PDK cell models | Xcelium, VCS |
| Layout viewing | KLayout | Cadence Virtuoso |
| Packaging for tapeout | Tiny Tapeout template and GitHub Actions | Foundry sign-off kit |

**PDK recommendation: IHP SG13G2 as the target, SKY130 for the first bring-up.** The [Tiny Tapeout shuttle list](https://tinytapeout.com/chips/) (read 30 Sep 2026) shows TTIHP27a closing in March 2027, which fits a project ending in April. The next SKY130 shuttles close on 30 Nov 2026 (too early for my design) and in May 2027 (after the project ends). IHP also runs its own [open-source MPW service](https://www.ihp-microelectronics.com/services/research-and-prototyping-service/mpw-prototyping-service/low-cost-open-source-mpw-access-1) at about 2,800 EUR per mm², which could suit next year's student chips. GF180 (TTGF27a, April 2027) is the fallback.

This corrects one point in the scope questions: SKY130 shuttles are still running through Tiny Tapeout, so SKY130 remains a live option.

## Timeline

The flow and a first full run come first, in October and November, so the demonstrator design has a working flow to go through after the exams.

The month-by-month milestones are in the table below.

Friday logs run every week throughout. Tiny Tapeout lists TTIHP27a only as "March 2027", so the sign-off date moves once the exact day is published; if the tapeout is dropped, the same dates still give a verified GDS by mid-March.

| Month | Milestone that shows it is done |
| --- | --- |
| Oct 2026 | Counter clean on SKY130 and IHP (done 30 Sep); survey table drafted; container installs on my laptop and a lab PC |
| Nov 2026 | LibreLane and ORFS compared; flow accepts Tiny Tapeout projects; demonstrator chosen |
| Dec 2026 | Student guide v0 tested by a classmate; interim note sent |
| Feb 2027 | Demonstrator design passes its testbench and fits the tile |
| Mar 2027 | Clean DRC, LVS and timing; Tiny Tapeout submission (if approved) |
| Apr 2027 | A classmate follows the guide on a clean machine; report submitted |

## Week by week

Each row is one Friday log. The first counter run landed on 30 Sep, ahead of the original timeline, so November now goes on the second flow and choosing the demonstrator. The exam and break weeks are my guess at the UCC calendar; check them against the official dates.

| Friday | Week | Focus | What the log reports | Status |
| --- | --- | --- | --- | --- |
| Fri 2 Oct | W40 | Plan, scope questions, first counter run (PR #1) | Send plan and scope questions to Prof. Popovici; ask for the website link; first log | In progress |
| Fri 9 Oct | W41 | Merge PR #1; Tiny Tapeout study path parts 1 and 2 | Notes from the videos, FAQ, SiliWiz and Wokwi lessons; risk assessment drafted | Not started |
| Fri 16 Oct | W42 | Counter on the Tiny Tapeout IHP Verilog template | GitHub Actions green (test, gds, docs); GDS screenshot | Not started |
| Fri 23 Oct | W43 | Local hardening with tt\_tool; start the tool survey | LibreLane 3.0.3 (Tiny Tapeout) against 3.1 (our image): same result or not | Not started |
| Fri 30 Oct | W44 | Tool survey write-up; PDK and shuttle decision | Report chapter 2 first draft; decision recorded from Prof. Popovici's answers | Not started |
| Fri 6 Nov | W45 | Second flow: OpenROAD-flow-scripts runs the counter | ORFS run clean on IHP (and SKY130) inside the same container | Not started |
| Fri 13 Nov | W46 | Compare LibreLane with ORFS | Table of area, slack, run time and set-up effort for both flows | Not started |
| Fri 20 Nov | W47 | Flow accepts a Tiny Tapeout project as it stands | `src/`, `test/`, `info.yaml` layout; cocotb and gate-level tests in CI | Not started |
| Fri 27 Nov | W48 | Choose the demonstrator design | Three candidates, one agreed; spec with pin map and a 1,000-gate budget | Not started |
| Fri 4 Dec | W49 | Student guide v0: install and first run | A classmate follows it on a clean machine; short interim note to Prof. Popovici | Not started |
| Fri 11 Dec | W50 | Exams: light week | Short log; tidy docs | Not started |
| Fri 18 Dec | W51 | Exams: light week | Short log | Not started |
| 25 Dec, 1 Jan | W52, W53 | Christmas break | No log expected (confirm with Prof. Popovici) | Not started |
| Fri 8 Jan | W01 | Restart: re-run the flow; begin demonstrator RTL | Flow still clean on the pinned image; RTL skeleton committed | Not started |
| Fri 15 Jan | W02 | Demonstrator RTL core | Core blocks written with cocotb unit tests passing | Not started |
| Fri 22 Jan | W03 | Full testbench; first harden on IHP | Every spec feature tested; first area and timing numbers | Not started |
| Fri 29 Jan | W04 | Fit the tile and meet timing | Design fits the planned tiles at the target clock | Not started |
| Fri 5 Feb | W05 | Gate-level simulation clean; guide chapters 2 and 3 | GL tests pass; guide covers reading reports and fixing DRC and timing | Not started |
| Fri 12 Feb | W06 | Design freeze candidate | `docs/info.md` written; freeze tag in the repo | Not started |
| Fri 19 Feb | W07 | Sign-off round 1 on IHP | DRC, LVS, antenna and timing across corners; list of violations | Not started |
| Fri 26 Feb | W08 | Fix sign-off issues | All violations closed; Tiny Tapeout actions green on the submission repo | Not started |
| Fri 5 Mar | W09 | Final checks; confirm TTIHP27a date and budget | Clean sign-off; go or no-go on submission from Prof. Popovici | Not started |
| Fri 12 Mar | W10 | Submit to TTIHP27a, if approved | Submission confirmed, or a tagged release of the verified GDS | Not started |
| Fri 19 Mar | W11 | Buffer for a shuttle slip; start the report | Methods chapter drafted | Not started |
| Fri 26 Mar | W12 | Report: results | Flow comparison and demonstrator results written up | Not started |
| Fri 2 Apr | W13 | Student guide complete; dry runs | One or two classmates run the whole guide on clean machines | Not started |
| Fri 9 Apr | W14 | Fix the guide; full report draft | Draft report sent to Prof. Popovici | Not started |
| Fri 16 Apr | W15 | Revise the report; compile the logbook | Feedback addressed; logbook assembled from the weekly logs | Not started |
| Fri 23 Apr | W16 | Presentation and demo | Slides done; demo rehearsed | Not started |
| Fri 30 Apr | W17 | Submit | Report, logbook and a v1.0 release of the repository | Not started |

### Friday log template

Save each week as `logbook/2026-W41.md` (ISO week number) and email the same text to Prof. Popovici before the weekly meeting.

```markdown
# Week 41 (5 to 9 Oct 2026)

## Done
- 

## Problems and how I fixed them
- 

## Evidence
- Commit or PR link, screenshot, report numbers

## Next week
- 

## Questions for Prof. Popovici
- 
```

## Weekly routine

I meet Prof. Popovici once a week. The week's log entry is written and the work pushed before that meeting, so the final logbook writes itself. (The meeting time and place, and how the project hours fit into the week, are kept in the private `ucc-private` repo.)

- **Friday log:** what I did, what broke and how I fixed it, what is next, and any question for Prof. Popovici. He asked for mistakes to be recorded, so failed runs count. Keep entries in `logbook/` in the repo, one file per week (`2026-W40.md`), and email him the same text before the meeting.
- **Weekly meeting:** bring the latest log and one screenshot or report (layout, timing summary, DRC count).
- **Repository habits:** every flow change goes through a pull request; CI runs the reference design so a broken flow is caught at once; tool and PDK versions are pinned and written in the README.
- **Student view:** each time a step works, write the student-guide paragraph for it that same week, while the pitfalls are fresh.

## Risks

The biggest risk is the shuttle date, because it fixes when the design must be finished; everything else has a workable fallback.

| Risk | Effect | Fallback |
| --- | --- | --- |
| TTIHP27a slips, or no budget for a tile | No silicon during the project | Deliver a verified, tapeout-ready GDS; submit to the next shuttle after the project |
| Tools do not install cleanly on lab PCs or laptops | Students cannot follow the guide | Use one pinned container for everything; test the guide on a clean machine each month |
| IHP flow support is less mature than SKY130 | DRC or LVS errors with no clear fix | Bring the flow up on SKY130 first; keep the PDK a single setting; ask on the IHP and LibreLane forums |
| Design too large for the tile or misses timing | Late redesign | Choose a small design early; run the full flow on it every week from January |
| Tool versions change under us | The guide stops matching the tools | Pin versions; upgrade only on purpose, with a log entry |
| Semester 1 exams and coursework | Little project time in December and January | Front-load the survey and the first full run into October and November |
| Laptop or disk failure | Lost work | Push to GitHub at least every Friday |

For the university risk assessment: this is desk and computer work only, so the usual items apply (display-screen use, laptop batteries and chargers, fire exits and extinguishers, as mentioned in the meeting).

## Open questions and next steps

Five answers from Prof. Popovici would lock this plan; the full list, with defaults, is in [scope-questions-for-prof-popovici.md](scope-questions-for-prof-popovici.md).

1. Is the documented, reusable flow the main deliverable, with my chip as the first worked example?
2. Which two "open flows" did he mean (LibreLane and OpenROAD-flow-scripts is my guess)?
3. Is a real Tiny Tapeout submission expected, and is there budget for a tile on TTIHP27a (March 2027)?
4. Which PDK does he prefer, and does the group have links with IHP?
5. What are the fixed dates for the interim report, final report and presentation?

This week:

- [ ] Send the scope questions and this plan to Prof. Popovici, and ask for the website link he mentioned
- [ ] Write the first Friday log entry (week of 28 Sep) on Thursday 1 Oct, ready for the first weekly meeting on 2 Oct
- [ ] Review and merge the first-run pull request (counter through LibreLane on SKY130) once it is up
- [ ] Work through the [Tiny Tapeout study path](tiny-tapeout-study-path.md) (Prof. Popovici's 30 Sep request), then start the open-tool survey table for report chapter 2
- [ ] Draft the one-page risk assessment

## Sources

- Kamrul's Google Drive folder "EE6019 - Research Project": the 25 Sep meeting transcript, the 24 Sep options note and the 19 to 21 Sep email thread (private, not linked here)
- [Tiny Tapeout shuttle list](https://tinytapeout.com/chips/), read 30 Sep 2026
- [IHP low-cost open-source MPW access](https://www.ihp-microelectronics.com/services/research-and-prototyping-service/mpw-prototyping-service/low-cost-open-source-mpw-access-1), read 30 Sep 2026
