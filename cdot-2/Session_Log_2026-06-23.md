# Session Log — Static VSL Cosmology

**Date:** 2026-06-23
**Scope:** Foundational correction of the redshift law and its downstream
consequences; systematic recomputation of open problems; document restructuring into
v1/v2/v3.
**Companion files:** `Core_Principles_v2.md`, `Open_Problems_v2.md` (full history),
`Open_Problems_v3.md` (compacted working doc).

---

## Executive summary

This session found and fixed the single deepest error in the project: the redshift
law, which had been $1+z = c_\text{now}/c_\text{emit}$ (linear) since the first
session, is actually $1+z = (c_\text{now}/c_\text{emit})^2$ (squared) under invariant
mass. The correction propagated through every distance, age, and the supernova
comparison. A second correction — treating SNe Ia as true standard candles in proper
units — removed a phantom over-dimming that had appeared catastrophic.

**Net effect: the model looks better, not worse.** Both corrections removed
artifacts rather than adding epicycles. Three results (OP-1 age, OP-5 over-dimming,
OP-9 Etherington refutation) improved on correction. The model's remaining tension is
mild and specific: it predicts $q_0 = 1/(3P) > 0$ (gentle deceleration) where SNe show
acceleration.

---

## The main thread: redshift law correction (→ OP-11)

### How it was found

The chain started from an ontology question — what physically changes between epochs
vs. what only changes in map units. The author rejected the "only $c$-ratios are
physical" framing as ill-chosen and supplied a cleaner one: an **energy-conserving map
frame** where photon energy and frequency are genuinely conserved in flight (no energy
lost to the vacuum), and redshift is a *measurement* artifact (the modern clock runs
faster). This dissolved an ambiguity that had blocked the derivation.

### The two secure anchors

1. **Electromagnetism, exact at all epochs:** $c = 1/\sqrt{\epsilon_0\mu_0}$.
2. **Identical $\epsilon_0,\mu_0$ scaling** (polarization-alignment argument, Puthoff):
   otherwise the impedance $Z_0=\sqrt{\mu_0/\epsilon_0}$ drifts and cosmologically
   aligned polarization could not survive. Forces
   $\epsilon_0\propto\mu_0\propto K \propto c^{-1}$.

These are electromagnetism + an observational argument, **not** PV assumptions. With
$e,h,m$ invariant they force $\alpha$ invariant, Bohr radius $\propto c^{-1}$, and
atomic frequency $\nu\propto c^2$.

### The derivation (single application, no double-count)

The discipline is the GR one: gravitational redshift is the clock-rate difference
applied *once*, never multiplied by a separate wavelength-stretch. The author
explicitly flagged the double-count risk; an early attempt (building the time unit
from atomic light-crossing time) did double-count and was discarded. The clean
derivation: a spectrograph compares the photon's conserved frequency to a local
reference line, common $c_\text{now}$ cancels, and since the emitted frequency carried
$\nu_\text{emit}\propto c_\text{emit}^2$:
$$1+z = \nu_\text{ref}/\nu_\text{phot} = (c_\text{now}/c_\text{emit})^2.$$

### Why the linear law was wrong

It tacitly assumed the *emitted* frequency was epoch-independent — that an ancient
hydrogen line had the same $\nu$ as a modern one. False:
$\nu_\text{atomic}\propto c^2$.

### The unifying insight: redshift power = mass scaling

For $m\propto c^s$: $\;1+z = (c_\text{now}/c_\text{emit})^{s+2}$. The redshift power
and the mass scaling are **one degree of freedom**:
- $s=0$ (invariant mass) ⇔ squared redshift. **Current model.**
- $s=-3/2$ (PV mass) ⇔ √-redshift. (The author's old PV notebook result
  $z=\sqrt K-1$ lives here — the trivial PV branch the project departs from.)
- $s=-1$ ⇔ the discarded linear law — neither invariant nor PV; a scaling nobody
  chose. Confirms it was an unexamined assumption.

The author's two long-standing uncertainties ("linear vs squared redshift" and
"invariant vs PV mass") are therefore the **same question**. The author committed to
squared redshift / invariant mass, holding the PV-mass tension as an explicit escape
hatch to revisit later. Independent confirmation from the author's own old notes:
$z=\sqrt K-1 \Rightarrow K=(1+z)^2$ corresponds to PV mass — i.e. the old notes were
strictly PV-framework, which the project now goes beyond.

### Collateral: $G\propto c^{-2}$ is PV/Dicke-native

The audit established $G\propto K^2\propto c^{-2}$ as the value reproducing GR
weak-field — exactly OP-8's $g=-2$. So $g=-2$ is not a free selection. The earlier
"constant $G$ gives $g=+1$" argument stacked two deviations and is overridden. This
largely discharges the OP-8 "standing debt."

---

## Systematic recomputation (in order)

- **OP-1 (age):** Unchanged at $\tau = \tfrac34 H_0^{-1}\approx 10.5$ Gyr — the
  invariant-mass pivot had already set $p=2$, and the squared redshift law uses the
  same $p$. The redshift and clock-rate powers are the same quantity, automatically
  consistent. Added closed-form lookbacks: $u(z)=\tfrac{3}{2H_0}[(1+z)^{1/3}-1]$,
  $\tau(z)=\tfrac{3}{4H_0}[1-(1+z)^{-2/3}]$. Stellar-age tension downgraded to mild.
- **OP-2 ($a_0$):** Unaffected by redshift (present-epoch quantities). But the
  coefficient-2 floor gives baseline $a_0=2cH_0$, so with the old $1/2\pi$ factor the
  prediction is $cH_0/\pi\approx2.17\times10^{-10}$ — an 80% overshoot; matching needs
  $1/4\pi$. The "90% match" was always tuned through the undetermined geometric factor.
- **OP-3 (rotation curves):** Unaffected (galactic-scale, present-epoch) and
  *strengthened* — the $G\propto c^{-2}$ it relies on is now PV-native, not selected.
- **OP-5 (SN distance):** See below — the major recomputation.
- **OP-9 (conformal):** Refutation withdrawn — see below.

---

## The standard-candle correction (→ OP-5, OP-9)

The first squared-law SN recomputation gave $D_L=(1+z)^{1-1/(2P)}D_\text{proper}$ and
$q_0=4/(3P)>0$ — still wrong-signed, no improvement. Then the author raised the
decisive objection: **SNe are standard candles, and the same luminosity correction we
applied to orbit-stability / faint-young-Sun must apply here.**

Correct: in proper units all local physics is epoch-independent, so a SN Ia has
epoch-invariant proper luminosity $L_\text{std}$. The map-frame $L\propto c^{2P}$ is a
*units artifact*, not intrinsic dimming. Applying it as dimming was double-counting —
the same phantom as faint-young-Sun. With a true standard candle and only the genuine
transport factors:
$$D_L = (1+z)\,D_\text{proper}\quad\text{(clean Etherington form, no $P$-dependence).}$$

**Consequences:**
- The catastrophic $(1+z)^{5/2}$ over-dimming **never existed** — it was the units
  error. Residual at $P=2$ drops to ~0.10 mag vs ΛCDM proxy.
- The deceleration parameter improves to $q_0=1/(3P)$ — but is still **positive for
  all $P$**. No mass scaling reproduces observed acceleration under the volume law.
  This is the genuine remaining tension.
- The prior "S′ mimics acceleration, $q_0=-3/2$" result was a **linear-law artifact**
  and does not survive.

**OP-9 (Etherington):** the refutation rested on the model's $P$-dependent dimming
exponent — the units error. With it gone, the model sits *on* the Etherington line.
The verdict softens from "cleanly excluded" to "implies a decelerating
$H(z)=2H_0(1+z)^{7/6}$, the same mild $q_0$-sign tension." The model remains a genuine
rival to FLRW; the capstone hope (projection + rotation curves back-project to GR)
stays excluded.

---

## Digressions recorded

### OP-12 — Sciama relation and the mass-budget conundrum

The cosmic coincidence $c^2\sim GM_u/R_u$ is **not preserved** by the model: with
physical map quantities it drifts as $R^{-10}$, unrescuable with firm
$G\propto c^{-2}$. The apparent "exact identity" (via Hubble radius + critical mass) is just
$\rho_c$'s definition rearranged. Key clarification: the model's Machianism is the
*counting* rule $c\propto N$, which is **distinct from and incompatible with**
gravitational-potential (Sciama) Machianism — usually conflated, but this model forces
them apart.

Mass budget: removing dark matter leaves $\Omega_b\sim0.05$, but the static model has
**no Friedmann constraint**, so low density is not a flatness crisis. Price: $H_0$ and
matter density $n$ are decoupled free inputs (no Sciama link to relate them).

(Two corrections to Claude's own reasoning happened here: first wrongly calling the
critical-mass version an "identity," then wrongly claiming the Hubble radius and map
horizon diverge — they track exactly, $c/H=R/3$ for the volume law. The author caught
the conflation.)

### OP-13 — Galaxy size evolution (a consistency success)

The orbital-expansion law $r\propto c^2$ predicts galaxies intrinsically *smaller* at
high $z$ by $(1+z)^{-2/P}=(1+z)^{-1}$ at $P=2$. This sits **between** the observed
late-type ($(1+z)^{-0.75}$, van der Wel 2014; $-0.81$ JWST 0<z<9) and early-type
($(1+z)^{-1.5}$) size-evolution exponents — with no free parameter. Caveats: the model
gives one universal exponent (can't reproduce the morphology split), and ΛCDM already
explains the trend via halo growth, so this is consistency, not a unique win. Still,
it points the right way — the cleanest positive test so far, in contrast to the SN
tension.

---

## Document restructuring

- **v1:** original snapshots (author's, from prior day) — historical origin.
- **v2:** `Core_Principles_v2.md` + `Open_Problems_v2.md` — this session's full results
  with complete derivation history and superseded text preserved with obsolescence
  markers.
- **v3:** `Open_Problems_v3.md` — compacted (1454 → ~135 lines), open points only,
  numbers preserved, self-contained settled-foundation header.
- **OP-10:** proposed (unit/ontology consistency) but never written; absorbed into
  OP-11. Number intentionally vacant.

LaTeX hygiene maintained throughout: after every edit, a delimiter-balance check
(double-dollar count even, single-dollar count even) and a wrapped-inline-math check,
with fixes applied before presenting. Known minor render issue: inline math inside table cells in the v2
archives may render imperfectly in some viewers; v3 has no table-math.

---

## State at session end

**Settled foundation:** static flat space; $c\propto N\propto R^3$; invariant mass;
$\epsilon_0\propto c^{-1}$ (EM-forced); $\nu\propto c^2$; $G\propto c^{-2}$
(PV-native); squared redshift $1+z=(c_\text{now}/c_\text{emit})^2$; proper age
$\approx10.5$ Gyr.

**The one make-or-break open question:** does any non-volume horizon law (S′,
$c\propto R^{2/3}$) give $q_0<0$ to match observed acceleration? The volume law cannot.
This is the next calculation and determines whether any version of the model is
viable against SN data.

**Other open:** OP-2 ($a_0$ coefficient), OP-4 ($\dot\alpha$ — never converged), OP-6
(genesis/asymmetry, speculative), OP-12 (what pins $n$). Minor cleanups: OP-7 $s$-fit
and OP-9 "fork" text still cite superseded linear-law results (conclusions corrected
inline). Needed eventually: a real Pantheon+ fit to measure $s$ directly.

**On parallelizing (author's note):** the multi-agent exploration is deferred. The
foundation is still settling, and this session's progress depended on tight
error-catching scrutiny; parallel branch-exploration would need that rigor built in
first.
