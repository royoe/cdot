#!/usr/bin/env python3
"""
backreaction_corrected.py — 2026-07-13. Independent confirmation of the worker's
normalization correction (Update-WP3-BackreactionMagnitudeCorrected-2026-07-13).

Corrected relations (sdot = ds/dt = (2/3) N E in H_tau0=1 units):
  d(tilde_pi)/ds = (5/2) a^3 F_Q / (bar_g * sdot)     [was: missing 1/sdot]
  dP/ds          = tilde_pi N (kl x)^2 sdot + P        [was: missing sdot]
  D_pi = tilde_pi kl x N E/(9 a^3);  D_pR = P/(6 a^3)  [unchanged, reconfirmed]

Gold-standard cross-check (worker's method 2, rebuilt independently):
  build t(s) = int ds/sdot, integrate the unambiguous d/dt forms
  ( d tilde_pi/dt = (5/2) a^3 F_Q / bar_g ;  d(P e^{-s})/dt = tilde_pi N (kl x)^2 sdot^2 e^{-s} )
  directly on the t-axis, map back, compare.
Then the two-pass perturbative iteration.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.special import zeta

KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)
u_g0 = A_RAD*T_G0**4; OM_G = (u_g0/C0**2)/rho_crit
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
om_nu0 = float(u_nu(0.0))*u_g0/C0**2/rho_crit; om_cold = OM_CL - om_nu0
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
a = np.exp(1.5*s); z = 1/a-1
E = np.exp(-1.5*s)*X0/(x*r); E2 = E*E
u = np.array([float(u_hat(zi)) for zi in z])
Om_s0 = E2 - u
N = np.exp(2.5*s); Q = 1/N
lnS = np.log([float(Ssrc(si)) for si in s])
bar_g = np.gradient(lnS, s) + 3*KL*x - 0.5
sdot = (2/3)*N*E

def quadrature(Om_s):
    integ = Q**(-2/3)*Om_s
    I = cumulative_trapezoid(integ[::-1], s[::-1], initial=0.0)[::-1]
    F = Q**(2/3)*(5.0*I)          # = Q^{2/3} * (-5) * int_0^s = +5 * int_s^0
    F_Q = -0.4*np.exp(2.5*s)*np.gradient(F, s)
    return F, F_Q

def D_of(F_Q):
    src_pi = 2.5*a**3*F_Q/(bar_g*sdot)                     # CORRECTED
    tp = cumulative_trapezoid(src_pi, s, initial=0.0)
    src_P = tp*N*(KL*x)**2*sdot                            # CORRECTED
    P = np.exp(s)*cumulative_trapezoid(src_P*np.exp(-s), s, initial=0.0)
    return tp*KL*x*N*E/(9*a**3) + P/(6*a**3), tp, P

F, F_Q = quadrature(Om_s0)
D0, tp, P = D_of(F_Q)

# gold standard: t-axis integration
t = cumulative_trapezoid(1/sdot, s, initial=0.0)
dpi_dt = 2.5*a**3*F_Q/bar_g
tp_t = cumulative_trapezoid(dpi_dt, t, initial=0.0)
srcP_t = tp_t*N*(KL*x)**2*sdot**2
Pe_t = cumulative_trapezoid(srcP_t*np.exp(-s), t, initial=0.0)
P_t = np.exp(s)*Pe_t
D0_t = tp_t*KL*x*N*E/(9*a**3) + P_t/(6*a**3)
m = z < 1e5
gs_err = np.max(np.abs((D0[m]-D0_t[m])/np.maximum(np.abs(D0_t[m]),1e-30)))
print(f"gold-standard t-axis vs corrected s-integration: max rel diff (z<1e5) = {gs_err:.2e}")

print(f"\n{'z':>7} {'D0/E^2 (corrected)':>20} {'worker':>12}")
wk = {1100:-6.8e-7, 100:-6.5e-5, 20:-9.5e-4, 2:-2.5e-2, 1:-4.7e-2, 0.5:-6.8e-2, 0.0:-9.5e-2}
for zq in (1100,100,20,2,1,0.5,0.0):
    i = np.argmin(abs(z-zq))
    print(f"{zq:>7} {D0[i]/E2[i]:>20.3e} {wk[zq]:>12.1e}")

# two-pass iteration
D_prev = D0
for it in (1,2):
    Fi_, FQi = quadrature(Om_s0 - D_prev)
    Di, _, _ = D_of(FQi)
    i0 = -1
    print(f"iteration {it}: D/E^2 at z=0 = {Di[i0]/E2[i0]:.4e}   "
          f"(shift from previous: {abs(Di[i0]-D_prev[i0])/abs(D_prev[i0])*100:.2f}%)")
    D_prev = Di
i0=-1
print(f"\nrecombination check (z=1100): D/E^2 = {D0[np.argmin(abs(z-1100))]/E2[np.argmin(abs(z-1100))]:.2e}  (WP4a untouched)")
