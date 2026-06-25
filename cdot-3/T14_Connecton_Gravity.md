# T14 — Connecton Gravity

*Note: This topic is speculative — it is a research direction with a clear logical
structure and several quantitative checks, but it has not been adopted into the core
of the model. It is recorded here because it produced a specific negative result (the
ballistic/diffusive dilemma) that is worth preserving, and because it represents the
leading candidate for eventually deriving $G \propto c^{-2}$ from first principles.*

---

## The Idea

Gravity may share the same substrate that drives $c(t)$. The proposal is to posit a
field quantum — the **connecton** — that embodies the relational principle (T12)
physically: it is the carrier of the "connection" between particles that the counting
rule $c \propto N$ requires.

A connecton has the following properties:
- **Massless**, zero rest energy.
- **Near-zero but finite energy**: its wavelength is of order the horizon distance,
  giving frequency $\sim H_0$ and energy $\hbar H_0 \approx 1.5 \times 10^{-33}$ eV —
  the minimal quantum of the observable universe.
- **Propagates at the local speed of light** $c(t)$ at the time of propagation.
- **Conserved in number**: never destroyed. Momentarily absorbed by a massive particle
  (in a brief virtual $e^+e^-$ pair creation and re-emission), then re-emitted.
- **Emitted continuously by massive particles** (not only at creation); the emission
  rate is negligible in energy ($\sim 10^{-39}$ of rest energy per Hubble time) but
  ensures the counting-Mach relation holds at all epochs.

The horizon is the dominant source: horizon-scale connectons permeate the universe
from the first moments. At any point in space, the connecton density is dominated by
horizon-wavelength modes — long-wavelength, low-energy, pervasive.

---

## Energy Scale: The Minimal Quantum

A connecton with wavelength equal to the current horizon $R_0 = 6c_0/H_0^{\text{obs}}$
has frequency:
$$\nu_\text{connecton} = \frac{c_0}{R_0} = \frac{c_0 H_0^{\text{obs}}}{6c_0} = \frac{H_0}{6}.$$
More carefully, the horizon-wavelength mode has $\nu \sim H_0$, so:
$$E_\text{connecton} = h\nu \sim \hbar H_0 \approx 1.5 \times 10^{-33}\ \text{eV}.$$
This is not a free parameter — it is fixed by the horizon and not adjustable. It is the
same scale that appears in holographic/IR-cutoff discussions of dark energy and
gravitational entropy. The connecton hypothesis connects the cosmological expansion
($H_0$) to the fundamental quantum of the gravitational field.

---

## The Connecton Spectrum

Connectons emitted when the horizon was smaller have shorter wavelengths (higher
frequency). The spectrum has a dominant spike at the current horizon wavelength, with
a tail from connectons emitted at earlier (smaller-horizon) epochs.

For the volume law ($c \propto R^3$, $R \propto c^{1/3}$), the horizon at redshift $z$
was $R(z) = R_0(1+z)^{-1/6}$ (from Core Principles §4). The connecton wavelengths
range from $\lambda_0$ (current horizon) down to shorter values for earlier epochs.
The volume law's weak $(1+z)^{-1/6}$ scaling makes the spectrum **narrow**: all
connectons are within a factor of $\sim 3$ of the horizon wavelength (over any
accessible redshift range). This is unlike a broad spectrum theory; essentially
all connectons are in the same long-wavelength, low-energy regime.

---

## Scorecard Against Le Sage Objections

The connecton hypothesis is a variant of Le Sage gravity — a classical proposal
(Le Sage 1748) that gravity arises from a bombardment of "ultramundane corpuscles."
Le Sage theories have long been considered excluded by four objections. The connecton
hypothesis's scorecard:

### 1. Thermal catastrophe — SOLVED

**Le Sage problem:** a particle absorbing a constant flux of corpuscles must heat up
without limit.

**Connecton resolution:** connectons are **conserved** — when absorbed, they are
immediately re-emitted (after a virtual $e^+e^-$ pair, uncertainty time $\sim \hbar/mc^2$).
No energy is permanently absorbed. Poincaré's thermal objection applies to absorption
without re-emission; with perfect conservation, there is zero net energy deposition,
and the thermal catastrophe does not occur. This is exact and requires no tuning.

### 2. Drag — SOLVED

**Le Sage problem:** a moving body sweeps up more corpuscles from the front, decelerating.

**Connecton resolution:** gravity in this picture is a field gradient/delay effect,
not a momentum-transfer effect. Because the connecton energy is near zero, the
momentum per connecton ($p = E/c \sim \hbar H_0/c$) is negligible. Drag is proportional
to absorbed momentum, which is negligible per connecton; summed over the vast
population, the drag is still undetectable. This is quantitatively consistent with
the absence of observed gravitational drag on Solar System bodies.

### 3. Equivalence principle — CLEAN

**Le Sage problem:** different materials might have different "opacity" to corpuscles,
violating the equivalence principle (EP).

**Connecton resolution:** the source strength (the ability of a mass to emit and
re-absorb connectons) is $\propto$ particle count $\propto$ mass (invariant mass,
premise 3), and it is composition-independent: a proton and a neutron contribute
equally, as do electrons (modulo mass-weighting). The EP is clean by construction.

### 4. Distance law ($1/r$) — CONDITIONAL (central open problem)

**Le Sage problem:** geometric shadowing gives a $1/r^2$ flux deficit, leading to a
$1/r^3$ force (wrong).

**Connecton resolution attempt:** if connectons are absorbed and re-emitted with
**randomized directions** (diffusion), the steady-state connecton density satisfies a
Poisson equation $\nabla^2 \phi = -S\,\delta^3(\mathbf{x})$, whose Green's function
gives $\phi \propto 1/r$ — Newtonian $1/r$ potential, with $S \propto M$.

**The obstacle:** Newtonian $1/r$ requires diffusion (short mean free path, dense
scattering medium). Weak, long-range gravity requires transparency (ballistic transport
— connectons travel freely between galaxies). These two conditions — diffusion and
transparency — require opposite limits of the same scattering cross-section. A single
scattering medium cannot simultaneously be opaque (diffusion, $1/r$) and transparent
(long range, weak gravity).

In the natural case (sparse medium, long mean free path), connectons free-stream as
$1/r^2$ density halos around masses → force $\propto 1/r^3$ → wrong.

---

## The Ballistic/Diffusive Dilemma: The Central Unresolved Problem

The obstacle is a cousin of the original Le Sage thermal problem, but surviving at
the distance-law level even though conservation has already resolved the thermal/drag
issues.

**Attempted resolutions:**

1. **Matter is opaque, vacuum is transparent.** If only matter causes diffusion (not
   the vacuum between masses), then diffusion operates inside bodies but ballistic
   transport operates in the empty regions where long-range gravity acts.
   **Result:** still wrong. The $1/r$ Poisson equation requires diffusion in the
   regions where the $1/r$ form must hold — which are the empty regions between masses.
   Matter-only scattering gives $1/r$ only inside bodies; outside, the force law
   remains $1/r^3$.

2. **Self-interacting connecton sea.** If connectons scatter mainly off **each other**
   (or off the vacuum pair-field), the mean free path is set by the connecton density
   (which is very high everywhere, dominated by the horizon modes), not by the rare
   ordinary matter. The medium is then diffusive everywhere, including "empty" space.
   Ordinary matter only lightly perturbs this pre-existing diffusive medium. In this
   limit:
   - The diffusion equation holds in "empty" space → $1/r$ potential.
   - Gravity is a perturbation on the dense connecton sea → gravity remains weak.
   - This is a substantially different model: connectons as a self-interacting medium,
     not a thin gas.

This self-interacting sea picture is the leading candidate for escaping the dilemma, but
it has not been derived. Key open questions: (a) does the connecton-sea model give a
Newtonian $1/r$ force with the right coefficient? (b) does it give $G \propto c^{-2}$
with the right magnitude? (c) is it consistent with the global $\dot{c}/c = H$
bookkeeping?

---

## The Inertia No-Go Result

As a productive by-product of the connecton analysis, there is a clean argument showing
why the connecton **cannot** source inertia:

Gravity (in the connecton picture) is a gradient/sink/delay effect: the force arises
from the asymmetry of an incoming connecton field caused by an intervening mass. This
requires the connecton to carry **no net momentum** relative to a free-falling frame
(otherwise drag would violate the EP). A zero-momentum field cannot deliver a
momentum-reaction force to accelerate an inertial mass.

Gravity requires momentum-neutral connectons; inertia requires momentum-carrying
connectons. One field cannot do both.

This explains — at a mechanism level — **why inertial mass must be invariant and
axiomatic** (premise 3) rather than emergent from the connecton field. It is also
consistent with the impossibility of Sciama-type inertia from the counting-Mach rule
(T12, T11).

---

## Connection to the PV Framework

In the Polarizable Vacuum (PV) framework (Puthoff 2002), gravity is mediated by
variations in the vacuum refractive index $K = c_0/c$, with $g \propto -\nabla(\ln K)$.
The connecton capture-delay effect — when a mass perturbs the local connecton density,
it locally reduces $c$ (raising $K$) — is the microscopic origin of the PV refractive
index. In this reading, the connecton field *is* the PV vacuum, and the PV equations
are the macroscopic limit of the connecton dynamics. This makes $G \propto c^{-2}$ a
natural consequence: in PV, $G \propto c^4/(G_\text{Newton}\cdot c^2) \propto c^{-2}$
when normalized to the present-day value.

---

## Open Items, In Priority

1. **The ballistic/diffusive dilemma** — does the self-interacting connecton sea
   picture give diffusion at range (hence $1/r$) without making gravity strong at
   short range? If yes, this is the primary success of the connecton hypothesis and
   would establish a plausible mechanism for Newtonian gravity.

2. **Coefficient derivation** — if diffusion holds at range, does the resulting
   Poisson-equation Green's function give $G \propto c^{-2}$ with the correct
   magnitude, not just the $1/r$ form?

3. **Global bookkeeping** — is $\dot{c}/c = H$ from the connecton termination/turnover
   rate consistent with the same field giving local Newtonian gravity? The two
   requirements (global $c$ growth and local $1/r$ force) come from the same field and
   must be mutually consistent.

4. **Light bending** — does the connecton's propagation in a $K$-gradient background
   give the correct general-relativistic prediction for light deflection by the Sun
   ($1.75''$)? The PV framework gives the right answer; the connecton picture should
   reduce to PV in the appropriate limit.

5. **Whether matter must emit continuously or only at creation.** Continuous emission
   (preferred) gives clean EP and negligible energy drain. Emission only at creation
   would make the matter contribution history-dependent and could break the relational
   principle.
