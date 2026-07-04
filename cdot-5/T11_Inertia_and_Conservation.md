# T11 — Inertia and Conservation Laws

*Checked carefully against the counting-law change (Core Principles §1), as with
T5–T10. Result: **confirmed unaffected**, for the same structural reason as T7–T10:
everything here follows from the static map's *symmetries* (homogeneity, isotropy,
broken time-translation — Core Principles §0/§1, none of which reference the counting
law's functional form) and from fixed-redshift ratios (the squared law, $P=2$, T2). No
formula in this document integrates over cosmic history or references a horizon
*size*, so there is nothing here for the counting-law change to touch — a cleaner case
even than T9, since T11 doesn't need $H_0^\text{hor}$ at all.*

## Physical Concept

The conservation laws of a physical theory determine which quantities can be used as
reliable anchors across cosmic time and which cannot. In a universe with time-varying
$c$, the standard expectation — that energy is a conserved quantity — fails, and we
must derive from first principles what is actually conserved.

This topic also addresses the physical meaning of **inertia** in the model: what is the
origin of the resistance to acceleration, and how does it relate to the Machian premise
($c\propto N$)?

---

## The Symmetric Flip from Standard Cosmology

The model was constructed as the **conjugate frame** to standard cosmology. The
defining choice is:

| Quantity | Standard $\Lambda$CDM | This model |
|---|---|---|
| Photon energy in flight | Drops as $1/(1+z)$ | **Conserved** (premise 4) |
| Rest energy $mc^2$ | **Conserved** | Changes as $c$ changes |
| What "redshift" means | Photon lost energy | Atomic reference energy changed |

Neither frame is "more true" — they are related by the map ↔ observer transformation.
But the map frame is the one in which photons carry a conserved energy from emission to
detection, and it is in this frame that the model's dynamics are expressed.

---

## Conservation Laws from Symmetry

The static map has two exact symmetries and one broken symmetry — this is a statement
about premise 1 (static geometry) and the fact that *some* $c(t)$ varies (premise 2, in
whatever form), not about which specific counting law premise 2 takes:

- **Space translation symmetry** (the universe is homogeneous): by Noether's theorem,
  **linear momentum is conserved**.
- **Rotational symmetry** (the universe is isotropic): by Noether's theorem, **angular
  momentum is conserved**.
- **Time-translation symmetry is broken by $c(t)$**: by Noether's theorem, **energy is
  NOT conserved**.

These are not model assumptions — they follow from the symmetries of the map and the
corresponding Noether theorem. The result is firm regardless of $c(t)$'s specific
functional form: *any* non-constant $c(t)$ breaks time-translation symmetry, whether
it follows the old occupancy-counting power law or the new connectivity-counting
exponential. The result is firm: energy is precisely the quantity that can change in
this model, while momentum and angular momentum are precisely conserved. This is the
mathematical implementation of the symmetric flip.

---

## Free Particles: Peculiar Velocity Damping

For an unbound massive particle in free flight, with no external forces:
- Linear momentum is conserved: $p=p_0=\text{const}$.
- Mass is invariant: $m=\text{const}$.

In the relativistic formula with invariant mass:
$$u=\frac{p_0c}{\sqrt{p_0^2+m^2c^2}}.$$
This is an **increasing** function of $c$: the numerator $p_0c$ grows with $c$, while
in the non-relativistic limit the denominator $\approx mc$ grows at the same rate,
giving $u\approx p_0/m=\text{const}$. The coordinate velocity stays approximately
constant (NR) — it does not decrease.

What decreases is the ratio $u/c$ (velocity as a fraction of the current speed of
light):
$$\frac uc=\frac{p_0}{\sqrt{p_0^2+m^2c^2}}\propto(1+z)^{1/2},$$
where the $(1+z)^{1/2}$ scaling holds in the **non-relativistic limit**
($p_0\ll mc$), giving $u/c\approx p_0/(mc)\propto c^{-1}\propto(1+z)^{1/2}$. **This
exponent comes entirely from the squared redshift law ($P=2$, T2) — it does not
reference the counting law at all**, exactly the same separability already confirmed in
T7. It is unchanged from cdot-4 to cdot-5, letter for letter.

This is the model's **peculiar velocity damping**: free particles slow down *relative
to $c$* as the universe ages, even while their coordinate velocity stays approximately
constant. In $\Lambda$CDM, peculiar velocities in coordinate units decay as $(1+z)$;
here the coordinate velocity is conserved (NR: $p=mu\approx\text{const}$) but shrinks
relative to the growing $c$ as $(1+z)^{1/2}$. This is a consistency success: the model
does not predict runaway peculiar velocities, though the comparison with $\Lambda$CDM
differs in kind (velocity conserved here vs. damped there).

Meanwhile, the total energy $E=c\sqrt{p_0^2+m^2c^2}$ **increases** as $c$ grows. The
particle gains energy from the cosmos even while its coordinate velocity stays
constant. This is the symmetric flip in action: in $\Lambda$CDM, the same particle
would lose its peculiar momentum while its energy ($mc^2$) stays fixed.

---

## Bound Orbits: Angular Momentum Conservation

For a particle in a circular orbit, the relevant symmetry is isotropy: the vacuum is
isotropic, so **there is no torque available to change angular momentum**. Therefore:
$$L=mvr=\text{const}.$$
With $m$ invariant, $v=(GM/r)^{1/2}$ (force balance), and invariant $G$
($G\propto c^0$, T8):
$$L^2=m^2v^2r^2=m^2\cdot\frac{GM}{r}\cdot r^2=m^2GMr.$$
With $L$ invariant, $m$ invariant, and $G$ invariant: $r=L^2/(m^2GM)=\text{const}$.
**Orbits are static.** (T9 — a premise-3 result, already confirmed unaffected by the
counting-law change.)

The orbital energy $E=-GMm/(2r)=\text{const}$ as well — no energy drift in the orbit.
This is consistent with the symmetric-flip structure: energy is non-conserved for free
particles, but a bound orbit's energy is fixed when $G$, $m$, and $L$ are all
invariant.

---

## Inertia in the Model

The question of inertia divides into two parts: the origin and the magnitude. Both are
premise-3 (invariant mass) questions, untouched by premise 2's counting law.

### Not Sciama-type Machianism

Sciama's version of Mach's principle ties inertial mass to the gravitational potential
of the rest of the universe: $GM_u/(R_uc^2)\approx1$ (Sciama 1953). This would make
mass relational — the inertia of a particle depends on all the other matter in the
universe.

In this model, the Sciama relation fails — this conclusion is unchanged, though its
*quantitative* demonstration changed shape entirely under the counting-law revision;
see T12 for the full re-derivation and an important caveat about whether the ratio is
even cleanly computable under connectivity counting. The qualitative statement stands
regardless: the model's Machianism is in the counting rule ($c\propto N$), not in a
gravitational-potential relation, and nothing about replacing occupancy counting with
connectivity counting reintroduces a Sciama-type relation — if anything, the new
counting law makes even less contact with a fixed horizon "size" $R_u$ than the old one
did, so there is less structure available for a Sciama-type coincidence to hide in, not
more.

### What the model does say about inertia

Unchanged from cdot-4. The model is Machian about **$c$**, not about inertial mass.
The statement is: in a universe with only one particle (or none at all reachable from
a given point), $c\to0$ and the kinematic arena becomes vacuous — no clocks, no
rulers, no propagation. Dynamics become meaningless. (Under connectivity counting, the
precise statement is "no *reach*" rather than "no *occupancy*" — see T12 for the
updated language — but the physical conclusion is the same.)

But this is not the same as saying inertia vanishes. A particle alone in the universe
has the same rest mass (by premise 3), but no arena in which to exhibit it. "$c\to0$
for a lone particle" means physics becomes trivial, not that the particle has zero
inertia.

Inertial mass is **invariant and axiomatic** in this model (premise 3). The model does
not derive its magnitude — this is a limitation (it is what Mach's principle and the
Sciama formula aspire to do, and this model cannot). The connecton mechanism (T14)
specifically fails to provide an inertia-generating mechanism, by construction — this
is unaffected by which counting law the connecton sea's cosmological growth follows.

---

## The Interpretation of Energy Non-Conservation

Unchanged from cdot-4 — none of the three readings below reference the counting law's
functional form, only the fact that *some* $c(t)$ varies and that connectons exist as
a mechanism candidate.

**1. Connecton exchange (real mechanism).** A moving particle gains effective energy by
absorbing connectons (T14). Because each connecton carries energy $\sim\hbar H_0$, vast
numbers can boost a particle's energy without a thermal catastrophe (the total absorbed
power is negligible on astrophysical timescales). This is the only reading that posits
a physical mechanism; it ties energy non-conservation to the connecton field.

**2. Pure $c$-scaling (units).** Nothing physically flows; the quantity called energy
carries a factor of $c$, so it grows as $c$ grows — a bookkeeping/units effect. Rest
energy $mc^2$ grows not because the particle acquired a store of energy, but because
$c^2$ changed. Under this reading, rest energy is less fundamental than usually
assumed: $mc^2$ is a $c$-dependent quantity, not an invariant.

**3. Relational / Machian.** It is the addition of more particles to the universe
(premise 2: $c\propto N$, so growing $N$ raises $c$) that boosts a particle's effective
energy. Energy is referred to the global matter content, not traded with a local
reservoir. This is counting-Machianism extended from the arena ($c$) to energy. It is
the author's preferred reading, as it follows naturally from premise 2 and costs no
additional ontology. **Under connectivity counting, "$N$" here is network reach rather
than particle occupancy** — the reading survives the relabeling without any change in
substance, since the argument only needs "$N$ growing raises $c$," true under either
counting law.

**The "energy reservoir" phrasing is explicitly withdrawn** — it implies a local
source/sink for energy exchange that the physics does not support. The safe statement
is: energy is non-conserved on the map (the intended mirror of standard cosmology's
photon energy loss), and the correct physical interpretation is open.

---

## The Photon–Massive Particle Distinction

Unchanged from cdot-4. A subtle point: photons and massive particles conserve
*different* invariants under the same vacuum.

- **Photons** conserve frequency $\nu$ (energy $h\nu$). Evidence: cosmological
  spectral lines show a global redshift factor $1+z$ applied uniformly, consistent with
  frequency conservation in flight and a change in the atomic reference.
- **Massive particles** conserve momentum $p$. Follows from space homogeneity.

The difference is plausible: a photon has no rest frame, so it cannot be characterized
by momentum alone (since $p=h\nu/c$ and $c$ changes, a "conserved $p$" for a photon
would give a changing $\nu$, contradicting observation). The photon's robust invariant
is its phase — the number of wavefronts emitted equals the number received, which gives
frequency conservation. A massive particle has a rest frame, and its robust invariant
under space-homogeneity is its canonical momentum.

However, this argument has not been derived from a single Lagrangian that treats both
simultaneously. Whether a single VSL action can produce both $\nu=\text{const}$ for
photons and $p=\text{const}$ for massive particles consistently remains to be shown —
unchanged, still open.

---

## Open Questions

Unchanged from cdot-4 — none of these four questions are counting-law-sensitive:

- A VSL Lagrangian: is there a single variational principle that produces frequency
  conservation for photons and momentum conservation for massive particles, in a
  background with time-varying $c(t)$?
- The magnitude of peculiar velocity damping $(1+z)^{1/2}$ vs. $\Lambda$CDM's
  $(1+z)^1$: is this observable in large-scale peculiar velocity surveys (2MRS, 6dF,
  SDSS)?
- The relational interpretation of energy: is there a more explicit version that
  yields a checkable numerical prediction (e.g., the rate of energy gain per particle
  per Hubble time)?
- Can the argument that the vacuum exerts no torque (used to justify angular-momentum
  conservation) be made more rigorous? Are there corrections from the finite horizon
  (which breaks perfect isotropy at the largest scales)?
