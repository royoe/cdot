# Session Log — DESI DR2 BAO Confrontation (Update to T16)

**Date:** 2026-07-02
**Session window (UTC):** ~11:50 – 12:30 (continuation of the nine prior sessions of
this date, logged separately)
**Scope:** Execute the DESI DR2 BAO/Alcock–Paczyński confrontation — the test battery's
top-priority data test — presented as an update to T16.
**Outputs:** Update_2026-07-02_T16_DESI_BAO.md; this log
**Session classification:** Constructive, adverse result (decisive exclusion of the
geometric sector; one major collateral finding in T4's dilation chain)

---

## User Prompts

**[2026-07-02 ~11:50 UTC] Prompt 10 (this session):**

> Ok. Let's take a shot at DESI then. Present as an update to T16.

*(Prompts 1–9 and their results are in the session logs of this date.)*

---

## Session Activity (timestamps UTC, approximate)

- **11:52** — Setup validation. Established which observables the test depends on:
  transverse BAO is geometry (θ = L/D_p, straight lines in the static map), radial BAO
  is simultaneous spectroscopy (Δz per frozen proper ruler) — both immune to
  photon-rate effects. Noted D_H = dD_M/dz holds in any static monotonic mapping,
  exactly as in FRW, making the pipeline comparison convention-clean. While verifying
  the rate-immunity, found the §8 collateral issue in T4 (below).
- **11:56** — Verified DESI DR2 data via web search (arXiv 2503.14738/14739): 13
  measurements, 7 tracers, z_eff = 0.295–2.330, with per-tracer D_M–D_H correlations
  (ρ ≈ −0.40 to −0.46; ELG2/QSO approximated −0.44/−0.50, results insensitive).
  Fiducial-independence of the published values confirmed from the DR2 papers.
- **12:00 — Main fit.** Model: D_M/r_d = 6A[1−(1+z)^{−1/6}], D_H/r_d = A(1+z)^{−7/6},
  one nuisance A = (c/H₀)/r_d; full per-tracer 2×2 covariances. Results:
  **model χ² = 150.9** (13 pts, 1 param; best A = 35.19 ⇒ r_d = 121.7 Mpc at H₀=70) vs
  **ΛCDM χ² = 10.5** (2 params; Ω_m = 0.297, matching published DESI 0.2975 —
  pipeline validated). **Δχ² = +140.** Per-bin pulls: D_M high at low z (+2.6/+3.6/
  +2.7σ), D_H low mid-range (−6.9σ at z=0.934, −4.5σ at 1.321), BGS D_V +7.1σ, signs
  rotating by z = 2.33 — an unabsorbable z-dependent anisotropy.
- **12:05 — Parameter-free AP test.** F_AP = D_M/D_H with zero free parameters:
  **χ² = 67.8 for 6 points**; largest pull +6.7σ (z = 0.934); model high by 3.5–10%
  at 0.5 ≤ z ≤ 1.3, sign flipping at Lyα. Required-ruler analysis: transverse demands
  r_d = 119–126 Mpc, radial 112–122 Mpc, disagreeing by up to 10% at the same z —
  forecloses any L(z) ruler-evolution rescue.
- **12:10 — Family-level generalization.** Any static counting model:
  D_M ∝ [1−(1+z)^{−α}]/α, D_H ∝ (1+z)^{−(1+α)}, α = 1/(nP), from the exact
  D_p = R₀ − R_e. Free-α fit: α = 0.095 ± 0.010, χ² = 102.8 — still hopeless; AP-only
  wants α ≈ 0.05 (χ² = 35.7). The model's α = 1/6 is **7.1σ** from the least-bad
  member, which itself needs nP ≈ 10.5 — colliding with P = 2 (squared redshift law)
  and n = 3 (volume counting) and shifting q₀. General theorem noted: F_AP(z)
  determines D(z) ∝ exp∫dz/F completely; the data dictate ΛCDM's comoving shape,
  which no horizon-counting solution reproduces. **The exclusion lands on premises
  2 + 4, not on parameters.**
- **12:15 — Escape routes assessed:** (1) RSD/template systematics — only formal out;
  needs 20–100× DESI's systematic budget (+10% in F_AP vs 0.1–0.5% control), and a
  model-side anisotropic clustering pipeline to even claim it; (2) ruler evolution —
  foreclosed (§4); (3) exponent change — foreclosed (§5, 7σ cross-dataset collision);
  (4) abandoning the counting mapping — fits, but is falsification, not escape.
- **12:18 — Separability statement:** the local-gravity program (diffusion, river,
  RAR closure, two-fluid) does not depend on the z(D) mapping — it needs a sea and a
  horizon scale. The falsification is of the static counting cosmology; the
  MOND-derivation core separates and survives on its own tests.
- **12:20 — Collateral finding (§8, assigned out):** two photons in a spatially
  uniform medium with growing c(t) keep a frozen spatial gap c_e·dt_e, closed at
  reception at c₀ ⇒ arrival compression dt₀ = dt_e(1+z)^{−1/2} — omitted from T4's
  dilation chain ("arrival duration stretched by (1+z)" uses clocks only). If
  confirmed: light-curve dilation exponent 1/2 (vs DES-SN's measured 1 at sub-percent
  precision — an independent exclusion) and D_L = (1+z)^{3/4}D_p. Per-photon
  frequency unaffected (ω conserved, λ ∝ c(t) stretches; P = 2 redshift law safe);
  BAO unaffected. Needs a dedicated T2/T4 session.
- **12:25** — Wrote the T16 update with the six-item edit list and status changes.

## Results Summary

1. **The model fails the DESI DR2 BAO test decisively:** Δχ² = +140 (12σ-equivalent)
   with one fewer parameter than ΛCDM; zero-parameter AP channel alone χ² = 67.8/6.
2. **No rescue within the framework:** ruler evolution foreclosed by the
   radial/transverse required-ruler split; exponent changes foreclosed at the family
   level (best member still χ² = 103 and 7σ-inconsistent with the SN/age sector);
   only the quantitatively implausible RSD-template route remains formally open.
3. **The exclusion is premise-level:** the data's F_AP(z) dictates a
   redshift–distance mapping that no horizon-counting solution reproduces —
   premises 2 + 4 as constituted are falsified in the geometric channel.
4. **Separability:** the connecton local-gravity program is independent of the
   mapping and unaffected; it remains the framework's living core.
5. **Collateral major finding:** T4's time-dilation chain omits the photon
   arrival-rate compression (1+z)^{−1/2}; if it stands, the predicted dilation
   exponent is 1/2 against a sub-percent measurement of 1 — a second, independent
   falsification channel. Top-priority follow-up.

## Merge Recommendation

Merge the T16 update as written — the project's ethos requires the adverse result to
be recorded with the same prominence as the successes. Update Core §7's status table
in the same commit (edit 2) so the repository's headline claims stay honest. The §8
finding should get the next session before any further cosmological-sector work: it
is cheap to verify and, either way, decisive — confirmation closes the sector through
a second channel; refutation of my kinematic argument would require a premise-level
statement about photon propagation that the model currently lacks and needs anyway.
A separate decision session is then warranted on the program's structure: whether to
reconstitute the cosmological sector (new mapping premise) or to re-center the
project on the separable local-gravity/MOND-derivation core.
