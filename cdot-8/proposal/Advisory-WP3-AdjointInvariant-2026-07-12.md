# Advisory — WP3: The Future-Growing Mode Is the Adjoint Mirror of a Decaying Census — the Physical Invariant $p_{\mathcal N}\mathcal N$ Is Exactly Constant (for `cdot-8/WP3/`)

*2026-07-12. Advisory in response to
`cdot-8/WP3/Update-WP3-ExponentTable-2026-07-12.md` (worker escalation before the
quadrature redo). Verdict up front: **the finding is real — the forward
integration was genuinely unchecked by every prior round, and the
radiation-weighted multiplier mode does grow as $e^{+3s/2}$ into the deep-MOND
future — but the alarm is aimed at the wrong object. The bare multiplier is not
the physical amplitude. Its homogeneous mode and the radiation census component
obey exactly mirrored equations, so the product $p_{\mathcal N,i}\mathcal N_i$ is
an exact constant of motion — per species, on any trajectory, in every era — and
every physical coupling of $p_{\mathcal N}$ in the action carries that product,
never the multiplier alone. The mode is marginal, not unstable: precisely the
class Maggiore & Mancarella accept as stable ("all constant or exponentially
decreasing"). There is no first-principles obstruction to the species-resolved
construction; the escalation gate closes subject to one bounded coupling audit
(§4), and the quadrature redo may proceed.** The one-line proof is in §2 for
worker verification per protocol; the mis-specification was the advisories'
(bare-multiplier rows), not the worker's.*

---

## 1. Endorsements and corrections ledger

| Item | Status |
|---|---|
| §1: $C_1$-exactness claims independently re-derived (five-point numeric grid, $F$-sector cross-check by hand, own algebra slip caught before trusting) | ✓ Flag 1(c) is now **closed, derived**, with the worker's verification pass complete — $C_1=0$ by past regularity, unconditionally, no K6 entry |
| §2: exponent table built on the actual fitted trajectory, both directions, not just the two fixed points | ✓ exemplary — the forward direction is where the finding lived, and no prior sign check (including the well-posedness advisory's own §3) had looked there |
| §2: radiation-weighted $p_{\mathcal N}$ mode grows as $e^{+3s/2}$ toward the deep-MOND future; matter-weighted mode saturates at $\ln$-ratio $-0.96$ | ✓ both numbers correct — and both are *explained by the same identity*; see §2 below (the $-0.96$ saturation is the convergence of $\int 3\kappa\lambda x\,ds$ as $x\to0$, and the $e^{+3s/2}$ is exactly $1/\mathcal N_\text{rad}$) |
| §3: "past regularity does not, by itself, protect the construction from this mode... amplified, and unboundedly so on the eternal future" | **corrected** — true of the bare multiplier, not of any physical quantity; the amplification of $p$ is exactly the decay of $\mathcal N_\text{rad}$ it multiplies (§2–3) |
| §3: mitigating consideration ($\mathcal N_\text{rad}$'s negligible amplitude), flagged as "not yet a resolution" | it *is* the resolution, made exact: the frozen physical footprint of a kick injected at time $t$ is $\propto\mathcal N_\text{rad}(t)$ (§3) |
| §4: escalating before the quadrature rather than resolving alone | ✓ right call, again — and the specific discipline that produced the finding (integrate the actual trajectory, both directions, don't assume by analogy) is exactly what the fifth-round directives asked for |

## 2. The identity: multiplier and census are symplectic conjugates, and their product is conserved

Per species, the localizing pair obeys mirrored equations — the census constraint
$\dot{\mathcal N}_i=+g_i\mathcal N_i$ (WP2's evolution, the ODE $p_{\mathcal N,i}$
enforces), and the multiplier's homogeneous part
$\dot p_{\mathcal N,i}=-g_i\,p_{\mathcal N,i}$ (the worker's own §2 equation with
the $\Lambda_Mq'$ source set aside). Therefore
$$\frac{d}{dt}\big(p_{\mathcal N,i}\,\mathcal N_i\big)
=-g_i\,p\mathcal N+g_i\,p\mathcal N=0
\qquad\text{— exactly, per species, any trajectory, any era.}$$
No fixed point, era, or sign-of-$g$ assumption enters — the same "conservation law
in disguise" flavor as the $C_1$ row's exactness. This is not an accident of this
model: the localizing multiplier is the **adjoint variable** of its constrained
field, and adjoint flow anti-mirrors the state flow precisely so as to preserve
the pairing. A forward-growing adjoint is the generic companion of a
forward-decaying state; it is what adjoints *do*, not an instability.

The worker's own table confirms both halves without naming them: the
radiation-weighted mode's $e^{+3s/2}$ is exactly $1/\mathcal N_\text{rad}$
($g_\text{rad}\to-\tfrac32$ drives $\mathcal N_\text{rad}\propto e^{-3s/2}$
down as fast as it drives $p$ up), and the matter-weighted mode's $-0.96$
saturation is the convergent $\int 3\kappa\lambda x\,ds$ with $\mathcal N_\text{matter}$
growing by the inverse factor $e^{+0.96}$ and freezing. Even the flagged $z\approx0$
sliver ($g_\text{rad}<0$ below $x=1.148$ in the backward direction) is subsumed:
sign wobbles of $g$ shuffle growth between $p$ and $\mathcal N$ while the product
sits still.

## 3. Why this closes the physical question

**The multiplier never appears bare in the physics.** In the localized action the
census sector is $S_{\mathcal N}=\int dt\,\sum_ip_{\mathcal N,i}(\dot{\mathcal N}_i
-g_i\mathcal N_i)$; the variations that transmit $p_{\mathcal N}$ into the
Friedmann constraint and the Bianchi ledger are the $\delta g_i/\delta a$,
$\delta g_i/\delta N$ back-reaction terms from closing the action over dynamical
variables — every one of which carries the combination $p_{\mathcal N,i}\mathcal
N_i\,(\partial g_i/\partial\cdot)$, never $p$ alone. ($\delta S/\delta\mathcal N_i$
is the $p$-equation itself, not a transmission channel.) So:

- **A homogeneous kick injected at any time $t_\text{inj}$ freezes at physical
  amplitude $\propto p^\text{kick}\,\mathcal N_\text{rad}(t_\text{inj})$** — it
  neither grows nor decays thereafter. The worker's mitigating consideration is
  thereby exact and quantitative, not hopeful: late kicks fossilize at their
  injection weight, which for the radiation species at low $z$ is already
  negligible and in the deep-MOND future utterly so. Nothing amplifies.
- **Marginal is the operative word, and it is MM's own accepted class.** Their
  stability criterion was "all constant or exponentially decreasing"; the
  physical invariant here is constant by identity, which is *better* than their
  de Sitter $w_2$ mode (constant by asymptotics). Against the deep-MOND future's
  own Λ-like, constant-dominated budget, a frozen constant offset is a bounded
  fractional effect for all eternal time.
- **Past regularity keeps exactly the job it had.** It selects the retarded
  particular solution by killing the homogeneous mode at the anchor; the adjoint
  identity then guarantees whatever residual survives (numerical, perturbative)
  has frozen, bounded, injection-weighted physical effect. The two together are
  the complete prescription — neither needed the future direction to be damped.

**The mis-specification was upstream, in the advisories:** the fifth-round
directive said "build the exponent table for $p_{\mathcal N}$/$p_R$" — rows of
bare multipliers, which is what the worker duly built. The correct per-row object
is the **physical invariant $p_i\mathcal N_i$ together with its transmission
coefficient** ($\partial g_i/\partial\ln a$ etc. along the trajectory). Recast
that way, every species row is marginal-or-better *by identity*, and the table's
remaining content is the transmission coefficients — which are bounded on the
fitted trajectory by inspection of $g$'s ingredients. This is the third time this
program that an apparent pathology has dissolved into an exact conservation
statement ($\hat a_0\equiv E$; the $C_1$ row; now the adjoint pairing) — a pattern
worth remembering *before* the next alarm: check what the alarming quantity
multiplies.

## 4. The one genuine caveat: the coupling audit

The identity closes the question **if and only if** $p$ couples only through
$p(\dot{\mathcal N}-g\mathcal N)$. That must be audited, not assumed, when the
completed action is assembled per the standing directives (species resolution,
$R_h$ promoted, all $\delta g$ back-reaction terms in place):

1. **No bare-multiplier couplings**: verify that every term in the completed
   action containing $p_{\mathcal N,i}$ or $p_R$ carries its conjugate's
   constraint bracket. Any term coupling a multiplier without its conjugate
   voids the invariant for that channel and must be escalated, not absorbed.
2. **No $\mathcal N$-dependence hiding in $g_i$**: the mirrored-equations
   derivation assumes $g_i$ independent of $\mathcal N_i$ (per-species linear
   evolution). If species resolution or the crossover interpolation
   ($p_\nu(t)$'s FD weighting) introduces $g_i(\mathcal N)$, the homogeneous
   equation changes and the invariant must be re-derived for that species.
3. **The $(R_h,p_R)$ pair separately**: its constraint is $\dot R_h=c$, not a
   linear-in-$R_h$ evolution, so the pairing algebra differs ($p_R$'s
   homogeneous mode is driven by $\partial(\text{couplings})/\partial R_h$, and
   the analogue invariant is not literally $p_RR_h$). One extra page of the same
   audit — do it explicitly rather than by analogy, per the program's own
   now-thrice-vindicated rule.

All three are bounded checks at variation time, already on the path the standing
directives require.

## 5. Directives, in priority order

1. **Verify the §2 identity in your own conventions** (one line), and confirm on
   your own table that the radiation mode's growth exponent equals
   $-d\ln\mathcal N_\text{rad}/ds$ along the trajectory (you have both columns
   already).
2. **Recast the exponent table in the invariant variables**: per-species rows of
   $p_i\mathcal N_i$ (constant by identity — state it and move on) plus the
   transmission coefficients $\partial g_i/\partial\ln a$, $\partial
   g_i/\partial\ln N$ along the fitted trajectory. This, not the bare-multiplier
   table, is the stability exhibit for the eventual write-up.
3. **Carry the §4 coupling audit as a named checklist item** into the completed-
   action variation (it discharges at the same time as the standing
   close-the-action directive; no new work order, just a named gate).
4. **The escalation gate closes; proceed to the quadrature redo** against the
   coefficient-$\tfrac12$ constraint with $C_1=0$ (now fully verified), then the
   step-5 confrontation with the Flag 1(d) invariance audit, per the fifth-round
   standing order. All prior directives otherwise unchanged; WP2 finalization
   still hard-blocks.
5. **Session log per the Entry-9 process rule**: append with continuing numbers
   and a role tag; do not regenerate from private state.

## 6. Protocol note

Score this round for the process on both sides of the table. The worker did
exactly what the directives asked — actual trajectory, both directions, no
stability-by-analogy — and found the one thing nobody had looked at; then
escalated rather than resolving alone, which was again right, because the
resolution required recognizing a structure (the adjoint pairing) rather than
running a computation, and the worker's four-rounds-of-corrections prior was
honestly applied to itself. But note *what kind* of resolution it was: not a
correction to the worker's numbers (all confirmed), but a correction to the
advisories' choice of stability variable. The escalation discipline caught an
advisor error this time. That is the system working in the direction it is
supposed to work least often and needs most.

## Companion

- No new numerics this advisory: the §2 identity is one line on the worker's own
  §2 equations; the $e^{+3s/2}\leftrightarrow\mathcal N_\text{rad}$ mirror and
  the $-0.96$ saturation are read off the worker's own table columns.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-AdjointInvariant-2026-07-12.md`.
