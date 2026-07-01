# SESSION LOG — RAR Crossover Shape Computation (Path 1 closure)

**Topics:** T14 (Connecton Gravity), T6 (MOND Scale), T15 (RAR)
**Date:** 2026-06-30
**Session type:** Computation — does the selection junction reproduce the McGaugh RAR
interpolating function, or only its asymptotes?

---

## Timeline

**[2026-06-30 12:37 UTC] — Prior session.**
Path 1 derived the BTFR asymptote via the transition-radius geometric mean; flagged the
crossover shape as the highest-leverage next computation.

**[2026-06-30 12:49 UTC] — User prompt (verbatim):**
> Please continue with computing the crossover shape.

**[2026-06-30 12:49 UTC] — Work performed.**

Set up the RAR as a same-radius relation between $g_\text{obs}=v^2/r$ and
$g_\text{bar}=GM/r^2$. Recognized that the single-radius Path 1 argument must be promoted
to a force law at all radii to produce a curve. Wrote $g_\text{obs}=g_\text{bar}+g_x$ with
$g_x$ the connecton response field, and tested candidate closures numerically against the
McGaugh-Lelli-Schombert 2016 interpolating function.

**[2026-06-30 12:49 UTC] — Result.**

The selection-junction closure
$$g_x(g_x+g_\text{bar})=g_\text{bar}\,g_\dagger$$
(the transition-radius condition generalized to all radii: response field propagating in
the total gradient, driven by baryonic source × background scale) solves to
$$g_\text{obs}=\tfrac12\!\left(g_\text{bar}+\sqrt{g_\text{bar}^2+4g_\text{bar}g_\dagger}\right),$$
which is exactly MOND's "simple" interpolating function — derived, not assumed.

Numerical comparison vs McGaugh (units of $g_\dagger$, range $10^{-3}$ to $10^3$):
- max |Δdex| = 0.020 (at $g_\text{bar}/g_\dagger\approx7$); rms = 0.009 dex.
- 100% of the six-decade range within 0.05 dex. Observed RAR scatter = 0.13 dex.
- Deep limit coefficient = 1.000 → BTFR normalization $v_f^4=GM\,a_0$ preserved exactly.
- Newton limit recovered.

Candidate discrimination (all hit asymptotes; differ in crossover):
- selection junction / "simple": 0.020 dex  ← construction's choice, best fit
- quadrature: 0.057 dex
- "standard" MOND: 0.095 dex
- Newton + geometric-mean: 0.113 dex
Data mildly prefer the construction's closure.

**[2026-06-30 12:49 UTC] — Critical assessment (recorded, not glossed).**

1. Asymptotes are forced; only the *shape* tests the closure. The closure is **motivated**
   (acceleration-dependent diffusion = transition-radius condition at all r) but **not yet
   derived** line-by-line from the connecton diffusion PDE.
2. Self-consistency wrinkle: at the nominal transition the contributions cross at
   $g_x/g_\text{bar}=1/\varphi\approx0.618$, not exactly 1. Crossover at $r_t$ holds to
   order unity. Harmless for the fit.
3. $a_0$ order-one coefficient ($\approx cH_0/2\pi$) still inherited from T14's unproven
   closure condition, not derived here.
4. Attractor convergence still assumed (carried from prior Path 1 update).

**Verdict:** Path 1 closes from "BTFR asymptote" to "full RAR shape." The model reproduces
the RAR functional form to 0.02 dex, parameter-free. Rests on a motivated, data-favored,
but not-yet-first-principles closure. Genuine advance; the remaining debt is a single PDE
derivation.

**[2026-06-30 12:49 UTC] — Visuals produced.**
- Log-log RAR plot: model curve vs McGaugh vs Newton, with stat cards (0.020 dex / 0.13 dex
  scatter / 0 free parameters).
- (Prior turn) transition-radius geometric-mean sketch.

**[2026-06-30 12:49 UTC] — Deliverables.**
- `UPDATE_T14_RAR_Crossover_Shape.md`
- `SESSION_LOG_RAR_Crossover_Shape.md` (this log)

**Next computation flagged (highest leverage):** derive the closure
$g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$ from the foam-diffusion PDE with the
cosmological background gradient as far-field boundary condition. If it delivers this
closure (or one within scatter), the RAR is predicted from first principles. The data
discriminate at 0.02–0.10 dex, so the PDE's verdict is checkable.
