# Compute Plan

**Principle:** hardware changes how long runs take, not whether results are valid. Same model file + same software
= same answers. Two rules: one machine type per comparison; record machine, driver and llama.cpp version.

## Machines

| Machine | Role | Notes |
|---|---|---|
| **ThinkPad T14 Gen 1 (AMD)** — Ryzen 7 PRO 4750U (8C/16T, Zen 2), Radeon Vega 7 iGPU, 16GB DDR4-3200, 256GB SSD, Windows | Coding, debugging (10–50 items), search experiments on CPU, speed/memory benchmarks per level | ~6GB RAM free under Windows; page file 3GB (set to System managed). Est. 3–5 s per Belebele prompt for 4B (estimate). Vega iGPU may lose to CPU; ROCm unsupported; no NPU. Comfortable up to 4B. |
| **Google Colab Pro** ($9.99/mo, 100 compute units) | Main paid compute, January | T4 ≈ 1.2 units/h → ~80+ T4-hours/month (estimate, `VERIFY`). Use T4/L4. Subscribe only when the grid is ready. |
| **Kaggle** (free) | Pilots, backup, building calibration files | ~30 GPU-h/week, 12-h sessions `VERIFY` |
| **Department GPU** | Fastest, if borrowable | Ask: which GPU/VRAM, remote access, booking, storage, install rights |
| **RunPod / Vast.ai** | Emergency backup | RTX 4090 ≈ $0.27–0.69/h `VERIFY` |

**Budget:** Colab Pro for 1–2 months ($10–20). Everything else free.

## Grid size (why the laptop can't run it)

| Part | Count | Prompts |
|---|---|---|
| RQ2, gold passage | 4 models × 5 levels × 3 languages × 900 | 54,000 |
| RQ2, + retrieved and no-passage conditions | × 3 conditions | 162,000 |
| RQ2b, new calibrated files only | 2 models × 2 levels × 3 imatrices (Eng/Ceb/Tgl) × 3 languages × 900 | 32,400 |
| **Total** | | **≈194,000** |

At 3–5 s per prompt (estimate) that is ≈160–270 laptop hours, i.e. 7–11 days non-stop, before retries
(retrieved-passage prompts are longer, so likely more). The "no imatrix" arm of RQ2b reuses the RQ2 files.
Ways to shrink it if needed: retrieved-passage condition in full for Cebuano only; fewer models. Re-estimate
after the week-1 `llama-bench` numbers.

## Laptop actions

- [ ] Task Manager → Performance → Memory → "Slots used." If 1 of 2: a 16GB DDR4-3200 SO-DIMM gives 32GB **and** dual-channel memory (≈2× local AI speed). Lenovo PSREF: one soldered + one SO-DIMM slot, up to 32GB `VERIFIED`.
- [ ] Page file → System managed.
- [ ] Close the browser during runs.
- [ ] Convert full-size models and build imatrix files in the cloud (needs ~8GB+ RAM for 4B).

## Measured numbers (fill in week 1)

| Machine | Backend | Model | pp512 (t/s) | tg128 (t/s) | Peak RAM | Date |
|---|---|---|---|---|---|---|
| T14 | CPU | | | | | |
| T14 | Vulkan | | | | | |

## Cloud habits

- Code on GitHub; cloud only runs tested code.
- Store models and data as **private** datasets (Kaggle) / Drive (Colab); never public.
- Resumable scripts: append each result to JSONL; skip completed IDs on restart.
- Copy results back to the laptop for analysis; delete copyrighted corpora from shared machines when done.
