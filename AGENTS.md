# AGENTS.md — Cebuano Thesis ("Search and Shrink")

Context and working rules for any AI agent (Claude or otherwise) helping with this thesis.
Read this file fully before doing anything. Then read `docs/status.md`.

---

## 1. The project in one paragraph

An undergraduate BS Computer Science thesis at Visayas State University (VSU), Baybay City, Leyte.
Working title (decided 2026-11-22): **"Search and Shrink: Quantization and Calibration Losses for Cebuano,
Tagalog and English in Small Offline Language Models."** The study measures how much accuracy small,
open-weight language models lose in Cebuano (versus Tagalog and English) when they are compressed
(quantized) to run offline on cheap hardware, and whether calibrating the compression with Cebuano
text reduces that loss. A supporting chapter measures Cebuano search (BM25 vs. multilingual embeddings)
on a realistic corpus and feeds the results into the compressed models. A Cebuano linguist verifies an
error taxonomy of the models' mistakes. It is a **measurement study, not a system build**: the pipeline
is apparatus; the contribution is the research questions, the experiment grid and the analysis.

## 2. The researcher

- **Jamir Oasis M. Andrade**, senior BSCS student at VSU, DOST undergraduate scholar, graduating July 2027.
- **Native Cebuano speaker.** This is a research asset (error analysis, data sanity checks).
- **Strong software engineering / web-dev background; casual (non-expert) knowledge of ML and NLP.**
- Starts job applications in January 2027, so January–February experiments should be as hands-off as possible.

### How to communicate with him

- Explain in **plain language with analogies**. Define every piece of jargon on first use.
- He works best with **clear visibility**: tables, checklists, explicit next steps, dates.
- Be **critical and pragmatic**. Point out weak spots, risks and overclaims directly. Do not flatter.
- Short sentences. Lead with the answer, then the detail.

## 3. Current status (snapshot — `docs/status.md` is the live version)

- **As of 2026-11-17:** topic chosen, novelty checked, plan written. Nothing has been run yet.
- **As of 2026-11-21:** the NCRC-V check is done and the **copra study is dropped**; this is the thesis topic.
  No adviser approval is needed before the proposal: the adviser and panel weigh in **at the proposal defense**.
  Background: `reference/copra-study.md`.
- **Next milestone:** proposal defense on **Friday, 2026-12-18**. The proposal covers the first chapters
  (introduction, review of literature, methodology; see `docs/proposal/README.md` for the open question
  about chapter numbering).
- **Final defense:** mid to late May 2027.

## 4. Research questions (current framing)

RQ numbers follow the pipeline order (search, then read). **RQ2 + RQ2b are the core contribution.**

| ID | Question | Role |
|---|---|---|
| RQ1 | Starting from published MTEB Belebele baselines, how much does Cebuano search accuracy drop on a realistic corpus with thousands of real Cebuano distractor passages, and do Cebuano-aware keyword search or hybrid search close the gap to Tagalog and English? | Supporting |
| RQ2 | How much accuracy does each GGUF quantization level (Q8_0 → Q2_K) cost in Cebuano and Tagalog versus English, when a small model answers from the correct passage, a retrieved passage, or no passage? | **Core** |
| RQ2b | At the lowest levels (Q3_K_M, Q2_K), does calibrating the compression (llama.cpp importance matrix) with Cebuano or Tagalog text recover accuracy compared with English or no calibration? | **Core, most original** |
| RQ3 | What kinds of mistakes do the models make in Cebuano, and which kinds grow with compression? (Categories finalized and verified by a Cebuano linguist.) | Supporting |

Full detail: `docs/methodology/research-questions.md`.

## 5. Novelty: what is taken and what is ours (checked 2026-11-17)

**Do not claim these. They already exist:**
- "First Cebuano retrieval baselines." → MTEB's **BelebeleRetrieval** task covers `ceb_Latn`/`tgl_Latn` with
  ~259 models' public scores, including BM25 = 0.784 nDCG@10 on Cebuano. **CebQA** (UP Cebu, Springer chapter)
  compared BM25 vs DPR on Cebuano news.
- "First quantization study on any Philippine language." → **Waskito et al. (Findings of IJCNLP-AACL 2026)**
  measured perplexity of GPTQ-quantized models on Cebuano/Filipino/Waray/Ilocano/Pangasinan (Indonesian
  calibration only). **Marie & Fujita (arXiv 2508.20893)** released GGUF Filipino translation scores without analysis.

**Safe claims (always prefix with "to our knowledge"):**
- First systematic **downstream-task** evaluation of GGUF/llama.cpp quantization (Q8_0–Q2_K) in Cebuano and Tagalog.
- First test of **Cebuano- and Tagalog-language calibration** for llama.cpp quantization.
- End-to-end Cebuano search-then-answer test on a realistic corpus, building on MTEB and CebQA baselines.
- A Cebuano error taxonomy of LLM output, verified by a linguist.

Full detail: `docs/literature/novelty-check.md`.

## 6. Hard rules for agents

1. **Never invent sources, numbers, quotes or results.** If you don't have it, say so and mark it `VERIFY`.
2. **Evidence tags.** Every factual claim in project docs carries one of:
   - `VERIFIED` — checked against the original source (link it).
   - `VERIFY` — plausible, from a secondary source or memory; confirm before relying on it.
   - `TBD` — a decision or value not yet set (e.g., set with the adviser or linguist).
   - `UNCONFIRMED` — searched for but not found or not opened.
   Don't upgrade a tag without opening the source. Estimates are labeled "(estimate)".
3. **No overclaiming novelty.** Use the safe wording in section 5. If you find new prior work, add it to
   `docs/literature/sources.md` and flag it in `docs/status.md` immediately.
4. **Copyright.** Never commit or publish copyrighted corpus text (news articles, CebuaNER texts, scraped pages).
   `data/` is git-ignored. Share code plus source IDs/URLs, not article text. See `docs/methodology/data-and-licensing.md`.
5. **Reproducibility.** Every experiment logs per-item JSONL (prompt, raw output, parsed answer, score),
   model file checksum, llama.cpp version, hardware. Scripts must be resumable. See `experiments/README.md`.
6. **One machine per comparison.** Never mix laptop and cloud results inside one comparison.
7. **Statistics.** Every reported score gets a 95% confidence interval; comparisons on the same items use
   paired tests; clustered bootstrap by passage. Don't claim a difference whose interval includes zero.
8. **Scope lock.** Extensions (CebQuAD, hand-written Cebuano test set) stay "if time permits." Don't add models,
   languages or tasks without the researcher agreeing and logging it in `docs/decisions.md`.
9. **Decisions get logged.** Any change to RQs, grid, datasets, tools or schedule → append to `docs/decisions.md`
   with date and reason. Keep `docs/status.md` current after every working session.
10. **Ask before destructive or outward actions** (deleting files, sending emails, publishing, spending money).

## 7. Hardware and compute

| Machine | Use | Notes |
|---|---|---|
| Lenovo ThinkPad T14 Gen 1 — Ryzen 7 PRO 4750U (Zen 2), Vega 7 iGPU, 16GB DDR4 (≈6GB free under Windows), 256GB SSD | Code, debugging on small samples, search experiments (CPU), speed/memory benchmarks | Expect ~3–5 s per Belebele prompt for a 4B model (estimate). Vega iGPU may not beat CPU via Vulkan; ROCm unsupported; no NPU. Up to 4B models comfortably. |
| AWS EC2 `g4dn.xlarge` (T4 16 GB), ap-southeast-1, paid from credits | Main compute for the full grid (decided 2026-11-21; replaces Colab Pro) | Spot for unattended runs; one instance type for every comparison; budget alert on. |
| Kaggle (free) | Pilots, backup, building calibration files | ~30 GPU-h/week, 12-h sessions (VERIFY current quota) |
| Department GPU | Fastest option if borrowable | Borrowing rules TBD |
| RunPod | Emergency paid backup | ~$0.34–0.69/h for an RTX 4090 (VERIFY) |

Full detail: `docs/methodology/compute.md`.

## 8. Repository map

```
cebuano-thesis/
├── AGENTS.md                  ← you are here (rules + context)
├── CLAUDE.md                  ← imports AGENTS.md for Claude tools
├── README.md                  ← human-facing map of the project
├── KICKSTART_PROMPT.md        ← the prompt that starts a new Claude session
├── docs/
│   ├── status.md              ← LIVE: where we are, this week, blockers (update every session)
│   ├── primer.md              ← the long explainer: background → prior work → methods → risks
│   ├── at-a-glance.md         ← one-page overview with analogies
│   ├── decisions.md           ← dated decision log + open decisions
│   ├── timeline.md            ← week-by-week plan to the final defense
│   ├── literature/
│   │   ├── sources.md         ← every source, with evidence tags
│   │   └── novelty-check.md   ← what's taken, what's ours, safe wording
│   ├── methodology/
│   │   ├── research-questions.md
│   │   ├── experiment-design.md   ← grid, fixed settings, statistics
│   │   ├── data-and-licensing.md  ← datasets, decoy corpus, copyright
│   │   ├── error-taxonomy.md      ← RQ3 protocol with the linguist
│   │   └── compute.md
│   ├── labs/                  ← hands-on learning labs (e.g. running a local model)
│   ├── proposal/              ← chapter drafts for the proposal defense
│   └── meetings/              ← adviser, NCRC-V, linguist meeting notes
├── reference/
│   ├── copra-study.md         ← the dropped previous study (background only)
│   └── reports/               ← earlier research reports (read-only background)
├── experiments/               ← code lives here (see experiments/README.md)
└── data/                      ← local only, git-ignored (copyrighted corpora, model files)
```

## 9. How to work in this repo

- **Start of every session:** read `docs/status.md`, then the file(s) relevant to the task.
- **End of every session:** update `docs/status.md` (what changed, next steps, blockers) and, if any decision
  was made, `docs/decisions.md`.
- **Writing thesis chapters:** draft in `docs/proposal/`, in Markdown. Keep claims tagged until verified;
  strip tags only in the final export.
- **Writing code:** follow `experiments/README.md`. Test on 10–20 items locally before any cloud run.
- **When unsure:** ask one clear question rather than guessing. When the researcher isn't available,
  take the most conservative reading and note it in `docs/status.md`.
