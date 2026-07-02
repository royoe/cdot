# Session Log — New Observational Tests for the Model (Test Battery / T22 Proposal)

**Date:** 2026-07-02
**Session window (UTC):** ~08:05 – 08:30 (continuation of the same conversation as the
Consistency Audit session logged separately)
**Scope:** Survey of observational probes beyond those in T1–T21; current (2025–2026)
observational landscape; new derivations where the model's prediction was computable.
**Outputs:** Update_2026-07-02_Observational_Test_Battery.md; this log
**Session classification:** Constructive (three new derived results, one sign
correction to T15, one new topic proposed)

---

## User Prompts

**[2026-07-02 ~08:05 UTC] Prompt 2 (this session):**

> Considering the current state of standard cosmology, are there any other observational
> results that we could use to challenge the proposed model?

*(Prompt 1 and its results are in Session_Log_Consistency_Audit_2026-07-02.md.)*

---

## Session Activity (timestamps UTC, approximate)

- **08:06** — Web search: DESI DR2 status. Confirmed: percent-level BAO distance ratios
  over the full survey range; evolving-dark-energy preference 2.3σ (Pantheon+) to
  ~3–4σ (DES-SN5YR combinations), dataset-dependent and contested (CMB/BAO/SN
  cross-tensions; neutrino-mass tension at ~3σ pushing toward negative masses under
  ΛCDM). Relevance: the standard model's own strain increases the value of
  calibration-light geometric tests; SN-calibration residuals are acknowledged even
  within mainstream analyses (relevant to T4's Framing 2).
- **08:08** — Web search: T_CMB(z) constraints. β = 0.022 ± 0.018 in T(z)=T₀(1+z)^{1−β}
  (SZ, 104 clusters); absorber measurements to z≈3 (e.g. 7.9±1.0 K at z=1.97);
  Chluba (2014) objection that non-standard TRR requires FIRAS-visible spectral
  distortions.
- **08:10** — Derivations computed and numerically verified:
  1. **Redshift drift:** dt_e/dt₀ = (1+z)^{1/2} from fixed D; result
     ż = H₀^obs(1+z)[1−(1+z)^{1/6}] — negative at all z, opposite sign to ΛCDM for
     z ≲ 2; velocity drift −0.15 to −0.75 cm/s/yr over z = 0.5–5.
  2. **Effective radial rate:** H_eff(z) ≡ c/(dD_p/dz) = H₀^obs(1+z)^{7/6}; 17–28%
     above ΛCDM E(z) with ~10% shape variation across the DESI range; AP parameter
     F_AP = D_M·H/c deviates +9.1% (z=0.51), +8.2% (z=1.0), −1.6% (z=2.33) — a
     sign-changing, r_d-free signal vs 1–2% data. Identified that chronometer-H
     (∝(1+z)^{2/3}, proper-time) and BAO-H (∝(1+z)^{7/6}, geometric) are *different
     observables* in this model, differing by (1+z)^{1/2} — itself a distinctive
     prediction, and the resolution of audit item II.7.
  3. **T(z) relation:** photon spectrum Planck at constant absolute T in flight (no
     FIRAS distortion); absorber transition energies lower by (1+z)^{-1}; reported
     temperature T(z) = T₀(1+z) exactly (β=0). Automatic pass; SZ channel flagged as
     an open sub-check.
- **08:12** — **T15 sign error found:** with g†(z) ∝ (1+z)^{-5/6} smaller in the past
  and g_bar(r) time-independent (static orbits, invariant M), the MOND region
  g_bar < g† *shrinks* at high z (r_t ∝ (1+z)^{+5/12} larger in the past — T19 §6
  already states this correctly). T15's claim of "a larger fraction of the disk
  dynamically MOND-like at high z" is backwards. Corrected implication: high-z disks
  more Newtonian, declining outer rotation curves, lower BTFR zero-point — the
  direction of the Genzel/Lang (2017) high-z declining rotation curves, awkward for
  constant-a₀ MOND. Converted from an error into a live testable signature.
- **08:15–08:25** — Assembled and prioritized the full battery (see update doc):
  Tier 1 (data exist, computable now): BAO/AP anisotropy; T(z) [passed]; solar-system
  PPN γ (Cassini 10⁻⁵) as the tightest ignored constraint on connecton gravity; cluster
  missing mass / Bullet Cluster (sharpens audit item III.1 into an observational
  requirement). Tier 2 (needs model development): redshift drift (ELT-ANDES); precision
  D/H BBN (inputs now available from T21); structure growth fσ₈/RSD (entirely unworked,
  highest-stakes gap after CMB); GW standard sirens + c_gw premise; cosmic-chronometer
  vs BAO H(z) split. Tier 3: μ = m_p/m_e and clock-ratio invariance (automatic pass);
  cosmic dipoles (potential advantage — model has a preferred frame); two-sided age
  test (>14.5 Gyr object would confirm model, falsify ΛCDM); high-z RAR/BTFR evolution;
  FRB dispersion measures. Non-discriminating (recorded to close off): SN time
  dilation, Tolman SB, D_L/D_A duality, laboratory ċ searches.

## Results Summary

1. **Three new derived predictions** merged into the proposed T22: ż(z) (sign-opposite
   to ΛCDM), H_eff(z) = H₀(1+z)^{7/6} with AP deviations of 2–9%, and T(z) = T₀(1+z)
   (exact pass, β=0).
2. **One correction:** T15 MOND-fraction sentence reversed (T19 was already right);
   downstream edits to T6/T17 wording.
3. **One priority reordering:** PPN/light bending promoted to the top of T14's open
   items; BBN D/H elevated in T13.
4. **One structural sharpening:** the Bullet Cluster / cluster missing-mass data make
   the PBH-vs-RAR division of labour (audit item III.1) an observational requirement
   (PBHs must dominate clusters, not inner galaxies), not merely an internal tension.
5. **Identified the model's most distinctive near-term signature:** chronometer-H and
   BAO-H must disagree by (1+z)^{1/2} here and agree in ΛCDM.

## Merge Recommendation

Create T22 from the update document after cross-checking the three derivations
(especially the dt_e/dt₀ step in the drift formula and the static-ruler AP mapping).
Apply the T15 sign correction immediately — it is unambiguous and T19 already contains
the correct statement. The AP comparison should be re-run against the actual DESI DR2
D_H/r_d, D_M/r_d, and F_AP data vectors in a dedicated session before any exclusion
language is used.
