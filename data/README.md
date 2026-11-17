# data/ — local only

Everything in this folder except this README is **git-ignored**. Never commit or upload it publicly.

## Expected contents

```
data/
├── models/          # GGUF files (large; keep only what you're using)
├── belebele/        # downloaded via `datasets` (cached)
├── decoys/
│   ├── ceb/         # cleaned CebuaNER chunks (+ HPLT top-up)
│   ├── tgl/         # NewsPH chunks
│   └── eng/         # English news chunks
├── calibration/     # ceb/tgl/eng calibration text (~100 KB each)
└── imatrix/         # built importance-matrix files
```

## Why it's private

News texts (CebuaNER, NewsPH, scraped pages) are copyrighted. Research use is fair use; redistribution is not.
Share build scripts and source IDs instead. See `docs/methodology/data-and-licensing.md`.

## Storage budget

Reserve ~40–60 GB on the 256 GB SSD. A 4B model is ~2.5 GB at Q4, ~4.3 GB at Q8, ~8 GB at full precision (estimate).
