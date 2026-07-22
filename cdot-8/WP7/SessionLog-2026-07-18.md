# Session Log — cdot-8/WP7 (2026-07-18)

*New work package, new file. WP6 closed (tensor speed exact; sub-task 1
closed; sub-tasks 2/3 closed conditionally on a cross-checked envelope).
Proceeding to WP7 (perturbation theory / CMB & matter power spectrum)
per the author's explicit choice, under Gate 1(b)'s standing
provisional-failure caveat on the cosmological background (WP4a's 27%
$\theta_*$ miss) — WP7 proceeds on current radiation-era assumptions,
per the author's own sequencing instruction, not a claim that miss is
resolved.*

---

## Entry 1 — Structural first installment: linear perturbation machinery imported, the horizon-scale M5 question posed (2026-07-18)

**Prompt (verbatim):**
> I'm all for proceeding to WP7.

**Summary of work performed:**

1. **Researched what's already established in AeST's own literature**
   before deriving anything, per this program's established rhythm.
   Found the founding paper (arXiv:2007.00082, already archived) contains
   a complete linear cosmological perturbation system, not just an
   abstract-level claim — Newtonian-gauge scalar/vector perturbations
   reducing to an effective fluid ($\delta,\theta$) with a nonstandard
   pressure contrast $\Pi$ sourced by the vector-field perturbations
   $\chi,\mathcal E_\alpha$, plus $\mathcal E_\alpha$'s own evolution
   equation. Quoted directly, not reconstructed from the abstract.

2. **Identified the key simplification the founding paper itself
   reports**: for a wide range of AeST's *native* parameters,
   $c_\text{ad}^2,w$ are small enough that $\Pi\to0$, giving dustlike
   evolution and a decoupled vector field — explicitly tied to AeST's
   own free $K(Q)$ function, which cdot-8's charter replaces wholesale
   with the census/M5-quadrature result. Whether this same simplification
   applies to cdot-8's own $F(Q)$ is a genuine, open, checkable question,
   not yet checked.

3. **Posed the genuinely new (cdot-8-specific) question**, mirroring but
   distinct from WP5/WP6's own local-decoupling questions: does $\delta
   \mathcal N$ (the perturbation of the horizon-wide census integral,
   WP2 §1) source new terms in the perturbed equations, beyond what
   already enters through background quantities? Flagged explicitly that
   WP5/WP6's own "local decoupling" answer cannot be assumed to carry
   over here — those arguments relied on strict locality ($\ll R_h$),
   while cosmological (CMB-relevant) perturbations include near- and
   super-horizon scales, precisely where a horizon-integral quantity's
   own fluctuation is least obviously negligible.

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`,
`references/arXiv.2007.00082.md` (updated), this entry.

**Status: structural first installment only, deliberately checkpointed**
— matches WP5/WP6's own opening rhythm rather than pushing to a full
power-spectrum calculation in one pass. Imported machinery is solid
(direct quotation from the primary source); the horizon-scale M5
question is posed, not resolved, and recommended as the next concrete
derivation task before attempting to check the $\Pi\to0$ simplification
for cdot-8's own $F(Q)$. Every finding inherits Gate 1(b)'s
provisional-failure caveat. WP6's own remaining item (sub-task 2's exact
$\alpha_1,\alpha_2$) remains separately flagged, not conflated with
WP7's scope. Nothing in `cdot-7/` was touched.

---

## Entry 2 (worker) — Advisory assessed: $\delta\mathcal N\neq0$ resolved with a window function; the real finding is a crossover-era fluid-form breakdown (2026-07-18)

**Reference:** `Advisory-WP7-FirstInstallment-2026-07-18.md` +
`wp7_structure.py`. **Reproduced the script before accepting anything.**

**Accepted, verified independently**: $\delta\mathcal N\neq0$, with the
per-mode M5 force carrying the standard spherical top-hat window
$W(kR_h)=3j_1(kR_h)/(kR_h)$ — confirmed this is exactly the real-space
top-hat's Fourier transform, the same window used throughout structure-
formation theory. Reproduced the table exactly: clean sub-horizon import,
a genuine new low-$\ell$/super-horizon M5 term at $kR_h\lesssim$ few
(not yet derived), $\sim8\%$ window at the first-peak scale.

**Accepted, the round's real finding**: pre-computing cdot-8's own
scalar-sector $w(a)$ from the established quadrature ($\rho_s=\tfrac12
QF_Q-\tfrac13F$, checked inline against $\Omega_s$ to $10^{-4}$ using
the same long-validated closure machinery this session has relied on
throughout) shows $\Omega_s$ crosses zero at $z\approx9640$ — $w,
c_\text{ad}^2$ formally diverge there (a generic, understood feature of
any fluid decomposition whose density crosses zero, not exotic). The
founding paper's fluid description cannot be used through this crossing;
the underlying field variables stay regular. WP7 must run the crossover
in field variables, falling back to the fluid form only where $|\Omega_s|
=O(1)$.

**Noted approvingly**: the advisory records its own v1 script failing an
inline self-check before delivery, catching two of its own errors — the
same discipline this program has held to throughout, now demonstrated on
the advisor's own side, and what surfaced the zero-crossing finding.

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§2a + updated status), this entry.

**Status: genuine, verified structural progress.** $\delta\mathcal
N\neq0$ established with its functional form; the crossover-era
fluid-breakdown finding reshapes how the $\Pi\to0$ question must be
approached (not a simple check — a question only cleanly answerable
away from the crossover). Next: derive the low-$\ell$ M5 term explicitly;
set up the field-variable crossover treatment. Every finding inherits
Gate 1(b)'s caveat — this crossover-era structure is coherent with, not
new damage beyond, WP4a's own background-level miss in the same era.
Nothing in `cdot-7/` was touched.

---

## Entry 3 (worker) — The M5 term derived, grounded in WP3's own established action (2026-07-18)

**Prompt (verbatim):**
> Please continue with the M5 term.

**Summary of work performed:**

1. **Went back to WP3's own record for the exact M5 action term**
   rather than reconstruct it from summary recollection, given how many
   corrections that saga went through. Confirmed $S_{M5}=\int dt\,
   \Lambda_M[Q-q(\mathcal N_\text{tot})]$, with $\Lambda_M,Q$ single,
   spatially-uniform functions of time — and the already-established
   identity $\Lambda_M=Na^3F_Q/(16\pi\tilde G)$ ($C_1=0$ already
   resolved), both quoted directly from the primary WP3 documents, not
   re-derived from scratch.

2. **Worked out the perturbative extension**: promoted $\mathcal N_i$ to
   its actual horizon-ball-integral definition while $\Lambda_M,Q$ stay
   uniform, giving a genuine linear-order M5 contribution to any single
   mode's own field equation, proportional to $\Lambda_Mq'(\bar{\mathcal
   N}_\text{tot})\times W(kR_h)$.

3. **Checked this isn't a repeat of the $D\equiv0$ artifact** before
   trusting it survives — confirmed it's a structurally different piece
   of the action (the $\Lambda_M$-$\mathcal N_\text{tot}$-$Q$ coupling,
   not the census/horizon sector's own kinetic back-reaction that
   resolved to zero).

4. **Obtained $q'(\bar{\mathcal N}_\text{tot})$ without introducing a new
   unknown**: via the chain rule along the already-established
   background trajectory, $q'=\dot{\bar Q}/\dot{\bar{\mathcal
   N}}_\text{tot}$, both sides already computable from existing scripts.

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§4, new), this entry.

**Status: the M5 term's structural form is established and grounded,
not yet numerically assembled.** The functional form, window scaling,
and coefficient (expressed entirely in already-verified background
quantities) are done. Not yet done: assembling into the specific
perturbed Einstein equation, the density/volume/horizon-boundary
decomposition, and the actual numerical coefficient along cdot-8's
trajectory — staged as the next concrete step. Nothing in `cdot-7/` was
touched.

---

## Entry 4 (worker) — Assembly continued: boundary question resolved from WP2's own text, target equation identified and checked against the inviolable-matter directive (2026-07-18)

**Prompt (verbatim):**
> Please proceed.

**Summary of work performed:**

1. **Checked the "horizon-boundary piece" against WP2's own original
   definition** rather than assume a separate contribution exists.
   Confirmed directly: the census integral's domain is a comoving ball
   of *coordinate* radius $R_h(t)$ — a pure background quantity, not
   itself perturbed. Resolves the question: no separate boundary-shift
   term exists beyond the volume-element piece already derived; the
   "three pieces" are density, volume, and $R_h(t)$'s own background
   role in the window's argument.

2. **Confirmed the density+volume decomposition** against the primary
   WP2 text: $\delta\mathcal N_i(k,t)=\bar{\mathcal N}_i\,W(kR_h)\,
   [\delta_i-3\Phi]$.

3. **Resolved which equation the new term enters, checked against WP3's
   own hard directive** (matter-sector continuity is inviolable — a
   named, non-negotiable constraint from early in WP3). Since matter
   couples to the metric alone (no disformal coupling, K1), the new M5
   term enters the gravitational constraint equation ($\delta G^0_0$),
   not matter's own continuity equation — checked against the directive
   explicitly, not assumed compatible by default.

4. **Assembled the term** into the perturbed Poisson-type equation, with
   the overall structure and coefficient in already-established
   quantities — but flagged the overall numerical prefactor as not yet
   independently cross-checked, recommending the natural verification
   (consistency with the already-established background $\tfrac12QF_Q$
   term at $k\to0$) as the next concrete step, given this program's
   repeated history of normalization errors surviving a first pass.

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§5, new), this entry.

**Status: the M5 term is now structurally complete and assembled**, with
one explicit, honestly-flagged verification step remaining (the $k\to0$
background cross-check) before the numerical prefactor should be treated
as final. Nothing in `cdot-7/` was touched.

---

## Entry 5 (worker) — The flagged $k\to0$ check fires: assembled term was incomplete, corrected (2026-07-18)

**Prompt (verbatim):**
> Check WP7/advisory for update.

**Reference:** `Advisory-WP7-SeparateUniverseCheck-2026-07-18.md` +
`m5_separate_universe_check.py`. Ran the flagged verification step
before proceeding, exactly as recommended.

**Verified the load-bearing identity by hand before accepting the
correction**: the required $k\to0$ coefficient, $\tfrac{d}{dQ}[-\tfrac
F3+\tfrac{QF_Q}2]=\tfrac{F_Q}6+\tfrac{QF_{QQ}}2$, confirmed by direct
differentiation, not just by trusting the script. My §5 assembled term
carried only $\tfrac{F_Q}2q'$ — the check fires, confirming a real gap.

**Understood the gap, not just patched it**: §5 varied $Q$ only where it
appears *explicitly* in the M5 constraint term, at fixed $\Lambda_M$ — a
legitimate partial derivative, but incomplete, since $\delta Q=q'\delta
\mathcal N$ also propagates through $\Lambda_M(Q)$ itself (field-
dependent via $F_Q$) and through the scalar's own $-F/3$ background
term. Together the three channels reproduce the required identity
exactly — nothing new, just the same perturbation carried consistently
everywhere $Q$ enters.

**Accepted the corrected coefficient**: $\delta G^0_0\supset8\pi G[\tfrac
{F_Q}6+\tfrac{QF_{QQ}}2]q'\bar{\mathcal N}_\text{tot}W(kR_h)[\delta_
{\mathcal N}-3\Phi]$ — noting the $QF_{QQ}/2$ piece is $O(1)$, not a
refinement, and that $F_{QQ}(Q_0)$ is now on its third independent
load-bearing appearance in this program (WP5's condensate mass, the SZ
stability sign, and this term) — a genuine coherence signal for the
zero-adjustable-element claim.

**Carried two flags forward, not dismissed**: the $\bar{\mathcal N}_i$
bookkeeping precision, and a genuine, unresolved gauge question (the
comoving-coordinate census domain makes $\delta\mathcal N$ Newtonian-
gauge-specific — consistent for now, but a real open item for the
covariant-completion program, potentially $O(1)$ exactly where this term
lives).

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§6, new), this entry.

**Status: the M5 term is now verified via the separate-universe check,
with a corrected coefficient and two flags carried forward.** Next: set
up the field-variable crossover treatment with this completed term
included. Nothing in `cdot-7/` was touched.

---

## Entry 6 (worker) — Field-variable crossover treatment worked out: M5 doesn't touch the scalar/vector equations at all, only the Einstein equation (2026-07-18)

**Prompt (verbatim):**
> Continue.

**Summary of work performed:**

1. **Stated plainly why $\Omega_s=0$ isn't a physical singularity**:
   $F,F_Q,F_{QQ}$ are smooth through the crossing; the $w_s,c_{\text{ad},s}
   ^2$ divergence is a generic artifact of forcing any field into a fluid
   description whenever its energy density changes sign. Concluded the
   correct fix is to never build the fluid description for this sector,
   evolving $\chi,\gamma,\alpha,\mathcal E_\alpha$ directly throughout —
   not a special patch only at the crossing.

2. **Checked, rather than assumed, whether M5 modifies $\chi,\gamma$'s
   own field equation** on top of the already-derived Einstein-equation
   term. Found $S_{M5}$ contributes $+\Lambda_MA^\mu$ to WP6 Step 2's
   $\phi$-equation, which already carries $-F_QA^\mu$ from the base AeST
   action — and since $\Lambda_M=Na^3F_Q/(16\pi\tilde G)$ identically
   (already established, $k$-independent since M5 is one constraint per
   slice), **these two terms cancel exactly, at every $k$.**

3. **Concluded $\phi$'s and $\alpha$'s own perturbed equations are
   unmodified by M5** — the founding paper's system (§1) can be used
   exactly as imported, with the *only* M5 content living in the
   Einstein-equation term already derived (§4–§6). This is the same
   "M5 doesn't disturb local physics" pattern WP5 found for solar-system
   scales, now checked directly (not assumed by analogy) for the
   cosmological field equations specifically.

4. **Stated confidence honestly**: the $k$-independence of $\Lambda_M$ is
   solid (same structural fact used throughout this arc); the
   cancellation is then algebraic and low-risk, but hasn't been checked
   numerically the way the $k\to0$ test caught §5's earlier gap —
   recommended as the natural next verification.

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§7–8, new), this entry.

**Status: WP7's structural phase is essentially complete.** The imported
system is clean sub-horizon; the one genuine new M5 term is derived,
verified, and corrected; the scalar/vector equations need no
modification at all; the crossover-era breakdown is resolved by
construction (never building the fluid description) rather than by a
special-case patch. Remaining: the numerical cross-check of the all-$k$
cancellation claim, and the eventual full numerical solve. Every result
inherits Gate 1(b)'s caveat. Nothing in `cdot-7/` was touched.

---

## Entry 7 (worker) — Attempting the recommended check surfaced a genuine ambiguity underneath §7, not yet resolved (2026-07-18)

**Prompt (verbatim):**
> Proceed.

**Summary of work performed:**

1. **Tried to state §7's recommended numerical cross-check precisely
   enough to actually run it**, and in doing so found that $S_{M5}=\int
   dt\,\Lambda_M[Q-q(\mathcal N_\text{tot})]$ is written, throughout
   WP3's own record, as a *pure time integral* — unambiguous only in the
   homogeneous background it was built for. §7 varied it against a
   specific Fourier mode as though $Q$ were a well-defined local field's
   value, but that covariantization was never actually settled.

2. **Identified two genuinely different readings**: $Q$ as the true
   global (all-space) zero mode of $\dot\phi$ — in which case a single
   $k\neq0$ mode trivially doesn't source $S_{M5}$ at all — versus $Q$
   as a horizon-ball average matching $\mathcal N_\text{tot}$'s own
   definition — in which case §7's cancellation argument applies, but
   with a window factor that needs showing explicitly, not just
   asserting by analogy.

3. **Checked whether the existing record already settles this — it
   doesn't**: confirmed directly that WP2's own $\mathcal N$ was built
   "reducing to cdot-7's $M_h/m_P$ in the *symmetric sector* by
   construction," i.e., only ever for the homogeneous system. This
   question is genuinely new, not something WP2/WP3 already answered.

4. **Did not resolve it, flagged it explicitly instead** — both readings
   plausibly give the same qualitative conclusion but for different
   reasons and different $k$-dependence, and this bears on how $Q$
   itself is defined at perturbative order, arguably prior to the
   already-completed M5-term derivation. Recommended settling this
   explicitly, likely with an advisor cross-check, before further
   numerical assembly.

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§9–10, new), this entry.

**Status: a genuine foundational ambiguity found and flagged, not
papered over.** Everything through §6 (the imported system, the window
function, the Einstein-equation M5 term) is unaffected and stands. §7's
specific conclusion needs this question resolved before being treated as
settled. Nothing in `cdot-7/` was touched.

---

**Continued in `SessionLog-2026-07-19.md`** — split by calendar day
2026-07-21 once this file (previously spanning 2026-07-18 through
2026-07-21 in one continuously-growing file) got long; entries after
this point were originally Entries 8+ in this same file.
