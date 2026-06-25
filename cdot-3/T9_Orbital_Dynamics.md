# T9 — Orbital Dynamics and the Faint Young Sun

## Observational Background

### The Faint Young Sun Paradox

Solar models predict that the Sun has brightened by approximately 30% over the last
4.5 Gyr, starting from about 70% of its current luminosity at formation. Yet
geological evidence — including banded iron formations, sedimentary rocks, and fossil
evidence — shows that liquid water was present on Earth's surface at least 3.8 Gyr
ago, when the Sun was considerably fainter than today.

Under the Sun's current luminosity, the early Earth (with its primordial $\sim 10\%$
higher CO₂ atmosphere) would have been frozen at early epochs. But with 70% of
current luminosity and no additional greenhouse effect, the mean surface temperature
would be well below freezing for the first $\sim 1$–$2$ Gyr. The geological record
contradicts this. This is the **faint young Sun paradox** (Sagan & Mullen 1972).

Standard resolutions invoke a thicker early greenhouse atmosphere (CO₂, CH₄, N₂O).
These are possible but require specific atmospheric evolution histories.

### Orbital Expansion

The Earth-Moon distance is known to be increasing at $\approx 3.8$ cm/year from tidal
dissipation (LLR measurements). The primary cause is angular-momentum transfer from
Earth's rotation to the Moon's orbit via ocean tides. This is a local mechanical
effect, not a cosmological one.

For planetary orbits around the Sun, tidal effects are negligible (the Sun-Earth
energy dissipation rate is tiny). The Earth-Sun distance changes are dominated by
perturbations from other planets, and any secular trend is very small and not yet
measured directly with sufficient precision.

---

## Orbital Evolution in the Model

### Derivation

For an adiabatic circular orbit (varying slowly enough that angular momentum is
approximately conserved at each instant), the force balance is:
$$\frac{mv^2}{r} = \frac{GMm}{r^2} \implies v^2 = \frac{GM}{r}.$$
Angular momentum conservation: $L = mvr = \text{const}$.

Combining: $v = L/(mr)$ and $v^2 = GM/r$, so $L^2/(m^2r^2) = GM/r$, giving:
$$r = \frac{L^2}{m^2 GM}.$$

With invariant $m$ ($s = 0$), invariant $L$ (the isotropic vacuum exerts no torque —
T11), and $G \propto c^{-2}$ ($g = -2$):
$$r \propto \frac{1}{G} \propto c^{+2}.$$

The orbit expands as $r \propto c^2$. Since $c \propto (1+z)^{-1/2}$ (from the squared
redshift law), at $z = 1$ the Earth-Sun distance was
$$r(z=1) = r_\text{now} \cdot (c_\text{emit}/c_\text{now})^2 = r_\text{now}/\sqrt{2} \approx 0.707\,r_\text{now}.$$

### Orbital velocity

From $v = (GM/r)^{1/2}$ with $G \propto c^{-2}$ and $r \propto c^2$:
$$v \propto (c^{-2}/c^2)^{1/2} = c^{-2}.$$
As $c$ increases, orbital velocities **decrease**. Present orbits are slower than past
orbits in coordinate velocity, but atomic clocks also tick faster, so the orbital period
in proper time scales as $T_\text{proper} \propto r/v \cdot (c/c_0)^2 \propto c^4/c^2 = c^2$.
Orbital periods (in proper atomic time) increase as $c$ grows — years become longer.

---

## Constant Stellar Flux: Resolving the Faint Young Sun Paradox

### Stellar luminosity scaling

The luminosity of a main-sequence star is set by the nuclear burning rate, which
depends on the nuclear reaction cross-sections and the thermal conditions in the core.
In this model, with $\epsilon_0 \propto c^{-1}$ and atomic frequencies $\nu \propto c^2$,
the nuclear photon energies scale as $E \propto c^2$. The luminosity (energy per unit
proper time) scales as:
$$L \propto c^{2p} = c^4 \quad (p = 2\ \text{for invariant mass}).$$

As $c$ increases, stars get brighter as $L \propto c^4$.

### Flux balance

The flux received at a planet is:
$$F = \frac{L}{4\pi r^2}.$$
With $L \propto c^4$ and $r \propto c^2$:
$$F \propto \frac{c^4}{c^4} = \text{const}.$$
The stellar flux is **exactly constant** over cosmic time, regardless of the specific
value of $c$. Stars brighten as they age cosmologically, but planets move outward to
exactly compensate.

**This is not a coincidence**: it follows from $r \propto c^2$ (angular-momentum
conservation + $G \propto c^{-2}$) combined with $L \propto c^4$ (nuclear photon
energy $\propto c^2$, rate $\propto \nu \propto c^2$). Both are consequences of
$G \propto c^{-2}$ and invariant mass; they cannot come apart.

### Implications for the faint young Sun paradox

In this model, the faint young Sun paradox is automatically resolved — there is no
paradox, because the stellar flux at a planet has always been constant. The early Earth
received the same total solar flux as today (in proper-time units), even though the Sun
was "fainter" in absolute terms and the Earth was closer. The geological evidence for
liquid water at early epochs is fully consistent with the model.

This is a **genuine consistency success** — the model predicts constant flux without
fine-tuning, and the prediction matches the geological record.

---

## Present Orbital Expansion Rate

The present rate of orbital expansion:
$$\frac{\dot{r}}{r} = 2\frac{\dot{c}}{c} = 2H_0^{\text{hor}} = H_0^{\text{obs}} \approx 7 \times 10^{-11}\ \text{yr}^{-1}.$$
For the Earth-Sun distance $r_\oplus \approx 1$ AU $= 1.496 \times 10^{11}$ m:
$$\dot{r}_\oplus = r_\oplus \cdot H_0^{\text{obs}} \approx 1.496 \times 10^{11} \times 7 \times 10^{-11}\ \text{m/yr} \approx 10\ \text{m/yr}.$$

This is an expansion of $\sim 1$ cm/day, or about $10$ meters per year. This is
much larger than tidal effects for Earth's orbit, but is it observationally ruled out?

Current measurements of the Earth-Sun distance via planetary radar are accurate to
$\sim 1$–$10$ meters in absolute terms, but the **secular rate** over decades is
measured via spacecraft tracking and timing. No secular expansion of this magnitude
has been reported; the reported drift of the astronomical unit is an order of magnitude
smaller ($\sim 1.5$ m/yr from some analyses, with large uncertainty). Whether the
model's prediction is already excluded by planetary radar data is a quantitative
question that requires careful analysis. The $\dot{G}/G$ and $\dot{r}/r$ effects are
related (T8), and a self-consistent computation of both is needed.

---

## Broader Implications

### Planet formation and the habitable zone

As $c$ increases, orbits expand and the habitable zone moves outward. In the model,
the habitable zone expands at the same rate as orbits ($\dot{r}_\text{HZ}/r_\text{HZ}
= 2H_0^{\text{hor}}$), ensuring that a planet initially in the habitable zone **remains
there indefinitely** (to the extent that stellar mass and stellar evolution are
otherwise unchanged). This is a remarkable property: the universe may be fine-tuned for
long-term planetary habitability not by initial conditions but by the ongoing dynamics
of varying $c$.

### Long-period evolution

Looking back to $z = 1$: Earth's orbit was $\sim 0.7$ AU. At $z = 5$: $\sim 0.4$ AU.
The orbit was smaller, but the stellar flux was the same, and the star was proportionally
dimmer. The surface conditions on a planet at those epochs would be governed by the
same flux, hence similar temperature balance (to the extent that the atmosphere also
evolves self-consistently, which is a separate question).

### Binary stars and compact objects

For binary stellar systems, the same expansion $r \propto c^2$ applies. The orbital
period evolution and gravitational wave emission rate in a binary pulsar would be
modified relative to GR predictions (since $G$ changes). This is potentially testable
with the Hulse-Taylor binary and similar systems (T8).

---

## Open Questions

- A precise comparison with planetary radar and LLR data: is the predicted $\dot{r}/r
  \approx H_0^{\text{obs}}$ compatible with current measurements of the
  astronomical unit?
- The faint-young-Sun prediction is robust for constant atmospheric composition.
  The actual early Earth had a different atmosphere; detailed climate modelling is
  beyond scope, but the fundamental flux-constancy result is independent of atmosphere.
- The angular-momentum conservation argument (T11) is the key physics. It requires
  that the vacuum exerts no torque — i.e., that the vacuum field is exactly isotropic
  to the level of precision required. Are there corrections from local mass
  distributions that break this isotropy at measurable levels?
- Does the cosmological orbital expansion leave any signature in the geological record
  (e.g., in the periodicity of climate cycles, tidal rhythmites, or coral growth bands
  that record the length of the year)?
