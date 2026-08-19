# Behringer ECM8000 — the owner's calibration files

`ECM8000_0deg.txt` (on-axis, for sweeps) and `ECM8000_90deg.txt` (grazing, for moving-mic RTA),
REW calibration-file format (`frequency_Hz<space>dB`), 1/3-octave points.

**Provenance:** made by the owner by **substitution against a miniDSP UMIK-1 (serial 7158244) that
carries its factory calibration** — the UMIK-1 measured first, the ECM8000 in its place, the
difference became the ECM8000's correction; separately at 0° and 90° (files dated 2026-05-08). They are the files the owner uses in REW — sweeps
with the 0° file, moving-mic RTA with the 90° one.

Note: the owner's original `ECM8000_0dgr_cal2.txt` had a corrupted digit on the 20 kHz line
(`3.4ß50`); the intended value is `3.450` — the previous revision of the file (before its sign
convention was flipped) read `−3.450` there, and the 12.5 k → 16 k trend (2.685 → 3.068) agrees.
Fixed here and in the owner's working copies on 2026-08-19; the 90° file was never affected.

Whether REW had these files loaded for a given session cannot be established from the session data;
REW's SPL curves carry the calibration when it is loaded, the impulse responses never do.
