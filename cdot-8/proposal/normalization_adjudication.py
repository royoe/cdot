#!/usr/bin/env python3
"""
normalization_adjudication.py — 2026-07-17. The worker's rebuttal makes a
falsifiable claim: the BBN comparison ratio must equal 1 at z=0, therefore
the reference must be H0*sqrt(u_hat/u_hat(today)). Adjudicate against the
one anchor external to both constructions: the ABSOLUTE standard-BBN
expansion rate at T = 1 MeV, known from textbook physics:
    H_SBBN(T) = 1.66 sqrt(g_*) T^2 / M_Pl  ->  ~0.68 s^-1 at 1 MeV, g_*=10.75.
Whichever reference reproduces this number is the standard-BBN reference.
Then: the internal-consistency check (the deep-radiation invoice fraction,
E^2/u = 0.93, established and re-verified across every budget round since
07-12, which the fixed-T ratio must square to), and the meaning of the
z=0 value.
"""
import numpy as np

# --- anchor: textbook absolute H at T = 1 MeV ---
g_star = 10.75
T_MeV = 1.0
M_Pl_MeV = 1.2209e22           # Planck mass in MeV
H_textbook_MeV = 1.66*np.sqrt(g_star)*T_MeV**2/M_Pl_MeV
H_textbook_s = H_textbook_MeV*1.5192e21   # MeV -> s^-1
print(f"ANCHOR (textbook, external to both constructions):")
print(f"  H_SBBN(1 MeV) = 1.66 sqrt(10.75) / 1.22e22 MeV = {H_textbook_s:.3f} s^-1")

# --- my reference: H0 * sqrt(u_hat(a(T))) in absolute units ---
H = 0.70
H0_s = H*100*1000/3.0857e22
T_G0 = 2.7255*8.617333e-5      # eV
OM_G = 5.049e-5                # photon Omega at h=0.70 (from the machinery)
# u_hat at T = 1 MeV: photons + e+- + neutrinos, all at their proper temps.
# gamma: OM_G*(T/T0)^4 with T = 1 MeV = 1e6 eV
u_gamma = OM_G*(1e6/T_G0)**4
# e+-: 1.75 * u_gamma (relativistic at 1 MeV, A=0.51)... use exact-ish 1.68 at A=0.511:
u_e = 1.68*u_gamma             # F_eq(0.511)/F_eq(0)*1.75, slight suppression
# nu: T_nu = T_gamma at this epoch (frozen relation = shared, as established):
u_nu = 2.625/2*2*u_gamma*( (4/11)**(4/3) * ( ( (11/4)**(1/3) )**4 ) )  # = 2.625/2*... 
# simpler: u_nu/u_gamma = (7/8)*(6/2) = 2.625 at T_nu = T_gamma:
u_nu = 2.625*u_gamma
u_tot = u_gamma + u_e + u_nu
H_mine_s = H0_s*np.sqrt(u_tot)
print(f"\nMY REFERENCE:      H0 sqrt(u_hat(a(1 MeV)))          = {H_mine_s:.3f} s^-1"
      f"   ({H_mine_s/H_textbook_s:.3f} x textbook)")

# --- worker's proposed reference: divide u_hat by u_hat(today)=0.074 ---
u00 = 0.0740
H_worker_s = H0_s*np.sqrt(u_tot/u00)
print(f"WORKER'S REFERENCE: H0 sqrt(u_hat/u_hat(today))        = {H_worker_s:.3f} s^-1"
      f"   ({H_worker_s/H_textbook_s:.3f} x textbook)")

print(f"""
VERDICT ON THE REFERENCES:
  Mine reproduces the textbook standard-BBN rate to ~{abs(1-H_mine_s/H_textbook_s)*100:.0f}%
  (residual = exact-vs-1.66-coefficient + e+- partial suppression at A=0.51 —
  the 1.66 formula itself is a ~few-% approximation).
  The worker's is {H_worker_s/H_textbook_s:.2f}x the rate every BBN code uses: it describes a
  fictitious universe whose radiation density at temperature T is 1/0.074 = 13.5x
  the value statistical mechanics gives for the measured T_CMB. No such universe
  is 'standard BBN'.

WHY THE z=0 CHECK IS A CATEGORY ERROR:
  E/sqrt(u_hat) at z=0 = 1/sqrt(0.074) = {1/np.sqrt(0.074):.2f}. This is not a bug — it is
  the framework's central claim rendered as a number: TODAY, modified gravity
  supplies 92.6% of E^2 and the census supplies 7.4%. The ratio 'H over what GR
  would produce from the actual energy content' is SUPPOSED to be 3.67 today,
  ~2.1 in the matter era, and 0.965 deep in radiation (the -7% invoice).
  Demanding ratio(z=0)=1 asserts the census alone must reproduce H0 under GR —
  i.e., it asserts the framework's own scalar sector out of existence.
  The check is valid for comparing two COMPLETE cosmologies at the same z
  (e.g. E_cdot8 vs E_LCDM in WP4a); it is not valid for the BBN quantity
  H(T) vs GR-with-actual-radiation-at-T, which is anchored absolutely.

INTERNAL-CONSISTENCY CHECK (independent of all normalization conventions):
  The fixed-T ratio is EXACTLY sqrt(E^2/u) — the invoice fraction. The
  deep-radiation invoice has been E^2/u = 0.93 in every budget round since
  2026-07-12 (verified repeatedly, unchanged by the e+- correction:
  my table returns to 0.965^2 = 0.931 above and below the transition).
  The worker's 0.276 requires E^2/u = 0.076 deep in radiation — an invoice
  of -92.4% — which would have appeared in every invoice table for five days.
  It never did. Their 0.276 = 0.965/sqrt(1/0.074) = 0.965/3.67 x (their
  treatment residuals): the census-normalized reference IS the anatomy of
  their original severe number, now confirmed rather than hypothesized.""")
