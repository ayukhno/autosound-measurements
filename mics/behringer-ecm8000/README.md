# Behringer ECM8000 — the owner's calibration files

`ECM8000_0deg.txt` (on-axis) and `ECM8000_90deg.txt` (grazing incidence), REW calibration-file
format (`frequency_Hz<space>dB`), 1/3-octave points.

**Which file goes with which measurement.** The microphone stands upright at the listening
position, so sound from the stage reaches it edge-on: everything measured at the listening
position — sweeps and moving-mic RTA alike — uses the **90°** file. Only **near-field** captures,
where the microphone is pointed at the driver, use the **0°** file. (An earlier revision of this
file stated the opposite for sweeps; that was wrong, and the sets are being re-checked against the
owner's own account of how each group was taken.)

The choice only matters at the top: the two files agree to 0.27 dB on average below 1 kHz, and
diverge above 2 kHz — 3.4 dB at 10 kHz, 5.9 dB at 16 kHz, 7.35 dB at 20 kHz. A curve taken with
the wrong one of the two is trustworthy in the bass and midrange and wrong by up to 7 dB in the
last octave.

⚠️ **The June 2026 session:** the owner reports that one group of measurements was captured with
the other file loaded, noticed at the time in REW. Which group is not yet identified. Impulse
responses are unaffected either way — REW never writes a calibration into an IR — but the
`rta-mmm/` curves, which do carry REW's calibration, should be read with that in mind above 2 kHz.

**Provenance:** made by the owner by **substitution against a miniDSP UMIK-1 (serial 7158244) that
carries its factory calibration** — the UMIK-1 measured first, the ECM8000 in its place, the
difference became the ECM8000's correction; separately at 0° and 90° (files dated 2026-05-08).

Note: the owner's original `ECM8000_0dgr_cal2.txt` had a corrupted digit on the 20 kHz line
(`3.4ß50`); the intended value is `3.450` — the previous revision of the file (before its sign
convention was flipped) read `−3.450` there, and the 12.5 k → 16 k trend (2.685 → 3.068) agrees.
Fixed here and in the owner's working copies on 2026-08-19; the 90° file was never affected.

Whether REW had these files loaded for a given session cannot be established from the session data;
REW's SPL curves carry the calibration when it is loaded, the impulse responses never do.
