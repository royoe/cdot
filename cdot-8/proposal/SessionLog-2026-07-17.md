# Session Log — cdot-8/WP4 (2026-07-17)

*Continues `SessionLog-2026-07-16.md` (three entries: WP4a assessment,
discrepancy hunt, WP4a-closure/WP4b review with pre-decision checklist).
Shared, single-writer-at-a-time log per the Entry-9 process rule
(2026-07-12). Note: the worker reported an accidental overwrite of the
07-16 log during their correction round — repair of that file plus the
standing numbering reconciliation is queued as one combined delivery on
the worker's side. Times in SAST (UTC+2).*

---

## Entry 1 — WP4b re-derivation: the 0.276 refuted; worker's cdot-8 side confirmed, error localized in the reference construction; corrected verdict BBN-compatible; WP3 formally closed (advisor session, 2026-07-17, ~09:0x–09:4x SAST)

**Prompt (verbatim):**
> Two more updates for cross check.
> [uploaded: `Update-WP4b-BBN-Correction-2026-07-16.md` — both advisor
> flags confirmed real (Flag 1 an actual factor-2 code bug, not prose;
> Flag 2 the ν-temperature gap); WP3 closed by symbolic inspection
> (∂g_i/∂N=0 exactly); corrected recalculation with closure feedback gives
> H ratio 0.19–0.27, previous table withdrawn; transition-width sensitivity
> unresolved. `Update-WP4b-Converged-2026-07-17.md` — ad hoc width removed
> via direct entropy conservation for T_γ(a); (11/4)^{1/3} reproduced from
> first principles; WP4a regression exact; x(s)=3.3–3.44 sane; converged
> H_τ̂/H_SBBN ≈ 0.276, ΔN_eff ≈ −5.7; escalated for independent
> re-derivation before feeding the decision.]

**Summary (advisor; full construction in `wp4b_rederivation.py`):** **The
severe result is refuted; the worker's escalation discipline is what caught
it.** Independent construction with identical thermal physics both sides
and the comparison built through ONE shared T↔a map (entropy-derived
T_γ(a); frozen T_ν; corrected e± at 1.75) so all bookkeeping cancels by
construction: the BBN confrontation ratio at fixed local temperature is
$$H_{\hat\tau}(T)/H_\text{SBBN}(T) = E(a(T))/\sqrt{u(a(T))} = 0.965\text{–}1.007$$
across T = 3→0.02 MeV — a 3.5% deficit, not 72%, with a brief transient
*above* unity mid-annihilation (x dips to 3.315 off the fixed point).
Checks all clean: 1.75/1.75 limits; boost 0.7138 = (4/11)^{1/3} exact;
**WP4a regression E(1090)=18397.6 ✓**; μ-saturation max y = 0.775 = the
fixed-point value (no saturation). **Diagnosis**: the worker's cdot-8 side
is right — their sanity numbers (x range, regression, boost) are
numerically identical to mine — so the factor-3.5 error lives in their
independently-built reference side; magnitude matches the stack
0.965/[(11/4)^{2/3}×1.75] = 0.281 (naive T-z mapping on the reference plus
e± mismatch), hypothesis-grade until their code confirms. **New K6 rule
adopted: comparisons between models at a shared physical variable must be
built through one shared map, never two independently-assembled sides.**
**Corrected leading-order BBN verdict: cdot-8 passes** — ΔN_eff,eff ≈ −0.3
at freeze-out; Y_p ≈ 0.243 (within 1σ of 0.2453±0.0034); D/H ~−1%
(negligible); Li-7 −10–15% (favorable lean). Both the "severe" (converged
update) and "borderline −2.3σ" (checklist round) framings superseded.
**Decision-input sharpened at both ends**: the expansion deficit is a
*crossover-era* phenomenon — 3.5% deep in radiation (BBN passes), 21% at
recombination (θ* fails by 27%), passing SN below — one epoch, one
structural cause (census crossover z_eq ≈ z*, set by Σm_ν), one failing
observable bracketed by passes; KATRIN coupling tightens (Σm_ν sets the
crossover). **WP3 formally closed** (worker's symbolic ∂g_i/∂N=0 accepted;
checklist item discharged). Ledger: worker's escalation posture credited
explicitly; advisor Flag-1 "likely benign" guess corrected by worker's
confirmation (real code bug); worker's entropy machinery endorsed with one
inverted above/below-decoupling prose sentence flagged.

**Files produced (Entry 1):** `Advisory-WP4b-Rederivation-2026-07-17.md`,
`wp4b_rederivation.py`, `SessionLog-2026-07-17.md` (this file).

**Open items handed forward:** worker verification of the shared-map
construction + reference-side bug anatomy for the ledger; the consolidation
batch (now including the shared-map K6 rule, the WP4b errata chain, the
census-law scope statement, and all previously listed items); worker log
repair (07-16 overwrite) + numbering reconciliation; **then the author's
Foundation §6 item 6 decision with the corrected input: crossover-era
failure, radiation-era pass, low-z pass, levers 5–10% vs 27%, KATRIN
coupled at the crossover; the KATRIN clock remains the program's most
time-critical item.**

---

## Entry 2 — WP4b normalization adjudication: the rebuttal's z=0 check is a category error; the reference is absolutely anchored; BBN-compatible verdict reinstated (advisor session, 2026-07-17, ~11:0x SAST)

**Prompt (verbatim):**
> The worker objects...
> [uploaded: `Update-WP4b-RederivationRebuttal-2026-07-17.md` — worker runs
> the re-derivation script, observes ratio = 3.67 at z=0, asserts any
> correct comparison must give 1 there, diagnoses a "missing division by
> u00 = 0.074," multiplies the table by √0.074 to recover 0.26–0.27, and
> declares the severe 0.276 result confirmed by two independent
> constructions; recommends routing to the author as a severe BBN finding.]

**Summary (advisor; adjudication in `normalization_adjudication.py`):**
**Rebuttal rejected — the first worker correction this program declines,
adjudicated on grounds external to both parties.** (1) **Absolute anchor**:
standard BBN's H(1 MeV) = 0.68 s⁻¹ (textbook, used by every BBN code, fixed
by G and statistical mechanics at measured T_CMB). My reference
H₀√u(a(T)) gives 0.673 s⁻¹ (0.994×); the rebuttal's census-normalized
H₀√(u/u_today) gives 2.474 s⁻¹ (3.65×) — a fictitious universe with 13.5×
the physical radiation density at fixed T. (2) **Category error named**:
the ratio E/√u at z=0 is *supposed* to be 3.68 — it is the framework's
central claim as a number (modified gravity supplies 92.6% of E² today);
demanding 1 normalizes the scalar sector out of existence. The z=0=1 check
is valid for two complete cosmologies at the same z (the WP4a quantity),
invalid for the absolutely-anchored fixed-T BBN quantity. (3)
**Convention-free tiebreaker**: the fixed-T ratio ≡ √(E²/u), the invoice
fraction — established at 0.93 deep-radiation in every budget round since
07-12; the rebuttal's 0.276 requires an invoice of −92.4% that five days
of tables never showed. **Ledger, both directions**: worker's original bug
anatomy now confirmed as the census-normalized reference (0.965×√0.074 =
0.263 ≈ their 0.19–0.27/0.276) — my earlier stack hypothesis (1.96×1.75)
was right in localization, wrong in mechanism, corrected; presentation gap
owned (the re-derivation advisory should have stated and interpreted the
z=0 value preemptively — new rule: state a delivered quantity's value at
the reader's most natural sanity point before they compute it and read a
bug into it); rebuttal's inline-check instinct endorsed but its proposed
check would have institutionalized the error — **absolute-anchor K6 rule
adopted instead** (every confrontation ratio carries one absolutely-known
external anchor verified inline); escalation-asymmetry note recorded (five
accepted advisor errors made the prior favor the worker; the rebuttal's
confidence tracked the prior, not the physics; verdicts go by anchor and
consistency, not track record). **Reinstated verbatim**: ratio 0.965–1.007;
ΔN_eff ≈ −0.3; Y_p ≈ 0.243 (1σ); cdot-8 passes BBN at leading order;
crossover-era localization and decision input unchanged.

**Files produced (Entry 2):**
`Advisory-WP4b-NormalizationAdjudication-2026-07-17.md`,
`normalization_adjudication.py`, `SessionLog-2026-07-17.md` (this file,
two entries).

**Open items handed forward:** worker verification of the four-line
absolute-anchor computation + invoice consistency, then withdrawal of the
rebuttal's routing and the errata-chain entry (census-normalized-reference
anatomy across the three affected WP4b updates); consolidation batch
(+absolute-anchor rule, +presentation-gap rule); **then the author's
Foundation §6 item 6 decision on the re-derivation advisory's §4 input,
unchanged**; worker log repair + numbering reconciliation (standing);
**the KATRIN clock remains the program's most time-critical item.**

---

## Entry 3 — WP5 first installment: decoupling argument confirmed with variational mechanism; clock pinned via charter identity; lensing prediction backbone delivered; m_x question given its testable expected answer (advisor session, 2026-07-17, ~13:0x SAST)

**Prompt (verbatim):**
> First touch on WP5.
> [uploaded: `Update-WP5-WeakFieldStructure-2026-07-17.md` — worker imports
> Ψ=Φ from AeST (Skordis-Złośnik PRL 127, 161302; Hamiltonian analysis
> 6 DOF) per K1; states the load-bearing decoupling argument (M5 constrains
> only the background zero mode Q₀(t) since 𝒩 is a horizon integral,
> insensitive to local rearrangement — named assumption, flagged);
> recovers ∇·[μ(|∇Φ|/a₀(z))∇Φ]=4πGρ with a₀(z)=λċ(z) from the closure;
> defers the Mistele two-limit (m_×) question and the actual lensing-RAR
> curve; requests confirmation of the decoupling reading before building.]

**Summary (advisor; numerics in `wp5_decoupling_check.py`):** **Decoupling
argument confirmed and strengthened.** The variational half completes it:
δS_M5/δφ(x) spreads Λ_M's force with weight 1/V_horizon while Λ_M is
extensive (∝Na³F_Q) — the product is finite but *spatially uniform* at
leading order, i.e., exactly the verified background φ-equation and
nothing local; census side δ𝒩 = 0 at first order (binding-energy terms
second order, mass-fraction suppressed). M5 constrains the zero mode and
only the zero mode; local δQ obeys unmodified AeST quasistatics at the
background's a₀(t). Precedent named: unimodular gravity's global volume
constraint — same structure, known safe. Worker's named-assumption flag
kept. Two benign caveats carried (percent-level adiabatic drift;
homogeneous khronon gradient is AeST's own setup). **Clock pinned** (five
clock-class errors this session demand it): â₀(z) = (2/3)λc₀H_τ̂(z),
charter identity, exact; absolute anchor verified inline — (2/3)λc₀H₀ =
1.386e-10 vs cdot-7's fitted 1.39e-10 m/s² (absolute-anchor rule applied
on WP5's day one). Evidence-collapse statement carried verbatim: the
lensing curve is the SAME prediction as the dynamical â₀(z)/SN fit —
WP5's value is cross-probe consistency with zero freedom, not a new
curve. **Prediction backbone delivered**: â₀(z_lens)/â₀(0) = E(z_lens) =
1.06/1.16/1.24/1.36/1.60/1.86 at z = 0.1/0.25/0.35/0.5/0.75/1.0 —
low-acceleration RAR branch shifts by √E (11% at z=0.35, 17% at 0.5),
within stacked-survey precision; live and falsifiable both ways
(redshift-independent-a₀ findings would pressure it directly). **m_×
question given its structural expected answer to test**: AeST's m_× term
belongs to the dust-mimicking scalar cdot-8's charter discards — if no
analog survives in the closed action, the two-limit question dissolves,
the quasistatic sector is pure AQUAL, and the low-acceleration lensing
RAR stays MOND-like (consistent with the Mistele-McGaugh-Hossenfelder
data that pressures vanilla AeST) — a distinguishing advantage claimed
only if the inspection delivers it (verdict-scoping rule). **Housekeeping**:
Foundation §6 item 6 decision remains the standing gate (WP5 is
legitimate parallel work; the decision must not age out silently);
worker's adjudication confirmation still pending; worker's log companion
says "new" for a file already carrying two advisor entries — Entry-9 rule
flagged again, plus the 07-16 overwrite repair.

**Files produced (Entry 3):**
`Advisory-WP5-DecouplingConfirmed-2026-07-17.md`,
`wp5_decoupling_check.py`, `SessionLog-2026-07-17.md` (this file, three
entries).

**Open items handed forward:** second installment — (a) m_× inspection
first (expectation pre-registered), (b) lensing-RAR-by-lens-redshift
confrontation on the backbone, (c) Mistele two-limit only if (a) finds a
survivor; worker confirmation of the normalization adjudication; **the
author's Foundation §6 item 6 decision — still the gate**; consolidation
batch; worker log repairs (overwrite + numbering + Entry-9); **the KATRIN
clock remains the program's most time-critical item.**

---

## Entry 4 — WP5 m_× adjudication: worker's core finding confirmed against the fetched primary source; the tested hypothesis bundled two scales (advisor error #6); lensing-tension attribution reverses to the m-channel; RAR curve unblocked; zero-freedom m_eff task pre-registered (advisor session, 2026-07-17, ~15:0x SAST)

**Prompt (verbatim):**
> Worker has tested and found the claim to fail.
> [uploaded: `Update-WP5-WeakFieldStructure-2026-07-17.md` with new §6a —
> worker checks the pre-registered m_× hypothesis against Mistele
> arXiv:2305.07742, transcribes its Eq. (1), finds m_× = Q₀√((2−K_B)/2K_B)
> with no J-dependence, flags a "notational collision" (Mistele's Q₀ a
> fixed constant, claimed unrelated to the program's Q(t)), concludes the
> hypothesis fails, that "the m_× ambiguity, and the associated known
> weak-lensing tension it produces, very likely persists in cdot-8 exactly
> as in vanilla AeST," and carries the two-limit question forward as
> blocking the lensing-RAR curve.]

**Summary (advisor; primary source fetched in full — arXiv:2305.07742v3 =
PRD 110, 024062; skeleton in `meff_skeleton.py`):** **Split adjudication.**
(1) **Worker's core finding CONFIRMED exactly**: m_× is built from K_B and
Q₀ only, no free-function dependence; replacing F(Q) cannot remove it; the
pre-registered hypothesis as stated fails, test correctly executed. (2)
**But the hypothesis bundled two scales — advisor error #6 (source
misattribution), owned; worker inherited the bundle.** The paper explicitly
separates m (ghost-condensate mass: "controls whether AeST reproduces
MOND," sets r_c = (r_M f_G/m²)^{1/3}, constrained by MMH 2023 A&A 676 A100
— THE weak-lensing tension — and THE dust-mimicking device) from m_×
("not related to the ghost condensate... does not affect the ability of
AeST to reproduce MOND... not yet constrained phenomenologically").
Worker's "tension persists exactly as in vanilla AeST" attaches to the
wrong scale — the tension lives in the sector cdot-8's charter discards.
(3) **Q₀ flag over-corrected**: Mistele's Q₀ is the frozen background
condensate chemical potential — the same object cdot-8 evolves as Q(t),
adiabatically frozen for quasistatics; consequence: m_× and m_eff inherit
epoch dependence Q(z). (4) **The corrected zero-freedom task**: cdot-8's
closed action has no native m² term, but δQ = δφ̇ − Q₀Φ means the
quadrature F generates m_eff² ~ ½Q₀²F_QQ(Q₀) — computable, no tuning
escape in either direction (AeST can tune m; cdot-8 cannot). Skeleton
pre-registered: F_QQ(1, today) = −0.696 (H₀² units; inline check F/Ω_s =
+1.82 vs +1.77 ✓) → m_eff ~ 1.4e-4/Mpc (1/m_eff ≈ 7300 Mpc, ~7000× lighter
than AeST's chosen 1/Mpc, because cdot-8's F is Hubble-scale by
construction) → r_c(1e11 M_sun) ≈ 80 Mpc ≫ 1–3 Mpc survey radii →
condensate negligible at all lensing scales → MOND persists → consistent
with the MMH data that pressures vanilla AeST — the distinguishing
advantage returns via the m-channel, claimed only if the careful pass
confirms. Careful-pass flags: F_QQ < 0 sign/stability treatment explicit;
m_eff(z) along the trajectory; the f_G/16πG̃ dictionary done slowly (the
advisor's own cross-frame error record demands the skeleton be treated as
target, not result). (5) **RAR curve UNBLOCKED**: the paper's own
quantitative conclusion — m_× effects sub-percent for galaxy observables,
percent-level only for wide binaries (not WP5's deliverable); survey lens
scales sit in the two-field limit (m_×l ≪ 1) → the
lensing-RAR-by-lens-redshift confrontation proceeds now on the E(z)
backbone with a sub-percent m_× systematics line; two-limit question
demoted to wide-binary footnote.

**Files produced (Entry 4):**
`Advisory-WP5-ScaleUnbundling-2026-07-17.md`, `meff_skeleton.py`,
`SessionLog-2026-07-17.md` (this file, four entries).

**Open items handed forward:** worker: §6a correction (m vs m_× attribution
+ Q₀ softening) and errata; second installment — (a) careful m_eff
normalization pass vs the pre-registered skeleton, (b) lensing-RAR
confrontation vs Brouwer 2021 / Mistele et al. 2310.15248; WP4b
adjudication confirmation + errata chain still owed; consolidation batch
(+error #6); log repairs (07-16 overwrite + numbering + Entry-9); **the
author's Foundation §6 item 6 decision on WP4a — still the standing gate**;
**the KATRIN clock remains the program's most time-critical item.**

---

## Entry 5 — WP5 dictionary delivered: SZ stability paper (2109.13287) resolves all three §6c blockers; Q₀ confirmed verbatim; exact μ² = −Q₀²F_QQ/(2(2−K_B)); F_QQ<0 is the stability-required sign; conclusion exact and K_B-bracketed; §7 staleness flagged (advisor session, 2026-07-17, ~17:0x SAST)

**Prompt (verbatim):**
> One more touch point on WP5.
> [uploaded: `Update-WP5-WeakFieldStructure-2026-07-17.md` with new §6b/§6c —
> worker accepts the m-vs-m_× correction with their own primary-source
> re-check and corrects §6a explicitly; records the Q₀ characterization as
> "genuinely unresolved" (not confirmed in Mistele's paper itself);
> reproduces the m_eff skeleton numerically and accepts the qualitative
> Hubble-scale conclusion; attempts the careful pass, confirms the
> quadratic δQ² piece structurally, and stops honestly at three blockers —
> (i) the Q-vs-Y=(∇φ+Q₀A)² map, (ii) the f_G/G̃↔Ĝ factor, (iii) whether
> F_QQ<0 is a ghost/tachyon — recommending a touch point with the advisor
> before deriving the full second-order action from scratch. §7 status
> unchanged, still routing the RAR curve behind the two-limit question.]

**Summary (advisor; source fetched in full — Skordis & Złośnik PRD 106,
104041 = arXiv:2109.13287v2; numerics in `meff_exact_dictionary.py`):**
**All three blockers dissolve against the one source where the condensate
mass is actually defined.** (1) **Q₀ closed verbatim**: SZ state — on FLRW
"Q → Q̄ = φ̄̇"; "K(Q̄) has a minimum at Q₀"; quasistatics live "in the late
universe where the time derivative of the background field has settled in
its minimum Q₀... expand φ = Q₀t + ϕ." Mistele's Q₀ IS the frozen
background φ̇ — the advisor's characterization confirmed at the primary
source, the worker's demand for exactly that anchor vindicated. cdot-8
difference noted for the write-up: AeST settles at a minimum (F_Q = 0);
cdot-8 slides under M5 (F_Q ≠ 0 = the invoice); linear δQ term =
background e.o.m., mass term unaffected. (2) **Exact dictionary**: SZ Eq.
10 gives K₂ = −F_QQ/4; SZ Eq. 58 gives μ² = 2K₂Q₀²/(2−K_B) =
−Q₀²F_QQ/(2(2−K_B)) — sector-additive at quadratic order (no Y-map
computation; the |Y|^{3/2} term contributes nothing at second order per
SZ, so the evolving a₀(Q) coefficient cannot leak into μ²);
Q-renormalization invariant (Q₀²F_QQ unchanged under Q → sQ — the "Q₀=1"
convention safe); no G factors in μ² at all (f_G renormalizes G_N, blocker
ii moot). (3) **Sign resolved favorably**: SZ stability demands K₂ > 0 ⟺
F_QQ < 0 — the quadrature's −0.696 gives K₂ = +0.174: the tachyon worry
inverts into a passed stability check. Cross-paper consistency: SZ's M² at
λ_s→0 = 2m_×² in Mistele's notation ✓. (4) **Numbers, exact and
K_B-bracketed**: 1/μ = 5.1–10.0 Gpc across K_B ∈ [0.1,1.5]; r_c(1e11
M_⊙) = 64–100 Mpc ≫ 1–3 Mpc survey radii. AeST must impose μ⁻¹ ≳ Mpc by
hand (SZ verbatim); cdot-8 gets Gpc for free from the invoice —
3+ orders of margin, immune to O(1) residue. Bonus: SZ's k < μ
unbounded-Hamiltonian window moves from sub-horizon (AeST) to
super-horizon (cdot-8), where SZ's own caveat hands over to FLRW/M5. **One
worker verification remains**: cdot-8's F occupies SZ's −F(Y,Q) slot with
matching sign (the WP0/WP3 Friedmann cross-check, sign made explicit).
(5) **§7 staleness flagged**: still routes the RAR curve behind the
two-limit question, contradicting the §5 unblock and the worker's own §6b;
rewrite directed — the lensing-RAR confrontation is WP5's only remaining
deliverable and nothing blocks it.

**Files produced (Entry 5):**
`Advisory-WP5-DictionaryDelivered-2026-07-17.md`,
`meff_exact_dictionary.py`, `SessionLog-2026-07-17.md` (this file, five
entries).

**Open items handed forward:** worker: F-slot sign verification (one
line); §7 rewrite; then the lensing-RAR-by-lens-redshift confrontation
(Brouwer 2021, Mistele et al. 2310.15248; E(z) backbone; μ(z) cutoff line
optional); WP4b adjudication confirmation + errata chain still owed;
consolidation batch (+μ² dictionary, +Q₀ closure, +§6c-restraint worked
example); log repairs (07-16 overwrite + numbering + Entry-9); **the
author's Foundation §6 item 6 decision on WP4a — still the standing
gate**; **the KATRIN clock remains the program's most time-critical
item.**

---

## Entry 6 — WP5 confrontation adjudicated and closed: §6c/§7 accepted (dictionary jointly verified, F-slot sign confirmed by worker); §8's restraint source-confirmed (pooled literature non-decisive both ways); differential intra-survey bin-ratio test designed; WP5 closes as pre-registered prediction + test design; WP5b scope flagged to author (advisor session, 2026-07-17, ~19:0x SAST)

**Prompt (verbatim):**
> Please check attached file for another touchpoiint.
> [uploaded: `Update-WP5-WeakFieldStructure-2026-07-17.md` with §6c rewritten
> (full independent line-by-line verification of the SZ dictionary via
> ar5iv, including the delegated F-slot sign check — SZ Eq. 1's
> −𝓕/(16πG̃) slot matches WP3's −(a³N/16πG̃)F(Q) — and the M²=2m_×²
> cross-paper algebra; superseded text kept in a details block), §7
> rewritten (staleness corrected; RAR confrontation the only remaining
> deliverable), and new §8: backbone cross-validated against cdot-7's own
> pre-existing fitted a₀(z) (read-only run: 4–5% offset at z=0.25, 1–2% at
> z=1.0; own table-misreading self-caught); literature reconnaissance
> (neither Brouwer 2021 nor Mistele et al. 2024 bins lenses by redshift —
> both pool 0.1<z<0.5, ⟨z⟩≈0.2–0.25, a₀ universal); the tempting naive
> comparison (pooled 1.24 vs predicted 12–16% enhancement) explicitly
> resisted pending three items: (i) papers' uncertainty structure, (ii)
> n(z) weighting, (iii) zero-point conventions.]

**Summary (advisor; sources: Brouwer A&A 650 A113, Mistele et al. JCAP04
(2024)020 at the level of their stated systematics; design in
`rar_bin_test_design.py`):** (1) **§6c/§7 accepted, closed** — the
dictionary is now a jointly-verified program result (μ⁻¹ ≈ 5–10 Gpc, r_c ≈
64–100 Mpc), delegated sign check confirmed by the worker independently;
goes to the consolidation batch. (2) **§8 backbone cross-validation
accepted**: two independent-origin constructions (cdot-7 data fit
pre-dating cdot-8 vs covariant closure) agree 4–5% (z=0.25) → 1–2% (z=1.0,
consistent with Foundation §5.5's 1.86 ✓); offset promoted to the
theory-side systematic band (±4–5% low-z → ±1–2% at z=1), with the design
consequence that only long redshift lever arms beat it. Worker's
self-caught table misreading noted — presentation-gap rule operating on
their side. (3) **§8 restraint source-confirmed on item (i)**: Mistele et
al. carry 0.1 dex (~26%) systematic on the ESD→acceleration conversion
alone; Brouwer et al. name the missing-baryon budget "the single most
severe limitation" — both floors exceed and are common-mode with the
12–16% pooled signal. Symmetric verdict: **the pooled literature can
neither confirm nor exclude â₀ ∝ H_τ̂** — no positive hint, small
evidentiary weight either way. Adjacent reportables: the z-binned lensing
RAR does not exist in the literature (genuine gap-finding); Brouwer's 6σ
early/late-type split is a named differential systematic for any binned
analysis (type mix drifts with z in flux-limited samples). (4) **Design
delivered — the observable that survives**: intra-survey differential bin
ratio R = a₀(z_hi)/a₀(z_lo) → E(z_hi)/E(z_lo), null R ≡ 1, amplitude √R
in deep-MOND lensing; zero-point, absolute M/L, and the 0.1 dex conversion
band cancel as common modes. Lever-arm ladder: 0.17/0.33 → 1.104 (~1σ,
not decisive); 0.15/0.45 → 1.208 (1.5–2σ); 0.2/0.6 → 1.292 (viable);
0.2/0.75 → 1.417 (decisive class); 0.2/1.0 → 1.651 (≫ theory band).
Scoping caution carried: this tests a₀-tracks-H vs a₀-constant, not
cdot-8's E-shape vs ΛCDM's (evidence-collapse identity, where it should
be). (5) **WP5 CLOSES** as: pre-registered prediction (E(z) curve +
theory band + √E amplitude law) + demonstrated literature gap +
differential test design with systematics budget and feasibility ladder —
complete, self-standing, registered before any binned data exist. Binned
catalog reprocessing = new data analysis, outside the loop's remit:
**WP5b-or-external-proposal is an author scope decision**, flagged
alongside — not instead of — the standing Foundation §6 item 6 gate.

**Files produced (Entry 6):**
`Advisory-WP5-ConfrontationDesign-2026-07-17.md`,
`rar_bin_test_design.py`, `SessionLog-2026-07-17.md` (this file, six
entries).

**Open items handed forward:** author: (a) Foundation §6 item 6 decision
on WP4a — the standing gate, input stable since the adjudication round;
(b) WP5b scope decision (binned KiDS analysis in-program vs external).
Worker: WP4b adjudication confirmation + errata chain (aging);
consolidation batch (now +μ² dictionary, +WP5 closure package, +error #6,
+K6 rules); log repairs (07-16 overwrite + numbering + Entry-9). **The
KATRIN clock remains the program's most time-critical item.**

---

## File closure — 2026-07-17 (appended 2026-07-18)

This file is complete at six entries. The two decision gates prepared at
its close (Foundation §6 item 6 on WP4a; WP5b scope) were resolved by the
author on 2026-07-18 — Gate 1: **(b), provisional structural failure**,
proceed through WP7 on current radiation-era assumptions before revisiting
them; Gate 2: **(a)**, WP5 closes as delivered, no WP5b, future-facing
predictions as the stated goal. Resolutions recorded in
`DecisionGates-2026-07-18.md`; the session record continues in
`SessionLog-2026-07-18.md` (this directory).
