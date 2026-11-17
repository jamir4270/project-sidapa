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
