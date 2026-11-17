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
- Clustered bootstrap CIs; paired tests; quantization gap; decision rule.

## Compute and Reproducibility
- From `../methodology/compute.md`; logging; versions; one machine per comparison.

## Ethical Considerations
- No human-subject data collection beyond the linguist's expert labeling (consent for acknowledgment).
- Copyright: research fair use; no redistribution of article text.
- Responsible-use note: results describe model behavior, not language quality or speakers.
- Check with adviser whether VSU ethics review is needed for the linguist's involvement `TBD`.
