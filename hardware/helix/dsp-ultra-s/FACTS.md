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
| 5 | **Bell (PK) bands are the RBJ peaking EQ, and the Q you type is the RBJ Q.** A free fit of the A/B ratio recovers the entered value: **Q 1 → 1.031**, **Q 4 → 4.028**, at 400 Hz and −12 dB. A "symmetric" definition would have shown up as a factor of two at this depth; it did not. **Boost mirrors cut**: +12 dB at Q 4 fits **Q 3.991 / +11.85 dB** against the cut's 4.028 / −11.95 dB — 0.9 % in Q and 0.10 dB in level. | `measurements/fact5-bell-{cut-q1,cut-q4,boost-q4}-{before,after}.txt`, 2026-08-20: output layer, channel `w_L`, one band changed at a time, everything else cleared; fit residuals 0.97 / 0.56 / 0.19 dB. Two unfiltered references 74 s apart agree to 0.16 dB RMS, which is this A/B's noise floor; references 13 minutes apart differ by 0.95 dB RMS, so each filter was ratioed against the reference nearest it in time. | verified |
| 7 | **A ±12 dB band at 400 Hz does not push this midbass out of linearity.** The boost fit returns +11.85 dB of the entered +12.00 with the smallest residual of the three (0.19 dB); compression or a rattle would have cost level and left structure in the residual. | the fact 5 boost pair. | verified for this driver, at this level, at this frequency |
| 6 | The channel **Phase** control (0–360°) is a 2nd-order all-pass whose coefficients the DSP derives from the channel's crossover frequency (for the sub, from the LPF); it adds delay above the turn frequency and is not available on the midbass reference in practice. | forum sources + the owner's practice (skill `helix-phase-allpass.md`) — **not** bench-verified here. | folklore, flagged |

`formats/atf_full_eq_sample.txt` is under the skill's MIT code licence as a fixture and CC BY 4.0
here as data — either is fine.
