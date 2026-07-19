# Session Log — cdot-8/WP3 (2026-07-13)

*New calendar date, new file, continuing from `SessionLog-2026-07-12.md` (eleven
entries). Same per-prompt logging convention.*

---

## Entry 12 — Adjoint invariant verified; quadrature redo surfaces a second constant (2026-07-13)

**Prompt (verbatim):**
> Please check for proposal update advisory and addendum.

(Reference: `Advisory-WP3-AdjointInvariant-2026-07-12.md` — the future-growing
radiation mode found in Entry 11 is real but aimed at the wrong object: the
multiplier and the census component it constrains obey mirrored equations, so
$p_{\mathcal N,i}\mathcal N_i$ is exactly conserved per species; the mode is marginal,
not unstable, and the escalation gate closes subject to a coupling audit. Plus
`Addendum-AdjointRound-CoupledInvariant-2026-07-13.md` — sharpening the coupling
audit to the full coupled symplectic spectrum (since M5's closure makes every $g_i$
depend on the background), pre-verifying one audit row, and noting the program now
has two coexisting priors — corrections-on-second-read, and alarms-dissolving-into-
identities — with neither entitled to decide a round on its own.)

**Summary of work performed:**

1. **Independently verified the adjoint identity** $\frac{d}{dt}(p_{\mathcal N,i}
   \mathcal N_i)=0$ before accepting it: built $\mathcal N_\text{rad}(s)$ and
   $p_{\mathcal N,\text{rad}}^\text{hom}(s)$ from the same shared $g_\text{rad}(s)$
   independently and checked their product directly — constant to $2\times10^{-16}$
   across the whole forward trajectory. Entry 11's "instability" is confirmed to be
   the bare multiplier's adjoint growth exactly compensating the census component's
   decay, not a physical runaway — the escalation gate closes as both advisors found.

2. **Proceeded to the cleared quadrature redo**: solved $\tfrac12QF_Q-\tfrac13F=
   \Omega_s(a)$ (the corrected, coefficient-$\tfrac12$, $C_1=0$ constraint) as a
   linear ODE for $F(Q)$. Caught and fixed a numerical-integration error along the
   way (naive trapezoidal integration directly in $Q$, which spans ten orders of
   magnitude, produced spurious noise at high $z$; redone properly on the uniform,
   well-resolved $s$-grid). Matter-era power law comes out $F\propto Q^{1.77}$,
   close to but not exactly the prior round's $Q^{9/5}$.

3. **Found a second, previously undiscussed integration constant.** With the
   arbitrary choice of anchoring the integral at today, $F(Q)$ changes sign and
   diverges in the deep radiation era — traced to the invoice's own small-negative
   radiation-era value, weighted by $Q^{-2/3}$, giving a genuinely divergent
   integrand ($\propto a^{-26/9}$), not a numerical artifact. This constant ($C_2$,
   the homogeneous solution $F\propto Q^{2/3}$ of *this* corrected ODE) is distinct
   from $C_1$ (which entered the earlier, different integrated $\phi$-equation and
   was resolved by past regularity acting on its $a^{-3}$ dust-like scaling) — $C_2$
   only appears once the quadrature is actually solved, which no prior round had
   done.

4. **Did not fix $C_2$ by convenient assumption.** Flagged that its milder
   ($a^{-10/9}$) scaling might look subdominant by a naive comparison to radiation,
   but the $C_1$ episode already showed "looks subdominant" is not the same as
   "harmless" once correctly weighted — the same disciplined treatment ($C_1$'s
   past-regularity derivation, or the Maggiore-Mancarella deep-RD anchor) is needed
   here too, not yet attempted.

**Files produced:** `Update-WP3-QuadratureRedo-2026-07-13.md`, this entry.

**Open items handed forward:** determine $C_2$ properly (past-regularity scaling
argument or deep-RD anchor, per the established discipline) before trusting the
reconstructed $F(Q)$'s radiation-era behavior; the coupling audit (three items from
the adjoint-invariant round, one pre-seeded) still pending, to be discharged when the
action is closed over dynamical variables; WP2 finalization still hard-blocks.
cdot-7's own priority queue, above all the KATRIN clock, remains unstarved and
untouched — nothing in `cdot-7/` was edited.

---

## Entry 13 — $C_2$ is the kernel, not another $C_1$: confirmed (2026-07-13)

**Prompt (verbatim):**
> Review uploaded.

(Reference: `Advisory-WP3-C2Kernel-2026-07-13.md`, a sole-advisor round — the
stand-in was unavailable this round. Resolution: $C_2$ multiplies the kernel of the
*corrected* Hamiltonian constraint operator, $\tfrac12QF_Q-\tfrac13F$; it carries
identically zero background energy density and is subdominant in both time
directions, so no past-regularity or anchor argument applies or is needed — the
"divergence" Entry 12 reported is the particular solution correctly tracking the
invoice's own zero-crossing, with closed-form coefficients. $C_2$ is to be carried
symbolically into the still-pending step-5 confrontation, not zeroed now. A
three-slot constant taxonomy — current/kernel/multiplier, each with its own correct
treatment — was recorded for reuse.)

**Summary of work performed:**

1. **Independently verified every load-bearing claim before accepting the
   resolution** — did not treat the advisory's own thorough verification as a
   substitute for doing it myself: re-derived the closed-form attractor ratios from
   scratch ($30/17$ matter, $15/13$ radiation, both matching to all digits shown);
   confirmed the kernel property ($Q^{2/3}$ solves the corrected homogeneous
   equation, residual $2.3\times10^{-10}$); and, on my own independent trajectory
   computation (not the advisory's script), confirmed $C_2$'s background
   invisibility by varying it from $-500$ to $+100$ and finding the deep-past
   $F(z=2\times10^6)$ unchanged to 8 decimal places.

2. **Corrected my own prior document in place**: the $\rho\propto a^{-10/9}$ figure
   in `Update-WP3-QuadratureRedo-2026-07-13.md` was the old, $\phi$-sector-only
   accounting; under the corrected accounting this construction actually uses, the
   mode's constraint contribution is zero, not merely small — noted explicitly
   rather than silently amended.

3. **Adopted the constant taxonomy** (current constants → regularity; kernel
   constants → step-5 audit; multiplier constants → adjoint pairing + anchor) as a
   standing classification tool for this construction.

**Files produced:** `Update-WP3-C2KernelConfirmed-2026-07-13.md`, this entry;
correction applied in place to `Update-WP3-QuadratureRedo-2026-07-13.md`.

**Open items handed forward:** the coupling audit (three items, one pre-seeded,
from the adjoint-invariant round) and the step-5 confrontation itself — the
$(C_2,\Lambda_M)$ invariance check, now the last unexamined slot in the whole
construction — both substantial, not yet attempted. WP2 finalization still
hard-blocks. cdot-7's own priority queue, above all the KATRIN clock, remains
unstarved and untouched.

---

## Entry 14 — Action closed over dynamical variables; coupling audit discharged; a new back-reaction on the Hamiltonian constraint (2026-07-13)

**Prompt (verbatim):**
> Go for open WP3 items...

(Authorization to proceed with the two standing WP3 items: the coupling audit and
the step-5 confrontation.)

**Summary of work performed:**

1. **Closed the action over dynamical variables for the first time in the
   program**: species-resolved census pairs $(\mathcal N_i,p_i)$, $R_h$ promoted
   to a dynamical variable with its own multiplier $p_R$ via $\dot R_h=Nc$, $c$
   expressed through the WP1 dictionary rather than as an external function. Stated
   the lapse-covariance convention explicitly before varying (per flag-3/flag-6
   practice) and showed it is the *unique* choice reproducing both WP2's $N=1$
   formula and the addendum's independently pre-verified row — not an arbitrary
   pick among options.

2. **Verified every new equation of motion against an actual solved coupled
   system** (not paper algebra alone, per this program's established discipline):
   $\delta S/\delta N$'s new terms (residual $1.3\times10^{-9}$), $\delta S/\delta
   R_h$ (residual $3.3\times10^{-11}$), the sourced identity $\dot\pi_i=-\Lambda_M
   q'(\mathcal N_\text{tot})\mathcal N_i$ with $\pi_i\equiv p_i\mathcal N_i$ (on an
   actual integrated trajectory, residuals $\sim10^{-10}$), and $p_R$'s own
   sourcing equation $\dot p_R=(Nc/R_h^2)\sum_i\pi_i$ (full six-variable coupled
   solve, residuals $\sim10^{-11}$).

3. **Discharged all three coupling-audit items with concrete answers, not
   assumptions**: item 1 (no bare-multiplier couplings) passes for the species
   multipliers $p_i$ by a general structural argument, but **fails for $p_R$**,
   which appears bare in the Hamiltonian constraint — flagged as a genuinely
   different kind of check (boundedness of $p_R(t)$ itself, not adjoint-pairing
   protection). Item 2 (coupled symplectic spectrum, per the addendum's
   sharpening): confirmed the species multipliers couple to each other through
   $S_{M5}$'s shared source term exactly as anticipated, with no hidden
   $g_i(\mathcal N)$ dependence and no pairing-breaking term found. Item 3
   ($(R_h,p_R)$, explicitly not by analogy): resolved as a **pure sourced
   integral**, structurally unlike the species pairs (no homogeneous mode for
   either $R_h$ or $p_R$), needing its own past-regularity anchor.

4. **Found a new back-reaction on the Hamiltonian constraint**: the newly-closed
   $S_{\mathcal N}$ and $S_{R_h}$ sectors add a term $\frac{8\pi G}{3a^3}[\sum_i
   \pi_i\,c/R_h+p_Rc]$ to the same boxed constraint the $S_{M5}$ back-reaction
   already modified once (LapseBackreaction round). This term has never appeared
   in any prior round's Friedmann-constraint derivation, including the
   just-confirmed $C_2$-kernel quadrature. **Deliberately did not attempt a
   from-memory numerical magnitude estimate** — doing so with recalled-but-
   unverified AQUAL machinery risked manufacturing a false reading; flagged
   instead as the concrete next numerical step, to be done with the actual
   `census_closure.py`/`quadrature_c2.py` machinery.

**Files produced:** `Update-WP3-ClosedActionCouplingAudit-2026-07-13.md`, this
entry; verification script in session scratchpad (not part of the permanent
record).

**Open items handed forward:** the magnitude of the new $\pi_i,p_R$ back-reaction
term — this determines whether the quadrature needs re-solving a third time
before the razor/total-Bianchi confrontation (step 5 proper) is meaningful.
Recommend a check-in before attempting step 5, mirroring the LapseBackreaction
precedent: building the razor check on a constraint that might shift again would
repeat the mistake the checkpoint discipline exists to catch. WP2 finalization
still hard-blocks. cdot-7's own priority queue, above all the KATRIN clock,
remains unstarved and untouched — nothing in `cdot-7/` was edited.

---

## Entry 15 — The back-reaction magnitude advisory has a normalization bug: corrected, effect roughly doubles (2026-07-13)

**Prompt (verbatim):**
> Response uploaded to proposal

(Reference: `Advisory-WP3-BackreactionMagnitude-2026-07-13.md` +
`backreaction_magnitude.py`, sole-advisor round. Endorsed the closed action and
all three coupling-audit dispositions; computed the deferred magnitude with the
real trajectory machinery — claimed $D/E^2$ peaking at $-4.85\%$ at $z=0$,
negligible at recombination and beyond, one perturbative iteration sufficing.)

**Summary of work performed:**

1. **Did not accept the magnitude figure without an independent cross-check**,
   per standing protocol. Re-derived the advisory's own working relation
   ($q'(\mathcal N_\text{tot})\mathcal N_\text{tot}=(dQ/ds)/\bar g$) from my own
   verified equations and confirmed it is exactly right — a genuinely elegant,
   parametrization-free trick. But traced the equation it feeds
   ($\dot\pi_\text{tot}=\tfrac52\Lambda_MQ/\bar g$) back to its source and found
   it is a $d/dt$ equation, not $d/ds$ as the advisory's script integrates it —
   missing one factor of $\dot s=\tfrac23NE$.

2. **Verified this three independent ways** before reporting it: (a) careful
   hand tracking of every $d/dt\leftrightarrow d/ds$ conversion; (b) built a
   genuine coordinate-time axis by numerically integrating $dt=ds/\dot s$ on the
   actual trajectory and re-integrated the unambiguous $dt$-form directly,
   confirmed against the $\dot s$-corrected $ds$-integration to $10^{-6}$
   relative precision; (c) confirmed the separate algebraic step (converting
   $\tilde\pi,P$ into constraint contributions) is untouched — the bug is
   isolated to the time-integration of $\tilde\pi,P$ alone, not the audit
   dispositions or the closed-action validations.

3. **Corrected magnitude**: peak (still at $z=0$) is $D/E^2\approx-9.5\%$ to
   $-10.3\%$ after iteration — roughly double the advisory's $-4.85\%$. Ran the
   perturbative iteration with the corrected formula: converges within two
   passes ($7.4\%$ then $0.4\%$ relative shifts), confirming the "perturbative,
   not structural" verdict survives even though the absolute size roughly
   doubles. WP4a/WP4b remain untouched at $10^{-7}$ and $10^{-11}$ respectively —
   the correction does not reopen either promoted check.

**Files produced:** `Update-WP3-BackreactionMagnitudeCorrected-2026-07-13.md`,
this entry; verification scripts in session scratchpad.

**Open items handed forward:** requested the advisor independently re-check the
$\dot s=\tfrac23NE$ factor and the $t(s)$ cross-check before this correction is
taken as final — a factor-of-2 discrepancy feeding step 5 deserves a second
confirmation, per the same courtesy every prior correction in this program has
received in both directions. Pending that: proceed to step 5 on the
twice-iterated $\Omega_s^\text{corr}$. WP2 discharge-by-incorporation proposal
not yet assessed. WP2 finalization still hard-blocks; the KATRIN clock remains
the program's most time-critical item; nothing in `cdot-7/` was edited.

---

## Entry 16 — Correction confirmed bilaterally; step 5 formally cleared (2026-07-13)

**Prompt (verbatim):**
> Check for update.
> Right. Uploaded now. Try again

(Reference: `Advisory-WP3-MagnitudeCorrectionConfirmed-2026-07-13.md` +
`backreaction_corrected.py` — the advisor's independent re-derivation and
from-scratch rebuild of the $t$-axis gold-standard method, confirming the
normalization correction reported in Entry 15.)

**Summary of work performed:**

Ran the advisor's confirmation script myself before accepting the confirmation
at face value (same discipline applied to a confirmation as to any other
claim): reproduced all seven $D/E^2$ table points to the advisor's quoted
precision, the gold-standard $t$-axis agreement ($1.5\times10^{-4}$), and the
two-pass iteration deltas ($7.38\%$, then $0.40\%$, converging to
$D_2/E^2=-1.028\times10^{-1}$ at $z=0$) — exact match, no discrepancies. The
advisor owned the bug plainly (named mechanism: "a booby-trapped expression...
whose Jacobian factors have cancelled internally, leaving a rate that reads as
axis-free"), confirmed WP4a/WP4b remain untouched, and clarified that M7's
invoice $\Omega_s=E^2-\Omega_\text{census}$ itself never changed — only the
internal decomposition between the $F$-sector and the multiplier sectors did.

**Files produced:** this entry (no new update document — a verification pass on
an already-complete correction, not a new finding).

**Status: step 5 is now formally cleared on both sides**, on the twice-iterated
constraint $\Omega_s^\text{corr}=\Omega_s-D_2$ (peak correction $-10.3\%$ at
$z=0$), with the full ledger specified: the $\pi_i$/$p_R$ sectors' own
continuity contributions, the acceleration-equation channel (from $g_i$'s
$\dot a$-dependence, named but not yet built), and the $(C_2,\Lambda_M)$
invariance audit, $C_2$ carried symbolically throughout. This is the entire
remaining WP3 queue. WP2 discharge-by-incorporation still awaits explicit
confirmation (proposed: fold WP2 into the closed action's $S_{\mathcal N_i}$
constraints rather than tracking it as a separate deliverable). WP4a/WP4b
otherwise unblocked. The KATRIN clock remains the program's most time-critical
item; nothing in `cdot-7/` was touched.

---

## Entry 17 — Step 5 run: three items close cleanly, the $(C_2,\Lambda_M)$ audit finds a genuine unfixed free parameter (2026-07-13)

**Prompt (verbatim):**
> Go for step 5!

**Summary of work performed:**

1. **Acceleration-equation channel**: derived $S_{\mathcal N}+S_{R_h}$'s
   contribution to $\delta S/\delta a$ (the named, not-yet-built ledger item),
   verified via nested finite differences on synthetic test functions,
   converging to $\sim10^{-7}$ relative residual as step size is refined —
   closes this item.

2. **Total-Bianchi closure**: recognized as structurally guaranteed once every
   individual equation of motion is independently verified (a consequence of
   general covariance, not a separate result to manufacture) — stated honestly
   as such rather than oversold as new numerics.

3. **The razor**: holds by construction at every iteration (the quadrature is
   solved specifically to make it hold) — but recognized this means it is
   satisfiable for *any* $C_2$, so it is not, on its own, an independent test.

4. **The $(C_2,\Lambda_M)$ invariance audit — the substantive result**: ran the
   iterated construction with $C_2$ carried explicitly (not reset to zero) for
   several trial values, converged to full numerical stability (8 passes).
   **$C_2$ does not cancel.** $D/E^2$ at $z=0$ swings from $-0.103$ ($C_2=0$) to
   $+0.113$ ($C_2=10$) to $+0.974$ ($C_2=50$) — an order-unity, physically
   consequential effect on the energy-budget decomposition, even though the
   *fitted background* $E(a)$ itself never changes (protected by construction).
   Checked whether "$D\equiv0$ at all times" could fix $C_2$: **no single $C_2$
   zeros $D$ at more than one redshift** (checked five points, $z=2$ to $z=0$) —
   ruling out the one internal candidate closure condition available. This is
   exactly the scenario the C2Kernel advisory itself flagged as the failure
   mode ("$C_2$ surviving in observables without being selected... is precisely
   a failure of the razor").

**Files produced:** `Update-WP3-Step5Confrontation-2026-07-13.md`, this entry;
verification scripts in session scratchpad.

**Status: not a unilateral kill.** Reported per the program's standing
discipline — verified three ways, not resolved alone. Candidates for what
might still fix $C_2$: an unexplored boundedness condition on $\Lambda_M,\pi_i,
p_R$ (e.g. future-boundedness, analogous to $C_1$'s past-regularity); a
physical requirement this background-only analysis can't see; or genuine,
irreducible freedom (an honest but consequential outcome for the "zero
adjustable parameters" claim). **Recommend a touch point before proceeding
further** on this specific question, mirroring the pattern that resolved the
well-posedness snag and the exchange-term construction. WP2
discharge-by-incorporation still pending; WP4a/WP4b unaffected. The KATRIN
clock remains the program's most time-critical item; nothing in `cdot-7/` was
touched.

---

## Entry 18 — Sign bug confirmed, forward divergence reproduced, scheme test 1 clears, the real ambiguity found in my own construction (2026-07-15)

**Prompt (verbatim):**
> Update uploaded.

(Reference: `Advisory-WP3-Step5Audit-SchemeTest-2026-07-13.md` +
`c2_future_audit.py` — advisor confirmed and extended the $(C_2,\Lambda_M)$
finding: owns a second, independent sign bug in the magnitude scripts
(propagated from the original delivery); reproduces the audit and extends it
**forward** to $s=3$, finding both channels diverge into the deep-MOND future
with unequal slopes, so no constant $C_2$ bounds the future either — "the
program's first non-dissolving alarm"; proposes $D$ is
**scheme-dependent** (Lagrange-multiplier rescaling + past-regularity
interacting badly when the rescaling factor is unbounded) as the likely
resolution, with a decisive two-branch test assigned.)

**Summary of work performed:**

1. **Independently confirmed the sign bug**: reproduced $F/\Omega_s=-1.797$
   (wrong sign) via a direct probe of what my own `cumulative_trapezoid`
   construction actually computes ($\int_0^s$, contradicting my own code's
   comment). Fixed and confirmed $+30/17$ recovered. **Flagged one nuance the
   advisor's writeup didn't cover**: the *un-iterated* $D$ simply flips sign as
   claimed, but the *fully-iterated, converged* $D$ shifts in **magnitude** too
   ($0.0888$ vs. $0.1029$, $\sim14\%$) — the iteration isn't symmetric under
   $D\to-D$.

2. **Reproduced the forward-divergence finding exactly** by running
   `c2_future_audit.py` directly — matched every number to the digit, no
   discrepancy.

3. **Ran scheme test 1** (uniform $N$ multiplying the whole constraint
   bracket, the advisory's specific proposal): derived the rescaled
   Euler-Lagrange equation directly, found the homogeneous mode is
   $p_i^\text{hom}/N$ — since $p_i^\text{hom}$ already diverges as
   $t\to-\infty$ and $N\to0$ there, dividing makes it diverge *faster*, so
   past regularity selects the identical solution in both schemes. Verified on
   a synthetic solved system (residuals $\sim10^{-13}$). **This specific
   rescaling is scheme-invariant — does not explain the finding.**

4. **Found the real ambiguity by re-examining my own prior work**: my claim in
   `Update-WP3-ClosedActionCouplingAudit-2026-07-13.md` that the lapse
   placement inside $g_i$ was "the unique choice" was underjustified — the
   addendum's pre-verified row is blind to *which* functional form of $g_i(N)$
   is used, so it never actually distinguished my choice from the equally
   valid alternative of multiplying the *entire* $g_i$ bracket by $N$
   (weight-drift term included, not just shell-sweep). $\pi_i(t)$ itself is
   identical under either choice (the $g_i$-dependence cancels structurally,
   for any $g_i$), but $\partial g_i/\partial N$ — which the constraint
   contribution actually uses — differs between the two schemes for radiation
   (not for matter, whose weight-drift term vanishes identically). **This is a
   sharper, concrete candidate mechanism, distinct from the advisory's general
   hypothesis**, not yet numerically closed since it requires species-resolved
   $\mathcal N_i(t)$ trajectories not yet built (deliberately not
   reconstructed from memory, per the standing discipline).

**Files produced:** `Update-WP3-SchemeTestPartial-2026-07-15.md`, this entry;
verification scripts in session scratchpad.

**Status: not a kill, not a resolution.** Scheme test 1 (as specifically
proposed) closes with a negative result. The more promising lead is the
$g_i$-internal lapse-placement ambiguity found this round — recommend this
replace the originally-assigned M5-orientation-flip test as the next concrete
step, pending species-resolved census machinery. WP2 discharge-by-incorporation
still held. WP4a/WP4b unaffected regardless of outcome. The KATRIN clock
remains the program's most time-critical item; nothing in `cdot-7/` was
touched.

---

## Entry 19 — Advisor's "WP3 closes positive" resolution: observable-level claim confirmed, "D is purely gauge" claim not yet closed (2026-07-15)

**Prompt (verbatim):**
> New update. Please continue.

(Reference: `Advisory-WP3-Step5Resolution-2026-07-15.md` +
`scheme_species_test.py` — advisor ran the $g_i$-internal scheme test
species-resolved on the fitted trajectory: $D/E^2(z=0)=+0.138$ under scheme A
vs $-0.023$ under scheme B, order-unity/sign-changing difference. Advisor's
verdict: scheme-dependence confirmed by direct computation; every physical
output ($E(z)$, invoice, $F(Q)$, WP4a/WP4b inputs) is built from machinery
that never references the $g_i$ placement, hence scheme-invariant; $D$,
$\Lambda_M$, $\pi_i$, $C_2$ are therefore pure bookkeeping gauge; **WP3 closes
with a positive verdict, kill condition does not trigger.**)

**Summary of work performed:**

1. **Reproduced the delivered numbers exactly** (the $D/E^2$ table, both
   schemes, to the digit) — no discrepancy in the arithmetic.

2. **Did not accept "WP3 closes positive" at face value** — closing an entire
   work package is exactly the kind of consequential claim warranting the same
   scrutiny already applied to two prior advisor errors this session.
   Re-derived the argument's load-bearing assumption from scratch: that
   $\mathcal N_i(t)$ itself (used identically in both schemes' $D$
   calculation) is scheme-independent.

3. **Confirmed this holds for matter** ($p^\text{sp}=\tfrac52$): the
   weight-drift term distinguishing schemes A and B vanishes identically for
   this species, so matter's census cannot be scheme-dependent regardless of
   placement.

4. **Found this is *not* separately checked for radiation** ($p^\text{sp}=1$):
   $g_\text{rad}^A\ne g_\text{rad}^B$ whenever $N\ne1$ (essentially always
   except today — $N=(c/c_0)^{5/2}$ is the established, non-trivial two-clock
   lapse, not a residual gauge value pinned to unity). Neither script actually
   solves $\dot{\mathcal N}_\text{rad}=\mathcal N_\text{rad}g_\text{rad}
   ^{A\text{ or }B}$ with the real $N(t)$ trajectory and checks it against the
   independently-known $\Omega_G(1+z)^4$ scaling used throughout — both simply
   assume the standard scaling and plug it into each scheme's $D$ formula. If
   neither scheme's own constraint actually reproduces that scaling when
   solved with the true $N(t)$, the "purely gauge" characterization would need
   qualification.

**Files produced:** `Update-WP3-Step5ResolutionAssessment-2026-07-15.md`, this
entry (note: an earlier attempt to write this file this session failed
silently — reconfirmed on disk before proceeding further).

**Status: not a kill; not yet a fully closed positive verdict either.** The
observable-level claim (§1 of the update: $E(z)$, invoice, $F(Q)$,
WP4a/WP4b — all scheme-independent by construction) is solid and independently
re-verified; recommend proceeding to WP4a without reservation on this basis.
The stronger theoretical claim ("$D$ is purely gauge, full stop") should carry
an explicit caveat pending one cheap, well-defined follow-up test (integrate
$\mathcal N_\text{rad}(t)$ under each scheme's own $g_\text{rad}$ with the real
$N(t)$, check against $\Omega_G(1+z)^4$) rather than being stated as fully
settled. WP2 discharge-by-incorporation: agreed for matter, held for radiation
pending the test. The KATRIN clock remains the program's most time-critical
item; nothing in `cdot-7/` was touched.

---

## Entry 20 — Advisor retracts the positive verdict; my own re-derivation finds a missing factor of 3 and a wrong test target underneath it (2026-07-15)

**Prompt (verbatim):**
> Please check the latest update.

(Reference: `Advisory-WP3-Step5Retraction-FrameTest-2026-07-15.md` +
`census_scheme_check.py` — advisor ran my §3 test to completion: neither
scheme A nor B, integrated with the real $N(t)$ trajectory, reproduces
$(1+z)^4$ for radiation — off by orders of magnitude, not a small residual.
Diagnosis: the closed-action $g_i$ is "frame-implicit," missing a
$dt/d\hat\tau$ factor somewhere; retracted the "WP3 closes positive" verdict
(fourth advisor error, this one a scoping error — verdict language exceeded
the specific test's demonstrated scope); held WP4a promotion; assigned a
"frame test" — re-derive $g_i$ directly from the covariant foliation-integral
definition — as the decisive next step.)

**Summary of work performed:**

1. **Reproduced the retraction's numbers exactly** — no arithmetic
   disagreement with the delivered orders-of-magnitude mismatch.

2. **Questioned the test's target before accepting its conclusion**: $\mathcal
   N_\text{rad}$ (a horizon-mass-over-Planck-mass count, per WP2's own
   definition) is not the same object as $\Omega_\text{rad}(z)=\Omega_{G,0}
   (1+z)^4$ (a density fraction) — nothing requires them to track each other.
   Computed $\mathcal N_\text{rad}(s)$ **algebraically**, directly from WP2's
   covariant definition on the fitted trajectory, no ODE or scheme involved:
   $d\ln\mathcal N_\text{rad}/ds=-\tfrac32+3\,d\ln r/ds$ — positive and
   growing into the past, nowhere near $-6$, for structural reasons, not
   because anything is broken.

3. **Found the actual bug**: this algebraic result matches WP2's *original*
   evolution equation (at $N=1$, with its stated coefficient of $3$ on the
   shell-sweep term) to $7\times10^{-12}$ — validating WP2 completely. But
   `Update-WP3-ClosedActionCouplingAudit-2026-07-13.md`'s closed-action
   $g_i$ carries coefficient $1$, not $3$, on that term — a plain arithmetic
   slip in transcribing WP2's own formula, present since the very first
   closed-action round, never caught because nobody checked $g_i$ against
   WP2's original formula directly until now. Not a scheme (A vs. B)
   question at all — both inherited the same missing factor.

4. **Surfaced, without resolving, the deeper question**: both $R_h$'s
   defining relation and the census evolution equation are, in WP2's original
   form, stated entirely on coordinate time with no reference to matter's
   proper time anywhere — raising the possibility that the census/horizon
   sector needs no lapse-dependence in the action at all, which would make
   $D\equiv0$ identically and dissolve the whole back-reaction/$C_2$
   question. A quick reparametrization check argues the other way, but I do
   not trust that hand-check given how many derivation errors this specific
   question has already produced this session (mine and the advisor's) —
   explicitly not asserting a resolution here.

**Files produced:** `Update-WP3-FrameTestFactorOfThree-2026-07-15.md`, this
entry; confirmed the file landed on disk before proceeding, per the standing
lesson from the earlier silent write failure.

**Status: neither the retraction's "kinematic failure" framing nor the
original "$D$ is gauge" framing is confirmed as stated.** Two independent,
verified findings (wrong test target; missing factor of 3) sit underneath
both, and neither invalidates the other's core observable-level conclusion
($E(z)$, invoice, $F(Q)$, WP4a/WP4b — still confirmed scheme-independent by
construction, unaffected by any of this). **Recommend**: redo the
census/horizon sector's reparametrization-invariant completion directly from
the covariant definition (the advisory's own §4 assignment), factor of 3
restored, and check *that* against the algebraic $\mathcal N_i(s)$ computed
here — not scheme A, not scheme B, not $(1+z)^4$. WP4a promotion: agree with
holding it, though for a different, narrower reason than the retraction's
(the $g_i$ formula every $D$ calculation used is independently confirmed
wrong, regardless of the scheme-gauge question). WP2 discharge held in full.
The KATRIN clock remains the program's most time-critical item; nothing in
`cdot-7/` was touched.

---

## Entry 21 — No-lapse form confirmed independently; a sixth advisor error found (written conclusion vs. delivered script mismatch); D≡0 stands on solid ground (2026-07-15)

**Prompt (verbatim):**
> Response added.

(Reference: `Advisory-WP3-CoefficientAndNoLapse-2026-07-15.md` +
`covariant_gi_derivation.py` — advisor confirmed my diagnosis via a direct
covariant derivation from M4's foliation-integral definition: boxed result
$g_i=(p_i^\text{sp}-\tfrac52)\dot c/c+3c/R_h$, $\dot R_h=c$, no lapse anywhere,
claimed to match the algebraic target to $\sim10^{-10}$; consequence $D\equiv0$
identically, the whole $C_2$/scheme saga a shadow of the coefficient
corruption; also self-caught a fifth error — an initial "coefficient 2" slip —
before publication.)

**Summary of work performed:**

1. **Ran the delivered script before accepting the claimed residual** — found
   it does not test the formula the advisory's prose states. The script's
   "Covariant" column retains $N$ on the shell-sweep term
   (`3*N*cR`), directly contradicting the written "$\dot R_h=c$, not
   $\dot R_h=Nc$" a few lines earlier in the same document. Running it as
   delivered: printed residual against the algebraic target is $5.25$
   (radiation), $4.50$ (cold) — not $10^{-10}$ as claimed. **Sixth advisor
   error**: a written conclusion and its own verification artifact
   disagreeing, with a residual claim that doesn't survive running the
   script that was supposed to establish it.

2. **Independently built and checked the form the prose actually states**
   ($g_i=(p_i^\text{sp}-\tfrac52)\dot c/c+3c/R_h$, $\dot R_h=c$, zero
   $N$-dependence anywhere) against the algebraic target from the prior
   round — exact match, to machine zero, as expected once stated plainly:
   it's the same chain-rule differentiation of the covariant definition
   written two ways, not two independent things that happen to agree.

3. **Confirmed $D\equiv0$ follows immediately**, not from a scheme test or a
   cancellation, but because $\partial g_i/\partial N=0$ and
   $\partial(\dot R_h-c)/\partial N=0$ identically once there is no $N$ to
   differentiate — the Hamiltonian constraint reverts exactly to the
   LapseBackreaction round's form, no census/horizon term at all.

4. **Noted the coupling-audit findings on $\pi_i,p_R$ become moot, not
   resolved** — those variables still exist with consistent internal
   dynamics, but no longer feed back into anything physical, so the
   bare-$p_R$ and coupled-symplectic-spectrum questions have nothing left to
   threaten.

**Files produced:** `Update-WP3-NoLapseConfirmed-2026-07-15.md`, this entry;
confirmed on disk before proceeding.

**Status: agree WP3 can close with a positive verdict**, reached
independently rather than accepted on the advisory's say-so, since its own
verification script's claim did not survive being run. The observable-level
scheme-invariance (established several rounds ago) still stands unmodified.
WP4a promotion: agree it can resume. WP2 discharge: agree it reopens
positively, WP2's original formula unmodified. Recommend the consolidation
log's error tally add this as a sixth entry. The KATRIN clock remains the
program's most time-critical item; nothing in `cdot-7/` was touched.
