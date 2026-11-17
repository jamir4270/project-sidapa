# Error Taxonomy Protocol (RQ3)

## Who does what

| Role | Person | Does |
|---|---|---|
| Researcher | Jamir | Collects errors, first-pass notes, double-labels 100 items blind |
| Linguist | `TBD` (VSU language/literature faculty) | Finalizes categories and codebook; labels errors (or a random 100); has the final say on disagreements |

No external SRC member is required by the department; the linguist strengthens validity.

## Inputs

- **Explanation run:** 200 Cebuano Belebele questions; model writes a 1–2 sentence reason, then the letter; at Q8_0 and Q2_K.
- **Tatoeba ceb→eng translations** at Q8_0 and Q2_K (sample).
- Sample 200–300 wrong outputs, stratified by level and model.

## Steps

1. **Open coding (Jamir):** a one-line note per error in your own words.
2. **Codebook (linguist):** group notes into 5–8 categories; one-page codebook with definition + one real example each.
3. **Labeling (linguist):** label all errors, or a random 100 if time is short (Jamir labels the rest using the codebook).
4. **Agreement:** Jamir labels the same 100 blind. Compute Cohen's kappa (`sklearn.metrics.cohen_kappa_score`). Target ≥ 0.6.
5. **Resolution:** disagreements → linguist's label wins. Report kappa before resolution.
6. **Analysis:** category shares by quantization level; which grow with compression.

## Starter categories (to test, not to impose)

| Category | Example |
|---|---|
| Answered in Tagalog | Reason written in Tagalog |
| Fell back to English | Reason or answer in English |
| Misread a Cebuano word | Wrong meaning for a common word |
| Morphology error | *mipalit* (bought) vs *gipalit* (was bought) confused |
| Named entity mangled | Name or place distorted |
| Hallucinated fact | Claim not in the passage |
| Instruction failure | No letter, extra text, wrong format |
| Right reasoning, wrong letter | Reason correct, letter mismatched |

## Logistics

- Prepare a spreadsheet: item ID, language, model, level, passage, question, output, gold, Jamir's note, linguist label, Jamir label.
- Budget the linguist's time: ~1 hour codebook session + ~2–3 hours labeling (estimate). Acknowledge in the thesis.
