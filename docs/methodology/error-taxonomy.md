# Error Taxonomy Protocol (RQ3)

## Who does what

| Role | Person | Does |
|---|---|---|
| Researcher | Jamir | Collects errors, open coding, adjudication support; second coder only if no other Cebuano speaker is available |
| Linguist | `TBD` (VSU language/literature faculty) | Finalizes categories and codebook; labels errors (or a random 100); has the final say on disagreements |

No external SRC member is required by the department; the linguist strengthens validity.

## Inputs

- **Explanation run:** 200 Cebuano Belebele questions; model writes a 1–2 sentence reason, then the letter; at Q8_0 and Q2_K.
- **Tatoeba ceb→eng translations** at Q8_0 and Q2_K (sample).
- Sample 200–300 wrong outputs, stratified by level and model.

## Steps

*Revised 2026-11-20 (proposed; confirm with Jamir and the adviser). Why and sources: `reference/reports/2026-11-20 RQ3 standardized error taxonomy brief.md`.*

1. **Automatic layer (no human judgment):** language ID on every output line with GlotLID (line-level pass rate,
   after Marchisio et al. 2024) → "answered in Tagalog" / "fell back to English"; parser → "instruction failure". `VERIFY` GlotLID covers `ceb_Latn`.
2. **Deductive start:** starter codebook from published typologies: MQM Accuracy vs Fluency; intrinsic vs extrinsic
   hallucination (Maynez et al. 2020); reasoning–answer misalignment (Ovalle et al. 2025). Linguist reviews it.
3. **Inductive rounds (hybrid coding, Fereday & Muir-Cochrane 2006):** Jamir open-codes batches of 30 errors; the linguist
   adds or merges Cebuano-specific categories. Stop when a full batch adds no new category; write the ending conditions
   down (Nickerson et al. 2013): categories don't overlap, every error fits one, the set is concise.
4. **Pilot:** two coders label 30 items blind; compare; refine definitions. Pilot items are excluded from the agreement score.
5. **Reliability:** two coders label 100 **fresh** items independently, with **model and quantization level hidden**.
   Second coder: a Cebuano speaker other than Jamir if possible (`TBD`); otherwise Jamir, stated as a limitation.
   Report Krippendorff's alpha (or Cohen's kappa) overall and per category, before resolution. Pre-set thresholds in
   chapter 3: α ≥ 0.800 reliable, 0.667–0.800 tentative, < 0.667 merge or redefine the category. `TBD` with adviser.
6. **Resolution:** the linguist's label wins on disagreements.
7. **Analysis:** category shares by quantization level, with intervals; no strong claims for rare categories.

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

**Added from Lab 1 (2026-11-22; seen in free writing, to test on the real outputs):**

| Category | Example from Lab 1 |
|---|---|
| Repetition loop / degenerate output | Same phrase repeated until the token limit ("*Pag-susi sa Pag-susi…*") |
| Other-language intrusion (not Tagalog or English) | *Aquí* (Spanish) inside a Cebuano answer |
| Meaning inversion | "Preparing is not very important" when the point was the opposite |
| Wrong word sense / wrong word choice | *bulad* (dried fish) for belongings; pigs or rats listed as pets |
| Invented word | *nanggagahom*, *natinagpangan* |
| Lost local knowledge | Philippine agencies (PAGASA) replaced by US ones at Q2_K |

Lab 1 also suggests **capping answer length** in the RQ3 explanation run and preferring models above the floor, or
many RQ3 outputs will be loops. Source: `../labs/lab-01-run-a-local-model.md`.

## Logistics

- Prepare a spreadsheet: item ID, language, passage, question, output, gold, auto language-ID flag, Jamir's note, coder 1 label, coder 2 label. Keep model and level in a separate key file until labeling is done.
- Budget the linguist's time: ~1 hour codebook session + ~2–3 hours labeling + ~1 hour pilot (estimate); second coder ~3–4 hours. Acknowledge in the thesis.
