# VW Passat B8 — front set 01 (2026-06-15): a second cabin for Resonalyze

Real-car measurements of a **VW Passat B8 sedan (LHD)** in the impulse-response JSON
[Resonalyze](https://github.com/DIMOSUS/Resonalyze) saves itself (format v7), so its Virtual DSP,
Auto delay and Auto crossover can run on them directly — offered in
[DIMOSUS/Resonalyze#86](https://github.com/DIMOSUS/Resonalyze/issues/86) (item 6) and built with
[autosound-tuning-skill](https://github.com/ayukhno/autosound-tuning-skill)'s
`rew_tool/resonalyze_ir.py` from a REW session with a physical loopback.

**License: CC BY 4.0** (repository `LICENSE`). Attribution: *autosound-measurements (ayukhno), CC BY 4.0*. The car and the rig in detail: [`../CAR.md`](../CAR.md).

## The car and the rig

- Three-way active front + sub + a dash centre: sealed-box **subwoofer** in the trunk (`sw`),
  **door woofers** (`w_L`, `w_R`), **A-pillar mids** (`m_L`, `m_R`), **tweeters** (`tw_L`, `tw_R`),
  **centre** on the dash (`c`). Rear fill exists but was measured on a different time base
  (7.7 ms timing offset) and is **not** in this package.
- Processor: **Helix DSP Ultra S**, 96 kHz. Every driver on its own DSP output.
- Measurement: **REW 5.40 β128** (June 2026), exponential sweep 20 Hz – 20 kHz, one sweep per
  channel, 256k samples (2.731 s) at 96 kHz, output channel L; **Behringer ECM8000** on a
  **Focusrite Scarlett 2i2 4th gen** with a physical loopback (output R → input 2) as REW's timing
  reference — the same rig your README describes. Mic at the driver's listening position.
- Measured **2026-06-15**, set `_01`: every driver played "clean" — no EQ, no delay, no crossover on
  the DSP — **except the protective high-passes the physics demands**: mids and centre 100 Hz LR24,
  tweeters 1 kHz LR24 (see below). Woofers and sub had no filter.
- The moving-mic RTA of each channel (`rta-mmm/`) was taken the same day (65536-point 1/48-oct RTA,
  Hann, 150 averages, mic moved over the listening area) — the magnitude view the tune was made with.

## What is in the box

| path | what |
|---|---|
| `ir-v7/<ch>.json` | the transfer impulse responses **as REW measured them** (protective HPFs still in the signal) |
| `ir-v7-compensated/<ch>.json` | the same with the protective HPF **removed by Resonalyze's own `ProtectiveHighPassCompensation`** — open these for alignment/crossover work; `sw`, `w_L`, `w_R` are byte-identical to `ir-v7/` |
| `rta-mmm/<ch>.txt` | moving-mic RTA magnitude, `freq_Hz<TAB>SPL_dB`, 1/48-oct native resolution, REW's SPL calibration |
| `dsp-state.json` | the DSP states to score against (below) |
| `manifest.json` | every number behind every file: REW title/uuid/date, `startTime`, REW's own delay, peak dBFS, the fractional shift, the HPF and the compensation record |

Every IR file also carries a `rewSource` block with the same provenance; Resonalyze's reader
ignores it.

### The eight channels

| file | REW title | REW delay, ms | transfer peak index | IR peak, dBFS | protective HPF | index of t = 0 in REW's buffer |
|---|---|---|---|---|---|---|
| `sw` | sw_01 (sw) | 9.6691 | 928 | -67.13 | — | 95072.000 |
| `w_L` | w-L_01 (sw) | 4.7788 | 459 | -49.36 | — | 95541.000 |
| `w_R` | w-R_01 (sw) | 4.9762 | 478 | -45.14 | — | 95522.000 |
| `m_L` | m-L_01 (sw) | 2.9066 | 279 | -29.14 | 100.0 Hz LR24 | 95720.967 |
| `m_R` | m-R_01 (sw) | 4.1241 | 396 | -29.13 | 100.0 Hz LR24 | 95604.082 |
| `tw_L` | tw-L_01 (sw) | 2.9813 | 286 | -28.62 | 1000.0 Hz LR24 | 95713.793 |
| `tw_R` | tw-R_01 (sw) | 4.1727 | 401 | -29.60 | 1000.0 Hz LR24 | 95599.417 |
| `c` | c_01 (sw) | 3.8638 | 371 | -37.21 | 100.0 Hz LR24 | 95629.073 |

## How the files were made — and checked

- **Time base.** Sample 0 of `transferRealSamples` is the loopback reference, as in every file
  Resonalyze writes. REW anchors its buffer on the mic-IR peak (an integer sample) and lets t = 0
  fall at a fractional index (last column above), so the transfer IR was rotated by the exact
  fraction with a linear-phase FFT shift — nothing was rounded (0.5 sample = 5 µs = 1.8 mm at
  96 kHz). REW's ~1 s of pre-roll (Farina harmonic images) wraps to the tail of the buffer, as your
  H1 estimator's own negative lags do. `sweepDeconvolutionRealSamples` is REW's buffer as served
  (peak at index 96000 = 1.000 s in), `sweepDeconvolutionPeakIndex` points at it.
- **Level.** REW's IR endpoint peak-normalises by default; these files were pulled with
  `normalised=false` and carry **fractions of full scale**, so the level relation between channels is
  the measured one (a sub's IR peak really is 18 dB under a woofer's). Same mic gain and same
  sweep level for all eight. No SPL calibration block: REW's SPL calibration lives in the RTA
  files (dB SPL), not in the IRs.
- **Format.** Written to `ImpulseResponseFile` v7 as of Resonalyze commit d11186e; each document
  passed a port of `Validate()`, and then all sixteen files were loaded through **your reader
  compiled verbatim** (`ImpulseResponseFile.LoadAsync`, app-side, with the audio/app types it
  mentions stubbed) and read back with `Resonalyze.Dsp.TimeAlignmentAnalysis`: on the mids and
  tweeters its full-band first arrival matches REW's own delay to within 0.01 ms; the woofer and
  sub reads are your estimator's opinion of an onset that leads the peak (they agree with what the
  same code said on the same data in our cross-check harness).
- **Compensation.** `ir-v7-compensated/` = `ProtectiveHighPassCompensation.RemoveFromImpulseResponse`
  (`maximumBoostDb` 40, the call `ExpSweepMeasurement.ApplyAverageResult` makes at capture time),
  peak re-found the way it does for a synchronized loopback, saved through your `SaveAsync`, then
  re-packed compactly with the provenance block restored. Removing the 1 kHz LR24 moves the tweeter
  arrivals 3 samples (31 µs) earlier — its group delay. Below the corner the compensated IRs
  carry amplified noise (your reliability mask is what should gate it); the raw files are there
  for anything that wants the untouched signal.
- **Not carried:** transfer coherence (REW computes none for a sweep), level meters, audio-session
  diagnostics. Sweep duration is inferred from the IR length (REW keeps IR = sweep length).

## DSP states to score against

Delays in ms (positive = plays later), Helix filter families (LR = Linkwitz-Riley, BW = Butterworth,
number = dB/oct), PEQ in `dsp-state.json` (RBJ Q; LS/HS = Helix LS_Q/HS_Q shelves). Both states were
reached on these very `_01` measurements plus the ear.

**v1 — the first attested hardware state (2026-07-12).** Delays and polarity computed with our
joint-phase method and accepted by ear; crossovers from the acoustic plan (junctions 70 / 320 / 3500 Hz).

| channel | HPF | LPF | polarity | delay ms | gain dB | all-pass |
|---|---|---|---|---|---|---|
| sw | — | 88 Hz BW36 | normal | 0.0 | n/a | — |
| w_L | 86 Hz LR12 | 215 Hz LR12 | normal | 3.69 | n/a | — |
| w_R | 86 Hz LR12 | 215 Hz LR12 | normal | 3.69 | n/a | — |
| m_L | 460 Hz BW24 | 2000 Hz LR12 | inverted | 3.12 | n/a | — |
| m_R | 460 Hz BW24 | 2000 Hz LR12 | inverted | 2.71 | n/a | — |
| tw_L | 3625 Hz BW24 | — | inverted | 2.27 | n/a | — |
| tw_R | 3625 Hz BW24 | — | inverted | 1.44 | n/a | — |

**Current — preset SQ v10.7 (2026-08-18), output layer, verified by the owner against the PC-Tool.**
Virtual-channel layer at defaults; PEQ banks and the two tweeter all-passes in `dsp-state.json`.

| channel | HPF | LPF | polarity | delay ms | gain dB | all-pass |
|---|---|---|---|---|---|---|
| sw | — | 88 Hz BW36 | normal | 0.0 | 0.0 | — |
| w_L | 92 Hz LR12 | 215 Hz LR12 | normal | 4.33 | -0.3 | — |
| w_R | 92 Hz LR12 | 215 Hz LR12 | normal | 3.05 | 0.6 | — |
| m_L | 460 Hz BW24 | 2000 Hz LR12 | inverted | 3.4 | -3.5 | — |
| m_R | 460 Hz BW24 | 2000 Hz LR12 | inverted | 2.13 | 0.9 | — |
| tw_L | 3625 Hz BW24 | — | inverted | 2.49 | -5.8 | AP2 2600 Hz Q 1.0 |
| tw_R | 3625 Hz BW24 | — | inverted | 1.25 | -4.2 | AP2 4220 Hz Q 0.63 |
| c | 714 Hz LR24 | 1897 Hz LR24 | normal | 1.95 | -8.5 | — |

Known open point in this state: our joint-phase reading shows a **cancellation around 117 Hz at the
left sub/woofer junction**; a fix is being tested in the car (sub LPF 88 Hz BW36 → LR24, or the sub
polarity flip your Auto delay proposes). So "current" is a live tune, not a final answer — v1 is the
attested reference, current is where the ear has got to.

## Caveats, honestly

- One sweep per channel (no averaging); SNR per REW 34–51 dB.
- The mic calibration (ECM8000 0°/90° files, [`mics/behringer-ecm8000`](../../../mics/behringer-ecm8000/)) is **not** applied to the IRs; REW's curves carry it.
- The centre channel is a dash driver with its own protective 100 Hz LR24; its "IR start" reads oddly
  after compensation (amplified LF noise) — see above.
- Rear channels are not on this time base and are omitted.

## Reproducing

Converter: `autosound-tuning-skill/skills/autosound-tuning/rew_tool/resonalyze_ir.py` (with
`--selftest`; the REW facts it rests on are in the skill's `rew-api-quirks.md`). The verification
harness (Resonalyze's reader compiled verbatim + its DSP diagnostics, and the compensation pass) and
the build script live in the owner's tuning-research repository; `manifest.json` records every
input and output of the build.

Questions, or a different form (WAV, text IR, more channels/sessions): ayukhno@gmail.com or
[DIMOSUS/Resonalyze#86](https://github.com/DIMOSUS/Resonalyze/issues/86).
