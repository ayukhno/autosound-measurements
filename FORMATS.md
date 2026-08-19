# Formats

Everything here is plain text a human can open. The time-base and level conventions are the
point of the repository, so they are spelled out per format.

## Resonalyze impulse-response JSON (format v7) — `ir-v7/`, `ir-v7-compensated/`, `hardware/**/measurements/`

The file [Resonalyze](https://github.com/DIMOSUS/Resonalyze) saves for one measured channel
(`source/Measurements/ImpulseResponseFile.cs`, `"format": "resonalyze-impulse-response"`,
`"version": 7`). Opens directly in Resonalyze (Impulse Response mode, Virtual DSP panel). For
everyone else, the three members that matter:

| member | meaning |
|---|---|
| `sampleRate` | Hz (integer) |
| `transferRealSamples` | the **transfer impulse response**: **sample 0 is the loopback reference (t = 0)**, sample *i* is at *i / sampleRate*; negative time (REW's pre-roll with the harmonic-distortion images) wraps to the **tail** of the buffer, as in Resonalyze's own circular H1 estimate. Amplitude: **fraction of full scale** of the recording chain — relative levels between the channels of one set are the measured ones |
| `transferPeakIndex` | index of the largest |sample| of the transfer IR |

Also present: `sweepDeconvolutionRealSamples` / `sweepDeconvolutionPeakIndex` (REW's buffer as
served, peak deep inside — what Resonalyze's raw deconvolution looks like), `lowFrequencyHz` /
`highFrequencyHz` (the sweep band), `sweepDurationSeconds`, `bits`, `playChannel`,
`measurementMode: LoopbackTransfer`, `timingReference: SynchronizedLoopback`, and a **`rewSource`
block** Resonalyze ignores: REW title/uuid/date, `startTimeS` (time of REW's sample 0),
`timeZeroIndex` (where t = 0 sat in REW's buffer — fractional), `rewDelayS` (REW's own interpolated
peak time), `peakDbfs`, `protectiveHighPass` (the high-pass that was IN the signal when measured,
or null), and in compensated files `compensation` (what was removed, by what code, peak before/after).

Reading it with numpy:

```python
import json, numpy as np
d = json.load(open("ir-v7/w_L.json"))
fs = d["sampleRate"]; h = np.asarray(d["transferRealSamples"])   # h[0] is t = 0 (loopback)
t = np.arange(h.size) / fs                                        # tail = negative time, wrap if you need it
```

Written by `autosound-tuning-skill/skills/autosound-tuning/rew_tool/resonalyze_ir.py` (which also
validates with a port of Resonalyze's `Validate()`); `ir-v7-compensated/` additionally went through
Resonalyze's own `ProtectiveHighPassCompensation` and `SaveAsync` before being re-packed with the
provenance block.

## Moving-mic RTA — `rta-mmm/<channel>.txt`

`#` comment lines (the REW title, date, uuid, REW's own notes), then `freq_Hz<TAB>SPL_dB`, one
point per 1/96 octave, the RTA's native 1/48-octave resolution with REW's display smoothing off,
REW's SPL calibration (dB SPL at the mic, with whatever mic calibration REW had loaded).

## `dsp-state.json`

One or more states of the processor's channels for the same cabin. Per channel: `hpf` / `lpf`
(`{family, hz, slope}` — `LR` Linkwitz-Riley, `BW` Butterworth, `BE` Bessel; slope in dB/oct),
`delay_ms` (positive = plays later), `inverted`, `gain_db`, `peq` (list of `{type, hz, gain_db, q}`
with `PK` / `LS` / `HS` — RBJ Q; `LS`/`HS` are the Helix LS_Q/HS_Q shelves, the RBJ shelf with
S = 1), `allpass` (`{order, hz, q}`). Top-level `_about` strings say where the state came from.

## `manifest.json`

Per set: converter and version, REW API, provenance note, the time-base and amplitude statements,
`files` (every IR file's `rewSource` plus sizes and peak positions), `compensation`, `rta` (per
RTA file: title, uuid, date, unit, smoothing, points), and where the DSP state lives. Treat it
as the machine-readable README.

## `index.json`

The catalogue tools read: `datasets[]` (id, car, session, path, channels, sampleRate, formats,
timingReference, license), `hardware[]`, `mics[]`. `tools/check.py` keeps it honest.
