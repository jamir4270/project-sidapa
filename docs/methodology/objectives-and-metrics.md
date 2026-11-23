# Objectives and Metrics

*What each objective measures, which number answers it, and which tool produces it. Written 2026-11-23.*
*Statistics (CIs, confirmatory tests C1–C4, decision rules): `experiment-design.md` → Statistics.*

**Measurement** = what you record (e.g., the letter the model picked). **Metric** = the number you compute from it
(e.g., accuracy). Status: **planned** = already in `experiment-design.md`; **new** = added 2026-11-23, exploratory,
computed from data the plan already collects (no extra runs).

## The four objectives

| # | Objective | Role |
|---|---|---|
| 1 | **Search:** how well Cebuano search works on a realistic library with decoys, compared with Tagalog and English, and which method narrows the gap | Supporting (RQ1) |
| 2 | **Compression:** how much accuracy 3–4 small models lose at each compression level in each language, with the correct passage, a retrieved one, or none, and whether Cebuano loses more than English | **Core (RQ2)** |
| 3 | **Calibration:** at the two lowest levels, whether building the importance matrix from Cebuano (or Tagalog) text recovers accuracy compared with English text or none | **Core (RQ2b)** |
| 4 | **Errors (conditional):** what kinds of mistakes the models make in Cebuano, and which kinds grow with compression | Supporting (RQ3) |

## Headline number per objective

| # | Headline number |
|---|---|
| 1 | Cebuano − English nDCG@10 drop at 10,000 decoys (H1), and which retriever shrinks it |
| 2 | Quantization gap (Cebuano drop − English drop) at Q4_K_M, Q3_K_M, Q2_K (C1–C3) |
| 3 | Cebuano-calibrated − English-calibrated accuracy on Cebuano at Q2_K (C4) |
| 4 | Which categories' shares rise from Q8_0 to Q2_K, with coder agreement ≥ the threshold (H3) |

---

## 1. Search (RQ1)

**Record:** for each question, the ranked list of passages each retriever returns.

| Metric | Plain meaning | Answers | Status |
|---|---|---|---|
| nDCG@10 | 0–1 score for how high the right passage ranks in the top 10; the metric MTEB uses, so directly comparable | Main search score | Planned |
| Recall@1, Recall@5 | Is the right passage first, or in the top 5? Match k to the number of passages given to the model (`TBD`) | What the model actually receives | Planned |
| Decoy curve | nDCG@10 at 0 / 500 / 2,000 / 10,000 decoys, per language | How much realism hurts | Planned |
| Language gap at 10k decoys (H1) | (Cebuano drop from 0 decoys) − (English drop) | Does Cebuano suffer more? | Planned |
| Retriever comparison | nDCG@10 of BM25, affix-stripping BM25, embedders, hybrid, in Cebuano | Which method closes the gap | Planned |
| Reproduction check | Our BM25 Cebuano nDCG@10 vs. MTEB's 0.784 | Is the pipeline trustworthy? | Planned |

## 2. Compression (RQ2)

**Record:** per question: raw output, parsed letter, correct or not, parse failure (the JSONL fields in `../../experiments/README.md`).

| Metric | Plain meaning | Answers | Status |
|---|---|---|---|
| Accuracy ± 95% CI | Share of questions right, per model × level × language × condition | Basic performance | Planned |
| Drop from Q8_0 | Accuracy at Q8_0 − accuracy at the level | Cost of each level | Planned |
| Quantization gap (C1–C3) | Cebuano drop − English drop (Tagalog gap reported too) | **Headline: does Cebuano lose more?** | Planned |
| Above-chance retained | (accuracy − 25%) ÷ (Q8_0 accuracy − 25%): share of real skill that survives | Fair comparison when Cebuano starts lower | New |
| File size (GB) | Size of each compressed file | Accuracy-vs-size trade-off | Planned |
| Parse-failure rate | Share of outputs with no valid A–D letter | Format breakdown | Planned |
| Letter collapse | Share of answers equal to the model's most common letter (~25% healthy; near 100% broken) | Known failure of low-bit models | New |
| Flip counts | Questions that go right → wrong (and wrong → right) from Q8_0 to each level | Also selects RQ3 items | New |
| Condition gaps | Gold − retrieved = cost of search mistakes; gold − none = value of the passage; none vs. 25% = memorization signal | Separates reading, search, memory | New (framing of planned runs) |
| SIB-200 accuracy, Tatoeba chrF, FLORES+ perplexity | Supporting tasks; perplexity lines up with Waskito et al. | Does the pattern hold beyond Belebele? | Planned |

## 3. Calibration (RQ2b)

**Record:** same per-question data, for each calibration (none / English / Cebuano / Tagalog) × seed × level × language.

| Metric | Plain meaning | Answers | Status |
|---|---|---|---|
| Accuracy, mean ± SD over 3 seeds | Score per calibration, with seed-to-seed wobble | Basic result | Planned |
| Cebuano-cal − English-cal, Cebuano, Q2_K (C4) | Helps / equivalent (within ±margin, `TBD`) / inconclusive | **Headline for calibration** | Planned |
| Recovery vs. no calibration | Calibrated accuracy − uncalibrated accuracy, per calibration language | Does any calibration help? | New (framing) |
| Share of loss recovered | (calibrated − uncalibrated) ÷ (Q8_0 − uncalibrated) | "Won back X% of what compression took" | New |
| Side effect on other languages | English accuracy with Cebuano calibration − English accuracy with English calibration | Does helping Cebuano hurt English? | New |

**Fairness measurements to log:** token count of each calibration file (token-matching across languages proposed
2026-11-21, awaiting go-ahead); overlap check against Belebele/FLORES text.

## 4. Errors (RQ3, conditional on coders by Jan 31, 2027)

**Record:** explanation-run outputs (reason + letter) for flipped and stayed-right questions, at Q8_0 and Q2_K.

| Metric | Plain meaning | Answers | Status |
|---|---|---|---|
| Category counts and shares, Q8_0 vs Q2_K | How often each error type appears | What mistakes happen | Planned |
| Q2 − Q8 share difference ± CI (H3) | Change in each category's share | Which types grow with compression | Planned |
| Krippendorff's alpha or Cohen's kappa ± CI | Coder agreement beyond chance, overall and per category | Is the taxonomy reliable? | Planned |
| Language-switch rate | Share of explanation lines labeled Tagalog or English instead of Cebuano | Most objective error category | Planned step, now a number |
| Reason–answer mismatch rate | Reason supports one option, letter says another | Reasoning vs. format failure | Planned (typology) |

**Fallback if no coders:** parse failures, letter collapse, flip counts, language-switch rate, and optionally
tokenizer fertility (tokens per word, per language).

---

## Where each number comes from (is it built into llama.cpp?)

**Mostly no.** llama.cpp **makes and runs** the compressed models. It does not score them on Belebele.
Your Python scripts send each prompt to the model, save the answer, and compute the metrics from the saved JSONL.
Tool features below are from memory unless tagged otherwise: `VERIFY` each against the tool's docs before relying on it.

| What | Tool | Built into llama.cpp? |
|---|---|---|
| Compress a model (Q8_0 → Q2_K) | `llama-quantize` (after `convert_hf_to_gguf.py`) | Yes (`VERIFY` script name) |
| Build the importance matrix from calibration text | `llama-imatrix`, then `llama-quantize --imatrix` | Yes (`VERIFY` flags) |
| Get each answer | `llama-server` + your client (`src/llm/`) | Runs the model; scoring is yours |
| File size | The `.gguf` file on disk | — (operating system) |
| Accuracy, drop, gap, above-chance retained, parse failures, letter collapse, flips, condition gaps, recovery, share recovered, side effects | Your analysis script (`src/analysis/`) over the JSONL | No |
| FLORES+ perplexity | `llama-perplexity` | Yes (`VERIFY`) |
| Optional extra: KL divergence vs. the full-quality model | `llama-perplexity` (KL-divergence mode) | Yes (`VERIFY`); not in the plan |
| Tokenizer fertility | `llama-tokenize` or the Hugging Face tokenizer | Partly (`VERIFY` `llama-tokenize`) |
| BM25 search | `bm25s` | No |
| Embedding search | `sentence-transformers` or similar (`TBD`) | No |
| nDCG@10, Recall@k | `ranx` | No |
| Tatoeba chrF | `sacrebleu` (`VERIFY` metric choice) | No |
| Language ID (language-switch rate) | GlotLID (`VERIFY` `ceb_Latn` coverage) | No |
| Agreement (alpha, kappa) | `krippendorff` package / `scikit-learn` (`VERIFY`) | No |
| Bootstrap CIs, C1–C4 | Your bootstrap script (`numpy`) | No |
| Speed (seconds per prompt) | `latency_ms` in the JSONL | Logged by your client |
