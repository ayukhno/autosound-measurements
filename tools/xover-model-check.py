#!/usr/bin/env python3
# Copyright (c) 2026 ayukhno — MIT (LICENSE-CODE)
"""Fit the fact 8 crossover captures against two models of the same filter and print the
error of each: the ANALOGUE prototype, and the DIGITAL one a bilinear transform prewarped
at the crossover frequency produces. The point of the pair is that they are the same
alignment written two ways, so whichever fits better says how the processor builds it.

    python3 tools/xover-model-check.py                # every set
    python3 tools/xover-model-check.py lr36-8k        # one set

Reads only hardware/helix/dsp-ultra-s/measurements/fact8-xover-<set>-{bypass,lp,hp}.txt,
so it reproduces the published numbers from the published files and nothing else.

Needs numpy and scipy.
"""
import os
import sys

import numpy as np
import scipy.signal as sg

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DIR = os.path.join(ROOT, "hardware", "helix", "dsp-ultra-s", "measurements")
FS = 96000.0
SETS = {"lr36-1k": ("LR", 3, 1000.0), "bw42-1k": ("BW", 7, 1000.0), "lr36-8k": ("LR", 3, 8000.0)}


def read(path):
    a = np.loadtxt(path, comments="*")
    return a[:, 0], 10 ** (a[:, 1] / 20.0) * np.exp(1j * np.radians(a[:, 2]))


def legs(name):
    f, byp = read(os.path.join(DIR, f"fact8-xover-{name}-bypass.txt"))
    _, lp = read(os.path.join(DIR, f"fact8-xover-{name}-lp.txt"))
    _, hp = read(os.path.join(DIR, f"fact8-xover-{name}-hp.txt"))
    return f, lp / byp, hp / byp


def analogue(f, fc, kind, order):
    """The textbook prototype, evaluated on the s plane — no sample rate anywhere."""
    s = 1j * f / fc
    k = np.arange(order)
    poles = np.exp(1j * np.pi * (2 * k + 1 + order) / (2 * order))
    den = np.ones_like(s)
    for p in poles:
        den = den * (s - p)
    lp, hp = 1 / den, s ** order / den
    return (lp ** 2, hp ** 2) if kind == "LR" else (lp, hp)


def digital(f, fc, kind, order):
    """What a biquad chain does: bilinear, prewarped at fc, so the sample rate is in it."""
    bl, al = sg.butter(order, fc, btype="low", fs=FS)
    bh, ah = sg.butter(order, fc, btype="high", fs=FS)
    lp = sg.freqz(bl, al, worN=f, fs=FS)[1]
    hp = sg.freqz(bh, ah, worN=f, fs=FS)[1]
    return (lp ** 2, hp ** 2) if kind == "LR" else (lp, hp)


db = lambda z: 20 * np.log10(np.abs(z) + 1e-30)


def run(name):
    kind, order, fc = SETS[name]
    f, LP, HP = legs(name)
    # Only where each leg clears the chain's own noise floor, and only around the corner:
    # deeper than that the file holds noise, and noise would flatter both models equally.
    band = (f > fc / 2.2) & (f < fc * 2.2)
    mL, mH = band & (db(LP) > -32), band & (db(HP) > -32)

    def err(model, at):
        lt, ht = model(f, at, kind, order)
        e = np.concatenate([db(LP)[mL] - db(lt)[mL], db(HP)[mH] - db(ht)[mH]])
        e = e[np.isfinite(e)]
        return np.sqrt((e ** 2).mean()), np.abs(e).max()

    label = f"{kind}{order * (12 if kind == 'LR' else 6)} at {fc:.0f} Hz"
    print(f"\n=== {name}  ({label}) ===")
    for what, model in (("analogue", analogue), ("digital ", digital)):
        rms, mx = err(model, fc)
        best = min(np.geomspace(fc * 0.85, fc * 1.18, 167), key=lambda x: err(model, x)[0])
        print(f"  {what}: at nominal fc  rms {rms:6.3f} dB  max {mx:6.3f} dB   |   "
              f"best-fit fc {best:8.1f} Hz ({best / fc - 1:+.2%})")


for name in (sys.argv[1:] or SETS):
    if name not in SETS:
        sys.exit(f"unknown set {name!r}; have: {', '.join(SETS)}")
    run(name)
