# VW Passat B8 — MMM RTA level check, 2026-08-24

Eleven moving-microphone RTA captures taken in one sitting: each of the seven front drivers alone,
then three sums. The set exists to answer one question — **what each channel actually contributes at
the listening position** — and not to describe timing: an RTA carries no phase and no impulse
response, so nothing here can be used for delay, polarity or crossover work.

## The state of the car

The processor held the **"levels only"** variant of the Resonalyze plan for this cabin: the crossover
structure and the PEQ of the plan, the image aimed with level alone (left side −2 dB midbass,
−4 dB midrange, −4 dB tweeter; scene offset 0 ms), as opposed to the "levels and delay" variant that
aims it with 0.25 ms of scene offset and only −1 dB of level.

The measured left/right difference below is consistent with exactly that, which is the set's own
check that the plan was really loaded — see the last section.

## The rig

- **Car:** VW Passat B8 sedan, LHD. Drivers and amplifiers: [`../CAR.md`](../CAR.md).
- **Microphone:** Behringer ECM8000, **moved through the listening area** during the averaging (MMM).
  No microphone calibration file is applied to these curves.
- **Interface and SPL:** Focusrite Scarlett 2i2 4th gen. REW's SPL calibration was in force —
  `splOffsetdB` = 102.3415, the same calibration the 2026-08-20 set carries.
- **REW 5.40 Beta 132**, 65536-point **1/48 octave RTA**, Hann window, **no smoothing**,
  **150 averages** per capture. 10:18–10:25 local, one capture roughly every 30–45 s.

## The files

[`rta-mmm/`](rta-mmm/) — one tab-separated curve per capture, `freq_Hz  SPL_dB`, `#` comment lines,
the same layout as the [2026-06-15 set](../2026-06-15_front-set-01/rta-mmm/). 1286 points each,
4.39 Hz to 47.0 kHz, 96 points per octave, unsmoothed. Resonalyze imports this directly — as an
overlay curve ("Import from text…") or as the EQ Wizard's measured curve.

Per-capture provenance — REW id, uuid, timestamp, the notes REW wrote, and the level figures below —
is in [`manifest.json`](manifest.json).

| capture | what it is | dB C | dB A | 22 Hz–22 kHz unweighted |
|---|---|---:|---:|---:|
| `sw` | subwoofer | 80.8 | 47.1 | 81.9 |
| `w_L` | midbass left | 75.4 | 62.7 | 75.7 |
| `w_R` | midbass right | 77.5 | 62.7 | 77.9 |
| `m_L` | midrange left | 71.5 | 71.8 | 71.7 |
| `m_R` | midrange right | 75.3 | 75.3 | 75.4 |
| `tw_L` | tweeter left | 65.8 | 67.6 | 68.4 |
| `tw_R` | tweeter right | 69.5 | 71.4 | 72.0 |
| `sum_sw_w` | subwoofer + both midbasses | 84.6 | 66.9 | 85.3 |
| `sum_L` | whole left side | 77.3 | 73.4 | 77.7 |
| `sum_R` | whole right side | 79.8 | 76.8 | 80.3 |
| `sum_all` | everything | 85.4 | 78.5 | 86.0 |

## What the level table says, and what it does not

Right minus left, per driver pair, in dB C: **midbass +2.1, midrange +3.8, tweeter +3.7**. The plan
loaded at capture time attenuates the left side by **2, 4 and 4 dB** on those same three pairs. The
measured differences reproduce the applied cuts to within 0.3 dB.

One thing follows: the plan really was in the processor at capture time — the set carries its own
proof of its own premise.

The tempting second conclusion — that the pairs would therefore be balanced at the microphone with
the cuts taken back out — is **not** supported by these numbers alone. The plan's PEQ is not
symmetric between the sides (8 bands left against 7 on the midranges, 10 against 13 on the
tweeters), and broadband level moves with EQ as well as with gain. The agreement is close enough to
be worth noticing and not close enough to be read as a measurement of driver balance.

Nor does anything here say which of the two variants is the better one to listen to. That is an ear
question, and the answer is not in an RTA.

## What is not recorded here

The volume the car was set to, the path the microphone travelled and how long each pass took, the
seat position, and whether the doors were closed. Treat the absolute SPL figures as a matched set
that compares within itself, not as an absolute room level.

Licence: CC BY 4.0, as the rest of this repository.
