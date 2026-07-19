#!/usr/bin/env python3
"""
wp5_decoupling_check.py — 2026-07-17. Two pieces for the WP5 first installment:
(1) the absolute anchor for the a0(z) identification (charter identity
    a0_hat(z) = (2/3) lambda c0 H_tau(z), exact on any trajectory), checked
    against cdot-7's fitted a0(0) = 1.39e-10 m/s^2;
(2) the prediction backbone: a0_hat(z)/a0_hat(0) = E(z) at the lens redshifts
    real stacked weak-lensing samples actually probe.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import interp1d

KL, X0, H = 0.4355, 1.10, 0.70
LAM = 0.3056
C0 = 2.99792458e8
H0_si = H*100*1000/3.0857e22
# absolute anchor: a0(0) = (2/3) * lambda * c0 * H_tau0
a0_pred = (2/3)*LAM*C0*H0_si
print(f"anchor: a0(0) = (2/3)*lambda*c0*H0 = {a0_pred:.3e} m/s^2  (cdot-7 fit: 1.39e-10)")

# E(z) at lens redshifts from the standard machinery
T_G0, A_RAD, G_N = 2.7255, 7.565723e-16, 6.67430e-11
K_B_EV = 8.617333e-5
rho_crit = 3*H0_si**2/(8*np.pi*G_N)
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
sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-6), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
print("\nlensing-RAR prediction backbone: a0_hat(z_lens)/a0_hat(0) = E(z_lens)")
print(f"{'z_lens':>8} {'E(z)':>8}   (survey context)")
ctx = {0.1:"SDSS/local stacks", 0.25:"KiDS bright lenses", 0.35:"KiDS/DES typical",
       0.5:"DES deep lenses", 0.75:"HSC deep", 1.0:"future/LSST"}
for zl in (0.1, 0.25, 0.35, 0.5, 0.75, 1.0):
    s = -np.log(1+zl)/1.5
    r = sol.sol([s])[0][0]
    x = x_of(r, s)
    E = (1+zl)*X0/(x*r)
    print(f"{zl:>8} {E:>8.3f}   ({ctx[zl]})")
print("\n(for contrast, LCDM E(z): 0.1->1.05, 0.35->1.19, 0.5->1.28, 1.0->1.62 —")
print(" similar at low z by construction of the fit; the OBSERVABLE is a0 tracking")
print(" ANY of these E's vs a0 = const, a ~15-30% a0 enhancement at z_lens=0.35-0.5)")
