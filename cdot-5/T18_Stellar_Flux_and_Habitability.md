# T18 — Stellar Flux and the Habitability Ratio

*Checked against the counting-law change: every result in this document (luminosity,
flux, and the habitability ratio) is a **present-value scaling** — it asks how a
quantity depends on the instantaneous value of $c$ at fixed stellar mass and
composition, never on cosmic history. None of it references $R$, $N$, or the horizon
law, so **all of it is confirmed unaffected** by the switch from occupancy to
connectivity counting. The one place cosmic history enters — converting a lookback
time into a $c_\text{past}/c_\text{now}$ ratio for the Sun's history — is **redone**
below using cdot-5's exact $c(\tau)$ relation (Core Principles §4a/§5a) in place of
cdot-4's linear approximation, and gives, by a numerical coincidence explained below,
almost exactly the same number.*

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

Under invariant mass and composition (Core Principles premise 3, unchanged from
cdot-4), bolometric luminosity is fixed by the balance between hydrostatic equilibrium
and radiative transport — **not** by the stellar radius. The stellar radius drops out of
the mass–luminosity relation entirely.

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
opacity ($\kappa\propto c^{-2}$). Every input here — $\epsilon_0\propto c^{-1}$ (EM-forced,
Core Principles §2), invariant $G,\hbar,m_p,m_e,e$ (premise 3) — is unchanged from
cdot-4 and does not reference the counting law.

**Why naive routes give $c^4$ — and why they are wrong.** One route uses
$L \sim E \cdot \nu \propto c^2 \cdot c^2 = c^4$. Another uses
$L = 4\pi R_\star^2\sigma_\text{SB}T_\text{eff}^4$ with $R_\star \propto c^{-1}$
(atomic Bohr-radius scaling) and $T_\text{eff} \propto c^2$ (Wien law with
$\nu\propto c^2$), also giving $c^4$. Both share the same hidden assumption: that
$T_\text{eff}$ tracks the atomic energy scale ($\propto c^2$). This is unjustified —
stellar surface temperature is set by the stellar structure, not by atomic scales. The
correct $T_\text{eff}$ from the mass–luminosity relation (with $R_\star\propto c^{-1}$
and $\sigma_\text{SB}\propto c^{-2}$) is:
$$T_\text{eff}^4 = \frac{L}{4\pi R_\star^2\sigma_\text{SB}}
\propto \frac{c^0}{c^{-2}\cdot c^{-2}} = c^4
\;\Longrightarrow\; T_\text{eff}\propto c^1,$$
not $c^2$. The mass–luminosity relation supersedes the naive routes.

**Caveat.** The formula uses electron-scattering (Thomson) opacity, which dominates in
hot stellar interiors and is the cleanest primary choice. Kramers (bound-free/free-free)
opacity scales differently with $c$ and would shift the exponent. The sign of the
habitability effect is robust; the magnitude is opacity-dependent.

---

## Received Stellar Flux: $F \propto c^0$

Under invariant $G$ (Core Principles premise 3, T8/T9 unchanged), orbits are static:
$d = \text{const}$. The received flux at Earth's orbital distance is:
$$F = \frac{L}{4\pi d^2} \propto \frac{c^0}{c^0} = c^0.$$

**Flux is $c$-invariant.** $L\propto c^0$ and $d=\text{const}$ combine to give constant
flux.

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

### Molecular temperature scale $T_\text{mol} \propto c^2$

Water's freezing and boiling points are set by hydrogen-bond energies, which scale like
all electromagnetic binding energies in the model: $E_\text{H-bond}\propto c^2$ (from
the Rydberg-like energy scale with invariant $m,e,h$ and $\epsilon_0\propto c^{-1}$).
With $k_B$ a fixed conversion between energy and kelvin:
$$T_\text{mol} \propto c^2.$$

### The ratio

$$\boxed{\,X = \frac{T_\text{eq}}{T_\text{mol}} \propto \frac{c^{1/2}}{c^2} = c^{-3/2}.\,}$$

As $c$ decreases toward the past, $X$ **increases**: the early Earth was **warmer
relative to water's freezing point**, not colder. The mechanism is purely relational:
the equilibrium temperature was slightly lower in absolute terms, but the molecular
yardstick for freezing was lower by more. The liquid-water window was wider.

None of the three exponents above ($L\propto c^0$, $F\propto c^0$, $X\propto c^{-3/2}$)
reference $N$, $R$, or the horizon law — they hold **identically** under connectivity
counting as under the excluded occupancy law. This is the same present-value pattern
established for the fine-structure constant, $G$, and orbital dynamics (T7/T8/T9).

---

## Magnitude over Earth's History — Redone with the Exact $c(\tau)$ Relation

**What changes here.** Converting "4.5 Gyr ago" into a $c_\text{past}/c_\text{now}$
ratio requires a cosmic-history input, which *does* depend on the counting law. cdot-4
used a linear approximation, $\Delta c/c\approx H_0^\text{hor}\cdot4.5\ \text{Gyr}$. The
connectivity law's post-percolation branch ($z<z_*\approx1.2$, Core Principles §3/§4a)
gives something better: an **exact, closed-form** relation between $c$ and proper
lookback time $\tau$, derived in T1 from the redshift law (T2, $1+z=(c_0/c_e)^2$,
unaffected by the counting-law change) combined with the horizon-law solution:
$$\frac{c(\tau)}{c_0} = 1-\frac{\tau}{\tau_\infty},\qquad
\tau_\infty=\frac{2}{H_0^\text{obs}}\approx27.9\ \text{Gyr}\ (H_0=70).$$
This is **exactly linear** in $\tau$ — a genuine simplification over cdot-4's
$3/4$-power law, and it needs no small-lookback approximation.

At $\tau=4.5$ Gyr:
$$\frac{c_\text{past}}{c_\text{now}} = 1-\frac{4.5}{27.94} = 0.839.$$
This corresponds to $1+z=(c_0/c_e)^2=1.42$, i.e. $z\approx0.42$ — safely inside the
post-percolation regime ($z<z_*\approx1.2$), so the exact relation above applies with no
extrapolation caveat needed for this particular calculation.

**Why this matches cdot-4's "$\approx0.84$" almost exactly.** cdot-4's linear
approximation used the *same* $H_0^\text{hor}=H_0^\text{obs}/2\approx35$ km/s/Mpc slope
(the $P=2$ relation, Core Principles §4a, unchanged from cdot-4) evaluated at $\tau=0$
and extrapolated linearly to 4.5 Gyr. cdot-5's relation turns out to actually **be**
exactly that same straight line, not merely tangent to some curved relation at
$\tau=0$ — so the two numbers agree to three figures ($0.839$ vs. cdot-4's $0.84$) by
construction, not coincidence of rounding. This is a genuine (mild) surprise: cdot-4's
small-lookback approximation happens to be cdot-5's exact result.

$$\frac{X_\text{past}}{X_\text{now}} = \left(\frac{0.839}{1}\right)^{-3/2} \approx 1.30.$$

**~30%** larger habitability ratio 4.5 Gyr ago — the same headline number as cdot-4,
now resting on an exact relation rather than an approximation.

---

## Implications for the Faint Young Sun Paradox

- **Sign: correct** — $X\propto c^{-3/2}$ pushes toward a warmer, more habitable
  early Earth, in the correct direction for the faint-young-Sun paradox.
- **Magnitude: ~30%** (opacity-dependent; §"Caveats" below), unchanged from cdot-4 and
  now on firmer footing (exact relation, not a linear approximation).
- **Distinctiveness.** The ~30% habitability improvement is a genuine, falsifiable
  prediction of the relational principle — both scales carry $c$-dependence, and the
  molecular scale is steeper. This is not fitted to the paradox; it is fixed by
  the scalings of $\sigma_\text{SB}$ and H-bond energies, none of which reference the
  counting law.
- **Classification: supplementary, not a full resolution.** The standard
  composition-driven brightening (~25–30% fainter early Sun) still reduces $T_\text{eq}$;
  the model's $c$-effect ($X\propto c^{-3/2}$) runs in the favorable direction with
  comparable magnitude but addresses the relative rather than absolute temperature.
  Additional greenhouse forcing may still be required for the full observed record.

---

## Caveats

1. **Opacity regime sets the exponent.** $L\propto c^0$ and $X\propto c^{-3/2}$ rest
   on **electron-scattering (Thomson) opacity**, $\kappa\propto c^{-2}$ — the dominant,
   cleanest opacity in hot stellar interiors. A Kramers (bound-free/free-free) regime
   scales differently and would shift both the $L$ exponent and the $X$ exponent. The
   robust claim is the **sign** (early Earth warmer relative to freezing), which holds
   provided $L$ does not scale strongly positively with $c$.

2. **Scaling-argument class.** All results are power-law scalings, not a full physical
   model. The habitability ratio is a leading-order estimate; the 30% figure is
   order-of-magnitude.

3. **Composition effect held separate.** The standard faint-young-Sun brightening is
   composition-driven (H→He over ~4 Gyr) and is independent of the $c$-scaling. Both
   effects are real and additive; the $c$-effect does not replace the composition effect.

4. **Albedo and atmosphere treated as $c$-independent.** Ice-albedo feedbacks and
   atmospheric composition (CO₂, CH₄) are assumed to track their present values.

5. **$k_B$ convention.** $T_\text{mol}\propto c^2$ assumes $k_B$ is a fixed
   energy-kelvin conversion. Stated explicitly wherever the result is used (T21 uses the
   same convention for its own $c$-scaling arguments).

---

## Open Questions

- **Full stellar-structure $L(c)$ derivation.** Opacity, nuclear cross-sections, and
  convective efficiency all carry $c$-dependence. This is the primary open calculation
  for establishing the habitability magnitude rigorously — unaffected in scope by the
  counting-law change, since it is a present-value calculation either way.
- **Quantitative climate comparison.** Does the ~30% habitability improvement
  (combined with or separate from standard greenhouse forcing) account for liquid water
  at 3.8 Gyr? At $\tau=3.8$ Gyr, $c/c_0=1-3.8/27.94=0.864$, $X$-ratio
  $=0.864^{-3/2}\approx1.25$ — a ~25% improvement, not yet checked against a real climate
  model with either counting law.
- **Albedo and atmospheric evolution.** Cloud-ice albedo feedbacks and changes in
  atmospheric composition modify the effective $X$; a fuller treatment should allow
  these to vary.
- **Molecular temperature scaling.** The result $T_\text{mol}\propto c^2$ uses the
  H-bond energy scaling directly. A check against specific H-bond and van-der-Waals
  energies in the model framework would tighten this.
