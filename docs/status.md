# Status — LIVE

*Update at the end of every working session. Newest information at the top of each section.*

**Last updated:** 2026-11-24
**Phase:** 1 — Prepare and propose (→ Dec 18)
**Next milestones:** SRC meeting + FM-VPA-06/07, **Fri 2026-11-27**; full draft to adviser Dec 7; proposal defense **Fri 2026-12-18**

## Where we are

- **New study (2026-11-24):** fine-tuning and evaluating an embedding model for Cebuano passage retrieval
  (`decisions.md`). Approval so far covers the direction, not a locked design; the RQs are not written yet.
- The "Search and Shrink" compression study is **archived** in `../archive/2026-11-search-and-shrink/` (git tag
  `search-and-shrink-final`). Reusable pieces are listed in that folder's README.
- Nothing has been run yet.

## This week (Nov 24–27)

- [x] Archive Search and Shrink; set the repo up for the new study (2026-11-24).
- [x] **Novelty search (first pass, 2026-11-24):** `literature/novelty-check.md`. No Cebuano embedder fine-tune or human-written
  Cebuano retrieval test set found (`UNCONFIRMED`). Still to do: direct ACL Anthology / Scholar / SEACrowd / MTEB task-list checks.
- [~] **Read the existing studies** (Armenian and Nigerian papers read at abstract/HTML level; CebQA paywalled): Navasardyan et al. 2026 (Armenian, LoResLM), the WiNLP 2025 Nigerian-language
  BGE-M3 paper, CebQA (Lagumbay & Roxas, NiDS 2025). One line each: what they did / what they did not do. Upgrade tags only after opening.
- [~] **CebQuAD:** Jamir reports it is usable (2026-11-24; basis — license text or author permission — to be recorded in
  `methodology/data-and-licensing.md`). QA pairs GPT-4o-mini-generated, speaker-validated (snippet); size still unknown.
- [~] **CebuaNER:** Jamir reports it is usable (2026-11-24). CC BY-NC 4.0 (card); card asks for an email before benchmark use →
  keep that email (or the permission) on record.
- [ ] **Test-set feasibility:** can ~300–500 Cebuano question–passage pairs be written/checked in December (estimate)?
- [ ] Draft RQs, IV/DV, metrics and validation plan; then one-page summary for Friday.
- [ ] Fill in FM-VPA-06/07 (check whether they need a title/topic).
- [ ] AWS: credit amount/expiry, GPU quota request, Budgets alert (still useful; smaller workload).

## Waiting on

| What | From | Since |
|---|---|---|
| GPU quota increase (G instances) | AWS | not requested yet |

## Blockers / risks right now

- **Time:** three days to the SRC meeting with no RQs yet; 3.5 weeks to the defense.
- **Test data:** Belebele retrieval is near ceiling (e5-large-instruct 0.875 ceb nDCG@10) and can't double as training
  data; the study needs a harder held-out Cebuano test set. This is the main risk.
- **Training data:** Cebuano query–passage pairs must be built (translation or LLM generation); small LLMs write poor
  Cebuano (Lab 1, archived).
- **Novelty unconfirmed:** the "no Cebuano embedder fine-tune exists" claim is from search snippets only.

## Recent changes

*Entries before 2026-11-24 refer to files now under `../archive/2026-11-search-and-shrink/` (same relative paths).*

- 2026-11-24 — **Switched to study B and archived Search and Shrink.** Final state committed and tagged
  (`search-and-shrink-final`); old-study docs moved with `git mv` to `archive/2026-11-search-and-shrink/` (README explains
  why and what was reused). Live AGENTS.md, README, KICKSTART and proposal README updated with banners/links; AGENTS.md
  sections 1–5 still describe the old study until the new RQs are locked.

- 2026-11-24 — **Scope discussion (not decided):** Jamir questioned why RQ1 (search) exists. History: it survived from merging
  two Nov 17 ideas after its novelty was taken. Claude's recommendation: drop RQ1 as an RQ; frame the study as the compressed
  *reader* for offline Cebuano document Q&A; a multi-passage distractor condition is a candidate (novelty UNCONFIRMED).
  Jamir also asked about pivoting to fine-tuning an embedder for Cebuano retrieval: quick scan found the method established
  for other low-resource languages (Armenian, Nigerian languages) and no Cebuano fine-tune paper (UNCONFIRMED); new sources
  logged in `literature/sources.md`. Decide at the Wed scope session.

- 2026-11-24 — **Adviser approved the topic change** (closes the manual's change-of-topic risk; logged in
  `decisions.md`). SRC already formed; FM-VPA-06/07 to be signed **Fri Nov 27**. To be ready, the scope decision
  (SRC focus question) and the calibration spec lock moved from Week B to **Wed–Thu this week**. Checklist v2.1
  (README + docx) re-planned by day.

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
  Same day: required chapter structure received (proposal = Ch I–IV; Gantt in Ch I §6; A–Z two-column glossary;
  Ch IV adds chapter intro, Research Framework figure, Ethical Considerations). Checklist updated; Word version with a
  section-by-section map: `Search-and-Shrink-Proposal-Checklist.docx`. Open decision #3 mostly answered (citation
  style still to ask).
  Later the same day: **DCST thesis manual (v2, Sep 2026) received**; checklist docx rebuilt as v2 (formatting rules,
  forms FM-VPA-06/07/08/09/11, HERC ethics review, proposal rubric). Citation style = **APA 7** (decision #3 closed
  except FM-VPA-09 and appendices). **New risks:** (1) the manual's change-of-topic process says discuss with the adviser
  first; the copra outline was defended in May 2026, so the Nov 21 "no adviser step" note may be wrong; settle
  this week. (2) RQ3 coders may need HERC clearance, which can start only after FM-VPA-09 is signed. (3) Model licenses
  (Gemma, Llama) must be in the license table.

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
