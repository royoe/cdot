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

## Entry 8 — Advisory adjudicates §9; §7 corrected at finite $k$ (2026-07-19)

**Prompt (verbatim):**
> Advice added.

**Summary of work performed:**

1. **Located and read** `Advisory-WP7-QDefinitionAdjudicated-2026-07-18.md`
   + `q_definition_adjudication.py` (timestamped 2026-07-19 06:46).
   **Reproduced the script before accepting anything** — the
   $1-W(kR_h)$ table and the $(aH/k)^2(1-W)$ scaling estimate reran
   exactly as delivered.

2. **Assessed reading (A) (global zero mode) ruled out**, three grounds:
   non-Machian/acausal; an incoherent all-space/horizon-ball pairing in
   one equation; and — the sharpest, a direct check against this
   document's own §4–§6 — the same $S_{M5}$ already produces a
   *windowed* $\delta\mathcal N$ when varied against densities, so its
   $Q$-side cannot consistently be windowless. All three hold up under
   independent reading, not just the advisory's assertion.

3. **Accepted reading (B)** (horizon-ball average, same ball as
   $\mathcal N_\text{tot}$) — the window symmetry §9 refused to assume by
   analogy is now derived rather than asserted, with one caveat carried
   forward (ball needs a center; fiducial-observer-anchored at
   perturbative order — joins the census-gauge flag as the same open
   item).

4. **Accepted the corrected §7 consequence**: the $-F_QA^\mu$/
   $+\Lambda_MA^\mu$ cancellation is exact only at $k\to0$ (reproducing
   §7's own worked case); at finite $k$ a $-F_Q(1-W(kR_h))$-weighted term
   survives — negligible sub-horizon ($(aH/k)^2$-suppressed, consistent
   with WP5/WP6), but $O(0.03$–$0.1)$ at $kR_h\sim1$–$6$, i.e. required
   (not optional) for the low-$\ell$ derivation. The low-$\ell$ sector now
   has both halves of its M5 structure (Einstein-side, §6; field-side,
   here) on the record.

5. **Updated** `Update-WP7-PerturbationStructure-2026-07-18.md` (§11,
   new) with the full adjudication, the corrected term, and the
   directives for the next assembly pass (rebuild §7's system with the
   field-side term, using two independent exact anchors; explicitly
   decide, on the WP2 record, whether census weights depend on local
   $Q$; carry the fiducial-center/census-gauge caveat forward together).

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§11), this entry.

**Status: §9's ambiguity resolved, §7 corrected (not overturned) at
finite $k$.** Everything through §6 stands unchanged; §7's practical
conclusion survives sub-horizon and at $k=0$ exactly, but needed
correction in the low-$\ell$ window — the same kind of "assumption
checked and found incomplete, not wrong in spirit" pattern as §6's own
correction earlier in this document. Not yet done: the numerical
cross-check of the corrected all-$k$ field equation; the explicit
decision on census-weight-$Q$-dependence; the full numerical
low-$\ell$/power-spectrum assembly. Nothing in `cdot-7/` was touched.

---

## Entry 9 (worker) — Running the recommended cross-check surfaces a second covariantization gap: $a^3$ vs. $R_h^3$ (2026-07-19)

**Prompt (verbatim):**
> Please continue.

**Summary of work performed:**

1. **Set out to run the accepted advisory's directive (1)** — rebuild
   §7's system with the field-side term, verify the $k\to0$ cancellation
   numerically alongside §6's separate-universe anchor — the natural
   next concrete step after §11's adjudication.

2. **Found a second gap while trying to state the check precisely**: the
   accepted correction's own derivation (Advisory §3) identifies
   $\Lambda_M$'s minisuperspace $a^3$ with $\mathcal N_\text{tot}$'s ball
   volume $(4\pi/3)R_h(t)^3$ ("$\Lambda_M$ extensive over the fiducial
   ball") without stating or deriving that these track each other. Traced
   $a^3$ to WP3's minisuperspace action (bare FRW scale factor, no $R_h$
   anywhere) and $R_h(t)$ to WP2's own $\dot R_h=c(t)$ definition — two
   independently-built objects.

3. **Checked numerically rather than assumed**: built and ran
   `wp7_lambda_extensivity_check.py` (saved to `cdot-8/WP7/`, reusing
   the validated trajectory machinery from `wp7_structure.py`),
   integrating $R_h(s)$ from its own defining relation with the same
   past-regularity anchor convention used throughout this program.
   **Result: $R_h(t)/a(t)$ is not constant anywhere in the checked
   range** — varies over nine orders of magnitude from deep radiation to
   today, including at $z_*$ and the $\Omega_s$ crossing where the new
   term actually lives. Identifying $a^3$ with $R_h^3$ is therefore a
   **modeling convention**, not a derived fact.

4. **Assessed the consequence honestly**: does not overturn §11's
   qualitative conclusion (the $k\to0$ limit is unaffected — no ball
   question arises there), but the term's finite-$k$ *normalization* —
   what will actually feed the numerical low-$\ell$ solve — is not yet
   secure pending an explicit, justified statement of this convention.
   **Not resolved, flagged rather than papered over** — recommending
   this be settled (ideally advisor-cross-checked), same discipline as
   §9.

**Files produced:** `wp7_lambda_extensivity_check.py` (new, in
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md` (§12,
new), this entry.

**Status: §11 stands as the best current statement, but its
finite-$k$ coefficient is now flagged, not certified.** The qualitative
structure (Einstein-side term §6 + field-side term §11, both vanishing
sub-horizon and at $k=0$) is unaffected. Recommending advisor input on
the $a^3\leftrightarrow R_h^3$ convention before treating §11's
coefficient as final or proceeding to the numerical low-$\ell$ solve.
Nothing in `cdot-7/` was touched.

---

## Entry 10 — Advisory concedes §12's catch in full (error #7); two established anchors pin the asymptotics regardless (2026-07-19)

**Prompt (verbatim):**
> Response uploaded.

**Summary of work performed:**

1. **Located and read** `Advisory-WP7-CovariantizationFreedom-2026-07-18.md`
   + `covariantization_adjudication.py`. **Reproduced the script before
   accepting anything** — its $d\ln R_h/ds$ and $R_h/e^s$ values match
   my own `wp7_lambda_extensivity_check.py` output exactly (independent
   confirmation, not a re-assertion of the same run).

2. **Assessed the concession**: the advisory concedes §12's catch in
   full — $a^3$ and $R_h^3$ are genuinely distinct volume conventions,
   never previously derived to coincide; logged as this program's
   error #7, caught by an independent runnable check before the
   coefficient was used for anything.

3. **Checked, rather than accepted on say-so, what the advisory claims
   survives**: two requirements already independently established in
   this record — §6's own exact $k\to0$ separate-universe result, and
   WP5's established local decoupling — pin the field-side term's
   cancellation factor to $\to1$ at $k=0$ and $\to0$ deep sub-horizon,
   for *any* admissible covariantization, regardless of the volume
   question. Verified directly: a fully local/pointwise reading (no
   window at all) gives a ratio that diverges as $k\to0$, violating
   Anchor 1 — a genuinely different, independently-excluded alternative
   from reading (A) (§9).

4. **Accepted the reformulation**: the field-side term is now written
   with an interpolating $\mathcal W(kR_h)$ pinned at both ends by the
   two anchors, top-hat $W$ adopted as a *stated default* (not a
   re-asserted derivation), with an explicit window-shape systematic
   band carried into the eventual low-$\ell$ deliverable. The three
   open flags (census gauge, fiducial center, this volume convention)
   are consolidated under one named item: *the census-sector
   covariantization freedom* — WP7's analog of WP6's own
   $\mathcal Y$-sector scope statement.

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§13, new), this entry.

**Status: the low-$\ell$ M5 signature's existence and asymptotic
pinning are now secure, independent of the conceded convention; its
detailed crossover shape is honestly carried as a named, bounded
systematic rather than false precision.** This is the same
"concede cleanly, keep what's independent, name the remaining freedom"
pattern WP6 used successfully. Next: run the two convention-independent
exact anchors as the assembly's brackets; decide the
census-weight-$Q$-dependence channel explicitly; the full numerical
low-$\ell$/power-spectrum solve. Nothing in `cdot-7/` was touched.

---

## Entry 11 — Census-weight-$Q$-dependence channel decided: no (2026-07-19)

**Prompt (verbatim):**
> Let's move to the decision on census weights.

**Summary of work performed:**

1. **Checked, rather than assumed either way**, whether $E_P(t)$ and the
   species exponents $p_i^\text{sp}$ carry independent local-$Q$-
   dependence, per the advisory's own directive to decide this
   explicitly on the WP2 record.

2. **Reread the existing definitions rather than adopt a new
   convention**: WP2's own foliation integral writes $E_P(t)$ with
   argument $(t)$ only, outside the spatial integral — a single
   time-slice normalization, same status as $\Lambda_M(t),Q(t)$; WP1 §5
   derives $p_i^\text{sp}$ as fixed kinematic exponents from the
   Planck-unit relabeling (matter $p=5/2$, radiation $p=1$, checked
   against known dilution laws), with no argument that could carry
   $Q$-dependence in the first place.

3. **Decided: no** — both objects are pure background/kinematic
   bookkeeping quantities; §5's density+volume decomposition of
   $\delta\mathcal N_i$ is the complete linear-order decomposition, no
   missing third channel. Scoped the decision narrowly — does not touch
   the separate, still-open census-sector covariantization-freedom item
   (§13).

**Files produced:**
`cdot-8/WP2/Update-WP2-Addendum-CensusWeightQDependence-2026-07-19.md`
(new), `Update-WP7-PerturbationStructure-2026-07-18.md` (§14–15, new),
this entry.

**Status: all four items from the original Q-definition advisory's
directive list are now addressed.** Remaining concrete queue: run the
two convention-independent exact anchors as numerical brackets; then the
full numerical low-$\ell$/power-spectrum solve. Nothing in `cdot-7/` was
touched.

---

## Entry 12 — WP2 addendum reviewed and accepted, with one amendment and one sharpening (2026-07-19)

**Prompt (verbatim):**
> Please check the advisors response to the addendum in the WP2 folder.

**Summary of work performed:**

1. **Located and read** `Advisory-WP2-AddendumReviewed-2026-07-19.md` +
   `census_weight_review.py` (in `cdot-8/WP2/`). **Verified the core
   claims independently**: $E_P\propto c^{5/2}$ is the standard
   Planck-energy scaling; the census integrand's $c^{p_i-5/2}$
   dependence reproduces WP2's own established $g_i=(p-\tfrac52)\dot c/c
   +3c/R_h$ structure exactly, with $p_\text{matter}-\tfrac52=0$ already
   fixed since WP1 §5 — not a new fact introduced to make the check
   work.

2. **Accepted the core verdict**: the addendum's "no local-$Q$-dependence"
   decision is correct on the definitions as written.

3. **Accepted the amendment**: my own scope note had drawn the line
   too cleanly — the alternative I declined (a locally-normalized
   census, $E_P(x,t)$ from a ball-smoothed local $c$) is excluded by
   convention, not by physics, so it properly files as **facet 4** of
   the census-sector covariantization freedom (§13), with my "no"
   recorded as the declared default rather than an independent closed
   fact.

4. **Accepted the sharpening**: the facet couples per species as
   $(p_i-\tfrac52)\delta c/c$, so matter is *exactly* immune
   ($p_m-\tfrac52=0$) — only radiation-class censuses feel it, meaning
   this facet touches only the radiation-era/crossover end of the
   low-$\ell$ term, not the matter-era part. A third untouchable item
   (matter-census invariance) now joins the freedom's two physical
   anchors.

**Files produced:**
`Update-WP2-Addendum-CensusWeightQDependence-2026-07-19.md` (§4, new),
`Update-WP7-PerturbationStructure-2026-07-18.md` (§13, §14 amended),
this entry.

**Status: WP2 addendum filed as amended and accepted.** The
census-sector covariantization freedom now has four named facets
(gauge status, fiducial center, volume convention, normalization
locality) and three untouchable anchors (separate-universe continuity,
sub-horizon decoupling, matter-census invariance). Remaining concrete
queue unchanged: run the two convention-independent exact anchors as
numerical brackets; then the full numerical low-$\ell$/power-spectrum
solve, with facet 4's band applied only to radiation-era coefficients
when quoted. Nothing in `cdot-7/` was touched.

---

## Entry 13 (worker) — Running the anchors as numerical brackets: Anchor 1 confirmed, Anchor 2 surfaces a major, escalated problem (2026-07-19)

**Prompt (verbatim):**
> Please continue with the anchors.

**Summary of work performed:**

1. **Built `wp7_anchor_brackets.py`** (saved to `cdot-8/WP7/`), running
   both convention-independent anchors as actual numerical checks
   rather than symbolic identities.

2. **Anchor 1 (k→0 separate-universe identity) confirmed numerically**:
   the $F_Q/6+QF_{QQ}/2$ coefficient stays finite and smooth through
   the $\Omega_s=0$ crossing itself ($z\approx9640$), with actual
   numbers, not just a general non-singularity argument. One honest
   caveat noted: it does grow large much further into the deep past
   ($z\sim10^6$), but this is the already-known, separately-tracked
   $F(Q)$ deep-radiation divergence from WP3's own record, not a new
   crossing-specific issue.

3. **Anchor 2 (sub-horizon decoupling) surfaced a major problem while
   checking it with real numbers instead of the illustrative
   placeholder**: computed $R_h(z_*)$ in physical Mpc and compared
   directly against WP4a's own established $r_s(z_*)=173.36$ Mpc and
   $D_p(z_*)=13074.3$ Mpc. **Result: $R_h(z_*)=3.32\times10^{-3}$ Mpc —
   smaller than $r_s(z_*)$ by $5.2\times10^4$, smaller than $D_p(z_*)$
   by $3.9\times10^6$.** Every observationally accessible CMB multipole
   therefore sits at $kR_h(z_*)\sim10^{-7}$–$10^{-4}$, deep in the
   $kR_h\ll1$ regime, meaning the field-side term's $(1-W)$ factor is
   negligible everywhere observable — not just small sub-horizon as
   previously framed.

4. **Identified the consequence honestly**: this directly contradicts
   the "$kR_h\sim6$ at the first acoustic peak" labeling used
   illustratively since §2a (`wp7_structure.py` Part A) — never
   actually checked against the real $R_h(z)$ trajectory until now,
   and off by four to six orders of magnitude when checked. Does not
   kill the M5 terms as algebraic structures, but threatens to
   substantially deflate the entire practical "genuine, unavoidable
   low-$\ell$ signature" framing built across §2a–§15.

5. **Did not declare a unilateral verdict** — two live possibilities
   named: either the physical conclusion really is this deflationary
   (the term is real but practically unobservable given cdot-8's own
   $R_h(z)$), or $R_h(t)$ (built for a *background*-level reduction
   check) is simply the wrong length scale for the *perturbative*
   window's smoothing radius, and a different, larger scale is what
   the physics needs. **Recommended explicit advisor input** before
   further numerical low-$\ell$ assembly is built on the current
   $R_h(z)$ convention.

**Files produced:** `wp7_anchor_brackets.py` (new, in `cdot-8/WP7/`),
`Update-WP7-PerturbationStructure-2026-07-18.md` (§16, new), this entry.

**Status: a major, consequential finding, escalated rather than
resolved or buried.** Anchor 1 stands confirmed. Anchor 2's mechanics
(the $\to1$/$\to0$ asymptotic pinning) are unaffected, but the *scale*
at which the transition actually occurs, given cdot-8's own literal
$R_h(z)$, appears to place the entire observable CMB/LSS range deep in
the negligible regime — a finding that, if it survives review, would
substantially revise (not just refine) §2a–§15's low-$\ell$ narrative.
Awaiting advisor/author input before proceeding to the numerical
power-spectrum assembly. Nothing in `cdot-7/` was touched.

---

## Entry 14 — Advisory concedes §16 in full (error #8); the phenomenology map inverts, relocating to the growth history (2026-07-19)

**Prompt (verbatim):**
> Response in WP7/advisory

**Summary of work performed:**

1. **Located and read** `Advisory-WP7-PhenomenologyMapInverted-2026-07-19.md`
   + `wp7_phenomenology_map.py`. **Reproduced the script before accepting
   anything** — $R_h(z_*)$ and $R_h(\text{today})$ match my own
   `wp7_anchor_brackets.py` output to the digit; the "elasticity" values
   check against my own independently-computed $d\ln R_h/ds$.

2. **Assessed the concession**: my $R_h(z_*)$ number and the "$kR_h\sim6$
   first acoustic peak" error (five orders of magnitude, illustrative
   value never checked, hardened across two prior advisories) are both
   confirmed — logged as advisor error #8.

3. **Assessed the correction, which inverts rather than confirms §16's
   conclusion**: $R_h(t)$ is time-dependent, so a mode's coupling has an
   *exit history* ($W\approx1$ while $R_h(t)<1/k$, decoupling once
   $R_h(t)$ grows past it) — I had checked $kR_h$ correctly but only at
   one fixed epoch ($z_*$), missing that every observable mode was fully
   coupled through recombination and only decouples later. Verified the
   mode-exit epochs and the growth-era coefficient magnitude directly
   (ratios $-0.58$ to $-0.67$, an $O(0.6)$ effect, matching the
   advisory's own prose though not its script's inline comment — a
   minor, noted inconsistency).

4. **Accepted the reframing**: the acoustic-peak-scale signature is
   genuinely negligible (my original number stands), the field-side term
   vanishes at $z_*$, but the Einstein-side term is at full,
   scale-independent strength there (required for consistency, no
   distinctive shape); a late-time $\ell\lesssim10$ remnant survives; and
   a new, order-one growth-history effect (the coupled-era Poisson-source
   modification) becomes WP7's central deliverable.

**Files produced:** `Update-WP7-PerturbationStructure-2026-07-18.md`
(§17, new), this entry.

**Status: §16's number confirmed; its practical conclusion superseded,
not simply restored.** The low-$\ell$/first-peak signature this program
chased since §2a is genuinely gone, replaced by a different, arguably
more consequential one (the growth history) — an honest example of an
error-catch cycle relocating a result rather than simply killing or
vindicating it. Next: errata the two advisories carrying the wrong
$8\%$ figure; build the coupled-era growth equation (radiation-class
census terms added) as the concrete numerical target; then the
late-time $\ell\lesssim10$ derivation. Nothing in `cdot-7/` was
touched.

---

## Entry 15 — Errata filed for the two advisories carrying the wrong first-peak figure (2026-07-19)

**Prompt (verbatim):**
> Contine.

**Summary of work performed:**

1. **Located both advisories carrying the wrong "$kR_h\sim6$/several-percent
   window" claim**: `Advisory-WP7-FirstInstallment-2026-07-18.md` (the
   origin, §1) and `Advisory-WP7-QDefinitionAdjudicated-2026-07-18.md`
   (propagated the same illustrative range in §3 without re-deriving it).

2. **Added a short, additive erratum notice to the top of each file**
   (not rewriting their content) pointing to the correction in
   `Update-WP7-PerturbationStructure-2026-07-18.md` §16–17, and stating
   explicitly what remains unaffected in each (the import/$\delta\mathcal
   N\neq0$/$\Omega_s$-crossing finding in the first; the reading-(A)-
   vs-(B) adjudication and the qualitative asymptotic structure in the
   second).

3. **Filed errors #7 and #8 formally in
   `cdot-8/proposal/ErrataAndMethodologyLog-2026-07-18.md` §2** (the
   program's consolidated error tally), with full detail on what was
   caught, how, and what survived each concession — and an explicit note
   that both were caught by the worker running literal, already-
   established definitions against advisor-asserted numbers, in
   consecutive rounds, direct evidence the verify-both-directions
   discipline works bidirectionally.

**Files produced:** erratum notices in both advisory files (edited),
`ErrataAndMethodologyLog-2026-07-18.md` (edited), this entry.

**Status: errata complete.** Remaining queue: build the coupled-era
growth equation properly (radiation-class census terms added to the
$O(0.6)$ estimate); then the late-time $\ell\lesssim10$ derivation.
Nothing in `cdot-7/` was touched.

---

## Entry 16 (worker) — Own bug caught while building the growth equation: $R_h(s)$'s exponent was wrong, inherited unchanged by two advisor rounds; corrected, growth equation built (2026-07-19)

**Prompt (verbatim):**
> Contine. [continuing directly from the errata task]

**Summary of work performed:**

1. **Set out to build the coupled-era growth equation properly** (§17's
   directive: add radiation-class census terms to the matter-only
   estimate), and before extending `wp7_lambda_extensivity_check.py`'s
   $R_h(s)$ integration, re-derived it from WP2's own $s\equiv\ln(c/c_0)$
   definition rather than trusting the inherited formula.

2. **Found a genuine bug**: the existing integrand used $e^{(2/3)s}$,
   correct only if $s\equiv\ln(a/a_0)$ — WP2's own record fixes
   $s\equiv\ln(c/c_0)$, giving $c/c_0=e^s$ directly and a corrected
   integrand $dR_h/ds=\tfrac32(c_0/H_0)e^s/E(s)$. **This bug had been
   reused unchanged across three rounds**, including two advisor
   reproductions (`covariantization_adjudication.py`,
   `wp7_phenomenology_map.py`) that copied the formula rather than
   re-deriving it.

3. **Checked the consequence directly**: numerical shifts of $O(1)$
   ($R_h(z_*)$: $3.3\times10^{-3}\to9.5\times10^{-4}$ Mpc; mode-exit
   epochs shift modestly) but every qualitative conclusion built on the
   old numbers — errors #7, #8, the mode-exit/growth-history reframing —
   survives unchanged, if anything slightly reinforced.

4. **Built the growth equation properly** with both fixes applied: the
   exact $d\ln\mathcal N_\text{tot}/ds=d\ln\hat u/ds+3+3\,d\ln R_h/ds$
   (derived from WP2's per-species evolution equation plus WP1's density
   map, showing $\mathcal N_i/\mathcal N_\text{tot}=\rho_{i,\text{phys}}/
   \rho_\text{tot,phys}$ exactly — census weight fractions equal
   ordinary density fractions). **Result**: the coupled-era Poisson-
   source modification stays at $O(0.5$–$0.7)$ through the matter era,
   matching §17's cruder estimate to within $\sim15\%$ — the order-one
   growth-history conclusion is robust to both corrections.

**Files produced:** `wp7_growth_equation.py` (new, in `cdot-8/WP7/`),
`Update-WP7-PerturbationStructure-2026-07-18.md` (§18, new),
`ErrataAndMethodologyLog-2026-07-18.md` (new worker-side entry), this
entry.

**Status: bug caught and fixed before further propagation; growth
equation delivered on the corrected trajectory.** The coupled-era
growth-history signature (§17's central deliverable) is now confirmed
order-one on the exact census-weight formula, not just the matter-only
estimate. Next: the late-time $\ell\lesssim10$ derivation. Nothing in
`cdot-7/` was touched.

---

## Entry 17 (worker) — The late-time $\ell\lesssim10$ signature: sourcing epoch identified (2026-07-19)

**Prompt (verbatim):**
> Continue with the last item.

**Summary of work performed:**

1. **Built `wp7_late_time_signature.py`** (saved to `cdot-8/WP7/`,
   reusing §18's corrected $R_h(z)$), defining a coupling profile
   $g(z;\ell)=k(z,\ell)R_h(z)$ with $k(z,\ell)=\ell/D_p(z)$ (the standard
   flat-sky relation, $D_p(z)$ built as a genuine function of $z$ via
   the same machinery as WP4a's $D_p(z_*)$, not just evaluated at one
   point).

2. **Result**: the field-side $(1-W)$ term is negligible ($\lesssim1\%$)
   by $z\gtrsim2$–$3$ and turns on to $O(0.1$–$1)$ over $z\sim0.3$–$1$
   for $\ell=2$–$10$ — squarely inside the standard dark-energy-
   domination window that sources the ordinary ISW effect. This
   identifies *where* (in redshift) the late-time signature is sourced,
   sharpening §17's qualitative "ISW-era" framing into an actual epoch
   range.

3. **Cross-checked independently**: the same formula evaluated at
   $z=z_*$ reproduces full coupling ($(1-W)\sim10^{-15}$–$10^{-14}$),
   matching §16–18's recombination-era finding via a completely
   different, continuous-in-$z$ construction — two independent routes,
   same conclusion.

4. **Stated honestly what this is not**: identifies *where* the term
   turns on, not yet the actual ISW $\Delta C_\ell$ modification, which
   needs the full line-of-sight Bessel-function projection weighted by
   the Weyl potential's time-derivative — flagged as the next, harder
   numerical step, not attempted here. Also noted the near-$z=0$
   coordinate artifact of the flat-sky $\ell=kD$ approximation itself
   (not a physical divergence).

**Files produced:** `wp7_late_time_signature.py` (new, in
`cdot-8/WP7/`), `Update-WP7-PerturbationStructure-2026-07-18.md` (§19,
new), this entry.

**Status: all four items from §17's directive list are now addressed.**
WP7's structural phase — the imported system, the window-function
architecture, the Einstein-side and field-side M5 terms, the growth-
history central result, and the late-time signature's sourcing epoch —
is complete. Remaining, honestly: the two exact anchors folded into the
corrected numerical system; the actual ISW $\Delta C_\ell$ computation;
the eventual full Boltzmann-style power-spectrum solve. Nothing in
`cdot-7/` was touched.

---

## Entry 18 (worker) — Folding the two exact anchors into the fully corrected assembly (2026-07-19)

**Prompt (verbatim):**
> Please proceed with the folding.

**Summary of work performed:**

1. **Built `wp7_folded_anchors.py`** (saved to `cdot-8/WP7/`),
   consolidating §18's corrected $R_h(s)$ and exact $d\ln\mathcal
   N_\text{tot}/ds$ into one pipeline and running both anchors on it
   together.

2. **Anchor A (k→0)**: confirmed the assembly introduces no arithmetic
   inconsistency (residual $=0$ to machine precision) — framed honestly
   as a regression/assembly check on the corrected pipeline, not a fresh
   re-derivation of the identity §6 already proved.

3. **Anchor B (kR_h≫1), checked more sharply than before**: verified the
   field-side term converges *monotonically and exactly* to
   $-F_Q(\text{today})=-1.8538$ as $kR_h\to\infty$ — literally the same
   symbol and numerical value as WP6 Step 2's static $-F_QA^\mu$ term
   (both differentiate the same action term at the same epoch), not
   merely the same order of magnitude. At galaxy/solar-system scales
   ($kR_h\sim10^5$–$10^9$), confirmed WP5/WP6's PPN/pulsar results are
   recovered with zero residual correction on the fully corrected
   pipeline.

**Files produced:** `wp7_folded_anchors.py` (new, in `cdot-8/WP7/`),
`Update-WP7-PerturbationStructure-2026-07-18.md` (§20, new), this entry.

**Status: anchor-folding task complete.** Both brackets hold cleanly on
the corrected assembly, with Anchor B now established as an exact
recovery rather than an order-of-magnitude check. Remaining: the actual
ISW $\Delta C_\ell$ line-of-sight projection; the eventual full
Boltzmann-style power-spectrum solve. Nothing in `cdot-7/` was touched.

---

## Entry 19 (worker) — Attempting the ISW estimate surfaces a foundational, prior gap: does $\Omega_s$ cluster? (2026-07-19)

**Prompt (verbatim):**
> Good! Proceed with the next step.

**Summary of work performed:**

1. **Attempted a first, leading-order ISW $\Delta C_\ell$ estimate**
   (`wp7_isw_estimate.py`): standard sub-horizon growth equation sourced
   by $\Omega_m(a)$ alone, M5 correction added as a fractional
   enhancement using §18/§19's machinery, compared kernels for
   $\ell=2,5,10$.

2. **Did not trust the output at face value**: the standard-case result
   gave $\Omega_m(z=50)=0.13$ and an ISW kernel peaking near $z\approx27$
   — both physically implausible. Checked why rather than reporting the
   number.

3. **Found the real issue**: computed cdot-8's own
   $\Omega_m,\Omega_\text{rad},\Omega_s$ decomposition and found
   $\Omega_s$ is 40–90% of the total budget at essentially every epoch
   from $z_*$ to today ($0.767$ at $z=50$, $0.430$ at $z_*$, $0.926$
   today) — nothing like $\Lambda$CDM's dark energy. My script silently
   assumed $\Omega_s$ is smooth/non-clustering, sourcing $H(a)$ but not
   $\Phi$ — almost certainly wrong given $\Omega_s$ is "dust-like"
   ($w\approx0$) through the matter era per §2a, exactly the equation of
   state a *clustering* component has.

4. **Escalated rather than patched**: identified this as a foundational
   gap prior to and larger than the M5-specific ISW question — whether
   $\Omega_s$'s own perturbations (via the already-imported
   $\chi,\mathcal E_\alpha$ field system) source $\Phi$ at all has never
   been addressed in this WP7 arc; all prior $\Omega_s$-perturbation
   discussion concerned the background crossover and fluid-vs-field
   description, not clustering. **Explicitly did not report the
   script's own $1.15\times$ ratio as a result** — flagged it only as
   the symptom that surfaced the gap.

**Files produced:** `wp7_isw_estimate.py` (new, in `cdot-8/WP7/`),
`Update-WP7-PerturbationStructure-2026-07-18.md` (§21, new), this entry.

**Status: a new, consequential, unresolved question found and escalated,
not pushed through with an unreliable number.** Recommending this be
settled — does $\Omega_s$ cluster, and if so how strongly — before any
further growth/ISW/power-spectrum numerics. Nothing in `cdot-7/` was
touched.

---

## Entry 20 (worker) — Exploring the $\Omega_s$-clustering question while the advisor is offline: machinery validated against plain AeST, then applied (2026-07-19)

**Prompt (verbatim):**
> The advisor is having a break for a few hours. In the mean time,
> please explore possible causes and that the machinery build can
> reproduce the expected results for plain AeST without cdot
> assumptions.

**Summary of work performed:**

1. **Built `wp7_aest_native_check.py`** (saved to `cdot-8/WP7/`), in two
   parts, per the author's own instruction.

2. **Part 1 — validated the general $\rho,P,c_\text{ad}^2$ machinery
   against AeST's own published, closed-form result**, with zero cdot-8
   content: the founding paper's native "sculpted FRW" $K(Q)=-2\Lambda+
   \mathcal K_2(Q-Q_0)^2$ toy model gives a general, convention-invariant
   $c_\text{ad}^2=(dK/dQ)/(Q\,d^2K/dQ^2)$. Checked symbolically
   (SymPy): this reduces to exactly $(Q-Q_0)/Q$ for the paper's own
   $K(Q)$, matching their quoted perturbative $c_\text{ad}^2\approx
   2w_0/a^3$ result in the appropriate limit; integrating their own
   field equation and substituting gives exactly a dust term plus a
   constant ($\Lambda$) term in $\rho(a)$ — the claimed dust+CC
   decomposition, reproduced symbolically with no numerics and no
   cdot-8 assumptions at all.

3. **Part 2 — applied the same, now-validated formula
   ($c_\text{ad}^2=F_Q/(QF_{QQ})$, convention-invariant) to cdot-8's
   own quadrature-solved $F(Q)$ trajectory**, computed for the first
   time in this program. **Result: $c_\text{ad}^2=O(1)$–$O(4)$
   throughout the entire growth-relevant range** ($z=0$ to $z\sim3000$)
   — quintessence-like, not dust-like, unlike AeST's own native $K(Q)$
   which is specifically engineered to keep $c_\text{ad}^2$ small.

4. **Checked one apparent anomaly before reporting**: near the
   $\Omega_s=0$ crossing, $c_\text{ad}^2$ swings sign and grows large —
   confirmed this is the already-known, already-explained crossing-era
   fluid breakdown from §2a, not a new artifact. Also caught and
   excluded a boundary finite-difference artifact at the very last few
   grid points near $z=0$.

5. **Stated honestly what this does and doesn't settle**: substantially
   de-escalates §21's blocker (disfavors strong dust-like clustering),
   lending real support to the "quintessence barely clusters
   sub-horizon" approximation my rough ISW attempt used without
   justification — but doesn't fully settle large-scale/ISW-relevant
   effects, and the fluid-$c_\text{ad}^2$ approximation itself still
   wants the field-variable treatment through the crossing (§7).
   Recommended as supporting evidence for the advisor's eventual
   review, not a substitute for it.

**Files produced:** `wp7_aest_native_check.py` (new, in `cdot-8/WP7/`),
`Update-WP7-PerturbationStructure-2026-07-18.md` (§22, new), this entry.

**Status: genuine, self-directed progress on the standing blocker while
awaiting advisor input.** The machinery is now independently validated
against a published, closed-form AeST result, and the same formula
gives the first direct evidence on whether cdot-8's own $\Omega_s$
clusters. Nothing in `cdot-7/` was touched.
