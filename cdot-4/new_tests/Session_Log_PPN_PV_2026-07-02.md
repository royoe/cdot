# Session Log — PPN and Lensing: the PV-Symmetry Check (Local Gravity / Two-Regime Dictionary)

**Date:** 2026-07-02
**Session window (UTC):** ~08:30 – 08:55 (continuation of the same conversation as the
Consistency Audit and Test Battery sessions, logged separately)
**Scope:** Check whether the assumed symmetry with Polarizable Vacuum (PV) theory
preserves the model's alignment with weak-field GR phenomenology (PPN γ/β, light
bending, Shapiro delay, gravitational redshift, perihelion precession).
**Outputs:** Update_2026-07-02_PPN_PV_Local_Gravity.md; this log
**Session classification:** Constructive (assumption checked and resolved; one new
forced premise; two new open constraint classes; fork reframing)

---

## User Prompts

**[2026-07-02 ~08:30 UTC] Prompt 3 (this session):**

> As to PPM and lensing my assumptions have been that the symmetry with PV theory would
> preserve alignment. Can we check that?

*(Read as PPN. Prompts 1–2 and their results are in
Session_Log_Consistency_Audit_2026-07-02.md and Session_Log_Test_Battery_2026-07-02.md.)*

---

## Session Activity (timestamps UTC, approximate)

- **08:32** — Decomposed "PV symmetry" into two separable ingredients: (a) the K-field
  equation (coefficient A in K = 1 + A·GM/rc²), which alone controls light propagation
  since the model's EM sector forces n = K exactly; (b) the matter-response dictionary
  (exponent σ in m ∝ K^σ), which controls clocks, rulers, orbits. Tabulated the PV
  dictionary (m ∝ K^{3/2}, E ∝ K^{-1/2}, L ∝ K^{-1/2}) against the model's cosmological
  dictionary (m ∝ K⁰, E ∝ K^{-2}, L ∝ K^{+1}) — they share only the EM sector.
- **08:35** — Symbolic verification (sympy) of the two-test pincer:
  - Light deflection/Shapiro: n = K forces **A = 2** (for 1.75″ / Cassini
    γ−1 = (2.1±2.3)×10⁻⁵), independent of matter dictionary.
  - Gravitational redshift: ν ∝ m·ε₀⁻² ∝ K^{σ−2}; requirement (σ−2)A = −1 with A=2
    forces **σ = 3/2 — uniquely the PV mass law**.
  - Failure branches quantified: σ=0 kept locally → gravitational redshift **4× GR**
    (excluded by Galileo GREAT, (0.19±2.48)×10⁻⁵, at ~10⁴σ); renormalizing A=1/2 to fix
    clocks → light bending **¼× GR** (excluded by VLBI/Cassini). No intermediate (A,σ)
    exists.
  - Downstream matches verified: rulers a_B ∝ K^{−1/2} (γ consistency between light and
    rulers); rest energy and all local energies ∝ K^{−1/2} uniformly (EP clean,
    MICROSCOPE-safe); β=1 inherited from Puthoff's exponential-metric results at tested
    order.
- **08:38** — Consistency sweep of the resulting two-regime structure:
  - Core premise 3's wording ("independent of the **cosmological** vacuum state")
    already permits local gravitational dressing — clarification, not contradiction.
  - LLR: local dressing drifts only via K_grav ∝ c⁻²(t); with K_grav(Moon) ≈ 1.15×10⁻¹¹,
    secular effects ~10⁻²²/yr — negligible; the ×720 refutation of cosmological
    G ∝ c⁻² untouched.
  - Cosmological squared redshift law unaffected (galaxy potentials are the ordinary
    ~10⁻⁵ corrections).
  - α invariant locally too (ε₀c invariant in any regime).
  - T14 inertia no-go: compatible but wording must change to "axiomatic baseline m₀,
    locally dressed m₀K_grav^{3/2}."
- **08:40** — Identified the reframing: locally ν ∝ c^{1/2} is the **P = 1/2 PV-mass
  branch** that T1 (infinite proper age) and T4 rejected *cosmologically*. The
  invariant-vs-PV mass fork (T8) resolves as regime-split both/and: PV branch governs
  space (static gravity, forced by Cassini/GREAT), invariant branch governs time
  (cosmology, forced by Pantheon+/LLR).
- **08:45** — New exposures identified:
  1. **A = 2 must be derived** from connecton diffusion (δK = 2φ/c² — the
     time-plus-space factor 2); same epistemic status as invariant G until then.
     Sharpens T14 open item 5.
  2. **Preferred-frame PPN α₁ (<10⁻⁴), α₂ (<4×10⁻⁷)**: the sea frame gives
     (v/c)² ≈ 1.5×10⁻⁶ for the solar system's 370 km/s motion — raw scale an order of
     magnitude *above* the α₂ bound; the coefficient must be shown suppressed or zero.
     Now the sharpest unexamined solar-system threat to the program.
  3. **Lense-Thirring / frame dragging**: scalar PV has none; the connecton B_c
     machinery might supply it — untested two-sided check (GP-B ~20%, LAGEOS ~2%).
  4. **Seam rationale open**: candidate relational distinction — local K is a
     redistribution of connecton density at fixed global count; cosmological K is the
     count level itself. Recorded as a theoretical debt parallel to invariant G/m (T8).

## Results Summary

1. **The assumption is confirmed in conclusion, corrected in reasoning.** PPN/lensing
   alignment is preserved — but not by symmetry; only by reinstating the full PV matter
   dictionary *locally* (m ∝ K_grav^{3/2}), which the model rejected cosmologically. A
   uniform dictionary fails observationally by a factor of 4 in either direction.
2. **The local PV dictionary is uniquely forced** by bending (A=2) + gravitational
   redshift (σ=3/2), given the model's own EM sector — upgrading the assumption to a
   derived-but-unexplained structural premise (the Two-Regime Dictionary).
3. **Fork reframing:** the P=1/2 PV branch and the P=2 invariant branch both survive, in
   different regimes, each empirically forced in-domain.
4. **New threats registered:** the underived factor 2 in the K-field equation, and
   above all preferred-frame α₂ < 4×10⁻⁷ vs the model's raw (v/c)² ~ 10⁻⁶ scale;
   plus the Lense-Thirring/B_c check.
5. **Six-item edit list** (update doc §5): Core premise-3 clarification, T8 fork
   reframing, T1/T4 cross-notes, T14 open-item revisions, Test Battery Tier-1 item 3
   update, and a proposed new topic (T23 or a T22 section).

## Merge Recommendation

The algebra is elementary and was symbolically verified; edits 1–5 can be merged after
cross-checking the two exclusion branches (the ×4 redshift and ×¼ bending numbers) and
the Galileo GREAT / Cassini / α₂ bound citations. The α₁/α₂ computation and the
connecton derivation of A = 2 should each get a dedicated session; the α₂ check is
recommended first, since a non-suppressed coefficient would be fatal regardless of every
other success.
