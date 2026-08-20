# Six-point capture: which dips a filter can fix, and which it cannot

**What this settles.** A dip in a car's response is one of two things, and they look
alike on a magnitude plot:

- a **resonance or absorption** — the cabin or the driver itself losing energy at that
  frequency. It is minimum-phase, an inverse filter really does refill it, and the cost
  is only the energy the boost puts back.
- a **cancellation** — two arrivals subtracting at the microphone. No filter fixes it:
  boosting spends excursion and headroom to make two arrivals cancel a little louder,
  and the null does not move.

They differ in one behaviour: **a resonance stays at the same frequency when the
microphone moves; a cancellation shifts.** That is the whole test, and it is why this
capture is built around sampling a volume rather than a point.

## Why six positions and not one, or two

Single-point measurements in a car are not stable above the **Schroeder frequency**,
which in a car cabin is about **150–200 Hz**. Above it many room modes overlap, the sum
behaves as a random process, and sound pressure at a point becomes Rayleigh-distributed
— which makes a measured value **much more likely to be too low than too high**.

A deep null measured at one point above 200 Hz is therefore, on its own, the *expected*
outcome of where you happened to put the microphone. It is not yet a fact about the car.

Sources, with what each actually supports:

- **Geddes & Blind, "The Localized Sound Power Method", AES Convention 76, paper 2127
  (1984)** — the abstract, which is public, states: *"Single point microphone
  measurements in enclosed spaces lack sufficient stability to be useful for sound
  system equalization (above the Schroeder frequency)."* The paper is paywalled; the
  numbers usually credited to it here (six microphones, the ear ellipsoid, ~1/3-octave
  reliable resolution) come from secondary summaries, not from the source.
- **Strauß, Treichel & Kessler, DAGA 2010** (Fraunhofer IDMT with BMW) — the Schroeder
  frequency in a car is "about 150–200 Hz"; above it the modal sum gives Gaussian real
  and imaginary parts and a Rayleigh distribution of sound pressure, with the
  too-low/too-high asymmetry quoted above.
- **miniDSP, "Microphone techniques in car cabins"** — the practitioner view: a single
  fixed point scores 2/5 for reproducibility with errors to ~20 dBr concentrated in the
  mid and high frequencies; a moving mic 4/5; an array 5/5.

**Averaging alone is not the answer here.** The industry uses the six-point average to
decide *what to equalise to*. This protocol needs the six positions **kept separately**,
because the average is precisely the operation that destroys the stay-versus-move
signal. Six positions give both: the average the literature trusts, and the spread that
labels each dip.

Below about 150 Hz the six positions should agree closely. That is a built-in sanity
check on the rig, not a wasted measurement — if they disagree down there, something is
wrong before any conclusion is drawn.

## The six positions

Origin is the point the **centre of the head** occupies in normal seating. The six
samples are two ear positions across three driver postures — that is what "the volume
where ears actually are" means, and it is reproducible with a tape measure:

| # | posture | lateral | vertical | fore/aft |
|---|---|---|---|---|
| 1 | nominal, left ear | −9 cm | 0 | 0 |
| 2 | nominal, right ear | +9 cm | 0 | 0 |
| 3 | tall driver, left ear | −9 cm | +7 cm | −4 cm (further back) |
| 4 | tall driver, right ear | +9 cm | +7 cm | −4 cm |
| 5 | short driver, left ear | −9 cm | −7 cm | +5 cm (further forward) |
| 6 | short driver, right ear | +9 cm | −7 cm | +5 cm |

Pairwise separations land between 14 and 18 cm, which is a useful fraction of a
wavelength from roughly 500 Hz up — the band where the classification question is live.

**If time forces a cut, drop positions 3 and 4** and run four. Both ears and two heights
survive; what is lost is the tall-driver corner of the ellipsoid and some of the spread
statistics. Do not cut below four.

## Tripod or hand? Both, for different parts

A tripod cannot realistically be repositioned six times inside a cabin to centimetre
accuracy — the head position sits above a seat, boxed in by the door, the console and
the roof. Anyone who has tried knows this. So the honest answer is that the two halves
of this capture need different precision, and only one of them needs the tripod.

**Timing needs the tripod — no exceptions.** Arrival times, excess phase, anything
sub-sample: a hand adds ±2 samples of wander between takes and drifts five samples over
a quarter of an hour (measured; see the constraint list below). That destroys the very
quantity being read. The reference channel, the drift anchors and any capture whose
arrival you intend to use must be taken with the microphone mechanically fixed.

**The six-position spread does not.** What that half reads is whether a dip *moves in
frequency* between points **14–18 cm apart**, and how far the level at one frequency
spreads across the volume. A hand places the microphone to within a centimetre or two —
roughly a tenth of the separation being measured. The signal survives that comfortably;
what it costs is a noise floor of about **1–2 dB RMS per position**, so a level spread
smaller than that cannot be called meaningful. Say so in the notes and the result stands.

**Better than either, and cheap: a jig.** A flat bar or a piece of plywood with six
marked holes at the offsets below, clamped to the headrest posts or mounted on the
tripod head, and one microphone moved between them. Millimetre repeatability, one
mechanical fixture, seconds per move. If this capture is going to be run more than once,
build the jig first — it removes the whole dilemma and makes the positions reproducible
between sessions and between cars, which hand-holding never will.

**If it must be hand-held, take more positions, not fewer.** Precision per sample is
what a hand loses; count is what it can cheaply buy back. Ten or twelve quick positions
scattered through the same volume give a better spread statistic than six imprecise
ones, and the stay-versus-move verdict only gets clearer. The six below are then a
minimum sampling of the volume, not a target to hit exactly.

## The capture

Order the session **by position, not by channel** — six microphone moves instead of
forty-eight:

At each of the six positions, with the microphone fixed:

1. a **reference channel** (pick one and keep it for the whole session — a midrange
   works well: sharp arrival, good signal) — this is the position's drift anchor;
2. then **every driver in turn, played solo**, every other channel muted.

Then, once, wherever the microphone ends up:

3. one **moving-mic average** per driver, mic wandered through the same volume;
4. a **repeat of position 1** — reference channel and one driver — as the end-of-session
   drift control;
5. **near-field** per driver: 7–15 cm from the cone, on axis. This separates what the
   driver does from what the cabin does to it, and it is the only capture here that says
   anything about the driver itself.

## Why each constraint

- **Solo drivers.** The criterion reads one driver's response at a time; the sum of
  several is a different signal. A driver that cannot be soloed cannot be used. This is
  the one hard requirement.
- **EQ off, all-pass off.** An all-pass *is* added excess phase by construction — it
  corrupts the quantity in question. Output EQ off too, or the dip's label is taken on
  an already-corrected curve. A **protective high-pass** to keep a driver safe is fine
  and expected: leave it in and write down what it is.
- **Swept sine, on a timing reference.** Phase is only meaningful when the sweep sits on
  a reference — a physical loopback is best, an acoustic timing reference acceptable.
  Without one, phase and everything computed from it is arbitrary. Confirm it is active
  before the first sweep; this is the single thing most casually-taken measurements get
  wrong.
- **A tripod for anything timed.** Measured on 2026-08-20 in the reference cabin:
  hand-held repeats 25 s apart differ by **0.9–2.4 dB RMS** over 100 Hz–16 kHz with
  arrivals wandering **±2 samples**, drifting five samples over a quarter of an hour. On
  a tripod the same repeats agree to **0.18–0.25 dB RMS** and **0.09 samples**. Those
  numbers are why the reference channel and the drift anchors are mechanically fixed —
  and why the six ellipsoid positions, which read a 14–18 cm displacement rather than a
  sub-sample arrival, can survive a hand. See "Tripod or hand?" above.
- **The gain set once.** The interface's input gain is set on the loudest channel before
  the first sweep and never touched again; the level relation between channels is what
  makes a set analysable.

## Temperature, and why the drift anchors exist

Cabin air temperature moves every arrival in proportion to its acoustic path: about
**0.43 samples per °C on a 0.9 m path at 96 kHz**. A six-position session takes long
enough for that to matter. Two facts from the reference cabin, both measured:

- two unfiltered captures **74 s apart** agree to **0.16 dB RMS**;
- two **thirteen minutes apart** differ by **0.95 dB RMS**, 4 dB at 166 Hz — it had
  rained in between.

Hence the reference channel at every position, and the repeat at the end. And: **do not
ventilate between captures.** Opening the doors starts the steepest part of the
re-warming transient. Ventilate between blocks, then sit closed for three or four
minutes before resuming.

## What to write down

- Vehicle: make, model, body, left- or right-hand drive.
- Where each measured driver sits and where it aims, and whether the enclosure is sealed
  or ported.
- **Driver models** — Fs and rated passband set the trust band and the protective floor.
- Crossover and protective filters in force per channel, even with EQ off.
- Microphone, interface, which **calibration file** was loaded, and mic orientation. A
  microphone standing upright at the listening position is a grazing-incidence
  measurement and wants the 90° file; near-field, aimed at the driver, wants 0°.
- Where the origin was, and the six offsets as actually realised.
- Who was in the car and where they sat. A torso is a reflector; above 2 kHz a shift of
  a few centimetres moves an interference pattern by several dB.
- Confirmation that the timing reference was active and source tone controls off.

## Export

Anything that keeps phase on the session's own time base:

- **Resonalyze**: the measurement files as saved (IR JSON v7).
- **REW**: `File → Export → Measurement as text` **including phase**, or the whole
  `.mdat`. For impulse responses on an absolute time base, `File → Export → Impulse
  response as text` with normalisation and windowing off — that export is the one that
  carries the start time; see [`FORMATS.md`](../FORMATS.md).
- Moving-mic captures as text; magnitude is enough there.

Keep the six positions as six files. Do not pre-average them.

## What comes back

Per driver, per candidate dip, across the six positions:

- **stays at one frequency** → a resonance, and worth a filter;
- **moves, or varies in depth by many dB** → a cancellation, and worth none;
- the **spread across the six** at that frequency, which is the honest confidence
  interval on any single-point claim about it — and, above the Schroeder frequency,
  what tells you whether the average is describing the car or the sampling.

Plus the six-point average itself, which is what the field would equalise to.

Results, data and code go back to whoever captured the session, and the set can be
published here under CC BY 4.0 if its owner wants it published.
