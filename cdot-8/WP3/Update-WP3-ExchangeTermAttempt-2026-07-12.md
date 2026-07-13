# Update — WP3: A Candidate Exchange Term, and a Well-Posedness Snag

*Companion: `SessionLog-2026-07-12.md` (this directory), Entry 7. Responds to
`cdot-8/proposal/Advisory-WP3-TouchPoint-ExchangeTarget-2026-07-12.md`. All three of
that advisory's claims independently re-verified below (§0) before use, per protocol.
Then attempts the actual construction its directives call for. Finds real progress and
one concrete, unresolved well-posedness issue — reported as a checkpoint, not a kill or
a pass, following the same touch-point pattern the advisor just modeled.*

---

## 0. Independent verification of the touch-point advisory

- **Three equivalent forms** (i) $a^3F_Q\propto N\Leftrightarrow$ (ii) $a^3(\rho_\phi+
  p_\phi)=$const$\Leftrightarrow$ (iii) continuity source $=-\dot p_\phi$: verified two
  ways on synthetic (non-physical) trajectories — $QF_Q=\rho_\phi+p_\phi$ confirmed as a
  pure algebraic identity (residual $4\times10^{-16}$), and (ii)$\Leftrightarrow$(iii)
  confirmed as pure calculus (residual $1.6\times10^{-9}$), independent of whether (i)
  actually holds.
- **Consistency with this session's own §2 identity** (`Update-WP3-ActionLevelAttempt`):
  substituting the demanded current $a^3F_Q=kN$ into that identity's right-hand side and
  simplifying algebraically (by hand) reproduces $-\dot p_\phi$ exactly — confirmed.
- **Shell-sweep dimensioning** (demanded rate $\tfrac53H_{\hat\tau}$ vs. sweep rate
  $\tfrac32H_{\hat\tau}$, ratio $9/10$): re-derived independently from $R_h\propto
  c^{3/4}$, $\dot R_h=c$, and the two-clock lapse — every intermediate step ($\dot c/c=
  \tfrac43c/R_h$, $H_t=2c/R_h$, $c/R_h=\tfrac12NH_{\hat\tau}$) checks out algebraically.
  Confirmed.

**Named assumption, stated before varying anything (directive 4 discharged)**: the
aether normalization throughout is $A^\mu A_\mu=-1$ with respect to $g_{\mu\nu}$, the
single AeST metric — no disformal $\hat g$ exists (WP1 finding); this is the only
metric in play anywhere in this construction.

---

## 1. A candidate construction

Following the shell-sweep hypothesis, promote the census to an auxiliary dynamical
variable satisfying WP2's own evolution equation as a constraint, and add a second
constraint tying $Q$ to it (M5/M2's content):
$$S_{\mathcal N}=\int dt\,p_{\mathcal N}\Big[\dot{\mathcal N}-\mathcal N\,g(t)\Big],
\quad g(t)\equiv\Big(p-\tfrac52\Big)\tfrac{\dot c}c+\tfrac{3c}{R_h},\qquad
S_{M5}=\int dt\,\Lambda_M\big[Q-q(\mathcal N)\big].$$
Varying the total action ($S_\text{EH}+S_\phi+S_m+S_{\mathcal N}+S_{M5}$) w.r.t. $\phi$
gives the modified equation
$$\frac{d}{dt}(a^3F_Q)=16\pi\tilde G\,\frac{d}{dt}\!\left(\frac{\Lambda_M}{N}\right)$$
— **this explicitly breaks the free conservation law, sourced by $\Lambda_M$, exactly
as intended** — a genuine, checkable step forward from the free-EOM assumption that
caused the third escalation.

---

## 2. The snag: one multiplier too many

Varying w.r.t. $\mathcal N$ gives $\dot p_{\mathcal N}=-p_{\mathcal N}g(t)-\Lambda_M
q'(\mathcal N)$ — a *new*, independent equation for $p_{\mathcal N}$'s own dynamics, with
no boundary condition yet fixing it. Counting: two new Lagrange multipliers
($p_{\mathcal N}$, $\Lambda_M$) were introduced to enforce what is physically *one*
relation (tie $Q$ to the census). This over-introduces freedom — the system as
constructed is under-determined, not over-determined as one might have feared from the
opposite direction. **This is a genuine well-posedness problem with this specific
construction, not yet resolved.**

**A second candidate, avoiding the extra multiplier**: instead of promoting
$\mathcal N$ to an auxiliary dynamical field, use WP2's evolution equation's own
closed-form solution directly — $\mathcal N(t)=\mathcal N(t_0)\exp\big[\int_{t_0}^t
g(t')dt'\big]$, a genuine *functional* of the entire history of $a(\cdot)$, anchored at
the one physically measured value $\mathcal N(t_0)\leftrightarrow\Omega_\text{closure}
=0.074$ — and impose $S_{M5}=\int dt\,\Lambda_M(t)\big[Q(t)-q(\mathcal N[t])\big]$
directly, with no second multiplier. This avoids the extra degree of freedom (no new
undetermined integration constant beyond the one already-measured $\mathcal N(t_0)$),
but makes the action **genuinely nonlocal in time**: varying w.r.t. $a(t')$ at any
moment must account for how that changes $\mathcal N(t)$ at *every later* $t>t'$,
giving an integro-differential equation of motion for $a(t)$ rather than an ODE. This
is a real, if unusual, category (nonlocal actions appear elsewhere in modified
gravity), but carrying out that functional variation correctly is a nontrivial
technical undertaking I have not completed.

---

## 3. What this means, and what's still needed

Both candidate constructions confirm the qualitative picture from the previous update
(M5 must genuinely source $\phi$'s equation, not modify $F(Q)$ alone) and both keep
matter's own conservation completely untouched (directive 1 satisfied by construction
— $S_m[g]$ never appears in either candidate). Neither is yet a complete, verified
implementation: the auxiliary-field version has one undetermined multiplier too many;
the nonlocal-functional version is well-posed in principle (anchored only at the one
physically measured $\mathcal N(t_0)$) but requires a genuine functional/nonlocal
variation I have not carried out. **Recommend a touch point before proceeding further**
— this is exactly the kind of fork (which construction, if either, is the right one to
push on) where getting a second read is more valuable than pressing ahead alone,
mirroring the pattern the advisory itself just modeled.

---

## 4. Status

No kill, no pass — concrete progress on two fronts (a genuine sourced-EOM structure;
confirmation matter stays untouched) and one clearly-stated, unresolved technical
obstacle (which construction correctly encodes "one physical constraint, no spurious
extra freedom"). The stability/zero-crossing joint check (touch-point directive 2) and
the full WP2 finalization (directive 3) are appropriately deferred until one
construction is settled, since checking them against an ill-posed candidate would not
be informative.
