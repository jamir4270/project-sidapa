# Sources

*Every source the thesis may cite, with its evidence tag. Add new sources here before citing them in a chapter.
Tags: `VERIFIED` opened and checked · `VERIFY` secondary or memory · `UNCONFIRMED` not found/opened.*

## Core prior work

| Short name | Citation / link | What it gives us | Tag |
|---|---|---|---|
| MTEB BelebeleRetrieval | Task file: https://github.com/embeddings-benchmark/mteb (mteb/tasks/retrieval/multilingual/belebele_retrieval.py); results: https://github.com/embeddings-benchmark/results | Cebuano/Tagalog search baselines; 488 passages, 900 Qs; BM25 0.784, e5-large-instruct 0.875 (ceb nDCG@10) | VERIFIED |
| MMTEB | https://arxiv.org/abs/2502.13595 | The benchmark that includes BelebeleRetrieval | VERIFIED |
| CebQA / CebQuAD | Lagumbay & Roxas, UP Cebu. Project: https://cvsc.upcebu.edu.ph/index.php/project/cebqa-cebuano-question-answering-system/ · Springer: https://link.springer.com/chapter/10.1007/978-3-032-10827-2_28 | Cebuano QA: BM25 vs DPR (BM25 63%), F1 49.50 at k=1 | VERIFIED (page); venue/year/size/license UNCONFIRMED |
| Waskito et al. | "Multilinguality after Quantization," Findings of IJCNLP-AACL 2026, pp. 155–180. https://aclanthology.org/2026.findings-aacl.9/ | Perplexity under GPTQ for CEB/FIL/WAR/ILO/PAG; Indonesian calibration, low transfer to PH languages | VERIFIED (Fig. 5 values UNCONFIRMED) |
| Marie & Fujita | "The Uneven Impact of Post-Training Quantization in Machine Translation," arXiv 2508.20893 | GGUF Q4_K_M/Q2_K; low-resource hit hardest; same-language calibration helps; fil_PH in released data | VERIFIED (fil rows VERIFY) |
| Marchisio et al. 2024 | "How Does Quantization Affect Multilingual LLMs?" arXiv 2407.03211 | Automatic metrics understate damage; low-resource and small models suffer more | VERIFIED |
| FilBench | EMNLP 2025, arXiv 2508.03523; harness: https://github.com/filbench/filbench-eval | 27 LLMs on Tagalog/Cebuano; baseline numbers; SIB-200 ceb = 99 items | VERIFIED (72.23 vs 75.56 inconsistency in paper) |
| SEA-BED | ACL 2026, arXiv 2508.12243 | SEA embedding benchmark; no Cebuano, no Filipino retrieval | VERIFIED |
| Miller 2024 | "Adding Error Bars to Evals," arXiv 2411.00640 | Statistics recipe: clustered SEs, paired tests | VERIFIED |
| Cebuano Wikipedia quality | "How Good is Your Wikipedia?" arXiv 2411.05527 | ~99% bot-written; dedup removes ~80% | VERIFIED |
| Chimoto et al. | "Calibrating Beyond English," arXiv 2601.18306 | Target-language calibration (African languages) | VERIFY |
| Community imatrix test | Reddit r/LocalLLaMA, English vs Norwegian vs Malayalam imatrix | No significant difference | VERIFY (forum; cite cautiously) |

## Offline / on-device motivation (added 2026-11-22; found by search, not yet opened)

*"Offline" is the study's motivation, not a tested claim. Cite these for "small compressed models run on ordinary/edge hardware."*

| Short name | Citation / link | What it gives us | Tag |
|---|---|---|---|
| AWQ | Lin et al., "AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration," MLSys 2024 (Best Paper). https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html · arXiv 2306.00978 | Quantization explicitly motivated by on-device use; reports runs on desktop/mobile GPUs, laptops, Raspberry Pi | VERIFY |
| On-device LM review | Xu et al., "On-Device Language Models: A Comprehensive Review," arXiv 2409.00088 (2024) | Survey: compression and deployment of LMs on edge devices | VERIFY (preprint) |
| MobileLLM | Liu et al., "MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases," ICML 2024, PMLR 235:32431–32454. https://proceedings.mlr.press/v235/liu24ce.html | Peer-reviewed case for small models on devices | VERIFY |
| llama.cpp | ggml-org/llama.cpp, https://github.com/ggml-org/llama.cpp (cite as software, with the commit used) | Stated aim: LLM inference with minimal setup on a wide range of local hardware | VERIFY (only mirrors seen; check the live README) |
| Local-LLM community | e.g., r/LocalLLaMA | Illustrates real-world practice only; grey literature, never the sole support | — |
 (added 2026-11-20; found by search, not yet opened)

| Short name | Citation / link | What it gives us | Tag |
|---|---|---|---|
| MQM | W3C MQM Community Group, https://www.w3.org/community/mqmcg ; Lommel et al. 2014 | Standard error typology (Accuracy, Fluency, …; minor/major/critical) | VERIFY |
| Freitag et al. 2021 | "Experts, Errors, and Context," TACL 9:1460–1474, https://arxiv.org/abs/2104.14478 | MQM applied by professional annotators | VERIFY |
| Kocmi et al. 2024 | "Error Span Annotation," WMT 2024, https://aclanthology.org/2024.wmt-1.131 | Lighter alternative to MQM | VERIFY |
| Maynez et al. 2020 | "On Faithfulness and Factuality in Abstractive Summarization," ACL, https://arxiv.org/abs/2005.00661 | Intrinsic vs extrinsic hallucination | VERIFY |
| Ovalle et al. 2025 | "Beg to Differ: Understanding Reasoning-Answer Misalignment Across Languages," EMNLP MRL workshop, https://arxiv.org/abs/2512.22712 | Reasoning–answer misalignment taxonomy, multilingual | VERIFY (v1/v2 differ) |
| Dou et al. 2022 | "Scarecrow," ACL, https://aclanthology.org/2022.acl-long.501 | How to build an error typology via pilot annotation | VERIFY |
| Fereday & Muir-Cochrane 2006 | IJQM 5(1):80–92, DOI 10.1177/160940690600500107 | Hybrid deductive–inductive coding | VERIFY |
| Nickerson et al. 2013 | "A method for taxonomy development…," EJIS 22(3):336–359, DOI 10.1057/ejis.2012.26 | Taxonomy method with ending conditions | VERIFY |
| Kundisch et al. 2021 | "An Update for Taxonomy Designers," BISE, https://link.springer.com/article/10.1007/s12599-021-00723-x | Only 48% of taxonomies report ending conditions | VERIFY |
| Marchisio et al. 2024b | "Understanding and Mitigating Language Confusion in LLMs," EMNLP, https://arxiv.org/abs/2406.20052 | Line-level pass rate (automatic language-switch metric) | VERIFY |
| GlotLID | Kargaran et al., EMNLP 2023 Findings, https://arxiv.org/abs/2310.16248 | Language ID for 1,665 languages | VERIFY (`ceb_Latn` coverage) |
| Krippendorff | *Content Analysis* (2004/2019); thresholds 0.667 / 0.800 | Reliability thresholds | VERIFY |
| O'Connor & Joffe 2020 | IJQM 19, DOI 10.1177/1609406919899220 | Intercoder reliability practice | VERIFY |

## Datasets

| Dataset | Link | License | Tag |
|---|---|---|---|
| Belebele | https://huggingface.co/datasets/facebook/belebele | CC BY-SA 4.0 | VERIFIED |
| SIB-200 | https://huggingface.co/datasets/Davlan/sib200 | CC BY-SA 4.0 | VERIFY |
| Tatoeba | via FilBench | CC BY 2.0 FR | VERIFY |
| FLORES+ | openlanguagedata/flores_plus (HF) | CC BY-SA 4.0 | VERIFY |
| CebuaNER | https://huggingface.co/datasets/josephimperial/CebuaNER (arXiv 2310.00679) | Non-commercial research, fair use | VERIFIED |
| Leipzig Corpora, Cebuano | https://curl.corpora.uni-leipzig.de/languages/ceb | CC BY | VERIFIED |
| HPLT 2.0 cleaned (ceb_Latn) | https://huggingface.co/datasets/HPLT/HPLT2.0_cleaned | CC0 | VERIFIED |
| NewsPH | Hugging Face `newsph` | GPL-3.0 | VERIFIED |
| CebQuAD | `jhoannarica/cebquad_split`, `jhoannarica/CebQuAD_fixed` (HF) | Unknown | UNCONFIRMED |

## Background and context

| Source | Use | Tag |
|---|---|---|
| Filipino NLP catalog — https://ljvmiranda921.github.io/filipino-nlp | Map of datasets and people | VERIFIED |
| FilBench blog — https://ljvmiranda921.github.io/projects/2025/08/21/filbench | Beginner intro | VERIFIED |
| Lj Miranda, "On what it takes" (May 2026) — https://ljvmiranda921.github.io/notebook/2026/05/23/on-what-it-takes/ | Field direction | VERIFIED |
| RA 8293 Sec. 185 (fair use), as amended by RA 10372 | Copyright basis | VERIFIED |
| Lenovo PSREF, ThinkPad T14 Gen 1 (AMD) | RAM: soldered + one SO-DIMM, up to 32GB | VERIFIED |

## Do not cite

| Source | Why |
|---|---|
| arXiv 2505.20276 | Not opened; claim "4-bit hurts non-English more" unverified |
| Any claim of "first Cebuano retrieval baseline" | Taken by MTEB/CebQA |
