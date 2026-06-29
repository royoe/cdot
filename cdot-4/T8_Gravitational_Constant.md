# T8 — The Gravitational Constant

## Observational Background

Newton's gravitational constant $G$ appears in the force law $F = GMm/r^2$ and in
Einstein's field equations as the coupling between spacetime curvature and the
stress-energy tensor. Locally, $G$ is measured to be:
$$G = 6.674 \times 10^{-11}\ \text{m}^3\,\text{kg}^{-1}\,\text{s}^{-2}.$$

Whether $G$ varies with time or position is tested by several methods:

- **Lunar Laser Ranging (LLR):** $|\dot{G}/G| < 1.5 \times 10^{-13}\ \text{yr}^{-1}$
  (95% CL; Hofmann & Müller 2018).
- **Pulsar timing** (especially the Hulse-Taylor binary): $|\dot{G}/G| < 10^{-11}\ \text{yr}^{-1}$.
- **Big Bang Nucleosynthesis:** constrains $G$ at $z \sim 10^{10}$ relative to today;
  limits $G$ variation to $\lesssim 20$–$30\%$ over cosmic history.
- **CMB acoustic peaks:** the position of the first acoustic peak constrains $G$ during
  recombination ($z \sim 1100$).

These constraints, taken together, show that $G$ is constant to high precision over
both local (Solar System) and cosmological timescales.

---

## The Legacy Choice: $G \propto c^{-2}$ (Superseded)

*This section records why $G \propto c^{-2}$ was adopted in cdot-3 and why it has been
superseded. The reasoning here is historical; the current model takes **invariant G**
(§ "The Model's Choice: Invariant G" below).*

### Origin and value

In the Polarizable Vacuum (PV) framework (Puthoff 2002; Dicke 1957), gravity is
mediated by variations in the refractive index $K$ of the vacuum. The gravitational
potential is $\Phi = -GM/rc^2$, and the PV field equations relate $K = c_0/c$ to the
mass distribution. In this framework, the natural coupling is:
$$G \propto c^4/\Phi_\text{cosmic},$$
and with $\Phi_\text{cosmic} \sim c^6$ (from the cosmological $c \propto R^3$ law),
one obtains $G \propto c^{-2}$.

More directly: $G \propto c^{-2}$ was the **unique** power law satisfying four constraints
simultaneously:
1. **Reproduces GR weak-field results** (Schwarzschild metric, PPN parameters) in the PV
   framework.
2. **Gives orbital expansion $r \propto c^2$** with invariant mass (T9), which produced
   constant received stellar flux.
3. **Keeps the SN Hubble diagram self-consistent** under the squared redshift law.
4. **Passes through the Dicke (1957) "natural units" value**, equating gravitational and
   inertial definitions of $G$.

For these reasons, $G \propto c^{-2}$ was the adopted value in cdot-3, though flagged
explicitly as *selected by agreeing constraints, not derived from a first principle* — a
standing theoretical debt.

### Why the PV justification lost standing

Reasons (1) and (4) above are **PV-framework features**. The model already abandoned PV
for the mass scaling: it takes invariant mass $s = 0$, not PV's $m \propto c^{-3/2}$, on
empirical grounds. Once PV is abandoned for mass, the PV-native value of $G$ loses its
privileged status. Adopting invariant $G$ makes mass-invariance and $G$-invariance both
breaks from PV in the same direction — more internally consistent, not less.

---

## Self-Consistent LLR Computation: $G \propto c^{-2}$ Is Decisively Refuted

Under $G \propto c^{-2}$, the naive comparison was:
$$\frac{\dot{G}}{G} = -2H_0^{\text{hor}} \approx -7 \times 10^{-11}\ \text{yr}^{-1},$$
vs the LLR bound $1.5 \times 10^{-13}\ \text{yr}^{-1}$ — a factor ~500 tension. But the
LLR observable is not just $\dot G/G$; it couples three independent effects: orbital
expansion $r \propto c^2$, varying $c$ in the ranging formula, and varying atomic clock
rate $\nu \propto c^2$ (Core Principles §5a). The self-consistent calculation follows.

### Round-trip ranging (what LLR actually measures)

The laser round-trip time in coordinate time is $\Delta t_\text{coord} = 2r_\text{EM}/c$.
The atomic clock accumulates ticks at $\nu(t) = \nu_0(c/c_0)^2$, so:

$$\Delta\tau = \nu(t)\,\Delta t_\text{coord} = \nu_0\!\left(\frac{c}{c_0}\right)^2 \cdot \frac{2r_0}{c_0}\!\left(\frac{c}{c_0}\right)^2\!\bigg/\!\left(\frac{c}{c_0}\right)
= \frac{2\nu_0 r_0}{c_0}\!\left(\frac{c}{c_0}\right)^3.$$

The LLR data reduction assumes $c = c_0$ and $\nu = \nu_0$, inferring:

$$r_\text{LLR}(t) = \frac{c_0\,\Delta\tau}{2\nu_0} = r_0\!\left(\frac{c}{c_0}\right)^3.$$

The LLR-measured range rate is therefore:

$$\frac{\dot{r}_\text{LLR}}{r_\text{LLR}} = 3\frac{\dot{c}}{c} = 3H_0^\text{hor} = \tfrac{3}{2}H_0^\text{obs}.$$

This factor of $\tfrac{3}{2}H_0^\text{obs}$ decomposes into three contributions:

| Effect | Scaling | Rate |
|:-------|:--------|-----:|
| Orbital expansion $r \propto c^2$ | $+2H_0^\text{hor}$ | $+27.6$ mm/yr |
| Speed of light in travel time | $-H_0^\text{hor}$ | $-13.8$ mm/yr |
| Atomic clock rate $\nu \propto c^2$ | $+2H_0^\text{hor}$ | $+27.6$ mm/yr |
| **Total cosmological (LLR-measured)** | $+3H_0^\text{hor}$ | **$+41.4$ mm/yr** |

The orbital expansion and clock rate both contribute; the speed-of-light factor partially
cancels. The net cosmological contribution to the LLR signal is **larger** than the
naively estimated coordinate orbital rate of 27.6 mm/yr.

### Orbital period

The coordinate orbital period: $T_\text{coord} = 2\pi/\omega$ with
$\omega^2 = G(t)M/r^3 \propto c^{-2}/c^6 = c^{-8}$, so $T_\text{coord} \propto c^4$.
In atomic clock time: $T_\text{atomic} = T_\text{coord}\cdot\nu/\nu_0 \propto c^4 \cdot c^2 = c^6$:

$$\frac{\dot{T}_\text{atomic}}{T_\text{atomic}} = 6H_0^\text{hor} = 3H_0^\text{obs}
\approx 2.15\times10^{-10}\ \text{yr}^{-1}, \quad
\dot{T}_\text{atomic} = 0.51\ \text{ms/yr.}$$

The cumulative timing residual after 50 years of LLR: $\delta t \approx \frac{1}{2}(3H_0^\text{obs})t^2 \approx 8.5\ \text{s.}$
LLR timing precision is nanoseconds per shot; an 8.5 s drift is unmistakable.

### Inferred $\dot{G}/G$

From Kepler's third law, $G_\text{fit} \propto r^3/T^2 \propto c^9/c^{12} = c^{-3}$:
$$\frac{\dot{G}_\text{fit}}{G_\text{fit}} = -3H_0^\text{hor} = -\tfrac{3}{2}H_0^\text{obs}
\approx -1.08\times10^{-10}\ \text{yr}^{-1}.$$

The self-consistent analysis **worsens** the tension by a factor of $\tfrac{3}{2}$ relative
to the naive estimate.

### Verdict

![](../figures/llr_constraint.svg)
*Figure: Left — LLR Earth-Moon range-rate budget. The cosmological term (41.4 mm/yr, blue)
is larger than the tidal dissipation (38.2 mm/yr, gray); together they predict 79.6 mm/yr,
more than twice the observed 38.2 mm/yr. The LLR non-tidal bound (0.058 mm/yr, red dashed
line) rules out the cosmological component by a factor of 717.
Right — log-scale comparison of $|\dot{G}/G|$ for the LLR bound, pulsar timing, and the
model's coordinate and LLR-inferred values.*

| Observable | $G \propto c^{-2}$ prediction | Observed / bound | Tension |
|:-----------|:-----------------|:-----------------|:-------:|
| Non-tidal LLR range rate | $+41.4$ mm/yr | $< 0.058$ mm/yr | $\times 717$ |
| Cumulative period residual (50 yr) | $\sim 8.5$ s | $\sim 10^{-6}$ s (ns/shot) | $\gg 10^6$ |
| Inferred $\dot{G}/G$ (LLR pipeline) | $-1.08\times10^{-10}$ yr$^{-1}$ | $< 1.5\times10^{-13}$ yr$^{-1}$ | $\times 720$ |
| Total LLR range rate | $79.6$ mm/yr | $38.2$ mm/yr (observed) | $\times 2.1$ |

The self-consistent calculation is approximately 50% worse than the naive $\dot G/G$
comparison because the clock-rate and ranging effects add to the orbital expansion
signal instead of cancelling it.

### Why tidal and cosmological contributions are independent

Tidal dissipation transfers angular momentum from Earth's spin to the Moon's orbit
(measurably slowing Earth's rotation by $\approx 1.7$ ms/century). The cosmological
expansion ($r \propto c^2$) follows from the adiabatic invariant $L = m\sqrt{GMr} = \text{const}$
as $G$ varies — it conserves the Moon's angular momentum and does NOT slow Earth. These
are therefore genuinely additive, and the tidal contribution cannot be re-attributed to
cosmological origin without violating Earth-rotation timing.

---

## The Model's Choice: Invariant $G$

The self-consistent LLR result (×720 tension, 79.6 vs 38.2 mm/yr) makes $G \propto c^{-2}$
untenable without a local screening mechanism. No such mechanism exists in the model's
relational framework (where $c \propto N_\text{horizon}$ is driven by the global particle
count, not the local density). The resolution adopted from cdot-4 onward is **invariant
$G$** ($G \propto c^0$).

Under invariant $G$ with invariant mass:
- **Orbital expansion is zero.** From $v^2 r = GM = \text{const}$ and $vr = \text{const}$,
  $r = L^2/(m^2 GM) = \text{const}$. Orbits are static; the LLR ranging signal has no
  cosmological component.
- **$\dot G = 0$ trivially.** All LLR, pulsar-timing, and BBN $G$-variation constraints
  are satisfied at root.
- **$G_\text{BBN} = G_0$** (no amplification). The severe BBN tension ($G_\text{BBN} \sim
  10^{10} G_0$ under $G \propto c^{-2}$) disappears.
- **The "local screening" escape is moot.** There is nothing to screen; the mechanism
  question becomes irrelevant.

The cost: orbital expansion — and the galaxy-size-evolution consistency ($r_e \propto
(1+z)^{-1}$, T10) that depended on it — is withdrawn. The constant-stellar-flux feature
is also lost; received flux now drifts as $F \propto c^4$. However, the habitability ratio
$X = T_\text{eq}/T_\text{mol} \propto c^{-1/2}$ shows the early Earth was warmer relative
to water's freezing point, converting this apparent problem into a positive prediction
(Core Principles §6; T9).

The standing **theoretical debt** transfers: $G \propto c^{-2}$ needed a first-principle
derivation; so now does $G \propto c^0$. Providing a relational-framework derivation of
invariant $G$ is the open theoretical task. The debt is not erased — it is relocated.

---

## Why Mass is Invariant (Not the PV Value)

In the PV framework (Puthoff 2002), the self-energy of a particle in the vacuum
field $K$ scales as $m \propto K^{3/2} \propto c^{-3/2}$. This gives $s = -3/2$, the
"PV mass" scaling. The model adopts $s = 0$ (invariant mass).

Several observations favour $s = 0$:
- The SN Hubble diagram (T4) constrains $s$ via the redshift power $P = s+2$. Fits
  favour $s \approx 0$, not $s = -3/2$.
- Invariant mass is required for the symmetric-flip conservation structure (T11).

**Why is $m$ invariant rather than following the PV self-energy scaling?** This is
an open question. The PV self-energy calculation may not be the correct treatment of
mass in a fully self-consistent variable-$c$ framework. The invariant-mass choice has
better empirical support; its theoretical justification is a standing debt.

Invariant $G$ and invariant $m$ are now both breaks from PV in the same direction,
forming a more consistent non-PV pairing. Neither is derived; both are empirically
required.

---

## Open Questions

- **Theoretical derivation of invariant $G$** from the relational principle ($c \propto N$
  → $G$ = const). The connecton mechanism (T14) is the leading candidate for connecting
  the relational principle to $G$; the foam-diffusion result needs to be re-examined under
  the assumption of a constant coupling (T14).
- **Theoretical derivation of invariant mass** — same class of standing debt (T11).
- ~~**Self-consistent LLR computation** — Done (June 2026)~~: tension was $\times720$ under
  $G \propto c^{-2}$; this result motivated the adoption of invariant $G$.
- ~~**Local screening mechanism**~~ — **Moot**: $G$ is constant; no variation to screen.
- ~~**BBN constraint on $G$ at $z \sim 10^{10}$**~~ — **Resolved**: $G_\text{BBN} = G_0$
  under invariant $G$; the $\times10^{10}$ amplification does not occur.
