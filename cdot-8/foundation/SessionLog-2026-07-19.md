# Session Log — cdot-8 advisor sessions (2026-07-19)

*Continues from `SessionLog-2026-07-18.md` (thirteen entries, closed).
Per-day file per the program's convention; numbering continues the
advisor-side sequence.*

---

## Entry 1 — WP2 addendum reviewed and accepted: census weights carry no local-Q dependence under the definitions as written (density+volume decomposition complete); one amendment — the declined alternative files as facet 4 of the census-sector covariantization freedom; one sharpening — the matter census is exactly immune by the p = 5/2 cancellation (advisor session, 2026-07-19)

**Prompt (verbatim):**
> Please review this addendum...
> [uploaded: `Update-WP2-Addendum-CensusWeightQDependence-2026-07-19.md`
> — answers the flagged channel from
> Advisory-WP7-QDefinitionAdjudicated §4.2, in writing on the WP2/WP1
> record: E_P(t) = √(ℏc(t)⁵/G) is a per-slice normalization by
> definition (same status as Λ_M(t), Q̄(t)); c(t) = c₀(a/a₀)^{2/3} is
> WP1's kinematic pre-Q relabeling relation, background-only; the
> p_i^sp exponents are fixed structural labels (matter 5/2, radiation 1)
> with nowhere for a local field value to enter; decision: NO local-Q
> dependence — the WP7 §5 density+volume decomposition is the complete
> linear-order δ𝒩; background-Q̄ dependence of 𝒩̄_i(t) correctly
> distinguished and already carried; scope note separating this from the
> covariantization-freedom item.]

**Summary (advisor; verification in `census_weight_review.py`):** (1)
**Accepted** — every textual claim verifies (E_P's argument list; c(t)'s
pre-Q kinematic status; p_i^sp derivations matching the g_i structure on
record: p_m − 5/2 = 0, p_γ − 5/2 = −3/2 ✓). The decision is the right
kind — made on the definitions as written, in writing, as directed. The
density+volume decomposition is complete at linear order under the
default; assembly proceeds on it. (2) **Amendment**: the scope note
draws the line one notch too cleanly — the declined alternative (a
locally-normalized census, E_P(x,t) from the ball-smoothed local c,
which would close a δc ∝ q′δ𝒩 self-consistency loop as a coefficient
renormalization within the same window architecture) is excluded by the
definitions as built, not by physics: it files as **facet 4 of the
census-sector covariantization freedom** (gauge status, center, volume
convention, normalization locality), with the addendum's decision as the
declared default — the freedom item's standard pattern (default stated,
alternative banded, anchors untouchable). (3) **Sharpening — the facet
is bounded hard**: the census integrand ∝ c^{p_i − 5/2}, so the
local-c alternative couples as (p_i − 5/2)(δc/c): **matter is EXACTLY
immune (p_m = 5/2 — the same cancellation that zeroes g_matter's ċ/c
term)**; only radiation-class censuses (−3/2) feel it. The matter-era
low-ℓ structure is convention-free on facet 4; the freedom touches only
the radiation-era/crossover end — the item shrinks where the late-time
CMB lives. Third untouchable added to the freedom item's anchors:
matter-census invariance. (4) Directives: file with the amendment; add
the immunity bound; WP7 assembly unchanged, radiation-era coefficient
band inherits facet 4's width when low-ℓ numbers are quoted.

**Files produced (Entry 1):**
`Advisory-WP2-AddendumReviewed-2026-07-19.md`,
`census_weight_review.py`, `SessionLog-2026-07-19.md` (this file, one
entry).

**Open items handed forward:** worker: WP7 assembly (two exact anchors,
default window + shape band, facet-4 band on radiation-era coefficients,
low-ℓ system under Gate 1(b) framing); consolidation-batch sighting
(standing); **KATRIN watch item — Gate-1-class input on arrival**;
post-WP7 revisit queue unchanged. Nothing in `cdot-7/` was touched.

---

## Entry 2 — WP7 R_h reality check adjudicated: worker's catch CONCEDED as advisor error #8 (ΛCDM horizon value imported without computing — kR_h(z*) wrong by five orders); corrected map INVERTS the phenomenology: all modes M5-coupled through recombination (separate-universe-required, scale-independent), mode-exit history z_exit(k) derived, W-shape relocated to ℓ ≲ 10 late-time; NEW central finding — coupled-era growth modification O(0.6) of the matter source (advisor session, 2026-07-19)

**Prompt (verbatim):**
> Update...
> [uploaded: `wp7_anchor_brackets.py` + updated WP7 file — worker
> computes R_h(z) from the literal WP2 definition (Ṙ_h = c(t) =
> c₀e^{2s/3}) on the exact trajectory machinery: R_h(z* = 1090) ~
> 3.3e-3 Mpc vs r_s = 173.36 Mpc and D_p = 13074.3 Mpc (WP4a values) —
> kR_h(z*) ~ 1e-6–1e-5 for ALL observable CMB multipoles (ℓ = 2–2500
> table included): deep in W → 1. Finding: the "kR_h ~ 6 at the first
> acoustic peak" identification used illustratively since §2a was never
> checked against the actual R_h(z) trajectory and is off by many orders
> of magnitude.]

**Summary (advisor; corrected map in `wp7_phenomenology_map.py`):** (1)
**Conceded in full — advisor error #8**: the illustrative kR_h table
hardened into a claim ("first peak carries ~8% window, must be carried",
repeated in two advisories) without ever being run against R_h(t); class
= external-framework value (ΛCDM's ~285 Mpc comoving horizon) imported
into a variable-c trajectory without computing — with c ∝ a^{2/3},
light crawled early and the causal ball is ~100× smaller before
trajectory differences; the exact class this program polices;
worker-caught with the literal definition; their numbers confirmed to
the digit (R_h(z*) = 3.318e-3 Mpc reproduced). (2) **The corrected map
inverts rather than erases**: W(kR_h(t)) sweeps DOWN through k as R_h
grows — each mode has an exit epoch R_h(t_k) = 1/k: z_exit ≈ 6.5
(first-peak k), 16 (k = 0.1), 56 (cluster scales); ℓ ≲ 10 still
transitioning today. Three regimes: (a) at z* all observable modes sit
at W ≈ 1 — the (1−W) field-side term VANISHES there (~1e-12, not 8% —
both advisories to be errata'd); the Einstein-side term is full-strength
but scale-independent, and at W = 1 it is exactly the
separate-universe-consistent linear response the cdot-8 background
already implies — REQUIRED for consistency, no distinctive k-shape at
z*; (b) the distinctive W-shape survives at ℓ ≲ 10 via late-time
(ISW-era) evolution — the low-ℓ signature relocated, not erased; (c)
**NEW CENTRAL FINDING**: during each mode's coupled era the M5 response
modifies the Poisson source by (F_Q/6 + QF_QQ/2)q′𝒩̄ with elasticity
dlnQ/dln𝒩 ≈ −0.29 (dlnQ/ds = −5/2 vs census engulfment 3dlnR_h/ds) —
**O(0.6) of the matter source through the matter era** in first
estimate (exact number owed to the assembly under the two anchors):
growth history (σ8-class) replaces the acoustic peaks as WP7's central
deliverable AND — Gate 1(b) intact — its central risk. Re-scoped
statement: the AeST system imports cleanly for each mode AFTER its
exit; during the coupled era the separate-universe M5 response must be
carried. WP5/WP6 untouched (kR_h(today) ~ 1e5–1e9 quasistatic ✓
verified). (3) **Directives**: errata for the two 8%-claims;
illustrative-table rule to the fold-in queue (label or compute — nothing
in a table that can harden); assembly's first numerical target = the
coupled-era growth equation (elasticity from the trajectory with
radiation-class censuses added, evolved through exits, σ8-class output);
then the ℓ ≲ 10 late-time derivation with the window-shape + facet-4
bands (both freedoms now explicitly confined to the late/large-scale
regime); z_exit(k) into the toolchain. (4) Ledger note for the author:
#7 and #8 both advisor errors caught by the worker in consecutive
rounds — error-catching is genuinely bidirectional; the loop is healthy.

**Files produced (Entry 2):**
`Advisory-WP7-PhenomenologyMapInverted-2026-07-19.md`,
`wp7_phenomenology_map.py`, `SessionLog-2026-07-19.md` (this file, two
entries).

**Open items handed forward:** worker: coupled-era growth assembly
(first target), errata pair, late-time low-ℓ derivation; standing:
consolidation-batch sighting; **KATRIN watch item — Gate-1-class input
on arrival**; post-WP7 revisit queue unchanged. Nothing in `cdot-7/`
was touched.

---

## Entry 3 — WP7 §18–§22 adjudicated: worker's s-convention catch confirmed (advisor's non-independent "reproduction" owned, K6 rule added); §22 Part 2 dictionary-transplant error caught (c_ad² formula validated on AeST's map, applied to cdot-8's different map — correct matter-era c_ad² ≈ −0.004 to −0.04, dust-like); §21 answered structurally — Ω_s MUST cluster (it is the dark matter: ~4.4% baryons + ~3% ν + ~92% scalar); growth system fully specified (advisor session, 2026-07-19)

**Prompt (verbatim):**
> Advice on WP7, please.
> [uploaded: WP7 file extended with §18 (worker catches own R_h(s)
> exponent bug — s ≡ ln(c/c₀) per WP2's record, not ln(a/a₀):
> dR_h/ds = (3/2)(c₀/H₀)e^s/E; inherited unchanged by two advisor
> rounds; corrected R_h(z*) = 9.54e-4 Mpc, R_h(0) = 2598 Mpc; qualitative
> conclusions survive, checked directly; exact dln𝒩_tot/ds derived —
> coefficient stays O(0.5–0.7); filed as worker erratum), §19 (late-time
> (1−W(g(z;ℓ))) epoch profile: turn-on z ~ 0.3–1 for ℓ = 2–10, ISW
> window; z* cross-check 1e-15 via independent construction; honest
> scoping), §20 (anchors folded on corrected pipeline: Anchor A regression
> 0; Anchor B sharpened — field-side coefficient → −F_Q(today) = −1.8538
> EXACTLY = WP6 Step 2's symbol and number; WP5/WP6 zero residual), §21
> (ISW attempt surfaced foundational gap: standard smooth-Ω_s growth gave
> Ω_m(z=50) = 0.13, kernel peaked z ≈ 27 — implausible; question posed:
> does Ω_s cluster? 1.15× number explicitly NOT reported; escalated as
> fork-class), §22 (self-directed while advisor offline per author
> instruction: c_ad² machinery validated against AeST's sculpted-FRW
> closed form symbolically — exact dust+Λ reproduction, zero cdot-8
> input; then c_ad² = F_Q/(QF_QQ) applied to cdot-8's trajectory:
> O(1)–O(4) through growth era — "quintessence-like, not dust-like";
> de-escalates §21 preliminarily; honest limits stated).]

**Summary (advisor; verification in
`omega_s_clustering_adjudication.py`):** (1) **§18 confirmed** from the
machinery's own z-map (1+z = e^{−1.5s} + WP1's law ⟹ c = c₀e^s ⟹
s = ln(c/c₀), coefficient 1); corrected values reproduce to the digit
(9.541e-4 Mpc, 2598 Mpc). **Advisor's share owned**: my "independent
reproduction" copied the integrand's convention reading rather than
re-deriving from WP2 — while my own wp7_structure.py used the correct
1.5 factor elsewhere; two conventions in one toolchain, never
cross-checked. **K6 rule: convention factors are re-derived from the
defining document at first use in every new script, never copied from a
prior script, including one's own.** (2) **§19–§20 accepted**: the epoch
profile is clean ((1−W) > 1 entries are W's negative first lobe, min
≈ −0.086 — one explanatory sentence directed); §20's exact −F_Q
unification with WP6 (same symbol, same number, zero residual at
kR_h ~ 1e5–1e9) accepted as the anchor-task completion. (3) **§22:
Part 1 endorsed (absolute-anchor rule applied exactly right); Part 2
DICTIONARY-TRANSPLANT ERROR caught**: c_ad² = F_Q/(QF_QQ) is exact for
AeST's (ρ,P) = (QK_Q−K, K) map — which Part 1 validated — but cdot-8's
own inline-verified map is ρ_s = ½QF_Q − ⅓F; "invariant under K → cK"
is true and irrelevant (the transplant changed the MAP, not the scale).
Two-route exposure: invoice-anchored c_ad² = w + (dw/ds)/(dlnρ_s/ds) =
−0.0044 to −0.041 across z = 3–100 vs transplanted 1.3–1.5 — two orders
apart. **K6 entry: a formula's validation certifies it for the
dictionary it was validated on; a different (ρ,P) map requires
re-derivation, not reuse.** The de-escalation INVERTS — constructively.
(4) **§21 answered structurally — Ω_s MUST cluster**: (i) budget: 4.42%
baryon-class + 2.98% massive ν + 92.6% scalar today (77% at z=50, 43%
at z*) — nothing else to form structure with; (ii) corrected numbers:
w ≈ 0 AND c_ad² ≈ 0 through the matter era — the founding paper's
dust-like Π → 0 clustering criteria hold exactly where structure forms;
(iii) architecture: AeST's Q-sector is DESIGNED to cluster like CDM —
the theory's dark-matter mechanism, imported wholesale. The
Ω_m(z=50) = 0.13 symptom dissolves (missing clusterer found); the
worker's refusal to report the mis-specified 1.15× number was exactly
right. **Growth system fully specified**: dust-like scalar clustering
(imported Π → 0 evolution) + baryons + massive ν + M5 coupled-era
source with exit history + late-time w → −0.68 DE transition — a
unified DM→DE component with calculable growth; WP7's central
computation, now well-posed; field-variable care at the crossover
stands. (5) **Directives**: replace §22 Part 2's table with the
invoice-anchored route + file the transplant; build the growth system
(first sanity: δ_s tracks δ_b in the matter era; total growth ~
Ω_eff ≈ Ω_s + Ω_b universe) THEN add M5 + exits; ISW ΔC_ℓ follows on
the validated system with §19's profile. (6) Bidirectionality note
stands — both directions exercised again in one round.

**Files produced (Entry 3):**
`Advisory-WP7-OmegaSClusteringAdjudicated-2026-07-19.md`,
`omega_s_clustering_adjudication.py`, `SessionLog-2026-07-19.md` (this
file, three entries).

**Open items handed forward:** worker: §22 correction + growth system
per specification + ISW thereafter; standing: consolidation-batch
sighting; **KATRIN watch item — Gate-1-class input on arrival**;
post-WP7 revisit queue unchanged. Nothing in `cdot-7/` was touched.

---

## Entry 4 — Two issues assessed jointly: (1) Q₂/EFE tension source-verified (Park/Hees/Famaey/Desmond/Durakovic 2026, (1.6±1.8)e-27 s⁻²) — real, screening-immune (tidal argument), pressures a program CHOICE not derived structure; μ-swap revisit gains a second quantified motivation; IF re-fit recommended to top of post-WP7 queue; (2) WP7 growth snag diagnosis sharpened — Π ≈ c_ad²δ closure structurally wrong (negative c_ad², adiabatic-vs-rest-frame transplant); field-variable system now unavoidable (advisor session, 2026-07-19)

**Prompt (verbatim):**
> Two issues: The last step in WP7 hit a snag, and a review of recent
> Cassini data revealed a possible conflict. Please assess and advice.
> [uploaded: WP6 file with new EFE/Q₂ sub-task — worker validated
> machinery against the paper's own (e_N, Q₂) pair to 4 sig figs
> (catching their own e_N = a_e/a₀ slip via the validation), then
> computed cdot-7's Simple-IF/a₀ = 1.39e-10 prediction Q₂ ≈ 3.71e-26 —
> ~23× the new bound, ~21σ; family-switch check (RAR δ=1, a₀ = 1.26)
> gives the same tension; correctly distinguished from sub-task 1
> (transition-region vs deep-Newtonian); escalated not killed; routed to
> ConsolidationLog for cdot-7 relevance; AeST-inheritance question
> honestly open. WP7 file §24 (growth system: Stage 1 sanity passes,
> Ω_eff = 0.89–0.97, z=50 symptom gone; Stage 2 interim P_M5/P_std ≈
> 0.57–0.60 with honest caveat — baseline Φ grows ×2.4 at low z where
> dust treatment unlicensed) and §25 (general (w, c_ad², Π) equations
> verified from primary source; implementation broke — δ_b negative by
> z~30; diagnosed as own quasi-static shortcut; checkpointed honestly;
> staging requested).]

**Summary (advisor; source verification via web search):** **Issue 1 —
Q₂/EFE**: (1) Paper VERIFIED live (Q₂ = (1.6±1.8)e-27, 40% over Hees
2014's (3±3)e-27); worker's ~21σ arithmetic checks; Blanchet-Novak's
standard-IF range (2.1e-27 – 4.1e-26) corroborates — cdot-7's 3.7e-26
sits at the known shallow-transition top, now cut into by the new
bound. Worker's handling exemplary (absolute-anchor validation catching
their own slip; escalate-don't-kill; honest inheritance conditional).
(2) **Screening-immunity confirmed via the tidal argument**: the EFE
quadrupole is imprinted at r_t ~ √(GM/a₀) ~ 7000 AU where the external
field (e_N ~ 1–1.6) sets an anisotropic boundary; Saturn at 9.5 AU sits
in an interior that transmits, not screens, an external tidal term —
Q₂ probes the transition shape, the one place the theory MUST be
MONDian to fit galaxies; AeST is AQUAL-class quasistatically with a
Gpc-scale mass term irrelevant at r_t ⟹ default expectation: cdot-8
inherits its chosen IF's tension; the AeST-specific-suppression
loophole is open but mechanism-free — flagged as such. (3) **What's
actually under pressure: a program CHOICE** — the Simple IF and a₀ are
Foundation.md inputs, not census-derived structure; and the program
already owns the price list: the WP6 μ-collision round's 24–41% closure
exposure for Cassini-safe swaps. Q₂ gives the μ-swap revisit its second
independent quantified motivation (T22 + Q₂ push the same direction:
sharper transition; Desmond-Hees-Famaey 2024 maps the joint-survival
space). **Recommendation to the author: promote the IF re-fit
(sharpness-parameterized family; Q₂ + T22 in the likelihood; Δχ² ≈ 13
Simple-preference as the traded benefit; 24–41% as the cost envelope)
to the top of the post-WP7 revisit queue** — the second nature-set
clock, already ticking; sequencing per Gate 1(b) is the author's call.
**Issue 2 — WP7 snag**: §24 accepted as framed (Stage 1 passes; Stage 2
properly caveated — the ×2.4 Φ growth is the dust treatment overdriving
where w → −0.68); §25's checkpoint discipline right; **diagnosis
sharpened — the quasi-static shortcut was not the only structural
problem**: Π ≈ c_ad²δ_s is the ADIABATIC-fluid closure, wrong twice
over — (i) cdot-8's matter-era c_ad² is NEGATIVE (−0.004 to −0.04):
imaginary sound speed manufactures instability (likely part of the
δ_b < 0 pathology); (ii) the DE-literature approximation is rest-frame
c_s², not c_ad² — the transplant is a cousin of §22's dictionary error;
(iii) the founding paper's ∇²[K_B ℰ_α + (2−K_B)χ] term IS the closure,
not a correction to it. **Directive: go directly to the field-variable
system** — coupled (δ_b, θ_b, χ, ℰ_α, Φ) with full k-dependence, §7's
standing directive now unavoidable (every fluid shortcut has failed at
the same wall from a different side); staged WP3-rhythm with §24
Stage 1 as the matter-era regression target. Fold-ins: tidal-argument
mechanism; closure lesson (third dictionary-class K6 entry).

**Files produced (Entry 4):**
`Advisory-WP6WP7-Q2AndGrowthSnag-2026-07-19.md`,
`SessionLog-2026-07-19.md` (this file, four entries).

**Open items handed forward:** AUTHOR DECISION: IF re-fit promotion and
its sequencing vs Gate 1(b). Worker: field-variable growth system
(staged); Q₂ item held open pending the author's call; standing:
consolidation-batch sighting; **KATRIN + Q₂ — two external clocks**.
Nothing in `cdot-7/` was touched.

---

## Entry 5 — WP7 §26 assessed: double failure accepted as signal, joint staged round confirmed; Stage 0 delivered — stiffness audit exonerates the physics (|μ_eff|/H < 1 everywhere; suspects = formulation K2 + units K3); audit byproduct is the round's discovery: Hubble-tracking tachyonic effective mass μ² ≈ −0.5H² through the matter era = the scalar's clustering mechanism (F_QQ's fourth load-bearing appearance) (advisor session, 2026-07-19)

**Prompt (verbatim):**
> One more update from the worker.
> [uploaded: WP7 file with §26 — advisor accepted on both prior issues
> (Q₂ recorded in the WP6 file + ConsolidationLog Item 16); the
> field-variable system attempted a SECOND time with a careful closure:
> direct δ,θ evolution equations; χ = Q̄(θ+α) algebraic; α̇ = ℰ_α − Ψ;
> ℰ_α equation with the bare field equation's F_Q (correctly
> distinguished from ρ_s's M5-modified Friedmann combination — the §23
> dictionary lesson applied); Φ via momentum constraint, real
> k-dependence. It also failed — solver step-size collapse, invalid
> values, worse than §25. Checkpointed, not patched a third time. Two
> careful solo failures declared real signal; the dedicated WP3-rhythm
> round with advisor cross-checking at each stage requested. §24 Stage
> 1/2 numbers remain the current caveated best.]

**Summary (advisor; audit in `wp7_stiffness_audit.py`):** (1) **§26
accepted; joint staged round CONFIRMED** (advisor cross-checking per
stage; §24 Stage 1 as regression target; both anchors as brackets). The
second attempt's closure logic was right where it mattered — the
F_Q-vs-ρ_s distinction applied correctly under pressure — which is
exactly why the failure is signal. (2) **Stage 0 delivered — the
stiffness audit**: K1 (effective-mass stiffness) EXONERATED —
|μ_eff|/H ≲ 0.7 at every epoch: no fast oscillator; the physics
integrates at ordinary tolerances in regular variables (the ULA-class
averaged closure is NOT needed — noted preemptively). K2 (singular
factors) PRIME SUSPECT: the effective-fluid δ,θ definitions carry
1/ρ_s and c_ad²; |1/c_ad²| = 20–230 THROUGH the matter era; their
equations carry Π/(1+w). **Standing rule: state variables are (χ or γ,
α, ℰ_α, δ_b, θ_b, Φ) only; effective-fluid objects are output
diagnostics.** Hypothesis: §26 kept δ,θ as state — check against the
script in the joint round. K3 (units) CO-SUSPECT: |F_Q| spans 4473 →
1.85 in H₀² units; the founding paper's dK/dQ lives in ITS
normalization. **The round opens with one written dictionary line per
imported equation before any code** — third dictionary-class trap,
pre-empted. (3) **The discovery**: the audit's μ² zeros traced to real
sign structure, verified two ways (matter-era closed form Q²F_QQ =
(36/25)F vs interior spline: 889 vs 875 at z=10, 1.6%): **μ²/H² =
−(36/25)(30/34)f_s/(2−K_B) ≈ −0.5, constant through the matter era —
a scale-free, Hubble-tracking tachyonic effective mass — flipping to
the doubly-verified stable sign (F_QQ(0) = −0.696, Gpc Compton) near
today.** Tachyonic at |μ| < H = Jeans-class growing mode = the
clustering mechanism §23's requirement demanded: the quadrature F,
built only to pay the invoice, destabilizes the smooth solution through
exactly the era where the scalar must cluster and withdraws it exactly
when the component turns dark-energy-like. **F_QQ's fourth load-bearing
appearance** (condensate mass; stability sign; constraint feedback;
structure formation). Caveats as Stage-1 tasks: robust F_QQ(z) for the
flip location (my quick spline endpoint at z=0 disagreed with the
verified record — interior solid, boundary not; the closed-form route
was forced by that disagreement); full dispersion ω² = c_s²k² + μ²(z)
with the 𝒴-sector's c_s² (SZ-healthy at today's anchor); SZ scope
consistency noted. (4) **Staged plan as informed**: 0 ✓ audit; 1 robust
F_QQ + dispersion (growth RATE now a checkable prediction); 2 units
contract; 3 pure-field system per K2's rule, implicit solver, §24
regression + anchors; 4 M5 + exits + ISW ΔC_ℓ. (5) Housekeeping:
ConsolidationLog Item-16 citation confirms the record is live — the
file-sighting item softens to routine; fold-ins queued; **two external
clocks** (KATRIN; Q₂ awaiting the author's sequencing call).

**Files produced (Entry 5):**
`Advisory-WP7-StiffnessAuditAndClusteringMechanism-2026-07-19.md`,
`wp7_stiffness_audit.py`, `SessionLog-2026-07-19.md` (this file, five
entries).

**Open items handed forward:** JOINT STAGED ROUND (Stages 1–4, per
plan, worker + advisor per stage); AUTHOR: Q₂/IF-re-fit sequencing
decision (standing); KATRIN watch. Post-WP7 revisit queue: IF re-fit
(promoted, pending author), μ-swap (subsumed into IF re-fit),
low-Σm_ν re-closure (KATRIN-aligned), radiation-era assumptions per
Gate 1(b). Nothing in `cdot-7/` was touched.

---

## Entry 6 — Onboarding documents (new project Foundation.md + Progress.md) assessed against the session record: accurate and honest as written; two headline gaps (KATRIN absent from both; WP7 blocker described pre-Stage-0 — audit rules and μ² clustering-mechanism finding missing); five secondary additions; ready-to-merge insertion text supplied (advisor session, 2026-07-19)

**Prompt (verbatim):**
> I have had made a new project Foundation for cdot-8 and added a
> Progress document to add clarifications on where we currently are.
> The purpose of these is to recruit assistance with particular issues
> from other agents that do not have the full context. Please asses
> these within your current content and adivce if there are important
> elements missing.

**Summary (advisor):** (1) **Verdict: both documents are accurate,
well-scoped, and preserve the honesty conventions** — nothing
contradicts the record; Gate 1(b) carried correctly everywhere;
Progress §6's methodology note (verify-before-trust bidirectional;
escalate-don't-decide; "every crisis except WP4a's has dissolved")
called out as the best single page and exactly the right prior
calibration for a recruit. Foundation §3's "critical divergence,
adopted knowingly" and §11 likewise endorsed as-is. (2) **Headline gap
1 — KATRIN absent from both**: Σm_ν = 1.374 eV is quoted as acceptance
data with no exposure statement, yet it implies m_β ≈ 0.458 eV against
KATRIN's published partial-data bound < 0.45 eV (90% CL), campaigns
complete, final analysis (< 0.3 eV sensitivity) pending — the
framework's sharpest nature-scheduled falsification test; registered
criterion (detection ~0.46 required; null excludes) and the
WP4a-lever alignment (low-Σm_ν re-closure is the named revisit
candidate KATRIN will adjudicate) both supplied as insertion text.
(3) **Headline gap 2 — the top-priority open item (WP7 growth system)
is described pre-Stage-0**: the drafted diagnosis ("the crossing's
negative c_ad²") is narrower than the record (c_ad² negative through
the WHOLE matter era); missing: the audit's exoneration of the physics
(|μ_eff|/H < 0.7 everywhere — failures are formulation + units), the
two standing rules that prevent a recruited agent from repeating both
failures (pure field-variable state; written units contract per
imported equation), the Stage 0–4 plan with 0 complete, and the
**μ²(z) ≈ −0.5H² Hubble-tracking clustering-mechanism finding**
(F_QQ's FOURTH appearance — Foundation §7 says three) with its Stage-1
caveats — both the item's recruiting asset (checkable growth-rate
target) and a required safety flag (μ² < 0 must not be misread as a
found instability). Replacement text supplied. (4) **Secondary
additions**: the two exact numerical anchors as page-one
non-negotiables (separate-universe coefficient (F_Q/6 + QF_QQ/2)q′;
sub-horizon −F_Q = WP6's own number); facet 4 (normalization locality,
per-slice default) + the matter-immunity third untouchable added to
open item 5; the α₂ provisional envelope (K_B ≲ 4e-10, flagged
provisional, potentially binding) + the K_B → 0 benignity statement
(the squeeze is survivable — envelope ≠ existential threat); the
post-WP7 revisit queue consolidated as one explicit list (IF re-fit
[author sequencing + single-μ economy-vs-freedom author question],
low-Σm_ν re-closure [KATRIN-aligned], radiation-era assumptions);
consistency nit Ω_closure 0.0750 (docs) vs 0.074 (toolchain) — one
reconciling line, since a careful recruit will check. (5) All quoted
numbers traced to the session record; no new computation this round.

**Files produced (Entry 6):**
`Advisory-OnboardingDocsAssessed-2026-07-19.md`,
`SessionLog-2026-07-19.md` (this file, six entries).

**Open items handed forward:** author: merge decisions on the proposed
insertions (KATRIN block; WP7 Stage-0 replacement; five secondary
items). Standing: joint staged WP7 round (Stages 1–4); Q₂/IF-re-fit
sequencing decision; **KATRIN watch**. Nothing in `cdot-7/` was
touched.
