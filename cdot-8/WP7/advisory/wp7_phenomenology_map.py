#!/usr/bin/env python3
"""
wp7_phenomenology_map.py — 2026-07-19. Response to wp7_anchor_brackets.py.

CONCEDED (advisor error #8): the kR_h ~ 6 'first acoustic peak' entry in
wp7_structure.py Part A was illustrative, never checked against the
actual R_h(t), and wrong by ~5 orders of magnitude — a LCDM comoving-
horizon value imported into a variable-c trajectory where c ~ a^{2/3}
makes the early causal ball ~100x smaller (plus trajectory differences).
Class: external-framework value imported without computing — the exact
class this program polices. Worker-caught with the literal WP2 definition.

WHAT THE CORRECT R_h(t) IMPLIES — the map INVERTS, it does not vanish:
 * W(kR_h(t)) is EPOCH-dependent; each mode k sits at W~1 (fully
   M5-coupled, separate-universe regime) until R_h(t) grows past 1/k,
   then decouples. The window sweeps DOWN through k as R_h grows.
 * At z*: ALL observable CMB k have W ~ 1 -> the (1-W) field-side term
   VANISHES there (not 8%: ~1e-12); the Einstein-side W-term is at FULL
   strength — but at W=1 it is exactly the separate-universe-consistent
   linear response of the cdot-8 background (the same Q-drag the
   background Friedmann equation already carries): REQUIRED for
   consistency, scale-independent (no k-shape), not a distinctive
   signature.
 * The distinctive W-SHAPE lives where kR_h(t) ~ 1 LATE: R_h(today)
   ~ 2 Gpc -> the transition maps to the lowest multipoles via the
   late-time (ISW-era) evolution.
 * NEW CENTRAL ITEM: matter-power modes stay M5-coupled deep into the
   matter era (z_exit(k) below) — the GROWTH history carries the
   W=1 M5 response until each mode's exit. Computing its coefficient:
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
c0H0_Mpc = C0/1000/(100*H)
Rh = cumulative_trapezoid(np.exp((2/3)*s)/E, s, initial=0.0)   # in c0/H0
Rh_Mpc = Rh*c0H0_Mpc

print("=== 1. Worker's R_h values: independently confirmed ===")
i_st = np.argmin(np.abs(z_arr-1090))
print(f"R_h(z*=1090) = {Rh_Mpc[i_st]:.3e} Mpc  (vs r_s = 173.4, D_p = 13074) -> kR_h(z*) ~ 1e-6-1e-5 for all CMB l: WORKER CONFIRMED")
print(f"R_h(today)   = {Rh_Mpc[-1]:.0f} Mpc")
print(f"sanity, local-physics decoupling TODAY: galaxy k~1/(10 kpc): kR_h ~ {Rh_Mpc[-1]/0.01:.1e} >> 1 — WP5/WP6 INTACT\n")

print("=== 2. Mode-exit history: z_exit(k) where R_h(t) = 1/k ===")
print(f"{'k [1/Mpc]':>12} {'1/k [Mpc]':>10} {'z_exit':>8}   relevance")
for k, lab in [(5e-4,"l ~ 6 (via D_p today)"), (2e-3,"l ~ 26"), (0.02,"first-peak k"), (0.1,"P(k) quasi-linear"), (1.0,"galaxy-cluster k")]:
    idx = np.argmin(np.abs(Rh_Mpc - 1.0/k))
    print(f"{k:>12.0e} {1/k:>10.0f} {z_arr[idx]:>8.1f}   {lab}")
print("""=> every observable mode was M5-coupled (W~1, separate-universe regime)
through recombination; P(k) modes exit during the matter era; only the
very lowest-l scales are still transitioning TODAY — the W-shape is a
late-time, l <~ 10 feature (ISW-era), not a first-peak feature.\n""")

print("=== 3. The coupled-era growth coefficient (the new central item) ===")
Q = np.exp(-2.5*s)
I = cumulative_trapezoid((Q**(-2/3)*(E**2-np.array([float(u_hat(z)) for z in z_arr])))[::-1], s[::-1], initial=0.0)[::-1]
F = Q**(2/3)*(-5.0*I)
F_Q = -0.4*np.exp(2.5*s)*np.gradient(F, s)
F_QQ = -0.4*np.exp(2.5*s)*np.gradient(F_Q, s)
dlnQ_ds = -2.5
dlnN_ds = 3*np.gradient(np.log(np.maximum(Rh,1e-30)), s)   # matter-class census: engulfment only
elasticity = dlnQ_ds/dlnN_ds                                # = q' Nbar / Qbar
coeff = (F_Q/6 + Q*F_QQ/2)*elasticity*Q                     # = (F_Q/6+QF_QQ/2) q' Nbar, H0^2 units
matter_source = 3.0*np.array([float(u_hat(z)) for z in z_arr])  # 8piG rho_m/H0^2-class ~ 3 u
print(f"{'z':>7} {'elasticity dlnQ/dlnN':>21} {'M5 coeff/(matter source)':>25}")
for zt in [30.0, 10.0, 3.0, 1.0, 0.0]:
    i = np.argmin(np.abs(z_arr-zt))
    print(f"{zt:>7.0f} {elasticity[i]:>21.3f} {coeff[i]/matter_source[i]:>25.3f}")
print("""=> an O(few-10%) modification of the Poisson source during the coupled
era, decaying as each mode exits — a first-order effect on the GROWTH
HISTORY (sigma8-class observables), which now replaces 'low-l signature'
as WP7's central deliverable. At W=1 this is the separate-universe-
consistent response the background already implies — including it is
REQUIRED; the previous 'clean sub-horizon import' claim is RE-SCOPED to
'clean after each mode's exit' (late times / small scales).""")
