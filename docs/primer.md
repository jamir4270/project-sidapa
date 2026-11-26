# Cebuano Retrieval Study — At a Glance + Primer

*For Jamir, to read and use when shaping the study. It is background and a map of choices, not a design. Anything
marked **your call** is an open decision. Evidence tags as in AGENTS.md: `VERIFIED` (opened), `VERIFY` (from memory
or a secondary source), `UNCONFIRMED` (not found), `TBD` (not decided). The workspace was reset on 2026-11-26, so
earlier source notes are gone: every tag here needs re-checking when you add the source to `literature/`.*

**The analogy used throughout:** a **library**. The **passages** are the books, the **query** is a patron's request,
and the **retriever** is the librarian who brings back the few books most likely to help. A RAG system then hands
those books to a **reader** (a language model) to answer. This study is about the librarian only.

---

# Part A — At a glance

## The study in one sentence (working shape, yours to change)

Does an embedding model **fine-tuned on Cebuano** find the right Cebuano passage better than **off-the-shelf
multilingual** embedding models, on in-domain news, on other kinds of text, and on the way people actually search?

## The pieces

| Piece | Working idea | Status |
|---|---|---|
| Independent variable | The retriever: BM25 · off-the-shelf multilingual embedders · the same embedder(s) fine-tuned on Cebuano | **your call** which models |
| Dependent variables | Retrieval scores: Recall@k, MRR@10, nDCG@10 | Standard; which is the headline is **your call** |
| Output (artifact) | A fine-tuned Cebuano embedding model | Counts only if it beats baselines on a credible test |
| Training data | Options: CebQuAD train split, CebuaNER passages, translated English pairs | **your call** |
| Test data | Options: CebQuAD test (in-domain), Belebele (formal, translated), a human-written query set (colloquial / code-switched) | **your call** |
| Statistics | Paired bootstrap confidence intervals | Method known; claims `TBD` |

## What already exists vs. what seems open (first-pass search, `UNCONFIRMED` until redone)

| Already done (don't claim) | Seems open (claim only "to our knowledge") |
|---|---|
| Cebuano retrieval baselines: MTEB BelebeleRetrieval; CebQA (BM25 beat dense search) | An embedder **fine-tuned for Cebuano retrieval** with reported Cebuano scores |
| A Cebuano QA dataset: CebQuAD (LLM-generated, speaker-validated questions) | A Cebuano retrieval test set with **human-written** queries, incl. colloquial and Bisaya–English |
| The method works for other low-resource languages: Armenian (2026), Yorùbá/Igbo/Hausa (2025) | How much **code-switched** Cebuano queries hurt retrieval, and whether fine-tuning helps |
| Code-switched retrieval benchmark, but only English–Chinese/Japanese (CSR-L, 2026) | |

## Key dates

| Date | What |
|---|---|
| Fri 2026-11-27 | SRC meeting, FM-VPA-06/07 |
| 2026-12-07 | Full draft to adviser |
| **2026-12-18** | **Proposal defense** |
| Mid–late May 2027 | Final defense |

---

# Part B — Primer

## 1. Why retrieval, and why Cebuano

- **RAG** (retrieval-augmented generation) = librarian + reader. If the librarian brings the wrong book, the best reader
  still answers wrong. So retrieval quality caps the whole system.
- Cebuano has ~20 million speakers `VERIFY`, but little clean digital text; Cebuano Wikipedia is ~99% bot-written
  (arXiv 2411.05527, `VERIFY`). Most search models learned Cebuano only as a small slice of huge multilingual training.
- Real Cebuano searches mix in English ("Bisaya–English" / "Bislish") and use everyday wording. Benchmarks built from
  formal, translated text may not show how models handle that.

**Read:** Lewis et al. 2020, "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," NeurIPS `VERIFY`.
Skim the intro and figure 1 only.

## 2. How a librarian works: three kinds of retriever

| Kind | How it works | Library analogy | Strength / weakness |
|---|---|---|---|
| **BM25** (lexical) | Scores each passage by shared words, rare words count more | Index cards by keyword | Fast, no training, great on names/numbers; misses synonyms and affixed forms (*mipalit* vs *gipalit*) |
| **Bi-encoder** (dense embedder) | Turns query and passage separately into vectors; nearest vectors win | A "map of meaning" where similar books sit close | Handles paraphrase; quality depends on training; the passage map is built once in advance |
| **Cross-encoder** (reranker) | Reads query and passage *together*, outputs a relevance score | A librarian who skims each shortlisted book | Most accurate, too slow for a whole library; used to re-order a top-50 |

**Key terms:** *token* (sub-word piece the model reads), *embedding/vector* (the list of numbers for a text),
*cosine similarity* (how close two vectors point), *corpus* (all passages), *index* (the pre-computed passage vectors).

**Read:**
1. Robertson & Zaragoza 2009, "The Probabilistic Relevance Framework: BM25 and Beyond" `VERIFY`. The BM25 formula
   sections only; enough to explain *k1* and *b*.
2. Reimers & Gurevych 2019, "Sentence-BERT," EMNLP `VERIFY`. The idea of a bi-encoder (figure 1).
3. Karpukhin et al. 2020, "Dense Passage Retrieval for Open-Domain Question Answering," EMNLP `VERIFY`. The classic
   dense-vs-BM25 comparison; note *in-batch negatives*. CebQA's "DPR" is this method.
4. Manning, Raghavan & Schütze 2008, *Introduction to Information Retrieval*, Cambridge (free online) `VERIFY`.
   Ch. 6 (scoring) for BM25 background.

## 3. How an embedder is trained

- **Contrastive learning:** show the model a query, its correct passage (*positive*), and wrong passages (*negatives*).
  Pull the positive closer, push negatives away. Like teaching the librarian with "this book, not those."
- **In-batch negatives:** the other queries' positives in the same batch serve as free negatives. Bigger batches give
  more negatives (why "cached" losses that simulate big batches exist).
- **Hard negatives:** wrong passages that *look* right (e.g. top BM25 results that aren't the answer). They teach more
  than random ones. Risk: a "hard negative" that actually answers the query (a false negative) teaches the wrong thing.
- **Pretraining vs fine-tuning:** big models (E5, BGE-M3) were already trained contrastively on huge multilingual data.
  Fine-tuning nudges them toward one language or domain with a small dataset.
- **Where training pairs come from:** an existing QA dataset (CebQuAD), LLM-generated queries for passages
  (E5/Gecko-style), or translating English pairs (the Armenian study's route).
- **Two risks to understand before deciding:** (1) *in-domain overfitting*: gains on data like the training set may
  not carry over (the Nigerian study: big gains on its own test, almost none on MIRACL); (2) *circularity*: if
  training and test questions come from the same generator, the model may learn the generator's style.

**Read:**
1. Wang et al. 2022, "Text Embeddings by Weakly-Supervised Contrastive Pre-training" (E5), arXiv 2212.03533 `VERIFY`.
2. Wang et al. 2024, "Multilingual E5 Text Embeddings: A Technical Report," arXiv 2402.05672 `VERIFY`. The model
   family the Armenian study fine-tuned; check which languages and data it used.
3. Chen et al. 2024, "BGE M3-Embedding," arXiv 2402.03216 `VERIFY`. Dense + sparse + multi-vector in one model.
4. Lee et al. 2024, "Gecko: Versatile Text Embeddings Distilled from Large Language Models," arXiv 2403.20327 `VERIFY`.
   LLM-generated training queries, and relabeling positives/negatives with an LLM.
5. Sentence-transformers documentation, "Loss Overview" and "Training Overview" `VERIFY`. What
   MultipleNegativesRankingLoss and its cached version actually do.

## 4. How retrieval is evaluated

- **The setup:** a corpus, a set of queries, and *qrels* (relevance judgments: which passages count as correct for
  each query).
- **Metrics** (all per query, then averaged):

| Metric | Plain meaning |
|---|---|
| Recall@k | Is a correct passage anywhere in the top k? (k should match how many passages the reader would get) |
| MRR@10 | 1 ÷ rank of the first correct passage; rewards ranking it high |
| nDCG@10 | Like MRR but handles several correct passages and graded relevance; MTEB's headline metric |

- **Validity issues to understand:** test passages leaking into training; *generic queries* that fit many passages;
  *domain shift* (news vs. other text); *ceiling effects* (strong models already score high on Belebele `VERIFY`).
- **Statistics:** scores on a few hundred queries wobble; report confidence intervals and use paired comparisons
  (same queries, two models).

**Read:**
1. Thakur et al. 2021, "BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models,"
   NeurIPS Datasets & Benchmarks `VERIFY`. Why testing beyond the training domain matters; BM25 is a stubborn baseline.
2. Muennighoff et al. 2023, "MTEB: Massive Text Embedding Benchmark," EACL `VERIFY`; then MMTEB (arXiv 2502.13595,
   `VERIFY`) for BelebeleRetrieval.
3. Manning et al. 2008, ch. 8 (evaluation in IR) `VERIFY`.
4. Miller 2024, "Adding Error Bars to Evals," arXiv 2411.00640 `VERIFY`. Confidence intervals and paired tests.

## 5. Prior work closest to this study

| Work | Why it matters | What to look for when reading |
|---|---|---|
| Belebele (Bandarkar et al., ACL 2024) `VERIFY` | Source of formal Cebuano test passages | How passages were translated; what "parallel" gives you |
| MTEB BelebeleRetrieval results `VERIFY` | Published Cebuano baselines to reproduce | Which models top Cebuano; BM25 score |
| CebQA (Lagumbay & Roxas, NiDS 2025; Springer, paywalled) `VERIFY` | Closest Cebuano work; built CebQuAD; BM25 beat DPR | How retrieval was scored; DPR training; dataset construction |
| CebQuAD (Hugging Face) `VERIFY` | Likely training (and in-domain test) data | Split by article; templated questions |
| CebuaNER (PACLIC 2023, arXiv 2310.00679) `VERIFY` | Possible extra Cebuano passages | License; source overlap with CebQuAD |
| Navasardyan et al. 2026, Armenian (arXiv 2603.22290) `VERIFY` | Closest method template | Translated training data; data size vs. gain; human gold pairs |
| Omotoso et al. 2025, Nigerian languages (WiNLP) `VERIFY` | BGE-M3 fine-tuning for low-resource languages | In-domain vs out-of-domain gap |
| CSR-L, Zeng et al. 2026 (Findings ACL, arXiv 2604.17632) `VERIFY` | Code-switched queries hurt retrievers | How they wrote and validated code-switched queries |
| SEA-BED (ACL 2026, arXiv 2508.12243) `VERIFY` | SEA embedding benchmark, no Cebuano | Which models do well on Filipino |
| FilBench (EMNLP 2025, arXiv 2508.03523) `VERIFY` | Philippine-language LLM benchmark | Context: no retrieval category |

## 6. Candidate data and models (re-check each before use)

| Item | What | Possible use | License note |
|---|---|---|---|
| CebQuAD | ~27.6k QA rows from Cebuano news, split by article `VERIFY` | Training; in-domain test | None stated on the card `VERIFY`; record your basis for "usable" |
| Belebele `ceb_Latn` | ~900 questions, ~488 passages, translated from English `VERIFY` | Formal, out-of-domain test | CC BY-SA 4.0 `VERIFY` |
| CebuaNER | ~4.3k news articles `VERIFY` | Optional passages | CC BY-NC 4.0 `VERIFY`; card asks for an email before benchmark use |
| Palito | Literary + religious Cebuano | Optional passages | `VERIFY` |
| HPLT 2.0 `ceb_Latn` | Web crawl | Openly licensed passages (e.g. for a releasable test set) | `VERIFY` |
| WebFAQ `tgl` | Tagalog QA pairs | Optional: Tagalog transfer | `VERIFY` |
| Models: BGE-M3, mE5-base, mE5-large-instruct, Qwen3-Embedding, CebBERT | Baselines / fine-tuning bases | | `VERIFY` each license |

## 7. Open decisions (all **your call**)

1. **Research questions:** how many, and which is the core.
2. **Fine-tuning base(s):** one multilingual model, or also CebBERT (Cebuano-only pretraining) as a comparison.
3. **Training data:** CebQuAD only, or plus translated / generated pairs, or CebuaNER passages.
4. **Test sets:** in-domain (CebQuAD test), formal (Belebele), human-written (colloquial / code-switched);
   if human-written, its size, passage source and who checks it.
5. **Generic questions in CebQuAD:** filter, count multiple passages as relevant, or report both.
6. **Duplicates:** how strict (exact only, or near-duplicate) and what to report.
7. **Headline metric** and which comparisons are the pre-declared claims.
8. **Release:** model and/or test set; licenses of training data and passages decide what is possible.

## 8. Risks to keep in view

- **Novelty is from a first-pass search** (`UNCONFIRMED`); redo it before Dec 7.
- **Ceiling:** strong models may already score high on Belebele and CebQuAD, leaving little room to show gains.
- **Domain/circularity:** a win only on data like the training data is a weak result.
- **Licenses:** record the basis for "usable" for every dataset and model.
- **Time:** one day to the SRC meeting, about three weeks to the defense.

## 9. Suggested reading order (about 8–10 hours, estimate)

| # | Reading | Time | Why at this point |
|---|---|---|---|
| 1 | Karpukhin et al. 2020 (DPR), intro + method + results | 1.5 h | Dense vs BM25, in-batch negatives |
| 2 | Reimers & Gurevych 2019 (Sentence-BERT), intro + figure 1 | 0.5 h | What a bi-encoder is |
| 3 | Thakur et al. 2021 (BEIR), intro + results discussion | 1 h | Out-of-domain testing; BM25 is hard to beat |
| 4 | Navasardyan et al. 2026 (Armenian), whole paper | 1.5 h | Closest template |
| 5 | Omotoso et al. 2025 (Nigerian), whole paper (short) | 0.5 h | In-domain vs out-of-domain lesson |
| 6 | CebQA (if you can get it) + CebQuAD card | 1 h | The Cebuano baseline you build on |
| 7 | CSR-L 2026, benchmark-construction sections | 1 h | How to build code-switched queries |
| 8 | Multilingual E5 report or BGE-M3 paper (your base model's) | 1 h | Know the model you fine-tune |
| 9 | Sentence-transformers loss docs | 0.5 h | Practical training choices |
| 10 | Miller 2024 | 0.5 h | Statistics for your results |

For each reading, write one line: *what they did / what they did not do / what it means for my study*, and log it
in `literature/` (see `context-checklist.md`).
