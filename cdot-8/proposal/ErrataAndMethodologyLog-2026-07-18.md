# Errata, Methodology (K6), and Jointly-Verified Results Log — cdot-8 (2026-07-18)

*Companion to `cdot-8/ConsolidationLog-2026-07-12.md`, which tracks
cdot-7-portable findings only. This log tracks what's specific to
cdot-8/AeST itself: the accumulated methodology rules ("K6" pattern
library, referenced repeatedly across WP3–WP6 advisories without a
consolidated home until now), the full error tally (both sides, this
session), and the AeST-specific results both worker and advisor have
independently confirmed and should be treated as established program
facts going forward. Requested across at least three consecutive
advisory rounds (WP6 ScaleUnbundling, DictionaryDelivered,
ForkResolved); delivered here.*

---

## 1. The K6 methodology pattern library

Rules this program has learned the hard way, named so they don't need
re-deriving from a fresh mistake each time:

1. **Verify the solution is the physical one before verifying algebra on
   it.** Idealized fixed points and actual fitted trajectories can both
   satisfy the same equations while giving different answers to a
   confrontation question — WP3's recurring trap (see
   `ConsolidationLog-2026-07-12.md` Item 11).
2. **A sign flip found in one place does not generally propagate as a
   simple shortcut everywhere downstream** — each dependent number needs
   its own check (WP3's scheme-dependence/sign-errata rounds).
3. **Verdict-scoping**: a round's conclusion must not exceed what the
   specific test actually showed — "WP3 closes positive" was retracted
   for over-reaching this way, not for being numerically wrong.
4. **Inherited-conventions**: before applying someone else's formula in a
   new context, check its underlying normalization/assumptions — the
   $m_\times$ bundling error, the Foster-Jacobson $c_i$ mapping, and the
   Mistele-vs-cdot-8 $Q_0$ question are all instances of this.
5. **Don't badge a task as "quick" or "cheap" by inherited framing** — the
   original proposal called WP4a "immediate/cheap"; it required a full
   first-principles resolution of two historically-unsettled conventions.
6. **Loose-thread hygiene**: state explicitly what remains open when a
   round closes, rather than letting it quietly drop.
7. **Absolute-anchor rule**: every confrontation ratio needs at least one
   absolutely-known external anchor, verified inline — not just internal/
   relative consistency.
8. **Bundled-scales rule**: don't conflate two physically-distinct
   parameters under one hypothesis — the $m$-vs-$m_\times$ episode is the
   named example (advisor error, owned as such).
9. **A "quantity must equal 1/X at some reference point" sanity check is
   only valid once you've confirmed what's actually being compared
   decomposes into** — the $z=0$ category-error episode (see
   `ConsolidationLog` Item 15).
10. **Presentation-gap rule**: before comparing printed numbers, confirm
    whether a script is printing an absolute quantity or a ratio, and
    whether it's already multiplied by a normalization constant — caught
    twice this session (the re-derivation script's missing `u00` division;
    the worker's own initial misreading of the $a_0$-confrontation table).
11. **Version-provenance rule** (new, this round): when quoting a specific
    sentence from a paper as evidence, state which version was checked
    (arXiv preprint vs. published journal version) — text can differ
    between them, and an unresolved disagreement over a quote should be
    stated as "checked version X, not found" rather than asserted as a
    flat contradiction of the other party's claim.
12. **Convention re-derivation rule** (new, WP7): a normalization/
    convention factor (e.g. what a variable like $s$ actually means) gets
    re-derived from the defining document at first use in *every* new
    script — never copied from a prior script, including one's own. This
    is how one worker-side bug ($R_h(s)$'s exponent) survived three
    rounds: the advisor's own "independent" reproduction copied the same
    convention reading instead of re-deriving it, while a *different*
    script by the same advisor used the correct convention elsewhere,
    unreconciled.
13. **Dictionary-transplant rule** (new, WP7): a formula validated against
    one theory's specific $(\rho,P)(Q)$ (or equivalent) map certifies it
    for *that map only* — applying it to a different theory with a
    structurally different map is not licensed by the formula's own
    invariance under overall rescaling ($K\to cK$), since a different map
    is not merely a rescaling. Check the actual coefficient ratios before
    reusing a validated formula across theories, even closely related
    ones.
14. **Domain-boundary derivative rule** (new, WP7 Stage 1): a numerical
    derivative evaluated at the literal edge of a solved ODE's domain is
    unreliable regardless of how it's computed (finite difference,
    spline, or analytic formula fed boundary-only data) — different
    methods can disagree, including in sign. Fix at the root by
    extending the integration slightly past the point of interest so it
    becomes a genuine interior point, then cross-check at least two
    differentiation methods on the extended domain, rather than trusting
    reproducibility of the same method across scripts as independent
    verification.

## 1a. A significant, previously-unnoticed anchor correction found while building Stage 1 (WP7, 2026-07-19)

$F_{QQ}(\mathcal Q_0,\text{today})=-0.696$ — cited in three places
(WP5's condensate mass; the SZ stability check; WP7 §27's tachyonic-mass
finding) — is a **domain-boundary numerical artifact**, not a robust
result: it was computed at $s=0$, the literal edge of the ODE's solved
domain, and reproduced identically by the *same* differentiation method
in a second script (`meff_skeleton.py`), which is reproducibility of a
shared artifact, not independent verification. Self-caught while
building a robust $F_{QQ}(z)$ for Stage 1 (`Update-WP7-
PerturbationStructure-2026-07-18.md` §28): extending the ODE integration
slightly past $s=0$ so it becomes a genuine interior point, three
independent differentiation methods agree closely on
**$F_{QQ}(0)\approx-0.17$** (not $-0.696$) — roughly a factor of 4
smaller in magnitude, same sign. **Every qualitative conclusion built on
the old value appears to survive** (SZ stability still satisfied;
WP5's condensate negligibility likely strengthens, since smaller
$|F_{QQ}|$ gives an even larger Compton wavelength) — but the specific
numbers in WP5 and Foundation.md need recomputing and are flagged
provisional pending that. Not yet propagated into those documents;
recommended for explicit advisor review first, per the K14 rule above.

**CONFIRMED, 2026-07-20** (`Advisory-WP7-FQQCorrectionConfirmed-2026-07-20.md`,
secondary advisor, cross-checked by the worker before accepting): three
independent implementations now agree, $F_{QQ}(0)\approx-0.169$. One
detail in the confirming advisory's own propagation needed a fix before
use — its condensate-mass recomputation used `meff_skeleton.py`'s
simplified formula (implicitly fixing $\mathcal K_B=1$) rather than the
$\mathcal K_B$-range scan (`meff_exact_dictionary.py`) that produced
WP5's actually-quoted band; recomputed correctly, the update is
$\mu^{-1}\approx10$–$20$ Gpc, $r_c\approx100$–$160$ Mpc (not the
single-point figures the advisory quoted). Propagated into
`Foundation.md` §7/§8 and `Update-WP5-WeakFieldStructure-2026-07-17.md`.
K14 status: **confirmed**, not just proposed.

## 2. Error tally, both sides, this session (descriptive, not a strict global count)

**Advisor-side, confirmed:**
- Early $\dot s$-normalization slip (WP3).
- A sign flip in $F/\Omega_s$ ($-30/17$ reported as $+30/17$).
- An underjustified uniqueness claim on $g_i$'s lapse placement (WP3).
- "WP3 closes positive" — a verdict-scoping over-reach, retracted.
- A script/prose mismatch with a false residual claim (WP3 NoLapse round).
- The $m_\times$/$m$ bundling error ("advisor error #6" in the WP5 record)
  — the tested hypothesis conflated two distinct AeST parameters.
- WP4b re-derivation script: a missing division by `u00` inflated the
  reference-side numbers by $\sqrt{u_{00}}$.
- WP7 "advisor error #7": the §3 claim "$\Lambda_M$ is extensive over the
  fiducial ball, hence $\Lambda_M/V_\text{ball}=F_Q$-density" silently
  identified $\Lambda_M$'s minisuperspace $a^3$ with $\mathcal N_\text{tot}$'s
  horizon-ball volume $(4\pi/3)R_h(t)^3$ — two objects built by different
  routes, never shown to track each other. Worker-caught via
  `wp7_lambda_extensivity_check.py` before the coefficient was used for
  anything; conceded in full
  (`Advisory-WP7-CovariantizationFreedom-2026-07-18.md`). What survived:
  two independently-established physical anchors (§6's exact $k\to0$
  result; WP5's local decoupling) still pin the term's asymptotics
  regardless of the convention — only the detailed crossover shape was
  demoted to a stated, bounded freedom.
- WP7 "advisor error #8": the illustrative "$kR_h\sim6$ at the first
  acoustic peak" table entry (`wp7_structure.py` Part A, originating in
  `Advisory-WP7-FirstInstallment-2026-07-18.md`, then propagated without
  re-derivation in `Advisory-WP7-QDefinitionAdjudicated-2026-07-18.md`)
  imported a $\Lambda$CDM comoving-horizon-scale value into cdot-8's own
  variable-$c$ trajectory without ever computing cdot-8's actual $R_h(z)$.
  Worker-caught via `wp7_anchor_brackets.py`: $R_h(z_*)=3.3\times10^{-3}$
  Mpc against WP4a's own $r_s(z_*)=173.4$ Mpc, $D_p(z_*)=13074$ Mpc — off
  by four to six orders of magnitude, since $c(t)\propto(a/a_0)^{2/3}\to0$
  in the deep past makes early causal balls far smaller than a standard
  (constant-$c$) particle horizon. Conceded in full
  (`Advisory-WP7-PhenomenologyMapInverted-2026-07-19.md`); the corrected
  picture *relocates* the low-$\ell$ signature (to the coupled-era growth
  history and a late-time $\ell\lesssim10$ remnant) rather than erasing it.
  **Both #7 and #8 were caught by the worker running the literal,
  already-established definitions against numbers the advisor had
  asserted — in consecutive rounds, on the advisor's own side — direct
  evidence the verify-both-directions discipline is working
  bidirectionally, not just advisor-checks-worker.**
- WP4b: two flagged bugs in the worker's own first-pass script (the
  $e^\pm$/photon ratio off by a factor of 2; post-annihilation neutrino
  scaling applied at all $z$) — these were advisor-caught corrections to
  the *worker's* code, listed here for completeness of the record, not as
  advisor errors.

**Advisor-side, disputed, NOT confirmed as an error (worker holds
position after independent re-check):** the claim that a specific severity
quote ("the single most severe limitation of our analysis") appears in
Brouwer et al. 2021's published A&A version. Checked three times by the
worker (arXiv via ar5iv twice, and the publisher's own aanda.org page
directly) — not found in any version accessed. Per the version-provenance
rule (§1 item 11): this is recorded as "not found in the versions the
worker could access," not as a settled contradiction of the advisor's
claim, since the worker cannot rule out a version-dependent discrepancy
they simply couldn't reach. Status: **open, low-stakes** (the underlying
substantive point — missing baryons as a real, common-mode systematic —
is agreed by both sides regardless).

**Worker-side, confirmed (self-caught before use, or caught by advisor and
conceded):**
- WP4a: an uncontrolled, direct $\Omega_b$ comparison (should have been a
  controlled swap experiment) — conceded after the advisor's swap
  experiment and the worker's own reproduction of it.
- WP4b: first $e^\pm$ attempt used the frozen/decoupled (neutrino-style)
  distribution instead of the true-equilibrium form — self-caught via the
  sign of the numerical trend before being used.
- WP4b: naive coordinate-energy conservation for the photon-temperature
  boost (giving the wrong exponent) — self-caught before use.
- WP4b: the "severe rebuttal" episode — a $z=0$-must-equal-1 category
  error, then a follow-up constant-$g_*$ error in the "absolute anchor"
  check — both explicitly conceded in
  `WP4b/Update-WP4b-RebuttalWithdrawn-2026-07-17.md`.
- WP6: $J^\mu$ initially mischaracterized as a scalar current rather than
  the aether's own acceleration vector — caught via direct primary-source
  verification before it propagated further than §1/§2a.
- WP7: a **dictionary-transplant error** (§22 Part 2 of
  `Update-WP7-PerturbationStructure-2026-07-18.md`, corrected in §23).
  Validated $c_\text{ad}^2=F_Q/(QF_{QQ})$ symbolically against AeST's own
  published closed-form $(\rho,P)=(QK_Q-K,\,K)$ map (a genuine, correct
  validation, still standing) — then applied the *same* formula to
  cdot-8's own $F(Q)$ trajectory, silently assuming it shared the same
  underlying $(\rho,P)(Q)$ structure up to an overall rescaling. It
  doesn't: cdot-8's own established $\rho_s=\tfrac12QF_Q-\tfrac13F$ has
  coefficient ratio $-3/2$ on $\{QF_Q,F\}$, against AeST's own $-1$ (via
  $K=-\tfrac12F$) — not proportional, confirmed symbolically. "Invariant
  under $K\to cK$" was true and irrelevant: the transplant changed the
  map, not the scale. Advisor-caught (`Advisory-WP7-
  OmegaSClusteringAdjudicated-2026-07-19.md`), independently reproduced
  and confirmed before accepting. **Consequence**: the correct,
  map-independent computation ($c_\text{ad}^2=w+(dw/ds)/(d\ln\rho_s/ds)$,
  using cdot-8's own already-validated $w(a),\rho_s(a)$ directly) gives
  $c_\text{ad}^2=O(-0.01\text{ to }-0.04)$ through the matter era —
  *small*, the opposite conclusion from the transplanted formula's
  $O(1$–$1.5)$. This inverted §21/§22's "smooth quintessence"
  de-escalation: $\Omega_s$ clusters, dust-like, through the matter era.
  **K6-class lesson**: a formula's validation certifies it for the
  specific $(\rho,P)(Q)$ map it was validated on; transplanting to a
  theory with a different map needs re-derivation, not reuse — even when
  the formula "looks" scale-invariant.
- WP6 sub-task 1: an initial wrong asymptotic formula for the naked-simple
  $\mu$'s Saturn anomaly (modeled as power-law-suppressed rather than
  constant) — self-caught by re-deriving against `cdot-4/T22`'s own exact
  quoted asymptote before trusting the comparison.
- WP7: `wp7_lambda_extensivity_check.py`'s $R_h(s)$ integration used
  $dR_h/ds\propto e^{(2/3)s}$, correct only if $s\equiv\ln(a/a_0)$ — but
  WP2's own record fixes $s\equiv\ln(c/c_0)$, under which $c/c_0=e^s$
  by definition and $dR_h/ds=\tfrac32(c_0/H_0)e^s/E(s)$. Self-caught
  while building the coupled-era growth equation (§18 of
  `Update-WP7-PerturbationStructure-2026-07-18.md`), by re-deriving the
  formula from WP2's own $s\equiv\ln(c/c_0)$ definition before extending
  the script, rather than trusting the inherited exponent. **Notably,
  this bug was reused unchanged across three rounds — the worker's own
  §12/§16, and the advisor's §13/§17 reproductions
  (`covariantization_adjudication.py`, `wp7_phenomenology_map.py`) —
  without either side re-deriving it from the primary definition until
  now.** Consequence checked directly: numerical shifts of $O(1)$
  (e.g. $R_h(z_*)$: $3.3\times10^{-3}\to9.5\times10^{-4}$ Mpc), but every
  qualitative conclusion built on the old numbers (errors #7, #8; the
  mode-exit/growth-history reframing) survives unchanged.

**Pattern, stated plainly**: every error on both sides this session was
caught before being used to make a final, unqualified claim — either by
the other party's independent check, or by the same party's own
self-verification against an established result. This is the discipline
this program has run on throughout; the tally exists to make it visible,
not to keep score.

## 3. AeST-specific results both parties have independently confirmed — established program facts

These are not cdot-7-portable (they depend on AeST's field content) but
are now solid, cross-verified program results, not open questions:

- **The condensate/effective-mass dictionary**: $\mu^2=2\mathcal K_2
  \mathcal Q_0^2/(2-K_B)=-\mathcal Q_0^2F_{QQ}(\mathcal Q_0)/(2(2-K_B))$
  (Skordis-Złośnik PRD 106, 104041, Eq. 58), giving cdot-8 $\mu^{-1}
  \approx5$–$10$ Gpc, $r_c\approx64$–$100$ Mpc — a genuine, zero-freedom
  distinguishing feature from vanilla AeST's hand-tuned Mpc-scale $\mu$.
- **$Q_0$ identification**: Mistele's (and SZ's) $Q_0$ is the frozen
  cosmological background value of $\dot\phi$ — the same object cdot-8
  evolves as $Q(t)$ — confirmed verbatim from the companion stability
  paper (three independent quotes), closing the notational-collision
  question raised in WP5 §6b.
- **The $\mathcal Y$-sector charter scope statement**: cdot-8's "zero
  adjustable elements" claim is a $Q$-sector-only claim. The $\mathcal
  Y$-sector (MOND interpolation shape, high-gradient screening/tracking
  completion) is, and remains, AeST-inherited functional freedom — the
  background quadrature has zero support on $\mathcal Y$ (which vanishes
  identically on the homogeneous background), so this is not a gap to be
  closed, it's a category the zero-freedom claim was never about.
  **Recommended for the charter document itself**, stated proactively.
- **The single-$\mu$ economy-vs-freedom question**: cdot-7's historical
  "AQUAL economy" (one interpolating function for both cosmological
  closure and galaxy/solar-system physics) is a choice, not a structural
  necessity, in cdot-8's actual covariant construction — the $Q$-sector
  (closure) and $\mathcal Y$-sector (galaxy/solar-system) are formally
  distinct objects. Whether to keep them unified is **explicitly an open
  author question**, routed to the Gate-1 post-WP7 revisit, not decided
  by default in either direction.
- **One design fact, two faces**: AeST's Maxwell-only aether kinetic term
  simultaneously gives $c_{13}=0$ (exact $c_\text{gw}=c_\gamma$, "in all
  situations") and $c_{123}=0$ (the aether's own spin-0 mode is
  non-dynamical) — confirmed independently by the worker via direct
  primary-source fetches and symbolic (sympy) checks, not just asserted.
  This is *why* $\phi$ exists in AeST at all, and why WP6's PPN
  singularity is a truncation artifact (see the fork-resolution episode,
  §5c of `WP6/Update-WP6-TensorSpeedStructure-2026-07-18.md`) rather than
  a defect in AeST itself.

## 4. Small housekeeping items, closed here

- **Log-numbering convention, clarified rather than reconciled**: this
  program runs two intentionally-independent numbering streams — each
  `cdot-8/WPn/SessionLog-*.md` numbers its own entries from 1 within that
  file, and the shared `cdot-8/proposal/SessionLog-*.md` numbers its own
  entries from 1 within each day's file. These are not meant to align by
  entry number; cross-references between the two streams should cite by
  date + filename + section, not by bare entry number. No file needs
  renumbering.
- **07-16 overwrite note**: already present and explicit in
  `WP4b/SessionLog-2026-07-16.md`'s own header — no further action needed.
- **WP4b file sighting**: `WP4b/Update-WP4b-RebuttalWithdrawn-2026-07-17.md`
  is present in the repository (written 2026-07-17, confirmed on disk);
  the advisor loop's own next sync will pick it up.

**Status**: consolidation/errata batch delivered, closing the item
requested across the WP6 ScaleUnbundling, DictionaryDelivered, and
ForkResolved rounds. `ConsolidationLog-2026-07-12.md` Items 11–15 (the
cdot-7-portable subset) delivered alongside this file in the same pass.
