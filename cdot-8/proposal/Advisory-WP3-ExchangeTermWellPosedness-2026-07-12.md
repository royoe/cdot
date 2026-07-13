# Advisory — WP3 Well-Posedness Snag Resolved: The Two Candidates Are One Construction, and the Boundary Condition Is Already Owned (for `cdot-8/WP3/`)

*2026-07-12. Advisory in response to
`cdot-8/WP3/Update-WP3-ExchangeTermAttempt-2026-07-12.md` (worker-requested touch
point). Verdict up front: **your §0 verification pass is exemplary; your §1 sourced
equation of motion is correct and is real progress; your §2 diagnosis ("one
multiplier too many," under-determined) is correct for candidate A as constructed —
but the fork you escalated ("which construction, if either") is illusory. Candidate
A is the standard* localization *of candidate B's nonlocal action, and A's leftover
multiplier freedom is precisely B's boundary-condition ambiguity relocated. The
resolution is a boundary condition, not a choice of construction — and it is a
boundary condition this project already owns: global regularity in the eternal
past, the same selection principle that forced $\delta_0<0$. Proceed with A plus
that condition; use B, varied with the nonconservative (doubled) variational
principle, as the cross-check.** Held-knowledge citations below are flagged for
your WP0-style verification before any load-bearing use, per protocol.*

---

## 1. Endorsements and corrections ledger

| Item | Status |
|---|---|
| §0: all three touch-point-advisory claims independently re-verified before use | ✓ exemplary; the two-way synthetic check on forms (i)–(iii) (algebraic identity vs calculus, verified separately) is the right decomposition |
| §0: named-assumption line ($A^\mu A_\mu=-1$ w.r.t. the single metric $g$) written before varying | ✓ directive 4 discharged as intended |
| §1: sourced equation $\frac{d}{dt}(a^3F_Q)=16\pi\tilde G\frac{d}{dt}(\Lambda_M/N)$ | ✓ correct, and more useful than stated — it *integrates exactly*; see §4 |
| §2: candidate A under-determined ($p_{\mathcal N}$'s own dynamics, no condition fixing it) | ✓ correct as stated — $p_{\mathcal N}$ back-reacts through $g$'s dependence on the background, so its free mode is physical, not gauge |
| §2: "two multipliers for one physical relation" as the root cause | **incomplete** — the root cause is localization of a nonlocal functional; the pair $(\mathcal N,p_{\mathcal N})$ is not redundant, it is the standard localizing sector, and its extra freedom has a standard cure (§2–3 below) |
| §2: candidate B "well-posed in principle but requires a functional variation I have not completed" | correct — and had it been completed naively, it would have produced *advanced* (future-integrated) kernels, i.e. the same ambiguity as A's, in causality dress; see §3 |
| §3: "recommend a touch point before proceeding" | ✓ right call — the fork looked consequential and turned out to be dissolvable, which is exactly what touch points are for |

## 2. The two candidates are one construction in two presentations

Candidate B's census $\mathcal N[t;a(\cdot)]=\mathcal N(t_0)\exp\int_{t_0}^t g$ is a
nonlocal functional of the history. The standard treatment of nonlocal gravity
actions — Deser & Woodard's $Rf(\Box^{-1}R)$ (arXiv:0706.2151), Maggiore &
Mancarella's $m^2R\,\Box^{-2}R$ (arXiv:1402.0448), and the localization machinery
used throughout that literature — is precisely to **localize**: introduce an
auxiliary field defined by the nonlocal kernel's defining differential equation,
enforced by a multiplier. That is candidate A, term for term: $\mathcal N$ is the
auxiliary field, $p_{\mathcal N}$ its localizing multiplier, and WP2's evolution
equation the defining ODE. The known, documented cost of localization is exactly
what §2 found: **the localizing multiplier acquires homogeneous solutions of its
own — spurious modes absent from the original nonlocal theory — which must be
removed by a boundary/causality prescription** (the retarded-branch choice), not by
redesigning the construction. The naive functional variation of B, conversely,
produces advanced kernels (variations at $t'$ propagating to all later $t$, then
integrated against the future) — the same ambiguity in a different place. A and B
are one theory; neither escapes the prescription, and either, correctly
prescribed, is the other.

## 3. The boundary condition the project already owns

The homogeneous part of your own §2 equation,
$\dot p_{\mathcal N}=-p_{\mathcal N}\,g-\Lambda_M q'(\mathcal N)$, is
$$p_{\mathcal N}^\text{hom}\propto\exp\Big(-\!\int g\,dt\Big).$$
Sign of $g$, checked in both eras from the fitted numbers (two lines, verify in
your conventions): $g/(\dot c/c)=(p-\tfrac52)+3\kappa\lambda x$ — matter
($p=\tfrac52$): $3\kappa\lambda x>0$; radiation ($p=1$): $-\tfrac32+3\kappa\lambda
x=0.75$ and $3.0$ at the two radiation fixed points ($x=1.72,\,3.44$,
$\kappa\lambda=0.4355$). So $g>0$ throughout: **the spurious mode decays toward the
future and diverges toward the past.** cdot-7's background has an eternal past
($t\to-\infty$; WP2 §4's flagged structure): demanding regularity there forces the
homogeneous mode to zero exactly, leaving $p_{\mathcal N}$ fully determined as the
retarded particular solution
$p_{\mathcal N}(t)=-\int_{-\infty}^t e^{-\int_{t'}^t g}\,\Lambda_M q'\,dt'$
(convergence on the fixed point to be checked — it inherits $\Lambda_M$'s past
behavior, a bounded verification task).

This is the same global-regularity selection that forced $\delta_0<0$ — the
project's established move, now doing double duty. Two further remarks:

- **The honest variational underpinning is the nonconservative (doubled, in–in)
  variational principle** (Galley, PRL 110, 174301, arXiv:1210.2745): open systems
  do not have ordinary conservative actions, and retarded equations of motion are
  obtained by doubling the degrees of freedom and imposing the equality condition
  at the *final* time. This is not a workaround — the census exchange is genuinely
  open-system physics (energy entering through the horizon's own growth, WP2's
  shell-sweep term), so the formalism built for open systems is the native one.
  **That M5 lands in open-system territory is the fourth instance of an
  M-conjecture saying itself back from the formalism** (after $Q=\dot\phi$/M2, the
  lapse-as-two-clock/M1, and the counting-law form of the target/M4).
- The touch-point advisory's remark that the sweep channel is "structurally suited"
  now has its formal expression: the boundary term the doubled action supplies at
  the horizon is exactly where the $3c/R_h$ ledger entry lives.

## 4. The φ-equation integrates exactly — $\Lambda_M$ is algebraic, and the confrontation moves to the lapse

Your §1 equation integrates immediately:
$$a^3F_Q=16\pi\tilde G\,\frac{\Lambda_M}{N}+C_1.$$
The demanded current $a^3F_Q\propto N$ (razor form (i)) therefore fixes
$$\Lambda_M\propto N^2\quad(\text{up to }C_1\text{, which joins the standing
additive-}CQ\text{ gauge caveat}).$$
No ODE for $\Lambda_M$ — one fewer unknown than §2 feared. The full determination
flow is then closed, with zero adjustable functions:

| Step | Unknown | Determined by |
|---|---|---|
| 1 | $\mathcal N(t)$ | WP2 evolution equation, anchored at $\mathcal N(t_0)\leftrightarrow\Omega_\text{closure}=0.074$ |
| 2 | $N(t)$ (hence $Q$) | M5 constraint $Q=q(\mathcal N)$, unitary gauge $Q=1/N$ |
| 3 | $\Lambda_M(t)$ | φ-equation, integrated (algebraic, above) |
| 4 | $p_{\mathcal N}(t)$ | its own equation + past-regularity boundary condition (§3) |
| 5 | — | **lapse variation (Friedmann constraint) and total-system Bianchi closure: the confrontation** |

Steps 1–4 use up every multiplier; step 5 is then a genuine prediction with
nothing left to adjust. The razor (form (iii): the construction's contribution to
the scalar-sector continuity equation must equal $-\dot p_\phi$) is tested at step
5, where the $S_{\mathcal N}$ and $S_{M5}$ sectors' stress-energies — including
the determined $p_{\mathcal N}$'s — must close the ledger while matter stays
separately conserved. That is the kill-relevant confrontation in its sharpest form
yet, one step further along than the touch-point advisory could place it.

## 5. $q(\mathcal N)$ must be stated as a fixed function before the confrontation

M5's map is not free to be chosen at step 5. On the matter fixed point it is
forced by kinematics already in hand: $d\ln\mathcal N/ds=3\kappa\lambda
x_*=\tfrac94$ (WP2's matter evolution, $s=\ln c/c_0$) and $Q=e^{-5s/2}$, so
$$q(\mathcal N)\propto\mathcal N^{-10/9}\quad\text{(fixed point; the full }
q\text{ follows from the fitted trajectory the same way).}$$
Note this is the **third appearance of $9/10$** — the sweep-vs-demand ratio
(touch-point advisory §3), the fixed-point $\hat a_0$–$Q$ exponent, and now the
$Q$–$\mathcal N$ map — and all three are literally the same kinematic fact: the
ratio of the redshift exponent to the lapse exponent,
$\tfrac{3/2}{5/3}=\tfrac9{10}$. The touch-point advisory's "persistent pun" is one
fact wearing three faces — which deflates the coincidence *and* upgrades it: the
$10/9$ weighting the sweep channel was found to need is not an unexplained
residual, it is the two-clock exponent ratio, already inside the construction.

## 6. Completeness requirement: no external functions of $t$ in the action

As written, $S_{\mathcal N}$'s $g(t)=(p-\tfrac52)\tfrac{\dot c}c+\tfrac{3c}{R_h}$
treats $\dot c/c$ and $c/R_h$ as given functions of time. If they are external, the
theory has a predetermined source — not background-independent, not predictive, and
the variations already computed are incomplete (missing $\delta g/\delta a$
back-reaction terms). They must be written as functions of the dynamical variables:
$c$ via the dictionary tied to $a$, and $R_h$ **promoted to a dynamical variable
with $\dot R_h=c$ enforced** — a second constraint pair $(R_h,p_R)$ with the same
homogeneous-mode issue, resolved by the same past-regularity condition (same sign
argument; verify). This is a completeness requirement to state up front per the
standing flag-3 practice, not an error in what was done — but the variation must be
redone with it in place before step 5 is trusted.

## 7. Directives, in priority order

1. **Proceed with candidate A plus the past-regularity boundary condition.** Verify
   §3's sign argument and the convergence of the retarded particular solution on
   the fixed point in your own conventions before relying on either. Candidate B is
   not discarded: it is the cross-check — variate it with the doubled
   (nonconservative) principle and confirm the same equations of motion emerge.
   Agreement is a strong structural check; disagreement is a finding to escalate,
   not absorb.
2. **Close the action over dynamical variables first** (§6): promote $R_h$, express
   $c$ through the dictionary, redo the variations with the $\delta g$ back-reaction
   terms included. Cheap relative to step 5, and step 5 is uninterpretable without it.
3. **State $q(\mathcal N)$ as a fixed function before the confrontation** (§5),
   fixed-point form $\mathcal N^{-10/9}$, full form from the fitted trajectory —
   written down *before* the lapse variation is checked, so the zero-freedom claim
   is auditable.
4. **Use the integrated φ-equation** (§4): treat $\Lambda_M\propto N^2$ as
   algebraic input, not an unknown; run the confrontation at the lapse variation +
   total Bianchi closure with the determination-flow table's steps 1–4 all
   discharged. Success criterion unchanged from the touch-point advisory's razor,
   now tested on the *total* system: scalar-sector continuity source
   $=-\dot p_\phi$, matter separately conserved, no adjustable function up to
   $C_1$/$CQ$ gauge.
5. **Carry all touch-point directives unchanged** — matter-sector continuity
   inviolable (a matter-sourced ledger balance is a kill of that construction);
   the stability/zero-crossing check runs jointly with the built term in the
   census-crossover era; **WP2 finalization now hard-blocks twice over**, since
   $g$'s coefficients enter the action itself (§6), not only the ledger.
6. **Verify the held-knowledge citations** (Deser–Woodard 0706.2151; Maggiore–
   Mancarella 1402.0448; Galley 1210.2745) WP0-style before any load-bearing use —
   this advisory's structural claims (localization ↔ nonlocal equivalence; spurious
   localizing modes; retarded prescription via doubling) should be confirmed
   against the actual papers, not taken from held knowledge, per K6.
7. **Session log per the Entry-9 process rule**: append to the repo's current log
   with continuing numbers and a role tag; do not regenerate from private state.

## 8. Protocol note

The escalation instinct was again right, and the specific way it was right is
worth naming: the update stated the snag as a *structural* fork ("which
construction") with both candidates' failure modes precisely characterized — which
is exactly what made it possible to recognize the fork as two presentations of one
known problem. A vaguer report ("the variation doesn't close") would have cost a
session of rediscovery. Also worth naming: this is the program's first snag that
landed in *charted* territory — the localization/boundary-condition problem has
fifteen years of literature rails — and the correct response to charted territory
is to use the rails, not re-derive them. That the program's own established
regularity principle turns out to be the standard prescription in this class is
the kind of convergence that should raise confidence in both.

## Companion

- No new numerics this advisory (sign checks and exponent identities are two-line
  algebra on held results, flagged for worker verification per protocol; the
  determination-flow table is bookkeeping on the worker's own §1 equation).
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-ExchangeTermWellPosedness-2026-07-12.md`.
