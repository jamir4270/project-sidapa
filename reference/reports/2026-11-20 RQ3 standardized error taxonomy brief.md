# Research brief: making the RQ3 error taxonomy standardized and validated

*Quick-mode brief, 2026-11-20. Written with AI assistance (Claude, ARS deep-research quick mode). Sources were found by
web search; none of the full texts was opened in this session, so every source is tagged `VERIFY` until opened.*

## The question

RQ3 sorts the models' Cebuano mistakes into categories. Right now the categories come from Jamir's notes, and one
linguist finalizes them. A panel can call that subjective. Is there a standard or validated way to arrive at the
categories?

## Short answer

Yes, mostly. You can't make error categories perfectly objective, but you can make them **standard** (built on
published typologies, not invented from scratch), **systematic** (a published method for building a taxonomy, with
explicit stopping rules) and **reliable** (two people label independently and agree above a pre-set threshold).
Panels accept that combination. Some categories don't need human judgment at all: a program can measure them.

**Analogy:** doctors don't invent new disease names for each patient. They use a standard list (ICD), add a local
note when something doesn't fit, and a second doctor's diagnosis should match the first. Do the same with errors.

## Five methods to combine

### 1. Start from a published error typology, not a blank page (deductive start)

| Typology | What it is | What to borrow for RQ3 | Tag |
|---|---|---|---|
| **MQM (Multidimensional Quality Metrics)** | The standard error typology for translation quality, from the EU QTLaunchPad/QT21 projects; the WMT evaluations use it. Core dimensions include Accuracy, Fluency, Terminology, Style, Locale convention. Errors get minor/major/critical severity. | The top-level split: **Accuracy** (meaning wrong: mistranslation, addition, omission, untranslated) vs **Fluency** (form wrong: grammar, spelling, word form). Use it for the Tatoeba translations and the written reasons. | `VERIFY` ([W3C MQM group](https://www.w3.org/community/mqmcg); [Freitag et al. 2021, TACL](https://arxiv.org/abs/2104.14478)) |
| **Intrinsic vs extrinsic hallucination** (Maynez et al., ACL 2020) | Intrinsic = distorts what the passage says; extrinsic = adds what the passage doesn't say. | Split your "hallucinated fact" category into these two. Well-known and easy to define. | `VERIFY` ([arXiv 2005.00661](https://arxiv.org/abs/2005.00661)) |
| **Reasoning–answer misalignment** (Ovalle et al., 2025, EMNLP MRL workshop) | Taxonomy of cases where a model's written reasoning doesn't support its chosen option, across languages; misalignment is higher in lower-resource settings. | Grounds your "right reasoning, wrong letter" category in published work, and is the closest prior work to your explanation run. | `VERIFY` ([arXiv 2512.22712](https://arxiv.org/abs/2512.22712)) |
| **Scarecrow** (Dou et al., ACL 2022) | Ten error types for machine-written text (e.g., redundancy, incoherence, commonsense), built from expert analysis plus pilot rounds of crowd annotation. | A model of *how* to build a typology: expert draft → pilot annotation → revise. | `VERIFY` ([ACL 2022](https://aclanthology.org/2022.acl-long.501)) |

### 2. Add Cebuano-specific categories from the data (inductive step)

The published typologies are English- and translation-centred. They have no category for Cebuano verb-focus affixes
(*mi-* vs *gi-*) or Tagalog interference. Those should **emerge from the data**, with the linguist naming them.

The accepted name for "start from a template, then let new codes emerge" is **hybrid deductive–inductive coding**
(Fereday & Muir-Cochrane 2006, *International Journal of Qualitative Methods*) `VERIFY`
([DOI 10.1177/160940690600500107](https://journals.sagepub.com/doi/pdf/10.1177/160940690600500107)). Citing it turns
"I made up categories" into "I followed a documented hybrid coding method."

### 3. Use a published taxonomy-building method with stopping rules

**Nickerson, Varshney & Muntermann (2013)**, *European Journal of Information Systems* 22(3), 336–359, is the standard
method for building taxonomies in information systems research `VERIFY`
([RePEc](https://econpapers.repec.org/RePEc:taf:tjisxx:v:22:y:2013:i:3:p:336-359)). It alternates empirical-to-conceptual
rounds (group real examples) and conceptual-to-empirical rounds (derive categories from theory), and stops only when
**ending conditions** are met. These are objective ones (the taxonomy is valid, e.g. categories don't overlap and every
error fits somewhere) and subjective ones (it is useful: concise, explanatory). A 2021 update (Kundisch et al.,
*Business & Information Systems Engineering*) found that only 48% of published taxonomies reported their ending
conditions `VERIFY` ([Springer](https://link.springer.com/article/10.1007/s12599-021-00723-x)). Reporting yours is an
easy way to be more rigorous than most.

**Practical stopping rule (TBD with linguist):** code errors in batches of 30; stop adding categories when a whole batch
produces no new category (this is called saturation).

### 4. Let a program measure what it can (removes subjectivity entirely)

| Category | How to measure automatically | Tag |
|---|---|---|
| Answered in Tagalog / fell back to English | Run a language identifier line by line on each output. This is the **line-level pass rate** from Marchisio et al. 2024 ("Understanding and Mitigating Language Confusion in LLMs," EMNLP 2024), which used fastText. For Cebuano, use **GlotLID** (EMNLP 2023 Findings, 1,665 languages). | `VERIFY` ([arXiv 2406.20052](https://arxiv.org/abs/2406.20052); [GlotLID](https://arxiv.org/abs/2310.16248); confirm `ceb_Latn` is in GlotLID's label list) |
| Instruction failure (no letter, extra text) | Your answer parser already flags it | n/a |

Then the humans only label the categories that need judgment (meaning, morphology, hallucination). Fewer subjective
calls means a smaller target for the panel.

### 5. Prove reliability with two independent labelers

- **Two coders, labeling blind and independently.** Report agreement *before* discussing disagreements.
- **Metric:** Cohen's kappa (two coders) or **Krippendorff's alpha** (any number of coders; handles missing labels).
  Krippendorff's convention: α ≥ 0.800 = reliable; 0.667–0.800 = tentative conclusions only; below 0.667 = don't use
  `VERIFY` ([summary](https://en.wikipedia.org/wiki/Krippendorff%27s_alpha); original: Krippendorff, *Content Analysis*).
  **Fix the threshold in chapter 3 before you see the data.**
- **Report agreement per category,** not just overall; a weak category gets merged or redefined.
- **Practice guide to cite:** O'Connor & Joffe (2020), "Intercoder Reliability in Qualitative Research: Debates and
  Practical Guidelines," *IJQM* 19 `VERIFY` ([UCL Discovery](https://discovery.ucl.ac.uk/10091273/1/1609406919899220.pdf)).

## Three weak spots in the current protocol

| Weak spot | Why it matters | Fix |
|---|---|---|
| Jamir is the second coder | He wrote the open-coding notes, so he isn't independent; agreement looks better than it is | Get a **second Cebuano speaker** (another student or faculty member) to label the 100 blind. Jamir keeps the open coding and adjudication only. If no one is available, keep Jamir and state the limitation. |
| Coders can see the quantization level | A coder who knows an output came from Q2_K may expect worse errors (confirmation bias) | **Hide model and level** in the labeling sheet; reveal only at analysis time. |
| Agreement is measured on items used to build the codebook | It inflates agreement | **Pilot on 30 items, refine the codebook, then measure agreement on fresh items.** |

## Recommended protocol (replaces steps 1–5 in `docs/methodology/error-taxonomy.md`)

1. **Automatic layer:** language ID per line (GlotLID) + parse failures. No human judgment.
2. **Deductive start:** the linguist reviews a starter codebook built from MQM Accuracy/Fluency, intrinsic/extrinsic
   hallucination and reasoning–answer misalignment.
3. **Inductive rounds:** Jamir open-codes batches of 30; the linguist adds or merges Cebuano-specific categories;
   stop at saturation (Nickerson-style ending conditions, written down).
4. **Pilot:** both coders label 30 items blind, compare and refine the codebook.
5. **Reliability:** two coders label 100 *fresh* items blind (level hidden). Krippendorff's alpha overall and per
   category; pre-set target α ≥ 0.667 (tentative) / 0.800 (reliable). `TBD` with adviser.
6. **Resolution and analysis:** linguist adjudicates; category shares by quantization level, with intervals.

**Extra cost (estimate):** one pilot round (~1 hour each for two coders) and a second coder's ~2–3 hours. Same timeline
weeks (15–18).

## What this does *not* fix

- Categories are still human judgments; this makes them **defensible and reliable**, not "objective."
- Sample sizes per category will be small (200–300 errors split 6–8 ways); report shares with intervals and avoid
  strong claims about rare categories.
- None of these sources was opened in this session. Open each before citing it in chapter 2 or 3.

## Sources

- W3C MQM Community Group — https://www.w3.org/community/mqmcg
- Freitag et al. 2021, "Experts, Errors, and Context," TACL — https://arxiv.org/abs/2104.14478
- Kocmi et al. 2024, "Error Span Annotation," WMT — https://aclanthology.org/2024.wmt-1.131 (lighter alternative to MQM)
- Maynez et al. 2020, ACL — https://arxiv.org/abs/2005.00661
- Ovalle et al. 2025, "Beg to Differ" — https://arxiv.org/abs/2512.22712
- Dou et al. 2022, "Scarecrow," ACL — https://aclanthology.org/2022.acl-long.501
- Fereday & Muir-Cochrane 2006, IJQM — https://journals.sagepub.com/doi/pdf/10.1177/160940690600500107
- Nickerson et al. 2013, EJIS — https://econpapers.repec.org/RePEc:taf:tjisxx:v:22:y:2013:i:3:p:336-359
- Kundisch et al. 2021, BISE — https://link.springer.com/article/10.1007/s12599-021-00723-x
- Marchisio et al. 2024, "Language Confusion," EMNLP — https://arxiv.org/abs/2406.20052
- Kargaran et al. 2023, GlotLID — https://arxiv.org/abs/2310.16248
- Krippendorff's alpha thresholds — https://en.wikipedia.org/wiki/Krippendorff%27s_alpha
- O'Connor & Joffe 2020, IJQM — https://discovery.ucl.ac.uk/10091273/1/1609406919899220.pdf
