# What REW's own exports of this measurement look like

Three files, all of the same channel (`w_L`, plus one of `m_L`), kept as REW wrote them —
reference material for anyone building a REW → anything importer, and the evidence behind the
timing statements in the set's README. Analysed against REW's API on 2026-08-19 (REW 5.40
Beta 132, API 0.9.6).

| file | REW route | what it carries |
|---|---|---|
| `w_L.ir-text.txt` | `File → Export → Impulse response as text`, normalise **off**, window **off**, headers **on** | 16 header lines + 262144 samples. The samples are **fractions of full scale**, identical to the API's `?normalised=false` data to float32. The header states `Peak value before normalisation`, `Peak index`, `Response length`, `Sample interval (seconds)`, **`Start time (seconds)`** and `Data offset (dB)` (the SPL offset). This is the only export that carries the absolute time base exactly. |
| `w_L.wav-no-t0.wav` | `Export → Impulse response as WAV`, 32-bit float, mono, 96 kHz, everything unticked | the same 262144 samples, bit-identical — and **no timing at all**: nothing in the file says that t = 0 sits at sample 95541. |
| `w_L.wav-t0-at-256.wav` | the same, with **`Place t=0 at sample index` = 256** | 166859 samples: REW cut 95285 = 95541 − 256 from the head, so t = 0 lands exactly on sample 256. This is the only way a WAV carries the loopback time base, and only by that convention. |

Two things measured here, not assumed:

- **The header's peak is interpolated.** `Peak value before normalisation` = 3.4054602e-3 while the
  largest sample is 3.4045896e-3 — 0.0022 dB higher, i.e. the sub-sample peak, not a sample.
- **`Place t=0 at sample index` snaps the measurement itself.** `m_L`'s start time was
  −0.997093402 s (t = 0 at the fractional sample 95720.967); after exporting it that way
  (`m_L.wav-t0-at-256.wav`, not kept here) REW reported −0.997093750 s — exactly 95721.000 — and
  cut 95465 samples. The file is honest (t = 0 on sample 256, data bit-identical), but a WAV can
  only place t = 0 on a whole sample, and the act of exporting moved the session's own timing by
  0.033 samples. The other seven channels were untouched. For sub-sample timing use the text
  export or the API.
