# Novelty Check (2026-11-17)

*Summary first; the full report follows. Safe wording is in section "Safe wording". Re-run a short check before the proposal defense and before final submission.*

## Summary

| Claim | Verdict | Why |
|---|---|---|
| First Cebuano retrieval baselines | Fails | MTEB BelebeleRetrieval (ceb/tgl, ~259 models, BM25 0.784); CebQA (BM25 vs DPR) |
| First quantization study on any Philippine language | Fails as worded | Waskito et al. 2026 (perplexity, GPTQ, Indonesian calibration); Marie & Fujita 2025 (Filipino GGUF scores released, unanalysed) |
| First Cebuano error taxonomy | Probably holds | Nothing found; say "to our knowledge" |

**Still open:** task accuracy across GGUF levels in Cebuano/Tagalog vs English; Cebuano/Tagalog calibration; end-to-end search-then-answer on a realistic corpus.

---

## Full report

> **Numbering note:** the report below numbers the questions differently from the rest of the workspace.
> Report RQ1 = our **RQ2** (compression), report RQ1b = our **RQ2b** (calibration), report RQ2 = our **RQ1** (search).
> The workspace keeps pipeline order (search, then read). See `../methodology/research-questions.md`.
>
> **Superseded points (2026-11-17):** this report predates later decisions. (1) RQ3 uses a **Cebuano linguist**,
> not just "a second native speaker" (`../decisions.md`). (2) The main grid runs on **AWS (credits)**, not the laptop;
> the "~15 laptop hours at ~1 s/prompt" figure is too optimistic, see the grid-size math in
> `../methodology/compute.md`. (3) The adviser script at the end has been updated to match.


Two of your three "first" claims fail as written, and the third is unproven. Cebuano retrieval baselines already exist. MTEB, the standard embedding benchmark, ships a Belebele retrieval task with a Cebuano subset, and it publishes scores for about 259 models plus an official BM25 baseline. UP Cebu's CebQA paper has also compared BM25 with dense retrieval on Cebuano news. Quantization of Philippine languages has also been measured. A November 2026 ACL-venue paper (Waskito et al.) reports quantized-model perplexity for Cebuano, Filipino, Waray, Ilocano and Pangasinan. A 2025 study (Marie & Fujita) ran GGUF-quantized models on Filipino translation and released the scores without analysing them. No prior Cebuano error taxonomy turned up, but nobody searched hard for one, so treat that claim as "to our knowledge" only. The good news is real, though. What remains open is the part that suits your laptop best: downstream accuracy across the llama.cpp quantization ladder in Cebuano and Tagalog, Cebuano-text calibration, and an end-to-end search-then-answer test on a harder corpus. Make quantization the core, turn retrieval into the "realistic pipeline" chapter, and you can still defend a clear, novel proposal by December 18.

## Each "first" claim, checked against named prior work

A quick glossary first. **nDCG@10** is a 0-to-1 retrieval score: 1.0 means the right passage was ranked first every time. **BM25** is classic keyword search. An **embedder** turns text into vectors so search can match on meaning. **GGUF** is the model file format llama.cpp uses. Q8_0 to Q2_K are its shrink levels, roughly 8-bit down to 2-bit. An **importance matrix (imatrix)** is a calibration file built by running sample text through the model, so the shrinking step protects the weights that text relies on most. **Perplexity** measures how "surprised" a model is by real text. It is cheap to compute but is not task accuracy.

| Your claim | Verdict | Prior work that breaks or limits it | What is still open |
|---|---|---|---|
| First Cebuano retrieval baselines (BM25 vs embedders on Belebele ceb/tgl/eng) | **Fails** | MTEB BelebeleRetrieval ceb/tgl/eng subsets, about 259 models scored, official BM25 baseline; CebQA (UP Cebu, Springer) BM25 vs DPR | Distractor corpus, end-to-end answer accuracy, Cebuano-aware BM25, analysis of *why* ceb trails tgl |
| First quantization measurements for any Philippine language | **Fails** | Waskito et al., Findings of IJCNLP-AACL 2026 (perplexity, GPTQ, CEB/FIL/WAR/ILO/PAG); Marie & Fujita, arXiv 2508.20893 (fil_PH in WMT24++, GGUF Q4_K_M/Q2_K) | Downstream accuracy on GGUF k-quants in ceb/tgl; Philippine-language calibration |
| First Cebuano error taxonomy, checked by a second native speaker | **Partially holds (unverified)** | None found. FilBench mentions Filipino/Cebuano confusion in translations but gives no counts | Probably open, but run a targeted search before claiming it |

### Retrieval: MTEB already ran your exact RQ1 setup

MTEB's BelebeleRetrieval task does exactly what your RQ1 proposed. The corpus is the unique Belebele passages, the queries are the Belebele questions, and each query has one correct passage. It covers `ceb_Latn`, `tgl_Latn`, Waray and Ilocano, plus every pairing with English ([MTEB task file](https://github.com/embeddings-benchmark/mteb/blob/main/mteb/tasks/retrieval/multilingual/belebele_retrieval.py)). The task is part of MMTEB, MTEB's flagship multilingual benchmark ([MMTEB paper](https://arxiv.org/abs/2502.13595)). The Cebuano subset is tiny: **488 passages and 900 questions** ([MTEB stats](https://github.com/embeddings-benchmark/mteb/blob/main/mteb/descriptive_stats/Retrieval/BelebeleRetrieval.json)). Published per-language scores already exist ([MTEB results repo](https://github.com/embeddings-benchmark/results)):

| Model | ceb-ceb | tgl-tgl | eng-eng | ceb corpus / eng query |
|---|---|---|---|---|
| BM25 (mteb/baseline-bm25s) | 0.784 | 0.842 | 0.916 | 0.548 |
| multilingual-e5-large-instruct | 0.875 | 0.920 | 0.959 | 0.919 |
| BAAI/bge-m3 | 0.844 | 0.916 | 0.956 | 0.872 |
| Qwen3-Embedding-0.6B | 0.769 | 0.790 | 0.959 | 0.852 |
| embeddinggemma-300m | 0.762 | 0.781 | 0.964 | 0.858 |

Three patterns are already public. Keyword search beats two modern small embedders on monolingual Cebuano. BM25 collapses when the query and corpus languages differ. Strong models score Cebuano about 0.04–0.08 below Tagalog. You can confirm and explain these patterns, but you cannot present them as discoveries. No paper analyses these Cebuano numbers. They sit in a results repository as leaderboard data ([MTEB results repo](https://github.com/embeddings-benchmark/results)).

CebQA closes the door further. Lagumbay and Roxas built an end-to-end Cebuano question-answering system that compares ElasticSearch/BM25 with FAISS/DPR retrieval and uses a fine-tuned XLM-RoBERTa reader. BM25 retrieved best, at 63% accuracy, and the full pipeline reached 49.50 F1 when it used only the top passage. The paper also introduced **CebQuAD**, described as "the first Cebuano QA dataset": questions generated by GPT-4o mini from Cebuano news and validated by Cebuano speakers ([UP Cebu CVSC](https://cvsc.upcebu.edu.ph/index.php/project/cebqa-cebuano-question-answering-system/)). It is a Springer proceedings chapter ([Springer](https://link.springer.com/chapter/10.1007/978-3-032-10827-2_28)). The exact venue, year and dataset size were not confirmed. CebQA differs from your design in useful ways. It uses an older retriever (DPR), not modern multilingual embedders. Its reader extracts answer spans rather than generating answers, and it does not use quantized models. Its questions are LLM-generated, not human-written.

Outside these two, the gap is real. SEA-BED (ACL 2026) has no Filipino retrieval tasks and no Cebuano at all ([SEA-BED](https://arxiv.org/html/2508.12243v2)), and MIRACL covers neither language ([MIRACL](https://arxiv.org/pdf/2210.09984)).

### Quantization: Waskito et al. measured Cebuano perplexity in November 2026

Waskito, Wicaksono, Aji and Wibowo quantized Qwen3-8B, Llama-3.1-8B-Instruct and Aya Expanse 8B to 2, 3 and 4 bits with GPTQ. As a cross-lingual check, they then measured FLORES+ perplexity on 17 Austronesian languages, including **CEB, FIL, WAR, ILO and PAG** ([ACL Anthology](https://aclanthology.org/2026.findings-aacl.9/)). That single paper sinks "any Philippine language." Its Philippine coverage is narrow, though. It reports perplexity only, uses GPTQ rather than GGUF k-quants, calibrates only on Indonesian (never a Philippine language), and shows results only as ratios in one figure. It also ran Belebele, but only on its five target languages: English, Tamil, Indonesian, Swahili and Chinese ([PDF](https://aclanthology.org/2026.findings-aacl.9.pdf)). One finding matters for you: **Philippine languages showed a low transfer effect from Indonesian calibration**, and cross-lingual effects were negligible except at 2-bit ([PDF](https://aclanthology.org/2026.findings-aacl.9.pdf)). That gives your Cebuano-calibration experiment a direct motivation.

Marie and Fujita translated all 55 WMT24++ languages, including `en-fil_ph`, with models quantized by several methods, including GGUF Q4_K_M and Q2_K. They reported only six languages in the paper and released the rest as Hugging Face datasets ([arXiv](https://arxiv.org/html/2508.20893v1); [EvalScope](https://evalscope.readthedocs.io/en/latest/benchmarks/wmt24pp.html)). Filipino scores for quantized models therefore very likely exist publicly, though nobody has confirmed the Filipino rows. Their headline result fits your hypothesis. Under Qwen3-8B at GGUF 2-bit, translation quality dropped about 2 points for Japanese and French but about 17 for Bengali and Malayalam ([ar5iv](https://ar5iv.labs.arxiv.org/html/2508.20893)).

Calibrating in the target language is an established idea. Chimoto et al. studied it for African languages ([arXiv](https://arxiv.org/html/2601.18306v1)). A community llama.cpp test used English, Norwegian and Malayalam imatrices and found no statistically significant difference ([Reddit mirror](https://libreddit.winscloud.net/r/LocalLLaMA/comments/1j9ih6e/english_k_quantization_of_llms_does_not)). Nobody has done it with Cebuano or Tagalog text. Your contribution is to extend the method to Cebuano, not to invent it. Be ready for a null result: that Reddit test is a warning that calibration language may not matter.

### Error taxonomy: probably open, not yet proven

None of the three novelty searches found a Cebuano error taxonomy for LLM output. FilBench, the main Filipino LLM benchmark, notes Filipino/Cebuano confusion in translations without counting it ([FilBench](https://arxiv.org/html/2508.03523v1)). CebQA's speaker validation checked dataset quality, which is not the same as classifying model errors ([UP Cebu CVSC](https://cvsc.upcebu.edu.ph/index.php/project/cebqa-cebuano-question-answering-system/)). Still, no search targeted "Cebuano error analysis" directly, so the claim is plausible but unchecked.

## The upside: free baselines and proof the topic matters

This prior work helps you more than it hurts. MTEB gives you a published BM25 number (0.784 on ceb-ceb) that you can reproduce in an afternoon. That is a guaranteed "my pipeline matches the literature" result for your proposal. CebQA gives you a local comparison point (BM25 best, 63%) and a second Cebuano dataset. Waskito et al. show that a 2026 ACL venue accepted Philippine-language quantization as worth measuring, and their perplexity setup gives you a number to compare against. Marie and Fujita's released Filipino scores are a dataset you can analyse for free. A panel can no longer call the topic irrelevant. Your job is to show you go further.

## Repositioned design: quantization as the core, retrieval as the realistic test

Keep the title. Reorder and sharpen the questions.

**RQ1 (core, quantization).** How much downstream accuracy do Cebuano and Tagalog lose relative to English as small models move down the GGUF ladder (Q8_0, Q6_K, Q4_K_M, Q3_K_M, Q2_K)? Use 3–4 models in the 1.7B–4B range on Belebele (900 questions per language), SIB-200 and Tatoeba ceb→en. Add FLORES+ perplexity on one model so you can line up directly with Waskito et al. The 1–4B size range matters: the earlier hardware check found it comfortable on 16GB, while 8B at Q8 is borderline ([msf.github.io](https://msf.github.io/blogpost/local-llm-performance-framework13.html)). SIB-200 has only 99 Cebuano items ([FilBench](https://arxiv.org/html/2508.03523v1)), so report its confidence intervals and lean on Belebele and Tatoeba.

**RQ1b (the novel hook, calibration).** At Q3_K_M and Q2_K, compare four calibration conditions for two models: no imatrix, an English imatrix, a Cebuano imatrix and a Tagalog imatrix. The Tagalog arm tests whether a sibling language transfers, extending Waskito's Indonesian-transfer finding to llama.cpp. Build the calibration text from Cebuano news, and make sure none of it overlaps FLORES/Belebele passages; overlap would leak test data into calibration. Building an imatrix needs the full-precision model in memory, about 8GB for a 4B model. Do that step on Kaggle if the laptop struggles.

**RQ2 (retrieval-to-reader, end to end).** Start by reproducing the MTEB numbers: your free baseline. Then make the task realistic. Add a few thousand human-written Cebuano news passages as distractors, and avoid Cebuano Wikipedia, which is about 99% bot-written ([arXiv 2411.05527](https://arxiv.org/pdf/2411.05527)). Compare plain BM25, BM25 with a simple Cebuano affix stripper (for prefixes like *nag-/mag-/gi-*), multilingual-e5-large-instruct, bge-m3, and a hybrid that merges BM25 and dense rankings. Feed the top passages to your quantized readers from RQ1. Score multiple-choice accuracy with a gold passage, a retrieved passage and no passage (closed-book). The question becomes: **which hurts Cebuano answers more, worse search or a smaller model?** MTEB cannot answer that.

Add a short gap analysis using the existing MTEB numbers. Explain why Cebuano trails Tagalog using tokenizer fertility (how many tokens each language needs per word) and Belebele's high word overlap between questions and passages. As an optional second test set, run your best retriever and reader on CebQuAD's test split and compare with CebQA's reported results. CebQuAD is native Cebuano news, which offsets Belebele's translated text, but its questions are LLM-generated and its license and size are unverified. Drop it first if time runs short.

**RQ3 (errors).** Sort 200–300 failures into types such as Tagalog substitution, English fallback, affix errors, name errors and invented facts. Have a second native speaker label a shared subset, and report Cohen's kappa, a 0-to-1 agreement score corrected for chance.

**Feasibility.** An earlier estimate put a full five-level, four-model, three-language Belebele grid at about 54,000 prompts and roughly 15 laptop hours, if each prompt takes about one second (an unverified estimate). Restricting calibration to two models keeps RQ1b to a similar size. Retrieval prompts are longer, so run RQ2 on Cebuano in full but only the best retriever for Tagalog and English. Embedding a few thousand passages with a large embedder on CPU should take minutes to under an hour. None of this has to finish before December 18. The proposal needs a pilot, not results.

| Dates | Proposal-defense milestone |
|---|---|
| Nov 17–23 | Do the checks below. Reproduce MTEB BM25 ceb-ceb (0.784). Lock RQs. |
| Nov 24–30 | Pilot: one 4B model at Q8_0/Q4_K_M/Q2_K on 100 Belebele questions in ceb/tgl/eng. Build one Cebuano imatrix. |
| Dec 1–7 | Small distractor pilot (1–2k passages, BM25 plus one embedder). Draft introduction, related work and methods. |
| Dec 8–14 | Pilot chart (accuracy vs bit-width), compute plan, slides. |
| Dec 15–18 | Rehearse; buffer. |

Since resume season starts in January, the fail-safe structure matters: RQ1 alone is a complete thesis if RQ2 slips.

### Safe wording for each claim

For retrieval, say: "Prior work established Cebuano retrieval baselines on Belebele (MTEB/MMTEB) and Cebuano news (CebQA). We extend them with a distractor-augmented corpus, Cebuano-aware lexical retrieval, and end-to-end answer accuracy with quantized local readers."

For quantization, say: "To our knowledge, this is the first systematic downstream evaluation of GGUF/llama.cpp quantization (Q8_0 to Q2_K) in Cebuano and Tagalog, and the first study of Philippine-language importance-matrix calibration. Prior work measured perplexity only, using GPTQ with Indonesian calibration (Waskito et al., 2026), or included Filipino without analysing it (Marie & Fujita, 2025)."

For errors, say: "To our knowledge, the first error taxonomy of quantized small-model outputs in Cebuano, with inter-annotator agreement."

Never write "first Cebuano retrieval baselines," "first Cebuano QA" or "first quantization study of a Philippine language."

## Checks to do yourself before the defense

1. Download `bnjmnmarie/wmt24pp-qtranslated-scores` on Hugging Face and confirm that `fil_PH` rows exist.
2. Check whether Waskito et al. posted an earlier arXiv preprint, which would move their priority date, and read their Figure 5 values for CEB and FIL.
3. Get the CebQA chapter through your library or adviser to confirm the venue, year, CebQuAD size and license. Check the license on the `jhoannarica` Hugging Face datasets, and consider emailing the authors.
4. Search Google Scholar and the ACL Anthology for "Cebuano" combined with "error analysis," "quantization" or "imatrix." Also search llama.cpp GitHub discussions for Tagalog, Filipino or Cebuano imatrix experiments.
5. Check arXiv 2510.23896 and the 26-language OneRuler list in Mekala et al. (arXiv 2505.20276) for Filipino.
6. Check the SEA-HELM leaderboard for quantized Tagalog scores, and FilBench's full text for quantized entries.
7. Filter the MTEB leaderboard by Cebuano to capture the newest models, and confirm the licenses for Belebele and your distractor news sources.
8. Email the FilBench network ([filbench.github.io](https://filbench.github.io/)) to make sure no one is already running this exact study.

## What to tell your adviser

"A novelty check turned up close prior work, so I'm reframing. MTEB already publishes Cebuano retrieval scores on Belebele, including a BM25 baseline, and UP Cebu's CebQA compared BM25 with dense retrieval on Cebuano news. A November 2026 AACL Findings paper measured perplexity of quantized models on Cebuano and Filipino, but only with GPTQ, Indonesian calibration and no downstream tasks. My core contribution is now the first downstream evaluation of llama.cpp quantization levels in Cebuano and Tagalog against English, plus a test of whether calibrating on Cebuano or Tagalog text reduces the loss. Retrieval becomes a realistic end-to-end chapter: harder distractor passages, Cebuano-aware keyword search, and quantized readers, using the MTEB numbers as reproduced baselines. An error taxonomy, finalized and verified by a Cebuano linguist, finishes the study. I code and pilot on my laptop and run the full grid on an AWS GPU instance paid from my credits, and I'll bring a pilot to the December 18 defense."

## Conclusion

The novelty check moved your contribution, not your topic. The retrieval half of "Search and Shrink" turned out to be the crowded half, because benchmark builders already sweep many languages at once. The shrink half is still open, because quantization studies pick a handful of big languages and stop there. Your advantage is the one that holds up: you can run many shrink levels cheaply on consumer hardware, and you can judge Cebuano output as a native speaker. A careful negative result counts too. If Cebuano calibration does nothing, that is exactly the kind of measured answer local developers need before they ship offline models.
