# Update — WP2: The Covariant Census

*Companion: `SessionLog-2026-07-12.md` (this directory). Executes Proposal §6 WP2:
"Define $\mathcal N$ on $\Sigma_t$; well-posedness; evolution equation; recover the
$dr/ds$ system in the symmetric sector." No kill condition is stated for WP2 in the
proposal (only WP0, WP1, WP3 carry explicit kill conditions) — this pass is assessed
against its four listed success items directly. Builds on WP1's established
$c(t)=c_0(a(t)/a_0)^{2/3}$ dictionary; the literal `dr/ds` system was located and
quoted verbatim from `cdot-7/Radiation-1/census_closure.py` and `ResearchNotes.md`
§(radiation-era), not inferred from notation guesswork.*

**Scope, as the proposal itself states it**: "in the symmetric sector." This pass
checks the homogeneous (FRW) background only — inhomogeneous well-posedness (Cauchy
development, aether caustics) is perturbation-theory territory, explicitly WP7's job,
not this one's.

---

## 1. The foliation integral

Define, on the aether-orthogonal slice $\Sigma_t$ (WP1/M1: the AeST FRW comoving
spatial section at cosmic time $t$), using AeST's **own** aether-orthogonal projector
$q_{\mu\nu}=g_{\mu\nu}+A_\mu A_\nu$ — the identical object the AeST action already uses
to build the scalar invariant $Y=q^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi$ (WP0
extraction, arXiv:2007.00082 eq. 5) — the census as a genuine covariant integral:
$$\mathcal N(t)\ \equiv\ \int_{\Sigma_t\cap\{\chi\le\chi_h(t)\}}
\frac{\rho_{E,\text{coord}}(x,t)}{E_P(t)}\,\sqrt{q}\,d^3x,$$
with $\rho_{E,\text{coord}}$ the coordinate-frame energy density (WP1's bookkeeping
convention), $E_P(t)=\sqrt{\hbar c(t)^5/G}$, and the integration region a comoving ball
of coordinate radius $R_h(t)\equiv a_0\chi_h(t)$ satisfying $\dot R_h=c(t)$ — cdot-7's
own definitional horizon relation (Foundation §2.1), now written as a genuine integral
of the WP1-established $c(t)=c_0(a(t)/a_0)^{2/3}$: $R_h(t)=c_0a_0^{-2/3}\int^t
a(t')^{2/3}dt'$.

**This is the concrete cash-out of the proposal's own M1 observation** ("the aether
frame supplies exactly the simultaneity slicing the census integral needs... the
census was always a foliation-dependent object; AeST provides the foliation as a
field") — not merely restated here but *identified*: $q_{\mu\nu}$ is not a new object
introduced for the census, it is AeST's own $Y$-invariant's projector, already present
in the action before cdot-8 touched anything.

In the homogeneous sector, $\rho_{E,\text{coord}}(x,t)=\rho_{E,\text{coord}}(t)$ and the
integral collapses to $\mathcal N(t)=[\rho_{E,\text{coord}}(t)/E_P(t)]\cdot(4\pi/3)
R_h(t)^3$ — **by construction, this reduces exactly to cdot-7's own $M_h(t)=\mathcal
N(t)m_P(t)$** (Foundation §2.1). This reduction is not circular reasoning disguised as
a result: it is the correct and required check that a covariant definition, built from
AeST's own geometric objects, actually reproduces the already-fitted empirical layer
(K4/G4) in the preferred-frame limit — precisely as ADM mass is defined as a surface
integral and *checked* to reduce to the Newtonian mass, not merely asserted to.

---

## 2. The evolution equation — genuinely new content

cdot-7 never wrote down $\dot{\mathcal N}$; it used $\mathcal N$ (equivalently $M_h$)
only algebraically, as an input to the AQUAL closure. Differentiating §1's homogeneous
form directly, with $\rho_{E,\text{coord}}(t)=\rho_{E,0}(c/c_0)^p$ for a species of
coordinate-energy-density exponent $p$ (WP1 §5) and $E_P(t)\propto c(t)^{5/2}$:
$$\boxed{\ \frac{\dot{\mathcal N}}{\mathcal N}=\left(p-\frac52\right)\frac{\dot c}{c}
+\frac{3c}{R_h}\ }$$
Two terms, cleanly separated: a **weight-drift** term (how a single already-enclosed
entity's own census weight changes) and a **shell-sweep** term (new comoving entities
entering as the horizon grows, $3\dot R_h/R_h=3c/R_h$ — a direct check: differentiating
a fixed comoving number density's contained count, $n_\text{com}\cdot\frac{4\pi}3R_h^3$,
gives exactly this $3c/R_h$ rate, confirming the decomposition independently of the
census-weight bookkeeping).

**Matter ($p=5/2$): the weight-drift term vanishes identically.** $\dot{\mathcal
N}/\mathcal N=3c/R_h$ only — matter's census count grows *purely* by sweeping up
already-fixed-weight entities, with zero internal drift. This is not a new assumption;
it is the derived content of cdot-7's own stated claim that a massive particle's census
weight is "epoch-invariant by premise 3" (Foundation §2.1) — now shown to mean,
specifically, *no source term in $\mathcal N$'s evolution beyond horizon growth*, a
checkable statement the original formulation asserted but never wrote as an ODE.

**Radiation ($p=1$): a genuine, nonzero weight-drift, $-\tfrac32(\dot c/c)$.** Each
already-enclosed photon's own census contribution *decays* as the bookkeeping Planck
energy $E_P(t)$ grows faster than the photon's own coordinate energy — exactly cdot-7's
stated $E_\gamma/E_P\propto c^{-3/2}$ "relative to matter's constant weight" (Foundation
§2.1), now derived as a rate rather than quoted as a ratio.

---

## 3. Recovering the $dr/ds$ system

The literal target, located verbatim (not inferred) in `cdot-7/Radiation-1/
census_closure.py` and `ResearchNotes.md`:
$$\mu(x)g_h=\frac{GM_h}{R_h^2},\quad g_h=\frac{c^2}{\kappa R_h},\quad a_0=\lambda\dot c,
\quad x=\frac{g_h}{a_0}\ \Longrightarrow\ \frac{dr}{ds}=\kappa\lambda\,x(r,s)\,r,$$
$$r\equiv\frac{R_h}{R_{h,0}},\ \ s\equiv\ln\frac{c}{c_0},\ \ x(r,s)=\mu^{-1}\!\Big(\mu(x_0)\,
r^2e^{-2s}S(s)\Big),\ \ S(s)\equiv\frac{\rho_\text{source}(c)}{\rho_\text{source,0}}.$$
With $M_h(t)=\mathcal N(t)m_P(t)$ (§1) and $\rho_\text{source}\equiv\rho_{E,\text{coord}}$
(the same object entering §1–2), $S(s)$ is exactly the coordinate energy-density ratio
already used in the existing, independently-validated code — **the system is recovered
identically, not approximately**, because $\mathcal N$ was constructed in §1
specifically to equal $M_h/m_P$ in this sector. **What this check actually establishes**
is narrower and more honest than "WP2 derives cdot-7's dynamics": the AQUAL closure
itself ($\mu(x)g_h=GM_h/R_h^2$, $a_0=\lambda\dot c$) is **taken as given here**, exactly
as it is cdot-7's own adopted premise 4 plus closure — WP2 does not derive it from
AeST's actual field equations. That re-derivation (recovering AQUAL as a genuine
weak-field limit of the AeST Lagrangian, rather than importing it as before) is WP5's
job; tying $\mathcal N$'s value to $Q_0(t)$ via the field equations themselves (rather
than via the *already-adopted* closure relation used here) is WP3's M5. **WP2's
contribution is the covariant definition of the object ($\mathcal N$) these later work
packages need, plus confirmation that it slots into the existing, validated system
without alteration.**

---

## 4. Well-posedness

**Convergence of the census integral, symmetric sector.** Given $R_h(t)$ finite, the
integral trivially converges (a bounded region, finite homogeneous density). $R_h(t)$'s
own convergence as $t\to$genesis is inherited entirely from whatever behavior $c(t)$
[equivalently $a(t)$] already has — this was checked, and is not new to WP2: cdot-7's
existing numerical work (`Fable-1/separatrix_check.py`, the fixed-point analysis)
already establishes the trajectory's past behavior for its *own* closure. WP2 adds
nothing here except noting the dependency explicitly.

**A genuine open item, flagged rather than resolved.** cdot-7's own fixed-point
trajectory ($R_h\propto c^{3/4}$) reaches genesis ($c\to0$) only as $t\to-\infty$ —
Foundation itself states this ("the backward attractor to $c\to0$ as $w\to\infty$"),
an eternal, non-singular past, not a finite-time Big Bang. Given WP1's identification
$c\propto a^{2/3}$, this *requires* AeST's own sourced $a(t)$ to share this eternal-past
structure if cdot-7's phenomenology is to be reproduced (K4/G4). **This is not
necessarily a red flag**: cdot-7's closure sits permanently in AQUAL's transition
regime ($x=O(1)$ at both the matter and radiation fixed points, "squarely in AQUAL's
transition zone, not deep-Newtonian," Foundation §2.4) rather than ever passing through
an ordinary Newtonian/GR phase — the standard FRW singularity theorems assume ordinary
GR dynamics and reasonable energy conditions, neither of which need hold in a
permanently MOND-modified background, so a non-singular past is a plausible, not an
alarming, feature. **But it is unconfirmed**: WP2 cannot check it, since checking
requires AeST's actual sourced Friedmann equation under the closure constraint — WP3
and WP4's territory. **Recommend this be WP3/4's first numerical check**, ahead of
reproducing the fixed-point numbers themselves: does the census-closed AeST background
actually admit an eternal, $c\to0$-only-as-$t\to-\infty$ past, or does it hit an
ordinary finite-time singularity that cdot-7's own closure (built without a full metric
theory underneath) simply never had to confront?

---

## 5. Success verdict against WP2's four stated items

| Item | Status |
|---|---|
| Define $\mathcal N$ on $\Sigma_t$ | **Done** — §1, using AeST's own $q_{\mu\nu}$, reducing to cdot-7's $M_h/m_P$ in the symmetric sector by construction. |
| Well-posedness | **Partially addressed** — symmetric-sector convergence explained (inherited, not new); the genesis/eternal-past structure is flagged as a real, unresolved, non-alarming open item for WP3/4, not silently assumed. |
| Evolution equation | **Done, and new** — $\dot{\mathcal N}/\mathcal N=(p-\tfrac52)(\dot c/c)+3c/R_h$; matter's zero-weight-drift and radiation's weight-decay are now derived rates, not quoted ratios. |
| Recover the $dr/ds$ system, symmetric sector | **Done**, with the honest caveat that the AQUAL closure itself is used as given (not yet derived from AeST's field equations — that is WP3/WP5), so "recovery" means *slots in without alteration*, not *re-derives from nothing*. |

No kill condition applies (none is stated for WP2). **Recommend proceeding to WP3** —
the closure constraint proper (tying $Q_0(t)$ to $\mathcal N(t)$ via AeST's actual field
equations, superseding this pass's use of the closure as an adopted input) — carrying
forward the genesis/eternal-past check as WP3/4's first item.
