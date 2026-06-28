#!/usr/bin/env python3
"""
fit_pantheon.py — Pantheon+ Hubble diagram fit
Compares the VSL static cosmology (q₀ = +1/6) against flat ΛCDM (q₀ ≈ −0.55)
and matter-only EdS (q₀ = +0.5) using the Brout et al. 2022 distance-modulus data.

VSL model (Core Principles §4a, P=2, n=3 volume law):
    D_p(z) = R₀ [1 − (1+z)^{−1/6}],   R₀ = 6c/H₀ [Mpc]
    D_L(z) = (1+z) D_p(z)
    q₀     = 1/(nP) = +1/6

Fit strategy: for each model, the combination (M_B + 5 log₁₀ H₀) is a free
nuisance parameter fitted analytically (weighted mean offset). This leaves
the shape of D_L(z) as the discriminant between models.

Errors: diagonal only (MU_SH0ES_ERR_DIAG). The full stat+sys covariance matrix
is saved at data/Pantheon+SH0ES_STAT+SYS.cov for future use.

Usage: python3 cdot-3/fit_pantheon.py   (run from project root)
"""

import pathlib
import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIGS = ROOT / 'figures'
FIGS.mkdir(exist_ok=True)

plt.rcParams.update({
    'text.usetex':          False,
    'mathtext.fontset':     'cm',
    'font.family':          'serif',
    'font.size':            12,
    'axes.labelsize':       14,
    'axes.titlesize':       12,
    'legend.fontsize':      10.5,
    'xtick.labelsize':      11,
    'ytick.labelsize':      11,
    'axes.linewidth':       1.0,
    'xtick.direction':      'in',
    'ytick.direction':      'in',
    'xtick.top':            True,
    'ytick.right':          True,
    'xtick.minor.visible':  True,
    'ytick.minor.visible':  True,
    'lines.linewidth':      1.8,
})

C_KMS = 299792.458  # speed of light, km/s

# ── Load data ──────────────────────────────────────────────────────────────────
raw = np.genfromtxt(ROOT / 'data' / 'Pantheon+SH0ES.dat', names=True)

# Hubble-flow cut: exclude Cepheid calibrators, exclude z < 0.023
# (below 0.023 peculiar velocities ≳ cosmological signal)
mask = (raw['IS_CALIBRATOR'] == 0) & (raw['zHD'] > 0.023)
z_obs  = raw['zHD'][mask]
mu_obs = raw['MU_SH0ES'][mask]
sig    = raw['MU_SH0ES_ERR_DIAG'][mask]
w      = 1.0 / sig**2

print(f"Pantheon+ Hubble-flow SNe: {mask.sum()} of {len(raw)}")
print(f"  z range: {z_obs.min():.4f} – {z_obs.max():.3f}")
print(f"  μ range: {mu_obs.min():.2f} – {mu_obs.max():.2f}")

# ── Model luminosity distances ─────────────────────────────────────────────────

# Pre-compute comoving distance tables on a fine grid for speed
_z_tab = np.linspace(0, 2.5, 50_000)

_Om, _OL = 0.30, 0.70
_integrand = 1.0 / np.sqrt(_Om * (1 + _z_tab)**3 + _OL)
_dc_tab = cumulative_trapezoid(_integrand, _z_tab, initial=0.0)

# q₀ = 0 reference: flat coasting universe (Ω_m=2/3, Ω_Λ=1/3)
# q₀ = Ω_m/2 − Ω_Λ = 1/3 − 1/3 = 0  ✓
_Om0, _OL0 = 2/3, 1/3
_integrand0 = 1.0 / np.sqrt(_Om0 * (1 + _z_tab)**3 + _OL0)
_dc0_tab = cumulative_trapezoid(_integrand0, _z_tab, initial=0.0)

def dl_lcdm(z_arr, H0, Om=0.30, OL=0.70):
    """Flat ΛCDM D_L [Mpc]."""
    if Om == _Om and OL == _OL:
        dc = np.interp(z_arr, _z_tab, _dc_tab)
    else:
        from scipy.integrate import quad
        dc = np.array([quad(lambda zp: 1/np.sqrt(Om*(1+zp)**3 + OL),
                            0, zi)[0] for zi in np.atleast_1d(z_arr)])
    return C_KMS / H0 * (1 + np.atleast_1d(z_arr)) * dc

def dl_q0(z_arr, H0):
    """Flat coasting D_L [Mpc], q₀=0 (Ω_m=2/3, Ω_Λ=1/3)."""
    dc = np.interp(np.atleast_1d(z_arr), _z_tab, _dc0_tab)
    return C_KMS / H0 * (1 + np.atleast_1d(z_arr)) * dc

def dl_vsl(z_arr, H0, P=2, n=3):
    """VSL static cosmology D_L [Mpc]."""
    R0 = n * P * C_KMS / H0                          # Mpc
    Dp = R0 * (1.0 - (1.0 + z_arr)**(-1.0 / (n*P)))  # proper distance
    return (1.0 + z_arr) * Dp

def mu_model(dl_Mpc):
    """Distance modulus from D_L in Mpc."""
    return 5.0 * np.log10(dl_Mpc * 1e6 / 10.0)

# ── Best-fit offset (marginalise over M_B + 5 log₁₀ H₀) ──────────────────────
H0_REF = 70.0  # km/s/Mpc

mu_lcdm_obs = mu_model(dl_lcdm(z_obs, H0_REF))
mu_vsl_obs  = mu_model(dl_vsl(z_obs, H0_REF))
mu_eds_obs  = mu_model(dl_lcdm(z_obs, H0_REF, Om=1.0, OL=0.0))

def fit_offset(mu_th):
    """Weighted-mean offset d = <μ_obs − μ_th>_w; returns (d, χ², χ²/dof)."""
    d    = np.sum(w * (mu_obs - mu_th)) / w.sum()
    res  = mu_obs - mu_th - d
    chi2 = float((w * res**2).sum())
    return d, chi2

d_lcdm, chi2_lcdm = fit_offset(mu_lcdm_obs)
d_vsl,  chi2_vsl  = fit_offset(mu_vsl_obs)
d_eds,  chi2_eds  = fit_offset(mu_eds_obs)

# q₀=0 offset: the single free parameter for the residual panel
d_q0,   chi2_q0   = fit_offset(mu_model(dl_q0(z_obs, H0_REF)))

dof = len(z_obs) - 1          # 1 fitted parameter (the offset)

print(f"\n  χ²/dof  (diagonal errors, z > 0.023, dof={dof}):")
print(f"  ΛCDM (q₀≈−0.55)  χ²/dof = {chi2_lcdm/dof:.4f}   (χ²={chi2_lcdm:.1f})")
print(f"  VSL  (q₀=+1/6)   χ²/dof = {chi2_vsl /dof:.4f}   (χ²={chi2_vsl:.1f})")
print(f"  EdS  (q₀=+1/2)   χ²/dof = {chi2_eds /dof:.4f}   (χ²={chi2_eds:.1f})")
print(f"  q₀=0 (coasting)  χ²/dof = {chi2_q0  /dof:.4f}   (χ²={chi2_q0:.1f})")
print(f"\n  Δχ² (VSL − ΛCDM) = {chi2_vsl - chi2_lcdm:+.1f}")
print(f"  Δχ² (EdS − ΛCDM) = {chi2_eds - chi2_lcdm:+.1f}")

# Effective fitted H₀: offset ≡ −5 log₁₀(H₀/H0_REF), so H₀_fit = H0_REF·10^(−d/5)
for name, d in [('ΛCDM', d_lcdm), ('VSL', d_vsl), ('EdS', d_eds)]:
    H0_fit = H0_REF * 10**(-d / 5.0)
    print(f"  Effective H₀ ({name}): {H0_fit:.2f} km/s/Mpc")

# ── Predicted Δμ table at key redshifts ──────────────────────────────────────
z_key = np.array([0.1, 0.2, 0.5, 1.0, 1.5, 2.0, 2.3])
mu_lcdm_key = mu_model(dl_lcdm(z_key, H0_REF)) + d_lcdm
mu_vsl_key  = mu_model(dl_vsl(z_key, H0_REF))  + d_vsl
print(f"\n  Δμ (VSL − ΛCDM) after best-fit offset:")
print(f"  {'z':>5}  {'Δμ [mag]':>10}")
for zi, dmu in zip(z_key, mu_vsl_key - mu_lcdm_key):
    print(f"  {zi:5.2f}  {dmu:+10.3f}")

# ── Smooth curves for plotting ────────────────────────────────────────────────
z_g = np.geomspace(0.022, 2.4, 600)
mu_lcdm_g = mu_model(dl_lcdm(z_g, H0_REF)) + d_lcdm
mu_vsl_g  = mu_model(dl_vsl(z_g, H0_REF))  + d_vsl
mu_eds_g  = mu_model(dl_lcdm(z_g, H0_REF, Om=1.0, OL=0.0)) + d_eds

# Shape differences relative to q₀=0: H₀ cancels in the ratio, no free parameters
mu_q0_g      = mu_model(dl_q0(z_g, H0_REF))   # same H₀, cancels below
dmu_lcdm_q0  = mu_model(dl_lcdm(z_g, H0_REF)) - mu_q0_g
dmu_vsl_q0   = mu_model(dl_vsl(z_g, H0_REF))  - mu_q0_g
dmu_eds_q0   = mu_model(dl_lcdm(z_g, H0_REF, Om=1.0, OL=0.0)) - mu_q0_g

# ── Bin data by redshift for readability ──────────────────────────────────────
edges = np.geomspace(z_obs.min(), z_obs.max(), 28)
z_b, mu_b, sig_b, n_b = [], [], [], []
for lo, hi in zip(edges[:-1], edges[1:]):
    sel = (z_obs >= lo) & (z_obs < hi)
    if sel.sum() < 2:
        continue
    wb = w[sel]
    z_b.append(np.average(z_obs[sel], weights=wb))
    mu_b.append(np.average(mu_obs[sel], weights=wb))
    sig_b.append(1.0 / np.sqrt(wb.sum()))
    n_b.append(sel.sum())
z_b, mu_b, sig_b = map(np.array, [z_b, mu_b, sig_b])
mu_lcdm_b = mu_model(dl_lcdm(z_b, H0_REF)) + d_lcdm
# Data residuals relative to q₀=0, using the ΛCDM-calibrated H₀.
# d_lcdm absorbs M_B + 5log H₀ from the best-fitting model; this keeps data
# near the ΛCDM curve and lets q₀=0 serve as a neutral zero reference.
dmu_data_q0_b = mu_b - mu_model(dl_q0(z_b, H0_REF)) - d_lcdm

# ── Figure ────────────────────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(6.5, 7.8), sharex=True,
    gridspec_kw={'height_ratios': [2.5, 1.0], 'hspace': 0.06},
    constrained_layout=False,
)

# ── Upper panel: Hubble diagram ───────────────────────────────────────────────
ax1.errorbar(z_b, mu_b, yerr=sig_b,
             fmt='o', color='0.30', markersize=4.5,
             capsize=2.5, elinewidth=0.8, linewidth=0.8,
             label='Pantheon+ binned', zorder=4)
ax1.plot(z_g, mu_lcdm_g, color='steelblue', lw=2.0,
         label=r'$\Lambda$CDM  $(q_0 \approx -0.55)$')
ax1.plot(z_g, mu_vsl_g,  color='firebrick',  lw=2.0, ls='--',
         label=r'VSL static  $(q_0 = +1/6)$')
ax1.plot(z_g, mu_eds_g,  color='forestgreen', lw=1.4, ls=':',
         label=r'Matter-only  $(q_0 = +1/2)$')

ax1.set_ylabel(r'Distance modulus $\mu$  [mag]')
ax1.legend(frameon=False, loc='upper left')

stat_text = (
    rf"$\chi^2/\mathrm{{dof}}$:  "
    rf"$\Lambda$CDM $= {chi2_lcdm/dof:.3f}$,  "
    rf"VSL $= {chi2_vsl/dof:.3f}$" + "\n"
    rf"$\Delta\chi^2$ (VSL $-$ $\Lambda$CDM) $= {chi2_vsl - chi2_lcdm:+.0f}$"
)
ax1.text(0.97, 0.04, stat_text, transform=ax1.transAxes,
         ha='right', va='bottom', fontsize=9.5,
         bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='0.75', lw=0.7))

# ── Lower panel: residuals relative to q₀=0 (coasting universe) ──────────────
# Model curves have no free parameters — H₀ cancels in the ratio.
# Data has one offset (H₀ / M_B) fitted to q₀=0.
ax2.axhline(0, color='0.40', lw=1.2, ls='-', zorder=1)
ax2.plot(z_g, dmu_lcdm_q0, color='steelblue', lw=2.0,
         label=r'$\Lambda$CDM  $(q_0 \approx -0.55)$')
ax2.plot(z_g, dmu_vsl_q0,  color='firebrick',  lw=2.0, ls='--',
         label=r'VSL  $(q_0 = +1/6)$')
ax2.plot(z_g, dmu_eds_q0,  color='forestgreen', lw=1.4, ls=':',
         label=r'EdS  $(q_0 = +1/2)$')
ax2.errorbar(z_b, dmu_data_q0_b, yerr=sig_b,
             fmt='o', color='0.30', markersize=4.5,
             capsize=2.5, elinewidth=0.8, linewidth=0.8, zorder=4)

ax2.text(0.97, 0.88, 'acceleration', color='steelblue', fontsize=9.5,
         ha='right', va='top', transform=ax2.transAxes)
ax2.text(0.97, 0.12, 'deceleration', color='firebrick', fontsize=9.5,
         ha='right', va='bottom', transform=ax2.transAxes)

ax2.set_xlabel(r'Redshift $z$')
ax2.set_ylabel(r'$\Delta\mu$ rel. to $q_0\!=\!0$  [mag]')
ax2.set_xscale('log')
ax2.set_xlim(0.022, 2.6)
ax2.set_ylim(-0.42, 0.62)
ax2.legend(frameon=False, loc='upper left', fontsize=9.5)

import matplotlib.ticker as mticker
ax2.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:g}'))
ax2.xaxis.set_minor_formatter(mticker.NullFormatter())

fig.subplots_adjust(left=0.13, right=0.97, top=0.97, bottom=0.09, hspace=0.06)
out = FIGS / 'pantheon_hubble_diagram.svg'
fig.savefig(out, format='svg', bbox_inches='tight')
print(f'\nSaved {out.relative_to(ROOT)}')
