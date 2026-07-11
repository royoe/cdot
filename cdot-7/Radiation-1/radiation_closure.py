"""
radiation_closure.py
---------------------
cdot-7, Session 2026-07-10: first attempt at Foundation.md Sec.6 item 5
(radiation-era closure). Archived so every number in the accompanying update
document and session log can be independently re-run, not merely trusted.

Steps 1-4 are derived/verified to the project's usual standard (cross-checked at
least two independent ways). Step 5 (multi-species) is order-of-magnitude /
estimate-level and is flagged as such throughout -- see the docstrings below and
the update document.
"""
import numpy as np
from scipy.integrate import solve_ivp

# ----------------------------------------------------------------------------
# Fixed inputs, all already established elsewhere in this project (not new
# assumptions introduced in this session).
# ----------------------------------------------------------------------------
G = 6.674e-11              # m^3 kg^-1 s^-2
c0 = 2.998e8                # m/s
Mpc = 3.0857e22              # m
H0 = 70e3 / Mpc              # s^-1  (fixed throughout this project, not fit)
a_rad = 7.5657e-16           # J m^-3 K^-4 (radiation constant)
T_gamma0_K = 2.725           # K, measured CMB temperature today
kB_eV_per_K = 8.617333e-5    # eV/K

kappa_lambda = 3 / (4 * 1.72)   # from Foundation Sec.2.2's x_* = 3/(4*kappa*lambda) = 1.72
x0_today = 1.10                  # Foundation Sec.5.5/5.6: today's actual (off-fixed-point) operating point
mu = lambda x: x / (1 + x)         # simple interpolating function, joint-fit-preferred (Sec.6 item 8)
mu_inv = lambda y: y / (1 - y)


# ----------------------------------------------------------------------------
# STEP 1: coordinate-frame scaling of the radiation source term.
#   Photon number conserved in coordinate terms (new assumption, flagged,
#   symmetric to Sec.6 item 9) + E_gamma(t) = hbar*k*c(t) (Foundation Sec.3.3,
#   already established) => u_gamma(t) ~ c(t)^{+1}, rho_gamma_eff = u_gamma/c^2 ~ c(t)^{-1}.
#   Cross-checked via the coordinate<->local dictionary derived from Sec.3.1's
#   own local length (~c^-3/2) and frequency (~c^5/2) scalings: a coordinate
#   density ~c^p maps to local ~c^{p-7}. Applied here as a standalone check.
# ----------------------------------------------------------------------------
def dictionary_check():
    """Cross-check Step 1's exponents against the general coordinate->local map."""
    # radiation: coordinate exponent p=1 -> local exponent p-7=-6 -> (1+z)^4 (since c~(1+z)^-2/3)
    p_rad_local = 1 - 7
    # matter: coordinate rho_m*c^2 exponent p=5/2 -> local exponent p-7=-4.5 -> (1+z)^3
    p_mat_local = 2.5 - 7
    z_exp_rad = -p_rad_local / 1.5   # convert c-exponent to (1+z)-exponent, since c ~ (1+z)^{-2/3}
    z_exp_mat = -p_mat_local / 1.5
    assert abs(z_exp_rad - 4) < 1e-9, "expected (1+z)^4 for radiation"
    assert abs(z_exp_mat - 3) < 1e-9, "expected (1+z)^3 for matter"
    return z_exp_rad, z_exp_mat


# ----------------------------------------------------------------------------
# STEP 2: the extended closure and its two fixed points.
#   x_* = (1 - n/2) / (kappa*lambda) for a source rho ~ c^n.
#   Matter (n=+1/2) reproduces Foundation's x_*=3/(4 kappa lambda) exactly.
#   Radiation (n=-1) gives a second fixed point, exactly double.
# ----------------------------------------------------------------------------
def fixed_point(n, kl=kappa_lambda):
    p = 1 - n / 2
    return p / kl


def z_eq(Omega_closure, eta, H0_=H0):
    """Closed form: 1+z_eq = rho_0 / rho_gamma_eff(t0)."""
    rho_c0 = 3 * H0_**2 / (8 * np.pi * G)
    rho_0 = Omega_closure * rho_c0
    u_gamma0 = a_rad * T_gamma0_K**4
    rho_gamma0 = eta * u_gamma0 / c0**2
    return rho_0 / rho_gamma0, rho_0, rho_gamma0


# ----------------------------------------------------------------------------
# STEP 3: full trajectory through the crossover.
#   ODE recast in s=ln(c/c0):  dr/ds = kappa*lambda * x(r,s) * r
#   y(r,s) = r^2 [ Ym*exp(-1.5 s) + Yg*exp(-3 s) ],  x = mu_inv(y)
#   Ym, Yg normalized so that at s=0 (today), y = mu(x0_today).
# ----------------------------------------------------------------------------
def integrate_trajectory(Omega_closure, eta, s_end=-10.0, max_step=0.01):
    ratio, rho_0, rho_gamma0 = z_eq(Omega_closure, eta)
    ratio = rho_gamma0 / rho_0  # rho_gamma,0 / rho_0, dimensionless
    y0_today = mu(x0_today)
    Ym = y0_today / (1 + ratio)
    Yg = ratio * Ym

    def rhs(s, r):
        r = r[0]
        y = r**2 * (Ym * np.exp(-1.5 * s) + Yg * np.exp(-3 * s))
        y = min(y, 0.999999)
        return [kappa_lambda * mu_inv(y) * r]

    sol = solve_ivp(rhs, [0, s_end], [1.0], dense_output=True,
                     max_step=max_step, rtol=1e-9, atol=1e-12)
    return sol, Ym, Yg


def x_at_redshift(sol, Ym, Yg, z):
    chi = (1 + z)**(-2 / 3)
    s = np.log(chi)
    r = sol.sol(s)[0]
    y = min(r**2 * (Ym * np.exp(-1.5 * s) + Yg * np.exp(-3 * s)), 0.999999)
    return mu_inv(y)


# ----------------------------------------------------------------------------
# STEP 5 (order-of-magnitude only -- see update document for caveats):
#   neutrino relativistic->non-relativistic transition using this project's
#   own fitted Sigma m_nu (Foundation Sec.5.6), and the standard e+e-
#   annihilation entropy-transfer kink size.
# ----------------------------------------------------------------------------
def neutrino_transition_redshift(sigma_m_nu_eV=1.374, n_species=3):
    T_gamma0_eV = T_gamma0_K * kB_eV_per_K
    T_nu0_eV = T_gamma0_eV * (4 / 11)**(1 / 3)
    m_nu = sigma_m_nu_eV / n_species
    return m_nu / T_nu0_eV, m_nu, T_nu0_eV


def ee_annihilation_estimate():
    T_gamma0_eV = T_gamma0_K * kB_eV_per_K
    m_e_eV = 0.511e6
    one_plus_z = m_e_eV / T_gamma0_eV
    u_boost = (11 / 4)**(4 / 3)
    return one_plus_z, u_boost


if __name__ == "__main__":
    print("=== Step 1: dictionary cross-check ===")
    print(dictionary_check(), "-> (4, 3) expected\n")

    print("=== Step 2: fixed points ===")
    x_matter = fixed_point(0.5)
    x_rad = fixed_point(-1)
    print(f"x*_matter = {x_matter:.3f}  (Foundation: 1.72)")
    print(f"x*_rad    = {x_rad:.3f}  (= 2 x*_matter = {2*x_matter:.3f})\n")

    print("=== Step 2/3: z_eq and trajectories across conventions ===")
    for Om, label in [(0.074, "current"), (0.115, "SN+a0 a0-anchored"), (0.134, "SN+a0 kappa=1")]:
        for eta in (1, 2):
            zeq, rho0, rhog0 = z_eq(Om, eta)
            sol, Ym, Yg = integrate_trajectory(Om, eta)
            x_recomb = x_at_redshift(sol, Ym, Yg, 1100.0)
            print(f"  Omega_cl={Om} ({label}), eta={eta}: z_eq={zeq-1:.0f}, "
                  f"x(z=1100)={x_recomb:.3f}")

    print("\n=== Step 5: neutrino transition (this project's own fitted mass) ===")
    onepz, m_nu, T_nu0 = neutrino_transition_redshift()
    print(f"m_nu = {m_nu:.4f} eV, T_nu,0 = {T_nu0:.4e} eV, 1+z_nu,nr = {onepz:.1f}")

    print("\n=== Step 5: e+e- annihilation (standard, order-of-magnitude) ===")
    onepz_ee, boost = ee_annihilation_estimate()
    print(f"1+z ~ {onepz_ee:.2e}, u_gamma boost through transition ~ {boost:.3f}x")
