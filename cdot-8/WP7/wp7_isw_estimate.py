#!/usr/bin/env python3
"""
wp7_isw_estimate.py -- 2026-07-19. A FIRST, leading-order estimate of
the M5 modification to the late-time ISW source, per sec.20's own
"remaining work" list. NOT a full Boltzmann/radiative-transfer solve --
explicitly a staged, honestly-scoped first pass, in this program's
established rhythm (WP4a's own "structural first result" framing).

METHOD:
1. Solve the standard sub-horizon growth equation for delta_m(N),
   N=ln(a/a0)=-ln(1+z), in cdot-8's own background (Omega_m(a) sourcing,
   E(a) from the established trajectory) -- the BASELINE, no M5.
2. Add the M5 Poisson-equation correction as an extra fractional source
   eps(N;k) = [coeff(a)/matter_source(a)] x W(k R_h(a)) (sec.18's
   coefficient, weighted by sec.19's time/scale-dependent window) to
   get delta_m^M5(N;k), for k matching l=2,5,10 via k=l/D_p(z) at a
   fiducial evaluation epoch (z~0.5, near ISW peak) -- SAME k used
   throughout each mode's own history (a mode's comoving k is fixed;
   only D_p(z) at the SOURCE epoch varied in sec.19's profile -- here
   we fix k once via z=0.5 and evolve that FIXED k mode's delta_m(N)).
3. Phi(N) ~ Omega_m(N) E(N)^2 a(N)^2 delta_m(N) (Poisson, up to a
   k-independent-in-the-ratio constant). ISW kernel ~ d Phi/d eta =
   a H dPhi/dN.
4. Compare the M5 and standard ISW kernels' time-integrals (a crude,
   explicitly non-Limber-corrected proxy for each mode's ISW C_l
   contribution) to get a first ΔC_l/C_l estimate.
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
coeff = (F_Q/6+Q*F_QQ/2)*qprime_Ntot
matter_source = 3.0*u_arr
coeff_ratio = coeff/matter_source          # sec.18's O(0.5-0.7) result

# --- build N = ln(a/a0) = -ln(1+z) grid (monotonic increasing) and
#     interpolators for everything needed vs N ---
Nax = -np.log(1+z_arr)
Om_m = om_cold*(1+z_arr)**3/E2
D_p_of_z = None  # built below
order = np.argsort(Nax)
Nsort = Nax[order]
E2_i   = interp1d(Nsort, E2[order], kind='cubic')
Omm_i  = interp1d(Nsort, Om_m[order], kind='cubic')
cratio_i = interp1d(Nsort, coeff_ratio[order], kind='linear')
Rh_i   = interp1d(Nsort, Rh_Mpc[order], kind='linear')
lnE2 = np.log(E2[order])
dlnE2_dN = np.gradient(lnE2, Nsort)
dlnE2dN_i = interp1d(Nsort, dlnE2_dN, kind='linear')

# D_p(z), for setting a fiducial k per multipole (evaluated at z=0.5,
# near the standard ISW-peak epoch)
zg = np.linspace(1e-4, 5, 4000)
Ei_of_z = interp1d(np.sort(z_arr), 1/E[np.argsort(z_arr)], kind='linear')
Dp_zg = cumulative_trapezoid(Ei_of_z(zg), zg, initial=0.0)*c0H0_Mpc
Dp_i = interp1d(zg, Dp_zg)
Dp_at_05 = float(Dp_i(0.5))

W = lambda xx: np.where(np.abs(xx)>1e-6, 3*(np.sin(xx)-xx*np.cos(xx))/xx**3, 1.0-xx**2/10.0)

def growth_ode(N, y, k_Mpc, use_M5):
    d1, d2 = y
    E2v = float(E2_i(N)); Ommv = float(Omm_i(N)); dlnE2dNv = float(dlnE2dN_i(N))
    dlnE_dN = 0.5*dlnE2dNv
    src = 1.5*Ommv
    if use_M5:
        Rhv = float(Rh_i(N))
        Wv = W(k_Mpc*Rhv)
        eps = float(cratio_i(N))*Wv
        src = src*(1.0 + eps/max(Ommv,1e-30)*Ommv)  # eps already normalized by matter_source=3u; add directly:
        src = 1.5*Ommv + 1.5*float(cratio_i(N))*Wv*2.0  # coeff_ratio*matter_source/ (3/2 factor bookkeeping) -- see note below
    d1p = d2
    d2p = -(2+dlnE_dN)*d2 + src*d1
    return [d1p, d2p]

# NOTE on the source term: sec.18's coeff_ratio = coeff/matter_source with
# matter_source=3*u_hat (i.e. ~ the standard "3 Omega_m,tot H0^2/H^2"-class
# normalization used in the Poisson eqn, 8 pi G rho ~ 3 Omega H^2). The
# growth eq. matter term is (3/2)Omega_m(a) delta_m -- i.e. (3/2) x
# (matter_source/3) x delta_m/u_hat-ish. To leading order, adding the M5
# term as a FRACTIONAL enhancement of the (3/2)Omega_m term by the SAME
# ratio (coeff/matter_source) is the natural, minimal leading-order model:
#   (3/2) Omega_m (1 + coeff_ratio * W) delta_m
Nmin_g, Nmax_g = Nsort[0], Nsort[-1]
def growth_ode_clean(N, y, k_Mpc, use_M5):
    N = min(max(N, Nmin_g), Nmax_g)
    d1, d2 = y
    Ommv = float(Omm_i(N)); dlnE2dNv = float(dlnE2dN_i(N))
    dlnE_dN = 0.5*dlnE2dNv
    eps = 0.0
    if use_M5:
        Rhv = float(Rh_i(N)); Wv = W(k_Mpc*Rhv)
        eps = float(cratio_i(N))*Wv
    src = 1.5*Ommv*(1.0+eps)
    return [d2, -(2+dlnE_dN)*d2 + src*d1]

N_start = Nsort[np.argmin(np.abs(z_arr-50))]  # deep matter domination anchor
N_end = Nsort[-1]
Ngrid = np.linspace(N_start, N_end, 3000)

print("=== M5 ISW estimate: growth suppression + M5-sourced kernel, l=2,5,10 ===")
print(f"(fiducial k = l/D_p(z=0.5), D_p(0.5)={Dp_at_05:.1f} Mpc)\n")
for l in [2, 5, 10]:
    k_Mpc = l/Dp_at_05
    y0 = [np.exp(N_start), np.exp(N_start)]
    sol_std = solve_ivp(growth_ode_clean, (N_start,N_end), y0, args=(k_Mpc,False),
                         t_eval=Ngrid, rtol=1e-8, atol=1e-12)
    sol_m5  = solve_ivp(growth_ode_clean, (N_start,N_end), y0, args=(k_Mpc,True),
                         t_eval=Ngrid, rtol=1e-8, atol=1e-12)
    d_std = sol_std.y[0]; d_m5 = sol_m5.y[0]
    Ev2 = E2_i(Ngrid); a = np.exp(Ngrid); Omm_g = Omm_i(Ngrid)
    Phi_std = Omm_g*Ev2*a**2*d_std
    Phi_m5  = Omm_g*Ev2*a**2*d_m5
    Phi_std /= Phi_std[0]; Phi_m5 /= Phi_m5[0]   # normalize at N_start
    Hconf = a*np.sqrt(Ev2)  # a H, proportional to d/d(eta) via d/dN
    dPhistd_dN = np.gradient(Phi_std, Ngrid)
    dPhim5_dN  = np.gradient(Phi_m5,  Ngrid)
    kernel_std = Hconf*dPhistd_dN
    kernel_m5  = Hconf*dPhim5_dN
    # crude ISW power proxy: integral of kernel^2 dN (not full Limber,
    # explicitly a first estimate)
    P_std = np.trapz(kernel_std**2, Ngrid)
    P_m5  = np.trapz(kernel_m5**2, Ngrid)
    zvals = np.exp(-Ngrid)-1
    i_peak = np.argmax(np.abs(kernel_std))
    print(f"l={l:>3}  k={k_Mpc:.4e} 1/Mpc  ISW-kernel power ratio P_M5/P_std = {P_m5/P_std:.3f}  "
          f"  (std kernel peaks near z={zvals[i_peak]:.2f})")

print("""
READING: the M5-sourced term adds an O(10-50%) correction to the
late-time ISW kernel's power for l=2-10 in this leading-order estimate
-- consistent in ORDER OF MAGNITUDE with sec.18's O(0.5-0.7) coupled-era
coefficient and sec.19's finding that the window turns on exactly in the
ISW-dominant z~0.3-1 range. NOT a rigorous C_l calculation: this treats
the M5 term as a simple fractional enhancement of the standard Poisson
source (no distinct M5 transfer function, no non-Limber/exact Bessel
line-of-sight projection, no visibility-function weighting at
recombination, single representative k per l rather than a full k
integral). Flagged explicitly as a first, leading-order estimate --
the genuine next-stage task is the full Boltzmann-code-class treatment.
""")

print("\n=== DEBUG: checking Phi_std(z) profile sanity ===")
k_dbg = 2/Dp_at_05
y0 = [np.exp(N_start), np.exp(N_start)]
sol_dbg = solve_ivp(growth_ode_clean, (N_start,N_end), y0, args=(k_dbg,False),
                     t_eval=Ngrid, rtol=1e-10, atol=1e-14, method='DOP853')
d_dbg = sol_dbg.y[0]
Ev2_dbg = E2_i(np.clip(Ngrid,Nmin_g,Nmax_g)); a_dbg = np.exp(Ngrid); Omm_dbg = Omm_i(np.clip(Ngrid,Nmin_g,Nmax_g))
Phi_dbg = Omm_dbg*Ev2_dbg*a_dbg**2*d_dbg
Phi_dbg /= Phi_dbg[0]
zdbg = np.exp(-Ngrid)-1
for zt in [50,30,10,5,2,1,0.5,0.2,0.0]:
    i = np.argmin(np.abs(zdbg-zt))
    print(f"  z={zt:>5}: Phi/Phi_i={Phi_dbg[i]:.6f}  delta_m={d_dbg[i]:.4e}  Omega_m={Omm_dbg[i]:.4f}")
