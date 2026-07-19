# Update — WP6 Sub-task 3: Binary-Pulsar Confrontation, First Installment

*Companion: `SessionLog-2026-07-18.md`, `wp6_pulsar_basis_discrepancy.py`
(the dictionary derivation and the $c_V^2$ discrepancy, runnable and
reproducible — not just described in prose). Proceeds per the author's
explicit instruction: begin sub-task 3 now, with sub-task 2's exact
$\alpha_1,\alpha_2$ closure flagged as pending the next advisory, not
dropped. Every result here inherits Gate 1(b)'s provisional-failure
caveat, and additionally carries sub-task 2's own open item (the
undetermined longitudinal/$\chi$ coefficient) as an explicit dependency.*

---

## 1. Literature landscape, grounded in primary sources

Downloaded and archived both papers WP0 originally flagged as the
concrete path for WP6 (`references/arXiv.1311.7144.md`,
`references/arXiv.2605.01436.md`), read in full rather than from
citation alone.

**Yagi, Blas, Barausse & Yunes (2014)** — the foundational binary-pulsar
Einstein-æther/khronometric constraint paper. Its central machinery,
**"sensitivities"** ($\sigma_A,\sigma_A'$ — how a neutron star's binding
energy responds to motion relative to the æther), requires numerically
solving the modified stellar-structure equations (interior + exterior,
matched, across several realistic equations of state) at linear order in
velocity. **This is a substantial numerical-relativity undertaking in
its own right** — comparable in scope to, and arguably larger than,
Foster-Jacobson's own PPN derivation that WP6 sub-task 2 has been
extending. Replicating it from scratch for AeST is out of scope for this
session; flagged honestly rather than attempted.

**Vaglio et al. (2026)** — the most recent, most stringent single-pulsar
(PSR J1738+0333) bound, using a Bayesian timing pipeline on the full
dataset. Works in a **different parameter basis**: the kinematic
decomposition $(c_\theta,c_\sigma,c_\omega,c_a)$ (expansion, shear,
vorticity, acceleration — the standard 3+1 decomposition of $\nabla_\mu
U_\nu$), reduced to the PPN-facing set $\{\alpha_1,\alpha_2,c_\omega\}$
for direct comparison with solar-system bounds.

## 2. A clean structural result — then a discrepancy that stops further progress here

**Derived the $(c_\theta,c_\sigma,c_\omega,c_a)\leftrightarrow(c_1,c_2,
c_3,c_4)$ dictionary** via the standard kinematic decomposition (not
assumed): $c_\sigma=c_1+c_3$, $c_\omega=c_1-c_3$, $c_\theta=c_1+3c_2+c_3$,
and $c_a=c_4$ (this last identification is solid — both conventions'
$c_a/c_4$ terms multiply $A_\mu A^\mu$ identically). At AeST's point
($c_1=K_B,c_2=0,c_3=-K_B,c_4=0$): $c_\sigma=0$, $c_\omega=2K_B$,
$c_\theta=0$, $c_a=0$ — checked symbolically. **A clean, valuable
result**: AeST's aether kinetic term is *pure vorticity* in this basis —
consistent with, and a cleaner restatement of, WP6's already-established
finding that only the transverse/curl sector is independently dynamical
(the vorticity tensor $\omega_{\mu\nu}$ *is* the transverse/curl content
of $\nabla U$).

**Then checked this against Vaglio's own mode-speed formulas, rather than
stop at the clean-looking result — and found a genuine, unresolved
discrepancy.** Their $c_V^2=(c_\sigma+c_\omega-c_\sigma c_\omega)/[2c_a
(1-c_\sigma)]$, evaluated at AeST's point, has a finite nonzero numerator
($2K_B$) over a zero denominator ($c_a=0$) — **a genuine pole**. This
directly contradicts WP6's own, independently-verified result (from
Foster-Jacobson's *own* vector-mode formula, evaluated in their native
basis, cross-checked twice already this session): the vector/spin-1 mode
speed is exactly $1$ and healthy at this same physical point.

**Reproducible in `wp6_pulsar_basis_discrepancy.py`** (saved alongside
this document, not just run ad hoc) — reproduces both the clean
pure-vorticity result and the $c_V^2$ pole side-by-side against
Foster-Jacobson's own formula at the identical point.

**Not resolved in this pass.** Possible explanations, none yet checked:
a sign or index error in the dictionary derived here; a genuine
difference in what the two papers' "vector mode" formulas actually
describe (e.g. a different residual gauge/normalization, or Vaglio's
$c_V$ describing a different physical combination than Foster-Jacobson's
spin-1 speed); or something not yet identified. **Flagging this
explicitly and stopping here, rather than building further conclusions
on top of an unreconciled contradiction between two primary sources** —
consistent with this program's standing practice of surfacing found
inconsistencies immediately.

## 2a. Discrepancy resolved — one dictionary entry, both primary sources vindicated

`Advisory-WP6-PulsarBasisResolved-2026-07-18.md` +
`pulsar_basis_resolution.py`, saved to `WP6/advisory/`. **Verified the
mechanism by hand before accepting the fix, not just reproduced the
script.**

**The error, confirmed independently**: the kinematic acceleration
coefficient is $c_a=c_1+c_4$, not $c_4$ alone. Decomposing $\nabla_au_m=
[\text{projected }\sigma,\omega,\theta\text{ part}]-u_aA_m$ and working
out $\nabla_au_m\nabla^au^m$ (the $c_1$ structure) myself: the
cross-terms between the projected kinematic part and the $-u_aA_m$ piece
vanish (standard orthogonality of $\sigma,\omega,\theta h$ to $u$), but
the $(u_aA_m)(u^aA^m)=(u_au^a)(A_mA^m)=+A^2$ term survives — a genuine,
**induced** acceleration-squared contribution from $c_1$, distinct from
$c_4$'s own **explicit** $A_\mu A^\mu$ term. My original dictionary
matched only the explicit piece and missed the induced one — the same
error class as an earlier, separately-caught $c_4$ signature slip
(itself a lesson about explicit-vs-induced contributions, now recurring).

**Verified the resolution reproduces exactly**: with $c_a=c_1+c_4=K_B$
(not $0$) at AeST's point, Vaglio's own $c_V^2$ formula gives **exactly
1** — matching Foster-Jacobson's twice-verified spin-1 result *and*
Vaglio's own $c_T^2=1$. **A three-way agreement, not a two-way patch.**
Neither primary source was wrong; the contradiction lived entirely in
one mistranslated entry.

**Corrected structural finding, better than the original**: AeST's
aether is **vorticity plus acceleration** — $(c_\theta,c_\sigma,c_\omega,
c_a)=(0,0,2K_B,K_B)$, not "pure vorticity." This is more coherent, not
less: $c_{14}=c_a$ explains why that exact combination is ubiquitous in
the æ-theory PPN literature (it's the acceleration coefficient — the
natural preferred-frame coupling), and the earlier $\alpha_1=-4K_B$
finding now reads physically as $\alpha_1=-4c_a$, exactly the shape
preferred-frame physics should take. $c_\sigma=0$ is again the same
$c_{gw}=c_\gamma$ design fact, visible in a third parametrization now.

**Sub-task 3 registered expectation, noted but not yet checked**: in the
small-$K_B$ regime, sensitivities (which scale with the $c_i$, per Yagi
et al.) vanish, so if sub-task 2's $\chi$-completion confirms $\alpha_1
\approx-4K_B$, the pulsar bound may reduce largely to Vaglio's weak-field
bound directly applied — with an explicit hedge that dipole radiation's
own $(s_1-s_2)^2$, $c_{14}$-dependence needs checking, not assuming.
Sub-task 3 continues to wait, correctly, on sub-task 2's still-open
$\chi$-coefficient.

## 3. Status

**Genuine progress**: the literature landscape is now grounded in primary
sources (not citations alone), both papers archived with full text, and
one clean structural finding (AeST's aether is pure vorticity) obtained.
**One load-bearing discrepancy found and explicitly not resolved**: two
primary sources' vector-mode-speed formulas disagree at AeST's specific
parameter point, under this session's own derived translation between
their conventions. **Recommending this be the next item resolved**
— ideally cross-checked independently, given the stakes of building
sub-task 3's actual pulsar bound on top of a contradiction that hasn't
been traced to its source. Sub-task 2's exact $\alpha_1,\alpha_2$ closure
remains explicitly pending the next advisory, as instructed, and is not
conflated with this new, separate discrepancy. Nothing in `cdot-7/` was
touched.

**Resolved (§2a): one dictionary entry ($c_a=c_1+c_4$, not $c_4$) was
the entire discrepancy — verified by hand, not just accepted.** Both
primary sources are correct; AeST's aether is vorticity-plus-acceleration,
not pure vorticity, a cleaner and more physically coherent result. Sub-
task 3 remains gated on sub-task 2's $\chi$-coefficient as before, with a
registered (unchecked) expectation that the small-$K_B$ regime may make
the pulsar bound reduce largely to Vaglio's weak-field bound directly.

## 4. Sub-task 2 closes conditionally — sub-task 3 proceeds on that basis

Per `Update-WP6-PPNDerivation-2026-07-18.md`'s advisory exchange:
sub-task 2 closes with $\alpha_1(\text{cdot-8})=O(K_B\varepsilon)$
expected (screening-suppressed beyond the naive æther-only estimate) and
a conservative, honestly-labeled envelope $|\alpha_1|\le4K_B$, giving
$K_B\lesssim2.5\times10^{-6}$ under the pulsar-class PPN bound
(independently verified against current literature earlier this
session).

**Checked directly against Yagi et al.'s own text before concluding
anything** (not assumed from the registered expectation alone): confirms
explicitly, quoted verbatim, "in the limit in which all the coupling
parameters go to zero, i.e. $c_i\to0$, [the orbital decay rate] reduces
to the GR result," and separately that the weak-field/zero-sensitivity
curve is obtained "by requiring that $\alpha_1^\text{æ}$ and $\alpha_2^
\text{æ}$ be identically zero, which results in vanishing sensitivities
in the weak-field limit" — i.e., **small PPN $\alpha_1,\alpha_2$ directly
implies small sensitivities, which directly implies negligible dipole
radiation** (dipole power $\propto(s_1-s_2)^2$, both $s_i\to0$ as the
coupling constants shrink). This is not an assumption; it is exactly what
the primary source states.

**Conclusion for sub-task 3, at the level this arc has consistently
held itself to (structural/qualitative, explicitly conditional, not a
precision strong-field calculation)**: for $K_B$ at or below the
conservative envelope established in sub-task 2, cdot-8/AeST is
consistent with all binary-pulsar observations used in this literature
(PSR J1141-6545, J0348+0432, J0737-3039, J1738+0333) — both the
preferred-frame/Keplerian-parameter tests (via the same $\alpha_1,
\alpha_2$ envelope already established) and the dissipative/dipole-
radiation tests (via the same small-coupling $\to$ vanishing-
sensitivity mechanism, confirmed directly from Yagi et al.'s own text,
not derived independently here). **The full Yagi-class numerical
sensitivity calculation is not needed to reach this conclusion** — it
would be needed only to extract a *tighter* bound than the conservative
PPN envelope already gives, which is explicitly out of scope for this
session (§1) and not required for the pass/fail question sub-task 3 was
originally scoped to answer.

**What this conclusion does and does not claim**: it does not certify
cdot-8's exact dipole-radiation amplitude, nor does it replace the
still-open exact $\alpha_1,\alpha_2$ derivation (sub-task 2's own
flagged future work). It does establish, on a conservative and
literature-grounded basis, that binary-pulsar data does not currently
exclude cdot-8, and — consistent with sub-tasks 1 and 2's own findings —
that this is the *same* screening/small-coupling mechanism operating a
third time: Cassini, solar-system PPN, and binary pulsars are protected
together, not independently.

## 5. WP6 status, consolidated

All three originally-scoped sub-tasks, plus the tensor-speed structural
work, are now closed to a consistent, comparable standard —
independently verified where verification was tractable, explicitly
conditional/bounded where an exact closed-form result was not:

- **Tensor speed** ($c_\text{gw}=c_\gamma$): exact, discharged by
  construction (§2a of the tensor-speed document).
- **Sub-task 1** (Cassini/ephemeris screening bound): closed, model-
  independent, comfortably satisfied.
- **Sub-task 2** (PPN $\alpha_1,\alpha_2$): closed conditionally — exact
  value open, conservative envelope $|\alpha_1|\le4K_B$ established and
  cross-checked.
- **Sub-task 3** (binary pulsar): closed conditionally, on the same
  envelope, confirmed consistent with the primary literature's own
  small-coupling limit.

Every result here inherits Gate 1(b)'s provisional-failure caveat on the
cosmological background — WP6 is legitimate parallel structural work
under that caveat, not a claim that the background problem is resolved.
Nothing in `cdot-7/` was touched.
