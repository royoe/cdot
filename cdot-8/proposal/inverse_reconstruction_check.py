#!/usr/bin/env python3
"""
inverse_reconstruction_check.py — 2026-07-12, advisory companion (third WP3
escalation). Every number in Advisory-WP3-InverseReconstruction-2026-07-12.md
in one pass.

Five parts:
  (1) Foundation 5.5's quoted "a0hat(z)/a0hat(0)" values are ABSOLUTE values in
      1e-10 m/s^2 (anchor a0(0)=1.39e-10), not ratios: reproduced exactly from
      the four-term trajectory (kappa*lambda=0.4355, delta0=-0.0909) times 1.39.
  (2) The exact identity a0hat(z)/a0hat(0) = E(z) = H_tau(z)/H_tau0: the
      a0_confrontation.py ratio formula and budget_invoice.py's E(s) are the
      same algebraic expression; equivalently a0hat = (2/3)*lambda*c0*H_tau
      identically on ANY trajectory (one line from a0 = lambda*cdot plus the
      redshift law).
  (3) The worker's forced Q(a) (xi*Q = -H0^2 a^4 dOmega_s/da) reproduced on the
      actual invoice trajectory — confirming their algebra before rejecting
      their premise.
  (4) The corrected reconstruction: with Q fixed by M1's khronon-clock
      identification, Q = dt/dtau = (1+z)^{5/3} (exact on any trajectory), F(Q)
      exists by quadrature d(F/Q)/dQ = 3 H0^2 Omega_s / Q^2. Matter era:
      d lnF/d lnQ -> 9/5; demanded shift-current violation is exactly ONE lapse
      factor: a^3 F_Q ∝ a^{5/3} = dtau/dt (free AeST would be a^0 = const).
  (5) Fixed-point analytics: a0hat ∝ Q^{9/10} exactly; the effective exponent n
      in a0hat ∝ Q^n along the fitted trajectory (0.4–0.9, nothing near the
      worker's n >~ 7, which divided a 1.39x-inflated growth by an
      artifact-flat Q_forced).
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d

# ---- four-term fit numbers (Foundation 2.2) -----------------------------------
KL, EPS0 = 0.4355, -0.0909          # kappa*lambda, delta_0
A0_TODAY = 1.39                      # fitted a0(0) in 1e-10 m/s^2
F55_QUOTED = {0.33: 1.69, 0.85: 2.35, 1.00: 2.57, 1.44: 3.30}  # Foundation 5.5

# ---- invoice-trajectory constants (as budget_invoice.py) ----------------------
X0 = 1.10
T_G0, A_RAD, C0, G_N, H = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11, 0.70
K_B_EV = 8.617333e-5
rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)
u_g0 = A_RAD*T_G0**4
OM_G = (u_g0/C0**2)/rho_crit
T_NU0 = (4/11)**(1/3)*T_G0
M_NU = 1.374/3
OM_CL = 0.074

def mu_s(x):  return x/(1+x)
def imu_s(y): return y/(1-y)

# ================================================================================
# (1) Foundation 5.5: absolute values, not ratios
#     Pure-matter closure trajectory exactly as cdot-7/Fable-1/closure_dynamics.py
#     (a_code = c/c0, source = matter only), a0hat ratio as a0_confrontation.py.
# ================================================================================
xs = 3.0/(4*KL)
mus = mu_s(xs)
r0 = 1.0 + EPS0
rhs = lambda a, Y: [KL*imu_s(min(mus*Y[0]**2/a**1.5, 1-1e-13))*Y[0]/a]
solm = solve_ivp(rhs, [1.0, 1e-3], [r0], dense_output=True, rtol=1e-11, atol=1e-13)
x0m = imu_s(min(mus*r0*r0, 1-1e-13))

def a0hat_ratio(z):
    """(x0 r0)/(x r) * (1+z)  [a0_confrontation formula; a_code^{-3/2} = 1+z]."""
    ac = (1+z)**(-2/3)
    r = solm.sol(ac)[0] if z > 0 else r0
    x = imu_s(min(mus*r*r/ac**1.5, 1-1e-13))
    return (x0m*r0)/(x*r)*(1+z)

print("(1) Foundation 5.5 labeling check (four-term trajectory, x0 = %.4f):" % x0m)
print(f"    {'z':>5} {'ratio (traj)':>13} {'x 1.39':>8} {'F5.5 quoted':>12} {'quoted/ratio':>13}")
for z, q in F55_QUOTED.items():
    rat = a0hat_ratio(z)
    print(f"    {z:5.2f} {rat:13.3f} {rat*A0_TODAY:8.3f} {q:12.2f} {q/rat:13.3f}")
print("    => quoted values are a0hat(z) in 1e-10 m/s^2 (anchor 1.39), NOT ratios.")
print("       True fitted ratios: growth x%.2f by z=1, not x%.2f."
      % (a0hat_ratio(1.0), F55_QUOTED[1.00]))

# ================================================================================
# (2) The identity a0hat(z)/a0hat(0) = E(z) = H_tau/H_tau0
#     One line: a0 = lam*cdot, H_t = (3/2)cdot/c (exact from the redshift law),
#     local accel unit ~ c^{7/2}, H_tau = H_t (c0/c)^{5/2}  =>
#     a0hat/H_tau = (2/3) lam c0 = const on ANY trajectory.
#     Numerically: both formulas are e^{-3s/2} x0/(x r) — identical expressions.
# ================================================================================
print("\n(2) identity a0hat ratio == E(z) (same trajectory, same formula):")
for z in (0.33, 0.85, 1.00, 1.44):
    s_t = -(2/3)*np.log(1+z)                     # s = ln(c/c0), 1+z = e^{-3s/2}
    ac = np.exp(s_t)
    r = solm.sol(ac)[0]
    x = imu_s(min(mus*r*r/ac**1.5, 1-1e-13))
    E_t = np.exp(-1.5*s_t)*(x0m*r0)/(x*r)        # E(s) = e^{-3s/2} x0 r0/(x r)
    print(f"    z={z}: E = {E_t:.4f}   a0hat ratio = {a0hat_ratio(z):.4f}   "
          f"diff = {abs(E_t-a0hat_ratio(z)):.1e}")
print("    => a0hat = (2/3)*lambda*c0*H_tau identically; the a0 ~ cH coincidence")
print("       is an exact trajectory-wide identity of the framework.")

# ================================================================================
# Three-component invoice trajectory (exactly as budget_invoice.py) for (3)-(5)
# ================================================================================
F0 = 7*np.pi**4/120
ag = np.concatenate([[0], np.logspace(-3, 7, 500)])
Fg = np.array([quad(lambda x, A=A: x*x*np.sqrt(x*x+A*A)/(np.exp(x)+1), 0, 60,
                    limit=300)[0] for A in ag])
Fi = interp1d(np.log10(ag[1:]), np.log10(Fg[1:]), kind='cubic')
def F_fast(A):
    A = np.asarray(A, float)
    return np.where(A < 1e-3, F0, 10**Fi(np.log10(np.maximum(A, 1e-3))))
REL = (7/8)*(4/11)**(4/3)
def u_nu(z):
    A = M_NU/(K_B_EV*T_NU0*(1+z))
    return 3*REL*(1+z)**4*F_fast(A)/F0
om_nu0 = float(u_nu(0.0))*u_g0/C0**2/rho_crit
om_cold = OM_CL - om_nu0
def u_hat(z):
    return om_cold*(1+z)**3 + OM_G*(1+z)**4 + OM_G*u_nu(z)
u0 = float(u_hat(0.0))
def S(s):
    z = np.exp(-1.5*s)-1
    return (u_hat(z)/u0)*np.exp(5*s)

mu0 = mu_s(X0)
def x_of(r, s):
    return imu_s(min(mu0*r*r*np.exp(-2*s)*float(S(s)), 1-1e-13))
sol = solve_ivp(lambda s, r: [KL*x_of(r[0], s)*r[0]], (0, -9.6), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
s = np.linspace(-1e-6, -9.6, 12000)
r = sol.sol(s)[0]
x = np.array([x_of(ri, si) for ri, si in zip(r, s)])
a = np.exp(1.5*s); z = 1/a - 1
E = np.exp(-1.5*s)*X0/(x*r)
E2 = E*E
u = np.array([float(u_hat(zi)) for zi in z])
Om_s = E2 - u                                    # the invoice (M7)

# ================================================================================
# (3) worker's forced Q reproduced (their algebra is correct)
# ================================================================================
Qf = -a**4*np.gradient(Om_s, a)
Qf0 = Qf[0]
print("\n(3) worker's Q_forced = -H0^2 a^4 Omega_s'(a), normalized (their table):")
for zt, ref in [(0.33, 0.948), (0.85, 0.911), (1.00, 0.906), (1.44, 0.895), (20, 0.861)]:
    i = np.argmin(abs(z-zt))
    print(f"    z={zt:>5}: {Qf[i]/Qf0:.3f}   (worker: {ref})")
print("    => algebra confirmed; premise (free shift-current F_Q ~ a^-3) is what fails.")

# ================================================================================
# (4) corrected reconstruction: Q from M1, F(Q) by quadrature
#     Q = dt/dtau = (1+z)^{5/3} exact on any trajectory (lapse (c/c0)^{5/2},
#     redshift law (c0/c)^{3/2}).  d(F/Q)/dQ = 3 Om_s/Q^2  (H0 = 1 units).
#     Gauge: additive C*Q piece has F - Q F_Q = 0 (zero density; total
#     derivative in the action) — quadrature run in C = 0 gauge.
# ================================================================================
Q = (1+z)**(5/3)
FoQ = cumulative_trapezoid(3*Om_s/Q**2, Q, initial=0.0)
F = Q*FoQ
F_Q = np.gradient(F, Q)
lna = np.log(a)
with np.errstate(divide='ignore', invalid='ignore'):
    slopeF = np.gradient(np.log(np.abs(F)+1e-30), np.log(Q))
    srcJ = np.gradient(np.log(np.abs(a**3*F_Q)+1e-30), lna)
print("\n(4) corrected reconstruction (Q = (1+z)^{5/3} from M1):")
print(f"    {'z':>6} {'d lnF/d lnQ':>12} {'(-> 9/5)':>9} {'d ln(a^3 F_Q)/d ln a':>21} {'(-> 5/3)':>9}")
for zt in (5, 20, 100):
    i = np.argmin(abs(z-zt))
    print(f"    {zt:>6} {slopeF[i]:12.3f} {1.8:9.2f} {srcJ[i]:21.3f} {5/3:9.3f}")
print("    free AeST current conservation would demand d ln(a^3 F_Q)/d ln a = 0;")
print("    the census closure demands exactly ONE lapse factor: a^3 F_Q ∝ dtau/dt = a^{5/3}.")

# ================================================================================
# (5) fixed-point analytics and the effective exponent n in a0hat ∝ Q^n
# ================================================================================
print("\n(5) a0hat vs Q with both correctly identified:")
print("    fixed point: a0hat ∝ (1+z)^{3/2}, Q ∝ (1+z)^{5/3}  =>  n = 9/10 exactly.")
print("    fitted trajectory (corrected ratios):")
for zt in (0.33, 0.85, 1.00, 1.44):
    rat = a0hat_ratio(zt)
    n = np.log(rat)/np.log((1+zt)**(5/3))
    print(f"    z={zt}: a0hat ratio = {rat:.3f}, Q = {(1+zt)**(5/3):.3f}  =>  n = {n:.2f}")
print("    => n in 0.4-0.9, sub-linear; nothing near n >~ 7 (that figure divided a")
print("       1.39x-inflated a0hat growth by the over-determined, artifact-flat Q_forced).")
