# CdotRecommendations.md — External Review Advice for cdot-7

*Prepared 2026-07-08 by Claude (external reviewer role), for consolidation into the
cdot-7 project. Reflects the state of `Foundation.md` and `ResearchNotes.md` as of the
four-term fit (§14) and the first M-σ discriminating test (§15). Advice is ordered by
how much each item could change the project's headline conclusions. Reviewer caveat:
several load-bearing external anchors (MUSE-DARK III, MIGHTEE-HI, current KATRIN
status, DESI evolving-DE fits) are at or past the reviewer's knowledge cutoff (end of
Jan 2026) and were not independently verifiable — items flagged accordingly.*

---

## 1. Overall Assessment

The project's epistemic hygiene is well above the norm for its genre and has held up
under pressure: adopted-vs-derived flagging at point of use, dead ends recorded to
prevent retries, bugs documented rather than erased, sub-session results independently
re-derived before merging, pipelines validated against published results before being
trusted (Pantheon+ SN-only reproduced to a third of a sigma; the four-term fit's
3/2-vs-2/3 coefficient bug caught by the required back-validation step working exactly
as designed). This process quality is itself a publication asset.

The strongest substantive results, in the reviewer's view:

1. **The Planck-unit invariance principle** (Foundation §3) — a genuine conceptual
   tightening that answers the standard Ellis–Uzan "varying c is dimensionally
   meaningless" objection by relocating all physical content into dimensionless
   invariance plus the single portal a₀ = λċ. It unifies two previously independent
   postulates and retro-explains the exact LLR cancellation and the exactly-standard
   SN candle.
2. **The exact EdS correspondence of the photon sector** (§5.5) — explains in one
   stroke why the framework passes the tired-light executioners (distance duality,
   Tolman dimming, time dilation, FIRAS), and constitutes most of the classical-frame
   dictionary (see §3 below).
3. **The instability-as-Λ mechanism jointly fit to real data** — the rigid,
   few-parameter coupling between the SN expansion history and the a₀(z) evolution is
   the framework's best card: ΔχSN² ≈ +2.0 vs ΛCDM, with the same parameters
   describing the measured a₀(z) evolution far better than either constant-a₀ MOND
   (excluded by the detected evolution) or a free linear law.

The project has progressed from "decisive test specified but not run" to "decisive
test run once, survived at the edge, with remaining fragilities precisely quantified."
The main concern was not so much alleviated as **converted**: from an internal
factor-of-~2.5 mass discrepancy into an external, laboratory-adjudicated bet
(Σmν ≈ 1.37 eV at the KATRIN edge) with an expiry date. That is a better class of
problem, and a more publishable one.

---

## 2. The Four-Term Fit — Precise Characterization (do not let later edits soften this)

The mass census closes at χ²_mass = 0.06, which is striking — but only by placing
Σmν = 1.374 eV, slightly *past* KATRIN's 90% CL edge. Three consequences to keep
explicit in any write-up:

- **Physical reading.** This is three quasi-degenerate neutrinos at ~0.46 eV each,
  making neutrinos roughly 40% of the framework's total matter budget — a
  hot-dark-matter-adjacent cosmology in classical-frame language. A referee will say
  "this is dark matter, just hot dark matter at the laboratory limit." Foundation §0's
  conditional wording should preempt that exact phrasing rather than let a referee
  coin it.
- **The historical exposure.** HDM cosmologies died on structure formation
  (free-streaming erasure of small-scale power). The framework's missing
  perturbation sector formally protects it from that test but reads as the deferred
  sector hiding precisely the question this solution most needs answered. State this
  proactively.
- **The tension synthesis (belongs somewhere explicit as one sentence):** *the mass
  census and the local RAR now pull the same parameter in opposite directions, and
  the fitted neutrino value is partly an artifact of where that tug-of-war settles.*
  The mass term rewards higher a₀ (ρ₀ ∝ a₀²); RAR alone prefers a₀ ≈ 1.26×10⁻¹⁰
  vs the joint 1.39×10⁻¹⁰ (Δχ² ≈ 7–13). The RAR-vs-rest tension is the legitimate
  successor to "sharpest current internal tension." The per-galaxy RAR covariance
  (replacing the ÷17.6 downweighting) is not bookkeeping — it directly sets how hard
  RAR is allowed to pull, and therefore where Σmν lands.

**Highest-value single computation remaining: the MCMC posterior on
(ε₀, κλ, λ, Σmν).** Σmν = 1.374 eV means nothing citable without an interval, and the
overlap of that posterior with the shrinking KATRIN allowance is the entire viability
question for the "no dark matter" claim. This ranks above everything else in
Foundation §6 item 1 because it could retire the framework's central claim cheaply.

---

## 3. The Classical-Frame Presentation (recommended primary framing for publication)

The frames are related by a Dicke-style units rescaling, verified observable by
observable (do **not** claim a full conformal equivalence — without a relativistic
completion there is no metric on either side to transform; present it as a units
transformation demonstrated sector by sector, an IOU alongside §6 item 7).

**Dictionary:** a(t) ∝ c(t)^(3/2); proper time dτ ∝ (c/c₀)^(5/2)dt; R_h ↔ the FRW
particle horizon (fixed-point D_p(∞) = 2c/H₀ is EdS's particle horizon exactly);
conserved wavenumber ↔ standard cosmological redshift; fixed point ↔ EdS
(a ∝ τ^(2/3), q₀ = +1/2); finite-future coordinate singularity ↔ ordinary asymptotic
de Sitter phase; a₀ = λċ ↔ a₀(t) = (2λ/3)·cH(t).

**Surviving physical content, classically stated:**

1. A flat FRW universe containing only ordinary matter (Ω ≈ 0.10–0.13 at fit values)
   — no CDM, no Λ.
2. The Friedmann constraint replaced by an AQUAL condition at the particle horizon:
   μ(g_h/a₀)g_h = GM_h/d_p², c² = κ g_h d_p. On EdS, d_p = 2c/H gives g_h = cH/2κ and
   x = 3/(4κλ) automatically constant — transparently why EdS is the scale-free
   solution — with the horizon condition fixing Ω_* = μ(x_*)/2κ: the MONDian boost
   (μ < 1) at the horizon lets ~0.1 of critical density drive an expansion that in GR
   would require Ω_m = 1. This is a *sharper* narrative than the static-frame one.
3. a₀(t) = (2λ/3)cH(t): the Milgrom coincidence a₀ ≈ cH₀/2π promoted from numerology
   to a dynamical law. This places the work in the friendly Milgrom a₀ ~ cH₀
   literature rather than the hostile varying-c literature.
4. Dark energy as an instability of the EdS solution, not a substance. The effective
   ρ_x(z) ≡ 3H²/8πG − ρ_m grows in time → transient phantom, w < −1 approaching −1
   from below. Distinctive and decidable vs Λ (w = −1 exactly) and thawing
   quintessence (w > −1). Compare at the level of H(z) directly, since
   w-decomposition depends on the assumed Ω_m (theirs ~0.3, yours ~0.1). DESI
   evolving-DE fits are the natural comparison (post-cutoff status: verify current
   results before citing).

**What the classical frame exposes:** (a) the mass budget becomes a blunt Friedmann
normalization statement every cosmologist can locate; (b) LLR/dilation/duality are
revealed as tests of frame bookkeeping, trivially satisfied — the real tests are
elsewhere; (c) **the second Friedmann equation**: check what continuity equation the
matter sector obeys and whether the effective ρ_x conserves anything sensible — a
referee asks this in the first paragraph and the static frame renders it invisible.

**What is lost (accept, don't resist):** genesis becomes an unremarkable big bang;
the Machian premise reads motivated in the static frame and ad hoc in the classical
one (choose presentation frame with this in mind); the entire §3 exponent apparatus
compresses to one sentence. That work was real — it *proved* the equivalence, and the
36σ-dead redshift bug shows the equivalence was not automatic — but its output is
scaffolding, not physics.

---

## 4. BAO — the Largest Unexamined Danger

Ranked above the remaining four-term-fit refinements in danger level. The fitted
H(z) is EdS-shaped to ~0.1% before z ~ 5 and departs recently. Pantheon+ reaches only
z ≈ 1.4 with the offset marginalized; BAO measures d_A(z)/r_d and H(z)·r_d out to
z ≈ 2.33 (Ly-α), squarely in the transition region. Even granting that r_d itself
needs the missing radiation era, the *relative* BAO shape across redshift is a shape
test of exactly the kind the SN fit passes — and it has not been looked at. A
ΛCDM-vs-EdS-shaped H(z) difference at z ~ 2 is not subtle. Run this before investing
further in secondary channels.

---

## 5. M-σ — Status and a Concrete Hypothesis for the Open Puzzle

The first discriminating test (§15 / Foundation §5.7) is real progress: full-AQUAL
with evolving a₀(z) beats fixed-normalization Newtonian virial dynamics on 135 real
quiescent galaxies (0.1266 vs 0.1345 dex; +0.0078 ± 0.0015 dex; 100% of bootstrap
resamples; holds in both redshift halves). Keep "suggestive first pass, not decisive"
wording — the effect (0.008 dex) is an order of magnitude smaller than the
uncorrected IMF systematic (~0.1–0.2 dex), so the bootstrap figure measures internal
stability, not protection against that systematic.

**Hypothesis for the naive-vs-full-AQUAL puzzle** (naive deep-MOND formula, wrong for
this transition-regime population, nonetheless gives the lowest raw scatter,
0.1185 dex): in deep-MOND, σ² = Γ√(GMa₀) — R_e cancels exactly. The full-AQUAL
treatment reintroduces R_e twice (g_bar = GM/R_e² and σ² = Γ g_obs R_e) with only
partial cancellation. High-z effective radii plausibly carry ~0.1 dex of measurement
error, so the naive formula may win simply because it is immune to the noisiest input
— a lower-variance predictor beating a more-correct one, standard behavior when
scatter is the metric.

**Directly testable, and the recommended next M-σ step:** generate mock catalogs
under the full-AQUAL model, inject realistic R_e noise, and check whether the naive
formula wins on the mocks too. If yes, the puzzle dissolves and *supports* the full
treatment. Do this before IMF cross-normalization or enlarging the z > 1.6 tail.

---

## 6. External Anchors to Re-verify Before Any Submission

All post-date or sit at the reviewer's knowledge cutoff; the project's notes say they
were verified by search at the time, but their subsequent reception matters:

- **MUSE-DARK III** (Ciocan et al. 2026, A&A 709, L16) and **MIGHTEE-HI**
  (Vărăşteanu et al. 2025): the a₀(z) sector's discriminating power over a free
  linear law hangs on these. If the evolution detection becomes contested or
  systematics-dominated, most of that power goes with it — a single-point-of-failure
  risk. Also check whether the MIGHTEE-vs-MUSE zero-point discrepancy has acquired a
  literature resolution (affects the nuisance-parameter setup).
- **KATRIN**: current bound and projected timeline toward ~0.3 eV — this is the
  framework's stated expiry mechanism.
- **DESI DR2+ evolving-DE fits**: current (w₀, w_a) posture, for the transient-phantom
  comparison in §3 above.

---

## 7. Publication Strategy

**Do not publish the full framework as a "new cosmology" paper in a mainstream venue
yet.** The CMB/BAO gap draws an immediate, currently unanswerable objection, and the
varying-c framing gets the work dismissed unread.

**Recommended path, in order:**

1. Complete: MCMC posteriors (esp. Σmν interval), the BAO shape check (§4 above),
   per-galaxy RAR covariance, H₀ propagated, external-anchor re-verification (§6).
2. **Lead with the phenomenological paper, classically framed** (per §3): a flat,
   matter-only (Ω ≈ 0.1) MONDian cosmology in which an AQUAL condition at the
   particle horizon replaces the Friedmann constraint, a₀ = (2λ/3)cH(t), EdS as the
   unstable scale-free solution, its instability as dark energy — jointly fit to
   Pantheon+ and the measured a₀(z) evolution with two effective parameters; the
   μ-discrimination result as a secondary finding. Venue class: MNRAS / PRD / JCAP.
   A referee can engage with this on first read, and it connects to the Milgrom
   a₀ ~ cH₀ literature.
3. The full static-frame framework rides behind as a carefully written arXiv
   preprint (expect endorsement friction and possible gen-ph classification for the
   ontological version) or a foundations-oriented venue (Found. Phys.; CQG for the
   formal parts), with scope limits stated as plainly as Foundation.md now states
   them.
4. **Present the falsification conditions prominently, as assets**: the dated KATRIN
   condition, and the rigid zero-new-parameter coupling between the SN history and
   a₀(z). Referees respect frameworks that specify their own kill switch.

**Framing guidance:** embrace, rather than resist, the observation that the
static-space varying-c language is a choice of description — the physical content is
the horizon closure, the a₀–H coupling, and the instability. The a₀(z) phenomenology
is what is testable; the ontology is what gets it dismissed. Publish the former
first and let the latter follow.

---

## 8. Consolidated Priority List (reviewer's ordering; supplements Foundation §6)

1. MCMC posterior on (ε₀, κλ, λ, Σmν) — the Σmν interval vs KATRIN is the viability
   question. (§2)
2. BAO relative-shape confrontation of the fitted H(z). (§4)
3. Second-Friedmann/continuity check of the classical-frame dynamical system. (§3)
4. Per-galaxy RAR covariance — controls the RAR-vs-mass-census tug-of-war and hence
   where Σmν lands. (§2)
5. External-anchor re-verification: MUSE-DARK III / MIGHTEE-HI status, KATRIN
   timeline, DESI comparison. (§6)
6. M-σ mock-catalog R_e-noise test to resolve the naive-vs-full-AQUAL puzzle. (§5)
7. H₀ propagated as a systematic (~9% lever on ρ₀).
8. Draft the classical-frame §2.2 derivation end-to-end (horizon condition → fixed
   point → instability → cosmography) as the phenomenological paper's core — this
   will also surface exactly where the continuity-equation question bites. (§3, §7)
