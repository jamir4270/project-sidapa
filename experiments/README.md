# Experiments

Code for the experiments. Nothing here yet; this is the planned layout and the rules.

## Planned layout

```
experiments/
├── README.md
├── pyproject.toml / requirements.txt
├── configs/                 # one YAML per experiment (models, levels, languages, conditions)
├── src/
│   ├── data/                # load Belebele/SIB-200/Tatoeba/FLORES; build decoy corpus; chunking; dedup
│   ├── search/              # bm25, affix-stripping bm25, embedders, hybrid fusion, ranx scoring
│   ├── llm/                 # llama-server client, prompt template, answer parser
│   ├── quant/               # scripts wrapping convert / llama-quantize / llama-imatrix
│   ├── analysis/            # bootstrap CIs, paired tests, quantization gap, figures
│   └── utils/               # logging, checksums, resumable runner
├── scripts/                 # entry points: run_rq1.py, run_rq2.py, run_rq2b.py
├── notebooks/               # Kaggle/Colab notebooks that call scripts (no logic inside notebooks)
└── results/
    ├── raw/                 # per-item JSONL (git-ignored; copy to private storage)
    └── summary/             # small CSVs/figures safe to commit
```

## Rules

1. **Per-item logging.** One JSONL line per item: run_id, experiment, model, quant level, calibration, language, condition,
   item_id, passage_id, prompt, raw_output, parsed_answer, gold, correct, latency_ms, timestamp.
2. **Resumable.** On start, read existing JSONL and skip completed (run_id, item_id) pairs. A 12-hour session cutoff must lose nothing.
3. **Record versions.** llama.cpp commit, model repo + revision, GGUF SHA-256, Python package versions, machine (CPU/GPU, driver).
4. **One machine per comparison.** Store the machine in every row; analysis refuses to mix machines within a comparison.
5. **Test small first.** 10–20 items locally before any cloud run.
6. **No copyrighted text in git.** Corpora and outputs that quote passages stay in `results/raw/` (ignored) or private storage.
7. **Configs, not edits.** Change behavior via `configs/`, not by editing code between runs.
8. **Seeds.** Fix random seeds for sampling, bootstrap and decoy selection.

## First milestones

- [x] ~~Week 1: speed benchmark on the T14~~ Done by hand in Lab 1; dropped from the thesis (2026-11-22).
- [ ] Week 2: `run_rq1.py --reproduce-mteb` (BM25 + e5 on ceb/tgl/eng); `run_rq2.py` pilot (1 model × Q8/Q4/Q2 × 100 Qs × 3 languages).
