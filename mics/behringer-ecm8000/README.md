# Behringer ECM8000 — the owner's calibration files

`ECM8000_0deg.txt` (on-axis, for sweeps) and `ECM8000_90deg.txt` (grazing, for moving-mic RTA),
REW calibration-file format (`frequency_Hz<space>dB`), 1/3-octave points.

**Provenance:** made by the owner by **substitution against a miniDSP UMIK-1 (serial 7158244) that
carries its factory calibration** — the UMIK-1 measured first, the ECM8000 in its place, the
difference became the ECM8000's correction; separately at 0° and 90° (files dated 2026-05-08). They are the files the owner uses in REW for
these measurements — sweeps with the 0° file, moving-mic RTA with the 90° one; REW's SPL curves
carry them, the impulse responses do not.

⚠️ `ECM8000_0deg.txt` line 34 reads `20000.000000 3.4ß50` in the original — a corrupted digit
(intended 3.450 by the trend). Kept as-is so the file is what was used; fix it before you load it.
