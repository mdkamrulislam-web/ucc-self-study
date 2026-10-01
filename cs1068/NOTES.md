# CS1068 Introductory Programming in Python — guide notes

- **Page:** `cs1068/index.html` (title "CS1068 Study Guide")
- **Original artifact:** none. Started 1 Oct 2026 in the repo from a Claude Code session (project "CS1068 Introductory Programming in Python"), so it is **edited here directly**, like EE6041.
- **Progress key:** `cs1068-guide-done-v1` → `l1`…`l15`
- **Last content update:** 1 Oct 2026 (lectures 0.1–3.1)
- **Course material:** the project's shared files, `CS1068 - Introductory Programming in Python/` (Week 0–3 slides, lab and practice sheets, Quizzes 2–3, Canvas notices, Winter 2022–23 to 2025–26 papers). Kamrul's own lab submissions are in `Week N/Lab/My Submissions/`; the guide doesn't use them.

## Module facts
- Lecturer: Dr Tatiana Tabirca. Co-taught as CS1068 / CS6501 / CS6506 (same lectures and labs; the Canvas page is labelled CS1068). Assumes no programming background.
- Lectures Tue 2–3 pm BHSC G01, Thu 2–3 pm BHSC G05 (Thu 5 Nov in WGB G20). Labs Wednesdays, WGB G.21, 10–11 or 11–12, from 23 Sep.
- Python 3, VS Code, Ubuntu in the labs.
- Assessment (Canvas): mid-term quiz 5% (Wed 28 Oct, in the lab slot, mostly multiple choice, like the weekly quizzes); programming assignment 10% (released 28 Oct; Canvas says due "Wednesday, 5 November 2026" but 5 Nov is a Thursday); programming project 15% (spec on Thu 5 Nov; rest of the notice was cut off in the PDF); final exam 70%. Lecture 0.1 said "in-class test Thu 29 Oct"; Canvas is newer.
- Lectures 0.1 and 0.2 are not examined (Canvas).
- Exam format (all four past papers): 90 min, 70 marks, answer all four questions, handwritten; no calculators from 2024–25. Q1 short parts (complete program, fix errors, explain/document code), Q2 functions with loops/random, Q3 lists of tuples/dicts, Q4 text files. Internal examiner on the papers: Dr Kieran Herley.
- **GenAI:** "Phase 1" (now) forbids using AI to generate solutions for labs and practice sheets; GenAI is not permitted for the mid-term quiz or the assignment. **Never put lab, practice, quiz-5% or assignment answers in the guide**, and don't write Kamrul's lab code. Explaining ideas with the lecturer's own examples and past papers is fine. The weekly quizzes are ungraded and show answers after submission, so the guide explains them.

## Coverage

| Lecture | Lessons |
|---|---|
| 0.2, 1.1 Thinking like a programmer, programming overview | 1 From problem to program · 2 Your first program |
| 1.2 Variables, data types, operators | 3 Variables and assignment · 4 Data types · 5 Operators and precedence |
| 2.1 Input, output, type conversion | 6 Type conversion · 7 input() gives a string · 8 print(), sep and end · 9 f-strings |
| 2.2 Conditional statements | 10 The if statement · 11 else and elif · 12 Nested if, and/or/not |
| 3.1 Functions | 13 Defining and calling · 14 return vs print · 15 Docstrings and built-ins |

Extras: Python playground, weekly quizzes 2–3 explained, labs and deadlines (topics only, no answers), exam practice (4 past-paper Q1 openers with solutions + 3 exam-style questions), still to come (topics mapped to past-paper questions), cheat sheet.

## How this guide is built
- One self-contained HTML file. CSS copied from the CS6322 guide with a blue accent; no maths library.
- Code examples are `<pre class="py" data-run>` with HTML-escaped code, followed by `<pre class="out">` showing the real output. The page highlights them on load and adds a **Try it** button that turns the block into an editor and runs it with **Pyodide 0.26.4** from cdn.jsdelivr.net (loaded on first use, ~10 MB). `input()` uses a browser prompt, pre-filled from `data-stdin` (lines separated by `&#10;`). A trailing `  #!!` on a line marks it red.
- **After editing, run `python3 tools/check_examples.py cs1068/index.html`**: it runs every example in Python and fails on any output that doesn't match the page.
- For local testing of the runner without the CDN, set `window.CS1068_PYODIDE` to a folder holding the npm `pyodide@0.26.4` files.

## To do
- [ ] After Practice 3 closes (7 Oct): add 2025–26 Q1(iii) ("largest of three" with errors) to Exam practice. Held back because it overlaps Practice 3 exercise 3.
- [ ] Next lectures (expected: loops, then strings, lists, dictionaries, files) as new lessons; move exam questions from "Still to come" into practice as each topic lands.
- [ ] Before 28 Oct: a mid-term quiz revision section in the weekly-quiz style.
