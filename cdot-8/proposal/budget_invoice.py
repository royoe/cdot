#!/usr/bin/env python3
"""
budget_invoice.py — 2026-07-12, advisory companion (second WP3 escalation).

Computes the *demanded* gravity-sector energy density ("the invoice") along the
ACTUAL fitted census trajectory — not the idealized fixed-point-through-today
solution the worker (and the advisor's first reply) used.

Chain:
  closure ODE (coordinate time)  ->  E(a) = H_tau/H_tau0 via the two-clock
  dictionary  ->  Friedmann accounting  ->  rho_s(a) = 3H_tau^2/8piG - rho_census(a).

Key formula (derived in the advisory, §2):
  E(s) = e^{-3s/2} * x0 / (x(s) r(s)),   a = e^{3s/2},  1+z = e^{-3s/2}.
  [check: on a fixed point x=x*, r ∝ e^{(1-n/2)s}: matter FP -> E ∝ a^{-3/2},
   radiation FP -> E ∝ a^{-2}, i.e. H^2 ∝ a^{-3}, a^{-4} — Friedmann-shaped.]

Outputs:
  (0) sanity: worker's Omega_closure formula; idealized-FP shortfall (their 13.3);
  (1) E^2 a^3 plateau in the matter era (demanded Omega_m,eff);
  (2) rho_s a^3 plateau (the dust-like invoice amplitude);
  (3) radiation era: E^2/u_census ratio and the effective Delta-N_eff at BBN;
  (4) w_s(a) landmarks of the invoice component;
  (5) comparison of E^2(a) against flat LCDM (0.315, 0.685) out to z=1100.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import interp1d
from scipy.special import zeta

# ---- working cosmology (as census_closure.py) --------------------------------
KL, X0 = 0.4355, 1.10
LAM = 0.3056
T_G0, A_RAD, C0, G_N, H = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11, 0.70
K_B_EV = 8.617333e-5
rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)
u_g0 = A_RAD*T_G0**4
OM_G = (u_g0/C0**2)/rho_crit
T_NU0 = (4/11)**(1/3)*T_G0
M_NU = 1.374/3
OM_CL = 0.074

def mu_s(x):  return x/(1+x)
def imu_s(y): return y/(1-y)

# ---- (0) worker's checks reproduced ------------------------------------------
om_formula = (8/9)*KL*LAM*X0**2*mu_s(X0)
print(f"(0) Omega_closure formula = {om_formula:.4f} (worker: 0.0750; quoted 0.074)")
print(f"    idealized FP-through-today shortfall: 1/{om_formula:.4f} = "
      f"{1/om_formula:.1f}x (worker's 13.3x reproduced)")

# ---- census source (three-component) -----------------------------------------
F0 = 7*np.pi**4/120
z3 = 1.5*zeta(3, 1)
ag = np.concatenate([[0], np.logspace(-3, 7, 500)])
Fg = np.array([quad(lambda x, A=A: x*x*np.sqrt(x*x+A*A)/(np.exp(x)+1), 0, 60,
                    limit=300)[0] for A in ag])
Fi = interp1d(np.log10(ag[1:]), np.log10(Fg[1:]), kind='cubic')
def F_fast(A):
    A = np.asarray(A, float)
    return np.where(A < 1e-3, F0, 10**Fi(np.log10(np.maximum(A, 1e-3))))
REL = (7/8)*(4/11)**(4/3)
def u_nu(z):
    A = M_NU/(K_B_EV*T_NU0*(1+z))
    return 3*REL*(1+z)**4*F_fast(A)/F0
om_nu0 = float(u_nu(0.0))*u_g0/C0**2/rho_crit
om_cold = OM_CL - om_nu0
def u_hat(z):                      # census Friedmann density / rho_crit (today units)
    return om_cold*(1+z)**3 + OM_G*(1+z)**4 + OM_G*u_nu(z)
u0 = float(u_hat(0.0))
def S(s):                          # coordinate-frame closure source, S(0)=1
    z = np.exp(-1.5*s)-1
    return (u_hat(z)/u0)*np.exp(5*s)

# ---- integrate the actual trajectory, get E(a) --------------------------------
mu0 = mu_s(X0)
def x_of(r, s):
    return imu_s(min(mu0*r*r*np.exp(-2*s)*float(S(s)), 1-1e-13))
sol = solve_ivp(lambda s, r: [KL*x_of(r[0], s)*r[0]], (0, -9.6), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
s = np.linspace(-1e-6, -9.6, 6000)
r = sol.sol(s)[0]
x = np.array([x_of(ri, si) for ri, si in zip(r, s)])
a = np.exp(1.5*s); z = 1/a - 1
E = np.exp(-1.5*s)*X0/(x*r)        # H_tau/H_tau0
E2 = E*E
u = np.array([float(u_hat(zi)) for zi in z])   # census, today-normalized
rho_s = E2 - u                                  # the invoice
print(f"\n    E(a=1) = {E[0]:.6f}  (normalization check, must be 1)")
print(f"    Omega_s(z=0) = {rho_s[0]:.4f}  (= 1 - {OM_CL} - Omega_gamma,nu-kin)")

# ---- (1,2) matter-era plateaus -------------------------------------------------
for zq in (20, 50, 100, 200):
    i = np.argmin(abs(z-zq))
    print(f"    z={zq:>4}: E^2 a^3 = {E2[i]*a[i]**3:.4f}   rho_s a^3 = "
          f"{rho_s[i]*a[i]**3:.4f}   rho_s/rho_census = {rho_s[i]/u[i]:.3f}")

# ---- (3) radiation era and BBN --------------------------------------------------
print("\n    radiation era (ratio to census = ratio to standard rad. history):")
for zq in (1e4, 1e5, 5e5):
    i = np.argmin(abs(z-zq))
    print(f"    z={zq:>7.0f}: E^2/u_census = {E2[i]/u[i]:.4f}   "
          f"rho_s/u = {rho_s[i]/u[i]:+.4f}")
i = np.argmin(abs(z-4e5))          # BBN-ish (T~0.1 MeV ~ z 4e8 actually; use trend)
Hratio = np.sqrt(E2[i]/u[i])
# Delta-Neff equivalent: H^2 ∝ 1 + 7/43*... use standard: H^2 ratio = 1 + 0.163*dNeff
dNeff = (E2[i]/u[i]-1)/( (7/8)*(4/11)**(4/3)/ (1+3*REL) )
print(f"    deep-radiation H_tau/H_std = {Hratio:.4f}  "
      f"(effective dNeff ~ {dNeff:+.2f}; trend value, BBN epoch is beyond grid)")

# ---- (4) invoice equation of state ----------------------------------------------
lnrho = np.log(np.abs(rho_s)); lna = np.log(a)
w_s = -1 - np.gradient(lnrho, lna)/3
for zq in (0, 0.5, 2, 10, 100, 1000):
    i = np.argmin(abs(z-zq))
    print(f"    z={zq:>5}: w_s = {w_s[i]:+.3f}" if zq>0 else
          f"\n    z={zq:>5}: w_s = {w_s[i]:+.3f}")

# ---- (5) comparison with flat LCDM ----------------------------------------------
Om_L, OL = 0.315, 0.685
E2_lcdm = Om_L/a**3 + OL + 9.15e-5/a**4
m5 = (z < 1100)
dev = E2[m5]/E2_lcdm[m5]
print(f"\n    E^2 vs LCDM(0.315,0.685): H ratio range over z<1100: "
      f"[{np.sqrt(dev.min()):.3f}, {np.sqrt(dev.max()):.3f}]")
for zq in (0.5, 2, 10, 100, 1089):
    i = np.argmin(abs(z-zq))
    print(f"    z={zq:>5}: H/H_LCDM = {np.sqrt(E2[i]/(Om_L/a[i]**3+OL+9.15e-5/a[i]**4)):.4f}")
