#!/usr/bin/env python3
"""
wp4a_check.py — 2026-07-16. Independent reproduction and provenance audit of
the worker's WP4a computation, with attention to whether cdot-7-era or cdot-4-
era assumptions have leaked in.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.special import zeta

KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0_MS, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
Mpc = 3.0857e22   # m
H0_si = H*100*1000/Mpc            # 1/s
c_over_H0_Mpc = C0_MS / H0_si / Mpc
print(f"c/H0 = {c_over_H0_Mpc:.2f} Mpc  (standard Hubble distance)")
rho_crit = 3*H0_si**2/(8*np.pi*G_N)
u_g0 = A_RAD*T_G0**4
OM_G = (u_g0/C0_MS**2)/rho_crit
T_NU0 = (4/11)**(1/3)*T_G0; M_NU = 1.374/3; OM_CL = 0.074
F0 = 7*np.pi**4/120
ag = np.concatenate([[0], np.logspace(-3,7,400)])
Fg = np.array([quad(lambda x,A=A: x*x*np.sqrt(x*x+A*A)/(np.exp(x)+1),0,60,limit=300)[0] for A in ag])
Fi = interp1d(np.log10(ag[1:]), np.log10(Fg[1:]), kind='cubic')
def Ffd(A):
    A = np.asarray(A,float); return np.where(A<1e-3, F0, 10**Fi(np.log10(np.maximum(A,1e-3))))
REL = (7/8)*(4/11)**(4/3)
def u_nu(z):
    A = M_NU/(K_B_EV*T_NU0*(1+z)); return 3*REL*(1+z)**4*Ffd(A)/F0
om_nu0 = float(u_nu(0.0))*u_g0/C0_MS**2/rho_crit
om_cold = OM_CL - om_nu0
Om_b = om_cold          # worker's identification: Omega_b = Omega_closure - Omega_nu^census
print(f"census: Omega_cold = {om_cold:.5f}, Omega_nu = {om_nu0:.5f}, Omega_G = {OM_G:.2e}")

def u_hat(z): return om_cold*(1+z)**3 + OM_G*(1+z)**4 + OM_G*u_nu(z)
u00 = float(u_hat(0.0))
def Ssrc(s):
    z = np.exp(-1.5*s)-1
    return (u_hat(z)/u00)*np.exp(5*s)
mu0 = X0/(1+X0)
def x_of(r,s):
    y = min(mu0*r*r*np.exp(-2*s)*float(Ssrc(s)), 1-1e-13); return y/(1-y)

# integrate the closure ODE FAR into the past (need z ~ 10^10 for r_s convergence)
sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-25.0), [1.0],
                rtol=1e-11, atol=1e-14, dense_output=True, max_step=0.01)
# grid for D_p (z from 0 to z*)
z_star = 1089.80
s_star = -np.log(1+z_star)/1.5
s_Dp = np.linspace(-1e-9, s_star, 8000)
r_Dp = sol.sol(s_Dp)[0]
x_Dp = np.array([x_of(ri,si) for ri,si in zip(r_Dp,s_Dp)])
E_Dp = np.exp(-1.5*s_Dp)*X0/(x_Dp*r_Dp)
z_Dp = np.exp(-1.5*s_Dp)-1
# D_p(z*) = int_0^z* c/(H0 E) dz    ,   dz = -1.5 e^{-1.5 s} ds = -(1+z)*1.5 ds
dz_ds = -1.5*(1+z_Dp)
Dp_star_Mpc = -cumulative_trapezoid(c_over_H0_Mpc/E_Dp * dz_ds, s_Dp, initial=0.0)[-1]
print(f"\nD_p(z*={z_star}) = {Dp_star_Mpc:.1f} Mpc   (worker: 13074.3)")

# r_s: integrate from z* to z ~ 10^10 (need to CHECK convergence carefully)
for smax in (-15, -18, -21, -24):
    s_rs = np.linspace(s_star, smax, 20000)
    r_rs = sol.sol(s_rs)[0]
    x_rs = np.array([x_of(ri,si) for ri,si in zip(r_rs,s_rs)])
    E_rs = np.exp(-1.5*s_rs)*X0/(x_rs*r_rs)
    z_rs = np.exp(-1.5*s_rs)-1
    R_bg = 3*Om_b/(4*OM_G*(1+z_rs))     # baryon-photon ratio
    cs = 1.0/np.sqrt(3*(1+R_bg))         # in units of c
    dz_ds_rs = -1.5*(1+z_rs)
    # r_s = int_{z*}^{inf} cs*c/(H0 E) dz. dz sign: z increases as s decreases (going backward).
    integrand = cs*c_over_H0_Mpc/E_rs * dz_ds_rs
    rs_val = -cumulative_trapezoid(integrand, s_rs, initial=0.0)[-1]
    zmax = np.exp(-1.5*smax)-1
    print(f"r_s to z={zmax:.1e}: {rs_val:.3f} Mpc")

# What if we use Omega_b_effective consistent with radiation-era physics?
# In cdot-8, the census defines "matter-like" but the pre-recombination FLUID
# that couples to photons is only genuinely baryonic matter, not neutrinos.
# The worker's Omega_b = 0.0442 identification assumes ALL cold matter is baryons.
# Standard LCDM Omega_b_h^2 = 0.02237 => Omega_b = 0.0456 at h=0.70.
# Very close to worker's 0.0442 — so THIS ISN'T THE PROBLEM.

# Now: what does E(z) look like at recombination compared to standard?
i_star = np.argmin(abs(z_Dp - z_star))
print(f"\nE(z*={z_star}) cdot-8 = {E_Dp[i_star]:.1f}")
# Standard LCDM at z~1100: E ~ sqrt(Omega_m (1+z)^3 + Omega_r (1+z)^4)
Om_m_lcdm = 0.315; Om_r_lcdm = 9.15e-5
E_lcdm = np.sqrt(Om_m_lcdm*(1+z_star)**3 + Om_r_lcdm*(1+z_star)**4)
print(f"E(z*={z_star}) LCDM   = {E_lcdm:.1f}")
print(f"ratio cdot-8/LCDM at recombination: {E_Dp[i_star]/E_lcdm:.4f}")

# Check E in the sound-horizon integration range (deep radiation)
for zq in (1e3, 1e4, 1e6, 1e8):
    i = np.argmin(abs(np.exp(-1.5*s_rs)-1-zq))
    E_lcdm_z = np.sqrt(Om_m_lcdm*(1+zq)**3 + Om_r_lcdm*(1+zq)**4)
    print(f"z={zq:.0e}: E_cdot8 = {E_rs[i]:.2e}, E_LCDM = {E_lcdm_z:.2e}, ratio = {E_rs[i]/E_lcdm_z:.3f}")

# Now — the key question the worker's report didn't ask:
# Is the D_p formula correct in cdot-8's own framework?
# In cdot-7 (Foundation §5.5), D_p is the "coordinate/proper" distance whose
# derivation involved the c(z) factor in the null geodesic. In standard cosmology
# D_M = c ∫ dz/H(z) — with a CONSTANT c. In a varying-c framework the null geodesic
# has ds = c(t) dt, so the coordinate distance ∫ dr = ∫ c(t) dt = ∫ c(z)/(H(z)(1+z)) dz
# (using dt/dz = -1/((1+z)H)). This gives a FACTOR of c(z) inside the integral
# that the worker's use of "c_0" (constant) doesn't carry.
# In cdot-7 with c ∝ a^{2/3} => c/c0 = (1+z)^{-2/3}, the D_p integral becomes
# int_0^z* c(z)/(H(z)(1+z)) dz — this is worker's D_p formula IF they used H_local not H_tau,
# but with H_tau (matter-frame Hubble rate) and c=c_0 constant since we're in matter frame...
# Need to check WHICH clock/frame D_p is computed in cdot-8.
