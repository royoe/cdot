# T18 — Stellar Flux and the Habitability Ratio

*Note: this topic is a scaling-argument analysis. The key results ($L\propto c^0$,
$F\propto c^0$, $X\propto c^{-3/2}$) rest on the radius-independent radiative
mass–luminosity relation with electron-scattering opacity. The sign of the habitability
shift is robust; the magnitude is opacity-regime-dependent. A full stellar-structure
derivation of $L(c)$ is the primary open calculation.*

---

## Observational Background: The Faint Young Sun Paradox

Solar models predict that the Sun has brightened by approximately 30% over the last
4.5 Gyr, starting from about 70% of its current luminosity at formation. Yet geological
evidence — including banded iron formations, sedimentary rocks, and fossil evidence —
shows that liquid water was present on Earth's surface at least 3.8 Gyr ago, when the
Sun was considerably fainter than today.

Under the Sun's current luminosity, the early Earth (with its primordial $\sim10\%$
higher CO₂ atmosphere) would have been frozen at early epochs. But with 70% of current
luminosity and no additional greenhouse effect, the mean surface temperature would be
well below freezing for the first $\sim1$–$2$ Gyr. The geological record contradicts
this. This is the **faint young Sun paradox** (Sagan & Mullen 1972).

Standard resolutions invoke a thicker early greenhouse atmosphere (CO₂, CH₄, N₂O).
These are possible but require specific atmospheric evolution histories.

---

## Stellar Luminosity: $L \propto c^0$

Under invariant mass and composition, bolometric luminosity is fixed by the balance
between hydrostatic equilibrium and radiative transport — **not** by the stellar radius.
The stellar radius drops out of the mass–luminosity relation entirely.

**The standard radiative mass–luminosity relation** (electron-scattering opacity)
contains no $R_\star$:
$$L \propto \frac{\mu^4 m_p^4}{k_B^4}\,\frac{a\,c}{\kappa}\,G^4 M^3.$$
This follows from eliminating $R_\star$ between hydrostatic equilibrium
($T_c \sim GM\mu m_p/(k_B R_\star)$) and radiative transport; $R_\star$ cancels exactly.
Only $a$, the explicit $c$, and $\kappa$ carry $c$-dependence:

| Factor | Derivation | Scaling |
|---|---|---|
| $a$ | $a = \pi^2 k_B^4/(15\hbar^3 c^3)$, $k_B/\hbar$ invariant | $c^{-3}$ |
| $c$ | explicit | $c^{+1}$ |
| $\kappa^{-1}_\text{es}$ | $r_e = e^2/(4\pi\epsilon_0 mc^2)\propto c^{-1}$, $\sigma_T\propto r_e^2\propto c^{-2}$, $\kappa=\sigma_T/m_p$ | $c^{+2}$ |
| $G^4 M^3 \mu^4 m_p^4/k_B^4$ | all invariant | $c^0$ |

$$L \propto c^{-3}\cdot c^{+1}\cdot c^{+2} = c^0.$$

**Luminosity is $c$-invariant** at fixed composition — a three-way cancellation between
the radiation constant ($a\propto c^{-3}$), the propagation speed ($c^{+1}$), and the
opacity ($\kappa\propto c^{-2}$).

**Why earlier routes gave $c^4$ — and why they were wrong.**

Route A used $L \sim E \cdot \nu \propto c^2 \cdot c^2 = c^4$. Route B used
$L = 4\pi R_\star^2\sigma_\text{SB}T_\text{eff}^4$ with $R_\star \propto c^{-1}$
(atomic Bohr-radius scaling) and $T_\text{eff} \propto c^2$ (Wien law with
$\nu\propto c^2$), consistently giving $c^4$. Both routes share the same hidden
assumption: that $T_\text{eff}$ tracks the atomic energy scale ($\propto c^2$). This
is unjustified — stellar surface temperature is set by the stellar structure, not by
atomic scales. The correct $T_\text{eff}$ from the mass–luminosity relation (with
$R_\star\propto c^{-1}$ and $\sigma_\text{SB}\propto c^{-2}$) is:
$$T_\text{eff}^4 = \frac{L}{4\pi R_\star^2\sigma_\text{SB}}
\propto \frac{c^0}{c^{-2}\cdot c^{-2}} = c^4
\;\Longrightarrow\; T_\text{eff}\propto c^1,$$
not $c^2$. Routes A and B were internally consistent but used a premise the
mass–luminosity relation contradicts. The mass–luminosity relation supersedes them.

**Caveat.** The formula uses electron-scattering (Thomson) opacity, which dominates in
hot stellar interiors and is the cleanest primary choice. Kramers (bound-free/free-free)
opacity scales differently with $c$ and would shift the exponent. The sign of the
habitability effect is robust; the magnitude is opacity-dependent.

---

## Received Stellar Flux: $F \propto c^0$

Under invariant $G$ (T8, T9), orbits are static: $d = \text{const}$. The received flux
at Earth's orbital distance is:
$$F = \frac{L}{4\pi d^2} \propto \frac{c^0}{c^0} = c^0.$$

**Flux is $c$-invariant.** This restores a constant-flux result, but through a
different mechanism from cdot-3: in cdot-3, $L\propto c^4$ and $r\propto c^2$ cancelled
to give $F\propto c^0$; here $L\propto c^0$ and $d=\text{const}$ achieve the same
outcome.

The drift rate from the $c$-scaling alone is zero. The standard solar brightening
(~25–30% over 4.5 Gyr from core composition evolution: H→He raises $\mu$, the core
contracts and heats, nuclear rate rises) is a **separate, composition-driven effect**
that is independent of and additive to the $c$-scaling. It is not included in the $c$
power laws below.

---

## The Habitability Ratio: $X \propto c^{-3/2}$

Rather than asking whether the raw flux was constant, the correct model-native question
is whether the *conditions for liquid water* were maintained. Both the flux-derived
temperature and the molecular energy scale that sets water's phase boundaries vary with
$c$; their ratio is the physically meaningful quantity.

### Definition

$$X \equiv \frac{T_\text{eq}}{T_\text{mol}},$$
where $T_\text{eq}$ is Earth's radiative-equilibrium surface temperature and $T_\text{mol}$
is the water molecular (phase-boundary) temperature scale.

### Equilibrium temperature $T_\text{eq} \propto c^{1/2}$

Radiative balance: absorbed stellar flux equals thermal re-emission:
$$\frac{L}{4\pi d^2}\,\pi R_E^2\,(1-A) = 4\pi R_E^2\,\sigma_\text{SB}\,T_\text{eq}^4.$$
Earth's radius $R_E$ cancels (absorbing cross-section $\pi R_E^2$ vs. radiating area
$4\pi R_E^2$). With $L\propto c^0$, $d=\text{const}$, and $\sigma_\text{SB}\propto c^{-2}$:
$$T_\text{eq}^4 \propto \frac{L}{\sigma_\text{SB}\,d^2} \propto \frac{c^{0}}{c^{-2}}
= c^2 \quad\Longrightarrow\quad T_\text{eq} \propto c^{1/2}.$$

As $c$ decreases toward the past, $T_\text{eq}$ was slightly lower in absolute terms.
At $c_\text{past}/c_\text{now}\approx0.84$: $T_\text{eq,past}/T_\text{eq,now}\approx0.84^{1/2}\approx0.92$
— roughly 8% cooler. The equilibrium temperature was lower; the question is relative to
what yardstick.

### Molecular temperature scale $T_\text{mol} \propto c^2$

Water's freezing and boiling points are set by hydrogen-bond energies, which scale like
all electromagnetic binding energies in the model: $E_\text{H-bond}\propto c^2$ (from
the Rydberg-like energy scale with invariant $m,e,h$ and $\epsilon_0\propto c^{-1}$).
With $k_B$ a fixed conversion between energy and kelvin:
$$T_\text{mol} \propto c^2.$$
At $c_\text{past}/c_\text{now}\approx0.84$: $T_\text{mol,past}/T_\text{mol,now}\approx0.84^2\approx0.71$
— the freezing threshold was 29% lower.

### The ratio

$$\boxed{\,X = \frac{T_\text{eq}}{T_\text{mol}} \propto \frac{c^{1/2}}{c^2} = c^{-3/2}.\,}$$

As $c$ decreases toward the past, $X$ **increases**: the early Earth was **warmer
relative to water's freezing point**, not colder. The mechanism is purely relational:
the equilibrium temperature was slightly lower in absolute terms (~8%), but the
molecular yardstick for freezing was much lower (~29%). The liquid-water window was
wider.

---

## Magnitude over Earth's History

Using $c_\text{past}/c_\text{now}\approx0.84$ at 4.5 Gyr lookback
(from $\Delta c/c\approx H_0^\text{hor}\cdot4.5\ \text{Gyr}\approx0.16$,
$H_0^\text{hor}=H_0^\text{obs}/2\approx35\ \text{km/s/Mpc}$):

$$\frac{X_\text{past}}{X_\text{now}} = \left(\frac{0.84}{1}\right)^{-3/2} \approx 1.30.$$

**~30%** larger habitability ratio 4.5 Gyr ago. The equilibrium temperature was 8%
lower; the freezing threshold was 29% lower; the margin between them grew by ~30%.

---

## Implications for the Faint Young Sun Paradox

**cdot-3:** paradox automatically resolved — $L\propto c^4$ and $r\propto c^2$ cancelled
to give constant flux; the relational argument was not needed.

**cdot-4, old derivation:** $L\propto c^4$ with static orbit gave $F\propto c^4$.
Paradox partially eased by $X\propto c^{-1/2}$ (~9% habitability gain). The direction
was correct; the magnitude was small.

**cdot-4, corrected:** flux is again $c$-invariant ($L\propto c^0$, $d=\text{const}$).
The model's contribution is now **purely relational** — not from extra flux, but from
the molecular temperature scale falling faster than the equilibrium temperature.

- **Sign: correct** — $X\propto c^{-3/2}$ pushes toward a warmer, more habitable
  early Earth, in the correct direction for the faint-young-Sun paradox.
- **Magnitude: ~30%** (opacity-dependent), up from the erroneous ~9%.
- **Distinctiveness.** The ~30% habitability improvement is a genuine, falsifiable
  prediction of the relational principle — both scales carry $c$-dependence, and the
  molecular scale is steeper. This is not fitted to the paradox; it is fixed by
  the scalings of $\sigma_\text{SB}$ and H-bond energies.
- **Classification: supplementary, not a full resolution.** The standard
  composition-driven brightening (~25–30% fainter early Sun) still reduces $T_\text{eq}$;
  the model's $c$-effect (X∝c^{-3/2}) runs in the favorable direction with comparable
  magnitude but addresses the relative rather than absolute temperature. Additional
  greenhouse forcing may still be required for the full observed record.

---

## Caveats

1. **Opacity regime sets the exponent.** $L\propto c^0$ and $X\propto c^{-3/2}$ rest
   on **electron-scattering (Thomson) opacity**, $\kappa\propto c^{-2}$ — the dominant,
   cleanest opacity in hot stellar interiors. A Kramers (bound-free/free-free) regime
   scales differently and would shift both the $L$ exponent and the $X$ exponent. The
   robust claim is the **sign** (early Earth warmer relative to freezing), which holds
   provided $L$ does not scale strongly positively with $c$ (which would require an
   unusual opacity scaling).

2. **Scaling-argument class.** All results are power-law scalings, not a full physical
   model. The habitability ratio is a leading-order estimate; the 30% figure is
   order-of-magnitude.

3. **Composition effect held separate.** The standard faint-young-Sun brightening is
   composition-driven (H→He over ~4 Gyr) and is independent of the $c$-scaling. Both
   effects are real and additive; the $c$-effect does not replace the composition effect.

4. **Albedo and atmosphere treated as $c$-independent.** Ice-albedo feedbacks and
   atmospheric composition (CO₂, CH₄) are assumed to track their present values.

5. **$k_B$ convention.** $T_\text{mol}\propto c^2$ assumes $k_B$ is a fixed
   energy-kelvin conversion. Stated explicitly wherever the result is used.

---

## Open Questions

- **Full stellar-structure $L(c)$ derivation.** Opacity, nuclear cross-sections, and
  convective efficiency all carry $c$-dependence. This is the primary open calculation
  for establishing the habitability magnitude rigorously.
- **Quantitative climate comparison.** Does the ~30% habitability improvement
  (combined with or separate from standard greenhouse forcing) account for liquid water
  at 3.8 Gyr?
- **Albedo and atmospheric evolution.** Cloud-ice albedo feedbacks and changes in
  atmospheric composition modify the effective $X$; a fuller treatment should allow
  these to vary.
- **Molecular temperature scaling.** The result $T_\text{mol}\propto c^2$ uses the
  H-bond energy scaling directly. A check against specific H-bond and van-der-Waals
  energies in the model framework would tighten this.
