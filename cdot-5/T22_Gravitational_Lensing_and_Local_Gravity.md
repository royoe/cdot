# T22 — Gravitational Lensing and Local Gravity

*Checked against the counting-law change: this entire topic is **local, solar-system-
and galactic-scale physics** — the river construction (§2), the GEM force-sector frame
(§3), and the RAR-closure-vs-ephemeris confrontation (§4) — evaluated at fixed cosmic
epoch throughout. None of it references $N$, $R$, or the horizon law; $g_\dagger$ and
$G$ enter as external parameters exactly as in T14/T15/T17. **Confirmed unaffected in
full**, the same pattern already established for T14 (connecton gravity) and T17
(galaxy morphology). This document is carried forward from cdot-4 essentially verbatim;
the only cdot-5-specific note is that wherever $g_\dagger$'s *numerical* value would
matter (it does not, materially, anywhere below — see §4's caveat), it would inherit
T6/T14/T15's open three-candidate-length question, not a new one specific to this topic.*

This topic is speculative and unfinished — it checks whether the model's local
(solar-system-scale) gravity survives confrontation with PPN data (light bending, Shapiro
delay, gravitational redshift) and with planetary ephemerides. Four sessions feed this
topic, unchanged from cdot-4. The first pass assumed symmetry with Polarizable Vacuum (PV)
theory and concluded that alignment requires an explicit new local premise (a "Two-Regime
Dictionary": mass locally dressed as $m\propto K_\text{grav}^{3/2}$, distinct from its
cosmological invariance) forced by two data points. A second pass reconsidered the force
sector via the gravitoelectromagnetic (GEM) correspondence and exposed a serious,
independent crisis: the derived RAR closure (T14/T15), taken to the solar-system regime,
predicts an anomalous acceleration excluded by planetary ephemerides by ~3.5 orders of
magnitude. A third pass — prompted by the author's own correction that a flat, static
space with uniform constants was never the intended picture; the design intent was always
a local $c$-field, lower in wells, composing additively with the cosmological $c(t)$ —
found that the *flow* implementation (the sea's rest frame itself falling inward, the
Gullstrand–Painlevé "river" of GR) is *uniquely forced* once strict $m,G$ invariance is
required alongside the bending/redshift data: a three-channel pincer (index $A$, flow
$\xi$, dressing $\sigma$) has the unique solution $A=0,\xi=1$ under $\sigma=0$, with the
withdrawn Two-Regime Dictionary recovered as the *other* branch ($\xi=0\Rightarrow
A=2,\sigma=3/2$). This session supplied the uniqueness theorem but not a derivation of
the flow profile itself from connecton microphysics. A fourth pass attempted that
derivation via a full superfluid/quantum-hydrodynamics treatment (Madelung transform,
condensate order parameter); this document instead re-derives the same result,
$w=\sqrt{2GM/r}$, from plain energy conservation (a pressureless population free-falling
from rest at cosmological infinity) — recovering the third session's own lighter-weight
suggestion rather than the fourth session's heavier machinery, and avoiding a
manufactured circulation-quantization/frame-dragging tension that only the superfluid
reading produced (§2.2). **The Two-Regime Dictionary is superseded and withdrawn from
this topic; mass and $G$ remain strictly invariant, with no local exception.** The river
construction also gives the ephemeris tail crisis a derived target (an exact identity
linking the closure's exponent to a speed ratio, §4) in place of the two vaguer
"resolution paths" first recorded. Nothing here is adopted into Core Principles — the
uniqueness theorem itself depends on emergent local Lorentz invariance (§3), which is
not yet derived, and on the flow's functional form, which is not yet derived from
connecton microphysics (§2.2, §5).

---

## 1. The Question

The model departs from GR in two premises that matter locally: mass is invariant
(Core Principles premise 3; T8/T21), and $G$ is invariant (T8, adopted after the ×720
LLR refutation of $G\propto c^{-2}$) — both unchanged from cdot-4 to cdot-5. Does the
model still reproduce PPN $\gamma=\beta=1$ light bending, Shapiro delay, and
gravitational redshift at the precision solar-system tests require — using the same
invariant $m$, $G$ used everywhere else in the model, with no local exception?

## 2. The River: Local Gravity as a Coherent Inflow

### 2.1 Why a second component is needed

T14 already derives a Newtonian potential $\phi=-GM/r$ from connecton diffusion (a
local, fixed-epoch calculation, unaffected by the counting-law change): masses absorb
and re-emit connectons, and net emission sources a Poisson profile in the
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
introduces for the distance-law problem, just applied to two coexisting populations
instead of one. The diffusive fraction sources $\phi$; a **ballistic (long-mean-free-path,
free-streaming) fraction** carries the inflow. No new ontology is required.

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

**Ontology flag — resolved, category distinction.** This derivation treats the ballistic
fraction as ordinary matter with mechanical (kinetic) energy. T12 §"What Is a Connecton?"
argues a connecton is better read as a conserved unit of connection — a relation, not a
particle — with "no kinetic energy of its own." $w$ here is the velocity of the network's
*collective configuration*, not of an individual link, exactly as phonons or water waves
carry well-defined energy without their underlying constituents translating — T12's
statement is about links, this derivation is about the pattern. Separately, for a
non-dissipative (isentropic) population the ordinary first law reduces to
$d(w^2/2)=-d\phi$, i.e. $\tfrac12w^2+\phi=E$ *is* what non-dissipative thermodynamics
gives, not a rival assumption to it. See T14 Open Item 8.

**Newton recovered.** For steady radial flow, a comoving parcel's acceleration is the
convective derivative $w\,dw/dr = \tfrac12\,d(w^2)/dr = -GM/r^2$ — Newton's law, exactly,
as the material derivative of the flow. Free fall is comoving with the ballistic
component; there is one potential and one coupling, so no double-counting arises and the
equivalence principle is structural rather than assumed.

**A horizon, if light rides the same flow.** $w(r)=c$ at $r=2GM/c^2$ — the Schwarzschild
radius. The metric this flow defines,
$$ds^2 = -c^2dt^2 + (dr + w\,dt)^2 + r^2 d\Omega^2,$$
(the ingoing/physical patch, with $w>0$ the inward flow speed — the sign is opposite for
the outgoing, white-hole patch) is the Gullstrand–Painlevé form — a standard, exact
rewriting of the Schwarzschild solution in different coordinates (Painlevé 1921;
Gullstrand 1922; popularized as the "river model" by Hamilton & Lisle 2008), valid
outside any static spherical mass by Birkhoff's theorem, not just for black holes. Being
the same spacetime, it reproduces GR's light bending, Shapiro delay, gravitational
redshift, and perihelion precession exactly, automatically, with **no separate index law
and no local mass dictionary** — *provided* light is actually carried by this flow.

**The Flow-Coupling Premise, and why it is forced rather than assumed.** Whether light is
actually advected by $w(r)$ is not free-standing: it follows from requiring strict $m,G$
invariance together with the observed bending and redshift, via a uniqueness argument.
Generalize §2's setup with three possible local channels a mass could source in the sea:
an **index** channel $A$ ($K-1=A|\Phi|/c^2$, light index $n=K$ — §2's withdrawn route), a
**flow** channel $\xi$ (sea rest frame falls inward at $w$, $w^2=2\xi|\Phi|$; $\xi=1$ is
the escape-velocity normalization of §2), and a **dressing** channel $\sigma$
($m\propto K^\sigma$, §2's withdrawn route). Requiring emergent Lorentz invariance in the
local sea frame (§3, still itself a derivation target, not yet proven) so that SR time
dilation applies to a clock held static against the flow, and using that the flow field
with general $\xi$ is exactly the Gullstrand–Painlevé form of Schwarzschild with mass
$\xi M$ (so its bending contribution is $4\xi\,GM/bc^2$, matching §2's horizon-at-$w=c$
construction), the redshift and bending constraints become
$$\text{(R)}\ \ \xi+(2-\sigma)A=1, \qquad \text{(B)}\ \ \xi+\tfrac{A}{2}=1.$$
**Theorem:** imposing $\sigma=0$ (strict local mass invariance, already the model's
standing commitment — T8/T21) forces the *unique* solution
$$\boxed{A=0,\quad \xi=1}$$
— zero index coupling, pure flow at exactly the escape-velocity normalization used in
§2. The withdrawn Two-Regime Dictionary is recovered as the *other* branch: forbidding
flow ($\xi=0$, i.e. assuming a static sea) uniquely forces $(A,\sigma)=(2,3/2)$ instead.
The two sessions that produced §2's approach and the original PV dictionary are the two
branches of one system; requiring invariant mass selects the flow branch.

**Independent cross-check (no relativity needed).** A test body's acceleration from the
flow's material derivative is $\xi\,GM/r^2$ (§2.2). This must equal the ordinary
Newtonian acceleration already fixed by Cavendish/Kepler measurements with the model's
own invariant $G$ — no rescaling permitted — which forces $\xi=1$ directly, independent
of the bending/redshift pincer above. Two independent routes to the same $\xi=1$ is a
genuine consistency success.

**What this theorem does and does not establish.** It is a **constraint-satisfaction**
result: *given* that the flow takes the Gullstrand–Painlevé/Schwarzschild-$\xi M$
functional form, invariance plus data pick out $A=0,\xi=1$ uniquely. It does not, by
itself, derive that connecton dynamics *produces* exactly this functional form — that is
§4's entrainment/depletion calculation and T14 open item 5, unchanged. It also inherits
the emergent-Lorentz-invariance dependency from §3: the redshift constraint (R) used SR
dilation of a clock moving through the sea, which presupposes the very premise §3 flags
as an unproven derivation target. So the chain is: (invariant $m,G$, already adopted) +
(emergent local Lorentz invariance, **not yet derived**) + (GP functional-form ansatz,
**not yet derived from microphysics**) $\Rightarrow$ $A=0,\xi=1$ uniquely, matching all
solar-system data. This is tighter and more economical than the withdrawn Two-Regime
Dictionary, but two explicit debts remain before "exact Schwarzschild phenomenology" is
established rather than uniquely selected among consistent options.

**Structural bonus, conditional on the same debts: frame dragging.** Because GP($\xi M$)
is exactly Schwarzschild, its rotating generalization (the Doran/river form of Kerr) is
exactly Kerr — so if the flow-functional-form ansatz holds for a spinning mass, frame
dragging with the correct GR spin-2 normalization (the factor 4 flagged in §3 as a
two-sided test) comes structurally, not as a separate derivation. This would answer §3's
Lense–Thirring item outright, *conditional on* the same open microphysical derivation of
$w(r)$ from connecton dynamics — a scope gain to bank once that derivation exists, not a
result to claim yet.

**Mass stays invariant, full stop.** Because no local dressing is needed, the T8 fork
between invariant mass (cosmology) and PV mass (the withdrawn local dictionary) is
resolved by elimination rather than regime-splitting: mass is invariant everywhere,
matching every other topic in the model. No edit to T8 or Core premise 3 is required.

### 2.3 Where the river ends

Stationarity requires the local infall acceleration $GM/r^2$ to exceed the sea's own
global rate of change, $\dot c\sim3g_\dagger$ (T14 kinematics, a present-value relation
using today's $H_0^\text{hor}$, unaffected by the counting-law change — see T15's own
confirmation of this pattern). Equating them,
$$r = \sqrt{GM/3g_\dagger} = r_t/\sqrt3,$$
gives the MOND transition radius directly from the flow picture, with no new parameter —
unchanged from, and independent of, the superfluid-vs-ballistic framing question above,
and unaffected by the counting-law change since $g_\dagger$ enters here purely as
today's external parameter, exactly as in T14/T15.

## 3. GEM as the Force-Sector Frame

The river fixes *why* $\phi_g\propto M/r$ produces the right kinematics for a test
population, and now for light. It says nothing about whether the model's real preferred
frame (the static sea; the solar system moves through it at ~370 km/s,
$(v/c)^2\approx1.5\times10^{-6}$) produces a fatal preferred-frame signature, or how
frame dragging arises. The gravitoelectromagnetic (GEM) correspondence — the
$(g_{00},g_{0i})$ Maxwell-like sector of linearized GR, sourced by mass currents — fits
the connecton program natively: the sea already carries momentum currents with exact
conservation (T11, unchanged from cdot-4); the coherent-flow field $B_c$ used in T17/T19
is already a gravitomagnetic-type object; the river above supplies $\mathbf{E}_g$; and
collective modes propagate at $c$, giving $c_\text{gw}=c$ for free (closes the GW170817
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
data. The RAR closure derived in T14/T15 (confirmed unaffected by the counting-law
change in both documents),
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

**Note on $g_\dagger$'s value here.** This confrontation uses $g_\dagger\approx1.2\times
10^{-10}$ m/s² — the empirically fitted MOND value, the same number T14/T15/T17 use as
"today's external parameter." It does **not** depend on which of T6/T14's three
candidate cosmological lengths ($L$, $R_\text{now}$, $D_p(\infty)$) turns out to set
$g_\dagger$ from first principles — that question, still open, affects the *derivation*
of $g_\dagger$'s value, not its use here as a fitted input. This confrontation is
therefore fully unaffected by the counting-law change and by T6/T14's still-open
three-candidate-length question.

**The river gives the fix a derived target.** Define the cosmological Bernoulli speed
$v_c(r)=\sqrt{2g_\dagger r}$ — the speed the sea's global floor acceleration would build
over scale $r$. Then, identically,
$$\frac{w(r)}{v_c(r)} = \sqrt{\frac{g_\text{bar}}{g_\dagger}},$$
which is exactly the exponent of the MLS/RAR exponential function. This is an exact
algebraic identity (independent of the ballistic-vs-superfluid framing question in §2 —
it only uses $w=\sqrt{2GM/r}$ and $g_\dagger$ as an external parameter), not a
conjecture.

**A bridge to T14's own marginally-bound population.** T14's transition radius
$r_t=\sqrt{GM/g_\dagger}$ is where its dynamical-selection mechanism concentrates the
surviving, marginally-bound population, giving $v_f^4=GM g_\dagger$ (T14 §"Toward the
RAR"). Evaluating the river's escape speed there gives the exact identity
$w(r_t)=\sqrt2\,v_f$ — the two populations coincide in speed, up to a fixed factor, at
exactly the radius T14 already singles out independently. This raises the entrainment
calculation from a standalone conjecture to a plausible restatement of T14's own binding
open item (attractor convergence, T14 Open Item 2): the "fraction not entrained in the
coherent river" and the "surviving marginally-bound population" may be one object.
Suggestive, not yet proven — see T14 §"Toward the RAR" for the identity and its caveat.

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

1. **[Top priority] Derive $w(r)=\sqrt{2GM/r}$ (equivalently, the entrainment/depletion
   law) from connecton microphysics, §2.2 and §4.** One derivation would (a) establish
   the Flow-Coupling Premise's functional-form ansatz, completing the uniqueness theorem
   into an actual derivation; (b) shift the RAR closure from simple to the
   empirically-preferred MLS exponential; (c) dissolve the ephemeris exclusion
   identically. T14's own attractor-convergence open item (marginally-bound population
   at $r_t$) may be the same calculation — see the bridge identity $w(r_t)=\sqrt2\,v_f$,
   §4 and T14 §"Toward the RAR." This is now the single most consequential calculation
   in the program, merging what were three previously-separate open items.
2. **Emergent local Lorentz invariance (§3).** Load-bearing in three places at once:
   $\alpha_1=\alpha_2=0$; the redshift mechanism itself (§2.2's SR-dilation argument);
   and the exactness of the river-equals-GR correspondence. A transport-level derivation
   is now the single most important underived assumption in the local sector.
3. **Two-population coexistence — open, with quantified candidates (T14 Open Item 6).**
   The river needs a non-scattering ("ballistic") fraction of the sea coexisting with
   the scattering ("diffusive") fraction T14 says fills all of space. Two candidates now
   quantified (endpoint-only interaction; illustrative Rayleigh-type cross-section) —
   see T14 §"One Sea, Two Descriptions." Neither yet derived from an explicit
   re-anchoring rate equation.
4. **Momentum/inertia consistency of the river — RESOLVED (T14 Open Item 7).** The
   restored ram-pressure budget ($2\pi\rho_\text{bg}R_b^2r/m\sim10^{-26}$ of gravity for
   any bound body) shows comoving with the flow is necessarily geometric, not a
   disguised momentum-transfer push — see T14 §"The Inertia No-Go Result."
5. **De-double-counting — RESOLVED (T14 Open Item 9).** $(\mathbf w\cdot\nabla)\mathbf
   w=\nabla(w^2/2)=-\nabla\phi$ identically, given Bernoulli — the river's force and
   T14's diffusion force are the same $-\nabla\phi$ by construction, not two additive
   contributions; see T14's Open Items list.
6. **Amplitude normalization** (inherited from T14): $\delta n\to\phi$ must reproduce $G$
   at the correct magnitude from connecton microphysics. Unchanged by the river.
7. **Preferred-frame $\alpha_1,\alpha_2$ (§3).** Raw scale $(v/c)^2\approx1.5\times10^{-6}$
   sits an order of magnitude above the $\alpha_2$ bound ($<4\times10^{-7}$); the
   emergent-Lorentz-invariance argument (item 2) is a candidate zero, not a proof.
   **From cdot-4's deferred test battery (T23 Part III), not yet connected here**: the
   Secrest et al. quasar-number-count dipole ($\sim4$–$5\sigma$ excess over the
   kinematic expectation from the solar system's motion) is an independent,
   observational probe of the *same* preferred-frame question — a genuine excess would
   need a source, and this model's ontological preferred frame (the static connecton
   sea, item 2's emergent-Lorentz-invariance candidate notwithstanding) is a natural
   place to look, in principle a place this model could *outperform* $\Lambda$CDM rather
   than merely match it. Not evaluated — no quantitative link between the sea's
   properties and a predicted quasar-dipole amplitude has been worked out.
8. **Quadrupole radiation coefficient (§3)** — well-posed, uncalculated. (Lense–Thirring
   normalization is now a structural consequence of item 1, §2.2 "Structural bonus.")

**Cross-references.** T14 §"One Sea, Two Descriptions" states explicitly that the
global cosmological $c(t)$ and this topic's local flow $w(r)$ are two regimes of one
connecton density/velocity field, not two mechanisms — see there for the single-field
statement and its own consistency flags (items 3–5 above are T14 Open Items 6, 7, and 9
respectively, cross-posted; T14 Open Item 8, the connecton-ontology reconciliation, is
resolved per T12 and noted in §2.2 above). T14 open item 5 points here for the
flow-profile derivation. T8 §"Why Mass is Invariant" — no edit needed; mass remains
invariant everywhere, the local dressing this topic once proposed is withdrawn (§2).
T17/T19 — the two-gravitomagnetic-regimes requirement (§3) is a consistency constraint
on $B_c$, not yet built into either topic. T15 — once the entrainment law (item 1) is
resolved one way or the other, the RAR comparison should be re-run with the MLS form
alongside simple; the transition-region difference (≤4.5%) is close to current data
resolution. T6/T14 — the three-candidate-length question for $g_\dagger$'s *origin* is
explicitly independent of everything in this document (§4's note). Core Principles — no
premise addition proposed; premises 2 and 4 could eventually be sharpened to state the
single-field picture and "stationary, not static" frequency conservation explicitly, but
that edit is deferred, not made here.
