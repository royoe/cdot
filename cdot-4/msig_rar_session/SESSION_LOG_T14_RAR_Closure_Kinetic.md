# SESSION LOG — Kinetic Derivation of the RAR Closure (T14 Open Item 1)

**Topics:** T14 (Connecton Gravity), T6 (MOND scale), T15 (RAR)
**Date:** 2026-06-30
**Session type:** First-principles derivation attempt — does the connecton foam-diffusion
PDE deliver the RAR closure, or a different one?

---

## Timeline

**[2026-06-30 ~12:49 UTC] — Prior session.**
RAR crossover update closed Path 1 to the full RAR via the closure
$g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$ (motivated, not derived; 0.02 dex vs McGaugh).
Flagged the PDE derivation of this closure as highest-leverage open item.

**[2026-06-30 14:21 UTC] — User prompt (verbatim):**
> Let's drop back to T14 for a bit. You ended the change request with:
> 6. The Next Computation (highest leverage) — Derive the closure g_x(g_x+g_bar)=g_bar g†
> from the connecton foam-diffusion equation with the cosmological background gradient as
> the far-field boundary condition. ... Can we proceed on this?

**[2026-06-30 14:21 UTC] — Work performed.**

1. Reduced the closure to a constitutive law via nonlinear (AQUAL-type) Poisson:
   $D(g)g=g_\text{bar}$, with the target closure equivalent to $D(g)=g/(g+g_\dagger)$
   (the simple μ-function). So "derive closure" = "derive $D(g)$."
2. First pass exposed a trap: writing the relaxation balance as $g(g+g_d)=g_\text{bar}g_d$
   is just restating the closure. Required a genuine kinetic argument for $D(g)$.
3. Built the excess-field steady state: production $\propto g_\text{bar}$ balanced by
   relaxation $\nu g_x$. The non-trivial step is the scaling of $\nu$.
4. Kinetic theory: $\nu=n_\text{scatter}\sigma c$. The ambient population an excess
   connecton relaxes against is the TOTAL field, because connectons are identical,
   conserved, re-emitted quanta (T14 premise) — an excess connecton cannot distinguish
   background from other excess. Hence $\nu\propto g_\text{tot}=(g_x+g_\text{bar})/g_d$.
5. Steady state then yields $g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$ — the target,
   derived from indistinguishability rather than assumed.

**[2026-06-30 14:21 UTC] — Result.**

- Closure derived from connecton indistinguishability (pre-existing T14 premise) +
  generalized-Poisson reduction. Deep-MOND coefficient exactly 1 (BTFR exact); Newton
  recovered.
- Data discrimination among relaxation laws:
  - ν ∝ total flux (indistinguishable quanta): 0.020 dex ← derived + best
  - ν ∝ excess only: 0.113 dex (data-excluded)
  - quadrature: 0.057 dex
  - ν const: no MOND
  The empirical RAR selects the indistinguishability law and excludes the alternatives in
  the transition region.
- Crossover at $g_\text{bar}=g_\dagger/2$ (clean), superseding the earlier golden-ratio
  wrinkle (artifact of the geometric-mean framing).

**[2026-06-30 14:21 UTC] — Critical assessment.**

DERIVED: the RAR functional form (shape), from indistinguishability + Poisson reduction;
the derivation uses an existing premise rather than adding one. Data exclude alternatives.

STILL OPEN:
1. Scale coefficient — $g_\dagger=cH_0/2\pi$ still traces to the unproven closure condition
   $4\pi GL\rho_\text{bg}/(3\sigma)=c$. Shape derived, absolute scale not.
2. Relaxation-time closure, not full transport — Step 1 assumes AQUAL-type divergence
   structure; Step 3 uses a relaxation-time approximation. A full Boltzmann/transport
   derivation of $D(g)$ is one rung deeper.
3. Attractor convergence still assumed (separate dynamical-systems question, unaffected).

**Verdict:** PDE verdict is POSITIVE — kinetics delivers the target closure, not a different
one, and the data exclude the near alternatives. Status moves from "fits the RAR" to
"predicts the RAR shape." "From first principles" is qualified: shape from
indistinguishability; scale coefficient remains the open item.

**[2026-06-30 14:21 UTC] — Visual produced.**
Residual-vs-McGaugh plot for the three relaxation laws with the ±0.13 dex scatter band;
total-flux law near zero throughout, alternatives bulging below the band in the transition.

**[2026-06-30 14:21 UTC] — Deliverables.**
- `UPDATE_T14_RAR_Closure_Kinetic_Derivation.md`
- `SESSION_LOG_T14_RAR_Closure_Kinetic.md` (this log)

**Next computation flagged:** (1) derive $g_\dagger=cH_0/2\pi$ from the closure condition
(shared with the T6 $a_0$-coefficient debt); (2) derive $D(g)=g/(g+g_\dagger)$ from the
connecton Boltzmann equation to remove the relaxation-time ansatz.
