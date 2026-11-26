# Experiments

Code for the experiments. Nothing here yet. Entry-point scripts go in `scripts/`; the layout grows with the study.

## Rules

1. **Per-query logging.** One JSONL line per query: run_id, model (+ revision), dataset, query_id, ranked passage IDs,
   scores, metric values, timestamp.
2. **Resumable.** On start, read existing output and skip completed (run_id, query_id) pairs.
3. **Record versions.** Model repo + revision, Python package versions, seeds, machine (CPU/GPU, driver).
4. **One machine per comparison.** Store the machine in every row.
5. **Test small first.** A small sample locally before any cloud run.
6. **No copyrighted text in git.** Raw outputs that quote passages stay in `results/raw/` (git-ignored).
7. **Seeds.** Fix random seeds for training, sampling and bootstrap.
