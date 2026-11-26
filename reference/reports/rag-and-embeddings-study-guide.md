---
title: "Finding the Right Book: A Study Guide to Information Retrieval, Embedding Models and Cebuano Retrieval"
date: 2026-11-26
---

# Finding the Right Book

### A foundational study guide to information retrieval, embedding models, RAG and Cebuano passage retrieval

*For a senior BSCS student with a software engineering background who is new to IR and NLP. Version 2,
2026-11-26.*

---

## How to read this guide

This is a map of a field, not a cheat-sheet for one experiment. The aim is **domain literacy**: knowing why the
field exists, where its ideas came from, what its words mean and how its methods fail. With that, a paper reads
like a conversation you can follow rather than a wall of jargon. The guide doesn't write thesis sections or make
design decisions. It gives you what you need to make them.

**Five sections:**

1. **Why the field exists and where you stand.** The problem, your study's place in it, what is settled vs. open,
   and the pitfalls.
2. **Evolution and diversity of the field.** How the "librarians" evolved, and why there are so many kinds.
3. **Core jargon and working mechanics.** Indexing, representation, contrastive training, evaluation and
   statistics, step by step.
4. **Methodologies, trade-offs and current state.** Baselines, fine-tuning and data strategies, and the
   multilingual and Philippine realities.
5. **Defense-style check and guided reading path.** Hard questions with hints, and what to read in what order.

### Two kinds of label you will see

**Depth labels.** Every topic is marked so you know how hard to study it:

| Label | Meaning |
|---|---|
| **[CORE]** | Know it cold. You should be able to explain it on a whiteboard and defend choices about it. |
| **[ADJACENT]** | Recognize it. Know what it is, why it exists and how it relates to your study. You don't need the internals. |

**Evidence labels.** These follow the rule "never invent facts":

| Tag | Meaning |
|---|---|
| `[VERIFY·L]` | The paper's listing (arXiv, ACL Anthology or publisher page) was checked on 2026-11-26. The full text was **not** read. |
| `[VERIFY]` | A well-known work or fact cited from memory. Very likely right; confirm it before you cite it. |
| `[ESTIMATE]` | A rule of thumb or rough number, not a measured result. |
| `[UNCONFIRMED]` | Searched for but not found, or not traceable to a primary source. |

No source in this guide was read in full for it, so nothing is marked "verified". Any figure quoted from a paper
also carries a tag: check it against the paper's own tables before repeating it.

### The running analogy: the library

| Library | Retrieval / RAG term |
|---|---|
| All the books on the shelves | The **corpus** (knowledge base, document collection) |
| One page or section of a book | A **passage** or **chunk** |
| A patron with a request | The **query** |
| The card catalogue, built before anyone asks | The **index** |
| The librarian who fetches the most promising books | The **retriever** |
| A second librarian who skims the pile and re-orders it | The **reranker** |
| The student who reads the fetched pages and writes the answer | The **reader / generator**, usually a large language model (LLM) |
| Drills of "for this request, *this* book, not *those*" | **Contrastive training** |
| An exam where you know which book is right for each request | An **evaluation set** with **relevance judgments (qrels)** |

**The study, in this picture.** Most librarians in the world learned their trade mostly on English requests. Can
you give one on-the-job training at a Cebuano library so that it fetches the right Cebuano book more often than
the general-purpose librarians? And can you prove it with a fair exam? That is a question about the **librarian
only**, not the student.

> **Where the analogy breaks (general).** A real librarian *understands* requests and can ask a follow-up
> question. A retriever does neither. It computes a score for every passage and sorts. A retriever also can't
> "know" that no book answers the request: it always returns its top-k, even when all of them are useless. Keep
> the analogy for intuition, and drop it whenever you need to reason precisely.

---

# Section 1 — Why the field exists and where you stand

## 1.1 The core problem [CORE]

**Information retrieval (IR)** answers one question at enormous scale: *given a need expressed in words, which
few items out of millions should I look at?* Manning et al. (2008, ch. 1) define IR as finding material of an
unstructured nature (usually text) that satisfies an information need within large collections. Search engines,
e-mail search, legal discovery, library catalogues and product search are all IR.

Three features make it hard:

1. **Vocabulary mismatch.** The patron says "bagyo" and the book says "unos" or "typhoon". Words differ even when
   the meaning is the same. This is the oldest problem in the field and the main reason "embeddings" were
   invented.
2. **Scale.** You can't carefully read a million books for every request. The method must pre-compute something
   (an index) so that answering is fast.
3. **Relevance is fuzzy.** Whether a passage "answers" a query is a human judgment. It can be partial, and two
   judges may disagree. Evaluation has to live with this.

> **Library picture.** A library with a million books and no catalogue is useless, however good its books are.
> IR is the science of building catalogues and training librarians. The more recent RAG systems add a student
> who reads what the librarian fetches.

## 1.2 Why embeddings exist [CORE]

For decades, the "catalogue" was word-based. You matched the words in the request against the words in the books
(Section 2). That fails on vocabulary mismatch. **Embeddings** represent meaning as coordinates on a map, so that
texts that *mean* similar things sit close together even when they share no words. A request and its answer can
then be matched by distance on the map instead of by shared spelling.

In 2018–2020 this became practical and competitive, because pretrained transformer language models could produce
such maps after relatively cheap training (Reimers & Gurevych, 2019; Karpukhin et al., 2020) `[VERIFY]`.

## 1.3 Why RAG made retrieval matter again [CORE]

LLMs answer from what they absorbed in training. Their knowledge has a cutoff, they can't see private documents,
and they **hallucinate** (state falsehoods confidently). **Retrieval-augmented generation (RAG)** turns the
closed-book exam into an open-book one: retrieve relevant passages first, then let the LLM answer from them
(Lewis et al., 2020; Guu et al., 2020) `[VERIFY]`.

The consequence for you: **retrieval quality is a ceiling on RAG quality.** If the librarian brings the wrong book,
even a brilliant student answers wrong, or answers confidently from the wrong source. A thesis about only the
retriever is still a thesis about the part of RAG that decides what the LLM gets to read.

## 1.4 Where a Cebuano fine-tuning study fits

```
                      Information Retrieval
                               │
        ┌──────────────────────┼─────────────────────────┐
     Lexical               Dense / neural              Evaluation science
   (BM25, …)          (embeddings, rerankers)        (test collections, metrics,
        │                      │                       statistics)
        │          ┌───────────┼────────────┐                │
        │     Monolingual   Multilingual   Multimodal         │
        │     English-first  & low-resource  (adjacent)       │
        │                      │                              │
        │            Adaptation to one language ◀─────────────┤
        │            (fine-tuning for Cebuano)                │
        └──────── baseline to beat ──────▶ YOUR STUDY ◀── how you prove it
```

Your study sits where three lines cross:

- **Dense retrieval**: the method you adapt.
- **Multilingual and low-resource NLP**: the reason adaptation might be needed. Cebuano is a thin slice of what
  general models were trained on.
- **Evaluation science**: the way you show that the adaptation helped, and where.

## 1.5 What is well established vs. genuinely open

| Well established (don't present as new) | Plausibly open (claim only "to our knowledge", after a proper literature search) |
|---|---|
| Dense retrievers can beat BM25 when trained on enough in-domain data (Karpukhin et al., 2020) `[VERIFY]` | A multilingual embedder fine-tuned specifically for **Cebuano** retrieval, with results reported on more than one kind of test set `[UNCONFIRMED]` |
| Dense retrievers often fail to generalize out of domain, where BM25 stays robust (Thakur et al., 2021) `[VERIFY]` | A Cebuano retrieval test with **human-written, colloquial** queries `[UNCONFIRMED]` |
| Fine-tuning a multilingual embedder on a small amount of target-language data can give large gains. Shown for Armenian (Navasardyan et al., 2026) and Yorùbá/Igbo/Hausa (Omotoso et al., 2025) `[VERIFY·L]` | How much **code-switched** Cebuano–English (Bisaya–English) queries hurt retrieval, and whether fine-tuning helps `[UNCONFIRMED]` |
| Code-switched queries hurt retrievers, at least for English–Chinese/Japanese (Zeng et al., 2026) `[VERIFY·L]` | Which training data source (QA pairs, translated pairs, LLM-generated queries) works best for Cebuano `[UNCONFIRMED]` |
| Cebuano retrieval scores exist for some models, via the Belebele-based retrieval task in MMTEB (Enevoldsen et al., 2025) `[VERIFY]` | |
| A Cebuano retriever–reader QA system exists (CebQA), in which BM25 reportedly beat DPR (Lagumbay & Roxas, 2025) `[VERIFY]` (from a project page, not the paper) | |

The right column is the outcome of a quick search, not a systematic one. Treat it as a hypothesis about the
literature, and test it yourself before writing "first" anywhere.

## 1.6 Pitfalls to watch for from day one [CORE]

| Pitfall | What it looks like | Why it matters |
|---|---|---|
| **Domain–language confound** | Train on Cebuano *news*, test on Cebuano *news*, score goes up | You can't tell whether the model learned Cebuano or learned news (Section 4.3) |
| **Leakage** | The same article, or a near-duplicate, appears in both train and test | Inflated scores; examiners check this first |
| **Weak baselines** | Comparing only against untuned models, or skipping BM25 | A win over a weak opponent proves little; BM25 is famously hard to beat |
| **Evaluation bugs** | Missing model prefixes, truncation, wrong normalization | Baselines look worse than they really are, and your gain looks bigger |
| **Ceiling effects** | Baselines already score near the maximum on the test set | No room to show an improvement |
| **Circularity** | An LLM writes both the training and the test questions | The model learns the generator's style, not real search |
| **Overclaiming** | "First Cebuano retrieval model", or "significant" without a statistical test | Easy for a panel to puncture |
| **Small test sets** | 100 queries and a 0.02 difference | Within the noise; needs confidence intervals (Section 3.6) |

---

# Section 2 — Evolution and diversity of the field

The field didn't progress in a straight line from bad to good. Each generation of librarian fixed a specific
failure of the last, and most older methods are still in use because each new one brought its own failure. The
history explains why a modern paper still reports BM25.

## 2.1 The timeline, told as library history

| Era | Library picture | What happened | Key works |
|---|---|---|---|
| **1950s–60s: Test collections** [CORE idea] | Before arguing which catalogue is best, agree on a fair exam | The **Cranfield experiments** compared indexing methods on a fixed set of documents, queries and relevance judgments. This "Cranfield paradigm" is still how retrieval is evaluated. | Cleverdon (1967) `[VERIFY]`; Voorhees (2002) `[VERIFY]` |
| **1960s–70s: Vector space & term weighting** [CORE idea] | Catalogue cards weighted by how *distinctive* each word is | Documents and queries as vectors of word weights; similarity by angle (cosine). **IDF**: rare words are more informative. **TF-IDF** combines term frequency with IDF. | Salton et al. (1975) `[VERIFY]`; Spärck Jones (1972) `[VERIFY]` |
| **1970s–90s: Probabilistic models → BM25** [CORE] | A smarter card system: count matches, with diminishing returns and fairness to short books | The probabilistic relevance framework produces **BM25**, the default lexical ranker for decades. It is still the baseline everyone reports. | Robertson & Zaragoza (2009) `[VERIFY]` |
| **1990s: TREC and shared tasks** [ADJACENT] | Annual library competitions with shared exams | TREC scales up Cranfield, with pooled judgments and standard metrics. CLEF and others add **cross-language IR**. | Voorhees (2002) `[VERIFY]`; Manning et al. (2008, ch. 8) `[VERIFY]` |
| **1990: Latent semantic indexing** [ADJACENT] | First attempt at a "map of meaning": compress word–document counts into concepts | Matrix factorization of term–document counts, which partly handles synonyms | Deerwester et al. (1990) `[VERIFY]` |
| **2000s: Learning to rank** [ADJACENT] | Train the librarian on many signals (clicks, links, word matches) | Machine-learned ranking functions over hand-built features power web search | Liu (2009) `[VERIFY]` |
| **2013: Word embeddings** [ADJACENT] | Every *word* gets coordinates on a meaning map | word2vec shows that word meaning can be learned from co-occurrence | Mikolov et al. (2013) `[VERIFY]` |
| **2017–2019: Transformers & BERT** [CORE idea] | A librarian who can actually read a whole sentence in context | The transformer architecture; BERT pretraining; **cross-encoder reranking** gives big jumps on MS MARCO | Vaswani et al. (2017); Devlin et al. (2019); Nogueira & Cho (2019) `[VERIFY]` |
| **2019–2020: Dense retrieval** [CORE] | A map of meaning for every *passage*, pre-computed once | **Sentence-BERT bi-encoders**; **DPR** beats BM25 on open-domain QA; **RAG** and REALM connect retrieval to generation | Reimers & Gurevych (2019); Karpukhin et al. (2020); Lewis et al. (2020); Guu et al. (2020) `[VERIFY]` |
| **2020–2021: Better training, new architectures** | Better drills; librarians who compare word by word; learned keyword cards | Hard-negative mining, denoising, distillation; **late interaction** (ColBERT); **learned sparse** (SPLADE) | Xiong et al. (2021); Qu et al. (2021); Hofstätter et al. (2021); Khattab & Zaharia (2020); Formal et al. (2021) `[VERIFY]` |
| **2021: The generalization reality check** [CORE] | The trained librarian is lost in a different library | **BEIR**: many dense models trained on one dataset do worse than BM25 on others | Thakur et al. (2021) `[VERIFY]` |
| **2021–2023: General-purpose embedders** | Librarians trained on *everything*, ready for any library | Large-scale contrastive pretraining on web pairs (E5, GTE, BGE); unsupervised Contriever; **MTEB** leaderboard | Wang et al. (2022a); Li et al. (2023); Xiao et al. (2024); Izacard et al. (2022); Muennighoff et al. (2023) `[VERIFY]` |
| **2022–2024: Synthetic training data** [CORE for you] | Let a writer invent practice requests for every book | LLMs generate queries for passages: InPars, Promptagator, GPL, multilingual SWIM-IR | Bonifacio et al. (2022); Dai et al. (2022); Wang et al. (2022b) `[VERIFY]`; Thakur et al. (2024) `[VERIFY·L]` |
| **2024–2026: LLM-based & strongly multilingual embedders** | Very large, very well-read librarians | Billion-parameter embedders top leaderboards; strong open multilingual models; **MMTEB** covers 250+ languages | Chen et al. (2024); Wang et al. (2024a; 2024b) `[VERIFY]`; Lee et al. (2024; 2025b); Zhang et al. (2025); Enevoldsen et al. (2025) `[VERIFY·L]` |
| **2023–2026: RAG matures** [ADJACENT] | The student and librarian start working as a team | Surveys, adaptive retrieval, graph RAG, LLM-judged evaluation, document-image retrieval | Gao et al. (2023a); Asai et al. (2024); Edge et al. (2024); Es et al. (2024) `[VERIFY]`; Faysse et al. (2025) `[VERIFY·L]` |

## 2.2 The families of librarian, and why each still exists

| Family | Depth | How it scores | Library picture | Why it still exists | Typical failure |
|---|---|---|---|---|---|
| **Lexical (sparse)**: BM25 | [CORE] | Shared words, weighted by rarity, saturated, length-normalized | Keyword index cards | No training, cheap, robust out of domain, excellent on names, numbers and rare terms | Vocabulary mismatch; word forms (*mipalit* vs *gipalit*) unless the text is stemmed |
| **Dense bi-encoder** | [CORE] | Query and passage encoded *separately*; score = vector similarity | A map of meaning; nearest pins win | Handles paraphrase and cross-lingual matches; passages encoded once in advance | Needs training data; weak on exact strings; degrades outside its training distribution |
| **Cross-encoder (reranker)** | [CORE idea] | Query and passage read *together* | A librarian who skims each shortlisted book | Most accurate per pair | Far too slow for a whole corpus, so it is only used on a shortlist |
| **Learned sparse**: SPLADE | [ADJACENT] | A neural model picks weighted index terms, including related words | Smart extra keywords on every card | Keeps inverted-index speed with some semantic matching | Training cost; less studied in low-resource languages |
| **Late interaction / multi-vector**: ColBERT | [ADJACENT] | One vector per token; matches token by token | Comparing request and book word by word | More precise than one vector per passage; cheaper than a cross-encoder | Much larger index |
| **Hybrid** (lexical + dense) | [ADJACENT, useful] | Merge two ranked lists, e.g. with Reciprocal Rank Fusion: score = Σ 1/(60 + rank) (Cormack et al., 2009) `[VERIFY]` | Ask two librarians and combine their picks | Often beats either alone, because their errors differ | Two systems to maintain |
| **Generative / LLM retrieval** | [ADJACENT] | An LLM generates document IDs, or judges relevance directly | The student goes to the shelves themself | Research frontier | Costly; scale limits |

**The pattern to remember:** in a modern pipeline these usually aren't rivals. They are **stages**. A cheap
retriever (BM25, dense or hybrid) fetches about 100 candidates, an expensive reranker orders them, and an LLM reads
the top few. Your study is about the first stage.

> **Where the analogy breaks.** A "map of meaning" suggests a single, objective geometry of meaning. In reality,
> each model builds its *own* map, shaped by its training data. Two models can disagree about what is "near", and
> distances from different models can't be compared. Also, "meaning" on these maps is whatever the training pairs
> rewarded. A model trained on question–answer pairs puts *questions near their answers*, not near similar
> questions.

## 2.3 The multilingual and low-resource branch [CORE for you]

- **Multilingual pretrained models** (mBERT; XLM-R, Conneau et al., 2020 `[VERIFY]`) share one vocabulary and one
  set of weights across ~100 languages. Data is dominated by a few languages, so low-resource languages get little
  capacity. This is the **curse of multilinguality**: past a point, adding languages to a fixed-size model hurts
  each one (Conneau et al., 2020) `[VERIFY]`. Wu & Dredze (2020) `[VERIFY]` found that mBERT does worse on its
  lowest-resource languages.
- **The resource gap.** Joshi et al. (2020) `[VERIFY]` group the world's languages by available data. Most sit in
  the lowest groups.
- **Multilingual retrieval benchmarks**: TyDi QA → Mr. TyDi → MIRACL (18 languages, human judgments) (Clark et al.,
  2020; Zhang et al., 2021; 2023) `[VERIFY]`. As far as this guide knows, **none includes Cebuano** `[VERIFY]`
  against their language lists.
- **Translated, parallel evaluation**: Belebele (Bandarkar et al., 2024) `[VERIFY]` covers 122 language variants,
  including `ceb_Latn`. Its passages come from FLORES-200, built by the NLLB project (NLLB Team et al., 2022)
  `[VERIFY]`. These are formal, translated texts.
- **Language adaptation methods**: continued pretraining on the target language (Ebrahimi & Kann, 2021; Alabi et
  al., 2022) `[VERIFY]`; language adapters (Pfeiffer et al., 2020) `[VERIFY]`; multilingual distillation (Reimers &
  Gurevych, 2020) `[VERIFY]`; synthetic multilingual training data (Thakur et al., 2024) `[VERIFY·L]`.

## 2.4 The RAG ecosystem around retrieval [ADJACENT]

You only need to recognize these:

| Component | What it does | Key reference |
|---|---|---|
| Chunking strategies | Fixed-size vs. sentence- or paragraph-based splits, with overlap | Gao et al. (2023a) `[VERIFY]` |
| Query rewriting / HyDE | An LLM writes a hypothetical answer, and the system embeds that instead of the query | Gao et al. (2023b) `[VERIFY]` |
| Long-context use | LLMs use the start and end of a prompt better than the middle ("lost in the middle") | Liu et al. (2024) `[VERIFY]` |
| Adaptive / self-reflective RAG | The model decides when to retrieve and critiques what it gets | Asai et al. (2024) `[VERIFY]` |
| Graph RAG | Builds a knowledge graph over the corpus for global questions | Edge et al. (2024) `[VERIFY]` |
| RAG evaluation | LLM-judged faithfulness and context relevance | Es et al. (2024) `[VERIFY]` |
| Multimodal retrieval | Image–text spaces; retrieving page screenshots without OCR | Radford et al. (2021) `[VERIFY]`; Faysse et al. (2025) `[VERIFY·L]` |

---

# Section 3 — Core jargon and working mechanics

## 3.1 Indexing: building the catalogue [CORE]

**Inverted index (lexical).** For every word, a list of the passages that contain it (a *posting list*), like the
index at the back of a textbook (Manning et al., 2008, ch. 1–2) `[VERIFY]`. At query time, only passages sharing a
query word are scored.

**BM25.** For a query with words q₁…qₙ and a passage D:

```
            n                 f(qᵢ, D) · (k₁ + 1)
BM25(D,Q) = Σ  IDF(qᵢ) · ─────────────────────────────────────
           i=1            f(qᵢ, D) + k₁ · (1 − b + b · |D| / avgdl)
```

- **f(qᵢ, D)**: how often the word occurs in the passage, with **diminishing returns** set by **k₁** (commonly
  ~1.2–2.0 `[ESTIMATE]`).
- **IDF**: high for rare words. *Ang* is in nearly every passage and is almost worthless. *Yolanda* is rare and
  informative.
- **|D| / avgdl**: passage length relative to the average. **b** (commonly ~0.75 `[ESTIMATE]`) controls how much
  long passages are penalized.

Source: Robertson & Zaragoza (2009) `[VERIFY]`.

**Language-specific preprocessing matters for BM25.** Lowercasing, tokenization and **stemming** (reducing words to
a root) are designed per language. Cebuano is affix-heavy (*mi-*, *gi-*, *-on*, *-an*, *nag-*). Without a Cebuano
stemmer, *gipalit* and *mipalit* are different words to BM25. That can weaken the baseline, or make your
comparison unfair if you don't report the setting. `[VERIFY]` whether a Cebuano stemmer exists in standard
toolkits such as Pyserini/Lucene.

**Vector index (dense).** A matrix of passage embeddings. **Exact search** compares the query with every passage,
which is fine for tens of thousands of passages `[ESTIMATE]`. **Approximate nearest neighbor (ANN)** search, such as
HNSW graphs or FAISS's IVF/PQ (Malkov & Yashunin, 2020; Johnson et al., 2021) `[VERIFY]`, trades a little recall
for large speed-ups on millions of passages. **[ADJACENT]** for a thesis-sized corpus, but know that the term means
"fast, slightly lossy search".

## 3.2 Representation: from text to vector [CORE]

```
"Asa man ang VSU?"
   │ 1 Tokenize      → ["▁Asa", "▁man", "▁ang", "▁V", "SU", "?"]    (illustrative split)
   │ 2 Embed tokens  → one starting vector per token
   │ 3 Transformer   → each token vector updated by attending to all others (context)
   │ 4 Pool          → one vector: mean of tokens, or [CLS], or last token
   ▼ 5 Normalize     → e ∈ ℝ^d, ‖e‖ = 1     (d is often 384–1024)
```

| Term | Meaning | Why it matters for you |
|---|---|---|
| **Token / tokenizer** | Sub-word pieces from a fixed vocabulary (WordPiece, SentencePiece) | A language that is poorly covered gets chopped into many meaningless pieces. Measure tokens per word for Cebuano in each candidate model. |
| **Self-attention** | Each token's vector mixes in information from the others | How the model disambiguates words by context |
| **Pooling** | Combining token vectors into one | Fixed per model; follow the model card |
| **Embedding dimension (d)** | Length of the vector | Affects storage; Matryoshka training allows truncation (Kusupati et al., 2022) `[VERIFY]` |
| **Cosine similarity / dot product** | Closeness of two vectors; equal once vectors are normalized | The scoring function of dense retrieval |
| **Max sequence length** | Tokens beyond it are cut off | Silent truncation of long passages |
| **Prefixes / instructions** | E.g. `query: ` and `passage: ` for E5 (Wang et al., 2022a) `[VERIFY]` | Forgetting them lowers baseline scores, a classic evaluation bug |
| **Bi-encoder vs. cross-encoder** | Separate encoding vs. joint reading | Speed vs. accuracy |

**Why raw BERT isn't a search engine.** A pretrained language model learned to fill in masked words, not to put
questions near their answers. Reimers & Gurevych (2019) `[VERIFY]` showed that naive BERT sentence vectors did
poorly on similarity. **Contrastive training** is what turns a reader into a fetcher.

> **Where the analogy breaks.** The analogy treats "learning to read" (pretraining) and "learning to fetch"
> (contrastive training) as separate skills. In a model they share the same weights. Training hard on fetching can
> erode some reading ability in other languages or domains (**catastrophic forgetting**), which a human librarian
> wouldn't suffer from a two-week course.

## 3.3 Contrastive training [CORE]

**The idea.** Nobody knows the "correct" coordinates for a passage, but you can say *relatively* that this query
belongs nearer this passage than those. So you train on comparisons.

| Term | Meaning | Library picture |
|---|---|---|
| **Anchor** | The query | The request slip |
| **Positive** | A passage that answers it | The right book |
| **Negative** | A passage that doesn't | A wrong book |
| **Hard negative** | A wrong passage that looks right: same topic, shared words | A book from the right shelf that still doesn't answer |
| **False negative** | A passage labelled wrong that actually is right | The answer key is wrong. The drill teaches a mistake |
| **In-batch negatives** | Other queries' positives in the same batch, used as negatives | Free wrong books from the other students' requests |

**The loss (InfoNCE / MultipleNegativesRankingLoss).** For query q, positive p⁺, negatives p₁…pₙ and cosine
similarity s:

```
                         exp( s(q, p⁺) / τ )
  loss = − log ───────────────────────────────────────────
                exp( s(q, p⁺) / τ ) + Σⱼ exp( s(q, pⱼ) / τ )
```

Read it as a multiple-choice question: the loss is small when the model gives the right passage most of the
probability. **τ (temperature)** sets how sharply the scores are separated. Sentence-transformers' default "scale"
of 20 corresponds to τ = 0.05 `[VERIFY]` in the current docs. Sources: van den Oord et al. (2018); Henderson et al.
(2017) `[VERIFY]`.

**In-batch negatives, concretely.** With a batch of B pairs, the similarity matrix is B × B. The diagonal holds the
positives and everything else is a negative. That is B − 1 negatives per query for free (Karpukhin et al., 2020)
`[VERIFY]`.

```
          p₁   p₂   p₃   p₄
    q₁  [ ✔    ✘    ✘    ✘ ]
    q₂  [ ✘    ✔    ✘    ✘ ]
    q₃  [ ✘    ✘    ✔    ✘ ]     ← but if q₃ and q₄ came from the SAME article,
    q₄  [ ✘    ✘    ✘?   ✔ ]       p₃ may answer q₄ too: an in-batch false negative
```

Consequences:

- **Bigger batches mean more negatives**, and usually better models. Memory limits batch size, so **GradCache**
  (Gao et al., 2021b) `[VERIFY]` recomputes the same loss in chunks. In sentence-transformers it is
  `CachedMultipleNegativesRankingLoss`.
- **Datasets with many questions per article** produce in-batch false negatives. Sampling one question per article
  per batch is a common mitigation `[ESTIMATE]`.

**Hard-negative mining.** Retrieve the top passages for each query with BM25 or the current model, remove the
positive, and train against the rest. DPR used BM25 negatives (Karpukhin et al., 2020). ANCE refreshed negatives
during training (Xiong et al., 2021). RocketQA showed that many mined "negatives" are actually false negatives and
filtered them with a cross-encoder (Qu et al., 2021) `[VERIFY]`. The trade-off: harder negatives teach more, *and*
carry a higher risk of being secretly correct.

**Other losses to recognize [ADJACENT]:** triplet loss with a margin; CosineSimilarity / CoSENT for graded
similarity (STS); MarginMSE for distilling a cross-encoder teacher (Hofstätter et al., 2021) `[VERIFY]`;
MatryoshkaLoss as a wrapper (Kusupati et al., 2022) `[VERIFY]`.

## 3.4 How today's embedders are built [CORE]

```
Stage 0  Language-model pretraining     masked-word filling on raw text        → learns to read
Stage 1  Weakly-supervised contrastive  huge naturally paired web data          → rough "what goes with what"
         pretraining                     (title↔body, Q↔A, post↔reply)
Stage 2  Supervised fine-tuning          curated labelled pairs + hard negatives → precise fetching
Stage 3  Target adaptation               your language / domain pairs            → on-the-job training
```

Stages 1–2 are the E5/GTE recipe (Wang et al., 2022a; Li et al., 2023) `[VERIFY]`. Multilingual E5 applies it
across ~100 languages (Wang et al., 2024a) `[VERIFY]`. **A fine-tuning study starts after stage 2 and only adds
stage 3.** That is why it is feasible on modest compute.

## 3.5 Retrieval evaluation [CORE]

**The Cranfield setup.** A fixed **corpus**, fixed **queries**, and **qrels** (which passages are relevant to each
query, optionally graded 0/1/2). Every system produces a **run** (a ranked list per query), and metrics compare the
run with the qrels (Voorhees, 2002; Manning et al., 2008, ch. 8) `[VERIFY]`.

**Worked example.** Two queries, one relevant passage each:

```
Query A:  rank 1 ✘   rank 2 ✘   rank 3 ✔   rank 4 ✘   rank 5 ✘
Query B:  rank 1 ✔   rank 2 ✘   rank 3 ✘   rank 4 ✘   rank 5 ✘
```

| Metric | Measures | A | B | Mean |
|---|---|---|---|---|
| **Recall@k** (= hit rate / top-k accuracy when there is one relevant passage) | Is the relevant passage in the top k? | @1 = 0, @3 = 1 | @1 = 1, @3 = 1 | @1 = 0.5, @3 = 1.0 |
| **Precision@k** | Share of the top k that is relevant | @3 = 0.33 | @3 = 0.33 | 0.33 |
| **Reciprocal rank → MRR** | 1 / rank of the first relevant passage | 0.333 | 1.0 | **0.667** |
| **nDCG@k** | Rank-discounted gain, normalized so perfect = 1; supports graded relevance and multiple relevant passages | 0.5 | 1.0 | **0.75** |

nDCG for query A: DCG = 1 / log₂(3 + 1) = 0.5, and IDCG = 1 / log₂(2) = 1, so nDCG = 0.5 (Järvelin & Kekäläinen,
2002) `[VERIFY]`.

**What each metric means for a user:**

- **Recall@k**, with k equal to the number of passages a RAG system feeds the LLM: did the student get the right
  page at all?
- **MRR@10**: how high was the *first* right page? This is the MS MARCO convention (Nguyen et al., 2016)
  `[VERIFY]`.
- **nDCG@10**: overall ranking quality with graded relevance. This is MTEB's headline retrieval metric (Muennighoff
  et al., 2023) `[VERIFY]`.
- **MAP** [ADJACENT]: mean average precision, common in classic TREC work.

**Evaluation workflow (what actually runs).** Freeze the corpus, queries and qrels. For each system, index the
corpus and retrieve the top 100 per query. Score with a standard tool (pytrec_eval, ranx or the MTEB evaluator)
`[VERIFY]`. **Keep per-query scores**, because statistics and error analysis need them. Then read the failures.

**First sanity check:** reproduce one *published* number, such as a public model's MTEB score on a task, before you
trust your own pipeline.

## 3.6 Statistical rigor [CORE]

A test set is a **sample** of all the questions people could ask. Another sample would give slightly different
scores (Miller, 2024) `[VERIFY·L]`.

- **Confidence interval (CI).** A range likely to contain the score you would get on the whole population of
  questions, for example nDCG@10 = 0.71 [0.67, 0.75].
- **Paired comparison.** Both systems answer the *same* queries. Compute the per-query difference
  (score_B − score_A), then a CI for its mean. This is far more sensitive than comparing two separate averages,
  because it cancels out how hard each query is. **If the CI of the difference includes 0, don't claim a
  difference.**
- **Paired bootstrap** (Efron & Tibshirani, 1993) `[VERIFY]`. Resample the queries with replacement about 10,000
  times `[ESTIMATE]`, recompute the mean difference each time, and take the 2.5th and 97.5th percentiles.
- **Alternatives.** The paired t-test, and the randomization (permutation) test, which Smucker et al. (2007)
  `[VERIFY]` favored in a comparison of IR significance tests. Miller (2024) `[VERIFY·L]` argues that simple
  Central-Limit-Theorem standard errors usually suffice, recommends **clustered** standard errors when queries come
  in related groups (e.g. many questions from one article), and gives **power analysis** formulas to size a test
  set *before* building it.
- **Multiple comparisons** [ADJACENT]. Comparing many systems on many test sets raises the chance that one "win" is
  luck. Decide in advance which comparisons are your main claims.

> **Where the analogy breaks.** An exam answer key implies one right answer per question. Real qrels are often
> **incomplete**: annotators couldn't judge every passage, so a correct passage that nobody judged counts as
> wrong. A better model can be punished for finding answers the key missed. Spot-check top-ranked "misses" by hand.

## 3.7 The data, briefly [CORE for the shapes, not the formats]

The standard retrieval test layout comes from BEIR (Thakur et al., 2021) `[VERIFY]`: a `corpus.jsonl` (id, title,
text), a `queries.jsonl` (id, text) and a `qrels` TSV (query-id, corpus-id, score). Training data for
sentence-transformers is just columns: anchor, positive and optionally negative. What matters conceptually:

```
corpus   p1 "Ang Visayas State University (VSU) usa ka pampublikong unibersidad nga nahimutang sa Baybay City, Leyte."
         p2 "Ang bagyong Yolanda (Haiyan) miigo sa Sidlakang Visayas niadtong Nobyembre 2013 ..."
         p4 "Ang Baybay usa ka siyudad sa kasadpang baybayon sa Leyte, nailhan sa pantalan ug sa unibersidad."
queries  q1 "Asa nahimutang ang VSU?"            (formal)
         q2 "unsa year naigo si Yolanda sa Leyte?" (code-switched)
qrels    q1→p1 = 2 (fully relevant)   q1→p4 = 1 (partially relevant)   q2→p2 = 2
```

*The Cebuano here was written by a non-native writer as an illustration. A native speaker should correct it.*

Notice three things:

- **graded relevance** (q1→p4 = 1), which nDCG can use and Recall@k can't;
- **code-switching** in q2;
- **p4 as a natural hard negative for q1**, or arguably a partial positive. Deciding cases like this is part of
  building clean data.

---

# Section 4 — Methodologies, trade-offs and current state

## 4.1 Baselines: who your librarian must beat [CORE]

| Baseline type | Why include it | Watch out for |
|---|---|---|
| **BM25** | The standard lexical reference; robust; reported by nearly every retrieval paper | Preprocessing (tokenizer, stemming, stopwords) and k₁/b settings; report them |
| **Off-the-shelf multilingual embedders** (e.g. mE5, BGE-M3, Qwen3-Embedding, LaBSE) | Shows what a general-purpose librarian already achieves | Prefixes, max length, pooling, license; pick models of comparable size to your base model *and* at least one strong model |
| **The un-tuned base model** | The direct "before" for your "after" | Same evaluation code and settings as the tuned model |
| **Hybrid** (BM25 + dense) [optional] | Shows whether fine-tuning closes a gap that a cheap fusion already closes | More systems to report |
| **Published numbers** (e.g. MMTEB Belebele Cebuano) [sanity check] | Confirms your evaluation pipeline reproduces known results | Different versions and settings |

## 4.2 Kinds of fine-tuning, on three axes [CORE]

| Axis | Options | Notes |
|---|---|---|
| **What you train on** | **Continued pretraining** (masked-word task on raw target-language text) vs. **task fine-tuning** (contrastive, on query–passage pairs) vs. **distillation** (copy a teacher's scores or embeddings) | Continued pretraining needs only raw text (Gururangan et al., 2020; Ebrahimi & Kann, 2021; Alabi et al., 2022) `[VERIFY]` |
| **How much you change** | **Full** fine-tuning vs. **layer freezing** vs. **adapters** (Houlsby et al., 2019; Pfeiffer et al., 2020) vs. **LoRA** (Hu et al., 2022) `[VERIFY]` | For ~300M–600M-parameter encoders, full fine-tuning on one cloud GPU is typical. LoRA matters for billion-parameter embedders `[ESTIMATE]` |
| **What you adapt to** | **Domain** (new topic or style, same language) vs. **language** (new grammar, morphology, tokens) | Same tools, different problems (next subsection) |

**Instruction tuning and preference tuning (RLHF, DPO)** are [ADJACENT]. They are for generators, not retrievers.

## 4.3 Domain adaptation vs. language adaptation [CORE]

| | Domain adaptation | Language adaptation |
|---|---|---|
| What is new | Topic vocabulary and style in a known language | Grammar, morphology, spelling, tokenizer coverage, cross-lingual alignment |
| Typical failure before | Doesn't know domain terms or abbreviations | Fragmented tokens; affixed forms treated as unrelated; weak alignment with other languages |
| Extra tools | Domain synthetic queries (GPL; Wang et al., 2022b) `[VERIFY]` | **Translate-train** (Navasardyan et al., 2026) `[VERIFY·L]`; **cross-lingual transfer** from a related language such as Tagalog; **vocabulary extension**; **multilingual distillation** (Reimers & Gurevych, 2020) `[VERIFY]` |

**The confound.** Real Cebuano datasets are usually *also* one domain, often news. Training and testing on the same
source mixes language gains with domain gains (and dataset-style gains). Omotoso et al. (2025) `[VERIFY·L]` report
large MRR gains on their own in-domain test but only a small gain on MIRACL Yorùbá (e.g. 0.5952 → 0.5996). The
standard remedy is **more than one test set**: in-domain, out-of-domain in the same language, and
realistic-query tests.

> **Where the analogy breaks.** "Retraining the librarian for a Cebuano library" suggests that the library is the
> language. In practice the library is *a particular collection*, such as news from certain outlets in certain
> years. The librarian may learn that collection's habits rather than Cebuano itself.

## 4.4 Training-data strategies and their trade-offs [CORE]

| Strategy | Source of pairs | Pros | Cons / failure modes | Examples |
|---|---|---|---|---|
| **Existing human/QA data** | A QA dataset's questions + source passages | Real target-language text; relevance mostly reliable | Usually one domain; templated or LLM-assisted questions may be unnatural; many questions per passage cause in-batch false negatives | DPR on NQ (Karpukhin et al., 2020) `[VERIFY]`; CebQuAD (Lagumbay & Roxas, 2025) `[VERIFY]` |
| **LLM-generated queries** | An LLM writes questions for passages | Scales to any passage collection; adjustable style | **Circularity**; LLM fluency in Cebuano is uncertain (see FilBench); needs filtering | InPars, Promptagator, GPL `[VERIFY]`; SWIM-IR, Gecko `[VERIFY·L]` |
| **Translated English pairs** | Machine-translate an English dataset | Large, diverse, cheap | Translation noise; "translationese" doesn't match real queries | Navasardyan et al. (2026): ~10k noisy pairs were enough, and more didn't help `[VERIFY·L]` |
| **Unsupervised** | Crops or dropout views of raw text | Needs only raw text | Usually weaker than supervised | Contriever; SimCSE `[VERIFY]` |
| **Distillation** | A teacher's scores or embeddings | Transfers strong-model knowledge | Needs a good teacher in or near the language | Reimers & Gurevych (2020); TAS-B `[VERIFY]` |
| **Mixed sources** | Any combination | Diversity | Must be **ablated** (remove one source at a time) to know what helped | — |

**Practical trade-offs:**

| Dimension | Cheaper / safer | More ambitious / riskier |
|---|---|---|
| Base model size | ~300M–600M encoder | Billion-parameter LLM embedder (needs LoRA, more compute) |
| Data | One clean source, well split | Many sources (needs ablations) |
| Negatives | In-batch only | Mined hard negatives (needs false-negative filtering) |
| Test sets | One in-domain test | In-domain + out-of-domain + human-written (more convincing, more work) |
| Hyperparameters | Library defaults; LR ~1e-5–3e-5, 1–3 epochs `[ESTIMATE]` | Searched on a validation split (more compute, more rigor) |

## 4.5 Current state: multilingual embedders [CORE awareness]

- **Leaderboards.** MTEB (Muennighoff et al., 2023) `[VERIFY]` and its multilingual expansion MMTEB, with 500+
  tasks across 250+ languages (Enevoldsen et al., 2025) `[VERIFY·L]`. MMTEB's authors reported that the best
  *publicly available* model was multilingual-e5-large-instruct, at ~560M parameters `[VERIFY·L]` (from the
  abstract). Leaderboards change monthly, so quote a date when you cite one.
- **LLM-based embedders** (E5-Mistral, NV-Embed, Gecko, Qwen3-Embedding, Gemini Embedding) top many leaderboards
  but are expensive to fine-tune and serve. Qwen3-Embedding ships at 0.6B, 4B and 8B under Apache 2.0 `[VERIFY·L]`.
  Gemini Embedding is API-only `[VERIFY]`.
- **Regional rankings differ.** SEA-BED, a Southeast Asian embedding benchmark (169 datasets, 10 languages
  including Filipino, mostly human-made), reports model rankings that differ sharply from MMTEB (Ponwitayarat et
  al., 2026) `[VERIFY·L]`. A model's global rank is weak evidence about its Cebuano performance.

## 4.6 Current state: Philippine and Cebuano NLP [CORE context]

| Resource / finding | What it is | Status |
|---|---|---|
| **Speaker base** | Cebuano is among the most widely spoken Philippine languages, roughly 20M+ speakers | `[VERIFY]` (use a census or Ethnologue citation) |
| **Cebuano Wikipedia** | Very large but overwhelmingly bot-generated (Lsjbot); ~99% of articles reported bot-created. Alshahrani et al. (2023) show models trained on bot-generated wiki text underperform (studied for Arabic) | `[VERIFY]` (Cebuano figure from secondary sources) |
| **CebQA / CebQuAD** | Retriever–reader Cebuano QA and a Cebuano QA dataset from news; BM25 reportedly beat DPR (Lagumbay & Roxas, 2025) | `[VERIFY]` (paper not read) |
| **CebuaNER** | 4,000+ annotated Cebuano news articles for NER (Pilar et al., 2023) | `[VERIFY·L]` |
| **Belebele `ceb_Latn`** | Translated, formal reading-comprehension passages and questions (Bandarkar et al., 2024) | `[VERIFY]` |
| **SEACrowd** | A hub of ~500 SEA datasets with standard loaders (Lovenia et al., 2024); a place to discover Cebuano data | `[VERIFY·L]` |
| **FilBench** | An LLM benchmark covering Filipino, Tagalog and Cebuano; the best model scored ~72% (Miranda et al., 2025). LLMs are still imperfect in Philippine languages, which matters if you plan LLM-generated Cebuano data | `[VERIFY·L]` |
| **Code-switching** | Bisaya–English mixing is common in everyday Cebuano; the CSR-L paper shows code-switched queries degrade retrievers, but for English–Chinese/Japanese only (Zeng et al., 2026) | `[VERIFY·L]` for CSR-L; `[UNCONFIRMED]` for any Cebuano-specific measurement |
| **Model pretraining coverage** | Whether Cebuano is in XLM-R's CC-100 pretraining languages, and how much Cebuano a given embedder saw | `[VERIFY]` (check each model's report) |

**What this means in practice:** data is scarce, mostly news and formal text, partly machine-generated. Realistic
user queries in Cebuano are essentially undocumented in retrieval benchmarks `[UNCONFIRMED]`. That scarcity is both
the motivation for a study like yours and its biggest methodological risk.

---

# Section 5 — Defense-style check and guided reading path

## 5.1 Defense-style questions (with brief answers and hints)

Try answering each one aloud before reading the hint.

**Foundations**

1. **"Why not just use BM25?"**
   *Hint:* vocabulary mismatch, paraphrase and cross-lingual matches. Then concede BM25's robustness (BEIR; CebQA)
   and explain how your design measures it fairly, including preprocessing.
2. **"If RAG is the application, why evaluate only retrieval?"**
   *Hint:* retrieval caps RAG quality; isolating it avoids confounding with the generator; end-to-end metrics
   (faithfulness, answer F1) are scoped out and named as future work.
3. **"What's the difference between a bi-encoder and a cross-encoder, and why does your study use the former?"**
   *Hint:* separate vs. joint encoding; pre-computable index; speed. Rerankers sit downstream.

**Training**

4. **"What exactly does fine-tuning change in the model?"**
   *Hint:* all (or some) weights are nudged by the contrastive loss so that Cebuano queries land near their
   passages. Mention catastrophic forgetting.
5. **"Where do your negatives come from, and how do you know they're really negative?"**
   *Hint:* in-batch and/or mined; the false-negative risk (RocketQA); your mitigation (filtering, one question per
   article per batch, spot checks).
6. **"Why this base model?"**
   *Hint:* multilingual coverage, size vs. compute, license, published baselines, tokenizer behavior on Cebuano
   (measured, not assumed).
7. **"Isn't using LLM-generated or translated data circular or unnatural?"**
   *Hint:* name the circularity risk; keep test queries from a different source than training queries; cite the
   Armenian result on noisy data.

**Evaluation**

8. **"Your model improved on the in-domain test. How do you know it learned Cebuano and not just your dataset?"**
   *Hint:* the domain–language confound; an out-of-domain Cebuano test; the Nigerian MIRACL example.
9. **"How do you know there's no leakage?"**
   *Hint:* split by article or source; exact and near-duplicate checks across the split; report the check.
10. **"Why nDCG@10 (or MRR@10, or Recall@k) as the headline?"**
    *Hint:* match the metric to the use. Recall@k for "is it in what the LLM reads"; MRR or nDCG for ranking.
    Say which is primary *before* seeing results.
11. **"Is a 0.03 improvement meaningful?"**
    *Hint:* paired CI on the per-query difference; if it includes 0, no claim; power analysis for the test-set
    size.
12. **"Your qrels list one relevant passage per question. Isn't that unfair?"**
    *Hint:* incomplete qrels; generic questions; manual spot checks of top "misses"; graded or multiple relevance
    where possible.

**Scope and contribution**

13. **"Fine-tuning helps low-resource languages. Hasn't that already been shown?"**
    *Hint:* yes, for Armenian and Nigerian languages. Your contribution is the *Cebuano evidence* and *where* it
    helps (domain, register, code-switching), plus any reusable test set. Say "to our knowledge".
14. **"Why should anyone care about Cebuano retrieval specifically?"**
    *Hint:* speaker population `[VERIFY]`; scarce natural data despite the huge bot-written Wikipedia; RAG and
    search for Cebuano users; Bisaya–English reality.
15. **"What would make you conclude fine-tuning *didn't* work, and is that publishable?"**
    *Hint:* define the failure criteria up front. A well-measured negative result (e.g. BM25 still wins out of
    domain) is a valid finding.

## 5.2 Guided reading path

Times are `[ESTIMATE]`s for focused reading of the named parts only. For each paper, write one line: *what they
did / what they didn't do / what it means for my study.*

### A. Foundations: what the field is (about 5 h)

| # | Reading | Parts | Why |
|---|---|---|---|
| A1 | Manning et al. (2008), *Introduction to Information Retrieval* (free online) | Ch. 1, 6 (skim), 8 | Inverted index, term weighting, evaluation basics |
| A2 | Robertson & Zaragoza (2009) | BM25 sections | Defend your lexical baseline |
| A3 | Reimers & Gurevych (2019), Sentence-BERT | Intro + Figure 1 | What a bi-encoder is |
| A4 | Karpukhin et al. (2020), DPR | Intro, method, results | Dense vs. BM25; in-batch negatives |
| A5 | Lewis et al. (2020), RAG | Intro + Figure 1 | Why retrieval feeds generation |
| A6 | Thakur et al. (2021), BEIR | Intro + results discussion | The generalization reality check |

### B. Training and evaluation: how the work is done (about 6 h)

| # | Reading | Parts | Why |
|---|---|---|---|
| B1 | Wang et al. (2022a), E5 | Sections 3–4 | The modern embedder recipe |
| B2 | Wang et al. (2024a), Multilingual E5, *or* Chen et al. (2024), BGE-M3 (whichever is your base) | Whole report | Know the model you adapt |
| B3 | Qu et al. (2021), RocketQA | False-negative section | Negative-mining pitfalls |
| B4 | Sentence-transformers docs: Training Overview, Loss Overview | — | Practical training choices |
| B5 | Muennighoff et al. (2023), MTEB; Enevoldsen et al. (2025), MMTEB | Intro, task design | How embedders are compared; where Cebuano numbers live |
| B6 | Järvelin & Kekäläinen (2002) | nDCG definition | The headline metric |
| B7 | Miller (2024); Smucker et al. (2007) | Recommendations; conclusions | Confidence intervals, paired tests, power |

### C. Low-resource and regional context: where your study sits (about 6 h)

| # | Reading | Parts | Why |
|---|---|---|---|
| C1 | Joshi et al. (2020); Wu & Dredze (2020) | Intros + key figures | Why low-resource languages lag |
| C2 | Navasardyan et al. (2026), Armenian | Whole paper | Closest method template |
| C3 | Omotoso et al. (2025), Nigerian languages | Whole paper | The in-domain vs. out-of-domain lesson |
| C4 | Lagumbay & Roxas (2025), CebQA (if accessible) + CebQuAD card | Method + retrieval results | The Cebuano baseline |
| C5 | Zeng et al. (2026), CSR-L | Benchmark construction | How to build code-switched queries |
| C6 | Thakur et al. (2024), SWIM-IR | Method | Synthetic multilingual data |
| C7 | Ponwitayarat et al. (2026), SEA-BED; Miranda et al. (2025), FilBench | Intro + findings | Regional evaluation landscape |
| C8 | Bandarkar et al. (2024), Belebele | Construction section | What a formal, translated Cebuano test does and doesn't measure |

### D. Adjacent: read only if a question pulls you there

Khattab & Zaharia (2020), ColBERT · Formal et al. (2021), SPLADE · Gao et al. (2023a), RAG survey · Liu et al.
(2024), lost in the middle · Gururangan et al. (2020), domain-adaptive pretraining · Hu et al. (2022), LoRA ·
Faysse et al. (2025), ColPali.

---

# Glossary

| Term | Plain meaning |
|---|---|
| **Ablation** | Removing one ingredient to measure its effect |
| **Anchor / positive / negative** | Query / correct passage / wrong passage in contrastive training |
| **ANN (approximate nearest neighbor)** | Fast, slightly lossy vector search (HNSW, IVF/PQ) |
| **Bi-encoder** | Encodes query and passage separately into vectors |
| **BM25** | Lexical ranking function with IDF, term-frequency saturation and length normalization |
| **Catastrophic forgetting** | Losing old abilities after fine-tuning on new data |
| **Chunk / passage** | A piece of a document small enough to embed and retrieve |
| **Code-switching** | Mixing languages in one utterance (e.g. Bisaya–English) |
| **Confidence interval (CI)** | A range likely to contain the true value of a score |
| **Contrastive learning** | Pull matching pairs together, push non-matching pairs apart |
| **Corpus** | The full collection being searched |
| **Cosine similarity** | Vector similarity by angle; equals the dot product for normalized vectors |
| **Cranfield paradigm** | Evaluation with fixed documents, queries and relevance judgments |
| **Cross-encoder / reranker** | Reads query and passage together and outputs a relevance score |
| **Curse of multilinguality** | Per-language quality dropping as more languages share a fixed-size model |
| **Dense retrieval** | Retrieval with embedding vectors |
| **Domain shift** | Test data differs in topic or style from training data |
| **Embedding** | A vector representing meaning |
| **False negative** | Labelled irrelevant but actually relevant |
| **Hard negative** | A wrong passage that looks right |
| **IDF** | Inverse document frequency: the rarer a word, the more weight it gets |
| **In-batch negatives** | Other pairs' positives in the batch used as negatives |
| **InfoNCE / MNRL** | The standard contrastive loss (MultipleNegativesRankingLoss) |
| **Inverted index** | Word → list of passages containing it |
| **Leakage** | Test information seen during training |
| **LoRA / adapters** | Parameter-efficient fine-tuning via small added weights |
| **MRR** | Mean reciprocal rank of the first relevant result |
| **nDCG** | Normalized discounted cumulative gain: a rank-aware, graded-relevance metric |
| **Paired test** | Comparing two systems query by query on the same queries |
| **Pooling** | Combining token vectors into one text vector |
| **Qrels** | Relevance judgments: the answer key |
| **RAG** | Retrieval-augmented generation |
| **Recall@k** | Share of the relevant passages found in the top k |
| **Run** | A system's ranked results for all queries |
| **Stemming** | Reducing words to a root so that inflected forms match |
| **Temperature (τ)** | Loss parameter controlling how sharply scores are separated |
| **Token / tokenizer** | Sub-word unit / the tool that splits text into them |
| **Zero-shot** | Evaluated on data or tasks not seen in training |

---

# References

*APA 7. Tags: `[VERIFY·L]` = listing checked 2026-11-26, full text not read; `[VERIFY]` = from memory, confirm
before citing. No entry has been read in full for this guide.*

- Alabi, J. O., Adelani, D. I., Mosbach, M., & Klakow, D. (2022). Adapting pre-trained language models to African languages via multilingual adaptive fine-tuning. *COLING 2022*. https://arxiv.org/abs/2204.06487 `[VERIFY]`
- Alshahrani, S., Alshahrani, N., Dey, S., & Matthews, J. (2023). Performance implications of using unrepresentative corpora in Arabic natural language processing. *ArabicNLP 2023*. https://aclanthology.org/2023.arabicnlp-1.19 `[VERIFY·L]`
- Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. (2024). Self-RAG: Learning to retrieve, generate, and critique through self-reflection. *ICLR 2024*. https://arxiv.org/abs/2310.11511 `[VERIFY]`
- Bandarkar, L., et al. (2024). The Belebele benchmark: A parallel reading comprehension dataset in 122 language variants. *ACL 2024*. https://arxiv.org/abs/2308.16884 `[VERIFY]`
- Bonifacio, L., Abonizio, H., Fadaee, M., & Nogueira, R. (2022). InPars: Data augmentation for information retrieval using large language models. https://arxiv.org/abs/2202.05144 `[VERIFY]`
- Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D., & Liu, Z. (2024). BGE M3-Embedding: Multi-lingual, multi-functionality, multi-granularity text embeddings through self-knowledge distillation. *Findings of ACL 2024*. https://arxiv.org/abs/2402.03216 `[VERIFY]`
- Clark, J. H., et al. (2020). TyDi QA: A benchmark for information-seeking question answering in typologically diverse languages. *TACL, 8*. https://arxiv.org/abs/2003.05002 `[VERIFY]`
- Cleverdon, C. W. (1967). The Cranfield tests on index language devices. *Aslib Proceedings, 19*(6), 173–194. `[VERIFY]`
- Conneau, A., et al. (2020). Unsupervised cross-lingual representation learning at scale. *ACL 2020*. https://arxiv.org/abs/1911.02116 `[VERIFY]`
- Cormack, G. V., Clarke, C. L. A., & Büttcher, S. (2009). Reciprocal rank fusion outperforms Condorcet and individual rank learning methods. *SIGIR 2009*. https://doi.org/10.1145/1571941.1572114 `[VERIFY]`
- Dai, Z., et al. (2022). Promptagator: Few-shot dense retrieval from 8 examples. https://arxiv.org/abs/2209.11755 `[VERIFY]`
- Deerwester, S., Dumais, S. T., Furnas, G. W., Landauer, T. K., & Harshman, R. (1990). Indexing by latent semantic analysis. *Journal of the American Society for Information Science, 41*(6), 391–407. `[VERIFY]`
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *NAACL 2019*. https://arxiv.org/abs/1810.04805 `[VERIFY]`
- Ebrahimi, A., & Kann, K. (2021). How to adapt your pretrained multilingual model to 1600 languages. *ACL 2021*. https://arxiv.org/abs/2106.02124 `[VERIFY]`
- Edge, D., et al. (2024). From local to global: A graph RAG approach to query-focused summarization. https://arxiv.org/abs/2404.16130 `[VERIFY]`
- Efron, B., & Tibshirani, R. J. (1993). *An introduction to the bootstrap*. Chapman & Hall. `[VERIFY]`
- Enevoldsen, K., et al. (2025). MMTEB: Massive Multilingual Text Embedding Benchmark. *ICLR 2025*. https://arxiv.org/abs/2502.13595 `[VERIFY·L]`
- Es, S., James, J., Espinosa-Anke, L., & Schockaert, S. (2024). RAGAS: Automated evaluation of retrieval augmented generation. *EACL 2024 Demos*. https://arxiv.org/abs/2309.15217 `[VERIFY]`
- Faysse, M., et al. (2025). ColPali: Efficient document retrieval with vision language models. *ICLR 2025*. https://arxiv.org/abs/2407.01449 `[VERIFY·L]`
- Feng, F., Yang, Y., Cer, D., Arivazhagan, N., & Wang, W. (2022). Language-agnostic BERT sentence embedding. *ACL 2022*. https://arxiv.org/abs/2007.01852 `[VERIFY]`
- Formal, T., Piwowarski, B., & Clinchant, S. (2021). SPLADE: Sparse lexical and expansion model for first stage ranking. *SIGIR 2021*. https://arxiv.org/abs/2107.05720 `[VERIFY]`
- Gao, L., Zhang, Y., Han, J., & Callan, J. (2021b). Scaling deep contrastive learning batch size under memory limited setup. *RepL4NLP 2021*. https://arxiv.org/abs/2101.06983 `[VERIFY]`
- Gao, L., Ma, X., Lin, J., & Callan, J. (2023b). Precise zero-shot dense retrieval without relevance labels. *ACL 2023*. https://arxiv.org/abs/2212.10496 `[VERIFY]`
- Gao, T., Yao, X., & Chen, D. (2021a). SimCSE: Simple contrastive learning of sentence embeddings. *EMNLP 2021*. https://arxiv.org/abs/2104.08821 `[VERIFY]`
- Gao, Y., et al. (2023a). Retrieval-augmented generation for large language models: A survey. https://arxiv.org/abs/2312.10997 `[VERIFY]`
- Gururangan, S., et al. (2020). Don't stop pretraining: Adapt language models to domains and tasks. *ACL 2020*. https://arxiv.org/abs/2004.10964 `[VERIFY]`
- Guu, K., Lee, K., Tung, Z., Pasupat, P., & Chang, M.-W. (2020). REALM: Retrieval-augmented language model pre-training. *ICML 2020*. https://arxiv.org/abs/2002.08909 `[VERIFY]`
- Henderson, M., et al. (2017). Efficient natural language response suggestion for Smart Reply. https://arxiv.org/abs/1705.00652 `[VERIFY]`
- Hofstätter, S., Lin, S.-C., Yang, J.-H., Lin, J., & Hanbury, A. (2021). Efficiently teaching an effective dense retriever with balanced topic aware sampling. *SIGIR 2021*. https://arxiv.org/abs/2104.06967 `[VERIFY]`
- Houlsby, N., et al. (2019). Parameter-efficient transfer learning for NLP. *ICML 2019*. https://arxiv.org/abs/1902.00751 `[VERIFY]`
- Hu, E. J., et al. (2022). LoRA: Low-rank adaptation of large language models. *ICLR 2022*. https://arxiv.org/abs/2106.09685 `[VERIFY]`
- Izacard, G., et al. (2022). Unsupervised dense information retrieval with contrastive learning. *TMLR*. https://arxiv.org/abs/2112.09118 `[VERIFY]`
- Järvelin, K., & Kekäläinen, J. (2002). Cumulated gain-based evaluation of IR techniques. *ACM TOIS, 20*(4), 422–446. `[VERIFY]`
- Johnson, J., Douze, M., & Jégou, H. (2021). Billion-scale similarity search with GPUs. *IEEE Transactions on Big Data, 7*(3). https://arxiv.org/abs/1702.08734 `[VERIFY]`
- Joshi, P., Santy, S., Budhiraja, A., Bali, K., & Choudhury, M. (2020). The state and fate of linguistic diversity and inclusion in the NLP world. *ACL 2020*. https://arxiv.org/abs/2004.09095 `[VERIFY]`
- Karpukhin, V., et al. (2020). Dense passage retrieval for open-domain question answering. *EMNLP 2020*. https://arxiv.org/abs/2004.04906 `[VERIFY]`
- Khattab, O., & Zaharia, M. (2020). ColBERT: Efficient and effective passage search via contextualized late interaction over BERT. *SIGIR 2020*. https://arxiv.org/abs/2004.12832 `[VERIFY]`
- Kusupati, A., et al. (2022). Matryoshka representation learning. *NeurIPS 2022*. https://arxiv.org/abs/2205.13147 `[VERIFY]`
- Lagumbay, J. R. T., & Roxas, R. R. (2025). CebQA: Cebuano question answering system. *NiDS 2025* (Springer). Project page: https://cvsc.upcebu.edu.ph/index.php/project/cebqa-cebuano-question-answering-system/ `[VERIFY]` (venue and year not confirmed from the paper)
- Lee, C., et al. (2025a). NV-Embed: Improved techniques for training LLMs as generalist embedding models. *ICLR 2025*. https://arxiv.org/abs/2405.17428 `[VERIFY]`
- Lee, J., et al. (2024). Gecko: Versatile text embeddings distilled from large language models. https://arxiv.org/abs/2403.20327 `[VERIFY·L]`
- Lee, J., et al. (2025b). Gemini Embedding: Generalizable embeddings from Gemini. https://arxiv.org/abs/2503.07891 `[VERIFY·L]`
- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS 2020*. https://arxiv.org/abs/2005.11401 `[VERIFY]`
- Li, Z., et al. (2023). Towards general text embeddings with multi-stage contrastive learning. https://arxiv.org/abs/2308.03281 `[VERIFY]`
- Liu, N. F., et al. (2024). Lost in the middle: How language models use long contexts. *TACL, 12*. https://arxiv.org/abs/2307.03172 `[VERIFY]`
- Liu, T.-Y. (2009). Learning to rank for information retrieval. *Foundations and Trends in Information Retrieval, 3*(3), 225–331. `[VERIFY]`
- Lovenia, H., et al. (2024). SEACrowd: A multilingual multimodal data hub and benchmark suite for Southeast Asian languages. *EMNLP 2024*. https://aclanthology.org/2024.emnlp-main.296/ `[VERIFY·L]`
- Malkov, Y. A., & Yashunin, D. A. (2020). Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs. *IEEE TPAMI, 42*(4). https://arxiv.org/abs/1603.09320 `[VERIFY]`
- Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to information retrieval*. Cambridge University Press. https://nlp.stanford.edu/IR-book/ `[VERIFY]`
- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. https://arxiv.org/abs/1301.3781 `[VERIFY]`
- Miller, E. (2024). Adding error bars to evals: A statistical approach to language model evaluations. https://arxiv.org/abs/2411.00640 `[VERIFY·L]`
- Miranda, L. J. V., Aco, E., Manuel, C., Cruz, J. C. B., & Imperial, J. M. (2025). FilBench: Can LLMs understand and generate Filipino? *EMNLP 2025*, 2496–2529. https://aclanthology.org/2025.emnlp-main.127/ `[VERIFY·L]`
- Muennighoff, N., Tazi, N., Magne, L., & Reimers, N. (2023). MTEB: Massive Text Embedding Benchmark. *EACL 2023*. https://arxiv.org/abs/2210.07316 `[VERIFY]`
- Navasardyan, Z., Minsayan, B., Bughdaryan, S., & Davtyan, H. (2026). Less is more: Adapting text embeddings for low-resource languages with small scale noisy synthetic data. *LoResLM 2026*, 362–370. https://arxiv.org/abs/2603.22290 `[VERIFY·L]`
- Nguyen, T., et al. (2016). MS MARCO: A human generated machine reading comprehension dataset. https://arxiv.org/abs/1611.09268 `[VERIFY]`
- NLLB Team, et al. (2022). No language left behind: Scaling human-centered machine translation. https://arxiv.org/abs/2207.04672 `[VERIFY]`
- Nogueira, R., & Cho, K. (2019). Passage re-ranking with BERT. https://arxiv.org/abs/1901.04085 `[VERIFY]`
- Omotoso, A., Shopeju, H., Joshua, A. M., & Oni, S. (2025). Improving BGE-M3 multilingual dense embeddings for Nigerian low resource languages. *WiNLP 2025*, 224–229. https://aclanthology.org/2025.winlp-main.33 `[VERIFY·L]`
- van den Oord, A., Li, Y., & Vinyals, O. (2018). Representation learning with contrastive predictive coding. https://arxiv.org/abs/1807.03748 `[VERIFY]`
- Pfeiffer, J., Vulić, I., Gurevych, I., & Ruder, S. (2020). MAD-X: An adapter-based framework for multi-task cross-lingual transfer. *EMNLP 2020*. https://arxiv.org/abs/2005.00052 `[VERIFY]`
- Pilar, M. B. E., et al. (2023). CebuaNER: A new baseline Cebuano named entity recognition model. *PACLIC 37*, 792–800. https://aclanthology.org/2023.paclic-1.79 `[VERIFY·L]`
- Ponwitayarat, W., Limkonchotiwat, P., et al. (2026). SEA-BED: How do embedding models represent Southeast Asian languages? *ACL 2026*. https://arxiv.org/abs/2508.12243 `[VERIFY·L]`
- Qu, Y., et al. (2021). RocketQA: An optimized training approach to dense passage retrieval for open-domain question answering. *NAACL 2021*. https://arxiv.org/abs/2010.08191 `[VERIFY]`
- Radford, A., et al. (2021). Learning transferable visual models from natural language supervision. *ICML 2021*. https://arxiv.org/abs/2103.00020 `[VERIFY]`
- Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. *EMNLP-IJCNLP 2019*. https://arxiv.org/abs/1908.10084 `[VERIFY]`
- Reimers, N., & Gurevych, I. (2020). Making monolingual sentence embeddings multilingual using knowledge distillation. *EMNLP 2020*. https://arxiv.org/abs/2004.09813 `[VERIFY]`
- Robertson, S., & Zaragoza, H. (2009). The probabilistic relevance framework: BM25 and beyond. *Foundations and Trends in Information Retrieval, 3*(4), 333–389. `[VERIFY]`
- Salton, G., Wong, A., & Yang, C. S. (1975). A vector space model for automatic indexing. *Communications of the ACM, 18*(11), 613–620. `[VERIFY]`
- Sentence-Transformers documentation. (n.d.). Loss overview; Training overview. https://sbert.net/docs/sentence_transformer/loss_overview.html `[VERIFY]`
- Smucker, M. D., Allan, J., & Carterette, B. (2007). A comparison of statistical significance tests for information retrieval evaluation. *CIKM 2007*. https://doi.org/10.1145/1321440.1321528 `[VERIFY]`
- Spärck Jones, K. (1972). A statistical interpretation of term specificity and its application in retrieval. *Journal of Documentation, 28*(1), 11–21. `[VERIFY]`
- Thakur, N., Reimers, N., Rücklé, A., Srivastava, A., & Gurevych, I. (2021). BEIR: A heterogeneous benchmark for zero-shot evaluation of information retrieval models. *NeurIPS 2021 Datasets and Benchmarks*. https://arxiv.org/abs/2104.08663 `[VERIFY]`
- Thakur, N., Ni, J., Hernández Ábrego, G., Wieting, J., Lin, J., & Cer, D. (2024). Leveraging LLMs for synthesizing training data across many languages in multilingual dense retrieval. *NAACL 2024*. https://aclanthology.org/2024.naacl-long.426 `[VERIFY·L]`
- Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS 2017*. https://arxiv.org/abs/1706.03762 `[VERIFY]`
- Voorhees, E. M. (2002). The philosophy of information retrieval evaluation. In *CLEF 2001*, LNCS 2406, 355–370. Springer. `[VERIFY]`
- Wang, K., Thakur, N., Reimers, N., & Gurevych, I. (2022b). GPL: Generative pseudo labeling for unsupervised domain adaptation of dense retrieval. *NAACL 2022*. https://arxiv.org/abs/2112.07577 `[VERIFY]`
- Wang, L., et al. (2022a). Text embeddings by weakly-supervised contrastive pre-training. https://arxiv.org/abs/2212.03533 `[VERIFY]`
- Wang, L., et al. (2024a). Multilingual E5 text embeddings: A technical report. https://arxiv.org/abs/2402.05672 `[VERIFY]`
- Wang, L., et al. (2024b). Improving text embeddings with large language models. *ACL 2024*. https://arxiv.org/abs/2401.00368 `[VERIFY]`
- Wu, S., & Dredze, M. (2020). Are all languages created equal in multilingual BERT? *RepL4NLP 2020*. https://arxiv.org/abs/2005.09093 `[VERIFY]`
- Xiao, S., et al. (2024). C-Pack: Packed resources for general Chinese embeddings. *SIGIR 2024*. https://arxiv.org/abs/2309.07597 `[VERIFY]`
- Xiong, L., et al. (2021). Approximate nearest neighbor negative contrastive learning for dense text retrieval. *ICLR 2021*. https://arxiv.org/abs/2007.00808 `[VERIFY]`
- Zeng, et al. (2026). Code-switching information retrieval: Benchmarks, analysis, and the limits of current retrievers. *Findings of ACL 2026*. https://aclanthology.org/2026.findings-acl.636/ `[VERIFY·L]` (full author list not checked)
- Zhang, X., Ma, X., Shi, P., & Lin, J. (2021). Mr. TyDi: A multi-lingual benchmark for dense retrieval. *MRL 2021*. https://arxiv.org/abs/2108.08787 `[VERIFY]`
- Zhang, X., et al. (2023). MIRACL: A multilingual retrieval dataset covering 18 diverse languages. *TACL, 11*. https://arxiv.org/abs/2210.09984 `[VERIFY]`
- Zhang, Y., et al. (2025). Qwen3 Embedding: Advancing text embedding and reranking through foundation models. https://arxiv.org/abs/2506.05176 `[VERIFY·L]`

---

*End of guide. Work through Section 5.1 aloud. Wherever an answer feels shaky, follow the reading path for that
topic.*
