# Mic-shift capture: which dips a filter can fix, and which it cannot

> ⚠️ **Revision pending (2026-08-20).** Two microphone positions is the minimum this
> protocol was built on, and it is about to become six. Geddes & Blind (AES 76, 1984,
> *The Localized Sound Power Method*) established that a single point in a car cabin is
> not stable enough to equalize from **above the Schroeder frequency**, which Strauß,
> Treichel & Kessler (DAGA 2010) put at **150–200 Hz** for a car: above it the modal sum
> is effectively random, sound pressure is Rayleigh-distributed, and a measured value is
> **much more likely to be too low than too high** — so a deep single-point null above
> 200 Hz is the expected outcome of sampling, not a fact about the system. The field
> standard answer is six positions in the ear ellipsoid, averaged, worth about 1/3-octave
> of reliable resolution.
>
> That does not replace the stay-versus-move test — averaging destroys exactly the
> position dependence this protocol uses as its signal — but six positions give both:
> the average the literature trusts, and the per-position spread that labels each dip.
> **Wait for the revision before running this in a car.** Below ~150 Hz the two-point
> version is still sound.

**What this settles.** A dip in a car's response is one of two things, and they look
alike on a magnitude plot:

- a **resonance or absorption** — the room or the driver itself losing energy at that
  frequency. It is minimum-phase, an inverse filter really does refill it, and the fix
  costs the amplifier only the energy the boost puts back.
- a **cancellation** — two arrivals (direct + reflection, or two drivers) subtracting at
  the microphone. No filter fixes it: boosting there spends excursion and headroom to
  make the two arrivals cancel a little louder, and moves the null nowhere.

Telling them apart from one measurement is the open question. Telling them apart from
**two** is easy, and that is what this capture is for: **a dip that stays at the same
frequency when the microphone moves is a resonance; a dip that shifts is a
cancellation.** That gives every dip a ground-truth label without relying on anyone's
tuning history — which is what any single-measurement criterion has to be tested
against, on a cabin it has never seen.

Everything below is an ordinary sweep session. No gear beyond what a REW- or
Resonalyze-based tuner already has. About 40–60 minutes for two drivers.

---

## The capture

For each **driver**, played **solo** (every other channel muted), with **EQ and any
all-pass off**:

| # | capture | why |
|---|---|---|
| 1 | swept sine at the listening position **P0** | the measurement a criterion has to judge from |
| 2 | the same sweep at **P1**, mic moved **20–30 cm** from P0 | the second point — this is the ground truth |
| 3 | one **moving-mic average** (MMM), mic wandered in a ~30 cm cloud around P0 | shows which dips survive being averaged over space |
| 4 | the **P0 sweep repeated**, mic untouched | the drift floor: how much this rig's phase reading breathes take to take |

Two positions is the minimum and it is enough. A third is a robustness extra, not a
requirement.

**A head with two ear microphones is the ideal rig.** If the ear spacing is ~20–25 cm,
the two ears *are* P0 and P1, fixed and repeatable with no drift between them: sweep one
ear, then the other, driver unchanged. One caveat, not a problem: at that spacing the
stay-versus-move test is sharpest in the midrange — below ~500 Hz the two points are a
small fraction of a wavelength and positional nulls barely move, above ~2 kHz nearly
everything moves. The analysis accounts for it.

Moving the mic by tilting the seat back or sliding the seat works just as well, as long
as the displacement is recorded and nothing else in the car changes.

## Why each constraint

- **Solo drivers.** The criterion reads one driver's phase at a time; the sum of several
  drivers is a different signal. A driver that cannot be soloed cannot be used. This is
  the one hard requirement.
- **EQ off, all-pass off.** An all-pass filter *is* added excess phase by construction —
  it corrupts exactly the quantity in question. Output EQ off too, or the dip's label is
  taken on an already-corrected curve. A **protective high-pass** to keep the driver safe
  is fine and expected: leave it in and write down what it is, it can be de-embedded
  afterwards. If the rig can only capture with the full crossover network live, the data
  is still usable — say so in the notes and prefer the gentlest slopes available.
- **Swept sine, with a timing reference.** Phase is only meaningful when the sweep sits
  on a reference — a physical loopback cable is best, an acoustic timing reference is
  acceptable. Without one, phase and everything computed from it is arbitrary. This is
  the single thing most casually-taken measurements get wrong; confirm it is active
  before the first sweep.
- **Near-field captures (optional, valuable).** One near-field sweep per driver separates
  what the driver does from what the cabin does to it, and turns a "the driver is dipping
  here" argument into a measurement.

## What to write down (a short text note is enough)

- Vehicle: make, model, body, left- or right-hand drive.
- Where each measured driver sits and where it aims (doors, pillars, kick panels, dash
  firing at the glass, boot), and whether the enclosure is sealed or ported.
- **Driver models** — the Fs and rated passband set the trust band and the protective
  floor per driver. The model name is enough, the rest can be looked up.
- Crossover and protective filters actually in force per measured channel (type, slope,
  corner), even with EQ off.
- Microphone, interface, which **calibration file** was loaded, and mic orientation
  (0° / 90°).
- Where P0 was and how far, in which direction, P1 was from it.
- Confirmation that the timing reference was active and that source tone controls were
  off.

## Export

Anything that keeps phase on the session's own time base:

- **Resonalyze**: the measurement files as saved (IR JSON v7).
- **REW**: `File → Export → Measurement as text` **including phase**, or the whole
  `.mdat`. For impulse responses on an absolute time base, `File → Export → Impulse
  response as text` with normalisation and windowing off — that export is the one that
  carries the start time; see [`FORMATS.md`](../FORMATS.md).
- MMM as text; magnitude is enough there.

## What comes back

Per driver and per candidate dip: the P0/P1 comparison gives the label — *stays* (a
resonance, worth a filter) or *moves* (a cancellation, worth none) — and a
single-measurement criterion computed from P0 alone gives its verdict. Whether the two
agree on a cabin the criterion has never been fitted to is the whole question. Results,
data and code go back to whoever captured the session, and the set can be published here
under CC BY 4.0 if its owner wants it published.
