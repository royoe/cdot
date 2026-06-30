# Change Document — Paleo-Insolation and the Habitability Ratio under Invariant $G$

**Date:** 2026-06-29 (revised after a factor-audit)
**Status:** New material. A consequence of the invariant-$G$ adoption (see the companion
*Change Document — Adoption of Invariant $G$*). Addresses whether removing Earth's
orbital expansion leaves the early Earth too cold to be habitable. **Result: it does
not** — and the model supplies a $c$-dependent shift to the habitability ratio in the
*favourable* direction for the faint-young-Sun paradox. Suggested home: a new section in
**T9 (Orbital Dynamics)** or a short new topic file **"Habitability and the Faint Young
Sun"**, with a status-table row in Core Principles.

> **Revision note.** An earlier draft of this document derived $X\propto c^{-1/2}$ from a
> luminosity scaling $L\propto c^4$. That was **wrong**: it used a stellar radius scaled
> as an atomic length ($R_\star\propto c^{-1}$). A factor-audit corrected this. The
> bolometric luminosity is **radius-independent** (set by hydrostatic equilibrium with
> radiation pressure), so the radius drops out entirely; the correct $c$-scaling of
> luminosity at fixed composition is $L\propto c^{0}$, giving $X\propto c^{-3/2}$. The
> *direction* is unchanged (early Earth warmer relative to freezing); the magnitude is
> larger. The error and its correction are recorded in §4.1 for transparency.

---

## 1. The worry

Adopting invariant $G$ removes orbital expansion ($r\propto c^2$ → $r=$ const; companion
change doc). Naively this seems to refreeze the early Earth: the past Sun was fainter and
there is no longer an expanding orbit to compensate. The worry is a unit artifact — it
tracks the received flux in fixed human units while ignoring that the molecular
temperature scale that defines "frozen" also moves with $c$.

## 2. The correct question: a dimensionless ratio

The model is relational. "Was the early Earth colder?" is meaningful only as a
**dimensionless comparison** between Earth's equilibrium temperature and the temperature
scale governing habitability — the molecular energy scale of water (freezing/boiling).
Define the **habitability ratio**
$$X \equiv \frac{T_\text{eq}}{T_\text{mol}}.$$
Constant $X$ ⇒ equally habitable early Earth (no problem). Drifting $X$ ⇒ a real,
testable paleoclimate prediction.

## 3. Model scalings used (all firm)

- Lengths $\ell\propto c^{-1}$; energies $E\propto c^{2}$ ($\nu\propto c^2$).
- $\hbar, e, m, k_B$ invariant ($k_B$ fixed energy↔kelvin conversion ⇒ kelvin temps
  track energy $\propto c^2$).
- Invariant $G$: orbital distance $d\propto c^0$; $G\propto c^0$.
- Radiation constant $a=\dfrac{\pi^2 k_B^4}{15\,\hbar^3 c^3}\propto c^{-3}$.
- Stefan–Boltzmann $\sigma_\text{SB}=\dfrac{\pi^2 k_B^4}{60\,\hbar^3 c^2}\propto c^{-2}$.
- Thomson opacity (electron scattering, dominant in hot interiors):
  $\kappa_\text{es}=\sigma_T/m_p$, $\sigma_T\propto r_e^2$,
  $r_e=\dfrac{e^2}{4\pi\epsilon_0 m c^2}\propto c^{-1}$ (since $\epsilon_0\propto c^{-1}$),
  so $\sigma_T\propto c^{-2}$ and $\kappa_\text{es}\propto c^{-2}$.

## 4. Derivation

### 4.1 Stellar luminosity is radius-independent: $L\propto c^0$

**Why radius drops out.** Bolometric luminosity is fixed by hydrostatic equilibrium (with
radiation pressure), not by the stellar radius. The earlier draft's $L\propto c^4$ came
from a surface relation $L=4\pi R_\star^2\sigma_\text{SB}T_\text{eff}^4$ with $R_\star$
mis-scaled as an atomic length ($c^{-1}$); this was the error. The correct treatment uses
the radius-independent (Eddington) radiative luminosity.

**The standard radiative mass–luminosity relation** (electron-scattering opacity), which
contains no radius:
$$L \propto \frac{\mu^4 m_p^4}{k_B^4}\,\frac{a\,c}{\kappa}\,G^4 M^3.$$
Only $a$, $c$, and $\kappa$ carry $c$-dependence in this model:
$$L \propto a\,c\,\kappa^{-1} \propto c^{-3}\cdot c^{+1}\cdot c^{+2} = c^{0}.$$
**Luminosity is $c$-invariant** at fixed composition — a clean cancellation between the
radiation constant ($a\propto c^{-3}$), the explicit $c$, and the opacity
($\kappa\propto c^{-2}$).

### 4.2 The faint-young-Sun brightening is a *separate*, composition-driven effect

The standard ~25–30% solar brightening over $\sim$4 Gyr is **not** a $c$-scaling effect.
It arises from core composition evolution: H→He raises the mean molecular weight $\mu$,
the core contracts and heats, the nuclear reaction rate rises, and $L$ increases — at
essentially fixed fundamental constants over the relevant timescale. This stands on its
own and is independent of the model. The model's contribution (§4.3) is a *separate*,
additive $c$-dependent shift of the habitability ratio.

### 4.3 Equilibrium temperature and the habitability ratio

Radiative balance (Earth radius $R_E$ cancels — absorbing $\pi R_E^2$ vs radiating
$4\pi R_E^2$):
$$T_\text{eq}^4 = \frac{L\,(1-A)}{16\pi\,\sigma_\text{SB}\,d^2}
\propto \frac{c^{0}}{c^{-2}\cdot c^{0}} = c^{2}
\;\Longrightarrow\; T_\text{eq}\propto c^{1/2}.$$
Water's molecular temperature scale (H-bond/binding energies $\propto c^2$, $k_B$ fixed):
$T_\text{mol}\propto c^{2}$. Hence
$$\boxed{\,X=\frac{T_\text{eq}}{T_\text{mol}}\propto \frac{c^{1/2}}{c^{2}} = c^{-3/2}.\,}$$
$X\propto c^{-3/2}$: in the past ($c$ smaller) $X$ was **larger** — the early Earth was
**warmer relative to water's freezing point**, not colder.

## 5. Magnitude over Earth history

With $\Delta c/c\sim H_0^{\text{hor}}t$ and $H_0^{\text{hor}}=H_0^{\text{obs}}/2$, over
$t\approx4.5$ Gyr: $c_\text{past}/c_\text{now}\approx0.84$. Then
$$\frac{X_\text{past}}{X_\text{now}}=\left(\frac{c_\text{past}}{c_\text{now}}\right)^{-3/2}
\approx(0.84)^{-3/2}\approx 1.30,$$
a **~30%** larger habitability ratio 4.5 Gyr ago (vs the erroneous ~9% in the earlier
draft). Order-of-magnitude; the exact figure depends on the age/$H_0$ structure.

## 6. The faint-young-Sun connection (favourable, falsifiable — and *supplementary*)

The standard paradox: the Sun was ~25–30% fainter ~4 Gyr ago (composition effect, §4.2),
which with today's atmosphere would freeze the oceans, yet the record shows liquid water
— conventionally requiring large early greenhouse forcing.

The model adds a *separate*, additive effect: $X\propto c^{-3/2}$ makes the early Earth
~30% warmer relative to freezing. **The model does not replace the standard explanation;
it supplements it** — reducing the greenhouse forcing the record otherwise requires. The
*direction* is the strong, robust claim; the ~30% *magnitude* is opacity-dependent (§7).
This is a genuine, distinctive, falsifiable consequence of the relational principle (both
the radiative balance and the molecular yardstick scale with $c$).

## 7. Caveats (load-bearing assumptions)

1. **Opacity choice sets the exponent.** $X\propto c^{-3/2}$ rests on **electron-
   scattering (Thomson) opacity**, $\kappa\propto c^{-2}$ — the dominant, cleanest opacity
   in hot stellar interiors, hence a reasonable primary choice. A Kramers (bound-free/
   free-free) regime scales differently and would shift the exponent. The robust claim is
   the **sign** (early Earth warmer rel. to freezing), which holds provided $L$ does not
   scale strongly positively with $c$.
2. **$L\propto c^0$ via the radius-independent relation.** This is the corrected, careful
   result (§4.1); it supersedes the earlier $L\propto c^4$. A full stellar-structure
   solution (coupling hydrostatic equilibrium, energy generation, and radiative transport
   under the model's scalings simultaneously) would confirm the exponent rigorously and is
   the recommended follow-up. Present status: clean scaling result with the dominant
   opacity, not yet a full structure calculation.
3. **Composition effect held separate.** The standard faint-young-Sun brightening (§4.2)
   is composition-driven at fixed constants and is treated as independent of and additive
   to the model's $c$-effect — not folded into the $c$-scaling.
4. **Albedo/atmosphere and $k_B$ convention.** $A$ and atmosphere held $c$-independent;
   $k_B$ a fixed energy↔kelvin conversion (stated explicitly wherever the result is used).

## 8. Net

Invariant $G$ **survives** the paleo-insolation test. In the model's relational terms the
governing quantity is $X=T_\text{eq}/T_\text{mol}\propto c^{-3/2}$ (corrected from an
earlier erroneous $c^{-1/2}$), which makes the early Earth ~30% warmer relative to
liquid-water conditions over 4.5 Gyr — the correct direction to **ease the faint-young-Sun
paradox**, as a supplement to (not a replacement for) the standard composition-driven
brightening. The result rests on radius-independent (Eddington) luminosity with electron-
scattering opacity; the sign is robust, the magnitude is opacity-dependent, and a full
stellar-structure derivation of $L(c)$ is the recommended next step.
