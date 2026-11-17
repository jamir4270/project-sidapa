# Research Questions

*Numbering follows the pipeline order (search → read → errors). RQ2 and RQ2b are the core contribution.*

## General objective

To measure how much accuracy small, open-weight language models lose in Cebuano, relative to Tagalog and English,
when quantized for offline use on consumer hardware, whether Cebuano-language calibration reduces that loss, and
how Cebuano search performs on a realistic corpus within a question-answering pipeline.

## Research questions

**RQ1 — Search (supporting).** Starting from the published MTEB BelebeleRetrieval baselines, how much does Cebuano
search accuracy (Recall@5, nDCG@10) drop on a realistic corpus with thousands of real Cebuano distractor passages,
and do Cebuano-aware keyword search (affix stripping) or hybrid search close the gap to Tagalog and English?

**RQ2 — Compression (core).** How much multiple-choice accuracy does each GGUF quantization level (Q8_0, Q6_K,
Q4_K_M, Q3_K_M, Q2_K) cost in Cebuano and Tagalog versus English, when a small model answers from the gold passage,
a retrieved passage, or no passage?

**RQ2b — Calibration (core, most original).** At Q3_K_M and Q2_K, does building the llama.cpp importance matrix
from Cebuano or Tagalog text recover accuracy compared with English text or no calibration?

**RQ3 — Errors (supporting).** What kinds of errors do the models make in Cebuano, and which categories grow as
compression increases? (Categories finalized and verified by a Cebuano linguist; agreement reported as Cohen's kappa.)

## Hypotheses (falsifiable)

| ID | Hypothesis | Falsified if |
|---|---|---|
| H1 | Cebuano search accuracy falls more than English as decoys are added | Cebuano–English gap interval includes zero at 10,000 decoys |
| H2 | The quantization gap (Cebuano drop − English drop) is positive at Q4_K_M and below | Gap interval includes zero at every level |
| H2b | Cebuano calibration yields higher Cebuano accuracy than English calibration at Q2_K | Paired difference interval includes zero |
| H3 | Language-switching and morphology errors grow with compression | Category shares don't change across levels |

A falsified hypothesis is still a result. Report it with its interval.

## Specific objectives (chapter 1 wording draft)

1. To reproduce published Cebuano, Tagalog and English search baselines and measure search accuracy on a corpus extended with real distractor passages.
2. To measure multiple-choice accuracy of small open-weight models across five GGUF quantization levels in Cebuano, Tagalog and English, with gold, retrieved and no passages.
3. To compare English, Cebuano and Tagalog importance-matrix calibration at low-bit quantization.
4. To develop and validate, with a Cebuano linguist, a taxonomy of model errors in Cebuano, and relate error categories to quantization level.
5. To measure inference speed and memory of each quantization level on a 2020-era consumer laptop.

## Scope and limitations (draft)

- Text only; Cebuano, Tagalog, English.
- Small models (≈1.5B–4B; optionally one 7–8B). No training or fine-tuning.
- Belebele passages are translations, not native Cebuano text.
- Multiple-choice accuracy; free-text quality only through the error taxonomy.
- Results reflect specific model versions and llama.cpp builds; recorded for reproducibility.
