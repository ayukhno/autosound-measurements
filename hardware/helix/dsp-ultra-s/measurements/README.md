Measurement files behind `FACTS.md` go here (Resonalyze IR v7 or `freq<TAB>dB<TAB>deg` text), one
A/B pair per fact, named `<fact>-<what>-{before,after}.<ext>`.

- **Fact 5 (bell Q convention, and boost against cut)** — `fact5-bell-cut-q1`, `fact5-bell-cut-q4`,
  `fact5-bell-boost-q4`, each a before/after pair. REW's unsmoothed magnitude and phase resampled to
  1/96 octave, 20 Hz - 20 kHz. Take the after minus the before in dB and fit an RBJ peaking response:
  the entered Q comes back within a few per cent. Use the `-before` file that belongs to the pair —
  the cabin moved by about 1 dB RMS over the thirteen minutes between the first reference and the
  last, while two references 74 s apart agree to 0.16 dB.
- **Fact 1 (AP1 / AP2 all-pass)** — `fact1-apf-{ap1-4k,ap2-4k-q0.7,ap2-8k-q0.7,ap2-8k-q4}` over
  `fact1-apf-bypass`, 2026-09-01, electrical. Four filters against one reference, as in the fact 8
  sets. Magnitude is the validity check rather than the result: an all-pass that moved the level by
  more than a few hundredths of a dB was not an all-pass, and none of these did (0.04 dB worst).
  The phase is the measurement, and it separates a bilinear-transformed digital biquad from the
  analogue prototype only up high — 8 kHz is where the two forms are 9.5° apart and 1 kHz is where
  they are not.
- **Fact 2 (shelf Q convention)** — `fact2-shelfq-{ls,hs}-q{0.3,0.7,2}` over `fact2-shelfq-bypass`,
  2026-09-01, electrical, +6.0 dB at 1000 Hz, one band changed at a time. Q 0.3 and Q 2 are the ends
  of the range the PC-Tool accepts, not a choice: it clamps a shelf Q to 0.3 … 2.
- **Fact 9 (Bessel normalisation)** — `fact9-be36-1k-{lp,hp}` over `fact9-be36-1k-bypass`,
  2026-09-01, electrical. The level at the corner IS the answer here, not a check on the capture:
  a −3 dB-normalised prototype and a delay-normalised one differ by 2.6 dB at the corner alone.
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
- **Fact 8, low orders** — `fact8-xover-lr{12,24}-1k-{lp,hp}` over `fact8-xover-lr-1k-bypass`,
  2026-09-01, electrical, one reference for all four legs. Read them the same way as the LR36/BW42
  sets above. At 1 kHz they do not separate an analogue model from a digital one (0.02–0.05 dB
  apart, under what this rig resolves) and are not meant to — the 8 kHz sets decide the form, and
  these close the family and serve as a regression fixture.

**Second bench series, 2026-09-01** — the four sets above named `fact1-apf-*`, `fact2-shelfq-*`,
`fact9-be36-*` and `fact8-xover-lr{12,24}-*` were captured in one session, 20 sweeps, each set with
its **own** reference. Divide by the reference of the same set and never across sets. Same rig and
protocol as the fact 8 set, and deliberately the same grid — 1/96 octave anchored at 20 Hz, 957
points, 20 – 19897 Hz — so the two series can be read by the same code. They were exported from REW
straight over its API from the unsmoothed raw spectrum, resampled to that grid by complex averaging
with each measurement's own delay taken out before averaging and restored after, so a cell average
loses no level to rotation within the cell.
