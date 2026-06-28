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

These constraints, taken together, suggest $G$ is constant to high precision over
both local (Solar System) and cosmological timescales.

---

## The Model's Prediction: $G \propto c^{-2}$

### Origin and value

In the Polarizable Vacuum (PV) framework (Puthoff 2002; Dicke 1957), gravity is
mediated by variations in the refractive index $K$ of the vacuum. The gravitational
potential is $\Phi = -GM/rc^2$, and the PV field equations relate $K = c_0/c$ to the
mass distribution. In this framework, the natural coupling is:
$$G \propto c^4/\Phi_\text{cosmic},$$
and with $\Phi_\text{cosmic} \sim c^6$ (from the cosmological $c \propto R^3$ law),
one obtains $G \propto c^{-2}$.

More directly: $G \propto c^{-2}$ is the **unique** power law that:
1. **Reproduces GR weak-field results** (the Schwarzschild metric and PPN parameters)
   in the PV framework.
2. **Gives orbital expansion $r \propto c^2$** with invariant mass (T9), which is
   required for constant stellar flux.
3. **Keeps the SN Hubble diagram self-consistent** under the squared redshift law.
4. **Passes through the Dicke (1957) "natural units" value**, which equates gravitational
   and inertial definitions of $G$.

For these reasons, $G \propto c^{-2}$ is strongly preferred — it satisfies four
independent constraints simultaneously — but it is **selected by agreeing constraints,
not derived from a first principle**. Providing a derivation from the relational
principle ($c \propto N$ → $G \propto c^{-2}$, perhaps via the connecton mechanism T14)
is a standing theoretical debt.

### Rate of change

With $G = G_0(c_0/c)^2 = G_0(1+z)$ using $c_\text{emit}/c_0 = (1+z)^{-1/2}$
(so $c_0/c_\text{emit} = (1+z)^{+1/2}$ and $(c_0/c_\text{emit})^2 = (1+z)$), the present-day
rate of change is:
$$\frac{\dot{G}}{G} = -2\frac{\dot{c}}{c} = -2H_0^{\text{hor}} = -\frac{2H_0^{\text{obs}}}{P}
= -H_0^{\text{obs}} \approx -7 \times 10^{-11}\ \text{yr}^{-1}.$$

(Using $P = 2$, so $H_0^{\text{hor}} = H_0^{\text{obs}}/2 \approx 3.5 \times 10^{-11}$
yr$^{-1}$; $\dot{G}/G = -2 \times 3.5 \times 10^{-11} \approx -7 \times 10^{-11}$
yr$^{-1}$.)

This is **roughly 500× larger than the LLR bound** ($1.5 \times 10^{-13}$ yr$^{-1}$).
This is a potential conflict between the model and Solar System data.

---

## The Tension with Solar System Constraints

The LLR bound $|\dot{G}/G| < 1.5 \times 10^{-13}$ yr$^{-1}$ is a direct measurement
of the long-term stability of the Moon's orbit. If $G$ were changing at
$-7 \times 10^{-11}$ yr$^{-1}$, the Moon's orbit would expand (since a weaker $G$
gives a larger equilibrium orbit) at a measurable rate over the 50+ year baseline of
LLR.

However, the interpretation requires care:

1. **What $G$ does LLR measure?** LLR measures the effective gravitational coupling
   between bodies in the Solar System. In the PV framework, $G_\text{eff}$ is the
   coupling at scales of $\sim 1$ AU in the local vacuum state. The cosmological $G$
   in the model is defined globally via the horizon-averaged $c$. Whether local Solar
   System measurements track the cosmological variation is a non-trivial question in
   any scalar-tensor or varying-constant theory.

2. **The PV framework and local shielding.** In Dicke-Brans-Jordan scalar-tensor
   theories, the local value of the gravitational coupling can be screened from
   cosmological variations by the local mass distribution (the "chameleon mechanism").
   Whether an analogous screening operates here is unknown.

3. **Orbital expansion compensates.** In this model, orbits expand as $r \propto c^2$
   (T9). As $G$ weakens, the orbit simultaneously expands such that orbital periods
   $T \propto r^{3/2}/(GM)^{1/2}$ are kept consistent. The net observable (e.g., the
   Moon's distance from Earth) involves both effects. Whether the LLR observable — which
   involves the actual Earth-Moon distance and the orbital timing — is sensitive to
   $\dot{G}/G$ or to a combination of $\dot{G}$ and $\dot{r}$ effects requires explicit
   computation.

4. **The strength of the LLR constraint.** The LLR bound assumes $G$ varies while
   everything else is constant. In a model where $c$, $G$, orbital radii, and atomic
   frequencies all vary together in a correlated way, the effective constraint on any
   single quantity like $\dot{G}/G$ may be weaker than the naive number suggests.

**This remains an important open constraint that the model must address explicitly.**
A self-consistent computation of the LLR observable — using the model's combined
$c(t)$, $G(t)$, $r(t)$ evolution — is required before concluding there is a conflict.

---

## Why Mass is Invariant (Not the PV Value)

In the PV framework (Puthoff 2002), the self-energy of a particle in the vacuum
field $K$ scales as $m \propto K^{3/2} \propto c^{-3/2}$. This gives $s = -3/2$, the
"PV mass" scaling. But the model adopts $s = 0$ (invariant mass).

The conflict between PV and invariant mass is unresolved. Several observations favour
$s = 0$:
- The SN Hubble diagram (T4) constrains $s$ via the redshift power $P = s+2$. Fits
  favour $s \approx 0$, not $s = -3/2$.
- Invariant mass is required for the symmetric-flip conservation structure (T11).

**Why is $m$ invariant rather than following the PV self-energy scaling?** This is
an open question. The PV self-energy gives $m \propto K^{3/2}$, but this
self-energy calculation may not be the correct treatment of mass in a fully
self-consistent variable-$c$ framework. The invariant-mass choice has better empirical
support; its theoretical justification is a standing debt.

---

## Cosmological Variation of $G$

The model predicts $G \propto c^{-2} \propto (1+z)$ — i.e., $G$ was larger in the
past. At $z = 1$: $G_\text{emit} = 2\,G_\text{now}$, a 100% increase. At $z = 5$:
$G \approx 6\,G_\text{now}$.

Observational tests:
- **BBN:** a larger $G$ at $z \sim 10^{10}$ would speed up the Hubble rate during
  nucleosynthesis, changing the freeze-out temperature and hence the $^4$He abundance.
  Current data allow $G$ to have been within $\sim 20$–$30\%$ of its present value
  at BBN; the model's prediction ($G$ larger by $\sim z$ at high $z$, giving
  $G \sim 10^{10}\,G_\text{now}$ at $z \sim 10^{10}$) is in severe tension with this
  bound. This has not been computed in detail.
- **Pulsar timing:** binary pulsar orbital decay measures $\dot{G}/G$ and constrains it
  more loosely than LLR ($\lesssim 10^{-11}$ yr$^{-1}$), still above the model's
  $7 \times 10^{-11}$ yr$^{-1}$.

---

## Open Questions

- A self-consistent LLR computation: what is the predicted rate of change of the
  Earth-Moon distance in this model, where $G$, $r$, $c$, and atomic clock rates
  all vary together?
- The BBN constraint on $G$ at $z \sim 10^{10}$: is the model's large $G$ variation
  at early epochs compatible with observed light-element abundances?
- A theoretical derivation of $G \propto c^{-2}$ from the relational principle
  ($c \propto N$ → $G \propto c^{-2}$) — the central unresolved theoretical debt.
  The connecton mechanism (T14) is the current leading candidate for this derivation,
  if the ballistic/diffusive dilemma can be resolved.
- Whether there is any "screening" analogue in this framework that would make local
  Solar System measurements insensitive to the cosmological $G$ variation.
