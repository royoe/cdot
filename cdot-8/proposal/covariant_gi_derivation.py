#!/usr/bin/env python3
"""
covariant_gi_derivation.py — 2026-07-15. Derive g_i unambiguously from M4's
covariant foliation-integral definition, resolving both open questions:
  (a) does the census/horizon sector need a lapse promotion at all?
  (b) does the covariant derivation reproduce the factor of 3, or scheme A, or B,
      or a third form?

Definition (M4, WP2 §1): N_i(t) = int_{Sigma_t cap horizon} rho_E,i / E_P
  where the integrand is a scalar density under reparametrization, the domain
  is a spatial slice of the aether-orthogonal foliation, and the horizon is
  the closure's own r(s) surface.

On the homogeneous background: N_i(t) = rho_coord,i(t) * V_horizon(t) / m_P^coord(t)
  with rho_coord,i ∝ c^{p_i} (dictionary), V_horizon ∝ R_h(t)^3, m_P^coord ∝ c^{5/2}.

Under a reparametrization t -> t'(t), N_i is a SCALAR (a count is a count — 
does not transform), while dt and R_h's *rate* dR_h/dt do transform. The
covariant statement of "shell sweep": the shell entering the horizon per unit
PROPER time is dR_h/dtau = c (this is the physical statement, in the atomic-
clock frame). In coordinate time, dR_h/dt = c * dtau/dt = c * N. So R_h's own
defining relation IS lapse-carrying: dR_h/dt = Nc — the closed-action round's
lapse promotion of this specific relation was correct.

Similarly, the density-drift term (p_i^sp - 5/2) dot(c)/c is a log-derivative
of a scalar quantity — a scalar per unit t. Log-derivatives on the coordinate
clock stay coordinate-clock; no reparametrization introduces a lapse.

So the correct closed-action g_i has:
  - shell-sweep piece: 3 * Nc/R_h  (worker's factor of 3, WP2's original, plus
    scheme A's lapse placement on the sweep term)
  - density-drift piece: (p_i^sp - 5/2) dot(c)/c  (no lapse — it's a coordinate
    log-derivative of a scalar)
That's neither pure scheme A (missing the 3) nor scheme B (extra N on drift).
It's a THIRD form, matching WP2 verbatim at N=1 (as required) and carrying the
lapse on exactly the term whose covariant derivation demands it.

Test: integrate d(ln N_rad)/ds = g_rad^covariant / sdot with real N(t), compare
to the direct algebraic result from the worker's §2 definition
  d(ln N_rad)/ds = -3/2 + 3 dln(r)/ds
which is exact by construction.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.special import zeta

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
sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-9.6), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
s = np.linspace(-9.4, -1e-6, 12000)
r = sol.sol(s)[0]
x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
E = np.exp(-1.5*s)*X0/(x*r); N = np.exp(2.5*s)
sdot = (2/3)*N*E
h    = 1.5*sdot                        # dot(c)/c
cR   = KL*x*h                          # c/R_h on-shell (=kl x h; verify below)

# Verify c/R_h = kl x h on the fitted trajectory (not just fixed point)
# c/R_h from mu(x) = mu0 r^2 e^{-2s} S(s) => x = mu^-1(mu0 r^2 ...) ; R_h = r R_h0
# Alternative: from AQUAL definition of x itself in cdot-7. Trust WP2's derivation:
# The relation c/R_h = kl x dot(c)/c IS the definition of x on the fitted trajectory
# (dot c / c = kl x r_dot / r ; dot r / r = kl x dot c/c ; combine with dot R_h = c)
# So cR = kl x h is exact by construction of x. Numerical check:
dlnr_ds = np.gradient(np.log(r), s)
xk_check = dlnr_ds/(KL*1.0)  # should equal x from d ln r / ds = kl x
print(f"cross-check: x from d(ln r)/ds vs x from mu: max rel diff = "
      f"{np.max(np.abs(xk_check-x)/x):.2e}")

# ALGEBRAIC target (worker's §2 result, verified there):
#   d ln N_rad/ds = -3/2 + 3 * d ln r/ds  (radiation, p^sp = 1)
#   d ln N_cold/ds = 0 + 3 * d ln r/ds     (matter, p^sp = 5/2, drift zero)
target_rad_s  = -1.5 + 3*dlnr_ds
target_cold_s =        3*dlnr_ds

# SCHEME candidates evaluated on the trajectory (in d/ds form: /sdot):
# A (worker's original closed action, WITH missing factor of 3, WITH single N on sweep):
gA_rad_s = (-1.5*h + 1*N*cR)/sdot
# B (scheme B, uniform N on whole bracket, WITH missing 3):
gB_rad_s = N*(-1.5*h + 1*cR)/sdot
# CORRECTED FORM proposed above: covariant derivation, factor 3, N only on sweep:
gCov_rad_s  = (-1.5*h + 3*N*cR)/sdot
gCov_cold_s = (   0   + 3*N*cR)/sdot

# Compare (at N=1 all should reduce; but with real N(t) only the covariant form should track)
print("\ntest of each candidate g_rad(s)/sdot against the exact algebraic target:")
print(f"{'z':>10} {'target':>10} {'A':>10} {'B':>10} {'Covariant':>12}")
for zq in (0.0, 1, 10, 100, 1e3, 1e4, 1e5):
    i = np.argmin(abs(np.exp(-1.5*s)-1-zq))
    print(f"{zq:>10} {target_rad_s[i]:>10.4f} {gA_rad_s[i]:>10.4f} "
          f"{gB_rad_s[i]:>10.4f} {gCov_rad_s[i]:>12.4f}")

# Cold species check
print("\ncold: covariant vs target (should agree)")
for zq in (0.0, 10, 1000):
    i = np.argmin(abs(np.exp(-1.5*s)-1-zq))
    print(f"z={zq:>6}: target = {target_cold_s[i]:.4f}   covariant = {gCov_cold_s[i]:.4f}")

# Full-trajectory residual for the covariant form
rad_resid = np.max(np.abs(gCov_rad_s - target_rad_s))
cold_resid = np.max(np.abs(gCov_cold_s - target_cold_s))
print(f"\nfull-trajectory max residual: rad {rad_resid:.2e}, cold {cold_resid:.2e}")
