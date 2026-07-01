# SESSION LOG — Background-Density Derivation Attempt (Negative + Corrective)

**Topics:** T14 (Connecton Gravity), Core Principles (horizon geometry, premise 1), T6
**Date:** 2026-06-30
**Session type:** Derivation attempt — derive $\rho_\text{bg}(r)$ to close the $a_0$
coefficient. Outcome: negative result + internal inconsistency exposed.

---

## Timeline

**[2026-06-30 14:33 UTC] — Prior session.**
Reported $a_0=c^2/R_0=cH_0/6$ as "derived from horizon geometry, contingent on one O(1)
gradient coefficient $|\nabla\ln\rho_\text{bg}|=1/R_0$." Flagged the density-profile
calculation as the way to close it.

**[2026-06-30 14:43 UTC] — User prompt (verbatim):**
> Let's try deriving the background density too.

**[2026-06-30 14:43 UTC] — Work performed.**

Read Core premises (uniform static particle sea, n=const → the gradient must be in the
CONNECTON sea, not the particle density). Computed candidate $\rho_\text{bg}(r)$ profiles:
- Route A (rho ∝ c(u), inherited from emission epoch): |dln rho/dr| = H0h/c0 = 3/R0 →
  g_dagger = 3c^2/R0 = dot c = cH0/2. Overshoots a0 by 2.83×.
- Route B (conserved deposition as horizon sweeps r): rho ∝ 1/c(r) ∝ r^-3, |dln rho/dr| =
  3/r → 3/R0 at horizon. Same factor 3.
- Both return dot(c), NOT c^2/R0. The prior "c^2/R0" silently dropped a factor 3 (from
  c ∝ R^3).

Deeper finding: the 3/R0 gradient points along the line of sight toward the observer →
cannot be a physical force (every galaxy can't fall toward every observer). Core premise 1
(homogeneous static sea) → no net directional gradient. So g_dagger is NOT a
background-gradient acceleration.

Correct framing: g_dagger = c^2/lambda_floor (saturation scale; isotropic; no factor 3),
lambda_floor = connecton minimal-quantum wavelength.

Inconsistency exposed: T14 §"Energy Scale" gives lambda_floor two ways differing by 6=3P:
- "wavelength ~ horizon distance" → lambda=R0=6c/H0 → g_dagger=cH0/6 (fits)
- "nu ~ H0" → lambda=c/H0=R0/6 → g_dagger=cH0 (6× too big)
Both asserted in T14; mutually inconsistent.

**[2026-06-30 14:43 UTC] — Result (negative + corrective).**

The coefficient is NOT closed. The gradient route gives cH0/2 (wrong by 2.8×). The
saturation route gives cH0/6 ONLY by choosing lambda_floor=R0 over nu=H0 — currently a
choice, not a derivation. The prior session's "derived, one contingency" was too strong:
the contingency is not a mild O(1) factor but a factor-6 ambiguity rooted in an internal
T14 inconsistency.

**[2026-06-30 14:43 UTC] — Critical assessment.**

- RAR shape: still derived (kinetic closure, unaffected).
- RAR scale: OPEN. cH0/6 fits but is not derived. Gradient picture is the wrong object;
  saturation picture is right but its coefficient depends on the unresolved floor-wavelength
  definition (factor 3P ambiguity in T14).
- This is a genuine corrective finding: forcing the derivation exposed that two statements
  in T14's energy-scale section cannot both be true.

Recommend: downgrade the prior a0 update (its coefficient derivation does not survive; its
corrections to the old 2pi and the dot-c/gradient distinction remain valid). Revert Core §7
RAR line to "scale coefficient open."

**[2026-06-30 14:43 UTC] — Visual.**
None produced (negative result; the prior session's a0-vs-H0 plot already shows the cH0/6
fit, which still stands numerically).

**[2026-06-30 14:43 UTC] — Deliverables.**
- `UPDATE_T14_Background_Density_Negative.md`
- `SESSION_LOG_Background_Density.md` (this log)

**Next computation flagged:** resolve the connecton floor wavelength from first principles —
state which Hubble rate (obs vs hor) sets nu and which length (R0, c/H0, or R0/3) is the
physical fluctuation floor. Each gives a definite coefficient (cH0/6, cH0, cH0/2); only one
matches a0. Derive which, do not pick the fitting one.
