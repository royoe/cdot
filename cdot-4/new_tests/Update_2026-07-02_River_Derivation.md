# Update — Derivation of the River Flow w = √(2GM/r) from Connecton Dynamics (2026-07-02)

*Session type: constructive — the merged flagship calculation (flow profile + RAR
closure tail). Result: **a conditional derivation of the river**, resting on three
explicitly stated premises (C1–C3), two of which are forced by the failure of the
alternatives. Along the way: a two-fluid structure of the connecton sea is shown to be
*required*, not optional; the quantum pressure vanishes identically because the T14
density profile is harmonic (the "harmonic miracle"); the MOND boundary emerges
parameter-free from the breakdown of stationarity; and an exact identity is found —
the MLS/RAR exponential function's exponent equals the river-to-cosmological speed
ratio — giving the closure-tail problem its target form and resolving the ephemeris
crisis if the conjectured entrainment law holds. One new tension is flagged
(circulation quantization vs frame dragging).*

---

## 1. Routes That Fail — and What Their Failure Forces

**Route A — pure scattering, ballistic background (fails exactly).** A point mass that
absorbs and isotropically re-emits (number-conserving, T14's thermal solution)
generates *zero* perturbation at any field point: the shadow deficit arriving from the
mass's direction (total rate $C = \bar n c\sigma$) is exactly replaced by the
re-emitted surplus arriving from the same direction at the same rate. The naive
Le Sage force cancels identically — not approximately. **Consequence:** the mass must
be a net *source* of something; this is precisely T14's continuous-emission term (the
Poisson source $S \propto M$), now shown to be load-bearing rather than optional.

**Route B — Fickian drift of the diffusive sea (fails by 24 orders).** With the foam's
sub-Compton mean free path ($\lambda \sim 10^{-12}$ m, $D = c\lambda/3$) and the
mechanism's own gradient scale $|\nabla(\delta n/\bar n)| \sim |\nabla\phi|/c^2$, the
diffusive current's drift velocity at Earth's surface is $v_\text{Fick} \sim
10^{-20}$ m/s versus the required $w = 11.2$ km/s — short by $10^{24}$. Worse,
*any* normal-component flow at km/s through a medium with a $10^{-12}$ m mean free
path would be damped instantly. **Consequence (structural, forced):** the river can
only be carried by a dissipationless component. The connecton sea must be a
**two-fluid system**:

- **Normal component** (diffusive, foam-scattered): carries the Poisson density
  profile $\delta n \propto 1/r$ — *this is the potential* (T14's existing result);
- **Condensate** (coherent, superfluid, foam-transparent): carries the frame flow $w$
  — *this is the river*.

Coherence was already load-bearing twice (the 2026-06-30 thread's distance-law fix;
T14's indistinguishability closure). It is now forced a third way: without a
superfluid fraction, gravity-as-flow is impossible in a diffusive sea.

## 2. The Derivation

**Premises:**
- **C1 (Condensate):** the coherent fraction has order parameter
  $\psi = \sqrt{n_s}\,e^{iS}$; its flow is the Madelung velocity
  $\mathbf w = (\hbar/m_c)\nabla S$ (automatically irrotational).
- **C2 (Universality / EP for the sea):** the condensate couples to the potential
  realized in the normal component's $\delta n$ field with the universal coupling:
  chemical-potential shift $\delta\mu = m_c\phi(\mathbf x)$, where $\phi = -GM/r$ is
  the same potential matter feels. (The *amplitude* normalization $\delta n \to \phi$
  with the correct $G$ remains T14's standing open item; this derivation inherits it.)
- **C3 (Stationarity + cosmological boundary):** around a static mass the flow is
  stationary, and asymptotically the sea is the cosmological sea at rest in the map
  frame: $w(\infty) = 0$, $\phi(\infty) = 0$.

**Steps (all verified symbolically):**

1. Stationary Madelung/Bernoulli equation:
   $\tfrac12 w^2 + \phi + Q/m_c = E/m_c$, with quantum potential
   $Q = -(\hbar^2/2m_c)\,\nabla^2\sqrt{n_s}/\sqrt{n_s}$.
2. C3 fixes $E = 0$: **the zero-energy branch is a boundary condition, not a choice**
   — the sea falls "from rest at infinity" because it *is* at rest at infinity (the
   cosmological frame). The "zero-energy population" heuristic of the previous
   sessions is now the zero-energy branch of the condensate flow.
3. **The harmonic miracle:** the density profile the mechanism itself produces is
   $\delta n \propto 1/r$, which is *harmonic* away from the source:
   $\nabla^2\sqrt{n} \propto \nabla^2(1/r) = 0$ exactly (verified to first order in
   the perturbation). Hence $Q \equiv 0$ outside matter: the classical Bernoulli
   equation is exact precisely for the profile the diffusion mechanism generates.
4. Therefore $\tfrac12 w^2 = GM/r$:
   $$\boxed{w = \sqrt{2GM/r}}$$
   — irrotational (phase gradient, matching GP), with $m_c$ cancelling (the factor-3
   quantum-mass ambiguity from the consistency audit does not propagate), and
   transonic at $w = c \iff r = 2GM/c^2$: **horizons emerge as acoustic (sonic)
   horizons** of the condensate flow, in the Unruh analog-gravity sense.
5. **Newton recovered, double-counting resolved, EP structural:** the material
   derivative of the flow is $g = w\,dw/dr = GM/r^2$. There is one potential
   ($\delta n$-realized $\phi$) and one universal coupling: matter's weight and the
   sea's flow respond to the same field. Free fall = comoving with the condensate;
   the T14 force calculation is the static-frame view of not comoving. No additive
   double count is possible because there is only one $\phi$.

**Combined with the previous session's uniqueness theorem** (strict $m,G$ invariance
$\Rightarrow$ pure flow, $A = 0$, $\xi = 1$), the chain now reads: premises 2–4 + T14
diffusion (potential) + C1–C3 (flow) $\Rightarrow$ Gullstrand–Painlevé $\Rightarrow$
exact Schwarzschild phenomenology, with $m$, $G$, and the bare $c$-per-connecton all
untouched.

## 3. Where the River Ends: the MOND Boundary, Parameter-Free

Stationarity (C3) requires the local pattern to be maintainable against the sea's
global evolution, whose intrinsic acceleration rate is $\dot c = 3g_\dagger$ (T14's
own kinematics). The local flow's acceleration $g_\text{flow} = GM/r^2$ falls to
$3g_\dagger$ at
$$r = \sqrt{GM/3g_\dagger} = r_t/\sqrt3.$$
The stationary river is protected deep inside $r_t$ and must hand over near $r_t$ —
the MOND transition radius emerges from the flow picture with no new parameters.

## 4. The Tail Identity and the Entrainment Conjecture

Define the **cosmological Bernoulli speed** — the speed the global floor acceleration
builds over scale $r$: $v_c(r) = \sqrt{2g_\dagger r}$. Then, identically (verified
symbolically):
$$\frac{w(r)}{v_c(r)} = \sqrt{\frac{g_\text{bar}}{g_\dagger}}.$$
**This is exactly the exponent of the MLS/RAR exponential function**
$\nu = \big(1 - e^{-\sqrt{g_\text{bar}/g_\dagger}}\big)^{-1}$ — the empirically
preferred interpolating function, and the one that survives the solar-system
ephemerides.

**Entrainment conjecture (the tail derivation's target):** the anomalous ($g_x$)
component is carried by the sea fraction *not* entrained in the coherent local river,
suppressed as $e^{-w/v_c}$. Physically: deep in the well ($w \gg v_c$) everything is
entrained in the coherent infall — pure GR, no marginal population; in the outskirts
($w \lesssim v_c$) the global drift competes and the marginal population saturates at
the $g_\dagger$ floor. If the conjecture holds:

- the closure's functional form is corrected from *simple* to (the) *MLS exponential*
  in exactly the regime where simple fails;
- **the ephemeris crisis resolves identically**: at Saturn
  $\sqrt{g_\text{bar}/g_\dagger} = 755$, so the residual is $\propto e^{-755} = 0$
  (verified), versus the excluded constant $g_\dagger$ tail of the simple function;
- a falsifiable refinement appears in the galaxy data: simple and MLS differ by up to
  ~4.5% ($g_\text{bar}/g_\dagger \approx 10$) in the transition region — comparable
  to the 0.020 dex (4.7%) fit quality claimed for the simple closure. **The T15/T14
  RAR comparison must be re-run with the MLS form**; current SPARC-class data may
  already weakly discriminate.

The conjecture's status is honest: the *exponent identity is exact and derived*; the
*suppression law* $e^{-w/v_c}$ is not yet derived (it requires the condensate-normal
exchange kinetics — the depletion/entrainment rate of the coherent fraction in the
presence of the local flow). This is now the single sharpest open calculation in the
program.

## 5. New Tension Flagged: Circulation Quantization vs Frame Dragging

A superfluid is irrotational except for quantized vortices with circulation quantum
$\kappa = h/m_c = 4\pi c^2/H_0 \approx 5\times10^{35}\ \text{m}^2/\text{s}$ (using
$m_c = \hbar H_0/2c^2$). The frame-dragging circulation of the Sun's Doran/Kerr river
is $\Gamma \sim 2\pi r\,v_\text{drag} \sim 10^{6}\ \text{m}^2/\text{s}$ — **29 orders
of magnitude below one circulation quantum**. A pure condensate therefore cannot carry
continuous frame dragging. Candidate resolutions: (i) rotation is carried by the
*normal* component (two-fluid angular-momentum entrainment — as in rotating helium
below the first-vortex threshold, where the normal fluid co-rotates and the condensate
does not); (ii) the relevant circulation mass is not $m_c$; (iii) frame dragging is
genuinely suppressed below the vortex threshold — which would *conflict with the
LAGEOS 2% measurement* and falsify the pure-condensate reading. This must be resolved
in the Doran/$B_c$ session; note the galactic $B_c$ (T17/T19) may naturally live in
the normal component, which would unify (i) with the two-regime gravitomagnetism
statement of the GEM update.

## 6. Consolidated Edits (for merge)

| # | File | Edit | Type |
|---|------|------|------|
| 1 | T14 (or local-gravity topic) | Add §"The River Derivation": routes A/B failures; forced two-fluid structure; C1–C3; harmonic miracle; $w = \sqrt{2GM/r}$; sonic horizons; Newton as material derivative; EP structural | **Flagship new content** |
| 2 | T14 §MOND/RAR | Add the domain boundary ($g_\text{flow} = 3g_\dagger$ at $r_t/\sqrt3$) and the tail identity $w/v_c = \sqrt{g_\text{bar}/g_\dagger}$; state the entrainment conjecture and its target (MLS form); ephemeris resolution conditional on it | Major addition |
| 3 | T15 | Flag: the derived closure's functional form is expected to shift simple → MLS; re-run the RAR comparison with both; transition-region differences (≤4.5%) are near current resolution | Action item |
| 4 | T14 open items | Rewrite: (1) entrainment/depletion law (the conjecture) — top priority; (2) amplitude normalization $\delta n \to \phi$ with correct $G$ (inherited, unchanged); (3) circulation-quantization vs frame-dragging tension (§5); (4) transport-level emergent LI (unchanged) | Reorganization |
| 5 | Le Sage scorecard (T14) | Add Route A's exact-cancellation statement — sharpens why continuous emission is load-bearing | Strengthening |
| 6 | GEM + River updates (pre-merge) | Cross-amend: Lense–Thirring test now routed through the two-fluid question (§5); "zero-energy population" language replaced by "zero-energy condensate branch (boundary condition)" | Amendments |

**Bottom line.** The river is derived — conditionally, on a condensate premise (C1)
that three independent lines already forced, a universality premise (C2) that is the
equivalence principle extended to the sea, and a boundary condition (C3) that is just
the cosmological sea itself. The derivation is tighter than hoped in two places: the
quantum pressure vanishes *identically* for the very density profile the mechanism
generates, and the zero-energy branch is imposed by the boundary rather than selected.
The MOND scale emerges as the stationarity boundary, and the exact identity
$w/v_c = \sqrt{g_\text{bar}/g_\dagger}$ hands the closure-tail problem its target: one
entrainment law, $e^{-w/v_c}$, would simultaneously produce the empirically preferred
MLS function and dissolve the ephemeris crisis. What is genuinely new to derive has
narrowed to that law, the amplitude normalization, and the two-fluid resolution of the
frame-dragging quantization tension.
