# Status — LIVE

*Update at the end of every working session. Newest information at the top of each section.*

**Last updated:** 2026-11-21
**Phase:** 1 of 5 — Prepare and propose (Nov 17 → Dec 18)
**Next milestone:** Proposal defense, Friday 2026-12-18

## Where we are

- Topic chosen; research questions drafted; novelty checked (2026-11-17); plan and timeline written.
- Nothing has been run yet.
- **Topic is final (2026-11-21):** NCRC-V check done; the copra study is dropped. No adviser approval is needed before the proposal; the adviser and panel weigh in at the Dec 18 defense.

## This week (Nov 17–23)

- [x] NCRC-V visit done (2026-11-21). Copra study dropped.
- [ ] Optional: brief the adviser/instructor with the one-page pitch (no approval needed; useful for chapter-coverage question and linguist referral).
- [ ] ~~Ask the department about borrowing the GPU~~ Low priority: department PC is now last-resort backup only (liability risk).
- [ ] Ask VSU language faculty whether a Cebuano linguist can verify the error taxonomy. Also find a second Cebuano-speaking coder for RQ3 (see revised protocol).
- [ ] Laptop: check Task Manager → Memory → "Slots used"; set the page file to System managed.
- [ ] Install llama.cpp; run `llama-bench` on one 4B model, CPU vs Vulkan; record numbers in `methodology/compute.md`.
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

- **Time:** five weeks to the proposal defense. Protect the week-2 proof of concept.
- **Floor effect (Lab 1, 2026-11-22):** Qwen3-1.7B loops in Tagalog/Cebuano even at Q8_0. If a model scores near chance on Belebele Cebuano, it can't show compression loss. Week-2 proof of concept must run the Q8_0 floor check per candidate (proposed rule in `decisions.md`, open decision #1).

## Recent changes

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
- Open risks flagged, not yet acted on: Qwen3 thinking mode must be disabled and logged; statistics plan has no
  multiple-comparison correction or pre-declared headline tests; check that Leipzig calibration text is news, not
  bot-written Wikipedia; re-check for newer small models before fixing the model list (Dec 7).

- 2026-11-17 — Workspace created. RQs reframed after novelty check: compression (RQ2) and calibration (RQ2b) are the core; search (RQ1) is supporting.
