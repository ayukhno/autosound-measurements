#!/usr/bin/env python3
# Copyright (c) 2026 ayukhno — MIT (LICENSE-CODE)
"""Validate the repository: index.json points at things that exist; every dataset has its
README/manifest and every file the manifest names; every impulse-response JSON passes the
Resonalyze ImpulseResponseFile.Validate() rules (format v7, commit d11186e — the same port
rew_tool/resonalyze_ir.py uses to write them); RTA files parse; dsp-state parses; the
licences are there. Exit 1 on the first class of failure found, after listing all of them.

    python3 tools/check.py            # whole repo
    python3 tools/check.py PATH ...   # only these IR json files / dataset dirs

Needs numpy.
"""
import glob
import json
import math
import os
import sys

import numpy as np

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FAILS = []


def fail(msg):
    FAILS.append(msg)
    print("FAIL", msg)


def ok(msg):
    print("  ok", msg)


def validate_v7(doc):
    """Port of Resonalyze ImpulseResponseFile.Validate() for the members a file may carry."""
    def f(msg):
        raise ValueError(msg)
    if doc.get("format") != "resonalyze-impulse-response":
        f(f"Unsupported file format '{doc.get('format')}'.")
    v = doc.get("version")
    if not isinstance(v, int) or v < 4 or v > 7:
        f(f"Unsupported impulse response version {v}.")
    fs = doc.get("sampleRate")
    if not isinstance(fs, int) or fs < 44_100 or fs > 768_000:
        f("The sample rate is outside the supported range.")
    if doc.get("bits") not in (16, 24):
        f("Only 16-bit and 24-bit measurements are supported.")
    lo, hi = float(doc.get("lowFrequencyHz", 0)), float(doc.get("highFrequencyHz", 0))
    if lo > 0 or hi > 0:
        if not math.isfinite(lo) or not math.isfinite(hi) or lo <= 0 or hi <= lo or hi > fs / 2.0 * 1.001:
            f("The sweep frequency band is invalid.")
    elif not (1 <= doc.get("octaves", 0) <= 24):
        f("The octave count is outside the supported range.")
    dur = float(doc.get("sweepDurationSeconds", 0))
    if not math.isfinite(dur) or dur <= 0 or dur > 3600:
        f("The sweep duration is invalid.")
    if doc.get("playChannel") not in ("Mono", "Left", "Right", "Stereo"):
        f("The playback channel is invalid.")
    if doc.get("measurementMode") not in ("SweepDeconvolution", "LoopbackTransfer"):
        f("The measurement mode is invalid.")
    if doc.get("timingReference", "SynchronizedLoopback") not in ("SynchronizedLoopback", "RecordedSweep"):
        f("The timing reference is invalid.")
    sweep = np.asarray(doc.get("sweepDeconvolutionRealSamples", ()), dtype=float)
    if sweep.size == 0:
        f("The sweep deconvolution impulse response contains no samples.")
    imag = doc.get("sweepDeconvolutionImaginarySamples")
    if imag is not None and len(imag) != sweep.size:
        f("Sweep deconvolution real and imaginary sample arrays have different lengths.")
    spk = doc.get("sweepDeconvolutionPeakIndex")
    if not isinstance(spk, int) or not (0 <= spk < sweep.size):
        f("The sweep deconvolution peak index is outside the sample array.")
    runs, acc = doc.get("averageRunCount", 1), doc.get("acceptedAverageRunCount", 1)
    if runs < 1 or acc < 1:
        f("The averaging run counts are invalid.")
    if acc > runs:
        f("Accepted averaging runs exceed requested runs.")
    transfer = doc.get("transferRealSamples")
    if transfer is not None:
        transfer = np.asarray(transfer, dtype=float)
        if transfer.size == 0:
            f("The transfer impulse response contains no samples.")
        timag = doc.get("transferImaginarySamples")
        if timag is not None and len(timag) != transfer.size:
            f("Transfer real and imaginary sample arrays have different lengths.")
    if doc.get("measurementMode") == "LoopbackTransfer" and transfer is None:
        f("Loopback transfer files must include transfer impulse response samples.")
    if transfer is not None:
        tpk = doc.get("transferPeakIndex")
        if not isinstance(tpk, int) or not (0 <= tpk < transfer.size):
            f("The transfer peak index is outside the sample array.")
    if not np.all(np.isfinite(sweep)):
        f("Sweep deconvolution impulse response sample is not a finite number.")
    if transfer is not None and not np.all(np.isfinite(transfer)):
        f("Transfer impulse response sample is not a finite number.")
    coh = doc.get("transferCoherence")
    if coh is not None:
        if transfer is None:
            f("Transfer coherence requires transfer impulse response samples.")
        if len(coh) != transfer.size // 2 + 1:
            f("Transfer coherence length does not match the transfer impulse response.")
        c = np.asarray(coh, dtype=float)
        if not np.all(np.isfinite(c)) or c.min() < 0 or c.max() > 1:
            f("Transfer coherence sample is outside the valid range.")
    return True


def check_ir_file(path):
    try:
        with open(path, encoding="utf-8-sig") as fh:
            doc = json.load(fh)
        validate_v7(doc)
        # our files additionally promise: sample 0 = loopback, and the provenance block
        src = doc.get("rewSource")
        if src is None:
            fail(f"{path}: no rewSource block (provenance)")
        ok(f"{os.path.relpath(path, ROOT)}: v{doc['version']} {doc['sampleRate']} Hz, "
           f"{len(doc['transferRealSamples'])} samples, peak {doc['transferPeakIndex']}")
    except Exception as e:  # noqa: BLE001
        fail(f"{path}: {type(e).__name__}: {e}")


def check_rta_file(path):
    n = 0
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("#") or not line.strip():
                    continue
                a, b = line.split("\t")
                float(a), float(b)
                n += 1
        if n < 10:
            fail(f"{path}: only {n} data lines")
        else:
            ok(f"{os.path.relpath(path, ROOT)}: {n} points")
    except Exception as e:  # noqa: BLE001
        fail(f"{path}: {type(e).__name__}: {e}")


def check_dataset(path):
    print(f"dataset {os.path.relpath(path, ROOT)}")
    for name in ("README.md", "manifest.json"):
        if not os.path.exists(os.path.join(path, name)):
            fail(f"{path}: missing {name}")
    mpath = os.path.join(path, "manifest.json")
    if os.path.exists(mpath):
        m = json.load(open(mpath, encoding="utf-8"))
        for key, entry in (m.get("files") or {}).items():
            for sub in ("ir-v7", "ir-v7-compensated"):
                p = os.path.join(path, sub, entry.get("file", key + ".json"))
                if os.path.isdir(os.path.join(path, sub)) and not os.path.exists(p):
                    fail(f"{path}: manifest names {sub}/{entry.get('file')} which is missing")
        for key, entry in (m.get("rta") or {}).items():
            p = os.path.join(path, entry.get("file", ""))
            if not os.path.exists(p):
                fail(f"{path}: manifest names {entry.get('file')} which is missing")
    for sub in ("ir-v7", "ir-v7-compensated"):
        for p in sorted(glob.glob(os.path.join(path, sub, "*.json"))):
            check_ir_file(p)
    for p in sorted(glob.glob(os.path.join(path, "rta-mmm", "*.txt"))):
        check_rta_file(p)
    ds = os.path.join(path, "dsp-state.json")
    if os.path.exists(ds):
        try:
            json.load(open(ds, encoding="utf-8"))
            ok("dsp-state.json parses")
        except Exception as e:  # noqa: BLE001
            fail(f"{ds}: {e}")


def check_index():
    print("index.json")
    idx = json.load(open(os.path.join(ROOT, "index.json"), encoding="utf-8"))
    for d in idx.get("datasets", []):
        p = os.path.join(ROOT, d["path"])
        if not os.path.isdir(p):
            fail(f"index: dataset path missing {d['path']}")
        if not os.path.exists(os.path.join(ROOT, d.get("carDoc", ""))):
            fail(f"index: carDoc missing for {d['id']}")
        # A channel is proved by the file its dataset actually declares: an
        # impulse-response set owes ir-v7/<ch>.json, an RTA-only set owes
        # rta-mmm/<ch>.txt. A set declaring both owes both.
        formats = d.get("formats", [])
        expected = []
        if "resonalyze-ir-v7" in formats:
            expected.append(("ir-v7", ".json"))
        if "rta-txt" in formats:
            expected.append(("rta-mmm", ".txt"))
        for ch in d.get("channels", []):
            for sub, ext in expected:
                if not os.path.exists(os.path.join(p, sub, ch + ext)):
                    fail(f"index: {d['id']} lists channel {ch} but {sub}/{ch}{ext} is missing")
        ok(f"dataset {d['id']}")
    for h in idx.get("hardware", []):
        if not os.path.exists(os.path.join(ROOT, h["path"])):
            fail(f"index: hardware path missing {h['path']}")
        else:
            ok(f"hardware {h['id']}")
    for m in idx.get("mics", []):
        for fn in m.get("files", []):
            if not os.path.exists(os.path.join(ROOT, m["path"], fn)):
                fail(f"index: mic file missing {m['path']}/{fn}")
        ok(f"mic {m['id']}")
    return idx


def main(argv):
    if argv:
        for a in argv:
            if os.path.isdir(a):
                check_dataset(a)
            else:
                check_ir_file(a)
    else:
        for name in ("LICENSE", "LICENSE-CODE", "README.md", "FORMATS.md", "CONTRIBUTING.md"):
            if not os.path.exists(os.path.join(ROOT, name)):
                fail(f"missing {name}")
        idx = check_index()
        for d in idx.get("datasets", []):
            check_dataset(os.path.join(ROOT, d["path"]))
        for p in sorted(glob.glob(os.path.join(ROOT, "hardware", "**", "measurements", "*.json"), recursive=True)):
            check_ir_file(p)
    if FAILS:
        print(f"\n{len(FAILS)} failure(s)")
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
