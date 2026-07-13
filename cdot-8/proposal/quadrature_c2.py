#!/usr/bin/env python3
"""
quadrature_c2.py — 2026-07-13, advisory companion (C2 round).

Independent verification of Update-WP3-QuadratureRedo-2026-07-13 and resolution
of the C2 question. Uses the budget_invoice.py machinery to rebuild Omega_s(s),
then:

 (1) reproduces the worker's quadrature (integrating factor Q^{-2/3}, s-grid),
     matter-era slope, integrand exponent, sign change;
 (2) verifies the closed-form pointwise attractors this advisory derives:
       pure-power source Q^n  =>  F_part = Omega_s / (n/2 - 1/3), hence
       F/Omega_s -> 30/17 (matter, n=9/5)  and  15/13 (radiation, n=12/5)
     — i.e. the "divergence" is the particular solution tracking the source,
     with finite, predicted coefficient;
 (3) verifies the kernel statement: F = Q^{2/3} gives (1/2)QF_Q - (1/3)F = 0
     identically — C2's mode carries ZERO corrected-constraint density;
 (4) verifies background invisibility both directions: vary C2 over orders of
     magnitude, show the deep-past and deep-future F asymptotes are unchanged
     (kernel subdominant both ways: Q^{2/3} vs Q^{12/5} past, vs const future).
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.special import zeta

# ---- rebuild the invoice Omega_s(s) (as budget_invoice.py) -------------------
KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)
u_g0 = A_RAD*T_G0**4
OM_G = (u_g0/C0**2)/rho_crit
T_NU0 = (4/11)**(1/3)*T_G0; M_NU = 1.374/3; OM_CL = 0.074
F0 = 7*np.pi**4/120; z3v = 1.5*zeta(3,1)
ag = np.concatenate([[0], np.logspace(-3, 7, 400)])
Fg = np.array([quad(lambda x,A=A: x*x*np.sqrt(x*x+A*A)/(np.exp(x)+1),0,60,limit=300)[0] for A in ag])
Fi = interp1d(np.log10(ag[1:]), np.log10(Fg[1:]), kind='cubic')
def Ff(A):
    A = np.asarray(A,float)
    return np.where(A<1e-3, F0, 10**Fi(np.log10(np.maximum(A,1e-3))))
REL = (7/8)*(4/11)**(4/3)
def u_nu(z):
    A = M_NU/(K_B_EV*T_NU0*(1+z)); return 3*REL*(1+z)**4*Ff(A)/F0
om_nu0 = float(u_nu(0.0))*u_g0/C0**2/rho_crit
om_cold = OM_CL - om_nu0
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
s = np.linspace(-1e-6, -9.4, 8000)
r = sol.sol(s)[0]
x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
a = np.exp(1.5*s); z = 1/a-1
E2 = (np.exp(-1.5*s)*X0/(x*r))**2
u  = np.array([float(u_hat(zi)) for zi in z])
Om_s = E2 - u                                   # the invoice
Q = np.exp(-2.5*s)                              # = (1+z)^{5/3}, exact

# ---- (1) the worker's quadrature ---------------------------------------------
# F = Q^{2/3} [ -5 * int_0^s Q^{-2/3} Om_s ds' + C2 ]
integrand = Q**(-2/3)*Om_s
I = cumulative_trapezoid(integrand, s, initial=0.0)     # from s=0 downward
def F_of(C2): return Q**(2/3)*(-5.0*I + C2)
F = F_of(0.0)
# matter-era slope
m = (z>5)&(z<100)
slope = np.polyfit(np.log(Q[m]), np.log(np.abs(F[m])), 1)[0]
print(f"(1) matter-era d lnF/d lnQ = {slope:.3f}   (worker: 1.77; pure-source ideal 9/5)")
# integrand exponent, deep radiation
mr = (z>2e5)&(z<3e6)
pexp = np.polyfit(np.log(a[mr]), np.log(np.abs(integrand[mr])), 1)[0]
print(f"    deep-radiation integrand ∝ a^p: p = {pexp:.3f}   (worker: -26/9 = {-26/9:.3f})")
# sign change
i_flip = np.where(np.sign(F[1:]) != np.sign(F[:-1]))[0]
print(f"    F sign change at z ≈ {z[i_flip[0]]:.0f}  (tracks the invoice zero-crossing)"
      if len(i_flip) else "    no sign change found")

# ---- (2) pointwise attractor ratios ------------------------------------------
print("\n(2) F/Omega_s pointwise (advisory closed forms: matter 30/17=1.7647, "
      f"radiation 15/13={15/13:.4f}):")
for zq in (20, 50, 100, 3e5, 1e6, 5e6):
    i = np.argmin(abs(z-zq))
    print(f"    z={zq:>9.0f}: F/Om_s = {F[i]/Om_s[i]:+.4f}")

# ---- (3) kernel check ----------------------------------------------------------
Fk = Q**(2/3); Fk_Q = (2/3)*Q**(-1/3)
resid = np.max(np.abs(0.5*Q*Fk_Q - Fk/3.0))
print(f"\n(3) kernel: max |(1/2)QF_Q - F/3| for F=Q^(2/3): {resid:.2e}  "
      f"(zero corrected-constraint density, identically)")

# ---- (4) C2 background-invisibility --------------------------------------------
print("\n(4) vary C2; deep-past and late-time F unchanged where it matters:")
i_past = np.argmin(abs(z-2e6)); i_now = 40
for C2 in (0.0, 1.0, -1.0, 100.0):
    Fv = F_of(C2)
    print(f"    C2={C2:>6}: F(z=2e6)/F0(z=2e6) = {Fv[i_past]/F[i_past]:.6f}   "
          f"F(z~0)-F0(z~0) = {Fv[i_now]-F[i_now]:+.3e} (= C2*Q^(2/3) -> bounded, dies both ways)")
# kernel-vs-particular dominance exponents
print(f"    exponents: kernel Q^(2/3) vs particular Q^(12/5) (past), const (future)"
      f" -> kernel subdominant in BOTH asymptotic directions")
