# Contributing a cabin or a hardware fact

Thank you. Two kinds of things belong here; everything else goes to the method repositories.

## A cabin measurement set

**What to measure** (the minimum that makes a set computable):

1. **Per-driver loopback-referenced sweeps** — one REW sweep per DSP output, mic at the listening
   position, REW's timing reference set to a physical loopback on the same interface, **no timing
   offset**, all channels in one REW session at one mic gain and one sweep level. Drivers play
   "clean" (no EQ, no delay, no crossover) except the protective high-passes a driver physically
   needs — write those down per channel, they are part of the data.
2. **Moving-mic RTA per channel** (the level/voicing view) — optional but valuable.
3. **The DSP state** you would defend by ear (crossovers, delays, polarity, gains, PEQ, all-pass),
   and, if you have it, an earlier attested state — a set is worth far more with an end point.

**What to send.** Either the REW session (`.mdat`) and the per-channel notes, or the converted set
(`ir-v7/`, `rta-mmm/`, `dsp-state.json`, `manifest.json`, `README.md` — see an existing set and
`FORMATS.md`). The converter is
`autosound-tuning-skill/skills/autosound-tuning/rew_tool/resonalyze_ir.py`; run it with `--hpf`
for every channel that had a protective high-pass.

**Naming.** `cars/<make>-<model>-<generation>-<body>-<drive>/` (e.g. `vw-passat-b8-sedan-lhd`),
sessions `<YYYY-MM-DD>_<what>` (e.g. `2026-06-15_front-set-01`), channels `sw`, `w_L`, `w_R`,
`m_L`, `m_R`, `tw_L`, `tw_R`, `c`, `r_L`, `r_R` (add your own with a line in the README).

**Privacy.** No VIN, no plates, no names of people, no precise addresses, no photos showing plates.
The cabin id is model-level.

**`CAR.md`** — the install (drivers, positions and aiming, processor, amplifiers, source), the rig
(mic, interface, cal files), anything that helps someone read your measurements.

## A hardware fact

A fact is a claim about a device that a measurement settles — "this processor's LS_Q shelf is the
RBJ shelf with S = 1", "delays on the two layers add". Put it in `hardware/<vendor>/<device>/FACTS.md`
with: the claim, the **protocol** (single-variable A/B: sweep → change one thing → sweep, mic
untouched), the **measurement files** in `measurements/` (v7 IRs or `freq<TAB>dB[<TAB>deg]` text),
the fit or the number that decides it, and the date/firmware. A fact without its measurement is a
forum post — it can wait in a "pending" line, not in the table.

## Mechanics

- Branch `car/<id>` or `hw/<id>`; one set or one device per PR.
- Run `python3 tools/check.py` before pushing (needs numpy); CI runs the same.
- By submitting you license the data under **CC BY 4.0** and any script under **MIT**, and you
  confirm you have the right to. Please sign commits with `git commit -s` (DCO).
- Large sessions (> ~200 MB) — open an issue first; they may go to a release asset with only the
  descriptors in the tree.
