# Decision Log

*Append-only. Newest first. Each entry: date, decision, reason, who decided. Open decisions at the bottom.*

## Decisions

### 2026-11-17 — Quantize every model ourselves; RQ2 main grid uses no imatrix
- **Decision:** Build all GGUF files from one full-precision file per model; the RQ2 grid uses no imatrix. Never use downloaded GGUFs whose calibration is unknown.
- **Reason:** Many community GGUFs are built with a mostly-English imatrix; mixing them in would blur RQ2 with RQ2b.
- **By:** Claude, approved by Jamir ("proceed"). Confirm with the adviser.

### 2026-11-17 — Workspace under git
- **Decision:** Local git repo; `data/`, model files and raw outputs stay ignored.
- **By:** Jamir.

### 2026-11-17 — Use Colab Pro as main paid compute
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

### 2026-11-17 — Lean toward switching from copra to this study (pending)
- **Decision:** Switch, unless NCRC-V commits a named expert and sample access this week.
- **Reason:** Copra depends on an expert to set every threshold, 600–800 field photos, station permissions, trader graders and a phone camera Jamir lacks; adviser's expertise is NLP; department favors CS-driven studies. See `reference/copra-study.md`.
- **By:** Jamir. **Status:** pending NCRC-V and adviser.

## Open decisions

| # | Decision | Options | Needed by |
|---|---|---|---|
| 1 | Final model list | 3–4 models from Qwen3 1.7B/4B, Gemma 3 4B, Llama 3.2 3B, SeaLLMs v3 1.5B; optional 7–8B | Dec 7 (chapter 3) |
| 2 | Prompt instruction language | English vs. Cebuano | Dec 7 |
| 3 | Proposal chapter coverage | VSU format: which chapters are "the proposal" | Nov 23 (ask adviser) |
| 4 | Linguist | Who; how many hours | Dec 14 |
| 5 | Main compute | Department GPU vs. Colab Pro | Dec 18 |
| 6 | CebQuAD | Include if license allows; drop otherwise | Dec 7 |
