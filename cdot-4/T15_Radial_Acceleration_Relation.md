# T15 — The Radial Acceleration Relation (RAR)

*Note: the RAR, MOND scale (T6), and rotation curves (T5) are related but now at different stages. The retardation mechanism of T5 is dead ($\sim10^6$ shortfall); it is not a precondition for the connecton route. The RAR closure is substantially derived from the connecton program (T14) — see §"Status in This Model" below. The T5 rotation-curve order-of-magnitude problem and the empirical RAR stand at different levels of description; progress on the RAR is no longer gated on T5.*

---

## Observational Background

The **Radial Acceleration Relation** (McGaugh, Lelli, Schombert 2016) is the sharpest,
most theory-neutral statement of the rotation-curve anomaly. It is derived from
$\sim150$ galaxies spanning five decades in baryonic mass, covering spirals,
ellipticals, dwarfs, and low-surface-brightness galaxies.

The relation states: the observed centripetal gravitational acceleration $g_\text{obs}$
(inferred from rotation curves or velocity dispersions) is a **tight one-parameter
function** of the baryonic Newtonian prediction $g_\text{bar}$ (computed from the
observed stellar and gas mass only):
$$g_\text{obs} = \frac{g_\text{bar}}{1 - e^{-\sqrt{g_\text{bar}/g_\dagger}}},$$
with a single universal scale:
$$g_\dagger \approx 1.2\times10^{-10}\ \text{m/s}^2.$$

Key features:
- **Scatter:** $\sim0.13$ dex (residual scatter after fitting one parameter). This is
  as tight as observational errors allow.
- **No residual dependence** on galaxy size, morphology, surface brightness, or
  environment — only baryonic acceleration enters.
- **Two limiting regimes:**
  - $g_\text{bar} \gg g_\dagger$ (Newtonian): $g_\text{obs} \to g_\text{bar}$.
  - $g_\text{bar} \ll g_\dagger$ (deep MOND): $g_\text{obs} \to
    \sqrt{g_\text{bar}\,g_\dagger}$, which gives flat rotation curves and the
    Baryonic Tully-Fisher Relation $v^4 = GM\,g_\dagger$ (T6).

The BTFR (T6) is the deep-MOND limit of the RAR. The RAR is the more general,
two-regime statement; it is the most theoretically demanding form of the challenge.

---

## Dimensional Match: The Scale $g_\dagger \sim cH_0$

The MOND acceleration scale $g_\dagger$ is numerically:
$$g_\dagger = \frac{c^2}{R_0} = \frac{cH_0^{\text{obs}}}{6} \approx 1.2\times10^{-10}\ \text{m/s}^2,$$
using $R_0=6c/H_0^{\text{obs}}$ (Core Principles §4a). The coefficient $6=3P$ is derived from the horizon radius, not a numerical near-miss (T6, T14). In the connecton picture (T14), $g_\dagger=c^2/R_0$ is identified as the sea's kinematic acceleration — the coefficient is fixed by horizon geometry. The MOND scale tracks $H_0^{\text{obs}}$, not $\dot{c}/c = H_0^{\text{hor}} = H_0^{\text{obs}}/P$ — the two differ by $P=2$, so $g_\dagger\neq\dot{c}$.

**Caveat on the match:** $cH_0$ is the *only* acceleration that can be formed from
the two characteristic quantities of the model ($c$ and $H_0$). So the scale match
is dimensionally inevitable — shared by MOND, every cosmologically motivated proposal,
and any model that generates an acceleration from the Hubble constant. It is a
necessary condition, not a distinctive prediction.

---

## Status in This Model

Three honest levels:

**1. Scale.** $g_\dagger \sim cH_0$ — robust, inevitable. The model knows the scale.

**2. Mechanism.** The $\dot{c}/c$ retardation route is **dead** (T5): it is
distance-keyed, not acceleration-keyed, and fails by $10^3$–$10^6$ at galactic scales
regardless of the counting law. The RAR's transition is keyed to local acceleration
crossing $g_\dagger$ — retardation-type effects are structurally ruled out by this
diagnostic alone.

The **connecton foam-sea** (T14) is the leading mechanism and has substantially derived the RAR:
- It gives Newtonian $1/r$ via diffusion through quantum foam — not distance-keyed.
- The acceleration floor $g_\dagger=c^2/R_0=cH_0/6$ is derived from the horizon radius (not a background gradient — the homogeneous isotropic sea has no net directional gradient; T14).
- The sea density is a holographic standing population $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ ($\hbar$-free; T14) — a standalone structural result linking the sea to dark energy, not the source of $g_\dagger$ (which is kinematic: $c^2/R_0$).

The **RAR closure is derived** from connecton indistinguishability — the constitutive law $D(g)=g/(g+g_\dagger)$ (MOND's "simple" interpolation) follows from excess connectons relaxing against the total ambient population. The old functional-form wall (Bekenstein-Milgrom $D\propto|\nabla\rho|$) is bypassed — the closure is derived directly from the indistinguishability premise already in T14.

**3. Structural diagnostic (the useful constraint).** Because the RAR is
acceleration-keyed, any viable mechanism must be acceleration-keyed. Retardation,
any light-travel-time or distance-ratio correction, and any purely Newtonian
additive term that is linear in $M$ are all ruled out structurally — regardless of
coefficient. A nonlinear source coupling ($\sqrt{M}$ for Tully-Fisher) is required.

---

## The $\sqrt{M}$ Requirement

The deep-MOND regime of the RAR gives $g_\text{obs} = \sqrt{g_\text{bar}\,g_\dagger}$.
For a circular orbit this is $v^2/r = \sqrt{GM/r^2 \cdot g_\dagger}$, giving:
$$g_\text{MOND} \propto \frac{\sqrt{M}}{r}.$$
This $\sqrt{M}$ dependence (in contrast to Newton's $M/r^2$) is MOND's irreducible
nonlinear signature. The BTFR $v^4 = GM\,g_\dagger$ follows directly.

Any *direct-source* mechanism linear in $M$ — retardation terms, linear diffusion, additive GEM fields — gives $M/r$ and the wrong Tully-Fisher slope $v^4\propto M^2$. The resolution (T14): the quarter power emerges from where the surviving population sits ($r_t\propto\sqrt{M}$), not from the source coupling. The field equations remain linear; the nonlinearity is in the attractor geometry. The RAR closure then follows from connecton indistinguishability. See T14 for the derivation; criticality-as-license is superseded.

---

## Relationship to T6 (MOND $a_0$) and T5 (Rotation Curves)

The three problems are related but now at different stages:
- **T6/T14:** $g_\dagger=c^2/R_0=cH_0/6$ from horizon kinematics (6 from $R_0=6c/H_0$); $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ a standalone $\hbar$-free identity. **Substantially derived.** Open: force-law derivation of kinematic identification.
- **T15 (RAR functional form):** closure derived from connecton indistinguishability (T14); 0.020 dex vs McGaugh. **Substantially derived.**
- **T5 (rotation curves, order-of-magnitude):** the retardation mechanism is dead ($\sim10^6$ shortfall). The connecton route advances the RAR independently; the T5 order-of-magnitude problem (does the Lorentz filter produce order-unity flat curves?) remains open as the attractor-convergence question.

These are no longer gated on each other via the retardation route. Progress on T15/T6 via the connecton program is independent of the T5 retardation failure.

---

## Observational Discriminant: Epoch Dependence

If $g_\dagger \sim c(t)H_0^{\text{obs}}(t)$, the MOND scale should vary with cosmic
epoch. In this model, $H_0^{\text{obs}}(z) = H_0^{\text{obs}}/(1+z)^{1/3}$ (from the
horizon ODE: $H^{\text{hor}} = 3kR^2 \propto c^{2/3} \propto (1+z)^{-1/3}$), so:
$$g_\dagger(z) \propto c(z)\,H^{\text{obs}}(z) \propto
\frac{1}{(1+z)^{1/2}}\cdot\frac{1}{(1+z)^{1/3}} = \frac{1}{(1+z)^{5/6}}.$$
Since $(1+z)^{5/6} > 1$ for $z > 0$, $g_\dagger(z) < g_\dagger(0)$: the MOND threshold
was **smaller in the past** and grows over cosmic time. Galaxy rotation curves at
high $z$ should show a **lower** MOND threshold acceleration — the MOND-like regime
would kick in at smaller $g_\text{bar}$, making a larger fraction of the disk
dynamically MOND-like at high $z$. This is observationally testable in principle
(high-$z$ kinematic surveys), though current data are sparse.

---

## Open Questions

- **Force-law derivation of $g_\dagger$:** $g_\dagger=c^2/R_0=cH_0/6$ is identified kinematically (sea's crossing acceleration; the 6 from $R_0=6c/H_0$). The open task is to derive $g_\dagger=c^2/R_0$ from the connecton equations of motion (T14 §Open Items).
- **Transport kernel:** The RAR closure is derived from a relaxation-time ansatz; replacing it with a full Boltzmann derivation is the deepening task (T14).
- **Attractor convergence:** Does the Lorentz filter genuinely concentrate the surviving population at $r_t$ at all radii? Dynamical-systems proof is the binding open item (T14, T17).
- **Epoch dependence:** Does $g_\dagger\propto c(t)H_0(t)$ vary with cosmic epoch? In this model $g_\dagger(z)\propto(1+z)^{-5/6}$ — a lower MOND threshold in the past, giving a larger fraction of high-$z$ disks in the MOND-like regime. Testable with JWST/IFU kinematic surveys.
- **RAR scatter:** Can the observed 0.13 dex scatter be predicted from the coherence-factor $f=v_\text{rot}/\sigma$ variation across bulges (T17)? The model predicts environmental and morphological residuals; pure MOND predicts zero.
