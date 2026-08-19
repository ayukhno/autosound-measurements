# autosound-measurements

Car-audio measurements you can actually compute on: per-driver, **loopback-referenced** impulse
responses of real car cabins on one absolute time base, the moving-mic RTA curves next to them, the
DSP state the ear finally accepted — and, separately, **hardware facts** about DSP processors and
microphones that were established by measurement rather than read off a forum.

The data repository of [autosound-tuning-skill](https://github.com/ayukhno/autosound-tuning-skill)
(a REW-driven car-audio tuning method written for AI coding agents) and
[Autosound TCC](https://github.com/ayukhno/autosound-tcc) (its desktop front-end), made public so
that other tools — first of all [Resonalyze](https://github.com/DIMOSUS/Resonalyze), whose
impulse-response format the cabin sets are written in — can run on the same cabins and the
methods can be compared on data instead of opinions.

**License:** data **CC BY 4.0** ([`LICENSE`](LICENSE)); the few scripts **MIT**
([`LICENSE-CODE`](LICENSE-CODE)). Cite as *"autosound-measurements (ayukhno), CC BY 4.0"* with a
link to the set you used.

## What is here

| path | contents |
|---|---|
| [`cars/`](cars/) | one directory per cabin (`<make-model-body-drive>`, no VIN, no plates), a `CAR.md` with the install and the rig, and one directory per measurement session (`<date>_<set>`) |
| [`hardware/`](hardware/) | facts about processors / interfaces / amplifiers that hold on the bench, each with the measurement behind it |
| [`mics/`](mics/) | microphone calibration files as used, with their provenance |
| [`FORMATS.md`](FORMATS.md) | the file formats used and how to read them (Resonalyze IR JSON v7, RTA text, `dsp-state.json`, `manifest.json`) |
| [`index.json`](index.json) | a machine-readable catalogue of everything above, for tools |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | how to add a cabin or a hardware fact, and what a set must contain |
| [`tools/check.py`](tools/check.py) | the validator CI runs on every push (formats, manifests, index) |

## Cabins

| cabin | session | channels | rate | what is in it |
|---|---|---|---|---|
| [VW Passat B8 sedan, LHD](cars/vw-passat-b8-sedan-lhd/CAR.md) | [2026-06-15 front set 01](cars/vw-passat-b8-sedan-lhd/2026-06-15_front-set-01/) | sub · woofers L/R · mids L/R · tweeters L/R · centre (8) | 96 kHz | transfer IRs raw and protective-HPF-compensated (Resonalyze v7), moving-mic RTA per channel, two DSP states (attested v1, current) |

## Hardware facts

| device | facts |
|---|---|
| [Helix DSP Ultra S](hardware/helix/dsp-ultra-s/FACTS.md) | AP2 all-pass = textbook 2nd order; LS_Q/HS_Q shelves = RBJ S=1; delays of the virtual and the output layer SUM; 30 PEQ bands per channel, gain separate; the PC-Tool "Full EQ (30 bands)" bank sample; bell-Q at ±12 dB pending |

## How the cabin sets are made

Loopback-referenced exponential sweeps in REW (timing reference = a physical loopback on the same
interface), pulled over REW's API **unnormalised** and written as Resonalyze's impulse-response
JSON by `rew_tool/resonalyze_ir.py` of the skill — sample 0 of every transfer IR is the loopback
arrival, levels are fractions of full scale, nothing rounded in time. Each set's `README.md` and
`manifest.json` say exactly what was measured, how, and what every number means; `FORMATS.md`
has the reader's view.

## Contributing

A cabin set from another car — any processor, any mic — is what this repository is for. See
[`CONTRIBUTING.md`](CONTRIBUTING.md): what to measure, how to name things, what not to include
(anything that identifies a person or a specific vehicle), and the CC BY 4.0 agreement.
Contact: ayukhno@gmail.com · issues here.
