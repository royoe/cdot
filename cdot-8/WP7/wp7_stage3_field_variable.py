#!/usr/bin/env python3
"""
wp7_stage3_field_variable.py -- 2026-07-20. Stage 3: the pure
field-variable rebuild, per K2's state-variable rule and the confirmed
Stage-2 units contract (dK/dQ = -F_Q/2 in the E_alpha equation
specifically; bare F_Q only in the bulk-current term, not used here).

STATE: (delta_b, theta_b, delta_s, theta_s, alpha, E_alpha) -- 6
variables. Phi is NOT a separate ODE state: used algebraically via the
sub-horizon Poisson equation (matching sec.24's own already-validated
convention -- the momentum-constraint/superhorizon refinement is
explicitly deferred to Stage 4, where the M5/mode-exit machinery lives
anyway). chi is recovered algebraically: chi = Qbar*(theta_s+alpha)
(NO gamma needed -- theta=delta_phi/Qbar, chi=delta_phi+Qbar*alpha=
Qbar*(theta+alpha), confirmed by direct substitution).

Pi is computed via the FULL formula (not the c_ad^2*delta_s-only
approximation that broke sec.26): Pi = c_ad^2 delta_s -
c_ad^2/(8 pi Gtilde a^2 rhobar) * (-k^2/a^2)[K_B E_alpha+(2-K_B)chi]
-- in the established Omega-normalized convention (8 pi G rhobar_s ->
3 H0^2 Omega_s), this bracket-term coefficient becomes a clean,
dimensionless kappa=(k/(a H0))^2 combination.

REGRESSION CHECK (advisor-recommended): with Pi artificially forced to
0 (decoupling the vector sector), must reproduce sec.24's own Stage-1
Omega_eff growth (Phi roughly constant in the matter era) EXACTLY.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d

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
sol = solve_ivp(lambda s,r:[KL*x_of(r[0],s)*r[0]], (0,-11), [1.0],
                rtol=1e-10, atol=1e-13, dense_output=True, max_step=0.005)
s = np.linspace(-10.8, -1e-6, 16000)
r = sol.sol(s)[0]
x = np.array([x_of(ri,si) for ri,si in zip(r,s)])
E2 = (np.exp(-1.5*s)*X0/(x*r))**2
E = np.sqrt(E2)
z_arr = np.exp(-1.5*s)-1
Q_arr = np.exp(-2.5*s)
u_arr = np.array([float(u_hat(z)) for z in z_arr])
Om_s = E2 - u_arr
I = cumulative_trapezoid((Q_arr**(-2/3)*Om_s)[::-1], s[::-1], initial=0.0)[::-1]
F_arr = Q_arr**(2/3)*(-5.0*I)
F_Q = -0.4*np.exp(2.5*s)*np.gradient(F_arr, s)
Om_s_frac = Om_s/E2
Om_b = om_cold*(1+z_arr)**3/E2

w = -(1/4.5)*np.gradient(np.log(np.abs(Om_s)), s) - 1
dw_ds = np.gradient(w, s)
dlnrho_ds = np.gradient(np.log(np.abs(Om_s)), s)
cad2 = w + dw_ds/dlnrho_ds

# --- N=ln(a/a0) grid + interpolators ---
Nax = -np.log(1+z_arr)
order = np.argsort(Nax)
Nsort = Nax[order]
E2_i = interp1d(Nsort, E2[order], kind='cubic')
w_i = interp1d(Nsort, w[order], kind='linear')
cad2_i = interp1d(Nsort, cad2[order], kind='linear')
Oms_i = interp1d(Nsort, Om_s_frac[order], kind='linear')
Omb_i = interp1d(Nsort, Om_b[order], kind='linear')
Q_i = interp1d(Nsort, Q_arr[order], kind='linear')
FQ_i = interp1d(Nsort, F_Q[order], kind='linear')
lnE2 = np.log(E2[order]); dlnE2_dN = np.gradient(lnE2, Nsort)
dlnE2dN_i = interp1d(Nsort, dlnE2_dN, kind='linear')
Nmin_g, Nmax_g = Nsort[0], Nsort[-1]

def rhs(N, y, kappa):
    """kappa = (k/(a H0))^2, the established dimensionless gradient measure."""
    N = min(max(N, Nmin_g), Nmax_g)
    delta_b, theta_b, delta_s, theta_s, alpha, Ealpha = y
    Ev2 = float(E2_i(N)); Hc = np.sqrt(Ev2)
    dlnE_dN = 0.5*float(dlnE2dN_i(N))
    Omb = float(Omb_i(N)); Oms = float(Oms_i(N))
    wv = float(w_i(N)); cad2v = float(cad2_i(N))
    Qb = float(Q_i(N)); FQv = float(FQ_i(N))
    dKdQ = -0.5*FQv                       # Stage-2 Contract Line 2: NOT bare F_Q
    a = np.exp(N)

    # Phi: sub-horizon Poisson (algebraic), matching sec.24's own convention
    Phi = -1.5*(Omb*delta_b + Oms*delta_s)/kappa
    Psi = Phi

    chi = Qb*(theta_s + alpha)
    bracket = K_B*Ealpha + (2-K_B)*chi
    Pi = cad2v*delta_s - cad2v*(-kappa)*bracket   # (-k^2/a^2)->(-kappa H0^2), H0^2 absorbed in Omega convention

    # Phi' needed for delta's/delta_b's own 3 Phi' source term -- since Phi is
    # algebraic in delta_b,delta_s, use the quasi-static approximation Phi'~0
    # relative to the k^2 theta term (standard sub-horizon growth-equation
    # practice; consistent with sec.24's own level of approximation).
    dPhi_dN = 0.0

    ddb = 3*dPhi_dN - kappa*theta_b/Hc
    dtb = Psi/Hc
    dds = 3*(wv*delta_s - Pi) + (1+wv)*(3*dPhi_dN - kappa*theta_s/Hc)
    dts = 3*cad2v*theta_s + (Pi/(1+wv) + Psi)/Hc
    dalpha = (Ealpha - Psi)/Hc
    dEalpha = ( dKdQ*chi - (2-K_B)*( Qb/(1+wv)*Pi + (Hc+Qb)*chi - 3*cad2v*Hc*Qb*alpha ) )/(K_B*Hc) - Ealpha
    return [ddb, dtb, dds, dts, dalpha, dEalpha]

zstart = 100.0
N_start = Nsort[np.argmin(np.abs(z_arr-zstart))]
N_end = Nsort[-1]
Ngrid = np.linspace(N_start, N_end, 3000)
d0 = np.exp(N_start)
y0 = [d0, d0, d0, d0, 0.0, 0.0]

print("=== REGRESSION CHECK: Pi forced to 0 (vector sector decoupled) ===")
def rhs_nopi(N, y, kappa):
    N = min(max(N, Nmin_g), Nmax_g)
    delta_b, theta_b, delta_s, theta_s, alpha, Ealpha = y
    Ev2 = float(E2_i(N)); Hc = np.sqrt(Ev2)
    Omb = float(Omb_i(N)); Oms = float(Oms_i(N))
    wv = float(w_i(N))
    Phi = -1.5*(Omb*delta_b + Oms*delta_s)/kappa
    Psi = Phi
    ddb = -kappa*theta_b/Hc
    dtb = Psi/Hc
    dds = 3*wv*delta_s + (1+wv)*(-kappa*theta_s/Hc)
    dts = Psi/Hc
    return [ddb, dtb, dds, dts, 0.0, 0.0]

kappa_test = 1e-6   # very large scale, kappa small, so Phi doesn't blow up
sol_nopi = solve_ivp(rhs_nopi, (N_start,N_end), y0, args=(kappa_test,), t_eval=Ngrid,
                      rtol=1e-9, atol=1e-13, method='RK45')
delta_b, theta_b, delta_s, theta_s = sol_nopi.y[:4]
Ev2_g = E2_i(np.clip(Ngrid,Nmin_g,Nmax_g))
Omb_g = Omb_i(np.clip(Ngrid,Nmin_g,Nmax_g)); Oms_g = Oms_i(np.clip(Ngrid,Nmin_g,Nmax_g))
Phi_check = -1.5*(Omb_g*delta_b+Oms_g*delta_s)/kappa_test
Phi_check /= Phi_check[0]
zg = np.exp(-Ngrid)-1
for zt in [100,50,30,10,5,2,1,0.5,0.2,0.0]:
    i = np.argmin(np.abs(zg-zt))
    print(f"  z={zt:>5}: Phi/Phi_i={Phi_check[i]:.4f}  (sec.24 comparison: should be ~0.94-1.01 through matter era, then evolve at low z)")

print("\n=== STAGE 3: full system, Pi via full formula, k=1e-3 1/Mpc ===")
c0H0_Mpc = C0/1000/(100*H)
k_Mpc = 1e-4
a_at_Nstart = np.exp(N_start)
kappa = (k_Mpc*c0H0_Mpc)**2 / a_at_Nstart**2 * a_at_Nstart**2  # kappa=(k/(aH0))^2 in a0=1 units -> (k c0/H0)^2/a^2, computed per-N below properly
def rhs_kappa_of_N(N, y):
    a = np.exp(N)
    kap = (k_Mpc*c0H0_Mpc/a)**2
    return rhs(N, y, kap)
sol3 = solve_ivp(rhs_kappa_of_N, (N_start,N_end), y0, t_eval=Ngrid,
                  rtol=1e-8, atol=1e-12, method='Radau', max_step=0.01)
if not sol3.success:
    print("FAILED:", sol3.message)
else:
    delta_b, theta_b, delta_s, theta_s, alpha, Ealpha = sol3.y
    for zt in [100,50,30,10,5,2,1,0.5,0.2,0.0]:
        i = np.argmin(np.abs(zg-zt))
        print(f"  z={zt:>5}: delta_b={delta_b[i]:.4e}  delta_s={delta_s[i]:.4e}  alpha={alpha[i]:.3e}  Ealpha={Ealpha[i]:.3e}")
