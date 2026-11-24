# Proposal Chapters

**Working title:** Search and Shrink: Quantization and Calibration Losses for Cebuano, Tagalog and English in Small Offline Language Models

Drafts for the **Dec 18, 2026** proposal defense, written in Markdown and exported to the VSU template at the end.

## Chapter structure

The defended copra outline (VSU DCST, May 2026) used this order, so these drafts follow it:

| File | Chapter | Status |
|---|---|---|
| `ch1-introduction.md` | I. Introduction (background, problem, objectives, significance, scope and limitations, time and place) | Outline |
| `ch2-review-of-literature.md` | II. Review of Literature | Outline |
| `ch3-definition-of-terms.md` | III. Operational Definition of Terms | Outline |
| `ch4-methodology.md` | IV. Methodology | Outline |

**Required structure (received 2026-11-23):** front matter (title page, approval sheet, table of contents);
Ch I with the **Gantt chart inside section 6 (Time and Place)**; Ch II subsections by theme; Ch III a **two-column
glossary sorted A–Z**; Ch IV = chapter introduction, 1. Research Design with a **Research Framework figure**,
2. study-specific sections, 3. **Ethical Considerations**; back matter (Literature Cited, Appendices). So the proposal
is chapters I–IV. Still to ask: FM-VPA-09 copy, required appendices, whether the proposal needs a Declaration of Originality.

**DCST Undergraduate Thesis Manual for BSCS (v2, Sep 2026), key rules** (received 2026-11-23; local copy only):
APA 7th with DOIs; problems as declarative statements, not questions; 3–5 measurable specific objectives; Scope and
Limitations as one subsection; simple month-level Gantt; Ch II subheadings end with relation/adoption/gap, recent
sources (≤5 years) preferred; Ch III borderless A–Z table, no formulas; Ch IV includes the ethical review process and
an Ethical Considerations section (needed for HERC); generative-AI use declared (tool, purpose, scope); A4, Times New
Roman 12, margins 1.5 in top/left, 1.0 in bottom/right, double-spaced, borderless tables. Forms: FM-VPA-06/07 before
the defense; FM-VPA-08, -11, -09 after; then HERC. Proposal rubric: literature synthesis 20%, methodology 30%.
Full section-by-section map, formatting rules, process and rubric: `../Search-and-Shrink-Proposal-Checklist.docx` (v2).

## Build checklist (Nov 23 → Dec 18)

*Added 2026-11-23. Jamir writes every chapter; this list is the order to learn and write in. Each task says what
to read first, what to produce, and when it is done. Tick `[x]` as you go. Bring questions to Claude while writing:
"critique this section", "is this claim tagged right", "explain X" — not "write this".*

**Writing order (changed 2026-11-24):** Ch I (rough draft) → Ch II → Ch III → Ch IV → revise Ch I to match Ch IV.
Ch III defines terms *as used in the text*, so it is built from the chapters before it: keep a running list of
terms while writing Ch I–II, write Ch III from that list, then add any new terms after Ch IV. Ch I is drafted first
but revised last, because its objectives and scope must match the methodology exactly.

### Week A — Nov 23–29: foundations + pilot

- [x] **Topic change:** adviser approved (2026-11-24). SRC already formed; paperwork pending.
- [ ] **By Thu Nov 26 (ready for Friday):** read at-a-glance + primer (Tue); Leipzig check (Tue); question session
  with Claude and **decide the scope / SRC focus question** (Wed); **lock the calibration spec**, write a one-page
  study summary in your own words (printed), one-line answers to the five SRC comments, fill in FM-VPA-06/07 (Thu).
- [ ] **Fri Nov 27: meet the SRC, get FM-VPA-06/07 signed.** Also ask: FM-VPA-09 copy, defense booking, appendices,
  whether the proposal needs a Declaration of Originality. Done when: answers in `../meetings/`.
- [ ] **Template skeleton:** title page and front matter in the VSU template. Done when: saved.
- [ ] **Read the big picture:** `../at-a-glance.md`, then `../primer.md` (~3 h, estimate). Write down every
  sentence you could not explain to a classmate. Done when: a question list exists; bring it to Claude.
- [ ] **Ch I — rough draft** (`ch1-introduction.md`, weekend after Friday): background, problem as declarative
  statements, objectives, significance, scope and limitations, time and place. Build on the Friday one-page summary.
  Start the running term list. Done when: 1–2 rough pages exist.
- [ ] **Pilot (proof of concept):** one 4B model, Q8_0/Q4_K_M/Q2_K, 100 Belebele questions × 3 languages;
  reproduce MTEB BM25 Cebuano (0.784). Learn from: `../labs/lab-01-run-a-local-model.md`, `../../experiments/README.md`.
  Done when: one accuracy table + floor check result. *This is the strongest thing you can show the panel.*
- [ ] **Leipzig check** (calibration D1): years and largest sizes for ceb newscrawl, tgl news, eng news/newscrawl;
  license line from the FAQ page. Done when: pasted to Claude and logged.
- [ ] **AWS GPU quota request** (takes days; not needed until January, but start the clock). Done when: requested.

### Week B — Nov 30–Dec 6: literature + design decisions

- [ ] **Read the core papers** in `../literature/sources.md` → "Core prior work". Minimum: Waskito et al.,
  Marie & Fujita, Marchisio et al., Chimoto et al., MMTEB, FilBench, CebQA, Miller 2024. For each: one line
  "what they did / what they did not do". Open each source and upgrade its tag only after reading it.
- [ ] **Ch II — Review of Literature** (`ch2-review-of-literature.md`): write each section, ending with "what is
  still missing". Learn from: your one-line notes, `../literature/novelty-check.md` (safe wording). Done when:
  the last section states the gap in one paragraph. Add new terms to the running list.
- [ ] **Ch III — Definitions** (`ch3-definition-of-terms.md`): from the running term list; borderless two-column
  table sorted A–Z; each term as used in this study, no formulas. Done when: every term used in Ch I–II is defined.
- [ ] **Close open decisions due Dec 7** in `../decisions.md`: #1 model list (use pilot floor check),
  #2 prompt language, #6 CebQuAD, #7 RQ3 protocol.
- [ ] **Ch IV — Methodology** (`ch4-methodology.md`). Learn from: `../methodology/` (research-questions,
  experiment-design, objectives-and-metrics, data-and-licensing, compute, error-taxonomy). Required parts: chapter
  introduction; 1. Research Design with the Research Framework figure; 2. study-specific sections; 3. Ethical
  Considerations (new: copyright, consent and credit for the linguist/coder, no personal data, AI-use disclosure
  if required). Done when: you can answer "how do you know the calibration is valid?" from the text alone.
  Then add any new Ch IV terms to Ch III.
- [ ] **Revise Ch I** to match Ch IV, and add the Gantt chart in section 6. Done when: objectives match Ch IV exactly.
- [ ] **Literature Cited:** only sources the chapters cite, each opened.
- [ ] **Dec 7: full draft to the adviser.**

### Week C — Dec 7–13: revise + prepare to defend

- [ ] Revise with adviser comments; log any RQ/scope changes in `../decisions.md`.
- [ ] Gantt chart from `../timeline.md`.
- [ ] Slides (10–15 min, estimate): lead with the calibration question, show the pilot table.
- [ ] One-page printed handout for every panelist (the SRC reacted to a verbal pitch with nothing to read).
- [ ] Name the RQ3 linguist / second coder (target Dec 14).
- [ ] Panel date confirmed.

### Week D — Dec 14–18: dry runs + defend

- [ ] Dry run 1 with a classmate; practise answers to the five SRC comments (scope, novelty, focus, "weak",
  calibration validity).
- [ ] Final export to the VSU template; strip evidence tags only here.
- [ ] **Defend Dec 18.** Record every panel comment in `../meetings/`.

## Rules for drafting

- Every factual claim carries an evidence tag until verified (see AGENTS.md §6). Strip tags only at export.
- Cite only sources in `../literature/sources.md`.
- Use the safe novelty wording from `../literature/novelty-check.md`.
- Keep the copra outline's good habits: clear scope, ethics section, Gantt chart, operational definitions.
- Avoid the copra outline's mistakes: unsourced numbers, outdated model claims, overclaiming ("mathematically exact").
