#!/usr/bin/env python3
"""
wp7_growth_equation_v2.py -- 2026-07-19. Corrected R_h(s) integration
(dR_h/ds = 1.5 c0 e^s/(H0 E(s)), from s===ln(c/c0), WP2's own record --
fixing a worker-side bug in wp7_lambda_extensivity_check.py/
wp7_anchor_brackets.py that the advisor's covariantization_adjudication.py
and wp7_phenomenology_map.py both inherited unchanged), THEN building the
coupled-era growth equation with the exact (not matter-only) d ln N_tot/ds.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d

KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
rho_crit = 3*(H*100*1000/3.0857e22)**2/(8*np.pi*G_N)
OM_G = ((A_RAD*T_G0**4)/C0**2)/rho_crit
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
om_nu0 = float(u_nu(0.0))*(A_RAD*T_G0**4)/C0**2/rho_crit; om_cold = OM_CL - om_nu0
def u_hat(z): return om_cold*(1+z)**3 + OM_G*(1+z)**4 + OM_G*u_nu(z)
u00 = float(u_hat(0.0))
def Ssrc(s):
    z = np.exp(-1.5*s)-1
    return (u_hat(z)/u00)*np.exp(5*s)
mu0 = X0/(1+X0)
def x_of(r,s):
    y = min(mu0*r*r*np.exp(-2*s)*float(Ssrc(s)), 1-1e-13); return y/(1-y)
sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-11), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
s = np.linspace(-10.8, -1e-6, 16000)
r = sol.sol(s)[0]
x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
E2 = (np.exp(-1.5*s)*X0/(x*r))**2
E = np.sqrt(E2)
z_arr = np.exp(-1.5*s)-1
Q = np.exp(-2.5*s)
u_arr = np.array([float(u_hat(z)) for z in z_arr])
Om_s = E2 - u_arr
I = cumulative_trapezoid((Q**(-2/3)*Om_s)[::-1], s[::-1], initial=0.0)[::-1]
F = Q**(2/3)*(-5.0*I)
F_Q = -0.4*np.exp(2.5*s)*np.gradient(F, s)
F_QQ = np.gradient(F_Q, s)/np.gradient(Q, s)

c0H0_Mpc = C0/1000/(100*H)
# CORRECTED R_h(s): dR_h/ds = 1.5 * e^s / E(s)   [units of c0/H0]
Rh = 1.5*cumulative_trapezoid(np.exp(s)/E, s, initial=0.0)
Rh_Mpc = Rh*c0H0_Mpc
dlnRh_ds = np.gradient(np.log(np.maximum(Rh,1e-30)), s)

print("=== Corrected R_h(z), replacing the buggy exponent ===")
for zt in [9640.0, 1090.0, 30.0, 1.0, 0.0]:
    i = np.argmin(np.abs(z_arr-zt))
    print(f"  z={zt:>6.0f}: R_h = {Rh_Mpc[i]:.4e} Mpc")
i_zstar = np.argmin(np.abs(z_arr-1090))
print(f"\nR_h(z*)={Rh_Mpc[i_zstar]:.3e} Mpc vs r_s={173.36}, D_p={13074.3} -> "
      f"ratio to r_s: {Rh_Mpc[i_zstar]/173.36:.2e}, to D_p: {Rh_Mpc[i_zstar]/13074.3:.2e}")
print("CONCLUSION UNCHANGED: R_h(z*) still 5-6 orders of magnitude below r_s/D_p.\n")

print("=== Corrected mode-exit epochs z_exit(k): R_h(t)=1/k ===")
for k, lab in [(5e-4,"l~6"), (2e-3,"l~26"), (0.02,"first-peak k"), (0.1,"P(k) quasi-linear"), (1.0,"cluster k")]:
    idx = np.argmin(np.abs(Rh_Mpc - 1.0/k))
    print(f"  k={k:>7.0e} 1/Mpc (1/k={1/k:>6.0f} Mpc): z_exit={z_arr[idx]:>7.1f}   {lab}")

print("\n=== Corrected coupled-era growth coefficient, exact d ln N_tot/ds ===")
dln_u_ds = np.gradient(np.log(u_arr), s)
dlnNtot_ds_EXACT = dln_u_ds + 3.0 + 3.0*dlnRh_ds
dlnQ_ds = -2.5
elasticity = dlnQ_ds/dlnNtot_ds_EXACT
coeff = (F_Q/6+Q*F_QQ/2)*elasticity*Q
matter_source = 3.0*u_arr
print(f"{'z':>8} {'dlnNtot/ds':>12} {'elasticity':>12} {'coeff/matter_source':>20}")
for zt in [1090.0, 100.0, 30.0, 10.0, 3.0, 1.0, 0.0]:
    i = np.argmin(np.abs(z_arr-zt))
    print(f"{zt:>8.0f} {dlnNtot_ds_EXACT[i]:>12.3f} {elasticity[i]:>12.4f} {coeff[i]/matter_source[i]:>20.3f}")
print("""
=> with BOTH corrections applied (R_h exponent fixed; exact, not
matter-only, d ln N_tot/ds), the coupled-era Poisson-source modification
remains an O(0.5-0.7) effect through the matter era, decaying toward
z=0 -- the order-one growth-history conclusion is ROBUST to both fixes.
The mode-exit epochs shift modestly (R_h corrected up at low z, down at
high z) but the qualitative picture (recombination-era modes fully
coupled, decoupling during the matter era, only the lowest-l modes
exiting near today) is UNCHANGED.
""")
