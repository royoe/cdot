#!/usr/bin/env python3
"""
wp4b_check.py — 2026-07-16. Verification of the WP4b leading-order claims.
(1) F_eq limits and the e+/- -to-photon RATIO (worker's prose says 3.5; check).
(2) The Delta N_eff arithmetic from their H-ratio table.
(3) Reverse-engineer their D/H number: did they fold in the omega_b lever?
(4) Leading-order Li-7 estimate (absent from their update).
(5) The pre-annihilation neutrino-temperature question: what the census
    machinery currently assumes vs what the BBN window requires.
"""
import numpy as np
from scipy.integrate import quad

# (1) F_eq and the ratio
def F_eq(A):
    return quad(lambda x: x*x*np.sqrt(x*x+A*A)/(np.exp(np.sqrt(x*x+A*A))+1), 0, 200, limit=500)[0]
F_bose = quad(lambda x: x**3/(np.exp(x)-1), 0, 200, limit=500)[0]   # per-dof photon integral
print("(1) e+- to photon energy ratio at A=0:")
print(f"    per-dof fermion/boson = {F_eq(0)/F_bose:.4f}  (expect 7/8 = 0.875)")
ratio = 4*F_eq(0)/(2*F_bose)
print(f"    u_e+-/u_gamma = (4 dof x F_eq)/(2 dof x F_bose) = {ratio:.4f}  (correct value: 7/4 = 1.75)")
print(f"    worker's prose claims 3.5 -> that is the g_*-UNITS contribution (vs photon's 2),")
print(f"    not the ratio. Factor-2 prose slip; code disposition unknown until confirmed.")
print(f"    Boltzmann check: F_eq(50)/F_eq(0) = {F_eq(50)/F_eq(0):.2e} (worker: ~1e-19)")

# (2) Delta N_eff arithmetic from H ratio 0.94
Hr = 0.94
g_star_BBN = 2 + 3.5 + 2*3*0.875   # gamma + e+- + 3 nu species at T_nu=T_gamma (pre-annihilation): 2+3.5+5.25
dg = (Hr**2 - 1)*g_star_BBN
dNeff = dg/1.75                     # one nu species = 7/8 x 2 dof = 1.75 g-units
print(f"\n(2) H/H_std = 0.94 -> Delta g_* = {dg:.2f} of g_* = {g_star_BBN}")
print(f"    Delta N_eff = {dNeff:.2f}   (worker: -0.7)  ✓ arithmetic consistent")

# (3) D/H decomposition
# standard sensitivities: dln(D/H)/dN_eff ≈ +0.135 ; dln(D/H)/dln(omega_b) ≈ -1.6
dln_D_Neff = 0.135*dNeff
dln_D_omb  = -1.6*np.log(0.0217/0.0224)
print(f"\n(3) D/H: Delta N_eff term = {dln_D_Neff*100:+.1f}%  omega_b term = {dln_D_omb*100:+.1f}%")
print(f"    net = {(dln_D_Neff+dln_D_omb)*100:+.1f}%  -> D/H = {2.53*np.exp(dln_D_Neff+dln_D_omb):.2f}e-5")
print(f"    worker's 2.47e-5 = -2.4% -> consistent ONLY if omega_b lever was folded in (not stated)")

# Y_p cross-check: dY_p/dN_eff ≈ 0.013; omega_b term small
Yp = 0.247 + 0.013*dNeff - 0.0043*np.log(0.0224/0.0217)
print(f"    Y_p = {Yp:.4f}  (worker: 0.238) ✓ ; obs 0.2453+/-0.0034 -> tension = {(0.2453-Yp)/0.0034:.1f} sigma")

# (4) Li-7 leading order: dln(Li)/dN_eff ≈ +0.4 (approx, via Be-7 channel); dln(Li)/dln(omega_b) ≈ +2
dln_Li = 0.4*dNeff + 2*np.log(0.0217/0.0224)
print(f"\n(4) Li-7 leading-order: {dln_Li*100:+.0f}% vs SBBN (observed deficit needs ~-65 to -70%)")
print(f"    direction favorable, magnitude ~40% of the needed shift — same verdict as the hunt")

# (5) the nu-temperature question
print(f"\n(5) census machinery nu term: REL=(7/8)(4/11)^(4/3) x interp — assumes POST-annihilation")
print(f"    T_nu at ALL z. Correct at z < ~1e9 (WP4a unaffected: r_s converged below there).")
print(f"    In the BBN window (T=2->0.05 MeV, z~1e10->2e8) the pre-annihilation era has T_nu=T_gamma:")
pre = 2 + 3.5 + 5.25       # correct g_* at T ~ 1-2 MeV
machinery_nu = 3*0.875*2*(4/11)**(4/3)  # what REL-scaling gives, in g-units
pre_machinery = 2 + 3.5 + machinery_nu
print(f"    correct g_*(1 MeV) = {pre:.2f}; machinery-scaled nu gives {pre_machinery:.2f}")
print(f"    -> u underestimated by {(1-pre_machinery/pre)*100:.0f}% at T>~m_e IF the WP4b run kept the")
print(f"    machinery's nu scaling. H ratio error ~ {(1-np.sqrt(pre_machinery/pre))*100:.0f}% — same order as the")
print(f"    signal being computed. Needs worker confirmation of what their code did.")
