# Change Document — Paleo-Insolation and the Habitability Ratio under Invariant $G$

**Date:** 2026-06-29
**Status:** New material. A consequence of the invariant-$G$ adoption (see the companion
*Change Document — Adoption of Invariant $G$*). Addresses whether removing Earth's
orbital expansion leaves the early Earth too cold to be habitable. **Result: it does
not** — and the model makes a falsifiable prediction in the *favourable* direction for
the faint-young-Sun paradox. Suggested home: a new section in **T9 (Orbital Dynamics)**
or a short new topic file **T-paleo / "Habitability and the Faint Young Sun"**, with a
status-table row in Core Principles.

---

## 1. The worry

Adopting invariant $G$ removes orbital expansion ($r\propto c^2$ → $r=$ const; companion
change doc). Two effects then seem to make the early Earth colder, with nothing to
compensate:
- **Lower solar luminosity in the past.** $L\propto c^4$ and $c$ was smaller, so the Sun
  was intrinsically fainter.
- **No orbital compensation.** Previously, orbital expansion ($r\propto c^2$) exactly
  cancelled the luminosity drop to keep received flux constant ($F=L/4\pi r^2\propto c^4/(c^2)^2=c^0$). With static orbits that cancellation is gone, so received flux
  drifts as $F\propto c^4$ — apparently leaving a frozen early Earth.

Taken at face value this looks like a fresh refutation. It is not, because it asks the
question in fixed human units instead of in the model's own relational terms.

## 2. The correct question: a dimensionless ratio

The model is relational — every energy, length, and time is referred to $c$. "Was the
early Earth colder?" is only physically meaningful as a **dimensionless comparison**
between Earth's equilibrium temperature and the temperature scale that actually governs
habitability: the molecular energy scale of water (its freezing/boiling points). Both
scale with $c$; asking whether the numerator dropped while ignoring the denominator is a
unit artifact.

Define the **habitability ratio**
$$X \equiv \frac{T_\text{eq}}{T_\text{mol}},$$
where $T_\text{eq}$ is Earth's radiative-equilibrium temperature and $T_\text{mol}$ is
the characteristic molecular temperature of liquid water (H-bond / phase-boundary scale).
If $X$ is constant as $c$ evolves, the early Earth was equally habitable and there is no
problem. If $X$ drifts, the model makes a real paleoclimate prediction.

## 3. Model scalings used (all firm)

- Lengths $\ell\propto c^{-1}$ (Bohr radius and all atomic/solid lengths).
- Energies $E\propto c^{2}$ (Rydberg, all binding energies; $\nu\propto c^2$).
- $\hbar, e, m, k_B$ invariant ($k_B$ is a fixed energy↔kelvin conversion, so a kelvin
  temperature tracks its energy scale $\propto c^2$).
- Invariant $G$: orbital distance $d\propto c^0$ (no expansion); $G\propto c^0$.
- Stefan–Boltzmann constant $\sigma_\text{SB}=\dfrac{\pi^2 k_B^4}{60\,\hbar^3 c^2}\propto c^{-2}$ (the $c$ here is the physical, varying speed of light).

## 4. Derivation

### 4.1 Stellar luminosity $L\propto c^4$ (verified two ways)

*Route A (energy/time).* Energy radiated per unit time: energy scale $\propto c^2$;
characteristic time scale (atomic $1/\nu$, or light-crossing $\ell/c$) $\propto c^{-2}$,
so rate $\propto c^{+2}$. Hence $L\sim E/t\propto c^2\cdot c^2 = c^4$.

*Route B (surface emission).* $L = 4\pi R_\star^2\,\sigma_\text{SB}\,T_\text{eff}^4$, with
$R_\star\propto c^{-1}$ (a length), $\sigma_\text{SB}\propto c^{-2}$, and the stellar
surface temperature tracking the internal atomic energy scale $T_\text{eff}\propto c^2$:
$$L \propto (c^{-1})^2\,(c^{-2})\,(c^{2})^4 = c^{-2-2+8} = c^{4}.\qquad\checkmark$$

Both routes agree: $L\propto c^4$.

### 4.2 Earth's equilibrium temperature $T_\text{eq}\propto c^{3/2}$

Radiative balance (absorbed sunlight = thermal re-emission):
$$\frac{L}{4\pi d^2}\,\pi R_E^2\,(1-A) = 4\pi R_E^2\,\sigma_\text{SB}\,T_\text{eq}^4.$$
**The Earth's radius $R_E$ cancels** (absorbing cross-section $\pi R_E^2$ vs radiating
area $4\pi R_E^2$ — the factor of 4 is independent of $R_E$). This is the precise reason
the "smaller/larger Earth" intuition does **not** enter the equilibrium temperature: body
size drops out of the energy balance. Solving,
$$T_\text{eq}^4 = \frac{L\,(1-A)}{16\pi\,\sigma_\text{SB}\,d^2}
\propto \frac{c^4}{c^{-2}\cdot c^0} = c^{6}
\;\Longrightarrow\; T_\text{eq}\propto c^{3/2}.$$
(The albedo $A$ is dimensionless and treated as $c$-independent.)

### 4.3 The molecular (water) temperature scale $T_\text{mol}\propto c^2$

Water's freezing and boiling points are set by hydrogen-bond / molecular binding
energies, which scale like all energies, $\propto c^2$. In kelvin ($k_B$ fixed),
$T_\text{mol}\propto c^2$.

### 4.4 The habitability ratio

$$\boxed{\,X = \frac{T_\text{eq}}{T_\text{mol}} \propto \frac{c^{3/2}}{c^{2}} = c^{-1/2}.\,}$$

$X$ is **not** constant — it scales as $c^{-1/2}$. In the past, $c$ was smaller, so $X$
was **larger**: the early Earth was **warmer relative to water's freezing point**, not
colder. The lower solar flux is real, but it is *outweighed* because the molecular
yardstick (the freezing point itself) dropped faster ($\propto c^2$) than the equilibrium
temperature ($\propto c^{3/2}$).

## 5. Magnitude over Earth history

The model's horizon rate gives a fractional $c$ change over a lookback $t$ of
$\Delta c/c\sim H_0^{\text{hor}}\,t$, with $H_0^{\text{hor}}=H_0^{\text{obs}}/2$. Over
$t\approx4.5$ Gyr (age of the Earth):
$$\frac{\Delta c}{c}\sim H_0^{\text{hor}}\cdot 4.5\ \text{Gyr}\approx 0.16,
\qquad \frac{c_\text{past}}{c_\text{now}}\approx 0.84.$$
Then
$$\frac{X_\text{past}}{X_\text{now}} = \left(\frac{c_\text{past}}{c_\text{now}}\right)^{-1/2}
\approx (0.84)^{-1/2}\approx 1.09,$$
a ~9% larger habitability ratio 4.5 Gyr ago. With $T_\text{eq}\approx255$ K today, this
corresponds to of order ~20 K of effective warming *relative to the freezing point* in
the deep past (order-of-magnitude; the exact figure depends on the age/$H_0$ structure
and on how $X$ is converted to a temperature offset).

## 6. The faint-young-Sun connection (a favourable, falsifiable prediction)

The standard **faint young Sun paradox**: stellar models give the Sun ~25–30% fainter
~4 Gyr ago, which (with today's atmosphere) would freeze Earth's oceans — yet the
geological record shows persistent liquid water, conventionally requiring large early
greenhouse forcing.

This model's $X\propto c^{-1/2}$ pushes in **exactly the right direction**: it makes the
early Earth *warmer relative to the freezing point*, partially offsetting the faint young
Sun **without** invoking as much greenhouse gas. This is a genuine, distinctive,
falsifiable prediction — testable against the paleotemperature and paleo-greenhouse
record — and it is a *consequence* of the relational principle (both flux and molecular
yardstick scale with $c$), not a fitted patch.

**Direction is robust; magnitude is not yet pinned.** Whether the effect is large enough
to *fully* resolve the paradox (vs merely ease it) requires a quantitative comparison to
the reconstructed early-Earth temperature and greenhouse budget. The sign is the strong
claim; the size is open.

## 7. Caveats (load-bearing assumptions)

1. **$L\propto c^4$ is the pivotal input.** Verified two ways here (§4.1), but real
   stellar luminosity depends on opacity and nuclear-reaction rates that also carry
   $c$-dependence. A full stellar-structure treatment of $L(c)$ could shift the exponent;
   if it does, $X$'s exponent shifts and in principle the sign could change. The present
   result is "right sign, plausible size," not "established."
2. **Scaling-argument status.** This is a dimensional/scaling result, the same *class* of
   argument that produced a spurious $\sqrt M$ elsewhere this programme. The logic here is
   cleaner (an equilibrium energy balance, not a coherence estimate) and the body-size
   cancellation is exact, but the honest standard is met only by a worked stellar-
   structure + radiative-balance calculation. Flagged accordingly.
3. **Albedo and atmosphere held fixed.** $A$ and atmospheric composition are treated as
   $c$-independent; a fuller treatment would let cloud/ice-albedo feedbacks respond to the
   shifting $X$.
4. **$k_B$ as a fixed conversion.** Temperatures are taken to track energy ($\propto c^2$)
   with $k_B$ constant; this is the natural choice but is part of the unit convention and
   should be stated explicitly wherever the result is used.

## 8. Net

Invariant $G$ **survives** the paleo-insolation test. Removing orbital expansion looked
like it should refreeze the early Earth, but in the model's own relational terms the
governing quantity is the dimensionless ratio $X=T_\text{eq}/T_\text{mol}\propto c^{-1/2}$,
which makes the early Earth *warmer* relative to liquid-water conditions — the correct
direction to **ease the faint-young-Sun paradox**. This converts an apparent liability of
the invariant-$G$ choice into a falsifiable prediction. The principal open task is a
quantitative stellar-structure derivation of $L(c)$ to firm up both the exponent and the
magnitude.
