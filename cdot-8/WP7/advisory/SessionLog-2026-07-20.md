# Session Log — WP7 Advisory, 2026-07-20

*Running log for `cdot-8/WP7/advisory/` work, appended per-prompt, per
this project's convention. Continues from `SessionLog-2026-07-19.md`.
**Provenance note for this file specifically**: these entries are an
advisor session conducted directly with the author (not routed through
the worker's own upload-and-request cycle used in prior entries), with
the author acting as intermediary because the primary advisor (Fable 5)
was unavailable on token limits. Flagged here so a future reader doesn't
mistake the channel for the worker's own.*

---

## Entry 1 — Onboarded as secondary advisor; WP0–WP7 state assessed; §28 (the F_QQ(0) domain-boundary correction) independently re-derived and confirmed outright, with the condensate-mass consequence quantified (a check §28 itself flagged but did not run) (advisor session, 2026-07-20)

**Prompt (verbatim, from the author, in two turns):**
> This project has advanced significantly since our last touch point.
> We are currently working in cdot-8, on WP7, which is proceeding well,
> but hitting a lot of roadblocks that needs advice. Your role is now
> as secondary advisor to the main worker, to step in when the worker
> requests advice and the main advisor is unavailable (due to Fable 5
> token limits). Please assess the current state of cdot-8 up to WP7
> and assess the last question (§28) from the worker.
>
> [After a conversational assessment was returned:] Yes, please do.
> [confirming the offer to formalize the assessment as a written
> advisory, per this project's own convention]

**Summary.** Read `Foundation.md`, `Progress.md`, and the WP7 update/
advisory chain through §28 to build state. Found §28
(`Update-WP7-PerturbationStructure-2026-07-18.md`) to be the pending,
un-adjudicated item: the worker's own finding that the established
$F_{QQ}(\mathcal Q_0,\text{today})=-0.696$ anchor (cited in
`Foundation.md` §7, WP5's condensate mass, and the SZ stability check)
is a domain-boundary numerical artifact, with a corrected value
$\approx-0.17$ found via an extended-integration-domain, multi-method
check — explicitly flagged for advisor confirmation before propagating
(`ErrataAndMethodologyLog-2026-07-18.md` K14).

**Verified independently rather than accepted on the worker's account**
(`wp7_fqq_correction_crosscheck.py`, conventions re-derived from
`Foundation.md` §5/§7 directly, not copied from either
`wp7_stage1_FQQ_robust.py` or `meff_skeleton.py`, per K12): (1)
reproduced the *old* method's failure directly — plain double
`np.gradient` at the literal last index of a domain ending at $s=0$
gives $-0.6962$, matching the established anchor and confirming the
edge-artifact diagnosis mechanically, not just by citation; (2)
reproduced the *correction* independently — extending the domain past
$s=0$ so it becomes an interior point, two methods (analytic quadrature
chain; centered finite difference) give $-0.1692$ and $-0.1675$; (3)
confirmed the failure is confined to the boundary — old and new methods
agree to $0.0005$–$0.055\%$ from $z=9640$ down to $z=1$; (4)
**propagated the correction into the condensate-mass estimate, which
§28 flagged qualitatively but did not itself compute**:
$1/\mu_\text{eff}$ grows from $7260$ Mpc to $\approx14700$–$14800$ Mpc,
$r_c(10^{11}M_\odot)$ from $81$ to $\approx129$–$130$ Mpc — confirming
§28's own "likely reinforcing" claim with actual numbers. Also
re-derived $F_Q,F_{QQ}$ analytically by hand from the defining
quadrature relation ($F=\mathcal Q^{2/3}G$, $dG/ds=-5\mathcal
Q^{-2/3}\Omega_s$, $d\mathcal Q/ds=-2.5\mathcal Q$) — matches the code's
formula term-for-term, so the analytic method is confirmed correct, not
merely observed to run.

**Verdict: §28 confirmed outright.** $F_{QQ}(0)\approx-0.17$ (recommend
$-0.169$, splitting the two independently-confirmed methods), same
sign as before, roughly $4\times$ smaller in magnitude. Recommended
propagating to: `Foundation.md` §7's inline flag (currently reads
"pending confirmation"); WP5's condensate-mass numbers (rescale by the
confirmed factor, rerun rather than hand-scale since $r_c$'s
mass-dependence isn't linear); §27's tachyonic sign-flip epoch
(confirmed $z\approx0.13$–$0.15$, $\mu^2/H^2(0)\approx+0.05$ — a
narrower stable margin today than §27's original "near today" language
suggested, worth keeping in view against the still-unchecked
$c_s^2(z)$ epoch-dependence). Confirmed unaffected: the SZ stability
sign; the staged growth-system round's plan (K1/K2/K3 verdicts, the
state-variable rule); the "$\Omega_s$ clusters, dust-like" structural
conclusion (rests on three other arguments, not $F_{QQ}(0)$
specifically — the tachyonic mechanism is a fourth, refined by this
correction, not undermined).

**Files produced (Entry 1):**
`Advisory-WP7-FQQCorrectionConfirmed-2026-07-20.md`,
`wp7_fqq_correction_crosscheck.py`, this log entry.

**Open items handed forward, unchanged by this advisory:** the joint
staged growth-system round (Stages 1–4, worker + advisor per stage);
the $Q_2$/EFE interpolating-function re-fit sequencing decision
(author's call, standing); Gate 1(b)'s background-level caveat
(deferred by explicit instruction until after WP7); KATRIN watch.
**New, narrow action item for the worker**: propagate the confirmed
$F_{QQ}(0)\approx-0.169$ into `Foundation.md` §7 and WP5's file — this
advisory diagnoses and confirms the number but does not itself edit
those documents.

---

## Entry 2 — §29 (worker's correction to the secondary advisor's own Check 4) accepted and owned; §30/Stage 2's units contract independently confirmed *verbatim* against the founding paper's archived source, resolving a PDF-extraction ambiguity in the advisor's favor of the worker's original quote — cleared for Stage 3 (advisor session, 2026-07-20)

**Prompt (verbatim):**
> Step 2 is now completed, plese check records.
>
> [mid-turn:] Please note that downloaded references and papers are
> stored in the references folder, with a summary.

**Summary.** Read `Update-WP7-PerturbationStructure-2026-07-18.md`
§29–§30 (both new since Entry 1). §29: the worker reproduced the prior
advisory's script and independently re-derived $F_{QQ}$, confirming the
core result solidly (three independent implementations now agree on
$\approx-0.169$) — but caught a real gap in the prior advisory's own
Check 4: it used `meff_skeleton.py`'s single-$\mathcal K_B{=}1$ formula
rather than the $\mathcal K_B$-scanning `meff_exact_dictionary.py` that
actually produced WP5's quoted condensate-mass band, so the reported
"$14700$–$14800$ Mpc, $129$–$130$ Mpc" was one point of the corrected
range, not the range itself (correct: $\mu^{-1}\approx10$–$20$ Gpc,
$r_c\approx100$–$160$ Mpc). §30: the units contract for Stage 3, four
lines, most importantly Contract Line 2 — the founding paper's
$\mathcal E_\alpha$ equation coefficient is $d\mathcal K/d\mathcal
Q=-\tfrac12\mathcal F_Q(\text{background})$, not the bulk-current
$\mathcal F_Q$ both §25 and §26 used there, a genuine, previously-
unexamined error in both prior failed attempts.

**§29 accepted and owned without dispute** — the worker's correction is
right; the gap (not knowing which script produced a specific quoted
number) is exactly the kind of session-history detail a secondary
advisor without the full record will sometimes miss, not a physics
error, and is recorded as such rather than argued with.

**§30 verified independently, going further than the worker's own
internal self-consistency check**: attempted to fetch the founding
paper (arXiv:2007.00082) via `WebFetch`, first from the abstract page
(no useful content), then the PDF (extracted via `pdftotext`, which
recovered $\mathcal K(\bar Q)=-\tfrac12\mathcal F(0,\bar Q)$ and the
$8\pi/16\pi$ prefactors cleanly but **lost the parenthesization** of
the $\mathcal E_\alpha$ equation, leaving $\mathcal K_B\dot{\mathcal
E}+H\mathcal E$ vs. $\mathcal K_B(\dot{\mathcal E}+H\mathcal E)$
genuinely ambiguous from that extraction alone). **Per the author's
mid-turn note**, found the paper already archived at
`references/arXiv.2007.00082/newRMONDLett.tex` with its own summary —
re-checked against the clean LaTeX source directly, which resolved the
ambiguity in the worker's favor (confirming §25's original quote,
parentheses included) and confirmed all four of §30's claims verbatim:
$\mathcal K\equiv-\tfrac12\mathcal F(0,\bar{\mathcal Q})$ (line 355,
word for word); the $8\pi\tilde G$-vs-$16\pi\tilde G$ toy/full action
prefactors; $\mathcal K_2\equiv$ the coefficient of $(\bar{\mathcal
Q}-\mathcal Q_0)^2$ in $\mathcal K$'s own expansion, giving $\mathcal
K_2=-\tfrac14\mathcal F_{QQ}$ from the definition directly, not only
from WP5's downstream use of it; and the $\mathcal E_\alpha$ equation's
coefficient written literally as $d\mathcal K/d\mathcal Q$, confirming
Contract Line 2 by direct textual match rather than internal
consistency alone.

**Verdict: both accepted; Stage 2 cleared for Stage 3.** Added a
provenance note to `references/arXiv.2007.00082.md` recording the four
verified equations and this session's specific use of them, and a
note-to-self that `references/` should be checked for an already-
archived source before fetching a fresh copy of a paper already in this
program's citation list.

**Files produced (Entry 2):**
`Advisory-WP7-Stage2UnitsContractConfirmed-2026-07-20.md`, this log
entry. **Updated**: `references/arXiv.2007.00082.md` (provenance note).
No new script — both checks were direct textual verification against
the archived primary source.

**Open items handed forward, unchanged by this advisory:** Stage 3 (the
pure field-variable rebuild, worker's next action, using $d\mathcal
K/d\mathcal Q=-\tfrac12\mathcal F_Q$ in the $\mathcal E_\alpha$
equation specifically and bare $\mathcal F_Q$ only in the bulk-current
term); the $Q_2$/EFE sequencing decision (author's call, standing);
Gate 1(b)'s background-level caveat; KATRIN watch. **Correction
recorded, no further action needed**: the secondary advisor's own
condensate-mass numbers in `Advisory-WP7-FQQCorrectionConfirmed-2026-07-20.md`
are superseded by the worker's $\mu^{-1}\approx10$–$20$ Gpc,
$r_c\approx100$–$160$ Mpc — not re-edited, per this project's practice
of recording corrections forward.

---

## Entry 3 — Stage 3's fast-onset blowup diagnosed: a genuine, large, real eigenvalue in the never-audited vector sector, switched on entirely by the $\Pi$-feedback term above a tiny critical $k$; the $\Pi$-formula's own Fourier/$a^2$-normalization left as an open, unresolved question (advisor session, 2026-07-20)

**Prompt (verbatim):**
> Please examine the fast-onset blowup produced in Step 3 and advice.

**Summary.** Read §32 (Stage 3): a careful, correctly-closed
implementation ($\chi=\bar Q(\theta_s+\alpha)$ resolving the "$\chi$ or
$\gamma$" ambiguity; $\Pi$ via the full formula, not the
$c_\text{ad}^2\delta_s$-only shortcut that broke §26) reproduces and
*improves on* §24's own dust-sector regression target ($\Phi/\Phi_i=
0.50$ by $z=0$, decaying smoothly, versus §24's pathological $2.4\times$
growth) — but the full system, with $\Pi$ included, blows up fast:
$10^{10}$–$10^{18}$ within one integration step past $z=100$, unfixed
by a $10\times$ smaller $k$. Correctly localized by the worker to the
vector sector, which Stage 0's audit never touched (it only checked the
scalar condensate's $\mu_\text{eff}^2\propto\mathcal F_{QQ}$).

**Diagnosed directly** (`wp7_stage3_vector_stiffness_audit.py`, reusing
`wp7_stage3_field_variable.py`'s own trajectory and the Stage-2-confirmed
$d\mathcal K/d\mathcal Q=-\tfrac12\mathcal F_Q$ coefficient): built the
local $2\times2$ Jacobian of $(\alpha,\mathcal E_\alpha)$ alone,
freezing $\delta_s,\theta_s,\Phi$ as external sources. **Confirmed a
genuine large positive real eigenvalue** ($+485$ at $z=100$,
$k=10^{-4}\,\text{Mpc}^{-1}$ — exactly reproducing the coded blowup),
decreasing through $z=90,70,50$ ($+347,+159,+59$) and becoming a
stable, damped complex pair by $z=10$. **Isolated the cause**: setting
$\kappa=0$ gives a stable complex pair at every epoch checked — the
instability is switched on entirely by the $\Pi$-feedback term, with a
clean bifurcation at a tiny critical $\kappa$ whose corresponding
comoving $k_\text{crit}$ ranges from $\approx3.6\times10^{-7}$
($z=1090$) to $\approx3\times10^{-4}\,\text{Mpc}^{-1}$ ($z=10$) —
**essentially every cosmologically relevant $k$ is on the unstable
side once $z$ is a few tens or more**, not a narrow sub-horizon corner
case. Cross-checked the dominant term by hand
($\propto-(2-\mathcal K_B)^2c_\text{ad}^2\kappa\bar{\mathcal
Q}^2/[\mathcal K_BH_c(1+w)]$, quadratic in the already-legitimately-large
background $\bar{\mathcal Q}$): matches the coded Jacobian to within
rounding.

**One thing not settled**: tried two candidate Fourier/$a$-normalization
conventions for the $\Pi$-formula's own $\nabla^2\to
-k^2$-vs-$-k^2/a^2$ substitution by hand; they disagree with each other
by a factor of $a^2$ and neither tames the instability (one gives an
$O(1)$ correction, the other makes it $\sim1000\times$ *worse* at high
$z$). This is the one sub-term Stage 2's units contract didn't
separately itemize. Recommended as an explicit fifth dictionary line,
to be resolved before deciding whether the instability is a genuine
physical feature (requiring a quasi-static/slaved treatment of
$(\alpha,\mathcal E_\alpha)$ for $\kappa$ above threshold, the same
class of move standard Boltzmann codes make for stiff sectors) or
partly a normalization artifact.

**Files produced (Entry 3):**
`Advisory-WP7-Stage3VectorInstabilityDiagnosed-2026-07-20.md`,
`wp7_stage3_vector_stiffness_audit.py`, this log entry.

**Open items handed forward:** the $\Pi$-formula normalization check
(new, narrow, gates everything downstream — proposed as "Stage 3b");
pending that, either a quasi-static/slaved vector-sector treatment or a
revised Stage 3 attempt; the $Q_2$/EFE sequencing decision (author's
call, standing); Gate 1(b)'s background-level caveat; KATRIN watch.

---

## Entry 4 — Stage 3b confirmed: the comoving-Laplacian reading is right (now independently supported, not just self-consistent), the missing $1/(3\Omega_s)$ factor is a real bug regardless, and the vector-sector instability survives correction — treat as real physics, proceed to a quasi-static closure (advisor session, 2026-07-20)

**Prompt (verbatim):**
> Please assess the progress on 3b and advice.

**Summary.** Read §33 (the worker's independent reproduction of Entry
3's audit, term-by-term against the actual `rhs()` — accepted in full,
plus a genuine additional find: the paper's $\delta$-defining relation
uses the *identical* bracket and $1/(8\pi\tilde Ga^2\bar\rho)$ prefactor
as $\Pi$, so whatever Laplacian convention is adopted must satisfy both
equations at once) and §34 (Stage 3b itself): re-derived the
$\Pi$-formula's convention from the primary source's own internal
structure — an explicit $a^2$ already multiplying $\bar\rho$ in the
prefactor would double-count if $\nabla^2$ also meant the
physical/$1/a^2$-including Laplacian, so the natural reading is
$\nabla^2\to-k^2$ (bare comoving $k$), giving $\Pi\supset
c_\text{ad}^2\kappa/(3\Omega_s(a))\cdot[\text{bracket}]$ — matching this
program's own already-validated Poisson-equation convention exactly.
**This also surfaced a second, separate bug**: the coded $\Pi$ term has
no $\Omega_s(a)$ division at all. Tested all three readings (coded
bare-$\kappa$; derived comoving $\kappa/(3\Omega_s)$; the advisor's
earlier alternate physical $\kappa/(3a^2\Omega_s)$) through the vector
Jacobian: **the growing real eigenvalue survives all three** (comoving
roughly halves it, e.g. $485\to221$ at $z=100$; physical makes it far
worse). Concluded, with explicit humility: likely real physics, not a
units artifact — flagged for advisor cross-check before committing to
a redesign.

**Independently reproduced, not accepted on the worker's account**: ran
`wp7_stage3b_pi_normalization_check.py` directly (it dynamically
imports the secondary advisor's own `wp7_stage3_vector_stiffness_audit.py`
by path rather than duplicating it — confirmed this also re-exercises
Entry 3's audit correctly). Every number in the worker's table
reproduced exactly across all nine redshifts and three readings,
including the $z=1090$ physical-reading outlier ($+5.4\times10^{11}$).

**Added an independent argument the worker didn't have**: the
comoving-Laplacian reading isn't just internally self-consistent for
this one equation — it is the *standard* convention in the
cosmological-perturbation literature generally (e.g. Ma & Bertschinger
1995's own Poisson equation, bare comoving $k^2$ with explicit $a^2$ in
the source term, adopted specifically so $k$ stays an unambiguous,
redshift-independent label throughout a calculation). This also
retroactively explains why this program's own Poisson equation worked
correctly without the ambiguity ever surfacing before — it was built on
the standard convention from the start; Stage 3 is the first place an
imported equation forced the choice to be made explicit.

**Verdict: confirmed on all counts.** The $1/(3\Omega_s(a))$ fix is
right regardless and should go into the next implementation. The
instability's survival under an $O(2\times)$ correction (rather than
disappearing or staying bit-for-bit identical) is exactly the pattern
expected from a genuine physical effect being corrected by a modest,
separate normalization fix — supports "real physics" without proving
it. Endorsed proceeding to a quasi-static/slaved closure for $(\alpha,
\mathcal E_\alpha)$ above $\kappa_\text{crit}(z)$. Offered one optional,
not-blocking strengthening check: whether AeST's own native $K(Q)$
examples (Cosh/Exp/Higgs-like, whose $C_\ell^{TT}$/$P(k)$ are shown
matching Planck in the source paper) show the same instability when
run through this Jacobian — would settle whether this is a universal
feature of the imported equations or specific to cdot-8's own forced,
negative $c_\text{ad}^2$. Not attempted (would need reconstructing the
paper's own unit conventions for those parameter sets); flagged as
valuable future work, not a blocker.

**Files produced (Entry 4):**
`Advisory-WP7-Stage3bConfirmed-2026-07-20.md`, this log entry. No new
script — verification was direct re-execution of the worker's own
`wp7_stage3b_pi_normalization_check.py`.

**Open items handed forward:** fix the coded $\Pi$ term's
$1/(3\Omega_s(a))$ factor (uncontroversial, next implementation);
design the quasi-static/slaved $(\alpha,\mathcal E_\alpha)$ closure for
$\kappa>\kappa_\text{crit}(z)$ (worker's next action); optional
AeST-native cross-check (not yet attempted, no urgency assigned); the
$Q_2$/EFE sequencing decision; Gate 1(b)'s background-level caveat;
KATRIN watch.

---

## Entry 5 — Stage 3c's transition-zone pole located precisely: it is the full system's true stability boundary ($\text{Re}(\lambda_\text{max})=0$, at $z\approx18$–$20$), not the real$\leftrightarrow$complex split the worker named ($z\approx29$–$30$, still unstable on both sides) — recommended a hard, criterion-based switch there rather than a smoothed blend (advisor session, 2026-07-20)

**Prompt (verbatim):**
> Good progress from the worker now. Requested review of transition-zone
> design before continuing.

**Summary.** Read §35 (Stage 3b advisory accepted without dispute) and
§36 (Stage 3c): the worker implemented both recommended fixes (the
$1/(3\Omega_s(a))$ correction; algebraic elimination of $\mathcal
E_\alpha$ via $\dot{\mathcal E}_\alpha=0$, leaving $\alpha$ as the only
vector-sector ODE state), found the elimination denominator
$\text{coef}_E\equiv-\mathcal K_BH_c\,\partial\dot{\mathcal
E}_\alpha/\partial\mathcal E_\alpha$ has a genuine pole crossing zero
between $z=30$ and $z=10$, correctly recognized this as a structural
feature (not a numerical artifact) tied to the earlier stiffness
audit's own eigenvalue bifurcation, and checkpointed to request
transition-zone design review before implementing a switch.

**Verified independently, and found one precise correction worth
making before designing anything**: reconstructed the full
$\text{tr}(J),\det(J)$, and eigenvalue table along the trajectory
(reusing the audit script directly, Stage-3b normalization
substituted). The worker's own algebraic identity for $\text{coef}_E$
checked out by hand, term for term. But **the pole is not where the
eigenvalue pair goes from real to complex** ($z\approx29$–$30$, found
by bracketing the discriminant precisely) — the system is *still
unstable* on both sides of that point (complex pair with *positive*
real part from $z\approx20$ to $29$, e.g. $+1.27\pm2.65i$ at $z=28$).
**The pole is at the later, lower-$z$ point where
$\text{Re}(\lambda_\text{max})$ itself crosses zero** ($z\approx18$–
$20$) — the true Lyapunov stability boundary. Explained *why* these
coincide exactly rather than approximately: $J_{11}=0$ identically in
this system, so $\text{tr}(J)=J_{22}\propto\text{coef}_E$, and for any
such matrix $\text{tr}=0$ is exactly $\text{Re}(\lambda)=0$ whether the
pair is real or complex — the pole isn't a numerical artifact of the
elimination, it's the algebra correctly reporting where the timescale
separation the whole method needs genuinely vanishes.

**Design recommendation given**: a **hard, criterion-based switch** at
$\text{tr}(J)=0$ (not a smoothed blend across the wrongly-identified
$z\approx29$–$30$ boundary, which sits inside a region that isn't
dynamically uniform — real pair above it, growing spiral below it,
both unstable). Below the true boundary, integrate $(\alpha,\mathcal
E_\alpha)$ explicitly (fully justified there, untested but follows
directly); above it, keep the corrected slaving. Cited the precedent:
real Boltzmann codes switch the analogous photon–baryon tight-coupling
approximation at an explicit criterion with a safety margin, rather
than blending it continuously into the full equations — recommended
the same pattern here, plus the standard robustness check (confirm
insensitivity to the exact switch redshift within a margin).

**Files produced (Entry 5):**
`Advisory-WP7-Stage3cTransitionZoneReview-2026-07-20.md`, this log
entry. No new standalone script — the stability table extended the
existing audit script's own `jacobian()` function over a finer $z$-grid.

**Open items handed forward:** implement the hard switch at
$\text{tr}(J)=0$ (worker's next action); the untested regression
(explicit integration just below the true boundary staying bounded and
matching the slaved solution just above it); the switch-margin
sensitivity check; fix the $1/(3\Omega_s(a))$ factor if not already
done; optional AeST-native cross-check; $Q_2$/EFE sequencing; Gate
1(b)'s caveat; KATRIN watch.

---

## Entry 6 — Stage 3d's boundary-condition problem endorsed as correctly diagnosed, plus a compounding second issue found: the quasi-static approximation is already only marginal by $z\approx25$–$30$, a full ten-plus e-folds above the switch — recommended a Riccati/stable-subspace continuation seeded deep in the good regime, not a better guess at $z=100$ (advisor session, 2026-07-20)

**Prompt (verbatim):**
> Please have a look at the boundary-condition selection problem that
> the worker found.

**Summary.** Read §37: the worker built the hybrid closure exactly to
the prior advisory's spec (switch at $\text{tr}(J)=0$, confirmed at
$z=18.543$, matching the advisor's bracket) but found the result
wildly sensitive to the safety margin ($\delta_b(z{=}0)$ from $+0.14$
to $-1.8\times10^7$ across margins $0.2$ to $0.02$ e-folds). Correctly
traced this to the very first step: the inherited $z=100$ initial
condition ($\mathcal E_\alpha=0$) mismatches the algebraic slaved value
($\approx-76$, since $\chi\approx21.7$ from the large background
$\bar{\mathcal Q}\approx2190$) — and because the eliminated mode
*grows* rather than decays, this mismatch is not forgotten, it
amplifies. Correctly identified this as a **boundary-condition
selection problem, not a relaxation** — the same structural class as
WP3's own past-regularity/$C_1$ selection — and routed it for review
before attempting a fix.

**Reproduced exactly**: ran `wp7_stage3d_hybrid_closure.py` directly;
$z_\text{switch}=18.543$ and the full margin-sensitivity table both
matched. **Diagnosis endorsed as correct and well-reasoned** — standard
tight-coupling elimination relies on the eliminated variable's own
dynamics being stably damped (mismatches decay, so initial data doesn't
matter); here $\partial\dot{\mathcal E}_\alpha/\partial\mathcal
E_\alpha>0$ throughout the quasi-static phase, inverting that logic —
the algebraic relation is a selection criterion (zero overlap with the
growing eigendirection), not an attractor.

**Added a second, compounding finding**: computed $\lambda_\text{max}$
in its natural units for this specific check — per e-fold, since $N$
is the ODE's own time variable, so the adiabatic-elimination
requirement is $|\lambda_\text{max}|\gg1$ **per e-fold**, not per
Hubble time. Result: genuinely large ($\gg1$) only for
$z\gtrsim50$–$60$ ($\lambda\sim30$–$220$), already only order unity by
$z\approx25$–$30$ ($\lambda\sim0.3$–$3.4$) — a full ten-plus e-folds
in redshift above $z_\text{switch}=18.5$. **This means fixing only the
$z=100$ initial condition cannot be the whole fix**: the algebraic
relation itself drifts away from a trustworthy leading-order
approximation well before reaching the switch, independent of whatever
mismatch is carried forward from the start.

**Recommended**: a stable-subspace (Riccati-type) continuation —
express $\mathcal E_\alpha$ as a function of the slow variables that
evolves via its *own* consistency equation (derived by requiring
invariance under the true coupled dynamics), seeded deep in the
well-separated regime ($z\gtrsim60$, where the naive algebraic answer
is known-good, removing the initial-condition guesswork) and continued
through the marginal zone to the switch — rather than re-deriving the
same potentially-singular algebraic relation at every step. Flagged
explicitly as a real derivation needing the same care as everything
else, not a drop-in fix.

**One thing flagged but not confirmed**: an exploratory finite-difference
Jacobian of the full 6-variable system hinted at a possible *second*
unstable direction (tentatively gravitational/Jeans-like, from the
$\delta_b,\theta_b,\Phi$ coupling), distinct from the audited
$(\alpha,\mathcal E_\alpha)$ pair — but the finite-difference
construction isn't precise enough given the system's huge coefficient
range to trust as a stated result. Recommended a careful
(symbolic or properly-scaled) check of how many independent growing
directions the full system has before assuming one shooting/projection
parameter suffices.

**Files produced (Entry 6):**
`Advisory-WP7-Stage3dBoundaryConditionProblem-2026-07-20.md`, this log
entry. No new standalone script.

**Open items handed forward:** design and verify the Riccati/stable-
subspace continuation (new, the concrete next step); check the number
of independent unstable directions in the full 6-variable system (new,
flagged not confirmed); the $1/(3\Omega_s(a))$ fix and switch criterion
both stand as before; optional AeST-native cross-check; $Q_2$/EFE
sequencing; Gate 1(b)'s caveat; KATRIN watch.

---

## Entry 7 — §38's complex-Riccati gap resolved without needing a complex-Riccati: in the spiral zone every real direction shares one growth envelope, so hand off once (at $z\approx29$–$30$, not $z_\text{switch}=18.5$) and integrate explicitly the rest of the way (advisor session, 2026-07-20)

**Prompt (verbatim):**
> One more checkpoint.

**Summary.** Read §38: the worker derived the Riccati equation for
$\mu\equiv d\mathcal E_\alpha/d\alpha$ exactly as recommended, then
found — before implementing anything — that its fixed-point quadratic
(the frozen-coefficient/naive slaving limit) has a discriminant
proportional to the *original* $(\alpha,\mathcal E_\alpha)$ Jacobian's
own discriminant, vanishing at the **same** $z\approx29$–$30$ point
already found in Entry 5 — a full ten-plus e-folds above
$z_\text{switch}=18.5$. Correctly concluded the real Riccati slope
cannot be continued through the intervening spiral (complex-eigenvalue)
zone as a real-valued object at all, and routed the question of how to
generalize before attempting a complex/matrix version un-reviewed.

**Independently re-derived both claims from scratch, not just accepted
them**: rebuilt the Riccati equation from the substitution $\mathcal
E_\alpha=\mu\alpha+\nu$ into both defining equations — matches the
worker's exactly. Checked the discriminant claim algebraically:
$D_\mu=H_c^2D_J$ exactly (not approximately), confirmed both
symbolically and numerically ($D_J=+1.246\to D_\mu=+11751$ at
$z=29.5$; $D_J=-9.155\to D_\mu=-82213$ at $z=29.0$; ratio $=H_c^2$ to 5
figures each time). Since $H_c^2>0$ always, the two discriminants share
a sign and a zero identically — the worker's find is real and
precisely located, not a coincidence of rounding.

**Found this doesn't need a complex/matrix generalization to resolve**:
a real $2\times2$ system with complex eigenvalues has no preferred real
eigendirection — every real initial vector grows with the *same*
envelope $e^{\text{Re}(\lambda)N}$, differing only in oscillation
phase. The Riccati slope's job (select the one non-growing direction)
has nothing to act on once eigenvalues merge and go complex, because
there is no non-growing direction left to select in that zone — not a
gap in the method, a genuine absence of the object the method needs.
**Recommended a simpler fix than a generalization**: track the real
Riccati only as far as it stays real ($z\gtrsim29$–$30$, seeded deep at
$z\gtrsim60$ where the naive slaving is already accurate), hand off
*once* at that point to full explicit integration of $(\alpha,\mathcal
E_\alpha)$, and carry that single explicit phase all the way to $z=0$
— covering both the spiral-unstable zone and the later genuinely
stable zone continuously, with no special handling needed at
$z_\text{switch}=18.5$ at all. Explained why this fixes the
margin-sensitivity rather than relocating it: the previous failure came
from mismatching a *strongly growing* real mode over many e-folds
before even reaching the spiral zone; handing off correctly at
$z\approx30$ means entering the spiral with the properly-selected
small residual, after which growth is the same universal envelope
factor regardless of the residual's direction — fixed and computable,
not arbitrarily sensitive. Recommended the robustness check be redone
on the right parameter (vary the handoff redshift within the region
where $\mu$ is genuinely real, e.g. $z=35,32,30.5,29.8$, not the old
margin around $z_\text{switch}$).

**Files produced (Entry 7):**
`Advisory-WP7-Stage3eRiccatiSpiralResolution-2026-07-20.md`, this log
entry. No new standalone script — verification reused the existing
audit script's Jacobian directly.

**Open items handed forward:** implement the two-phase (Riccati then
single explicit integration) design and the corrected handoff-point
robustness check (worker's next action); the possible second unstable
direction in the full 6-variable system, still flagged, still not
confirmed; optional AeST-native cross-check; $Q_2$/EFE sequencing; Gate
1(b)'s caveat; KATRIN watch.
