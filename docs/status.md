# Status — LIVE

*Update at the end of every working session. Newest information at the top of each section.*

**Last updated:** 2026-11-23
**Phase:** 1 of 5 — Prepare and propose (Nov 17 → Dec 18)
**Next milestone:** Proposal defense, Friday 2026-12-18

## Where we are

- Topic chosen; research questions drafted; novelty checked (2026-11-17); plan and timeline written.
- Nothing has been run yet.
- **Topic is final (2026-11-21):** NCRC-V check done; the copra study is dropped. No adviser approval is needed before the proposal; the adviser and panel weigh in at the Dec 18 defense.

## This week (Nov 17–23)

**From Nov 23 on, the working list is the build checklist in `proposal/README.md`.**

- [x] NCRC-V visit done (2026-11-21). Copra study dropped.
- [ ] Optional: brief the adviser/instructor with the one-page pitch (no approval needed; useful for chapter-coverage question and linguist referral).
- [ ] ~~Ask the department about borrowing the GPU~~ Low priority: department PC is now last-resort backup only (liability risk).
- [ ] Ask VSU language faculty whether a Cebuano linguist can verify the error taxonomy. Also find a second Cebuano-speaking coder for RQ3 (see revised protocol).
- [ ] Laptop: check Task Manager → Memory → "Slots used"; set the page file to System managed.
- [x] Install llama.cpp; `llama-bench` CPU vs Vulkan (done in Lab 1; learning record only).
- [ ] Get the CebQA chapter (venue, year, CebQuAD size, license).
- [ ] Email the FilBench team asking whether anyone is working on Cebuano quantization or calibration.
- [ ] Check whether the copra title is registered anywhere that needs a change form.
- [ ] AWS: check credit amount and expiry; request G-instance vCPU quota (on-demand + spot) in ap-southeast-1; set a Budgets alert. Quota approval can take days — do it now.
- [~] Lab 1 done. Step 5: Qwen3-4B Q4_K_M on Vulkan = 39.5 t/s reading, 5.85 t/s writing vs CPU-only 34.8 / 4.99 → Vulkan iGPU modestly faster (in `compute.md`). Lab 1 complete. Results logged in `labs/lab-01-run-a-local-model.md`. Original task: follow `labs/lab-01-run-a-local-model.md` — install llama.cpp, chat with Qwen3-1.7B at Q4_K_M vs Q2_K in Cebuano/Tagalog/English, run `llama-bench` (learning only; thesis files are self-quantized).
- [x] Add a GitHub remote and push (backup). Done 2026-11-17 → github.com/jamir4270/project-sidapa. Confirm the repo is **private** on GitHub.

## Waiting on

| What | From | Since |
|---|---|---|
| GPU quota increase (G instances) | AWS | not requested yet |
| A linguist | VSU language faculty | — |

## Blockers / risks right now

- **RQ3 coders:** no linguist or second Cebuano coder yet. Name by Dec 14; Jan 31 cutoff, then fallback.
- **Time:** five weeks to the proposal defense. Protect the week-2 proof of concept.
- **Floor effect (Lab 1, 2026-11-22):** Qwen3-1.7B loops in Tagalog/Cebuano even at Q8_0. If a model scores near chance on Belebele Cebuano, it can't show compression loss. Week-2 proof of concept must run the Q8_0 floor check per candidate (proposed rule in `decisions.md`, open decision #1).

## Recent changes

- 2026-11-23 — **SRC feedback** (one member, after a verbal pitch with no handout): scope may be too small; novel
  beyond evaluating pretrained models?; needs focus (too many variables); "weak"; how is calibration valid?
  Claude's read: wide-but-shallow. Proposed (not decided): shrink RQ1 to a condition inside RQ2, deepen RQ2b
  (dose curve), and present calibration as the manipulated variable.
  **Calibration spec drafted, not locked** (D1–D7): D1 same genre for all three languages — Leipzig **news**
  (ceb newscrawl, tgl news, eng news/newscrawl; Jamir found that eng has no community corpus; years differ);
  D2 token-matched via equal `--chunks` at `-c 512` (N = 200 proposed, estimate); D3 language-ID cleaning;
  D4 dedup vs Belebele/FLORES and held-out set; D5 3 non-overlapping seeds; D6 held-out perplexity as a check that
  calibration took effect; D7 fixed build settings. Waiting on: Leipzig years, sizes and license line
  (docs say CC BY; a search snippet said "protected by copyright" → recheck).
  **Build checklist** for the proposal added to `proposal/README.md` (week-by-week, Jamir writes; Claude critiques).

- 2026-11-23 — New `methodology/objectives-and-metrics.md`: the four objectives (plain wording), metrics per objective
  (planned vs. new exploratory), headline numbers, and which tool produces each (llama.cpp makes/runs models; scoring is
  our Python). Tool claims tagged `VERIFY`. Linked from AGENTS map and experiment-design; logged in decisions.

- 2026-11-22 — **RQ3 kept, conditional** (logged in `decisions.md`): needs a linguist and/or second Cebuano coder, named
  by Dec 14 (target), confirmed by **Jan 31** (cutoff) or RQ3 falls back to an automatic failure analysis inside RQ2.
  Explanation-run items now sampled from questions that flipped right→wrong (Q8_0→Q2_K). Updated research-questions,
  error-taxonomy, experiment-design, open decision #4. (Dropping RQ3 was considered and rejected.)
  2026-11-23: both Word handouts now say RQ3 is conditional (Explained: sections 5 and 8, flipped-item sampling;
  Pitch Guide: script, Q10, ask #3 now also asks for a second Cebuano coder, summary row).

- 2026-11-22 — **Data analysis procedure adopted** (logged in `decisions.md`): paired clustered bootstrap for everything;
  four confirmatory claims (C1–C3 quantization gap at Q4_K_M/Q3_K_M/Q2_K, C4 calibration at Q2_K with equivalence
  margin), Bonferroni 98.75% CIs; H1/H3 secondary; rest exploratory; 3 calibration seeds (+~10,800 prompts, estimate).
  Closes the Nov 17 "no multiple-comparison correction / no headline tests" risk. Updated experiment-design (Statistics
  Steps 0–6, grid, fixed settings), research-questions hypotheses, ch4 outline, primer §14, timeline week 14.
  Thresholds still `TBD` (open decision #8): check the ±3 margin against week-2 pilot CIs.
  Both Word handouts updated the same day (Explained: hypotheses table, statistics rules table, known-gap warning removed, quiz answers; section 11 "Honest limits" panel Q&A removed, later sections renumbered; Pitch Guide: Q5 answer, prompt total ~205k, method row).

- 2026-11-22 — **Laptop speed benchmark dropped from the methodology** (specific objective 5 removed). "Offline" is motivation,
  backed by literature (4 candidate citations added to `literature/sources.md`, all `VERIFY`); file size per level goes in
  the results table. All four RQs run on AWS. Updated decisions, research-questions, experiment-design, compute, AGENTS,
  at-a-glance, primer, timeline, experiments README, lab 1, ch1 outline, both Word handouts. Lab 1 stays as a learning record.

- 2026-11-22 — Framing changed to **offline / resource-constrained use** (logged in `decisions.md`); new title decided: "Search and Shrink: Quantization and
  Calibration Losses for Cebuano, Tagalog and English in Small Offline Language Models" (updated in AGENTS.md, README,
  at-a-glance, proposal README, research-questions, lab 1, both Word handouts). Lab 1 run: Qwen3-1.7B (Q4, Q8), Qwen3-4B (Q4), Gemma 3 4B (Q4, Q2). Informal findings:
  Qwen3-1.7B loops in Tagalog/Cebuano even at Q8 (floor-effect risk); Gemma 3 4B strongest; Gemma Q2 collapses in
  Cebuano first, then Tagalog, while English survives (lost Philippine-specific knowledge). Logged 2026-11-22: results table in the lab file;
  proposed model-selection rule (open decision #1) and floor check in `experiment-design.md`; six new RQ3 starter categories
  in `error-taxonomy.md`. Jamir to confirm the Tagalog/Cebuano readings.

- 2026-11-21 — **NCRC-V task finished; copra study dropped.** Topic switch is final. Adviser has no say on the topic
  before the proposal (their say is at the defense), so no approval step. Updated AGENTS.md, decisions, copra note,
  NCRC-V meeting note, at-a-glance, README, timeline, primer. Word pitch guide reworked as a briefing + defense-pitch guide
  (no approval request).

- 2026-11-21 — Compute priority set: AWS → Kaggle/Colab → department PC (last resort; liability). Logged in `decisions.md`, `methodology/compute.md`.

- 2026-11-21 — **Main compute switched to AWS** (credits): EC2 `g4dn.xlarge` spot in ap-southeast-1, EBS, private S3,
  IAM, Budgets, Service Quotas; Kaggle backup; Colab Pro dropped. Logged in `decisions.md`; setup, budget (~$60–135,
  estimate) and workflow in `methodology/compute.md`; stale Colab mentions fixed in AGENTS.md, primer, at-a-glance,
  novelty-check, timeline, ch1. Word handouts regenerated with the AWS plan and priority order (2026-11-21).
  Also discussed (no doc change yet): calibration sets should be token-matched across languages and built from
  several random seeds — proposed for RQ2b, awaiting Jamir's go-ahead.

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
- Open risks flagged, not yet acted on: Qwen3 thinking mode must be disabled and logged; ~~statistics plan has no
  multiple-comparison correction or pre-declared headline tests~~ (fixed 2026-11-22); check that Leipzig calibration text is news, not
  bot-written Wikipedia; re-check for newer small models before fixing the model list (Dec 7).

- 2026-11-17 — Workspace created. RQs reframed after novelty check: compression (RQ2) and calibration (RQ2b) are the core; search (RQ1) is supporting.
