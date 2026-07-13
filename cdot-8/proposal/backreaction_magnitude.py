#!/usr/bin/env python3
"""
backreaction_magnitude.py — 2026-07-13. Magnitude of the new pi_i/p_R
back-reaction on the Hamiltonian constraint (worker's §4, deliberately deferred).

Working relations (all in H_tau0=1 units, s = ln(c/c0)):
  E(s)=e^{-3s/2}x0/(xr); N=e^{5s/2}; Q=1/N; h=dotc/c=(2/3)NE; a=e^{3s/2}
  bar_g(s) = dlnN_tot/ds = dlnS/ds + 3*kl*x - 1/2   (exact, species-resolved via S)
  pi-source (normalization-free): d(16piG*pi_tot)/ds = (5/2) a^3 F_Q / bar_g
  P = 16piG*p_R*c:  dP/ds = tilde_pi * N*(kl*x)^2*(2/3)*N*E ... /h -> in s:
     dP/ds = [16piG dot p_R c + 16piG p_R dot c]/h = tilde_pi*N*(kl*x)^2 + P
     (since dot p_R = (N c/R_h^2) pi_tot, c/R_h = kl*x*h, => term = tilde_pi N (kl x)^2 h / h)
  Constraint additions: D_pi = tilde_pi*kl*x*N*E/(9 a^3);  D_pR = P/(6 a^3)
  Compare against E^2.
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
s = np.linspace(-9.4, -1e-6, 9000)          # ascending: past -> today (for retarded integrals)
r = sol.sol(s)[0]
x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
a = np.exp(1.5*s); z = 1/a-1
E = np.exp(-1.5*s)*X0/(x*r); E2 = E*E
u = np.array([float(u_hat(zi)) for zi in z])
Om_s = E2 - u
N = np.exp(2.5*s); Q = 1/N
lnS = np.log([float(Ssrc(si)) for si in s])
bar_g = np.gradient(lnS, s) + 3*KL*x - 0.5

# quadrature F (C2=0), integral anchored at today: rebuild on ascending grid
integ = Q**(-2/3)*Om_s
# I(s) = int_0^s ... : compute cumulative from the top (s=0) downward
I_full = cumulative_trapezoid(integ[::-1], s[::-1], initial=0.0)[::-1]   # int_s^0 -> then negate
F = Q**(2/3)*(-5.0*(-I_full))    # -5 * int_0^s = -5 * ( -int_s^0 )
dFds = np.gradient(F, s)
F_Q = -0.4*np.exp(2.5*s)*dFds

# retarded tilde_pi
src_pi = 2.5*a**3*F_Q/bar_g
tilde_pi = cumulative_trapezoid(src_pi, s, initial=0.0)   # from s_min (deep past ~ -inf)
# retarded P: dP/ds = src_P + P  => P(s) = int e^{s-s'} src_P ds'
src_P = tilde_pi*N*(KL*x)**2
P = np.exp(s)*cumulative_trapezoid(src_P*np.exp(-s), s, initial=0.0)

D_pi = tilde_pi*KL*x*N*E/(9*a**3)
D_pR = P/(6*a**3)
D = D_pi + D_pR

print("magnitude of the new back-reaction term vs E^2 along the fitted trajectory:")
print(f"{'z':>9} {'D_pi/E^2':>12} {'D_pR/E^2':>12} {'D_tot/E^2':>12} {'D_tot/Om_s':>12}")
for zq in (5e5, 1e4, 1100, 100, 20, 5, 2, 1, 0.5, 0.1, 0.0):
    i = np.argmin(abs(z-zq))
    print(f"{zq:>9} {D_pi[i]/E2[i]:>12.3e} {D_pR[i]/E2[i]:>12.3e} "
          f"{D[i]/E2[i]:>12.3e} {D[i]/Om_s[i]:>12.3e}")
print(f"\nmax |D/E^2| over full range: {np.max(np.abs(D/E2)):.3e} at z={z[np.argmax(np.abs(D/E2))]:.2f}")
print(f"truncation check: |src_pi| at grid edge / |src_pi| max = "
      f"{abs(src_pi[0])/np.max(abs(src_pi)):.1e} (retarded integral converged)")
# C2 sensitivity of tilde_pi: kernel adds (2/3)C2 Q^{-1/3} to F_Q
src_pi_C2 = 2.5*a**3*(2/3)*Q**(-1/3)/bar_g
tp_C2 = cumulative_trapezoid(src_pi_C2, s, initial=0.0)
D_C2 = tp_C2*KL*x*N*E/(9*a**3)
print(f"C2 channel: max |D_pi(C2=1)/E^2| = {np.max(np.abs(D_C2/E2)):.3e} "
      f"(bounded; carried symbolically as before)")
