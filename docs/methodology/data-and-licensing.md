# Data and Licensing

## Datasets

| Dataset | What | Size (ceb) | Use | License |
|---|---|---|---|---|
| Belebele (`facebook/belebele`) | MC reading comprehension, FLORES passages (~79 words avg) | 900 Qs / 488 passages | RQ1, RQ2 | CC BY-SA 4.0 `VERIFIED` |
| MTEB BelebeleRetrieval results | Published search scores (~259 models) | ceb, tgl, cross-lingual | RQ1 baselines | Repo license `VERIFY` |
| SIB-200 | 7-topic classification | 99 | RQ2 check | CC BY-SA 4.0 `VERIFY` |
| Tatoeba ceb→eng | Sentence pairs | ~2,900 | RQ2 check | CC BY 2.0 FR `VERIFY` |
| FLORES+ | Translated sentences | ~1,000 | Perplexity run | CC BY-SA 4.0 `VERIFY` |
| CebuaNER texts | 4,258 Cebuano news articles (Yes the Best Dumaguete, Filipinas Bisaya, SunStar Cebu) | 4,258 articles | RQ1 decoys | Non-commercial research, fair use `VERIFIED` |
| Leipzig Cebuano (`ceb_community_2017`) | Web sentences, shuffled | ~729k sentences | RQ2b calibration text | CC BY `VERIFIED` |
| HPLT 2.0 cleaned, ceb_Latn | Web crawl | Large | Backup decoys (filter hard) | CC0 `VERIFIED` |
| NewsPH | Filipino news | ~2.2M | Tagalog decoys | GPL-3.0 `VERIFIED` |
| English news (TBD source) | News | Match ceb size | English decoys | `TBD` |
| CebQuAD | LLM-generated Cebuano QA from news | `UNCONFIRMED` | Optional 2nd test set | `UNCONFIRMED` |

**Never use:** Cebuano Wikipedia (≈99% bot-written) or synthetic text (e.g., Sailor2 `sea-synthetic`) as decoys or calibration.

## Building the decoy library (RQ1)

1. Collect CebuaNER articles (one word per line with tags → rebuild sentences with a short script). Top up from HPLT if needed.
2. Chunk into Belebele-sized passages (~80 words, ~4 sentences).
3. Clean: dedupe; language-ID filter (drop mostly Tagalog/English chunks); drop bot/template text.
4. Remove anything that duplicates a Belebele passage.
5. Spot-check ~50 questions for decoys that accidentally answer them; log cases.
6. Build Tagalog (NewsPH) and English decoy sets of the same size.
7. Sizes: 500 / 2,000 / 10,000 for the library-size curve.

Keep calibration text (Leipzig) separate from decoys (news) and from test passages.

## Copyright policy

- Legal basis: RA 8293 Sec. 185.1 (as amended by RA 10372) treats fair use for scholarship and research as non-infringing,
  judged on purpose, nature, amount used and market effect. Not legal advice; confirm with the adviser / VSU IP office.
- **Use privately; don't redistribute.** Copyrighted corpora stay in `data/` (git-ignored) and in private cloud datasets only.
- **If releasing the benchmark:** publish code + source IDs/URLs + build script, never article text.
- **Thesis document:** quote only short snippets with attribution.
- **Scraping:** prefer CebuaNER; if scraping, respect site terms and robots.txt.
- Chapter 3 includes a license table (dataset, license, citation, how used).
- Ask for VSU's IP policy (RA 10372 requires schools to adopt one) and cite it.

## CebQuAD split-leakage check (2026-11-24)

Script: `experiments/scripts/check_cebquad_splits.py` (stdlib only; data in `data/cebquad/`, git-ignored).
Source: `jhoannarica/cebquad_split` CSVs (train 19,300 / validation 2,732 / test 5,597 rows; no license stated).

| Check | Result |
|---|---|
| Split unit | **By article:** 0 article IDs shared between any two splits |
| Duplicate articles under different IDs | 3 across splits (2 train–val, 1 train–test); also ~6 within train |
| Shared passages (contexts) | train–val 25, train–test 13, val–test 1 (test: 13 of 3,842 = 0.3%) |
| Identical question + passage pairs | train–val 3, train–test 2, val–test 0 |
| Generic questions | 180 of 5,510 test questions (3.3%) also occur, word for word, with a different passage (e.g. "Asa gidala ang biktima human sa aksidente?"). Lower bound: near-identical templated variants are more common |

**Action:** before any test run, drop test/validation passages and pairs that also occur in train (exact match after
whitespace/case normalization). For retrieval, generic questions have several plausible passages: either filter them out
or treat every passage that answers them as relevant (`TBD`). Report the number removed.
