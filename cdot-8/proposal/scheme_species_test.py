#!/usr/bin/env python3
"""
scheme_species_test.py — 2026-07-15. Direct numerical closure of the worker's
§4 open question: does the g_i-internal lapse placement affect D?

Scheme A (worker's original / advisor's default):
  g_i = (p_i^sp - 5/2) dot(c)/c + N c/R_h
Scheme B (worker's identified alternative, N distributed uniformly inside):
  g_i = N [ (p_i^sp - 5/2) dot(c)/c + c/R_h ]

Both reduce to WP2 at N=1; sourced identity dot(pi_i) = -Lambda_M q' N_i
holds identically in both. But the Hamiltonian-constraint back-reaction uses
partial g_i / partial N — which differs for radiation (p_rad = 1):
   A: partial g_rad/partial N = c/R_h
   B: partial g_rad/partial N = -(3/2) dot(c)/c + c/R_h   [differ by -(3/2)h]

Species-resolved: build N_cold(s), N_rad(s) directly from census_closure
convention (log-derivatives = g_i evaluated species-by-species at N=1, which
is the physical trajectory), then compute D contributions species-by-species
under each scheme's own partial(g_i)/partial(N) formula.
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
h = 1.5*sdot  # dot(c)/c in same units

# species-resolved census (SIGN CORRECTED throughout)
u_cold = om_cold*(1+z)**3
u_gnu  = OM_G*((1+z)**4 + u_nu(z))
# working relations, per species: dot(N_i) = N_i g_i(N=1) => in s: dln N_i/ds - g_i(N=1)/sdot?
# actually pi source per species from d(pi_i)/ds = (a^3 F_Q) * (dQ/ds/(dln N_i/ds)) / sdot * 1
# — easier: use dot(pi_tot) = -Lambda_M q'(N_tot) N_tot; species split via weight w_i = N_i/N_tot.
w_cold = u_cold/(u_cold+u_gnu)
w_rad  = 1 - w_cold

# corrected quadrature (SIGN FIX INLINE per new rule)
integ = Q**(-2/3)*Om_s0
I = cumulative_trapezoid(integ[::-1], s[::-1], initial=0.0)[::-1]  # this IS int_0^s
F = Q**(2/3)*(-5.0*I)
# closed-form check inline (matter era)
m = (z>5)&(z<100)
print(f"inline closed-form check: F/Om_s (matter) = {np.mean(F[m]/Om_s0[m]):+.4f}   "
      f"(expected +30/17 = +{30/17:.4f})")
F_Q = -0.4*np.exp(2.5*s)*np.gradient(F, s)

# total pi (species-blind, correct)
src_pi = 2.5*a**3*F_Q/(bar_g*sdot)
tp_tot = cumulative_trapezoid(src_pi, s, initial=0.0)
tp_cold = w_cold*tp_tot           # species split
tp_rad  = w_rad *tp_tot

# per-species partial-g/partial-N contributions in each scheme
# constraint contribution D from species i = pi_i * (partial g_i/partial N) / (something) — but the
# aggregate formula D_pi = tilde_pi * (kl x) * N * E/(9 a^3) came from tilde_pi * c/R_h with
# c/R_h expressed via kl x h/2 = (kl x)(N E)/... Redo per species:
#   D_i = pi_i * (partial g_i/partial N) / (something) — actually from the closed-action derivation:
#   D_from_N_sector = -(8 pi G/3 a^3) * sum_i pi_i * (partial g_i/partial N)   (with our units)
# In H_tau0=1 units, the aggregate matches the earlier D_pi = tp * kl x N E/(9 a^3) since
# partial g/partial N = c/R_h = (kl x)(N h). Confirm this coefficient inline:
dgdN_A_cold = (KL*x)*(N*h)/N            # partial(N c/R_h)/partial N at N=1... careful: c/R_h itself
# c/R_h = kl x h from the fixed-point relation dot(c)/c = (4/3B) c^{1/4}, dot(R_h)=c on-shell.
# On the fitted trajectory, c/R_h = kl x h (holds off fixed point too via WP2). So:
cR = KL*x*h
dgdN_A_rad  = cR                        # scheme A: only sweep carries N
dgdN_B_cold = cR                        # matter: weight-drift vanishes (p^sp = 5/2)
dgdN_B_rad  = -1.5*h + cR               # radiation: -3/2 * dot(c)/c + c/R_h

# constraint contribution: D = -(8 pi G/3 a^3) sum pi_i dg_i/dN.
# In our normalization (tilde_pi = 16 pi G pi_tot, D was defined with /9), redo per species:
# D_pi_i^scheme = tilde_pi_i * dgdN_i / (some coeff). The aggregate expression
# D_pi = tp * kl x N E/(9 a^3) came from tp * cR/(6 a^3) with cR = 3(kl x)(N E)/2... let me just
# form the ratio scheme B / scheme A directly, which cancels the common coefficient:
D_A = tp_cold*dgdN_A_cold + tp_rad*dgdN_A_rad
D_B = tp_cold*dgdN_B_cold + tp_rad*dgdN_B_rad
# scale to advisory units: D_pi = tp * cR / (6 a^3), so per-species D_pi_i is
# scale = (1/(6*a**3)), but comparing schemes we just need D_A / D_B / E^2 relative changes.
scale = 1.0/(6.0*a**3)
DpiA = scale*D_A
DpiB = scale*D_B
# add p_R channel — SAME in both schemes (p_R sector unaffected by g_i internal placement)
src_P = tp_tot*N*(KL*x)**2*sdot
P = np.exp(s)*cumulative_trapezoid(src_P*np.exp(-s), s, initial=0.0)
D_pR = P/(6*a**3)
DA_tot = DpiA + D_pR
DB_tot = DpiB + D_pR

print("\n           D/E^2 comparison across schemes:")
print(f"{'z':>8} {'Scheme A':>12} {'Scheme B':>12} {'B - A':>12} {'(B-A)/A':>10}")
for zq in (1e4, 1100, 100, 20, 5, 2, 1, 0.5, 0.1, 0.0):
    i = np.argmin(abs(z-zq))
    dA, dB = DA_tot[i]/E2[i], DB_tot[i]/E2[i]
    diff = dB - dA
    rel = diff/dA if abs(dA)>1e-20 else 0
    print(f"{zq:>8} {dA:>+12.4e} {dB:>+12.4e} {diff:>+12.4e} {rel:>+10.2%}")

# Also: does the difference (B-A) affect the fitted background E(z)? NO by construction —
# E(z) comes from the closure ODE, which is scheme-independent. Confirmed by inspection.
# What about the C2 channel? Kernel F = Q^{2/3} produces the same F_Q, same pi source, same
# per-species split, so C2 sensitivity is identical in shape between schemes (only D_part differs
# by the scheme-difference term). Report kernel channel separately:
F_ker  = Q**(2/3)
FQ_ker = -0.4*np.exp(2.5*s)*np.gradient(F_ker, s)
src_pi_k = 2.5*a**3*FQ_ker/(bar_g*sdot)
tpk = cumulative_trapezoid(src_pi_k, s, initial=0.0)
tpk_cold, tpk_rad = w_cold*tpk, w_rad*tpk
DkerA = scale*(tpk_cold*dgdN_A_cold + tpk_rad*dgdN_A_rad)
DkerB = scale*(tpk_cold*dgdN_B_cold + tpk_rad*dgdN_B_rad)
i = np.argmin(abs(z-0))
print(f"\nkernel channel (per unit C2), z=0: A: {DkerA[i]/E2[i]:+.4e}   B: {DkerB[i]/E2[i]:+.4e}")
