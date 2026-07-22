#!/usr/bin/env python3
r"""
wp7_r3_reclosure_feasibility.py -- 2026-07-21. R3 (per
Advisory-WP7-InstabilityRecourses-2026-07-21.md sec.3, and the
advisor's own recommendation in Advisory-WP7-
R1FeasibilityResolvedNotViable-2026-07-21.md sec.4, following R1's now-
derived, confirmed-negative result, Section 16 of Update-WP7-
InstabilityRecourses-2026-07-21.md): a FIRST, bounded feasibility scan
for the re-closure recourse, NOT the full joint Q2/EFE re-fit -- see
the honest caveat below before treating any number here as a validated
resolution.

WHAT R3 CLAIMS (per the recourse advisory): c_ad^2(z) is a trajectory
OUTPUT, not a free input -- the matter-era w sitting slightly below
zero is what makes it negative, and that offset moves under a changed
census content or fit, notably the low-Sigma-m_nu re-closure that is
already the KATRIN-aligned WP4a lever (SessionLog-2026-07-16, "the
neutrino-mass lever, ~5% of the needed 27% [theta_star miss]"). The
advisory explicitly warns this "cannot be tuned in isolation -- the
invoice is forced at fixed E(z) and census" -- i.e. a FULLY rigorous R3
test requires the joint Q2/EFE re-fit (Gate 3's own standing, deferred
item), not attempted here.

WHAT IS ATTEMPTED INSTEAD, honestly scoped as a feasibility test: hold
the TOTAL closure fraction Omega_closure=0.074 fixed (the one number
this program's own census fit constrains directly) and vary ONLY the
internal split between the neutrino and cold-matter pieces (M_NU, the
per-flavor neutrino mass -- lower M_NU moves mass from the neutrino
sector to om_cold, at FIXED total Omega_closure), re-running the EXACT
SAME closure ODE (wp7_stage3e_riccati_handoff.py's own machinery,
unmodified) for each M_NU value. This does NOT re-fit E(z) itself
against any external data (that is the "joint re-fit" the advisory
flags as the real, heavier lever) -- it tests the narrower question of
whether the KATRIN-aligned direction (lower Sigma m_nu) shifts c_ad^2(z)
in the needed direction AT ALL, holding everything else fixed, before
committing to the full re-fit.
"""
import numpy as np
from scipy.integrate import quad, cumulative_trapezoid, solve_ivp
from scipy.interpolate import interp1d

KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
K_B = 0.4355
rho_crit = 3 * (H * 100 * 1000 / 3.0857e22)**2 / (8 * np.pi * G_N)
OM_G = ((A_RAD * T_G0**4) / C0**2) / rho_crit
T_NU0 = (4 / 11)**(1 / 3) * T_G0
OM_CL = 0.074
F0 = 7 * np.pi**4 / 120
ag = np.concatenate([[0], np.logspace(-3, 7, 400)])
Fg = np.array([quad(lambda x, A=A: x * x * np.sqrt(x * x + A * A) / (np.exp(x) + 1), 0, 60,
                     limit=300)[0] for A in ag])
Fi = interp1d(np.log10(ag[1:]), np.log10(Fg[1:]), kind='cubic')


def Ffd(A):
    A = np.asarray(A, float)
    return np.where(A < 1e-3, F0, 10**Fi(np.log10(np.maximum(A, 1e-3))))


REL = (7 / 8) * (4 / 11)**(4 / 3)
c0H0_Mpc = C0 / 1000 / (100 * H)


def build_trajectory(M_NU):
    """Rebuild the ENTIRE closure trajectory (unmodified machinery from
    wp7_stage3e_riccati_handoff.py) for a given per-flavor neutrino
    mass M_NU (eV), holding Omega_closure=0.074 fixed and redistributing
    the cold/neutrino split accordingly."""
    def u_nu(z):
        A = M_NU / (K_B_EV * T_NU0 * (1 + z))
        return 3 * REL * (1 + z)**4 * Ffd(A) / F0

    om_nu0 = float(u_nu(0.0)) * (A_RAD * T_G0**4) / C0**2 / rho_crit
    om_cold = OM_CL - om_nu0

    def u_hat(z):
        return om_cold * (1 + z)**3 + OM_G * (1 + z)**4 + OM_G * u_nu(z)

    u00 = float(u_hat(0.0))

    def Ssrc(s):
        z = np.exp(-1.5 * s) - 1
        return (u_hat(z) / u00) * np.exp(5 * s)

    mu0 = X0 / (1 + X0)

    def x_of(r, s):
        y = min(mu0 * r * r * np.exp(-2 * s) * float(Ssrc(s)), 1 - 1e-13)
        return y / (1 - y)

    sol = solve_ivp(lambda s, r: [KL * x_of(r[0], s) * r[0]], (0, -11), [1.0],
                     rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
    s = np.linspace(-10.8, -1e-6, 16000)
    r = sol.sol(s)[0]
    x = np.array([x_of(ri, si) for ri, si in zip(r, s)])
    E2 = (np.exp(-1.5 * s) * X0 / (x * r))**2
    z_arr = np.exp(-1.5 * s) - 1
    Q_arr = np.exp(-2.5 * s)
    u_arr = np.array([float(u_hat(z)) for z in z_arr])
    Om_s = E2 - u_arr
    I = cumulative_trapezoid((Q_arr**(-2 / 3) * Om_s)[::-1], s[::-1], initial=0.0)[::-1]
    F_arr = Q_arr**(2 / 3) * (-5.0 * I)
    F_Q = -0.4 * np.exp(2.5 * s) * np.gradient(F_arr, s)
    Om_s_frac = Om_s / E2

    w = -(1 / 4.5) * np.gradient(np.log(np.abs(Om_s)), s) - 1
    dw_ds = np.gradient(w, s)
    dlnrho_ds = np.gradient(np.log(np.abs(Om_s)), s)
    cad2 = w + dw_ds / dlnrho_ds

    Nax = -np.log(1 + z_arr)
    order = np.argsort(Nax)
    Nsort = Nax[order]
    E2_i = interp1d(Nsort, E2[order], kind='cubic')
    w_i = interp1d(Nsort, w[order], kind='linear')
    cad2_i = interp1d(Nsort, cad2[order], kind='linear')
    Oms_i = interp1d(Nsort, Om_s_frac[order], kind='linear')
    Q_i = interp1d(Nsort, Q_arr[order], kind='linear')
    FQ_i = interp1d(Nsort, F_Q[order], kind='linear')
    Nmin_g, Nmax_g = Nsort[0], Nsort[-1]
    return dict(E2_i=E2_i, w_i=w_i, cad2_i=cad2_i, Oms_i=Oms_i, Q_i=Q_i, FQ_i=FQ_i,
                Nmin_g=Nmin_g, Nmax_g=Nmax_g, om_nu0=om_nu0, om_cold=om_cold)


def coefs(traj, N, kappa):
    N = min(max(N, traj['Nmin_g']), traj['Nmax_g'])
    Ev2 = float(traj['E2_i'](N)); Hc = np.sqrt(Ev2)
    wv = float(traj['w_i'](N)); cad2v = float(traj['cad2_i'](N))
    Qb = float(traj['Q_i'](N)); FQv = float(traj['FQ_i'](N)); Oms = float(traj['Oms_i'](N))
    dKdQ = -0.5 * FQv
    kap3 = cad2v * kappa / (3 * Oms)
    return Hc, wv, cad2v, Qb, dKdQ, kap3


def aEE_aEalpha(traj, N, kappa):
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(traj, N, kappa)
    dPi_dEalpha = kap3 * K_B
    dPi_dalpha = kap3 * (2 - K_B) * Qb
    a_EE = (-(2 - K_B) * (Qb / (1 + wv) * dPi_dEalpha)) / (K_B * Hc) - 1.0
    a_Ealpha = (dKdQ * Qb - (2 - K_B) * (Qb / (1 + wv) * dPi_dalpha
                + (Hc + Qb) * Qb - 3 * cad2v * Hc * Qb)) / (K_B * Hc)
    return Hc, a_EE, a_Ealpha


if __name__ == '__main__':
    M_NU_baseline = 1.374 / 3
    k_Mpc = 2.71e-3
    zs = [1090, 100, 10, 1, 0.0]

    print(f"Baseline M_NU={M_NU_baseline:.4f} eV/flavor (Sigma m_nu={3*M_NU_baseline:.3f} eV),"
          f" Omega_closure={OM_CL} fixed throughout\n")

    print(f"{'M_NU (eV)':>10} {'Sigma m_nu':>11} {'om_nu0':>9} {'om_cold':>9}  "
          + "  ".join(f"cad2(z={zt})" for zt in zs))
    for M_NU in (M_NU_baseline, 0.3, 0.2, 0.1, 0.06, 0.02, 1e-6):
        traj = build_trajectory(M_NU)
        row = []
        for zt in zs:
            N = -np.log(1 + zt)
            row.append(f"{float(traj['cad2_i'](min(max(N, traj['Nmin_g']), traj['Nmax_g']))):11.5g}")
        print(f"{M_NU:10.4f} {3*M_NU:11.4f} {traj['om_nu0']:9.5f} {traj['om_cold']:9.5f}  "
              + "  ".join(row))

    print()
    print(f"{'M_NU (eV)':>10}  " + "  ".join(f"z={zt:>6}" for zt in zs) + "  [max Re(lambda)]")
    for M_NU in (M_NU_baseline, 0.3, 0.2, 0.1, 0.06, 0.02, 1e-6):
        traj = build_trajectory(M_NU)
        row = []
        for zt in zs:
            N = -np.log(1 + zt)
            kap = (k_Mpc * c0H0_Mpc / np.exp(N))**2
            Hc, a_EE, a_Ealpha = aEE_aEalpha(traj, N, kap)
            Jm = np.array([[0.0, 1.0 / Hc], [a_Ealpha, a_EE]])
            eig = np.linalg.eigvals(Jm)
            row.append(f"{max(eig.real):10.4g}")
        print(f"{M_NU:10.4f}  " + "  ".join(row))
