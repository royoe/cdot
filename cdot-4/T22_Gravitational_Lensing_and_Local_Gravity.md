
# T22 — Gravitational Lensing and Local Gravity

*Note: This topic is speculative and unfinished — it checks whether the model's local
(solar-system-scale) gravity survives confrontation with PPN data (light bending, Shapiro
delay, gravitational redshift) and with planetary ephemerides. Three sessions feed this
topic. The first pass assumed symmetry with Polarizable Vacuum (PV) theory and concluded
that alignment requires an explicit new local premise (a "Two-Regime Dictionary": mass
locally dressed as $m\propto K_\text{grav}^{3/2}$, distinct from its cosmological
invariance) forced by two data points. A second pass reconsidered the force sector via
the gravitoelectromagnetic (GEM) correspondence and exposed a serious, independent
crisis: the derived RAR closure (T14/T15), taken to the solar-system regime, predicts an
anomalous acceleration excluded by planetary ephemerides by ~3.5 orders of magnitude. A
third pass — prompted by re-examining the second pass's own derivation for
overcomplication — replaced the Two-Regime Dictionary entirely with a much simpler
picture: gravity as a coherent inflow ("river") of a free-streaming fraction of the
connecton sea, falling at the classical escape velocity $w=\sqrt{2GM/r}$. This is the
Gullstrand–Painlevé form of the Schwarzschild metric, and if the medium carrying it also
carries light (a natural reading of an existing premise, T12), the model reproduces exact
GR light bending, Shapiro delay, redshift, and perihelion precession **without any new
mass-dressing premise, and with mass strictly invariant everywhere** — resolving the T8
invariant/PV mass fork by dissolving it rather than regime-splitting it. **The Two-Regime
Dictionary is superseded and withdrawn from this topic.** The river construction also
gives the tail crisis a derived target (an exact identity linking the closure's exponent
to a speed ratio) and a named, well-posed open calculation, in place of the two vaguer
"resolution paths" first recorded. Nothing here is adopted into Core Principles — the one
premise the whole picture rests on (light is advected by the sea's bulk flow) is flagged
explicitly in §2 as underived.*

---

## 1. The Question

The model departs from GR in two premises that matter locally: mass is invariant
(T8/T21), and $G$ is invariant (T8, adopted after the ×720 LLR refutation of
$G\propto c^{-2}$). Does the model still reproduce PPN $\gamma=\beta=1$ light bending,
Shapiro delay, and gravitational redshift at the precision solar-system tests require —
using the same invariant $m$, $G$ used everywhere else in cdot-4, with no local
exception?

## 2. The River: Local Gravity as a Coherent Inflow

### 2.1 Why a second component is needed

T14 already derives a Newtonian potential $\phi=-GM/r$ from connecton diffusion: masses
absorb and re-emit connectons, and net emission sources a Poisson profile in the
foam-scattered, short-mean-free-path ("diffusive") population. Two quick checks show
this diffusive population cannot, by itself, also carry a coherent inflow:

- **Pure reshuffling cancels.** A mass that only absorbs and isotropically re-emits, at
  equal rate, produces zero net perturbation — the shadow deficit from its direction is
  exactly replaced by the re-emission surplus from the same direction. This is why T14's
  *net* (continuous-emission) source term is load-bearing, not decorative.
- **Diffusion is far too slow.** The diffusive drift speed implied by $D=c\lambda/3$
  with the foam's sub-Compton mean free path is $\sim10^{-20}$ m/s at Earth's surface,
  versus the $\sim11.2$ km/s (Earth's escape velocity) a coherent infall would need —
  short by 24 orders of magnitude. A medium with a $10^{-12}$ m mean free path damps any
  bulk flow at km/s instantly.

So the potential-carrying diffusive population and any coherent bulk inflow must be
**two distinct fractions of the sea** — exactly the ballistic/diffusive split T14 already
introduces for the distance-law problem (§"The Obstacle," T14), just applied to two
coexisting populations instead of one. The diffusive fraction sources $\phi$; a
**ballistic (long-mean-free-path, free-streaming) fraction** carries the inflow. No new
ontology is required — the model already has both transport regimes on the table.

### 2.2 The simple derivation

Model the ballistic fraction as ordinary free-falling matter: pressureless, and — because
it does not scatter — dissipationless. A pressureless fluid element falling from rest
conserves specific mechanical energy along its path:
$$\tfrac12 w(r)^2 + \phi(r) = E.$$
The boundary condition is the cosmological one already used throughout this model: the
sea is at rest in the map frame at spatial infinity, where $\phi\to0$, so $E=0$. Hence
$$\boxed{w(r) = \sqrt{-2\phi(r)} = \sqrt{2GM/r}}$$
— the ordinary escape/infall speed, nothing more exotic than energy conservation for a
particle dropped from rest at infinity, now applied to the sea's own ballistic
component rather than to an external test mass. (Earlier drafts reached the same
formula through a quantum superfluid treatment — Madelung transform, a condensate order
parameter, and a "quantum potential" term shown to vanish for this profile. That
machinery is not needed: for a pressureless, non-scattering population the quantum
pressure term isn't there to cancel in the first place. Treating the ballistic fraction
as ordinary collisionless matter, not a Bose condensate, gets to the same result in three
lines and — as a bonus — removes a manufactured problem: the superfluid picture implied
quantized circulation ($\kappa=h/m_c$) mismatched with the Sun's frame-dragging
circulation by 29 orders of magnitude. An ordinary collisionless population carries no
such quantization, so that tension simply does not arise. Whether/how it carries angular
momentum for frame dragging is still open — §3 — but it is now an ordinary kinetic-theory
question, not a manufactured no-go.)

**Newton recovered.** For steady radial flow, a comoving parcel's acceleration is the
convective derivative $w\,dw/dr = \tfrac12\,d(w^2)/dr = -GM/r^2$ — Newton's law, exactly,
as the material derivative of the flow. Free fall is comoving with the ballistic
component; there is one potential and one coupling, so no double-counting arises and the
equivalence principle is structural rather than assumed.

**A horizon, if light rides the same flow.** $w(r)=c$ at $r=2GM/c^2$ — the Schwarzschild
radius. The metric this flow defines,
$$ds^2 = -c^2dt^2 + (dr - w\,dt)^2 + r^2 d\Omega^2,$$
is the Gullstrand–Painlevé form — a standard, exact rewriting of the Schwarzschild
solution in different coordinates (Painlevé 1921; Gullstrand 1922; popularized as the
"river model" by Hamilton & Lisle 2008), valid outside any static spherical mass by
Birkhoff's theorem, not just for black holes. Being the same spacetime, it reproduces
GR's light bending, Shapiro delay, gravitational redshift, and perihelion precession
exactly, automatically, with **no separate index law and no local mass dictionary** —
*provided* light is actually carried by this flow.

**The one premise this rests on.** That proviso is not free. In laboratory analog-gravity
systems (e.g. BEC black-hole analogs), the acoustic metric governs phonons in the fluid,
not light, which is external to the medium and indifferent to its flow. Here the
situation is more favorable, because light is not external: T12 already identifies the
model's global light speed $c(t)$ with the connecton sea's own signal speed. Extending
that identification locally — light propagates as an excitation of the same medium whose
bulk flow is $w(r)$, and is advected by it exactly as the medium's own signals would be —
is a single, physically motivated assumption, not an independently new one. Call it the
**Flow-Coupling Premise**: *light is advected by the connecton sea's local bulk flow
$w(r)$, because light already shares the sea's signal speed globally (T12).* Granting it
delivers the full PPN success above from a Newtonian potential (T14) plus energy
conservation (undergraduate mechanics) — no coefficients to fit. This is considerably
lighter than the withdrawn Two-Regime Dictionary, which needed two independently-tuned
exponents ($A=2$, $\sigma=3/2$) with no first-principles source. But the premise is not
yet derived, and one input this construction leans on — a "uniqueness theorem" said to
show strict $m,G$ invariance forces pure-flow behavior with $A=0,\xi=1$ — comes from a
prior session whose write-up is not present anywhere in this repository. Until that
theorem is reconstructed and checked, or an equivalent argument is made from scratch,
this section's headline claim ("exact Schwarzschild phenomenology, no dressing needed")
should be read as promising and well-motivated, not established. See §4 open items.

**Mass stays invariant, full stop.** Because no local dressing is needed, the T8 fork
between invariant mass (cosmology) and PV mass (the withdrawn local dictionary) is
resolved by elimination rather than regime-splitting: mass is invariant everywhere,
matching every other topic in cdot-4. No edit to T8 or Core premise 3 is required.

### 2.3 Where the river ends

Stationarity requires the local infall acceleration $GM/r^2$ to exceed the sea's own
global rate of change, $\dot c\sim3g_\dagger$ (T14 kinematics). Equating them,
$$r = \sqrt{GM/3g_\dagger} = r_t/\sqrt3,$$
gives the MOND transition radius directly from the flow picture, with no new parameter —
unchanged from, and independent of, the superfluid-vs-ballistic framing question above.

## 3. GEM as the Force-Sector Frame

The river fixes *why* $\phi_g\propto M/r$ produces the right kinematics for a test
population, and now for light. It says nothing about whether the model's real preferred
frame (the static sea; the solar system moves through it at ~370 km/s,
$(v/c)^2\approx1.5\times10^{-6}$) produces a fatal preferred-frame signature, or how
frame dragging arises. The gravitoelectromagnetic (GEM) correspondence — the
$(g_{00},g_{0i})$ Maxwell-like sector of linearized GR, sourced by mass currents — fits
the connecton program natively: the sea already carries momentum currents with exact
conservation (T11); the coherent-flow field $B_c$ used in T17/T19 is already a
gravitomagnetic-type object; the river above supplies $\mathbf{E}_g$; and collective
modes propagate at $c$, giving $c_\text{gw}=c$ for free (closes the GW170817
premise-level check, $|c_\text{gw}-c|/c<10^{-15}$).

**Candidate resolution of $\alpha_2$ (conditional, not yet derived).** If the connecton
sector's collective dynamics are Maxwell-like *and* emergently Lorentz invariant at speed
$c$, uniform motion through the sea is unobservable to the force sector:
$\mathbf{E}_g,\mathbf{B}_g$ transform into each other as in electrodynamics, giving
$\alpha_1=\alpha_2=0$ identically — a Lorentzian-ether structure (ontological preferred
frame, no kinematical signature). **This is a derivation target, not a premise**: a
fundamental Lorentz-invariant massless vector field sourced by mass is otherwise
forbidden (spin-1 no-go — like-source repulsion, or negative field energy if the sign is
flipped). The connecton route would have to escape via its kinetic-medium character;
locating this evasion is the central open theoretical task.

**Empirical fingerprints, two-sided:**
- **Lense–Thirring normalization.** GR: $2GJ/(c^2a^3(1-e^2)^{3/2})$, including the spin-2
  factor 4 a naive spin-1 analogy misses — LARES-tested to ~2%, GP-B to ~19%. Now a
  question about how the *ballistic* population (§2) transports angular momentum —
  ordinary collisionless kinetic theory, not vortex quantization (§2.2). Deriving the
  factor 4 would be a landmark success; missing it is a clean kill.
- **Quadrupole radiation coefficient.** Dipole radiation vanishes automatically (mass ≡
  gravitational charge $\Rightarrow\dot{\mathbf d}=\mathbf P=$const); the double pulsar
  tests the GR quadrupole coefficient to $1.3\times10^{-4}$ — well-posed, uncalculated.

**Two gravitomagnetic regimes required.** The galactic $B_c$ of T17/T19 is a deep-MOND
coherent-flow object, enormously stronger than GR frame dragging from the same mass
currents. Consistency requires $B_c$ to reduce to GR's tiny dipole in the Newtonian
(solar-system) regime — any enhancement above GR is excluded at the 2% level (LAGEOS) —
while the coherent-flow enhancement operates only in the trans-critical regime, governed
by the same transition (§2.3) as the tail crisis below.

## 4. Major Confrontation: The RAR Closure's High-Acceleration Tail vs Planetary Ephemerides

Taking the solar-system domain seriously exposes a confrontation invisible to galaxy
data. The RAR closure derived in T14/T15,
$$g_x(g_x+g_\text{bar}) = g_\text{bar}\,g_\dagger,$$
is MOND's *simple* interpolating function. Its high-acceleration asymptote is
$$g_x \to g_\dagger - g_\dagger^2/g_\text{bar} \quad (g_\text{bar}\gg g_\dagger),$$
i.e. a **constant anomalous sunward acceleration $\approx1.13\times10^{-10}$ m/s²**,
essentially identical at Earth, Saturn, and Neptune. Planetary ephemeris bounds on
anomalous constant accelerations at Saturn ($\sim4\times10^{-14}$ m/s², Cassini-ranging
era) exclude it by a factor ~2800 (~3.5 orders of magnitude) — matching the known result
that ephemeris analyses (Hees et al. 2014, 2016) exclude MOND's simple interpolating
function specifically, while the exponential MLS form
($g_\text{obs}=g_\text{bar}/(1-e^{-\sqrt{g_\text{bar}/g_\dagger}})$) leaves a negligible
residual there. The 0.020 dex galactic match (T14/T15) cannot distinguish simple from
MLS-exponential — they diverge only at $g_\text{bar}/g_\dagger\sim10^5$–$10^8$, the
solar-system regime, so this exposure is invisible at galactic scale.

**The river gives the fix a derived target.** Define the cosmological Bernoulli speed
$v_c(r)=\sqrt{2g_\dagger r}$ — the speed the sea's global floor acceleration would build
over scale $r$. Then, identically,
$$\frac{w(r)}{v_c(r)} = \sqrt{\frac{g_\text{bar}}{g_\dagger}},$$
which is exactly the exponent of the MLS/RAR exponential function. This is an exact
algebraic identity (independent of the ballistic-vs-superfluid framing question in §2 —
it only uses $w=\sqrt{2GM/r}$ and $g_\dagger=c^2/R_0$), not a conjecture.

**What remains conjectural is the suppression law.** If the closure's anomalous
component $g_x$ is carried specifically by the fraction of the sea *not* entrained in
the coherent river — suppressed as $e^{-w/v_c}$, on the physical picture that deep in a
well ($w\gg v_c$) everything is swept into the coherent inflow (pure Newton/GR, no
marginal population left over), while in the outskirts ($w\lesssim v_c$) the global drift
competes and the marginal population saturates at the $g_\dagger$ floor — then the
closure's functional form shifts from simple to the MLS exponential exactly where
ephemerides need it: at Saturn, $\sqrt{g_\text{bar}/g_\dagger}=755$, so
$e^{-755}\approx0$, dissolving the exclusion. This would also predict a small,
falsifiable difference from the plain simple-function fit in the galactic transition
region (up to ~4.5% at $g_\text{bar}/g_\dagger\approx10$) — comparable to, and possibly
already resolvable against, the 0.020 dex SPARC-class data. **The entrainment/depletion
rate itself is not yet derived** — it requires the exchange kinetics between the
diffusive and ballistic populations — and is now the single most consequential
calculation in the program (§5, item 1).

**The honest stake.** If the entrainment law cannot be derived to match the MLS form (or
some other cutoff sufficient to pass ephemeris bounds), the pointwise closure is
falsified in the high-acceleration regime, and the T14/T15 RAR result must be demoted
from a derived closure to an emergent galactic-scale relation with an unexplained domain
boundary.

## 5. Status and Open Items, In Priority

1. **[Top priority] The entrainment/depletion law, §4.** One law, $e^{-w/v_c}$ or
   equivalent, would simultaneously (a) shift the RAR closure from simple to the
   empirically-preferred MLS exponential and (b) dissolve the ephemeris exclusion
   identically. The target identity is derived and exact; only the suppression kinetics
   remain open.
2. **The Flow-Coupling Premise and its "uniqueness theorem," §2.2.** The claim that light
   is advected by $w(r)$ (giving exact GR phenomenology for free) is well-motivated by
   T12 but not derived, and leans on a "uniqueness theorem" from a session not recorded
   anywhere in this repository. Reconstruct or re-derive it before treating §2's headline
   result as established.
3. **Amplitude normalization** (inherited from T14): $\delta n\to\phi$ must reproduce $G$
   at the correct magnitude from connecton microphysics. The river construction inherits
   this unchanged — it does not add a new dependency, but does not resolve the old one.
4. **Preferred-frame $\alpha_1,\alpha_2$ (§3).** Raw scale $(v/c)^2\approx1.5\times10^{-6}$
   sits an order of magnitude above the $\alpha_2$ bound ($<4\times10^{-7}$); the
   emergent-Lorentz-invariance argument is a candidate zero, not a proof.
5. **Angular-momentum transport / Lense–Thirring (§3).** Now an ordinary collisionless
   kinetic-theory question for the ballistic population (the superfluid-vortex framing
   and its manufactured quantization mismatch are withdrawn, §2.2) — still uncalculated.
6. **Quadrupole radiation coefficient (§3)** — well-posed, uncalculated.
7. **Two-population origin.** Why does the sea partition into a diffusive (scattering)
   fraction and a ballistic (free-streaming) fraction at all, and what sets the split?
   Parallel theoretical debt to invariant $G$/invariant $m$ (T8).

**Cross-references.** T14 open item 5 (light bending) points here. T8 §"Why Mass is
Invariant" — no edit needed; mass remains invariant everywhere, the local dressing this
topic once proposed is withdrawn (§2). T17/T19 — the two-gravitomagnetic-regimes
requirement (§3) is a consistency constraint on $B_c$, not yet built into either topic.
T15 — once the entrainment law (item 1) is resolved one way or the other, the RAR
comparison should be re-run with the MLS form alongside simple; the transition-region
difference (≤4.5%) is close to current data resolution. Core Principles — no premise
addition proposed; §2's Flow-Coupling assumption is recorded here, pending item 2, rather
than promoted to Core.
