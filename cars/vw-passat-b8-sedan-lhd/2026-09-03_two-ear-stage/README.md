# 2026-09-03 — two ears, one DSP

A session that asks a question rather than tunes a car: **can a per-channel DSP steer the
interaural cues a listener uses to place a stereo image?** It is published because the
answer came out **negative**, the prediction was **registered before the listening**, and
a negative result with its pre-registration is worth more to anyone building the same
mathematics than a success story would be.

The finding, written for the author of [Resonalyze](https://github.com/DIMOSUS/Resonalyze)
after his redirect to Geddes & Blind on `Resonalyze#91`, is
[`NOTE-to-resonalyze-author.md`](NOTE-to-resonalyze-author.md). Read that first — the rest
of this directory is what it stands on.

![Spread of the summed interaural cues across ear positions, by band](sigma-vs-band.png)

## What is in here

| file | what |
|---|---|
| [`NOTE-to-resonalyze-author.md`](NOTE-to-resonalyze-author.md) | the whole finding: rig, criteria, the model, the pre-registered prediction, the ear's verdict, our reading last and marked as ours |
| [`PREREG-vfr420-listening.md`](PREREG-vfr420-listening.md) | **the pre-registration** — the prediction and its refutation criteria, written before the listener heard anything, with the verdict appended and the Ukrainian original reproduced verbatim |
| [`criterion3-itd.json`](criterion3-itd.json) · [`criterion3-ild.json`](criterion3-ild.json) | the acceptance criteria, machine-readable: predicted against measured, per band, per ear |
| [`stage-picture-SQ.json`](stage-picture-SQ.json) | the band-by-band stage picture on the tuned preset |
| [`sigma-vs-band.png`](sigma-vs-band.png) · [`plot_sigma.py`](plot_sigma.py) | the chart above and the script that draws it |
| `stereobasis_research.mdat` | **the raw REW session**, 24.6 MB — 20 captures, needs REW 5.40+ to open. In-session name «дослідження стереобази.mdat»; sha256 `e3bc1bf572cbe4dad2a05beeb1d0a036ac09414dcd6cd3221f3846e74b4ae8fc` |

There is no `ir-v7/` here: this set is published as the raw session plus the derived
numbers, because the question it answers is about **pairs of positions**, and the
per-driver conversion the other sets use throws the pairing away.

## The rig

Tripod never moved. A ±45° arm carried **two microphone positions at ear locations**,
±9 cm from the head centre, and the pair was repeated at **three heights** (±7 cm) —
so every number here has a spread across ear positions, which is the whole point.

**There is no manikin.** Two bare microphones, no head, no pinnae. So an "interaural level
difference" in this set is cabin interference between two points 18 cm apart, not head
shadow plus pinna filtering — see §8 of the note, where we argue against ourselves with it.

**Sign convention: positive = toward the right.**

Two DSP states:

* `_57` — RAW baseline: all delays 0, crossovers off, EQ bypassed, protective high-passes
  only (`m` 100 Hz LR24, `tw` 1000 Hz LR24);
* `_58` — per-side sums on the tuned "SQ" preset.

Everything else about the cabin, the install and the microphone is in
[`../CAR.md`](../CAR.md). The aiming matters for reading this set: the left midrange and
tweeter point at the centre of the car, the right pair at the driver.

## Reading the JSON, if you do not read Ukrainian

The numbers are numbers; a few label strings are in Ukrainian. The full key:

| string | meaning |
|---|---|
| `"смугова взаємна кореляція з межею ±525 мкс (та сама, що в selftest)"` | band-wise cross-correlation with a ±525 µs search limit (18 cm / 343 m·s⁻¹), the same estimator the selftest uses |
| `"низ 300-800"` · `"серед 800-2k"` · `"верх 2-5k"` · `"най 5-10k"` | band names: low · mid · top · topmost |
| `"час"` · `"рівень"` | which cue dominates in that band: time · level |
| `"право"` · `"ліво"` · `"центр"` | the verdict for that band: right · left · centre |
| `"трохи"` · `"сильно"` | qualifier on that verdict: slightly · strongly (craft wording — see §8 of the note) |
| `"поза геометрією: інтерференція, не прихід"` | beyond geometry: the \|ITD\| exceeded the ±525 µs physical limit, so this is interference between the two points, not an arrival difference |
| `"образ розмитий, це не точка"` | the image is diffuse — not a point |
| `"позиція як частка між тим, що дає ліва сторона сама, і правою самою"` | position as a fraction between what the left side alone gives and what the right side alone gives |
| `"виміряні суми сторін _58 на двох вухах p2/p6, центр = їх сума"` | measured per-side sums `_58` at the two ear positions p2/p6; the centre is their sum |
| `"SQ, стан = зміст v_015 (= v_019), VFL ta 0, PK 3600 bypass"` | the preset this picture was taken on: the SQ tune, chain content `v_015` (identical to `v_019`), virtual-front-left time alignment 0, the 3600 Hz peaking band bypassed |
| `"ILD імунний до віртуального шару: VFL/VFR множать обидва вуха однаково"` | ILD is immune to the virtual layer: the virtual front L/R channels scale both ears alike, so they cancel in the ratio |

## The three acceptance criteria, all passed

Written down **before** the capture:

| checked | tolerance | result |
|---|---|---|
| rig repeatability, same position twice | ≤ 60 µs | **1.0 µs** |
| predicted vs measured, level (ILD) | ≤ 1.0 dB | **0.39 dB** |
| predicted vs measured, time (ITD) | ≤ 60 µs | **9 µs** |

An unplanned cross-check: impulse-response peaks **reconstructed from the prediction**
(6.083 / 6.344 / 6.312 / 5.885 ms) matched the **measured** ones (6.073 / 6.344 / 6.302 /
5.885 ms) to within 10 µs, with no fitting. The model is not in doubt in this set; what it
*means* is.

## Provenance and limits

One car, one seating position, one listener, one evening. Captured and analysed by the
project's `research` role; the listening was done by the car's owner against the AYA
competition evaluation disc. Between-session rig repeatability was **never measured** —
the arm was dismantled — and the σ figures come from **three** ear pairs, which is a weak
σ. The note names the rest of the holes itself, in §8.

Licence: **CC BY 4.0**, like every dataset here.
