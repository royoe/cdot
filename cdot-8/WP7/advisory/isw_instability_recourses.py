#!/usr/bin/env python3
"""
isw_instability_recourses.py — 2026-07-21. Assessment support for the
Stage-4 vector-sector instability escalation (WP7 §42-§43).

PART 1 — mechanism consistency: is the reported growth rate the
anti-Jeans rate |c_ad| k/(aH)?  (order-of-magnitude check against the
§42/§43 reported eigenvalues)
PART 2 — an omission in the Stage-4 assembly, flagged: §42 cites §7's
SUPERSEDED all-k cancellation; the corrected record (QDefinition +
CovariantizationFreedom advisories) has a field-side term
-F_Q(1-W(kR_h)) that ACTIVATES late for exactly these k. Where?
PART 3 — the leading recourse's linear-order mechanics: F_Y(0,Q)
renormalizes the gradient coefficient at LINEAR order while leaving the
background EXACTLY untouched (Y=0 on FRW) — the same declared-free
Y-sector of the WP6 scope statement.
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
u = np.array([float(u_hat(zi)) for zi in z_arr])
Om_s = E**2 - u
w = -(1/4.5)*np.gradient(np.log(np.abs(Om_s)), s) - 1
cad2 = w + np.gradient(w, s, edge_order=2)/np.gradient(np.log(np.abs(Om_s)), s, edge_order=2)
c0H0_Mpc = C0/1000/(100*H)
Rh_Mpc = cumulative_trapezoid(1.5*np.exp(s)/E, s, initial=0.0)*c0H0_Mpc  # corrected s-convention

print("=== PART 1: anti-Jeans rate |c_ad| k/(aH) vs reported eigenvalues ===")
print(f"{'k [1/Mpc]':>10} {'z':>5} {'|c_ad|':>7} {'k/(aH) ':>8} {'rate/H(z)':>10} {'reported':>16}")
for k, zt, rep in [(2.71e-3, 100.0, "1655 (units tbc)"), (2.71e-3, 0.0, "~8-9 x H0"), (1.1e-3, 0.0, ""), (5.4e-3, 0.0, "")]:
    i = np.argmin(np.abs(z_arr-zt))
    k_aH = k*c0H0_Mpc*(1+zt)/E[i]
    rate = np.sqrt(np.abs(cad2[i]))*k_aH
    print(f"{k:>10.2e} {zt:>5.0f} {np.sqrt(abs(cad2[i])):>7.3f} {k_aH:>8.1f} {rate:>10.2f} {rep:>16}")
print("""At z=0, k=2.71e-3: |c_ad| k/(aH) ~ 3 x H0 against the corrected ~8-9 —
same order, k-scaling right (rate grows ~linearly in k), z-trend right
(rate/H falls toward z=0 as |c_ad| shrinks and never crosses zero).
The advisor reframing holds: this is the c_ad^2<0 anti-Jeans branch —
negative effective pressure DESTABILIZES with k, the reverse of Jeans
stabilization; the scale-free mu^2 ~ -0.5 H^2 part was the good
(CDM-like) clustering driver, the c_eff^2 k^2 < 0 part is the pathology.
O(2-3) coefficient differences are the full 6x6's mixing factors.\n""")

print("=== PART 2: the superseded-§7 omission — when does -F_Q(1-W) activate? ===")
W = lambda xx: 3*(np.sin(xx)-xx*np.cos(xx))/xx**3
print(f"{'k [1/Mpc]':>10} {'z':>5} {'k R_h(z)':>9} {'(1-W)':>7}")
for k in [1.1e-3, 2.71e-3, 5.4e-3]:
    for zt in [100.0, 10.0, 1.0, 0.0]:
        i = np.argmin(np.abs(z_arr-zt))
        xk = k*Rh_Mpc[i]
        Wv = W(xk) if xk>1e-8 else 1.0
        print(f"{k:>10.2e} {zt:>5.0f} {xk:>9.3f} {1-Wv:>7.3f}")
print("""The Stage-4 assembly cites §7's all-k cancellation — SUPERSEDED by the
Q-definition round: the field equations carry -F_Q(1-W(kR_h)) at finite
k. For the ISW k's this term is OFF at z >~ 10 (kR_h << 1) and turns ON
at z <~ 1-3 — so it is NOT the cause of the z=100 instability, but it
is a real omission in the very window where the ISW signal forms, and
it must be carried in any rebuilt system (with the window-shape band).
Flagged as a required correction, not the cure.\n""")

print("=== PART 3: the leading recourse — F_Y(0,Q) at linear order ===")
print("""AeST's free function is F(Y,Q); the census quadrature determines ONLY
F(0,Q) — the Y-direction is the SAME declared-free sector as WP6's
screening scope statement. Expand: F ⊃ F_Y(0,Q(z)) * Y, and Y is
quadratic in the perturbations (the U_i U^i structure), so at LINEAR
order in the EOM this term renormalizes the gradient operator:
    (2-K_B)  -->  (2-K_B) + F_Y(0, Q(z))     [schematic weighting]
— a k^2-coefficient (effective sound speed) modification that:
  * leaves the FRW background EXACTLY untouched (Y = 0 identically);
  * leaves WP3's quadrature, the invoice, and all of WP1-WP4 untouched;
  * enters galaxy phenomenology only through the Y->0 end of the same
    completion function T22 and Q_2 already constrain.
REQUIREMENT for a sensible spectrum: c_eff^2(k,z) >~ 0 at cosmological
gradients, i.e. the completion's small-gradient end must supply the
pressure support the Q-sector's c_ad^2 < 0 removes. The completion
family is then pinned from THREE sides: deep-Newtonian (T22),
transition (Q_2), small-gradient/cosmological (stability) — plus KATRIN
on the census side. One function family, four external anchors: the
post-WP7 revisit becomes a single joint design problem.
TENSION TO STATE HONESTLY: deep-MOND galaxy phenomenology wants the
gradient response to SOFTEN at small |U|; cosmological stability wants
a positive floor at yet-smaller |U|. AeST's structure helps — the bare
(2-K_B)Y term is a positive-definite floor SEPARATE from the free
function — but whether the unstable direction (the longitudinal
alpha/E_alpha combination, which the rank-1 U-structure does NOT
protect) can be floored by an admissible F_Y is exactly the sharp
question the audit (Recourse 0) must answer first: WHERE does the
negative net from, given a positive-definite bare gradient term?""")
