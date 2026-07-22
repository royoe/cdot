# Session Log — cdot-8/WP7 (2026-07-20)

*Continued from `SessionLog-2026-07-19.md` (Entries 8–26). Same split
rationale as that file's own header — one log per calendar day. Entry
numbering continues unbroken from Entry 26.*

---

## Entry 27 (worker) — Secondary advisor confirms §28's $F_{QQ}$ correction; one propagation detail fixed before use (2026-07-20)

**Prompt (verbatim):**
> Please check advice from the assistant advisor in WP7/advisory.
> Consider this carefully as the new advisor (Opus 4.8) does not have
> the full context that the main advisor (Fable 5) has.

**Summary of work performed:**

1. **Located and read** `Advisory-WP7-FQQCorrectionConfirmed-2026-07-20.md`
   + `wp7_fqq_correction_crosscheck.py`, from the secondary advisor
   (routed here while the primary advisor is unavailable). **Reproduced
   the script myself before accepting anything** — all four checks ran
   exactly as reported.

2. **Accepted the core confirmation outright**: the secondary advisor
   independently re-derived the $s\leftrightarrow z$ convention, the
   $F(\mathcal Q)$ quadrature, and the analytic $F_{QQ}$ formula from
   `Foundation.md` directly (not copied from either prior script) —
   $F_{QQ}(0)\approx-0.169$ is now confirmed by three independent
   implementations, not two.

3. **Caught one propagation error, exactly the kind a secondary advisor
   without full session context would be prone to**: Check 4's
   condensate-mass recomputation used `meff_skeleton.py`'s simplified
   formula (implicitly fixing $\mathcal K_B=1$), not the $\mathcal K_B$-
   range scan (`meff_exact_dictionary.py`) that actually produced WP5's
   quoted $5$–$10$ Gpc band — confirmed by checking that Check 4's own
   "old" figure exactly reproduces the $\mathcal K_B=1.0$ row alone.
   Recomputed properly across the full range: $\mu^{-1}\approx10$–$20$
   Gpc, $r_c\approx100$–$160$ Mpc (not the narrower single-point figures
   the advisory quoted).

4. **Propagated the confirmed, correctly-recomputed numbers**: into
   `Foundation.md` §7/§8, `Update-WP5-WeakFieldStructure-2026-07-17.md`
   (as a dated correction note, not a silent rewrite), `Progress.md`
   item 3a (closed), and `ErrataAndMethodologyLog` K14 (marked
   confirmed).

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§29, new), edits to `Foundation.md`, `Update-WP5-
WeakFieldStructure-2026-07-17.md`, `Progress.md`,
`ErrataAndMethodologyLog-2026-07-18.md`, this entry.

**Status: $F_{QQ}$ correction fully confirmed and propagated.** The
secondary advisor's core physics was right and independently verified;
one propagation detail was caught and fixed rather than passed through,
consistent with treating a less-contextualized advisor's output with
the same scrutiny as any other claim in this program. Nothing in
`cdot-7/` was touched.

---

## Entry 28 (worker) — Stage 2: the units contract, one genuine correction found before any code (2026-07-20)

**Prompt (verbatim):**
> Good! Continue with Stage 2.

**Summary of work performed:**

1. **Checked the time convention directly from primary source** rather
   than assume: the founding paper's dots are cosmic-time derivatives
   ($H\equiv\dot a/a$, confirmed), while both prior implementation
   attempts integrated in e-fold time $N=\ln a$ — every equation needs
   $\dot X=H\,dX/dN$ applied explicitly. Checked both prior scripts:
   neither had this written down as a standalone, checked item, though
   neither's specific failure traces to it alone.

2. **Found a genuine, previously-unexamined normalization error**: the
   $\mathcal E_\alpha$ equation's "$dK/dQ$" coefficient is *not* the
   same object as the bulk-current $F_Q$ already used correctly
   elsewhere (§20). Checked directly from primary source: the paper's
   own $K(\bar Q)\equiv-\tfrac12F(0,\bar Q)$ definition exists
   specifically to reconcile its toy model's $1/(8\pi\tilde G)$
   normalization with the real action's $1/(16\pi\tilde G)$ one — so
   "$dK/dQ$" in that specific equation means $-\tfrac12F_Q$, not $F_Q$.

3. **Cross-checked this distinction independently before trusting it**:
   WP5's own separately-established $\mathcal K_2=-\tfrac14F_{QQ}$
   relation is only consistent with $K=-\tfrac12F$ — an independent
   confirmation, not just self-consistent algebra. Both prior
   implementation attempts used bare $F_Q$ in this equation; this is a
   genuine bug, now caught before Stage 3 rather than discovered by a
   third failed run.

4. **Worked out the remaining contract lines** ($k$-normalization to
   the established $\kappa=(k/aH_0)^2$ convention; background-quantity
   identifications, all reused unchanged from already-validated §18/
   §23/§24 conventions).

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§30, new), this entry.

**Status: units contract written and cross-checked, one real error
caught before code — exactly Stage 2's purpose.** Recommending this be
checked against the advisor before Stage 3's implementation, per the
accepted staging discipline. Nothing in `cdot-7/` was touched.

---

## Entry 29 (worker) — Stage 2 confirmed directly against primary source; cleared for Stage 3 (2026-07-20)

**Prompt (verbatim):**
> Good. Check for advice.

**Summary of work performed:** Located and read
`Advisory-WP7-Stage2UnitsContractConfirmed-2026-07-20.md`. **Verified
every quoted claim myself directly against the archived primary source**
(`references/arXiv.2007.00082/newRMONDLett.tex`) rather than accept the
advisory's own quotes at face value: $\mathcal K(\bar Q)=-\tfrac12
\mathcal F(0,\bar Q)$, the $8\pi$-vs-$16\pi\tilde G$ prefactors, the
$\mathcal K_2$ expansion definition, and the $\mathcal E_\alpha$
equation's exact parenthesization all match the source exactly.
Contract Line 2 is now confirmed by direct textual match, the strongest
verification available — both prior implementation attempts used the
wrong coefficient. The secondary advisor also owned their own §29
Check-4 error outright, with nothing further needed on my side.

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§31, new), this entry.

**Status: Stage 2 fully cleared, by both a worker-side and a second,
independent primary-source check.** Ready to proceed to Stage 3 (the
pure field-variable rebuild). Nothing in `cdot-7/` was touched.

---

## Entry 30 (worker) — Stage 3 attempted: dust-sector regression improves on §24, but the full system hits a new, vector-sector instability (2026-07-20)

**Prompt (verbatim):**
> Go for state 3

**Summary of work performed:**

1. **Resolved a closure gap before coding**: showed $\chi=\mathcal Q(
   \theta+\alpha)$, recoverable from $\theta,\alpha$ alone — no $\gamma$
   needed, resolving ambiguity in K2's own "$\chi$ or $\gamma$" state
   list. Confirmed $(\delta_b,\theta_b,\delta_s,\theta_s,\alpha,\mathcal
   E_\alpha)$ is a complete 6-variable state, $\Phi$ algebraic via
   sub-horizon Poisson (matching §24's convention).

2. **Regression check against §24, run first**: with $\Pi=0$ (vector
   decoupled), $\Phi$ now decays smoothly to $0.50\times$ by $z=0$ —
   better than §24's own pathological growth to $2.4\times$, since $w(z)$'s
   real transition is kept rather than the "always dust" shortcut.

3. **Full system (real $\Pi$, using the confirmed $-\tfrac12F_Q$
   coefficient) blew up.** Tried a $10\times$ smaller $k$ to check
   whether it was a $\kappa$-scaling/conditioning issue — reduced the
   blowup's scale by orders of magnitude but did not fix it; values were
   already huge one step past $z=100$, a fast instability, not slow
   drift.

4. **Localized rather than patched further**: Stage 0's own stiffness
   audit only checked the scalar condensate sector ($\mu_\text{eff}$
   from $F_{QQ}$) — it never audited the vector/$\mathcal E_\alpha$
   sector's own dynamics, which is where this instability appears to
   live.

**Files produced:** `wp7_stage3_field_variable.py` (new, in
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md`
(§32, new), this entry.

**Status: genuine progress (dust-sector regression improves on §24; a
real closure-gap resolved) alongside a newly-localized, not-yet-fixed
instability in the vector sector.** Recommending a dedicated vector-
sector stiffness audit (mirroring Stage 0's own scalar-sector approach)
as the next, narrow, advisor-cross-checked step, rather than a further
solo patch. Nothing in `cdot-7/` was touched.

---

## Entry 31 (worker) — §32's instability diagnosed by the secondary advisor: real, localized, and independently reproduced; one open normalization item found to have a second constraint (2026-07-20)

**Prompt (verbatim):**
> Check for advice.

**Summary of work performed:**

1. Found `Advisory-WP7-Stage3VectorInstabilityDiagnosed-2026-07-20.md` +
   `wp7_stage3_vector_stiffness_audit.py` in `WP7/advisory/` — exactly
   the vector-sector audit recommended in Entry 30.

2. **Ran the companion script myself before accepting anything**: every
   claimed number reproduced exactly — the $z=100$ eigenvalues
   $\{-13.2,+485\}$, the $\kappa=0$ stable complex pair
   $-0.5\pm8.37i$, the critical-$\kappa(z)$ scan. Cross-checked the
   advisory's own analytic-trace formula against the coded Jacobian
   entry by hand: $3.72\times10^6$ (formula) vs $3.68\times10^6$
   (code), $\sim1\%$ agreement. Verified the Jacobian is a faithful
   linearization of `wp7_stage3_field_variable.py`'s actual `rhs()`
   term-by-term, not an independent reconstruction that happens to
   agree.

3. **Went to the primary source myself on the one open item** (the
   $\Pi$-formula's Fourier/Laplacian normalization, which the advisor
   explicitly flagged as unresolved): found that `newRMONDLett.tex`
   line 456's $\Pi$ definition and line 437's $\delta$ definition share
   the IDENTICAL $\nabla^2[\mathcal K_B\mathcal E_\alpha+(2-\mathcal
   K_B)\chi]$ bracket — a second, independent constraint on the same
   unknown convention, not previously noticed by either the advisor or
   me. The stated Newtonian-gauge metric convention ($g_{ij}=a^2(1-2
   \Phi)\gamma_{ij}$, comoving spatial coordinates) favors the
   "comoving-Laplacian" ($\nabla^2\to-k^2$, no extra $a$) reading over
   the "physical-Laplacian" one — a plausibility argument, not a full
   derivation, and doesn't yet explain the reported $O(1)$ discrepancy
   with the current code. Left open for Stage 3b, not force-resolved.

**Files updated**: `Update-WP7-PerturbationStructure-2026-07-18.md`
(§33, new), this entry.

**Status: diagnosis accepted, independently verified, not merely
rubber-stamped.** The instability is real and precisely characterized
(a genuine large positive real eigenvalue, switched on entirely by the
$\Pi$-feedback term above a tiny critical $\kappa$, confined to the
vector sector Stage 0 never audited). **Recommending Stage 3b**: a
narrowly-scoped units-contract addendum resolving the $\Pi$-formula's
Laplacian convention, using the new $\delta$-definition cross-check as
an extra constraint, before any further explicit-ODE attempt or a
quasi-static/slaved-closure redesign. Nothing in `cdot-7/` was touched.

---

## Entry 32 (worker) — Stage 3b: the $\Pi$-formula's Laplacian convention worked out; instability survives every reading, likely real physics, flagged for advisor cross-check (2026-07-20)

**Prompt (verbatim):**
> Proceed to 3b.

**Summary of work performed:**

1. Re-derived the $\Pi$-formula's Fourier convention directly from
   `newRMONDLett.tex` line 456, using the formula's own internal
   self-consistency (the explicit $a^2$ already multiplying $\bar\rho$
   in its prefactor argues against $\nabla^2$ *also* meaning the
   $1/a^2$-including "physical" Laplacian — that would double-count):
   concluded $\nabla^2\to-k^2$ (bare comoving $k$), giving $\Pi_{\rm
   vec}=+\frac{c_\text{ad}^2\kappa}{3\Omega_s(a)}[\ldots]$, matching this
   program's own already-validated Poisson-equation convention exactly.

2. **Found a genuine, separate bug along the way**: the coded $\Pi$
   term in `wp7_stage3_field_variable.py` uses bare $\kappa$ with no
   $\Omega_s(a)$ division at all — wrong under either Laplacian
   reading, not just the disputed one.

3. **Tested numerically whether this resolves the instability**: wrote
   `wp7_stage3b_pi_normalization_check.py` (new, saved to
   `cdot-8/WP7/`), ran all three candidate readings (current bare-code,
   derived "comoving," advisor's alternate "physical") through the
   vector Jacobian. **Result: the growing real eigenvalue survives
   under all three** — the derived reading roughly halves the
   eigenvalue's magnitude (e.g. $485\to221$ at $z=100$, $k=10^{-4}\,
   \text{Mpc}^{-1}$) but doesn't remove it; the alternate reading makes
   it much worse. The normalization choice shifts the threshold's scale
   by an $O(1)$–$O(10)$ factor, nowhere near the $10^2$–$10^6$ needed to
   erase it.

4. **Did not declare this settled on my own derivation alone**: given
   this exact class of normalization/conversion work has produced
   subtle errors repeatedly elsewhere in this program (the $F_{QQ}(0)$
   domain artifact, the bare-vs-$-\tfrac12F_Q$ coefficient, several
   WP3-era factor-of-few slips), flagged the "explicit-$a^2$-implies-
   comoving" argument specifically for advisor cross-check before
   treating the instability as confirmed-real physics.

**Files produced/updated**: `wp7_stage3b_pi_normalization_check.py`
(new, `cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md`
(§34, new), this entry.

**Status: genuine progress, not fully closed.** The separate coded
$1/(3\Omega_s(a))$ bug should be fixed regardless of the outcome below.
The instability itself is very likely real (survives every reading
tried), but this specific conclusion is offered with appropriate
humility pending advisor review, rather than treated as settled.
**Recommended next step**: request advisor cross-check of this
derivation; if confirmed, design a quasi-static/slaved closure for
$(\alpha,\mathcal E_\alpha)$ above $\kappa_\text{crit}(z)$ as Stage 4's
prerequisite, rather than a fourth explicit-ODE attempt. Nothing in
`cdot-7/` was touched.

---

## Entry 33 (worker) — Stage 3b advisory accepted; Stage 3c (quasi-static closure) attempted, a genuine coordinate singularity found at the fast/slow transition, checkpointed (2026-07-20)

**Prompt (verbatim):**
> Advisory added.

**Summary of work performed:**

1. Found and reviewed `Advisory-WP7-Stage3bConfirmed-2026-07-20.md` —
   independently reran my own `wp7_stage3b_pi_normalization_check.py`,
   reproduced every number, and added a second, independent argument
   (the standard Ma & Bertschinger-style cosmological-perturbation
   convention) supporting the comoving-Laplacian reading beyond my own
   internal no-double-counting logic. Confirmed the missing
   $1/(3\Omega_s(a))$ bug is real regardless. Confirmed the instability
   survives every reading, reading the partial ($\sim2\times$) shift as
   the expected signature of a real physical effect being corrected by
   a genuine but non-dominant unit fix. Recommended proceeding to the
   quasi-static closure. **Accepted** (§35).

2. **Attempted Stage 3c**: built `wp7_stage3c_quasistatic_closure.py`
   (new, `cdot-8/WP7/`), implementing both the corrected $\Pi$
   normalization and an algebraic elimination of $\mathcal E_\alpha$
   (solving $d\mathcal E_\alpha/dN=0$ in closed form, leaving $\alpha$
   as the only vector ODE state). Regression at $\kappa\to0$ passed
   cleanly ($\Phi\to0.59\times$ by $z=0$, matching §32's own full-$\Pi$
   result in order and shape).

3. **The main test ($k=10^{-4}\,\text{Mpc}^{-1}$, the case that blew up
   explicitly) failed** — the solver choked. Diagnosed rather than
   forced past: found the elimination's own denominator equals exactly
   $-K_BH_c\,\partial\dot{\mathcal E}_\alpha/\partial\mathcal E_\alpha$
   (the $(2,2)$ entry the secondary advisor's own stiffness audit
   already computed), and it crosses zero right at the
   $\kappa\approx\kappa_\text{crit}(z)$ transition — a genuine
   coordinate singularity in the adiabatic elimination, not a numerical
   artifact.

4. **A second test (applying the closure unconditionally at very small
   $k=10^{-6}\,\text{Mpc}^{-1}$, safely sub-critical everywhere) also
   failed physically** ($\delta_s$ sign-flips, $\alpha\to-74$ by
   $z=0$) — the expected result of applying adiabatic elimination
   outside its regime of validity (no fast/slow separation exists
   there).

**Files produced**: `wp7_stage3c_quasistatic_closure.py` (new,
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md` (§35,
§36, new), this entry.

**Status: genuine progress, checkpointed rather than patched.** The
quasi-static closure is sound in the regime it's designed for and its
failure modes are both understood, not mysterious — but it cannot be a
single global substitution; it needs regime-gating (explicit ODE below
$\kappa_\text{crit}(z)$, algebraic slaving safely above it) plus a
deliberate treatment of the transition zone where the elimination
denominator itself vanishes, structurally reminiscent of WP3's own
homogeneous-mode/kernel-constant difficulties. Recommending advisor
review of this transition-zone design before implementing a hard or
smoothed switch. Nothing in `cdot-7/` was touched.

---

## Entry 34 (worker) — Advisor corrects the transition-zone diagnosis (real stability boundary is lower than I thought); hybrid closure built to spec but exposes a deeper, WP3-shaped initial-condition problem (2026-07-20)

**Prompt (verbatim):**
> Check for response.

**Summary of work performed:**

1. Found `Advisory-WP7-Stage3cTransitionZoneReview-2026-07-20.md`.
   **Accepted a correction to my own §36 diagnosis**: I had named the
   discriminant's zero ($z\approx29$–$30$, real$\to$complex eigenvalue
   transition) as the switch point; the advisor showed the system is
   still unstable (growing complex spiral) all the way down to
   $z\approx18$–$20$ — the true boundary is $\text{Re}(\lambda_\text{
   max})=0$, i.e. $\text{tr}(J)=0$, a distinct, lower threshold.
   **Independently reconstructed the full tr/det/eigenvalue table
   myself** before accepting — matched the advisor's bracketing exactly
   ($\text{tr}=0$ between $z=19$ ($+0.078$) and $z=18.5$ ($-0.006$)).

2. **Built the hybrid closure exactly as recommended**:
   `wp7_stage3d_hybrid_closure.py` (new, `cdot-8/WP7/`) — hard switch at
   $\text{tr}(J)=0$ with a safety margin, quasi-static above, explicit
   ODE below. The switch redshift reproduces the advisor's bracket
   exactly ($z_\text{switch}=18.54$ at $k=10^{-4}\,\text{Mpc}^{-1}$).

3. **Ran the advisor's own recommended robustness check and it failed
   badly**: $\delta_b(z=0)$ spans $+0.14$ to $-1.8\times10^7$ across
   margins of $0.2$ to $0.02$ e-folds. **Diagnosed rather than reported
   as a bare failure**: traced it to the starting condition at $z=100$
   — $\chi=\bar{\mathcal Q}(\theta_s+\alpha)\approx21.7$ there (large,
   since $\bar{\mathcal Q}\approx2190$ even though $\theta_s$ is small),
   giving a slaved $\mathcal E_\alpha\approx-76.4$, wildly different from
   the true system's own IC ($\mathcal E_\alpha=0$). Since the eliminated
   mode is *growing* ($\text{Re}(\lambda)>0$) in this regime, this
   mismatch does not decay — it amplifies.

4. **Recognized the structural shape of the problem**: this is a
   boundary-condition SELECTION (like WP3's own past-regularity/$C_1$
   saga — pick the one non-runaway solution), not a dynamical relaxation
   (standard tight-coupling elimination works because the eliminated
   mode decays, forgetting mismatched initial data almost instantly —
   the opposite is true here).

**Files produced/updated**: `wp7_stage3d_hybrid_closure.py` (new,
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md` (§37,
new), this entry.

**Status: the switch criterion is confirmed and keeps; the closure
itself is not yet trustworthy.** The remaining problem is the
quasi-static phase's own initial/boundary condition, which likely needs
a consistency requirement (deep-past matching or a shooting method
enforcing boundedness) rather than inheriting the earlier explicit-ODE
convention unmodified. Checkpointed, not forced. Recommending this
specific point be routed to the advisor next, given how closely it
echoes WP3's own hardest historical difficulty. Nothing in `cdot-7/`
was touched.

---

## Entry 35 (worker) — Advisor endorses the diagnosis, adds an adiabaticity finding; my own check of their proposed fix surfaces a further, un-flagged complication (2026-07-20)

**Prompt (verbatim):**
> Check new advisory.

**Summary of work performed:**

1. Found `Advisory-WP7-Stage3dBoundaryConditionProblem-2026-07-20.md`.
   Endorses §37's boundary-condition/stable-manifold diagnosis in full.
   Adds: the quasi-static approximation's own adiabaticity
   ($|\lambda_\text{max}|\gg1$ per e-fold) is only good for
   $z\gtrsim50$–$60$, already marginal by $z\approx25$–$30$ — well above
   the switch itself, so fixing only the $z=100$ initial condition can't
   be the whole fix. **Independently reproduced their adiabaticity table
   exactly** before accepting it. Recommends a Riccati/stable-subspace
   continuation ($\mathcal E_\alpha=\mu(N)\alpha+\nu(N)$, $\mu,\nu$
   evolved by their own consistency equations, seeded at $z\gtrsim60$)
   as the standard fix for this class of problem. Also honestly flagged
   (not asserted): a possible second unstable direction in the full
   system, unconfirmed.

2. **Derived the Riccati equations myself rather than treating the
   recommendation as ready to implement**: got $\mu'=\partial\dot{
   \mathcal E}_\alpha/\partial\mathcal E_\alpha\cdot\mu+\partial\dot{
   \mathcal E}_\alpha/\partial\alpha-\mu^2/H_c$, with the naive
   frozen-coefficient slaving as its fixed point. **Checking the fixed
   point's own discriminant surfaced something the advisory didn't
   flag**: it is proportional to the original Jacobian's own
   discriminant and vanishes at the *same* $z\approx29$–$30$ point (not
   at the switch, $z\approx18.5$) — confirmed numerically. This means
   the real-valued slope $\mu$ stops existing as a real number a full
   ten-plus e-folds before the switch: once the eigenvalues turn
   complex, there is no single real stable eigendirection left to track
   — every real initial condition in that spiral zone grows at the same
   rate. **The proposed method, as a real-valued continuation, cannot
   be carried through the $z\approx18.5$–$29.5$ spiral zone at all.**

**Files updated**: `Update-WP7-PerturbationStructure-2026-07-18.md`
(§38, new), this entry.

**Status: the advisory's diagnosis and adiabaticity finding both
independently confirmed and accepted; the concrete method proposed
needs a genuine complex/matrix generalization before it can be
implemented — a new wrinkle neither party had surfaced before now.**
Checkpointed rather than attempting that derivation un-reviewed.
Recommending this specific point, and the advisor's own still-open
second-unstable-direction question, both be put to the advisor next.
Nothing in `cdot-7/` was touched.

---

## Entry 36 (worker) — Advisor resolves the spiral-zone question elegantly (one handoff, no complex generalization); implementing it surfaces a further numerical obstruction: the stable branch's forward-$N$ Riccati flow is itself repelling (2026-07-20)

**Prompt (verbatim):**
> Advice updated.

**Summary of work performed:**

1. Found `Advisory-WP7-Stage3eRiccatiSpiralResolution-2026-07-20.md`.
   Accepted the resolution: in the spiral zone every real direction
   shares the same growth envelope, so there's nothing to select there
   at all — track the real Riccati slope only where it's real
   ($z\gtrsim29$–$30$), hand off *once* to full explicit integration for
   everything below (covering both the spiral and later-stable zones
   continuously, no special handling at $z_\text{switch}=18.5$).
   **Re-derived $D_\mu=H_c^2D_J$ myself before trusting it** — confirmed
   exact, not approximate.

2. **Implemented the two-phase design**:
   `wp7_stage3e_riccati_handoff.py` (new, `cdot-8/WP7/`). Caught my own
   sign error before running anything further — an initial version
   picked the wrong (unstable) root of the fixed-point quadratic as the
   seed, caught by checking against already-known eigenvalues.

3. **The corrected run still failed**, at every handoff redshift tried
   ($35$ through $29.8$), with the same solver error as before, now
   localized to the Riccati phase itself. **Diagnosed cleanly**:
   linearizing the $\mu$-Riccati equation around its stable fixed point
   gives a growth coefficient $\lambda_\text{unstable}-\lambda_\text{
   stable}$, always positive — **forward-$N$ integration of the stable
   branch is itself a repelling flow**. Confirmed numerically: seeding
   at the exact analytic value at $z=60$ and integrating just
   $\Delta N=0.01$ forward already drifts measurably from truncation
   error alone; a $10^{-6}$–$10^{-9}$ perturbation blows the trajectory
   out of its own tabulated domain within a handful of steps. This is a
   known phenomenon in Riccati/shooting-method numerics (why such
   equations are normally integrated backward from a well-posed
   terminal point, or tracked as an unnormalized vector rather than a
   scalar ratio).

**Files produced/updated**: `wp7_stage3e_riccati_handoff.py` (new,
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md` (§39,
new), this entry.

**Status: the advisory's conceptual resolution (one handoff, no complex
generalization) is accepted and stands; the concrete numerical
implementation needs a different integration strategy** (backward
propagation from a well-posed point, or a compound/unnormalized-vector
formulation), neither yet attempted. Checkpointed rather than forcing a
fix without review — the fifth consecutive round on this single
sub-problem, each surfacing a genuine subtlety the last didn't
anticipate. Recommending the integration-direction/formulation question
be put to the advisor next. Nothing in `cdot-7/` was touched.

---

**Continued in `SessionLog-2026-07-21.md`.**
