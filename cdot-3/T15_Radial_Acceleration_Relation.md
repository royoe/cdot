# T15 — The Radial Acceleration Relation (RAR)

*Note: this problem stands or falls together with T5 (rotation curves) and T6 (MOND
acceleration scale). The $\sim10^{-6}$ order problem of T5 must be solved before
any further work on the RAR, MOND ($a_0$, T6), or rotation curves — these three are
the same open problem at different levels of description.*

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
$$g_\dagger \approx \frac{cH_0}{2\pi} \approx \frac{cH_0}{6} \approx 1.2\times10^{-10}
\ \text{m/s}^2,$$
using $H_0 = 70$ km/s/Mpc. This cosmological–galactic connection has been noted since
Milgrom (1983). In this model, $cH_0 = \dot{c}_0$ is a natural acceleration (the rate of change of
$c$). This follows directly from the counting rule $H_0 = \dot{c}/c$ (T3, T12), which
makes $H_0$ the fractional growth rate of $c$ and $cH_0$ the absolute rate — so the
dimensional match is structurally built in.

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

The **connecton foam-sea** (T14) is the current best candidate:
- It gives Newtonian $1/r$ via diffusion through quantum foam.
- It is not distance-keyed (steady-state diffusion profile, no $d/(c/H_0)$
  suppression).
- The background gradient $|\nabla\rho_\text{bg}| \sim \rho_\text{bg}H_0/c$ provides
  a mass-independent transition scale $\sim cH_0$ — the right structure.

But the **functional form is the wall** (T14, caveat 2): reproducing the RAR
interpolating function requires $D \propto |\nabla\rho|$ (Bekenstein-Milgrom), which
has no independent motivation and is disfavored by the natural linear reading.

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

Any mechanism linear in $M$ — retardation terms, linear diffusion, additive GEM
fields — gives $M/r$ and the wrong Tully-Fisher slope $v^4 \propto M^2$. A
**nonlinear source coupling** is required. See T6 for the diagnosis of why every
natural mechanism fails this test, and T14 for the GEM-specific analysis and the
live candidate directions (Lorentz-form $v\times B_c$ and criticality-as-license).

---

## Relationship to OP-2 (MOND $a_0$) and T5 (Rotation Curves)

The three problems are one:
- **OP-2/T6:** derive $a_0 \sim cH_0$ with the correct $1/(2\pi)$ coefficient.
- **OP-3/T5:** produce order-unity flat rotation curves at galactic radii without dark
  matter.
- **OP-17/T15:** reproduce the RAR functional form across all galaxy types.

Solving any one requires solving all three. The blocker common to all is the
$\sim10^{-6}$ order problem of T5 (retardation too small) plus the $\sqrt{M}$
nonlinearity problem (functional form). Do not pursue OP-2 or the RAR in isolation
until a viable acceleration-keyed, order-unity galactic mechanism exists.

---

## Observational Discriminant: Epoch Dependence

If $g_\dagger \sim c(t)H(t)$, the MOND scale should vary with cosmic epoch. At
redshift $z$, using the model's $c(t)$ and $H(t)$:
$$g_\dagger(z) \sim c(z)\,H(z) \propto \frac{c_0\,H_0}{(1+z)^{1/2}\,(1+z)^{1/3}}
= \frac{c_0 H_0}{(1+z)^{5/6}},$$
i.e. $g_\dagger$ was larger in the past — galaxy rotation curves at high $z$ should
show a higher MOND threshold acceleration. This is observationally testable in
principle (high-$z$ kinematic surveys), though current data are sparse.

---

## Open Questions

- Can the connecton foam-sea (T14) produce the RAR functional form — specifically the
  $\sqrt{g_\text{bar}\,g_\dagger}$ deep-MOND regime — through a nonlinear diffusion
  or Lorentz-type $v\times B_c$ coupling?
- Is the $1/(2\pi)$ coefficient of $g_\dagger = cH_0/(2\pi)$ derivable from the
  geometry of horizon counting (sphere surface), a quantum phase, or the closure
  condition $V=c$ (T14)?
- Does $g_\dagger$ vary with cosmic epoch as predicted? Upcoming high-$z$ IFU surveys
  (e.g. JWST kinematic data) may constrain this.
- Can the scatter in the RAR ($\sim0.13$ dex) be accounted for by local variations in
  the connecton-sea background gradient (due to overdensities, filaments, or cluster
  environments)? If so, the model predicts small but systematic environmental
  residuals — distinct from MOND, which predicts zero environmental dependence.
