#!/usr/bin/env python3
"""
wp4b_rederivation.py — 2026-07-17. Independent re-derivation of the WP4b
converged result, as the worker requested before it feeds the decision input.

Construction (both sides carry IDENTICAL local thermal physics, per K1):
  - T_gamma(a) from photon+e+- entropy conservation, solved exactly:
      [1 + s_e/s_gamma(T)] T^3 a^3 = T_gamma0^3
    (reproduces (11/4)^(1/3) boost at high T; reduces to T0/a after annihilation)
  - T_nu a = const = T_nu0 (frozen always) — automatically equals T_gamma
    above the transition since T_gamma a -> (4/11)^(1/3) T_gamma0 there.
  - u_hat(a) = cold + gamma(T_gamma(a)) + e+-(T_gamma(a)) + nu(T_nu0/a, massive FD)
  - closure ODE solved with this corrected S(s) to z ~ 5e11
  - THE BBN CONFRONTATION RATIO, at the same local temperature (what BBN
    physics actually runs on):
        H_cdot8(T)/H_SBBN(T) = E(a(T)) / sqrt(u_hat(a(T)))
    since H_SBBN at the same T (hence same a, same u composition) is
    H0 sqrt(u_hat) with no invoice. This is exact and frame-clean: any
    T-vs-z bookkeeping applies identically to both sides and cancels.
Checks: (i) WP4a regression at z=1090; (ii) mu-saturation monitor;
(iii) the (11/4)^(1/3) boost reproduced; (iv) x(s) near radiation fixed point.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import interp1d
from scipy.special import zeta

KL, X0, H = 0.4355, 1.10, 0.70
T_G0K, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
T_G0 = T_G0K*K_B_EV          # eV
M_E = 0.511e6                # eV
rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)
OM_G = ((A_RAD*T_G0K**4)/C0**2)/rho_crit
T_NU0 = (4/11)**(1/3)*T_G0; M_NU = 1.374/3; OM_CL = 0.074
F0 = 7*np.pi**4/120; F_BOSE = np.pi**4/15

# e+- equilibrium energy and pressure integrals (per the 4-dof species, ratios to photon)
def F_eq(A):
    if A > 60: return 0.0
    return quad(lambda x: x*x*np.sqrt(x*x+A*A)/(np.exp(np.sqrt(x*x+A*A))+1), 0, 250, limit=500)[0]
def P_eq(A):
    if A > 60: return 0.0
    return quad(lambda x: x**4/(3*np.sqrt(x*x+A*A))/(np.exp(np.sqrt(x*x+A*A))+1), 0, 250, limit=500)[0]
Agrid = np.concatenate([[0], np.logspace(-2, 1.9, 160)])
u_ratio_g = np.array([2*F_eq(A)/F_BOSE for A in Agrid])          # u_e/u_gamma
s_ratio_g = np.array([1.5*(F_eq(A)+P_eq(A))/F_BOSE for A in Agrid])  # s_e/s_gamma
u_ratio = interp1d(Agrid, u_ratio_g, kind='cubic', bounds_error=False, fill_value=(u_ratio_g[0],0.0))
s_ratio = interp1d(Agrid, s_ratio_g, kind='cubic', bounds_error=False, fill_value=(s_ratio_g[0],0.0))
print(f"limits: u_e/u_gamma(A=0) = {u_ratio(0):.4f} (expect 1.75); "
      f"s_e/s_gamma(A=0) = {s_ratio(0):.4f} (expect 1.75)")

# entropy conservation: [1 + s_ratio(m_e/T)] T^3 a^3 = T_G0^3   (a=1 today, e+- gone)
Tg = np.logspace(np.log10(T_G0*0.5), 7.7, 4000)     # eV, up to ~50 MeV
a_of_T = (T_G0**3/((1+s_ratio(M_E/Tg))*Tg**3))**(1/3)
T_of_a = interp1d(np.log(a_of_T[::-1]), np.log(Tg[::-1]), kind='cubic')
boost = Tg[-1]*a_of_T[-1]/T_G0
print(f"high-T boost check: T*a/T_G0 -> {boost:.4f} (expect (4/11)^(1/3) = {(4/11)**(1/3):.4f})")

# neutrino sector (frozen T_nu = T_NU0/a always; massive FD interp) — unchanged machinery
ag_ = np.concatenate([[0], np.logspace(-3,7,400)])
Fg_ = np.array([quad(lambda x,A=A: x*x*np.sqrt(x*x+A*A)/(np.exp(x)+1),0,60,limit=300)[0] for A in ag_])
Fi_ = interp1d(np.log10(ag_[1:]), np.log10(Fg_[1:]), kind='cubic')
def Ffd(A):
    A = np.asarray(A,float); return np.where(A<1e-3, F0, 10**Fi_(np.log10(np.maximum(A,1e-3))))
REL = (7/8)*(4/11)**(4/3)
om_nu0 = 3*REL*float(Ffd(M_NU/T_NU0))/F0*OM_G
om_cold = OM_CL - om_nu0

def u_hat_of_a(a):
    a = np.asarray(a, float)
    Tgam = np.exp(T_of_a(np.log(np.clip(a, a_of_T.min(), 1.0))))
    zp1 = 1/a
    u_g = OM_G*(Tgam/T_G0)**4
    u_e = u_g*u_ratio(M_E/Tgam)
    Anu = M_NU/(T_NU0*zp1)
    u_n = OM_G*3*REL*zp1**4*Ffd(Anu)/F0
    return om_cold*zp1**3 + u_g + u_e + u_n
u00 = float(u_hat_of_a(np.array([1.0]))[0])

sat_max = [0.0]
mu0 = X0/(1+X0)
def x_of(r, s):
    a = np.exp(1.5*s)
    Ssrc = float(u_hat_of_a(np.array([a]))[0])/u00*np.exp(5*s)
    y = mu0*r*r*np.exp(-2*s)*Ssrc
    sat_max[0] = max(sat_max[0], y)
    y = min(y, 1-1e-13)
    return y/(1-y)

sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-18.5), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.01)
def E_of_s(s):
    r = sol.sol(s)[0]
    x = np.array([x_of(ri,si) for ri,si in zip(np.atleast_1d(r),np.atleast_1d(s))])
    return np.exp(-1.5*np.asarray(s))*X0/(x*np.atleast_1d(r)), x

# WP4a regression
s1090 = -np.log(1090.8)/1.5
E1090, _ = E_of_s([s1090])
print(f"\nWP4a regression: E(z=1090) = {E1090[0]:.1f}  (established: 18398-18404) "
      f"{'OK' if abs(E1090[0]-18400)<40 else 'FAIL'}")

# THE RATIO at fixed T across the BBN window
print(f"\nBBN confrontation ratio H_cdot8(T)/H_SBBN(T) (same T, same species, both sides):")
print(f"{'T (MeV)':>9} {'z':>12} {'x(s)':>7} {'ratio':>8}")
for T_MeV in (3.0, 2.0, 1.0, 0.7, 0.3, 0.1, 0.05, 0.02):
    T = T_MeV*1e6
    a = float((T_G0**3/((1+s_ratio(M_E/T))*T**3))**(1/3))
    s = np.log(a)/1.5
    E, x = E_of_s([s])
    u = float(u_hat_of_a(np.array([a]))[0])
    print(f"{T_MeV:>9} {1/a-1:>12.3e} {x[0]:>7.3f} {E[0]/np.sqrt(u):>8.4f}")
print(f"\nmu-saturation monitor: max y = {sat_max[0]:.6f}  ({'SATURATED' if sat_max[0]>0.999 else 'no saturation'})")
