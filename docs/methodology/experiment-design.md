# Experiment Design

## Grid

| Experiment | Conditions | Count | Time at ~1 s/prompt (estimate) |
|---|---|---|---|
| RQ2 main (core) | 3–4 models × 5 levels (Q8_0, Q6_K, Q4_K_M, Q3_K_M, Q2_K) × 3 languages, gold passage, 900 Qs each | ~54,000 prompts | ~15 h (cloud T4 assumption) |
| RQ2b calibration | 2 models × 2 levels (Q3_K_M, Q2_K) × 4 calibrations (none, English, Cebuano, Tagalog) × 3 languages | ~43,000 prompts | ~12 h |
| RQ2b calibration seeds | 2 models × Q2_K × 3 calibration languages × 2 extra seeds × Cebuano test only | ~10,800 prompts | ~3 h |
| RQ2 conditions | Same models at Q8 and Q4; retrieved passage and no passage. Full grid in Cebuano; best retriever only for Tagalog/English | ~25,000 prompts | ~7 h |
| RQ2 extra tasks | SIB-200 (99), Tatoeba (500-pair sample), FLORES+ perplexity (one model) | Small | A few hours |
| RQ1 search | Reproduce MTEB (BM25, multilingual-e5-large-instruct) for ceb/tgl/eng; then + decoys (500 / 2,000 / 10,000), affix-stripping BM25, BGE-M3, Qwen3-Embedding-0.6B, hybrid | ~20 runs | Minutes each (CPU); large embedders in cloud |
| RQ3 explanation run (conditional on coders, cutoff Jan 31) | 200 Cebuano Qs (flipped right→wrong Q8→Q2 + matched stayed-right) with a short reason before the answer, at Q8 and Q2 | ~1,600 prompts | A few hours |

The T14 would take ~5–9 s per prompt (from Lab 1's measured speed; estimate), so the grid runs on AWS.

## Fixed settings (decide once; record in chapter 3)

- **Prompt:** one template; instructions in English (`TBD` vs Cebuano); passage + question + four options in the test language; "Answer with one letter."
- **Decoding:** temperature 0; max new tokens small (e.g., 5) for MC runs.
- **Parsing:** first A–D letter; unparseable = wrong; report parse-failure rate per level.
- **Models:** exact Hugging Face repo + revision; GGUF made by you with one llama.cpp version (record commit).
- **Calibration seeds:** 3 importance matrices per calibration language (seed 1 for the full RQ2b grid; seeds 2–3 at Q2_K, Cebuano test only), each from a different random sample of the calibration source.
- **Calibration text:** ~100 KB per language from Leipzig (Cebuano) / matched Tagalog / English source; no overlap with Belebele/FLORES (check by exact and near-duplicate matching).
- **Search:** e5 models need `query: ` / `passage: ` prefixes; BM25 via `bm25s`; hybrid via reciprocal rank fusion `TBD` parameters.
- **Machine:** one machine type per comparison; record GPU/CPU, driver, llama.cpp version.

## Metrics

| RQ | Metric |
|---|---|
| RQ1 | nDCG@10, Recall@1, Recall@5 (`ranx`) |
| RQ2/2b | Accuracy (MC); quantization gap = (ceb drop from Q8) − (eng drop from Q8); parse-failure rate |
| RQ2 extra | SIB-200 accuracy; Tatoeba chrF `VERIFY` metric choice; FLORES+ perplexity |
| RQ3 | Category counts/shares at Q8 and Q2; Cohen's kappa or Krippendorff's alpha (with CI) |
| Size | File size (GB) per model × quantization level, reported next to accuracy |

## Statistics (data analysis procedure, adopted 2026-11-22)

**One method everywhere: the paired clustered bootstrap.** Redraw Belebele passages with replacement 10,000 times;
recompute every statistic on each redraw; the spread of the redraws gives the confidence interval (CI). "Paired" means
every model, level, language and calibration is recomputed on the **same** redrawn passages, so item difficulty cancels
out. Belebele is parallel across languages, so language comparisons are paired too. Reference: Miller 2024,
arXiv 2411.00640 (`VERIFIED`).

### Step 0 — Lock before the January runs (log in `../decisions.md`)

| Setting | Proposed value | Status |
|---|---|---|
| Confirmatory claims | C1–C4 below (nothing else) | Adopted |
| Bootstrap resamples | 10,000, resampling passages | Adopted |
| Multiple-test correction | Bonferroni over C1–C4 → 98.75% CIs | Adopted |
| Equivalence margin (C4) | ±3 accuracy points | `TBD` — must be wider than the CI half-width seen in the week-2 pilot |
| Agreement threshold (RQ3) | kappa/alpha ≥ 0.6 | `TBD` |
| Calibration seeds | 3 per language | Adopted |
| Parse-failure flag | > 5% in a cell | `TBD` |

Setting these after seeing results would be cherry-picking.

### Step 1 — Validity checks (before any statistics)

Floor check (Q8_0 Cebuano clearly above 25%), reproduce MTEB BM25 Cebuano (0.784), parse-failure rate per cell
(flag cells above the threshold). See "Validity checks" below.

### Step 2 — Descriptive results

- **Table:** accuracy ± 95% CI for every model × level × language, with file size (GB).
- **Figure (one per model):** accuracy (y) vs. quantization level (x), one line per language.
- Accuracy is the mean of 0/1 scores (central tendency); the CI is the spread (variation). For RQ2b also report
  mean ± SD across the 3 calibration seeds.

### Step 3 — Confirmatory tests (only these four)

All pooled across models (average over models, same passage redraws). 98.75% CIs.

| # | Claim | Statistic | Supported if |
|---|---|---|---|
| C1 | H2 at Q4_K_M | Quantization gap = (Cebuano drop from Q8_0) − (English drop from Q8_0) | CI entirely above 0 |
| C2 | H2 at Q3_K_M | same | same |
| C3 | H2 at Q2_K | same | same |
| C4 | H2b at Q2_K | Cebuano accuracy: Cebuano-calibrated − English-calibrated, averaged over seeds | CI above 0 → **helps**; CI entirely inside ±margin → **equivalent** (no meaningful effect); otherwise → **inconclusive** |

C4's three outcomes make a null result reportable: "any effect is smaller than ±3 points" is a finding.

### Step 4 — Exploratory results (95% CIs, labeled exploratory, no claims of difference)

Per-model gaps; Q6_K; Tagalog vs English gaps; retrieved-passage and no-passage conditions; Tagalog and no
calibration in RQ2b; Q3_K_M calibration; SIB-200 (99 items, wide CIs), Tatoeba, FLORES+ perplexity.

### Step 5 — RQ1 search (secondary)

- Per-query nDCG@10, Recall@1, Recall@5 with the same paired bootstrap.
- **Secondary test H1:** at 10,000 decoys, (Cebuano nDCG@10 drop from 0 decoys) − (English drop), 95% CI.
- Retriever comparisons (BM25, affix-stripping BM25, embedders, hybrid): descriptive with 95% CIs.

### Step 6 — RQ3 errors (secondary)

- Category shares at Q8 and Q2 (the explanation run has only these two levels, so no trend test).
- **Secondary test H3:** Q2 − Q8 share per category, bootstrap 95% CI.
- Agreement (kappa or alpha) with a bootstrap CI, judged against the pre-set threshold.

### Methods deliberately not used

| Not used | Why |
|---|---|
| ANOVA | Scores are right/wrong (not continuous) and the same items repeat; the bootstrap gap tests the language × level interaction directly |
| Mixed-effects logistic regression (GLMM) | Answers the same question as C1–C3; harder to fit and defend. "If time permits" robustness check only |
| McNemar, Cochran's Q, Wilcoxon, chi-square | Each is covered by the paired bootstrap; fewer methods to explain |

### Practical notes

- **Code:** one script (~150 lines, estimate) reads the per-item JSONL, draws passage resamples once, computes every
  statistic from the same draws. Planned for Feb 15–21 (`../timeline.md`, week 14).
- **Detection limit:** one accuracy on 900 items at ~50% has a 95% CI of about ±3.3 points (1.96 × √(0.25/900));
  paired, pooled gaps should resolve about 2–3 points (estimate). Check in the week-2 pilot.
- **Pooling risk:** a model at the floor at Q2_K drags the pooled gap; the floor check guards against this. Report
  per-model gaps (Step 4) so a single model driving the result is visible.

## Validity checks

- **Floor check before fixing the model list (proposed 2026-11-22):** each candidate's Belebele Cebuano accuracy at Q8_0 must be clearly above chance (25%); a model at floor cannot show compression loss. Run in the week-2 proof of concept. Origin: Lab 1 (`../labs/lab-01-run-a-local-model.md`).
- **Independent items:** every prompt is sent alone, with no chat history (Lab 1 showed history contaminates answers).

- Reproduce MTEB Cebuano BM25 (0.784) and one FilBench Belebele number before trusting the pipeline.
- Closed-book condition measures memorization/contamination.
- Spot-check ~50 retrievals for decoys that accidentally answer the question.
- Run 10–20 items locally before every cloud run.
