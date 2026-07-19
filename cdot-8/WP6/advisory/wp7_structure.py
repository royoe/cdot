#!/usr/bin/env python3
"""
wp7_structure.py — 2026-07-18 (v2; v1's inline check FIRED — dictionary
normalization wrong and a narrative conflation — both fixed, recorded).

PART A — delta-N resolved structurally: M5 = ONE constraint per slice ->
per-mode force carries the horizon-volume window W(kR_h) = 3 j1(x)/x.
PART B — cdot-8's scalar-fluid w(a) from the CORRECT WP3 dictionary
rho_s = (1/2)Q F_Q - (1/3)F  [the Friedmann constraint's own combination,
which the quadrature was built to equate to Omega_s], verified inline,
plus the finding v1's failure exposed: Omega_s CROSSES ZERO in the
crossover era — the scalar cannot be described as a fluid through the
crossing; the field variables (chi, E_alpha) stay regular there.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d

print("=== PART A: per-mode M5 coupling window W(k R_h) ===")
W = lambda x: 3*(np.sin(x)-x*np.cos(x))/x**3
for x,lab in [(0.1,"super-horizon / SW plateau"),(1.0,"horizon crossing"),
              (6.0,"~first acoustic peak scale at z*"),(20.,"higher peaks"),
              (1e3,"matter power spectrum, galaxy scales")]:
    print(f"  kR_h={x:>6}: |W|={abs(W(x)):.2e}  ({lab})")
print("""=> AeST perturbation-system import is CLEAN sub-horizon (corrections
   <= (kR_h)^-2 ~ 1e-6 at galaxy scales); GENUINE new M5 term at kR_h <~
   few (low-l CMB / super-horizon); first-peak-scale window ~8% (epoch-
   dependent, order-of-magnitude — R_h(z*) is cdot-8's own, not LCDM's).
   Background theta* untouched either way (background vs perturbation).\n""")

print("=== PART B: cdot-8 scalar-fluid w(a); the zero crossing ===")
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
E2 = (np.exp(-1.5*s)*X0/(x*r))**2
u = np.array([float(u_hat(zi)) for zi in np.exp(-1.5*s)-1])
Om_s = E2 - u
z_arr = np.exp(-1.5*s)-1
Q = np.exp(-2.5*s)
I = cumulative_trapezoid((Q**(-2/3)*Om_s)[::-1], s[::-1], initial=0.0)[::-1]
F = Q**(2/3)*(-5.0*I)
F_Q = -0.4*np.exp(2.5*s)*np.gradient(F, s)
rho_dict = 0.5*Q*F_Q - F/3.0          # CORRECT WP3 constraint combination
m = (z_arr>5)&(z_arr<100)
print(f"inline check (v2): max|1 - rho_dict/Om_s|, matter era = "
      f"{np.max(np.abs(1-rho_dict[m]/Om_s[m])):.4f}   [v1 used QF_Q-F: 0.403 FAIL]")
# w from continuity on |Om_s| (ln a = 1.5 s):
w = -(1/4.5)*np.gradient(np.log(np.abs(Om_s)), s) - 1
# zero crossing:
sign_change = np.where(np.sign(Om_s[:-1]) != np.sign(Om_s[1:]))[0]
z_cross = z_arr[sign_change[0]] if len(sign_change) else None
print(f"\nOmega_s ZERO CROSSING at z ~ {z_cross:.0f}  (scalar share: +92.6% today")
print(f"  -> 0 at the crossing -> asymptotically -7% of the budget deep in radiation)")
print(f"\n{'z':>9} {'Om_s/E^2':>9} {'w(slope)':>9}")
for zt in [0.0, 0.5, 30.0, 1100.0, 1e4, 1e6]:
    i = np.argmin(np.abs(z_arr-zt))
    print(f"{zt:>9.0f} {Om_s[i]/E2[i]:>9.3f} {w[i]:>9.3f}")
print("""
READING (corrected): matter era w ~ 0 by construction (dust-like invoice);
today w < 0 (the scalar supplies acceleration, no Lambda); deep radiation
the scalar is a SMALL NEGATIVE (-7%) radiation-tracking component, w -> 1/3
by tracking. THE STRUCTURAL FINDING v1's failed check exposed: Omega_s
crosses ZERO in the crossover era — w and c_ad^2 formally diverge there,
so the founding paper's FLUID form CANNOT be used through the crossing;
the underlying FIELD variables (chi, E_alpha) remain perfectly regular.
WP7 must therefore run the crossover era in field variables, switching to
the fluid form only where |Omega_s| is O(1). And the crossing sits at
z ~ few x 10^3 — inside the already-flagged Gate 1(b) crossover zone:
the same problem region, now with a perturbation-level feature localized
in it. AeST's native dustlike-Pi->0 shortcut does NOT transfer there.""")
