# Decision Log

*Append-only. Newest first. Each entry: date, decision, reason, who decided. Open decisions at the bottom.*

## Decisions

### 2026-11-22 — Keep RQ3, conditional on finding coders; fallback by Jan 31; sample flipped items
- **Decision:** RQ3 (error taxonomy) stays, **on condition** that the people it needs are confirmed: a Cebuano linguist,
  a second native-speaker coder, or both. Target to name them: **Dec 14** (open decision #4). **Cutoff: Jan 31, 2027.**
  If nobody is confirmed by then, RQ3 as a coded taxonomy is dropped and replaced by an automatic analysis inside RQ2
  (no new RQ): parse-failure rate and answer collapse (e.g., always one letter) per level, count of questions that flip
  right→wrong from Q8_0 to Q2_K per language, optionally tokenizer fertility (tokens per word) per language.
- **Minimum roles:** linguist = approve the codebook + settle unresolved disagreements (a few hours, estimate);
  second coder = blind-label the same 100 items (~3–5 h, estimate). With only one person, a second coder matters more
  (agreement needs two coders); a linguist alone can verify categories but gives no agreement score.
- **Sampling change:** explanation-run items are drawn from Cebuano questions that **flipped right (Q8_0) → wrong
  (Q2_K)** in RQ2, plus a matched set that stayed right, so RQ3 studies the mistakes compression caused. RQ2 results
  exist before the RQ3 block (Feb 22), so this fits the timeline.
- **Reason:** RQ3 explains *why* Cebuano loses more, which RQ2 can't; but it depends on people not yet found and falls
  during job applications. A cutoff with a planned fallback means no half-finished RQ. Considered dropping RQ3
  (multiple-choice answers carry no text to code; weak link to RQ2); the flipped-item sampling fixes the link.
- **By:** Jamir, on Claude's recommendation.

### 2026-11-22 — Data analysis procedure: paired clustered bootstrap, four confirmatory claims
- **Decision:** One inferential method for all RQs: the paired clustered bootstrap (10,000 passage resamples, same
  resamples for every condition). Only four pre-registered confirmatory claims: C1–C3 = quantization gap (Cebuano drop
  − English drop) at Q4_K_M, Q3_K_M, Q2_K; C4 = Cebuano-calibrated − English-calibrated Cebuano accuracy at Q2_K, with a
  three-way outcome (helps / equivalent within ±margin / inconclusive). Pooled across models; Bonferroni → 98.75% CIs.
  H1 (search) and H3 (errors) are secondary at 95%; everything else exploratory. 3 calibration seeds per language
  (seeds 2–3 at Q2_K, Cebuano test only: ~10,800 extra prompts, ~3 h, estimate). ANOVA, GLMM, McNemar, Cochran's Q,
  Wilcoxon and chi-square not used (GLMM optional robustness check). Detail: `methodology/experiment-design.md`.
- **Reason:** Scores are binary and items repeat, so ANOVA doesn't fit; one method is less to code, explain and get
  wrong; a small confirmatory family controls false positives; the equivalence outcome makes a likely null RQ2b
  result defensible; seeds separate "calibration language" from "lucky sample".
- **Still open:** equivalence margin (proposed ±3 points), agreement threshold (proposed 0.6), parse-failure flag
  (proposed 5%) — open decision #8; lock before Jan 4.
- **By:** Jamir, on Claude's recommendation.

### 2026-11-22 — Drop the laptop speed benchmark from the methodology; "offline" is motivation, backed by literature
- **Decision:** Remove specific objective 5 (speed and memory per quantization level on the T14). "Offline" stays as the
  study's **motivation** (why models are compressed), supported by verified citations in chapters 1–2, not a claim the
  study tests. Report **file size per quantization level** in the main results table (it comes free from the AWS runs).
  Lab 1 benchmarks stay in `labs/` and `compute.md` as learning records, not thesis data. All four RQs run on AWS.
- **Reason:** No RQ needs the laptop; accuracy doesn't depend on the machine. One device can't support general speed
  claims. File size is device-independent and is the stronger evidence of offline fit. Keeps the study lean.
- **Supersedes:** the laptop-benchmark part of the 2026-11-22 framing entry below.
- **By:** Jamir, on Claude's recommendation.

### 2026-11-22 — New working title
- **Decision:** "Search and Shrink: Quantization and Calibration Losses for Cebuano, Tagalog and English in Small
  Offline Language Models." Replaces "…Measuring Retrieval and Quantization Losses in a Small Cebuano
  Question-Answering Pipeline on Consumer Hardware."
- **Reason:** Leads with the core contribution (RQ2 quantization + RQ2b calibration), names all three languages, and
  uses the offline framing. Search (RQ1) is supporting and introduced in chapter 1.
- **By:** Jamir (option 3 of three drafted).

### 2026-11-22 — Frame the study around offline, resource-constrained use (not "consumer hardware")
- **Decision:** Motivation and title say **offline / resource-constrained devices** (old laptops, cheap PCs, phones)
  instead of "consumer hardware." The T14 speed and memory benchmark per quantization level stays as a small
  supporting objective (specific objective 5), not a research question. *(Benchmark part superseded the same day: dropped; see above.)*
- **Reason:** Compression only matters because models must fit small, offline devices; "offline / resource-constrained"
  keeps that reason without tying claims to one device class. Accuracy results don't depend on the machine, so cloud
  runs don't conflict. The laptop benchmark gives developers a practical accuracy–size–speed table at low cost.
- **Title:** decided the same day (see the entry above).
- **By:** Jamir, on Claude's recommendation.

### 2026-11-21 — Copra study dropped; Search and Shrink is the thesis
- **Decision:** NCRC-V reality check completed; Jamir is not pursuing the copra study. "Search and Shrink" is the thesis
  topic for the Dec 18 proposal defense.
- **Process note:** The adviser does not approve the topic before the proposal; the adviser and panel weigh in at the
  proposal defense. No pre-approval step is needed.
- **By:** Jamir.

### 2026-11-21 — Compute priority order: AWS → Kaggle/Colab → department PC
- **Decision:** (1) **AWS** is the primary compute (entry below). (2) **Kaggle (free) and Colab** are the second tier:
  backup if AWS quota or credits fall through. Colab is reinstated as a backup only; because it assigns GPUs per
  session, any comparison run there must stay on one GPU type, recorded per run. (3) The **department research PC** is
  last resort only. Never mix machines inside one comparison; pick the machine before a comparison starts.
- **Reason:** The department PC would be dedicated to Jamir, but he would be personally liable for any problem with the
  machine (hardware, software, data). AWS keeps that risk off him and is paid from credits.
- **By:** Jamir.

### 2026-11-21 — Use AWS (with credits) as main compute; replaces Colab Pro
- **Decision:** Run the full grid (RQ2, RQ2b, conditions, extra tasks, RQ3 explanation run) on AWS EC2 `g4dn.xlarge`
  (1× NVIDIA T4, 16 GB) in **ap-southeast-1 (Singapore)**: spot for unattended grid runs, on-demand for short
  debugging. **All RQ2/RQ2b comparisons run on this one instance type.** Services: EC2, EBS (only while working),
  private S3 bucket (calibration text, imatrix files, results), IAM (non-root user), AWS Budgets (alerts), Service Quotas
  (GPU quota). Backups: see the priority-order entry above; never mix machines inside one comparison. No laptop speed
  benchmark in the thesis (dropped 2026-11-22). Colab Pro is dropped.
- **Reason:** Jamir has AWS credits. AWS gives a fixed, chosen GPU type every run (Colab assigns GPUs per session, which
  threatens "one machine per comparison"), no session caps for hands-off January runs, one storage place, and
  job-relevant cloud skills. Cost estimate ~$30–40 spot / ~$75–100 on-demand compute for ~100–135 GPU-h, plus
  ~$25–30 storage (all estimates; prices from third-party trackers, `VERIFY` in the AWS console).
- **Conditions / still open:** credit amount, program and expiry date `TBD` (must cover January–March); GPU quota
  increase requested and approved; budget alert set; instance type confirmed by timing the week-2 proof of concept
  (cost per 1,000 prompts). `g5g.xlarge` (ARM, T4G, ~$0.59/h) is the only alternative worth testing; `g4ad` (AMD) ruled out.
- **By:** Jamir.

### 2026-11-17 — Quantize every model ourselves; RQ2 main grid uses no imatrix
- **Decision:** Build all GGUF files from one full-precision file per model; the RQ2 grid uses no imatrix. Never use downloaded GGUFs whose calibration is unknown.
- **Reason:** Many community GGUFs are built with a mostly-English imatrix; mixing them in would blur RQ2 with RQ2b.
- **By:** Claude, approved by Jamir ("proceed"). Confirm with the adviser.

### 2026-11-17 — Workspace under git
- **Decision:** Local git repo; `data/`, model files and raw outputs stay ignored.
- **By:** Jamir.

### 2026-11-17 — Use Colab Pro as main paid compute *(superseded 2026-11-21 by AWS)*
- **Decision:** Subscribe to Colab Pro ($9.99/month) in January for the full grid; Kaggle as free backup; department GPU if borrowable.
- **Reason:** The T14 (Ryzen 7 PRO 4750U, Vega 7) is too slow for the full grid (~3–5 s/prompt, estimate). Hardware affects speed, not validity.
- **By:** Jamir.

### 2026-11-17 — A Cebuano linguist verifies the error taxonomy
- **Decision:** The linguist finalizes the categories and labels (or verifies) errors; Jamir does the first pass and double-labels 100 for kappa.
- **Reason:** Stronger than self-labeling; not a department requirement (no external SRC needed).
- **By:** Jamir.

### 2026-11-17 — Final defense window: mid to late May 2027
- **By:** Jamir.

### 2026-11-17 — Reframe after novelty check
- **Decision:** Compression (RQ2) and calibration (RQ2b) are the core contribution; search (RQ1) becomes a supporting, end-to-end chapter that reproduces MTEB baselines first. RQ numbers keep pipeline order.
- **Reason:** MTEB BelebeleRetrieval and CebQA already cover Cebuano search baselines; Waskito et al. (2026) measured perplexity (not task accuracy) for Philippine languages under compression.
- **By:** Jamir, on Claude's recommendation.

### 2026-11-17 — Copyright policy
- **Decision:** Use copyrighted corpora (news decoys) privately for research; never publish article text; share code plus source IDs/URLs; license table in the methodology chapter.
- **Reason:** RA 8293 Sec. 185 fair use for research covers internal use; redistribution is the risk.
- **By:** Jamir.

### 2026-11-17 — Proposal defense target: 2026-12-18
- **Decision:** Defend the new proposal by Friday Dec 18 so experiments run over the break and next semester. First week of January is the fallback.
- **By:** Jamir.

### 2026-11-17 — Lean toward switching from copra to this study *(resolved 2026-11-21: switched)*
- **Decision:** Switch, unless NCRC-V commits a named expert and sample access this week.
- **Reason:** Copra depends on an expert to set every threshold, 600–800 field photos, station permissions, trader graders and a phone camera Jamir lacks; adviser's expertise is NLP; department favors CS-driven studies. See `reference/copra-study.md`.
- **By:** Jamir. **Status:** resolved 2026-11-21 — switched (see above).

## Open decisions

| # | Decision | Options | Needed by |
|---|---|---|---|
| 1 | Final model list | 3–4 models from Qwen3 1.7B/4B, Gemma 3 4B, Llama 3.2 3B, SeaLLMs v3 1.5B; optional 7–8B. **Proposed selection rule (Lab 1, 2026-11-22):** keep a model only if its Belebele Cebuano accuracy at Q8_0 is clearly above chance (25%; exact margin `TBD`), measured in the week-2 proof of concept. Lab 1 hints: Qwen3-1.7B at floor risk; Gemma 3 4B strongest | Dec 7 (chapter 3) |
| 2 | Prompt instruction language | English vs. Cebuano | Dec 7 |
| 3 | Proposal chapter coverage | VSU format: which chapters are "the proposal" | Nov 23 (ask adviser) |
| 4 | Linguist and/or second Cebuano coder (RQ3 is conditional on this) | Who; how many hours (minimum roles in the 2026-11-22 entry) | Dec 14 target; **Jan 31 cutoff** → fallback |
| 5 | Main compute | **Decided 2026-11-21:** AWS → Kaggle/Colab → dept PC (see above). Still open: credit expiry, GPU quota | Dec 18 |
| 6 | CebQuAD | Include if license allows; drop otherwise | Dec 7 |
| 8 | Statistics thresholds: equivalence margin (proposed ±3 points; must exceed pilot CI half-width), agreement threshold (proposed 0.6), parse-failure flag (proposed 5%) | Accept / adjust after week-2 pilot | Jan 4 (before runs) |
| 7 | RQ3 protocol revision (2026-11-20 brief): automatic language ID, published typologies, pilot, two blind coders, pre-set alpha threshold; who is the second coder | Adopt / adopt partly / keep original | Dec 7 (chapter 3) |
