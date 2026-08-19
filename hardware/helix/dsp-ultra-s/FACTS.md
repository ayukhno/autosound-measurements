# Helix DSP Ultra S — hardware-verified facts

Audiotec-Fischer Helix DSP Ultra S, 96 kHz, PC-Tool (v4/v5 era), measured on the Passat B8 rig
(`cars/vw-passat-b8-sedan-lhd`) with the **single-variable A/B protocol**: loopback sweep → change
ONE thing in the DSP, mic untouched → sweep; the complex ratio of the two sweeps is the device's
response to that change. Dates are when the fact was pinned; "evidence" names what decided it.

| # | fact | evidence | status |
|---|---|---|---|
| 1 | **AP2 (2nd-order all-pass band in the EQ bank) is the textbook 2nd-order all-pass**, phase `−2·atan2((f/f0)/Q, 1 − (f/f0)²)`. | A/B on a tweeter channel, 2026-07: a free fit of the complex ratio recovered the entered f0/Q — fitted 4386 Hz / Q 3.82 against entered 4414 Hz / Q 4.0, 31° RMS residual. Use a HIGH Q for the check: a low-Q APF over a band-limited ratio is nearly degenerate with delay + offset. | verified (measurement files to be added to `measurements/`) |
| 2 | **LS_Q / HS_Q shelves at Q 0.7071 are the RBJ shelf with S = 1** — REW models them as its "LS Q"/"HS Q" types; REW's plain "Low shelf"/"High shelf" is a different definition. | REW filter-math cross-check to 0.000–0.05 dB (skill `rew-api-quirks.md`), consistent with REW's own Audiotec-Fischer equaliser export. | verified by model equivalence |
| 3 | **Delays on the virtual-channel layer and the output layer SUM** (max 20.82 ms each) — enter a delay in one layer only. | owner's PC-Tool practice, confirmed in the tune's audit trail. | verified in use |
| 4 | **30 PEQ bands per output channel; the channel gain is a separate control** (not in the EQ bank). The PC-Tool imports one channel's EQ from the tab-separated "Full EQ (30 bands)" bank — the same block REW exports with its Audiotec Fischer equaliser. | `formats/atf_full_eq_sample.txt` — a real REW export of a 20-band channel (PK bells + LS_Q/HS_Q shelves, 30 slots). | verified |
| 5 | **Bell (PK) Q convention** — REW's list and REW's export (Bandwidth = Fc/Q, i.e. RBJ) say RBJ; the Helix bell at ±12 dB has **not** been measured by us yet. | planned: woofer channel, −12 dB at ~400 Hz with Q 1 and Q 4, half-gain bandwidth from the A/B ratio (RBJ vs "symmetric" differ 2× in Q at 12 dB). | **pending** |
| 6 | The channel **Phase** control (0–360°) is a 2nd-order all-pass whose coefficients the DSP derives from the channel's crossover frequency (for the sub, from the LPF); it adds delay above the turn frequency and is not available on the midbass reference in practice. | forum sources + the owner's practice (skill `helix-phase-allpass.md`) — **not** bench-verified here. | folklore, flagged |

`formats/atf_full_eq_sample.txt` is under the skill's MIT code licence as a fixture and CC BY 4.0
here as data — either is fine.
