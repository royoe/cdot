# T18 — Stellar Flux and the Habitability Ratio

*Note: this topic is a scaling-argument analysis. All results ($L\propto c^4$,
$F\propto c^4$, $X\propto c^{-1/2}$) derive from dimensional scaling under the premise
$c(t)$ without a full stellar-structure calculation. The key load-bearing step is
$L\propto c^4$; the magnitude of the habitability ratio hinges on this exponent being
correct. A full stellar-structure treatment of $L(c)$ is the primary open calculation.*

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

## Stellar Luminosity: $L \propto c^4$

Under invariant mass ($m\propto c^0$) with atomic frequencies $\nu\propto c^2$ (§5a of
Core Principles) and $\epsilon_0\propto c^{-1}$, the energy scale of nuclear transitions
is $E\propto c^2$. The luminosity scales as $L\sim E\cdot\nu$ (energy per atomic
time-unit):

**Route A (energy × rate):** Energy scale $\propto c^2$; atomic rate $\propto\nu\propto c^2$:
$$L \propto c^2 \cdot c^2 = c^4.$$

**Route B (surface emission):** $L = 4\pi R_\star^2\,\sigma_\text{SB}\,T_\text{eff}^4$.
Stellar radius $R_\star\propto c^{-1}$ (atomic Bohr radii scale as $a_0\propto c^{-1}$ with
invariant $m$ and $e,h$); Stefan-Boltzmann $\sigma_\text{SB}\propto c^{-2}$ (from
$\sigma_\text{SB}=\pi^2k_B^4/(60\hbar^3c^2)$ with $k_B,\hbar$ invariant); effective
temperature $T_\text{eff}\propto c^2$ (from the Wien law with $\nu\propto c^2$):
$$L \propto (c^{-1})^2 \cdot c^{-2} \cdot (c^2)^4 = c^{-2} \cdot c^{-2} \cdot c^8 = c^4.$$

Both routes agree: $L\propto c^4$.

**Caveat.** The actual luminosity of a main-sequence star depends on nuclear reaction
rates, mean-free-path opacities, and convective transport efficiencies — all of which
carry their own $c$-dependence. The two-route consistency is reassuring but is not a
substitute for a full stellar-structure calculation. The exponent 4 is the leading-order
scaling; corrections could shift it.

---

## Received Stellar Flux: $F \propto c^4$

Under invariant $G$ (T8, T9), orbits are static: $r = L^2/(m^2 GM) = \text{const}$.
The received flux at a planet's orbital radius is:
$$F = \frac{L}{4\pi r^2} \propto \frac{c^4}{c^0} = c^4.$$

The drift rate is $\dot F/F = 4H_0^\text{hor} \approx 4\times H_0^\text{obs}/2
\approx 1.4\times10^{-10}$ yr$^{-1}$, locally unobservable, but an order-unity change
over $\sim$Gyr timescales.

**Comparison with cdot-3.** Under $G\propto c^{-2}$, orbits expanded as $r\propto c^2$,
giving $F=L/(4\pi r^2)\propto c^4/c^4 = c^0$ (constant flux). That exact cancellation
was the source of the earlier "automatic" resolution of the faint young Sun paradox.
Invariant $G$ removes the cancellation: flux now drifts. The question becomes whether
physical conditions for liquid water were nevertheless maintained.

---

## The Habitability Ratio: $X \propto c^{-1/2}$

Rather than asking whether the raw flux was constant, the correct model-native question
is whether the *conditions for liquid water* were maintained. Both the flux and the
molecular energy scale that sets water's phase boundaries vary with $c$; their ratio is
the physically meaningful quantity.

### Definition

$$X \equiv \frac{T_\text{eq}}{T_\text{mol}},$$
where $T_\text{eq}$ is Earth's radiative-equilibrium surface temperature and $T_\text{mol}$
is the water molecular (phase-boundary) temperature scale — the H-bond energy converted
to kelvin, which governs freezing and boiling.

### Equilibrium temperature $T_\text{eq} \propto c^{3/2}$

Radiative balance: absorbed stellar flux equals thermal re-emission:
$$\frac{L}{4\pi d^2}\,\pi R_E^2\,(1-A) = 4\pi R_E^2\,\sigma_\text{SB}\,T_\text{eq}^4.$$
Earth's radius $R_E$ cancels (absorbing cross-section $\pi R_E^2$ vs. radiating area
$4\pi R_E^2$ — the factor of 4 is body-size-independent). With $L\propto c^4$,
$d=\text{const}$, and $\sigma_\text{SB}\propto c^{-2}$:
$$T_\text{eq}^4 \propto \frac{L}{\sigma_\text{SB}\,d^2} \propto \frac{c^4}{c^{-2}}
= c^6 \quad\Longrightarrow\quad T_\text{eq} \propto c^{3/2}.$$

### Molecular temperature scale $T_\text{mol} \propto c^2$

Water's freezing and boiling points are set by hydrogen-bond energies, which scale like
all electromagnetic binding energies in the model: $E_\text{H-bond}\propto c^2$ (from
the Rydberg-like energy scale with invariant $m,e,h$ and $\epsilon_0\propto c^{-1}$).
With $k_B$ a fixed conversion between energy and kelvin:
$$T_\text{mol} \propto c^2.$$

### The ratio

$$\boxed{\,X = \frac{T_\text{eq}}{T_\text{mol}} \propto \frac{c^{3/2}}{c^2} = c^{-1/2}.\,}$$

As $c$ decreases toward the past, $X$ **increases**: the early Earth was warmer relative
to water's freezing point. The mechanism: the molecular yardstick ($\propto c^2$) fell
faster in the past than the equilibrium temperature ($\propto c^{3/2}$). This is a
direct consequence of the relational principle — both scales carry $c$-dependence, and
the molecular scale is steeper.

---

## Magnitude over Earth's History

Using $c_\text{past}/c_\text{now}\approx0.84$ at 4.5 Gyr lookback
(from $\Delta c/c\approx H_0^\text{hor}\cdot4.5\ \text{Gyr}\approx0.16$,
$H_0^\text{hor}=H_0^\text{obs}/2\approx35\ \text{km/s/Mpc}$):

$$\frac{X_\text{past}}{X_\text{now}} = \left(\frac{0.84}{1}\right)^{-1/2} \approx 1.09.$$

This is roughly $+9\%$ in the habitability ratio — or of order $\sim20$ K effective
warming relative to the freezing point at present-day conditions. At present mean surface
temperature $\approx15°$C (freezing at $0°$C), a 20 K shift is climatologically
significant.

---

## Implications for the Faint Young Sun Paradox

**Previous status (cdot-3):** the paradox was "automatically resolved" by constant
stellar flux ($F\propto c^0$). That resolution depended on $r\propto c^2$, which is
removed by invariant $G$.

**Current status (cdot-4):** the paradox is **partially eased** in the correct
direction.

- **Sign: correct** — $X$ pushes toward a warmer, more habitable early Earth.
- **Magnitude: open** — $\sim$20 K is significant but probably not the full deficit.
  Standard solar models place the early Sun at 70% luminosity, corresponding to an
  equilibrium temperature deficit of $\sim$25 K. The 20 K offset from $X$ reduces but
  does not eliminate the required additional greenhouse forcing.
- **Classification: partially eased, not automatically resolved.**

**Distinctiveness.** This is a genuine, falsifiable prediction of the relational model:
the early Earth's habitability ratio was higher (warmer relative to freezing) by a
specific amount tied to $\Delta c/c$ over the relevant epoch. The sign and approximate
magnitude are fixed by the theory; they are not fitted to the paradox.

---

## Caveats

1. **$L\propto c^4$ is the load-bearing assumption.** Verified by two independent
   routes (§ "Stellar Luminosity"), but a full stellar-structure calculation — tracking
   $c$-dependence through nuclear cross-sections, opacity, and convection — has not been
   done. An exponent shift would change $T_\text{eq}$ and the entire magnitude.

2. **Scaling-argument class.** All results here are power-law scalings, not full
   physical models. The habitability ratio is a leading-order estimate.

3. **Albedo and atmosphere treated as $c$-independent.** Ice-albedo feedbacks and
   changes in atmospheric composition (CO₂, CH₄, N₂O) are assumed to track their
   present values. A fuller treatment should allow these to respond to the changing
   flux and temperature.

4. **$k_B$ convention.** The result $T_\text{mol}\propto c^2$ assumes $k_B$ is a fixed
   energy-kelvin conversion. If the kelvin is redefined through $k_B\propto c^x$ for
   some $x\neq0$, the exponents change. The invariant-$k_B$ convention is consistent
   with the model's stance on $e,h$ but should be stated explicitly.

---

## Open Questions

- **Full stellar-structure $L(c)$ derivation.** Opacity, nuclear cross-sections, and
  convective efficiency all carry $c$-dependence. This is the primary open calculation
  for establishing the habitability magnitude.
- **Quantitative climate comparison.** Is the $\sim$20 K effective warming sufficient
  to explain liquid water at 3.8 Gyr without requiring large greenhouse forcing, or
  does additional CO₂/CH₄ still dominate?
- **Albedo and atmospheric evolution.** Cloud-ice albedo feedbacks and changes in
  atmospheric composition modify the effective $X$; a fuller treatment should allow
  these to vary.
- **Molecular temperature scaling.** The result $T_\text{mol}\propto c^2$ uses the
  H-bond energy scaling directly. A check against specific H-bond and van-der-Waals
  energies in the model framework would tighten this.
