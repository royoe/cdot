# Session Log — BAO Test Assumptions Audit (Addendum to the T16 Update)

**Date:** 2026-07-02
**Session window (UTC):** ~12:30 – 12:55 (continuation of the prior sessions of this
date, logged separately)
**Scope:** Author's challenge to the DESI test's early-universe assumptions: the
model's hot-plasma era is unworked, the working assumption had been
energy-scaling-identical initial conditions — re-check for misunderstanding.
**Outputs:** Addendum_2026-07-02_T16_BAO_Assumptions_Audit.md; this log
**Session classification:** Constructive (audit confirms the test; one new
constraint on the model's genesis epoch derived as a by-product)

---

## User Prompts

**[2026-07-02 ~12:30 UTC] Prompt 13 (this session):**

> Ok, there is definitely a missing ingredient here. BAOs are frozen in place since
> recombination, and we haven't really discussed how the hot plasma in the early
> epochs behaved in our model. My assumption was naively that the energy scaling
> should make the initial conditions identical in our model as in the standard model,
> but you must have used different conditions. Can you re-check the assumptions, and
> that there is no misunderstanding on this?

*(Prompts 1–12 and their results, including the DESI fit and the two figures, are in
the session logs of this date.)*

---

## Session Activity (timestamps UTC, approximate)

- **12:32** — Re-derived the failing quantity from scratch (third independent
  derivation, symbolic): dz/dD = (H₀^obs/c₀)(1+z)^{7/6} from the chain rule on
  1+z = (c₀/c_e)², D = ∫c dt, ċ/c = H₀^hor(1+z)^{-1/3}. Confirmed: every symbol is
  late-time; no plasma-era quantity can appear in dz/dD or D_p(z).
- **12:35** — Enumerated and audited the test's early-universe assumptions — exactly
  three: (i) one intrinsic scale (shared with ΛCDM analyses); (ii) statistical
  isotropy of the imprint — shown to be a symmetry THEOREM, not a plasma assumption
  (the imprint cannot know future lines of sight; homogeneity+isotropy of the static
  map force the 2-pt function to depend on proper |Δx| only), hence ANY imprint
  physics changes only the isotropic scale L, never the observed anisotropy — the AP
  channel is early-physics common-mode by construction; (iii) frozen proper length —
  forced by staticity. Everything else, including the value of r_d, was marginalized.
  Sanity check: the fitted 122 Mpc ruler reproduces the raw BAO angles (4.2° at
  z=0.5 vs ΛCDM's 4.3°); the failure is exclusively the radial/transverse
  required-ruler split.
- **12:40 — The identical-initial-conditions intuition, quantified:** ΛCDM's r_d =
  147.1 Mpc comoving = 0.134 Mpc PROPER at z=1100. Identical local physics at
  recombination would imprint the same proper scale; ΛCDM stretches it ×1101, the
  static model freezes it — a frozen 0.134 Mpc ruler is ~900× too small. Taken
  literally, the assumption adds a three-orders-of-magnitude normalization failure on
  top of the shape failure. The r_d-marginalization in the test was therefore maximal
  charity, not a different condition.
- **12:44 — NEW RESULT (by-product):** the model's own sound horizon in static space:
  L_s = (1/√3)∫c dt = (R_rec − R_gen)/√3, with R(z) = R₀(1+z)^{-1/6} and the model's
  recombination at z ≈ 1100 (same local atomic threshold; T(z) = T₀(1+z) exact).
  R_rec = 8.0 Gpc. Perturbations from the BBN epoch (z ~ 10¹⁰) give L_s = 4.3 Gpc —
  35× too large. Requiring L_s = 122 Mpc forces the acoustic/perturbation era to span
  only z ≈ 1290 → 1100 (z_gen/z_rec = 1.17) — the model's first quantitative
  constraint on its own genesis epoch, and a concrete falsifiable target for T16's
  PBH-genesis gate. Corollary: the model's plasma era cannot be a relabeled ΛCDM
  plasma era on the model's own kinematics.
- **12:48 — Residual channel restated:** RSD/template only; narrowed further by
  noting DESI fits the RSD amplitude (does not assume ΛCDM's) and reconstruction
  hardens the peak position; the rescue needs a coherent ~10% peak-position
  anisotropy bias from a velocity theory the model has not proposed, in a framework
  with no derived growing mode. Formally open; model-side ξ(s,μ) required to close.
- **12:52** — Wrote the addendum with the three-item edit list.

## Results Summary

1. **No misunderstanding found; the test stands.** The early universe enters the BAO
   test through a symmetry-forced isotropy, a staticity-forced frozenness, and a
   fully marginalized ruler value. The failing quantity (dz/dD vs D_p) is pure
   late-time kinematics — re-derived a third time to be sure.
2. **The identical-initial-conditions assumption is quantitatively self-defeating:**
   it would impose a frozen 0.134 Mpc proper ruler, ~900× too small; the test's
   marginalization protected the model from this.
3. **New constraint (silver lining):** the model's own r_d formula,
   L_s = (R_rec − R_gen)/√3, requires z_gen ≈ 1300 for a viable ruler — either the
   genesis gate is that late, or the model's ruler is Gpc-scale and the normalization
   fails independently of the shape.
4. The exclusion verdict of the main T16 update is unchanged; it is hardened by the
   audit.

## Merge Recommendation

Merge the addendum together with the main T16 update — the assumptions subsection
answers, in advance, the most natural objection any reader of the adverse result will
raise, and the genesis-epoch constraint gives T16's PBH-gate section its first
quantitative anchor. The RSD residual remains the only formally open channel and its
closure condition (a model-side anisotropic clustering computation) is already
recorded. Recommended next session remains the §8 photon-compression finding from the
main update: cheap to verify and decisive through an independent channel.
