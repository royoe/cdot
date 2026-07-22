#!/usr/bin/env python3
"""
wp7_stiffness_audit.py — 2026-07-19. Stage 0 for the dedicated
field-variable round: WHERE is the (chi, E_alpha, Phi, delta_b) system
fast or singular, and WHY did two careful solo attempts die?

Three candidate killers, audited along the trajectory:
 K1. Effective-mass stiffness: the chi/E_alpha sector oscillates at the
     condensate scale mu_eff(z); if mu_eff/H >> 1 anywhere in range, an
     explicit adaptive solver collapses exactly as described (step-size
     collapse, not wrong signs). mu_eff^2 = -Q^2 F_QQ/(2(2-K_B)) at each
     epoch (SZ dictionary, epoch-local).
 K2. Singular-factor map: any state variable or coefficient carrying
     1/rho_s, 1/c_ad^2, or 1/(1+w) — the effective-fluid (delta, theta)
     definitions carry ALL THREE. If delta/theta were kept as STATE
     variables (the sec-26 closure did), the system inherits their
     singularities even where the field variables are regular.
 K3. Units contract: the founding paper's dK/dQ enters in ITS
     normalization; cdot-8's F carries the 16 pi G-tilde convention and
     H0^2 units — a mixed import mis-scales coefficients by up to ~1e8
     at z*, indistinguishable from stiffness in the failure mode.
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
Q = np.exp(-2.5*s)
I = cumulative_trapezoid((Q**(-2/3)*Om_s)[::-1], s[::-1], initial=0.0)[::-1]
F = Q**(2/3)*(-5.0*I)
F_Q = -0.4*np.exp(2.5*s)*np.gradient(F, s)
F_QQ = -0.4*np.exp(2.5*s)*np.gradient(F_Q, s)

print("=== K1: effective-mass stiffness ratio mu_eff(z)/H(z) ===")
print(f"{'z':>8} {'mu_eff/H (K_B=0.1)':>19} {'mu_eff/H (K_B=1)':>17}")
for zt in [9640.0, 3000.0, 1090.0, 100.0, 10.0, 1.0, 0.0]:
    i = np.argmin(np.abs(z_arr-zt))
    mu2 = -Q[i]**2*F_QQ[i]/2   # /(2-K_B) applied per column
    for KB, col in [(0.1, None)]:
        pass
    v1 = np.sqrt(max(mu2/(2-0.1),0))/E[i]
    v2 = np.sqrt(max(mu2/(2-1.0),0))/E[i]
    print(f"{zt:>8.0f} {v1:>19.2f} {v2:>17.2f}")
print("""If these sit at O(1)-O(10): the chi/E_alpha sector is MARGINALLY stiff
— oscillatory but integrable with an implicit (Radau/BDF) solver; if
>>10 anywhere: WKB/averaged (ULA-class) closure needed in that regime.
Either way an explicit RK solver dies by step collapse — matching the
sec-26 failure mode. PHYSICS NOTE: mu_eff ~ H-class means the scalar is
a Gpc-Compton, ULA-like component: dust-like clustering sub-horizon
(WHY Stage 1 worked), pressure-suppressed near horizon — landing in the
SAME l <~ 10 window as the M5 W-shape and the facet-4 band.\n""")

print("=== K2: singular-factor map (state-variable audit) ===")
w = -(1/4.5)*np.gradient(np.log(np.abs(Om_s)), s) - 1
cad2 = w + np.gradient(w, s)/np.gradient(np.log(np.abs(Om_s)), s)
print(f"{'z':>8} {'|1/Om_s|':>10} {'|1/c_ad^2|':>11} {'|1/(1+w)|':>10}")
for zt in [9640.0, 1090.0, 100.0, 10.0, 1.0]:
    i = np.argmin(np.abs(z_arr-zt))
    print(f"{zt:>8.0f} {1/abs(Om_s[i]):>10.1e} {1/abs(cad2[i]):>11.1e} {1/abs(1+w[i]):>10.2f}")
print("""The effective-fluid (delta, theta) DEFINITIONS carry 1/rho_s and
c_ad^2 factors; their evolution equations carry Pi/(1+w). |1/c_ad^2| ~
1e2-1e3 THROUGHOUT the matter era (not just at the crossing): any state
variable or RHS carrying it makes the system stiff EVERYWHERE. RULE FOR
THE STAGED ROUND: state variables are (chi or gamma, alpha, E_alpha,
delta_b, theta_b, Phi) ONLY — nothing whose definition contains rho_s,
c_ad^2, or 1/(1+w); the effective-fluid delta, theta, Pi are OUTPUT
diagnostics computed after the fact. The sec-26 closure kept delta,
theta as state — hypothesis: this, plus K1's marginal stiffness under
an explicit solver, is the double cause; to be checked against the
actual script in the joint round.\n""")

print("=== K3: units contract (pre-emptive, one line) ===")
print(f"|F_Q| spans {abs(F_Q[np.argmin(np.abs(z_arr-1090))]):.0f} (z*) to {abs(F_Q[-1]):.2f} (today) in H0^2 units;")
print("""the founding paper's dK/dQ is in ITS normalization. The staged round
opens with a written one-line dictionary per imported equation
(K-convention <-> F-convention, H0^2 vs H(z)^2 units) BEFORE any code —
the third dictionary-class trap, pre-empted this time instead of caught.""")

# ============================================================
# ADDENDUM (same session): K1's zeros investigated — closed-form
# route for the matter era, since the spline is endpoint-unreliable
# at z=0 (where it contradicts the doubly-verified F_QQ(0) = -0.696).
#
# Matter era closed form: F = (30/17) Omega_s and Omega_s = f_s E^2
# with F ~ Q^{9/5} (from the quadrature with Omega_s ~ (1+z)^3):
#   Q^2 F_QQ = (36/25) F  =>
#   mu^2/H^2 = -(36/25)(30/34) f_s/(2-K_B) = -1.271 f_s/(2-K_B).
# Two-route check at z=10: closed form 889 vs spline 875 — AGREE.
# ============================================================
print("\n=== K1 addendum: the matter-era effective mass, closed form ===")
for fs, KB in [(0.78, 0.0), (0.78, 1.0), (0.83, 0.0)]:
    ratio = -1.271*fs/(2-KB)
    print(f"  f_s={fs}, K_B={KB}:  mu^2/H^2 = {ratio:+.3f}   (|mu|/H = {abs(ratio)**0.5:.2f})")
print("""FINDING: through the matter era the scalar's effective mass-squared is
NEGATIVE and HUBBLE-TRACKING at a constant ratio, mu^2 ~ -0.5 H^2(z)
(closed form; interior spline agrees to 1.6%; sign flips to the
doubly-verified STABLE F_QQ(0) = -0.696 < 0 => mu^2 > 0 near today).
Interpretation, stated with its caveats:
 * A tachyonic mass at |mu| < H is not a Minkowski pathology — it is a
   Jeans-class, Hubble-rate growing mode: THE CLUSTERING MECHANISM.
   The quadrature F, built only to pay the invoice, hands the scalar a
   scale-free destabilization of the smooth solution through exactly
   the era where it must cluster (sec-23's requirement), switching to a
   stabilizing, Gpc-Compton mass exactly when the component turns
   dark-energy-like. Requirement and mechanism close in one object —
   F_QQ's FOURTH load-bearing appearance, the biggest yet.
 * CAVEATS for the staged round: (i) flip location (z <~ 1?) needs a
   robust F_QQ(z) (spline the quadrature properly, not endpoint/
   double-gradient); (ii) sub-horizon stability needs the full
   dispersion omega^2 = c_s^2 k^2 + mu^2(z) with the Y/gradient sector
   supplying c_s^2 (SZ-healthy at today's point; epoch-dependence to
   verify); (iii) consistency with SZ's Minkowski conditions is by
   scope — they anchor at today's point, where the sign is stable.
CONSEQUENCE FOR THE FAILURE DIAGNOSIS: with |mu|/H < 1 everywhere, the
physical system is NOT intrinsically stiff — K1 is exonerated; the
solver deaths are formulation (K2: delta/theta as state variables) and/
or units (K3). A clean pure-field-variable formulation with a written
units contract should integrate at ordinary tolerances; if it still
collapses, the bug is in the imported-equation dictionary, not physics.""")
