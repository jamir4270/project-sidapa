# Experiment Design

## Grid

| Experiment | Conditions | Count | Time at ~1 s/prompt (estimate) |
|---|---|---|---|
| RQ2 main (core) | 3–4 models × 5 levels (Q8_0, Q6_K, Q4_K_M, Q3_K_M, Q2_K) × 3 languages, gold passage, 900 Qs each | ~54,000 prompts | ~15 h (cloud T4 assumption) |
| RQ2b calibration | 2 models × 2 levels (Q3_K_M, Q2_K) × 4 calibrations (none, English, Cebuano, Tagalog) × 3 languages | ~43,000 prompts | ~12 h |
| RQ2 conditions | Same models at Q8 and Q4; retrieved passage and no passage. Full grid in Cebuano; best retriever only for Tagalog/English | ~25,000 prompts | ~7 h |
| RQ2 extra tasks | SIB-200 (99), Tatoeba (500-pair sample), FLORES+ perplexity (one model) | Small | A few hours |
| RQ1 search | Reproduce MTEB (BM25, multilingual-e5-large-instruct) for ceb/tgl/eng; then + decoys (500 / 2,000 / 10,000), affix-stripping BM25, BGE-M3, Qwen3-Embedding-0.6B, hybrid | ~20 runs | Minutes each (CPU); large embedders in cloud |
| RQ3 explanation run | 200 Cebuano Qs with a short reason before the answer, at Q8 and Q2 | ~1,600 prompts | A few hours |
| Speed benchmark | `llama-bench` per model × level on the T14 | — | ~1 h |

The T14 would take 3–5× longer than the times above (estimate). Measure actual speed in week 1.

## Fixed settings (decide once; record in chapter 3)

- **Prompt:** one template; instructions in English (`TBD` vs Cebuano); passage + question + four options in the test language; "Answer with one letter."
- **Decoding:** temperature 0; max new tokens small (e.g., 5) for MC runs.
- **Parsing:** first A–D letter; unparseable = wrong; report parse-failure rate per level.
- **Models:** exact Hugging Face repo + revision; GGUF made by you with one llama.cpp version (record commit).
- **Calibration text:** ~100 KB per language from Leipzig (Cebuano) / matched Tagalog / English source; no overlap with Belebele/FLORES (check by exact and near-duplicate matching).
- **Search:** e5 models need `query: ` / `passage: ` prefixes; BM25 via `bm25s`; hybrid via reciprocal rank fusion `TBD` parameters.
- **Machine:** one machine type per comparison; record GPU/CPU, driver, llama.cpp version.

## Metrics

| RQ | Metric |
|---|---|
| RQ1 | nDCG@10, Recall@1, Recall@5 (`ranx`) |
| RQ2/2b | Accuracy (MC); quantization gap = (ceb drop from Q8) − (eng drop from Q8); parse-failure rate |
| RQ2 extra | SIB-200 accuracy; Tatoeba chrF `VERIFY` metric choice; FLORES+ perplexity |
| RQ3 | Category counts/shares per level; Cohen's kappa (linguist vs researcher) |
| Speed | Tokens/s (prompt processing and generation), peak RAM |

## Statistics

- 95% CIs by **clustered bootstrap** (resample passages; 1,000+ resamples).
- **Paired** comparisons for settings on the same items (paired bootstrap or McNemar).
- No claim of difference if its interval includes zero.
- Main claims on Belebele (900); SIB-200 (99) reported with wide intervals as supporting evidence.
- Reference: Miller 2024, arXiv 2411.00640.

## Validity checks

- **Floor check before fixing the model list (proposed 2026-11-22):** each candidate's Belebele Cebuano accuracy at Q8_0 must be clearly above chance (25%); a model at floor cannot show compression loss. Run in the week-2 proof of concept. Origin: Lab 1 (`../labs/lab-01-run-a-local-model.md`).
- **Independent items:** every prompt is sent alone, with no chat history (Lab 1 showed history contaminates answers).

- Reproduce MTEB Cebuano BM25 (0.784) and one FilBench Belebele number before trusting the pipeline.
- Closed-book condition measures memorization/contamination.
- Spot-check ~50 retrievals for decoys that accidentally answer the question.
- Run 10–20 items locally before every cloud run.
