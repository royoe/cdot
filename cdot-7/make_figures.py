#!/usr/bin/env python3
"""
make_figures.py — cdot-7, 2026-07-07 (v3: adds the raw, non-residual Hubble diagram)
Generates the illustrative figures for the AQUAL-consistent closure's fitting
results (Foundation.md S2.2, S5.5), built on the verified Fable-1 modules
(joint_fit.py for the real-data trajectory, a0_confrontation.py's a0hat machinery
reimplemented locally against the joint-fit trajectory). Saves to ../figures/.
"""
import sys, os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Fable-1'))
from joint_fit import load_pantheon, SNLike, trajectory, setup, CH0

FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
# Four-term joint fit (SN + a0(z) + local RAR + mass census), simple mu:
KL, EPS0, MUFORM = 0.4355, -0.0909, 'simple'
LAM = 0.3056                 # -> a0(0) = lambda*CH0
A0_LOC = LAM * CH0 * 1e10    # the fit's own predicted local a0, in 1e-10 m/s^2 units
A0_SPARC = 1.20              # SPARC's own canonical value, shown separately for comparison

plt.rcParams.update({'font.size': 10, 'axes.grid': True, 'grid.alpha': 0.3})

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Fable-1', 'data')
sn = SNLike(*load_pantheon(os.path.join(data_dir, 'pantheon.dat'),
                            os.path.join(data_dir, 'pantheon.cov')))

m_fit, ratio_fn = trajectory(EPS0, KL, sn, MUFORM)
# best-fit offset (analytic marginalization), applied so both figures use the same
# absolute-magnitude zero point as the fit itself
d = sn.mb - m_fit
offset = (sn.one @ (sn.Cinv @ d)) / sn.A11
resid = sn.mb - (m_fit + offset)

# EdS (fixed point, eps0=0) for comparison, same offset convention
m_eds, _ = trajectory(0.0, KL, sn, MUFORM)
offset_eds = (sn.one @ (sn.Cinv @ (sn.mb - m_eds))) / sn.A11
resid_eds = sn.mb - (m_eds + offset_eds)


def dl_shape_curve(eps0, lamt, muform, zgrid):
    """5*log10(d_L) on a smooth z grid, same convention as trajectory()'s SN-only output."""
    xs, mus, xinv = setup(lamt, muform)
    r0 = 1.0 + eps0
    rhs = lambda a, Y: [lamt * xinv(min(mus * Y[0] ** 2 / a ** 1.5, 1 - 1e-13)) * Y[0] / a]
    a_min = 0.98 * min((1 + zgrid) ** (-2 / 3.))
    sol = solve_ivp(rhs, [1.0, a_min], [r0], dense_output=True, rtol=1e-10, atol=1e-12)
    a = (1 + zgrid) ** (-2 / 3.)
    return 5 * np.log10((r0 - sol.sol(a)[0]) * (1 + zgrid))


# bin the real data in z for a readable plot (shared by both figures)
zbins = np.geomspace(sn.z.min(), sn.z.max(), 18)
zctr, mb_med, res_med, res_eds_med, res_err, mb_err = [], [], [], [], [], []
for lo, hi in zip(zbins[:-1], zbins[1:]):
    sel = (sn.z >= lo) & (sn.z < hi)
    if sel.sum() < 3:
        continue
    zctr.append(np.median(sn.z[sel]))
    mb_med.append(np.mean(sn.mb[sel] - offset))
    mb_err.append(np.std(sn.mb[sel]) / np.sqrt(sel.sum()))
    res_med.append(np.mean(resid[sel]))
    res_eds_med.append(np.mean(resid_eds[sel]))
    res_err.append(np.std(resid[sel]) / np.sqrt(sel.sum()))

# ---------------------------------------------------------------------------
# Figure 0: the raw Hubble diagram (not residuals) — data and model together
# ---------------------------------------------------------------------------
zg_smooth = np.geomspace(sn.z.min(), sn.z.max(), 300)
mu_fit_curve = dl_shape_curve(EPS0, KL, MUFORM, zg_smooth)
mu_eds_curve = dl_shape_curve(0.0, KL, MUFORM, zg_smooth)

fig, ax = plt.subplots(figsize=(6.8, 4.8))
ax.errorbar(zctr, mb_med, yerr=mb_err, fmt='o', color='#1f77b4', ms=5, capsize=3, zorder=3,
            label=f'Pantheon+ SNe, binned ({len(sn.z)} SNe, $z_\\mathrm{{HD}}>0.01$)')
ax.plot(zg_smooth, mu_fit_curve, color='#1f77b4', lw=2.2, zorder=4,
        label=f'joint-fit trajectory ($\\varepsilon_0={EPS0}$, $\\kappa\\lambda={KL}$)')
ax.plot(zg_smooth, mu_eds_curve, color='#d62728', lw=2, ls='--', zorder=2,
        label='exact EdS fixed point ($\\varepsilon_0=0$) — for comparison')
ax.set_xscale('log')
ax.set_xlabel('redshift $z$ (log scale)')
ax.set_ylabel(r'$m_b^\mathrm{corr}$ $-$ fitted offset  (mag)')
ax.set_title('cdot-7 Hubble diagram vs. real Pantheon+ (1701 SNe, full STAT+SYS covariance)\n'
             'raw magnitudes, not residuals — see the following figure for the fit quality')
ax.legend(loc='upper left', fontsize=8.5, framealpha=0.9)
fig.tight_layout()
fig.savefig(os.path.join(FIGDIR, 'cdot7_hubble_diagram_data.svg'))
plt.close(fig)
print('wrote cdot7_hubble_diagram_data.svg (raw magnitudes, real Pantheon+ data)')

# ---------------------------------------------------------------------------
# Figure 1: Hubble diagram residuals vs. real Pantheon+ SNe (binned), not a proxy
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.8, 4.6))
ax.axhline(0, color='0.4', lw=1.2, label='framework, joint Pantheon+ fit (zero by construction)')
ax.errorbar(zctr, res_med, yerr=res_err, fmt='o', color='#1f77b4', ms=5, capsize=3,
            label=f'Pantheon+ SNe, binned ({len(sn.z)} SNe, $z_\\mathrm{{HD}}>0.01$)')
ax.plot(zctr, res_eds_med, color='#d62728', lw=2, ls='--',
        label='exact EdS fixed point ($\\varepsilon_0=0$) — for comparison')
ax.set_xscale('log')
ax.set_xlabel('redshift $z$ (log scale)')
ax.set_ylabel(r'binned $m_b^\mathrm{corr}$ residual (mag)')
ax.set_title('cdot-7 vs. real Pantheon+ (1701 SNe, full STAT+SYS covariance)\n'
             f'four-term fit: $\\varepsilon_0={EPS0}$, $\\kappa\\lambda={KL}$, {MUFORM} $\\mu$ '
             f'(SN sector $\\Delta\\chi^2=+2.0$ vs $\\Lambda$CDM)')
ax.legend(loc='upper left', fontsize=8.5, framealpha=0.9)
fig.tight_layout()
fig.savefig(os.path.join(FIGDIR, 'cdot7_hubble_diagram.svg'))
plt.close(fig)
print('wrote cdot7_hubble_diagram.svg (real Pantheon+ data)')

# ---------------------------------------------------------------------------
# Figure 2: evolving a0 vs. MUSE-DARK III / MIGHTEE-HI, real joint-fit trajectory
# ---------------------------------------------------------------------------
zg2 = np.linspace(0.001, 1.6, 300)
a0_traj = A0_LOC * np.array([ratio_fn(z) for z in zg2])
a0_fixed = A0_LOC * (1 + zg2) ** 1.5
a0_const = np.full_like(zg2, A0_LOC)

fig, ax = plt.subplots(figsize=(6.5, 4.5))
ax.plot(zg2, a0_const, color='0.5', lw=1.8, ls=':', label='constant $a_0$ (standard MOND) — excluded')
ax.plot(zg2, a0_fixed, color='#d62728', lw=1.8, ls='--',
        label=r'naive fixed-point law $\propto(1+z)^{3/2}$ — excluded')
ax.plot(zg2, a0_traj, color='#1f77b4', lw=2.4, label='four-term joint-fit trajectory (this framework)')

# MUSE-DARK III (Ciocan et al. 2026): quantile bins + global point
z1, z2, zmid = 0.33, 1.44, 0.885
ax.errorbar([zmid], [2.38], yerr=[[0.10], [0.12]],
            fmt='o', color='black', ms=7, capsize=4, zorder=5,
            label=r'MUSE-DARK III, $a_0(z{\sim}1)$ (Ciocan et al. 2026)')
ax.plot([z1, z2], [1.99, 2.71], 'x', color='#2ca02c', ms=9,
        mew=2, zorder=5, label='MUSE-DARK III quantile bins')

# MIGHTEE-HI (Varasteanu et al. 2025)
ax.errorbar([0.05], [1.69], yerr=[[0.13], [0.13]], fmt='s', color='#9467bd', ms=7,
            capsize=4, zorder=5, label=r'MIGHTEE-HI, $z<0.08$ (Varasteanu et al. 2025)')

# SPARC canonical value (independent RAR-based local calibration) vs. this fit's own
# predicted local a0 -- shown as two distinct points, since they now visibly differ
ax.errorbar([0.0], [A0_SPARC], yerr=0.26, fmt='*', color='0.4', ms=11, zorder=4, capsize=4,
            label='SPARC canonical value ($z\\approx0$, independent of this fit)')
ax.errorbar([0.0], [A0_LOC], yerr=0.0, fmt='*', color='#1f77b4', ms=13, zorder=5,
            label='this fit\'s own predicted $a_0(0)$')

ax.set_xlabel('redshift $z$')
ax.set_ylabel(r'$a_0(z)$  [$10^{-10}\ \mathrm{m/s^2}$]')
ax.set_title('cdot-7: evolving MOND scale $a_0(t)=\\lambda\\dot c(t)$ vs. observation\n'
             f'(four-term fit: $\\kappa\\lambda={KL}$, $\\varepsilon_0={EPS0}$, '
             f'$\\lambda={LAM}$, incl. real SPARC RAR + mass census)')
ax.legend(loc='upper left', fontsize=8, framealpha=0.9)
ax.set_xlim(-0.03, 1.6)
ax.set_ylim(0, 3.2)
fig.tight_layout()
fig.savefig(os.path.join(FIGDIR, 'cdot7_a0_evolution.svg'))
plt.close(fig)
print('wrote cdot7_a0_evolution.svg (real joint-fit trajectory)')
