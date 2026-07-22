# Advisory — WP7 Stage 3d's Boundary-Condition Problem: Diagnosis Endorsed, and a Second, Compounding Issue Found — the Quasi-Static Approximation Is Already Marginal Well Before the Switch, Not Just At It; Recommend a Riccati/Stable-Subspace Continuation Seeded Deep in the Good Regime, Not a Better Guess at $z=100$ (for `cdot-8/WP7/`)

*2026-07-20. Advisory in response to §37 of
`Update-WP7-PerturbationStructure-2026-07-18.md` (Stage 3d).
Independently reran `wp7_stage3d_hybrid_closure.py` and extended its
own machinery for the additional check in §3 below. Gate 1(b) carried.
**Verdict up front: the worker's diagnosis is right and well-argued —
this is a boundary-condition/stable-manifold selection problem, not a
relaxation, precisely because the eliminated mode grows rather than
decays, and it is structurally the same class of problem as WP3's own
past-regularity/$C_1$ selection. I found one thing worth adding before
a fix is attempted: the quasi-static approximation's own validity
condition ($|\lambda_\text{max}|\gg1$ per e-fold, the natural
comparison since $N$ is the ODE's time variable) is already only
marginal by $z\approx25$–$30$ — a good ten-or-more e-folds in redshift
above $z_\text{switch}=18.5$ — so "pick a better initial condition at
$z=100$ and keep slaving all the way to the switch" cannot be the
whole fix even once solved correctly. Recommend a stable-subspace
(Riccati-type) continuation, seeded where the naive algebraic answer is
known-good and propagated by its own smooth equation through the
marginal zone, rather than re-deriving the same potentially-singular
algebraic relation at every step down to the switch.**

---

## 1. Reproduced and confirmed — the failure is exactly as reported

Ran `wp7_stage3d_hybrid_closure.py` directly. $z_\text{switch}(10^{-4}\,
\text{Mpc}^{-1})=18.543$, matching the advisor's own bracket exactly.
The margin scan reproduces the reported blow-up precisely:
$\delta_b(z{=}0)$ from $+0.144$ (margin $0.2$ e-folds) down to
$-1.8\times10^7$ (margin $0.02$) — many orders of magnitude of
sensitivity to a parameter that should not matter if the closure were
well-posed. Confirmed by direct inspection of the trace: the mismatch
is already present at $z=100$ ($\chi\approx21.7$ from
$\bar{\mathcal Q}\approx2190$ acting on $O(0.01)$ initial data, giving
a slaved $\mathcal E_\alpha\approx-76$ against the true initial
$\mathcal E_\alpha=0$) and grows monotonically through the quasi-static
phase.

## 2. The diagnosis is right, and worth stating precisely for the record

Standard tight-coupling/adiabatic elimination is valid because the
eliminated variable's own dynamics are **stably damped**: any mismatch
between the true value and the algebraic slaved value decays on the
fast timescale, so the choice of starting point for the *slow*
variables is all that matters — the fast variable's own initial value
is forgotten almost immediately. Here $\partial\dot{\mathcal
E}_\alpha/\partial\mathcal E_\alpha>0$ throughout the quasi-static
phase (confirmed directly: this is exactly $-\text{coef}_E/(\mathcal
K_BH_c)$, and $\text{coef}_E<0$ there per Stage 3b/3c), so the
"attractor" logic is inverted — any mismatch **grows**, and the
algebraic relation is not something the system relaxes onto, it is a
**selection criterion**: the one initial condition for which the
solution has zero overlap with the growing eigendirection at every
subsequent instant. This is exactly the same structure as WP3's own
past-regularity/$C_1=0$ selection (choose the constant of integration
that avoids the unphysical branch, not by waiting for anything to
decay). Good instinct to name that analogy explicitly.

## 3. What I'd add: the approximation is already marginal well before the switch

Computed $\lambda_\text{max}(z)$ (the same eigenvalue already audited
in Stage 3b/3c) directly in its **natural units for this check**: since
the ODEs are integrated in $N=\ln(a/a_0)$, the relevant adiabaticity
requirement for trusting an instantaneous/frozen-coefficient algebraic
elimination is $|\lambda_\text{max}|\gg1$ **per e-fold** (not per
Hubble time — $N$ is already the system's own clock) — the background
coefficients ($\Omega_s,c_\text{ad}^2,\bar{\mathcal Q}$, etc.) vary on
a timescale of order one e-fold, so the fast mode needs to be much
faster than *that* to justify freezing them while eliminating
$\mathcal E_\alpha$. Result:

| $z$ | $\lambda_\text{max}$ (per e-fold) |
|---:|---:|
| $100$ | $221.1$ |
| $80$ | $111.0$ |
| $60$ | $47.7$ |
| $50$ | $28.4$ |
| $40$ | $14.8$ |
| $30$ | $3.4$ |
| $25$ | $0.75$ |
| $22$ | $0.34$ |
| $20$ | $0.13$ |
| $18.5$ | $\approx0$ (the switch, by construction) |

**The separation is genuinely good ($\gg1$) only for
$z\gtrsim50$–$60$; it is already order unity by $z\approx25$–$30$**,
a full ten-plus e-folds in redshift above the switch itself. This means
the quasi-static phase, as currently scoped (slaving unchanged from
$z=100$ down to $z_\text{switch}+\text{margin}\approx18.6$), spends a
substantial stretch of its own domain ($z\approx20$–$30$) in a regime
where the *leading-order* algebraic answer is no longer a trustworthy
approximation to the true stable-manifold condition, independent of
whatever the $z=100$ initial-condition problem does. **Fixing only the
$z=100$ initial condition (e.g. by a shooting search on $\alpha(100)$)
would not by itself repair the $z\approx20$–$30$ stretch** — the
algebraic relation itself is drifting away from the true selection
condition there, not just carrying forward an old mismatch.

**One thing I was not able to confirm cleanly and want to flag rather
than assert**: a quick finite-difference Jacobian of the *full*
6-variable system (not just the $(\alpha,\mathcal E_\alpha)$ pair)
suggested there may be a **second** unstable direction distinct from
the audited one, tentatively of a more ordinary gravitational-Jeans
character from the $(\delta_b,\theta_b)$/$\Phi$ coupling. My own
finite-difference construction is not precise enough, given the huge
range of coefficient magnitudes in this system, to trust that number —
**recommend a careful (symbolic or carefully-scaled) check of how many
independent growing directions the full coupled system has** before
assuming a single shooting parameter (or a single stable-subspace
projection) is sufficient. If there are two, the selection condition
needs to eliminate both.

## 4. Recommendation: propagate the stable-subspace relation, don't re-derive it at each step

Rather than (a) guessing a better $z=100$ initial condition and
re-applying the same fixed algebraic formula down to the switch, or
(b) trying to patch the margin sensitivity with a smoother blend
(already argued against in Stage 3c's advisory, and this new finding
sharpens why: the *algebraic* answer itself, not just the switch
location, is what degrades approaching threshold) — recommend the
standard technique for this class of problem: treat "$\mathcal
E_\alpha$ as a function of the slow variables" as a **continued,
smoothly-evolving linear relation** (a Riccati-type object), not a
fresh algebraic solve at every point.

Concretely: seed the relation deep in the well-separated regime
($z\gtrsim60$, where the naive algebraic slaving is an excellent
leading-order approximation to the true stable-manifold condition —
this removes the guesswork the current initial condition has), then
**evolve it forward via its own consistency (Riccati) equation** —
derived by requiring the slaving relation stays invariant under the
true, coupled dynamics rather than being re-solved from a frozen-
coefficient snapshot at each step. This is the standard resolution for
"track a stable/decaying solution branch through a region where a
naive algebraic elimination becomes singular" (the same logic behind
transfer-matrix and Riccati-shooting methods for stiff two-point
problems, and for WKB connection through a marginal region). It should,
if implemented correctly, remain well-conditioned through the
$z\approx20$–$30$ marginal zone and hand off smoothly to explicit
integration once safely stable — but this is a genuine, non-trivial
derivation, not a drop-in fix, and should be verified with the same
care (reproduce, cross-check by hand, regression against the
already-trusted deep-$z$ regime) as everything else in this program
before being trusted.

## 5. What's solid regardless

The switch criterion itself ($\text{tr}(J)=0$, i.e. $z_\text{switch}=
18.54$ for this $k$) is unaffected by any of this and stays correct.
The dust-sector and $\Pi$-normalization fixes from Stages 3b/3c are
untouched. This is specifically about how the quasi-static *phase's*
own initial/ongoing condition should be determined, not about where it
ends.

## 6. Housekeeping

Nothing in `cdot-7/` was touched. Gate 1(b)'s caveat, $Q_2$/EFE
sequencing, and KATRIN watch are unchanged. The full-system
unstable-direction-count question (§3) and the optional AeST-native
cross-check (from Stage 3b) are both open, neither urgent relative to
this one.

## Companion

- No new standalone script — the adiabaticity table reused
  `wp7_stage3_vector_stiffness_audit.py`'s Jacobian with the Stage-3b
  normalization, evaluated over a finer $z$-grid; the full-system
  check was an exploratory finite-difference Jacobian on
  `wp7_stage3d_hybrid_closure.py`'s own `rhs_full`, flagged above as
  not precise enough to trust as a stated result.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-Stage3dBoundaryConditionProblem-2026-07-20.md`.
