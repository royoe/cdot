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
