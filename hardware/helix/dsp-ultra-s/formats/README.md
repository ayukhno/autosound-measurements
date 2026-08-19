# The formats REW and the PC-Tool exchange

Real files, kept as they came out, because a format claim without a file is a rumour.

| file | what it is | how it was produced |
|---|---|---|
| `atf_full_eq_sample.txt` | the Audiotec-Fischer **"Full EQ (30 bands)" bank** — the tab-separated block the HELIX / MATCH / BRAX PC-Tool imports into one channel: 18 bells, both `LS_Q` / `HS_Q` shelves, ten empty `None` slots | REW with *Equaliser = Audiotec Fischer / Full EQ (30 bands)*, **EQ window → copy the filters to the clipboard** (2026-07) |
| `atf_bank_with_modal_rows.txt` | the same bank holding REW's **`Modal`** rows next to a plain `PK` — the evidence that a modal filter travels in this layout as the bell it realizes | same route, REW 5.40 Beta 132, 2026-08-19 |
| `rew_filter_settings_text.txt` | REW's **own** filter-settings text (`File → Export → Filter settings as text`) for the very same filters — a different format, human-readable, not what the PC-Tool imports | REW 5.40 Beta 132, 2026-08-19 |

Two things worth knowing before writing a reader:

- **The bank is the clipboard, not the file menu.** `File → Export → Filter settings as text` writes REW's own layout (`rew_filter_settings_text.txt`); the tab-separated device bank comes from the EQ window's copy-to-clipboard with the device equaliser selected.
- **`Modal` rows carry a Q and a T60.** REW's modal filter is parameterised by Fc / gain / T60 target (its API refuses a `q`), but into this bank it writes the bell it realizes: `Modal  120.0  -6.0  Q 11.59  BW 10.35  T60 300`. That Q is not a textbook T60 identity — it lands on `π·f0·T60/ln(1000) · 10^(gain/40)` for both rows here, and measuring REW's own EQ response for the 120 Hz row returns 11.59 as well. A reader should take the Q column and ignore the T60; the processor has no modal slot.
