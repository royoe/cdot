# UPDATE — Path 1 Result: The $M^{1/4}$ Quarter Power as a Transition-Radius Geometric Mean

*Proposed update to T14, T6, T15, T17. Status: a derivation of the BTFR asymptote from
existing T14 ingredients; NOT yet a full RAR derivation. To be cross-checked and merged.
Session: 2026-06-30.*

---

## 1. Result in One Line

The $M^{1/4}$ "non-analytic wall" (T14) is an artifact of demanding a **direct** source
coupling. The Baryonic Tully-Fisher Relation $v_f^4 = GM_\text{bary}\,a_0$ emerges
**analytically** from two ingredients the model already has — linear mass-sourced
Newtonian gravity (foam diffusion, T14) and the mass-independent cosmological background
acceleration $g_\dagger\sim cH_0$ (T14) — joined at a mass-dependent transition radius.
No fractional-power source coupling appears anywhere.

---

## 2. The Derivation

Two accelerations, both already in T14:

- **Mass-sourced (linear in $M$):** foam diffusion gives Newtonian $\phi\propto M/r$, hence
  $$g_\text{mass}(r) = \frac{GM}{r^2}.$$
- **Cosmological background (mass-independent):** the horizon-growth gradient
  $|\nabla\rho_\text{bg}|\sim\rho_\text{bg}H_0/c$ gives
  $$g_\dagger \sim cH_0 \quad(\text{constant in } r,\ \text{independent of } M).$$

**Transition radius** — where the mass acceleration drops to the background:
$$\frac{GM}{r_t^2} = g_\dagger \quad\Longrightarrow\quad r_t = \sqrt{\frac{GM}{g_\dagger}}\ \propto\ \sqrt{M}.$$

**The attractor evaluation.** In the dynamical-selection picture (T14, T17), the surviving
marginally-bound population accumulates at the transition radius. Circular-orbit balance
evaluated at $r_t$, using $g(r_t) = g_\dagger$ by definition of $r_t$:
$$v_f^2 = g(r_t)\,r_t = g_\dagger\sqrt{\frac{GM}{g_\dagger}} = \sqrt{GM\,g_\dagger}.$$

Therefore:
$$\boxed{\,v_f^4 = GM\,g_\dagger = GM\,(cH_0),\qquad a_0\equiv g_\dagger\sim cH_0.\,}$$

The Lorentz-field form follows: $B_c = v_f/r = (GM\,g_\dagger)^{1/4}/r$ — the
$M^{1/4}$ amplitude that T14 called non-analytic.

---

## 3. Why This Is Not the Old Wall

The quarter power is the **geometric mean** of two linear quantities:
$$v_f^2 = \sqrt{g_N(r_t)\cdot g_\dagger}\quad\Longleftrightarrow\quad
(rB_c)^2 \propto g_N\cdot g_\dagger.$$

The five mechanisms that failed (T14, cdot-3) all evaluated the force at a **fixed**
radius and obtained $M/r$ (linear → $v^4\propto M^2$, wrong TF slope). The new element is
that **the radius itself is mass-dependent** ($r_t\propto\sqrt M$), and the velocity
samples the field at that mass-dependent radius. The field equation stays linear; the
nonlinearity lives in the **geometry of where the surviving population sits**, not in the
source coupling. This is why no fractional-power source is required.

---

## 4. Bonus: M-σ Becomes a Derived Consequence

Since $M_\text{BH}\propto\sigma^4\propto v_f^4 = GM_\text{bary}\,a_0$ (T17), and the BTFR
now falls out of the transition-radius geometry, the **M-σ relation is the same equation**
— exactly the "consistency condition" T16/T17 pointed at, now with a reason. The central
BH does not need to *source* the galactic field (Role 1 stays correctly ruled out, T6); it
merely tracks the baryonic normalization through the shared $a_0$. The $M^{1/4}$ in
$B_c\sim M_\text{BH}^{1/4}/r$ and the $M^{1/4}$ in $(GM_\text{bary}a_0)^{1/4}/r$ are the
same quarter power read through two masses that the BTFR locks together.

---

## 5. Honest Limitations (do not overstate on merge)

1. **BTFR asymptote, not full RAR.** This derives the deep-MOND limit (flat-curve
   velocity) and the scale. It does **not** yet derive the RAR interpolating function
   $g_\text{obs}=g_\text{bar}/[1-e^{-\sqrt{g_\text{bar}/g_\dagger}}]$. The crossover *shape*
   near $r_t$ depends on how the mass-sourced and background fields add there — uncomputed.
   Status: scale ✓, slope ✓, crossover shape open.

2. **The debt is relocated, not removed.** The construction assumes the selection
   attractor pins the velocity at $r_t$. T14 itself flags that convergence of the Lorentz
   filter to $B_c=v_f/r$ is unproven. Path 1 swaps a *quarter-power-source* problem (no
   natural home) for a *why-does-selection-pick-$r_t$* problem (a dynamical-systems
   question with a plausible attractor). Progress, not closure.

3. **Order-one coefficient still open.** $a_0\sim cH_0$ is dimensional; the observed
   $a_0\approx cH_0/2\pi$ (T6) factor is inherited from T14's unproven closure condition
   $4\pi GL\rho_\text{bg}/3\sigma = c$, not derived here.

---

## 6. Suggested Document Edits (on merge)

- **T14** — reclassify the "non-analytic wall" as *conditional on a direct-source
  assumption*. Add §: "Quarter power as transition-radius geometric mean" with the
  derivation of §2 above. Note the wall comes down onto the attractor-convergence problem
  (open item 2 of T14 is now the binding constraint, not the source non-analyticity).
- **T6 / T15** — record that the BTFR asymptote and scale are now derived from the
  transition-radius construction; the RAR crossover *shape* remains the open target. Move
  "$\sqrt M$ signature: why linear mechanisms fail" to note the geometric-mean escape.
- **T17** — M-σ downgraded from "independent tight correlation" to "derived consequence of
  the shared $a_0$ via the BTFR"; the four-link morphology chain is unaffected.
- **Core Principles §7** — change "Radial Acceleration Relation / MOND functional form:
  Open — scale matches, mechanism absent" to "**Partial** — BTFR asymptote and scale
  derived via transition-radius geometric mean (T14); RAR crossover shape and attractor
  convergence open." No core *premise* changes.

---

## 7. The Next Computation (highest leverage)

Compute the crossover shape: solve for $g(r)$ when the linear mass-sourced field and the
background field are joined through the selection filter near $r_t$, and compare to the
RAR interpolating function. If the natural junction reproduces the McGaugh form (or its
$\sim0.13$ dex tightness), Path 1 closes from "asymptote" to "RAR." If it does not, the
geometric-mean picture is a BTFR account only, and the RAR shape needs separate physics.
