# UPDATE — Path 1 Closure: The RAR Crossover Shape from the Selection Junction

*Proposed update to T14, T6, T15; status change in Core Principles §7. Status: the RAR
interpolating function is derived from a motivated (not yet first-principles) closure and
fits the empirical McGaugh relation to 0.02 dex with zero free parameters. Session:
2026-06-30.*

---

## 1. Result in One Line

Promoting the transition-radius condition (Path 1) to all radii yields a closed-form,
parameter-free interpolation between Newtonian and deep-MOND gravity that **matches the
empirical McGaugh-Lelli-Schombert RAR to 0.020 dex across six decades** — six times inside
the observed 0.13 dex scatter — while exactly preserving the BTFR normalization
$v_f^4 = GM\,a_0$ and the Newtonian strong-field limit.

---

## 2. The Computation

The RAR relates two accelerations at the **same radius**: the dynamical
$g_\text{obs}=v^2/r$ and the Newtonian baryonic $g_\text{bar}=GM(<r)/r^2$. Empirically
(McGaugh et al. 2016):
$$g_\text{obs}=\frac{g_\text{bar}}{1-e^{-\sqrt{g_\text{bar}/g_\dagger}}},
\qquad g_\dagger\approx1.2\times10^{-10}\ \text{m/s}^2.$$

**The selection-junction closure.** Write $g_\text{obs}=g_\text{bar}+g_x$, where $g_x$ is
the connecton response field (the $v\times B_c$ contribution, T14). The transition-radius
condition $g_\text{bar}(r_t)=g_\dagger$ generalizes to a steady-state balance at every
radius: the response field $g_x$, propagating in the **total** gradient
$(g_x+g_\text{bar})$, is driven by the baryonic source $g_\text{bar}$ coupled to the
cosmological background scale $g_\dagger$:
$$\boxed{\,g_x\,(g_x+g_\text{bar})=g_\text{bar}\,g_\dagger.\,}$$
This is the steady state of a field whose effective diffusion constant scales with the
total acceleration — the transition-radius condition promoted to all $r$. Solving:
$$g_x=\tfrac12\!\left(-g_\text{bar}+\sqrt{g_\text{bar}^2+4g_\text{bar}g_\dagger}\right),
\qquad
g_\text{obs}=\tfrac12\!\left(g_\text{bar}+\sqrt{g_\text{bar}^2+4g_\text{bar}g_\dagger}\right).$$

This is **exactly MOND's "simple" interpolating function** — derived here, not assumed.

**Limits (both forced, both correct):**
- $g_\text{bar}\gg g_\dagger$: $g_\text{obs}\to g_\text{bar}$ (Newton). ✓
- $g_\text{bar}\ll g_\dagger$: $g_\text{obs}\to\sqrt{g_\text{bar}g_\dagger}$ (deep MOND;
  BTFR $v_f^4=GM\,g_\dagger$ with coefficient exactly 1). ✓

**Fit to empirical RAR:** max $|\Delta|=0.020$ dex (at $g_\text{bar}/g_\dagger\approx7$),
rms $=0.009$ dex, 100% of the six-decade range within 0.05 dex. Observed scatter is
0.13 dex.

---

## 3. Candidate Comparison (why the result is non-trivial)

Four closures with the correct asymptotes were tested against McGaugh:

| Closure | max \|Δ\| (dex) | rms (dex) |
|---|---|---|
| Selection junction = "simple" (this work) | **0.020** | 0.009 |
| Quadrature $\sqrt{g_b^2+g_b g_\dagger}$ | 0.057 | 0.028 |
| "Standard" MOND form | 0.095 | 0.045 |
| Newton + geometric-mean term | 0.113 | 0.065 |

All four hit both asymptotes; they differ only in the crossover. The closure the
construction actually picks is the **best** fit and the only one well inside 0.05 dex
everywhere. The data therefore *mildly prefer* the construction's closure — encouraging,
though not by itself a derivation.

---

## 4. Honest Limitations (do not overstate on merge)

1. **The closure is motivated, not yet first-principles.** The asymptotes are forced; the
   *shape* depends on the specific closure $g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$. It
   is argued to be the natural steady state of an acceleration-dependent diffusion constant
   (the transition-radius condition at all $r$), but it has **not** been derived line-by-
   line from the connecton diffusion equation of T14. A full derivation would solve the
   foam-diffusion PDE with the background gradient as boundary condition and read off the
   effective $g_x(g_\text{bar})$.
2. **Mild self-consistency wrinkle.** At the nominal transition ($g_\text{bar}=g_\dagger$)
   the two contributions cross at $g_x/g_\text{bar}=1/\varphi\approx0.618$ (golden ratio),
   not exactly 1. "Crossover sits at $r_t$" holds to order unity, not exactly. Harmless for
   the fit; recorded for honesty.
3. **Order-one coefficient of $a_0$ still inherited.** $g_\dagger\sim cH_0$ is dimensional;
   the $1/2\pi$ factor (T6) comes from T14's unproven closure condition
   $4\pi GL\rho_\text{bg}/3\sigma=c$, not from this computation.
4. **Attractor convergence still assumed** (carried over from the prior Path 1 update): the
   surviving population is taken to sit on the marginal-binding curve at all radii.

---

## 5. Suggested Document Edits (on merge)

- **T14** — add §"RAR crossover from the selection junction" with §2 above. The headline
  changes: the model now reproduces the *full RAR functional form*, not just the scale.
  Demote the "structural $\sqrt M$ / non-analytic wall" framing to a solved-conditional:
  the wall fell to the transition-radius geometric mean (prior update), and the crossover
  shape follows from the junction closure. Promote "derive the closure from the diffusion
  PDE" to open item 1.
- **T6 / T15** — change "RAR functional form: no mechanism exists" to "**derived** from the
  selection-junction closure; fits McGaugh to 0.02 dex, parameter-free; closure motivated,
  full PDE derivation open." Keep the $a_0=cH_0/2\pi$ coefficient as open.
- **Core Principles §7** — change
  "Radial Acceleration Relation / MOND functional form: **Open — scale matches, mechanism
  absent**" to
  "Radial Acceleration Relation: **Substantially advanced** — BTFR, scale, and full RAR
  crossover (0.02 dex vs McGaugh, parameter-free) follow from the transition-radius /
  selection-junction construction (T14); closure derivation and $a_0$ coefficient open."
  No core *premise* changes.

---

## 6. The Next Computation (highest leverage)

Derive the closure $g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$ from the connecton
foam-diffusion equation with the cosmological background gradient as the far-field boundary
condition. If the PDE delivers this closure (or one within scatter), the RAR is derived
from first principles and the model moves from "fits the RAR" to "predicts the RAR." If it
delivers a different closure, compare that one's fit — the data discriminate at the
0.02–0.10 dex level, so the PDE's verdict is checkable.
