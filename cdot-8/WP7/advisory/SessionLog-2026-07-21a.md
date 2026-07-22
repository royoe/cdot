# Session Log — WP7 Advisory, 2026-07-21

*Running log for `cdot-8/WP7/advisory/` work, appended per-prompt, per
this project's convention. Continues from `SessionLog-2026-07-20.md`.
Provenance note carried forward: these entries are an advisor session
conducted directly with the author, with the author acting as
intermediary because the primary advisor (Fable 5) was unavailable on
token limits.*

---

## Entry 1 — §39's repelling-Riccati diagnosis confirmed analytically (rate $=\lambda_\text{unstable}-\lambda_\text{stable}$, unconditionally positive); simpler fix found and tested — drop the Riccati ODE, reuse Stage 3c's pointwise slaving with the handoff moved to $z\approx30$–$45$ instead of $z_\text{switch}=18.5$ (advisor session, 2026-07-21)

**Prompt (verbatim):**
> The worker has attempted, but hit another blocker. Please advice.

**Summary.** Read §39: implementing the accepted two-phase (Riccati
then explicit) design exactly to spec, the worker found the corrected
run still fails — the same "step size less than spacing between
numbers" error, now traced to the Riccati phase itself, at every
handoff redshift tried (including deep inside the supposedly-safe
real-eigenvalue region). Correctly diagnosed: linearizing around the
Riccati's stable fixed point shows the coefficient is always positive
— the physically-correct (stable) branch is itself a repeller under
forward-$N$ propagation, a known phenomenon in Riccati/shooting-method
numerics. Routed the choice of integration strategy (backward
propagation vs. a compound/unnormalized-vector formulation) to the
advisor as the fifth consecutive round on this sub-problem.

**Confirmed the diagnosis analytically before proposing anything**:
re-derived the linearized rate independently, $d(\delta\mu)/dN=
(a_{EE}-2\mu^*/H_c)\delta\mu$, and using $\mu^*=H_c\lambda$,
$a_{EE}=\lambda_\text{stable}+\lambda_\text{unstable}$, showed the rate
at the stable root is exactly $\lambda_\text{unstable}-\lambda_
\text{stable}$ — unconditionally positive by construction (not just
near the eventual threshold), matching a direct finite-difference check
on the Riccati RHS exactly at seven redshifts from $z=60$ to $z=30$.

**Rather than implement backward integration or a compound-vector
reformulation, tried a simpler alternative first — and it worked.**
Stage 3c's original pointwise algebraic slaving (re-solve
$\dot{\mathcal E}_\alpha=0$ fresh at every step, propagating nothing)
was never actually the problem; the problem was always the handoff
redshift ($z_\text{switch}=18.5$, deep inside the zone where the
frozen-coefficient approximation and $\text{coef}_E$ are both already
unreliable, per Entries 5–6). Moved the handoff to $z\approx30$–$45$
instead and reran: smooth, monotonically convergent
($\delta_b(z{=}0)$ from $0.436$ at $z_\text{handoff}=45$ to $0.374$ at
$z_\text{handoff}=30.2$, right at the edge of the real-eigenvalue
region) — no blow-up anywhere, nothing like Stage 3d's
eight-orders-of-magnitude sensitivity. **This works because pointwise
slaving never propagates $\mu$ as its own state, so there is nothing
for the repelling flow to act on**, and it's an excellent
leading-order approximation everywhere $|\lambda(N)|\gg1$
($z\gtrsim30$–$40$).

**Recommendation**: adopt this directly — Stage 3c's pointwise closure
with the handoff relocated to $z\approx35$ (comfortable margin), full
explicit integration below. Retire the Riccati-ODE approach as a
practical matter (§38's derivation and discriminant identity remain
correct and worth keeping on record, but the fix doesn't need them).
The possible second unstable direction in the full 6-variable system
remains open and unconfirmed, unaffected by this fix.

**Files produced (Entry 1):**
`Advisory-WP7-Stage3fPointwiseFixWorks-2026-07-21.md`,
`wp7_stage3f_pointwise_conservative_handoff.py`, this log entry.

**Open items handed forward:** adopt the pointwise-slaving/conservative-
handoff design as the closure going forward (worker's next action);
the possible second unstable direction in the full 6-variable system,
still flagged, still not confirmed; optional AeST-native cross-check
(from Stage 3b); $Q_2$/EFE sequencing; Gate 1(b)'s caveat; KATRIN watch.

---

## Entry 2 — Stage 4 hits a serious, escalation-worthy finding: the vector-sector instability never resolves at the actual ISW-relevant $k$ range — both §41 (no second unstable direction) and §42 (the catastrophic ISW-scale blow-up) independently confirmed to machine precision; read as the already-accepted negative-$c_\text{ad}^2$ mechanism reaching further in $k$ than expected, not a new pathology, but still directly threatens WP7's deliverable — recommended routing to the author now, alongside Gate 1(b) (advisor session, 2026-07-21)

**Prompt (verbatim):**
> Attempting stage 4 hit another problem. Please assess and advice.

**Summary.** Read §41 (Stage 3g, the full 6-variable stability audit,
built analytically to resolve the advisor's own earlier
finite-difference precision concern) and §42 (Stage 4, the first ISW
assembly attempt). §41: an exact, hand-derived $6\times6$ Jacobian
(validated against complex-step differentiation, exact to machine
precision, catching one of the worker's own transcription slips first)
found no second unstable direction — the full system's largest
eigenvalue is smaller than the isolated $(\alpha,\mathcal E_\alpha)$
pair's own (back-coupling damps it, a conservative direction), and a
separate small, persistent low-$z$ real eigenvalue is confirmed (via a
$\kappa\to0$ isolation test) to be the already-known scalar tachyonic
mode, not vector-sourced. §42: assembling the validated growth closure
with the M5 Einstein-constraint term and running at the actual
ISW-relevant $k$ ($\ell=2,5,10\to k\approx1.1$–$5.4\times10^{-3}\,
\text{Mpc}^{-1}$, per the established $k=\ell/D_p(z{=}0.5)$ convention)
blew up catastrophically — traced to the vector sector's fast
eigenvalue simply never crossing zero from $z=100$ to $z=0$ at these
$k$ (unlike the single, smaller $k=10^{-4}$ validated throughout
Stages 3b–3g), confirmed via the same machine-precision $6\times6$
Jacobian, not an artifact of the reduced picture or of pointwise
slaving. Correctly ruled out an M5-assembly artifact (§7's exact
cancellation means the field equations are M5-independent at every
$k$) and declined to declare a unilateral verdict, recommending advisor
review and the AeST-native cross-check as the most informative next
diagnostic.

**Both findings independently confirmed, to machine precision, not
accepted on account**: reran `wp7_stage3g_full_system_stability_audit.py`
directly — analytic-vs-complex-step residuals matched the reported
$\sim10^{-16}$ at every checked redshift; the eigenvalue scan and the
$\kappa\to0$ isolation test ($0.048\to0.0465$ at $z=10$; $0.255$ vs.
their $0.257$ at $z=0$) both reproduced closely. Ran
`wp7_stage4_isw_estimate.py` directly (one environment-only
`numpy.trapz` incompatibility hit and worked around with a one-line
monkey-patch, not a file edit — flagged so it isn't mistaken for a bug
in the script) and reproduced the reported blow-up exactly (e.g.
$\ell=5$: $\Phi_\text{std}/\Phi_i=-1.02\times10^7$ by $z=0$).
**Independently re-derived the core claim directly from the trusted
Jacobian** rather than only re-running the nonlinear integration:
scanned $\max\text{Re}(\lambda)$ at the three exact ISW $k$ values from
$z=100$ to $z=0$ — never crosses zero at any of them (e.g. $\ell=5$:
$1652$ at $z=100$, a *local minimum of $11.0$* near $z=0.5$, rising
again to $23.7$ by $z=0$). Contrasted directly against the already-
validated $k=10^{-4}$ case on the same Jacobian: it genuinely dips to
$\approx0.01$ near $z=18$–$20$ before settling at the small,
already-accepted residual ($0.25$–$0.38$) — a qualitatively different
trajectory, not merely a smaller version of the ISW-$k$ one.

**Offered a reframing, not just a confirmation**: rather than "a
different, more serious, unrelated instability," read this as the
*same* $c_\text{ad}^2<0$ mechanism already accepted since §23/27,
reaching further in $k$ than anyone had reason to check before Stage 4
forced the question. A negative effective pressure is destabilizing,
not restoring, in the dispersion relation — larger $k$ makes growth
*worse*, the opposite of ordinary Jeans stabilization — exactly
matching why $k=10^{-4}$ resolves comfortably while $k\gtrsim10^{-3}$
(only one-to-one-and-a-half decades larger) never does. **This changes
how surprising the finding is, not its severity**: $\Phi$ growing by
5–8 orders of magnitude by $z=0$ is nowhere near anything consistent
with the observed, mild ISW effect, regardless of how well-motivated
the underlying mechanism is.

**Recommendation**: don't hunt for a bug first — every check (M5
on/off, the exact Jacobian, the $\kappa\to0$ isolation) points at this
being the linear theory's genuine behavior under cdot-8's own forced
$F(Q)$, consistent with everything already accepted, not contradicting
it. Don't jump straight to the AeST-native cross-check either, even
though it's the most informative single next diagnostic (does AeST's
own tuned $K(Q)$ share this, meaning it's generic to the imported
field-perturbation system, or is it specific to cdot-8's own
zero-freedom $F(Q)$) — it's a real side-project, and per this
program's own standing practice, a finding that a work package's
central deliverable may not be achievable as scoped gets escalated to
the author, not decided by advisor-and-worker alone. Recommended
routing this to the author now, stated plainly, alongside Gate 1(b)'s
own still-open background tension — two independent open structural
questions the author may want to weigh together.

**Files produced (Entry 2):**
`Advisory-WP7-Stage4ISWInstabilityAssessed-2026-07-21.md`, this log
entry. No new script — verification reused
`wp7_stage3g_full_system_stability_audit.py`'s own analytic Jacobian
directly.

**Open items handed forward:** author input on sequencing (new,
recommended now, alongside Gate 1(b)); the AeST-native cross-check,
ready to run once authorized; $Q_2$/EFE sequencing; KATRIN watch.

---

## Entry 3 — R0/R1/R2 cross-checked: all three confirmed (R0(a) verified verbatim against primary source, R0(b) re-derived by hand, R1 and R2 reproduced numerically exactly) — plus one new finding neither the main advisor nor the worker caught: the founding paper's own stability section states a separate $\lambda_s>0$ condition that R1's recommended direction ($\lambda_s\to-1$) directly contradicts (advisor session, 2026-07-21)

**Prompt (verbatim):**
> Please check WP7 for updates and also advise from the main advisor.
> Assess the progress on R0, R1 and R2 and cross-check.

**Summary.** Read the main advisor's `Advisory-WP7-InstabilityRecourses-2026-07-21.md`
(woken specifically for the Stage-4 instability, per
`SessionLog-2026-07-21b.md`) and WP7 §43–46: §43 (my own Stage-4
advisory confirmed by the worker, plus a genuine `np.gradient`
`edge_order` boundary artifact caught in the $z\to0$ endpoint —
corrected floor $\sim8$–$9$, not $\sim24$, verdict unchanged), the main
advisor's mechanism-pinning (anti-Jeans branch of the accepted
$c_\text{ad}^2<0$ sign, rate $\sim|c_\text{ad}|k/aH$) and recourse
ladder (R0 audit → R1 $\mathcal Y$-sector completion → R2 AeST-native
cross-check → R3 re-closure → R4 nonlinear-saturation fallback), and
the worker's R0/R1/R2 attempts (§44–46): R0(a) confirms the founding
paper's own stability argument assumed $F_\mathcal Q(\text{
background})=0$, which cdot-8 never approaches; R0(b) traces the
instability to a single, dominant, $\kappa$-linear term in the exact
slot an $F_\mathcal Y(0,\mathcal Q)$ completion would renormalize; R2
shows AeST's own native, minimum-tracking tuning stays stable at the
same ISW $k$'s where cdot-8 never restabilizes; R1 shows a hypothesized
$(2-\mathcal K_B)\to(2-\mathcal K_B)(1+\lambda_s)$ substitution
suppresses the instability by many orders of magnitude as $\lambda_s
\to-1$, with the honest caveat that no action-level derivation of this
substitution exists yet and $\lambda_s=-1$ sits exactly at the paper's
own stated healthy-range boundary.

**All four checks (R0(a), R0(b), R1, R2) independently confirmed —
three numerically exact, one against primary source directly, not on
citation.** Re-derived R0(b)'s four-term decomposition by hand from the
$\mathcal E_\alpha$ equation's own substitutions before trusting the
script (matches exactly — $B$, the sole $\kappa$-dependent piece, is
even more dominant at high $z$ than reported, four-and-a-half orders of
magnitude at $z=100$ rather than the quoted one-to-two). Read
`references/arXiv.2007.00082/newRMONDLett.tex`'s "Stability and waves"
section directly for R0(a): the quoted $F_\mathcal Q(\text{background})
=0$ assumption, and the vector/scalar dispersion relations R1 draws its
healthy range from, all match verbatim. Ran `wp7_r1_gradient_completion_feasibility.py`
and `wp7_r2_aest_native_crosscheck.py` directly: every reported number
reproduced to the stated precision (one trivial, inconsequential
`np.gradient`-edge artifact noted in R2's own $z=0$ printout, not
affecting its stability verdict).

**Found something neither party flagged**: reading the same
primary-source paragraph one sentence further than R0(a)/R1 quote it,
the paper states a **second, separate stability condition** — "the
Hamiltonian for the [$\omega=0$, linearly-growing vector] mode is
positive for momenta larger than $\sim\mu$ and otherwise negative,
*also requiring that $\lambda_s>0$*" — distinct from the $\lambda_s>-1$
condition on the propagating ($\omega\neq0$) modes that R1's own
"healthy range" comes from. **R1's own recommended suppression range
($\lambda_s$ negative, approaching $-1$) sits entirely inside the
region this second condition appears to exclude.** Could not fully
resolve from the compact PRL text alone how binding this is (the
Hamiltonian analysis is cited to unavailable in-preparation companion
papers, and the paper's very next sentence frames low-momentum
negativity as an expected, tolerated Jeans-type feature) — but the
condition is stated explicitly, and directly conflicts with R1's
favored operating point. Added this as a second, independent open item
for R1's eventual action-level derivation to resolve, alongside the
already-flagged missing FRW derivation itself.

**Files produced (Entry 3):**
`Advisory-WP7-R0R1R2CrossCheck-2026-07-21.md`, this log entry. No new
script — verification reused the existing R0/R1/R2 scripts directly,
plus a direct read of the archived primary source.

**Open items handed forward:** the $\lambda_s>0$ condition's status in
the FRW (not Minkowski) setting, to be resolved alongside R1's own
already-flagged missing action-level derivation; author sequencing
decision on R0–R4 (standing, now with this additional nuance to weigh);
$Q_2$/EFE sequencing; Gate 1(b)'s caveat; Gate 4's paused status;
KATRIN watch.

---

## Entry 4 — §5's $\mathcal Y$-identity derivation reviewed and confirmed (bug-fix included); the "uniform substitution too crude" caution independently verified directly from the action itself; a bounded, concrete path through the remaining attribution problem identified (advisor session, 2026-07-21)

**Prompt (verbatim):**
> We are progressing on the reconciliation track, but the worker found
> issues with the uniform substitution hypothesis. Please review the
> assessment of the main advisor and the worker's progress so far, and
> advice.

**Summary.** Read the main advisor's `Advisory-WP7-RecourseRoundAssessed-2026-07-21.md`
(§4 of `Update-WP7-InstabilityRecourses-2026-07-21.md`, already
cross-checked in Entry 3) and the worker's subsequent §5: the first
piece of the commissioned action-level FRW derivation, working out
$\mathcal Y=q^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi$ to quadratic order.

**§5's core result reran independently** (`wp7_derivation_Y_identity.py`):
reproduces $\mathcal Y=a^{-2}(\nabla_i\chi)^2$ exactly, via two
structurally independent computations agreeing (not asserted, actually
demonstrated). The bug-fix (a missing second-order correction to
$A_0$, needed once the spatial part of the unit-timelike constraint is
included at $O(\epsilon^2)$) independently re-derived and confirmed
correct.

**The worker's own caution — that R1's "uniform substitution"
hypothesis is now known to be too crude — verified independently and
more sharply, directly from the action** (`newRMONDLett.tex` lines
336–347, read in full): $(2-\mathcal K_B)$ appears in **three**
structurally distinct places — a bare $-(2-\mathcal K_B)\mathcal Y$
term (the one that *does* get the $F_\mathcal Y$ correction), a
separate $+2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi$ term (built from
the aether's own covariant acceleration, which does *not*), and
$\mathcal F(\mathcal Y,\mathcal Q)$'s own background-level piece
(already correctly handled in the existing Y=0 derivation). This is a
structural guarantee, not just a plausible concern.

**A useful negative result**: checked that the paper's own
linear-perturbation section (lines 425–490, the one this whole WP7 arc
imports from) was derived with $\mathcal Y\equiv0$ built in from its
first line — there is no already-worked-out general-$\mathcal Y$
version of $\chi/\Pi/\mathcal E_\alpha$ to be found by reading further;
the attribution work is a genuine, necessary derivation, not a
shortcut waiting to be noticed.

**The worker's proposed shortcut (vary $-F_\mathcal Y(0,\bar{\mathcal
Q})\mathcal Y$ alone, add linearly to the existing equations) confirmed
mathematically sound** — $\mathcal Y$ starts at quadratic order with no
linear piece, so no higher-order correction is missed. **Sharpened it
further**: since this new term is functionally identical to the bare
$\mathcal Y$-term already in the action, its contribution to every
field equation has the *same functional form* as that bare term's,
scaled by $\lambda_s$. This narrows the remaining task from "redo the
full coupled variation" to "identify which existing $(2-\mathcal
K_B)$-proportional pieces in $\chi/\Pi/\mathcal E_\alpha$ trace to the
bare $\mathcal Y$-term specifically (get the $\lambda_s$ correction
automatically) versus the $\hat J^\mu\nabla_\mu\phi$ term (don't)" — a
bounded, checkable next step, reusing the $\chi$-projection machinery
§5 already built rather than re-deriving the whole system from scratch.

**Files produced (Entry 4):**
`Advisory-WP7-YIdentityDerivationReviewed-2026-07-21.md`, this log
entry. No new script — reused `wp7_derivation_Y_identity.py` directly,
plus a direct read of `newRMONDLett.tex` (full covariant action and
linear-perturbation section).

**Open items handed forward:** the worker's own narrower attribution
task (identify $\mathcal Y$-sourced vs. $\hat J$-sourced $(2-\mathcal
K_B)$ occurrences in $\chi/\Pi/\mathcal E_\alpha$), now with a concrete
strategy rather than an open-ended re-derivation; the $\lambda_s>0$
tension (Entry 3, unresolved); author sequencing decision on R0–R4;
$Q_2$/EFE sequencing; Gate 1(b)'s caveat; Gate 4's paused status;
KATRIN watch.

---

## Entry 5 — §6's refined-attribution divergence confirmed numerically and diagnostically (the "large fixed trace" claim independently re-derived, not just re-run), but the attribution criterion itself has a specific, previously-unflagged weak point: $\hat J_\mu$'s own spatial component is plausibly also a gradient-dotted-with-gradient structure, undermining the clean "Laplacian=$\mathcal Y$, friction=$\hat J$" split — a third reason to prioritize the actual coupled variation now (advisor session, 2026-07-21)

**Prompt (verbatim):** "Please check the progress..."

**Summary.** Checked WP7 for updates since Entry 4: the worker had
added §6 to `Update-WP7-InstabilityRecourses-2026-07-21.md`, applying
Entry 4's sharpening to produce a refined attribution of $(2-\mathcal
K_B)$'s occurrences in $\Pi/\mathcal E_\alpha$, and a new script,
`wp7_r1_refined_attribution.py`.

**Reran the script directly**: the headline result (max Re($\lambda$)
at $z=1090$ essentially unchanged, $3.355851\times10^8$, across
$\lambda_s=0$ to $-2$, despite $a_{\mathcal E_\alpha,\alpha}$ itself
swinging from $1.39\times10^{14}$ to $-1.39\times10^{14}$) reproduces
exactly. **Went further than the write-up and independently derived
*why*, by hand**: worked out the $2\times2$ eigenvalue formula's
discriminant explicitly and found $a_{EE}^2\approx1.126\times10^{17}$
dominates $4a_{\mathcal E_\alpha,\alpha}/H$ (which ranges only
$\pm\sim7\times10^{10}$ across the tested $\lambda_s$ range) by seven
orders of magnitude — confirming, not just asserting, that the large
fixed trace alone determines the dominant eigenvalue here, with all of
$\lambda_s$'s effect absorbed into the subdominant root.

**Found a specific, checkable weak point in the attribution criterion
itself**, not previously flagged by anyone: the criterion assumes
$\hat J^\mu\nabla_\mu\phi$ (the base action's separate term) is a pure
friction/mass-type structure with no spatial-gradient character, in
contrast to $\mathcal Y$'s pure-Laplacian character. But $\hat J_\mu=
\hat A^\alpha\nabla_\alpha\hat A_\mu$'s spatial component, at linear
order, is built from time-derivatives of $\partial_i\alpha$ — itself
already a spatial gradient — so $\hat J^i\nabla_i\phi$ is plausibly
also a gradient-dotted-with-gradient structure, which by the same
integration-by-parts logic that justifies $\mathcal Y\Rightarrow
\nabla^2$ would also produce some $\nabla^2$-type field-equation
contribution. Not fully checked (requires the perturbed Christoffel
symbols contracted into $\hat J_\mu$, not attempted here), but a
concrete, specific reason to distrust the clean dichotomy, not a vague
call for more rigor.

**Net effect**: three independent signals now converge on the same
recommendation — the two R1 attribution heuristics disagree starkly,
neither is derived, and the refined one's own assumption has an
identified gap. None of this kills R1, but neither numerical result
(uniform-substitution's "stabilizes by orders of magnitude" or refined-
attribution's "barely responds") should be reported as more than a
bracket. Recommending the actual coupled variation (varying $-F_
\mathcal Y(0,\bar{\mathcal Q})\mathcal Y$ directly through the same
route that produced $\chi/\Pi/\mathcal E_\alpha$, reusing §5's own
machinery) be prioritized now rather than exploring further heuristic
attributions.

**Files produced (Entry 5):**
`Advisory-WP7-RefinedAttributionAssessed-2026-07-21.md`, this log
entry. No new script — reused `wp7_r1_refined_attribution.py` directly
plus a hand-derived eigenvalue/discriminant check.

**Open items handed forward:** the actual coupled-variation derivation
for the $F_\mathcal Y(0,\bar{\mathcal Q})\mathcal Y$ term (now the
single most load-bearing next step for R1, per three independent
signals); whether $\hat J^i\nabla_i\phi$ itself contributes any
$\nabla^2$-type term (open, flagged, not yet checked); the $\lambda_s>0$
tension (Entry 3, still unresolved); author sequencing decision on
R0–R4; $Q_2$/EFE sequencing; Gate 1(b)'s caveat; Gate 4's paused status;
KATRIN watch.

---

## Entry 6 — §7's $\hat J_i=\partial_i\mathcal E_\alpha$ identity confirmed exactly: the flagged weak point was real, resolved by direct computation rather than argument, sharpened into a genuine $\mathcal E_\alpha$–$\varphi$ cross-term; one simplification offered for the next step (advisor session, 2026-07-21)

**Prompt (verbatim):** "Good progress. One more touchpoint and check
before we proceed."

**Summary.** Checked WP7 for updates since Entry 5: the worker had
added §7 to `Update-WP7-InstabilityRecourses-2026-07-21.md`, directly
computing the weak point flagged in Entry 5/`Advisory-WP7-
RefinedAttributionAssessed-2026-07-21.md` §3 (whether $\hat J_\mu$'s
spatial component carries gradient structure), via a new script,
`wp7_derivation_Jhat_identity.py`.

**Reran the script directly**: confirms $\hat J_i=\partial_i(\Psi+
\dot\alpha)=\partial_i\mathcal E_\alpha$ exactly, using the perturbed
$(t,x^1)$ Christoffel symbols. Spot-checked the underlying formula
($\hat J_\mu=\hat A^\alpha\partial_\alpha\hat A_\mu-\hat A^\alpha
\Gamma^\beta_{\alpha\mu}\hat A_\beta$, standard $\Gamma^a_{bc}$
construction) by hand against the code, not just the printed output —
correctly implemented.

**The flagged concern was real, and resolved the right way**: rather
than debate the qualitative point further, the worker computed the
exact quantity — sharper than the concern itself anticipated (not
"some gradient of $\alpha$," but exactly $\partial_i\mathcal E_\alpha$,
already one of the program's own established variables). This confirms
the base action's $2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi$ term's
spatial piece is $\propto a^{-2}\partial_i\mathcal E_\alpha\partial_i
\varphi$ — a genuine cross-term between $\mathcal E_\alpha$ and
$\varphi$, structurally distinct from both $\mathcal Y$'s self-gradient-
squared form and a bare friction term, confirming neither of §6's two
attribution hypotheses could have captured it.

**One simplification offered**: since $\chi\equiv\varphi+\dot{\bar\phi}
\alpha$, the cross-term rewrites as $a^{-2}\partial_i\mathcal E_\alpha
(\partial_i\chi-\dot{\bar\phi}\partial_i\alpha)$ — entirely in terms of
the program's own three standing variables ($\mathcal E_\alpha,\chi,
\alpha$), which should make the still-outstanding coupled-variation
step more directly comparable, term-by-term, with the already-published
$\chi/\Pi/\mathcal E_\alpha$ equations.

**Endorsed the worker's own checkpoint decision**: three consecutive
rounds (§5, §6, §7) have each surfaced real, non-obvious structure in
this one sub-problem — pausing for review here rather than pushing
straight into the full coupled variation is the right call, consistent
with this program's standing discipline.

**Files produced (Entry 6):**
`Advisory-WP7-JhatIdentityConfirmed-2026-07-21.md`, this log entry. No
new script — reused `wp7_derivation_Jhat_identity.py` directly; the
$\chi$-substitution is algebra only, not scripted.

**Open items handed forward:** the full coupled variation (varying both
$\mathcal Y$'s and $\hat J^\mu\nabla_\mu\phi$'s contributions together
through the Einstein-constraint/vector-equation system, using the
$\chi/\mathcal E_\alpha$ form as a starting simplification) — now the
single, well-located next step; the $\lambda_s>0$ tension (Entry 3,
still unresolved); author sequencing decision on R0–R4; $Q_2$/EFE
sequencing; Gate 1(b)'s caveat; Gate 4's paused status; KATRIN watch.

---

## Entry 7 — §8 confirmed exactly ($\hat J_0=0$); §9's first coupled-variation attempt reproduces as reported, but checking its own stated "$\chi$ independent of $\alpha$" convention finds a real fix, resolving residual mismatch (1) exactly and for free — with a new, third open item surfacing in its place (advisor session, 2026-07-21)

**Prompt (verbatim):** "Quick review round again."

**Summary.** Checked WP7 for updates since Entry 6: the worker had
added §8 ($\hat J_0=0$, extending §7's script) and §9 (the first
attempt at the full coupled variation,
`wp7_derivation_coupled_variation_attempt.py`) to `Update-WP7-
InstabilityRecourses-2026-07-21.md`.

**§8 reproduces exactly**: $\hat J_0=0$ and the orthogonality check
$\hat A^\mu\hat J_\mu=0$ both confirmed identically on rerun. Clean, no
issues — the $\hat J^\mu\nabla_\mu\phi$ term reduces entirely to its
spatial piece, one fewer moving part for the coupled variation.

**§9's own reported numbers reproduce exactly** on rerun (the Maxwell-
friction sanity check, and both listed residual mismatches).
**Checked the script's own stated convention rather than accepting
it**: it treats $\chi$ as "independent of $\alpha$... the paper's own
convention," but $\chi\equiv\varphi+\dot{\bar\phi}\alpha$ is not
actually independent of $\alpha$ — the genuinely independent fields are
$\varphi$ and $\alpha$, and holding $\chi$ fixed while varying $\alpha$
silently forces $\varphi$ to co-vary, a different (incorrect) variation
from holding $\varphi$ fixed. **Redid the variation the correct way**
(new script, `wp7_chi_dependence_check.py`): assembled the same
Lagrangian with $\chi\to\varphi+\dot{\bar\phi}\alpha$ substituted
throughout, varied at fixed $\varphi$, then rewrote the result in terms
of $\chi$ afterward (a pure relabeling, not a re-variation). Two
independent routes to this were tried before trusting it — the first
briefly disagreed with the second due to inadvertently conflating
"fixed $\chi$" with "fixed $\varphi$" in its own algebra; the
discrepancy was traced and resolved before reporting, not smoothed
over.

**Result**: the corrected $\chi$-coefficient becomes exactly $(2-
\mathcal K_B)H+(2-\mathcal K_B)\dot{\bar\phi}+F_Q/2+F_\mathcal Y\dot{
\bar\phi}$ — matching the published $(2-\mathcal K_B)(H+\dot{\bar\phi})
+F_Q/2$ exactly, plus one extra $F_\mathcal Y\dot{\bar\phi}\chi$ term
plausibly reflecting genuine new physics from the completion itself
(absent from the published, $F_\mathcal Y=0$ equation for exactly that
reason, not because it's wrong). **This resolves the worker's own
reported "residual mismatch (1)" exactly and for free**, via a
mechanical fix rather than the not-yet-derived $\Pi$/momentum-
constraint contribution the worker's own docstring speculated as the
explanation.

**Not a complete resolution, reported honestly**: a $(2-\mathcal
K_B)\dot\chi$ term, present in both the original and corrected
derivations unchanged, has no counterpart anywhere in the published
$\mathcal E_\alpha$ equation — a third open item, not on the worker's
original list, plausibly (redirecting the worker's own $\Pi$-instinct)
where the momentum-constraint's separate origin actually re-enters.
Mismatch (2) also shifts rather than resolves under the fix (drops one
term, gains another, still needs the background-EOM substitution the
worker already proposed).

**Files produced (Entry 7):**
`Advisory-WP7-CoupledVariationChiIndependenceCaught-2026-07-21.md`,
`wp7_chi_dependence_check.py` (new, standalone, reruns cleanly), this
log entry.

**Open items handed forward:** adopt the fixed-$\varphi$ variation for
the next iteration (straightforward substitution, demonstrated); the
now-isolated $(2-\mathcal K_B)\dot\chi$ term (new, most plausibly tied
to the still-missing $\Pi$/momentum-constraint derivation); mismatch
(2)'s background-EOM substitution (still open, now from a shifted
starting point); this advisory's own correction recommended for
independent re-verification given two manual approaches briefly
disagreed before resolution; the $\lambda_s>0$ tension (Entry 3, still
unresolved); author sequencing decision on R0–R4; $Q_2$/EFE sequencing;
Gate 1(b)'s caveat; Gate 4's paused status; KATRIN watch.

---

## Entry 8 — §10 confirmed exactly: worker independently reproduced the $\chi$-independence fix, derived an exact background identity, and showed the residual's $\dot\varphi$ piece traces exactly to $\Pi$'s own $\gamma$-term — one precise, checkable target identified for what remains (advisor session, 2026-07-21)

**Prompt (verbatim):** "Good progress now. Please do another quick
review."

**Summary.** Checked WP7 for updates since Entry 7: the worker added
§10 to `Update-WP7-InstabilityRecourses-2026-07-21.md`, independently
reproducing Entry 7's $\chi$-independence fix and extending it via a
new script, `wp7_derivation_coupled_variation_varphi_fixed.py`.

**Reran the script directly and checked the algebra by hand, not just
the printed output**: the residual (derived vector-EOM minus the
published $\chi/\alpha/\mathcal E_\alpha$-explicit terms, $\Pi$
deliberately excluded) regroups exactly into three pieces — $(2-
\mathcal K_B)\dot\varphi$, $F_\mathcal Y\dot{\bar\phi}\chi$ (expected
new physics from the completion), and $-(2-\mathcal K_B)(1-3c_\text{
ad}^2)H\dot{\bar\phi}\alpha$ — confirmed by direct algebraic expansion.
**Independently re-derived the background identity** $\ddot{\bar\phi}=
-3Hc_\text{ad}^2\dot{\bar\phi}$ from $a^3F_\mathcal Q=\text{const}$ and
the primary source's own $c_\text{ad}^2$ definition: exact, not an
approximation. **Independently re-derived $\Pi$'s leading $\gamma$-term
contribution** from the primary source's own $\delta$/$\Pi$ formulas:
matches the script's computation exactly, confirming the $\dot\varphi$
piece of the residual really does trace to $\Pi$'s momentum-constraint
origin — a structural confirmation, not just an elimination argument.

**One precise target identified, sharper than "still needs checking"**:
the residual carries **zero** net $\Psi$-dependence, while $\Pi$'s
leading $\gamma$-term carries a nonzero $-(2-\mathcal K_B)\dot{\bar\phi}
\Psi$ piece with no current counterpart. This is a falsifiable
prediction for the next step: $\Pi$'s own gradient/$\kappa_3$-bracket
piece (not yet derived) must supply a term that cancels this exactly,
leaving zero net $\Psi$-dependence — giving the still-open $\Pi$
derivation a specific number to check against rather than an
open-ended one.

**Files produced (Entry 8):**
`Advisory-WP7-PiGammaTermMatchConfirmed-2026-07-21.md`, this log entry.
No new script — verification reused
`wp7_derivation_coupled_variation_varphi_fixed.py` directly.

**Open items handed forward:** derive $\Pi$'s $\kappa_3$-bracket piece
from the $0i$ Einstein/momentum constraint (the single remaining piece
this five-round sub-derivation has converged on), checked against the
$\Psi$-cancellation prediction above; the $\lambda_s>0$ tension (Entry
3, still unresolved); author sequencing decision on R0–R4; $Q_2$/EFE
sequencing; Gate 1(b)'s caveat; Gate 4's paused status; KATRIN watch.

---

## Entry 9 — §11's first $\Pi$-momentum-constraint attempt: all five sub-results confirmed exactly, the assembly step independently re-derived and verified (not just its inputs), and a concrete, untested hypothesis offered for the honestly-flagged "bare $F_\mathcal Q$" gap (advisor session, 2026-07-21)

**Prompt (verbatim):** "Please assess worker progress."

**Summary.** Checked WP7 for updates since Entry 8: the worker added
§11 to `Update-WP7-InstabilityRecourses-2026-07-21.md`, attempting
$\Pi$'s own momentum-constraint derivation directly, via a genuine
shift perturbation $g_{01}=\epsilon B(t,x^1)$ extending the Christoffel
machinery already validated in §7/§8
(`wp7_derivation_momentum_constraint_attempt.py`, new).

**All five reported sub-results reproduce exactly on rerun**: $\hat
J_\mu$ (lower index) has zero $B$-dependence; $\hat J^\mu\nabla_\mu
\phi$'s $B$-linear piece is $B\dot{\bar\phi}\partial_1\mathcal
E_\alpha/a^2$; $\mathcal Q$'s and $\mathcal Y$'s own $B$-linear pieces
match exactly; the Maxwell term has exactly zero $B$-dependence.

**Went further than re-running the script**: independently reassembled
the candidate $T^0_{\ 1}$ from the five raw sub-results, using the
action's own signs, without reference to the write-up's own algebra —
and confirmed it matches the quoted candidate expression exactly (zero
symbolic difference). This verifies the *assembly step*, not just its
inputs.

**One presentation note, not a computational issue**: the isolated
$F_\mathcal Q$-proportional piece is $F_\mathcal Q(\partial_1\varphi-
\dot{\bar\phi}\partial_1\alpha)$, proportional to $\varphi-\dot{\bar
\phi}\alpha$, not $\chi$ itself as the write-up's phrasing suggests —
though the *combined* candidate expression is confirmed identical
either way; the underlying numbers are unaffected.

**A concrete, untested hypothesis offered for the honestly-flagged
gap**: this leftover piece is built purely from $\varphi$ and $\alpha$,
and the primary source's own scalar-sector variable $\theta\equiv
\varphi/\dot{\bar\phi}$ (already verified) is defined directly and only
from $\varphi$ — suggesting the leftover piece may belong to $\theta$'s
own momentum-constraint content, not to $\Pi$'s bracket at all. Not
checked here, but flagged as the cheapest of the write-up's own three
candidate explanations to test, since it only requires comparing
against an already-established primary-source formula.

**Endorsed the worker's checkpoint decision** — six consecutive rounds
(§5–§11) surfacing real structure in this one sub-derivation is a lot
to have converged this cleanly; pausing here rather than forcing a
match is the right call.

**Files produced (Entry 9):**
`Advisory-WP7-MomentumConstraintAttemptAssessed-2026-07-21.md`, this
log entry. No new script — verification reused
`wp7_derivation_momentum_constraint_attempt.py` directly, plus a
one-off symbolic reassembly check (not committed as a separate file).

**Open items handed forward:** check the $\theta$-attribution
hypothesis for the leftover $F_\mathcal Q$ piece (cheapest of the three
candidate explanations, untested); the Einstein-Hilbert sector's own
$B$-dependence (assumed reduce-to-standard-GR, not independently
verified); normalization/sign convention against $\Pi$'s own $8\pi
\tilde Ga^2\bar\rho$ factor; the $\Psi$-cancellation prediction from
Entry 8 (still to be checked once $\Pi$'s bracket is complete); the
$\lambda_s>0$ tension (Entry 3, still unresolved); author sequencing
decision on R0–R4; $Q_2$/EFE sequencing; Gate 1(b)'s caveat; Gate 4's
paused status; KATRIN watch.

---

## Entry 10 — §12's $\theta$-attribution confirmed exactly (last round's hypothesis vindicated by actual test, not assumption); §13's energy-constraint bracket match independently verified as a genuine, major result; a sign inconsistency found in the "second piece," checked, and shown not to resolve the mismatch by itself (advisor session, 2026-07-21)

**Prompt (verbatim):** "Very good progress in the last two steps.
Please assess and advice."

**Summary.** Checked WP7 for updates since Entry 9: the worker added
§12 (testing the $\theta$-attribution hypothesis from Entry 9) and §13
(a new, independent derivation of the energy constraint via $d(\text
{action})/d\Psi$) to `Update-WP7-InstabilityRecourses-2026-07-21.md`,
with two new scripts.

**§12 confirmed exactly**: `wp7_derivation_theta_attribution_check.py`
reproduces every printed line. The background identity $(1+w)\bar\rho
\times16\pi\tilde G=-\bar QF_\mathcal Q$ checked by hand from already-
established relations — a clean, standard k-essence identity, not
contrived. The remainder after subtracting the $\theta$-matched piece
also checked by direct expansion, matches exactly. **Last round's
hypothesis (that the leftover $F_\mathcal Q$ piece belongs to $\theta$'s
own equation, not $\Pi$'s bracket) is now a checked fact.**

**§13's headline result independently reproduced and confirmed
solid**: the bracket $2\kappa[\mathcal K_B\mathcal E_\alpha+(2-\mathcal
K_B)\chi]$ falls directly out of $d(\text{action})/d\Psi$, using only
the Maxwell and $\hat J$-term pieces — **zero dependence on the
$F_\mathcal Q/F_{\mathcal Q\mathcal Q}$ terms**, so this headline result
is completely unaffected by anything found below. Independently
re-derived the script's own $Q^{(2)}$ formula from the original
Y-identity machinery to confirm it wasn't assembled from a convenient
guess — matches term-for-term.

**Found a sign inconsistency, checked against the program's own
established convention**: the new script assembles $L\supset+F_
\mathcal Q Q^{(2)}+\tfrac12F_{\mathcal Q\mathcal Q}\gamma^2$ (plus
sign), but §9/§10's own already-validated scripts established the
correct sign as **minus** (matching the actual action's $-\mathcal
F(\mathcal Y,\mathcal Q)$ term). **Checked whether fixing this resolves
the open "second piece" mismatch — it does not**: neither sign makes
the remainder reduce to a clean multiple of $\gamma$; the required
ratio only works when $F_\mathcal Q=0$, which R0(a) already ruled out
for cdot-8's own trajectory. A real internal-consistency issue, but not
the resolution.

**One further hypothesis offered, not verified**: the true energy
constraint compares $\bar\rho\delta$ (not bare $\delta$), and $(1+w)
\bar\rho$ (not bare $(1+w)$) is exactly the combination already shown
to reduce cleanly to $F_\mathcal Q$-only form. Tried substituting this
through — did not immediately resolve the mismatch either, but flagged
as the most concrete lead for the next attempt.

**Files produced (Entry 10):**
`Advisory-WP7-EnergyConstraintBracketConfirmed-2026-07-21.md`, this log
entry. No new script — verification reused
`wp7_derivation_theta_attribution_check.py` and
`wp7_derivation_energy_constraint_attempt.py` directly, plus short,
one-off symbolic checks (sign-consistency test, $\bar\rho\delta$
substitution attempt) not committed as separate files.

**Open items handed forward:** fix the $F_\mathcal Q/F_{\mathcal Q
\mathcal Q}$ sign in `wp7_derivation_energy_constraint_attempt.py` for
internal consistency (doesn't resolve the mismatch alone); try the
$8\pi\tilde G\bar\rho\delta$ (not bare $\delta$) comparison next, the
most concrete lead now available; the momentum-constraint remainder
from Entry 9 (pure $\alpha/\mathcal E_\alpha$, still needs comparison
against $\Pi$'s bracket); the $\Psi$-cancellation prediction from Entry
8; the $\lambda_s>0$ tension (Entry 3, still unresolved); author
sequencing decision on R0–R4; $Q_2$/EFE sequencing; Gate 1(b)'s
caveat; Gate 4's paused status; KATRIN watch.

---

## Entry 11 — R1 resolved: not a viable recourse for the ISW-band instability, established by a fully derived (not guessed) completion, after eleven consecutive rounds of original derivation work (advisor session, 2026-07-21)

**Prompt (verbatim):** "The worker has completed the run. Please assess
and advice."

**Summary.** Checked WP7 for updates since Entry 10: the worker added
§15 (one more careful attempt at the $\gamma$-sector normalization,
per author request) and §16 (the final, derived answer to R1's
feasibility question) to `Update-WP7-InstabilityRecourses-2026-07-21.md`,
with two new scripts.

**§15 confirmed — a genuine, triply-verified negative result.** Ran
`wp7_derivation_gamma_sector_normalization_attempt.py` directly: three
independent checks (fresh bottom-up re-derivation, $\delta_2$
re-derivation, and a self-consistently-derived $c_0=-2$ normalization)
each reproduce exactly. **Independently re-derived $c_0=-2$ by hand**
from the already-confirmed bracket match and the primary source's own
$\delta$-formula, confirming it's derived, not guessed. The residual,
$F_\mathcal Q(\dot\varphi-3\dot{\bar\phi}\Psi)$, is a clean,
single-coefficient mismatch (3 vs. 1 on the $\Psi$ term) — itself
evidence this is a genuine open item, not an assembly artifact.
Endorsed stopping here after three ruled-out error sources.

**§16 confirmed — the payoff of eleven rounds, reproduces exactly.**
Ran `wp7_r1_derived_completion.py` directly: $\max\text{Re}(\lambda)$
at $z=1090$ is unchanged to 6 significant figures across the entire
tested $\lambda_s$ range, including exactly at $\lambda_s=-1$ (where
the original "uniform substitution" guess had found complete
stabilization). **Independently traced the new completion term back
through §10's own already-twice-verified result** (differentiating
$-F_\mathcal Y\dot{\bar\phi}\chi/\mathcal K_B$ w.r.t. $\alpha$ by hand)
and confirmed it matches the script's own term exactly — not just
numerically consistent, but traceably the same derived object.
Confirmed $\Pi$'s bracket and the Jacobian's trace are genuinely left
untouched by $\lambda_s$ in this script, matching §13's independently-
verified finding.

**Verdict: R1 is not a viable recourse — established, not merely
suspected.** The completion is real and structurally motivated
(confirmed via two independent constraint derivations, §10 and §13),
but modifies the wrong piece of the Jacobian: the destabilizing term
lives in $\Pi$'s trace contribution, and $\Pi$ is now confirmed
$F_\mathcal Y$-independent. The honest momentum-constraint caveat (§12's
term, not yet placed) is appropriately scoped, not glossed over — an
off-diagonal-type contribution unlikely to overturn a trace-dominance
already shown to hold by seven orders of magnitude.

**Recommending**: report this to the author as the resolution of the
commissioned derivation (target-list item 1, closed with a derived
answer); move the recourse ladder formally to R3/R4 per the original
sequencing, an author-level decision. The two durable results from this
arc regardless of R3/R4's outcome — a validated $(\chi,\alpha,\mathcal
E_\alpha)$ variable set (§9–§13) and a fully resolved R1 feasibility
question — stand on their own.

**Files produced (Entry 11):**
`Advisory-WP7-R1FeasibilityResolvedNotViable-2026-07-21.md`, this log
entry. No new script — verification reused
`wp7_derivation_gamma_sector_normalization_attempt.py` and
`wp7_r1_derived_completion.py` directly, plus a hand-derived
cross-check of the new completion term's sign/structure against §10.

**Open items handed forward:** author sequencing decision on R3
(re-closure) vs. R4 (nonlinear-saturation reframing) — the primary
open item now; the $\gamma$-sector normalization gap (§15, standing,
documented, not to be re-attempted without new information); the
momentum-constraint term's placement (§12, honest caveat on the R1
verdict, unlikely to overturn it); the $\lambda_s>0$ tension (Entry 3);
$Q_2$/EFE sequencing; Gate 1(b)'s caveat; Gate 4's paused status;
KATRIN watch.