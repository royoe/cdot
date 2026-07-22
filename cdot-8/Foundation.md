# Foundation — cdot-8: A Covariant Completion of cdot-7 on an AeST Chassis

*Status: this document is not yet formally promoted (the proposal's own
promotion gate — WP1–WP3 passing — has been met; this is the
promotion). It is written to bring a new expert advisor to current
understanding without requiring the session-by-session history; for
that history, and for open items/current status, see the companion
`Progress.md`. Prepared 2026-07-19.*

---

## 0. Purpose and Scope

cdot-8 is **not a supersession** of cdot-7 (the prior, independently-developed
variable-speed-of-light Machian cosmology framework). It is a **completion
program**: a generally covariant theory whose preferred-frame limit *is*
cdot-7 — same census closure, same $a_0=\lambda\dot c$ portal, same fitted
phenomenology — extended to make relativistic-level predictions (lensing,
PPN, gravitational waves, CMB/matter-power structure) that cdot-7's
Newtonian scope cannot. Two honest exit states were always on the table:
success (cdot-8 absorbs cdot-7 as its preferred-frame limit) or failure (a
stated kill condition triggers, cdot-7 stands unaffected, the negative
result is documented). **As of this writing, no kill condition has
triggered**; the program has passed its first three, hardest work packages
and is mid-way through a fourth.

cdot-7 remains the sole framework in data-contact use; nothing in cdot-8 is
citable inside cdot-7 except as "proposed." Findings that bear on cdot-7's
own established fit choices are routed through `ConsolidationLog-2026-07-12.md`
(candidate improvements) — cdot-7's own files are never edited from cdot-8
work.

## 1. Design Constraints Inherited as Negative Results

cdot-6's failure modes, promoted to axioms of *avoidance*:

- **D1 — no single-scalar universal dictionary.** cdot-6 died because a
  single scalar cannot simultaneously carry the spatial (PV-convention)
  and temporal (cosmological) scaling jobs cdot-7 needs. cdot-8 separates
  these structurally: local relativistic phenomenology is carried by the
  tensor metric, not a spatially-varying $c$; "variable $c$" survives only
  as the cosmological, foliation-defined relation between epochs.
- **D2 — no potential-based MOND.** Any local closure built on a
  potential-like scalar gives $1/r^2$ asymptotics for any smooth
  combination. The completion target is **relativistic AQUAL** — GR-like
  PPN where GR is tested, MOND in the weak field — never GR itself.
- **D3 — $c_\text{gw}=c_\gamma$ to $10^{-15}$** (GW170817), non-negotiable,
  must hold by construction.
- **D4 — matter-sector Lorentz invariance and the equivalence principle**:
  foliation effects confined to the gravity sector; matter universally
  coupled to a single metric.

## 2. What cdot-8 Keeps From cdot-7

The entire empirical layer is acceptance data, not something cdot-8 is free
to refit: the four-term fit ($\delta_0=-0.0909$, $\kappa\lambda=0.4355$,
$\lambda=0.3056$, $\Sigma m_\nu=1.374$ eV, $q_0=-0.44$, age 12.9 Gyr, using
the **Simple** interpolating function $\mu(x)=x/(1+x)$, explicitly
preferred over the standard alternative by $\Delta\chi^2\approx13$); the
census $\Omega_\text{closure}=0.074=\Omega_b+\Omega_\nu$
($\Omega_b=0.0442$, matching Planck's independent BBN $\omega_b$ to 3%);
the one portal $a_0=\lambda\dot c$; and the project's own methodology
(adopted-vs-derived flagging, verify-then-trust for every external anchor,
per-prompt session logs, kill conditions stated before work begins).

**One acceptance datum carries a live experimental exposure**: $\Sigma
m_\nu=1.374$ eV implies $m_\beta\approx0.46$ eV, at the edge of KATRIN's
current bound ($m_\beta<0.45$ eV, 90% CL, on partial data), with the
decisive final analysis (sensitivity $<0.3$ eV) pending — see
`Progress.md` for the registered falsification criterion.

## 3. The Chassis: AeST

Skordis & Złośnik's Aether-Scalar-Tensor theory (AeST; *PRL* 127, 161302
(2021), arXiv:2007.00082) supplies the field content and quasistatic/GW
structure: a metric $g_{\mu\nu}$, a unit-timelike vector $A_\mu$ (enforced
by a Lagrange multiplier), and a shift-symmetric scalar $\phi$, with action
$$S=\int d^4x\,\frac{\sqrt{-g}}{16\pi\tilde G}\Big[R-\frac{\mathcal K_B}2
\hat F^{\mu\nu}\hat F_{\mu\nu}+2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi
-(2-\mathcal K_B)\mathcal Y-\mathcal F(\mathcal Y,\mathcal Q)-\lambda(A^\mu
A_\mu+1)\Big]+S_m[g],$$
$\mathcal Q\equiv A^\mu\nabla_\mu\phi$, $\mathcal Y\equiv q^{\mu\nu}
\nabla_\mu\phi\nabla_\nu\phi$, $q_{\mu\nu}\equiv g_{\mu\nu}+A_\mu A_\nu$.
Matter couples to $g_{\mu\nu}$ alone — **no disformal metric**, unlike
TeVeS (a corrected reading of the original proposal's framing). By
construction the tensor mode propagates at $c_\gamma$ **in all
situations** (satisfies D3), and the quasistatic weak-field limit gives
$\Psi=\Phi$ (correct lensing) with AQUAL/MOND phenomenology.

**The critical divergence, adopted knowingly**: AeST's own cosmology gets
its dark-matter-mimicking behavior from its free function $\mathcal K(
\mathcal Q)$ chosen so the scalar's energy density evolves dust-like,
$\propto a^{-3}$ — the scalar *is* AeST's dark matter, and AeST's own
CMB/matter-power literature results are fits *of that component*. cdot-7's
central claim is the opposite: no dark component, $\Omega_\text{closure}=
0.075\approx\Omega_b+\Omega_\nu$, late-time acceleration from an
instability mechanism, not $\Lambda$ or a mimicking scalar. **cdot-8 keeps
AeST's field content, quasistatic limit, and GW sector, but replaces its
cosmological branch wholesale** with the census/M5 closure below.
Consequence, accepted knowingly: AeST's own CMB fit does not transfer;
cdot-8's CMB story is built from scratch (WP7), and currently carries an
open, unresolved tension (§9).

## 4. Mapping Conjectures (Realized)

- **M1 (foliation)**: cdot-7's coordinate frame = the aether rest frame /
  scalar-clock slicing of AeST's spontaneously-broken phase. AeST's
  shift-symmetric scalar behaves as ghost-condensate-like $k$-essence,
  generating an emergent preferred foliation for free.
- **M2 (the portal)**: $\dot c\leftrightarrow\mathcal Q_0=A^\mu\nabla_\mu
  \phi$ on the background; $a_0=\lambda\dot c$ becomes a *derived*
  quantity, $\hat a_0(z)=\tfrac23\lambda c_0H_{\hat\tau}(z)$, not a
  chosen parameter.
- **M3 (the dictionary)**: realized exactly in WP1 (§5).
- **M4 (the census)**: realized exactly in WP2 (§6).
- **M5 (the closure)**: realized in WP3 (§7) — the Machian boundary
  condition tying $\mathcal Q_0(t)$ to the census $\mathcal N(t)$, which
  AeST itself lacks (AeST's $\mathcal Q_0$ is a free parameter; cdot-8
  makes it a prediction).

## 5. The Dictionary as a Frame Map (WP1)

Coordinate quantities are physical quantities re-expressed in a running
Planck-unit system built from a bookkeeping $c(t)$ (freezing $G,\hbar$):
$X_\text{coord}(t)=X_\text{phys}(t)\,(c(t)/c_0)^{n_X}$. Requiring cdot-7's
bookkeeping redshift law $1+z=(c_0/c_z)^{3/2}$ to equal AeST's own
physical redshift **forces**
$$\boxed{c(t)=c_0\left(\frac{a(t)}{a_0}\right)^{2/3}}$$
— the unique relation, not assumed. This single relation reproduces *all*
of cdot-7's kinematic exponents (mass $\propto c^{1/2}$, length
$\propto c^{-3/2}$, frequency $\propto c^{5/2}$, density map $p\to p-7$)
as one theorem, and independently reproduces cdot-7's own $H_0=\tfrac32
\dot c_0/c_0$ relation.

**Two-clock dictionary** (addendum, load-bearing): coordinate time
$t_\text{coord}$ (native to $\dot R_h=c$, $a_0=\lambda\dot c$ — the
gravity-sector/khronon clock) and matter's own proper time $\tau$
(what atoms and photons actually measure) are *distinct*, related by
$$\boxed{\frac{d\tau}{dt_\text{coord}}=\left(\frac{c}{c_0}\right)^{5/2}}.$$
The two clocks coincide exactly at $t_0$ (so $H_0$ calibration is
unaffected), diverging only when integrating over cosmic time (ages,
high-$z$ distances) — this is what resolves the apparent tension between
cdot-7's own trajectory and its bounded-EdS-matching distance formula
(traced to a silent, unjustified equating of the two clocks in the
original derivation). This exact relation was already silently
implemented, unremarked, in cdot-7's own pre-cdot-8 code.

**Status: passed.** Kill condition (no disformal map reproduces the
photon sector) moot — AeST has no disformal metric to fail to reproduce.

## 6. The Covariant Census (WP2)

Using AeST's own aether-orthogonal projector $q_{\mu\nu}=g_{\mu\nu}+A_\mu
A_\nu$ (already present in the action's $\mathcal Y$-invariant, not
introduced ad hoc):
$$\mathcal N(t)\equiv\int_{\Sigma_t\cap\{\chi\le\chi_h(t)\}}
\frac{\rho_{E,\text{coord}}(x,t)}{E_P(t)}\sqrt q\,d^3x,\qquad
E_P(t)=\sqrt{\hbar c(t)^5/G},$$
over a comoving ball of coordinate radius $R_h(t)\equiv a_0\chi_h(t)$
satisfying $\dot R_h=c(t)$, i.e. $R_h(t)=c_0a_0^{-2/3}\int^ta(t')^{2/3}dt'$
— a genuine causal-horizon-type quantity, **not** the standard
constant-$c$ particle horizon (its early-time growth is far more
suppressed, since $c(t)\to0$ in the deep past — a fact that mattered
directly in WP7, §8). In the homogeneous sector this reduces exactly to
cdot-7's own $M_h(t)=\mathcal N(t)m_P(t)$ — the correct kind of check (ADM
mass reducing to Newtonian mass), not circular.

**Evolution equation** (genuinely new content, per species with
coordinate-energy-density exponent $p^\text{sp}$):
$$\boxed{\frac{\dot{\mathcal N}}{\mathcal N}=\Big(p^\text{sp}-\frac52\Big)
\frac{\dot c}{c}+\frac{3c}{R_h}}$$
— a weight-drift term (vanishes identically for matter, $p^\text{sp}=
\tfrac52$) plus a shell-sweep term (horizon growth sweeping up new
comoving content). The `dr/ds` census-closure system used throughout
cdot-7 is recovered identically, though with the AQUAL closure itself
still imported (not yet derived from the field equations — that was
WP3/5's job).

**Status: passed** (no kill condition stated for WP2; assessed against
four stated success items, all met). One item carried forward
unconfirmed: whether AeST's actual sourced background reaches genesis
only as $t\to-\infty$ (eternal, non-singular past, as cdot-7's own fixed
point does) — flagged for WP3/4, not yet independently reconfirmed on
AeST's own dynamics.

## 7. The Closure Constraint — M5 (WP3, the make-or-break work package)

M5 requires AeST's scalar to be sourced by the Machian census rather than
freely conserved. Implemented as a Lagrange-multiplier term in the closed,
general-lapse minisuperspace action:
$$S_{M5}=\int dt\,\Lambda_M\big[\mathcal Q-q(\mathcal N_\text{tot})\big],
\qquad\mathcal N_\text{tot}=\sum_i\mathcal N_i,$$
alongside per-species multiplier terms enforcing WP2's own evolution
equation, and an $R_h$ multiplier sector. **Final, confirmed result: the
census/horizon sector carries no lapse dependence at all** ($g_i=(p_i^
\text{sp}-\tfrac52)\dot c/c+3c/R_h$, $\dot R_h=Nc\to c$ literally, derived
directly from the covariant foliation-integral definitions) — so it does
not back-react on the Hamiltonian constraint. (An extended multi-round
saga initially found an apparent, scheme-dependent back-reaction term;
this was ultimately traced to two compounding errors — a wrong lapse
insertion and a factor-of-3 shell-sweep slip — both now corrected, and the
whole scheme-dependence question is moot once corrected.)

**Background Friedmann equation, final form**:
$$\boxed{H_{\hat\tau}^2=\frac{8\pi G}3\rho_m-\frac13F(\mathcal Q)+
\frac12\mathcal QF_Q(\mathcal Q)}$$
— coefficient $\tfrac12$ on the $\mathcal QF_Q$ term (not the bare
scalar-only $\tfrac13$; the extra $\tfrac16\mathcal QF_Q$ is $S_{M5}$'s
own back-reaction on the lapse constraint), with the background identity
$$\Lambda_M(t)=\frac{Na^3F_Q(\mathcal Q)}{16\pi\tilde G}$$
established from the $\mathcal Q$-field equation with the integration
constant $C_1=0$ fixed by past-regularity (exact, era-independent).

**$F(\mathcal Q)$ is fixed by quadrature**, not chosen: solving
$\tfrac12\mathcal QF_Q-\tfrac13F=\Omega_s(a)$ (the "invoice," below) for
$F$ gives $F(\mathcal Q)=\mathcal Q^{2/3}\big[-5\!\int Q'^{-2/3}\Omega_s\,
ds'+C_2\big]$, with $C_2$ a genuine kernel constant of the constraint
operator — it contributes exactly zero to any physical observable
(verified numerically), so it is carried symbolically and never fixed.
**Zero adjustable parameters survives**: every number entering $E(z)$,
$F(\mathcal Q)$, and $\hat a_0(z)$ traces to already-fixed cdot-7
quantities ($\kappa\lambda,\lambda,x_0$) and $\Omega_\text{closure}$ —
no new free function or constant was introduced.

**The invoice**, $\rho_s\equiv\tfrac12\mathcal QF_Q-\tfrac13F\equiv
\Omega_s(a)$: what the census-closed background (ordinary matter +
radiation alone) still needs, on top of that content, for AeST's own
Friedmann equation to reproduce cdot-7's independently-fitted expansion
history. This is a genuine, zero-knob *output*, not a fit: it comes out
**dust-like in the matter era** ($w_s\approx0$, $\Omega_s\approx0.26$–
$0.33$; matter-era power law $F\propto\mathcal Q^{1.77}$), **bends
$\Lambda$-like at late times** ($w_s\to-0.68$ today, $\Omega_s(0)=0.926$),
and is **small and slightly negative in the radiation era** ($\approx
-7\%$) — crossing exactly zero at $z\approx9640$ (a fluid-decomposition
artifact where the underlying field variables stay perfectly regular;
load-bearing for WP7, §8).

**Key numbers**: $\Omega_\text{closure}=0.074$; $F_{QQ}(\mathcal Q_0,
\text{today})\approx-0.169$ (in $H_0^2$ units — appears independently in
*four* places in the program: the condensate mass §8, the stability
sign check, WP7's perturbed-constraint coefficient, and WP7's own
matter-era structure-formation mechanism §10 — a genuine coherence
signal); $\mathcal Q\propto a^{-5/3}=(1+z)^{5/3}$ exactly.
**Corrected, 2026-07-20 (confirmed independently by two parties)**: an
earlier figure, $F_{QQ}(0)=-0.696$, was a domain-boundary numerical
artifact (a derivative evaluated at the literal edge of the solved ODE,
reproduced identically by a second script using the same flawed method
— not independent verification). The corrected value, cross-checked by
three independent methods (agreeing to $\sim1\%$) and confirmed by a
second, independent re-derivation, is $F_{QQ}(0)\approx-0.169$ — same
sign, roughly $4\times$ smaller in magnitude. Every qualitative
conclusion built on the old value survives (the sign, hence stability,
is unchanged; condensate negligibility strengthens, §8).

**Status: passed.** Kill condition (constraint inconsistent with the
Bianchi/constraint structure) did not trigger.

## 8. Weak Field With Evolving $a_0$ (WP5)

**Local/cosmological decoupling**: $\mathcal N_\text{tot}(t)$ is a
horizon-integrated number, not a local field. Varying $S_{M5}$ with
respect to the local scalar shows $\Lambda_M$'s force spreads with weight
$1/V_\text{horizon}$ per point while $\Lambda_M$ itself is extensive — the
product is finite and spatially uniform at leading order, reproducing
exactly the already-verified background equation and nothing more. **M5
constrains only the background mode**; the local quasistatic perturbation
around an individual mass obeys AeST's own (unmodified) field equations,
evaluated at whatever $\hat a_0(t)$ the background constraint sets for
that epoch. (Structurally identical to unimodular gravity's global volume
constraint — a known-safe precedent.)

**Recovered AQUAL equation**: $\nabla\cdot[\mu(|\nabla\Phi|/\hat a_0(z))
\nabla\Phi]=4\pi G\rho$, $\Psi=\Phi$, with
$$\boxed{\hat a_0(z)=\frac23\lambda c_0H_{\hat\tau}(z)}$$
— verified: $\hat a_0(0)=1.386\times10^{-10}$ m/s$^2$ vs. cdot-7's
independently-fitted $1.39\times10^{-10}$. This gives a genuine,
zero-new-parameter prediction: $\hat a_0(z_\text{lens})/\hat a_0(0)=
E(z_\text{lens})$ (e.g. $1.161$ at $z=0.25$, $1.237$ at $z=0.35$, $1.862$
at $z=1.0$) — the *same* prediction as the SN diagram and the dynamical
$\hat a_0(z)$ fit, not an independent new curve.

**The condensate mass**: expanding $F(\mathcal Q_0+\delta\mathcal Q)$ to
second order gives an effective ghost-condensate mass in AeST's own
established slot ($\mu^2=2\mathcal K_2\mathcal Q_0^2/(2-\mathcal K_B)$,
$\mathcal K_2=-\tfrac14F_{QQ}(\mathcal Q_0)$). Stability requires
$\mathcal K_2>0$ — automatically satisfied ($F_{QQ}\approx-0.169<0$),
not tuned. Numerically, scanned across AeST's stable $\mathcal K_B\in
[0.1,1.5]$ range (updated 2026-07-20 for the corrected $F_{QQ}$, using
the same exact-dictionary formula as the original figure): $\mu^{-1}
\approx10$–$20$ Gpc, condensate-transition radius $r_c\approx100$–$160$
Mpc for a $10^{11}M_\odot$ galaxy — roughly $2\times$ and $1.6\times$
the previously-quoted band respectively, four-plus orders of magnitude
above AeST's own hand-imposed requirement ($\mu^{-1}\gtrsim1$ Mpc) and
far beyond any galaxy/solar-system scale tested. **The condensate is
negligible everywhere observationally accessible** — a genuine,
zero-freedom distinguishing feature relative to vanilla AeST (which must
hand-tune this scale), and the correction only strengthens this.

**Weak-lensing RAR confrontation**: cdot-8 predicts a $\sim12$–$16\%$
acceleration-scale enhancement by $z\sim0.2$–$0.25$; the two natural
literature anchors (Brouwer et al. 2021 KiDS-1000; Mistele et al. 2024)
both pool their lens samples over $0.1<z<0.5$ with no redshift binning,
and carry systematic floors ($\sim26\%$ stellar-mass-conversion band,
cross-survey zero-point scatter) that are common-mode with, and larger
than, the predicted signal — **not a clean test either way**. A
differential (intra-survey bin-ratio) test design, which cancels these
common-mode systematics, was worked out and shown to need lens depth to
$z\sim0.6$–$1.0$ (DES/HSC-deep, LSST, or Euclid), not yet available.

**Status: closed as delivered** (author's decision, Gate 2). "Delivered"
means: a falsifiable, pre-registered, zero-new-parameter prediction + a
demonstrated literature gap + a differential test design with an explicit
systematics budget — not a completed data confrontation. No WP5b opened;
reprocessing survey catalogs is judged outside this program's charter.

## 9. The Relativistic Sector (WP6)

**Tensor speed**: $c_\text{gw}=c_\gamma$ confirmed exact "by construction,
in all situations" (inherited directly from AeST), independently
re-verified that M5 cannot touch the tensor sector (a scalar constraint
cannot source tensor perturbations at linear order in FRW). D3 satisfied
without qualification.

**Solar-system screening (sub-task 1)**: the Cassini-testable object is
AeST's own large-gradient screening/tracking completion, not the "naked
simple" $\mu(x)=x/(1+x)$ this program uses for cosmological-closure
convenience. Any reasonable screened completion passes the classical
anomalous-acceleration Cassini bound by 2–286+ orders of magnitude; the
naked simple function alone would fail by $\sim2800\times$ (a known,
pre-existing result, not a new cdot-8 finding).

**PPN preferred-frame parameters ($\alpha_1,\alpha_2$) and binary pulsars
(sub-tasks 2–3)**: a genuine, substantial original derivation (redoing
Foster-Jacobson-class Einstein-æther PPN machinery for AeST's actual field
content, since the literature's own formulas are singular for AeST's
aether alone). **Closed conditionally, not exactly**: a conservative
envelope $|\alpha_1|\le4\mathcal K_B$ was established (not an equality),
giving $\mathcal K_B\lesssim2.5\times10^{-6}$ under current pulsar bounds
($|\alpha_1|\lesssim10^{-5}$). Binary-pulsar tests (PSR J1141-6545,
J0348+0432, J0737-3039, J1738+0333) are consistent with this envelope.
**The exact (not envelope) $\alpha_1,\alpha_2$ closure remains open**,
explicitly flagged as pending further work, not abandoned. A second,
*provisional* $\alpha_2$-based envelope ($\mathcal K_B\lesssim4\times
10^{-10}$, potentially the binding one) also exists on the record, but
carries a double caveat: it's pending the same $E$-term re-derivation
as $\alpha_1$, *and* the solar-spin-alignment bound it uses
($1.6\times10^{-9}$) was flagged, via a live literature check, as
possibly $\sim100\times$ tighter than the commonly-cited value
($\sim2.4\times10^{-7}$, Nordtvedt) — **not to be used until the
underlying bound itself is verified.** The $\alpha_1$ pulsar envelope is
unaffected and is what sub-task 3 actually relies on. Worth noting for
calibration, not as an existential threat: **every established cdot-8
structure survives the $\mathcal K_B\to0$ corner smoothly** (the
condensate mass sits at its already-quoted band's own endpoint;
$m_\times\to\infty$ dissolves the two-quasistatic-limit question by
parameter squeeze; the spin-1 sector simply decouples; SZ stability
holds throughout) — the squeeze, if it lands, is survivable.

**A new, serious, unresolved tension (2026-07-19)**: the Solar System
quadrupole $Q_2$ (Park, Hees, Famaey, Desmond & Durakovic 2026,
arXiv:2602.17884; $Q_2=(1.6\pm1.8)\times10^{-27}$ s$^{-2}$) encodes MOND's
External Field Effect, sourced by the interpolating function's shape
*near* $a_0$ (the Milky Way's external field at the Sun,
$e_N=O(1)$–$O(2)$), not the deep-Newtonian tail — the screening argument
that resolves sub-task 1 does not transfer, since Saturn (9.5 AU) sits
deep inside the $\sim6500$ AU MOND transition radius and merely
*transmits* rather than screens the externally-imposed tidal term.
**cdot-7's own established, preferred fit (Simple IF, $a_0=1.39\times
10^{-10}$ m/s$^2$) predicts $Q_2\approx3.7\times10^{-26}$ s$^{-2}$ —
$\sim23\times$ the bound, $\sim21\sigma$ in tension**, independent of
which shallow-transition IF family is used. This strikes a *program
choice* (the interpolating-function/$a_0$ fit), not the census-derived
core. **Sequencing decided (2026-07-20)**: any re-fit is postponed until
after WP7, on the same logic as Gate 1(b)'s own deferral — the finding
itself stands, unresolved, and joins the post-WP7 revisit queue (see
`Progress.md` §4b).

## 10. Perturbation Theory (WP7, in progress)

AeST's own linear cosmological perturbation system (Newtonian gauge,
built from $\chi\equiv\varphi+\dot{\bar\phi}\alpha$, $\gamma\equiv
\dot\varphi-\dot{\bar\phi}\Psi$, $\mathcal E_\alpha\equiv\dot\alpha+\Psi$)
is imported directly — it reduces the Einstein equations to standard GR
fluid form with a nonstandard pressure contrast $\Pi$ sourced by the
vector-field perturbations. **The general (not just $\Pi\to0$) evolution
equations are quoted and verified from primary source.**

**The M5 low-$\ell$/horizon-scale structure**: M5's census constraint
sources a genuine new term in both the Einstein equation and the scalar
field equation at $kR_h(t)\lesssim$ few, governed by a spherical top-hat
window $W(kR_h(t))$ — clean sub-horizon decoupling recovered exactly
(the field-side term converges to literally the same $-F_Q A^\mu$
coefficient WP6's own PPN sector uses, at machine precision). Because
$R_h(t)$ (built from $\dot R_h=c(t)\to0$ in the deep past) grows far more
slowly at early times than a standard particle horizon, every mode was
fully coupled through recombination and only exits (decouples) during the
matter era — the signature relocates from "acoustic peaks" (originally,
incorrectly, expected) to (i) the **growth history** (an $O(0.5$–$0.7)$
coupled-era modification to the effective Poisson source, now WP7's
central deliverable) and (ii) a **late-time $\ell\lesssim10$ remnant**
(turning on over $z\sim0.3$–$1$, in the standard ISW window). **Any
assembly must reproduce, exactly, two non-negotiable anchors** (residual
$=$ error, not a tolerance): the $k\to0$ separate-universe identity
(Einstein-side coefficient $(F_Q/6+QF_{QQ}/2)q'$) and the sub-horizon
recovery of the field-side term to WP6's own $-F_Q$ (same symbol, same
number) — these bracket all remaining covariantization freedom. That
freedom itself has a fourth, named facet (normalization locality —
per-slice vs. ball-smoothed local $c$; per-slice is the declared
default) alongside census gauge status, fiducial center, and the volume
convention — bounded by a third untouchable beyond the two anchors: the
matter census is *exactly* immune to this facet ($p_m=5/2$
cancellation), so the freedom touches only radiation-class coefficients.

**Does the scalar sector ($\Omega_s$) cluster?** Resolved: **yes, dust-
like, through the matter era.** cdot-8's own map-independent adiabatic
sound speed ($c_\text{ad}^2=w+(dw/ds)/(d\ln\rho_s/ds)$, using the
already-established $w(a),\rho_s(a)$ directly — not the AeST-native
formula, which uses a structurally different $(\rho,P)(\mathcal Q)$ map
and does not transplant) gives $c_\text{ad}^2\sim-0.01$ to $-0.04$
through the matter era — small, matching AeST's own dust-like clustering
criteria almost exactly where structure forms. Combined with the budget
($\sim4.4\%$ baryons, $\sim3\%$ massive neutrinos vs. $77$–$92\%$ scalar
from $z=50$ to today — nothing else to build structure with) and AeST's
own design intent (the scalar sector's whole mechanism is CDM-mimicking
clustering), this is now a settled structural conclusion, not an
assumption.

**Open, not yet resolved — but now diagnosed, not just blocked**: the
actual coupled growth system (dust-like scalar + baryons/neutrinos + M5
source + mode exits), needed for a real ISW $\Delta C_\ell$ number, has
not yet been built successfully — two careful attempts at the general
fluid closure ($\Pi$ built from the field variables $\chi,\mathcal
E_\alpha$, with real $k$-dependence) both failed numerically. A
dedicated stiffness/failure-mode audit (Stage 0 of a staged, advisor-
cross-checked rebuild) found the physics is **not** intrinsically stiff
($|\mu_\text{eff}|/H<1$ everywhere) — both failures trace to
*formulation* (keeping the effective-fluid $\delta,\theta$ as state
variables, whose own definitions carry $c_\text{ad}^2\sim20$–$230$
through the matter era) and *units* (a founding-paper/cdot-8 convention
mismatch), not to a genuine instability. Two standing rules now guide
the rebuild: integrate only $(\chi\text{ or }\gamma,\alpha,\mathcal
E_\alpha,\delta_b,\theta_b,\Phi)$ — nothing whose *definition* contains
$\rho_s,c_\text{ad}^2,$ or $1/(1+w)$ — and write one units-dictionary
line per imported equation before any code.

**A genuine physical discovery came out of that same audit**: through
the matter era the scalar's own effective mass-squared is negative and
Hubble-tracking, $\mu^2/H^2\approx-1.27f_s/(2-\mathcal K_B)\approx-0.5$,
flipping to the stable sign at $z\approx0.13$–$0.15$ — confirmed by
independent re-derivation, giving $\mu^2/H^2(0)\approx+0.05$, a
*narrower* stable margin today than "near today" first suggested — read
physically, a Jeans-class growing mode, i.e. **the actual dynamical
mechanism behind $\Omega_s$'s dust-like clustering**, not just a
small-$c_\text{ad}^2$ diagnostic. $F_{QQ}$'s fourth load-bearing
appearance in the program. A first,
order-of-magnitude dispersion-relation estimate (canonical $c_s^2=1$)
puts this mechanism's Jeans scale *above* the Hubble radius — meaning it
can matter only at the very lowest multipoles ($\ell\lesssim2$–$3$), not
ordinary sub-horizon galaxy formation, which still relies on the scalar
tracking baryons gravitationally. This is simultaneously the item's
strongest recruiting asset (a concrete, checkable growth-rate target)
and a safety flag: **a negative $\mu^2$ here is the clustering
mechanism, not a bug** — do not "fix" it. This is the concrete next
piece of WP7, staged (Stage 0 done, Stage 1 in progress) with advisor
cross-checking at each step, not a quick patch. See `Progress.md` for
the full stage plan.

## 11. Status and Standing Caveats

Every result from WP4a onward inherits **Gate 1(b)**: cdot-8's own
recombination-era sound horizon gives $100\theta_*=1.326$ against
Planck's $1.04109\pm0.00030$ — a clean 27% overshoot, localized almost
entirely to the crossover-era $E(z)$ (not to $\Omega_b$, independently
validated to 3% against Planck's BBN value; not to BBN itself, which
passes). The author's ruling (2026-07-18): **provisional structural
failure, not a kill** — the background sector is "not yet viable as
stated," but the explicit instruction is to complete WP7 on current
assumptions first and revisit only afterward. **This caveat is carried by
every WP5/WP6/WP7 result** and is not resolved by anything in this
document. See `Progress.md` for the full decision-gate record and the
complete, current list of open items.
