#!/usr/bin/env python3
"""
four_term_fit.py — cdot-7, 2026-07-08
First attempt at Foundation.md Sec6 item 1: the decisive four-term joint fit
(SN + a0(z) + local RAR shape + mass census with Sum(m_nu) as a bounded nuisance).
Builds directly on joint_fit.py (SN likelihood, trajectory/closure machinery) plus
two new terms: the real SPARC RAR likelihood and the closure density mass-census term.

Data required (see data/ directory, already present for this run):
  data/pantheon.dat, data/pantheon.cov  — Pantheon+ SH0ES release (as in joint_fit.py)
  data/RAR.mrt                          — SPARC RAR master table, "Data Behind Figure 2"
                                           of McGaugh, Lelli & Schombert 2016, PRL 117,
                                           201101. Downloaded from
                                           https://astroweb.case.edu/SPARC/RAR.mrt
                                           (2693 points, 153 galaxies; log10 g_bar,
                                           e_gbar, log10 g_obs, e_gobs, in m/s^2).

Caveats carried forward honestly, not hidden:
  - RAR points are treated as statistically independent. They are not: multiple radii
    per galaxy share a common distance/inclination/M-L systematic. The true number of
    independent constraints on a0's *value* is closer to the galaxy count (153) than
    the point count (2693). Downweighted by N_points/N_galaxies in the joint chi2
    (a standard, approximate correction for clustered data) rather than left
    artificially, unrealistically tight.
  - Omega_b from BBN (Cooke, Pettini & Steidel 2018): Omega_b*h^2 = 0.02166 +/- 0.00019
    (combining their stat+sys in quadrature), deliberately not the Planck/LCDM value.
  - Sum(m_nu) prior: half-normal edge at the KATRIN 90%-CL bound (m_beta < 0.45 eV,
    2025), converted via the standard degenerate-hierarchy Sum(m_nu) ~= 3*m_beta.
  - H0 fixed at 70 km/s/Mpc throughout (not fit) — the SN likelihood alone cannot pin
    it once the absolute-magnitude offset is marginalized.
"""
import sys, os
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize, minimize_scalar

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from joint_fit import load_pantheon, SNLike, setup

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# ---------------------------------------------------------------------------
# Physical constants and external inputs (all stated, all verified before use)
# ---------------------------------------------------------------------------
G, C0 = 6.674e-11, 2.9979e8
H0 = 70 * 1000 / 3.0857e22          # s^-1, fixed throughout (not fit)
CH0 = (2. / 3.) * C0 * H0             # = a0 at lambda=1, today (a0 = lambda*(2/3)*c0*H0)
RHO_CRIT = 3 * H0**2 / (8 * np.pi * G)
OBH2, OBH2_ERR = 0.02166, 0.00019    # Cooke, Pettini & Steidel 2018 (BBN, not CMB)
H70 = 0.7
OMEGA_B = OBH2 / H70**2               # h=0.7 throughout, matching H0 above
SIGMA_MBETA_KATRIN = 0.45              # eV, 90% CL, KATRIN 2025
SUM_MNU_MAX = 3 * SIGMA_MBETA_KATRIN   # eV, degenerate-hierarchy conversion

N_RAR_POINTS, N_RAR_GALAXIES = 2693, 153
RAR_DOWNWEIGHT = N_RAR_POINTS / N_RAR_GALAXIES

A0_SPARC_SUMMARY = (1.20, 0.26)   # NOT used once RAR is included directly -- see note
MIGHTEE = (0.05, 1.69, 0.13)
MUSE_PT = (0.90, 2.38, 0.055)
MUSE_SLOPE = (1.59, 0.054)        # over 0.33 < z < 1.44


def mu_of_x(x, muform):
    return x / (1 + x) if muform == 'simple' else x / np.sqrt(1 + x * x)


def mu_force_inv(y, muform):
    """Solve mu(x)*x = y for x > 0 (the AQUAL force law, g_bar = mu(g_obs/a0)*g_obs)."""
    if muform == 'simple':
        return (y + np.sqrt(y * y + 4 * y)) / 2
    u = (y * y + np.sqrt(y**4 + 4 * y * y)) / 2
    return np.sqrt(u)


def setup_closure(lamt, muform):
    xs = 3.0 / (4 * lamt)
    if muform == 'simple':
        return xs, xs / (1 + xs), (lambda m: m / (1 - m))
    return xs, xs / np.sqrt(1 + xs * xs), (lambda m: m / np.sqrt(1 - m * m))


def trajectory(eps0, lamt, sn, muform):
    xs, mus, xinv = setup_closure(lamt, muform)
    r0 = 1.0 + eps0
    rhs = lambda a, Y: [lamt * xinv(min(mus * Y[0] ** 2 / a ** 1.5, 1 - 1e-13)) * Y[0] / a]
    sol = solve_ivp(rhs, [1.0, sn.a_min], [r0], dense_output=True, rtol=1e-10, atol=1e-12)
    x0 = xinv(min(mus * r0 * r0, 1 - 1e-13))
    def ratio(zz):
        a = (1 + zz) ** (-2 / 3.)
        r = sol.sol(a)[0]
        x = xinv(min(mus * r * r / a ** 1.5, 1 - 1e-13))
        return (x0 * r0) / (x * r) * a ** (-1.5)
    return (5 * np.log10((r0 - sol.sol(sn.a_ev)[0]) * (1 + sn.z)), ratio, x0,
            min(mus * r0 * r0, 1 - 1e-13))


# ---------------------------------------------------------------------------
# Load real data
# ---------------------------------------------------------------------------
sn = SNLike(*load_pantheon(os.path.join(DATA, 'pantheon.dat'), os.path.join(DATA, 'pantheon.cov')))
_rar = np.loadtxt(os.path.join(DATA, 'RAR.mrt'), skiprows=13)
GBAR, E_GBAR, GOBS, E_GOBS = 10**_rar[:, 0], _rar[:, 1], 10**_rar[:, 2], _rar[:, 3]
RAR_EXTRA_SCATTER = 0.0887   # dex, calibrated so reduced chi2 = 1 at best-fit a0 alone


def chi2_rar(a0, muform):
    x = mu_force_inv(GBAR / a0, muform)
    resid = np.log10(a0 * x) - np.log10(GOBS)
    sigma = np.sqrt(E_GOBS**2 + RAR_EXTRA_SCATTER**2)
    return np.sum((resid / sigma) ** 2) / RAR_DOWNWEIGHT


def chi2_a0z(kl, lam, eps0, sn, muform):
    _, ratio, _, _ = trajectory(eps0, kl, sn, muform)
    a0_0 = lam * CH0
    pred = lambda z: a0_0 * ratio(z)
    c2 = ((pred(MIGHTEE[0]) * 1e10 - MIGHTEE[1]) / MIGHTEE[2]) ** 2
    c2 += ((pred(MUSE_PT[0]) * 1e10 - MUSE_PT[1]) / MUSE_PT[2]) ** 2
    slope = (pred(1.44) - pred(0.33)) * 1e10 / 1.11
    c2 += ((slope - MUSE_SLOPE[0]) / MUSE_SLOPE[1]) ** 2
    return c2


def chi2_mass(kl, lam, sum_mnu, x0, mu0):
    kappa = kl / lam
    a0_0 = lam * CH0
    rho0 = (3 / (4 * np.pi)) * kappa * mu0 * x0 * x0 * a0_0 * a0_0 / (G * C0 * C0)
    omega_nu = sum_mnu / 93.14 / H70**2
    omega_pred = rho0 / RHO_CRIT
    sigma_ob = (OBH2_ERR / H70**2)  # propagate Omega_b uncertainty only, for simplicity
    c2 = ((omega_pred - OMEGA_B - omega_nu) / sigma_ob) ** 2
    # half-normal soft penalty above the KATRIN edge (not a hard cutoff)
    if sum_mnu > SUM_MNU_MAX:
        c2 += ((sum_mnu - SUM_MNU_MAX) / 0.1) ** 2
    if sum_mnu < 0:
        c2 += (sum_mnu / 0.01) ** 2
    return c2, omega_pred


def full_chi2(p, muform='simple', use_rar=True, use_mass=True):
    eps0, kl, lam, sum_mnu = p
    m_fit, ratio, x0, mu0 = trajectory(eps0, kl, sn, muform)
    c2 = sn.chi2(m_fit)
    c2 += chi2_a0z(kl, lam, eps0, sn, muform)
    if use_rar:
        c2 += chi2_rar(lam * CH0, muform)
    if use_mass:
        c2_mass, _ = chi2_mass(kl, lam, sum_mnu, x0, mu0)
        c2 += c2_mass
    return c2


if __name__ == '__main__':
    print(f'SNe: {len(sn.z)}   RAR points: {len(GBAR)} (downweight factor {RAR_DOWNWEIGHT:.1f})')
    print(f'Omega_b (BBN, h=0.7) = {OMEGA_B:.4f}    Sum(m_nu) KATRIN edge = {SUM_MNU_MAX:.2f} eV')
    print(f'CH0 (a0 at lambda=1) = {CH0*1e10:.3f}e-10 m/s^2\n')

    # --- validation 1: RAR alone reproduces the standalone calibration ---
    r = minimize_scalar(lambda a0: chi2_rar(a0, 'simple'), bounds=(0.5e-10, 2.5e-10), method='bounded')
    print(f'[validate] RAR alone, simple mu: a0 = {r.x*1e10:.3f}e-10, '
          f'chi2/downweight = {r.fun:.2f} (N_eff={N_RAR_GALAXIES})')

    # --- validation 2: three-term result (SN + a0z, rigid kappa=1, no RAR/mass) must
    #     match the previously-verified joint_fit.py numbers exactly (same convention:
    #     lambda = kappa*lambda, i.e. kappa=1) ---
    r3 = minimize(lambda p: full_chi2([p[0], p[1], p[1], 0.0], 'simple', False, False),
                  x0=[-0.068, 0.307], method='Nelder-Mead', options={'xatol': 1e-6, 'fatol': 1e-4})
    print(f'[validate] SN+a0(z) only (rigid kappa=1, old 3-term shape): '
          f'eps0={r3.x[0]:.4f} kl={r3.x[1]:.4f} chi2={r3.fun:.2f}  '
          f'(expect eps0=-0.0678, kl=0.307, chi2=1411.8)')

    # --- the four-term fit ---
    for muform in ('simple', 'standard'):
        res = minimize(lambda p: full_chi2(p, muform), x0=[-0.068, 0.307, 0.264, 0.5],
                        method='Nelder-Mead',
                        options={'xatol': 1e-6, 'fatol': 1e-4, 'maxiter': 20000})
        eps0, kl, lam, mnu = res.x
        m_fit, ratio, x0, mu0 = trajectory(eps0, kl, sn, muform)
        c2_sn = sn.chi2(m_fit)
        c2_a0z = chi2_a0z(kl, lam, eps0, sn, muform)
        c2_rar_ = chi2_rar(lam * CH0, muform)
        c2_mass_, omega_pred = chi2_mass(kl, lam, mnu, x0, mu0)
        print(f'\n=== FOUR-TERM FIT ({muform} mu) ===')
        print(f'  eps0={eps0:.4f}  kappa*lambda={kl:.4f}  lambda={lam:.4f}  '
              f'kappa={kl/lam:.3f}  Sum(m_nu)={mnu:.3f} eV')
        print(f'  a0(0) = {lam*CH0*1e10:.3f}e-10 m/s^2')
        print(f'  chi2: SN={c2_sn:.1f}  a0(z)={c2_a0z:.2f}  RAR={c2_rar_:.2f}  '
              f'mass={c2_mass_:.2f}  TOTAL={res.fun:.2f}')
        print(f'  Omega_closure(predicted) = {omega_pred:.4f}  vs Omega_b={OMEGA_B:.4f}'
              f'  (+ Omega_nu = {mnu/93.14/H70**2:.4f})')
