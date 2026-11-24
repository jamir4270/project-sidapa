# Timeline — Week by Week

*Dates after December are a plan to agree with the adviser. Tick the Status column as you go
(`[ ]` not started, `[~]` in progress, `[x]` done).*

## Phases

| Phase | Dates | Goal |
|---|---|---|
| 1. Prepare and propose | Nov 17 → Dec 18 | Proof of concept, proposal chapters, **defense Dec 18** |
| 2. Get ready (holidays, light work) | Dec 19 → Jan 3 | Panel revisions, decoy corpus, calibration text, resumable scripts |
| 3. Run the experiments | Jan 4 → Feb 21 | RQ2, RQ2b, RQ1, conditions, statistics (cloud, mostly hands-off) |
| 4. Sort the mistakes | Feb 22 → Mar 21 | RQ3 with the linguist |
| 5. Write and polish | Mar 22 → May 16 | Chapters 4–5, revisions, submit |
| Final defense | May 17 → 28 | Defend |

## Weeks

| Wk | Dates | Do | Done when | Status |
|---|---|---|---|---|
| 1 | Nov 17–23 | ~~NCRC-V visit~~ (done; copra dropped); AWS quota + budget alert; ask about a linguist; RAM slots + page file; install llama.cpp, `llama-bench` CPU vs Vulkan | Laptop speed numbers; AWS quota requested | [~] |
| 2 | Nov 24–30 | Proof of concept: reproduce MTEB BM25 + e5 Cebuano numbers; one 4B model at Q8/Q4/Q2 on 100 Qs per language (Kaggle if slow); read papers 1–9 | Two tables + one chart | [ ] |
| 3 | Dec 1–7 | Draft proposal chapters (intro, literature, definitions, methodology incl. license table and compute plan) | Full draft to adviser | [ ] |
| 4 | Dec 8–14 | Revise with adviser; slides; book panel; dry run | Panel date confirmed | [ ] |
| 5 | Dec 15–18 | Final dry run; **defend Dec 18** | Approved, revisions listed | [ ] |
| 6–7 | Dec 19–Jan 3 | Panel revisions; build decoy corpus (CebuaNER) + calibration text (Leipzig); resumable scripts | Corpus files, tested scripts | [ ] |
| 8 | Jan 4–10 | AWS: confirm quota and budget alert (or book dept GPU); private datasets; reproduce one FilBench Belebele number; start RQ2 grid | Baseline reproduced; grid running | [ ] |
| 9 | Jan 11–17 | Finish RQ2 main grid; parse-failure rates | Accuracy table | [ ] |
| 10 | Jan 18–24 | RQ2b: build 4 calibration files; run calibration grid | Calibration table | [ ] |
| 11 | Jan 25–31 | RQ1: search on the big library (BM25, e5, BGE-M3, affix BM25, hybrid); library-size curve | Search table + curve | [ ] |
| 12 | Feb 1–7 | RQ2 conditions (retrieved, none); SIB-200, Tatoeba, FLORES perplexity | Conditions table | [ ] |
| 13 | Feb 8–14 | **Buffer**; delete AWS disks/instances if done (S3 results kept) | All runs complete | [ ] |
| 14 | Feb 15–21 | Statistics: one bootstrap script, C1–C4 confirmatory + secondary/exploratory CIs; first figures | Results with error bars | [ ] |
| 15 | Feb 22–28 | RQ3: explanation run; collect 200–300 wrong outputs; first-pass notes; send to linguist | Sample sent | [ ] |
| 16 | Mar 1–7 | Linguist finalizes codebook | Codebook | [ ] |
| 17 | Mar 8–14 | Linguist labels; you label same 100 blind; kappa | Labels + kappa | [ ] |
| 18 | Mar 15–21 | RQ3 analysis; optional CebQuAD | Error figures | [ ] |
| 19–20 | Mar 22–Apr 4 | Write chapter 4 (results) | Draft | [ ] |
| 21–22 | Apr 5–18 | Write chapter 5; update earlier chapters | Draft | [ ] |
| 23 | Apr 19–25 | Full manuscript to adviser | Sent | [ ] |
| 24 | Apr 26–May 2 | Revise | Revised | [ ] |
| 25 | May 3–9 | Formatting, references, similarity check; submit to panel | Submitted | [ ] |
| 26 | May 10–16 | Slides, dry runs | Ready | [ ] |
| 27 | May 17–28 | **Final defense** | Defended | [ ] |

**Notes:** Weeks 8–13 are compute-heavy but hands-off, leaving room for job applications. Week 13 is a
deliberate buffer. If the proposal defense slips to early January, start the RQ2 grid over the break anyway.
