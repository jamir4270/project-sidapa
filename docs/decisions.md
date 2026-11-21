# Decision Log

*Append-only. Newest first. Each entry: date, decision, reason, who decided. Open decisions at the bottom.*

## Decisions

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
  supporting objective (specific objective 5), not a research question.
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
  (GPU quota). Backups: see the priority-order entry above; never mix machines inside one comparison. Speed benchmarks
  stay on the T14 (the offline / resource-constrained framing). Colab Pro is dropped.
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
| 1 | Final model list | 3–4 models from Qwen3 1.7B/4B, Gemma 3 4B, Llama 3.2 3B, SeaLLMs v3 1.5B; optional 7–8B | Dec 7 (chapter 3) |
| 2 | Prompt instruction language | English vs. Cebuano | Dec 7 |
| 3 | Proposal chapter coverage | VSU format: which chapters are "the proposal" | Nov 23 (ask adviser) |
| 4 | Linguist | Who; how many hours | Dec 14 |
| 5 | Main compute | **Decided 2026-11-21:** AWS → Kaggle/Colab → dept PC (see above). Still open: credit expiry, GPU quota | Dec 18 |
| 6 | CebQuAD | Include if license allows; drop otherwise | Dec 7 |
| 7 | RQ3 protocol revision (2026-11-20 brief): automatic language ID, published typologies, pilot, two blind coders, pre-set alpha threshold; who is the second coder | Adopt / adopt partly / keep original | Dec 7 (chapter 3) |
