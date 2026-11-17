# The Parked Copra Study

*Background only. This was the researcher's previous, already-defended thesis. It is parked pending the NCRC-V reality check.*

## What it was

"Mobile-Based Copra Visual Quality Classifier Using a Hybrid Computer Vision and Rule-Based Framework" (outline, May 2026),
revised by a primer (Nov 14, 2026). A phone app that grades one copra piece:

1. **Moisture gate:** user types the buyer's meter reading; ≥14% → Rejected (PCA AO No. 02 s. 2003); brackets from PNS/BAFPS 43:2009.
2. **Perception:** yolo26n-seg instance segmentation outlines clean_endosperm, surface_mold, tapahan_charring, insect_damage.
3. **Rules:** defect share per class → visual grade; final grade = worse of moisture and visual grade; plain-language explanation.
4. Offline Flutter app (ONNX Runtime). Evaluation: mask IoU/mAP, accuracy, weighted kappa vs reference grades, oracle vs end-to-end, ISO/IEC 25010 user testing (~30 respondents).

Closest prior work: Elecito et al. (2025), Southern Leyte State University, YOLOv11 detection, company A/B/C grades, 93.65% on 126 test images.

## Why it is parked

| Dependency | Status (Nov 2026) |
|---|---|
| Expert to set **every** rule threshold (standards only give lot-level limits) | None secured |
| 600–800 field photos + polygon annotation | No samples, no station access |
| Trader graders for reference grades; ~30 user-test respondents; ethics clearance | Not started |
| Phone camera for capture; 2–3 phones for speed tests | Researcher lacks a good camera phone |
| Adviser fit | Adviser's expertise is NLP |
| Original constraint | Wanted minimal fieldwork |

The study is well designed but **dependent**: its quality is decided by people and access not yet secured. The Cebuano
study's quality is decided by the researcher's own work.

## What would revive it

NCRC-V commits, this week, (1) a named expert with a threshold session within ~2 weeks, and (2) access to graded samples or a buying station.
Then: keep copra (already defended), narrow scope to model + rules, app as demo.

## Script for the adviser (if switching)

> "I went back to NCRC-V with a questionnaire on my three hurdles: expert help, dataset availability and complexity.
> [What they said.] Without a committed expert and a source of samples, the copra study depends on things I can't secure
> in time. I'd like to switch to a study in your area: measuring how much small AI models lose in Cebuano when compressed
> to run offline, and whether Cebuano calibration helps. It uses only public data and runs on my laptop plus about $10 a month
> of cloud compute. Here's a one-page pitch."

## Source files

The researcher holds the original outline PDF and the primer PDF. Not stored here.
