# Tiny Tapeout Study Path

First written 30 Sep 2026 as a Claude Doc and copied here on 4 Oct 2026. This file is now the copy to edit. It goes with the [EE6019 project plan](ee6019-project-plan.md).

Start with the Verilog flow on the IHP template: it is the flow our March 2027 tapeout will use, and it already runs the same open tools as our repo (LibreLane, Yosys, OpenROAD, cocotb).

## The four flows

Every Tiny Tapeout flow ends in the same place: a GitHub repository whose Actions build the GDS, which you then submit at [app.tinytapeout.com](https://app.tinytapeout.com/). They differ in how you describe the circuit and where the tools run.

| Flow | You describe the design with | Tools run on | Who it suits |
| --- | --- | --- | --- |
| [Wokwi](https://tinytapeout.com/digital_design/) | Gates drawn in a browser simulator | GitHub Actions | Beginners; first-year students |
| [Verilog (HDL)](https://tinytapeout.com/hdl/) | Verilog in `src/`, cocotb tests in `test/`, settings in `info.yaml` | GitHub Actions: `test`, `gds` (LibreLane), `docs`, `fpga` | Our project, and students who know an HDL |
| [Local hardening](https://tinytapeout.com/guides/local-hardening/) | The same Verilog repository | Your own machine: `tt_tool.py` with LibreLane 3.0.3 through pip, Docker, Python 3.11+ | Fast iteration; seeing every stage's reports |
| Analogue ([SKY130 template](https://github.com/TinyTapeout/ttsky-analog-template)) | A hand-drawn layout (Magic, Xschem) | Your own machine | Out of scope for us |

The Verilog flow's `gds` action runs synthesis, place and route, and sign-off with LibreLane, then re-runs your cocotb testbench on the gate-level netlist. That is the same chain our repo runs, just triggered by a push instead of `make`.

## Watch and read, in order

Work top to bottom; tick each one off and note anything worth a Friday log line.

**1. The big picture**

- [ ] Watch [From idea to chip design in minutes!](https://www.youtube.com/watch?v=qVWq_XZko-M), the overview on the [home page](https://tinytapeout.com/). The [teaching page](https://tinytapeout.com/teaching/) links an [older Tiny Tapeout 5 version](https://youtu.be/f4w1QOpHzOo) of the same intro; skip it unless you want a second pass.
- [ ] Watch [Making ASICs](https://www.youtube.com/watch?v=dckPKyO2nSo): what the hardening flow does, and how to read its logs
- [ ] Watch [Manufacturing ASICs](https://www.youtube.com/watch?v=aBDJQ9NYTEU): a factory tour from GDS to packaged chip
- [ ] Read [Making ASICs](https://tinytapeout.com/making_asics/) and the [FAQ](https://tinytapeout.com/faq/) (tile size, pins, clock, timeline)

**2. Fundamentals, quickly**

- [ ] [SiliWiz](https://tinytapeout.com/siliwiz/): draw a MOSFET and a CMOS inverter, to see what the layout layers mean
- [ ] [Digital design guide](https://tinytapeout.com/digital_design/), lessons 1 to 3 in Wokwi, starting with the [Getting started with Wokwi video](https://www.youtube.com/watch?v=F1SwXF2ny4g) (skip the puzzles unless curious)

**3. The Verilog flow we will use**

- [ ] Watch [Tiny Tapeout 4: working with an HDL](https://www.youtube.com/watch?v=KbWb6xd9jFE), the video on the [HDL page](https://tinytapeout.com/hdl/)
- [ ] Read [Important rules for HDL designs](https://tinytapeout.com/hdl/important/): the `tt_um_` naming and the fixed port list
- [ ] Read [Testing your design](https://tinytapeout.com/hdl/testing/): cocotb, Icarus, gate-level tests
- [ ] Read [Hardening locally](https://tinytapeout.com/guides/local-hardening/)
- [ ] Skim the [specs](https://tinytapeout.com/specs/): clock, GPIO and pinout
- [ ] Watch [Get your submission ready](https://www.youtube.com/watch?v=fCGPKdmM3Dc) (from the [home page](https://tinytapeout.com/)): what to check before a design is submitted

**4. How others teach it (for next year's students)**

- [ ] Look through the [basic workshop](https://tinytapeout.com/guides/workshop/) and its [slides](https://docs.google.com/presentation/d/1NHFC3NHHFAzqK8HMGjxMHXJJ6r4j15dY86nk-boGDNM)
- [ ] Look through the [advanced workshop](https://tinytapeout.com/guides/advanced-workshop/) (Verilog with the VGA Playground) and its [slides](https://docs.google.com/presentation/d/1koJF3XoDFvxR71SGVdqbspB6SHDFMA6V-9mGp6Gb3EE/edit?usp=sharing)
- [ ] Optional: the webinar [Build Your First Chip with Tiny Tapeout](https://www.youtube.com/watch?v=UVZK-kmN7wc) (found by search, not linked from the site)

## Try it: the counter on the IHP template

Put our existing counter through Tiny Tapeout's own IHP flow, first on GitHub and then locally, without submitting anything.

1. On GitHub, open [ttihp-verilog-template](https://github.com/TinyTapeout/ttihp-verilog-template), click **Use this template**, and create a public repository in your account.
2. Copy the counter RTL from our flow repo into `src/`. Rename the top module to `tt_um_mdkamrulislam_counter` and give it the fixed port list (`ui_in`, `uo_out`, `uio_in`, `uio_out`, `uio_oe`, `ena`, `clk`, `rst_n`).
3. In `info.yaml`, set `top_module`, `source_files` and the title; describe the design in `docs/info.md`.
4. Adapt `test/test.py` to check the count, then run it locally:

   ```bash
   cd test
   pip install -r requirements.txt
   make -B
   ```
5. Push. Check that the `test`, `gds` and `docs` actions go green, then download the GDS from the `gds` run and open it in KLayout.
6. Harden the same repository locally, following the [local hardening guide](https://tinytapeout.com/guides/local-hardening/):

   ```bash
   export PDK_ROOT=~/ttsetup/pdk PDK=ihp-sg13g2 LIBRELANE_TAG=3.0.3
   pip install librelane==$LIBRELANE_TAG
   ./tt/tt_tool.py --create-user-config --ihp
   ./tt/tt_tool.py --harden --ihp
   ./tt/tt_tool.py --print-warnings --ihp
   ```
7. Compare the result with our own `make harden PDK=ihp-sg13g2` run: area, cell count, timing slack and run time. That comparison is a good first entry for the tool survey.

Do not submit at app.tinytapeout.com yet: a submission reserves a paid tile, and the shuttle choice waits on Prof. Popovici.

## What this means for our project

Tiny Tapeout already solves the "students make a chip" problem, so our flow should feed into it rather than compete with it.

- **Design limits:** one tile is about 160 × 100 µm, roughly 1,000 logic gates, with 8 inputs, 8 outputs and 8 bidirectional pins, at 50 MHz or more ([FAQ](https://tinytapeout.com/faq/)). The demonstrator must fit this, or we buy extra tiles.
- **Repository layout:** make our flow accept a Tiny Tapeout project (`src/`, `test/`, `info.yaml`) as it stands, so a student's design moves from our flow to a submission with no rewrite.
- **Tool versions:** Tiny Tapeout's local hardening pins LibreLane 3.0.3; our container ships LibreLane 3.1. Check that a design clean in one is clean in the other, and note any difference in the report.
- **IHP chips are on loan:** under Tiny Tapeout's IHP terms the chips stay IHP's property, are lent for two years by default, cannot be sold or passed on, and ship only within the EU and Switzerland ([Hackster](https://www.hackster.io/news/tiny-tapeout-opens-an-ihp-shuttle-for-your-open-source-chip-designs-but-beware-the-new-terms-77e0b292cae4)). Ireland is in the EU, so this should be fine for UCC, but it is worth telling Prof. Popovici.
- **Next year's class:** Tiny Tapeout sells class bundles: up to 5 projects with 1 board for €565, up to 25 with 3 boards for €2,195, up to 75 with 5 boards for €5,325 ([teaching page](https://tinytapeout.com/teaching/)). This is the likely route for the student chips he mentioned.
- **Timeline:** chips take 6 to 9 months to make, up to a year to arrive. A March 2027 IHP submission would not return silicon before the project ends, as the plan already assumes.
- **Two flows:** Tiny Tapeout's GitHub Actions flow and a local LibreLane flow may be the "both those open flows" he meant. Worth asking.

## Sources

Pages read on 30 Sep 2026; videos rechecked on 1 Oct 2026. YouTube itself could not be opened from here, so titles come from YouTube's embed data where it answered and otherwise from the Tiny Tapeout page that embeds the video.

- [tinytapeout.com](https://tinytapeout.com/), [HDL](https://tinytapeout.com/hdl/), [HDL rules](https://tinytapeout.com/hdl/important/), [Testing](https://tinytapeout.com/hdl/testing/), [Local hardening](https://tinytapeout.com/guides/local-hardening/), [Guides](https://tinytapeout.com/guides/), [FAQ](https://tinytapeout.com/faq/), [Teaching](https://tinytapeout.com/teaching/), [Making ASICs](https://tinytapeout.com/making_asics/), [Digital design](https://tinytapeout.com/digital_design/)
- [ttihp-verilog-template](https://github.com/TinyTapeout/ttihp-verilog-template) on GitHub
- [Hackster: Tiny Tapeout opens an IHP shuttle, but beware the new terms](https://www.hackster.io/news/tiny-tapeout-opens-an-ihp-shuttle-for-your-open-source-chip-designs-but-beware-the-new-terms-77e0b292cae4)
