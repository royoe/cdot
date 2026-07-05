# SESSION LOG — z_rec Derivation and Constant c-Dependence Audit

**Topic:** Deriving z_rec from the model's own recombination physics; auditing the
c-dependence of constants (k_B, hbar, a_rad) in the recombination sector.
**Date:** 2026-07-04 / 2026-07-05 (UTC).
**Outcome:** Constructive — confirmed R_rec≈20.6 on firmer footing; closed two
escape routes for z_rec; localized the remaining problem to a kinetics question.
One update note.

---

## Timeline

**Prompt — "why is z_rec≈190 implausibly low?"**
- Showed my "implausible" was LCDM intuition. Derived the model's own c-threshold
  z_rec from Saha with E_bind∝c^2, T_eff∝c: got z_rec~2e6 (not 1090, not 190).
  Showed the three values (190 wanted, 1090 borrowed, 2e6 predicted) are mutually
  inconsistent — the real problem.

**Prompt — "derive z_rec carefully; did we miss dependencies?"**
- Full Saha treatment tracking every factor; z_rec~2e6 robust. Sensitivity table
  found the lever is the exponent p in X∝c^p (p=E_bind exp − T exp). cdot-5 gives
  p=1→z~2e6; p≈2 needed for z~1090.

**Prompt — "microwaves are free photons, so constant not T."**
- Made precise as p=2 (frozen-quanta ionization, c^0). Got z_rec≈1237, l1≈304.
  Stress-tested: value forced (∝X0/ln pref), not tuned; ~900-1600 across 6 orders
  of nuisance inputs. Flagged the two-temperature usage as the residual assumption.

**Prompt — "derive the split, or word it clearly."**
- Term-by-term primitive analysis. Found: equilibrium Saha uses ONE temperature
  (T_eff∝c) for all three terms → p=1 → z~2e6. The p=2 split requires OUT-OF-
  equilibrium (frozen-quanta) ionization, only valid post-decoupling. Premises P4
  and n_gamma-conservation both point to p=1 (thermal, coupled) AT recombination.
  Conclusion: the split cannot be derived; consistent premises give p=1, reopening
  the crisis. One escape: sudden (decoupling-limited) recombination — needs a
  kinetics demonstration (rate vs H_hor).

**Prompt — "is it caused by eta and conserved n_b?"**
- No. eta enters only logarithmically; 1e12 in eta → <5x in z_rec. Driver is large
  X0=E_bind/(k_B T_0)~5.8e4 × weak p=1 scaling. n_b-conservation is a spectator
  (may re-enter via recombination RATE in the kinetics treatment).

**Prompt — "check constants for hidden c-dependence, esp. k_B and Stefan-Boltzmann."**
- Audit: k_B is convention (track k_B T, no c-dep); hbar fixed (confirm in T7);
  a_rad=π²k_B⁴/(15ħ³c³) ∝ c^-3 — the flagged one. With a_rad∝c^-3 and T_eff∝c:
  rho_gamma∝c^1, n_gamma∝c^0 (const ✓), <E_gamma>∝c^1, rho_b∝c^2.
  => R∝c^2/c^1=c^1=(1+z)^-1/2 = cdot-5's 20.6. CONFIRMED; a_rad already baked in.
  Original R=680 = omitting a_rad's c^-3.
  Saha exponent: ionizing energy ∝c^1 by TWO routes (thermal k_B T_eff and mean
  photon energy) → p=1 stands. a_rad fixes R sector, NOT z_rec.

**Prompt — "write it up."** Produced UPDATE_NOTE_Constants_c_Dependence_Audit.md.

---

## Key numbers
- R_rec = R_0(1+z)^-1/2 = 20.6 (confirmed via a_rad∝c^-3).
- z_rec: p=1 → ~2e6 (disaster); p=2 → ~1237 (l1≈304, works). eta moves it <5x/1e12.
- X0 = E_bind/(k_B T_0) ≈ 5.79e4; ln(prefactor) ≈ 52; z_rec ≈ (X0/ln pref)^2.
- Photon-sector c-scalings: a_rad c^-3, rho_gamma c^1, n_gamma c^0, <E_gamma> c^1, rho_b c^2.

## Artifacts produced
- `UPDATE_NOTE_Constants_c_Dependence_Audit.md`
- `SESSION_LOG_zrec_and_Constants_Audit.md` (this log)

## Net position
- R_rec≈20.6 confirmed and stable (constants validate it).
- eta and hidden constants ruled out as z_rec levers.
- z_rec, hence the first-peak l1, hinges SOLELY on sudden-vs-gradual recombination
  kinetics (p=2 vs p=1). l1≈304 must NOT be treated as established until the
  sudden-recombination case is made.

## Open next steps
1. THE decisive calc: recombination/photoionization rate vs H_hor at the candidate
   epoch — is freeze-out sudden (p=2, rescues CMB) or gradual (p=1, crisis)?
   Check whether n_b (eta) re-enters with leverage through the rate.
2. Confirm hbar is c-invariant in T7.
3. If sudden case holds: fold derived z_rec≈1240, l1≈304 into T16, close open item.
   If gradual: record the static-a CMB obstruction at Core level.
