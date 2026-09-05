#!/usr/bin/env python3
"""Does our two-ear result reproduce in DIMOSUS's own cabin?

His v8 set (Resonalyze-test-data, CC BY 4.0) swept the left midrange solo while ONE
microphone was carried through seven positions: centre, L / LF / LFF, R / RF / RFF,
then back to centre. Left-to-right is 20 cm; the forward pairs add 10 and 20 cm.

So (L,R), (LF,RF), (LFF,RFF) are three "ear pairs" of one driver, 20 cm apart, the pair
translated forward - the same shape as our three ear HEIGHTS. If our finding is a
property of the construction rather than of our car, his data must show the same thing:
the interaural DELAY of one driver stable across the pairs, the interaural LEVEL not.

Everything is loopback-referenced on one absolute time base, so no fitting anywhere.
"""
import json, pathlib, numpy as np

D = pathlib.Path(__file__).parent/"v8"
FS = 96000.0
BANDS = [(500, 355, 710), (1000, 710, 1420), (2000, 1420, 2840),
         (3150, 2240, 4480), (5000, 3550, 7100)]
LIMIT_US = 20e-2/343.0*1e6          # 583 us: the physical limit for a 20 cm spacing

def ir(name):
    d = json.load(open(D/f"{name}.json"))
    return np.asarray(d["transferRealSamples"], dtype=float)

def band_cue(a, b, lo, hi):
    """(interaural delay us, interaural level dB) between two positions, in one band.
    Positive delay = b lags a."""
    n = 1 << int(np.ceil(np.log2(len(a) + len(b))))
    A, B = np.fft.rfft(a, n), np.fft.rfft(b, n)
    f = np.fft.rfftfreq(n, 1/FS)
    m = (f >= lo) & (f <= hi)
    ild = 10*np.log10(np.sum(np.abs(B[m])**2)/np.sum(np.abs(A[m])**2))
    X = np.zeros_like(A); X[m] = A[m]*np.conj(B[m])
    cc = np.fft.irfft(X, n)
    lim = int(LIMIT_US*1e-6*FS)
    idx = np.concatenate([np.arange(0, lim+1), np.arange(n-lim, n)])
    k = idx[int(np.argmax(cc[idx]))]
    if k > n//2: k -= n
    return k/FS*1e6, ild

print("Resonalyze v8, BMW F30, left midrange solo, one mic carried between positions")
print("pairs 20 cm apart, translated forward 0 / 10 / 20 cm\n")

pairs = [("L", "R", "0 cm"), ("LF", "RF", "+10 cm"), ("LFF", "RFF", "+20 cm")]
irs = {k: ir(f"mid_{k}") for k in ("L", "R", "LF", "RF", "LFF", "RFF")}

print(f"{'band':>7} | " + " | ".join(f"{lbl:^17}" for _, _, lbl in pairs) + " |   spread")
print("-"*86)
rows = []
for fc, lo, hi in BANDS:
    vals = [band_cue(irs[a], irs[b], lo, hi) for a, b, _ in pairs]
    itds = [v[0] for v in vals]; ilds = [v[1] for v in vals]
    cells = " | ".join(f"{t:>+7.0f}us {l:>+6.2f}dB" for t, l in vals)
    sig_t, sig_l = float(np.std(itds, ddof=1)), float(np.std(ilds, ddof=1))
    flip_t = len({np.sign(t) for t in itds}) > 1
    flip_l = len({np.sign(l) for l in ilds}) > 1
    print(f"{fc:>6} | {cells} | σ {sig_t:>5.0f}us {sig_l:>5.2f}dB"
          f"{'  ITD FLIPS' if flip_t else ''}{'  ILD FLIPS' if flip_l else ''}")
    rows.append((fc, sig_t, sig_l, flip_t, flip_l))

print("\ncontrol - the same position twice (centre, opening and closing sweep):")
c1, c2 = ir("mid_center"), ir("mid_center_final")
for fc, lo, hi in BANDS:
    t, l = band_cue(c1, c2, lo, hi)
    print(f"  {fc:>5} Hz   {t:>+6.1f} us   {l:>+6.2f} dB")
