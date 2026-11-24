# Novelty Check — Cebuano Embedding-Model Fine-Tuning for Retrieval

*Written 2026-11-24. Search-bounded: web search (general, arXiv, ACL Anthology via search engine) and Hugging Face pages,
8 queries plus 3 page-reading passes. Not a systematic review. Re-run before the Dec 7 draft and before the final defense.
The old study's novelty check is in `../../archive/2026-11-search-and-shrink/docs/literature/novelty-check.md`.*

## Verdict in one paragraph

The **method** is taken: fine-tuning a multilingual embedder (mE5, BGE-M3) with a small amount of synthetic or
translated data improves retrieval in low-resource languages (Armenian, Nigerian languages). **Cebuano retrieval
baselines** are taken (MTEB BelebeleRetrieval; CebQA). **No paper or model was found that fine-tunes an embedder for
Cebuano retrieval and reports Cebuano retrieval scores**, and no Cebuano retrieval test set with human-written
colloquial or code-switched (Bisaya–English) queries was found. Those two are the open space. The nearest existing
Cebuano resource, CebQuAD, has LLM-generated questions validated by speakers, so "human-checked" alone is not enough
to claim; "human-written, including colloquial and code-switched queries" is.

## What is taken (do not claim)

| Claim to avoid | Taken by | Tag |
|---|---|---|
| First Cebuano retrieval baselines / benchmark | MTEB BelebeleRetrieval (ceb, incl. cross-lingual; ~259 models' scores); CebQA (BM25 vs DPR on Cebuano news, BM25 best) | VERIFIED (MTEB) / VERIFY (CebQA, abstract-level) |
| First Cebuano QA dataset | CebQuAD (CebQA project): news articles, pseudonymized; QA pairs generated with GPT-4o mini and validated by Cebuano speakers; size and license not found | VERIFY (search snippet; Springer page paywalled, project page 404) |
| Fine-tuning embedders for low-resource languages works (as a new finding) | Navasardyan et al. 2026 (Armenian); Omotoso et al. 2025 (Yorùbá, Igbo, Hausa) | VERIFIED (arXiv HTML / ACL landing page read) |
| First code-switched retrieval benchmark | CSR-L (Zeng et al., Findings of ACL 2026): human-written English–Chinese and English–Japanese code-switched queries; code-switching degrades even strong multilingual retrievers. No Philippine language. | VERIFIED (arXiv HTML read) |
| First Cebuano embedding model | alphaedge-ai Qwen3-Embedding-ceb (vocabulary-trimmed Qwen3-Embedding-0.6B, **not retrained**, no Cebuano scores); DOST-ASTI BERT-ceb-cased (masked LM, not a retriever) | VERIFIED (model cards read) |

## What appears open (always "to our knowledge")

| Safe claim | Status |
|---|---|
| First embedding model fine-tuned for Cebuano passage retrieval, with Cebuano retrieval results | Not found in this search → `UNCONFIRMED` gap |
| First Cebuano retrieval test set with **human-written** queries, including colloquial and Cebuano–English code-switched queries | Not found → `UNCONFIRMED` gap (CebQuAD is the closest; check its query style once the paper is obtained) |
| First measurement of how much code-switched (Bisaya–English) queries hurt retrieval, and whether Cebuano fine-tuning reduces that | Not found; CSR-L shows the effect for zh/ja–en only → `UNCONFIRMED` gap |

## Lessons from the prior studies (design-relevant)

| Source | What they did | What it means for this study |
|---|---|---|
| Navasardyan et al. 2026 (LoResLM @ EACL) | mE5-base fine-tuned on Armenian pairs machine-translated from English Reddit title–body pairs (Gemma-2-27B); 10k pairs ≈ 1M pairs; retrieval 58.15 → 79.35; **185 manually created gold query–document pairs reviewed by 2 reviewers** | Precedent for (a) translated English pairs as training data, avoiding LLM-written Cebuano, (b) a small human test set (~185–300 pairs) being publishable, (c) two reviewers. Loss not named in their setup section. |
| Omotoso et al. 2025 (WiNLP) | BGE-M3 contrastive fine-tune on news-sourced pairs for Yorùbá/Igbo/Hausa; big gains on in-domain Wura test (MRR 0.78 → 0.92 Yorùbá) but **almost none on MIRACL Yorùbá (0.5952 → 0.5996)** | Warning: gains may not transfer outside the training domain. Test on a set from a different source than training, and report both. |
| CSR-L (Findings ACL 2026) | Human rewrites of queries into code-switched form, second-annotator validation; MTEB-based pipeline | Template for building code-switched queries (rewrite + validate). Cite as the closest code-switching work. |
| CebQA (NiDS 2025) | Retriever-reader on Cebuano news; BM25 beat DPR | Include BM25 as a strong baseline; dense ≠ automatically better in Cebuano. |

## Datasets, models and licenses checked (2026-11-24)

| Item | Finding | Implication |
|---|---|---|
| CebuaNER (`josephimperial/CebuaNER`) | Token-level NER (CoNLL style) from 4,258 Cebuano news articles; **CC BY-NC 4.0**; card asks users to **email before submitting it to any benchmarking project** | Usable for non-commercial research after rebuilding sentences; **email the authors** before using it in a benchmark; never redistribute text |
| Palito (`SEACrowd/palito`) | ~250k words per language; novels, stories, Bible; includes ceb; LGPL | Literary/religious register; possible training passages; odd license for text → `VERIFY` with adviser |
| HPLT 2.0 cleaned | Dataset license field CC0-1.0 (full terms not read) | Candidate source of openly licensed test passages; underlying web-text rights `VERIFY` |
| WebFAQ (`PaDaS-Lab/webfaq`) | 75 languages, CC BY 4.0; **Tagalog 21.5k pairs; no Cebuano** | Possible Tagalog training data (sibling-language transfer); scope decision needed |
| BGE-M3, multilingual-e5-base, multilingual-e5-large-instruct | MIT (model card metadata) | Fine-tuned derivatives can be released; training-data licenses still apply |
| Qwen3-Embedding-ceb-32768 | Vocabulary-trimmed, not retrained; Apache-2.0; no benchmark | A baseline, not prior work on fine-tuning |
| DOST-ASTI BERT-ceb-cased | Fill-mask model (iTANONG-DS, ICNLSP 2023); no license shown | Optional "no contrastive training" control; license `UNCONFIRMED` |

## Not resolved

- CebQuAD size, license, availability and query style (Springer chapter paywalled; project page now 404). Get it from
  the authors or the VSU library.
- JAIT 2025 "Benchmarking open-source LLMs on code-switched Tagalog-English": PDF unreadable; contents `UNCONFIRMED`.
- Full-text checks not done: ACL Anthology direct search, Google Scholar, SEACrowd catalogue, MTEB task list for any
  other ceb retrieval task. Do these before Dec 7.
- Ask: email the FilBench / SEACrowd community whether anyone is building Cebuano retrieval data.
