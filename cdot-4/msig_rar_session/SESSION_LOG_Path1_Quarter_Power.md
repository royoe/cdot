# SESSION LOG — Path 1 Attempt: $M^{1/4}$ Quarter Power as Geometric Mean

**Topics:** T14 (Connecton Gravity), T6 (MOND Scale), T15 (RAR), T17 (M-σ)
**Date:** 2026-06-30
**Session type:** Derivation attempt — testing whether Path 1 (geometric-mean reframing)
produces the quarter power analytically.

---

## Timeline

**[2026-06-30 10:16 UTC] — Prior session.**
Produced the five-path scoping document for the M-σ / $M^{1/4}$ non-analytic wall.

**[2026-06-30 12:37 UTC] — User prompt (verbatim):**
> Let's attempt Path 1 then.

**[2026-06-30 12:37 UTC] — Work performed.**

Re-read the relevant T14 / T6 machinery (foam-diffusion Newtonian $1/r$; cosmological
background gradient $g_\dagger\sim cH_0$; dynamical-selection attractor). Tested whether a
coupled foreground/background steady state yields $B_c^2\propto g_N\,g_\dagger$.

Key intermediate finding: a geometric mean **cannot** come from linear superposition of
the two fields (that gives Newton + constant, additive). It must come either from a
nonlinear field equation or from a junction/selection condition. Path 1's hypothesis is
the latter.

**[2026-06-30 12:37 UTC] — Result.**

The BTFR asymptote emerges analytically:
- Transition radius $r_t = \sqrt{GM/g_\dagger}\propto\sqrt M$ (where mass acceleration =
  background).
- Velocity sampled at $r_t$ (selection attractor): $v_f^2 = g_\dagger r_t = \sqrt{GM\,g_\dagger}$.
- Therefore $v_f^4 = GM\,g_\dagger$, i.e. BTFR with $a_0\equiv g_\dagger\sim cH_0$.
- $B_c = v_f/r = (GM\,g_\dagger)^{1/4}/r$ — the $M^{1/4}$ amplitude, now analytic.

Structural insight: the quarter power is the geometric mean of two **linear** quantities,
joined at a **mass-dependent** radius. The nonlinearity lives in the geometry of where the
surviving population sits, not in the source coupling. This is why the five fixed-radius
linear mechanisms (cdot-3) all failed with $v^4\propto M^2$, while this does not.

Bonus: M-σ becomes a derived consequence ($M_\text{BH}\propto\sigma^4\propto
v_f^4=GM_\text{bary}a_0$) rather than an independent input — the "consistency condition"
of T16/T17 now has a reason. BH Role 1 (sourcing) stays ruled out; the BH tracks the
baryonic normalization through the shared $a_0$.

**[2026-06-30 12:37 UTC] — Critical assessment (recorded, not glossed).**

1. Derives the BTFR **asymptote and scale only** — not the full RAR interpolating
   function. Crossover *shape* near $r_t$ uncomputed.
2. **Debt relocated, not removed:** assumes the selection attractor pins $v_f$ at $r_t$;
   T14 flags this convergence as unproven. Swaps a quarter-power-source problem (no natural
   home) for a why-$r_t$ dynamical-systems problem (plausible attractor).
3. Order-one coefficient ($a_0\approx cH_0/2\pi$) still inherited from T14's unproven
   closure condition, not derived here.

**Verdict:** Path 1 succeeds at its stated goal — the $M^{1/4}$ wall is shown to be an
artifact of demanding a direct source. It comes down onto the attractor-convergence /
RAR-shape problem. Genuine progress; not closure.

**[2026-06-30 12:37 UTC] — Visual produced.**
Inline SVG: log-log sketch of $g_\text{mass}=GM/r^2$ crossing $g_\dagger\approx cH_0$ at
$r_t\propto\sqrt M$, with $v_f^2=\sqrt{GM\,g_\dagger}$ read at the crossover.

**[2026-06-30 12:37 UTC] — Deliverables.**
- `UPDATE_T14_Path1_Quarter_Power_GeometricMean.md`
- `SESSION_LOG_Path1_Quarter_Power.md` (this log)

**Next computation flagged (highest leverage):** solve the crossover shape at the
selection junction near $r_t$ and compare to the McGaugh RAR interpolating function. Closes
Path 1 from "BTFR asymptote" to "RAR" if it matches; otherwise RAR shape needs separate
physics.
