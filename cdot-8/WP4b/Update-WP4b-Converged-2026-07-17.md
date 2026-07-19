# Update — WP4b: The Converged Result Is Much Larger Than Either Prior Estimate — a Genuine, Severe Deficit, Not a Bug I Can Find

*Companion: `SessionLog-2026-07-16.md` (this directory). Follows
`Update-WP4b-BBN-Correction-2026-07-16.md`, which withdrew the original
numbers and flagged an unconverged, transition-width-dependent recalculation
(ratio $\approx0.19$–$0.27$). This update removes the ad hoc width entirely
by solving entropy conservation directly, and reports what that gives —
which is more severe than either prior number, verified as carefully as I
can within this session, and escalated rather than finalized.*

---

## 1. Removing the ad hoc transition width

The previous round's "smooth switch" between pre/post-annihilation neutrino
treatments was patched over an arbitrary width because a hard switch broke
the ODE solver. Replaced it with the actual physics: solved **photon+$e^\pm$
entropy conservation directly** for $T_\gamma(a)$ (building the entropy
density from the same equilibrium energy and pressure integrals, verified at
$A=0$ to reproduce the known $u_{e^\pm}/u_\gamma=1.75$ and, correspondingly,
$s_{e^\pm}/s_\gamma=1.75$ in the relativistic limit), rather than assuming
$T_\gamma(z)=T_{\gamma,0}(1+z)$ throughout. This is not a free choice of
width — entropy conservation pins $T_\gamma(a)$ exactly, given only the
known equilibrium physics of the photon+$e^\pm$ bath.

**This surfaces a third issue, distinct from Flags 1–2**: $T_\gamma(z)=
T_{\gamma,0}(1+z)$, used everywhere in this session's BBN-era calculations
(including the original WP4a-adjacent assumption that this relation is exact
at all $z$), is only exact **after** the $e^\pm$ transition completes.
Checked numerically: at $T=5$ MeV (deep in the transition's past side), the
true redshift for a given temperature is $\sim40\%$ higher than the naive
$T_{\gamma,0}(1+z)$ relation gives, converging to the naive relation exactly
by $T\sim0.02$ MeV — reproducing the standard $(11/4)^{1/3}$ boost factor
from first principles, not merely citing it. Neutrino decoupling ($T_\text
{dec}\approx2.3$ MeV, standard value) is treated as sharp; below it,
neutrinos share $T_\gamma$; above it, the already-established, unmodified
$T_{\nu,0}(1+z)$ frozen relation applies — continuous at the switch since
$m_\nu\ll T$ on both sides, so no numerical discontinuity this time.

## 2. Verification before trusting the result

- **Regression check against WP4a**: with these corrections, $E(z)$ at
  recombination-era redshifts ($z=1090$: $18403$; $z=10^6$: $8.893\times
  10^9$) reproduces the previously-validated WP4a values *exactly* — the
  corrections are inert where they should be (recombination is far past the
  $e^\pm$ transition) and only bite where they should (BBN-era redshifts).
  This is the single most reassuring check available: nothing in this round
  broke what was already established.
- **Trajectory sanity**: $x(s)$ at BBN-era redshifts sits at $3.3$–$3.44$,
  properly close to the established radiation fixed point ($3.44$) with no
  saturation or runaway behavior — the closure ODE itself is behaving,
  not producing a numerical artifact dressed as physics.
- **Stability across nearly two decades in temperature**: the ratio holds
  at $0.27$–$0.28$ from $T=1$ MeV down to $T=0.02$ MeV, with no residual
  dependence on the (now physically-derived, not chosen) transition
  treatment — this is what "converged" means here, in contrast to the
  previous round's $0.19$–$0.27$ spread under an arbitrary width.

## 3. Result, reported without inventing false precision downstream

$$H_{\hat\tau}/H_\text{SBBN}\approx0.276\ \text{(stable across the BBN
window)},\qquad \Delta N_\text{eff}^\text{eff}\approx-5.7.$$

**This is roughly eight times larger than the previously-withdrawn
$-0.7$, and far outside the regime where the standard literature
sensitivity coefficients ($\partial Y_p/\partial N_\text{eff}\approx0.013$,
etc.) mean anything** — those are linearizations around the standard model,
valid for $|\Delta N_\text{eff}|$ of order $1$, not $6$. Reporting a
specific $Y_p$ or D/H number from a linear extrapolation at this magnitude
would manufacture false precision, not deliver a real estimate — explicitly
not done here. What can be said without a reaction-network code: a
deficit of this size, if it survives further scrutiny, would not plausibly
leave standard BBN's light-element successes intact — this is no longer a
"mild tension" question.

## 4. Status — escalating, not finalizing

**I have not found a bug in this calculation after real effort to find
one** (the regression check, the trajectory sanity check, and the
first-principles reproduction of the standard $(11/4)^{1/3}$ factor are all
clean) — but a result this severe, this late in a multi-round correction
process that already contained two confirmed bugs, warrants independent
re-derivation before being treated as settled. This is exactly the posture
this program has used throughout: verified as far as I can push it alone,
reported precisely, not asserted as final. **Recommend**: independent
re-derivation of the entropy-conservation step and the resulting $H(z)$
ratio before this feeds the Foundation §6 item 6 decision input — if it
holds up, the BBN confrontation is no longer "borderline" as the earlier
discrepancy-hunt round framed it, but a severe tension in its own right,
independent of and larger than the acoustic-scale miss. WP4a is unaffected
(confirmed by the regression check above). The KATRIN clock remains the
program's most time-critical item; nothing in `cdot-7/` was touched.
