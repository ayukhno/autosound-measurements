Measurement files behind `FACTS.md` go here (Resonalyze IR v7 or `freq<TAB>dB<TAB>deg` text), one
A/B pair per fact, named `<fact>-<what>-{before,after}.<ext>`.

- **Fact 5 (bell Q convention, and boost against cut)** — `fact5-bell-cut-q1`, `fact5-bell-cut-q4`,
  `fact5-bell-boost-q4`, each a before/after pair. REW's unsmoothed magnitude and phase resampled to
  1/96 octave, 20 Hz - 20 kHz. Take the after minus the before in dB and fit an RBJ peaking response:
  the entered Q comes back within a few per cent. Use the `-before` file that belongs to the pair —
  the cabin moved by about 1 dB RMS over the thirteen minutes between the first reference and the
  last, while two references 74 s apart agree to 0.16 dB.
- **Fact 1 (AP2)** — the fit pair is still queued for a bench session.
- **Fact 8 (crossover alignment and implementation)** — `fact8-xover-{lr36-1k,bw42-1k,lr36-8k}-{bypass,lp,hp}`,
  three per filter setting rather than a before/after pair, because a crossover has two legs and both
  are ratioed against the same unfiltered reference. **Electrical**: no microphone, so there is no
  cabin and no drift between captures; the whole discipline is that nothing but the filter changed
  within a set. Take `lp` and `hp` over `bypass` as complex ratios. The bypass file is also the
  chain's own noise floor — about −50 dB — so nothing deeper than ~1.5 octaves into a stopband is
  evidence. Phase comes from the impulse response on the loopback's time axis, not from REW's curve.
  `fact8-rew-measure-dialog.png` and `fact8-rew-analysis-prefs.png` are REW as it stood for every
  capture in the set — the sweep, the loopback routing and timing offset, and the impulse-response
  and frequency-response options that decide what the numbers mean. Two of those options matter to
  anyone re-deriving these files rather than reading them: **Align IR peak** shifts each buffer and
  records the shift in `startTime`, and REW **normalises every impulse response to peak = 1**, so
  levels have to come from the SPL curve and only the phase from the IR. The **1/24 smoothing** shown
  there is a display default and is not in these files; they are the unsmoothed curve.
