# Archive — "Search and Shrink" (Nov 17–24, 2026)

*Archived 2026-11-24. Read-only. Final state is also tagged in git: `search-and-shrink-final`.*

## What the study was

"Search and Shrink: Quantization and Calibration Losses for Cebuano, Tagalog and English in Small Offline Language
Models." A measurement study: how much accuracy small GGUF models lose in Cebuano vs. English at each llama.cpp
quantization level (Q8_0 → Q2_K) on Belebele, whether a Cebuano importance matrix (calibration) wins it back, plus a
supporting search chapter (RQ1: BM25 vs. embedders on Belebele with decoys) and a conditional error taxonomy (RQ3).

## Why it was set aside

See `docs/decisions.md`, entries of 2026-11-24. In short:
- RQ1 (search) and RQ2 (compression) tested two different machines; compression never touches the retriever, so the
  two halves could not inform each other. RQ1 had survived from merging two Nov 17 ideas after its novelty was taken.
- It was an evaluation-only study (SRC: "novel beyond evaluating pretrained models?").
- The researcher's interest is RAG search. New focus: fine-tuning and evaluating an embedding model for Cebuano retrieval.

## What was carried over to the live docs

| Piece | Now lives in |
|---|---|
| Datasets, decoy-library pipeline, copyright policy | `docs/methodology/data-and-licensing.md` |
| AWS compute plan | `docs/methodology/compute.md` |
| Logging / resumability / seed rules | `experiments/README.md` |
| Sources (retrieval sources most relevant now) | `docs/literature/sources.md` |
| VSU manual rules, forms, proposal structure | `docs/proposal/README.md` |
| Decision history | `docs/decisions.md` (never archived) |

Ideas worth reusing from the archived files: the paired clustered bootstrap with pre-declared confirmatory claims
(`docs/methodology/experiment-design.md`, works for nDCG@10); reproducing MTEB BelebeleRetrieval (BM25 = 0.784 ceb) as a
pipeline check; affix-stripping BM25; the decoy-size curve.

## What is here

| File | What it was |
|---|---|
| `docs/at-a-glance.md`, `docs/primer.md`, `docs/timeline.md` | Overview, long explainer, week-by-week plan |
| `docs/methodology/research-questions.md`, `experiment-design.md`, `objectives-and-metrics.md`, `error-taxonomy.md` | RQs, grid and statistics, metrics, RQ3 protocol |
| `docs/literature/novelty-check.md` | Novelty check for the compression study |
| `docs/proposal/ch1–ch4*.md`, `docs/proposal/README.md` | Chapter outlines and the old build checklist (snapshot) |
| `docs/*.docx` | Explainer, pitch guide, proposal checklist handouts |
| `docs/labs/lab-01-run-a-local-model.md` | Lab 1: running llama.cpp locally (learning record) |

Paths inside these files point to their old locations (e.g. `docs/primer.md`); read them relative to this folder.
