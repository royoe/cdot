# Update — WP5: The Local/Cosmological Decoupling Argument, and the Recovered Weak-Field Equation (First Installment)

*Companion: `SessionLog-2026-07-17.md` (this directory, new). Executes the
first piece of WP5 per the proposal ("recover AQUAL with $a_0=\lambda\dot
c(z)$; G1 lensing with evolving $a_0$; deliver the lensing-RAR-by-lens-
redshift prediction"). Deliberately scoped as a first installment, not a
complete WP5 pass — the remaining pieces (the actual lensing-RAR-vs-lens-
redshift curve, and the two-quasistatic-limit question WP0 flagged as
load-bearing) are substantial enough to warrant a checkpoint before
continuing, matching this program's established rhythm.*

---

## 1. What's imported, not re-derived

**$\Psi=\Phi$ (GR-like lensing, G1's core content) is established "by
construction" in AeST's own founding paper** (Skordis & Złośnik, PRL 127,
161302 (2021)) — a structural consequence of the aether being a genuinely
constrained (unit-timelike, Lagrange-multiplier-enforced), not independently
propagating, vector field, confirmed independently by the Hamiltonian
constraint analysis (Bataki, Skordis & Złośnik 2024: 4 first-class + 4
second-class constraints, exactly 6 physical DOF). This is invariant local
physics under this program's own K1 principle (Planck-unit invariance) and
is imported rather than re-derived — re-deriving it from scratch would
reproduce Skordis-Złośnik's own published calculation, not add anything
cdot-8-specific. **What cdot-8 needs to check is narrower: does the census/M5
closure disturb this structure?** — addressed in §2.

**The AQUAL weak-field limit's functional form** ($\mu(x)\nabla\Phi$,
$x=|\nabla\Phi|/a_0$) is likewise AeST's own established quasistatic limit,
not re-derived here.

## 2. The load-bearing question: does M5 touch the local, quasistatic sector at all?

M5 ($S_{M5}=\int dt\,\Lambda_M[Q-q(\mathcal N_\text{tot})]$) was built and
verified only in the **homogeneous, minisuperspace reduction** throughout
WP1–WP4b — $Q$ and $\mathcal N_\text{tot}$ are both purely time-dependent
quantities there. Since $\mathcal N$ is *defined*, from WP2 §1 onward, as a
**foliation integral over the entire horizon volume** ($\mathcal N(t)=
\int_{\Sigma_t\cap\text{horizon}}\rho_{E,\text{coord}}/E_P\,\sqrt q\,d^3x$),
not a local field, there is no already-built, spacetime-dependent version of
M5 to consult — this question has never been posed before in this program.

**Named assumption, stated before using it (per this program's own standing
practice — the aether-normalization flag, the $g_i$-placement flag)**:
$\mathcal N_\text{tot}(t)$, being a single horizon-integrated number, is
insensitive to any one local mass concentration's detailed structure — a
galaxy's own mass is already counted inside the census's integral, but
perturbing *where within the horizon* that mass sits, or how its density
profile looks locally, does not change the integral's value at leading
order. **M5 therefore constrains only the background, long-wavelength mode
$Q_0(t)$ (equivalently, $a_0(t)$'s cosmological evolution) — it does not
introduce any new constraint on the local perturbation $\delta Q(\mathbf
x,t)$ around an individual mass.** The local quasistatic sector is governed
by the *same* AeST field equations as the standard (non-Machian) theory,
evaluated at whatever $a_0(t)$ the background M5 constraint has set for that
system's epoch.

**Why this is the only well-motivated reading, not merely the convenient
one**: because $\mathcal N$ is inherently non-local by construction (an
integral, not a field), there is no natural way to promote M5 into a
*pointwise* local constraint without redefining what $\mathcal N$ means —
a much larger departure from everything already verified in WP2–WP4b than
this reading requires. **Flagged explicitly, not asserted as proven**: if a
future, more complete treatment ever needs $\mathcal N$ as a genuinely local
density (not just a horizon integral), this decoupling argument would need
re-examination. Nothing currently in the program requires that.

## 3. The recovered equation

$$\nabla\cdot\left[\mu\!\left(\frac{|\nabla\Phi|}{a_0(z)}\right)\nabla\Phi
\right]=4\pi G\rho,\qquad a_0(z)=\lambda\dot c(z),\qquad \Psi=\Phi,$$

with $a_0(z)$ read directly off the already-established, verified closure
trajectory (the same $\kappa\lambda$, $x_0$, $X_0$ machinery used
continuously since WP2) — no new fitting, no new free parameter. This is
the direct cdot-8 analog of cdot-7's own already-fitted $\hat a_0(z)$ curve
(Foundation §5.5, fit jointly to SN/RAR/mass-census data), now understood as
the correct *local* weak-field scale at each epoch given the decoupling
argument of §2, rather than an assumed correspondence.

## 4. What's genuinely still open — not attempted this round

**The two-quasistatic-limit question WP0 flagged as load-bearing**
(Mistele, arXiv:2305.07742: $m_\times\to0$ vs $m_\times\to\infty$, "percent-
level... except for wide binaries") — which limit cdot-8's own construction
sits in, and whether the lensing-RAR-by-lens-redshift prediction is
sensitive to it at the radii real lensing surveys probe (not wide
binaries) — has not been checked. **The actual lensing-RAR-vs-lens-redshift
curve** (the deliverable WP5 is named for) has not yet been built — it
requires combining §3's $a_0(z)$ with an actual weak-lensing mass-profile
formalism (converting a lensing-inferred acceleration/mass profile into the
same RAR form already fit dynamically), and reading the already-known
weak-lensing tension (Mistele, McGaugh & Hossenfelder 2023: AeST predicts a
low-acceleration deviation from MOND that current weak-lensing data don't
show) into what cdot-8 should honestly claim.

## 5. Confirmed and strengthened (advisory round, verified independently)

**The decoupling argument holds, on a sharper mechanism than §2 states.**
Varying $S_{M5}$ with respect to the *local* khronon $\phi(\mathbf x,t)$:
whatever spatial functional defines the background mode $\bar Q$ (volume
average, monopole — the choices differ only at second order),
$\delta\bar Q/\delta\phi(\mathbf x)$ spreads $\Lambda_M$'s force with weight
$1/V_\text{horizon}$ per point, while $\Lambda_M$ itself is extensive
($\propto Na^3F_Q$). The product is finite but **spatially uniform at
leading order** — exactly the already-verified background $\phi$-equation,
and nothing else. This is structurally identical to unimodular gravity's
global volume constraint (a Lagrange multiplier enforcing a spacetime-
integrated condition, well known not to introduce new local forces, only a
cosmological-constant-like background shift) — a known-safe precedent, not
a new risk. Checked independently before accepting: the argument holds for
either natural choice of $\bar Q$'s spatial definition, and the named
assumption from §2 (that $\mathcal N$ never needs to become a genuinely
local density) remains the only thing that could undo it — unneeded by
anything currently in WP1–WP4b.

**The clock, pinned explicitly** — warranted given this session's several
clock/convention-class errors: the unambiguous, exact-on-any-trajectory
identity is
$$\hat a_0(z)=\tfrac23\,\lambda\,c_0\,H_{\hat\tau}(z),$$
verified against the absolute anchor $\hat a_0(0)=1.386\times10^{-10}$
m/s² vs. cdot-7's independently fitted $1.39\times10^{-10}$ m/s². **Standing
epistemic note, carried verbatim because it matters for how this result
should be read**: by this identity, the lensing-RAR-by-redshift curve is
*the same prediction* as the dynamical $\hat a_0(z)$ fit and the SN
diagram — WP5 is a cross-probe consistency test with zero new freedom, not
an independent new curve. That is the honest deflation and the genuine
strength of this result at once.

**Prediction backbone**, $\hat a_0(z_\text{lens})/\hat a_0(0)=E(z_\text
{lens})$, verified against the established closure trajectory:

| $z_\text{lens}$ | $E(z)$ | survey context |
|---:|---:|---|
| 0.10 | 1.059 | SDSS/local stacks |
| 0.25 | 1.161 | KiDS bright lenses |
| 0.35 | 1.237 | KiDS/DES typical |
| 0.50 | 1.362 | DES deep lenses |
| 0.75 | 1.597 | HSC deep |
| 1.00 | 1.861 | future/LSST |

A $24\%$ enhancement at $z=0.35$, $36\%$ at $z=0.5$ — on the low-acceleration
RAR branch ($g\propto\sqrt{g_Na_0}$), an $11\%$–$17\%$ shift, within the
precision stacked weak-lensing samples now reach. Live and falsifiable in
both directions: a stacked-lensing finding of redshift-independent $a_0$
would pressure this directly.

## 6. Second installment's first task: does an $m_\times$-analog survive in cdot-8's own closed action?

AeST's own two-quasistatic-limit ambiguity and its known weak-lensing
tension (Mistele, McGaugh & Hossenfelder 2023: a predicted low-acceleration
departure from MOND that current data don't show) both trace to $m_\times$
— a mass-scale term belonging to AeST's native scalar sector. **cdot-8's
charter explicitly discards that native sector**, replacing it with the
census/M5-determined $F(Q)$. Whether cdot-8 inherits an $m_\times$-analog is
therefore a concrete, checkable question, not a re-import: does the
quadrature-determined $F(Q)$, expanded around the background $Q_0(t)$, carry
a term with the same structural role as AeST's own mass parameter? **Framed
as a hypothesis to test, not a conclusion to assume** (per this program's
verdict-scoping discipline): if no such term survives, the two-limit
question dissolves, the quasistatic sector is pure AQUAL at all accessible
radii, and the low-acceleration lensing RAR staying MOND-like would be
*consistent with the very data that pressures vanilla AeST* — a genuine
distinguishing feature, discovered by discarding rather than adding, but
claimed only if the inspection actually delivers it. Not yet attempted —
requires checking $F(Q)$'s exact role in AeST's action against where
$m_\times$ enters in the primary literature, not reasoning from memory of
either.

## 6a. The $m_\times$ inspection — the pre-registered hypothesis does not survive

Checked against the primary source (Mistele, arXiv:2305.07742) rather than
reasoning from memory of either AeST or cdot-8's own action. The paper's
quasistatic action (its Eq. 1) is
$$8\pi\hat GS=-\int d^4x\Big\{(\nabla\Phi)^2-2\nabla\Phi(\nabla\phi+Q_0A)+
(\nabla\phi+Q_0A)^2+J\big((\nabla\phi+Q_0A)^2\big)-m^2(\dot\phi/Q_0-\Phi)^2
+\tfrac{2K_B}{2-K_B}\nabla_{(i}A_{j)}\nabla^{(i}A^{j)}+8\pi\hat G\Phi\rho_b
\Big\},$$
with $m_\times\equiv Q_0\sqrt{(2-K_B)/(2K_B)}$. **$m_\times$ is built
entirely from $K_B$ (the aether vector's own spatial kinetic-term
coefficient) and $Q_0$ (a fixed coupling constant between $\nabla\phi$ and
the aether $A$) — it has no dependence on $J$ (AeST's free function, this
program's $F(Q)$) at all.** The paper is explicit that $J$ controls only the
MOND-interpolation shape via $\tilde\mu$'s limits, structurally separate
from $m_\times$.

**A notational collision worth flagging plainly, since it nearly caused a
misreading**: Mistele's "$Q_0$" is a *fixed coupling constant* in the
action (mass dimension 1, a parameter of the theory, not a dynamical
quantity) — an entirely different object from this program's own $Q_0(t)$/
$Q(t)$ (the cosmologically-evolving background value of the invariant
$Q=A^\mu\nabla_\mu\phi$ that the census/M5 machinery has been built around
since WP1). Same symbol, unrelated referent — caught before conflating them
into a claim that would not have followed from either.

**Consequence: the pre-registered hypothesis does not survive.** cdot-8's
charter modification replaces AeST's *native, freely-chosen* $F(Q)$ with the
census/M5-*determined* one — a change entirely within the scalar sector's
free function, the object Mistele's paper shows $m_\times$ is independent
of. cdot-8 has not touched the aether's own kinetic term ($K_B$) or the
fixed $\phi$–$A$ coupling ($Q_0$, Mistele's sense) at all — nothing in
WP1–WP4b modifies that sector, and WP0's own citation check already
confirmed cdot-8 inherits AeST's full constraint structure (Bataki et al.
2024: 4 first-class + 4 second-class constraints) unmodified. **The
$m_\times$ ambiguity, and the associated known weak-lensing tension it
produces, very likely persists in cdot-8 exactly as in vanilla AeST** — not
a distinguishing advantage discovered by discarding the native scalar, since
the discarded piece was never where $m_\times$ lived. Reported as the
honest outcome of a hypothesis that was framed, in advance, as something to
test rather than assume — and did not survive the test, per this program's
own verdict-scoping discipline.

**What this means for the remaining WP5 deliverable**: the two-quasistatic-
limit question (which of $m_\times\to0$ or $m_\times\to\infty$ applies) is
*not* dissolved and needs its own resolution before the lensing-RAR-vs-
lens-redshift curve can be built with confidence — carried forward as open,
not closed by this round.

## 6b. Correction accepted: the tension attaches to $m$, not $m_\times$ — and a sharper, zero-freedom question replaces it

**The advisory's correction is right, and I checked it against the primary
source myself rather than accepting it on say-so.** Re-fetched the paper
specifically for the $m$-vs-$m_\times$ distinction and confirmed by direct
quote: *"$m$ controls whether AeST reproduces MOND"* (the ghost-condensate
mass, the term $-m^2(\dot\phi/Q_0-\Phi)^2$'s coefficient — literally the
condensate's energy density, the dust-mimicking device this program's
charter discards), versus *"in contrast to $m$, the new mass parameter
$m_\times$ is not related to the ghost condensate... does not affect the
ability of AeST to reproduce MOND."* **My §6a conclusion — "the $m_\times$
ambiguity, and the associated known weak-lensing tension it produces, very
likely persists" — misattributed the tension to the wrong parameter.**
$m_\times$ genuinely has nothing to do with the MMH 2023 tension; $m$ does.
Correcting this explicitly rather than leaving §6a's sentence standing.

**The $Q_0$ point, re-examined**: the advisory's claim that Mistele's $Q_0$
is literally "the frozen background value of the condensate chemical
potential" (i.e., the same object as this program's own $Q(t)$) is
plausible and consistent with standard AeST notation conventions across
the wider literature, but **I could not independently confirm it is stated
explicitly in this specific paper** — the text introduces $Q_0$ as a bare
constant of the action without deriving it from a background solution
in the passages I could access. Recording this as genuinely unresolved
rather than accepting or rejecting outright: my original "entirely
different, unrelated referent" was likely too strong, but the advisory's
specific characterization isn't independently confirmed either.

**The corrected, sharper question**: does cdot-8's own quadrature-determined
$F(Q)$ generate an effective condensate mass, since $\delta Q=\delta\dot
\phi-Q_0\Phi$ has exactly the structure inside AeST's $m^2$-term? Checked
the skeleton computation's structure (not just its number): expanding
$F(Q_0+\delta Q)$ to second order gives a $\delta Q^2$ coefficient
$\propto F_{QQ}(Q_0)$, playing the same role as AeST's $m^2/Q_0^2$ — this
is the right shape of argument. **Reproduced the skeleton numerically**:
$F_{QQ}(1,\text{today})=-0.696$ ($H_0^2$ units), giving $m_\text{eff}\sim
1.4\times10^{-4}\,\text{Mpc}^{-1}$ — about $7000\times$ lighter than AeST's
chosen $m\sim1\,\text{Mpc}^{-1}$, and a condensate cutoff $r_c\sim80$ Mpc
for a $10^{11}M_\odot$ lensing-stack galaxy, far beyond the $1$–$3$ Mpc
survey radii.

**What I accept with confidence, and what I don't yet**: the *qualitative*
conclusion — cdot-8's effective condensate mass is Hubble-scale, not
Mpc-scale, because $F$ was built from the invoice ($\Omega_s$, an $O(1)$
quantity in $H_0^2$ units) with no free parameter tuned to galactic
physics — is robust to a normalization error of far less than the many
orders of magnitude needed to bring $r_c$ down to survey scales. **The
precise numerical prefactor is not yet independently verified** — matching
cdot-8's own $F(Q)$ normalization (from the $-\frac{a^3N}{16\pi\tilde G}
F(Q)$ term used throughout WP3) to Mistele's $J$/$m^2$ convention requires
a careful dictionary the advisory itself flags as its own historical
weak point (cross-frame normalization errors). Not attempted in full this
round — the qualitative conclusion (condensate negligible at lensing
scales) is what I'm willing to state now; the exact $r_c$ value is not.

## 6c. The careful $m_\text{eff}$ pass — resolved, exact dictionary confirmed against the primary source

§6c originally stopped short (recorded below, superseded) rather than
fabricate a normalization. The advisor's follow-up
(`Advisory-WP5-DictionaryDelivered-2026-07-17.md`,
`meff_exact_dictionary.py`) located the actual source where this is done
precisely: Skordis & Złośnik, "Aether scalar tensor theory: Linear
stability on Minkowski space," PRD 106, 104041 (arXiv:2109.13287) — the
companion stability paper, not Mistele's. **I did not accept this on the
advisor's say-so; I fetched the paper myself (via ar5iv) and checked every
load-bearing claim line by line**, including the one item the advisor
explicitly left for me:

- **$Q_0$, closed verbatim**: "$\phi\to\bar\phi(t)$" giving "$\mathcal Q\to
  \bar{\mathcal Q}=\dot{\bar\phi}$," with "$\mathcal K(\bar{\mathcal Q})$
  has a minimum at $\mathcal Q_0$ (a constant)" — confirmed exactly as the
  advisor characterized it. My §6b hedge was warranted at the time (Mistele
  alone doesn't say this) but the companion paper does.
- **The expansion**, their Eq. 10: $\mathcal F=(2-K_B)\lambda_s\mathcal Y-2
  \mathcal K_2(\mathcal Q-\mathcal Q_0)^2+\ldots$ — confirmed verbatim.
- **The mass formula**, their Eq. 58: $\mu^2\equiv2\mathcal K_2\mathcal
  Q_0^2/(2-K_B)$ — confirmed verbatim, exact equation, not paraphrased.
- **The stability condition**, their Eq. 31: $\mathcal K_2>0$ — confirmed.
  With $\mathcal K_2=-\frac14F_{QQ}(Q_0)$ and cdot-8's $F_{QQ}=-0.696<0$,
  this gives $\mathcal K_2=+0.174>0$: **the sign that looked like a tachyon
  worry is exactly the sign the paper's own stability analysis requires.**
- **The Mpc bound**, confirmed verbatim: "on observational grounds
  $\mu^{-1}$ must be larger than $\sim$Mpc" — the constraint AeST imposes
  by hand.
- **Quadratic-order sector-additivity**, confirmed verbatim: "the MOND-type
  term $\sim|\mathcal Y|^{3/2}$... do[es] not contribute to the second
  order action" — so the $Y$-sector (the imported MOND interpolation,
  which cdot-8 leaves untouched) and the $Q$-sector (what cdot-8's
  quadrature determines) genuinely separate at the order that matters; no
  field-redefinition dictionary is needed after all.
- **The one item left for me**: does cdot-8's $F(Q)$ occupy the same
  action slot, with matching sign, as SZ's $-\mathcal F(\mathcal Y,\mathcal
  Q)$? Fetched SZ's own action, their Eq. 1: $S=\int d^4x\sqrt{-g}/(16\pi
  \tilde G)\{R-2\Lambda-\ldots-(2-K_B)\mathcal Y-\mathcal F(\mathcal Y,
  \mathcal Q)-\lambda(\ldots)\}+S_m$ — **same prefactor $1/(16\pi\tilde
  G)$, same minus sign in front of $F$, as WP3's own validated minisuperspace
  term $-\frac{a^3N}{16\pi\tilde G}F(Q)$.** This is the exact match the
  dictionary is conditional on, and it holds.
- **Cross-paper consistency, checked myself rather than taken as asserted**:
  the propagating mass at $\lambda_s\to0$, $M^2=(2-K_B)Q_0^2/K_B$, should
  equal $2m_\times^2$ in Mistele's notation ($m_\times^2=Q_0^2(2-K_B)/(2K_B)$)
  — algebra confirms $M^2=2\times Q_0^2(2-K_B)/(2K_B)$ exactly. Holds.

**Result, now exact rather than a skeleton estimate**: with $F_{QQ}(Q_0{=}
1,\text{today})=-0.696$ ($H_0^2$ units, from the already-established
quadrature) and $K_B$ ranging over AeST's stable window $(0,2)$: $\mu^{-1}
\approx5$–$10$ Gpc, $r_c\approx64$–$100$ Mpc for a $10^{11}M_\odot$
lensing-stack galaxy — three-plus orders of magnitude above AeST's
hand-imposed $\mu^{-1}\gtrsim1$ Mpc requirement, and far beyond the 1–3 Mpc
that stacked-lensing surveys probe. **The skeleton's qualitative
conclusion is now the exact conclusion**: cdot-8's condensate is
negligible at every survey radius, MOND persists, and this is a genuine,
zero-freedom distinguishing feature relative to vanilla AeST (which must
tune $\mu$ by hand to avoid the same MMH 2023 tension). A bonus neither of
us anticipated: SZ's own low-$k$ unbounded-Hamiltonian caveat window
($k<\mu$) sits at cosmological-but-sub-horizon scales in AeST ($\mu^{-1}
\sim$Mpc) but is pushed to *super-horizon* scales in cdot-8 ($\mu^{-1}\sim$
Gpc) — squarely inside the regime where SZ's own Minkowski analysis
already concedes to the FLRW background, i.e. the M5-governed sector this
program controls directly.

**Status: the careful pass is done, independently verified against the
primary source at every step, not just reproduced numerically.** This
closes the last open structural question in WP5. The only remaining
deliverable is the lensing-RAR-vs-lens-redshift confrontation itself
(§7, rewritten below).

**Correction, 2026-07-20** (found in WP7, confirmed independently twice —
see `Update-WP7-PerturbationStructure-2026-07-18.md` §28–29): the
$F_{QQ}(Q_0,\text{today})=-0.696$ figure used above was a domain-boundary
numerical artifact (a derivative evaluated at the literal edge of the
solved ODE). The corrected value is $F_{QQ}(0)\approx-0.169$ — same
sign, roughly $4\times$ smaller in magnitude. Rescanning the same
$K_B\in(0,2)$ window with the corrected value (same exact-dictionary
formula, `meff_exact_dictionary.py`): **$\mu^{-1}\approx10$–$20$ Gpc,
$r_c\approx100$–$160$ Mpc** — roughly $2\times$ and $1.6\times$ the
originally-quoted band. Every conclusion above is unaffected in
substance and, if anything, more comfortable: the condensate is even
further from any observationally accessible scale, and SZ's low-$k$
window is pushed even further into the super-horizon regime already
argued to be safe. The qualitative picture ("the skeleton's conclusion
is the exact conclusion," negligible everywhere, zero-freedom relative
to vanilla AeST) stands unchanged; only these two numbers update.

<details><summary>Superseded: the original, honestly-incomplete §6c (kept for the record)</summary>

Went back to this program's own established action-level results (WP3,
`Update-WP3-ActionLevelAttempt-2026-07-12.md`): the validated minisuperspace
reduction gives $p_\phi=\frac1{8\pi\tilde G}F(Q)$, $\rho_\phi=-\frac1{8\pi
\tilde G}(F-QF_Q)$, confirming the skeleton's ansatz was structurally
sound but not the exact normalization. Flagged three blockers (the $Y$-to-$Q$
map, the $f_G$ factor, the $F_{QQ}<0$ sign question) and recommended a
touch point with the advisor rather than guess — all three dissolved
against the SZ stability paper, per the resolution above.

</details>

## 7. Status

**Superseded below — this section was stale as of the ScaleUnbundling/
DictionaryDelivered rounds; corrected in place.**

**All structural questions in WP5 are now closed.** §5's additions stand.
The $m_\times$ hypothesis (§6/§6a) was tested and does not survive — but
§6b corrected the attribution: the known MMH 2023 weak-lensing tension
traces to $m$ (the ghost-condensate mass), not $m_\times$, which is
phenomenologically inert at galaxy scales (sub-percent, per the source's
own figures — the two-quasistatic-limit question is a wide-binary
footnote, not a WP5 blocker). §6c then closed the sharper, zero-freedom
question this reframing opened: cdot-8's own $F(Q)$ generates an effective
condensate mass with $\mu^{-1}\approx5$–$10$ Gpc, $r_c\approx64$–$100$ Mpc
— confirmed exactly against the primary source (Skordis & Złośnik's
stability paper), not just estimated. Condensate negligible at all survey
radii; MOND persists; a genuine, zero-freedom distinguishing feature from
vanilla AeST.

**The only remaining WP5 deliverable is the lensing-RAR-vs-lens-redshift
confrontation itself** — nothing blocks it. Plan: use the already-delivered
$\hat a_0(z_\text{lens})/\hat a_0(0)=E(z_\text{lens})$ backbone (§5) as the
prediction, the $\mu(z)$ dictionary (§6c) as the condensate-cutoff
systematics line, and check against the stacked-lensing literature —
Brouwer et al. 2021 (KiDS-1000) and Mistele et al. 2024 (arXiv:2310.15248)
as anchors, per the advisory's directive.

## 8. First pass at the RAR-vs-lens-redshift confrontation: backbone cross-validated, literature reconnaissance done, statistical test not yet closed

**Positive cross-check, not previously done**: before trusting the
backbone against external data, checked it against this program's OWN
prior, independent result — cdot-7's SN/RAR-jointly-fitted $a_0(z)$
trajectory (`Fable-1/SessionLogEntry-8-A0Confrontation-2026-07-07.md`,
`a0_confrontation.py`), which predates cdot-8 entirely and was fit before
any of WP5's machinery existed. **Ran the actual script** (read-only, no
`cdot-7/` file touched) rather than trust a summarized figure: at
$z=0.25$, cdot-7's own fitted trajectory gives ratio $1.11$–$1.12$
(across its `simple`/`standard` $\mu$-form variants) against WP5's
backbone $E(0.25)=1.161$ — a real but modest $\sim4$–$5\%$ offset; by
$z=1.0$ the two converge to $1.82$–$1.85$ vs. $1.861$, agreement to
$\sim1$–$2\%$. (An initial reading of the script's printed table
suggested a much larger discrepancy at low $z$ — traced to my own
misreading of the table, which prints *absolute* $a_0$ in units of
$10^{-10}$ already multiplied by the $1.2$ SPARC anchor, not the bare
ratio; caught and corrected before writing this up.) **This is a genuine,
independent confirmation that cdot-8's covariantly-derived $E(z)$ backbone
is quantitatively consistent with cdot-7's own SN+RAR+MIGHTEE+MUSE-DARM-
fitted trajectory across the whole $0<z<1$ range**, not just at the $z=0$
anchor point checked earlier.

**Literature reconnaissance** (fetched both anchor papers directly rather
than assuming their structure): **neither Brouwer et al. 2021 (KiDS-1000
weak-lensing RAR) nor Mistele et al. 2024 (arXiv:2310.15248, joint
kinematic+lensing RAR) bins its lens sample by redshift.** Both pool the
KiDS-bright lens sample over $0.1<z<0.5$ (mean $\langle z\rangle\approx
0.2$–$0.25$) as a single population and treat $a_0$ as a universal
constant — Mistele et al. quote $a_0=1.24\times10^{-10}$ m/s² uniformly;
Brouwer et al. compare against McGaugh's canonical $1.2\times10^{-10}$
external baseline rather than reporting an independent fitted value. **The
proposal's "lensing-RAR-by-lens-redshift" deliverable, read as a direct
comparison against already-published numbers, does not exist yet in the
literature** — a genuine finding, not a shortcut taken. A real per-bin
test would need new redshift-binned analysis of the underlying KiDS lens
catalogs, beyond a literature comparison.

**What this means for the confrontation, done honestly rather than
rushed**: cdot-8 predicts $\sim12$–$16\%$ acceleration-scale growth
already by the anchors' own mean lens redshift ($z\sim0.2$–$0.25$), and
neither paper's own single quoted number shows an obvious sign of it
(Mistele's $1.24$ sits close to the canonical local $1.2$, not $12$–$16\%$
above it). **But asserting this as a real tension would repeat exactly the
kind of naive, uncontrolled comparison this program's own earlier work
(cdot-7's MIGHTEE-vs-SPARC zero-point episode; this session's WP4a/WP4b
normalization errors) has already shown to be unreliable without three
things I don't yet have in hand**: (i) the papers' own quoted statistical
uncertainty on $a_0$ (not located in this pass), (ii) the lens sample's
actual $n(z)$ weighting (a pooled measurement over a broad $n(z)$ smears
any redshift trend — a naive point-evaluation at the mean $z$ is not the
same calculation the survey performs), and (iii) a resolved zero-point
convention between whichever $a_0(0)$ anchor is used and each survey's own
fitting convention (cdot-7's own record already documents $0.3$–$0.5\times
10^{-10}$ cross-survey zero-point scatter as a known, non-decisive
systematic, not a discovery).

**Status: not yet a confrontation result, honestly.** What's solid: the
prediction backbone is now cross-validated against an independent,
pre-existing cdot-7 fit (new, valuable); the literature gap (no z-binned
lensing RAR exists yet) is a real, reportable finding in its own right.
What's still needed before a pass/tension verdict: the three items above —
this is the concrete next step, not a quick follow-up, and should be
scoped as such rather than forced to a premature conclusion in this pass.

## 9. WP5 closed — pre-registered prediction, literature gap, and a differential test design that escapes the pooled systematics

`Advisory-WP5-ConfrontationDesign-2026-07-17.md` +
`rar_bin_test_design.py` adjudicated §8's restraint directly: item (i)
(the papers' own uncertainty floors) closes from their own text —
**checked myself against both primary sources rather than accepted**.
Mistele et al.'s $\approx0.1$ dex ($\approx26\%$) systematic band on the
stellar-mass-to-$g_\text{obs}$ conversion is confirmed verbatim ("we
translate this 0.2 dex uncertainty [in stellar mass] into a $\sim0.1$ dex
uncertainty on $g_\text{obs}$"). **One claim did NOT survive my check**:
the advisory attributed to Brouwer et al. the characterization of the
missing-baryons systematic as "the single most severe limitation of our
analysis" — I could not find this phrase, or an equivalent severity
statement, anywhere in the paper; if anything Brouwer et al.'s own words
lean the other way ("current observational constraints indicate that the
resulting corrections are likely moderate"). **Flagging this as a
misquote, not accepting it into the record uncorrected** — it doesn't
invalidate the underlying point (missing baryons is a real, common-mode
degeneracy with any $a_0$ shift, and Brouwer et al. do discuss it at
length), but the severity language was overstated and shouldn't be
repeated as a direct quote. The independently-confirmed $6\sigma$
early/late-type RAR split is accurate as cited.

With that one correction, the adjudication stands: **both uncertainty
floors are real, common-mode with the 12–16% pooled signal, and large
enough that the pooled comparison genuinely cannot decide the question
either way** — §8's refusal to call a tension was correct, not merely
cautious. Reproduced `rar_bin_test_design.py` exactly: the intra-survey
differential bin ratio $R(z_\text{lo},z_\text{hi})=E(z_\text{hi})/E(z_\text
{lo})$ cancels the absolute zero-point and $M/L$ degeneracies that drown
the pooled numbers, leaving only differential (percent-level)
systematics. Feasibility ladder: KiDS-only median splits are
directional/$\sim1\sigma$; decisive ($3$–$5\sigma$) tests need $z_\text
{hi}\sim0.6$–$1.0$ lens bins, available only with DES/HSC-deep/LSST/Euclid
depth. Correctly scoped as a test of "$a_0$ tracks $H(z)$" vs. "$a_0$
constant," not of cdot-8's $E(z)$ shape against $\Lambda$CDM specifically
— any $a_0\propto H$ theory predicts nearly the same ratios.

**WP5 closes here**, per the advisory's directive and my own independent
check of it: (a) the pre-registered prediction ($E(z_\text{lens})$ curve,
$\pm4$–$5\%\to\pm1$–$2\%$ theory band, $\sqrt E$ amplitude law); (b) the
demonstrated literature gap (no z-binned lensing RAR published); (c) the
differential test design with its systematics budget and feasibility
ladder, registered before any binned analysis exists. **Reprocessing the
actual survey catalogs is new observational data-analysis work, outside
this program's charter as written — whether to pursue it as WP5b or as an
external proposal is an author scope decision**, alongside the standing
Foundation §6 item 6 gate on WP4a. Both are decision gates, not resolved
here.

**Standing housekeeping note**: the Foundation §6 item 6 decision (WP4a's
27% acoustic-scale miss) remains the gate for what this program's overall
findings are ultimately for — WP5 is legitimate parallel work under the
charter, but that decision should not age out silently while WP5/WP6
proceed. The KATRIN clock remains the program's most time-critical item;
nothing in `cdot-7/` was touched.

## 10. Note — a candidate dataset for the differential test, flagged for the record only

**2026-07-18, added after WP5's closure; does not reopen or change the
§9 verdict.** McGaugh, Mistele, Duey, Haubner, Lelli, Schombert & Li,
"The Baryonic Mass–Halo Mass Relation of Extragalactic Systems" (ApJ,
2026; arXiv:2603.06479), Table 1, provides six GAMA-II/KiDS-DR4
weak-lensing group-mass bins spanning $z=0.117$–$0.324$ with $V_f$ and
$M_b$ per bin — a genuinely redshift-spanning weak-lensing dataset,
unlike the two pooled anchors (Brouwer 2021, Mistele 2024) §8–9 already
examined. Reading off an effective $a_0$ per bin via the paper's own
baryonic Tully-Fisher normalization gives values that rise with $z$ at
face value (0.84 to $3.88\times10^{-10}$ m/s² across the six bins) — **but
the bins are constructed by baryonic mass, not redshift** (confirmed
against the paper's own methods text), and the mean $z$ increasing with
mass bin is very plausibly a flux-limited-survey selection effect (richer
groups detectable to greater distance), not a controlled redshift probe.
The paper itself doesn't address this. **This data is available and
worth knowing about; it is not yet the clean, mass-controlled differential
test §9 called for** — that would need the underlying group catalog for
a genuine 2D (mass, redshift) binning or a residuals-at-fixed-mass check,
not just this six-row summary table. Flagged as a candidate input for any
future WP5b-class effort; no action taken on it here, and §9's closure
stands unchanged.
