# Session Log — cdot-8 advisor sessions (2026-07-21)

*Continues from `SessionLog-2026-07-19.md` (six entries). Note: WP7
§27–§43 (the staged growth rounds, the Stage-4 escalation, and the
2026-07-21 instability advisory referenced in §43) were conducted in
parallel advisor sessions; this file logs the present session's rounds.*

---

## Entry 1 — Stage-4 ISW/growth vector-sector instability assessed at the author's request: mechanism map confirmed (anti-Jeans on the accepted c_ad² < 0 branch — rate ~ |c_ad|k/aH, scalings verified against reported eigenvalues); one required correction flagged (Stage-4 assembly cites §7's superseded all-k cancellation — the −F_Q(1−W) field-side term activates at z ≲ 1–3, inside the ISW window); recourse ladder delivered R0–R4 (advisor session, 2026-07-21)

**Prompt (verbatim):**
> We have ran several more iterations on WP7, good progress but ended
> in a significant block on the ISW/growth track vector-sector
> instability. Please assess and see if there are any likely recourses
> that could plausibly recover a sensible spectrum.
> [uploaded: WP7 file extended through §43 — the staged rounds §27–§41
> (validated growth closure at k = 1e-4/Mpc; 6×6 analytic stability
> audit; low-z growth identified as the known scalar tachyonic
> mechanism), §42 (Stage-4 assembly at the actual ISW k's = 1.1–5.4e-3
> /Mpc: the (α, ℰ_α) fast eigenvalue stays real positive z = 100 → 0
> at all three ℓ's — no z_switch exists; confirmed in the full
> machine-precision Jacobian; Φ grows 5–8 orders; escalated, not
> killed), and §43 (parallel-session advisory confirmed the numbers,
> reframed as the same c_ad² < 0 mechanism at larger k, routed to the
> author; worker's careful reassessment adopted the reframing and
> caught a shared np.gradient edge_order boundary artifact — corrected
> endpoint λ ~ 8–9 not 24, verdict unchanged).]

**Summary (advisor; computation in `isw_instability_recourses.py`):**
(1) **Mechanism pinned**: reported eigenvalues match the anti-Jeans
rate |c_ad|k/(aH) in order, k-scaling, and z-trend (3H₀ estimated vs
8–9H₀ corrected at z=0 — O(2–3) mixing factors); dispersion decomposes
ω² ≈ c_eff²k² + μ²(z): μ² ≈ −0.5H² (census-determined, F_QQ) is the
GOOD scale-free clustering driver; c_eff² ≈ c_ad² < 0 is the pathology
— and the two have different origins, which is what makes recourse
possible. (2) **Required correction regardless of recourse**: the
Stage-4 assembly cites §7's superseded all-k cancellation; the
corrected record's −F_Q(1−𝒲(kR_h)) field-side term is OFF at z ≳ 10
(not the cause of the z=100 instability) but activates at z ≲ 1–3
((1−W) = 0.3–1.0 by z=0 at these k) — inside the ISW window; must be
carried with its window-shape band in any rebuild. (3) **Recourse
ladder**: R0 audit (mandatory first, cheap, decision-informing): (a)
were the imported (α, ℰ_α) equations derived under the founding
paper's K_Q(background) = 0 minimum assumption? — cdot-8 never sits
there (F_Q spans 4473→1.85); any legitimately-dropped ∝K_Q term is
enormous for us (WP6 Step-2 sliding-condensate class); (b) where does
the negative c_eff² net from, given the positive-definite bare
(2−K_B)𝒴 gradient floor? — the unstable direction is the longitudinal
combination the rank-1 U-structure doesn't protect; tracing it
determines R1's feasibility. R1 (leading physical recourse): the
𝒴-sector small-gradient completion — F_𝒴(0,Q(z)) renormalizes the
gradient operator at LINEAR order (𝒴 quadratic in perturbations) while
leaving 𝒴 ≡ 0 on FRW: background, quadrature, invoice, WP1–WP4
EXACTLY untouched; requirement c_eff² ≳ 0 at cosmological gradients;
if R0(b) says reachable, the completion family is pinned from THREE
sides (T22 deep-Newtonian, Q₂ transition, stability small-gradient) +
KATRIN on the census side — one function family, four external
anchors: the post-WP7 revisit consolidates into a single joint design
problem; deep-MOND-softening vs stability-floor tension stated
honestly (AeST's bare (2−K_B)𝒴 floor is structural room pure AQUAL
lacks). R2 (attribution diagnostic, cheap): AeST-native cross-check —
their K-minimum has c_ad² ≳ 0, expect stable; closes the
assembly-error branch from the other side. R3 (heavy lever,
synergistic): re-closure — c_ad²(z) is a trajectory output (matter-era
w slightly below zero); moves under changed census content — the
low-Σm_ν/KATRIN-aligned lever; belongs inside the joint re-fit, not
standalone. R4 (fallback interpretation, not a recourse): nonlinear
a₀-saturation — the runaway self-quenches at MOND-scale gradients;
theory may survive as saturated texture while LINEAR predictivity at
these scales is lost — materially worse for WP7's deliverable;
recorded so the option space is honest. (4) **Recommended sequencing
(author's decision, not presumed)**: R0+R2 = one short round,
verdict-neutral, converts "pathology or error?" into a known quantity
and determines R1's reachability; R1+R3 live inside the already-
promoted IF-re-fit — the instability adds the fourth anchor to a
re-fit that was already coming, rather than opening a second crisis;
if R0(b) returns F_𝒴-unreachable, the remaining options are R3/R4 and
the verdict conversation changes character — the branch point worth
knowing before scheduling anything else. (5) Item remains routed to
the author per §43's joint agreement; this advisory is the requested
option map.

**Files produced (Entry 1):**
`Advisory-WP7-InstabilityRecourses-2026-07-21.md`,
`isw_instability_recourses.py`, `SessionLog-2026-07-21.md` (this file,
one entry).

**Open items handed forward:** AUTHOR: instability-recourse sequencing
(R0+R2 recommended as the verdict-neutral next round); Q₂/IF-re-fit
sequencing (standing, now joined by the stability anchor); **KATRIN
watch**. Worker (upon author's go): R0 audit + R2 cross-check + the §2
assembly correction. Gate 1(b) carried; the instability logged as the
second independent open structural question alongside WP4a. Nothing in
`cdot-7/` was touched.

---

## Entry 2 — R0/R1/R2 diagnostic round assessed: accepted in full (branch point resolved favorably on all three rungs); three additions delivered (λ_s → −1 = the scalar becoming honest dust; the λ_s > 0 tension located on a scale map — band sits 11–56× above μ; the vector-mass corner parametrically protected by WP6's K_B squeeze); recommendation: commission the action-level FRW derivation with general 𝓕(𝒴,𝒬) (advisor session, 2026-07-21)

**Prompt (verbatim):**
> Here is an update from the worker. Please assess and advice how to
> proceed.
> [uploaded: `Update-WP7-InstabilityRecourses-2026-07-21.md` — R0(a):
> founding paper's stability guarantee explicitly assumed
> F_Q(background) = 0 ("desired late Universe limit... ∂𝓕/∂𝒬 = 𝓕̄ = 0"
> verbatim) — the guarantee was never established at cdot-8's operating
> point (F_Q = 4473→1.85); precise qualifier: the imported EOM keep
> dK/dQ general (Stage-2 verified) — the equations aren't wrong, the
> HEALTH CLAIM doesn't cover us. R0(b): the negative pressure nets
> entirely from Π's κ-linear feedback term (c_ad²κ/3Ω_s) — dominant
> and uniformly destabilizing (secondary advisor refinement: 4.5 orders
> at z=100, not 1–2); the three κ-independent pieces modest and
> negative — the unstable direction sits exactly in the F_𝒴 slot:
> favorable for R1. R2: founding paper's own Higgs-like K(Q) built with
> its own parameters (read off its figure); Q̄(a) solved exactly via
> conserved charge (depressed-cubic reformulation catching a
> precision trap); native c_ad² ~ −6.5e-4 at z* collapsing to −1e-12
> today — identical Jacobian at identical k: stable by z≈100, stays
> stable — pathology is cdot-8-specific: minimum-tracking vs
> monotonically-forced (structural dichotomy). R1 (feasibility, NOT
> derivation — honestly scoped): F_𝒴 = (2−K_B)λ_s is the paper's own
> named free parameter (healthy range λ_s > −1); structural hypothesis
> (2−K_B) → (2−K_B)(1+λ_s) in the ℰ_α bracket: λ_s → −1 suppresses the
> instability by orders of magnitude, λ_s = −1 exactly gives clean
> k-independent stability (Re λ = −0.5) at every z and k; tension:
> −1 is the paper's own healthy-range boundary (M² ∝ 1+λ_s → 0);
> −0.99 to −0.999 already gets most benefit; gaps: no action-level FRW
> derivation exists for F_𝒴 ≠ 0 (refused to guess); secondary advisor
> catch — the paper ALSO states λ_s > 0 for the ω = 0 vector mode's
> Hamiltonian positivity (verbatim, lines 570–571), directly opposing
> λ_s → −1⁻, though the paper frames the low-momentum negativity as
> "likely akin to Jeans-type instabilities" and the full analysis
> lives in unavailable companion papers.]

**Summary (advisor; additions in `r1_viability_additions.py`):** (1)
**Round accepted in full, quality named**: every rung against the
primary source; the numerical trap caught pre-trust; hypothesis-vs-
derivation boundary drawn exactly right; both secondary-advisor
refinements accepted; R2's minimum-tracking-vs-monotonically-forced
dichotomy flagged for Foundation.md upon settlement — the cleanest
one-sentence account of why cdot-8's cosmology differs from its
chassis. Branch point resolved FAVORABLY on all rungs: genuine physics
(not error), cdot-8-specific, F_𝒴-slot reachable. (2) **Addition 1 —
what λ_s → −1 IS**: (2−K_B)(1+λ_s) → 0 makes the scalar ULTRALOCAL —
c_s² → 0 at cosmological gradients — i.e., HONEST DUST at linear
order, with the census-fixed, λ_s-untouched μ² ≈ −0.5H² driver still
supplying scale-free CDM-like growth; the pathology was c_eff² < 0,
CDM has c_s² = 0, the recourse approaches zero from the correct side —
principled, not epicyclic; leads any report to the author. (3)
**Addition 2 — the λ_s > 0 tension LOCATED**: the negative-Hamiltonian
zone sits at k ≲ μ ≈ 1e-4/Mpc; the stabilization band at 1.1–5.4e-3 =
**11–56× above μ**; the low-k zone is the paper's own "Jeans-type"
(clustering) sector, Hubble-frictioned on FRW; whether λ_s < 0
threatens k > μ is exactly what the compact PRL phrasing leaves open —
the FRW derivation starts with the scale map in hand; μ is WP5's
Gpc-Compton scale in its fourth sector. Not dissolved; located. (4)
**Addition 3 — the corner is K_B-protected**: M² = (2−K_B)(1+λ_s)Q₀²
/K_B — at the pulsar envelope K_B ≲ 2.5e-6 even 1+λ_s = 1e-5 leaves
M²/Q₀² ~ 8: the corner is dangerous only at O(1) K_B; WP6's squeeze is
load-bearing FOR the recourse — two previously unrelated results now
mutually supporting. (5) **Recommendation: commission the action-level
FRW derivation with general 𝓕(𝒴,𝒬)** — WP3-rhythm, jointly
cross-checked, Gate 4 paused until it lands; target list: (i) does the
(1+λ_s) renormalization hold and where is the true boundary; (ii) the
λ_s > 0 condition's fate on FRW (derive, don't cite — companions
unavailable), with the scale map and the ω = 0 constraint analysis;
(iii) the function-valued λ_s^eff(𝒴,Q) — small-𝒴 cosmological end vs
galaxy end: the same family as T22 + Q₂, now with the stability
anchor; (iv) the vector mass along the trajectory under the squeeze;
(v) only then the ISW rebuild (derived coefficients + the flagged
−F_Q(1−𝒲) correction + both anchors + both bands). Either outcome is
worth the round: landing favorably brings WP7's deliverable back into
reach with the completion pinned four ways; landing elsewhere narrows
honestly to R3/R4 with real information.

**Files produced (Entry 2):**
`Advisory-WP7-RecourseRoundAssessed-2026-07-21.md`,
`r1_viability_additions.py`, `SessionLog-2026-07-21.md` (this file,
two entries).

**Open items handed forward:** AUTHOR: commission decision on the
𝓕(𝒴,𝒬) FRW derivation (recommended); Q₂/IF-re-fit sequencing
(standing — the stability anchor now joins it); **KATRIN watch**.
Gate 4 paused; Gate 1(b) carried. Nothing in `cdot-7/` was touched.
