# Session Log — cdot-8/WP3 (2026-07-12)

---

## Entry 1 — Attempting WP3; a distance-formula tension found instead (2026-07-12)

**Prompt (verbatim):**
> Go for WP3.

**Summary of work performed:**

1. **Set up WP3's actual question precisely**: M5 combined with the AQUAL closure and
   WP2's $M_h=\mathcal N m_P$ is already cdot-7's own closure ODE, not yet involving
   $Q(t)$/AeST's field equations — so WP3's real content is checking whether AeST's
   Friedmann equation can be sourced (via some admissible free function $F(Q)$) to match
   whatever $H(t)$ the closure already demands. This required computing that $H(t)$
   explicitly.

2. **Derived $H(a)$ on cdot-7's matter fixed point via WP1's dictionary**: $H\propto
   a^{1/6}$ — cross-checked independently against Foundation §5.4's own quoted
   $a_0\propto c^{5/4}$ result (exact match), giving confidence in the derivation.

3. **Computed the genuinely covariant proper-distance formula for this $H(a)$**:
   unbounded, $\propto(1+z)^{7/6}-1$. **This does not match cdot-7's own quoted
   distance formula** (Foundation §5.2), which is bounded, $\propto1-(1+z)^{-1/2}$.
   Verified the integration method itself is correct by substituting literal EdS
   ($H^2\propto a^{-3}$) into the same integral and recovering cdot-7's quoted formula
   exactly — confirming that formula's covariant meaning specifically requires literal
   matter domination, which the fixed point (via the same dictionary) does not give.

4. **Confirmed independently, using only cdot-7's own internal algebra** ($R_h\propto
   c^{3/4}$ plus the redshift law, no reference to $a(t)$ at all), that this same
   distance formula IS reproduced — meaning the tension is real and specific: the
   redshift-forced $c(t)$-vs-$a(t)$ tie and the closure ODE's own solution, taken
   together, do not describe a spacetime whose covariant distances match what cdot-7
   claims for it.

5. **Assessed what survives and what doesn't**: the redshift law and the local
   (single-epoch) Planck-unit exponents are untouched (instantaneous statements, not
   integrals). What's in question is whether cdot-7's $R_h(t)$/$D_p(z)$ — built inside
   its own static-space ontology — corresponds to any genuine covariant distance once
   embedded in AeST, at least under a single power-law $c(t)$-vs-$a(t)$ tie.

6. **Did not declare a unilateral kill or pass.** This finding bears on WP1's own
   success claim (not only WP3) and touches cdot-7's four-term SN fit — its most
   validated empirical result — once that fit is asked to mean something covariantly.
   Escalated three live, non-exclusive options to the author (reopen WP1; check the
   actual perturbed $\delta_0\ne0$ trajectory instead of the exact fixed point, which
   Foundation itself treats as an unstable reference solution, not the physical one;
   treat this as informative about cdot-7 in its own right) rather than deciding which
   to pursue.

**Files produced:** `Update-WP3-DistanceTension-2026-07-12.md`, this log. No file in
`cdot-7/` touched — cdot-7 stands unaffected, per the proposal's own charter, pending
the author's read of this finding.

**Open items handed forward:** all three options in the Update document's §6, pending
author decision; WP3 proper (the constraint-propagation/Bianchi-consistency check) is
on hold until whichever of those is chosen resolves what $H(a)$ the closure actually
requires. cdot-7's own priority queue, above all the KATRIN clock, remains unstarved
and untouched by this session.

---

## Entry 2 — Unblocked: the two-clock resolution (2026-07-12)

**Resolution reached via `cdot-8/WP1/Update-WP1-Addendum-TwoClockDictionary-2026-07-12.md`**
(option 1 of Entry 1's three: WP1 reopened, not the fixed-point-vs-perturbed-trajectory
route). Root cause: WP1's original Planck-unit dictionary applied its own relabeling
rule to mass, length, and frequency but silently exempted time, tacitly setting
coordinate time equal to matter's proper time. Correcting this (deriving, not
asserting, $d\tau/dt_\text{coord}=(c/c_0)^{5/2}$ from the same rule already used for
the other three quantities) resolves the tension exactly: the covariant distance built
on proper time $\tau$ reproduces cdot-7's bounded, EdS-matching formula to
$1.9\times10^{-11}$, both by independent re-derivation and by direct confirmation that
`cdot-7/Fable-1/closure_dynamics.py` already implements this exact distinction
(`tau_proper` vs. `t_coord`) silently, since 2026-07-07, without ever stating it as a
principle in prose. Not a cdot-7 inconsistency, not a WP1 error requiring redesign — a
missing documentation/dictionary entry, now supplied.

**Verdict: WP3 is unblocked.** Target, precise: does AeST's Friedmann sector admit
$H_\tau^2\propto a^{-3}$ (fixed point) plus the fitted late-time departure, on matter's
own proper time, with the khronon/gravity-sector clock (carrying $Q_0$'s $a^{1/6}$-rate
evolution) as the separate object hosting the theory's novelty? WP3 proper — the
constraint-propagation/Bianchi-consistency check — is next.

---

## Entry 3 — WP3 proper surfaces a second, more severe tension (2026-07-12)

**Prompt (verbatim):**
> Continue on WP3 now.

**Summary of work performed:**

1. **Set up the actual field-equation check** using AeST's ordinary, additive Friedmann
   equation ($H_\tau^2=\tfrac{8\pi\tilde G}3\rho_m-\tfrac13(F-QF_Q)$, $\Lambda=0$ since
   cdot-7's acceleration is the separatrix instability, not a bare constant) against the
   fixed point's required $H_\tau^2\propto a^{-3}$.

2. **Identified why AQUAL's own mechanism cannot supply the difference at the
   background level**: AQUAL's field equation is a statement about spatial *gradients*
   ($\mu(x)$ compares field strength to $a_0$); an exactly homogeneous FRW background
   has zero spatial gradient by symmetry, so AQUAL's characteristic modification —
   using $\mu(x)<1$ to make less mass produce more binding, exactly how MOND avoids
   dark matter for galaxies — has no natural home there. cdot-7's own closure gets
   around this via an explicitly Machian, horizon-as-quasi-local-boundary construction,
   which is an *additional* postulate, not something AQUAL's local equation supplies on
   its own once covariantized.

3. **Quantified the severity, using cdot-7's own formula and fit numbers**
   ($\kappa\lambda=0.4355,\lambda=0.3056,x_0=1.10$): independently recomputed
   $\Omega_\text{closure}=0.0750$, matching the quoted 0.074. An ordinary Friedmann
   equation sourced by only this density falls short of the fixed point's required
   $\Omega_\text{total}=1$ by a factor of **13.3$\times$** ($\Delta\Omega\approx0.925$)
   — not a small correction; checked that AQUAL's own local boost factor $\mu(x_0)=
   0.524$ does not come close to bridging this (only reaches $\Omega_\text{closure}/
   \mu(x_0)=0.143$).

4. **Connected this to the proposal's own named risk**: §3's "critical divergence"
   passage already flags that AeST's native dust-mimicking scalar must be discarded —
   this session shows that once discarded (as required), *something* still must supply
   $\Delta\Omega\approx0.925$ at the background level, and the proposal names no
   candidate for what. Also noted this bites at the *background* level (WP3/4), earlier
   than the perturbation/CMB sector (WP7) the proposal already treats as high-risk —
   and is sharpest at high $z$, where the trajectory sits closest to the exact fixed
   point, i.e. exactly where CMB/structure data are most constraining.

5. **Considered four candidate escape routes** (checking the actual perturbed
   trajectory instead of the fixed point — flagged as unlikely to help, given the
   trajectory is *closest* to the fixed point at high $z$, not low; the missing
   component need not be literally cold dark matter, though it must still source $H^2$
   additively and track $a^{-3}$ at the fixed point; M5's Machian, census-determined
   sourcing of $Q_0(t)$ could preserve *some* distinctive, falsifiable content even if
   energetically dark-sector-like — the most promising partial rescue; a genuinely
   non-additive, AQUAL-like modification of AeST's own background field equations,
   which nothing in the extracted literature suggests exists).

6. **Escalated again, did not declare a unilateral kill.** This does not match the
   proposal's WP3 kill condition literally (no Bianchi/constraint-algebra
   inconsistency — the equations are consistent, they just don't have the energy
   budget the proposal's plan supplies for). Framed as a judgment call on whether this
   redefines what cdot-8 must mean by "no dark matter" (best candidate: no *freely-fit*
   dark sector, only Machian/census-determined gravitational content) rather than a
   technical pass/fail.

**Files produced:** `Update-WP3-BudgetTension-2026-07-12.md`, this entry. No file in
`cdot-7/` touched.

**Open items handed forward:** author decision on §5's escape routes (or another);
numerical check of the actual $\delta_0\ne0$ trajectory's budget requirement, not yet
done (flagged as unlikely to relieve the tension but not confirmed either way); if
option 3 (Machian-determined energy content) is pursued, WP3's own literal question
(Bianchi/constraint-algebra consistency of M5) still needs answering on top of this.
cdot-7's own priority queue, above all the KATRIN clock, remains unstarved and
untouched.

---

## Entry 4 — Advisory read; inverse reconstruction attempted (2026-07-12)

**Prompt (verbatim):**
> Please find updated advisory in the proposal folder.

**Summary of work performed:**

1. **Read and independently verified `cdot-8/proposal/Advisory-WP3-BudgetInvoice-
   2026-07-12.md` and `budget_invoice.py`** before building on either. Diagnosis
   (both the worker's Entry 3 finding and the advisor's own first-reply figures):
   the $13.3\times$ shortfall was computed on the idealized fixed-point-through-today
   solution, not the actual fitted trajectory — and a real correction to Entry 3's own
   §2: homogenization does not eliminate AQUAL's mechanism, it rotates the gradient
   into the *time* direction (the $-\tfrac13(F-QF_Q)$ term on $Q=\dot\phi$ *is* that
   limit). Author endorsed option 3 (post-invoice claim language: no *freely-adjustable*
   dark sector, gravitational-sector energy census-determined) as policy. New M7
   mapping conjecture (the invoice equation) and re-posed WP3 (inverse reconstruction
   first, constraint propagation second) adopted into the proposal via
   `Amendment-cdot8-Proposal-Invoice-2026-07-12.md`.

2. **Independently re-derived `budget_invoice.py`'s core $E(s)$ formula** from the
   two-clock dictionary and the closure ODE directly (not merely re-run) — exact
   match, including the fixed-point limits.

3. **Attempted the assigned inverse reconstruction (directive 1).** Derived the
   consistency condition $\xi Q(a)=-H_0^2a^4\Omega_s'(a)$ from requiring $F_Q(a)=
   \xi a^{-3}$ (exact) and Friedmann accounting to hold simultaneously — validated
   the formula against a synthetic, hand-constructed $F(Q)$ test case before trusting
   it on real data (recovered the true $Q(a)$ to $9\times10^{-7}$ relative error).

4. **Found a sharp shape mismatch.** The invoice-forced $Q(a)$ (computed along the
   actual fitted trajectory) is nearly flat ($<15\%$ variation out to $z=20$), while
   Foundation §5.5's independently-fit galactic MOND scale $\hat a_0(z)$ grows by a
   factor of $\sim2$ by $z=1$ and continues growing steeply — a sharp divergence, not
   a marginal one, under the simplest reading of M2 ($\hat a_0\propto Q$). Identified
   the one real escape route (a strongly nonlinear $\hat a_0=g(\lambda_s,Q)$, needing
   $\hat a_0\propto Q^n$ with $n\gtrsim7$) and flagged it as unmotivated by anything in
   AeST's own literature rather than ruling it out.

5. **Escalated again, did not declare a unilateral kill** — noted explicitly that both
   prior WP3 escalations turned out to hinge on something this session's setup had
   gotten subtly wrong, and flagged this pattern rather than assuming (or denying) this
   finding is the same kind of resolvable gap.

**Files produced:** `Update-WP3-InverseReconstruction-2026-07-12.md`, this entry.

**Open items handed forward:** author review of the shape-mismatch finding; if a
rescue via nonlinear $g(\lambda_s,Q)$ is pursued, it needs independent motivation, not
curve-fitting; WP4a (Stage-1 acoustic scale) and WP4b (BBN rate) remain queued per the
amendment, not yet started; the $\Delta N_\text{eff}\approx-0.5$ marker owed to cdot-7
via the consolidator (added to `cdot-8/ConsolidationLog-2026-07-12.md`). cdot-7's own
priority queue, above all the KATRIN clock, remains unstarved and untouched.

---

## Entry 5 — Third-escalation resolution checked and consolidated (2026-07-12)

**Prompt (verbatim):**
> Response to your third finding is added to proposal. Note that a new agent
> assessed the finding, and verified by the original proposer with a minor
> addendum. Please check and consolidate.

**Summary of work performed:**

1. **Read `Advisory-WP3-InverseReconstruction-2026-07-12.md`** (new stand-in agent)
   and `Addendum-ThirdEscalation-Assessment-2026-07-12.md` (original proposer's audit
   of the stand-in). Diagnosis: (i) Entry 4's reconstruction wrongly imposed AeST's
   *free*, shift-symmetric scalar equation of motion ($F_Q\propto a^{-3}$) on the
   *census-constrained* theory — exactly the dynamics M5 exists to modify — which
   over-determined the system and manufactured the artifact-flat $Q_\text{forced}$;
   (ii) Foundation §5.5's quoted $\hat a_0(z)$ values are absolute ($10^{-10}$ m/s²),
   not the ratios the equation's own label claims — inflating the apparent growth by
   the fit's own anchor factor $1.39$ and producing the earlier $n\gtrsim7$ figure.

2. **Independently verified both diagnoses before accepting them** — did not rubber-
   stamp. Checked the labeling-bug claim directly against `cdot-7/Foundation.md`'s
   source text (not just the advisory's script): the equation is explicitly labeled a
   ratio, but the same section's figure plots it directly against MUSE-DARK/MIGHTEE's
   *absolute* measurements on one axis — only coherent if Foundation's own numbers are
   also absolute. Re-derived the exact identity $\hat a_0=\tfrac23\lambda c_0H_\tau$
   from scratch (not from either script), checked algebraically at five arbitrary
   points spanning $c/c_0\in[0.5,2.0]$ — holds exactly everywhere, confirming it is a
   genuine identity, not a fixed-point-specific coincidence.

3. **Found one additional caveat neither prior document raised**: M1's
   "$\phi=t_\text{coord}$" identification (used to get $Q=(1+z)^{5/3}$) is
   dimensionally awkward — $Q$ needs acceleration-adjacent dimensions, while
   $dt_\text{coord}/d\tau$ is a dimensionless ratio. Assessed as likely harmless for
   every conclusion drawn (all comparisons are shape/exponent comparisons, insensitive
   to an absorbed constant), but flagged explicitly as something to pin down when M5
   is actually implemented at the action level, rather than silently absorbed.

4. **Verdict confirmed: not a kill.** A genuine $F(Q)$ exists by quadrature for any
   monotonic $Q(a)$; with $Q$ correctly identified via M1, the reconstruction gives a
   clean, geometrically-motivated result (census-constrained current departs from free
   conservation by exactly one power of the two-clock lapse). WP3's next step, per the
   stand-in's directives (accepted): implement M5 at the action level and check
   whether it actually produces this single-lapse-factor source — now a zero-freedom
   success criterion.

5. **Consolidated**: corrected `cdot-8/WP1/Update-WP1-Addendum-TwoClockDictionary-
   2026-07-12.md` §5(c) in place (struck through the wrong figures, added the correct
   ones — the qualitative conclusion survives and is sharper than originally
   reported). Added three new items to `cdot-8/ConsolidationLog-2026-07-12.md` (the
   §5.5 labeling bug, HIGH confidence; the exact $\hat a_0$–$H_\tau$ identity plus the
   evidence-ledger correction it implies; the canonical-$x_0$ reproducibility request)
   — bringing the log to ten items.

**Files produced:** `Update-WP3-ReconstructionResolved-2026-07-12.md`, this entry;
corrections to `cdot-8/WP1/Update-WP1-Addendum-TwoClockDictionary-2026-07-12.md` and
`cdot-8/ConsolidationLog-2026-07-12.md`.

**Open items handed forward:** the action-level M5 implementation (WP3's real next
step, with the zero-freedom success criterion and the stability/zero-crossing
sub-check carried forward); the dimensional caveat on $Q$'s identification, to be
resolved when that implementation is attempted; WP4a/WP4b still queued, unstarted.
cdot-7's own priority queue, above all the KATRIN clock, remains unstarved and
untouched — nothing in `cdot-7/` was edited, per charter.

---

## Entry 6 — Attempting the action-level implementation (2026-07-12)

**Prompt (verbatim):**
> Please continue with WP3.

**Summary of work performed:**

1. **Built the minisuperspace reduction** of AeST's action on the FRW/unitary-gauge
   background with the lapse $N(t)$ kept explicit (not fixed to 1), and validated it
   two ways before trusting it: varying w.r.t. $N$ reproduces WP0's extracted AeST
   Friedmann equation exactly; varying w.r.t. $\phi$ (before gauge-fixing) reproduces
   the free shift-current conservation law exactly. Resolved the dimensional caveat
   flagged in the prior document: M1's "$\phi=t_\text{coord}$" is the standard
   unitary/khronon gauge of ghost-condensate-type constructions, where $\phi$'s
   dimensions become "time" by the gauge choice and the physical content sits in the
   lapse $N=(c/c_0)^{5/2}$ — exactly the two-clock dictionary's lapse. Not an error.

2. **Derived, and numerically verified to $3\times10^{-9}$ precision** (finite
   differences on arbitrary test functions, not the physical trajectory), that the
   scalar sector's own continuity equation ($\dot\rho_\phi+3H(\rho_\phi+p_\phi)=0$,
   using AeST's own $\rho_\phi,p_\phi$ formulas) is *algebraically identical* to the
   free conservation law $\frac{d}{dt}(a^3F_Q)=0$, for *any* $F(Q)$ and $Q(t)$ — not a
   special property of the physical trajectory. Consequence: the zero-freedom
   quadrature from Entry 5 (which reproduces the invoice via the Friedmann equation
   alone) is *necessary but not sufficient* — taken alone, with the scalar sector's
   stress-energy still in its standard, unmodified form, it violates energy
   conservation, since the invoice demands $a^3F_Q\propto a^{5/3}$, not constant.

3. **Recognized this is not a contradiction of Entry 5's resolution but an independent
   route to exactly what the stand-in advisory's directive 2 already anticipated**:
   M5 cannot modify the scalar sector "for free" — it must supply the missing
   conservation-violating piece through an explicit energy-exchange channel. Identified
   WP2's own census evolution equation shell-sweep term ($3c/R_h$ — new mass entering
   the horizon via its own geometric growth, a genuinely global/Machian channel) as the
   natural, already-available candidate.

4. **Did not complete the construction.** Building the actual action-level term (which
   must couple $\phi$ explicitly, not just $Q$, to source this exchange, and must
   itself be shown Bianchi-consistent) looks like it may require treating the census's
   horizon as a genuine boundary with matter flux across it — closer to a
   junction-condition/boundary-value construction than a simple Lagrange-multiplier
   addition to a translation-invariant FRW action. Assessed as substantial, original
   work — plausibly the proposal's own §5 item 1 ("the program's heart") — not to be
   rushed within this pass given the stakes and this program's track record of subtle
   errors in exactly this kind of construction.

**Files produced:** `Update-WP3-ActionLevelAttempt-2026-07-12.md`, this entry.

**Open items handed forward:** constructing the actual energy-exchange term (shell-
sweep channel as the starting hypothesis) and verifying its own Bianchi consistency —
the concrete next step, not yet attempted; the stability/zero-crossing sub-check and
the aether-normalization-convention statement (both carried from Entry 5) still
pending once a concrete action-level term exists to check them against. cdot-7's own
priority queue, above all the KATRIN clock, remains unstarved and untouched.

---

## Entry 7 — Touch point requested: the action-level attempt assessed (advisor session, 2026-07-12, ~14:1x SAST)

**Prompt (verbatim, author to advisor):**
> Good progress on WP3. The worker has no major flags, but proposes a touch point
> before continuing. Please assess.
> [uploaded: `Update-WP3-ActionLevelAttempt-2026-07-12.md`, Entry 6's companion.]

**Summary (advisor):** Endorsed without major flags. Entry 6's §1 pre-validation
(both WP0 extractions reproduced before building) and the unitary/khronon-gauge
resolution of the dimensional caveat confirmed correct — with the closure that the
physical lapse $N=(c/c_0)^{5/2}$ *is* WP1's two-clock ratio; §2 confirmed from held
knowledge as the standard k-essence result (for any $(F,Q)$-only scalar
stress-energy, continuity $\Leftrightarrow$ free current conservation); §3's reading
endorsed (directive 2 arrived at constructively; quadrature-$F$ Friedmann-necessary
but Bianchi-insufficient; "not a kill, not a pass" correct). Value added, flagged
for worker verification per protocol:

1. **The exchange target in three equivalent forms**: (i) $a^3F_Q\propto N$;
   (ii) $a^3(\rho_\phi+p_\phi)=\text{const}$ — clock-free, exact on any trajectory,
   and the evocative form (the constrained scalar conserves-and-dilutes its
   inertial density like a counted census); (iii) continuity source
   $=-\dot p_\phi$ — the razor: the built term passes iff its contribution equals
   this exactly, no adjustable function up to the additive-$CQ$ gauge piece.
   Consistency check included: Entry 6's own §2 identity, evaluated on the demanded
   current $a^3F_Q\propto N$, yields exactly $-\dot p_\phi$.
2. **Pre-construction dimensioning of the shell-sweep candidate** (matter fixed
   point, $\hat\tau$ clock, conventions stated): demanded exchange rate per unit
   inertial density $\tfrac53H_{\hat\tau}$ vs sweep rate
   $3c/(R_hN)=\tfrac32H_{\hat\tau}$ — right size, ratio exactly $9/10$: either the
   multiplier structure supplies the $10/9$ weighting naturally, or sweep is not
   the whole channel. Residual known before construction begins; worker to redo in
   own conventions before relying on it.
3. **Cautions, priority-ordered**: matter-sector continuity inviolable (a
   matter-sourced exchange is a kill of that construction — K1/LLR exposure, report
   immediately rather than patch); the exchange term and the stability
   zero-crossing sub-check run *jointly* in the census-crossover era; **WP2
   promoted to hard prerequisite** (the ledger the total continuity check balances
   against; the sweep coefficient lives in its decomposition); the
   aether-normalization named-assumption line to be written before the multiplier
   term is varied.

---

## Entry 8 — Touch-point advisory delivered (advisor session, 2026-07-12, ~14:2x–14:3x SAST)

**Prompt (verbatim):**
> Please do.

**Summary:** Produced `Advisory-WP3-TouchPoint-ExchangeTarget-2026-07-12.md`
(location: `cdot-8/WP3/`): endorsements for the record; the three-forms derivation
with the Entry-6-identity consistency check; the sweep dimensioning with
conventions stated and a redo-in-own-conventions instruction; directives 1–5
(matter-continuity kill-of-construction condition; joint zero-crossing check; WP2
hard prerequisite; normalization line before variation; the razor success criterion
restated); protocol note endorsing the touch-point pattern. No new numerics
(two-line algebra on held results; worker verifies).

**Open items handed forward:** the exchange-term construction (WP2 first, then the
multiplier term against the form-(iii) razor); stability/zero-crossing joint check;
normalization assumption; all prior handoffs (consolidation-log items to cdot-7,
WP1 addendum §5(c) re-run — completed per Entry 5, WP4a/WP4b queued) unchanged;
**the KATRIN clock remains the program's most time-critical item.**

---

## Entry 9 — Session-log consolidation (advisor session, 2026-07-12, ~14:5x SAST)

**Prompt (verbatim):**
> One item before I accept this: The session log in the repo got polluted by the
> additional assessor, so there are two extra items that will get overwritten if I
> download this now. The last time I made a merge update, so this file is what is
> currently in the repo. Please consolidate the SessionLog so that the new items
> are appended to the current log, and update your internal log so that this comes
> right next time too, then present the updated SessionLog for download.

**Summary:** Repo version (worker+assessor entries 1–6, uploaded) adopted as the
canonical base; the advisor-side touch-point items appended as Entries 7–8 in the
repo log's numbering rather than the advisor's divergent private numbering; the
advisor's superseded private log archived locally, not delivered. **Process rule
adopted so this comes right next time:** this file is a *shared, single-writer-at-
a-time* log — whichever session (worker, stand-in, or advisor) writes next must
start from the repo's current version, append with continuing entry numbers and a
session-role tag in the entry heading, and deliver the full consolidated file;
advisor deliverables will no longer regenerate the log from private state. The
author's merge remains the arbiter between deliveries.

---

## Entry 10 — Exchange-term well-posedness snag assessed (stand-in advisor session, 2026-07-12, ~14:3x SAST)

**Prompt (verbatim):**
> The worker has reached another hurdle. Please assess
> cdot-8/WP3/Update-WP3-ExchangeTermAttempt-2026-07-12.md. and advice.

**Summary (stand-in advisor):** Worker's §2 diagnosis confirmed correct as stated
(candidate A under-determined: $p_{\mathcal N}$ back-reacts through $g$'s
background dependence, so its free mode is physical) — but the escalated fork
("which construction, if either") found to be illusory: **candidate A is the
standard localization of candidate B's nonlocal action** (Deser–Woodard /
Maggiore–Mancarella machinery; held-knowledge citations flagged for worker
verification), and A's leftover multiplier freedom is B's boundary-condition
ambiguity relocated — B's naive functional variation would produce advanced
kernels, the same ambiguity in causality dress. **Resolution: a boundary
condition, not a choice of construction — and one the project already owns.**
$p_{\mathcal N}^\text{hom}\propto\exp(-\int g\,dt)$ with $g>0$ in both eras
(matter: $3\kappa\lambda x$; radiation: $0.75$/$3.0$ at $x=1.72$/$3.44$) — the
spurious mode diverges toward the past, so global regularity in the eternal past
(the same principle that forced $\delta_0<0$) kills it exactly, leaving the
retarded particular solution. Honest variational base: Galley's nonconservative
(doubled, in–in) principle — appropriate because the census exchange is genuinely
open-system physics (horizon shell-sweep), the fourth instance of an M-conjecture
saying itself back from the formalism. Additional findings: the worker's §1
φ-equation **integrates exactly**, making $\Lambda_M\propto N^2$ algebraic (one
fewer unknown than feared) and moving the zero-freedom confrontation to the lapse
variation + total-system Bianchi closure with all multipliers pre-determined;
$q(\mathcal N)$ is forced on the fixed point ($\propto\mathcal N^{-10/9}$) and
must be stated before the confrontation; the three $9/10$'s (sweep-vs-demand,
$\hat a_0$–$Q$, $Q$–$\mathcal N$) are one kinematic fact, the redshift-to-lapse
exponent ratio $(3/2)/(5/3)$; and a completeness requirement — $g$'s ingredients
cannot be external functions of $t$: $R_h$ must be promoted to a dynamical
variable (second constraint pair, same regularity fix) and the variations redone
with $\delta g$ back-reaction included.

---

## Entry 11 — Well-posedness advisory delivered (stand-in advisor session, 2026-07-12, ~19:3x SAST)

**Prompt (verbatim):**
> Please write the advisory.

**Summary:** Produced `Advisory-WP3-ExchangeTermWellPosedness-2026-07-12.md`
(proposed location `cdot-8/WP3/`): endorsements/corrections ledger (worker's
diagnosis correct, root cause re-identified as localization rather than multiplier
redundancy); the A≡B equivalence; the past-regularity boundary condition with the
sign check in both eras; the integrated φ-equation and the five-step
determination-flow table (every multiplier determined, confrontation at the lapse
variation); the forced $q(\mathcal N)$ and the three-faces-of-$9/10$ observation;
the no-external-functions completeness requirement; directives 1–7 (proceed with
A + regularity BC, verify signs/convergence in own conventions; B via the doubled
principle as cross-check — agreement is a check, disagreement a finding; close the
action over dynamical variables before the confrontation; state $q(\mathcal N)$
first; use $\Lambda_M\propto N^2$ as algebraic input; all touch-point directives
carried, WP2 now hard-blocking twice over; verify the three held-knowledge
citations WP0-style; session log per the Entry-9 rule); protocol note (first snag
in charted territory — use the literature rails; the program's own regularity
principle coinciding with the standard prescription raises confidence in both).
No new numerics (two-line algebra on held results; worker verifies per protocol).

**Open items handed forward:** the exchange-term construction proper, now fully
specified (close the action per directive 2, then steps 1–4 of the determination
flow, then the lapse-variation/Bianchi confrontation against the razor); candidate
B cross-check via the doubled variational principle; held-knowledge citation
verification (Deser–Woodard 0706.2151, Maggiore–Mancarella 1402.0448, Galley
1210.2745); stability/zero-crossing joint check and WP2 finalization unchanged
and blocking; WP4a/WP4b and all consolidation-log handoffs unchanged; **the KATRIN
clock remains the program's most time-critical item.**

---

## Entry 12 — Fourth-round assessment: exchange-term attempt + well-posedness advisory (advisor session, 2026-07-12, ~19:3x SAST)

**Prompt (verbatim):**
> All right! One more round on WP3, reviewing the worker's flagged snag, the
> assessors review + session log. Please assess briefly.
> [uploaded: `Update-WP3-ExchangeTermAttempt-2026-07-12.md`,
> `Advisory-WP3-ExchangeTermWellPosedness-2026-07-12.md`, current
> `SessionLog-2026-07-12.md` (Entries 1–11).]

**Summary (advisor):** Both documents endorsed. Worker: §0 re-verification of all
three touch-point claims before use, and the named-assumption line written before
varying — protocol exemplary; the sourced φ-equation is real progress; the
under-determination diagnosis correct as stated. Stand-in: the A≡B localization
diagnosis, past-regularity boundary condition (reusing the $\delta_0<0$ selection
principle), integrated φ-equation with determination-flow table, forced
$q(\mathcal N)\propto\mathcal N^{-10/9}$, three-faces-of-$9/10$ unification, and
the no-external-functions completeness requirement all check out against held
context (sign values $0.75/3.0$ reproduced; exponent arithmetic verified;
localization/doubled-principle literature correctly characterized per held
knowledge, paper verification still owed per its own directive 6). Log follows the
Entry-9 rule. **One substantive flag the stand-in missed: $C_1$ is not gauge** —
a constant in $a^3F_Q$ is a free-conserved current, i.e. the amplitude of AeST's
native dust branch; the φ-equation fixes only $16\pi\tilde G\Lambda_M/N+C_1$, and
the degeneracy breaks at the lapse variation ($\delta S_{M5}/\delta N=-\Lambda_MQ/N
\ne0$ on-shell), so step 5 carries a hidden knob unless $C_1$ is fixed by stated
principle first — past regularity if derivable, census exhaustiveness
(adopted-and-flagged) if not. Plus three minor flags: the "two radiation fixed
points" misnomer ($1.72$ is the matter fixed point; reword, don't redo); the census
sector must be species-resolved in the action before the §6 redo (crossover era =
stability-check era); the determination "flow" is a coupled self-consistent system
off the fixed point.

---

## Entry 13 — Fourth-round addendum delivered (advisor session, 2026-07-12, ~19:4x–19:5x SAST)

**Prompt (verbatim):**
> Yes.

**Summary:** Produced `Addendum-FourthRound-C1NotGauge-2026-07-12.md` (proposed
location `cdot-8/WP3/`): endorsement of record with the cheap cross-checks listed;
flag 1 spelled out for worker verification — (a) $C_1$ as the native dust-mode
amplitude, (b) the $(\Lambda_M,C_1)$ degeneracy and its breaking at the lapse
variation, (c) the two candidate fixing principles in preference order
(past-regularity derived; census-exhaustiveness adopted-and-flagged per K6),
(d) a tightening of the $CQ$ caveat itself (zero energy density and absent from
the Friedmann constraint, but *not* a total derivative on FRW — it shifts
$p_\phi$ and the current; directive: verify at step 5 that physical outputs depend
only on the invariant combination of $(C,C_1,\Lambda_M)$, with the expected
$C$-cancellation escalated as a finding if it fails); flags 2–4 with concrete
one-line fixes. Stand-in directives 1–7 remain in force; flag 1(c) is required
before the step-5 confrontation, flag 1(d) runs at it.

**Files produced (Entries 12–13):**
`Addendum-FourthRound-C1NotGauge-2026-07-12.md`, `SessionLog-2026-07-12.md` (this
file, thirteen entries, appended to the repo base per the Entry-9 rule).

**Open items handed forward:** flag 1(c) discharge (the $C_1$-mode past-behavior
computation, then principle selection) — now blocking step 5; the flag 1(d)
$(C,C_1,\Lambda_M)$ invariance check at step 5; species-resolved census sector in
the §6 redo; all stand-in directives (A + regularity BC; B via the doubled
principle as cross-check; close the action over dynamical variables; state
$q(\mathcal N)$ first; citation verification WP0-style) unchanged; WP2
finalization still hard-blocking; WP4a/WP4b and all consolidation-log handoffs to
cdot-7 unchanged; **the KATRIN clock remains the program's most time-critical
item.**

---

## Entry 14 — Fifth round: MM primary-source checkpoint assessed (stand-in advisor session, 2026-07-12, ~20:1x SAST)

**Prompt (verbatim):**
> One more worker snag to handle:
> cdot-8/WP3/Update-WP3-MMPrimarySource-2026-07-12.md

**Summary (stand-in advisor):** Not a snag proper — a checkpoint: the Maggiore &
Mancarella source extracted on re-delivery, the citation is now verified at full
primary-source level (correctly attributed the first time, unlike Deser–Woodard),
and the worker proposes to adopt MM's practical method for Flag 1 — a finite
deep-RD initial-condition anchor plus their explicit homogeneous-mode exponent
check on this project's own $g(t)$ — in place of the abstract eternal-past limit,
reporting the plan before executing. Assessment: verification endorsed (directive
6 fully discharged); the exponent check is the load-bearing item and is exactly
right. Two substantive findings. (1) **Framing correction:** MM's $t_*$-
insensitivity stands on two legs — source vanishing in RD, and forward-decaying
homogeneous modes — and only the second transfers: this project's census/lapse
sourcing never shuts off, so there is no natural $U=S=0$ analogue; the finite
anchor is an *implementation* of past regularity (transients decay onto the
retarded particular solution = the attractor regularity selects), not a
replacement, and its validity is contingent on the exponent check passing in
every traversed era — including the eternal past, this project's analogue of MM's
inflationary counter-example era. (2) **Cheap scaling pre-computation:** the
addendum's flag 1(c) worry ("a free dust current is subdominant to radiation")
assumes $Q$ constant; on the census-closed background M1's clock gives
$Q\propto(1+z)^{5/3}$, so the $C_1$ term $-QC_1/6a^3$ scales as $(1+z)^{14/3}$ —
*steeper than radiation* into the past. A nonzero $C_1$ dominates the budget
toward the past and destroys the eternal-past structure, so past regularity
plausibly forces $C_1=0$ **derived** (option 1, the preferred outcome, no K6
mechanism-debt entry) — to be confirmed with the radiation-era/crossover clock
exponents as one more row of the same exponent table.

---

## Entry 15 — Fifth-round advisory delivered (stand-in advisor session, 2026-07-12, ~20:2x SAST)

**Prompt (verbatim):**
> Please do.

**Summary:** Produced `Advisory-WP3-AnchorAndC1-2026-07-12.md` (proposed location
`cdot-8/WP3/`): endorsements ledger (directive 6 closed; exponent-check plan
endorsed as load-bearing; "replacing the eternal-past approach" and "where the
sourcing term is already small" corrected); §2 the two-legs analysis and the
anchor-as-implementation adoption, with the stated contingency (a forward-growing
mode in any traversed era makes the anchor choice physical — escalate) and the
eternal-past row required in the mode table; §3 the $C_1$ scaling argument
spelled out for worker verification, with the general per-era condition (clock
exponent $>0$ matter / $>1$ radiation) and the two consistency remarks (derived
principle and finite anchor agree; the flag-1(b) "hidden knob" never existed in
the theory as defined, per MM's own homogeneous-choice-is-part-of-the-definition
language); §4 sharpened ordering — the exponent table does triple duty (anchor
legitimacy, flag 1(c) discharge, the directive-5 stability check) and goes first,
species-resolved from the outset per flag 3; §5 directives; §6 protocol note
(primary-source discipline paid twice; checkpoint instinct right).

**Files produced (Entries 14–15):** `Advisory-WP3-AnchorAndC1-2026-07-12.md`,
`SessionLog-2026-07-12.md` (this file, fifteen entries, appended to the repo base
per the Entry-9 rule).

**Open items handed forward:** build the per-era homogeneous-mode exponent table
(matter, radiation, crossover, eternal past; rows $p_{\mathcal N}$, $p_R$, $C_1$;
species-resolved) — now the first blocking item; verify §3's scaling and record
$C_1=0$ as derived if confirmed (escalate if the radiation-era clock exponent
$\le1$); demonstrate anchor-insensitivity; then the quadrature redo against the
coefficient-$\tfrac12$ constraint and the step-5 confrontation with the flag-1(d)
invariance check; all prior directives (well-posedness 1–7, addendum flags 2–4)
in force; WP2 finalization still hard-blocking; WP4a/WP4b and consolidation-log
handoffs to cdot-7 unchanged; **the KATRIN clock remains the program's most
time-critical item.**

---

## Entry 16 — Sixth round: exponent-table escalation assessed (stand-in advisor session, 2026-07-12, ~20:4x SAST)

**Prompt (verbatim):**
> Worker wants advice on unexpected future history...
> cdot-8/WP3/Update-WP3-ExponentTable-2026-07-12.md

**Summary (stand-in advisor):** The worker executed the fifth-round directives
(verify $C_1$-exactness, then build the exponent table on the actual fitted
trajectory, both directions) and escalated a genuinely new finding: the
radiation-weighted homogeneous mode of $p_{\mathcal N}$ grows without bound
toward the deep-MOND future ($g_\text{rad}\to-\tfrac32$ as $x\to0$, mode
$\propto e^{+3s/2}$) — past regularity anchors the mode to zero but does not damp
later injections, on an eternal future. Assessment: **the table is right and the
forward direction was genuinely unchecked by every prior round — but the alarm
object is the bare multiplier, which is not the physical amplitude.** The
multiplier and its conjugate census component obey exactly mirrored equations
($\dot p=-gp$ homogeneous, $\dot{\mathcal N}=+g\mathcal N$), so
$d(p_{\mathcal N,i}\mathcal N_i)/dt=0$ exactly — per species, any trajectory, any
era — and every physical coupling of $p$ in the action (the $\delta g$
back-reaction channels) carries the product $p\mathcal N$, never $p$ bare. The
growing mode is the standard adjoint anti-mirror of the decaying radiation
census; the physical footprint of any injected kick freezes at
$\propto\mathcal N_\text{rad}(t_\text{inj})$ — marginal, not unstable, and within
MM's own accepted stability class. The worker's own numbers confirm both halves
(the $e^{+3s/2}$ is exactly $1/\mathcal N_\text{rad}$; the matter mode's $-0.96$
saturation is the convergent $\int3\kappa\lambda x\,ds$). The mis-specification
was the advisories' (bare-multiplier table rows), not the worker's. One genuine
caveat: the identity holds iff $p$ couples only through
$p(\dot{\mathcal N}-g\mathcal N)$ — a bounded coupling audit at
completed-action variation time, with the $(R_h,p_R)$ pair audited explicitly
(different constraint structure, not literally $p_RR_h$). Third instance of an
apparent pathology dissolving into an exact conservation statement
($\hat a_0\equiv E$; the $C_1$ row; the adjoint pairing).

---

## Entry 17 — Sixth-round advisory delivered (stand-in advisor session, 2026-07-12, ~20:5x SAST)

**Prompt (verbatim):**
> Yes

**Summary:** Produced `Advisory-WP3-AdjointInvariant-2026-07-12.md` (proposed
location `cdot-8/WP3/`): endorsements ledger ($C_1$ closure now fully verified,
Flag 1(c) closed derived; the forward-integration discipline named as exemplary;
§3's "unbounded amplification" corrected to bare-multiplier-only; the worker's
own mitigating consideration upgraded from "not yet a resolution" to the exact
resolution); §2 the one-line conservation identity and its adjoint-flow reading,
with the worker's own table columns shown to confirm both halves; §3 why this
closes the physical question (no bare-multiplier couplings, kicks fossilize at
injection weight, marginal = MM's accepted class, past regularity keeps exactly
its old job) and the upstream mis-specification owned by the advisories; §4 the
coupling audit as the one genuine caveat (bare couplings, $g_i(\mathcal N)$
dependence, the $(R_h,p_R)$ pair explicitly); §5 directives (verify identity,
recast the table in invariant variables plus transmission coefficients, carry
the audit as a named gate, escalation gate closed — proceed to the quadrature
redo); §6 protocol note: the escalation discipline caught an *advisor* error
this round — the system working in the direction it needs most.

**Files produced (Entries 16–17):** `Advisory-WP3-AdjointInvariant-2026-07-12.md`,
`SessionLog-2026-07-12.md` (this file, seventeen entries, appended to the repo
base per the Entry-9 rule).

**Open items handed forward:** worker verification of the §2 identity and the
mirror check on their own table columns; recast the stability exhibit in
invariant variables; the §4 coupling audit as a named gate at completed-action
variation; then the quadrature redo against the coefficient-$\tfrac12$ constraint
with $C_1=0$ and the step-5 confrontation with the Flag 1(d) invariance audit;
all prior directives (well-posedness 1–7, addendum flags 2–4, fifth-round order
of work) in force; WP2 finalization still hard-blocking; WP4a/WP4b and
consolidation-log handoffs to cdot-7 unchanged; **the KATRIN clock remains the
program's most time-critical item.**

---

## Entry 18 — Fifth-round assessment and closing addendum (advisor session, 2026-07-12, ~20:4x SAST)

*[Renumbered from a duplicate "Entry 16" during the 2026-07-13 log repair: the stand-in's Entries 16–17 and this advisor entry collided in the merge. Content unchanged. See SessionLog-2026-07-13.md Entry 1 for the repair record.]*

**Prompt (verbatim):**
> One more round, hopefully the last...
> [uploaded: `Update-WP3-MMPrimarySource-2026-07-12.md`,
> `Advisory-WP3-AnchorAndC1-2026-07-12.md`, current `SessionLog-2026-07-12.md`
> (Entries 1–15).]

**Summary (advisor):** Both documents endorsed without reversal. Worker: the
primary-source discipline closed directive 6 in full — a misattribution caught and
corrected, then Maggiore–Mancarella confirmed at full-text level *and* found to
hand over the needed method plus its counter-example; the checkpoint-before-
execution instinct right again. Stand-in: both corrections correct and important —
the deep-RD anchor *implements* past regularity rather than replacing it, and
MM's source-smallness leg does not transfer (the census never shuts off), so
anchor validity is contingent on the exponent check; §4's ordering (exponent
table first, triple duty) endorsed. **Sharpening contributed
(`Addendum-FifthRound-C1RowExact-2026-07-12.md`):** $Q=(1+z)^{5/3}$ is an *exact
identity on any trajectory* (both $Q=1/N=(c_0/c)^{5/2}$ and $1+z=(c_0/c)^{3/2}$
are exact functions of $c$), so $\rho_{C_1}\propto Q/a^3\propto(1+z)^{14/3}$
exactly, always — verified independently through the $F$-sector route including
the $\Delta F$ integral ($\Delta(F-QF_Q)=-\tfrac9{14}C_1Q^{14/5}$, same power).
Hence the $C_1$ row of the exponent table is a one-liner: the mode dominates
every era in the history (all stiffness $<14/3$, including the deep-past
radiation attractor), **past regularity forces $C_1=0$ unconditionally — Flag
1(c) closed in the derived direction, no K6 debt** — and directive 3's
radiation-era escalation contingency is struck (the clock exponent is $5/3$
identically, it cannot fire). Two honesty caveats: the constraint-route
*coefficient* ($-QC_1/6a^3$) rests on the LapseBackreaction document not uploaded
this round — scaling confirmed two ways, coefficient stays on the worker's
verification list; and the exactness shortcut covers the $C_1$ row only — the
$p_{\mathcal N}$/$p_R$ rows remain trajectory-dependent, their eternal-past
entries genuinely open, MM's counter-example still the standing warning there.

**Files produced (Entry 16):** `Addendum-FifthRound-C1RowExact-2026-07-12.md`,
`SessionLog-2026-07-12.md` (this file, sixteen entries, appended to the repo base
per the Entry-9 rule).

**Open items handed forward:** worker verification of the exactness argument and
the constraint coefficient; the $p_{\mathcal N}$/$p_R$ exponent table
(species-resolved, eternal-past row included); anchor-insensitivity demonstration;
quadrature redo against the coefficient-$\tfrac12$ constraint with $C_1=0$; the
step-5 confrontation with the Flag 1(d) invariance audit (now the last place a
hidden knob could hide); WP2 finalization still hard-blocking; WP4a/WP4b and all
cdot-7 consolidation-log handoffs unchanged; **the KATRIN clock remains the
program's most time-critical item.**
