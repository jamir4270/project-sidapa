# Chapter IV — Methodology (outline)

## Research Design
- Quantitative, experimental measurement study (comparative evaluation). Pipeline as apparatus.
- Pipeline figure (from `../primer.md` §8).

## Datasets and Licensing
- From `../methodology/data-and-licensing.md`, including the license table.

## Decoy Corpus Construction
- Sources, chunking, cleaning, deduplication, overlap removal, size curve.

## Search Experiments (RQ1)
- Baseline reproduction (MTEB); methods (BM25, affix-stripping BM25, embedders, hybrid); metrics.

## Compression Experiments (RQ2, RQ2b)
- Models; GGUF conversion and quantization; calibration texts and imatrix; conditions; prompt; decoding; parsing.

## Error Analysis (RQ3)
- From `../methodology/error-taxonomy.md`.

## Statistical Analysis
- Full procedure: `../methodology/experiment-design.md` → Statistics (Steps 0–6).
- Descriptive: accuracy (mean of 0/1 scores) ± 95% CI per model × level × language; file size; accuracy-vs-level figure.
- Inferential: paired clustered bootstrap (10,000 passage resamples) for every CI and comparison.
- Four pre-registered confirmatory claims (C1–C3 quantization gap at Q4_K_M/Q3_K_M/Q2_K; C4 calibration at Q2_K),
  Bonferroni-corrected (98.75% CIs); C4 includes an equivalence margin (`TBD`).
- Secondary (H1 search, H3 errors) and exploratory results at 95% CIs, labeled as such.
- Agreement: kappa or Krippendorff's alpha with bootstrap CI vs. pre-set threshold.
- Justify not using ANOVA: binary, repeated-measures data (see the methods-not-used table).

## Compute and Reproducibility
- From `../methodology/compute.md`; logging; versions; one machine per comparison.

## Ethical Considerations
- No human-subject data collection beyond the linguist's expert labeling (consent for acknowledgment).
- Copyright: research fair use; no redistribution of article text.
- Responsible-use note: results describe model behavior, not language quality or speakers.
- Check with adviser whether VSU ethics review is needed for the linguist's involvement `TBD`.
