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

## Entry 7 — A candidate exchange term, and a well-posedness snag (2026-07-12)

**Prompt (verbatim):**
> A response from the proposer has been added.

(Reference: `cdot-8/proposal/Advisory-WP3-TouchPoint-ExchangeTarget-2026-07-12.md`,
a touch-point response — no escalation, no major flags — to Entry 6's update,
sharpening the exchange-term's target into three equivalent forms and
pre-dimensioning the shell-sweep candidate.)

**Summary of work performed:**

1. **Independently re-verified all three of the touch-point advisory's claims**
   before using them: the three-equivalent-forms algebra ($QF_Q=\rho_\phi+p_\phi$
   confirmed as a pure identity, residual $4\times10^{-16}$; the
   (ii)$\Leftrightarrow$(iii) calculus step confirmed, residual $1.6\times10^{-9}$);
   the consistency check against Entry 6's own identity (confirmed by hand,
   reproduces $-\dot p_\phi$ exactly); the shell-sweep dimensioning ($9/10$ ratio,
   every intermediate step re-derived and matching).

2. **Stated the aether-normalization convention explicitly, before varying anything**
   (touch-point directive 4): $A^\mu A_\mu=-1$ with respect to $g_{\mu\nu}$, the
   single AeST metric — no disformal $\hat g$, per WP1's earlier finding.

3. **Constructed a candidate action-level term**: promoted the census $\mathcal N$ to
   an auxiliary dynamical variable via a Lagrange multiplier enforcing WP2's own
   evolution equation, plus a second multiplier tying $Q$ to $\mathcal N$ (M2/M5's
   content). Varying w.r.t. $\phi$ gives a genuinely modified equation of motion,
   $\frac{d}{dt}(a^3F_Q)=16\pi\tilde G\frac{d}{dt}(\Lambda_M/N)$ — explicitly sourced,
   as intended, with matter's own action ($S_m[g]$) untouched throughout (touch-point
   directive 1 satisfied by construction).

4. **Found a well-posedness snag**: varying w.r.t. $\mathcal N$ gives an independent,
   undetermined equation for the census multiplier's own dynamics — two new
   multipliers were introduced to enforce what is physically one constraint,
   under-determining the system. Proposed a second candidate (using WP2's closed-form
   solution for $\mathcal N(t)$ directly as a nonlocal functional of $a(\cdot)$'s
   history, anchored only at the one measured value $\mathcal N(t_0)\leftrightarrow
   \Omega_\text{closure}=0.074$, with a single multiplier) that avoids the extra
   freedom but requires a genuine nonlocal/functional variation not yet carried out.

5. **Recommended a touch point rather than pushing further alone** — this specific
   fork (which construction is the physically correct one) seemed better served by a
   second read than by continuing to iterate solo, mirroring the advisor's own
   touch-point pattern from Entries 7–8.

**Files produced:** `Update-WP3-ExchangeTermAttempt-2026-07-12.md`, this entry.

**Open items handed forward:** resolution of the two-candidate fork (auxiliary-field
vs. nonlocal-functional); the stability/zero-crossing joint check and WP2
finalization, both appropriately deferred until a well-posed construction is settled
on. cdot-7's own priority queue, above all the KATRIN clock, remains unstarved and
untouched.

---

## Entry 8 — The fork dissolves; a new back-reaction finding (2026-07-12)

**Prompt (verbatim):**
> proposal updates delivered. Please proceed.

(Reference: `Advisory-WP3-ExchangeTermWellPosedness-2026-07-12.md` — the fork from
Entry 7 dissolves, candidate A and B are one construction under standard nonlocal-
gravity localization, resolved via a past-regularity boundary condition; plus
`Addendum-FourthRound-C1NotGauge-2026-07-12.md` — a required correction: the
integration constant $C_1$ is not gauge, it is the native dust mode, and must be
fixed by a stated principle before the confrontation.)

**Summary of work performed:**

1. **Delegated and completed citation verification** (directive 6): Deser & Woodard
   (arXiv:0706.2151), Maggiore & Mancarella (arXiv:1402.0448), and Galley (PRL 110,
   174301) all confirmed real and supporting the claims made about them (localization/
   homogeneous-mode/retarded-prescription machinery; the doubled, equate-at-final-time
   variational principle), with appropriately noted confidence caveats where full text
   wasn't accessible.

2. **Independently reproduced all "cheap algebra" claims**: the sign check across the
   traversed $x$-range, the three-faces-of-$9/10$ exponent arithmetic, and the trivial
   integration of the $\phi$-equation — all confirmed exactly.

3. **Attempting directive 4 (run the confrontation with $\Lambda_M$ as algebraic
   input) surfaced a finding neither prior document caught**: $S_{M5}$ has its own,
   explicit lapse-dependence and therefore back-reacts directly on the Hamiltonian/
   Friedmann constraint, not only on the $\phi$-equation — something both of this
   session's own prior updates missed (they tracked only $S_\phi$'s contribution to
   $\delta S/\delta N$). Verified term-by-term against finite differences (each of
   $S_\text{EH}$, $S_m$, $S_\phi$, $S_{M5}$'s own contributions individually, then the
   full algebraic combination) before trusting it — caught and corrected one flawed
   self-check along the way (comparing two sides that only need to agree once the
   constraint is actually imposed, not for arbitrary unconstrained inputs).

4. **Result**: the complete Hamiltonian constraint has the $QF_Q$ coefficient shifting
   from $\tfrac13$ (every prior round's implicit assumption) to $\tfrac12$, plus a new,
   explicit $C_1$-dependent term. This means the specific reconstructed $F(Q)\propto
   Q^{9/5}$ from the third/fourth escalations was solved against an incomplete version
   of the constraint and needs re-solving — and, promisingly, $S_{M5}$'s own
   back-reaction may already be the missing energy-exchange channel the previous
   update went looking for externally via the shell-sweep hypothesis, without needing
   a separately bolted-on term.

5. **Did not redo the quadrature yet** — flagged this as a natural checkpoint given
   how much shifted in a single pass, rather than compounding a possibly-still-
   incomplete picture with more downstream construction.

**Files produced:** `Update-WP3-LapseBackreaction-2026-07-12.md`, this entry.

**Open items handed forward:** re-solve the $F(Q)$ quadrature against the corrected
(coefficient-$\tfrac12$, $C_1$-inclusive) Hamiltonian constraint; re-derive the razor
success criterion using the complete stress-energy (φ-sector plus $S_{M5}$'s own
$a$-variation, not yet computed); Flag 1's $C_1$-determination (past regularity vs.
census exhaustiveness) now feeds directly into this re-solve rather than being
separable from it. cdot-7's own priority queue, above all the KATRIN clock, remains
unstarved and untouched — nothing in `cdot-7/` was edited.

---

## Entry 9 — Primary-source review of the citations (2026-07-12)

**Prompt (verbatim):**
> I have added arXiv.0706.2151.tex and arXiv.1402.0448/ as full source downloads to
> the reference folder. Please review and update.

**Summary of work performed:**

1. **Read the full Deser & Woodard (arXiv:0706.2151) source directly.** Found and
   corrected an overclaim in Entry 8's delegated citation check: this specific 2007
   letter does *not* use auxiliary-field-plus-Lagrange-multiplier localization (no
   auxiliary field, no multiplier, no "homogeneous mode" language appears anywhere in
   its text) — its own method is direct substitution of the retarded Green's function
   for the advanced one in the equations from naive variation, justified by citing
   Soussa & Woodard (2003) and, in a footnote, the Schwinger-Keldysh/in-in formalism.
   The auxiliary-field technique is real and standard in this literature but belongs
   more precisely to later papers (reportedly including Maggiore & Mancarella's own
   construction) — attributing it to *this* paper specifically was imprecise, now
   corrected.

2. **Found a genuine, useful connection** only visible from the primary text: this
   paper's own causality justification (Schwinger-Keldysh/in-in) is the same lineage
   as Galley's later classical "doubled" variational principle — two of the three
   cited papers share a causality principle, not merely a subject area, a stronger
   justification for invoking them together than previously stated.

3. **Found `references/arXiv.1402.0448/` is empty** — confirmed by direct directory
   listing, not a passing glance. The Maggiore & Mancarella source was not actually
   delivered; that citation remains at its earlier, abstract-level confidence, and the
   auxiliary-field technique this session's own construction most closely resembles is
   still unverified against primary source.

**Files produced:** `Update-WP3-CitationPrimarySource-2026-07-12.md`, this entry.

**Open items handed forward:** re-add the actual Maggiore & Mancarella source files
(the directory exists but is empty); all Entry 8 open items (re-solve the $F(Q)$
quadrature against the corrected Hamiltonian constraint) unchanged and still pending.
cdot-7's own priority queue, above all the KATRIN clock, remains unstarved and
untouched.

---

## Entry 10 — Maggiore & Mancarella, re-delivered and fully verified (2026-07-12)

**Prompt (verbatim):**
> Try again on the arXiv.1402.0448. The files failed to extract.

**Summary of work performed:**

1. **Re-checked the directory** — the source files were present this time
   (`paperMM160314.tex` and companions). Read the full paper.

2. **Confirmed the auxiliary-field-plus-two-multipliers localization exactly as the
   well-posedness advisory described** — this citation, unlike Deser-Woodard, was
   correctly attributed the first time; now verified at full primary-source level, not
   just abstract. The paper's own account of the homogeneous-mode issue ("all other
   solutions of the local formulation are spurious... whatever definition one takes for
   $\Box^{-1}$, the corresponding homogeneous solution is uniquely fixed") matches the
   "candidate A's extra freedom is B's boundary-condition ambiguity relocated"
   diagnosis precisely.

3. **Found something directly useful for this project's own open problem**: rather
   than an abstract eternal-past limit, the paper fixes its own homogeneous-mode
   ambiguity practically — anchoring at a finite initial time deep in radiation
   domination, where the sourcing curvature term is already small, and *explicitly
   checks* (not merely assumes) that the homogeneous modes decay or stay bounded
   across radiation domination, matter domination, and a preceding inflationary stage
   — while flagging, as a real counter-example, that a closely related model of
   theirs is stable in RD/MD but *not* in an inflationary era, i.e. this kind of
   stability does not come for free and must be checked per-construction.

4. **Adopted their method as the concrete plan for Flag 1** (the $C_1$/$p_{\mathcal
   N}$ determination): anchor at a deep-radiation-era initial condition rather than an
   eternal-past analytic limit, and run their same homogeneous-mode exponent check on
   this project's own $g(t)$ across the matter, radiation, and crossover eras before
   trusting any result — not yet executed, reported as the concrete next step.

**Files produced:** `Update-WP3-MMPrimarySource-2026-07-12.md`, this entry.

**Open items handed forward:** execute the adopted plan — re-solve the $F(Q)$
quadrature against the corrected Hamiltonian constraint (Entry 8), fixing $C_1$ via
the Maggiore-Mancarella-style deep-RD initial condition, then run their homogeneous-
mode stability check on this project's own trajectory before trusting the result.
cdot-7's own priority queue, above all the KATRIN clock, remains unstarved and
untouched.

---

## Entry 11 — The exponent table finds a future-directed instability (2026-07-12)

**Prompt (verbatim):**
> Advice added to proposal.

(Reference: `Advisory-WP3-AnchorAndC1-2026-07-12.md` — the deep-RD anchor is an
*implementation* of past regularity, not a replacement, and only one of Maggiore-
Mancarella's two legs transfers; a scaling argument suggesting $C_1=0$ comes out
derived rather than adopted. Plus `Addendum-FifthRound-C1RowExact-2026-07-12.md` —
sharpening the $C_1$ scaling into an exact, era-independent identity, striking one
contingency, and reporting the program has, for the first time, exactly zero
adjustable elements pending two bounded verifications.)

**Summary of work performed:**

1. **Verified the $C_1$-exactness claims independently** — $Q=(1+z)^{5/3}$ and
   $a^3=Q^{-9/5}$ confirmed exact (not fixed-point-specific) on a numerical grid
   spanning $c/c_0\in[0.3,3.0]$, catching and correcting one of my own algebra slips
   along the way (briefly inverted a WP1 exponent) before trusting the result. The
   $F$-sector cross-check reproduced by hand. $C_1=0$ via past regularity confirmed
   exact and era-independent.

2. **Built the per-era homogeneous-mode exponent table for $p_{\mathcal N}$**, per
   directive, using the actual fitted census trajectory (not just the two fixed
   points) — extended the well-posedness advisory's own sign check across the full
   crossover *and*, for the first time in this program, into the **future** branch,
   which no prior round had checked.

3. **Found a genuine, unanticipated problem**: the radiation-weighted homogeneous
   mode does not decay toward the future — it grows without bound, asymptotically as
   $e^{+3s/2}$, as the trajectory slides into the deep-MOND future (the physical,
   $\delta_0<0$ branch's own documented behavior). The matter-weighted mode, checked
   the same way, does decay forward. Also found the radiation-weighted mode's
   backward-direction sign is slightly *negative* right at $z=0$ (today sits just
   below the critical operating point $x=1.148$), a narrow feature the two-fixed-
   point-only check could not see.

4. **This is exactly the "instability lands somewhere unanticipated" pattern both
   advisories warned about, but in a different place**: both directed concern at the
   eternal past; the actual problem found is future-directed and radiation-specific.
   Noted a mitigating consideration (radiation's own amplitude is negligible at low
   $z$ and beyond) without resolving whether it rescues the construction.

5. **Escalated rather than proceeding to the quadrature redo** — this finding could
   be a real, first-principles obstruction to the species-resolved construction, or
   an artifact of treating a dynamically irrelevant sector's multiplier as
   significant; redoing the quadrature while this is open risks building on an
   unstable foundation twice over.

**Files produced:** `Update-WP3-ExponentTable-2026-07-12.md`, this entry.

**Open items handed forward:** resolution of the future-directed radiation-mode
instability (real problem vs. artifact of an irrelevant sector); the quadrature
redo remains on hold pending this. cdot-7's own priority queue, above all the KATRIN
clock, remains unstarved and untouched.
