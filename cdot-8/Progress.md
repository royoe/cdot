# Progress — cdot-8: Work-Package Status and Current Open Items

*Companion to `Foundation.md` (the theory as it now stands). This
document is the status dashboard: what's passed, what's open, what's
next, and the decision-gate record — without the round-by-round history
that produced it. Prepared 2026-07-19 for onboarding a new advisor.*

---

## 1. Work-package status at a glance

| WP | Topic | Status | One-line result |
|---|---|---|---|
| WP0 | Literature verification | **Passed** | No fatal AeST pathology found (2024–2026); binary-pulsar/Cassini gaps identified as WP6 leads |
| WP1 | Dictionary as frame map | **Passed** | $c(t)=c_0(a/a_0)^{2/3}$ forced by the redshift law; two-clock dictionary resolves a latent WP3 tension |
| WP2 | Covariant census | **Passed** | $\mathcal N(t)$ defined as a foliation integral; evolution equation derived; reduces to cdot-7's $M_h$ |
| WP3 | Closure constraint (make-or-break) | **Passed** | M5 closes consistently; $F(\mathcal Q)$ fixed by quadrature; zero adjustable parameters intact |
| WP4a | CMB acoustic scale | **Open, unresolved** | $100\theta_*=1.326$ vs. Planck $1.04109\pm0.00030$ — 27% overshoot, localized to crossover-era $E(z)$ |
| WP4b | BBN | **Passed** | $H/H_\text{SBBN}=0.965$–$1.02$ across the BBN window; $Y_p\approx0.243$, within 1σ of observed |
| WP5 | Weak field, evolving $a_0$ | **Closed as delivered** | Prediction + literature gap + differential test design registered; no data confrontation attempted (author's choice, not required) |
| WP6 | Relativistic sector (tensor speed, PPN, Cassini) | **Mostly closed, one new open item** | Tensor speed exact; Cassini screening passes by orders of magnitude; PPN closed on a conservative envelope, not exactly; **new: $Q_2$/EFE tension, $\sim21\sigma$, unresolved** |
| WP7 | Perturbations/CMB structure | **Paused (Gate 4)** | Vector-sector growth system fully closed at $k=10^{-4}$ Mpc$^{-1}$; ISW-relevant $k$'s ($\ell=2$–$10$) show the fast mode never restabilizing, $\Phi$ growing 5–8 orders of magnitude — paused by author decision, not resolved |

## 2. The standing background-level caveat (Gate 1)

**WP4a's 27% $\theta_*$ miss is not resolved.** It is cleanly localized
(not $\Omega_b$, not BBN, not the distance convention or $z_*$ choice —
all independently audited) to cdot-8's own $E(z)$ in the crossover era
($z_*$ to a few$\times10^4$). Three readings were offered (soft miss
pending WP7; provisional structural failure; decisive kill); **the
author's ruling (2026-07-18) is (b) — provisional structural failure,
not a kill**, with an explicit sequencing instruction: complete WP6 and
WP7 on current assumptions first, revisit the background afterward.
**Every WP5/WP6/WP7 result since carries this caveat explicitly** — none
of them constitute an all-clear on the cosmological background.

## 3. Gate 2 (resolved, closed)

WP5's remaining scope question — pursue an actual redshift-binned
lensing-RAR data confrontation (WP5b), or close WP5 as delivered — was
resolved by the author as **(a): close WP5, no WP5b.** The stated reason:
the program's goal going forward is establishing falsifiable predictions
for *future* survey data, not reprocessing existing catalogs in-program.

## 4. Currently open items, in priority order

1. **WP4a's 27% miss** (Gate 1) — deferred by explicit instruction until
   after WP7; not forgotten, not resolved.
2. **WP7's growth/ISW numerical system — PAUSED, Gate 4 (author,
   2026-07-21)**, not resolved and not a kill. Stages 0–3g (units
   contract, field-variable rebuild, vector-sector fast-mode diagnosis,
   $\Pi$-normalization correction, and a fully analytic, machine-
   precision-validated full-system stability audit) were all completed
   and cross-checked — the vector sector's instability was fully
   understood and safely closed **at the single test wavenumber
   $k=10^{-4}\,\text{Mpc}^{-1}$** (pointwise algebraic slaving above
   $z\approx35$, explicit integration below). **Stage 4 (assembling the
   actual ISW estimate) then found this closure does not extend to the
   wavenumbers $\ell=2$–$10$ actually require** ($k\approx1.1$–$5.4
   \times10^{-3}\,\text{Mpc}^{-1}$): the vector sector's fast eigenvalue
   never crosses zero from $z=100$ to $z=0$ at these larger $k$'s
   (confirmed in the exact $6\times6$ Jacobian), giving $\Phi$ growth of
   $5$–$8$ orders of magnitude by $z=0$ — nowhere near a physical ISW
   source. Read (advisor, confirmed on reassessment) as a *continuation*
   of the already-accepted $c_\text{ad}^2<0$ tachyonic-clustering
   mechanism to larger $k$ (negative effective pressure destabilizes
   rather than stabilizes at smaller scales — the opposite of ordinary
   Jeans behavior), not an unrelated new pathology — though this doesn't
   reduce the practical severity. **Author decision: pause here** rather
   than run the AeST-native cross-check (does the founding paper's own
   tuned $K(Q)$ share this instability?) or continue toward a fuller
   Boltzmann-style calculation. See Gate 4 in `DecisionGates-2026-07-18.md`
   and `WP7/Update-WP7-PerturbationStructure-2026-07-18.md` §33–§43 for
   the full technical arc. **A matter-era clustering mechanism was
   identified along the way**: $\mu^2/H^2\approx-0.5$ (Hubble-tracking,
   negative — the same Jeans-class growing mode now shown to worsen at
   larger $k$), flipping to the stable sign near today.
3a. **Closed, 2026-07-20**: the $F_{QQ}(\mathcal Q_0,\text{today})$
   anchor correction (previously $-0.696$, cited in four places) is now
   **confirmed** at $\approx-0.169$ by an independent secondary-advisor
   re-derivation, cross-checked by the worker (three independent
   implementations agree). Propagated into `Foundation.md` §7/§8 and
   `Update-WP5-WeakFieldStructure-2026-07-17.md`'s condensate-mass band
   (now $\mu^{-1}\approx10$–$20$ Gpc, $r_c\approx100$–$160$ Mpc — the
   confirming advisory's own propagation used the wrong formula
   convention for this step and was corrected before use, see WP7 §29).
   Every qualitative conclusion survives; several strengthen.
3. **The $Q_2$/External-Field-Effect tension (WP6, found 2026-07-19)** —
   cdot-7's own preferred interpolating function/$a_0$ choice predicts a
   Solar-System quadrupole $\sim21\sigma$ beyond a recent (2026),
   carefully-validated Cassini/DE440 bound. This strikes a *program
   choice* (the IF fit), not the census-derived core. A constructive path
   exists (re-fit the IF as a sharpness-parameterized family, using both
   this bound and an earlier, already-known $24$–$41\%$ Cassini-safety
   exposure as joint likelihood terms). **Sequencing decided (author,
   2026-07-20, Gate 3): postponed until after WP7**, on the same logic as
   Gate 1(b) — the finding stands, only the timing of any re-fit is
   deferred. See §4b's post-WP7 queue.
4. **WP6 sub-task 2's exact PPN closure** — $\alpha_1,\alpha_2$ are
   currently bounded by a conservative envelope ($|\alpha_1|\le4\mathcal
   K_B$), not computed exactly. A second, provisional $\alpha_2$-based
   envelope ($\mathcal K_B\lesssim4\times10^{-10}$) exists but rests on
   a solar-spin bound that may itself be $\sim100\times$ too tight — not
   to be used until verified. Explicitly flagged as future work, not
   abandoned; does not block anything currently in progress. Note for
   calibration: every established cdot-8 structure survives the
   $\mathcal K_B\to0$ limit smoothly — this squeeze is not an existential
   threat.
5. **The census-sector covariant completion, a named open item family**
   — several related, not-yet-resolved questions about how the
   horizon-ball census domain covariantizes at the perturbative level
   (gauge status; fiducial-center/translation invariance; the volume-
   normalization convention relating the minisuperspace action to the
   ball; and a fourth facet, normalization locality — $E_P$ per-slice vs.
   ball-smoothed local $c$, with per-slice as the declared default).
   Bounded, not open-ended: pinned by two exact physical anchors (the
   $k\to0$ separate-universe identity; the sub-horizon recovery to WP6's
   own $-F_Q$) plus a third untouchable (the matter census is *exactly*
   immune, $p_m=5/2$ cancellation — this freedom touches only
   radiation-class coefficients). Not closed, but not feared either.

## 4a. External clocks — measurements that will adjudicate this program regardless of its own progress

- **KATRIN (neutrino mass), the sharper and nearer-term of the two.**
  The census closure's $\Sigma m_\nu=1.374$ eV implies $m_\beta\approx
  0.458$ eV. KATRIN's partial-data bound is $m_\beta<0.45$ eV (90% CL);
  data-taking ended in 2025; the final analysis (sensitivity $<0.3$ eV)
  is pending. **Registered criterion**: a detection near $0.46$ eV is
  required for the census closure as currently fitted; a null result
  excludes it decisively. Note the alignment with item 1 above: WP4a's
  own named post-WP7 revisit lever is a low-$\Sigma m_\nu$ re-closure —
  KATRIN will adjudicate that lever's viability before this program
  reaches it.
- **The $Q_2$/EFE bound** (item 3 above) is the second such clock, and
  unlike KATRIN it has already landed — the measurement is published,
  only the program's response to it is pending.

## 4b. The post-WP7 revisit queue, consolidated

Three items currently live in separate places in the record; collected
here as the single list a recruit planning ahead should work from:

1. **Interpolating-function re-fit** (item 3's constructive path) — Simple
   IF replaced by a sharpness-parameterized family, fit jointly with the
   $Q_2$ bound and the T22 Cassini exposure; conditioned on a genuinely
   *author*-level question (whether a single-$\mu$ "economy" is worth
   trading for fit freedom). **Sequencing decided (2026-07-20, Gate 3):
   postponed until after WP7**, same logic as Gate 1(b).
2. **Low-$\Sigma m_\nu$ re-closure** (WP4a's own named lever for its 27%
   miss) — KATRIN-aligned; KATRIN's final result will bear directly on
   whether this lever is viable at all.
3. **Radiation-era assumption revisiting** (Gate 1(b)'s own deferred
   scope) — explicitly not dropped, deferred until after WP7 by the
   author's own instruction.

## 5. What's *not* open — established, load-bearing results a new advisor can build on

- The full background cosmology (WP1–WP3): the dictionary, the census,
  and the closure constraint all close consistently, with the "zero
  adjustable parameters" claim intact and independently checked several
  times over.
- BBN passes; the SN diagram (cdot-7, unaffected) passes.
- WP5's weak-field sector: the local/cosmological decoupling argument,
  the evolving-$a_0(z)$ prediction, and the condensate-mass
  negligibility result are all solid, independently verified, and not
  contested by anything discovered since.
- WP6's tensor-speed exactness and the (screened) Cassini bound are
  solid.
- WP7's $\Omega_s$-clusters-dust-like conclusion is now a settled
  structural result (three independent lines of argument converge:
  the corrected sound speed, the energy budget, and AeST's own design
  intent), not an open question — it was contested and resolved within
  this same work package (see §6).

## 6. Methodology note for a new advisor

This program runs a strict **verify-before-trust** discipline in both
directions: every advisor-delivered claim is independently re-run/
re-derived before being accepted, and every worker-side derivation is
expected to be checked the same way. Over the program's history this has
caught roughly a dozen substantive errors on each side (sign flips,
dictionary-transplant errors — using a formula validated for one
theory's $(\rho,P)(\mathcal Q)$ map on a different, structurally distinct
map — convention mismatches, scoping over-reaches), essentially all
caught by this same discipline rather than by luck. The single most
useful habit to carry forward: when a "kill" or a serious problem is
found, it gets **escalated, not decided unilaterally** — of the several
serious-looking crises this program has hit (a 13× energy-budget
shortfall, an apparent constraint back-reaction with no obvious fix, the
WP4a miss itself), every one *except* WP4a's has dissolved on closer
joint examination into a corrected setup rather than a real kill. WP4a's
own miss is the first that has not yet dissolved this way — which is
part of why it's being treated with real caution rather than assumed
away.

A full, granular error tally and a library of named methodology rules
("K6") are kept in `proposal/ErrataAndMethodologyLog-2026-07-18.md`, for
reference rather than as required reading.

## 7. Where to find things

- `Foundation.md` — the theory as it currently stands, written as a
  physics document (start here for the science).
- `proposal/Proposal-cdot8-CovariantCompletion-2026-07-11.md` — the
  original charter, design constraints, and kill conditions (still the
  authoritative statement of what would end the program).
- `proposal/DecisionGates-2026-07-18.md` — the full record of Gates 1
  and 2 as they were put to the author, with options and reasoning.
- `ConsolidationLog-2026-07-12.md` — findings relevant to cdot-7 itself,
  harvested from cdot-8 work, routed here rather than edited directly
  into cdot-7. Includes Item 16, the $Q_2$ tension.
- `proposal/ErrataAndMethodologyLog-2026-07-18.md` — the error tally and
  methodology-rule library.
- Per-WP directories (`WP0/` through `WP7/`) — the full derivation
  record, `Update-*.md` files for the technical detail, `SessionLog-*.md`
  for the round-by-round history, `advisory/` subfolders for
  advisor-delivered material. Not required reading for onboarding, but
  the ground truth if a specific claim in `Foundation.md` needs tracing
  back to its derivation.
