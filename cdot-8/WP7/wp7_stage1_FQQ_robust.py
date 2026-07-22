#!/usr/bin/env python3
"""
wp7_stage1_FQQ_extended.py -- extending the ODE integration slightly
past s=0 (into the mathematical future, z<0) so that s=0 (today, z=0)
becomes a genuine INTERIOR point with data on both sides, rather than
the literal edge of the solved domain -- removing the boundary-artifact
ambiguity found in wp7_stage1_FQQ_robust.py (old vs new F_QQ(0)
disagreeing in SIGN: -0.696 vs +0.43).
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d, UnivariateSpline

KL, X0, H = 0.4355, 1.10, 0.70
T_G0, A_RAD, C0, G_N = 2.7255, 7.565723e-16, 2.99792458e8, 6.67430e-11
K_B_EV = 8.617333e-5
K_B = 0.4355
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
# EXTEND the integration span to s=+0.5 (mathematical future, z<0) so
# that s=0 is an interior point, not the domain edge. Initial condition
# r(0)=1 still applies AT s=0; integrate BOTH forward (0 -> 0.5) and
# backward (0 -> -11) from there.
sol_back = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-11), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
sol_fwd  = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,0.5), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)

s_back = np.linspace(-10.8, -1e-6, 16000)
s_fwd  = np.linspace(1e-6, 0.5, 2000)
s = np.concatenate([s_back, [0.0], s_fwd])
r = np.concatenate([sol_back.sol(s_back)[0], [1.0], sol_fwd.sol(s_fwd)[0]])

x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
E2 = (np.exp(-1.5*s)*X0/(x*r))**2
z_arr = np.exp(-1.5*s)-1
u_arr = np.array([float(u_hat(z)) for z in z_arr])
Om_s = E2 - u_arr
Q = np.exp(-2.5*s)
# integrate from the deep past (s_back[0]) forward to build I(s) over the WHOLE extended range
I = cumulative_trapezoid((Q**(-2/3)*Om_s)[::-1], s[::-1], initial=0.0)[::-1]
F = Q**(2/3)*(-5.0*I)

i0 = len(s_back)  # index of s=0 exactly
print(f"z at index i0: {z_arr[i0]:.6e} (should be 0)")

spl = UnivariateSpline(s, Om_s, k=4, s=1e-6*len(s))
dOms_ds = spl.derivative()(s)
F_Q_new  = (2.0/3.0)*(F/Q) + 2.0*(Om_s/Q)
F_QQ_new = -(2.0/9.0)*(F/Q**2) - (2.0/3.0)*(Om_s/Q**2) - (4.0/5.0)*(dOms_ds/Q**2)

# also a plain centered finite difference on F_Q directly, now that s=0 is interior
F_QQ_centered = np.gradient(F_Q_new, s) * (-0.4*np.exp(2.5*s))

print("\n=== F_QQ(z) near today, now with s=0 as a genuine interior point ===")
for zt in [1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.0, -0.01, -0.05]:
    i = np.argmin(np.abs(z_arr-zt))
    print(f"  z={zt:>6}: F_QQ(analytic,new)={F_QQ_new[i]:>9.4f}   F_QQ(centered-FD)={F_QQ_centered[i]:>9.4f}")

print(f"\nAt the exact s=0 index: F_QQ(analytic)={F_QQ_new[i0]:.4f}, F_QQ(centered-FD)={F_QQ_centered[i0]:.4f}")
print(f"Established (old, double-FD, boundary-only) anchor: -0.696")

mu2_over_H2 = -Q**2*F_QQ_new/(2*(2-K_B)*E2)
print(f"\n=== mu^2/H^2 with the extended, interior-point F_QQ ===")
for zt in [3,1,0.5,0.2,0.1,0.05,0.0]:
    i = np.argmin(np.abs(z_arr-zt))
    print(f"  z={zt:>6}: mu^2/H^2 = {mu2_over_H2[i]:+.4f}")
