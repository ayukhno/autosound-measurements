# VW Passat B8 — front set _02, 2026-08-20

Eight front channels measured from scratch in one sitting, **by two independent programs**, in a
processor state that is written down rather than remembered. It supersedes
[`2026-06-15_front-set-01`](../2026-06-15_front-set-01/) for analysis: that set was taken with the
microphone in the owner's hand and with channel gains that were never recorded, and this one was
taken to remove both unknowns.

## What is different from the June set, and why it matters

- **The microphone stood on a tripod.** The June set — and every session before this one — was
  captured hand-held. Repeat captures taken here to measure it show what that cost: hand-held, two
  measurements 25 s apart differed by **0.9–2.4 dB RMS** over 100 Hz–16 kHz and their arrival times
  wandered by ±2 samples, drifting 5 samples (18 mm of path) over fifteen minutes. On the tripod the
  same repeats agree to **0.18–0.25 dB RMS** and **0.09 samples**. Any inter-channel timing taken
  from a hand-held set carries a few samples of position noise that no algorithm can see.
- **The processor was cleared and the state written out** — see [`dsp-state.json`](dsp-state.json):
  no EQ, no delay, no crossover, all gains at unity, all-pass off, RTC off, and only the protective
  high-passes the drivers need. Unity gain was chosen because it can be reproduced from one line of
  description; the June gains cannot be reconstructed at all.
- **Both programs measured the same cabin minutes apart**, with the microphone, the interface gain
  and the processor untouched between them.
- **Coherence exists** for every channel, from Resonalyze's four averaged runs. A REW sweep does not
  produce one.

## The rig

- **Car:** VW Passat B8 sedan, LHD. Drivers and amplifiers: [`../CAR.md`](../CAR.md).
- **Microphone:** Behringer ECM8000 on a tripod at the position the centre of the driver's head
  occupies in normal seating, capsule vertical (grazing incidence, so the **90°** calibration file is
  the right one for curves; impulse responses carry no calibration either way). The driver's seat and
  its backrest stayed in their normal position — **the operator sat in the passenger seat** and kept
  still through each capture.
- **Interface:** Focusrite Scarlett 2i2 4th gen, physical loopback (output R → input 2) as the timing
  reference for both programs. Input gain set once on the loudest channel and untouched from the
  first sweep to the last.
- **Block A — Resonalyze 4.x** (Windows 11 arm64 in a VM on the same Mac, Focusrite ASIO, 1024-sample
  buffer): exponential sweep 520 ms/octave (5.6715 s), 20 Hz–20 kHz requested, **4 runs averaged**,
  playback amplitude 0.5 = −9.03 dBFS RMS. 12:34–12:42 local.
- **Block B — REW 5.40 Beta 132** (macOS, Core Audio): 512k sweep, 20 Hz–20 kHz, **4 sweeps
  averaged**, **−9 dBFS** chosen to match Resonalyze exactly, output channel L. 13:50–13:56 local.

## The eight channels (block B, as published here)

| channel | first arrival, ms | IR peak, ms | SNR, dB | protective HPF | coherence 20–200 | 200 Hz–2 kHz | 2–16 kHz |
|---|---|---|---|---|---|---|---|
| `sw` | 6.5938 | 16.2144 | 33.1 | — | 0.997 | 0.691 | 0.106 |
| `w_L` | 3.3542 | 8.6203 | 44.3 | — | 0.997 | 1.000 | 0.970 |
| `w_R` | 4.5729 | 6.3914 | 44.0 | — | 0.999 | 0.993 | 0.952 |
| `m_L` | 2.5521 | 2.6186 | 55.3 | 100 Hz LR24 | 0.544 | 0.999 | 0.973 |
| `m_R` | 3.9271 | 3.9828 | 54.2 | 100 Hz LR24 | 0.569 | 1.000 | 0.979 |
| `tw_L` | 2.6146 | 2.6828 | 51.6 | 1000 Hz LR24 | 0.104 | 0.712 | 0.989 |
| `tw_R` | 3.9479 | 4.0094 | 51.0 | 1000 Hz LR24 | 0.090 | 0.660 | 0.988 |
| `c` | 3.3542 | 3.8245 | 50.1 | 100 Hz LR24 | 0.470 | 1.000 | 0.974 |

`sw`'s coherence collapses above 2 kHz and `tw_*`'s below 200 Hz for the same reason: there is no
signal there to be coherent about. Both mids and the centre sit behind a 100 Hz LR24, both tweeters
behind 1 kHz LR24; the coherence figures below those corners describe the noise floor, not the
measurement.

## The two programs agree

Same cabin, same microphone position, same processor state, forty minutes and one ventilation apart:

| channel | REW peak, ms | Resonalyze peak, ms | difference |
|---|---|---|---|
| `m_L` (control) | 2.6216 | 2.615 | 0.6 samples |
| `w_L` | 8.6203 | 8.615 | 0.5 |
| `m_L` (in set) | 2.6186 | 2.615 | 0.3 |
| `m_R` | 3.9828 | 3.979 | 0.4 |
| `tw_L` | 2.6828 | 2.677 | 0.6 |
| `tw_R` | 4.0094 | 4.010 | 0.1 |
| `sw` | 16.2144 | 16.323 | 6.4 |
| `m_L` (control, end) | 2.6150 | 2.604 | 1.1 |

Two channels are missing from that table on purpose. On **`w_R`** and **`c`** the two programs pick
*different peaks* — REW 6.3914 ms against Resonalyze 4.792 for `w_R`, REW 3.8245 against 4.208 for
`c` — while their **first arrivals agree** (4.573 / 4.656 and 3.354 / 3.396). Those two impulse
responses have two nearly equal maxima, and which one wins is a coin toss. Anything that keys
alignment to "the peak" will flip between them.

## What the cabin does to the two door woofers

Near-field captures of both woofers (7 cm from the grille, on axis) say the **drivers are a matched
pair**: 1.55 dB RMS apart over 40 Hz–2 kHz once a 1.8 dB level difference is removed. In the car,
from the listening position, they are not remotely the same thing. In-car minus near-field,
normalised at 40–80 Hz:

| Hz | left | right |
|---|---|---|
| 100 | **+9.9** | −2.8 |
| 125 | +6.3 | −2.0 |
| 160 | **−8.9** | −1.3 |
| 250 | +1.7 | −11.0 |
| 315 | +2.6 | −11.1 |
| 400 | +0.7 | **−19.0** |
| 630 | +1.9 | −14.2 |
| 1000 | −1.0 | −9.1 |

The left door — the near one, beside the listening position — is dominated by a boundary/modal pair:
**+10 dB at 100–125 Hz and −9 dB at 160 Hz**, nineteen decibels of swing inside half an octave. The
right door, across the cabin behind the console and the occupant, is flat at the bottom and shelved
down by 9–19 dB from 250 Hz up. Two identical drivers, mirrored positions, one cabin.

That is worth stating plainly because it is the kind of asymmetry that makes an automatic tuner
produce nonsense on this car while working elsewhere: the two channels that a stereo algorithm
expects to be each other's mirror are, acoustically, different systems.

## Temperature drift, and how to remove it

Cabin air temperature moves the arrival of every channel, in proportion to its acoustic path: 0.43
samples per degree on a 0.9 m path at 96 kHz. Each block therefore carries **three `m_L` captures** —
one before, one in its own slot, one after — and the drift between them is the block's own
thermometer.

- Block A drifted **+1.09 samples** over 445 s (the cabin was still warming after ventilation).
- Block B drifted **−0.64 samples** over 277 s, forty minutes later, as it cooled.

`manifest.json` → `drift.blockB_REW.perChannel` carries the correction for every channel, computed
from the controls and scaled by that channel's own acoustic path (its first arrival minus the 0.44 ms
of electronic latency the near-field capture reveals). **It is not applied to the files** — the
impulse responses here are as measured. Applying it is a fractional, linear-phase rotation.

Ventilating between captures makes this worse, not better: opening the doors starts the steepest part
of the transient. The controls exist so that a block taken in a warming cabin is still usable.

## What is in the box

| path | what |
|---|---|
| `ir-v7/<channel>.json` | the transfer impulse responses, Resonalyze IR JSON v7, sample 0 = the loopback reference, converted from REW by [`rew_tool/resonalyze_ir.py`](https://github.com/ayukhno/autosound-tuning-skill) |
| `ir-v7/m_L-ctl1.json`, `m_L-ctl3.json` | the drift controls |
| `ir-v7/w_L-nf.json`, `w_R-nf.json` | the near-field captures |
| `ir-v7/w_R-retake.json` | `w_R` measured again 12 minutes later, see the caveat below |
| `coherence/<channel>.txt` | Resonalyze's transfer coherence from block A, 1/48-octave band means |
| `block-a-resonalyze.json` | block A per channel: capture levels, peak, accepted runs, coherence summaries |
| `dsp-state.json` | the processor state everything was measured in |
| `manifest.json` | every number behind every file, the drift table, the near-field and level notes |

**Deliberately absent:** no moving-mic RTA this time (this session was about impulse responses), and
no protective-HPF-compensated copy — the high-passes are declared per channel in `manifest.json`, and
`Resonalyze.Dsp.ProtectiveHighPassCompensation` removes them in one call. The June set carries a
compensated copy if an example is wanted.

**Block A's own files** — Resonalyze's native v7, one per channel — are not in this repository: each
is about 95 MB, mostly a 2.1-million-sample transfer response and a 1-million-bin coherence array.
Ask if you want them; they are offered as a release asset rather than as repository content.

## Caveats, stated rather than discovered later

- **`w_R` in this block is not the calmest capture of that channel.** Measured again twelve minutes
  later (`w_R-retake`) it agrees within **0.19 dB RMS below 150 Hz and 0.46 dB to 500 Hz** — the band
  a door woofer actually works in — but differs by 1.3–3.0 dB RMS above 500 Hz, where a shift of the
  operator's torso moves the interference pattern. Use `w_R` for the set; use `w_R-retake` if
  something above 500 Hz depends on it.
- **The near-field captures were hand-held** — there was no way to mount the microphone at the cone
  that day. Their direct sound is 20 dB above everything else and both sides were captured
  identically, so the left/right comparison holds; treat them as valid below about 1 kHz.
- **The near-field level is not comparable** with the in-car captures: the sweep level was reduced for
  the short distance.
- The same ten channels were also captured at **0 dBFS**, nine decibels louder, and are in the REW
  file as `<channel> @0dBFS`. A back-to-back pair on `w_R` at the two levels differs by 0.17 dB RMS
  after removing the 9 dB, so the system is linear across that range; the louder block swept from
  9.89 Hz rather than 20 Hz.
- Microphone calibration is **not** in the impulse responses — it never is. The 90° file belongs to
  everything measured at the listening position, the 0° file to the near-field captures; see
  [`../../../mics/behringer-ecm8000`](../../../mics/behringer-ecm8000/).
