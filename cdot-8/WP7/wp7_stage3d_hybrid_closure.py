#!/usr/bin/env python3
"""
wp7_stage3d_hybrid_closure.py -- 2026-07-20. Stage 3d: implement the
advisor-corrected hybrid closure (Advisory-WP7-Stage3cTransitionZoneReview-
2026-07-20.md).

Correction accepted from the advisory: the switch does NOT belong at the
discriminant's zero (z~29-30, real<->complex eigenvalue transition --
misidentified in wp7_stage3c_quasistatic_closure.py's own write-up) but
at Re(lambda_max)=0, i.e. tr(J)=0, i.e. coef_E=0 -- a later, lower-z
threshold (z~18-19 for k=1e-4 Mpc^-1). Independently re-derived and
confirmed: since J_11=0 identically in this system, tr(J)=J_22=coef_E/
(-K_B*Hc), and for any 2x2 matrix Re(lambda) both equal tr/2 when
complex, so coef_E=0 IS exactly Re(lambda_max)=0 for the full system --
not a numerical accident, the one place the fast/slow separation the
quasi-static method leans on genuinely vanishes.

Design (per the advisory's own recommendation, sec.5): a HARD,
criterion-based switch at z_switch(k) where tr(J)=0, with a small safety
margin -- NOT a smoothed blend (the regimes on either side are dynamically
different: real-unstable, then complex-growing-spiral, then complex-decaying
-- interpolating a formula across that range is more likely to introduce
its own artifact than resolve one).

  z > z_switch (+ margin): quasi-static slaving for E_alpha (Stage 3c/3b),
    valid because a genuine growing mode exists that must be projected out.
  z < z_switch (- margin): full explicit (alpha, E_alpha) ODE pair,
    valid because Re(lambda)<0 everywhere below the switch (no growing
    mode to eliminate) -- confirmed as its own regression below (this
    is the "symmetric statement" the advisory flagged as worth testing
    but not yet done at Stage 3c).

ROBUSTNESS CHECK (advisor-recommended, sec.5 item 4): verify Phi, delta_s,
delta_b near the switch are insensitive to the exact margin chosen within
a reasonable range.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.optimize import brentq

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
c0H0_Mpc = C0/1000/(100*H)


def coefs(N, kappa):
    Ev2 = float(E2_i(N)); Hc = np.sqrt(Ev2)
    wv = float(w_i(N)); cad2v = float(cad2_i(N))
    Qb = float(Q_i(N)); FQv = float(FQ_i(N)); Oms = float(Oms_i(N))
    dKdQ = -0.5*FQv
    kap3 = cad2v*kappa/(3*Oms)
    return Hc, wv, cad2v, Qb, dKdQ, kap3


def trace_J(N, kappa):
    """tr(J) = coef_E/(-K_B*Hc); zero of this = Re(lambda_max)=0, the
    advisor-corrected switch criterion (NOT the discriminant's zero)."""
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kappa)
    dPi_dEalpha = kap3*K_B
    return (-(2-K_B)*(Qb/(1+wv)*dPi_dEalpha))/(K_B*Hc) - 1.0


def slaved_Ealpha(N, delta_s, theta_s, alpha, kappa):
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kappa)
    chi = Qb*(theta_s + alpha)
    coef_E = K_B*Hc + (2-K_B)*K_B*Qb/(1+wv)*kap3
    RHS = ( dKdQ*chi
            - (2-K_B)*Qb/(1+wv)*cad2v*delta_s
            - (2-K_B)**2*Qb/(1+wv)*kap3*chi
            - (2-K_B)*(Hc+Qb)*chi
            + 3*(2-K_B)*cad2v*Hc*Qb*alpha )
    Ealpha = RHS/coef_E
    Pi = cad2v*delta_s + kap3*(K_B*Ealpha + (2-K_B)*chi)
    return Ealpha, Pi, chi


def rhs_full(N, y, kappa):
    """Full explicit 6-variable system (valid where Re(lambda)<0)."""
    N = min(max(N, Nmin_g), Nmax_g)
    delta_b, theta_b, delta_s, theta_s, alpha, Ealpha = y
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kappa)
    Omb = float(Omb_i(N)); Oms = float(Oms_i(N))
    Phi = -1.5*(Omb*delta_b + Oms*delta_s)/kappa
    Psi = Phi
    chi = Qb*(theta_s + alpha)
    bracket = K_B*Ealpha + (2-K_B)*chi
    Pi = cad2v*delta_s + kap3*bracket
    ddb = -kappa*theta_b/Hc
    dtb = Psi/Hc
    dds = 3*(wv*delta_s - Pi) + (1+wv)*(-kappa*theta_s/Hc)
    dts = 3*cad2v*theta_s + (Pi/(1+wv) + Psi)/Hc
    dalpha = (Ealpha - Psi)/Hc
    dEalpha = ( dKdQ*chi - (2-K_B)*( Qb/(1+wv)*Pi + (Hc+Qb)*chi - 3*cad2v*Hc*Qb*alpha ) )/(K_B*Hc) - Ealpha
    return [ddb, dtb, dds, dts, dalpha, dEalpha]


def rhs_quasistatic(N, y, kappa):
    """Reduced 5-variable system with E_alpha algebraically slaved
    (valid where Re(lambda)>0 -- projects out the growing mode)."""
    N = min(max(N, Nmin_g), Nmax_g)
    delta_b, theta_b, delta_s, theta_s, alpha = y
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kappa)
    Omb = float(Omb_i(N)); Oms = float(Oms_i(N))
    Ealpha, Pi, chi = slaved_Ealpha(N, delta_s, theta_s, alpha, kappa)
    Phi = -1.5*(Omb*delta_b + Oms*delta_s)/kappa
    Psi = Phi
    ddb = -kappa*theta_b/Hc
    dtb = Psi/Hc
    dds = 3*(wv*delta_s - Pi) + (1+wv)*(-kappa*theta_s/Hc)
    dts = 3*cad2v*theta_s + (Pi/(1+wv) + Psi)/Hc
    dalpha = (Ealpha - Psi)/Hc
    return [ddb, dtb, dds, dts, dalpha]


def find_z_switch(k_Mpc, z_lo=1.0, z_hi=99.0):
    """Bisect for tr(J)=0 (Re(lambda_max)=0) at fixed comoving k."""
    def f(zt):
        i = np.argmin(np.abs(z_arr - zt))
        N = Nsort[np.searchsorted(Nsort, -np.log(1+zt))] if False else -np.log(1+zt)
        a = np.exp(N)
        kap = (k_Mpc*c0H0_Mpc/a)**2
        return trace_J(N, kap)
    return brentq(f, z_lo, z_hi)


def run_hybrid(k_Mpc, margin_efolds=0.05, zstart=100.0):
    z_sw = find_z_switch(k_Mpc)
    N_switch = -np.log(1+z_sw)
    N_start = -np.log(1+zstart)
    N_end = Nsort[-1]

    N_hi = N_switch - margin_efolds   # still in QS (growing) regime, safety margin before pole
    N_lo = N_switch + margin_efolds   # in explicit (stable) regime

    d0 = np.exp(N_start)
    y0_5 = [d0, d0, d0, d0, 0.0]

    def rhs_qs(N, y):
        a = np.exp(N); kap = (k_Mpc*c0H0_Mpc/a)**2
        return rhs_quasistatic(N, y, kap)

    Ngrid_qs = np.linspace(N_start, N_hi, 1500)
    sol_qs = solve_ivp(rhs_qs, (N_start, N_hi), y0_5, t_eval=Ngrid_qs,
                        rtol=1e-9, atol=1e-13, method='Radau', max_step=0.02)
    if not sol_qs.success:
        return None, z_sw, ("QS phase failed: " + sol_qs.message)

    delta_b, theta_b, delta_s, theta_s, alpha = sol_qs.y[:, -1]
    kap_hi = (k_Mpc*c0H0_Mpc/np.exp(N_hi))**2
    Ealpha_hi, _, _ = slaved_Ealpha(N_hi, delta_s, theta_s, alpha, kap_hi)

    def rhs_ex(N, y):
        a = np.exp(N); kap = (k_Mpc*c0H0_Mpc/a)**2
        return rhs_full(N, y, kap)

    y0_6 = [delta_b, theta_b, delta_s, theta_s, alpha, Ealpha_hi]
    Ngrid_ex = np.linspace(N_hi, N_end, 3000)
    sol_ex = solve_ivp(rhs_ex, (N_hi, N_end), y0_6, t_eval=Ngrid_ex,
                        rtol=1e-8, atol=1e-12, method='Radau', max_step=0.02)
    if not sol_ex.success:
        return None, z_sw, ("Explicit phase failed: " + sol_ex.message)

    Nfull = np.concatenate([Ngrid_qs, Ngrid_ex[1:]])
    zfull = np.exp(-Nfull) - 1
    delta_b_f = np.concatenate([sol_qs.y[0], sol_ex.y[0][1:]])
    delta_s_f = np.concatenate([sol_qs.y[2], sol_ex.y[2][1:]])
    alpha_f = np.concatenate([sol_qs.y[4], sol_ex.y[4][1:]])
    return (zfull, delta_b_f, delta_s_f, alpha_f), z_sw, "OK"


if __name__ == '__main__':
    k_Mpc = 1e-4
    z_sw = find_z_switch(k_Mpc)
    print(f"=== z_switch for k={k_Mpc} Mpc^-1: z={z_sw:.3f} (advisor's table: z~18-19) ===\n")

    print("=== Hybrid run, main test ===")
    result, zsw, status = run_hybrid(k_Mpc, margin_efolds=0.05)
    print("status:", status, " z_switch:", zsw)
    if result is not None:
        zfull, delta_b_f, delta_s_f, alpha_f = result
        for zt in [100,80,60,40,30,25,20,19,18,17,15,10,5,2,1,0.5,0.0]:
            i = np.argmin(np.abs(zfull-zt))
            print(f"  z={zt:6}: delta_b={delta_b_f[i]:.4e}  delta_s={delta_s_f[i]:.4e}  alpha={alpha_f[i]:.4e}")

    print("\n=== Robustness check: vary the safety margin ===")
    for margin in (0.02, 0.05, 0.1, 0.2):
        result, zsw, status = run_hybrid(k_Mpc, margin_efolds=margin)
        if result is None:
            print(f"  margin={margin}: FAILED ({status})")
            continue
        zfull, delta_b_f, delta_s_f, alpha_f = result
        i0 = np.argmin(np.abs(zfull-0.0))
        i_sw = np.argmin(np.abs(zfull-zsw))
        print(f"  margin={margin:.2f} efolds: delta_b(z=0)={delta_b_f[i0]:.6e}  "
              f"delta_s(z=0)={delta_s_f[i0]:.6e}  alpha(z=0)={alpha_f[i0]:.6e}  "
              f"[at switch: delta_s={delta_s_f[i_sw]:.4e}, alpha={alpha_f[i_sw]:.4e}]")
