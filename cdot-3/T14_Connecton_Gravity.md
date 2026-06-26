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

This self-interacting sea picture is the leading candidate for escaping the dilemma.
Its full development is in the next section.

---

## The Connecton Sea = Quantum Foam: Escaping the Dilemma

Identify the dense self-interacting connecton sea with the **quantum foam** — the
virtual $e^+e^-$ pairs of the QED vacuum. No new ontology is required: quantum foam
already exists and has density $\sim 1/\lambda_\text{Compton}^3 \sim 10^{37}$
m$^{-3}$.

If connectons scatter off this foam, the mean free path is sub-Compton → **diffusion
everywhere**, including "empty" space. Ordinary matter is only a weak perturbation on
the pre-existing dense medium → gravity stays weak. The $1/r$ Poisson equation holds
everywhere (diffusion in empty space, not just inside bodies):
$$\nabla^2\rho = S\,\delta^3(\mathbf{x}) \implies \rho \propto \frac{1}{r},
\quad S \propto M.$$

This **resolves the ballistic/diffusive dilemma**: the foam is the diffusive medium;
ordinary matter perturbs it weakly. The $1/r$ potential is restored, weak and
EP-clean (source strength $\propto M$, composition-independent).

It also **dodges the geometric $10^6$** (T5): a steady-state diffusion profile is not
a light-travel-time effect — it carries no $d/(c/H_0)$ suppression. This is the first
mechanism in the project that is both the right *type* (acceleration-keyed, not
distance-keyed) and free of the geometric death.

The connecton capture-delay in the foam is the microscopic origin of the PV refractive
index perturbation: a mass perturbs the local connecton density, locally reducing $c$
(raising $K$), and $g \propto -\nabla(\ln K)$ is the PV/Dicke force — so the connecton
picture reduces to the PV equations in the macroscopic limit, making $G \propto c^{-2}$
natural (the PV/Dicke-native value).

---

## Toward the RAR: A Gradient-Keyed Transition

Pure diffusion gives Newton ($g \propto 1/r^2$) — no MOND. The route to MOND requires
a **transition**: Newton above $g_\dagger$, modified below it. Two natural keying
possibilities were examined:

**Keyed to density** (mass perturbation $\sim$ background): fails. The mass
perturbation being comparable to the background gives a **mass-dependent** scale
$g_t \propto 1/M$ — wrong for the universal RAR.

**Keyed to gradients** (cosmological background gradient): works structurally. The
cosmic connecton sea rises with horizon distance, carrying an intrinsic background
gradient:
$$|\nabla\rho_\text{bg}| \sim \rho_\text{bg} H_0 / c \quad\text{(mass-independent,
cosmological)}.$$
Where the mass's connecton-density gradient drops to this background level, the
transition acceleration is:
$$g_t = \kappa\rho_\text{bg} H_0 / c \quad\text{(mass-independent)},$$
which is $\sim cH_0$ if $\kappa\rho_\text{bg} \sim c^2$ — the right structure for the
RAR (T15): universal $\sim cH_0$ onset, no dependence on galaxy mass or size.

### The closure condition $V = c$

The condition $\kappa\rho_\text{bg} \sim c^2$ is dimensionally a velocity$^2$ (forced
by the force law $g = \kappa\nabla\rho$). So it is the single physical statement
$V = c$ — the sea's characteristic velocity is the connecton propagation speed. One
power of $c$ is structural ($D = cL/3$ — connectons move at $c$). The other is a
concrete microphysical closure condition:
$$\frac{4\pi G L\rho_\text{bg}}{3\sigma} = c,$$
linking per-mass emission $\sigma$, mean free path $L$, and background density
$\rho_\text{bg}$. This is plausible and a specific derivation target, not a free fit.

This is distinct from the earlier OP-3 dimensional sleight-of-hand: there, the
"amplification" had no force-law backing. Here, $g = \kappa\nabla\rho$ is the actual
force law, and $V = c$ has definite physical meaning (the sea's signal speed).

### Caveat 2: the functional form is the wall

The gradient-keyed approach gives the **scale** $\sim cH_0$ for the transition — but
not the **functional form** of the RAR. The deep-MOND regime requires the
low-gradient diffusion to take the specific form $D \propto |\nabla\rho|$ (equivalently,
Bekenstein-Milgrom $\mu(x) \to x$ in the deep limit). If it did, everything would
close beautifully: $g \propto 1/r$ (flat curves), $v^4 = GM\,a_0$ (Tully-Fisher), and
$a_0 = cH_0$ — the same $V=c$ condition fixing the scale in both regimes.

But no independent physical reason for $D \propto |\nabla\rho|$ was found. Worse, the
natural reading (small mass-gradient riding on the large cosmic background gradient)
gives back *linear* response — Newton-on-a-background, **no MOND enhancement** — and
the obvious nonlinearity (flux saturation) pushes in the wrong direction (toward the
strong-field end). **Honest status:** the foam-sea robustly delivers Newtonian $1/r$;
the MOND/RAR functional form (T6, T15) does not fall out and is currently disfavored
by the natural reading.

---

## The $\sqrt{M}$ Problem: Linear Mechanisms vs. MOND

An additive two-component force law $\mathbf{g} = \mathbf{g}_\text{Newton} +
\mathbf{g}_\text{cosmo}$ (GEM-inspired) is the right *framing*: it leaves Newton
intact and avoids wrecking Solar System tests. The cosmological term must go as $1/r$
(a constant gives rising curves; $1/r^2$ just rescales $G$). But the MOND term must be:
$$g_\text{cosmo} \propto \frac{\sqrt{M}}{r} \quad\text{(Tully-Fisher: }v^4 = GM\,a_0\text{, T6)}.$$
This $\sqrt{M}$ is MOND's irreducible signature (T6, T15).

A *linear* additive term — the literal GEM analogue, since GEM is a linear theory
($\mathbf{B}_g \propto$ mass current $\propto M$) — gives $M/r$, hence $v^4 \propto M^2$:
**the wrong Tully-Fisher slope**.

**General diagnosis:** every natural mechanism (retardation, linear diffusion, additive
GEM-like terms) is *linear in $M$*. MOND's $\sqrt{M}$ demands a **nonlinear source
coupling**. This is why the scale keeps matching (dimensional, linear-friendly) while
the functional form keeps failing (needs nonlinearity). The one genuine nonlinearity
in the model is the **self-interacting connecton sea** — whether it can generate a
$\sqrt{M}$ coupling is the make-or-break question.

---

## The Catalytic-Cycle Calculation (Negative Result)

The author's favored self-interaction: connectons **catalyze** transient virtual
$e^+e^-$ pairs (triggering pair formation, driving $\dot{c}$ via premise 2) and are
re-emitted (capture/re-emission — nothing destroyed, conservation symmetry preserved).
The virtual pair is the *localized* intermediary the horizon-wavelength connecton
lacks. This was calculated in three stages:

1. **Real non-analytic $\sqrt{\phantom{E}}$.** The threshold density of states for pair
   creation gives $g \propto \sqrt{E_\text{exc}}$ — exactly the non-analytic form MOND
   needs.

2. **Wrong argument.** $E_\text{exc}$ is set by the pair's own rest energy
   ($\sim 2m_e c^2 \sim$ MeV), which swamps the galactic field-gradient energy
   ($|\nabla\phi|\lambda_C$) by $\sim 10^{33}$. The $\sqrt{\phantom{E}}$ is a
   *constant* prefactor, not $\sqrt{|\nabla\phi|}$.

3. **Collective version gives Newton.** The coarse-grained / collective version
   gives linear drift (Einstein relation: $v_\text{drift} \propto F$) → Newtonian
   gravity. The only route to sublinear ($\sqrt{}$) collective response is
   **cooperativity** (one pair's formation enhancing neighbors') — criticality —
   which belongs at the strong-field end, not the weak-field MOND end.

**Verdict:** the catalytic cycle robustly gives Newtonian gravity but **not MOND**. The
$\sqrt{M}$ requires a weak-field cooperative/non-analytic coupling that this mechanism
(like retardation, linear diffusion, additive GEM terms) does not supply. Not a proof
the model cannot do MOND, but a precise statement of what is missing.

---

## Criticality-as-License and the Lorentz-Form Target

### Two roles for central-black-hole criticality

All galaxies possess central black holes = strong-field critical surfaces. Two roles:

- **Role 1** (BH critical region *sources* the effect): ruled out. The amplitude would
  scale with $M_\text{BH}$, destroying the universal $a_0$.
- **Role 2** (criticality is an *existence condition* that *licenses* the non-analytic
  coupling, while the horizon sets the scale $a_0 \sim cH_0$): survives. The BH
  criticality need only *exist somewhere* (not operate in the weak field) to permit a
  non-analytic $B_c$ source, and $a_0$ stays universal. This dissolves the
  catalytic-calc dead end: criticality-as-license need only hold globally, not at
  every test-mass location. **Open:** a localized ($\sim$AU) BH critical surface
  licensing a coupling that acts at $\sim10$ kpc requires a
  global/topological condition, not a local source — conceivable, unproven.

### The Lorentz-form target equation

The two-component law sought is:
$$\mathbf{g} = \mathbf{g}_\text{Newton} + \mathbf{v}_\text{star} \times \mathbf{B}_c,$$
where $\mathbf{B}_c$ is a magnetic-like component of the $c$-field — a
*velocity-dependent* cross-product term. For a flat rotation curve, $B_c \sim v/r$,
i.e. $B_c \propto (GM\,a_0)^{1/4}/r$, and then:
$$v_\text{star} \times B_c = \frac{\sqrt{GM\,a_0}}{r}$$
**carries the correct $\sqrt{M}$** (deep-MOND + Tully-Fisher, T6). This repackages
the difficulty onto the source: $B_c$ must be sourced $\propto M^{1/4}$, an even more
non-analytic scaling than $\sqrt{M}$.

**Conjecture** (connecting criticality-as-license and the Lorentz form, unproven):
Role-2 criticality may be exactly what permits a non-analytic $B_c$ source, with the
$v\times B_c$ structure then delivering $\sqrt{M}$ and a horizon-set $a_0 \sim cH_0$
(T6). This is the first framing where velocity-dependence, the $\sqrt{M}$ requirement,
and a universal $a_0$ coexist without immediate contradiction — a direction for future
work, not a result.

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

1. **(Make-or-break) The RAR functional form.** Solve the nonlinear diffusion in the
   foam-sea picture: does it yield the deep-MOND $g \propto \sqrt{M}/r$ law and the
   RAR interpolating function, not just the $\sim cH_0$ scale? The catalytic-cycle
   route has been tested and gives Newton; the Lorentz-form $v\times B_c$ route
   (with criticality-as-license) is the live next target. Whether there is a
   weak-field cooperativity in the connecton foam is the central open question.

2. **Prove the closure condition** $4\pi G L\rho_\text{bg}/(3\sigma) = c$ (the $V=c$
   statement) — one power of $c$ is already structural ($D = cL/3$); the other
   requires a derivation linking the emission rate, mean free path, and background
   density.

3. **Coefficient derivation** — does the resulting Poisson-equation Green's function
   give $G \propto c^{-2}$ with the correct magnitude, not just the $1/r$ form?

4. **Global bookkeeping** — is $\dot{c}/c = H$ from the connecton termination/turnover
   rate consistent with the same field giving local Newtonian gravity? The two
   requirements (global $c$ growth and local $1/r$ force) come from the same field and
   must be mutually consistent.

5. **Light bending** — does the connecton's propagation in a $K$-gradient background
   give the correct general-relativistic prediction for light deflection by the Sun
   ($1.75''$)? The PV framework gives the right answer; the connecton picture should
   reduce to PV in the appropriate limit.

6. **Whether matter must emit continuously or only at creation.** Continuous emission
   (preferred) gives clean EP and negligible energy drain ($\sim 10^{-39}$ of rest
   energy per Hubble time). Emission only at creation would make the matter
   contribution history-dependent and could break the relational principle.
