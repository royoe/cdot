# UPDATE — T14: Background-Density Derivation — Negative Result + Internal Inconsistency Found

*Proposed update to T14 (§"Energy Scale: The Minimal Quantum" and §"Toward the RAR")
and a downgrade flag for the prior $a_0=cH_0/6$ result. Status: the attempt to derive the
$a_0$ coefficient from the background connecton density profile FAILED to close it, and in
doing so exposed (a) that the naive gradient picture gives the wrong object, and (b) an
internal inconsistency in T14's connecton energy-scale section. This is a corrective
update, not a confirming one. Session: 2026-06-30.*

---

## 1. Summary (read first)

The previous session reported $a_0 = c^2/R_0 = cH_0/6$ as "derived from horizon geometry,
contingent on one O(1) gradient coefficient." This session tried to close that contingency
by deriving the background density profile $\rho_\text{bg}(r)$. The result is **negative and
corrective**:

1. The honest gradient picture gives $g_\dagger = \dot c = 3c^2/R_0 = cH_0/2$, which
   **overshoots** the measured $a_0$ by $\sim2.8\times$. The factor 3 (from $c\propto R^3$)
   does not cancel. The prior "$c^2/R_0$" silently dropped this 3.
2. The cosmological inheritance gradient ($3/R_0$) points along the line of sight **toward
   the observer** — it cannot be a physical force (every galaxy cannot fall toward every
   observer). By Core premise 1 the sea is homogeneous/isotropic, so it has **no net
   directional gradient**. $g_\dagger$ is therefore **not** a background-gradient
   acceleration.
3. The correct framing is a **saturation/floor scale**: $g_\dagger = c^2/\lambda_\text{floor}$,
   where $\lambda_\text{floor}$ is the connecton ambient-fluctuation (minimal-quantum)
   wavelength. This carries no factor 3.
4. Under that framing the coefficient is pinned by $\lambda_\text{floor}$ — but T14's
   energy-scale section specifies it **two mutually inconsistent ways** (below). The
   $cH_0/6$ value is recoverable only by choosing one of them; it is currently a **choice,
   not a derivation**.

**The $a_0=cH_0/6$ result must be downgraded** from "derived (one O(1) contingency)" to
"obtained under a specific, not-yet-justified choice of the connecton floor wavelength;
the gradient route actually gives $cH_0/2$."

---

## 2. What Was Computed

**Route A — sea density inherited from $c(u)$.** If $\rho_\text{bg}\propto c(u)$ (connecton
sea level inherited from the epoch of emission), then along the past light cone
($du/dr = 1/c$):
$$\left|\frac{d\ln\rho_\text{bg}}{dr}\right|_0 = \frac{H_0^{\text{hor}}}{c_0} = \frac{3}{R_0}
\;\Rightarrow\; g_\dagger = c^2\cdot\frac{3}{R_0} = \frac{3c^2}{R_0} = \dot c = \frac{cH_0^{\text{obs}}}{2}.$$
Overshoots $a_0$ by 2.83× (at $H_0=70$). The factor 3 is structural ($c\propto R^3$).

**Route B — conserved-deposition profile.** The conserved sea laid down as the horizon
swept radius $r$ gives $\rho_\text{bg}(r)\propto 1/c(r)\propto r^{-3}$, again
$|\nabla\ln\rho|=3/r\to3/R_0$. Same factor 3.

**Diagnosis.** Both gradient routes return $\dot c$, not $c^2/R_0$. The prior session's
$c^2/R_0$ was not the output of the gradient calculation — it was $\dot c/3$ with the 3
unexplained.

**The deeper problem.** The $3/R_0$ gradient points toward the observer (earlier epochs lie
along our past light cone in every direction → the gradient is radial-inward to *us*). A
homogeneous static sea (Core premise 1) has no such physical gradient. So the gradient
picture is the wrong physical object for $g_\dagger$.

---

## 3. The Correct Framing — and the Inconsistency It Exposes

If $g_\dagger$ is a **saturation scale** (acceleration at which a mass-induced perturbation
matches the sea's ambient fluctuation floor), then
$$g_\dagger = \frac{c^2}{\lambda_\text{floor}},$$
with $\lambda_\text{floor}$ the connecton minimal-quantum wavelength. This is clean (no
factor 3) and isotropic (a floor, not a direction).

But T14's §"Energy Scale: The Minimal Quantum" specifies $\lambda_\text{floor}$ two ways
that disagree by $6=3P$:
- **"wavelength $\sim$ horizon distance"** → $\lambda_\text{floor}=R_0=6c/H_0^{\text{obs}}$
  → $g_\dagger = c^2/R_0 = cH_0^{\text{obs}}/6$ (**fits** $a_0$).
- **"$\nu\sim H_0$"** → $\lambda_\text{floor}=c/H_0^{\text{obs}}=R_0/6$
  → $g_\dagger = cH_0^{\text{obs}}$ (**6× too big**).

These cannot both hold. The factor between them is exactly $R_0/(c/H_0)=6=3P$ — the same
horizon factor at issue throughout. T14 currently asserts both (lines ~44–47:
"$R_0=6c_0/H_0$... frequency $\sim H_0/6$... horizon-wavelength mode has $\nu\sim H_0$").
The internal tension was harmless until the coefficient became load-bearing; it is now
exposed.

---

## 4. Honest Status of $a_0$

- The RAR **shape** remains derived (prior session, kinetic closure) — unaffected.
- The RAR **scale coefficient** is **not** derived. The gradient route gives $cH_0/2$
  (wrong by 2.8×); the saturation route gives $cH_0/6$ **only if** $\lambda_\text{floor}=R_0$
  is adopted over $\nu=H_0$. That adoption is currently unjustified, and T14 contains both.
- $cH_0/6$ still *fits* the data well (prior session's numerics stand). What is missing is a
  reason to prefer $\lambda_\text{floor}=R_0$. So: **fits, not predicts**, pending resolution
  of the wavelength definition.

---

## 5. Suggested Document Edits (on merge)

- **T14 §"Energy Scale: The Minimal Quantum"** — flag and resolve the
  $\lambda_\text{floor}=R_0$ vs $\nu=H_0$ inconsistency. Decide which is primitive. If
  $\nu=H_0^{\text{hor}}$ (horizon rate, not observable), then $\lambda=c/H_0^{\text{hor}}
  =R_0/3$, giving yet a third value $g_\dagger=3c^2/R_0$ — so the resolution must be stated
  carefully in terms of which Hubble rate and which length.
- **T14 §"Toward the RAR"** — replace the "$g_\dagger=c^2/R_0=cH_0/6$, derived" framing
  (from the prior update, if already merged) with: "the gradient picture gives
  $g_\dagger=\dot c=cH_0/2$ (overshoots); $g_\dagger$ is better understood as a saturation
  scale $c^2/\lambda_\text{floor}$; the value $cH_0/6$ requires $\lambda_\text{floor}=R_0$,
  which depends on resolving the energy-scale inconsistency above. Coefficient OPEN."
- **Core Principles §7** — REVERT the RAR line from "scale coefficient derived: $cH_0/6$" (if
  the prior update was merged) back to "**scale coefficient open**: shape derived; the
  gradient route gives $cH_0/2$, a saturation-scale route gives $cH_0/6$ contingent on the
  connecton floor-wavelength definition, which is internally ambiguous in T14 (factor $3P$)."
- **Prior update `UPDATE_T14_a0_Coefficient_Horizon.md`** — mark as **superseded** by this
  one: its central claim (coefficient derived as 6) does not survive the background-density
  check. Its *corrections* to the old $2\pi$ and the $\dot c$/gradient distinction remain
  valid and useful; its *derivation* of the coefficient does not.

---

## 6. What Would Actually Close It

Resolve the connecton floor wavelength from first principles:
1. State whether the minimal-quantum frequency is $H_0^{\text{obs}}$ or $H_0^{\text{hor}}$,
   and whether the relevant length is the horizon radius $R_0$, the Hubble length
   $c/H_0^{\text{obs}}$, or $R_0/3$.
2. Each choice gives a definite coefficient ($cH_0/6$, $cH_0$, or $cH_0/2$ respectively).
   Only one can match $a_0\approx cH_0/6$. The task is to *derive* which length is the
   physical fluctuation floor a mass-induced perturbation competes against — not to pick the
   one that fits.
3. Until then, $a_0=cH_0/6$ is a well-fitting hypothesis, not a derived prediction.

This is a more honest place to leave it than the prior session's "derived, one contingency."
