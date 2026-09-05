#!/usr/bin/env python3
"""How much of a whole stage a listener moves by shifting their head.

sigma of the SUM's interaural cues across three ear-height pairs (tuned preset,
VW Passat B8), each divided by a full-edge reference so the two cues can be read
on one axis. The references are DIFFERENT KINDS and the legend says so:

  ITD : 525 us -- the PHYSICAL limit for this rig's 18 cm ear spacing (18/343).
  ILD : 6 dB   -- a full-edge level difference from the literature.

Source numbers: results/two-ear-stage-control/, session 2026-09-03.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

F   = [500, 1000, 2000, 3150, 5000]
ITD = [60, 235, 383, 555, 420]          # us
ILD = [0.64, 4.03, 2.56, 2.36, 1.25]    # dB
itd_pc = [100*v/525.0 for v in ITD]
ild_pc = [100*v/6.0 for v in ILD]

fig, ax = plt.subplots(figsize=(7.6, 4.3), dpi=170)
fig.patch.set_facecolor("white"); ax.set_facecolor("white")

ax.axhspan(100, 130, color="#c62828", alpha=0.06, zorder=0)
ax.axhline(100, color="#c62828", lw=1.1, ls="--", zorder=2)
ax.text(450, 102.5, "moving your head spans a WHOLE stage width",
        color="#c62828", fontsize=8.5, ha="left", va="bottom")

ax.plot(F, itd_pc, "o-", color="#1565c0", lw=2, ms=6,
        label="σ interaural TIME ÷ 525 µs  (physical limit, 18 cm spacing)")
ax.plot(F, ild_pc, "s-", color="#ef6c00", lw=2, ms=6,
        label="σ interaural LEVEL ÷ 6 dB  (full-edge difference, literature)")

for x, y in zip(F, itd_pc):
    ax.annotate(f"{y:.0f}%", (x, y), textcoords="offset points", xytext=(0, 9),
                ha="center", fontsize=8.5, color="#1565c0")
for x, y in zip(F, ild_pc):
    ax.annotate(f"{y:.0f}%", (x, y), textcoords="offset points", xytext=(0, -15),
                ha="center", fontsize=8.5, color="#ef6c00")

ax.annotate("only here do BOTH cues survive the head moving",
            xy=(530, 9.5), xytext=(1150, 4), fontsize=8.5, color="#2e7d32",
            ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color="#2e7d32", lw=1.1))

ax.set_xscale("log"); ax.set_xlim(430, 6200); ax.set_ylim(0, 130)
ax.set_xticks(F); ax.set_xticklabels(["500", "1 k", "2 k", "3.15 k", "5 k"])
ax.set_xlabel("band centre, Hz")
ax.set_ylabel("spread across ear positions,\n% of a full stage edge")
ax.set_title("What moving your head does to the stereo cue\n"
             "σ over three ear-height pairs, tuned preset, one cabin", fontsize=11)
ax.grid(alpha=0.25, which="both", lw=0.6)
ax.legend(fontsize=8.5, loc="upper left", framealpha=0.95)
fig.tight_layout()
fig.savefig("sigma-vs-band.png", facecolor="white")
print("wrote sigma-vs-band.png")
for f, a, b in zip(F, itd_pc, ild_pc):
    print(f"  {f:>5} Hz   ITD {a:5.1f} %   ILD {b:5.1f} %")
