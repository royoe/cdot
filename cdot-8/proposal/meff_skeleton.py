#!/usr/bin/env python3
"""
meff_skeleton.py — 2026-07-17. Dimensional skeleton (advisor pre-registration,
NOT the careful normalization pass) for the corrected WP5 task:

Mistele 2305.07742 distinguishes TWO scales:
  m   — ghost-condensate mass: "controls whether AeST reproduces MOND",
        source of the r_c cutoff and the MMH 2023 weak-lensing tension,
        THE dust-mimicking device. AeST chooses m ~ 1/Mpc.
  m_x — vector-sector scale: "not related to the ghost condensate...
        does not affect the ability of AeST to reproduce MOND...
        not yet constrained phenomenologically."

cdot-8's action as written (WP1-WP3) contains F(Q) only — no native m^2 term.
BUT: in Newtonian gauge, delta(Q) = delta(phi_dot) - Q0*Phi, so expanding the
quadrature-determined F to second order generates an EFFECTIVE condensate mass
  m_eff^2 ~ (1/2) Q0^2 F_QQ(Q0)   [up to the careful f_G/16piG normalization]
with ZERO freedom — F is determined by the invoice.

Skeleton estimate: F is in H0^2 units (it supplies the invoice), Q0 = 1 today,
so F_QQ(1) = O(Omega_s-scale) => m_eff ~ sqrt(F_QQ) * H0/c — HUBBLE-scale,
not Mpc-scale. Then r_c = (r_M * f_G / m_eff^2)^{1/3} >> any lensing radius.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d

KL, X0, H = 0.4355, 1.10, 0.70
c_H0_Mpc = 2.99792458e8/(H*100*1000/3.0857e22)/3.0857e22
T_G0, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)
OM_G = ((A_RAD*T_G0**4)/C0**2)/rho_crit
T_NU0 = (4/11)**(1/3)*T_G0; M_NU = 1.374/3; OM_CL = 0.074
F0 = 7*np.pi**4/120
ag = np.concatenate([[0], np.logspace(-3,7,400)])
Fg = np.array([quad(lambda x,A=A: x*x*np.sqrt(x*x+A*A)/(np.exp(x)+1),0,60,limit=300)[0] for A in ag])
Fi = interp1d(np.log10(ag[1:]), np.log10(Fg[1:]), kind='cubic')
def Ffd(A):
    A = np.asarray(A,float); return np.where(A<1e-3, F0, 10**Fi(np.log10(np.maximum(A,1e-3))))
REL = (7/8)*(4/11)**(4/3)
def u_nu(z):
    A = M_NU/(K_B_EV*T_NU0*(1+z)); return 3*REL*(1+z)**4*Ffd(A)/F0
om_nu0 = float(u_nu(0.0))*(A_RAD*T_G0**4)/C0**2/rho_crit; om_cold = OM_CL - om_nu0
def u_hat(z): return om_cold*(1+z)**3 + OM_G*(1+z)**4 + OM_G*u_nu(z)
u00 = float(u_hat(0.0))
def Ssrc(s):
    z = np.exp(-1.5*s)-1
    return (u_hat(z)/u00)*np.exp(5*s)
mu0 = X0/(1+X0)
def x_of(r,s):
    y = min(mu0*r*r*np.exp(-2*s)*float(Ssrc(s)), 1-1e-13); return y/(1-y)
sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-9.6), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
s = np.linspace(-9.4, -1e-6, 12000)
r = sol.sol(s)[0]
x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
E2 = (np.exp(-1.5*s)*X0/(x*r))**2
u = np.array([float(u_hat(zi)) for zi in np.exp(-1.5*s)-1])
Om_s = E2 - u
Q = np.exp(2.5*s)*0 + np.exp(2.5*s)  # Q = e^{-5s/2}? no: Q=1/N = e^{-5s/2}
Q = np.exp(-2.5*s)
integ = Q**(-2/3)*Om_s
I = cumulative_trapezoid(integ[::-1], s[::-1], initial=0.0)[::-1]
F = Q**(2/3)*(-5.0*I)
m = (np.exp(-1.5*s)-1 > 5) & (np.exp(-1.5*s)-1 < 100)
print(f"inline closed-form check: F/Om_s (matter) = {np.mean(F[m]/Om_s[m]):+.3f} (target +1.765)")
dFds = np.gradient(F, s)
F_Q  = -0.4*np.exp(2.5*s)*dFds
F_QQ = -0.4*np.exp(2.5*s)*np.gradient(F_Q, s)
i0 = -1
print(f"F_QQ(Q0=1, today) = {F_QQ[i0]:+.4f}  (H0^2 units, Q dimensionless)")
m_eff_invMpc = np.sqrt(abs(F_QQ[i0])/2)/c_H0_Mpc     # ~ Q0 sqrt(F_QQ/2) * H0/c
print(f"m_eff ~ Q0 sqrt(F_QQ/2) H0/c = {m_eff_invMpc:.2e} / Mpc   (1/m_eff = {1/m_eff_invMpc:.0f} Mpc)")
print(f"AeST's chosen m ~ 1 / Mpc  ->  cdot-8's effective condensate mass is "
      f"~{1/m_eff_invMpc:.0f}x lighter")
# r_c for a large lensing-stack galaxy: r_M = sqrt(G M_b / a0), M_b ~ 1e11 Msun
Msun, a0 = 1.989e30, 1.39e-10
rM_m = np.sqrt(G_N*1e11*Msun/a0); rM_Mpc = rM_m/3.0857e22
rc_Mpc = (rM_Mpc/(m_eff_invMpc**2))**(1/3)   # f_G ~ 1
print(f"r_M(1e11 Msun) = {rM_Mpc*1000:.0f} kpc  ->  r_c ~ (r_M/m_eff^2)^(1/3) = {rc_Mpc:.0f} Mpc")
print(f"lensing stacks probe r <~ 1-3 Mpc  ->  condensate negligible at ALL survey radii")
print("PRE-REGISTERED EXPECTATION (skeleton; careful normalization pass assigned):")
print("cdot-8's F_QQ-generated condensate mass is Hubble-scale, r_c ~ O(100) Mpc,")
print("=> MOND persists at survey radii => consistent with MMH 2023 data => the")
print("distinguishing advantage returns via the m-channel, not the m_x-channel.")
