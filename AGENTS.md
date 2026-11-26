# AGENTS.md — Cebuano Retrieval Thesis

Context and working rules for any AI agent (Claude or otherwise) helping with this thesis.
Read this file fully before doing anything. Then read `docs/status.md`.

> **Fresh start (2026-11-26).** The workspace was reset. The only study context is `docs/primer.md`; everything else
> comes from the researcher through `docs/context-checklist.md`. Don't assume facts that are not in the repo.

---

## 1. The project in one paragraph

An undergraduate BS Computer Science thesis at Visayas State University (VSU), Baybay City, Leyte.
Working title: `TBD`. Working shape (the researcher's to change): fine-tune an embedding model for **Cebuano passage
retrieval** and test whether it finds the right passage better than off-the-shelf multilingual embedders and BM25.
Details and open decisions: `docs/primer.md`.

## 2. The researcher

- **Jamir Oasis M. Andrade**, senior BSCS student at VSU, DOST undergraduate scholar, graduating July 2027.
- **Native Cebuano speaker.** This is a research asset (data checks, query writing, error analysis).
- **Strong software engineering / web-dev background; casual (non-expert) knowledge of ML and NLP.**
- Starts job applications in January 2027, so January–February experiments should be as hands-off as possible.
- **He writes the paper and shapes the study.** Explain, critique and point to readings; don't lock design choices for him.

### How to communicate with him

- Explain in **plain language with analogies**. Define every piece of jargon on first use.
- He works best with **clear visibility**: tables, checklists, explicit next steps, dates.
- Be **critical and pragmatic**. Point out weak spots, risks and overclaims directly. Do not flatter.
- Short sentences. Lead with the answer, then the detail.

## 3. Current status (snapshot — `docs/status.md` is the live version)

- **As of 2026-11-26:** workspace reset; direction is Cebuano retrieval; RQs not written; nothing run.
- **Next:** SRC meeting + FM-VPA-06/07 on **Fri 2026-11-27**; full draft to adviser **2026-12-07**;
  proposal defense **Fri 2026-12-18**. Final defense mid to late May 2027.

## 4. Research questions

`TBD` — the researcher drafts them (`docs/context-checklist.md` item 2). Record them here once locked.

## 5. Novelty

Not checked in this workspace yet. A first-pass summary is in `docs/primer.md` Part A (`UNCONFIRMED`). Until a
proper check is logged in `docs/literature/`:
- Don't claim "first Cebuano retrieval baselines" (MTEB BelebeleRetrieval and CebQA exist `VERIFY`).
- Prefix any novelty claim with "to our knowledge."

## 6. Hard rules for agents

1. **Never invent sources, numbers, quotes or results.** If you don't have it, say so and mark it `VERIFY`.
2. **Evidence tags.** Every factual claim in project docs carries one of:
   - `VERIFIED` — checked against the original source (link it).
   - `VERIFY` — plausible, from a secondary source or memory; confirm before relying on it.
   - `TBD` — a decision or value not yet set.
   - `UNCONFIRMED` — searched for but not found or not opened.
   Don't upgrade a tag without opening the source. Estimates are labeled "(estimate)".
3. **No overclaiming novelty.** If you find new prior work, add it to `docs/literature/` and flag it in `docs/status.md`.
4. **Copyright.** Never commit or publish copyrighted corpus text. `data/` is git-ignored. Share code plus source
   IDs/URLs, not text.
5. **Reproducibility.** Every experiment logs per-query results (query, ranked passage IDs, scores, metric values),
   model name + revision, package versions, seeds and hardware. Scripts must be resumable. See `experiments/README.md`.
6. **One machine per comparison.** Never mix machines inside one comparison.
7. **Statistics.** Every reported score gets a 95% confidence interval; comparisons on the same queries use paired
   tests. Don't claim a difference whose interval includes zero.
8. **Scope lock.** Don't add models, datasets or tasks without the researcher agreeing and logging it in `docs/decisions.md`.
9. **Decisions get logged.** Any change to RQs, datasets, tools or schedule → append to `docs/decisions.md` with
   date and reason. Keep `docs/status.md` current after every working session.
10. **Ask before destructive or outward actions** (deleting files, sending emails, publishing, spending money).

## 7. Hardware and compute (what is available; confirm via checklist item 10)

| Machine | Notes |
|---|---|
| Lenovo ThinkPad T14 Gen 1 — Ryzen 7 PRO 4750U, Vega 7 iGPU, 16 GB RAM (~6 GB free), 256 GB SSD | Code, debugging, small tests. No CUDA. |
| AWS EC2 GPU (credits) | Candidate main compute; credit amount, expiry and quota `TBD` |
| Kaggle (free) | Pilots, backup; quota `VERIFY` |
| Department GPU | Borrowing rules `TBD` |

## 8. Repository map

```
project-sidapa/
├── AGENTS.md                  ← you are here (rules + context)
├── CLAUDE.md                  ← imports AGENTS.md for Claude tools
├── README.md                  ← human-facing map
├── KICKSTART_PROMPT.md        ← prompts to start a Claude session
├── docs/
│   ├── status.md              ← LIVE: where we are, this week, blockers
│   ├── primer.md              ← at a glance + primer + reading list
│   ├── context-checklist.md   ← what the researcher hands over, and where it goes
│   ├── decisions.md           ← dated decision log + open decisions (append-only)
│   ├── literature/            ← sources.md, novelty.md (created from checklist items 5–6)
│   ├── methodology/           ← data.md, compute.md, design notes
│   ├── labs/                  ← one file per hands-on run
│   ├── proposal/              ← VSU proposal rules and chapter drafts
│   └── meetings/              ← adviser, SRC meeting notes (from _template.md)
├── archive/                   ← set-aside material (empty)
├── reference/reports/         ← background reports (empty)
├── experiments/               ← code (see experiments/README.md)
└── data/                      ← local only, git-ignored
```

## 9. How to work in this repo

- **Start of every session:** read `docs/status.md`, then the file(s) relevant to the task.
- **End of every session:** update `docs/status.md` and, if any decision was made, `docs/decisions.md`.
- **Writing:** the researcher writes the thesis. Repo docs are supporting notes; drafts he asks for go in `docs/proposal/`.
- **Writing code:** follow `experiments/README.md`. Test on a small sample locally before any cloud run.
- **When unsure:** ask one clear question rather than guessing.
