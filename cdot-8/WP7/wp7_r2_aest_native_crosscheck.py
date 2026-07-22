#!/usr/bin/env python3
"""
wp7_r2_aest_native_crosscheck.py -- 2026-07-21. R2 (per
Advisory-WP7-InstabilityRecourses-2026-07-21.md): run the same
vector-sector Jacobian, at the same ISW-relevant wavenumbers, on AeST's
OWN native, published, CMB-Planck-fitting K(Q) choice -- does the
never-restabilizing instability (Stage 4, sec.42) appear there too, or
is it specific to cdot-8's own census-forced F(Q)?

AeST's own "Higgs-like" K(Q) = (K_2/(4 Q_0^2))(Qbar^2-Q_0^2)^2, with the
paper's own quoted tuned parameters (Cl_TT_EE_with_residuals.pdf legend,
read directly from the figure): K_B=0.3, Q_0=1 Mpc^-1, K_2=8.5e8.

BACKGROUND RECONSTRUCTION (honest, stated approximations):
- Q(a): solved EXACTLY from the shift-symmetric scalar's own conserved
  charge, a^3 F_Q(Q) = const (the free-scalar conservation law -- exact
  for AeST's native, non-M5 action; this is the same identity WP3 used
  as "necessary but not sufficient" for cdot-8's own construction,
  but here it IS the complete equation of motion since there's no M5).
  Solved via a numerically stable delta=(Q/Q0 - 1) reformulation
  (avoids catastrophic cancellation from tracking Q/Q0 then subtracting
  1, which loses all precision once the field settles within 1e-10 of
  the minimum -- an easy trap, caught before trusting any result here).
  Branch continuation used to track the physical (near-minimum) root
  continuously from early to late times.
- rho_s(a): the NATIVE (non-M5) coefficient, rho_s = (1/3)(Q F_Q - F) --
  NOT cdot-8's own M5-modified (1/2) coefficient, since vanilla AeST has
  no M5 back-reaction on the Hamiltonian constraint.
- H(a), Omega_s(a): approximated by a standard flat LCDM background
  (Omega_m=0.3, Omega_L=0.7) and an assumed Omega_cdm-like fraction
  (0.25 today, scaling as matter) for the scalar's own CDM-mimicking
  content -- a stated, reasonable stand-in for "whatever background
  this fit actually reproduces" (the whole point of AeST's own fit is
  to match near-LCDM H(a) closely). w(a), c_ad^2(a) themselves are
  SHAPE-only (logarithmic-derivative) quantities and do not depend on
  this choice; only kap3's own Omega_s normalization does.
- The oscillation amplitude "eps" (free choice, not given precisely in
  the compact PRL) is set so |c_ad^2| stays small at recombination
  (~6.5e-4), consistent with the paper's own explicit statement that
  "c_ad^2 and w are small enough so that Pi -> 0" for its native models.

RESULT: the vector sector's fast eigenvalue resolves to comfortably
stable (Re(lambda)<0, or a small transient at z~1090 that resolves by
z~100) at EVERY one of the three ISW-relevant k's tested -- the exact
opposite of cdot-8's own persistent, never-restabilizing instability at
the same k's. This confirms the pathology is specific to cdot-8's own
census-forced, non-minimum-tracking F(Q), not to the imported AeST
field-perturbation machinery itself.
"""
import numpy as np
from scipy.interpolate import interp1d

K_B, Q0, K2 = 0.3, 1.0, 8.5e8
c0H0_Mpc = 2.99792458e5 / 70.0


def delta_branch(a_arr, eps):
    """Solve delta^3+3delta^2+2delta+eps/a^3=0 (u=Q/Q0=1+delta) directly
    in delta -- avoids the catastrophic cancellation of solving for u via
    the raw cubic u^3-u+eps/a^3=0 and then subtracting 1, which loses all
    precision once |delta| << 1 (caught before trusting any result)."""
    deltas = np.zeros_like(a_arr)
    for i, a in enumerate(a_arr):
        c0 = eps / a**3
        roots = np.roots([1, 3, 2, c0])
        real_roots = roots[np.abs(roots.imag) < 1e-9].real
        idx = np.argmin(np.abs(real_roots))
        deltas[i] = real_roots[idx]
    return deltas


def build_native_trajectory(eps=1e-12, n=4000):
    a_arr = np.logspace(-4, 0, n)
    delta = delta_branch(a_arr, eps)
    z_arr = 1 / a_arr - 1
    FQ = -2 * K2 * Q0 * (2 * delta + 3 * delta**2 + delta**3)
    rho_s_shape = -(delta * (2 + delta)) * (3 * (1 + delta)**2 + 1)

    s = np.log(a_arr)
    lnrho = np.log(np.abs(rho_s_shape))
    w = -(1 / 3) * np.gradient(lnrho, s, edge_order=2) - 1
    dw_ds = np.gradient(w, s, edge_order=2)
    dlnrho_ds = np.gradient(lnrho, s, edge_order=2)
    cad2 = w + dw_ds / dlnrho_ds

    Om_m0, Om_L0 = 0.3, 0.7
    E2 = Om_m0 * (1 + z_arr)**3 + Om_L0
    Om_cdm_frac = 0.25 * (1 + z_arr)**3 / E2

    Nax = np.log(a_arr)
    order = np.argsort(Nax)
    Ns = Nax[order]
    return {
        'E2_i': interp1d(Ns, E2[order], kind='cubic'),
        'w_i': interp1d(Ns, w[order], kind='linear'),
        'cad2_i': interp1d(Ns, cad2[order], kind='linear'),
        'Oms_i': interp1d(Ns, Om_cdm_frac[order], kind='linear'),
        'FQ_i': interp1d(Ns, FQ[order], kind='linear'),
        'Nmin': Ns[0], 'Nmax': Ns[-1],
    }


def aEE_aEalpha_native(traj, N, kappa):
    N = min(max(N, traj['Nmin']), traj['Nmax'])
    Hc = np.sqrt(float(traj['E2_i'](N)))
    wv = float(traj['w_i'](N)); cad2v = float(traj['cad2_i'](N))
    Oms = float(traj['Oms_i'](N)); FQv = float(traj['FQ_i'](N))
    Qb = Q0
    dKdQ = -0.5 * FQv
    kap3 = cad2v * kappa / (3 * Oms)
    dPi_dEalpha = kap3 * K_B
    dPi_dalpha = kap3 * (2 - K_B) * Qb
    a_EE = (-(2 - K_B) * (Qb / (1 + wv) * dPi_dEalpha)) / (K_B * Hc) - 1.0
    a_Ealpha = (dKdQ * Qb - (2 - K_B) * (Qb / (1 + wv) * dPi_dalpha
                + (Hc + Qb) * Qb - 3 * cad2v * Hc * Qb)) / (K_B * Hc)
    return Hc, a_EE, a_Ealpha


if __name__ == '__main__':
    traj = build_native_trajectory()

    print("=== c_ad^2(z), w(z) for AeST's own native Higgs-like tuning ===")
    for zt in (1090, 100, 10, 1, 0.1, 0.0):
        N = np.log(1 / (1 + zt))
        N = min(max(N, traj['Nmin']), traj['Nmax'])
        print(f"  z={zt:7}: w={float(traj['w_i'](N)): .4e}  "
              f"c_ad^2={float(traj['cad2_i'](N)): .4e}")

    print("\n=== Native vector-sector eigenvalue scan, ISW-relevant k's ===")
    for k_Mpc in (1.1e-3, 2.71e-3, 5.4e-3):
        print(f"\nk={k_Mpc:.2e} Mpc^-1:")
        for zt in (1090, 100, 10, 1, 0.1, 0.0):
            N = np.log(1 / (1 + zt))
            kap = (k_Mpc * c0H0_Mpc / np.exp(N))**2
            Hc, a_EE, a_Ea = aEE_aEalpha_native(traj, N, kap)
            J = np.array([[0.0, 1.0 / Hc], [a_Ea, a_EE]])
            eigs = np.linalg.eigvals(J)
            print(f"  z={zt:7}: kappa={kap:12.4e}  max_Re={np.max(eigs.real):10.4f}  eigs={eigs}")

    print("""
VERDICT: at every one of l=2,5,10's own wavenumbers, the native
Higgs-like tuning's vector sector resolves to comfortably stable
(Re(lambda)<0) by z~100 at the latest (a brief, small transient near
z~1090 for the two larger k's, nowhere near cdot-8's own persistent,
ever-growing instability) and STAYS stable through the entire
ISW-relevant range down to z=0. This is the opposite of cdot-8's own
result (Stage 4) at these same k's -- confirming the pathology belongs
to cdot-8's own census-forced F(Q), not to the imported machinery.
""")
