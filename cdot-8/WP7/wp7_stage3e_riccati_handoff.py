#!/usr/bin/env python3
"""
wp7_stage3e_riccati_handoff.py -- 2026-07-20. Stage 3e: implement the
advisor-resolved two-phase design
(Advisory-WP7-Stage3eRiccatiSpiralResolution-2026-07-20.md).

Resolution accepted: §38's complex-Riccati gap does NOT need a complex/
matrix generalization. In the spiral (complex-eigenvalue) zone
(z~18.5-29.5 for k=1e-4 Mpc^-1), every real direction shares the same
growth envelope Re(lambda) -- there is no preferred direction left to
project onto or away from, so there is nothing for a stable-subspace
method to select there. The fix: track the real Riccati slope mu(N)
only as far as it IS real (z >~ 29-30, D_mu=D_J=0 there, an EXACT
identity: D_mu = Hc^2 * D_J, verified both algebraically and
numerically), seeded at z~60 where naive frozen-coefficient slaving is
already excellent, then HAND OFF ONCE to full explicit (alpha, E_alpha)
integration for the entire rest of the run (covering both the spiral-
unstable zone AND the later genuinely-stable zone in one continuous
phase -- z_switch=18.5 stops being a special point at all).

This replaces wp7_stage3d_hybrid_closure.py's two-switch design (which
mislocated the handoff at z_switch=18.5, deep inside the spiral zone,
and suffered catastrophic margin-sensitivity as a result).
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
c0H0_Mpc = C0/1000/(100*H)


def coefs(N, kappa):
    Ev2 = float(E2_i(N)); Hc = np.sqrt(Ev2)
    wv = float(w_i(N)); cad2v = float(cad2_i(N))
    Qb = float(Q_i(N)); FQv = float(FQ_i(N)); Oms = float(Oms_i(N))
    dKdQ = -0.5*FQv
    kap3 = cad2v*kappa/(3*Oms)
    return Hc, wv, cad2v, Qb, dKdQ, kap3


def aEE_aEalpha(N, kappa):
    """The two coefficients driving the Riccati equation:
    a_EE = d(Edot_alpha)/d(E_alpha), a_Ealpha = d(Edot_alpha)/d(alpha)."""
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kappa)
    dPi_dEalpha = kap3*K_B
    dPi_dalpha = kap3*(2-K_B)*Qb
    a_EE = (-(2-K_B)*(Qb/(1+wv)*dPi_dEalpha))/(K_B*Hc) - 1.0
    a_Ealpha = (dKdQ*Qb - (2-K_B)*(Qb/(1+wv)*dPi_dalpha + (Hc+Qb)*Qb - 3*cad2v*Hc*Qb))/(K_B*Hc)
    return Hc, a_EE, a_Ealpha


def forcing_C(N, kappa, theta_s, delta_s):
    """The theta_s/delta_s-sourced forcing term in K_B*Hc*dEalpha/dN
    (everything except the alpha- and E_alpha-proportional pieces),
    divided by K_B*Hc to match a_EE/a_Ealpha's own normalization."""
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kappa)
    C = ( dKdQ*Qb*theta_s
          - (2-K_B)*Qb/(1+wv)*cad2v*delta_s
          - (2-K_B)**2*Qb**2/(1+wv)*kap3*theta_s
          - (2-K_B)*(Hc+Qb)*Qb*theta_s )
    return C/(K_B*Hc)


def rhs_full(N, y, kappa):
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


def rhs_riccati_phase(N, y, kappa):
    """State: (delta_b, theta_b, delta_s, theta_s, alpha, mu, nu).
    E_alpha = mu*alpha + nu throughout this phase (valid only while
    the eigenvalues stay real, i.e. z well above the z~29-30 boundary)."""
    N = min(max(N, Nmin_g), Nmax_g)
    delta_b, theta_b, delta_s, theta_s, alpha, mu, nu = y
    Hc, a_EE, a_Ealpha = aEE_aEalpha(N, kappa)
    Omb = float(Omb_i(N)); Oms = float(Oms_i(N))
    wv = float(w_i(N)); cad2v = float(cad2_i(N)); Qb = float(Q_i(N))
    kap3 = cad2v*kappa/(3*Oms)

    Ealpha = mu*alpha + nu
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

    C = forcing_C(N, kappa, theta_s, delta_s)
    dmu = a_EE*mu + a_Ealpha - mu*mu/Hc
    dnu = (a_EE - mu/Hc)*nu + mu*Psi/Hc + C

    return [ddb, dtb, dds, dts, dalpha, dmu, dnu]


def run_two_phase(k_Mpc, z_seed=60.0, z_handoff=30.0, zstart=100.0):
    N_start = -np.log(1+zstart)
    N_seed = -np.log(1+z_seed)
    N_handoff = -np.log(1+z_handoff)
    N_end = Nsort[-1]

    def kap_of(N):
        return (k_Mpc*c0H0_Mpc/np.exp(N))**2

    # Phase 0: z=100 -> z_seed, explicit ODE with E_alpha started at its
    # own naive-slaved value at z=100 (adiabaticity is excellent there,
    # per the advisor's own table -- lambda_max~221/e-fold -- so this
    # start is safe; any transient mismatch decays before z_seed).
    d0 = np.exp(N_start)
    Hc0, a_EE0, a_Ealpha0 = aEE_aEalpha(N_start, kap_of(N_start))
    # naive algebraic slaved mu,nu at the start (frozen-coefficient fixed point).
    # STABLE root is the MINUS branch: lambda_stable=(a_EE-sqrt(D))/2 < lambda_unstable
    # (verified numerically: at z~100, a_EE=tr=208.5, roots {-12.6,+221.1} -- minus
    # branch gives -12.6, the stable one; using the plus branch here would silently
    # seed on the UNSTABLE eigendirection instead).
    mu0 = Hc0*(a_EE0 - np.sqrt(a_EE0**2 + 4*a_Ealpha0/Hc0))/2  # stable root
    C0v = forcing_C(N_start, kap_of(N_start), d0, d0)
    nu0 = -(a_Ealpha0*0 + C0v)/(a_EE0 - mu0/Hc0) if abs(a_EE0-mu0/Hc0) > 1e-30 else 0.0
    Ealpha_seed0 = mu0*0.0 + nu0

    y0_6 = [d0, d0, d0, d0, 0.0, Ealpha_seed0]

    def rhs_ex0(N, y):
        return rhs_full(N, y, kap_of(N))
    Ngrid0 = np.linspace(N_start, N_seed, 800)
    sol0 = solve_ivp(rhs_ex0, (N_start, N_seed), y0_6, t_eval=Ngrid0,
                      rtol=1e-9, atol=1e-13, method='Radau', max_step=0.02)
    if not sol0.success:
        return None, "phase0 failed: " + sol0.message

    delta_b, theta_b, delta_s, theta_s, alpha, Ealpha = sol0.y[:, -1]

    # Phase 1: z_seed -> z_handoff, Riccati continuation
    Hc_s, a_EE_s, a_Ealpha_s = aEE_aEalpha(N_seed, kap_of(N_seed))
    mu_seed = Hc_s*(a_EE_s - np.sqrt(max(a_EE_s**2 + 4*a_Ealpha_s/Hc_s, 0.0)))/2  # stable root
    nu_seed = Ealpha - mu_seed*alpha   # match continuously to phase-0 end state

    y1 = [delta_b, theta_b, delta_s, theta_s, alpha, mu_seed, nu_seed]

    def rhs_ric(N, y):
        return rhs_riccati_phase(N, y, kap_of(N))
    Ngrid1 = np.linspace(N_seed, N_handoff, 1500)
    sol1 = solve_ivp(rhs_ric, (N_seed, N_handoff), y1, t_eval=Ngrid1,
                      rtol=1e-10, atol=1e-14, method='Radau', max_step=0.01)
    if not sol1.success:
        return None, "phase1 (Riccati) failed: " + sol1.message

    delta_b, theta_b, delta_s, theta_s, alpha, mu, nu = sol1.y[:, -1]
    Ealpha_handoff = mu*alpha + nu

    # Phase 2: z_handoff -> 0, full explicit integration, no further switch
    y2 = [delta_b, theta_b, delta_s, theta_s, alpha, Ealpha_handoff]

    def rhs_ex2(N, y):
        return rhs_full(N, y, kap_of(N))
    Ngrid2 = np.linspace(N_handoff, N_end, 3000)
    sol2 = solve_ivp(rhs_ex2, (N_handoff, N_end), y2, t_eval=Ngrid2,
                      rtol=1e-8, atol=1e-12, method='Radau', max_step=0.02)
    if not sol2.success:
        return None, "phase2 failed: " + sol2.message

    Nfull = np.concatenate([Ngrid0, Ngrid1[1:], Ngrid2[1:]])
    zfull = np.exp(-Nfull) - 1
    delta_b_f = np.concatenate([sol0.y[0], sol1.y[0][1:], sol2.y[0][1:]])
    delta_s_f = np.concatenate([sol0.y[2], sol1.y[2][1:], sol2.y[2][1:]])
    alpha_f = np.concatenate([sol0.y[4], sol1.y[4][1:], sol2.y[4][1:]])
    return (zfull, delta_b_f, delta_s_f, alpha_f), "OK"


if __name__ == '__main__':
    k_Mpc = 1e-4
    print("=== Main run: seed z=60, handoff z=30 ===")
    result, status = run_two_phase(k_Mpc, z_seed=60.0, z_handoff=30.0)
    print("status:", status)
    if result is not None:
        zfull, delta_b_f, delta_s_f, alpha_f = result
        for zt in [100,80,60,40,30,25,20,18.5,15,10,5,2,1,0.5,0.0]:
            i = np.argmin(np.abs(zfull-zt))
            print(f"  z={zt:6}: delta_b={delta_b_f[i]:.4e}  delta_s={delta_s_f[i]:.4e}  alpha={alpha_f[i]:.4e}")

    print("\n=== Robustness check: vary handoff redshift within the real-Riccati region ===")
    for zh in (35.0, 32.0, 30.5, 29.8):
        result, status = run_two_phase(k_Mpc, z_seed=60.0, z_handoff=zh)
        if result is None:
            print(f"  z_handoff={zh}: FAILED ({status})")
            continue
        zfull, delta_b_f, delta_s_f, alpha_f = result
        i0 = np.argmin(np.abs(zfull-0.0))
        print(f"  z_handoff={zh:5}: delta_b(z=0)={delta_b_f[i0]:.6e}  "
              f"delta_s(z=0)={delta_s_f[i0]:.6e}  alpha(z=0)={alpha_f[i0]:.6e}")
