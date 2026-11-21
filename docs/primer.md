# Search and Shrink — A Primer

*From the problem to the methodology, written for Jamir. Last updated 2026-11-17.*

## How to read this

- **Part I** explains the problem: what Cebuano AI looks like, how question-answering AI works, and what
  "compressing" a model means.
- **Part II** covers what earlier studies already did, and where your study fits.
- **Part III** walks through the methodology one layer at a time, including the steps you haven't done before.
- **Part IV** lists the study's weaknesses, the decisions still open, the claims you can't use yet, and the order of work.

Claims carry evidence tags: `VERIFIED` (checked against a source), `VERIFY` (confirm before relying on it),
`TBD` (a decision or value still to set) and `UNCONFIRMED` (not found or not opened). Numbers marked
"(estimate)" are reasoned guesses, not measurements.

**The analogy used throughout:** an *open-book exam in a library*. A **librarian** (search) finds the right
page; a **student** (the language model) reads it and answers. Your thesis tests both, in Cebuano.

---

# Part I — The problem

## 1. Cebuano and AI

Cebuano (Bisaya, Binisaya) is spoken by roughly 20 million people, mostly in the Visayas and Mindanao `VERIFY`.
For AI, it is a **low-resource language**: there is little clean digital text to learn from.

That sounds odd, because Cebuano Wikipedia is one of the largest Wikipedias in the world. The catch: about 99% of
it was written by a bot (Lsjbot), and deduplication removes about 80% of its articles `VERIFIED`
([arXiv 2411.05527](https://arxiv.org/pdf/2411.05527)). Huge on paper, thin in real human-written text.

Consequence: models see far less real Cebuano than English or even Tagalog, so their Cebuano is weaker and
more fragile.

## 2. How a question-answering AI works (RAG)

RAG ("retrieval-augmented generation") = the open-book exam.

1. **Search (retrieval):** given a question, find the passages most likely to contain the answer.
2. **Read (generation):** give the question and the passages to a language model, which writes the answer.

Two kinds of librarian:

| Librarian | How it works | Strength | Weakness |
|---|---|---|---|
| **Keyword (BM25)** | Scores passages by shared words; rare words count more | Fast, reliable, needs no training | Literal: "bagyo" won't match "typhoon" |
| **Meaning (embeddings)** | A model turns text into vectors; similar meanings land close together | Matches meaning across different words | Only as good as its training in that language |

## 3. Shrinking a model (quantization)

A language model is billions of numbers (**parameters**). "4B" = 4 billion. Normally each is stored in 16 bits.
**Quantization** stores them with fewer bits: 8, 4, even 2. Like saving a photo as a smaller JPEG: it's smaller
and faster, but some detail is lost.

- **GGUF** is the file format used by **llama.cpp**, the free program that runs compressed models on ordinary computers.
- Its compression levels are named by bits: **Q8_0** (≈8-bit, light), **Q6_K**, **Q4_K_M**, **Q3_K_M**, **Q2_K** (≈2-bit, heavy).

**Why this matters for Cebuano:** research shows compression damage is *uneven across languages*. Picture a
photo where English is the big, bright subject and Cebuano is the fine print in the corner: compress the photo
and the fine print blurs first. Studies found automatic scores can barely move while human raters see real
damage, and that low-resource languages and smaller models suffer more `VERIFIED`
([Marchisio et al. 2024, arXiv 2407.03211](https://arxiv.org/html/2407.03211v2);
[Marie & Fujita 2025, arXiv 2508.20893](https://arxiv.org/abs/2508.20893)).

## 4. The "study guide" (calibration / importance matrix)

When llama.cpp compresses a model, it can first run sample text through it to see which numbers matter most,
and protect those. That record is an **importance matrix (imatrix)**. The sample text is the "study guide."
By default llama.cpp uses **no** study guide at all `VERIFY`. Many ready-made GGUF files on Hugging Face were
built with a community study guide that is mostly English `VERIFY` (check the uploader's model card). So "no
guide" and "English guide" are two different baselines, and both are arms in RQ2b. For the same reason, quantize
every model yourself from one full-precision file; never mix in downloaded GGUFs whose study guide is unknown.

**The open question:** does a Cebuano study guide protect Cebuano? A 2026 study found Indonesian calibration
did little for Philippine languages `VERIFIED` ([Waskito et al.](https://aclanthology.org/2026.findings-aacl.9/)),
and a community llama.cpp test with English, Norwegian and Malayalam imatrices found no significant difference
`VERIFY` (Reddit r/LocalLLaMA). So the answer could go either way, and a measured "no difference" is still useful.

## 5. Why it matters

Philippine developers building offline tools (barangay health, schools, LGU advisories) will run small, compressed
models on cheap hardware. Right now nobody can tell them how much Cebuano quality they lose, or how to reduce the loss.
This study gives them numbers measured on hardware like theirs.

---

# Part II — What earlier studies did

## 6. Prior work, and how your study differs

| Work | What it did | What it didn't do (your gap) |
|---|---|---|
| **MTEB BelebeleRetrieval** (part of MMTEB) | Search task built from Belebele: 488 passages, 900 questions per language, incl. `ceb_Latn`, `tgl_Latn`. Public scores for ~259 models. Cebuano nDCG@10: BM25 0.784; multilingual-e5-large-instruct 0.875; bge-m3 0.844; Qwen3-Embedding-0.6B 0.769 `VERIFIED` ([results repo](https://github.com/embeddings-benchmark/results)) | Tiny, easy corpus (near ceiling). No analysis paper. No distractors, no Cebuano-aware keyword search, no answer generation, no compression. |
| **CebQA / CebQuAD** (Lagumbay & Roxas, UP Cebu; Springer chapter) | End-to-end Cebuano QA: BM25 vs DPR retrieval, XLM-RoBERTa extractive reader. BM25 best (63% retriever accuracy); end-to-end F1 49.50 at k=1. CebQuAD = GPT-4o-mini-generated questions from Cebuano news, speaker-validated `VERIFIED` (project page) | Older retriever (DPR), extractive reader, no compressed generative models, LLM-generated questions. Venue, year, size, license `UNCONFIRMED`. |
| **FilBench** (EMNLP 2025) | 27 LLMs on Tagalog/Filipino/Cebuano tasks. GPT-4o best at 72.23% (paper also says 75.56% — internal inconsistency); best SEA model SEA-LION v3 70B 61.07% `VERIFIED` ([arXiv 2508.03523](https://arxiv.org/html/2508.03523v1)) | No retrieval category; small Cebuano slices (SIB-200 = 99 items); no compression study. |
| **SEA-BED** (ACL 2026) | Embedding benchmark for 10 SEA languages, 169 datasets `VERIFIED` ([arXiv 2508.12243](https://arxiv.org/html/2508.12243v2)) | No Cebuano; no Filipino retrieval tasks. |
| **Waskito et al.** (Findings of IJCNLP-AACL 2026) | GPTQ 2/3/4-bit on 8B models; perplexity on FLORES+ for 17 Austronesian languages incl. CEB, FIL, WAR, ILO, PAG; Indonesian calibration; Philippine languages showed low transfer `VERIFIED` ([ACL](https://aclanthology.org/2026.findings-aacl.9/)) | Perplexity only (not task accuracy); GPTQ not GGUF; no Philippine-language calibration; Belebele only on 5 non-Philippine languages. |
| **Marie & Fujita** (arXiv 2508.20893) | Translation under quantization (incl. GGUF Q4_K_M, Q2_K) for 55 languages incl. `en-fil_ph`; low-resource languages hit hardest; same-language calibration helps at low bits `VERIFIED` | Filipino scores released but not analysed (rows `VERIFY`). No Cebuano. Translation only. |
| **Marchisio et al. 2024** | Quantization hurts non-Latin and low-resource languages more; automatic metrics understate it `VERIFIED` | No Philippine languages. |

## 7. Your gap, in one sentence

> Cebuano search has public baselines, but no study has measured how much **task accuracy** Cebuano loses when
> models are compressed for offline use, or whether **calibrating with Cebuano text** reduces that loss; prior
> Philippine-language work measured perplexity only, with Indonesian calibration.

**The upside of prior work:** free baselines to reproduce (MTEB's 0.784), a local comparison point (CebQA),
and proof that a 2026 ACL venue considers Philippine-language quantization worth measuring.

---

# Part III — Your methodology, layer by layer

## 8. The whole pipeline

```
 Cebuano question (Belebele)
          │
          ▼
 ┌──────────────────────┐     RQ1: does it find the right page?
 │ Search               │ ──► Recall@5, nDCG@10 on a library with thousands of decoys
 │ BM25 / embeddings /  │
 │ hybrid               │
 └──────────┬───────────┘
            │ top passage (or the gold passage, or none)
            ▼
 ┌──────────────────────┐     RQ2: how much does compression cost?
 │ Small model, GGUF    │ ──► accuracy per level, Cebuano vs Tagalog vs English
 │ Q8_0 … Q2_K          │     RQ2b: does a Cebuano study guide help?
 └──────────┬───────────┘
            │ answer letter (A–D)
            ▼
 ┌──────────────────────┐     RQ3: what kinds of mistakes?
 │ Score vs answer key  │ ──► wrong answers sorted; linguist verifies categories
 └──────────────────────┘
```

## 9. Layer 0 — the data

| Dataset | What | Use |
|---|---|---|
| **Belebele** (`facebook/belebele`; `ceb_Latn`, `tgl_Latn`, `eng_Latn`) | 900 multiple-choice reading questions over 488 passages per language; passages average ~79 words; CC BY-SA 4.0 `VERIFIED` | Backbone for RQ1 and RQ2 |
| **SIB-200** | Topic classification, 99 Cebuano items | RQ2 small check |
| **Tatoeba ceb→eng** | ~2,900 sentence pairs `VERIFY` | RQ2 translation check |
| **FLORES+** | Professionally translated sentences | One perplexity run to compare with Waskito |
| **Decoys** (CebuaNER news texts, ~4,258 articles; NewsPH for Tagalog) | Real text that answers no question | RQ1 realistic library |
| **Calibration text** (Leipzig Cebuano, ~729k sentences, CC BY) | Sample text for the "study guide" | RQ2b |

Belebele passages are translations of English source texts (FLORES), so they're cleaner than real-world Cebuano.
State this as a limitation. Full detail: `methodology/data-and-licensing.md`.

## 10. Layer 1 — search (RQ1)

- **Reproduce first:** run MTEB's BelebeleRetrieval for ceb/tgl/eng with BM25 and multilingual-e5-large-instruct.
  Your numbers should match the published ones (0.784 and 0.875 for Cebuano). This proves your pipeline is correct.
- **Then go beyond MTEB:**
  - Add 5,000–10,000 real decoy passages per language (same size for each language).
  - Try a **Cebuano affix-stripping BM25** (strip prefixes like *nag-/mag-/gi-/mi-*), since keyword search
    struggles with Cebuano's verb forms.
  - Try a **hybrid** that merges BM25 and embedding rankings.
  - Plot accuracy against library size (500 / 2,000 / 10,000 decoys).
- **Metrics:** Recall@5 (is the right page in the top 5?), nDCG@10 (rewards ranking it higher).

## 11. Layer 2 — the compressed reader (RQ2)

- **Models:** 3–4 small open models, 1.5B–4B (candidates: Qwen3 1.7B/4B, Gemma 3 4B, Llama 3.2 3B,
  SeaLLMs v3 1.5B) `TBD` final list. Optional: one 7–8B model if cloud time allows.
- **Levels:** Q8_0, Q6_K, Q4_K_M, Q3_K_M, Q2_K (+ full-precision reference if hardware allows).
- **Conditions:** gold passage, retrieved passage, no passage (closed-book).
- **Prompt:** one fixed template, instructions in English, passage and question in the test language, answer with one letter.
  Temperature 0. Parse the first A–D letter; unparseable = wrong, and report the parse-failure rate (it's a finding).
- **Headline number — the quantization gap:** (Cebuano drop from Q8 to level X) minus (English drop from Q8 to level X), with a confidence interval.

### The steps you haven't done before

| Step | What it is | Command (check current llama.cpp README `VERIFY`) |
|---|---|---|
| Download | Get model weights from Hugging Face | `huggingface-cli download Qwen/Qwen3-4B --local-dir qwen3-4b` |
| Convert | Turn weights into one full-precision GGUF file | `python convert_hf_to_gguf.py qwen3-4b --outfile qwen3-4b-f16.gguf` |
| Quantize | Make the compressed versions | `llama-quantize qwen3-4b-f16.gguf qwen3-4b-Q4_K_M.gguf Q4_K_M` |
| Calibrate (RQ2b) | Build the study guide, then compress with it | `llama-imatrix -m qwen3-4b-f16.gguf -f ceb_calib.txt -o ceb.imatrix` then `llama-quantize --imatrix ceb.imatrix …` |
| Serve | Run the model as a local API your Python calls | `llama-server -m qwen3-4b-Q4_K_M.gguf` |
| Benchmark speed | Tokens per second on a machine | `llama-bench -m model.gguf` |

Converting and building calibration files need the full-size model in memory (~8GB for 4B) → do these in the cloud.

## 12. Layer 2b — calibration (RQ2b)

- 2 models × 2 levels (Q3_K_M, Q2_K) × 4 study guides (none, English, Cebuano, Tagalog) × 3 test languages.
- The Tagalog arm asks whether a sibling language transfers (extending Waskito's Indonesian finding).
- **Rule:** calibration text must never overlap Belebele/FLORES passages, or test data leaks into the study guide.

## 13. Layer 3 — errors (RQ3)

Multiple-choice answers are just letters, so the taxonomy uses outputs with words: a run where the model writes a
short reason before answering (200 Cebuano questions at Q8 and Q2), plus the Tatoeba translations.

1. You collect 200–300 wrong outputs and write first-pass notes.
2. A **Cebuano linguist** finalizes 5–8 categories into a codebook.
3. The linguist labels the errors (or a random 100 if time is short; you label the rest with the codebook).
4. You label the same 100 blind; compute **Cohen's kappa** (aim ≥ 0.6). Disagreements → linguist's label wins.
5. Show which categories grow with compression.

Starter categories to test: answered in Tagalog, fell back to English, misread a Cebuano word, wrong verb form
(*mipalit* vs *gipalit*), mangled a name, made up a fact, ignored instructions, right reasoning but wrong letter.
Full detail: `methodology/error-taxonomy.md`.

## 14. Statistics

Small test sets make scores wobbly. Rules (after [Miller 2024, "Adding Error Bars to Evals"](https://arxiv.org/html/2411.00640v1) `VERIFIED`):

- 95% confidence interval on every number, via **clustered bootstrap** (resample passages, since several questions share one).
- **Paired** comparisons when two settings answer the same questions.
- Don't claim a difference whose interval includes zero.
- Lean on Belebele (900 items) for main claims, not SIB-200 (99 items).

## 15. Compute

Your T14 is for code and small test runs. The full grid runs on **AWS EC2 `g4dn.xlarge`**
(one T4 GPU, paid from credits; decided 2026-11-21) with **Kaggle** as free backup; the department GPU if borrowable. Hardware changes speed, not results,
as long as each comparison runs entirely on one machine type. Full detail: `methodology/compute.md`.

---

# Part IV — Weaknesses and open decisions

## 16. Weaknesses a panel will find

| Weakness | Why it matters | Responses |
|---|---|---|
| "You're just running benchmarks" | Panels want a contribution, not a re-run | The contribution is the measurements nobody published (task accuracy under GGUF compression in Cebuano, Cebuano calibration, error taxonomy) |
| Belebele is translated, not native Cebuano | Cleaner than real text; may understate difficulty | State it; add real Cebuano decoys; optional CebQuAD or hand-written set |
| Small test sets | Wide error bars | Report intervals; main claims on 900-item Belebele |
| Calibration may make no difference | A null result | It's still a finding; report with tight intervals |
| Search adds little beyond MTEB | Weak RQ1 | RQ1 is supporting; RQ2/RQ2b stand alone |
| Compressed models fail to follow format at Q2 | Unparseable answers | Report parse-failure rate as a result |
| Error categories are subjective | "Just your opinion" | Linguist finalizes codebook; kappa on 100 double-labeled items |
| Prompt sensitivity | Results may depend on wording | Fix one template; optionally test a second on a small subset |
| Contamination | Models may have seen Belebele | Closed-book baseline shows how much is memorized |

## 17. Open decisions

1. Final model list (3 or 4 models; include a 7–8B?) `TBD`
2. Instructions in English vs. Cebuano in the prompt `TBD` (discuss with adviser)
3. Which proposal chapters the Dec 18 defense covers (VSU DCST format) `TBD`
4. Linguist: who, and how many hours `TBD`
5. Main compute: AWS decided 2026-11-21; credit expiry and GPU quota still `TBD`
6. Whether to include CebQuAD (depends on its license) `TBD`

## 18. Claims you cannot use yet

| Claim | Status |
|---|---|
| "First Cebuano retrieval baselines" | **Taken** (MTEB, CebQA). Don't use. |
| "First quantization study on any Philippine language" | **Taken** (Waskito; Marie & Fujita). Don't use. |
| CebQA venue, year, CebQuAD size and license | `UNCONFIRMED` |
| Filipino rows in Marie & Fujita's released data | `VERIFY` |
| Whether Waskito et al. had an earlier arXiv preprint | `VERIFY` |
| arXiv 2505.20276 ("4-bit hurts non-English more") | `UNCONFIRMED` — couldn't open; don't cite |
| Cloud run times | Estimates; measure in the proof of concept (laptop measured in Lab 1: ~5–9 s/prompt) |
| Kaggle quota, AWS instance prices, RunPod prices | `VERIFY` at time of use |
| Cebuano speaker count (~20 million) | `VERIFY` |

## 19. Order of work

1. ~~NCRC-V reality check~~ Done 2026-11-21; copra dropped. No pre-approval step; adviser weighs in at the defense.
2. Proof of concept: reproduce MTEB numbers; one 4B model at Q8/Q4/Q2 on 100 questions per language.
3. Draft proposal chapters; defend Dec 18.
4. Holiday: panel revisions, decoy corpus, calibration text, resumable scripts.
5. January–February: RQ2, RQ2b, RQ1, conditions, statistics.
6. Late Feb–March: RQ3 with the linguist.
7. March–May: write, revise, defend.

Week-by-week detail: `timeline.md`.

---

## Glossary

| Term | Meaning |
|---|---|
| BM25 | Keyword search scoring; rare shared words count more |
| Belebele | Multiple-choice reading benchmark in 122 language variants |
| Calibration / imatrix | Sample text llama.cpp uses to decide which weights to protect when compressing |
| Closed-book | Asking the model with no passage, to see what it answers from memory |
| Cohen's kappa | Agreement between two labelers, corrected for chance; 0.6+ is good |
| Confidence interval | The ± range around a score |
| Decoys (distractors) | Real passages added to the library that answer no question |
| Embeddings | Text turned into number vectors so similar meanings are close |
| GGUF | llama.cpp's model file format |
| Gold passage | The passage that actually contains the answer |
| llama.cpp | Free software that runs and compresses models on ordinary hardware |
| nDCG@10 | Search score rewarding the right passage ranked higher in the top 10 |
| Perplexity | How "surprised" a model is by text; cheap, but not task accuracy |
| Quantization | Storing model numbers with fewer bits to shrink it |
| Quantization gap | How much faster Cebuano accuracy drops than English as compression increases |
| RAG | Retrieval-augmented generation: search, then answer |
| Recall@k | Share of questions whose right passage is in the top k |
