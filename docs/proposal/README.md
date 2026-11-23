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
is chapters I–IV. Still to ask: citation style, FM-VPA-09 copy, required appendices.
Full section-by-section map: `../Search-and-Shrink-Proposal-Checklist.docx`.

## Build checklist (Nov 23 → Dec 18)

*Added 2026-11-23. Jamir writes every chapter; this list is the order to learn and write in. Each task says what
to read first, what to produce, and when it is done. Tick `[x]` as you go. Bring questions to Claude while writing:
"critique this section", "is this claim tagged right", "explain X" — not "write this".*

**Writing order and why:** definitions (learn the vocabulary) → literature (learn the field and the gap) →
methodology (the design; where the SRC questions live) → introduction (last, because it summarizes the rest).

### Week A — Nov 23–29: foundations + pilot

- [ ] **Admin (today):** ask the adviser (1) citation style for Literature Cited, (2) a copy of FM-VPA-09 and the
  Gantt format, (3) how and when to book the panel, (4) required appendices, (5) whether an AI-use disclosure is
  needed. Done when: answers written in `../meetings/`.
- [ ] **Template skeleton:** title page and front matter in the VSU template. Done when: saved.
- [ ] **Read the big picture:** `../at-a-glance.md`, then `../primer.md` (~3 h, estimate). Write down every
  sentence you could not explain to a classmate. Done when: a question list exists; bring it to Claude.
- [ ] **Ch III — Definitions** (`ch3-definition-of-terms.md`): two-column glossary sorted A–Z; define each listed
  term in your own words, as used in this study. Learn from: `../primer.md` glossary. Done when: every term has 1–3 sentences; unsure ones marked `?`.
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
  the last section states the gap in one paragraph.
- [ ] **Decide the SRC focus question:** shrink RQ1 to a condition inside RQ2? Add a calibration dose curve?
  Learn from: the Nov 23 SRC notes in `../status.md`. Done when: logged in `../decisions.md`. *Do this before Ch IV.*
- [ ] **Lock the calibration spec** (D1–D7). Done when: logged in `../decisions.md`.
- [ ] **Close open decisions due Dec 7** in `../decisions.md`: #1 model list (use pilot floor check),
  #2 prompt language, #6 CebQuAD, #7 RQ3 protocol.
- [ ] **Ch IV — Methodology** (`ch4-methodology.md`). Learn from: `../methodology/` (research-questions,
  experiment-design, objectives-and-metrics, data-and-licensing, compute, error-taxonomy). Required parts: chapter
  introduction; 1. Research Design with the Research Framework figure; 2. study-specific sections; 3. Ethical
  Considerations (new: copyright, consent and credit for the linguist/coder, no personal data, AI-use disclosure
  if required). Done when: you can answer "how do you know the calibration is valid?" from the text alone.
- [ ] **Ch I — Introduction** (`ch1-introduction.md`), written last, with the Gantt chart in section 6. Done when:
  objectives match Ch IV exactly.
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
