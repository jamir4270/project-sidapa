# Status — LIVE

*Update at the end of every working session. Newest information at the top of each section.*

**Last updated:** 2026-11-20
**Phase:** 1 of 5 — Prepare and propose (Nov 17 → Dec 18)
**Next milestone:** Proposal defense, Friday 2026-12-18

## Where we are

- Topic chosen; research questions drafted; novelty checked (2026-11-17); plan and timeline written.
- Nothing has been run yet.
- The switch from the copra study is **not official**. It depends on the NCRC-V visit and the adviser's approval.

## This week (Nov 17–23)

- [ ] NCRC-V visit with the questionnaire (expert help, dataset availability, complexity). Record answers in `meetings/`.
- [ ] Adviser meeting with the one-page pitch (`at-a-glance.md` + RQs). Get a yes / no / "show me a proof of concept."
- [ ] Ask the department about borrowing the GPU: which GPU, remote access, booking rules, storage.
- [ ] Ask VSU language faculty whether a Cebuano linguist can verify the error taxonomy. Also find a second Cebuano-speaking coder for RQ3 (see revised protocol).
- [ ] Laptop: check Task Manager → Memory → "Slots used"; set the page file to System managed.
- [ ] Install llama.cpp; run `llama-bench` on one 4B model, CPU vs Vulkan; record numbers in `methodology/compute.md`.
- [ ] Get the CebQA chapter (venue, year, CebQuAD size, license).
- [ ] Email the FilBench team asking whether anyone is working on Cebuano quantization or calibration.
- [ ] Check whether the copra title is registered anywhere that needs a change form.
- [x] Add a GitHub remote and push (backup). Done 2026-11-17 → github.com/jamir4270/project-sidapa. Confirm the repo is **private** on GitHub.

## Waiting on

| What | From | Since |
|---|---|---|
| Answers on expert help and data | NCRC-V | 2026-11-17 |
| Approval of the topic switch | Adviser | 2026-11-17 |
| GPU borrowing rules | Department | — |
| A linguist | VSU language faculty | — |

## Blockers / risks right now

- **Time:** five weeks to the proposal defense. Protect the week-2 proof of concept.

## Recent changes

- 2026-11-20 — Two Word handouts: `docs/Search-and-Shrink-Explained.docx` (full explainer with analogies) and
  `docs/Search-and-Shrink-Pitch-Guide.docx` (script, Q&A bank, asks, one-page leave-behind). RQ3 research brief
  (`reference/reports/2026-11-20 RQ3 standardized error taxonomy brief.md`): proposed protocol now in
  `methodology/error-taxonomy.md` (automatic language ID, published starting typologies, hybrid coding with ending
  conditions, pilot, two blind coders, Krippendorff's alpha with pre-set threshold). **Pending Jamir/adviser approval.**
  New RQ3 sources added to `literature/sources.md` as `VERIFY` (none opened yet).

- 2026-11-17 — First Claude session. Fixed stale text: novelty-check adviser script (now says linguist + Colab Pro),
  primer imatrix default (llama.cpp uses none by default, `VERIFY`), at-a-glance hypothesis softened, grid-size math
  added to `methodology/compute.md` (≈194k prompts; laptop can't run it). `git init` + first local commit, then pushed to GitHub `origin/main`.
- 2026-11-19 — Added `.claude/settings.json` so Claude is not listed as a co-author on commits or PRs.
- Open risks flagged, not yet acted on: Qwen3 thinking mode must be disabled and logged; statistics plan has no
  multiple-comparison correction or pre-declared headline tests; check that Leipzig calibration text is news, not
  bot-written Wikipedia; re-check for newer small models before fixing the model list (Dec 7).

- 2026-11-17 — Workspace created. RQs reframed after novelty check: compression (RQ2) and calibration (RQ2b) are the core; search (RQ1) is supporting.
