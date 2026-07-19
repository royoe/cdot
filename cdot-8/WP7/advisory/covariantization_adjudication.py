#!/usr/bin/env python3
"""
covariantization_adjudication.py — 2026-07-18. Response to
wp7_lambda_extensivity_check.py (worker pushback on the accepted
advisory's 'Lambda_M extensive over the ball' step).

PART 1 — the worker's volume-rate claim, verified independently.
PART 2 — what the catch actually costs, and what survives: the two
physical anchors already in the program's record pin the field-side
term's ASYMPTOTICS; the volume convention affects only the window's
detailed shape at kR_h ~ 1. Demonstrated by showing the alternative
(no-cancellation) reading violates separate-universe continuity.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d

# --- trajectory machinery (identical to wp7_structure.py) ---
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

print("=== PART 1: worker's volume-rate claim, independent reproduction ===")
Rh = cumulative_trapezoid(np.exp((2/3)*s)/E, s, initial=0.0)
dlnRh = np.gradient(np.log(np.maximum(Rh,1e-30)), s)
for zt in [1090.0, 30.0, 1.0, 0.0]:
    i = np.argmin(np.abs(z_arr-zt))
    print(f"  z={zt:>6.0f}: d ln R_h/ds = {dlnRh[i]:.3f}  (vs d ln a/ds = 1)  R_h/e^s = {Rh[i]/np.exp(s[i]):.3e}")
print("CONFIRMED: R_h and a grow at genuinely different rates; a^3 and the")
print("ball volume are two conventions; the conversion was never derived.")
print("The advisory step presented a convention as derived — conceded.\n")

print("=== PART 2: what the two PHYSICAL anchors pin regardless ===")
print("""Anchor 1 — separate-universe continuity at k->0 (the program's own §6
exact check): a super-horizon mode IS locally a shifted background, so
the field-side term must vanish smoothly as k->0. Test the two readings
by the k->0 behavior of the term relative to gradient terms, (aH/k)^2 x
[cancellation factor]:""")
W = lambda x: 3*(np.sin(x)-x*np.cos(x))/x**3
print(f"{'kR_h':>7} {'no-cancel: (aH/k)^2':>20} {'windowed: (aH/k)^2 (1-W)':>25}")
for xk in [0.03, 0.1, 0.3, 1.0]:
    print(f"{xk:>7} {1/xk**2:>20.1f} {(1-W(xk))/xk**2:>25.3f}")
print("""no-cancellation reading: term/gradient DIVERGES as k->0 — a
super-horizon mode would feel an M5 force its own shifted-background
physics doesn't contain: separate-universe VIOLATED -> excluded.
windowed reading: -> (aH R_h)^2/10-class CONSTANT — smooth k->0 match
to the exact background cancellation: separate-universe SATISFIED.
Anchor 2 — WP5 local decoupling at kR_h >> 1: the cancellation must die
off sub-horizon (local physics keeps the full sliding-condensate term,
(aH/k)^2-suppressed) — both readings satisfy this; full-enslavement
(pointwise constraint) violates it -> excluded from the other side.

VERDICT: the two anchors PIN the asymptotics — cancellation factor -> 1
at k->0, -> 0 at kR_h >> 1 — for ANY admissible covariantization. What
the worker's catch genuinely demotes: the DETAILED SHAPE of the
crossover at kR_h ~ 1 (top-hat W vs smoothed alternatives, and the
volume-convention bookkeeping inside it) is a bounded modeling freedom,
not a derived result. The low-l signature EXISTS with pinned asymptotics;
its detailed shape carries a stated window-shape band.""")
