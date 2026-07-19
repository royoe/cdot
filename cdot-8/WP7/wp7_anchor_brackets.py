#!/usr/bin/env python3
"""
wp7_anchor_brackets_v2.py -- cleaned up. Checking the REAL magnitude of
kR_h(z*) using the literal WP2 R_h(t) definition, rather than the
illustrative kR_h=0.1,1,6,20,1000 placeholder table used since sec.2a.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d

KL, X0, H = 0.4355, 1.10, 0.70
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
sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-11), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
s = np.linspace(-10.8, -1e-6, 16000)
r = sol.sol(s)[0]
x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
E = np.exp(-1.5*s)*X0/(x*r)
z_arr = np.exp(-1.5*s)-1

Rh_over_c0H0 = cumulative_trapezoid(np.exp((2.0/3.0)*s)/E, s, initial=0.0)
H0_kms_Mpc = 100*H
c0H0_Mpc = C0/1000/H0_kms_Mpc
print(f"c0/H0 = {c0H0_Mpc:.1f} Mpc  (sanity: standard value ~4283 Mpc for H0=70)")

print(f"\n{'z':>10} {'R_h [Mpc]':>14}")
for zt in [1e6, 1e4, 9640.0, 1090.0, 30.0, 1.0, 0.0]:
    i = np.argmin(np.abs(z_arr - zt))
    Rh_Mpc = Rh_over_c0H0[i]*c0H0_Mpc
    print(f"{zt:>10.0f} {Rh_Mpc:>14.6e}")

print(f"""
COMPARISON at z*=1090 (WP4a's established values):
  R_h(z*)   = {Rh_over_c0H0[np.argmin(np.abs(z_arr-1090))]*c0H0_Mpc:.4e} Mpc
  r_s(z*)   = 173.36 Mpc   (WP4a sound horizon)
  D_p(z*)   = 13074.3 Mpc  (WP4a comoving distance to last scattering)

R_h(z*) is smaller than r_s(z*) by a factor of {173.36/(Rh_over_c0H0[np.argmin(np.abs(z_arr-1090))]*c0H0_Mpc):.3e},
and smaller than D_p(z*) by a factor of {13074.3/(Rh_over_c0H0[np.argmin(np.abs(z_arr-1090))]*c0H0_Mpc):.3e}.

This means: for ANY k corresponding to an observable CMB multipole
(k = l/D_p(z*), l=2...few-thousand), kR_h(z*) is utterly tiny --
deep in the kR_h<<1 regime where W(kR_h)->1 and (1-W)->0. The
"kR_h~6 at the first acoustic peak" identification used illustratively
since sec.2a (wp7_structure.py Part A's table) was NEVER checked
against the actual R_h(z) trajectory -- checking it now shows it is
off by many orders of magnitude.
""")

l_list = [2, 10, 50, 220, 700, 2500]
Dp_zstar = 13074.3
i_zstar = np.argmin(np.abs(z_arr-1090))
Rh_zstar = Rh_over_c0H0[i_zstar]*c0H0_Mpc
W = lambda xx: 3*(np.sin(xx)-xx*np.cos(xx))/xx**3
print(f"{'l':>6} {'k [1/Mpc]':>12} {'kR_h(z*)':>12} {'W(kR_h)':>10} {'1-W':>10}")
for l in l_list:
    k = l/Dp_zstar
    xk = k*Rh_zstar
    Wv = W(xk) if xk>1e-8 else 1.0
    print(f"{l:>6} {k:>12.5e} {xk:>12.3e} {Wv:>10.6f} {1-Wv:>10.3e}")
