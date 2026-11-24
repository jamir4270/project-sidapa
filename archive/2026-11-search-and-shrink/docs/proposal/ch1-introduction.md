# Chapter I — Introduction (outline)

## Background of the Study
- Offline AI for Philippine communities; small models must be compressed to run on cheap hardware. Cite as motivation (not tested): AWQ (MLSys 2024), Xu et al. 2024 on-device review, MobileLLM (ICML 2024), llama.cpp — see `../literature/sources.md` `VERIFY`.
- Cebuano: ~20M speakers `VERIFY`; low-resource despite a huge, mostly bot-written Wikipedia (arXiv 2411.05527) `VERIFIED`.
- Question-answering AI (RAG): search, then read.
- Quantization damage is uneven across languages (Marchisio et al. 2024; Marie & Fujita 2025) `VERIFIED`.
- Prior Philippine-language work: perplexity only (Waskito et al. 2026); search baselines exist (MTEB, CebQA).

## Statement of the Problem
- Gap sentence (from `../literature/novelty-check.md`).
- Developers have no evidence of how much Cebuano task accuracy is lost at each compression level, or whether Cebuano calibration helps.

## Objectives of the Study
- General and specific objectives: copy from `../methodology/research-questions.md` and refine.

## Significance of the Study
- Developers building offline Cebuano tools (LGUs, health, schools).
- Philippine NLP community (first downstream GGUF results in Cebuano/Tagalog, to our knowledge).
- VSU / DCST (research capacity in low-resource NLP).
- Future researchers (reusable, reproducible pipeline; code + source IDs released).

## Scope and Limitations
- From `../methodology/research-questions.md`.

## Time and Place of the Study
- Nov 2026 – May 2027; DCST, VSU; cloud compute (AWS EC2 GPU instance; Kaggle as backup); Gantt chart from `../timeline.md`.
