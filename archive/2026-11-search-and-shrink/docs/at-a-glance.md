# Thesis at a Glance

*The 5-minute version. For depth, read `primer.md`.*

**Working title:** Search and Shrink: Quantization and Calibration Losses for Cebuano, Tagalog and English in Small Offline Language Models

## In 30 seconds

You're measuring how much a small, **compressed** AI model gets worse at Cebuano, and whether you can win some of
that back. To run AI offline on a cheap laptop or phone, models get shrunk. Prior work suggests shrinking hurts low-resource languages more
than English; for Cebuano, nobody has measured by how much on real tasks (to our knowledge).

| Item | In short |
|---|---|
| Core question | How much accuracy does Cebuano lose at each compression level, vs. English and Tagalog? |
| Most original part | Does "tuning" the compression with Cebuano text protect Cebuano? |
| Data | Public datasets only. No fieldwork. |
| Compute | Laptop for coding and small tests; AWS GPU instance (paid from credits) for all experiments |
| Next big date | Proposal defense, Friday Dec 18, 2026 |
| Final defense | Mid to late May 2027 |

## What this is — the open-book exam

A student takes an **open-book exam in a library**: find the right page, then read it and answer. That's RAG.

| Part | Analogy | Question | New? |
|---|---|---|---|
| RQ1 Search (supporting) | Keyword librarian vs. meaning librarian | In a realistic library full of real Cebuano decoys, how often do they still find the right page? | Partly — others used a tiny library |
| RQ2 Compression (core) | Shrinking the student like compressing a photo; Cebuano is the fine print that blurs first | How much worse does the student read Cebuano at each level? | Yes |
| RQ2b Calibration (most original) | The "study guide" the shrinking tool reads before deciding what to protect | Does a Cebuano study guide keep more Cebuano? | Yes |
| RQ3 Errors | A teacher sorting wrong answers by type | Which mistakes grow as the student shrinks? (linguist verifies) | Yes, to our knowledge |

Almost everything has an answer key (multiple choice; known correct page), so a computer grades it.

## Why it matters

A barangay health center wants an offline Cebuano Q&A app on an old laptop. They need a small, compressed model,
and nobody can tell them how much worse it gets in Cebuano or how to fix it. This thesis gives them the number.
Even "Cebuano is no worse" is a useful result: developers could compress safely.

## Where we are

Planning done and novelty checked; topic final (copra dropped 2026-11-21); nothing run yet. Next: proof of concept, then proposal chapters.
Live status: `status.md`.

## The whens

Prepare and propose (→ Dec 18) · Get ready (holidays) · Run experiments (Jan 4 → Feb 21) ·
Sort the mistakes (→ Mar 21) · Write and polish (→ May 16) · Final defense (late May). Detail: `timeline.md`.
