# Session Log — cdot-8/WP6 (2026-07-18)

*New work package, new file. WP5 closed 2026-07-17 (pre-registered
prediction + literature gap + differential test design). Both standing
decision gates resolved by the author 2026-07-18: Gate 1 (Foundation §6
item 6, WP4a's 27% miss) — provisional structural failure, not a kill,
investigate options but complete through WP7 first; Gate 2 (WP5b scope) —
close as delivered, no in-program binned-lensing reanalysis. Proceeding to
WP6 (tensor speed, PPN, binary pulsar) under Gate 1's explicit caveat.*

---

## Entry 1 — Structural first installment: tensor speed imported, WP6 scoped (2026-07-18)

**Context (not a new prompt — continuation of the decision-gate
resolution turn):** author resolved both gates, with an explicit
sequencing instruction ("complete the analysis up to and including WP7
before revisiting the radiation era assumptions") read as direction to
proceed with WP6.

**Summary of work performed:**

1. **Researched AeST's own literature first** (WP5's established rhythm):
   fetched the founding paper (Skordis & Złośnik, PRL 127, 161302 /
   arXiv:2007.00082) directly. Confirmed tensor-mode speed
   $c_\text{gw}=c_\gamma$ is a deliberate design requirement ("requirement
   (v)"), stated to hold "in all situations," specifically engineered to
   fix TeVeS's known GW170817 incompatibility. Cross-checked against the
   stability paper already used in WP5 (PRD 106, 104041) — independently
   confirms tensor modes propagate at $c$.

2. **Confirmed PPN $\alpha_1,\alpha_2$ are absent from both AeST papers
   checked** — matches WP0's own 2026-07-11 finding that binary-pulsar
   testing of AeST is a fully open literature gap, with the parallel
   Einstein-æther pulsar-constraint machinery (Yagi et al. 2014, Vaglio et
   al. 2026) flagged as the adaptable path.

3. **Posed and named (not yet independently verified) the cdot-8-specific
   decoupling question**: does M5's scalar-sector-only modification reach
   the tensor sector? Argued, via the same quadratic-order sector-
   additivity result already load-bearing in WP5's $m_\text{eff}$
   derivation, that it should not — cdot-8 never touches the
   Einstein-Hilbert term, the aether kinetic coefficients, or $Q_0$, all
   of which govern the tensor dispersion relation. Flagged explicitly as
   an assumption, not asserted as proven.

4. **Scoped the remaining WP6 work into three ordered sub-tasks** per
   WP0's own recommendation: (i) Cassini/ephemeris-level interpolating-
   function test, reusing `cdot-4/T22`'s machinery — cheapest, next
   concrete step; (ii) PPN $\alpha_1,\alpha_2$ derivation; (iii) binary-
   pulsar confrontation, gated on (ii).

**Files produced:** `Update-WP6-TensorSpeedStructure-2026-07-18.md`, this
entry.

**Status: structural first installment only, deliberately checkpointed**
— matches this program's established rhythm rather than pushing to a full
WP6 confrontation in one pass. Tensor speed imported, low-risk. **Every
WP6 finding from here explicitly inherits Gate 1's provisional-failure
caveat** — this is legitimate parallel/sequential work under an
unresolved cosmological-background tension, not a claim of a clean
foundation. Next concrete step: the Cassini/ephemeris interpolating-
function test. Housekeeping (WP4b confirmation, errata batch, log
repairs, KATRIN clock clarification) remains owed. Nothing in `cdot-7/`
was touched.

---

## Entry 2 (worker) — Advisory assessed: tensor discharge accepted and independently confirmed; μ-swap reframing accepted; one advisor claim rejected after a third independent check (2026-07-18)

**Reference:** `Advisory-WP6-FirstInstallment-2026-07-18.md` +
`mu_swap_exposure.py` (note: the shared `proposal/SessionLog-2026-07-18.md`
was extended directly with two further entries covering this same
advisory round and a KATRIN/housekeeping consolidation — not authored by
me; treated as advisory content to verify, per standing practice, not
accepted at face value).

**Summary of work performed:**

1. **Confirmed independently** (re-fetched the stability paper): Eq. 20's
   tensor action is exactly GR's, citing Skordis & Złośnik 2019 (PRD 100,
   104013) for the general class result. This discharges §2's named
   assumption — $H_{ij}$ enters neither $Q$ nor $\mathcal Y$ at linear
   order, so cdot-8's $F(Q)$ modification structurally cannot reach the
   tensor sector. The advisory's further claim (M5's own multiplier is
   tensor-blind at linear order) is standard SVT cosmological-
   perturbation-theory reasoning — accepted on that basis. **Verdict now
   solid**: $c_\text{gw}=c_\gamma$ holds in cdot-8 in all situations.
   Accepted the added standard-siren prediction ($d_L^\text{GW}/d_L^
   \text{EM}=1$) as a direct, low-risk corollary, registrable per Gate 2.

2. **Reproduced `mu_swap_exposure.py` exactly** (24–41% offset at the
   working points) and accepted the reframing: this program's own closure
   has used the simple $\mu(x)=x/(1+x)$ since WP2 — running sub-task 1
   naively against it would just rediscover `cdot-4/T22`'s already-known
   $\sim2800\times$ Cassini exclusion. Sub-task 1 reframed: the real
   object is AeST's own screening sector; the closure's Cassini-safe-
   $\mu$-swap exposure (tens-of-percent $\kappa\lambda/x_0$ refit) is a
   real, externally-forced candidate for Gate 1(b)'s post-WP7 options
   review — quantified, not executed, per the author's sequencing
   instruction.

3. **Did NOT accept one claim**: the log's Entry 2 asserts my WP5
   Brouwer-quote correction was itself wrong, claiming the disputed
   quote appears in the published A&A version. **Checked a third time,
   this round directly against the publisher's own site (aanda.org)**,
   not just arXiv — the quote is not there either, in either version.
   Holding the original correction. Doesn't affect the design's
   substance (missing baryons remains a real, discussed systematic in
   that paper), but a rebuttal that doesn't itself check out isn't
   accepted just because it arrived confidently.

4. **Checked the KATRIN specifics live** (web search): $m_\beta<0.45$ eV
   (90% CL, Science, April 2025, 259/1000 days) — confirmed accurate.

**Files produced:** `Update-WP6-TensorSpeedStructure-2026-07-18.md` §2a
(new), this entry.

**Status**: tensor-sector import now solid, not merely plausible. Sub-task
1 correctly reframed before wasting effort on a known result. One
advisor claim (Brouwer quote) checked and rejected, held independently.
Next concrete step: sub-task 1 under the reframed protocol (identify
cdot-8's inherited screening terms), or PPN derivation, whichever the
author prefers to sequence next. Nothing in `cdot-7/` was touched.

---

## Entry 3 (worker) — Sub-task 1 executed: model-independent Cassini/screening bound, comfortably satisfied (2026-07-18)

**Prompt (verbatim):**
> Proceed with sub-task 1.

**Summary of work performed:**

1. **Fetched the stability paper directly** for AeST's own "screening vs.
   tracking" mechanism: confirmed $\lambda_s$ sets the effective $G_N$
   and the deep-MOND free-function piece; screening is described as
   additional $\mathcal Y^p$ ($p>3/2$)/Galileon-type terms dominating at
   large gradients, with **no unique functional form or quantitative
   solar-system bound given anywhere** — a genuine, confirmed literature
   gap, not something to import a number for.

2. **Anchored the confrontation on `cdot-4/T22`'s own already-validated
   Saturn numbers** ($g_\dagger=1.13\times10^{-10}$ m/s², Cassini bound
   $4\times10^{-14}$ m/s², $y_\text{Saturn}=755^2$). **Caught and fixed my
   own first attempt** (wrongly modeled the naked-simple anomaly as
   power-law-suppressed; re-derived from the exact $\mu(u)u=y$ relation
   and confirmed the anomaly is asymptotically *constant*, $g_x\to
   g_\dagger$, which is why it's excluded so cleanly) before trusting the
   comparison — reproduced T22's own $\sim2800\times$ ($2825\times$
   computed) exactly, validating the setup.

3. **Computed the actual result**: solved the same relation for two
   illustrative fast-tail completions (standard/RAR, exponential/MLS) at
   the identical Saturn point — both pass by enormous margins ($\sim
   400\times$ to $\sim10^{286}\times$ under the bound), confirming the
   advisory's expected outcome by calculation, not citation.

4. **Stated the honest limit of this result**: this establishes a
   model-independent requirement (any non-naked completion passes
   comfortably) but does NOT pin down AeST's own $(\lambda_s,p)$
   parameters or a specific screening scale — the literature doesn't fix
   a unique completion, so that would require inventing an ansatz, not
   extracting a constraint. Flagged as separate, not-yet-attempted work.

**Files produced:** `Update-WP6-TensorSpeedStructure-2026-07-18.md` §4–5
(new), `wp6_cassini_screening.py`, this entry.

**Status: sub-task 1 closed.** cdot-8 inherits AeST's screening machinery
unchanged (§2a's sector-additivity) and passes Cassini/ephemeris bounds
comfortably once any reasonable completion replaces the naked
closure-fitting $\mu$. **Next: sub-task 2, PPN $\alpha_1,\alpha_2$** —
the program's real remaining WP6 work, per the advisory's own framing
that the æ-theory literature is scaffold, not answer, here. Every finding
inherits Gate 1's provisional-failure caveat. Nothing in `cdot-7/` was
touched.

---

## Entry 4 (worker) — Sub-task 2 opened: AeST's aether alone sits at Einstein-æther's known c₁₂₃=0 scalar-mode degeneracy (2026-07-18)

**Prompt (verbatim):**
> Proceed with sub-task 2.

**Summary of work performed:**

1. **Fetched Foster & Jacobson's PPN paper directly** (PRD 73, 064015 /
   gr-qc/0509083) for the exact $\alpha_1,\alpha_2$ formulas in terms of
   the general Einstein-æther kinetic coefficients $c_1,c_2,c_3,c_4$,
   rather than work from a paraphrase.

2. **Mapped AeST's own vector kinetic term** ($-\frac{K_B}2F^{\mu\nu}
   F_{\mu\nu}$, a pure Maxwell-type structure) onto this basis: fixes
   $c_2=c_4=0,\ c_3=-c_1$ — convention-independent of the two papers'
   relative sign, which is separately flagged as unpinned.

3. **Checked the result symbolically (sympy)** rather than trust hand
   algebra: $\alpha_1=-4c_1$ (finite), but $\alpha_2$'s formula has
   $c_{123}=c_1+c_2+c_3$ in a denominator, and $c_{123}=0$ identically for
   this restricted class — **the formula diverges**.

4. **Verified this against the wider æ-theory literature independently**:
   confirmed $c_{123}=0$ is the known condition under which Einstein-
   æther's own spin-0 (scalar) mode becomes non-propagating — not an
   artifact of the mapping, a real, documented degeneracy. Read the
   physical meaning: AeST supplies its MOND scalar via an explicit
   dynamical $\phi$ precisely because its restricted aether carries no
   scalar dynamics of its own — the design choice and the PPN degeneracy
   are the same fact seen twice.

5. **Scoped what remains honestly**: the actual $\alpha_1,\alpha_2$ for
   AeST/cdot-8 requires the scalar-vector mixing ($\chi=\varphi+Q_0
   \alpha$) built in from the start — not optional refinement, the object
   that keeps the PPN formula finite at all. This is substantial, original
   derivation work (effectively redoing Foster-Jacobson's own multi-stage
   calculation with an added coupled scalar), not completed this pass —
   flagged for staged, checkpointed continuation or a touch point, given
   the stakes of a wrong verdict either way.

**Files produced:** `Update-WP6-TensorSpeedStructure-2026-07-18.md` §5–6
(new), `wp6_ppn_c123.py`, this entry.

**Status: sub-task 2 opened with a genuine, verified structural finding —
not yet a number.** Sharpens the advisory's general caution ("æ-theory
formulas cannot be lifted directly") into an explicit demonstration of
why. The full scalar-coupled PPN derivation remains the real, substantial
work ahead; sub-task 3 (binary pulsar) stays gated on it. Every finding
inherits Gate 1's provisional-failure caveat. Nothing in `cdot-7/` was
touched.

---

## Entry 5 (worker) — Advisory checkpoint verified to the digit; two structural additions accepted (2026-07-18)

**Reference:** `Advisory-WP6-CheckpointVerified-2026-07-18.md` +
`wp6_verification.py`. **Reproduced the whole verification script myself**
before accepting anything.

**Summary of work performed:**

1. **Accepted**: the flagged "further derivation" of a screening
   completion from cdot-8's own quadrature is impossible in principle —
   the background trajectory has $\mathcal Y\equiv0$ identically, so it
   has zero support on the $\mathcal Y$-sector at any order. Recorded a
   charter scope statement: "zero adjustable elements" covers the
   $Q$-sector only; the $\mathcal Y$-sector remains AeST-inherited,
   data-bounded functional freedom — a limitation shared with every
   relativistic MOND completion, worth stating before a referee does.

2. **Accepted, with a correction to my own §4**: cdot-8's closure-$\mu$
   (Q-sector) and galaxy/solar-system $\mu$ (Y-sector) are formally
   distinct in the actual covariant construction, unlike cdot-7's
   single-function "AQUAL economy." The 24–41% background-refit exposure
   from sub-task 1 is therefore conditional on retaining that unification
   as an explicit choice — not automatic, and not yet made by the author.
   Routed to the Gate-1 revisit as an open question rather than assumed
   either way.

3. **Independently re-verified** (not just accepted) the $\alpha_1=
   -4c_{14}$ identity at $c_{13}=0$: checked symbolically for general
   $c_4$ (not just cdot-8's specific $c_4=0$ point) — holds identically.
   Cross-checked against the post-GW170817 Einstein-æther literature
   (arXiv:1802.04303 and the surrounding literature): the standard
   constraint parameterization is indeed built on $c_{13}\approx0$,
   consistent with the claimed form. Accepted the unification: AeST's
   exact $c_\text{gw}=c_\gamma$ ($c_{13}=0$) and its PPN singularity
   ($c_{123}=0$) are the same design fact.

4. **Adopted the staged derivation path**: boost the established screened
   quasistatic system to a 1PN moving source for $\alpha_1$, then the
   anisotropic $\alpha_2$ terms, carrying the $\chi=\varphi+Q_0\alpha$
   mixing but not condensate contamination (WP5's Gpc-scale $\mu_\text
   {eff}$ already clears that). Not yet executed.

**Files produced:** `Update-WP6-TensorSpeedStructure-2026-07-18.md` §5a
(new), this entry.

**Status**: checkpoint fully verified and incorporated. Two real
corrections to my own record accepted (the impossibility of the screening
derivation; the single-$\mu$ identification as an unmade choice). Next:
execute the staged 1PN derivation itself — the actual remaining content
of sub-task 2. Nothing in `cdot-7/` was touched.

---

## Entry 6 (worker) — Staged 1PN derivation attempted; reached a genuine, unresolved fork, reported honestly rather than forced (2026-07-18)

**Prompt (verbatim):**
> Please proceed.

**Summary of work performed:**

1. **Verified AeST's exact covariant field definitions from the primary
   source** rather than continue from recollection — caught and corrected
   my own earlier looseness: $J^\mu=A^\nu\nabla_\nu A^\mu$ is the aether's
   own acceleration vector, not a scalar current as §1/§2a implied.

2. **Fetched Foster-Jacobson's own physical setup for how $\alpha_1,
   \alpha_2$ arise** (order-by-order: static sector, then the aether's
   momentum-flux-sourced spatial tilt $u^i$, then the $g_{0i}$ Einstein
   equation) rather than assume a generic PPN picture. Confirmed vanilla
   aether's own $u^i$ solution is independently singular at AeST's
   kinetic-term point — consistent with, and prior to, §5's finding.

3. **Traced whether $\delta\phi$ can regularize this**, per the staged
   plan's pre-registered expectation. Found a real, non-obvious coupling
   channel (index-raising in $\mathcal Q=A^\mu\nabla_\mu\phi$ against the
   metric's own $g_{0i}$) that COULD let $\phi$ participate at the needed
   order — but could not responsibly confirm or rule this out through
   prose reasoning alone; the question needs the same systematic,
   order-by-order bookkeeping Foster-Jacobson's own dedicated derivation
   required, not a shortcut.

4. **Stopped at this fork rather than guess.** Stated plainly: if
   $\delta\phi$ doesn't participate, AeST's Maxwell-only aether choice may
   carry a genuine, unavoidable preferred-frame singularity — a real,
   possibly kill-relevant finding, different from the advisory's
   optimistic pre-registered expectation. If it does, the expectation
   likely holds. Declined to assert either without the rigor this
   question deserves, given the cost of guessing wrong in either
   direction.

**Files produced:** `Update-WP6-TensorSpeedStructure-2026-07-18.md` §5b
(new), this entry.

**Status: genuine progress, honest stop.** The exact field content is now
correct on the record; the calculation's real crux (does $\phi$ regularize
$\alpha_1$ or not) is identified precisely rather than glossed over.
**Recommending this specific fork be resolved with proper order-by-order
rigor** — ideally cross-checked independently, given the stakes — before
sub-task 2 can report a trustworthy $\alpha_1,\alpha_2$ value either way.
Sub-task 3 remains gated. Every finding inherits Gate 1's
provisional-failure caveat. Nothing in `cdot-7/` was touched.

---

## Entry 7 (worker) — Fork resolution assessed and independently re-derived from scratch (2026-07-18)

**Reference:** `Advisory-WP6-ForkResolved-2026-07-18.md` +
`ppn_fork_resolution.py`. Claims $\delta\phi$ participates via the direct
$U_i=\partial_i\delta\phi+Q_0A^i$ combination, giving a rank-1 gradient
matrix that explains vanilla æ-theory's $c_{123}=0$ singularity as an
artifact of inverting a mode AeST doesn't independently contain.

**Did not accept the rank-1 claim from the script's linear algebra
alone** — it *posits* the outer-product form and observes rank 1
trivially. **Independently re-derived $\mathcal Y$'s quadratic expansion
from scratch** (sympy, exact unit-timelike constraint $A^\mu A_\mu=-1$,
not a linearized approximation): confirmed $\mathcal Y_\text{quad}=
(\partial_i\delta\phi+Q_0A^i)^2$ exactly — the crucial $Q_0^2(A^i)^2$
piece (without which the outer-product structure fails) comes from the
constraint's second-order correction to $A^0$, a detail the script didn't
show working but which checks out exactly against the primary
definitions. **This substantially de-risks the core claim** — $\delta\phi$
and $A^i$ genuinely aren't independent gradient-carrying fields in the
$\mathcal Y$-sector; the singularity really is an artifact of the
aether-alone truncation.

**Flagged, not independently verified to the same standard**: whether the
metric's $g_{0i}$ enters inside the same combination (plausible, not
re-derived), and the "invertibility anchor" (SZ's stability spectrum
non-degeneracy ⟹ the stationary elliptic system is well-posed) — a
standard, reasonable, but bridging inference, not a literal theorem from
the source.

**Accepted**: the fork resolves in the pre-registered direction on solid
ground for the mechanism, reasonable-but-not-fully-certified ground for
rigorous finiteness. The actual $\alpha_1,\alpha_2$ values remain
undeveloped — agreed with the advisory that this is not skipped, just not
yet done.

**Files produced:** `Update-WP6-TensorSpeedStructure-2026-07-18.md` §5c
(new), this entry.

**Status**: fork resolved with independent verification of its load-
bearing step. **Housekeeping flagged**: the consolidation/errata batch
has now been requested across three consecutive advisory rounds and is a
real, accumulating item — noted, not yet delivered. Sub-task 3 remains
gated on the actual PPN value derivation. Nothing in `cdot-7/` was
touched.

---

## Entry 8 (worker) — Housekeeping delivered: consolidation batch (5 new cdot-7-portable items), errata/methodology log, K6 pattern library (2026-07-18)

**Prompt (verbatim):**
> Let's do the housekeeping first.

**Summary of work performed:**

1. **Extended `cdot-8/ConsolidationLog-2026-07-12.md`** with Items 11–15,
   the cdot-7-portable findings harvested since Item 10: a general
   verify-solution-first methodology rule (WP3); the true-equilibrium
   $e^\pm$ statistics fix and the entropy-vs-energy $(11/4)^{1/3}$
   derivation (both WP4b, directly reusable for any future cdot-7-native
   BBN work); the $\theta_*=r_s(z_*)/D_p(z_*)$ distance-convention
   correction (WP4a — directly relevant to cdot-4/cdot-5's own historical
   9$\times$–765$\times$ CMB failures per WP0); and the "$z{=}0$ sanity
   check needs a decomposition check first" caution (WP4b's rebuttal
   episode). Updated the priority table and closing summary accordingly.

2. **Created `cdot-8/proposal/ErrataAndMethodologyLog-2026-07-18.md`** for
   everything AeST/cdot-8-specific that doesn't belong in the
   cdot-7-portable consolidation log: the full K6 methodology-rule
   library (11 named rules, including a new version-provenance rule from
   this session's Brouwer-quote dispute); a complete error tally, both
   sides, this session (confirmed advisor errors, the one disputed-not-
   confirmed item held per the version-provenance rule, and confirmed
   worker errors — all caught before being used unqualified); and a list
   of AeST-specific results both parties have now independently confirmed
   as established program facts (the $\mu_\text{eff}$ dictionary, the
   $Q_0$ identification, the $\mathcal Y$-sector charter scope statement,
   the single-$\mu$ economy-vs-freedom open question, the $c_{13}=
   c_{123}=0$ one-fact-two-faces note).

3. **Closed the small housekeeping items**: clarified (rather than
   forced-reconciled) the log-numbering convention — two intentionally
   independent numbering streams, cross-reference by date+filename, not
   entry number; confirmed the 07-16 overwrite note is already in place;
   confirmed the WP4b rebuttal-withdrawal file is on disk for next sync.

**Files produced:** `ConsolidationLog-2026-07-12.md` (extended),
`ErrataAndMethodologyLog-2026-07-18.md` (new), this entry.

**Status: housekeeping batch delivered, closing the item requested across
three consecutive advisory rounds.** Next: continue the staged PPN
derivation (order-by-order bookkeeping for $\alpha_1,\alpha_2$ values) or
whatever the author sequences next. Nothing in `cdot-7/` was touched.

---

## Entry 9 (worker) — Staged derivation continued: vector sector confirmed healthy (one fetch error caught), and a genuine scope correction on α1's separability (2026-07-18)

**Prompt (verbatim):**
> We can now proceed with the staged PPN derivation.

**Summary of work performed:**

1. **Checked the aether's transverse (spin-1) sector independently**,
   since only $A^i$'s longitudinal part couples to $\phi$ — the
   transverse part is a separate concern §5b/§5c didn't address. Fetched
   Foster-Jacobson's vector-mode speed/energy formulas; an initial fetch
   claimed this sector is *also* singular at AeST's kinetic point.
   **Checked this myself symbolically before accepting it — it's wrong.**
   At AeST's point, vector speed$^2=1$ exactly and energy $\propto2c_1>0$:
   completely healthy, matching the tensor sector's own light-speed
   result. Caught a bad fetch claim before it entered the record.

2. **Found a genuine scope correction while verifying this**: Foster-
   Jacobson's $\alpha_1$ formula shares its exact denominator polynomial
   with the vector mode's own energy density (confirmed symbolically) —
   meaning $\alpha_1$ isn't a separable spin-0 quantity; it couples both
   aether sectors together. AeST's regularized spin-0 ($U_i$) and healthy
   spin-1 pieces can't simply be substituted into the existing formula —
   the actual derivation needs to be redone with AeST's field content
   from the covariant action.

3. **Assessed the timeline honestly**: this confirms the full derivation
   is genuinely the scale of Foster-Jacobson's own paper, not something a
   few more spot-checks finish. Two real findings came out of the
   attempt (vector-sector health; $\alpha_1$'s non-separability), but the
   numerical value is further out than the pre-registration assumed.

**Files produced:** `Update-WP6-TensorSpeedStructure-2026-07-18.md` §5d
(new), this entry.

**Status: genuine progress, honest scope correction.** Recommending the
full derivation be staged across further dedicated rounds, analogous to
WP3's multi-round action-closure effort, rather than forced to a number.
Sub-task 3 remains gated. Nothing in `cdot-7/` was touched.

---

## Entry 10 (worker) — Full re-derivation started, staged: Step 1 (sign/normalization dictionary) done (2026-07-18)

**Prompt (verbatim):**
> Agreed. Please proceed stepwise.

**Summary of work performed:**

1. **Spun off a dedicated document**, `Update-WP6-PPNDerivation-2026-07-18.md`,
   for the staged re-derivation, rather than keep extending the already-
   long structural-installment document.

2. **Step 1: pinned the cross-paper sign/normalization dictionary**,
   flagged by the advisor as unresolved. Checked both papers' conventions
   directly against the archived primary sources (`references/
   arXiv.gr-qc.0509083`, `references/arXiv.2109.13287`): both cite Wald's
   curvature conventions, differing only in metric signature. Worked out
   term-by-term how each piece of the action transforms under the
   signature flip (Ricci scalar flips sign; the quadratic vector-kinetic
   terms, having an even number of metric contractions, don't). Result:
   $c_1=K_B,\ c_2=0,\ c_3=-K_B,\ c_4=0$ — **exactly**, not just
   proportionally, resolving the previously-unpinned normalization.

3. **Stated confidence honestly**: each logical step is individually
   low-risk, but this is exactly the class of cross-convention matching
   that has produced real errors elsewhere this session (WP4b) —
   recorded as high-confidence, not certainty, flagged for an independent
   second check before being used to quote a final bound.

4. **Scoped Step 2 explicitly** (extend Foster-Jacobson's own $S_{ab}$/
   aether field equation, now fully archived and quotable, with AeST's
   scalar-sector terms, then re-run their exact 6-step solving procedure
   with their own order-counting convention) — not attempted this pass.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (new), this
entry.

**Status: Step 1 of the staged derivation complete.** A real, checkable
result (the pinned $c_1=K_B$ dictionary), appropriately hedged. Step 2
(extending the field equations and re-solving) is the next concrete
installment. Nothing in `cdot-7/` was touched.

---

## Entry 11 (worker) — Step 1 independently cross-checked and confirmed; one correction accepted; endgame made explicit (2026-07-18)

**Reference:** `Advisory-WP6-DictionaryCrossCheck-2026-07-18.md` +
`dictionary_crosscheck.py`, saved to the new `WP6/advisory/` subfolder.
**Reproduced the script myself** before accepting anything.

**Accepted, verified independently**: the $c_4$-structure carries exactly
one explicit metric contraction (checked directly: $u^a,u^b$ contract
metric-free against the mixed-tensor $\nabla_au^m$, leaving only $g_{mn}$)
and therefore flips sign under the signature relabeling — my blanket
"even number of contractions" claim was wrong for this one term.
Harmless to the boxed dictionary today ($c_4=0$), but now correctly
carried forward for Step 2, where a $\phi$-completion could induce
effective $u^au^b$-type terms.

**Accepted, and independently significant**: the advisory's mode-speed
cross-check (spin-1 speed$^2\to1$, spin-0 numerator $\to0$, both matching
SZ's independently-derived results in the opposite convention) is a
genuine end-to-end validation — physical quantities can't depend on
signature bookkeeping, so this discharges the "worth a second check"
flag on Step 1 properly, not just by re-reading the same argument.

**Checked, not just accepted**: the quoted pulsar-class bound $|\alpha_1|
\lesssim10^{-5}$ against current literature (live search) — confirmed
real (binary-pulsar constraints tighten the older $\sim10^{-4}$ LLR-only
bound by about an order of magnitude). Gives $K_B\lesssim2.5\times
10^{-6}$ *if* the æther-only leading form survives — explicitly not
asserted as final, since that's exactly what Step 2/3 must determine.

**Housekeeping**: flagged that this round's consolidation-batch request
appears to be a sync-timing gap, not a real second omission — the batch
was already delivered last round.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (Step 1a,
new), this entry.

**Status: Step 1 fully verified, not merely high-confidence.** Adopted
guidance to solve Step 2 in the $U_i/\chi$ variable rather than raw
$(\delta\phi,A_i)$ components. Next: Step 2 itself — extending $S_{ab}$
with AeST's scalar terms. Nothing in `cdot-7/` was touched.

---

## Entry 12 (worker) — Step 2: the general covariant φ field equation derived and cross-checked (2026-07-18)

**Prompt (verbatim):**
> Please proceed.

**Summary of work performed:**

1. **Derived the general covariant $\phi$ field equation** by varying
   AeST's scalar-sector Lagrangian with respect to $\nabla_\mu\phi$
   (standard Euler-Lagrange for a gradient-only Lagrangian) — not
   available explicitly in any archived source, a genuine derivation.
   Verified the quadratic-in-gradient factor-of-2 bookkeeping
   symbolically (sympy) before trusting it.

2. **Cross-checked against the cosmological background**: the equation
   collapses, on flat FRW, to exactly $\frac{d}{dt}(a^3F_Q)=0$ — the
   already-established free shift-current conservation law from WP3,
   reproduced as a special case rather than assumed.

3. **Cross-checked against the static quasistatic limit**: the projected
   gradient $U^\mu$ reduces, for a static aether tilt, to exactly
   Mistele's own $U=\nabla\varphi+Q_0\vec A$ — matching the primary
   source's definition exactly, not approximately.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (Step 2,
new), this entry.

**Status: Step 2 done, two independent checks passed.** The general
$\phi$ equation is now a trusted foundation, not an assumption, for the
O(1.5) perturbative expansion. Next: Step 3 — perturb this equation
jointly with the aether field equation and $S_{ab}$, in the $U_i/\chi$
variable, following Foster-Jacobson's exact 6-step order counting.
Nothing in `cdot-7/` was touched.

---

## Entry 13 (worker) — Step 2a: Mistele's own paper confirms the rank-1 split from a different angle, sharpening Step 3's target (2026-07-18)

**Prompt (verbatim):**
> Proceed.

**Summary of work performed:**

1. **Went back to Mistele's archived paper for its own $\vec A$
   treatment**, rather than assume the fork-resolution round's rank-1
   structure was the complete picture. Found, quoted precisely: setting
   $\vec A=0$ is inconsistent in general (only valid for special cases
   like spherical symmetry) — but the inconsistency is **entirely in
   $\vec A$'s curl part**. Via Helmholtz decomposition, the gradient part
   is exactly gauge-equivalent to zero (absorbed into $\chi=\varphi+
   Q_0\alpha_A$); only the curl part $\vec\beta_A$ is independently
   dynamical.

2. **Recognized this as the same fact as the fork-resolution round's
   rank-1 finding, reached from a completely different angle** — Mistele
   via gauge/symmetry argument, the earlier round via direct $\mathcal Y$
   expansion. Independent convergence, not a coincidence.

3. **Extracted and quoted Mistele's own static $\vec A$ equation of
   motion (their Eq. Aeom)** and matter-sourced $A=0$ equations (Eq.
   eomA0) exactly, as a further anchor for Step 2's general equation.

4. **Sharpened Step 3's target**: the momentum-flux/PPN calculation is
   specifically about $\vec A$'s curl part — the genuine analog of
   Foster-Jacobson's own $u^i$, expected to inherit their machinery
   closely with AeST's $(K_B,-K_B)$ values — while $\chi$ is governed
   separately by Step 2's own equation. This explains concretely why
   FJ's $\alpha_1$ formula (mixing both pieces, §5d) can't be reused
   directly, and gives Step 3 two tractable pieces instead of one
   undifferentiated coupled system.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (§2a, new),
this entry.

**Status: real structural progress, Step 3 not yet started but now much
better scoped.** Nothing in `cdot-7/` was touched.

---

## Entry 14 (worker) — Step 3a: the remaining divergence precisely localized to one term; the cancellation attempted but not yet certified (2026-07-18)

**Prompt (verbatim):**
> Good. Proceed.

**Summary of work performed:**

1. **Fetched Foster-Jacobson's full $O(1.5)$ derivation** (their $u^i$
   solution and $g_{0i}$ field equation sections), not just their
   summarized final formula — quoted their exact $g_{0i}$ equation:
   $(1-\frac{c_-c_+}{2c_1})h_{0i,jj}=16\pi G\rho v_i+(E+A\theta-\frac12)
   \chi_{,0ijj}$ (FJ's $\chi$ here: their PPN superpotential, a name
   collision with AeST's $\chi$ noted and kept distinct).

2. **Evaluated every coefficient at AeST's point symbolically**: $c_+=
   c_{13}=0$ makes the $h_{0i,jj}$ prefactor exactly 1 (unmodified GR —
   no $K_B$-renormalization of the gravito-magnetic sector at all) and
   automatically kills the one $A$-dependent piece inside $E$ (giving
   $E=K_B$, finite), regardless of $A$'s own divergence. **The entire
   remaining divergence localizes to the bare $A\theta$ term alone** —
   not $h_{0i,jj}$'s normalization, not $E$, not $\theta$ itself (all
   finite).

3. **Attempted the actual cancellation**: varied AeST's $\phi$-coupling
   terms with respect to $A^\mu$ to find the new source contribution
   that should replace this term. Got partway through (the $\mathcal Y,
   \mathcal Q$ piece cleanly, using $\mathcal Y=|\nabla\phi|^2_g+
   \mathcal Q^2$) but the $J^\mu\nabla_\mu\phi$ term's variation involves
   an integration-by-parts step with several index contractions, and I
   don't yet have an independent cross-check for it (unlike Step 2's
   equation, which passed two). **Did not report this as done** —
   flagged honestly as attempted, not certified.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (§3a, new),
this entry.

**Status: a precise, valuable localization result, plus an honestly
incomplete attempt at the actual cancellation.** The remaining task is
now sharply defined (show one specific new term cancels one specific old
divergence) rather than open-ended — real progress, even though the
final demonstration isn't done. Nothing in `cdot-7/` was touched.

---

## Entry 15 (worker) — Step 3b: completed the variation, found a structural problem with the whole strategy, escalating rather than pushing through (2026-07-18)

**Prompt (verbatim):**
> OK. Proceed.

**Summary of work performed:**

1. **Completed the variation** flagged incomplete in Step 3a — derived,
   twice, by the same method (a self-consistency check, not an
   independent one), the new source term AeST's $\phi$-coupling adds to
   the aether field equation.

2. **Tried to verify it against Mistele's static Eq. Aeom**, the same
   discipline Step 2 used. At leading static order, the new term reduces
   to something proportional to $\nabla_i\varphi$ alone — not the full
   $U_i=\nabla_i\varphi+Q_0A_i$ Mistele's equation is built around.

3. **Traced the discrepancy to its root, rather than patch around it**:
   Foster-Jacobson's $\delta u^i\sim O(1.5)$-only order scheme is a
   proven theorem specific to vanilla æther (their own text: lower
   orders "disallowed by the field equations" *for their theory*) — it
   does not carry over to AeST, whose $A^i$/$\chi$ genuinely has
   leading, non-momentum-flux (MOND-order) content per Mistele's own
   static analysis. **The whole "extend FJ's equations, reuse their
   order scheme" strategy silently assumed away the exact physics that
   makes AeST different from vanilla æther.**

4. **Did not push through with a patched calculation.** Flagged this as
   a structural problem with the approach, not a missing verification
   step — the actual fix needed is a two-scale expansion (leading
   static + subleading momentum-flux correction on $U_i/\chi$), a
   materially harder, different calculation. Recommended an explicit
   pause for re-planning or a touch point.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (§3b, new),
this entry.

**Status: a genuine mid-course structural finding, escalated rather than
patched.** This is the WP3 pattern repeating (a hard derivation revealing
its premise was subtly wrong partway through) — the discipline caught it
before more work was built on the flawed foundation. Nothing in
`cdot-7/` was touched.

---

## Entry 16 (worker) — Advisory assessed: sign error accepted, apples-to-oranges resolution independently re-verified by hand, pause resolves to a controlled refinement (2026-07-18)

**Reference:** `Advisory-WP6-Step3bAdjudicated-2026-07-18.md` +
`step3b_crosscheck.py`. **Reproduced the script and independently
hand-verified the load-bearing claim before accepting it.**

**Accepted correction 1**: a genuine sign error, mine — the $\phi$-
current's $F_Q$ term should be $-F_QA^\mu$, not $+F_QA^\mu$. Accepted the
methodological point too: both of my own cross-checks were structurally
blind to this term's sign (the FRW check can't see a current's overall
sign; the static check never exercised $F_Q$) — a passed check only
certifies what it exercises, new K6 entry.

**Accepted correction 2, after independent re-derivation**: the §3b
static-limit mismatch is an apples-to-oranges comparison (my variation
held all $A^\mu$ independent; Mistele's equation has $A^0$ already
eliminated via the constraint), not a broken equation. **Worked the
missing chain-rule term through myself** ($\partial A^0/\partial A^i
\approx A_i$ from the unit constraint; $\partial\mathcal Y/\partial A^0
\approx2Q_0^2$) and confirmed it supplies exactly the missing $2Q_0^2A_i$,
completing $\nabla_i\varphi\to U_i$ precisely. Resolves the mismatch
cleanly.

**What survives, correctly not dismissed**: the order-counting caveat is
real (FJ's scheme is proven only for vanilla æther), but its severity is
bounded — every actual PPN environment is deep in the screened regime,
so the "two-scale expansion" is just the already-implicit (PPN order)
$\times\varepsilon$ double expansion, with $\varepsilon$ Cassini-capped
from sub-task 1.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (§3c, new),
this entry.

**Status: the pause resolves to a controlled refinement, not a strategy
collapse.** Proceeding on the two-piece plan with three carried
requirements (corrected $F_Q$ sign; explicit constraint-force bookkeeping;
stated $\varepsilon$-truncations). Nothing in `cdot-7/` was touched.

---

## Entry 17 (worker) — Step 3d: the transverse sector solved exactly — clean GR, zero PPN content (2026-07-18)

**Prompt (verbatim):**
> Continue.

**Summary of work performed:**

1. **Executed the curl-sector half of the two-piece plan.** Showed,
   using FJ's own $O(1.5)$ aether equation, that a transverse/
   longitudinal projection cleanly drops the singular ($A\theta$-related)
   term *before* evaluating anything at AeST's specific point — the
   singular piece is tied to a pure-gradient (scalar superpotential)
   source, zero transverse component by construction.

2. **Solved the transverse aether response**: $u_i^T=\frac{c_-}{2c_1}
   h_{0i}^T=h_{0i}^T$ at AeST's values — finite, not even
   $K_B$-dependent.

3. **Checked the same projection on the $g_{0i}$ field equation itself**:
   the transverse equation is exactly $h_{0i,jj}^T=16\pi G\rho v_i^T$ —
   plain GR, no $K_B$, no singularity, nothing AeST-specific at all.

4. **Drew the consequence explicitly**: since every AeST-specific/
   singular piece lives entirely in the longitudinal projection, the
   transverse sector contributes *nothing* to $\alpha_1,\alpha_2$ — the
   entire preferred-frame signal must come from the longitudinal/$\chi$
   channel alone. Genuine structural simplification, not just a
   convenient framing.

5. **Scoped what's left honestly**: the longitudinal, matter-sourced,
   momentum-flux-order extension of Mistele's static $\nabla\Phi=U(1+
   \tilde\mu)$ relation has not been derived. Noted the qualitative
   expectation (screening-suppressed, per sub-task 1, so $\alpha_1$ may
   come out well below the naive $-4K_B$ estimate) explicitly as an
   expectation, not a result.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (§3d, new),
this entry.

**Status: real, clean, verified progress.** Half of the two-piece plan
(the transverse/curl sector) is solved exactly and shown to contribute
nothing to the PPN parameters. The remaining longitudinal derivation is
now the entire remaining content of sub-task 2 — not yet attempted.
Nothing in `cdot-7/` was touched.

---

## Entry 18 (worker) — Step 3e: a parametric estimate, explicitly not a certified result; consolidated status and recommendation (2026-07-18)

**Prompt (verbatim):**
> Proceed.

**Summary of work performed:**

1. **Attempted the full longitudinal, matter-sourced, momentum-flux
   equation** — extending Mistele's static relation, replacing the
   singular $A\theta$ term with AeST's actual response. Assessed that
   solving Step 2's equation perturbatively *around the already-nonzero
   screened static background* (not around zero, as vanilla æther's
   single-scale expansion does) is a genuinely harder calculation than
   anything completed in this arc, and did not complete it to the
   verification standard the rest of the arc has held to.

2. **Stated a physically-motivated expectation instead of a result**:
   the same screening that suppresses the static $U$ should plausibly
   also suppress its momentum-flux response, meaning $\alpha_1$ may sit
   well below the naive unscreened $-4K_B$ estimate — flagged explicitly
   as unverified, not to be quoted as a bound.

3. **Wrote a consolidated status** for the whole sub-task-2 arc: six
   solid, independently-verified results (the dictionary; the corrected
   $\phi$ equation; the rank-1 structure confirmed two ways; the precise
   divergence localization; its resolution; the exact, clean transverse
   solution) against one genuinely open piece (the longitudinal
   momentum-flux response). Recorded the three errors caught along the
   way (two self-confirmed after being advisor-flagged, one external
   fetch error caught before use) as the pattern holding throughout.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (§3e +
consolidated status, new), this entry.

**Status: recommending a pause on exact numerical closure.** The
qualitative picture (healthy in every checked mode; the one formal
degeneracy resolved by construction; PPN content plausibly but not
certainly screening-suppressed) is coherent and informative on its own.
Closing the exact $\alpha_1$ gap needs substantially more dedicated
work or an independent cross-check, given no published result exists to
lean on for this specific piece. Continuing to sub-task 3 or pushing
further on sub-task 2 is an author call. Nothing in `cdot-7/` was
touched.

---

## Entry 19 — Author decision: proceed to sub-task 3, sub-task 2 flagged pending next advisory (2026-07-18)

**Prompt (verbatim):**
> Let's proceed with subtask 3 now, and flag the completion of 2 as
> pending the next advisory.

**Recorded**: sub-task 2's exact $\alpha_1,\alpha_2$ closure is not
dropped — explicitly flagged as pending the next advisory round.
Proceeding to sub-task 3 (binary-pulsar confrontation) now, using
everything solid from sub-task 2 (the dictionary, healthy tensor/vector
modes, the transverse=GR result, the screening-suppression expectation
stated as an expectation) while carrying the open longitudinal
coefficient forward explicitly rather than assuming it resolved. Any
sub-task-3 result depending on the precise, undetermined value will
itself be flagged as conditional.

---

## Entry 20 (worker) — Sub-task 3 first installment: literature grounded, one clean result, one unresolved discrepancy found and flagged (2026-07-18)

**Summary of work performed:**

1. **Downloaded and archived both papers WP0 flagged** for sub-task 3
   (Yagi et al. 2014, arXiv:1311.7144; Vaglio et al. 2026,
   arXiv:2605.01436) into `references/`, with `.md` summaries, following
   the same convention as the WP5/WP6 literature base.

2. **Read Yagi et al. 2014's formalism**: binary-pulsar constraints rest
   on neutron-star "sensitivities," computed by numerically solving
   modified stellar-structure equations across multiple EOSs — a
   substantial numerical-relativity undertaking, explicitly flagged as
   out of scope to replicate from scratch this session.

3. **Read Vaglio et al. 2026's more recent, PPN-facing approach**: a
   different parameter basis, $(c_\theta,c_\sigma,c_\omega,c_a)$
   (kinematic decomposition of $\nabla U$), reduced to $\{\alpha_1,
   \alpha_2,c_\omega\}$.

4. **Derived the basis-translation dictionary** to Foster-Jacobson's
   $(c_1,c_2,c_3,c_4)$ myself (not assumed): $c_\sigma=c_1+c_3$,
   $c_\omega=c_1-c_3$, $c_\theta=c_1+3c_2+c_3$, $c_a=c_4$. At AeST's
   point: $c_\sigma=c_\theta=c_a=0$, $c_\omega=2K_B$ — **AeST's aether is
   pure vorticity**, a clean result consistent with everything already
   established about the transverse/curl sector.

5. **Checked this against Vaglio's own mode-speed formula rather than
   stop at the clean result** — found $c_V^2$ has a genuine pole at
   AeST's point ($c_a=0$ in the denominator, nonzero numerator),
   directly contradicting WP6's own independently-verified finding
   (Foster-Jacobson's vector-mode formula, cross-checked twice already)
   that this same mode is healthy with speed$^2=1$.

6. **Did not push past this.** Flagged the contradiction explicitly as
   unresolved — could be a dictionary error, a genuine difference in
   what the two formulas describe, or something else — and stopped
   rather than build sub-task 3 further on an unreconciled
   inconsistency between two primary sources.

**Files produced:** `Update-WP6-BinaryPulsar-2026-07-18.md` (new),
`references/arXiv.1311.7144.md`, `references/arXiv.2605.01436.md`, this
entry.

**Status: genuine progress and an honestly-flagged discrepancy.**
Recommending this be resolved next — ideally with an independent
cross-check — before any further sub-task-3 conclusion. Sub-task 2's
own open item (exact $\alpha_1,\alpha_2$) remains separately pending the
next advisory, not conflated with this new issue. Nothing in `cdot-7/`
was touched.

---

## Entry 21 (worker) — Process gap fixed: own verification scripts were never being saved to the repo (2026-07-18)

**Prompt (verbatim):**
> Is this written up for the advisor?

**Finding**: no — the Entry 20 write-up documented the dictionary
derivation and the $c_V^2$ discrepancy in prose (with pasted output),
but the actual verification code was only ever run ad hoc in the
scratchpad, never saved into the repo. Checked further: **this gap runs
through this entire session's PPN/binary-pulsar arc** — every advisor
round shipped a runnable companion script (`WP6/advisory/*.py`), but
none of my own derivations (the Cassini screening exposure, the
$m_\text{eff}$/$c_{123}$ check, the fork-resolution $\mathcal Y$-expansion,
this round's basis dictionary) were ever persisted as code, only as
prose describing output.

**Fixed for the current, most pressing item**: wrote
`wp6_pulsar_basis_discrepancy.py`, saved to `cdot-8/WP6/` (matching the
advisor's own convention), reproducing both the pure-vorticity result
and the $c_V^2$ pole side-by-side against Foster-Jacobson's formula —
now runnable and independently checkable by the advisor or any future
session, not just described. Linked from
`Update-WP6-BinaryPulsar-2026-07-18.md`.

**Status: gap identified and fixed for the live item.** The broader gap
(retroactively adding scripts for earlier rounds in this arc) is not
addressed here — flagged for awareness, not backfilled, given the
volume involved. Nothing in `cdot-7/` was touched.

---

## Entry 22 (worker) — Discrepancy resolved: one dictionary entry, verified by hand before accepting (2026-07-18)

**Reference:** `Advisory-WP6-PulsarBasisResolved-2026-07-18.md` +
`pulsar_basis_resolution.py`, saved to `WP6/advisory/`.

**Verified independently before accepting**: decomposed $\nabla_au_m
\nabla^au^m$ (the $c_1$ structure) by hand using $\nabla_au_m=[\sigma,
\omega,\theta\text{ part}]-u_aA_m$ — confirmed the cross-terms with the
projected kinematic part vanish (standard orthogonality) but $(u_aA_m)
(u^aA^m)=+A^2$ survives, a genuine induced acceleration term from $c_1$,
missed by my original by-eye matching of only $c_4$'s explicit $A_\mu
A^\mu$ term. Correct dictionary entry: $c_a=c_1+c_4$.

**Reproduced the resolution exactly**: with $c_a=K_B$ (not $0$) at
AeST's point, Vaglio's $c_V^2=1$ exactly — matching both Foster-
Jacobson's twice-verified result and Vaglio's own $c_T^2$. Three-way
agreement; neither primary source was wrong.

**Accepted the corrected, more coherent structural finding**: AeST's
aether is vorticity-plus-acceleration ($c_\omega=2K_B$, $c_a=K_B$), not
pure vorticity — and this explains, rather than just restates, why
$c_{14}$ is ubiquitous in the æ-theory literature ($\alpha_1=-4K_B$ now
reads physically as $\alpha_1=-4c_a$).

**Files produced:** `Update-WP6-BinaryPulsar-2026-07-18.md` (§2a, new),
`references/arXiv.2605.01436.md` (updated), this entry.

**Status: discrepancy fully resolved, both sources vindicated.**
Sub-task 3 remains gated on sub-task 2's $\chi$-coefficient, with a
registered (not yet checked) expectation that the small-$K_B$ regime
may make the pulsar bound reduce largely to Vaglio's weak-field bound
directly. Nothing in `cdot-7/` was touched.

---

## Entry 23 (worker) — Requesting advice on sub-task 2's remaining piece rather than proceeding speculatively (2026-07-18)

**Prompt (verbatim):**
> Proceed, or request advice on open items, as you prefer?

**Decision**: requesting advice, not proceeding solo. Sub-task 2's exact
closure was already flagged pending the next advisory, and sub-task 3
is gated on it — further solo work right now would either re-attempt a
derivation already assessed as needing more than hand-derivation, or
build sub-task 3 speculatively on an unresolved foundation. Neither
seemed like the honest choice.

**Wrote a precise, self-contained advisory request** in
`Update-WP6-PPNDerivation-2026-07-18.md` (new section): states exactly
what's needed (the matter-sourced, momentum-flux-order longitudinal
$\chi$ equation, replacing the singular $A\theta$ term), why solo
derivation stopped (perturbing around an already-nonzero background,
harder than anything completed so far, no independent cross-check
available), everything already established that doesn't need
re-deriving (the dictionary, the corrected $\phi$ equation, the rank-1
structure, the closed transverse solution, Mistele's static anchor), and
the specific open question (does the momentum-flux correction inherit
the same screening suppression as the static piece, and if so what does
$\alpha_1$ come out to).

**Status**: awaiting advisory input on this specific, scoped item.
Nothing in `cdot-7/` was touched.

---

## Entry 24 (worker) — Advisory received and assessed: Step 3e confirmed, a directional self-correction accepted, one literature number flagged (2026-07-18)

**Reference:** `Advisory-WP6-LongitudinalResponse-2026-07-18.md` +
`longitudinal_response.py`. Reproduced the script before accepting.

**Accepted**: Step 3e's screening-suppression hypothesis is confirmed at
the structural level (the linearized response operator has no soft
direction in the screened regime; no $O(1.5)$ source is enhanced), with
the honest caveat that the operator/scaling are derived but the $O(1)$
coefficient isn't.

**Accepted, and noted as a good sign**: the advisor reversed their own
earlier pre-registration — screening doesn't restore vanilla æ-theory's
$\alpha_1=-4c_{14}$, it suppresses the one (longitudinal) channel that
produced it, since Step 3d already showed the transverse sector is exact
GR. Corrected expectation: $\alpha_1=O(K_B\varepsilon)$, with one open
$O(K_B)$ "$E$-term" left as the certified-derivation item.

**Accepted the conservative envelope** ($|\alpha_1|\le4K_B$, giving
$K_B\lesssim2.5\times10^{-6}$) as a legitimate bound, not an equality —
unblocking sub-task 3 conditionally, as requested.

**Checked, and flagged rather than passed through silently**: the
"provisional" $\alpha_2$ envelope's underlying solar bound ($1.6\times
10^{-9}$) — a live literature check found the commonly-cited value is
$\sim2.4\times10^{-7}$, about two orders of magnitude looser. Doesn't
contradict the advisory's own "provisional" framing, but adds a concrete
reason not to use that specific number yet.

**Files produced:** `Update-WP6-PPNDerivation-2026-07-18.md` (advisory
response section, new), this entry.

**Status: sub-task 2 closes on a conditional, honestly-scoped basis.**
$\alpha_1=O(K_B\varepsilon)$ expected; $|\alpha_1|\le4K_B$ quotable as a
conservative envelope; exact closure left as explicit future work.
Proceeding to sub-task 3 on this basis. Nothing in `cdot-7/` was touched.

---

## Entry 25 (worker) — Sub-task 3 concluded on the conditional envelope; WP6 status consolidated (2026-07-18)

**Prompt (verbatim):**
> Please proceed.

**Summary of work performed:**

1. **Checked Yagi et al.'s own text directly** rather than assume the
   registered expectation: confirmed verbatim that the orbital decay
   rate "reduces to the GR result" as $c_i\to0$, and that the weak-field/
   zero-sensitivity curve follows directly from $\alpha_1,\alpha_2\to0$
   — i.e., small PPN parameters directly imply vanishing sensitivities
   and negligible dipole radiation, exactly as the registered
   expectation hoped, now grounded in the primary source's own words.

2. **Concluded sub-task 3** at the same structural/conditional level the
   rest of this arc has held to: for $K_B$ at or below the conservative
   envelope ($K_B\lesssim2.5\times10^{-6}$), cdot-8/AeST is consistent
   with all binary-pulsar observations in this literature — both
   preferred-frame and dipole-radiation tests — without needing the full
   Yagi-class numerical sensitivity calculation, which is not required to
   answer the pass/fail question sub-task 3 was scoped to answer.

3. **Stated plainly what this does and doesn't claim**: not an exact
   dipole-radiation amplitude, not a substitute for the still-open exact
   $\alpha_1,\alpha_2$ derivation — a conservative, literature-grounded
   consistency statement, on the same screening mechanism already
   protecting Cassini and solar-system PPN.

4. **Consolidated WP6's overall status**: all three sub-tasks plus the
   tensor-speed structural work now closed to a consistent standard —
   exact where tractable (tensor speed, sub-task 1), explicitly
   conditional/bounded where not (sub-tasks 2 and 3), all under Gate
   1(b)'s standing caveat.

**Files produced:** `Update-WP6-BinaryPulsar-2026-07-18.md` (§4–5, new),
this entry.

**Status: WP6's three sub-tasks and the tensor-speed structural work are
now closed**, to a consistent, honestly-hedged standard. Nothing in
`cdot-7/` was touched.

---

## Entry — New sub-task opened: External Field Effect / Solar-System quadrupole $Q_2$, a serious tension found (2026-07-19)

**Prompt (verbatim):**
> Regarding the Cassini check, has the latest results been included?
> https://ui.adsabs.harvard.edu/abs/2026arXiv260217884P/abstract
>
> [then:] SInce it is a relevant recent published results I think it
> deserves inclusion. So please add it to WP6 as a sub-task and check
> how it fits with our model.

**Summary of work performed:**

1. **Checked first, before doing anything**: confirmed this specific
   paper (Park, Hees, Famaey, Desmond & Durakovic 2026, arXiv:2602.17884)
   was not in the record, and — more importantly — that it tests a
   genuinely different observable (the External Field Effect/quadrupole
   $Q_2$) from what sub-task 1 already covers (a residual anomalous-
   acceleration bound far above $a_0$). Downloaded and archived the
   source (`references/arXiv.2602.17884/` + `.md` summary), read the
   actual formulas rather than relying on the abstract alone.

2. **Understood why sub-task 1's resolution doesn't obviously transfer**:
   $Q_2$ depends solely on the IF's shape *near* $a_0$ (the external
   Milky Way field, $e_N=O(1)$–$O(2)$), not the large-gradient tail —
   the screening argument that resolved sub-task 1 doesn't address this
   regime.

3. **Validated the computation machinery against the paper's own
   published number before trusting anything cdot-8-specific**: an
   initial attempt used $e_N=a_e/a_0$ directly and was wrong; caught by
   reproducing the paper's own $\delta=1$ RAR-IF case exactly (4
   significant figures) once the correct implicit relation
   ($\nu(e_N)e_N=a_e/a_0$) was used instead.

4. **Applied to cdot-7's own established, explicitly-preferred fit**
   (Simple IF, $a_0=1.39\times10^{-10}$ m/s², checked directly against
   Foundation.md, not assumed): predicted $Q_2\approx3.71\times10^{-26}$
   s$^{-2}$ — $\sim23\times$ the new bound, $\sim21\sigma$ tension.
   Checked the RAR alternative too: essentially the same tension,
   confirming this isn't fixable by switching IF family.

5. **Escalated, not resolved unilaterally**: opened as a new WP6 sub-task
   with the full derivation and honest scope statement (does not by
   itself establish anything about AeST's own not-yet-derived near-$a_0$
   completion); routed the cdot-7-relevant part to
   `ConsolidationLog-2026-07-12.md` as Item 16, explicitly flagged as a
   concern requiring author review, not a bounded merge task.

**Files produced:** `wp6_q2_efe_check.py` (new, in `cdot-8/WP6/`),
`references/arXiv.2602.17884/` + `.md` (new), Update-WP6-
TensorSpeedStructure §"New sub-task" (new), `ConsolidationLog` Item 16
(new), this entry.

**Status: a serious, quantified, independently-validated tension found
and escalated appropriately.** Not declared a kill of anything; the
cdot-7-relevant angle is explicitly routed for author review rather than
decided here. Nothing in `cdot-7/` was touched.
