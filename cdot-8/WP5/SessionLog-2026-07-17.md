# Session Log — cdot-8/WP5 (2026-07-17)

*New work package, new file. WP4a/WP4b closed (θ* fails by 27%, a genuine
crossover-era finding; BBN passes at leading order after a substantial,
multi-round normalization dispute that was ultimately resolved in BBN's
favor). Proceeding to WP5 per the user's explicit choice to follow the
original roadmap (WP5 → WP6 → WP7) rather than skip ahead to the
perturbation/CMB work.*

---

## Entry 1 — Structural first installment: the M5/local decoupling argument (2026-07-17)

**Prompt (verbatim):**
> Lets proceed towards WP7, carefully.

(Followed by a clarifying exchange: the original proposal gates WP7 behind
WP5 — weak field with evolving $a_0$ — and WP6 — tensor speed, PPN, binary
pulsar — neither of which had been started. User chose to go through WP5
and WP6 first rather than skip ahead.)

**Summary of work performed:**

1. **Researched what's already established in AeST's own literature**
   before deriving anything (via a background research pass over WP0's
   full literature review): $\Psi=\Phi$ (GR-like lensing) is established
   "by construction" in AeST's founding paper (Skordis & Złośnik 2021),
   confirmed independently by the Hamiltonian constraint analysis (Bataki
   et al. 2024). The AQUAL weak-field limit's functional form is likewise
   already established. **The load-bearing open question WP0 itself
   flagged**: Mistele's (arXiv:2305.07742) two quasistatic limits
   ($m_\times\to0$ vs $m_\times\to\infty$), with the proposal's own
   "lensing-RAR-by-lens-redshift" item explicitly flagged as needing to be
   checked against which limit it assumes.

2. **Identified and addressed the genuinely new (not literature-importable)
   question**: does cdot-8's own M5 closure constraint disturb the local,
   quasistatic (galaxy-scale) sector at all? Traced this to the fact that
   $\mathcal N$ is defined (WP2 §1) as a horizon-wide foliation integral,
   not a local field — meaning M5 has no natural pointwise/local
   generalization without redefining $\mathcal N$ itself. Concluded, as a
   **named assumption** (flagged explicitly, not asserted as proven): M5
   constrains only the cosmological background $Q_0(t)$/$a_0(t)$; local
   quasistatic physics around individual masses is governed by the
   standard (non-Machian) AeST field equations, evaluated at whatever
   $a_0(t)$ the background constraint sets for that epoch.

3. **Stated the recovered weak-field equation**: the standard AQUAL Poisson
   equation with $a_0(z)=\lambda\dot c(z)$ read directly off the
   already-established, verified closure trajectory — no new fitting.

**Files produced:** `Update-WP5-WeakFieldStructure-2026-07-17.md`, this
entry.

**Status: a structural first installment, not a complete WP5 pass.**
Deliberately checkpointed here rather than pushing to a complete lensing
prediction in one pass, given how load-bearing the decoupling argument is
and this program's repeated history of finding real problems exactly where
a modification was assumed (without checking) not to propagate somewhere
unexpected. **Not yet done**: the two-quasistatic-limit question itself
(which limit applies, and whether it matters at real lensing-survey
scales, as opposed to wide binaries); the actual lensing-RAR-vs-lens-
redshift curve; reconciling with the already-known weak-lensing tension
(Mistele, McGaugh & Hossenfelder 2023) that AeST itself carries
independent of cdot-8. The KATRIN clock remains the program's most
time-critical item; nothing in `cdot-7/` was touched.

---

## Entry 2 — Advisory confirms and strengthens the decoupling argument; the $m_\times$ hypothesis tested against the primary source and does not survive (2026-07-17)

**Prompt (verbatim):**
> Advice uploaded.

(Reference: `Advisory-WP5-DecouplingConfirmed-2026-07-17.md` +
`wp5_decoupling_check.py` — advisor confirmed the decoupling argument via
an explicit variational mechanism (the M5 multiplier's force on the local
field is spatially uniform at leading order, structurally identical to
unimodular gravity's global volume constraint); pinned the clock via the
charter identity $\hat a_0(z)=\tfrac23\lambda c_0H_{\hat\tau}(z)$, verified
against cdot-7's fitted value; delivered the lensing-RAR prediction
backbone ($\hat a_0(z_\text{lens})/\hat a_0(0)=E(z_\text{lens})$); and
directed the $m_\times$ inspection as the second installment's first task,
framed as a testable hypothesis — if no $m_\times$-analog survives in
cdot-8's closed action, the two-quasistatic-limit question dissolves and
the low-acceleration lensing RAR stays MOND-like, a potential distinguishing
advantage.)

**Summary of work performed:**

1. **Verified both numerical claims independently** — ran the delivered
   script: the anchor identity reproduces cdot-7's fitted $a_0(0)$ to
   $0.3\%$; the $E(z_\text{lens})$ backbone matches. Both incorporated into
   the WP5 record along with the variational mechanism (checked for either
   natural choice of the background mode's spatial definition) and the
   unimodular-gravity precedent, which is apt and well-known not to
   introduce new local forces.

2. **Did the $m_\times$ inspection by consulting the primary source**
   (Mistele, arXiv:2305.07742) rather than reasoning from memory of either
   AeST's or cdot-8's action. Found $m_\times\equiv Q_0\sqrt{(2-K_B)/(2K_B)}$
   is built entirely from $K_B$ (the aether vector's own kinetic-term
   coefficient) and a fixed coupling constant the paper also calls $Q_0$ —
   with **no dependence on $J$ (AeST's free function, this program's
   $F(Q)$)** at all.

3. **Caught a notational collision before it caused a wrong conclusion**:
   Mistele's "$Q_0$" is a fixed action parameter, unrelated to this
   program's own $Q_0(t)$/$Q(t)$ (the cosmologically-evolving background
   invariant the census/M5 machinery is built around) — same symbol,
   different object.

4. **Concluded the pre-registered hypothesis does not survive**: cdot-8's
   charter modification is entirely within the scalar sector's free
   function — the one thing $m_\times$ is independent of. cdot-8 has not
   touched the aether's own kinetic term or the fixed $\phi$–$A$ coupling.
   The $m_\times$ ambiguity, and the weak-lensing tension it produces, very
   likely persists in cdot-8 exactly as in vanilla AeST — reported as the
   honest outcome of a hypothesis that was framed in advance as something
   to test, per this program's verdict-scoping discipline, not as a
   disappointing result to soften.

**Files produced:** updates to `Update-WP5-WeakFieldStructure-2026-07-17.md`
(§§5–7), this entry.

**Status: the decoupling argument and prediction backbone are confirmed and
recorded; the $m_\times$ hypothesis is tested and fails.** The two-
quasistatic-limit question is therefore *not* dissolved and remains open,
needing its own resolution before the lensing-RAR-vs-lens-redshift curve
can be built with confidence. The Foundation §6 item 6 decision (WP4a's
27% acoustic-scale miss) remains the standing gate, unaffected by WP5's
parallel progress. The KATRIN clock remains the program's most
time-critical item; nothing in `cdot-7/` was touched.

---

## Entry 3 — Advisor unbundles $m$ from $m_\times$: the tension attaches to the wrong parameter in Entry 2's conclusion (2026-07-17)

**Prompt (verbatim):**
> Updated.

(Reference: `Advisory-WP5-ScaleUnbundling-2026-07-17.md` + `meff_skeleton.py`
— advisor owns "advisor error #6": Entry 2's hypothesis framing, which the
advisor itself had proposed, wrongly bundled two distinct AeST parameters
under one conclusion.)

**Summary of work performed:**

1. **Did not accept the correction on the advisory's say-so** — re-fetched
   the primary source (arxiv.org/html/2305.07742) twice, independently:
   once to confirm the $m$-vs-$m_\times$ distinction itself, once to probe
   the advisory's specific counter-claim about $Q_0$.

2. **Confirmed by direct quote**: *"$m$ controls whether AeST reproduces
   MOND"* (the ghost-condensate mass — the term this program's charter
   already discards, since cdot-8 replaces AeST's free $F(Q)$/native scalar
   sector with the census/M5-determined one) is the parameter behind the
   known Mistele–McGaugh–Hossenfelder 2023 weak-lensing tension, **not**
   $m_\times$: *"in contrast to $m$, the new mass parameter $m_\times$... is
   not related to the ghost condensate... does not affect the ability of
   AeST to reproduce MOND."* Entry 2's closing sentence — attributing the
   known tension to $m_\times$ — was wrong. $m_\times$ genuinely produces no
   lensing tension; it only matters for wide binaries, per the source's own
   conclusion.

3. **Checked, but could not confirm, the advisory's specific $Q_0$
   counter-claim** — that Mistele's $Q_0$ is literally the same object as
   this program's own $Q(t)$/$Q_0(t)$. Second re-fetch found the paper
   introduces $Q_0$ as a bare action constant without deriving it from a
   background solution in the passages accessible. Recorded as a genuinely
   open point, not resolved either way — Entry 2's "different object"
   framing was likely too strong, but the advisory's specific identification
   isn't independently confirmed either.

4. **Reproduced `meff_skeleton.py` exactly** by running it myself:
   $F_{QQ}(Q_0{=}1,\text{today})=-0.696$ ($H_0^2$ units, closed-form check
   $F/\Omega_s=+1.819$ vs target $+1.765$), $m_\text{eff}\sim1.4\times
   10^{-4}\,\mathrm{Mpc}^{-1}$ ($1/m_\text{eff}\approx7300$ Mpc), $r_c\sim81$
   Mpc for a $10^{11}M_\odot$ lensing-stack galaxy — far beyond stacked-
   survey radii ($1$–$3$ Mpc), suggesting the condensate is negligible at
   all survey scales and MOND phenomenology persists.

5. **Did not yet attempt the assigned "careful" pass** — the skeleton is
   explicitly labeled a pre-registered estimate by both parties, not a
   verified normalization. Accepted the *qualitative* conclusion (Hubble-
   scale, not Mpc-scale, condensate mass — robust to normalization errors
   far smaller than the ~4 orders of magnitude that would matter) but
   flagged the *exact* numerical prefactor as unverified, since matching
   cdot-8's own $F(Q)$ convention to Mistele's $J/m^2$ convention is exactly
   the class of cross-frame computation both the advisor and I have erred
   in earlier this session (WP4b's normalization disputes).

**Files produced:** `Update-WP5-WeakFieldStructure-2026-07-17.md` §6b (new),
this entry.

**Attempted the assigned careful $m_\text{eff}$ pass immediately after —
partial, honestly incomplete (§6c of the same document).** Went back to
WP3's own validated action-level result ($p_\phi=F/8\pi\tilde G$,
$\rho_\phi=-(F-QF_Q)/8\pi\tilde G$) and confirmed the quadratic-in-$\delta
Q$ piece of cdot-8's action has the right *shape* to match AeST's $m^2$
term — the skeleton's ansatz is structurally sound. But could not
responsibly complete the actual matching: it needs (i) the explicit
$Y$-to-$Q$ field-redefinition map between Mistele's $J(Y)$ convention and
cdot-8's $F(Q)$ convention, (ii) the $f_G$ ($\tilde G\leftrightarrow\hat
G$) rescaling factor, not established anywhere in this program's own
documents, and (iii) a genuine resolution of whether $F_{QQ}<0$ signals a
real instability or is a convention artifact — none of which reduce to a
quick lookup; all require either the full second-order perturbed action
(substantial, dedicated derivation) or the advisor's own working, if they
have it. **Deliberately did not fabricate a number** given this is exactly
the cross-frame-normalization error class that has bitten both parties
already this session (WP4b). Recommending a touch point with the advisor
on the $f_G$/$J(Y)$ dictionary specifically, before attempting the full
derivation from scratch.

**Status: the $m$-vs-$m_\times$ correction is accepted and independently
verified; the two-quasistatic-limit question is now understood to be a
minor wide-binary footnote, not a WP5 blocker.** The sharper, zero-freedom
question — whether cdot-8's own $F(Q)$ generates an effective condensate
mass, and whether it sits at galactic or cosmological scales — has a
skeleton estimate (Hubble-scale, condensate negligible at survey radii,
consistent with MOND persisting) that is qualitatively credible but **not
yet carefully verified — the careful pass itself is not yet done**, only
attempted and found to need more than a quick follow-up. The Foundation §6
item 6 decision (WP4a's 27% miss) remains the standing gate. The KATRIN
clock remains the program's most time-critical item; nothing in `cdot-7/`
was touched.

---

## Entry 4 — The careful $m_\text{eff}$ pass, resolved exactly against the primary source (2026-07-17)

**Prompt (verbatim):**
> Updated.

(Reference: `Advisory-WP5-DictionaryDelivered-2026-07-17.md` +
`meff_exact_dictionary.py` — answers my Entry 3 stop/touch-point request
directly. Advisor located the actual source that resolves all three §6c
blockers: Skordis & Złośnik's companion stability paper, PRD 106, 104041
(arXiv:2109.13287), distinct from Mistele's paper.)

**Summary of work performed:**

1. **Did not accept the advisory on its own presentation** — fetched the
   primary source myself (via ar5iv) and checked every load-bearing claim
   individually, including the one item the advisor explicitly left for
   me to verify.

2. **Confirmed, verbatim, against the fetched text**: the $Q_0$
   characterization ("$\phi\to\bar\phi(t)$," "$\mathcal Q\to\bar{\mathcal
   Q}=\dot{\bar\phi}$," "$\mathcal K(\bar{\mathcal Q})$ has a minimum at
   $\mathcal Q_0$"); the free-function expansion (Eq. 10); the exact mass
   formula $\mu^2=2\mathcal K_2\mathcal Q_0^2/(2-K_B)$ (Eq. 58, not
   paraphrased); the stability condition $\mathcal K_2>0$ (Eq. 31); the
   Mpc observational bound (quoted verbatim); and quadratic-order
   sector-additivity (the $|\mathcal Y|^{3/2}$ term "do[es] not contribute
   to the second order action," quoted verbatim).

3. **Verified the one remaining item myself**: fetched SZ's own action
   (Eq. 1) and checked it against WP3's already-validated minisuperspace
   term — same prefactor $1/(16\pi\tilde G)$, same minus sign in front of
   $F$. The match the whole dictionary is conditional on holds.

4. **Checked the cross-paper consistency claim algebraically myself**
   rather than accepting it asserted: $M^2=(2-K_B)Q_0^2/K_B$ at
   $\lambda_s\to0$ equals $2m_\times^2$ in Mistele's notation exactly,
   confirmed by direct substitution.

5. **Reproduced `meff_exact_dictionary.py`** by running it: $\mu^{-1}
   \approx5$–$10$ Gpc, $r_c\approx64$–$100$ Mpc across AeST's stable
   $K_B$ range — three-plus orders of magnitude above AeST's hand-imposed
   Mpc requirement.

**Files produced:** `Update-WP5-WeakFieldStructure-2026-07-17.md` §6c
(rewritten, exact result; original honestly-incomplete version kept in a
collapsed note) and §7 (rewritten — was stale, still routed the RAR curve
behind the two-limit question), this entry.

**Status: the careful $m_\text{eff}$ pass is done, independently verified
against the primary source at every step — not just reproduced
numerically. All structural questions in WP5 are now closed.** The
skeleton's qualitative conclusion (condensate negligible at survey radii,
MOND persists, a genuine zero-freedom distinguishing feature from
hand-tuned AeST) is now the exact, verified conclusion. **The only
remaining WP5 deliverable is the lensing-RAR-vs-lens-redshift confrontation
itself** — nothing blocks it; next step. The Foundation §6 item 6 decision
(WP4a's 27% miss) remains the standing gate. The KATRIN clock remains the
program's most time-critical item; nothing in `cdot-7/` was touched.

---

## Entry 5 — First pass at the lensing-RAR confrontation: backbone cross-validated against cdot-7's own independent fit, literature gap found, statistical verdict not yet closed (2026-07-17)

**Prompt (verbatim):**
> Updated.

(No new advisory this round — proceeded to the assigned next deliverable,
the lensing-RAR-vs-lens-redshift curve, per Entry 4's status.)

**Summary of work performed:**

1. **Cross-validated the prediction backbone against cdot-7's own,
   pre-existing, independently-fitted $a_0(z)$ trajectory** — ran
   `Fable-1/a0_confrontation.py` (read-only, `cdot-7/` untouched) rather
   than trust the summarized figures I recalled. Initially misread the
   script's printed table (it prints absolute $a_0$ pre-multiplied by the
   1.2 SPARC anchor, not the bare ratio) and briefly suspected a large
   low-$z$ discrepancy — caught this before writing it up, recomputed the
   ratio function directly: $1.11$–$1.12$ at $z=0.25$ vs. WP5's $E(0.25)=
   1.161$ ($\sim4$–$5\%$ offset), converging to $1.82$–$1.85$ vs. $1.861$
   at $z=1.0$ ($\sim1$–$2\%$). **Genuine, new confirmation**: cdot-8's
   covariant backbone is quantitatively consistent with cdot-7's own
   SN+RAR+MIGHTEE+MUSE-DARK-fitted trajectory across $0<z<1$, not just at
   the $z=0$ anchor checked earlier.

2. **Fetched both anchor papers directly** (Brouwer et al. 2021,
   arXiv:2106.11677; Mistele et al. 2024, arXiv:2310.15248) rather than
   assume their structure from the advisory's citation. **Found neither
   paper bins its lens sample by redshift** — both pool $0.1<z<0.5$
   (mean $\approx0.2$–$0.25$) as one population, treating $a_0$ as
   universal. Mistele et al. quote $a_0=1.24\times10^{-10}$ m/s²
   uniformly; Brouwer et al. compare to McGaugh's canonical $1.2$ rather
   than fitting their own value. **The proposal's "by lens redshift"
   deliverable does not exist pre-made in the cited literature** — a real
   finding, reported rather than glossed over.

3. **Declined to assert a tension or a pass from a naive point comparison**
   at the anchors' mean $z$ — cdot-8 predicts $12$–$16\%$ growth by
   $z\sim0.2$–$0.25$ and neither paper's single number obviously shows it,
   but a real verdict needs the papers' own quoted uncertainties (not
   located this pass), the actual lens $n(z)$ weighting (a pooled
   measurement smears any trend — point-evaluation at mean $z$ isn't the
   real calculation), and a resolved zero-point convention (cdot-7's own
   record already documents $0.3$–$0.5\times10^{-10}$ cross-survey
   zero-point scatter as a known systematic, not new). Recording this
   honestly as unresolved rather than forcing a premature verdict —
   exactly the discipline that caught real errors earlier this session.

**Files produced:** `Update-WP5-WeakFieldStructure-2026-07-17.md` §8 (new),
this entry.

**Status: real progress, not yet a confrontation result.** Solid: the
prediction backbone is now cross-validated against cdot-7's own
independent, pre-cdot-8 fit; the literature gap (no z-binned lensing RAR
published yet) is itself a reportable finding. Still needed: papers'
quoted uncertainties, $n(z)$-weighted forward modeling, and zero-point
convention resolution, before a pass/tension verdict on the RAR
confrontation — scoped as the concrete next step, not rushed. The
Foundation §6 item 6 decision (WP4a's 27% miss) remains the standing gate.
The KATRIN clock remains the program's most time-critical item; nothing in
`cdot-7/` was touched.

---

## Entry 6 — WP5 closed: differential test design adjudicated and independently checked; one advisor misquote caught (2026-07-17)

**Reference:** `Advisory-WP5-ConfrontationDesign-2026-07-17.md` +
`rar_bin_test_design.py`. Adjudicated §8's restraint as correct: the
papers' own uncertainty floors (Mistele's $\approx0.1$ dex/$26\%$
stellar-mass-conversion band; Brouwer's missing-baryons degeneracy) are
common-mode with, and larger than, the 12–16% pooled signal — the pooled
literature genuinely cannot decide the question. Proposed the intra-survey
differential bin-ratio test as WP5's actual closing deliverable.

**Independent verification before accepting**: confirmed Mistele's 0.1 dex
figure verbatim from the primary source. **Did NOT confirm** the
advisory's attributed quote to Brouwer et al. — "the single most severe
limitation of our analysis" — searched the paper specifically for this or
an equivalent severity statement and found none; if anything, Brouwer et
al.'s own text downplays the missing-baryons severity ("likely moderate").
Recorded as a caught misquote (not repeated as a direct quote in the WP5
record), while noting it doesn't undermine the underlying point. The
$6\sigma$ early/late-type RAR split citation checked out exactly.
Reproduced `rar_bin_test_design.py`: KiDS-only tests are directional
($\sim1\sigma$); decisive tests need $z\sim0.6$–$1.0$ lens bins (DES/HSC-
deep/LSST/Euclid). Correctly scoped as testing "$a_0$ tracks $H(z)$" vs.
constant, not cdot-8's $E(z)$ shape vs. $\Lambda$CDM specifically.

**Files produced:** `Update-WP5-WeakFieldStructure-2026-07-17.md` §9
(new), this entry.

**WP5 IS NOW CLOSED**: (a) pre-registered prediction ($E(z_\text{lens})$
curve + theory band + $\sqrt E$ amplitude law); (b) demonstrated literature
gap; (c) differential test design with systematics budget and feasibility
ladder. A complete, falsifiable, registered-before-data deliverable.
**Two decision gates now stand, handed to the author, neither resolved by
this session**: (1) Foundation §6 item 6 — the WP4a 27% acoustic-scale
verdict, the long-standing gate; (2) WP5b scope — pursue the binned
lensing-catalog reanalysis in-program or as an external proposal (new
observational data-analysis work, outside this program's charter as
written). The KATRIN clock remains the program's most time-critical item;
nothing in `cdot-7/` was touched.

---

## Entry 7 — Note only: a candidate dataset flagged, WP5's closure unchanged (2026-07-18)

**Prompt:** user pointed to McGaugh, Mistele et al. 2026 (arXiv:2603.06479)
Table 1 — six GAMA-II/KiDS weak-lensing group bins, $z=0.117$–$0.324$,
with per-bin $V_f,M_b$. Checked the paper directly (not just the table):
an effective per-bin $a_0$ (via the paper's own BTFR normalization) rises
with $z$ at face value, but the bins are constructed by baryonic mass,
not redshift — the $z$-mass correlation is very plausibly a flux-limited-
selection artifact, not a controlled probe, and the paper doesn't address
this. **Added as §10 of the Update document, explicitly as a flagged
candidate dataset only** — not a clean, mass-controlled test, per the
user's instruction not to change or reopen anything. WP5's §9 closure and
both standing decision gates are unaffected.
