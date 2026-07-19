#!/usr/bin/env python3
"""
theta_star_diagnosis.py — 2026-07-16. Deep-dive on the WP4a 27% miss.

Part 1: LOCALIZE. Factorize the miss between Omega_b (worker's §4 attribution)
        and E(z), by swapping each into LCDM's value separately.
Part 2: SENSITIVITY. The nu-mass experiment: Sigma m_nu = {1.374 (baseline),
        0.30, 0.06} eV with cold (PBH-like, option-iii) makeup keeping
        Omega_closure = 0.074. Keeping (kl, x0) fixed — derivative probe,
        NOT a refit (flagged).
Part 3: The R/c_s check: how much does the census Omega_b actually move r_s?
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.special import zeta

KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0_MS, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
Mpc = 3.0857e22
H0_si = H*100*1000/Mpc
c_H0 = C0_MS/H0_si/Mpc
rho_crit = 3*H0_si**2/(8*np.pi*G_N)
OM_G = ((A_RAD*T_G0**4)/C0_MS**2)/rho_crit
T_NU0 = (4/11)**(1/3)*T_G0; OM_CL_TOT = 0.074
z_star = 1089.80
F0 = 7*np.pi**4/120
ag = np.concatenate([[0], np.logspace(-3,7,400)])
Fg = np.array([quad(lambda x,A=A: x*x*np.sqrt(x*x+A*A)/(np.exp(x)+1),0,60,limit=300)[0] for A in ag])
Fi = interp1d(np.log10(ag[1:]), np.log10(Fg[1:]), kind='cubic')
def Ffd(A):
    A = np.asarray(A,float); return np.where(A<1e-3, F0, 10**Fi(np.log10(np.maximum(A,1e-3))))
REL = (7/8)*(4/11)**(4/3)

def build_model(m_nu_sum):
    m_nu = m_nu_sum/3
    def u_nu(z):
        A = m_nu/(K_B_EV*T_NU0*(1+z)); return 3*REL*(1+z)**4*Ffd(A)/F0
    om_nu0 = float(u_nu(0.0))*(A_RAD*T_G0**4)/C0_MS**2/rho_crit
    om_cold = OM_CL_TOT - om_nu0      # baryons + (option-iii cold if needed)
    def u_hat(z): return om_cold*(1+z)**3 + OM_G*(1+z)**4 + OM_G*u_nu(z)
    u00 = float(u_hat(0.0))
    def Ssrc(s):
        z = np.exp(-1.5*s)-1
        return (u_hat(z)/u00)*np.exp(5*s)
    mu0 = X0/(1+X0)
    def x_of(r,s):
        y = min(mu0*r*r*np.exp(-2*s)*float(Ssrc(s)), 1-1e-13); return y/(1-y)
    sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-25.0), [1.0],
                    rtol=1e-11, atol=1e-14, dense_output=True, max_step=0.01)
    def E_of(z):
        s = -np.log(1+np.asarray(z,float))/1.5
        r = sol.sol(s)[0]
        x = np.array([x_of(ri,si) for ri,si in zip(np.atleast_1d(r),np.atleast_1d(s))])
        return (1+np.asarray(z,float))*X0/(x*np.atleast_1d(r))
    return E_of, om_cold, om_nu0

def theta_star(E_of, Om_b):
    zg1 = np.linspace(0, z_star, 6000)
    Dp = np.trapezoid(c_H0/E_of(zg1[1:]), zg1[1:]) + c_H0/E_of([1e-6])[0]*zg1[1]  # small-z sliver
    zg2 = np.logspace(np.log10(z_star), 10, 8000)
    R = 3*Om_b/(4*OM_G*(1+zg2))
    cs = 1.0/np.sqrt(3*(1+R))
    rs = np.trapezoid(cs*c_H0/E_of(zg2), zg2)
    return rs, Dp, 100*rs/Dp

def E_lcdm(z, Om_m=0.315, Om_r=9.15e-5):
    z = np.asarray(z,float)
    return np.sqrt(Om_m*(1+z)**3 + Om_r*(1+z)**4 + (1-Om_m-Om_r))

# ---------- Part 1: localize ----------
E8, om_cold, om_nu = build_model(1.374)
rs0, Dp0, th0 = theta_star(E8, om_cold)
print(f"baseline cdot-8:      r_s={rs0:6.2f}  D_p={Dp0:7.1f}  100th*={th0:.3f}")
rsL, DpL, thL = theta_star(lambda z: E_lcdm(z), 0.0493)
print(f"LCDM reference:       r_s={rsL:6.2f}  D_p={DpL:7.1f}  100th*={thL:.3f}  (Planck 1.041)")
# swap experiments
rs_a, Dp_a, th_a = theta_star(E8, 0.0493)              # cdot-8 E, LCDM Omega_b
print(f"cdot-8 E, LCDM Ob:    r_s={rs_a:6.2f}  D_p={Dp_a:7.1f}  100th*={th_a:.3f}   <- Ob lever")
rs_b, Dp_b, th_b = theta_star(lambda z: E_lcdm(z), om_cold)   # LCDM E, census Ob
print(f"LCDM E, census Ob:    r_s={rs_b:6.2f}  D_p={Dp_b:7.1f}  100th*={th_b:.3f}   <- E lever")

# ---------- Part 2: nu-mass sensitivity (derivative probe, fit NOT redone) ----------
print("\nnu-mass sensitivity (Omega_closure held at 0.074 via option-iii cold makeup;")
print("(kl,x0) held fixed — derivative probe, real change requires refit):")
for mnu in (1.374, 0.60, 0.30, 0.06):
    E_of, ocold, onu = build_model(mnu)
    rs, Dp, th = theta_star(E_of, ocold if mnu==1.374 else om_cold)  # baryons unchanged; extra cold = PBH
    Ez = E_of([z_star])[0]/E_lcdm(z_star)
    print(f"  Sum m_nu={mnu:5.2f} eV: cold-census={ocold:.4f} (nu={onu:.4f})  "
          f"E(z*)/E_LCDM={Ez:.3f}  100th*={th:.3f}")
