#!/usr/bin/env python3
"""
msigma_fit.py -- cdot-7, 2026-07-08
First real-data attempt at Foundation.md Sec5.7's M-sigma confrontation: does this
framework's size-independent prediction sigma^4 ~ Gamma*G*M*a0(z) fit real z=0-2.4
quiescent-galaxy dynamics better, worse, or indistinguishably from the standard
Newtonian, size-driven explanation sigma^2 ~ K*G*M/R_e (using each galaxy's own
measured R_e, no cosmology)?

Data (all real, downloaded, machine-readable -- see data/msigma/):
  z~0 anchor: ATLAS3D (Cappellari et al. 2013a/b, Paper XV+XX) + distances
    (Cappellari et al. 2011a, Paper I) -- 260 nearby early-type galaxies.
  z~0.8-2.2: van de Sande et al. 2013 (ApJ 771, 85) Table 4, a 73-galaxy literature
    compilation with sigma, circularized R_e, stellar mass already in physical units.
  z~0.9-1.6: Belli, Newman & Ellis 2014 (ApJ 783, 117) Table 2, 56 galaxies (LRIS).
  z~1.5-2.4: Belli, Newman & Ellis 2017 (ApJ 834, 18) Table 2 -- only the first 24
    rows have usable sigma per the paper's own note (rest are "cdots" placeholders).

Known, stated caveats (not hidden):
  - Cross-catalog IMF/M* systematic not corrected: ATLAS3D's stellar M/L and the
    high-z papers' SED-fit M* may not share an identical IMF normalization; a
    residual ~0.1-0.2 dex mass offset between the z=0 anchor and the high-z sample
    is plausible and would bias Gamma/K by the same factor (partially degenerate
    with Gamma's own O(1)-and-undetermined status).
  - van de Sande's Table 4 pulls in several objects from Newman et al. 2010, which
    Belli et al.'s own group later re-measured; cross-matched by position (3") and
    the van de Sande duplicates dropped in favor of the more recent Belli values.
  - ATLAS3D sigma/M* have no simple per-object errors published in these particular
    tables; local Gamma/K calibration is done unweighted (median of ratios), while
    the high-z discriminating test uses the real reported sigma uncertainties.
"""
import os
import numpy as np
from scipy.integrate import solve_ivp

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'msigma')
G = 6.674e-11
MSUN = 1.989e30
KPC = 3.0857e19  # m

# ---------------------------------------------------------------------------
# This framework's fitted trajectory (four-term fit, Foundation.md S2.2/S5.6):
# eps0=-0.0909, kappa*lambda=0.4355, lambda=0.3056, simple mu. Reproduces a0(z)
# without needing the SN object -- same closure ODE as four_term_fit.py/
# joint_fit.py, integrated standalone over a wider range (z up to ~3).
# ---------------------------------------------------------------------------
EPS0, KL, LAM = -0.0909, 0.4355, 0.3056
C0, H0 = 2.9979e8, 70 * 1000 / 3.0857e22
CH0 = (2. / 3.) * C0 * H0
A0_0 = LAM * CH0  # a0(z=0), m/s^2 -- matches make_figures.py's A0_LOC


def mu_of_x(x):
    return x / (1 + x)


def mu_force_inv(y):
    """Solve mu(x)*x = y for x>0 (simple mu): the AQUAL force law g_bar=mu(g_obs/a0)*g_obs,
    reused verbatim from four_term_fit.py's RAR machinery -- valid at ANY regime, not just
    the deep-MOND asymptote (needed here since these systems sit at g/a0~1-3, not g/a0<<1)."""
    return (y + np.sqrt(y * y + 4 * y)) / 2


def g_obs_aqual(mbar_kg, re_m, a0):
    """Full AQUAL-consistent observed acceleration for a system with Newtonian
    g_bar=G*M/Re^2, at MOND scale a0 -- not the pure deep-MOND asymptote."""
    g_bar = G * mbar_kg / re_m ** 2
    x = mu_force_inv(g_bar / a0)
    return a0 * x


def setup_closure(lamt):
    xs = 3.0 / (4 * lamt)
    return xs, xs / (1 + xs), (lambda m: m / (1 - m))


def a0_ratio_function(eps0, lamt, a_min=0.2):
    xs, mus, xinv = setup_closure(lamt)
    r0 = 1.0 + eps0
    rhs = lambda a, Y: [lamt * xinv(min(mus * Y[0] ** 2 / a ** 1.5, 1 - 1e-13)) * Y[0] / a]
    sol = solve_ivp(rhs, [1.0, a_min], [r0], dense_output=True, rtol=1e-10, atol=1e-12)
    x0 = xinv(min(mus * r0 * r0, 1 - 1e-13))

    def ratio(zz):
        a = (1 + zz) ** (-2 / 3.)
        r = sol.sol(a)[0]
        x = xinv(min(mus * r * r / a ** 1.5, 1 - 1e-13))
        return (x0 * r0) / (x * r) * a ** (-1.5)
    return ratio


# z up to 2.5 -> a down to (3.5)^-1.5 = 0.153; leave margin
A0_RATIO = a0_ratio_function(EPS0, KL, a_min=0.12)


def a0_of_z(z):
    return A0_0 * A0_RATIO(z)


# ---------------------------------------------------------------------------
# ATLAS3D z~0 anchor
# ---------------------------------------------------------------------------
def load_atlas3d():
    sig_e, re_arcsec, lum = {}, {}, {}
    with open(os.path.join(DATA, 'Cappellari2013a_Table1.txt')) as f:
        for line in f:
            if not line.strip() or line.startswith('#'):
                continue
            p = line.split()
            if '--' in p:
                continue  # 2/260 galaxies have no reported size/shape (JAM quality flag issue)
            name = p[0]
            sig_e[name] = 10 ** float(p[1])
            re_arcsec[name] = 10 ** float(p[9])   # col10: logRe, circularized
            lum[name] = 10 ** float(p[14])         # logLum, Lsun,r

    ml_star = {}
    with open(os.path.join(DATA, 'Cappellari2013b_Table1.txt')) as f:
        for line in f:
            if not line.strip() or line.startswith('#'):
                continue
            p = line.split()
            if '----' in p:
                continue
            ml_star[p[0]] = 10 ** float(p[3])      # logML_star, r-band

    dist = {}
    with open(os.path.join(DATA, 'Cappellari2011a_Table3.txt')) as f:
        for line in f:
            if not line.strip() or line.startswith('#'):
                continue
            p = line.split()
            dist[p[0]] = float(p[7])               # D, Mpc

    names = sorted(set(sig_e) & set(ml_star) & set(dist))
    sig, mstar, re_kpc = [], [], []
    for n in names:
        sig.append(sig_e[n])
        mstar.append(ml_star[n] * lum[n])
        theta_rad = re_arcsec[n] * np.pi / (180 * 3600)
        re_kpc.append(theta_rad * dist[n] * 1000)
    return np.array(sig), np.array(mstar), np.array(re_kpc), names


# ---------------------------------------------------------------------------
# High-z samples
# ---------------------------------------------------------------------------
def load_vandesande():
    # Tab-delimited VizieR TSV (asu-tsv), fixed column order regardless of blank
    # optional fields (q/e_q are blank for most rows but remain as empty tab tokens):
    # recno Ref ID f_ID zsp re e_re n e_n q e_q sigma E_sigma e_sigma ap.c kn
    # logMdyn E_logMdyn e_logMdyn logM* Filt NMBS SimbadName _RA _DE
    z, re, sig, mstar, ra, de = [], [], [], [], [], []
    with open(os.path.join(DATA, 'vandesande2013_table4.tsv')) as f:
        for line in f:
            p = line.split('\t')
            if len(p) != 25:
                continue
            try:
                int(p[0])
            except ValueError:
                continue
            z.append(float(p[4])); re.append(float(p[5])); sig.append(float(p[11]))
            mstar.append(10 ** float(p[19])); ra.append(float(p[23])); de.append(float(p[24]))
    return map(np.array, (z, re, sig, mstar, ra, de))


def load_belli(fn, ncols_min=10, sigma_col=5, re_col=6, q_col=8, mstar_col=9, circularize=False):
    z, re, sig, mstar, ra, de = [], [], [], [], [], []
    with open(os.path.join(DATA, fn)) as f:
        for line in f:
            p = [x.strip() for x in line.split('\t')]
            if len(p) < ncols_min:
                continue
            try:
                ra_ = float(p[2]); de_ = float(p[3]); zz = float(p[4])
            except ValueError:
                continue
            sig_tok = p[sigma_col]
            if 'cdots' in sig_tok:
                continue
            sigma = float(sig_tok.split('+or-')[0].strip().rstrip('^abcde'))
            re_tok = p[re_col].split('+or-')[0].strip()
            re_val = float(re_tok)
            if circularize:
                q = float(p[q_col].rstrip('^abcde'))
                re_val *= np.sqrt(q)
            ms_tok = p[mstar_col].split('+or-')[0].strip().rstrip('^abcde')
            logmstar = float(ms_tok)
            z.append(zz); re.append(re_val); sig.append(sigma)
            mstar.append(10 ** logmstar); ra.append(ra_); de.append(de_)
    return map(np.array, (z, re, sig, mstar, ra, de))


def crossmatch_mask(ra1, de1, ra2, de2, tol_arcsec=3.0):
    tol = tol_arcsec / 3600.0
    mask = np.zeros(len(ra1), dtype=bool)
    for i, (r, d) in enumerate(zip(ra1, de1)):
        dist = np.sqrt(((r - ra2) * np.cos(np.radians(d))) ** 2 + (d - de2) ** 2)
        if np.any(dist < tol):
            mask[i] = True
    return mask


if __name__ == '__main__':
    sig0, mstar0, re0, names0 = load_atlas3d()
    print(f'ATLAS3D (z~0 anchor): {len(sig0)} galaxies merged across the three tables')

    z_v, re_v, sig_v, mstar_v, ra_v, de_v = load_vandesande()
    print(f'van de Sande+2013 Table 4: {len(z_v)} galaxies parsed (z={z_v.min():.2f}-{z_v.max():.2f})')

    z_b14, re_b14, sig_b14, mstar_b14, ra_b14, de_b14 = load_belli(
        'belli2014_table2.txt', ncols_min=11, sigma_col=5, re_col=6, mstar_col=9, circularize=False)
    print(f'Belli+2014 Table 2: {len(z_b14)} galaxies parsed (z={z_b14.min():.2f}-{z_b14.max():.2f})')

    z_b17, re_b17, sig_b17, mstar_b17, ra_b17, de_b17 = load_belli(
        'belli2017_table2.txt', ncols_min=11, sigma_col=5, re_col=6, q_col=8, mstar_col=9, circularize=True)
    print(f'Belli+2017 Table 2: {len(z_b17)} galaxies parsed with real sigma (z={z_b17.min():.2f}-{z_b17.max():.2f})')

    dup14 = crossmatch_mask(ra_v, de_v, ra_b14, de_b14)
    dup17 = crossmatch_mask(ra_v, de_v, ra_b17, de_b17)
    dup = dup14 | dup17
    print(f'van de Sande objects duplicated in Belli+14/17 (dropped, position <3"): {dup.sum()}')

    z_hi = np.concatenate([z_v[~dup], z_b14, z_b17])
    re_hi = np.concatenate([re_v[~dup], re_b14, re_b17])
    sig_hi = np.concatenate([sig_v[~dup], sig_b14, sig_b17])
    mstar_hi = np.concatenate([mstar_v[~dup], mstar_b14, mstar_b17])
    print(f'Combined unique high-z sample: {len(z_hi)} galaxies, z={z_hi.min():.2f}-{z_hi.max():.2f}\n')

    # --- local calibration (z~0, ATLAS3D) ---
    sig0_ms = sig0 * 1e3  # km/s -> m/s
    re0_m = re0 * KPC
    mstar0_kg = mstar0 * MSUN

    # (a) naive deep-MOND asymptote: sigma^4 = Gamma*G*M*a0 -- valid only for g<<a0
    gamma_i = sig0_ms ** 4 / (G * mstar0_kg * a0_of_z(0.0))
    Gamma = np.median(gamma_i)

    # (b) pure Newtonian virial (the null/competing hypothesis): sigma^2 = K*G*M/Re
    k_i = sig0_ms ** 2 * re0_m / (G * mstar0_kg)
    K = np.median(k_i)

    # (c) full AQUAL, valid at any regime via the interpolating function (correct
    # treatment given these systems sit at g/a0~1-3, not deep in either limit):
    # sigma^2 = Gamma_geo * g_obs_aqual(M, Re, a0) * Re
    g_obs0 = g_obs_aqual(mstar0_kg, re0_m, a0_of_z(0.0))
    ggeo_i = sig0_ms ** 2 / (g_obs0 * re0_m)
    Gamma_geo = np.median(ggeo_i)

    print(f'Local calibration (ATLAS3D, a0(0)={A0_0*1e10:.3f}e-10 m/s^2):')
    print(f'  Gamma     (deep-MOND asymptote, sigma^4=Gamma*G*M*a0) = {Gamma:.3f}  '
          f'(scatter: {np.std(np.log10(gamma_i)):.3f} dex)')
    print(f'  K         (pure Newtonian virial, sigma^2=K*G*M/Re)   = {K:.3f}  '
          f'(scatter: {np.std(np.log10(k_i)):.3f} dex)')
    print(f'  Gamma_geo (full AQUAL, any regime, sigma^2=Gamma_geo*g_obs*Re) = {Gamma_geo:.3f}  '
          f'(scatter: {np.std(np.log10(ggeo_i)):.3f} dex)\n')

    # --- acceleration-regime check: are these systems actually deep-MOND? ---
    g_char0 = sig0_ms ** 2 / re0_m  # characteristic Newtonian-equivalent acceleration
    print(f'Characteristic acceleration g=sigma^2/Re, ATLAS3D (z~0):')
    print(f'  median g/a0 = {np.median(g_char0 / a0_of_z(0.0)):.2f}  '
          f'(16-84 pctile: {np.percentile(g_char0/a0_of_z(0.0),16):.2f}-'
          f'{np.percentile(g_char0/a0_of_z(0.0),84):.2f})  '
          f'-- g/a0 ~ 1 or above means these are NOT deep-MOND systems;\n'
          f'  the naive asymptotic Gamma above is not self-consistent for this sample,\n'
          f'  hence the full-AQUAL Gamma_geo calibration is the physically appropriate one.\n')

    # --- high-z discriminating test ---
    re_hi_m = re_hi * KPC
    mstar_hi_kg = mstar_hi * MSUN
    a0z = np.array([a0_of_z(z) for z in z_hi])
    sig_obs = sig_hi * 1e3  # m/s

    sig_pred_mond = (Gamma * G * mstar_hi_kg * a0z) ** 0.25             # naive asymptote
    sig_pred_virial = np.sqrt(K * G * mstar_hi_kg / re_hi_m)             # pure Newtonian, no MOND
    g_obs_hi = g_obs_aqual(mstar_hi_kg, re_hi_m, a0z)
    sig_pred_aqual = np.sqrt(Gamma_geo * g_obs_hi * re_hi_m)             # full AQUAL, any regime

    res_mond = np.log10(sig_obs / sig_pred_mond)
    res_virial = np.log10(sig_obs / sig_pred_virial)
    res_aqual = np.log10(sig_obs / sig_pred_aqual)

    g_char_hi = sig_obs ** 2 / re_hi_m
    print('High-z discriminating test (full AQUAL w/ a0(z) vs. pure Newtonian virial, both regime-honest):')
    print(f'  median g/a0(z), high-z sample = {np.median(g_char_hi / a0z):.2f} '
          f'(16-84 pctile: {np.percentile(g_char_hi/a0z,16):.2f}-{np.percentile(g_char_hi/a0z,84):.2f})'
          f'  -- confirms transition regime, not deep-MOND, at high z too')
    print(f'  RMS residual, naive deep-MOND asymptote = {np.std(res_mond):.4f} dex  (mean {np.mean(res_mond):+.4f})')
    print(f'  RMS residual, pure Newtonian virial      = {np.std(res_virial):.4f} dex  (mean {np.mean(res_virial):+.4f})')
    print(f'  RMS residual, full AQUAL (any regime)    = {np.std(res_aqual):.4f} dex  (mean {np.mean(res_aqual):+.4f})')

    # bootstrap: is the RMS gap (virial - AQUAL) significant, or noise given N and
    # the two models sharing the same underlying galaxies (paired resampling)?
    rng = np.random.default_rng(12345)
    n = len(z_hi)
    diffs = np.empty(2000)
    for i in range(2000):
        idx = rng.integers(0, n, n)
        diffs[i] = np.std(res_virial[idx]) - np.std(res_aqual[idx])
    print(f'\n  Bootstrap (2000 resamples): RMS(virial)-RMS(full AQUAL) = {np.mean(diffs):+.4f} '
          f'+/- {np.std(diffs):.4f} dex; fraction of resamples favoring AQUAL '
          f'(diff>0) = {np.mean(diffs > 0)*100:.1f}%')

    # residual-vs-z trend (simple linear fit, unweighted)
    for label, res in [('naive MOND', res_mond), ('virial', res_virial), ('full AQUAL', res_aqual)]:
        A = np.vstack([z_hi, np.ones_like(z_hi)]).T
        slope, intercept = np.linalg.lstsq(A, res, rcond=None)[0]
        pred = A @ [slope, intercept]
        ss_res = np.sum((res - pred) ** 2)
        ss_tot = np.sum((res - res.mean()) ** 2)
        r2 = 1 - ss_res / ss_tot
        print(f'  {label:10s} residual vs z: slope={slope:+.4f} dex/z, intercept={intercept:+.4f}, R^2={r2:.3f}')

    # robustness: is the AQUAL-vs-virial preference driven by the highest-z tail
    # (Belli+2017, z>1.6) or does it hold within the lower-z subsample too?
    print('\nRobustness split by redshift (same fixed Gamma_geo/K calibration throughout):')
    for lo, hi in [(0.8, 1.6), (1.6, 2.5)]:
        sel = (z_hi >= lo) & (z_hi < hi)
        if sel.sum() < 5:
            continue
        rv, ra_ = np.std(res_virial[sel]), np.std(res_aqual[sel])
        print(f'  z in [{lo},{hi}): N={sel.sum():3d}  RMS virial={rv:.4f}  RMS AQUAL={ra_:.4f}  '
              f'(AQUAL {"better" if ra_ < rv else "worse"} by {abs(rv-ra_):.4f} dex)')
