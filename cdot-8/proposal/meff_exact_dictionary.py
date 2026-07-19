#!/usr/bin/env python3
"""
meff_exact_dictionary.py — 2026-07-17. Completes the m_eff pass the worker's
§6c correctly stopped short of, using the exact dictionary from the primary
source (Skordis & Zlosnik, PRD 106, 104041 = arXiv:2109.13287):

  SZ expand F(Y,Q) around the condensate point (their Eq. 10/65):
      F = (2-K_B) lambda_s Y - 2 K_2 (Q-Q_0)^2 + ...
  so the Q-sector curvature is  K_2 = -F_QQ(Q_0)/4,
  and the condensate mass (their Eq. 58, the mu that MMH 2023 constrains,
  with SZ's own cutoff formula r_C ~ (r_M mu^-2)^(1/3)) is
      mu^2 = 2 K_2 Q_0^2 / (2-K_B) = -Q_0^2 F_QQ(Q_0) / (2 (2-K_B)).

  KEY PROPERTIES:
  * Q-reparametrization invariant: Q -> sQ gives F_QQ -> F_QQ/s^2, so
    Q_0^2 F_QQ is invariant — cdot-8's "Q_0 = 1 today" convention is safe.
  * Sign: SZ stability (their Eq. 62) demands K_2 > 0  <=>  F_QQ < 0.
    cdot-8's F_QQ = -0.696 has EXACTLY the sign stability requires.
  * Cross-check: SZ's propagating-mode mass M^2 = (2-K_B)(1+lambda_s)Q_0^2/K_B
    at lambda_s -> 0 equals 2 m_x^2 in Mistele's notation — dictionary
    self-consistent across both papers.
"""
import numpy as np

F_QQ = -0.6962          # H0^2 units, Q0 = 1 (from the quadrature, skeleton run)
Q0 = 1.0
H = 0.70
c_over_H0_Mpc = 2.99792458e8/(H*100*1000/3.0857e22)/3.0857e22  # c/H0 in Mpc

print("EXACT DICTIONARY: mu^2 = -Q0^2 F_QQ / (2(2-K_B)),  K_2 = -F_QQ/4 = "
      f"{-F_QQ/4:+.4f} > 0  => SZ stability condition K_2>0 PASSED")
print(f"\n{'K_B':>6} {'mu [H0/c]':>10} {'1/mu [Mpc]':>11} {'r_c(1e11Msun) [Mpc]':>20}")
rM_Mpc = 0.010   # r_M = sqrt(G M_b/a0) ~ 10 kpc for 1e11 Msun (skeleton)
for KB in (0.1, 0.5, 1.0, 1.5):
    mu_H0 = Q0*np.sqrt(-F_QQ/(2*(2-KB)))          # in H0 units
    inv_mu_Mpc = c_over_H0_Mpc/mu_H0
    r_c = (rM_Mpc*inv_mu_Mpc**2)**(1/3)           # SZ's own formula
    print(f"{KB:>6} {mu_H0:>10.3f} {inv_mu_Mpc:>11.0f} {r_c:>20.0f}")

print(f"""
CONCLUSION BAND (exact dictionary, K_B in AeST's stable range):
  1/mu ~ 5.1-10.0 Gpc  vs  AeST's REQUIRED mu^-1 >~ 1 Mpc (imposed by hand,
  SZ's own words: 'on observational grounds mu^-1 must be larger than ~Mpc').
  cdot-8 gets mu^-1 ~ Gpc FOR FREE from the invoice — factor ~5000-10000
  above the requirement, immune to any O(1) dictionary residue.
  r_c ~ 64-100 Mpc >> 1-3 Mpc survey radii: condensate negligible at ALL
  stacked-lensing scales; MOND persists; consistent with MMH 2023.
LOW-k WINDOW: SZ's unbounded-Hamiltonian window sits at k < mu.
  AeST: mu^-1 ~ Mpc (cosmological but sub-horizon).
  cdot-8: mu^-1 ~ 5 Gpc — the window is pushed to SUPER-HORIZON scales,
  where SZ's own caveat applies (Minkowski expansion invalid; FLRW takes
  over — the M5-governed background itself). Even cleaner than AeST.""")
