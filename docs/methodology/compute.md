# Compute Plan

**Principle:** hardware changes how long runs take, not whether results are valid. Same model file + same software
= same answers. Two rules: one machine type per comparison; record machine, driver and llama.cpp version.

## Machines

**Priority (decided 2026-11-21):** 1. AWS → 2. Kaggle / Colab → 3. department research PC (last resort: Jamir would be liable for the machine). Laptop for development and speed benchmarks throughout. Never mix machines inside one comparison.

| Machine | Role | Notes |
|---|---|---|
| **ThinkPad T14 Gen 1 (AMD)** — Ryzen 7 PRO 4750U (8C/16T, Zen 2), Radeon Vega 7 iGPU, 16GB DDR4-3200, 256GB SSD, Windows | Coding, debugging (10–50 items), search experiments on CPU, speed/memory benchmarks per level | ~6GB RAM free under Windows; page file 3GB (set to System managed). Est. 3–5 s per Belebele prompt for 4B (estimate). Vega iGPU may lose to CPU; ROCm unsupported; no NPU. Comfortable up to 4B. |
| **AWS EC2 `g4dn.xlarge`** (1× T4 16 GB, 4 vCPU, 16 GiB), ap-southeast-1 — **main compute** (decided 2026-11-21) | Full grid (RQ2, RQ2b, conditions, extra tasks, RQ3 run); converting models and building imatrix files | Paid from AWS credits. Spot for unattended runs (~$0.29/h snapshot), on-demand for debugging (~$0.736/h) `VERIFY` ([DoIT](https://www.doit.com/compute/spot/ap-southeast-1/g4dn.xlarge)). **Every RQ2/RQ2b comparison on this one type.** |
| **Kaggle** (free) — backup tier 2 | Pilots, backup if AWS falls through | ~30 GPU-h/week, 12-h sessions `VERIFY` |
| **Department research PC** — last resort | Only if AWS and Kaggle/Colab both fail (liability risk) | Ask: which GPU/VRAM, remote access, booking, storage, install rights |
| **Google Colab (Pro if needed)** — backup tier 2 | Backup alongside Kaggle | GPU type varies per session: keep each comparison on one recorded GPU type |
| **RunPod / Vast.ai** | Emergency backup | RTX 4090 ≈ $0.27–0.69/h `VERIFY` |

**Budget (AWS, from credits; all estimates, check the AWS Pricing Calculator):**

| Item | Estimate |
|---|---|
| GPU time ~100–135 h (grid ~54 h at ~1 s/prompt + extras, builds, reruns ×1.5–2) | ~$30–40 spot · ~$75–100 on-demand |
| EBS disk ~150 GB, only during active months (~2) | ~$25–30 |
| S3 (calibration text, imatrix files, results; a few GB) | < $5 |
| Public IPv4 while running, data transfer of results | ~$1 |
| **Total** | **~$60–135** |

Re-estimate after timing the week-2 proof of concept (cost per 1,000 prompts). `g5g.xlarge` (ARM + T4G, ~$0.59/h
on-demand in Singapore `VERIFY`) is the only cheaper option worth testing; `g4ad` (AMD, 8 GB) is ruled out.

## AWS setup (do once, in this order)

| # | Step | Why |
|---|---|---|
| 1 | Check credit amount, program and **expiry** (`TBD`) | Must cover January–March |
| 2 | Create an IAM user for daily work; lock away the root account with MFA | Safety |
| 3 | **AWS Budgets** alert (e.g., at 50% and 80% of the credit) | Catches forgotten resources |
| 4 | **Service Quotas** → request vCPUs for G instances (on-demand **and** spot) in ap-southeast-1 | New accounts often start at 0; approval can take days |
| 5 | Private S3 bucket (block public access on) | Calibration text, imatrix files, results |
| 6 | Launch `g4dn.xlarge` from an NVIDIA/Deep Learning AMI, build llama.cpp with CUDA, run 10–20 items | Week-2 proof of concept doubles as AWS training |

## AWS run workflow

1. Start the instance → `git clone` the scripts → download original weights and Belebele from Hugging Face.
2. Convert → quantize → build imatrix files → run the grid (resumable JSONL, so a spot interruption loses nothing).
3. Copy results and imatrix files to S3 → the script **shuts the instance down** when done.
4. On the laptop: pull results from S3, analyze.

**Cost traps:** EBS disks and snapshots bill while the instance is stopped (delete between active periods); never create
a NAT gateway; no SageMaker notebooks; Singapore costs ~40% more than us-east-1 (accepted for now).

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
- Store models, calibration text and results in the **private** S3 bucket (Kaggle private datasets for backup runs); never public.
- Resumable scripts: append each result to JSONL; skip completed IDs on restart.
- Copy results back to the laptop for analysis; delete copyrighted corpora (decoy news text) from cloud storage when done.
- Record instance type, AMI, NVIDIA driver/CUDA version and llama.cpp commit in every run log.
