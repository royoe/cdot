#!/usr/bin/env python3
"""
fit_pantheon.py — Pantheon+ Hubble diagram fit, cdot-5 (connectivity counting)

Compares the cdot-5 connectivity-counting cosmology (D_p = (c/H0) ln(1+z), q0 = 0
at leading order) against flat LambdaCDM (q0 ~ -0.55), the q0=0 coasting reference,
and cdot-4's old volume-law VSL model (q0 = +1/6), using the Brout et al. 2022
distance-modulus data. Same methodology as cdot-3/cdot-4's fit_pantheon.py: single
nuisance parameter (M_B + 5log10 H0) fitted analytically per model; diagonal errors
only (full stat+sys covariance is on disk for future use, not applied here).

Usage: python3 cdot-5/fit_pantheon.py   (run from project root)
"""

import pathlib
import numpy as np
from scipy.integrate import cumulative_trapezoid

ROOT = pathlib.Path(__file__).resolve().parent.parent
C_KMS = 299792.458  # speed of light, km/s
H0_REF = 70.0       # km/s/Mpc

raw = np.genfromtxt(ROOT / 'data' / 'Pantheon+SH0ES.dat', names=True)
mask = (raw['IS_CALIBRATOR'] == 0) & (raw['zHD'] > 0.023)
z_obs = raw['zHD'][mask]
mu_obs = raw['MU_SH0ES'][mask]
sig = raw['MU_SH0ES_ERR_DIAG'][mask]
w = 1.0 / sig**2

print(f"Pantheon+ Hubble-flow SNe: {mask.sum()} of {len(raw)}")
print(f"  z range: {z_obs.min():.4f} - {z_obs.max():.3f}")

_z_tab = np.linspace(0, 2.5, 50_000)


def _dc_table(Om, OL):
    integrand = 1.0 / np.sqrt(Om * (1 + _z_tab)**3 + OL)
    return cumulative_trapezoid(integrand, _z_tab, initial=0.0)


_dc_lcdm = _dc_table(0.30, 0.70)
_dc_q0 = _dc_table(2/3, 1/3)


def dl_lcdm(z, H0=H0_REF):
    dc = np.interp(z, _z_tab, _dc_lcdm)
    return C_KMS / H0 * (1 + np.atleast_1d(z)) * dc


def dl_q0(z, H0=H0_REF):
    dc = np.interp(z, _z_tab, _dc_q0)
    return C_KMS / H0 * (1 + np.atleast_1d(z)) * dc


def dl_vsl_old(z, H0=H0_REF):
    """cdot-4 volume-law counting: D_p = R0[1-(1+z)^-1/6], R0 = 6c/H0."""
    R0 = 6 * C_KMS / H0
    Dp = R0 * (1.0 - (1.0 + z)**(-1.0/6))
    return (1.0 + z) * Dp


def dl_exp(z, H0=H0_REF):
    """cdot-5 connectivity counting: D_p = (c/H0) ln(1+z) (P-independent)."""
    Dp = (C_KMS / H0) * np.log(1.0 + z)
    return (1.0 + z) * Dp


def mu_model(dl_Mpc):
    return 5.0 * np.log10(dl_Mpc * 1e6 / 10.0)


def fit_offset(mu_th):
    d = np.sum(w * (mu_obs - mu_th)) / w.sum()
    res = mu_obs - mu_th - d
    chi2 = float((w * res**2).sum())
    return d, chi2


dof = len(z_obs) - 1
print(f"\n  chi2/dof (diagonal errors, z>0.023, dof={dof}):")
results = {}
for name, fn in [('LambdaCDM (q0~-0.55)', dl_lcdm),
                  ('q0=0 coasting', dl_q0),
                  ('cdot-4 volume law (q0=+1/6)', dl_vsl_old),
                  ('cdot-5 connectivity law (q0=0)', dl_exp)]:
    mu_th = mu_model(fn(z_obs))
    d, chi2 = fit_offset(mu_th)
    H0_fit = H0_REF * 10**(-d / 5.0)
    results[name] = (d, chi2)
    print(f"  {name:32s} chi2/dof={chi2/dof:.4f}  chi2={chi2:8.2f}  H0_fit={H0_fit:.2f}")

chi2_lcdm = results['LambdaCDM (q0~-0.55)'][1]
chi2_exp = results['cdot-5 connectivity law (q0=0)'][1]
chi2_old = results['cdot-4 volume law (q0=+1/6)'][1]
print(f"\n  Delta chi2 (cdot-5 - LambdaCDM) = {chi2_exp - chi2_lcdm:+.1f}")
print(f"  Delta chi2 (cdot-4 - LambdaCDM) = {chi2_old - chi2_lcdm:+.1f}")
print(f"  Delta chi2 (cdot-5 - cdot-4)    = {chi2_exp - chi2_old:+.1f}")

z_key = np.array([0.1, 0.2, 0.5, 1.0, 1.5, 2.0, 2.3])
d_lcdm = results['LambdaCDM (q0~-0.55)'][0]
d_exp = results['cdot-5 connectivity law (q0=0)'][0]
mu_lcdm_key = mu_model(dl_lcdm(z_key)) + d_lcdm
mu_exp_key = mu_model(dl_exp(z_key)) + d_exp
print("\n  Delta mu (cdot-5 - LambdaCDM) after best-fit offsets:")
for zi, dm in zip(z_key, mu_exp_key - mu_lcdm_key):
    print(f"  z={zi:4.2f}  {dm:+.3f} mag")
