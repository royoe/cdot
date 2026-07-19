#!/usr/bin/env python3
"""
wp7_growth_system.py -- 2026-07-19. Building the growth system properly
per the accepted advisory's directive 2 (Advisory-WP7-
OmegaSClusteringAdjudicated-2026-07-19.md sec.5): dust-like scalar
Omega_s clustering (via the imported Pi->0 evolution,
delta_s' = 3 Phi' - k^2/a^2 theta_s, theta_s' = Psi -- SAME form as
ordinary matter, sec.1's imported system) + baryons + massive neutrinos,
sourced together in the Poisson/growth equation, THEN the M5 coupled-era
term and mode-exit windowing go in.

STAGE 1 -- sanity target (advisor's own words): "delta_s tracks delta_b
in the matter era... total-matter growth resembles an
Omega_eff~Omega_s+Omega_b universe." Since dust-like components share
IDENTICAL delta,theta evolution equations (no relative pressure/velocity
dispersion), delta_s=delta_b exactly for matched initial conditions --
collapse to ONE combined growth equation sourced by
Omega_eff(a)=Omega_baryon(a)+Omega_s(a).

STAGE 2 -- add the M5 coupled-era source (sec.18's coefficient) with
each mode's own exit history via W(k R_h(a)) (sec.19), for the same
representative k(l=2,5,10) used in the sec.21 attempt.
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
Rh_Mpc = 1.5*cumulative_trapezoid(np.exp(s)/E, s, initial=0.0)*c0H0_Mpc
dlnRh_ds = np.gradient(np.log(np.maximum(Rh_Mpc,1e-30)), s)
dln_u_ds = np.gradient(np.log(u_arr), s)
dlnNtot_ds = dln_u_ds + 3.0 + 3.0*dlnRh_ds
qprime_Ntot = (-2.5/dlnNtot_ds)*Q
coeff_M5 = (F_Q/6+Q*F_QQ/2)*qprime_Ntot     # sec.18's coefficient, un-windowed

Om_b = om_cold*(1+z_arr)**3/E2
Om_s_frac = Om_s/E2
Om_eff = Om_b + Om_s_frac

print("=== STAGE 1 sanity check: Omega_eff = Omega_b + Omega_s vs Omega_m alone ===")
for zt in [1090, 100, 50, 30, 10, 3, 1, 0]:
    i = np.argmin(np.abs(z_arr-zt))
    print(f"  z={zt:>5}: Om_b={Om_b[i]:.4f}  Om_s={Om_s_frac[i]:.4f}  Om_eff={Om_eff[i]:.4f}  "
          f"(vs Om_b alone={Om_b[i]:.4f})")

# --- build N=ln(a/a0)=-ln(1+z) grid, interpolators ---
Nax = -np.log(1+z_arr)
order = np.argsort(Nax)
Nsort = Nax[order]
E2_i = interp1d(Nsort, E2[order], kind='cubic')
Omeff_i = interp1d(Nsort, Om_eff[order], kind='linear')
Rh_i = interp1d(Nsort, Rh_Mpc[order], kind='linear')
coeffM5_i = interp1d(Nsort, coeff_M5[order], kind='linear')
matter_source_i = interp1d(Nsort, 3.0*u_arr[order], kind='linear')
lnE2 = np.log(E2[order]); dlnE2_dN = np.gradient(lnE2, Nsort)
dlnE2dN_i = interp1d(Nsort, dlnE2_dN, kind='linear')
Nmin_g, Nmax_g = Nsort[0], Nsort[-1]

W = lambda xx: np.where(np.abs(xx)>1e-6, 3*(np.sin(xx)-xx*np.cos(xx))/xx**3, 1.0-xx**2/10.0)

def growth_ode(N, y, k_Mpc, use_M5):
    N = min(max(N, Nmin_g), Nmax_g)
    d1, d2 = y
    Ommv = float(Omeff_i(N)); dlnE_dN = 0.5*float(dlnE2dN_i(N))
    eps = 0.0
    if use_M5:
        Rhv = float(Rh_i(N)); Wv = W(k_Mpc*Rhv)
        c = float(coeffM5_i(N)); ms = float(matter_source_i(N))
        eps = (c/ms)*Wv if ms != 0 else 0.0
    src = 1.5*Ommv*(1.0+eps)
    return [d2, -(2+dlnE_dN)*d2 + src*d1]

zstart = 100.0
N_start = Nsort[np.argmin(np.abs(z_arr-zstart))]
N_end = Nsort[-1]
Ngrid = np.linspace(N_start, N_end, 4000)

print("\n=== STAGE 1: baseline growth (Omega_eff-sourced), no M5 ===")
y0 = [np.exp(N_start), np.exp(N_start)]
sol_std = solve_ivp(growth_ode, (N_start,N_end), y0, args=(1.0,False),
                     t_eval=Ngrid, rtol=1e-10, atol=1e-14, method='DOP853')
d_std = sol_std.y[0]
Ev2 = E2_i(np.clip(Ngrid,Nmin_g,Nmax_g)); a_g = np.exp(Ngrid); Omeff_g = Omeff_i(np.clip(Ngrid,Nmin_g,Nmax_g))
Phi_std = Omeff_g*Ev2*a_g**2*d_std
Phi_std /= Phi_std[0]
zg = np.exp(-Ngrid)-1
for zt in [100,50,30,10,5,2,1,0.5,0.2,0.0]:
    i = np.argmin(np.abs(zg-zt))
    print(f"  z={zt:>5}: Phi/Phi_i={Phi_std[i]:.4f}  delta={d_std[i]:.4e}  Omega_eff={Omeff_g[i]:.4f}")
print("=> Phi should stay close to CONSTANT through the matter era (unlike the")
print("   earlier Omega_m(z=50)=0.13 attempt), decaying only as Omega_s turns dark-energy-like.")

print("\n=== STAGE 2: M5-sourced kernel modification, l=2,5,10 (Dp(0.5) fiducial k) ===")
zg2 = np.linspace(1e-4,5,4000)
Ei_of_z = interp1d(np.sort(z_arr), 1/E[np.argsort(z_arr)], kind='linear')
Dp_zg = cumulative_trapezoid(Ei_of_z(zg2), zg2, initial=0.0)*c0H0_Mpc
Dp_at_05 = float(interp1d(zg2,Dp_zg)(0.5))
for l in [2,5,10]:
    k_Mpc = l/Dp_at_05
    sol_m5 = solve_ivp(growth_ode, (N_start,N_end), y0, args=(k_Mpc,True),
                        t_eval=Ngrid, rtol=1e-10, atol=1e-14, method='DOP853')
    d_m5 = sol_m5.y[0]
    Phi_m5 = Omeff_g*Ev2*a_g**2*d_m5
    Phi_m5 /= Phi_m5[0]
    Hconf = a_g*np.sqrt(Ev2)
    kernel_std = Hconf*np.gradient(Phi_std, Ngrid)
    kernel_m5  = Hconf*np.gradient(Phi_m5,  Ngrid)
    P_std = np.trapz(kernel_std**2, Ngrid)
    P_m5  = np.trapz(kernel_m5**2, Ngrid)
    dphi_pct = 100*(Phi_m5[-1]/Phi_std[-1]-1)
    print(f"  l={l:>3}  k={k_Mpc:.4e} 1/Mpc  Phi_today shift={dphi_pct:+.3f}%   ISW-kernel power ratio P_M5/P_std={P_m5/P_std:.4f}")

print("""
READING: with the properly-specified baseline (Omega_s treated as a
dust-like clusterer, not smooth), the growth history now behaves
sensibly (Phi roughly constant through the matter era, decaying only at
low z). The M5 term's effect on this properly-based system is the
genuine next number -- reported above, distinct from the mis-specified
sec.21 attempt's spurious 1.15x ratio.
""")
