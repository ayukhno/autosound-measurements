# VW Passat B8 — sedan, left-hand drive

A three-way active front with a dash centre and a trunk sub, tuned for SQ competition (EMMA /
AYA classes) with the [autosound-tuning-skill](https://github.com/ayukhno/autosound-tuning-skill)
method: loopback sweeps for timing and phase, moving-mic RTA for voicing, one change at a time,
the ear as the last judge.

## Install

| DSP output | channel | driver / placement | amplifier |
|---|---|---|---|
| C / D | `w_L` / `w_R` | door woofers, treated doors, stock locations | Ground Zero GZA 125.4 |
| E / F | `m_L` / `m_R` | midranges, A-pillars, bottom on the dash; L aimed at the centre, R at the driver | Ground Zero GZPA 4SQ |
| G / H | `tw_L` / `tw_R` | tweeters, A-pillars above the mids (+2 cm depth); L aimed at the centre, R at the driver | Ground Zero GZPA 4SQ |
| B | `c` | centre, dash | — |
| K | `sw` | subwoofer in a sealed 35 l box in the trunk | Audison SR 1.500 |
| (I / J) | `r_L` / `r_R` | rear fill — not in the published sets (measured on a different time base) | — |

- **Processor:** Helix DSP Ultra S, 96 kHz native; two processing layers (virtual channels + outputs).
- **Source:** Isudar T72X head unit → S/PDIF optical → DSP; for measurements REW plays through the
  interface into the DSP's digital input (output channel L; the interface's output R is the loopback).

## Measurement rig

- **Mic:** Behringer ECM8000 with the owner's own 0° / 90° calibration files ([`mics/behringer-ecm8000`](../../mics/behringer-ecm8000/)).
- **Interface:** Focusrite Scarlett 2i2 4th gen; **physical loopback** (XLR, output R → input 2) as
  REW's timing reference — every sweep on one absolute time base.
- **Software:** REW 5.40 (beta), API on; the skill's `rew_tool/` for analysis. From the 2026-08-20
  session onward, Resonalyze is used as a second, independent measurement program on the same rig.
- Sweeps at the driver's listening position; moving-mic RTA over the listening area, 150 averages.

### Where the microphone is, and who is in the car

Stated because it is half of what a response means, and because it changed between sessions:

- **From 2026-08-20:** microphone on a **tripod**, capsule vertical, at the point the centre of the
  driver's head occupies in normal seating. The driver's seat and its backrest stay in their normal
  position and **the operator sits in the passenger seat**, still, through each capture. Calibration:
  the **90°** (grazing) file for anything at the listening position, the **0°** file for near-field.
- **Before that, including the 2026-06-15 set:** the microphone was **hand-held** at the same point,
  the operator in the driver's seat with the seat slid back. Repeat captures measured on 2026-08-20
  put a number on what that costs — 0.9–2.4 dB RMS between takes 25 s apart and ±2 samples of arrival
  wander, against 0.2 dB and 0.09 samples on the tripod — so inter-channel timing from the earlier
  sets carries a few samples of position noise.

## Sessions

| session | what | notes |
|---|---|---|
| [`2026-06-15_front-set-01`](2026-06-15_front-set-01/) | the eight front channels, per-driver loopback sweeps + moving-mic RTA, two DSP states | drivers "clean" except protective HPF (mids/centre 100 Hz LR24, tweeters 1 kHz LR24) |
| [`2026-08-20_front-set-02`](2026-08-20_front-set-02/) | the eight front channels again, measured **twice** — in Resonalyze and in REW, minutes apart on one microphone position — plus near-field of both door woofers and per-block drift controls | processor cleared and written out (`dsp-state.json`): no EQ, no delay, no crossover, unity gains, RTC off, protective HPFs only. Microphone on a tripod. Supersedes the June set for analysis |
