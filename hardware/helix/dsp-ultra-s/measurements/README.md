Measurement files behind `FACTS.md` go here (Resonalyze IR v7 or `freq<TAB>dB<TAB>deg` text), one
A/B pair per fact, named `<fact>-<what>-{before,after}.<ext>`.

- **Fact 5 (bell Q convention, and boost against cut)** — `fact5-bell-cut-q1`, `fact5-bell-cut-q4`,
  `fact5-bell-boost-q4`, each a before/after pair. REW's unsmoothed magnitude and phase resampled to
  1/96 octave, 20 Hz - 20 kHz. Take the after minus the before in dB and fit an RBJ peaking response:
  the entered Q comes back within a few per cent. Use the `-before` file that belongs to the pair —
  the cabin moved by about 1 dB RMS over the thirteen minutes between the first reference and the
  last, while two references 74 s apart agree to 0.16 dB.
- **Fact 1 (AP2)** — the fit pair is still queued for a bench session.
