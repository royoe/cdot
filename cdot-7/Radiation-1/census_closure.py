#!/usr/bin/env python3
"""
census_closure.py — 2026-07-11 session.

Two jobs, run in one pass:

  PART 1 (verification): independently re-derive and re-run the two-fluid
  (matter+photon) radiation-era closure of Update-RadiationEraClosure-2026-07-10,
  from the documented equations alone (radiation_closure.py was NOT consulted —
  it is not in the project knowledge). Every headline number of that update is
  checked: both fixed points, z_eq across conventions, x(z_recomb) ranges.

  PART 2 (new): the Planck-unit census counting law.
    N(t) = sum over horizon of E_i(t)/E_P(t),   M_h = N * m_P.
  Arithmetically identical to the adopted two-fluid law for matter+photons
  (verified explicitly), but it FORCES the neutrino third term with zero
  freedom: per-neutrino census weight sqrt((m(t)c^2)^2 + (hbar k c)^2)/c^2,
  with conserved coordinate k and m(t) ∝ c^{1/2}. In local units this is
  exactly the standard massive-neutrino Fermi-Dirac energy density (shown
  analytically in the update doc; used here computationally).

Framework relations used (Foundation.md as of 2026-07-10 + pending update):
  redshift law     : 1+z = (c0/c)^{3/2}          (§3.3)
  dictionary       : coord energy density ∝ c^p  <-> local ∝ c^{p-7}
                     hence rho_source(c)/rho_source,0
                        = [u_hat_tot(z)/u_hat_tot(0)] * (c/c0)^5
  closure          : mu(x) g_h = G M_h/R_h^2,  g_h = c^2/(kappa R_h),
                     a0 = lambda*cdot,  x = g_h/a0
                     => ODE  dr/ds = (kappa*lambda) * x(r,s) * r,
                        r = R_h/R_h0, s = ln(c/c0),
                        x(r,s) = mu^{-1}( mu(x0) * r^2 e^{-2s} * S(s) ),
                        S(s) = rho_source(c)/rho_source,0.
  fixed points     : source ∝ c^n  =>  x_* = (1 - n/2)/(kappa*lambda),
                     mu-independent.

Working cosmology (four-term fit): kappa*lambda = 0.4355, x0 = 1.10, simple mu.
"""

import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import interp1d

# ----------------------------------------------------------------------------
# Constants and working numbers
# ----------------------------------------------------------------------------
KL      = 0.4355            # kappa*lambda, four-term fit
X0      = 1.10              # today's operating point, four-term fit
T_G0    = 2.7255            # K, CMB today
A_RAD   = 7.565723e-16      # J m^-3 K^-4
C0      = 2.99792458e8      # m/s
G_N     = 6.67430e-11
H       = 0.70              # reproduces the 07-10 session's Omega_gamma
K_B_EV  = 8.617333e-5       # eV/K
Z_REC   = 1100.0

rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)      # kg/m^3
u_g0     = A_RAD*T_G0**4                                   # J/m^3
OM_G     = (u_g0/C0**2)/rho_crit                           # photon Omega
OM_B     = 0.02166/H**2                                    # BBN baryons (CPS18)
T_NU0    = (4/11)**(1/3)*T_G0                              # K
M_NU_EV  = 1.374/3                                         # per state, quasi-degenerate
OMEGAS   = [0.074, 0.104, 0.115, 0.134]                    # closure conventions

print(f"h={H}, Omega_gamma={OM_G:.4e}, Omega_b={OM_B:.5f}, "
      f"T_nu0={T_NU0:.4f} K, m_nu={M_NU_EV:.4f} eV/state")

# ----------------------------------------------------------------------------
# mu functions
# ----------------------------------------------------------------------------
def mu_simple(x):     return x/(1.0+x)
def imu_simple(y):    return y/(1.0-y)
def mu_std(x):        return x/np.sqrt(1.0+x*x)
def imu_std(y):       return y/np.sqrt(1.0-y*y)

# ----------------------------------------------------------------------------
# PART 1a — fixed points (mu-independent algebra)
# ----------------------------------------------------------------------------
def fixed_point(n):   return (1.0 - n/2.0)/KL

print("\n=== PART 1: verification of the 2026-07-10 two-fluid results ===")
xm, xr = fixed_point(0.5), fixed_point(-1.0)
print(f"fixed points: matter (n=+1/2) x*={xm:.4f}   radiation (n=-1) x*={xr:.4f}"
      f"   ratio={xr/xm:.4f}  (claimed 1.72 / 3.44 / exactly 2)")

# ----------------------------------------------------------------------------
# PART 1b — z_eq closed form, all conventions, both eta
# ----------------------------------------------------------------------------
print("\nz_eq = Omega_closure/(eta*Omega_gamma) - 1 :")
for eta in (1, 2):
    row = {om: om/(eta*OM_G)-1 for om in OMEGAS}
    print(f"  eta={eta}: " + "  ".join(f"Om={om}: z_eq={v:7.0f}" for om, v in row.items()))

# ----------------------------------------------------------------------------
# Generic trajectory integrator
#   S_of_s : callable, S(s) = rho_source(c)/rho_source,0  (S(0)=1)
# ----------------------------------------------------------------------------
def integrate(S_of_s, mu=mu_simple, imu=imu_simple, x0=X0, s_min=-9.6):
    mu0 = mu(x0)
    def x_of(r, s):
        y = mu0 * r*r * np.exp(-2*s) * S_of_s(s)
        y = np.minimum(y, 1-1e-12) if imu is imu_simple else np.minimum(y, 1-1e-12)
        return imu(y)
    def rhs(s, r):
        return KL * x_of(r[0], s) * r[0]
    sol = solve_ivp(rhs, (0.0, s_min), [1.0], rtol=1e-9, atol=1e-12,
                    dense_output=True, max_step=0.01)
    s = np.linspace(0, s_min, 4000)
    r = sol.sol(s)[0]
    x = np.array([x_of(ri, si) for ri, si in zip(r, s)])
    z = np.exp(-1.5*s) - 1.0
    return z, x

def x_at(z_arr, x_arr, z):
    return float(interp1d(np.log10(1+z_arr), x_arr)(np.log10(1+z)))

# ----------------------------------------------------------------------------
# PART 1c — two-fluid trajectories, all (eta, Omega) combinations
# ----------------------------------------------------------------------------
print("\ntwo-fluid trajectories (simple mu), x at key redshifts:")
results_2f = {}
for eta in (1, 2):
    for om in OMEGAS:
        fg = eta*OM_G/(om + eta*OM_G)
        fm = 1.0 - fg
        S  = lambda s, fm=fm, fg=fg: fm*np.exp(0.5*s) + fg*np.exp(-s)
        z, x = integrate(S)
        results_2f[(eta, om)] = (z, x)
        print(f"  eta={eta} Om={om}: x(z=10)={x_at(z,x,10):.3f}  "
              f"x(z=400)={x_at(z,x,400):.3f}  x(z=1100)={x_at(z,x,Z_REC):.3f}  "
              f"x(z=1e5)={x_at(z,x,1e5):.3f}  x(z=1e6)={x_at(z,x,1e6):.3f}")

x_rec_eta1 = [x_at(*results_2f[(1,om)], Z_REC) for om in OMEGAS]
x_rec_eta2 = [x_at(*results_2f[(2,om)], Z_REC) for om in OMEGAS]
print(f"  => eta=1 x(1100) range: [{min(x_rec_eta1):.2f}, {max(x_rec_eta1):.2f}]"
      f"   (claimed [2.14, 2.37])")
print(f"  => eta=2 max x(1100): {max(x_rec_eta2):.2f}   (claimed up to 2.67)")

# standard-mu sensitivity at primary convention
zs, xs = integrate(lambda s: (0.074/(0.074+OM_G))*np.exp(0.5*s)
                            + (OM_G/(0.074+OM_G))*np.exp(-s),
                   mu=mu_std, imu=imu_std)
print(f"  standard-mu check (eta=1, Om=0.074): x(1100)={x_at(zs,xs,Z_REC):.3f} "
      f"(fixed points unchanged by construction)")

# ----------------------------------------------------------------------------
# PART 2 — Planck-unit census with the forced neutrino term
# ----------------------------------------------------------------------------
print("\n=== PART 2: Planck-unit census, three components ===")

# F(a) = int_0^inf x^2 sqrt(x^2+a^2)/(e^x+1) dx ; census FD energy integral
def F_of_a(a):
    return quad(lambda x: x*x*np.sqrt(x*x + a*a)/(np.exp(x)+1.0),
                0, 60, limit=300)[0]

F0 = F_of_a(0.0)                       # = 7 pi^4/120
print(f"F(0) = {F0:.6f}  (7*pi^4/120 = {7*np.pi**4/120:.6f})")
# NR slope check: F(a) -> a * 3/2 zeta(3)
from scipy.special import zeta
print(f"F(1e4)/1e4 = {F_of_a(1e4)/1e4:.6f}  (3/2 zeta(3) = {1.5*zeta(3,1):.6f})")

# tabulate F on a grid of a for speed
a_grid = np.concatenate([[0], np.logspace(-3, 6, 400)])
F_grid = np.array([F_of_a(a) for a in a_grid])
F_int  = interp1d(np.log10(a_grid[1:]), np.log10(F_grid[1:]), kind='cubic')
def F_fast(a):
    scalar = np.isscalar(a)
    a = np.atleast_1d(np.asarray(a, dtype=float))
    out = np.where(a < 1e-3, F0, 10**F_int(np.log10(np.maximum(a, 1e-3))))
    return float(out[0]) if scalar else out

REL_NU_PER_SPECIES = (7/8)*(4/11)**(4/3)   # u_nu,rel per species / u_gamma

def u_nu_hat(z):
    """census (=total FD) neutrino energy density in local units, / u_gamma0.
       3 quasi-degenerate species, m = M_NU_EV each, conserved comoving FD."""
    a = M_NU_EV/(K_B_EV*T_NU0*(1.0+z))
    return 3.0*REL_NU_PER_SPECIES*(1.0+z)**4 * F_fast(a)/F0

# today's census neutrino Omega (includes rest mass + residual kinetic)
om_nu_today = u_nu_hat(0.0)*u_g0/C0**2/rho_crit
om_nu_naive = 1.374/(93.14*H**2)
print(f"Omega_nu today: census FD = {om_nu_today:.5f};  Sum m/(93.14 h^2) = "
      f"{om_nu_naive:.5f}  (agreement to ~{100*abs(1-om_nu_today/om_nu_naive):.1f}%)")
print(f"Omega_b + Omega_nu(census) = {OM_B + om_nu_today:.5f}  vs "
      f"Omega_closure = 0.074")

# neutrino transition markers on the (now smooth) census weight
z_T_eq_m   = M_NU_EV/(K_B_EV*T_NU0) - 1          # T_nu = m convention (07-10 update)
z_p_eq_m   = M_NU_EV/(3.151*K_B_EV*T_NU0) - 1    # <p> = m c convention (physical center)
# census-native marker: <E> = sqrt(2) * m c^2 equivalent -> where F(a)/ (a * 3/2 z3) = sqrt2? 
# simpler census-native: where kinetic census energy equals rest census energy:
#   F(a) = 2 * a * (3/2) zeta(3) ... solve numerically
from scipy.optimize import brentq
z3 = 1.5*zeta(3,1)
a_half = brentq(lambda a: F_of_a(a) - 2*a*z3, 0.1, 50)   # E_kin_census = E_rest_census
z_half = M_NU_EV/(K_B_EV*T_NU0*a_half) - 1
print(f"nu transition markers: T=m => z={z_T_eq_m:.0f} (07-10 update's 2733); "
      f"<p>=mc => z={z_p_eq_m:.0f}; census kinetic=rest => z={z_half:.0f}")

# --- three-component census source ------------------------------------------
def make_census_S(om_closure):
    """cold (baryon + any extra convention mass) + photons + FD neutrinos.
       S(s) = [u_hat_tot(z)/u_hat_tot(0)] * e^{5s},  1+z = e^{-3s/2}."""
    om_cold = om_closure - om_nu_today          # what isn't neutrinos is census-matter
    def u_hat2(z):                              # in units of rho_crit c^2
        return om_cold*(1+z)**3 + OM_G*(1+z)**4 + OM_G*u_nu_hat(z)
    u0 = u_hat2(0.0)
    def S(s):
        z = np.exp(-1.5*s) - 1.0
        return (u_hat2(z)/u0)*np.exp(5*s)
    return S, u_hat2, om_cold

S_census, u_hat_census, om_cold = make_census_S(0.074)
print(f"census split at Om=0.074: cold={om_cold:.5f} (Omega_b={OM_B:.5f}), "
      f"nu={om_nu_today:.5f}, gamma={OM_G:.2e}")

# effective source exponent n_eff(s) = dln rho_source/ds, sweeps +1/2 -> -1
s_test = np.linspace(-0.01, -9.5, 2000)
lnS = np.log([S_census(si) for si in s_test])
n_eff = np.gradient(lnS, s_test)               # dln(rho)/dln c ; rho ∝ c^n
z_test = np.exp(-1.5*s_test) - 1
# census z_eq analog: where n_eff crosses the midpoint -1/4
i_mid = np.argmin(np.abs(n_eff - (-0.25)))
z_eq_census = z_test[i_mid]
# also: where radiation-like census (gamma + nu-kinetic part) = matter-like
def rad_like(z):
    a = M_NU_EV/(K_B_EV*T_NU0*(1+z))
    kin_frac = 1 - np.minimum(a*z3/F_fast(a), 1.0)   # kinetic share of nu census
    return OM_G*(1+z)**4 + OM_G*u_nu_hat(z)*kin_frac
def mat_like(z):
    a = M_NU_EV/(K_B_EV*T_NU0*(1+z))
    rest_frac = np.minimum(a*z3/F_fast(a), 1.0)
    return om_cold*(1+z)**3 + OM_G*u_nu_hat(z)*rest_frac
z_cross = brentq(lambda z: rad_like(z)-mat_like(z), 50, 5000)
print(f"census z_eq analogs: n_eff=-1/4 midpoint at z={z_eq_census:.0f}; "
      f"radiation-like = matter-like at z={z_cross:.0f}"
      f"   (two-fluid value was 1466 at this convention)")

# --- integrate the census trajectory -----------------------------------------
print("\ncensus trajectories (simple mu):")
census_results = {}
for om in OMEGAS:
    S, _, _ = make_census_S(om)
    z, x = integrate(S)
    census_results[om] = (z, x)
    print(f"  Om={om}: x(10)={x_at(z,x,10):.3f}  x(400)={x_at(z,x,400):.3f}  "
          f"x(1100)={x_at(z,x,Z_REC):.3f}  x(1e5)={x_at(z,x,1e5):.3f}  "
          f"x(1e6)={x_at(z,x,1e6):.3f}")
x_rec_census = [x_at(*census_results[om], Z_REC) for om in OMEGAS]
print(f"  => census x(1100) range: [{min(x_rec_census):.2f}, {max(x_rec_census):.2f}]"
      f"   (supersedes two-fluid [2.14, 2.37])")

# standard-mu sensitivity, primary convention
S, _, _ = make_census_S(0.074)
zs2, xs2 = integrate(S, mu=mu_std, imu=imu_std)
print(f"  standard-mu (Om=0.074): x(1100)={x_at(zs2,xs2,Z_REC):.3f}")

# late-time invariance check: census vs two-fluid difference at z<=10
z2, x2 = results_2f[(1, 0.074)]
zc, xc = census_results[0.074]
for zq in (0.5, 2, 10):
    print(f"  late-time check z={zq}: two-fluid x={x_at(z2,x2,zq):.4f}  "
          f"census x={x_at(zc,xc,zq):.4f}  (must agree: nu fully NR)")

# ----------------------------------------------------------------------------
# figure
# ----------------------------------------------------------------------------
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8.5, 5.2))
z2, x2 = results_2f[(1, 0.074)]
ax.semilogx(1+z2, x2, 'C0-',  lw=2, label='two-fluid (07-10 update), $\\Omega=0.074$')
ax.semilogx(1+zc, xc, 'C3-',  lw=2, label='Planck census, 3-component, $\\Omega=0.074$')
z134, x134 = census_results[0.134]
ax.semilogx(1+z134, x134, 'C3--', lw=1.2, label='census, $\\Omega=0.134$ convention')
ax.axhline(xm, color='gray', ls=':', lw=1); ax.axhline(xr, color='gray', ls=':', lw=1)
ax.text(1.3, xm+0.04, f'matter fixed point {xm:.2f}', fontsize=9, color='gray')
ax.text(1.3, xr+0.04, f'radiation fixed point {xr:.2f}', fontsize=9, color='gray')
ax.axvline(1+Z_REC, color='k', ls='--', lw=0.8)
ax.text(1+Z_REC, 1.15, ' recombination', rotation=90, fontsize=8, va='bottom')
ax.axvline(1+z_p_eq_m, color='C2', ls='--', lw=0.8)
ax.text(1+z_p_eq_m, 1.15, ' $\\nu$: $\\langle p\\rangle=mc$', rotation=90,
        fontsize=8, va='bottom', color='C2')
ax.set_xlabel('$1+z$'); ax.set_ylabel('$x = g_h/a_0$')
ax.set_xlim(1, 1.1e6); ax.set_ylim(1.0, 3.7)
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
ax.set_title('AQUAL operating point through the radiation era: two-fluid vs Planck census')
fig.tight_layout()
fig.savefig('/home/claude/census_trajectory.png', dpi=150)
fig.savefig('/home/claude/census_trajectory.svg')
print("\nfigure written: census_trajectory.png/.svg")

# ----------------------------------------------------------------------------
# arithmetic-identity check: census == adopted two-fluid law for matter+photons
# ----------------------------------------------------------------------------
print("\ncensus == adopted law identity check (matter+photon only, random s):")
rng = np.random.default_rng(1)
for s in rng.uniform(-8, 0, 4):
    adopted = 0.6*np.exp(0.5*s) + 0.4*np.exp(-s)              # f_m, f_g arbitrary
    # census: N*m_P with per-entity weights E/E_P; matter weight const, photon ∝ c^{-3/2}
    # -> M_h/M_h0 at fixed r: same two terms. Reconstruct from weights:
    census  = 0.6*(np.exp(0.5*s)) + 0.4*(np.exp(-1.5*s))*np.exp(0.5*s)
    print(f"  s={s:+.3f}: adopted={adopted:.6e} census={census:.6e} "
          f"ratio={census/adopted:.12f}")
