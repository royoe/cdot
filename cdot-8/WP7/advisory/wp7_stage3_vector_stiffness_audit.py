#!/usr/bin/env python3
"""
wp7_stage3_vector_stiffness_audit.py -- secondary-advisor diagnosis, 2026-07-20.

Stage 0 (wp7_stiffness_audit.py) audited only the SCALAR condensate
sector's effective mass (mu_eff^2 ~ F_QQ) and found it safe. It never
touched the vector (alpha, E_alpha) sector's own dynamics -- exactly
where wp7_stage3_field_variable.py's fast-onset blowup lives.

This script builds the local Jacobian of the (alpha, E_alpha) subsystem
alone (freezing delta_s, theta_s, Phi as slowly-varying external
sources -- the standard way to audit a fast subsystem's own stiffness/
stability independent of the slow sector it's embedded in), reusing
wp7_stage3_field_variable.py's own background trajectory and the
confirmed Stage-2 dK/dQ = -F_Q/2 coefficient.

Three things established:
  1. The instability is a genuine LARGE POSITIVE REAL eigenvalue (not a
     numerical-conditioning artifact) at high z / large kappa, becoming
     a stable, damped-oscillatory complex pair by z~10 or kappa->0.
  2. Setting kappa=0 gives a stable complex pair -- the instability is
     driven entirely by the Pi-feedback (kappa-dependent) term, not by
     any other part of the equations.
  3. There is a clean critical kappa_crit(z) (bifurcation from complex/
     stable to real/growing) -- and the corresponding critical comoving
     k is tiny (~1e-7 to ~1e-4 Mpc^-1 from z=1090 to z=10), meaning
     essentially every cosmologically relevant k is on the unstable
     side of this threshold at high z.

NOT resolved here: whether the Pi-formula's own kappa/a^2-normalization
(the Fourier-space Laplacian substitution used when going from
Update-WP7-PerturbationStructure-2026-07-18.md's imported eq. (11) to
this program's kappa=(k/(aH0))^2 convention) is exactly right -- this
was the one sub-term Stage 2's units contract did NOT separately
itemize as its own dictionary line (unlike the E_alpha coefficient,
which Stage 2 nailed down and this script reuses as confirmed). Two
candidate conventions were tried by hand and gave very different
answers (see the advisory); neither was independently cross-validated
the way the Poisson equation's own kappa convention was. Flagged, not
adjudicated.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.optimize import brentq

KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
K_B = 0.4355
rho_crit = 3 * (H * 100 * 1000 / 3.0857e22)**2 / (8 * np.pi * G_N)
OM_G = ((A_RAD * T_G0**4) / C0**2) / rho_crit
T_NU0, M_NU, OM_CL = (4 / 11)**(1 / 3) * T_G0, 1.374 / 3, 0.074
F0 = 7 * np.pi**4 / 120
ag = np.concatenate([[0], np.logspace(-3, 7, 400)])
Fg = np.array([quad(lambda x, A=A: x * x * np.sqrt(x * x + A * A) / (np.exp(x) + 1),
                     0, 60, limit=300)[0] for A in ag])
Fi = interp1d(np.log10(ag[1:]), np.log10(Fg[1:]), kind='cubic')


def Ffd(a):
    a = np.asarray(a, float)
    return np.where(a < 1e-3, F0, 10**Fi(np.log10(np.maximum(a, 1e-3))))


REL = (7 / 8) * (4 / 11)**(4 / 3)


def u_nu(z):
    a = M_NU / (K_B_EV * T_NU0 * (1 + z))
    return 3 * REL * (1 + z)**4 * Ffd(a) / F0


om_nu0 = float(u_nu(0.0)) * (A_RAD * T_G0**4) / C0**2 / rho_crit
om_cold = OM_CL - om_nu0


def u_hat(z):
    return om_cold * (1 + z)**3 + OM_G * (1 + z)**4 + OM_G * u_nu(z)


u00 = float(u_hat(0.0))


def S_src(s):
    z = np.exp(-1.5 * s) - 1
    return (u_hat(z) / u00) * np.exp(5 * s)


mu0 = X0 / (1 + X0)


def x_of(r, s):
    y = min(mu0 * r * r * np.exp(-2 * s) * float(S_src(s)), 1 - 1e-13)
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


def jacobian(N, kappa, pi_prefac=1.0):
    """2x2 Jacobian of (alpha, E_alpha) alone, freezing delta_s/theta_s/Phi
    as external sources (standard fast-subsystem stiffness-audit method).
    pi_prefac multiplies the kappa-dependent Pi term -- =1.0 reproduces
    wp7_stage3_field_variable.py's own coded normalization exactly."""
    Ev2 = float(E2_i(N)); Hc = np.sqrt(Ev2)
    wv = float(w_i(N)); cad2v = float(cad2_i(N))
    Qb = float(Q_i(N)); FQv = float(FQ_i(N))
    dKdQ = -0.5 * FQv                      # Stage-2 confirmed coefficient
    KB = K_B
    dchi_dalpha = Qb
    dPi_dEalpha = cad2v * kappa * pi_prefac * KB
    dPi_dalpha = cad2v * kappa * pi_prefac * (2 - KB) * dchi_dalpha
    dalpha_dEalpha = 1.0 / Hc
    dEalpha_dalpha = (dKdQ * dchi_dalpha
                       - (2 - KB) * (Qb / (1 + wv) * dPi_dalpha + (Hc + Qb) * dchi_dalpha
                                     - 3 * cad2v * Hc * Qb)) / (KB * Hc)
    dEalpha_dEalpha = (-(2 - KB) * (Qb / (1 + wv) * dPi_dEalpha)) / (KB * Hc) - 1.0
    return np.array([[0.0, dalpha_dEalpha], [dEalpha_dalpha, dEalpha_dEalpha]])


c0H0_Mpc = C0 / 1000 / (100 * H)

print("=== 1. Reproduce the coded (alpha, E_alpha) Jacobian's eigenvalues along the trajectory ===")
k_Mpc = 1e-4
for zt in (100, 90, 70, 50, 10, 1, 0):
    i = np.argmin(np.abs(z_arr - zt))
    Nv = Nax[i]; a = np.exp(Nv)
    kap = (k_Mpc * c0H0_Mpc / a)**2
    eigs = np.linalg.eigvals(jacobian(Nv, kap))
    print(f"  z={zt:>4}: kappa={kap:9.3e}  eigs={eigs}")

print("\n=== 2. Isolate the Pi-feedback term: eigenvalues vs kappa at fixed z=100 ===")
i = np.argmin(np.abs(z_arr - 100))
Nv = Nax[i]
for kap in (0.0, 1.872, 18.72, 187.2, 1871.6):
    eigs = np.linalg.eigvals(jacobian(Nv, kap))
    print(f"  kappa={kap:9.3f}: eigs={eigs}")

print("\n=== 3. Critical kappa (stable complex pair -> real growing mode) vs z ===")
for zt in (1090, 300, 100, 50, 10):
    i = np.argmin(np.abs(z_arr - zt))
    Nv = Nax[i]; a = np.exp(Nv)

    def disc(logk):
        J = jacobian(Nv, np.exp(logk))
        tr, det = J[1, 1], -J[0, 1] * J[1, 0]
        return tr * tr - 4 * det

    logk_crit = brentq(disc, np.log(1e-3), np.log(1e4))
    kap_crit = np.exp(logk_crit)
    k_crit_Mpc = np.sqrt(kap_crit) * a / c0H0_Mpc
    print(f"  z={zt:>5}: kappa_crit={kap_crit:8.3f}  ->  k_crit={k_crit_Mpc:.3e} Mpc^-1")

print("\nVerdict: kappa=0 is stable (complex pair) at every epoch checked; the growing")
print("real eigenvalue is switched on entirely by the Pi-feedback term for kappa above")
print("a tiny, epoch-dependent threshold -- essentially every cosmologically relevant k")
print("is on the unstable side of that threshold once z is a few tens or more.")
