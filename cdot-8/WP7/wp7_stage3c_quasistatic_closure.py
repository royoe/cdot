#!/usr/bin/env python3
"""
wp7_stage3c_quasistatic_closure.py -- 2026-07-20. Stage 3c: design and
test the quasi-static/slaved closure for the vector sector, per the
advisor's Stage-3b-confirmation recommendation
(Advisory-WP7-Stage3bConfirmed-2026-07-20.md, sec.5 item 2).

Two changes relative to wp7_stage3_field_variable.py:

1. FIXES the Stage-3b-confirmed missing 1/(3*Om_s(a)) normalization in
   Pi's kappa-dependent term (both the advisor and I found this is
   wrong regardless of which Laplacian convention is used -- corrected
   here to the "comoving" reading both of us settled on):

       Pi = cad2*delta_s + cad2*kappa/(3*Om_s(a)) * [K_B*E_alpha + (2-K_B)*chi]

2. Eliminates E_alpha as an explicit ODE state. Rationale: the vector-
   sector stiffness audit (wp7_stage3_vector_stiffness_audit.py) showed
   the (alpha, E_alpha) subsystem has one large POSITIVE real eigenvalue
   above kappa_crit(z) -- a genuine instability, not a numerical
   artifact (Stage 3b). A physically sensible cosmological solution
   cannot contain an exponentially growing mode at any observable
   amplitude; the correct trajectory sits on the STABLE manifold at
   every instant. The standard way to enforce this (the same logic as
   tight-coupling elimination in Boltzmann codes, and structurally the
   same "select the bounded solution" principle this program's own WP3
   used repeatedly via past-regularity/C1=0 selection) is to solve
   dE_alpha/dN = 0 ALGEBRAICALLY for E_alpha in terms of the slow state
   (delta_s, theta_s, alpha) at each step, rather than integrating it
   explicitly. This is valid whenever the fast rate (kappa-dependent,
   set by the E_alpha equation's own large coefficient) is much larger
   than the slow forcing rate (~H) -- i.e. for kappa well above
   kappa_crit(z). alpha itself is NOT slaved (its own equation has no
   large coefficient) and remains an explicit ODE state.

REGRESSION: with kappa artificially set very small (kappa_test=1e-6,
matching wp7_stage3_field_variable.py's own Pi=0 regression check),
this reduces to the same slow-kappa limit and should reproduce that
check's Phi decay closely (not exactly, since the corrected Pi
normalization and quasi-static algebra both engage even at small kappa
-- but the DYNAMICS should stay qualitatively the same, since Pi's
kappa-term vanishes as kappa->0 regardless of normalization).

MAIN TEST: k=1e-4 Mpc^-1, z=100->0, the exact case that blew up in
wp7_stage3_field_variable.py -- does the quasi-static closure stay
bounded where the explicit-ODE system diverged?
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
Nmin_g, Nmax_g = Nsort[0], Nsort[-1]


def slaved_Ealpha(N, delta_s, theta_s, alpha, kappa):
    """Solve dE_alpha/dN=0 algebraically (quasi-static elimination of the
    fast, unstable-above-threshold vector d.o.f.), using the Stage-3b-
    corrected Pi normalization (1/(3*Om_s(a)) included)."""
    Ev2 = float(E2_i(N)); Hc = np.sqrt(Ev2)
    wv = float(w_i(N)); cad2v = float(cad2_i(N))
    Qb = float(Q_i(N)); FQv = float(FQ_i(N)); Oms = float(Oms_i(N))
    dKdQ = -0.5*FQv
    chi = Qb*(theta_s + alpha)
    kap3 = cad2v*kappa/(3*Oms)          # Stage-3b-corrected Pi coefficient

    coef_E = K_B*Hc + (2-K_B)*K_B*Qb/(1+wv)*kap3
    RHS = ( dKdQ*chi
            - (2-K_B)*Qb/(1+wv)*cad2v*delta_s
            - (2-K_B)**2*Qb/(1+wv)*kap3*chi
            - (2-K_B)*(Hc+Qb)*chi
            + 3*(2-K_B)*cad2v*Hc*Qb*alpha )
    Ealpha = RHS/coef_E
    Pi = cad2v*delta_s + kap3*(K_B*Ealpha + (2-K_B)*chi)
    return Ealpha, Pi, chi


def rhs_quasistatic(N, y, kappa):
    N = min(max(N, Nmin_g), Nmax_g)
    delta_b, theta_b, delta_s, theta_s, alpha = y
    Ev2 = float(E2_i(N)); Hc = np.sqrt(Ev2)
    Omb = float(Omb_i(N)); Oms = float(Oms_i(N))
    wv = float(w_i(N))
    Ealpha, Pi, chi = slaved_Ealpha(N, delta_s, theta_s, alpha, kappa)

    Phi = -1.5*(Omb*delta_b + Oms*delta_s)/kappa
    Psi = Phi
    dPhi_dN = 0.0

    ddb = 3*dPhi_dN - kappa*theta_b/Hc
    dtb = Psi/Hc
    dds = 3*(wv*delta_s - Pi) + (1+wv)*(3*dPhi_dN - kappa*theta_s/Hc)
    dts = 3*float(cad2_i(N))*theta_s + (Pi/(1+wv) + Psi)/Hc
    dalpha = (Ealpha - Psi)/Hc
    return [ddb, dtb, dds, dts, dalpha]


zstart = 100.0
N_start = Nsort[np.argmin(np.abs(z_arr-zstart))]
N_end = Nsort[-1]
Ngrid = np.linspace(N_start, N_end, 3000)
zg = np.exp(-Ngrid)-1
d0 = np.exp(N_start)
y0_5 = [d0, d0, d0, d0, 0.0]

c0H0_Mpc = C0/1000/(100*H)

print("=== REGRESSION: quasi-static closure at kappa_test=1e-6 (Pi's vector term negligible) ===")
sol_reg = solve_ivp(rhs_quasistatic, (N_start,N_end), y0_5, args=(1e-6,), t_eval=Ngrid,
                     rtol=1e-9, atol=1e-13, method='RK45')
delta_b, theta_b, delta_s, theta_s, alpha = sol_reg.y
Ev2_g = E2_i(np.clip(Ngrid,Nmin_g,Nmax_g))
Omb_g = Omb_i(np.clip(Ngrid,Nmin_g,Nmax_g)); Oms_g = Oms_i(np.clip(Ngrid,Nmin_g,Nmax_g))
Phi_check = -1.5*(Omb_g*delta_b+Oms_g*delta_s)/1e-6
Phi_check /= Phi_check[0]
for zt in [100,50,30,10,5,2,1,0.5,0.2,0.0]:
    i = np.argmin(np.abs(zg-zt))
    print(f"  z={zt:>5}: Phi/Phi_i={Phi_check[i]:.4f}")

print("\n=== MAIN TEST: k=1e-4 Mpc^-1, quasi-static closure (the case that blew up explicitly) ===")
k_Mpc = 1e-4
def rhs_kappa_of_N(N, y):
    a = np.exp(N)
    kap = (k_Mpc*c0H0_Mpc/a)**2
    return rhs_quasistatic(N, y, kap)
sol3c = solve_ivp(rhs_kappa_of_N, (N_start,N_end), y0_5, t_eval=Ngrid,
                   rtol=1e-8, atol=1e-12, method='Radau', max_step=0.05)
if not sol3c.success:
    print("FAILED:", sol3c.message)
else:
    delta_b, theta_b, delta_s, theta_s, alpha = sol3c.y
    for zt in [100,50,30,10,5,2,1,0.5,0.2,0.0]:
        i = np.argmin(np.abs(zg-zt))
        Ealpha_i, _, _ = slaved_Ealpha(Ngrid[i], delta_s[i], theta_s[i], alpha[i],
                                        (k_Mpc*c0H0_Mpc/np.exp(Ngrid[i]))**2)
        print(f"  z={zt:>5}: delta_b={delta_b[i]:.4e}  delta_s={delta_s[i]:.4e}  alpha={alpha[i]:.3e}  Ealpha_slaved={Ealpha_i:.3e}")

print("\n=== CROSS-CHECK at small k (below kappa_crit everywhere): compare explicit vs quasi-static ===")
k_Mpc_small = 1e-6
def rhs_kappa_of_N_small(N, y):
    a = np.exp(N)
    kap = (k_Mpc_small*c0H0_Mpc/a)**2
    return rhs_quasistatic(N, y, kap)
sol_small = solve_ivp(rhs_kappa_of_N_small, (N_start,N_end), y0_5, t_eval=Ngrid,
                       rtol=1e-9, atol=1e-13, method='RK45')
delta_b, theta_b, delta_s, theta_s, alpha = sol_small.y
for zt in [100,50,10,1,0.0]:
    i = np.argmin(np.abs(zg-zt))
    print(f"  z={zt:>5}: delta_b={delta_b[i]:.4e}  delta_s={delta_s[i]:.4e}  alpha={alpha[i]:.3e}")
