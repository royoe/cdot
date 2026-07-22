# Session Log — cdot-8/WP7 (2026-07-21)

*Continued from `SessionLog-2026-07-20.md` (Entries 27–36). Same split
rationale as that file's own header — one log per calendar day. Entry
numbering continues unbroken from Entry 36. As of this file, also see
`Update-WP7-InstabilityRecourses-2026-07-21.md` (split out the same day
as this log, for the same reason) for the R0/R1/R2 technical content
Entries 41–44 describe.*

---

## Entry 37 (worker) — Stage 3f resolves the whole chain: no Riccati needed, just the right handoff redshift for the pointwise slaving that was already correct (2026-07-21)

**Prompt (verbatim):**
> Advice added. Looks promising!

**Summary of work performed:**

1. Found `Advisory-WP7-Stage3fPointwiseFixWorks-2026-07-21.md` +
   `wp7_stage3f_pointwise_conservative_handoff.py`. Confirms §39's
   repelling-flow diagnosis precisely (verified both analytically and
   by finite difference), then sidesteps the whole Riccati apparatus:
   Stage 3c's *original* pointwise slaving (fresh algebraic solve every
   step, no propagated $\mu(N)$) was never the problem — there is
   nothing for a repelling flow to act on if nothing is propagated.
   Stage 3d's catastrophic sensitivity came entirely from the wrong
   handoff redshift ($z_\text{switch}=18.5$, already known from §37 to
   sit deep in the marginal zone), not from any flaw in pointwise
   slaving, which is excellent throughout $z\gtrsim30$–$40$.

2. **Ran the companion script myself and reproduced every number
   exactly**: handoff redshifts $45$ down to $30.2$ give smooth,
   monotonically convergent results ($\delta_b(z{=}0)$ from $0.436$ to
   $0.374$, $\lesssim15\%$ spread) — nothing like Stage 3d's
   catastrophic sensitivity.

3. **Adopted as the standard closure**: pointwise slaving, handoff at
   $z\approx35$, full explicit integration below. Retired the
   Riccati-ODE approach as a working method (its discriminant identity
   and repelling-flow finding remain correct and useful — they're what
   ruled out the wrong fix and pointed at the simpler one).

**Files updated**: `Update-WP7-PerturbationStructure-2026-07-18.md`
(§40, new), this entry.

**Status: the long chain from §32's original blow-up through §33–§39 is
resolved.** The vector sector's fast/unstable mode is real physics, its
$\Pi$-term normalization is correct, and it can be safely and cheaply
eliminated above $z\approx35$ with simple pointwise algebraic slaving —
no exotic machinery needed after all. **One item remains before this is
fully validated**: the possible second unstable direction in the full
6-variable system (flagged §38, not yet confirmed) — recommended for a
careful check before treating the closure as complete and moving to
Stage 4. Nothing in `cdot-7/` was touched.

---

## Entry 38 (worker) — Stage 3g: the full 6-variable stability audit, done analytically — no second unstable direction found; the low-$z$ growth is the already-known scalar tachyonic mechanism (2026-07-21)

**Prompt (verbatim):**
> Please do the check.

**Summary of work performed:**

1. Built `wp7_stage3g_full_system_stability_audit.py` (new,
   `cdot-8/WP7/`) — the full $6\times6$ Jacobian, done **analytically**
   (the system is linear at fixed $N$) rather than by finite difference,
   directly addressing the advisor's own stated precision concern.

2. **Caught my own transcription error before trusting anything**: a
   real finite-difference cross-check flagged a large discrepancy in
   row 3; traced it to a missing $1/H_c$ on the $\Pi/(1+w)$ term, fixed
   to match the coded `rhs_full` exactly. **Validated the corrected
   Jacobian via complex-step differentiation** (machine-precision exact,
   immune to the cancellation error real finite differences suffer given
   this system's huge coefficient range) — residuals $\sim10^{-16}$
   everywhere.

3. **Scanned the full spectrum, $z=100$ to $z=0$**: confirmed the
   $(\alpha,\mathcal E_\alpha)$ sub-block exactly reproduces the earlier
   $2\times2$ analysis (consistency check). Found the full coupled
   system's actual eigenvalues are somewhat *smaller* than the isolated
   $2\times2$'s throughout high $z$ (e.g. $60$ vs $221$ at $z=100$) —
   real back-coupling damping, not alarming. **No independent growing
   direction found in the vector-sector regime.**

4. **A separate small real eigenvalue persists from $z\approx10$ to
   $z=0$** — checked directly whether it's vector-sourced by rerunning
   with $\kappa\to0$: **essentially unchanged**, confirming it is **not**
   sourced by the vector sector at all. It is the already-known scalar
   tachyonic-clustering mechanism (§23/§27), present regardless of the
   vector coupling — not the advisor's tentatively-suspected
   "gravitational-Jeans" new instability, and not something this
   closure needs to address.

**Files produced**: `wp7_stage3g_full_system_stability_audit.py` (new,
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md` (§41,
new), this entry.

**Status: the last open item from Stage 3f is closed.** No second
unstable direction requiring its own selection condition exists — the
full system has exactly two distinct, previously-identified growing
mechanisms (the vector sector's fast mode, handled by Stage 3f's
closure; the scalar tachyonic clustering mode, an already-accepted
feature since §27, unrelated to the vector sector). **The vector-sector
closure is now fully validated.** Nothing in `cdot-7/` was touched.

---

## Entry 39 (worker) — Stage 4 attempted: assembly straightforward, but a serious escalation-worthy finding — the vector-sector instability never resolves at the k-scales the ISW estimate actually needs (2026-07-21)

**Prompt (verbatim):**
> Proceed to Stage 4.

**Summary of work performed:**

1. Assembled the growth closure (§32–§41, unmodified by M5 per §7) with
   the M5 Einstein-constraint term (§4–§6's corrected coefficient, no
   re-derivation) into `wp7_stage4_isw_estimate.py` (new, `cdot-8/WP7/`)
   — solving the M5-augmented Poisson equation for $\Phi$ in closed
   form.

2. **Running at the actual ISW-relevant $k$** ($\ell=2,5,10\to
   k\approx1.1$–$5.4\times10^{-3}\,\text{Mpc}^{-1}$, via the established
   $k=\ell/D_p(z{=}0.5)$ convention) **blew up catastrophically.**
   Diagnosed rather than patched: Stage 3f/g's entire vector-sector
   closure was validated at exactly **one** wavenumber ($k=10^{-4}\,
   \text{Mpc}^{-1}$), roughly $10$–$50\times$ smaller than what
   $\ell=2$–$10$ actually require. Checked $z_\text{switch}(k)$ directly:
   it decreases with $k$ and **for $k\gtrsim10^{-3}\,\text{Mpc}^{-1}$, no
   switch exists in $z\in[0,2000]$ at all** — the fast eigenvalue stays
   real and positive from $z=100$ to $z=0$.

3. **Confirmed this is not a reduced-model or pointwise-slaving
   artifact**: reran §41's exact, complex-step-validated $6\times6$
   Jacobian at these $k$ values — the same large, positive, real
   eigenvalue is present in the full system at every redshift checked,
   never crossing zero. Even with pure pointwise slaving throughout (no
   handoff, avoiding literal divergence), $\Phi$ still grows $5$–$8$
   orders of magnitude from $z=100$ to $z=0$ — nothing like a physical
   ISW source, and completely swamping the M5 signature.

**Files produced**: `wp7_stage4_isw_estimate.py` (new, `cdot-8/WP7/`),
`Update-WP7-PerturbationStructure-2026-07-18.md` (§42, new), this entry.

**Status: NOT declaring a unilateral kill.** This is a different, more
serious finding than anything in §32–§41 (which all concerned one
scale) — the vector sector's instability gets *worse*, not better, at
smaller scales, and specifically afflicts the wavenumber range low-$\ell$
CMB/ISW observables actually probe. Since §7 established the field
equations are unmodified by M5 at every $k$, this cannot be fixed by
adjusting the M5 assembly. Two things stated plainly: this is
cdot-8's *own* $F(Q)$/background behavior, not a statement about AeST's
native CMB-fitting parameter choices (making the long-flagged, still-
optional AeST-native cross-check considerably more urgent than
"optional"); and nothing yet rules out an undiagnosed error in this
specific assembly rather than genuine physical pathology — this
program's own track record shows both are live possibilities.
**Recommending advisor review of this finding specifically**, and the
AeST-native cross-check as the most informative next diagnostic, before
any further ISW/power-spectrum numerics. Nothing in `cdot-7/` was
touched.

---

## Entry 40 (worker) — §42 confirmed and reframed by the advisor; careful reassessment finds one genuine numerical correction, substance unchanged (2026-07-21)

**Prompt (verbatim):**
> Advisory added. No obvious resolution found. Please reassess carefully before making conclusions.

**Summary of work performed:**

1. Found `Advisory-WP7-Stage4ISWInstabilityAssessed-2026-07-21.md`.
   Reproduced both §41/§42 exactly. Reframes §42 as a *continuation* of
   the already-accepted $c_\text{ad}^2<0$ mechanism (§23/§27) to larger
   $k$, not an unrelated new pathology — negative effective pressure
   destabilizes rather than stabilizes at larger $k$, opposite of
   ordinary Jeans behavior, exactly matching "worse at larger $k$."
   Severity unchanged; recommends routing to the author (alongside Gate
   1(b)) rather than the advisor/worker deciding the next diagnostic
   unilaterally.

2. **Did the requested careful reassessment, not a rubber stamp**:
   independently re-verified the advisor's "dip then rise to $\sim24$ by
   $z=0$" claim with a finer scan — reproduced it initially, but tracing
   *why* the rise happened surfaced something neither of us had caught:
   **it's a numerical artifact**. $c_\text{ad}^2$ is built via two
   nested `np.gradient` calls, and the default one-sided boundary
   formula (`edge_order=1`) is inaccurate right at the trajectory's
   last few points — exactly where the "rise" showed up. **Confirmed
   directly**: recomputing with `edge_order=2` removes the jump
   entirely (last six $c_\text{ad}^2$ values go from a sharp spike to
   perfectly smooth), while the underlying $\Omega_s(z)$ itself was
   smooth throughout — the artifact lived purely in the differentiation.

3. **This doesn't change the substantive finding, and simplifies it**:
   the instability still never approaches zero anywhere from $z=100$ to
   $z=0$ at the ISW-relevant $k$'s; with the artifact removed it's
   likely a monotonic floor near $8$–$9$, not a dip-then-spike. Flagged
   as a general numerical-hygiene item for future use of this
   trajectory's derivative-built quantities near $z=0$.

**Files updated**: `Update-WP7-PerturbationStructure-2026-07-18.md`
(§43, new), this entry.

**Status: advisor's reframing adopted (same mechanism, larger reach,
not new physics); one small, genuine numerical correction found and
reported; the escalation-worthy verdict is unchanged and, if anything,
more straightforward than either party's first pass.** Agreeing this
goes to the author now, alongside Gate 1(b), rather than proceeding to
the AeST-native cross-check unilaterally. Nothing in `cdot-7/` was
touched.

---

## Entry 41 (worker) — R0 attempted: both diagnostic questions answered directly from the primary source and the trusted coefficients (2026-07-21)

**Prompt (verbatim):**
> I have awakened the main advisor for a check on possible recourses for recovering WP7. Please check the advise and attempt R0 as proposed.

**Summary of work performed:**

1. Found `Advisory-WP7-InstabilityRecourses-2026-07-21.md` (main
   advisor). Confirms the anti-Jeans mechanism; proposes a recourse
   ladder R0 (audit) → R1 ($\mathcal F(\mathcal Y,\mathcal Q)$
   small-gradient completion) → R2 (AeST-native cross-check) → R3
   (re-closure) → R4 (nonlinear saturation, fallback framing).

2. **R0(a)**: checked the primary source directly for whether AeST's
   own stability guarantee assumes $F_\mathcal Q(\text{background})=0$.
   **Confirmed explicitly** — the founding paper's own "Stability and
   waves" section states outright it uses "the desired late Universe
   limit for which... $\partial\mathcal F/\partial\mathcal Q=\bar{
   \mathcal F}=0$" in deriving the healthy scalar dispersion relation.
   Valid at AeST's own intended operating point; not at cdot-8's
   ($F_\mathcal Q$ ranges $\approx4473\to1.85$, never near zero). The
   imported FRW equations of motion themselves are still correct and
   general (Stage 2 already confirmed this) — but the paper's own basis
   for calling this sector "healthy" simply doesn't cover cdot-8's
   regime.

3. **R0(b)**: decomposed $\partial\dot{\mathcal E}_\alpha/\partial
   \alpha$ (`wp7_r0_instability_source_audit.py`, new, `cdot-8/WP7/`)
   into its four additive pieces — only one carries any
   $\kappa$-dependence at all (the $\Pi$-feedback term,
   $\propto c_\text{ad}^2\kappa$), and it dominates the total by 1–2
   orders of magnitude at every redshift checked, uniformly
   destabilizing, while the remaining three pieces are modest and
   negative. **The negative effective pressure nets entirely from this
   one, already-identified term** — confirmed by decomposition, not
   argument.

**Files produced**: `wp7_r0_instability_source_audit.py` (new,
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md` (§44,
new — later moved to `Update-WP7-InstabilityRecourses-2026-07-21.md`
§1 when that document was split out, 2026-07-21), this entry.

**Status: R0 complete, favorable to R1.** Since the unstable direction
is a $\kappa$-linear (gradient-squared) term, and AeST's own
$\mathcal Y$-sector completion enters at exactly that same order while
leaving the FRW background untouched, R1 is not structurally blocked —
though not yet shown to work. R2 (per the advisory's own "R0+R2 as one
short round") has not yet been run. Gate 4's paused status is unchanged;
this is diagnostic work, not a resumption. Nothing in `cdot-7/` was
touched.

---

## Entry 42 (worker) — R2: the AeST-native cross-check, clean and opposite result (2026-07-21)

**Prompt (verbatim):**
> Please proceed with R2.

**Summary of work performed:**

1. Built AeST's own tuned "Higgs-like" $\mathcal K(\mathcal Q)$
   background directly (`wp7_r2_aest_native_crosscheck.py`, new,
   `cdot-8/WP7/`), using the founding paper's own quoted parameters —
   read numerically off its own CMB-fit figure ($\mathcal K_B=0.3,
   \mathcal Q_0=1\,\text{Mpc}^{-1},\mathcal K_2=8.5\times10^8$), not
   available in the `.tex` source text.

2. Solved $\bar{\mathcal Q}(a)$ exactly from the scalar's own conserved
   charge $a^3F_\mathcal Q=\text{const}$ (the complete EOM here, no M5
   to complicate it). **Caught a genuine numerical trap first**:
   tracking $\bar{\mathcal Q}/\mathcal Q_0$ and subtracting $1$ loses
   all precision once the field settles near the minimum; reformulated
   directly in terms of the deviation $\delta$, solving the equivalent
   depressed cubic instead — clean throughout.

3. Used the **native** (non-M5) $\rho_s$ coefficient, a $\Lambda$CDM
   stand-in for $H(a)$ (stated as an approximation not affecting the
   shape-only $w,c_\text{ad}^2$ quantities).

4. **Result**: $c_\text{ad}^2$ is negative for AeST's own tuning too
   (same sign, confirming the mechanism is generic to the imported
   machinery) but enormously smaller ($\approx-6.5\times10^{-4}$ at
   recombination, collapsing toward $\sim-10^{-12}$ by today, vs.
   cdot-8's own persistent $\sim-0.01$ to $-0.07$). **Running the
   identical Jacobian at the identical three ISW wavenumbers gives the
   opposite qualitative result**: resolves to stable by $z\approx100$
   (a brief, small transient at $z=1090$ for the two larger $k$'s) and
   stays stable all the way to $z=0$ — the opposite of cdot-8's
   never-restabilizing behavior at these same $k$'s.

**Files produced**: `wp7_r2_aest_native_crosscheck.py` (new,
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md` (§45,
new — later moved to `Update-WP7-InstabilityRecourses-2026-07-21.md`
§2 when that document was split out, 2026-07-21), this entry.

**Status: R2 confirms the pathology belongs to cdot-8's own
census-forced $F(\mathcal Q)$, not to the imported AeST machinery.**
AeST's own solution stays anchored at $\mathcal K$'s minimum with a
controlled, shrinking deviation; cdot-8's $\mathcal Q\propto(1+z)^{5/3}$
never approaches any stationary point at all — a genuine structural
distinction, not just a smaller number. Together with R0, this closes
the "error vs. genuine consequence" question from both sides: it's a
real, load-bearing consequence of cdot-8's own zero-freedom closure.
Gate 4's paused status unchanged; this remains diagnostic work.
Nothing in `cdot-7/` was touched.

---

## Entry 43 (worker) — R1 attempted: a genuine feasibility signal, with a serious gap flagged honestly (2026-07-21)

**Prompt (verbatim):**
> Let's try the R1 recourse.

**Summary of work performed:**

1. **Confirmed what's rigorous first**: the primary source's own $F_
   \mathcal Y=(2-\mathcal K_B)\lambda_s$ parametrization, already named
   as a free cosmological parameter, already used in its own Minkowski
   stability analysis (vector mass $M^2\propto(1+\lambda_s)$, scalar
   $k^2$ coefficient $\propto(1+\tfrac12\mathcal K_B\lambda_s)$, both
   requiring $\lambda_s>-1$).

2. **Stated plainly what's not yet done**: the actual cosmological
   (FRW) system this whole WP7 arc uses was derived with $\mathcal Y
   \equiv0$ built in — there is no existing derivation of how $F_
   \mathcal Y$ modifies it. A full action-level re-derivation was not
   attempted, given the risk of an unverified error in exactly the kind
   of calculation that has repeatedly needed independent cross-checking
   in this program.

3. **Attempted a feasibility test instead**
   (`wp7_r1_gradient_completion_feasibility.py`, new, `cdot-8/WP7/`),
   explicitly scoped as testing a structural hypothesis, not deriving
   or validating a fix: $(2-\mathcal K_B)\to(2-\mathcal K_B)(1+
   \lambda_s)$ in the $\mathcal E_\alpha$ equation's own bracket (where
   R0(b) isolated the destabilizing term).

4. **Result**: moving $\lambda_s$ toward $-1$ (staying inside the
   healthy $\lambda_s>-1$ range) suppresses the instability by orders
   of magnitude; $\lambda_s=-1$ exactly gives clean, $k$-independent
   stability everywhere. **But $\lambda_s=-1$ is exactly the founding
   paper's own stated healthy-range boundary** (vector mass $\to0$
   there) — a real, specific tension, not resolved by this test.
   Encouragingly, $\lambda_s$ comfortably inside the healthy range
   (e.g. $-0.99$ to $-0.999$) already captures most of the benefit.

**Files produced**: `wp7_r1_gradient_completion_feasibility.py` (new,
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md` (§46,
new — later moved to `Update-WP7-InstabilityRecourses-2026-07-21.md`
§3 when that document was split out, 2026-07-21), this entry.

**Status: a genuine, quantitative feasibility signal, not a validated
recourse.** Recommending this be reported alongside R0/R2's findings
with an explicit request for the real action-level derivation before
$\lambda_s$ near $-1$ is treated as anything more than promising. Gate
4's paused status unchanged. Nothing in `cdot-7/` was touched.

---

## Entry 44 (worker) — secondary advisor cross-checks R0/R1/R2, all confirmed; one new primary-source finding sharpens R1's gap (2026-07-21)

**Prompt (verbatim):**
> Please check the advisory from the assistant advisor. All confirmed, but for a brief note on R1.

Found `Advisory-WP7-R0R1R2CrossCheck-2026-07-21.md`. Reran R0/R1/R2's
scripts directly and reproduced every reported number. Two refinements
verified independently against `newRMONDLett.tex` before accepting:
(1) R0(b)'s dominance is $z$-dependent — four-and-a-half orders of
magnitude at $z=100$, not a flat "1–2 orders"; (2) a **second,
previously-unflagged condition** in the same stability section: the
paper states the residual ($\omega=0$) vector mode's Hamiltonian
"also requir[es] $\lambda_s>0$" (verified verbatim, lines 570–571) —
directly conflicting with R1's own favored suppression range
($\lambda_s<0$, approaching $-1$). Framed by the paper's own next
sentence as possibly a tolerable Jeans-type effect, not obviously
fatal — but unresolved from the compact PRL text alone. Added as a
brief note to what is now `Update-WP7-InstabilityRecourses-2026-07-21.md`
§3 (not a new section, per the prompt — this was §46 of the main
document before the file split later this same day): R1's gap list
now has two items — the missing action-level FRW derivation, and
whether $\lambda_s>0$ survives, relaxes, or doesn't transfer in the FRW
(not Minkowski) setting. Gate 4's paused status unchanged. Nothing in
`cdot-7/` was touched.

---

## Entry 45 (worker) — main advisor assesses the full R0/R1/R2 round: three genuine reframings, recommendation to commission the action-level derivation (2026-07-21)

**Prompt (verbatim):**
> Good. Now check for update from the main advisor.

Found `Advisory-WP7-RecourseRoundAssessed-2026-07-21.md` (written before
the secondary advisor's own cross-check, processed here in sequence).
Accepts R0/R1/R2 in full. Independently verified both quantitative
claims (`r1_viability_additions.py`, run directly) before accepting:
$\mu\approx10^{-4}\,\text{Mpc}^{-1}$ sits $11$–$56\times$ below the ISW
instability band; the vector mass at WP6's pulsar-squeezed $\mathcal
K_B$ stays heavy ($M^2/\mathcal Q_0^2\approx8$) even at $(1+\lambda_s)=
10^{-5}$ — both reproduced exactly. Three reframings added: (a)
$\lambda_s\to-1$ is the point where the scalar becomes literal, honest
dust ($c_s^2\to0$) at linear order, not an arbitrary suppression trick
— principled, not epicyclic; (b) the $\lambda_s>0$ tension has a scale
map — the flagged zone sits $11$–$56\times$ *below* where stabilization
is needed, adjacent but distinct, not dissolved but located; (c) the
"dangerous corner" ($M^2\propto1+\lambda_s$) is parametrically
protected by WP6's own $\mathcal K_B$ pulsar squeeze via the $1/\mathcal
K_B$ factor — a constraint that looked like pure cost in WP6 turns out
load-bearing for this recourse. **Recommendation: commission the
action-level FRW derivation** (general $\mathcal F(\mathcal Y,\mathcal
Q)$ kept throughout), five-item target list, Gate 4 remaining paused
until it lands. Written up as §4 of
`Update-WP7-InstabilityRecourses-2026-07-21.md`. **Status: assessment
accepted, not yet acted on** — a recommendation to commission
substantial original theoretical work, not something to start
unilaterally. Nothing in `cdot-7/` was touched.

---

## Entry 46 (worker) — the commissioned derivation begins: $\mathcal Y$'s exact quadratic-order form established, a genuine bug caught and fixed along the way (2026-07-21)

**Prompt (verbatim):**
> I agree to proceed on the the action-level FRW derivation.

**Summary of work performed:**

1. Started target-list item 1 (does $(2-\mathcal K_B)\to(2-\mathcal
   K_B)(1+\lambda_s)$ hold in the FRW system?). First necessary step:
   derive $\mathcal Y=q^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi$ itself to
   quadratic order in Newtonian-gauge perturbations — never previously
   done anywhere in this program.

2. **Derived, via an exact algebraic identity**
   ($D_\mu\phi\equiv\nabla_\mu\phi+A_\mu\mathcal Q$ is the $A$-orthogonal
   projection of $\nabla_\mu\phi$; $\mathcal Y=g^{\mu\nu}D_\mu\phi D_\nu
   \phi$ identically): $\mathcal Y=a^{-2}(\nabla\chi)^2$, governed
   entirely by $\chi\equiv\varphi+\dot{\bar\phi}\alpha$ — exactly the
   combination already central to the imported system.

3. **Caught a genuine bug before trusting this**: computing $\mathcal Y$
   two independent ways (direct sum vs. the $D_\mu\phi$ identity) first
   gave *different* answers. Traced to root cause rather than picking
   the more plausible one: the unit-timelike constraint, combined with
   metric-consistent index raising, needs a second-order correction to
   $A_0$ itself that the paper's own linear-order ansatz never states
   (since it only works to linear order). Fixed via
   `wp7_derivation_Y_identity.py` (new, `cdot-8/WP7/`), symbolically
   verified both methods now agree exactly, matching the predicted
   $a^{-2}(\nabla\chi)^2$ to machine precision.

4. **Direct action-level consequence derived**: expanding $\mathcal F(
   \mathcal Y,\mathcal Q)$ around $\mathcal Y=0$ confirms $(2-\mathcal
   K_B)\to(2-\mathcal K_B)+F_\mathcal Y(0,\bar{\mathcal Q})$ as the
   coefficient of $\chi$'s gradient-squared term — rigorously, for this
   isolated piece of the action.

5. **Identified what remains, honestly**: the base action also carries
   a *separate* $2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi$ term (built
   from the aether's own acceleration, not from $\mathcal Y$) sharing
   the same bare $(2-\mathcal K_B)$ but **not** touched by $F_\mathcal
   Y$. Distinguishing which occurrences in $\Pi$/$\mathcal E_\alpha$
   trace to $\mathcal Y$ vs. this $\hat J$-term — the harder remaining
   piece of item 1 — means R1's original "uniform substitution"
   hypothesis is now known to be too crude to be final.

**Files produced**: `wp7_derivation_Y_identity.py` (new, `cdot-8/WP7/`),
`Update-WP7-InstabilityRecourses-2026-07-21.md` (§5, new), this entry.

**Status: genuine, verified progress on item 1, not yet complete.**
Checkpointing here rather than pushing further without review, given
how many subtle corrections this exact class of derivation has produced
throughout this program (this round included). Recommending this
specific finding be cross-checked before the harder remaining step (the
full coupled Einstein+scalar+vector variation). Gate 4 remains paused.
Nothing in `cdot-7/` was touched.

---

## Entry 47 (worker) — advisory confirms §5, sharpens the attribution problem; applying it reveals a stark, must-report divergence (2026-07-21)

**Prompt (verbatim):**
> Check for advisory and proceed.

**Summary of work performed:**

1. Found `Advisory-WP7-YIdentityDerivationReviewed-2026-07-21.md`.
   Confirms §5's symbolic result and bug-fix exactly (independent
   rerun). Independently confirms, directly from the primary source
   (verified myself: `newRMONDLett.tex` lines 336–347), that $(2-
   \mathcal K_B)$ appears in three structurally distinct places in the
   action — only one ($-(2-\mathcal K_B)\mathcal Y$) gets the $F_
   \mathcal Y$ correction, the separate $\hat J^\mu\nabla_\mu\phi$ term
   does not. Confirms no shortcut exists in the primary source (its own
   perturbation section assumes $\mathcal Y\equiv0$ from line 1).
   Proposes a valid, bounded shortcut: since the new term is
   functionally identical to the bare $\mathcal Y$-term, only need to
   identify which $(2-\mathcal K_B)$-proportional pieces in the
   *published* formulas trace to $\mathcal Y$ (Laplacian-type) vs.
   $\hat J^\mu\nabla_\mu\phi$ (friction/acceleration-type, no $\nabla^2$).

2. **Applied this criterion** (`wp7_r1_refined_attribution.py`, new,
   `cdot-8/WP7/`): only the *inner* $(2-\mathcal K_B)$ inside $\Pi$'s
   own $\nabla^2[\ldots]$ bracket gets the $\lambda_s$ correction; the
   *outer* one in the $\mathcal E_\alpha$ equation's bracket
   (multiplying friction/mass-type terms, no Laplacian) stays bare.

3. **Result: a stark reversal.** Under this refined attribution, the
   instability barely responds to $\lambda_s$ at all ($\max\text{Re}(
   \lambda)$ at $z=1090$: $3.3559\times10^8\to3.3559\times10^8$ across
   $\lambda_s=0\to-2$, unchanged to 4 figures) — diagnosed to the
   Jacobian's own *trace* being enormous and, under this hypothesis,
   driven by a term never touched by $\lambda_s$ at all, dominating
   regardless of what the $\lambda_s$-sensitive off-diagonal entry does.

**Files produced**: `wp7_r1_refined_attribution.py` (new, `cdot-8/WP7/`),
`Update-WP7-InstabilityRecourses-2026-07-21.md` (§6, new), this entry.

**Status: a must-report divergence, not a resolved answer.** The
original "uniform substitution" test and this "refined attribution"
test are both structurally motivated, neither rigorously derived, and
give *opposite* conclusions about whether R1 can work at all. This
sharpens, rather than resolves, why the full coupled-variation
derivation is essential. Not treating either result as final —
recommending this divergence be the focus of the next review round.
Gate 4 remains paused. Nothing in `cdot-7/` was touched.

---

## Entry 48 (worker) — advisory confirms §6's arithmetic, flags a specific weak point in the attribution criterion; verified and sharpened into an exact identity (2026-07-21)

**Prompt (verbatim):**
> Ok, my bad. Please check the response in Advisory-WP7-RefinedAttributionAssessed-2026-07-21.md

**Summary of work performed:**

1. Found and read `Advisory-WP7-RefinedAttributionAssessed-2026-07-21.md`.
   Confirms §6's numbers exactly and independently re-derives the
   "large fixed trace dominates" claim via the $2\times2$ eigenvalue
   formula. **Verified this arithmetic myself directly**: $a_{EE}^2
   \approx1.126\times10^{17}$ against $4a_{\mathcal E_\alpha,\alpha}/H$
   ranging $\pm3.0\times10^{10}$ at $z=1090$ — matches exactly.

2. **Flags a specific weak point**: the refined attribution's
   "friction/mass, no Laplacian" half (for the $\hat J^\mu\nabla_\mu
   \phi$-sourced terms) assumes $\hat J_\mu$'s spatial component carries
   no gradient structure — argued, not proven, to be doubtful.

3. **Checked this directly rather than accepting the qualitative
   argument**: computed $\hat J_i$ symbolically using the actual
   perturbed-FRW Christoffel symbols
   (`wp7_derivation_Jhat_identity.py`, new, `cdot-8/WP7/`). **Result:
   $\hat J_i=\partial_i(\Psi+\dot\alpha)=\partial_i\mathcal E_\alpha$
   exactly** — confirms and sharpens the weak point precisely (not just
   "some gradient," but exactly $\mathcal E_\alpha$'s own gradient).
   This means the $\hat J^\mu\nabla_\mu\phi$ term's spatial piece is a
   genuine $\mathcal E_\alpha$-$\varphi$ gradient *cross*-term —
   structurally distinct from both $\mathcal Y$ (a single field squared)
   and a pure friction term, meaning **neither of §6's two attribution
   hypotheses is correct as stated.**

**Files produced**: `wp7_derivation_Jhat_identity.py` (new,
`cdot-8/WP7/`), `Update-WP7-InstabilityRecourses-2026-07-21.md` (§7,
new), this entry.

**Status: precisely locates what the actual coupled-variation
derivation needs to account for; does not yet complete it.** Three
consecutive rounds (§5, §6, this one) have each surfaced genuine,
easy-to-miss structure — checkpointing here per this program's standing
discipline rather than pushing into the full variation unreviewed. Gate
4 remains paused. Nothing in `cdot-7/` was touched.

---

## Entry 49 (worker) — $\hat J_0=0$ exactly, confirmed via the same Christoffel-symbol machinery: the entire $\hat J^\mu\nabla_\mu\phi$ term reduces to its spatial piece (2026-07-21)

**Prompt (verbatim):**
> Please check advisory

(continuing the recommended next step after processing
`Advisory-WP7-JhatIdentityConfirmed-2026-07-21.md`, which confirmed §7's
$\hat J_i=\partial_i\mathcal E_\alpha$ identity and offered the
$\chi$-substitution simplification for the coupled variation still to
come)

**Summary of work performed:**

1. Extended `wp7_derivation_Jhat_identity.py` (same file as §7's $\hat
   J_i$ derivation, `cdot-8/WP7/`) with a $\hat J_0$ computation, reusing
   the already-validated Christoffel-symbol machinery.

2. **Result: $\hat J_0=0$ exactly**, to linear order. **Independent
   consistency check, also exact**: the orthogonality identity $\hat
   A^\mu\hat J_\mu=0$ (expected on general grounds for a unit-norm
   congruence's own acceleration) holds identically once $\hat J_0$ and
   $\hat J_i$ are combined with $\hat A^\mu$ through the same
   self-consistent, second-order-corrected $A_0$ ansatz §5 established —
   a third independent pass of this same machinery, not a new assumption
   introduced to force the check through.

3. **Direct consequence**: since $\hat J^0=g^{00}\hat J_0=0$ too, the
   entire $\hat J^\mu\nabla_\mu\phi$ term reduces to just its spatial
   piece, $\hat J^i\nabla_i\phi\approx a^{-2}\partial_i\mathcal E_\alpha
   \partial_i\varphi$ — no separate time-component contribution to carry
   through the coupled variation. Combined with the advisory's own
   $\chi$-substitution ($\varphi=\chi-\dot{\bar\phi}\alpha$), this is
   expressible entirely in the program's three standing variables
   ($\chi,\alpha,\mathcal E_\alpha$).

4. **Verified from the saved script's own output before writing anything
   up** (this program's own standing discipline): reran
   `wp7_derivation_Jhat_identity.py` directly from `cdot-8/WP7/` after
   adding the $\hat J_0$ and orthogonality checks to its own
   `if __name__=='__main__':` block — both print `True` exactly,
   confirmed live, not assumed from the standalone scratch check that
   found this first.

**Files updated**: `wp7_derivation_Jhat_identity.py` (extended, not new),
`Update-WP7-InstabilityRecourses-2026-07-21.md` (§8, new), this entry.

**Status: a genuine simplification, not a resolution of the attribution
question.** Does not by itself determine how the $\hat J^\mu\nabla_\mu
\phi$ cross-term propagates into the modified $\Pi$/$\mathcal E_\alpha$
equations — the actual Euler-Lagrange variation of the combined action
(this term plus $-F_\mathcal Y(0,\bar{\mathcal Q})\mathcal Y$) remains
the substantial next step, not yet attempted. What this establishes: one
fewer moving part in that variation (no separate time-component piece),
and a third consecutive confirmation that computing these quantities
exactly keeps surfacing real, checkable structure. Checkpointing here
before attempting the full variation. Gate 4 remains paused. Nothing in
`cdot-7/` was touched.

---

## Entry 50 (worker) — first attempt at the actual coupled variation: a real methodological bug caught and fixed (validated), leading terms match, two residual mismatches honestly left open (2026-07-21)

**Prompt (verbatim):**
> Please proceed!

**Summary of work performed:**

1. Assembled the full $\alpha$-dependent quadratic-order Lagrangian
   (bare $\mathcal Y$, the new $F_\mathcal Y(0,\bar{\mathcal Q})
   \mathcal Y$ completion, $2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi$,
   the Maxwell-like $\hat F^{\mu\nu}\hat F_{\mu\nu}$ term, and
   $\mathcal F(\mathcal Y,\mathcal Q)$'s own $\mathcal Q$-dependence)
   and varied it directly w.r.t. $\alpha$
   (`wp7_derivation_coupled_variation_attempt.py`, new,
   `cdot-8/WP7/`) — sidestepping the attribution-guessing problem
   entirely, per the advisories' own recommendation.

2. **Computed a new building block along the way**: extracted $\mathcal
   Q$'s own second-order perturbation from `Qcal` in
   `wp7_derivation_Y_identity.py` (already there, never displayed
   before). $\mathcal Q^{(1)}=\gamma$ (no $\alpha$-dependence, as
   expected); $\mathcal Q^{(2)}$ contains a genuine $\alpha$-$\varphi$
   cross term, not previously computed anywhere in this program.

3. **Caught and fixed a genuine methodological bug before trusting
   anything**: initially treated $\kappa=k^2/a^2$ as a constant symbol
   in the Euler-Lagrange time derivative — wrong, since $a(t)$ is
   time-dependent, and this produced a spurious $3H$ (canonical-scalar)
   friction coefficient for the Maxwell term alone. **Fixed by keeping
   $\kappa=k^2/a(t)^2$ explicit; re-ran the Maxwell term alone and it
   then exactly reproduces $\mathcal K_B(\dot{\mathcal E}_\alpha+H
   \mathcal E_\alpha)$** — a clean, validating cross-check, confirmed
   by direct computation.

4. **Result with the full Lagrangian**: leading terms match the
   published vector equation exactly ($\mathcal K_B(\dot{\mathcal E}_
   \alpha+H\mathcal E_\alpha)$, the leading $(2-\mathcal K_B)H\chi$ and
   $F_\mathcal Q$-proportional $\chi$ pieces). **Two residual
   mismatches honestly left open**, each precisely located: (1) the
   published $\chi$ coefficient carries an extra $(2-\mathcal K_B)\dot{
   \bar\phi}$ piece not produced here — plausibly traces to $\Pi$'s
   separate Einstein-momentum-constraint origin (not a raw
   field-variation object), not attempted in this pass; (2) the derived
   $\alpha$-coefficient comes out in terms of $dK/d\mathcal Q$ and
   $\ddot{\bar\phi}$, not $c_\text{ad}^2H\dot{\bar\phi}$ as published —
   plausibly resolved by substituting the background scalar's own
   equation of motion ($a^3F_\mathcal Q=$const), not yet done.

**Files produced**: `wp7_derivation_coupled_variation_attempt.py` (new,
`cdot-8/WP7/`), `Update-WP7-InstabilityRecourses-2026-07-21.md` (§9,
new), this entry.

**Status: genuine, partially-verified progress, not a completed
derivation.** The Maxwell-friction fix is a real, validated result on
its own. The two residual mismatches are reported honestly as open,
each with a specific, checkable next step, not forced through under
pressure — consistent with this program's standing discipline given how
much this exact sub-problem has surfaced across five consecutive rounds
(§5–§9). Recommending cross-check before treating any coefficient
conclusion as final. Gate 4 remains paused. Nothing in `cdot-7/` was
touched.

---

## Entry 51 (worker) — advisor catches a real bug in §9's convention ($\chi$ not independent of $\alpha$); independently confirmed and extended: mismatch (1)'s remainder traced exactly to $\Pi$'s own gamma-term (2026-07-21)

**Prompt (verbatim):**
> Some advice provided, please check and proceed.

**Summary of work performed:**

1. Found `Advisory-WP7-CoupledVariationChiIndependenceCaught-2026-07-21.md`.
   §8 and §9's own numbers both reproduce exactly. **Advisor catches a
   real bug**: §9 treated $\chi$ as independent of $\alpha$ when varying
   — but $\chi\equiv\varphi+\dot{\bar\phi}\alpha$ is not actually
   independent; the true independent fields are $(\varphi,\alpha)$.
   Varying at fixed $\chi$ silently forces $\varphi$ to co-vary — a
   different, wrong variation.

2. **Independently re-ran the advisor's own companion script
   (`wp7_chi_dependence_check.py`) before accepting anything** —
   reproduces exactly: redoing the variation at fixed $\varphi$
   resolves the reported "residual mismatch (1)" exactly and
   mechanically (not via the not-yet-derived $\Pi$ contribution §9's
   own docstring had speculated), with one extra, expected $F_\mathcal
   Y\dot{\bar\phi}\chi$ new-physics term. A new, third open item (a
   $\dot\chi$-type term with no published counterpart) surfaces in its
   place; mismatch (2) shifts, doesn't resolve.

3. **Extended this further** (`wp7_derivation_coupled_variation_varphi_
   fixed.py`, new, `cdot-8/WP7/`): redid the derivation directly in
   $(\varphi,\alpha)$ (avoiding the $\chi$-bookkeeping presentation
   ambiguity), and derived a clean, exact background identity from
   $a^3F_\mathcal Q=$const: $\ddot{\bar\phi}=-3Hc_\text{ad}^2\dot{\bar
   \phi}$. Substituting this, the residual reduces to exactly
   $(2-\mathcal K_B)\dot\varphi+F_\mathcal Y\dot{\bar\phi}\chi-(2-
   \mathcal K_B)(1-3c_\text{ad}^2)H\dot{\bar\phi}\alpha$.

4. **Checked the $\dot\varphi$ piece directly against $\Pi$'s own
   definition** (using $\delta$'s leading $\gamma$-dependence, $\gamma
   \equiv\dot\varphi-\dot{\bar\phi}\Psi$): $(2-\mathcal K_B)\dot{\bar
   \phi}/(1+w)\cdot[\Pi\text{'s leading }\gamma\text{-term}]=(2-
   \mathcal K_B)\gamma$. **The $(2-\mathcal K_B)\dot\varphi$ piece
   matches exactly** — a genuine, confirmed (not merely plausible)
   result: $\Pi$'s momentum-constraint origin is precisely what
   completes the vector equation's $\dot\varphi$-dependence.

**Files produced**: `wp7_derivation_coupled_variation_varphi_fixed.py`
(new, `cdot-8/WP7/`), `Update-WP7-InstabilityRecourses-2026-07-21.md`
(§10, new), this entry.

**Status: genuine forward progress on two fronts.** Mismatch (1) is
now mechanically resolved (advisor's fix, independently confirmed), and
its remainder is now *shown*, not guessed, to trace exactly to $\Pi$'s
own leading term. Still open: $\Pi$'s $-(2-\mathcal K_B)\dot{\bar\phi}
\Psi$ piece and its $\kappa_3\cdot$bracket piece vs. the alpha/cad2
residual, both requiring $\Pi$'s actual derivation from the $0i$
Einstein constraint — not yet attempted, now the clear, well-motivated
next step. Gate 4 remains paused. Nothing in `cdot-7/` was touched.

---

## Entry 52 (worker) — advisory confirms §10 exactly, sharpens the open item into a precise prediction; first attempt at $\Pi$'s own momentum-constraint derivation — genuine partial progress, one real gap honestly left open (2026-07-21)

**Prompt (verbatim):**
> Advice added. Please assess and proceed.

**Summary of work performed:**

1. Found `Advisory-WP7-PiGammaTermMatchConfirmed-2026-07-21.md`. §10
   reproduces exactly, including the algebra by hand. **Sharpened
   target identified**: the residual currently carries zero net $\Psi$-
   dependence, so $\Pi$'s own $\kappa_3$-bracket piece must supply a
   specific $\Psi$-term canceling the $\gamma$-term's $-(2-\mathcal
   K_B)\dot{\bar\phi}\Psi$ piece exactly — a sharp, falsifiable check.
   **Independently reran `wp7_derivation_coupled_variation_varphi_
   fixed.py` before accepting** — reproduces exactly.

2. **Attempted $\Pi$'s own derivation directly**
   (`wp7_derivation_momentum_constraint_attempt.py`, new,
   `cdot-8/WP7/`): extended the perturbed-FRW metric with a genuine
   shift perturbation $g_{01}=\epsilon B(t,x^1)$, extending the
   validated Christoffel machinery. $T^0_{\ i}$ obtained via
   $d(\text{quadratic action})/dB$ at $B=0$.

3. **Clean sub-results, each independently checked**: $\hat J_\mu$
   (lower index) has no $B$-dependence at linear order. $\hat J^0$
   (upper index) picks up a genuine new $B$-linear term once contracted
   into $\hat J^\mu\nabla_\mu\phi$. $\mathcal Q$'s and $\mathcal Y$'s
   own $B$-linear pieces computed cleanly. The Maxwell term has exactly
   zero $B$-dependence at this order.

4. **Assembled these**: the result contains the expected $\dot{\bar
   \phi}\partial_1\Psi$ piece (encouraging), but also a bare $F_\mathcal
   Q\partial_1\chi$ piece with no counterpart in the published $\delta$/
   $\Pi$ bracket — a genuine, unresolved discrepancy, reported honestly
   rather than forced to match.

**Files produced**: `wp7_derivation_momentum_constraint_attempt.py`
(new, `cdot-8/WP7/`), `Update-WP7-InstabilityRecourses-2026-07-21.md`
(§11, new), this entry.

**Status: genuine, partial progress, not a completed or fully verified
derivation of $\Pi$.** The clean sub-results are reported with
confidence; the assembled candidate does not yet cleanly reproduce the
published bracket. Plausible, not-yet-checked candidates for the gap
listed (normalization, Einstein-Hilbert cross-terms, the $\gamma^2$
term's own $B$-contribution). Checkpointing here, consistent with this
program's standing discipline, given this is the sixth consecutive
round (§5–§11) surfacing genuine structure in this one sub-derivation.
Gate 4 remains paused. Nothing in `cdot-7/` was touched.

---

## Entry 53 (worker) — advisor confirms §11's assembly and offers a testable hypothesis for the "bare $F_\mathcal Q$" gap; confirmed exactly via an exact background identity (2026-07-21)

**Prompt (verbatim):**
> Advice added.

**Summary of work performed:**

1. Found `Advisory-WP7-MomentumConstraintAttemptAssessed-2026-07-21.md`.
   Every sub-result and the assembly step itself reproduce exactly
   (independently re-derived from the five raw pieces, not just
   re-run). A presentation correction (no computational error): the
   isolated "$F_\mathcal Q$" piece is $F_\mathcal Q(\partial_1\varphi-
   \dot{\bar\phi}\partial_1\alpha)$, not $F_\mathcal Q\partial_1\chi$.
   **Concrete, testable hypothesis offered**: this piece may belong to
   the scalar sector's own $\theta$-equation ($\theta=\varphi/\dot{\bar
   \phi}$), not to $\Pi$'s bracket.

2. **Checked this directly**
   (`wp7_derivation_theta_attribution_check.py`, new, `cdot-8/WP7/`):
   verified the exact background identity $(1+w)\bar\rho\cdot16\pi
   \tilde G=-\dot{\bar\phi}F_\mathcal Q$ using already-established
   background relations. This means $-(1+w)\bar\rho\,\partial_1\theta
   \cdot16\pi\tilde G=F_\mathcal Q\partial_1\varphi$ — **matching the
   $\varphi$-part of the isolated piece exactly. The hypothesis is
   confirmed, not merely plausible.**

3. **Isolated the remainder** after subtracting the theta-matched
   piece: $2(2-\mathcal K_B)\dot{\bar\phi}\partial_1\mathcal E_\alpha-2
   (2-\mathcal K_B+F_\mathcal Y)\dot{\bar\phi}^2\partial_1\alpha$ — pure
   $\alpha,\mathcal E_\alpha$, no $\varphi$, containing an expected new
   $F_\mathcal Y$-proportional piece (same character as §10's own term).

**Files produced**: `wp7_derivation_theta_attribution_check.py` (new,
`cdot-8/WP7/`), `Update-WP7-InstabilityRecourses-2026-07-21.md` (§12,
new), this entry.

**Status: genuine, confirmed partial resolution.** The "bare $F_
\mathcal Q$" gap is no longer an open mismatch — its $\varphi$-part is
exactly identified as the standard fluid momentum source, verified via
an exact background identity. The remaining $\alpha/\mathcal E_\alpha$-
only piece still needs comparison against $\Pi$'s own bracket
structure — not attempted here, the next concrete, bounded step. Gate
4 remains paused. Nothing in `cdot-7/` was touched.

---

## Entry 54 (worker) — the energy constraint, derived directly: an exact match to $\Pi$'s own bracket (2026-07-21)

**Prompt (verbatim):**
> Please go ahead.

**Summary of work performed:**

1. Rather than pursue the momentum-constraint remainder further,
   derived the **energy** constraint directly by varying the already-
   assembled action w.r.t. $\Psi$ (the lapse perturbation already
   present throughout, no new field needed) — $\Psi$ is genuinely
   non-dynamical here (no $\dot\Psi$ anywhere), so $d(\text{action})/d
   \Psi=0$ is the energy constraint directly, the natural parallel to
   §11's shift-vector extraction and §9–§10's alpha-variation.

2. **Built the full $\Psi$-dependent Lagrangian**
   (`wp7_derivation_energy_constraint_attempt.py`, new, `cdot-8/WP7/`):
   $\mathcal Y$ has no $\Psi$-dependence at all (already established in
   §5); only $\mathcal F(\mathcal Y,\mathcal Q)$'s own $\mathcal Q$-
   dependence (via $\gamma$ and $\mathcal Q^{(2)}$) and the Maxwell/J
   terms (via $\mathcal E_\alpha$) carry $\Psi$.

3. **Result: an exact match.** $d(\text{action})/d\Psi$ splits cleanly
   into $2\kappa[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi]$ —
   confirmed, zero symbolic difference, to be **exactly** the published
   $\delta$/$\Pi$ bracket — plus a second, $\gamma$-sector piece not
   yet matched to the standard $(1+w)/(\dot{\bar\phi}c_\text{ad}^2)
   \gamma$ term, reported honestly as unresolved.

**Files produced**: `wp7_derivation_energy_constraint_attempt.py` (new,
`cdot-8/WP7/`), `Update-WP7-InstabilityRecourses-2026-07-21.md` (§13,
new), this entry.

**Status: a major, positive, verified result.** The bracket $[\mathcal
K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi]$ — the structure this whole
sub-derivation has circled since §7 — now falls directly out of an
independent action-level variation, not guessed or reverse-engineered.
This validates the program's own established $(\chi,\alpha,\mathcal
E_\alpha)$ variable set at the level of the actual field equations, not
just the new completion. The unmatched $\gamma$-sector piece and §12's
momentum-constraint remainder are left open for the next round. Gate 4
remains paused. Nothing in `cdot-7/` was touched.

---

## Entry 55 (worker) — advisor confirms §12 and §13's headline result; finds a real sign inconsistency (fixed, doesn't resolve the gap); a more careful hypothesis tried, also negative (2026-07-21)

**Prompt (verbatim):**
> Some adivce added. Let me know if it helps.

**Summary of work performed:**

1. Found `Advisory-WP7-EnergyConstraintBracketConfirmed-2026-07-21.md`.
   §12 confirmed exactly — the $\theta$-attribution hypothesis is "now
   a checked fact." **§13's headline bracket-match result independently
   reproduced and shown unaffected by anything below** (the bracket
   comes purely from Maxwell+$\hat J$ terms, zero $F_\mathcal Q$/
   $F_{\mathcal Q\mathcal Q}$ dependence).

2. **A real sign inconsistency found**: §13's script used $+F_\mathcal
   Q\mathcal Q^{(2)}$, inconsistent with §9/§10's own validated
   $-F_\mathcal Q$ convention. **Independently verified and fixed** in
   `wp7_derivation_energy_constraint_attempt.py` — confirmed the minus
   sign is correct by direct comparison. **Checked whether the fix
   resolves the gap — it does not**; the corrected piece is simply the
   negative of the original.

3. **Tried the advisor's more careful hypothesis** (compare against
   $8\pi\tilde G\bar\rho\,\delta$'s own $\gamma$-term, not bare
   $(1+w)$): substituting the established background identities gives
   exactly $F_\mathcal Q(1+1/c_\text{ad}^2)\gamma-2F_\mathcal Q\dot{\bar
   \phi}\Psi$ — **not** a clean multiple of $\gamma$. Independently
   confirms the advisor's own negative finding.

**Files updated**: `wp7_derivation_energy_constraint_attempt.py`
(sign fixed, docstring extended), `Update-WP7-InstabilityRecourses-
2026-07-21.md` (§14, new), this entry.

**Status: a real bug fixed, the headline §13 result reconfirmed
unaffected, one more honest negative result on the remaining gap.**
The $(\chi,\alpha,\mathcal E_\alpha)$ variable set is now independently
validated at the level of both the vector equation and the energy
constraint's leading structure. This is the eighth consecutive round
(§5–§14) on this sub-derivation; the still-open $\gamma$-sector piece
concerns only the base theory's own bookkeeping, not the new
completion's two already-isolated terms. Flagged for the author's own
judgment on whether to keep chasing it or defer it. Gate 4 remains
paused. Nothing in `cdot-7/` was touched.

---

## Entry 56 (worker) — one more careful shot at the $\gamma$-sector normalization, per the author's request: a genuine, precisely-characterized negative result (2026-07-21)

**Prompt (verbatim):**
> Give the normalisation one more shot.

**Summary of work performed:**

1. **Three independent checks performed**
   (`wp7_derivation_gamma_sector_normalization_attempt.py`, new,
   `cdot-8/WP7/`), each ruling out a plausible error source: (1) a
   fresh, bottom-up re-derivation of the entire $\mathcal F(\mathcal Y,
   \mathcal Q)$ expansion, using independently-named symbols, confirms
   §14's corrected sign convention exactly — no hand-assembly error;
   (2) $\delta_2$ re-derived directly from the unit constraint — exactly
   correct, no propagated error from §5; (3) the normalization constant
   $c_0=-2$ derived **self-consistently** from the already-confirmed
   bracket match itself (not guessed), using the standard, unambiguous
   $\nabla^2\to-k^2$ Fourier convention.

2. **Result**: applying $c_0=-2$ to the $\gamma$-sector piece gives a
   precise, clean residual $F_\mathcal Q(\dot\varphi-3\dot{\bar\phi}
   \Psi)$ — not zero, still not a clean multiple of $\gamma$. A genuine
   negative result, not an assembly artifact, with two concrete
   (unchecked) candidate explanations offered.

**Files produced**: `wp7_derivation_gamma_sector_normalization_
attempt.py` (new, `cdot-8/WP7/`), `Update-WP7-InstabilityRecourses-
2026-07-21.md` (§15, new), this entry.

**Status: a genuine, careful, multiply-cross-checked negative result,
not resolved.** Three plausible error sources ruled out; the residual
is real and now precisely characterized. The headline §13 bracket-match
result stands unaffected. Recommending this now be treated as a
standing, documented open item rather than re-attempted without new
information, while the two confirmed $F_\mathcal Y$-completion terms
and the confirmed bracket are used directly for the next step. Gate 4
remains paused. Nothing in `cdot-7/` was touched.

---

## Entry 57 (worker) — the actual answer to R1's feasibility question: the derived completion does not stabilize the ISW band; target-list item 1 resolved (2026-07-21)

**Prompt (verbatim):**
> Please proceed.

**Summary of work performed:**

1. Assembled the actually-derived R1 modification
   (`wp7_r1_derived_completion.py`, new, `cdot-8/WP7/`), using only
   what §5–§15 confirmed, not guessed: §10's confirmed new term
   ($F_\mathcal Y\dot{\bar\phi}\chi$, contributing to the
   $(\alpha,\mathcal E_\alpha)$ Jacobian's off-diagonal entry only) and
   §13's confirmed result that $\Pi$/$\delta$'s bracket — and hence the
   Jacobian's trace $a_{EE}$ — is completely $F_\mathcal Y$-independent.

2. **Re-ran the stability scan** with this surgical, derived
   modification (Pi/delta/theta all exactly as originally coded, only
   the vector equation's own new term added). **Result: essentially no
   stabilization at the ISW band** — $\max\text{Re}(\lambda)$ at
   $z=1090$ unchanged to 6 significant figures across $\lambda_s\in[-1.5,
   10]$, including exactly at $\lambda_s=-1$ where the earlier crude
   "uniform substitution" guess had found complete stabilization.

3. **This confirms, now derived rather than guessed, the qualitative
   conclusion §6's "refined attribution" heuristic reached by
   structural argument**: the trace $a_{EE}$ dominates and is untouched
   by $F_\mathcal Y$.

**Files produced**: `wp7_r1_derived_completion.py` (new,
`cdot-8/WP7/`), `Update-WP7-InstabilityRecourses-2026-07-21.md` (§16,
new), this entry.

**Status: R1's central feasibility question is now answered, derived
rather than guessed, after eleven consecutive rounds (§5–§16).** R1 is
not a viable recourse for the ISW/growth instability. One honest
caveat not resolved: §12's momentum-constraint-sourced $F_\mathcal Y$
term is not included in this scan (its placement in the coupled system
wasn't pinned down), though it's unlikely to overturn the conclusion
since the trace itself stays confirmed independent of it regardless.
Recommending this be reported to the author/advisor as the resolution
of the commissioned derivation. Gate 4 remains paused; this diagnostic
arc is now substantively complete. Nothing in `cdot-7/` was touched.

---

## Entry 58 (worker) — advisory confirms §16 exactly; R3 (re-closure), a first bounded feasibility scan: a modest dent, not a resolution (2026-07-21)

**Prompt (verbatim):**
> Advisory added, in full agreement with your claims. Let's try R3.

**Summary of work performed:**

1. Found `Advisory-WP7-R1FeasibilityResolvedNotViable-2026-07-21.md`.
   Confirms §15 and §16 exactly, including an independent by-hand trace
   of the new completion term through §10's own result, and confirms
   $\Pi$'s bracket is genuinely left bare in the script. Recommends the
   recourse ladder move to R3 or R4 — author chose R3.

2. **Attempted R3 as a first, bounded feasibility test**
   (`wp7_r3_reclosure_feasibility.py`, new, `cdot-8/WP7/`), explicitly
   scoped as NOT the full joint Q2/EFE re-fit the advisory flags as the
   real, heavier lever: held $\Omega_\text{closure}=0.074$ fixed and
   varied only the neutrino/cold-matter split (lower $M_\nu$, the
   KATRIN-aligned direction), re-running the unmodified closure ODE for
   each value.

3. **Result**: $c_\text{ad}^2(z{=}1090)$ moves from $-0.219$ to
   $-0.126$ (roughly halved) as $M_\nu\to0$ (an unphysical endpoint),
   and the instability drops correspondingly but **stays
   catastrophically large** ($3.36\times10^8\to1.64\times10^8$ at
   $z=1090$) — nowhere close to stabilizing. At $z=10$ the instability
   actually **worsens slightly** as $M_\nu\to0$.

**Files produced**: `wp7_r3_reclosure_feasibility.py` (new,
`cdot-8/WP7/`), `Update-WP7-InstabilityRecourses-2026-07-21.md` (§17,
new), this entry.

**Status: R3's cheap, bounded first test is negative on its own but
does not close the door on the full re-fit.** The neutrino/cold split
alone moves $c_\text{ad}^2$ in the right direction but by an
insufficient amount, and not even monotonically across all redshifts —
confirming the advisory's own caution that this lever cannot be tuned
in isolation. The heavier, synergistic lever (a joint re-fit letting
$E(z)$ itself respond) has not been attempted. Recommending this be
reported back before deciding on the full re-fit vs. R4. Gate 4 remains
paused; Gate 3's Q2/EFE sequencing remains the standing prerequisite.
Nothing in `cdot-7/` was touched.
