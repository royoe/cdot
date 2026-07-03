# Update — Reinstating the Local c-Field Without Breaking m and G Invariance: the Flow (River) Implementation (2026-07-02)

*Session type: constructive. Prompted by the author's correction of a statement in the
GEM update ("a flat, static space with spatially uniform constants has no gravitational
redshift at all"): the design intent — documented in the 2026-06-30 development thread
and surviving vestigially in T14 (open item 5's "K-gradient background"; the Le Sage
scorecard) — was always that c varies locally, lower in gravitational wells where
connectons are shadowed, with the cosmological c(t) composing on top. Question: can the
local c-field for light be reintroduced without breaking m and G invariance?*

***Answer: yes — and uniquely.** Strict local m,G invariance plus the observed
bending/redshift phenomenology force the local c-effect to be implemented as a **flow**
of the sea (the Gullstrand–Painlevé "river" of GR) with exactly zero density–index
coupling. This supersedes the previous session's "forced σ=3/2 mass dressing"
conclusion, withdraws the Two-Regime Dictionary premise, and simplifies the model. The
cost is a specific, well-posed microphysical debt: derive the escape-velocity frame-flow
profile from connecton dynamics.*

---

## 0. The Correction and the Recovered Intent

The disputed statement was true under its assumptions but smuggled in a **third,
unstated assumption**: flat map + uniform constants + *sea locally at rest*. The
author's shadowing picture breaks exactly the third. A stationary configuration still
conserves photon frequency in flight (that half of the argument stands — frequency
conservation follows from time-translation invariance, not from the medium being at
rest), so gravitational redshift must still be an *emitter* effect. But an emitter
effect has **two** possible channels, not one: the local constants (index/dressing —
the only channel the PPN/PV session considered) *and the emitter's velocity relative to
the local sea rest frame*. The 2026-06-30 thread (recovered via conversation search)
shows the local c-field was the original gravity mechanism ("gravity = gradient in the
c-field," anchored to PV's K); it never made it into the premises, and only T14's
Le Sage scorecard and open item 5 preserve it. This update restores it — in a corrected
form.

## 1. The Three-Channel Pincer and a Uniqueness Theorem

Let a mass source three possible local structures in the sea:

- **Index channel** $A$: density–speed coupling, $K - 1 = A\,|\Phi|/c^2$, light index
  $n = K$ (the author's stated intuition: shadowed density → lower $c$);
- **Flow channel** $\xi$: the sea's local rest frame falls inward at $w$, with
  $w^2 = 2\xi|\Phi|$ (river normalization; $\xi = 1$ is escape velocity / zero-energy
  infall);
- **Dressing channel** $\sigma$: local mass response $m \propto K^\sigma$.

Clock rates (given emergent Lorentz invariance in the local sea frame — the premise
already proposed in the GEM update for $\alpha_2$): SR dilation × constants response,
slowdown $= [\xi + (2-\sigma)A]\,|\Phi|/c^2$. Light: the index contributes deflection
$2A\,GM/bc^2$; the flow field with general $\xi$ is *exactly* the Gullstrand–Painlevé
form of Schwarzschild with mass $\xi M$ (verified below), contributing $4\xi\,GM/bc^2$.
The observational constraints:

$$\text{(R) redshift:}\quad \xi + (2-\sigma)A = 1 \qquad
\text{(B) bending:}\quad \xi + \tfrac{A}{2} = 1$$

**Theorem (verified symbolically):** imposing strict local invariance $\sigma = 0$ —
the author's requirement — the system has the *unique* solution
$$\boxed{A = 0,\qquad \xi = 1.}$$
The index channel must vanish identically, and the flow must sit at exactly the
escape-velocity (zero-energy) normalization. Conversely, forbidding the flow
($\xi = 0$, the static-sea assumption of the PPN/PV session) uniquely forces
$(A, \sigma) = (2, 3/2)$ — the PV dressing branch. The two sessions' answers are the
two branches of one system; the author's clarification selects the branch that
preserves the premises.

Independent cross-checks: (i) Kepler/Cavendish separately force $\xi = 1$ (test-body
acceleration in GP($\xi M$) is $\xi GM/r^2$ with the bare, invariant $G$); (ii) the
flow branch has $\gamma = 1$ *structurally* — GP($\xi$) ≡ Schwarzschild($\xi M$), so the
bending-to-redshift ratio is automatic at any $\xi$, unlike the index branch where it
had to be engineered.

## 2. What the Flow Implementation Is

The Gullstrand–Painlevé (river) form of the Schwarzschild solution:
$$ds^2 = -c^2dt^2 + \big(dr + \sqrt{2GM/r}\,dt\big)^2 + r^2d\Omega^2.$$
Its constant-$t$ slices are **exactly flat** — the model's flat static map, unchanged.
All of gravity is carried by a radially infalling frame field $w(r) = \sqrt{2GM/r}$,
with local physics being special relativity with respect to the flowing sea:

1. **Gravitational redshift** = SR time dilation of a held-static clock moving at $w$
   through the sea: $\sqrt{1 - w^2/c^2} = \sqrt{1 - 2GM/rc^2}$ — the exact
   Schwarzschild factor to all orders, with $m$ untouched (verified: $w$ at Earth's
   surface = 11.19 km/s = escape velocity; GREAT-tested redshift reproduced exactly).
2. **The author's intuition realized:** the *coordinate* speed of light in the map
   frame is $dr/dt = -w \pm c$ — outbound light genuinely travels slower in the well,
   and round trips are delayed (Shapiro, exact). The composition with cosmology is
   literally what was intended: $c(t) \mp w(\mathbf{x})$ — the cosmological variation
   and the local gravitational variation compose additively in velocity,
   multiplicatively in redshift factors. But the mechanism is **advection, not index**:
   the connectons' own propagation speed stays $c$; the shadow (sink) drives the
   *inflow*, and the inflow carries the light.
3. **m and G invariance: strictly preserved.** No dressing anywhere. $G$ remains the
   bare source coupling; $m_0$ is untouched locally and cosmologically. Premise 3
   stands in its strong form.
4. **Exactness and scope:** because GP is exactly Schwarzschild (and its rotating
   extension — the Doran/river form of Kerr — is exactly Kerr), the model inherits, to
   the extent the flow field equals GR's: all PPN parameters ($\gamma = \beta = 1$),
   perihelion precession, **frame dragging with the correct spin-2 factor natively**
   (answering the GEM session's Lense–Thirring question structurally — the "swirl" of
   the river around a rotating mass is Kerr's), horizons (surfaces where $w = c$: the
   sea flows inward faster than its own signal speed — natural for a medium), photon
   spheres, and EHT-compatible black-hole shadows. This is a decisive scope gain over
   the PV/index branch, whose horizonless exponential metric is under strong-field
   pressure.

## 3. Premise-Level Consequences

1. **Premise 2 sharpened (count, not density):** the theorem's $A = 0$ requires that
   local connecton *density* perturbations do **not** modulate $c$ at first order.
   This is consistent with — and now demanded by — T12's grounding: $c$ is the
   connectons' own propagation speed, not a density-dependent collective sound speed.
   Premise 2 should read: *$c$ is set by the global count within the horizon
   (relational anchor); local density perturbations move the sea's rest frame and carry
   momentum flux, but do not change $c$.* The cosmological $c \propto N$ and the local
   $A = 0$ are thereby reconciled: one is the global anchor, the other a local
   redistribution.
2. **Premise 4 amended (stationary, not static):** frequency conservation in flight
   holds for any *stationary* sea configuration, including steady flows. Wording
   change only.
3. **The Two-Regime Dictionary premise (PPN/PV update) is WITHDRAWN.** With the flow
   channel admitted, no local dictionary exists at all: local physics is SR in the
   flowing sea; only the global count sets scales. The "why does matter respond
   differently to spatial vs temporal K" seam question dissolves — there is no spatial
   K. The PPN/PV update's §3–§5 must be amended before merge: its pincer stands as the
   $\xi = 0$ branch, its conclusion superseded by this session's theorem. The $P=1/2$
   "both branches" reframing is likewise retired (elegant, but no longer needed).
4. **Emergent Lorentz invariance is promoted to a load-bearing premise doing triple
   duty:** (i) $\alpha_1 = \alpha_2 = 0$ (GEM update); (ii) the gravitational-redshift
   mechanism itself (SR dilation vs the sea); (iii) the exactness of the river ≡ GR
   correspondence. It is now the single most important underived assumption in the
   local sector and must be scheduled for a transport-level derivation.

## 4. Microphysical Debts (well-posed, in priority order)

1. **Derive the frame-flow profile $w = \sqrt{2GM/r}$.** Naive estimates fail
   instructively: the Le Sage shadow-drift anisotropy gives $w \sim |\Phi|/c$
   (verified: 0.21 m/s at Earth's surface vs the required 11.2 km/s — short by
   $5\times10^4$, and second-order in $\Phi$ for the redshift); material continuity for
   a steady sink gives $w \propto r^{-2}$, the wrong profile. The river is therefore a
   **frame/pattern flow** (the locus of local flux isotropy), not conserved material
   transport — the same point Hamilton & Lisle make about GR's river not being a
   conserved fluid. **In-house candidate:** the sea's local rest frame is defined by
   its **zero-energy (marginally-bound) population**, which falls from rest at infinity
   at exactly $w = \sqrt{2GM/r}$ (Bernoulli $\tfrac12 w^2 = GM/r$) — the *same*
   population T14's RAR mechanism privileges at $r_t$. Suggestive identity (exact):
   $w(r_t) = \sqrt{2}\,v_\text{flat}$ — the zero-energy river meets the flat-curve
   velocity scale precisely at the transition radius, hinting that the river
   (Newtonian/GR interior) and the RAR tail (exterior) are two regimes of one
   population. This is now the same calculation as the closure-tail rederivation from
   the GEM session (Boltzmann-weighted marginal population) — **the two most important
   open problems in the program have merged into one.**
2. **Re-read the T14 diffusion force as the river's action (de-double-count).** The
   momentum-flux anisotropy computed in T14 for a *held-static* body must be shown to
   be the static-frame view of the flow (the force needed to not comove), with
   free-falling bodies seeing isotropic flux (frame of local isotropy = free-fall
   frame). This upgrade would make the equivalence principle *structural*: free fall
   = comoving with the sea. If instead the diffusion force is additive to the flow,
   Newton is double-counted — a consistency requirement, not an optional refinement.
3. **Transport-level emergent Lorentz invariance** (see §3.4).
4. **Doran/Kerr connection for $B_c$:** identify the galactic coherent-flow $B_c$
   (T17/T19) and the river's swirl field as the same object in two regimes, governed
   by the same transition machinery as debt 1.

## 5. Consolidated Edits (for merge)

| # | File | Edit | Type |
|---|------|------|------|
| 1 | Core Principles | Sharpen premise 2 (global count, not local density; $A=0$); amend premise 4 (stationary); note premise 3 stands in strong form locally | Premise edits |
| 2 | Core Principles / T14 | Add the flow implementation: local gravity = GP/river frame field of the sea; uniqueness theorem (σ=0 ⇒ A=0, ξ=1); emergent-LI premise promoted (triple duty) | **New core content** |
| 3 | PPN/PV update (pre-merge amendment) | §3–5: pincer re-labeled as the ξ=0 branch; Two-Regime Dictionary premise withdrawn; P=1/2 reframing retired; conclusion superseded | Supersession |
| 4 | GEM update (pre-merge amendment) | Lense–Thirring question upgraded: correct factor structural via Doran, pending flow derivation; α₂/LI premise now shared with redshift mechanism | Amendment |
| 5 | T14 | Le Sage scorecard: add the flow reading (sink drives frame inflow); open item 5 rewritten: derive $w = \sqrt{2GM/r}$ (zero-energy population candidate); merged with the closure-tail rederivation task; de-double-counting requirement (§4.2) | Reorganization |
| 6 | T12 | Note: $c$ = connecton propagation speed, density-independent, is now *required* ($A=0$), not merely natural | Strengthening |
| 7 | Test Battery (T22 proposal) | Solar-system rows updated: γ, β, redshift, frame dragging, strong field all inherited exactly *conditional on the flow derivation*; EHT added as a passed-by-construction row under the same condition | Update |

**Bottom line.** The author's correction was right, and following it through yields the
cleanest result of the day: the local c-field returns — as intended, lower effective
light speed in wells, composing with the cosmological c(t) — but implemented as a flow
of the sea rather than an index, and this implementation is *uniquely forced* by
strict m,G invariance plus bending and redshift data. The model's local gravity is now
Gullstrand–Painlevé's river with a connecton substrate: flat slices matching the static
map, exact GR phenomenology including frame dragging and horizons, no dictionaries, no
dressing, two fewer premises than yesterday — and one sharply-posed debt, the
escape-velocity frame-flow profile, which has merged with the RAR closure-tail problem
into a single calculation about the sea's zero-energy population.
