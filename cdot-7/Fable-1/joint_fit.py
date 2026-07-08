#!/usr/bin/env python3
"""
joint_fit.py — cdot-7, Fable-2 session 2026-07-07
First-pass execution of Foundation §6 item 1: joint fit of the framework to the real
Pantheon+ SN compilation (full STAT+SYS covariance) and published a0(z) constraints.
Companion to Update-JointFit-2026-07-07.md; reproduces every number quoted there.

Data (place in ./data/):
  curl -sL -o data/pantheon.dat "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat"
  curl -sL -o data/pantheon.cov "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STAT%2BSYS.cov"

Likelihoods:
  SN: m_b_corr vs 5log10(D_L shape), absolute-mag/H0 offset analytically marginalized,
      full covariance, zHD > 0.01 (1590 SNe). Validation: flat LCDM must return
      Om = 0.331 +/- 0.018, chi2 = 1403.7 (published: 0.334 +/- 0.018).
  a0: SPARC 1.20+/-0.26 (z=0); MIGHTEE-HI 1.69+/-0.13 (z=0.05); MUSE-DARK III
      full-sample 2.38+/-0.055 (z_eff=0.90) and slope a1 = 1.59+/-0.054 over
      0.33<z<1.44 (both 1-sigma from 95% CIs). CAVEAT: MUSE point and slope are
      correlated (same sample) — first-pass indicative only; definitive version
      needs per-bin data. Model: a0(z) = A * a0hat(z)/a0hat(0) from the trajectory;
      rigid case A = (kappa*lambda) * c0*H0hor(lam=1) with kappa=1, H0=70
      (CH0 = 4.53e-10 m/s^2; A scales as H0).
"""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.optimize import minimize, minimize_scalar
import pandas as pd

CH0 = 4.53  # (2/3) c0 H0_obs in 1e-10 m/s^2 at H0=70


def load_pantheon(path_dat='data/pantheon.dat', path_cov='data/pantheon.cov', zcut=0.01):
    df = pd.read_csv(path_dat, sep=r'\s+')
    cov = np.loadtxt(path_cov, skiprows=1).reshape(len(df), len(df))
    sel = df['zHD'].values > zcut
    z, mb = df['zHD'].values[sel], df['m_b_corr'].values[sel]
    Cinv = np.linalg.inv(cov[np.ix_(sel, sel)])
    return z, mb, Cinv


class SNLike:
    def __init__(self, z, mb, Cinv):
        self.z, self.mb, self.Cinv = z, mb, Cinv
        self.one = np.ones(len(z)); self.A11 = self.one @ Cinv @ self.one
        self.a_ev = (1 + z) ** (-2 / 3.); self.a_min = 0.98 * self.a_ev.min()
    def chi2(self, model_shape):
        d = self.mb - model_shape; Cd = self.Cinv @ d
        return d @ Cd - (self.one @ Cd) ** 2 / self.A11


def setup(lamt, muform='simple'):
    xs = 3.0 / (4 * lamt)
    if muform == 'simple':
        return xs, xs / (1 + xs), (lambda m: m / (1 - m))
    return xs, xs / np.sqrt(1 + xs * xs), (lambda m: m / np.sqrt(1 - m * m))


def trajectory(eps0, lamt, sn, muform='simple'):
    """Returns (mu_shape at SN redshifts, a0hat-ratio function)."""
    xs, mus, xinv = setup(lamt, muform); r0 = 1.0 + eps0
    rhs = lambda a, Y: [lamt * xinv(min(mus * Y[0]**2 / a**1.5, 1 - 1e-13)) * Y[0] / a]
    sol = solve_ivp(rhs, [1.0, sn.a_min], [r0], dense_output=True, rtol=1e-10, atol=1e-12)
    x0 = xinv(min(mus * r0 * r0, 1 - 1e-13))
    def ratio(zz):
        a = (1 + zz) ** (-2 / 3.); r = sol.sol(a)[0]
        x = xinv(min(mus * r * r / a**1.5, 1 - 1e-13))
        return (x0 * r0) / (x * r) * a ** (-1.5)
    return 5 * np.log10((r0 - sol.sol(sn.a_ev)[0]) * (1 + sn.z)), ratio


A0_DATA = [(0.00, 1.20, 0.26), (0.05, 1.69, 0.13), (0.90, 2.38, 0.055)]
A0_SLOPE = (1.59, 0.054)


def chi2_a0(ratio, A, data=A0_DATA):
    c2 = sum(((A * ratio(zz) - v) / s) ** 2 for zz, v, s in data)
    return c2 + ((A * (ratio(1.44) - ratio(0.33)) / 1.11 - A0_SLOPE[0]) / A0_SLOPE[1]) ** 2


if __name__ == '__main__':
    sn = SNLike(*load_pantheon())
    print(f'SNe: {len(sn.z)}  zmax={sn.z.max():.2f}')

    # LCDM validation
    zg = np.linspace(0, 2.4, 3000)
    def mu_lcdm(Om):
        I = cumulative_trapezoid(1 / np.sqrt(Om * (1 + zg)**3 + 1 - Om), zg, initial=0)
        return 5 * np.log10(np.interp(sn.z, zg, (1 + zg) * I))
    r = minimize_scalar(lambda Om: sn.chi2(mu_lcdm(Om)), bounds=(0.1, 0.6), method='bounded')
    print(f'LCDM: Om={r.x:.3f} chi2={r.fun:.1f}   [published: 0.334 +/- 0.018]')
    chi2_ref = r.fun

    # joint fits
    def joint(p, muform='simple', rigid=True):
        m, ratio = trajectory(p[0], p[1], sn, muform)
        A = p[1] * CH0 if rigid else p[2]
        return sn.chi2(m) + chi2_a0(ratio, A)

    for label, muform in [('simple', 'simple'), ('standard', 'standard')]:
        r = minimize(lambda p: joint(p, muform), x0=[-0.06, 0.30],
                     method='Nelder-Mead', options={'xatol': 1e-5, 'fatol': 1e-3})
        m, ratio = trajectory(r.x[0], r.x[1], sn, muform)
        print(f'JOINT rigid ({label}): eps0={r.x[0]:.4f} kl={r.x[1]:.3f} '
              f'chi2={r.fun:.1f} [SN {sn.chi2(m):.1f} | a0 {r.fun - sn.chi2(m):.1f}] '
              f'dchi2_SN={sn.chi2(m) - chi2_ref:+.1f}')
    rA = minimize(lambda p: joint(p, rigid=False), x0=[-0.06, 0.30, 1.4],
                  method='Nelder-Mead', options={'xatol': 1e-5, 'fatol': 1e-3})
    print(f'JOINT free-A: kl={rA.x[1]:.3f} A={rA.x[2]:.2f} '
          f'=> kappa = {rA.x[1] * CH0 / rA.x[2]:.2f}')
