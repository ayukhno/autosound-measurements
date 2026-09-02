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

---

## Third bench series, 2026-09-02 — the phase control, and four things measured alongside it

Fifty-seven sweeps in one day, same rig and the same grid as the two series above, exported the
same way. The set answers two questions Resonalyze's author asked about the HELIX channel **Phase**
control (issue [DIMOSUS/Resonalyze#88](https://github.com/DIMOSUS/Resonalyze/issues/88)) and
carries four unrelated results that came cheap while the bench was standing.

Every group has **its own reference capture** and only ratios within a group mean anything.
`../bench3-manifest.json` lists every file with its REW id, date, SNR, delay and caveats, and names
the reference each group divides by.

**The phase control** — `phase-ref-*`, `phase-slopeoff-*`, `phase-midhigh-*`, `phase-steps-*`,
`phase-cap-*`. The control is a second-order all-pass with Q = 1 whose corner the PC-Tool places so
that the phase equals the setting at the channel's reference crossover; the reference is the
low-pass on a subwoofer channel and the high-pass otherwise, taken **as entered**, whether that
filter is active, bypassed or set to `slope = OFF`. The `phase-cap-*` files are the ones that
matter most to an implementer: **the corner cannot exceed about 18.0 kHz**, so at a high reference
crossover the low settings all collapse onto that one filter — at 5000 Hz the settings 5.625°,
11.25° and 28.125° are literally the same measurement, while at 500 Hz the documented 5.625° grid
works exactly. Audiotec Fischer do not document that ceiling and we cannot say whether it is
deliberate.

**AP1 at three more frequencies** — `fact1-apf-s3-*`, extending the fact 1 set. The first-order
all-pass does not sit where it is typed and the error grows with frequency: −0.5 % at 250 Hz,
−0.7 % at 1 kHz, −4.9 % at 8 kHz, against the −1.6 % at 4 kHz already in `fact1-apf-ap1-4k`. AP2
lands within 0.05 % on the same rig, which is what makes this a property of the section rather than
of the measurement.

**Delay quantisation** — `delay-*`. A typed delay is rounded to a whole sample at 96 kHz: 0.05 ms
(4.800 samples) measures 5.0003, 0.32 ms (30.720) measures 30.9996. Both fractions chosen were
above the half-sample, so these files do not separate rounding from truncation upward.

**PEQ and cascade** — `peq-1k-*` and `cascade-lr24-*`. A peaking band is textbook RBJ, a cut is the
exact mirror of a boost, the width does not depend on the gain, and a high-pass and low-pass
measured separately multiply into the measurement of both engaged to 0.045 dB and 0.30° rms.

**Level** — `level-*`. Re-uploading the whole configuration to the processor changes nothing
(+0.0001 dB), and a typed −6.0 dB gain measures −5.9998 dB.

### Four defects in this set, and what they do and do not cost

These are in the data. Each one is also flagged in the header of the file it affects.

1. **An AP1 was left engaged at 8 kHz from REW #55 to #67** — the operator set it for
   `fact1-apf-s3-ap1-8k` and did not switch it off before moving on. It therefore sits in
   `phase-midhigh-*` and `phase-steps-*` as an extra first-order all-pass with its corner at
   7611.6 Hz. **It costs nothing**, and that is not an assumption: every affected group's own
   reference was captured inside the same window, so the stray filter appears identically in
   numerator and denominator and divides out of every ratio. Where the window ends was measured
   rather than assumed — `phase-steps-lp5000-byp-ph0` over `fact1-apf-s3-bypass` fits a clean
   first-order all-pass at 7608.3 Hz (0.146° rms), and `delay-0` over that same file shows it
   already gone. The affected groups fit as tightly as the clean ones, 0.11–0.29° rms. The general
   rule this illustrates: on a ratio bench a forgotten all-pass is the most forgiving mistake
   available, **provided the reference is taken in the same state**. Had the mistake landed
   between a reference and its captures, the set would have been lost.
2. **A 1.00 dB level step happened part way through sweep #49**, `phase-slopeoff-lp5000-ph0`. A
   sweep is a time-frequency map, so that file is 1 dB low above about 1.2 kHz and correct below
   it. Phase is untouched — the all-pass fit against it is 0.15° rms — but magnitude ratios into
   that group are not usable without correcting the step.
3. **`cascade-lr24-bypass-disturbed` is a bad capture.** Its bin-to-bin phase step is three times
   the session norm and ratios against it are wrong by up to 10 dB. Use `level-gain0`, the same
   bypassed state two minutes later, as the cascade group's reference; the manifest already names
   it as such. Comparing a session's reference captures against one another before trusting any of
   them is what found this.
4. **`phase-steps-lp5000-on-ph180` was mis-titled in REW** as 5.625°. The fit is unambiguous — a
   Q = 1 all-pass with its corner at 4979 Hz is the 180° setting. The file name states what was
   measured; the header records the original title.
