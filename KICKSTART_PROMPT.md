# Kickstart Prompts

Use these in Claude Desktop with this folder (`cebuano-thesis/`) connected as the project's working folder.

---

## 1. First session (paste once)

```
You're helping me with my undergraduate CS thesis. This folder is the thesis workspace.

Before doing anything else:
1. Read AGENTS.md fully. It has the project context, my background, how to talk to me, and hard rules.
2. Then read, in order: docs/status.md, docs/at-a-glance.md, docs/primer.md, docs/decisions.md, docs/timeline.md,
   docs/literature/novelty-check.md (summary section), and reference/copra-study.md.

Then reply with:
A. A 10-line summary of the study in plain language: what it is, the core research questions, what's novel,
   and what's already taken by prior work.
B. Where we are right now and what this week requires, as a checklist.
C. Anything in the docs that looks inconsistent, outdated, or risky. Be critical.
D. One question for me, if anything blocks you.

Rules for this session:
- Don't edit any files yet, except that you may fix obvious typos if you tell me.
- Don't invent sources or numbers; use the evidence tags in AGENTS.md.
- Explain jargon with analogies. I have a strong software engineering background but I'm not an ML expert.
- Be pragmatic and critical; don't flatter.
```

---

## 2. Every later session (paste at the start)

```
Read AGENTS.md and docs/status.md. Then tell me in 5 lines: where we are, what's next this week, and any blocker.
Today I want to: [describe the task].
At the end of the session, update docs/status.md (and docs/decisions.md if we decided anything).
```

---

## 3. Useful task prompts

**After the NCRC-V visit**
```
I visited NCRC-V. Here's what they said: [notes].
Fill in docs/meetings/2026-11-ncrc-v-visit.md, apply the go/no-go rule, record the decision in docs/decisions.md,
update docs/status.md, and draft what I should tell my adviser.
```

**Proof of concept (week 2)**
```
Help me build the week-2 proof of concept described in docs/timeline.md and docs/methodology/experiment-design.md,
following experiments/README.md. Start with reproducing the MTEB BelebeleRetrieval Cebuano BM25 number (0.784).
Write code in experiments/, test on 20 items first, and log results as JSONL.
```

**Drafting a proposal chapter**
```
Draft docs/proposal/ch2-review-of-literature.md from its outline. Cite only sources in docs/literature/sources.md,
keep evidence tags on claims, and use the safe novelty wording from docs/literature/novelty-check.md.
```

**Weekly review**
```
Compare docs/status.md and docs/timeline.md with what's actually done. Mark the week's statuses, list what slipped,
and propose how to recover without moving the Dec 18 defense.
```
