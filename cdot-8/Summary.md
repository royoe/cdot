# Summary — cdot-8: A Covariant Completion of cdot-7 on an AeST Chassis

*A results-oriented overview, written to stand on its own. For the
session-by-session derivation history see `Progress.md` and the
per-work-package `Update-*.md` files; for the theory as it currently
stands, `Foundation.md`. Prepared 2026-07-21.*

---

## 1. What cdot-8 is

cdot-7 is an independent, variable-speed-of-light ($c(t)$) Machian
cosmology: a Newtonian-scope framework in which the enclosed mass within
an observer's cosmological horizon, the horizon's own radius, and the
value of $c$ are all mutually, self-consistently determined, and in
which late-time acceleration and a MOND-like weak-field law both emerge
from that same closure rather than being added by hand (a cosmological
constant, dark matter). It has an established, working four-term fit to
supernova, weak-lensing, and mass-census data, and is the sole framework
in data-contact use.

cdot-8 is **not a supersession** of cdot-7. It is a **completion
program**: an attempt to build a fully, generally covariant theory whose
preferred-frame, weak-field limit reproduces cdot-7's own closure,
fitted phenomenology, and portal relation *exactly*, while adding
relativistic-level structure (gravitational lensing, PPN parameters,
gravitational-wave speed, CMB/matter-power perturbation theory) that
cdot-7's Newtonian scope cannot address at all. Two honest outcomes were
built into the program from the start: success (cdot-8 absorbs cdot-7 as
a limit) or a stated kill condition firing (cdot-7 stands unaffected,
the negative result is simply recorded). Nothing in cdot-8 is citable
inside cdot-7 except as "proposed," and cdot-7's own files have never
been edited from cdot-8 work — anything bearing on cdot-7 itself is
routed through a separate consolidation log instead.

As of this writing, no kill condition has fired. The program has passed
its first three, hardest work packages (the dictionary, the covariant
census, and the closure constraint — this last one make-or-break by
design) and is midway through the fourth (relativistic weak-field/PPN)
and seventh (cosmological perturbations), with one open background-level
tension (Gate 1(b)) and one newly-found, paused perturbation-theory
tension (Gate 4) carried as standing caveats on everything downstream.

## 2. The chassis, and what had to be replaced

cdot-8 borrows its field content wholesale from **AeST** (Aether-Scalar-
Tensor theory; Skordis & Złośnik, *PRL* 127, 161302 (2021)): a metric
$g_{\mu\nu}$, a unit-timelike aether vector $A_\mu$ (enforced by a
Lagrange multiplier $\lambda$), and a shift-symmetric scalar $\phi$, with
action
$$S=\int d^4x\,\frac{\sqrt{-g}}{16\pi\tilde G}\Big[R-\frac{\mathcal K_B}2
\hat F^{\mu\nu}\hat F_{\mu\nu}+2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi
-(2-\mathcal K_B)\mathcal Y-\mathcal F(\mathcal Y,\mathcal Q)
-\lambda(A^\mu A_\mu+1)\Big]+S_m[g].$$
Matter couples to $g_{\mu\nu}$ alone (no disformal metric, unlike
TeVeS), which is what makes the equivalence principle and $c_\text{gw}=
c_\gamma$ (GW170817's decisive post-2017 constraint) automatic rather
than tuned. AeST's quasistatic weak-field limit independently reproduces
AQUAL/MOND phenomenology with correct lensing ($\Psi=\Phi$).

**What AeST does *not* supply, and cdot-8 replaces wholesale, is AeST's
own cosmology.** AeST's free function $\mathcal K(\mathcal Q)$ is
normally *chosen* so its scalar's energy density dilutes like ordinary
dust — the scalar mimics cold dark matter, and AeST's own published CMB
fits are fits of that mimicking component. cdot-8's founding claim is
the opposite: no adjustable dark component, a closure whose only content
is baryons and neutrinos (the same census that already anchors cdot-7),
with late-time acceleration and structure growth sourced by an
*instability mechanism*, not a free function tuned to look like $\Lambda$
or CDM. Realizing this covariantly is what the rest of cdot-8's work
packages do.

## 3. The census/M5 mechanism — cdot-7's Machian closure, made covariant

This is the structural heart of cdot-8, and the piece most directly
comparable to cdot-7's own core idea (see §7 for the full comparison).

- **The covariant census** (WP2): using AeST's own aether-orthogonal
  projector $q_{\mu\nu}=g_{\mu\nu}+A_\mu A_\nu$ (already present in the
  action, not introduced ad hoc), define
  $$\mathcal N(t)\equiv\int_{\Sigma_t\cap\{\chi\le\chi_h(t)\}}
  \frac{\rho_{E,\text{coord}}}{E_P(t)}\sqrt q\,d^3x,\qquad
  E_P=\sqrt{\hbar c(t)^5/G},$$
  a dimensionless energy inventory over a comoving ball of coordinate
  radius $R_h(t)$ satisfying $\dot R_h=c(t)$ — the exact same horizon-
  growth law cdot-7 used, now derived as a foliation integral rather than
  assumed. In the homogeneous limit this reduces exactly to cdot-7's own
  $M_h(t)=\mathcal N(t)m_P(t)$.
- **The closure, M5** (WP3): a Lagrange-multiplier term in the action,
  $S_{M5}=\int dt\,\Lambda_M[\mathcal Q-q(\mathcal N_\text{tot})]$, ties
  the scalar's background rate $\mathcal Q\equiv A^\mu\nabla_\mu\phi$ to
  the census — the Machian statement that the scalar's own dynamics are
  fixed by how much "stuff" is inside the horizon, not free. This is
  cdot-7's own $a_0=\lambda\dot c$/horizon-binding closure, rebuilt as a
  genuine covariant constraint rather than a Newtonian-limit relation.
- **The output, not an input**: solving the resulting constraint fixes
  AeST's free function *by quadrature* —
  $F(\mathcal Q)=\mathcal Q^{2/3}\big[-5\!\int\mathcal Q'^{-2/3}
  \Omega_s\,ds'+C_2\big]$ — using only already-fixed cdot-7 numbers
  ($\Omega_\text{closure}=0.074$, the fitted expansion history). No new
  free function or constant is introduced anywhere in this step.

## 4. Results by work package (brief)

| WP | Result |
|---|---|
| WP0 | Full literature pass; no fatal AeST pathology found; binary-pulsar/Cassini gaps identified as leads |
| WP1 | $c(t)=c_0(a/a_0)^{2/3}$ **forced** by the redshift law, reproducing every one of cdot-7's kinematic exponents as one theorem; a two-clock (coordinate-time vs. matter-proper-time) dictionary resolves a latent tension |
| WP2 | The covariant census, §3 above — passed |
| WP3 | The closure, §3 above — passed, the program's make-or-break package |
| WP4a | CMB acoustic scale: $100\theta_*=1.326$ vs. Planck's $1.04109\pm0.00030$, a clean 27% overshoot, localized to the crossover-era $E(z)$ — **open**, ruled "provisional structural failure, not a kill" (Gate 1(b)) |
| WP4b | BBN: passes cleanly, $Y_p\approx0.243$ |
| WP5 | Weak field with evolving $a_0$: AQUAL recovered exactly, $\hat a_0(z)=\tfrac23\lambda c_0H(z)$ matches cdot-7's own fit; a genuine, zero-new-parameter lensing prediction registered; closed as delivered (no data confrontation attempted, by author's choice) |
| WP6 | Tensor speed exact; Cassini screening passes by orders of magnitude; PPN closed on a conservative envelope; **new open item**: a Solar-System quadrupole bound ($Q_2$) puts cdot-7's own preferred fit in $\sim21\sigma$ tension — a program-choice issue, not a census/core one, deferred (Gate 3) |
| WP7 | Perturbation theory — see §5–§6; **paused** (Gate 4) after a serious finding at the scales the central deliverable (ISW $\Delta C_\ell$) actually needs |

## 5. The scalar and vector sector, in detail

This section works through every symbol that appears in cdot-8's
perturbation-theory machinery, what it is in AeST's own terms, and what
it represents physically in the cosmology cdot-8 builds. The whole
system is imported directly from AeST's own founding paper (its linear
perturbation theory is not re-derived, only checked); what's genuinely
cdot-8-specific is (a) which background trajectory and $F(\mathcal Q)$
these equations are evaluated on, and (b) the M5 correction layered on
top (§5.6).

### 5.1 Background fields and their perturbations

| Symbol | AeST meaning | Cosmological role |
|---|---|---|
| $\phi$ | The shift-symmetric scalar field of the base action. Split as $\phi=\bar\phi+\varphi$ (background + perturbation). | Carries the "extra," non-metric gravitational content — the field whose dynamics, closed by M5, produce cdot-8's late-time acceleration/structure-growth mechanism. |
| $A_\mu$ | The unit-timelike aether vector, $A^\mu A_\mu=-1$. Perturbed in Newtonian gauge as $A_\mu=\{-1-\Psi,\,\nabla_i\alpha\}$ — i.e. its only dynamical perturbation is a single scalar potential $\alpha$ (a "vector" in the sense of the AeST field content, but a scalar mode under cosmological perturbation theory). | Defines the preferred foliation (M1's own mapping conjecture: this frame *is* cdot-7's coordinate frame). $\alpha$ is the aether's own velocity-potential-like perturbation. |
| $\mathcal Q\equiv A^\mu\nabla_\mu\phi$ | The scalar's rate of change along the aether's flow — the argument of the free function $\mathcal F(\mathcal Y,\mathcal Q)$. On the FRW background, $\mathcal Q=\dot{\bar\phi}$. | cdot-8's version of cdot-7's $\dot c$: the mapping conjecture M2 identifies $\dot c\leftrightarrow\mathcal Q_0$ on the background, so that $a_0=\lambda\dot c$ becomes a genuinely *derived* quantity, $\hat a_0(z)=\tfrac23\lambda c_0H(z)$, not a chosen parameter. Exactly $\mathcal Q\propto(1+z)^{5/3}$ on cdot-8's own trajectory. |
| $\mathcal Y\equiv q^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi$ | The scalar's gradient squared, projected orthogonal to the aether ($q_{\mu\nu}=g_{\mu\nu}+A_\mu A_\nu$). Vanishes on a homogeneous background. | Governs the scalar's spatial-gradient (MOND-regime) physics; not directly load-bearing for the *cosmological* perturbation sector, which lives entirely in $\mathcal Q$'s perturbations. |
| $\mathcal F(\mathcal Y,\mathcal Q)$, written $F(\mathcal Q)$ on the background ($\mathcal Y=0$) | AeST's one genuinely free function. In AeST's own native cosmology, chosen by hand to make the scalar mimic CDM. | **Wholesale replaced.** Fixed by the census/M5 quadrature (§3) — a *zero-freedom output* of cdot-8's own closure, using only already-established cdot-7 numbers. This single substitution is what makes cdot-8's cosmology structurally different from AeST's own, despite sharing every equation of motion. |
| $F_\mathcal Q\equiv dF/d\mathcal Q$ | The scalar's own "equation of state" slope. | Appears as the coefficient of the base action's bulk-current vector-field term ($-F_\mathcal QA^\mu$) — the term WP6's PPN derivation and WP7's sub-horizon field-side recovery both key off, at the *same* numerical value in both places, a nontrivial cross-check. |
| $F_{\mathcal{QQ}}\equiv d^2F/d\mathcal Q^2$ | The quadrature function's curvature at the background point $\mathcal Q_0$. | Appears independently in **four** separate places in cdot-8: the weak-field condensate mass ($\mu^2\propto F_{QQ}$, WP5), the SZ stability sign check, WP7's perturbed-Einstein-constraint coefficient, and — most importantly — the sign of the scalar's own cosmological effective mass (§5.5). One number, four unrelated load-bearing uses, with no new parameter introduced for any of them — a coherence signal the program treats as significant. Current value: $F_{QQ}(\mathcal Q_0,\text{today})\approx-0.169$ (corrected in 2026-07-20 from an earlier, artifact-contaminated $-0.696$). |
| $\mathcal K(\mathcal Q)\equiv-\tfrac12F(0,\mathcal Q)$ | The "toy"/background normalization AeST's own founding paper uses in its sculpted-FRW action, related to the full covariant $F$ by an exact factor of $-\tfrac12$ (confirmed directly against the primary source, including the compensating $8\pi\tilde G$-vs-$16\pi\tilde G$ prefactor difference between the two actions). | Purely a bookkeeping/normalization object — but getting the $\mathcal K$-vs-$F$ distinction right was load-bearing: two independent implementation attempts in this program used the *wrong* one of the two (bare $F_\mathcal Q$ instead of $-\tfrac12F_\mathcal Q$) in the vector-field perturbation equation, a bug only caught and fixed once this distinction was pinned down explicitly (WP7 Stage 2). |
| $\mathcal K_2\equiv-\tfrac14F_{QQ}(\mathcal Q_0)$ | The coefficient of $(\bar{\mathcal Q}-\mathcal Q_0)^2$ in $\mathcal K$'s own Taylor expansion — i.e. $F_{QQ}$ read in the founding paper's own normalization. | The same curvature as above, appearing under AeST's native notation; used as an independent cross-check of the $F_{QQ}$ value quoted throughout. |
| $\mathcal K_B$ | A dimensionless AeST parameter controlling the aether kinetic term's normalization (appears throughout as $2-\mathcal K_B$ and $\mathcal K_B$ coefficients). | Constrained (not derived) by PPN/binary-pulsar bounds to $\mathcal K_B\lesssim2.5\times10^{-6}$ (conservative envelope); every established cdot-8 result is checked to survive the $\mathcal K_B\to0$ limit smoothly, so this squeeze is not existential. |

### 5.2 The perturbation variables — vector sector

| Symbol | Definition | Meaning |
|---|---|---|
| $\alpha$ | The aether's own scalar perturbation, $A_\mu\supset\nabla_i\alpha$ (see §5.1). | The "vector-sector" perturbation proper — physically, a peculiar-velocity-potential-like degree of freedom for the aether fluid, distinct from the scalar field's own $\varphi$. |
| $\mathcal E_\alpha\equiv\dot\alpha+\Psi$ | A gauge-invariant combination of $\alpha$ and the metric potential $\Psi$ (analogous to how $\theta$ combines a velocity with a potential in ordinary fluid perturbation theory). | The aether's own "momentum"-type variable; together with $\alpha$, forms a genuinely dynamical 2-variable subsystem with its own evolution equation, sourced by $\chi$ and $d\mathcal K/d\mathcal Q$. |
| $\chi\equiv\varphi+\dot{\bar\phi}\,\alpha$ | A gauge-invariant combination of the scalar perturbation $\varphi$ and $\alpha$. | The combination that actually sources both the pressure perturbation $\Pi$ and $\mathcal E_\alpha$'s own evolution — the scalar and vector sectors are coupled through this single object, not independently. |
| $\gamma\equiv\dot\varphi-\dot{\bar\phi}\,\Psi$ | The gauge-invariant time-derivative of the scalar perturbation. | Feeds the effective density contrast $\delta$ (below) through the $c_\text{ad}^2$-weighted term. |

### 5.3 The perturbation variables — effective "fluid" description

AeST's own founding paper shows that, defined appropriately, the whole
scalar-vector sector can be written to look exactly like an ordinary GR
fluid species — obeying the *same* continuity and Euler equations as
baryons or photons — but with an unusual pressure term:

| Symbol | Definition | Meaning |
|---|---|---|
| $\delta$ | $\delta\equiv\dfrac{1+w}{\dot{\bar\phi}c_\text{ad}^2}\gamma+\dfrac1{8\pi\tilde Ga^2\bar\rho}\nabla^2\big[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi\big]$ | The scalar sector's *effective* density contrast — built entirely from the field variables $\gamma,\alpha,\mathcal E_\alpha$, not a separately-evolved quantity. This is $\Omega_s$'s own perturbation, i.e. the object whose clustering behavior (§5.5) sources structure growth. |
| $\theta$ | $\theta\equiv\varphi/\dot{\bar\phi}$ | The scalar sector's *effective* velocity divergence. |
| $\Pi$ | $\Pi=c_\text{ad}^2\delta-\dfrac{c_\text{ad}^2}{8\pi\tilde Ga^2\bar\rho}\nabla^2\big[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi\big]$ | The **nonstandard pressure contrast** — this is *not* a dark fluid in the usual sense: $\Pi$ doesn't close under $\delta,\theta$ alone, it depends on the vector-field perturbations $\alpha,\mathcal E_\alpha$ directly. This is the single quantity through which the vector sector feeds back into the scalar sector's own growth equation. |
| $w$ | Effective equation of state, $w\equiv p_s/\rho_s$, computed directly from the established background trajectory ($w=-\frac{1}{4.5}\,d\ln|\Omega_s|/ds-1$). | Diagnoses the scalar's own thermodynamic-like behavior: $w\approx0$ (dust-like) through the matter era, bending to $w\to-0.68$ today — the equation of state of the component actually driving late-time acceleration. |
| $c_\text{ad}^2$ | The *adiabatic* sound speed, $c_\text{ad}^2=w+(dw/ds)/(d\ln\rho_s/ds)$, built map-independently directly from $w(a),\rho_s(a)$ (cdot-8-specific — AeST's own native formula uses a structurally different $(\rho,P)(\mathcal Q)$ map that does not transplant). | **The single most consequential number in the whole perturbation sector.** Small and negative through the matter era ($\sim-0.01$ to $-0.04$), meaning the scalar behaves almost exactly like AeST's own dust-clustering criterion predicts — but the *sign* (negative) is what makes it a genuine **tachyonic/Jeans-class instability** rather than an inert, pressureless fluid: see §5.5. |
| $\Omega_s(a)$ | $\rho_s\equiv\tfrac12\mathcal QF_\mathcal Q-\tfrac13F\equiv\Omega_s(a)$ — "the invoice." | What the census-closed background (baryons + neutrinos alone) still needs, on top of that content, for AeST's own Friedmann equation to reproduce cdot-7's independently-fitted expansion history — a genuine, zero-knob *output*, not a fit. Dust-like in the matter era ($\Omega_s\approx0.26$–$0.33$), bending $\Lambda$-like today ($\Omega_s(0)=0.926$), and small and slightly negative in the radiation era (crossing exactly zero at $z\approx9640$ — a fluid-description artifact, not a physical singularity: the underlying field variables $\chi,\gamma,\alpha,\mathcal E_\alpha$ stay perfectly regular there, since $F,F_\mathcal Q,F_{QQ}$ are smooth functions of $\mathcal Q$ straight through the crossing). |

### 5.4 The M5 term in the perturbation sector

| Symbol | Meaning |
|---|---|
| $\Lambda_M(t)$ | M5's own Lagrange multiplier, identically equal (an established background identity, not an independent quantity) to $Na^3F_\mathcal Q(\mathcal Q)/16\pi\tilde G$. |
| $\mathcal N_\text{tot}$ | The total covariant census (§3), summed over species. |
| $q(\mathcal N_\text{tot})$ | The closure function tying $\mathcal Q$ to the census, $\mathcal Q=q(\mathcal N_\text{tot})$. |
| $\delta\mathcal N_i(k,t)=\bar{\mathcal N}_i(t)\,W(kR_h(t))\,[\delta_i(k,t)-3\Phi(k,t)]$ | The perturbed census, weighted by a spherical top-hat window in $k$-space. |
| $W(kR_h)$ | The window function ($\to1$ super-horizon, $\to0$ sub-horizon) controlling how strongly a given mode's perturbation is "seen" by the horizon-wide census integral. Because $R_h(t)$ (built from $\dot R_h=c(t)\to0$ in the deep past) grows far more slowly at early times than an ordinary particle horizon, essentially every observationally relevant mode is *fully coupled* through recombination and only exits (decouples) during the matter era — a genuinely cdot-8-specific structural feature, absent from ordinary $\Lambda$CDM-style horizon-crossing pictures. |

The scalar/vector **field equations themselves** ($\chi,\gamma,\alpha,
\mathcal E_\alpha$'s own evolution) are, remarkably, **exactly unmodified
by M5, at every $k$** — a base-action bulk-current term
($-F_\mathcal QA^\mu$) and an M5-sourced term ($+\Lambda_MA^\mu$) cancel
identically, since $\Lambda_M$'s own value is *defined* by the same
background identity above and carries no $k$-dependence (M5 is one
constraint per time-slice, not a local field). **M5's only effect on
the perturbation sector is a single additive term in the Einstein
constraint equation** (the Poisson-type equation for $\Phi$):
$$\delta G^0_0\supset8\pi G\Big[\frac{F_\mathcal Q}6+\frac{\mathcal Q
F_{\mathcal{QQ}}}2\Big]q'\,\bar{\mathcal N}_\text{tot}\,W(kR_h)\,
[\delta_\mathcal N-3\Phi]$$
— using, once again, the same $F_{\mathcal{QQ}}$ that already appears
in three other places in the program (§5.1).

### 5.5 The physical picture: what actually sources structure growth

Putting the pieces together: cdot-8's cosmology has **no cold dark
matter and no cosmological constant**. What plays their role is the
scalar-vector sector's own perturbation, $\delta$ (equivalently
$\Omega_s$'s own density contrast), clustering *dust-like* through the
matter era and *dominating* the energy budget at essentially every epoch
from recombination to today (40–90% of the total, unlike $\Lambda$CDM's
dark energy, which is negligible until $z\lesssim1$). The mechanism
making it cluster at all, rather than smoothly track the background, is
a genuine **tachyonic (negative-mass-squared) instability**: through the
matter era, $\mu_\text{eff}^2/H^2\approx-1.27f_s/(2-\mathcal K_B)\approx
-0.5$ — a Jeans-class growing mode, not a bug, flipping to the stable
sign only very near today ($z\approx0.13$–$0.15$). The same negative
$c_\text{ad}^2$ that produces this is, structurally, the source of
everything else described here — including, ultimately, the finding that
paused WP7 (§6).

### 5.6 The vector-sector instability — a hard-won structural finding

Building the actual coupled numerical system exposed a second, distinct
instability, this time in the **vector** ($\alpha,\mathcal E_\alpha$)
subsystem rather than the scalar one: for wavenumbers above a critical,
redshift-dependent threshold $\kappa_\text{crit}(z)$, the linearized
$(\alpha,\mathcal E_\alpha)$ system develops a genuine, large, positive
real eigenvalue — sourced entirely by the same negative $c_\text{ad}^2$
via the $\Pi$-feedback term in $\mathcal E_\alpha$'s own evolution
equation. This was fully diagnosed and safely closed *at one test
wavenumber* ($k=10^{-4}\,\text{Mpc}^{-1}$, where the instability resolves
by $z\approx20$–$30$ and can be handled by pointwise algebraic slaving of
the fast mode) — but assembling the actual ISW calculation revealed that
at the wavenumbers the CMB's low multipoles ($\ell=2$–$10$) actually
probe ($k\approx1.1$–$5.4\times10^{-3}\,\text{Mpc}^{-1}$), the same
instability **never resolves at all**, from $z=100$ all the way to
$z=0$ — confirmed in the exact, machine-precision-validated full system,
not an artifact of any approximation. Physically: a negative effective
pressure is *destabilizing* rather than restoring in the dispersion
relation, so — the reverse of ordinary Jeans behavior — smaller scales
(larger $k$) are *more* unstable, not less. This is read as the *same*
mechanism behind §5.5's accepted clustering, now shown to have a much
larger reach than anyone had reason to check before Stage 4 forced the
question — not an unrelated new pathology, but a serious one regardless:
$\Phi$ growing five to eight orders of magnitude between recombination
and today is nowhere near the observed, mild ISW effect. **This finding
paused WP7's ISW/growth track** (Gate 4, 2026-07-21) rather than being
patched or pushed through; it stands, unresolved, as a second
independent open structural question alongside Gate 1(b)'s background
tension.

## 6. Current status

| Item | Status |
|---|---|
| Gate 1(b) — WP4a's 27% $\theta_*$ miss | Open. Ruled "provisional structural failure, not a kill"; revisit deferred until after WP7. |
| Gate 2 — WP5's data-confrontation scope | Resolved: closed as delivered, no further data-processing work. |
| Gate 3 — the $Q_2$/EFE tension | Open, deferred until after WP7 (same logic as Gate 1(b)). cdot-7's own preferred fit is $\sim21\sigma$ in tension with a 2026 Solar-System quadrupole bound. |
| Gate 4 — WP7's ISW/growth track | **Paused, 2026-07-21.** The vector-sector instability described in §5.6 does not resolve at the wavenumbers the central deliverable needs. Not a kill; effort redirected elsewhere pending a considered view on how to weigh this alongside Gate 1(b). |
| WP7's $\Omega_s$-clusters-dust-like conclusion | Settled, load-bearing, unaffected by Gate 4. |
| Zero-adjustable-parameters claim | Intact throughout — every new number introduced by WP1–WP7 traces to already-fixed cdot-7 quantities or the census; no new free function or constant anywhere. |

## 7. Connection to earlier cdot iterations — the horizon, before and after covariance

The single idea that survives, essentially unchanged in spirit, from
cdot-7 through every later cdot-8 work package is this: **the observable
universe's own horizon is not a passive boundary but an active,
Machian participant in the dynamics** — what's inside it, and how fast
it's growing, feeds back into the physics happening at every point
inside it. cdot-7 built this concept directly, without covariance:

$$\dot R_h=c(t),\qquad c^2=\kappa\,g_hR_h,\qquad g_h\equiv c^2/R_h,$$

with $g_h$ the horizon's own AQUAL-modified binding acceleration and
$R_h$ the horizon radius growing at the local light speed since genesis.
This is a two-dimensional dynamical system for $(R_h,c)$, not an
algebraic relation — and its single most important feature is that the
scale-free fixed point of this system is **unstable**. cdot-7's entire
account of late-time cosmic acceleration is that instability, not a
cosmological constant: deviations from the fixed-point trajectory are
negligible in the past and grow at late times, exactly $\Lambda$'s
phenomenology, produced by a genuine dynamical runaway in the
horizon/light-speed system rather than a constant term in the action.
The enclosed mass driving $g_h$ is, in turn, a **Planck-unit census** —
a dimensionless count of everything (matter, radiation, eventually
neutrinos) inside $R_h$, measured against the *instantaneous* Planck
mass/energy, which is what makes the whole construction genuinely
Machian rather than merely geometric.

cdot-8 inherits every piece of this, but rebuilds each one as a
genuinely covariant object rather than a preferred-frame construction:

- **The horizon itself** ($\dot R_h=c(t)$) survives *unchanged* as a
  literal equation — but is now *derived*, not assumed: WP2 shows it
  falls directly out of AeST's own $q_{\mu\nu}=g_{\mu\nu}+A_\mu A_\nu$
  foliation structure, already present in the base action for unrelated
  reasons (building the $\mathcal Y$ invariant), rather than being
  posited as a new physical hypothesis.
- **The Planck-unit census** ($\mathcal N(t)$) survives as a foliation
  integral over the same comoving ball, now built from AeST's own
  aether-orthogonal projector rather than a flat-space particle count —
  and reduces to cdot-7's own $M_h(t)=\mathcal N(t)m_P(t)$ exactly in the
  homogeneous limit, the correct kind of check (a relativistic ADM-type
  quantity collapsing to the already-known Newtonian one, not a
  coincidence).
- **The Machian closure** ($c^2=\kappa g_hR_h$, tying the horizon's
  binding acceleration to $\dot c$ via $a_0=\lambda\dot c$) survives as
  M5: a genuinely covariant Lagrange-multiplier constraint in the action
  itself, $S_{M5}=\int dt\,\Lambda_M[\mathcal Q-q(\mathcal N_\text{tot})]$,
  replacing the old algebraic/ODE relation between $c$, $g_h$, and $R_h$
  with a field-theoretic one between $\mathcal Q$ (the scalar's own rate
  of change — $\dot c$'s covariant counterpart, M2) and the census. Where
  cdot-7 had to *posit* the specific form $c^2=\kappa g_hR_h$ (rejecting,
  on stated grounds, an alternative built from the AQUAL potential
  directly), cdot-8's version has its functional form — $F(\mathcal Q)$
  — **derived by quadrature** from the closure condition alone, with
  zero remaining freedom.
- **The unstable-fixed-point acceleration mechanism** survives as
  $\Omega_s$'s own tachyonic clustering instability (§5.5): both are, at
  bottom, the statement that a Machian, horizon-tied quantity has an
  unstable direction whose growth *is* late-time acceleration, rather
  than acceleration being sourced by an inert constant or a separately
  fitted dark component. cdot-7's version lives in the *background*
  dynamical system $(R_h,c)$; cdot-8's lives in the *perturbations* of a
  covariant scalar field sourced by the same census — a genuine
  generalization, not merely a re-derivation, since it now makes
  falsifiable predictions (a growth history, an ISW signature) that the
  background-only picture never could.

**What going covariant exposed, and could not have been found any other
way**: cdot-7's horizon/instability mechanism was only ever checked
against the *background* expansion history and, indirectly, against
weak-field/local phenomenology. It was never possible, within cdot-7's
own Newtonian scope, to ask how this mechanism behaves as a genuine field
perturbation at a specific comoving wavenumber $k$ — because cdot-7 has
no perturbation theory at all. cdot-8's covariant completion is precisely
what makes that question askable, and §5.6's finding is the answer:
*the same instability that correctly produces late-time acceleration in
the background, and correctly clusters structure in the matter era,
turns out to grow without bound, at every redshift, for the specific
range of scales the CMB's lowest multipoles are sensitive to.* This is
not a failure of the covariant program as such — it is exactly the kind
of question a genuinely covariant, perturbation-theory-capable
completion of cdot-7's own core idea was built to be able to ask, and it
has surfaced a real, previously invisible tension between the mechanism
that makes cdot-7 work at the background level and the observations a
full theory must also match at the level of structure. Gate 4 keeps this
open, honestly, rather than resolving it either way — the shared
horizon/census architecture is what makes cdot-7 and cdot-8 the same
research program at bottom, and it is also, now, the specific place
where that program's furthest-developed instantiation has hit its
hardest and most consequential open question to date.
