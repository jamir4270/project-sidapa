# Context Checklist — what Jamir hands to Claude

*The workspace was reset on 2026-11-26. Claude knows only what is in `primer.md` and what you give it here.
Work top to bottom; each item says what to give and where it goes. Paste or drop files in, then tell Claude
"process item N." Claude files it, tags it, and updates `status.md`.*

## Before the SRC meeting (Fri 2026-11-27)

- [ ] **1. Your study in your words.** 3–5 sentences: what you want to find out and why. Rough is fine.
  → Claude updates `primer.md` Part A and AGENTS.md §1.
- [ ] **2. Research questions / objectives draft.** Even half-formed. Say which one is the core.
  → AGENTS.md §4; `decisions.md` once you lock them.
- [ ] **3. What the adviser and SRC have said so far.** Dates, who, what they asked for or objected to.
  → `meetings/` (one file per meeting, from `_template.md`).
- [ ] **4. Form requirements.** What FM-VPA-06/07 ask for (title? topic? objectives?).
  → `proposal/README.md`.

## Before the full draft (Mon 2026-12-07)

- [ ] **5. Sources you have read.** For each: citation + link/DOI, and one line each of *what they did / what they
  did not do / what it means for my study*. Say if you opened the full text or only the abstract.
  → `literature/sources.md` (Claude sets the evidence tag from what you say).
- [ ] **6. Prior work that overlaps your idea.** Anything that looks like it already does what you plan.
  → `literature/novelty.md`; flagged in `status.md`.
- [ ] **7. Datasets you plan to use.** Name, link, size, license text (or permission email), and your basis for
  "usable." Do not paste the corpus text itself.
  → `methodology/data.md`.
- [ ] **8. Models you plan to compare or fine-tune.** Name, link, license.
  → `methodology/data.md`.
- [ ] **9. Your answers to the open decisions** in `primer.md` §7 (any you have settled).
  → `decisions.md`, one dated entry each.
- [ ] **10. Compute you actually have.** AWS credit amount and expiry, GPU quota status, Kaggle, department GPU.
  → AGENTS.md §7; `methodology/compute.md`.
- [ ] **11. Anything you ran or checked yourself.** Commands, outputs, numbers, notes.
  → `labs/` (one file per run) and `status.md`.

## Any time

- [ ] **12. Deadlines that change** (defense date, draft dates, job applications). → `status.md`, AGENTS.md §3.
- [ ] **13. Things you want Claude never / always to do.** → AGENTS.md §6 or Claude's memory.

## What Claude does with each item

1. Files it where the arrow says; creates the file if it does not exist yet.
2. Tags every claim (`VERIFIED` only if a source was opened; otherwise `VERIFY` / `UNCONFIRMED`).
3. Points out gaps, contradictions and overclaims, plainly.
4. Ticks the item here and logs it in `status.md`.
