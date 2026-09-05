# Pre-registration: `VFR PK 420 Hz −3 dB`, written before the listening

Registered by the `research` role on **2026-09-03**, **before** the listener heard
anything. The point of the file is that the ear's verdict can be **checked** rather than
recounted.

The original was written in Ukrainian and is reproduced verbatim at the end, so this
translation (made 2026-09-05, for publication) can be checked against it. Nothing in the
prediction was changed after the listening — the verdict is appended below it, as it was
in the original.

---

## State and move

Base chain `v_021` plus variant C, and **together with it** a right-side level
correction: `VFR PK 420 Hz −3 dB Q 1.0`. It is that correction that is being listened to.

## What two independent pipelines already agreed on

| | research | tuning session |
|---|---|---|
| centre ITD, 300–800 Hz, `v_021` | +20 µs | **+15 µs** |
| centre interaural coherence `ρ` | 0.77 | **0.78** |
| level at 315 / 400 / 500 / 630 Hz | +2.15 / +2.93 / +3.48 / −5.21 dB (measured) | +2.1 / +2.9 / +3.2 / −5.3 (modelled) |

Variant C by itself does not move time (Δ −1 µs) and adds about +1 dB to the right at
400/500 Hz. The correction `VFR PK 420 −3` gives a centre Δ of **+43 µs** and `ρ`
0.78 → 0.83.

## The prediction the ear will test

1. **Direction.** The centre in the **300–600 Hz** band should move **left, toward the
   middle** — it currently sits right by +2.2…+3.5 dB, and the cut removes level from the
   right side. This is the body of a male voice, the snare, the bottom of a bass guitar.
2. **Selectivity.** The top of the voice, sibilants and cymbals should **not** move. If
   the whole image moves, the model is describing something other than what happens.
3. **Focus.** `ρ` rises 0.78 → 0.83, so the centre should become slightly **tighter**, not
   only displaced. A small effect; not hearing it is not a refutation.

## What we are NOT predicting, and it matters

**The +43 µs change in time is neither an improvement nor a problem.** The spread of the
centre's ITD across ear heights in this band is **σ 60 µs**. The move shifts time by less
than sitting down differently does. It cannot be read as a result; it is here as a side
effect of a level move, not as a target.

## What would make this a refutation

- the centre in 300–600 Hz **does not move**, or moves **right**;
- the **whole** image moves, top included;
- **focus gets worse**.

Any of those is a finding and is recorded as it is. Numbers are not rewritten to match the
ear.

## What we ask to be sent back with the verdict

- the **predicted ILD change** in 300–600 Hz from this move, so the ear can be compared
  against magnitude and not only direction;
- the Arbiter's words as spoken.

---

# Verdict: REFUTED by ear, 2026-09-04

Recorded by `research` on 2026-09-05 from the tuning session's journal (entry
`2026-09-04T07:52:37+00:00`). Hardware unchanged, base `v_021`.

**What was heard was not a shift but a break-up.** The images pulled apart instead of
moving. The Arbiter, verbatim with translation:

> "At −3 dB, track 8: the left-centre image went left, but there is no sound from the
> right-centre; the right-centre went right, no sound in the left-centre."
> — [Verbatim log: «−3 дБ AYA №8 — ЛЦ ушел в лево, но немє звуку з ПЦ, ПЦ — пішов в
> право, немає звуку в ЛЦ»]

> "The −6 dB variant is worse still." — [Verbatim log: «Т1б (−6) — ще гірше»]

> On the `VFL −3` control: "on the whole, everything falls apart" — [Verbatim log:
> «в цілому все розвалюється»]; "on track 25 the right-centre image drifts right at some
> point and comes back" — [Verbatim log: «25 ПЦ в якийсь момент пливе в право і
> вертається»]

That is exactly two of the three refutation criteria this file registered in advance: the
whole image moved, and focus got worse.

| prediction | ear |
|---|---|
| 1. centre 300–600 Hz moves left | **no** — the images stretched apart, the centre did not travel |
| 2. the top does not move | **yes, confirmed** |
| 3. `ρ` 0.78 → 0.83, focus improves | **no, the opposite** — "everything falls apart" |

So the model's **band selectivity was confirmed by ear**: a correction at 420 Hz did stay
in its band and did not drag the top with it. What was not confirmed is the next link —
that a change in ILD in that band moves the **position** of the image. The model computes
the physical shift correctly; the shift does not mean what we assumed.

**And a wider class closed the same day.** A 34-measurement series found no stable
left-to-right level asymmetry to steer with: mean L−R over 250–6300 Hz = −0.19 dB,
band-by-band range 8.0 dB, and the same difference computed two ways (MMM in the head zone
versus a swept sine from the fixed tripod point) correlates only **+0.42** and diverges by
up to **9.2 dB**. So the band-wise side difference above ~500 Hz is a property of head
position, not of the system. All four level moves attempted that day traded one defect for
another.

**A side finding, not ours but belonging here:** the `VFL −3` control partly worked on
track 8 — bass echoes on the right "stopped interfering" — at the cost of pushing the
right-centre image further right. The move was not kept, but it is the first time a
direction was named for that track.

---

## Original, as registered (Ukrainian)

The file above is a translation. This is the text as written on 2026-09-03 and 2026-09-05.

```
# Передбачення ДО прослуховування: VFR PK 420 −3 dB

Записано роллю `research` 2026-09-03, **до** того як тюн-сесія слухала. Сенс файла в
тому, щоб вердикт вуха можна було перевірити, а не переказати.

## Стан і хід

База `v_021` + варіант C, і **разом із ним** рівнева поправка правого борту:
`VFR PK 420 −3 dB`. Слухається перша саме поправка.

## Що вже зійшлось на числах (двома незалежними пайплайнами)

| | research | тюн-сесія |
|---|---|---|
| ITD центру, 300–800, `v_021` | +20 мкс | **+15 мкс** |
| `ρ` центру | 0,77 | **0,78** |
| рівень 315/400/500/630 | +2,15 / +2,93 / +3,48 / −5,21 dB (вимір) | +2,1 / +2,9 / +3,2 / −5,3 (модель `v_021`) |

Варіант C сам по собі часу не рухає (Δ −1 мкс) і додає ~+1 dB праворуч на 400/500.
Поправка `VFR PK 420 −3` дає Δ центру **+43 мкс** і `ρ` 0,78 → 0,83.

## Передбачення, яке перевіряється вухом

1. **Напрям.** Центр у смузі **300–600 Гц** має поїхати **ліворуч, до середини** — бо
   там він зараз стоїть праворуч на +2,2…+3,5 dB, а хід прибирає рівень саме з правого
   борту. Це тіло чоловічого голосу, малий барабан, низ бас-гітари.
2. **Вибірковість.** Верх голосу, сибілянти й тарілки **не мають зрушити**. Якщо поїде
   весь образ цілком — модель описує не те, що відбувається.
3. **Фокус.** `ρ` росте 0,78 → 0,83, тобто центр має стати трохи **зібранішим**, не
   лише зміщеним. Ефект дрібний; якщо його не чути — це не спростування.

## Чого НЕ передбачаємо, і це важливо

**Зміна часу +43 мкс — не покращення й не проблема.** Розкид ITD центру по висотах вуха
в цій смузі — **σ 60 мкс**. Тобто хід рухає час менше, ніж його зсуває власне посадка
голови. Читати цей +43 як результат не можна; він тут як побічний ефект рівневого ходу,
не як ціль.

## Що зробить це спростуванням

- центр у 300–600 **не зрушив** або поїхав **праворуч**;
- зрушив **увесь** образ, включно з верхом;
- стало **гірше за фокусом**.

Будь-що з цього — знахідка, і записується як є. Числа під слух не переписуються.

## Вердикт: СПРОСТОВАНО вухом, 2026-09-04

**Почуто не зсув, а розпад.** Образи розʼїжджаються замість рухатись. Дослівно
Арбітра: «−3 дБ AYA №8 — ЛЦ ушел в лево, но немє звуку з ПЦ, ПЦ — пішов в право,
немає звуку в ЛЦ»; «Т1б (−6) — ще гірше»; на контролі `VFL −3` — «в цілому все
розвалюється», «25 ПЦ в якийсь момент пливе в право і вертається».

Це рівно два з трьох критеріїв спростування, які цей файл записав наперед: поїхав
увесь образ, і стало гірше за фокусом.

| передбачення | вухо |
|---|---|
| 1. центр 300–600 їде ліворуч | **ні** — образи розтягнулись, центр не поїхав |
| 2. верх (сибілянти, тарілки) не рухається | **так, підтверджено** |
| 3. `ρ` 0,78 → 0,83, фокус кращає | **ні, навпаки** — «все розвалюється» |

Тобто **смугова вибірковість моделі підтверджена вухом**: правка на 420 Гц справді
лишилась у своїй смузі й не потягла верх. Не підтвердилась інша ланка — що зміна ILD
у цій смузі рухає **позицію** образу. Модель рахує величину правильно; величина не
означає того, що ми думали.
```
