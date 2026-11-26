# Kickstart Prompts

Use these in Claude Desktop with this folder (`project-sidapa/`) as the working folder.

---

## 1. First session (paste once)

```
You're helping me with my undergraduate CS thesis. This folder is the thesis workspace.

Before doing anything else:
1. Read AGENTS.md fully.
2. Then read docs/status.md, docs/primer.md and docs/context-checklist.md.

Then reply with:
A. A 5-line summary of the study as the repo describes it.
B. Which checklist items you need from me first, and why.
C. Anything that looks inconsistent or risky. Be critical.
```

---

## 2. Every later session (paste at the start)

```
Read AGENTS.md and docs/status.md. Then tell me in 5 lines: where we are, what's next this week, and any blocker.
Today I want to: [describe the task].
At the end of the session, update docs/status.md (and docs/decisions.md if we decided anything).
```

---

## 3. Handing over context

```
Process context-checklist item [N]. Here it is: [paste or attach].
```

**Weekly review**
```
Compare docs/status.md with what's actually done. Mark the week's statuses, list what slipped,
and propose how to recover without moving the Dec 18 defense.
```
