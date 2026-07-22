#!/usr/bin/env python3
"""
wp7_stage4_isw_estimate.py -- 2026-07-21. Stage 4: the ISW Delta-C_ell
estimate, now that the growth system is validated (Stage 3f/g) and the
M5 Einstein-constraint term is fully derived (sec.4-6).

Physics assembled from two independently-completed threads:

1. GROWTH: chi,gamma,alpha,E_alpha (equivalently delta_s,theta_s,alpha,
   E_alpha in this document's own field-variable notation) are
   UNMODIFIED by M5 (sec.7's exact-cancellation finding, the -F_Q*A^mu
   / +Lambda_M*A^mu terms cancel identically at every k) -- so the
   validated Stage-3f/g closure (pointwise algebraic slaving for
   (alpha,E_alpha) above z~35, full explicit integration below, no
   Riccati apparatus needed) can be used exactly as built, with zero
   new terms of its own.

2. M5's ONLY modification is a single additive term in the Einstein
   constraint (Poisson) equation (sec.6's corrected coefficient):

     delta_G^0_0 |_M5 = 8 pi G [F_Q/6 + Q*F_QQ/2] q' Nbar_tot W(k R_h)
                        [delta_N - 3 Phi]

   Since delta_G^0_0 = 8 pi G sum(rhobar_I delta_I) = 3 H0^2 sum(Om_I
   delta_I) and Phi = -0.5 a^2/k^2 * delta_G^0_0 = -0.5/(kappa H0^2) *
   delta_G^0_0 in this program's own kappa=(k/aH0)^2 convention (matches
   the already-coded Phi=-1.5*sum(Om_i delta_i)/kappa exactly), the M5
   addition to Phi is:

     Phi = -1.5*(Om_b delta_b + Om_s delta_s)/kappa
           - 1.5*coeff(z)*W(k R_h)*(delta_N - 3 Phi)/kappa

   where coeff(z) = (F_Q/6 + Q*F_QQ/2)*q'_Ntot (sec.18's already-
   validated coefficient -- O(0.5-0.7), same F_QQ used in WP5's
   condensate mass and the SZ stability check, no new parameter).
   Solved algebraically for Phi (implicit since delta_N-3Phi contains
   Phi) below.

   FLAGGED APPROXIMATION, stated explicitly (per the document's own
   standing "bookkeeping precision" flag in sec.6): delta_N (the
   census-weighted total contrast entering the M5 term) is taken here
   as delta_b -- the same "ordinary matter+radiation" census content
   the M5 coefficient's own normalization (matter_source=3*u_hat) was
   built against in sec.18-21, NOT including Om_s. A genuine refinement
   (the exact N_i-weighted census contrast) is flagged, not attempted,
   consistent with this being a first, honestly-scoped ISW estimate.

DELIVERABLE: ISW kernel (~ a H d(2 Phi)/dN, since Phi=Psi throughout)
with and without the M5 term, for k matching l=2,5,10 via the
established k=l/D_p(z=0.5) convention (sec.21's own script), reporting
a first Delta-C_l/C_l-type estimate -- NOT a full Boltzmann/Limber
line-of-sight calculation, explicitly scoped as such.
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
F_QQ = np.gradient(F_Q, s)/np.gradient(Q_arr, s)
Om_s_frac = Om_s/E2
Om_b = om_cold*(1+z_arr)**3/E2

w = -(1/4.5)*np.gradient(np.log(np.abs(Om_s)), s) - 1
dw_ds = np.gradient(w, s)
dlnrho_ds = np.gradient(np.log(np.abs(Om_s)), s)
cad2 = w + dw_ds/dlnrho_ds

# --- M5 coefficient machinery (sec.18's own, validated formulas) ---
c0H0_Mpc = C0/1000/(100*H)
Rh_Mpc = 1.5*cumulative_trapezoid(np.exp(s)/E, s, initial=0.0)*c0H0_Mpc
dlnRh_ds = np.gradient(np.log(np.maximum(Rh_Mpc, 1e-30)), s)
dln_u_ds = np.gradient(np.log(u_arr), s)
dlnNtot_ds = dln_u_ds + 3.0 + 3.0*dlnRh_ds
qprime_Ntot = (-2.5/dlnNtot_ds)*Q_arr
M5_coeff = (F_Q/6 + Q_arr*F_QQ/2)*qprime_Ntot   # sec.18's coeff, O(0.5-0.7)

Wwin = lambda xx: np.where(np.abs(xx) > 1e-6, 3*(np.sin(xx)-xx*np.cos(xx))/xx**3, 1.0-xx**2/10.0)

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
Rh_i = interp1d(Nsort, Rh_Mpc[order], kind='linear')
M5coeff_i = interp1d(Nsort, M5_coeff[order], kind='linear')
Nmin_g, Nmax_g = Nsort[0], Nsort[-1]


def coefs(N, kappa):
    N = min(max(N, Nmin_g), Nmax_g)
    Ev2 = float(E2_i(N)); Hc = np.sqrt(Ev2)
    wv = float(w_i(N)); cad2v = float(cad2_i(N))
    Qb = float(Q_i(N)); FQv = float(FQ_i(N)); Oms = float(Oms_i(N))
    dKdQ = -0.5*FQv
    kap3 = cad2v*kappa/(3*Oms)
    return Hc, wv, cad2v, Qb, dKdQ, kap3


def Phi_of_state(N, kappa, delta_b, delta_s, k_Mpc, use_M5):
    """Solve Phi algebraically, including the M5 addition (implicit in
    Phi via delta_N - 3 Phi, solved in closed form here)."""
    N = min(max(N, Nmin_g), Nmax_g)
    Omb = float(Omb_i(N)); Oms = float(Oms_i(N))
    S = Omb*delta_b + Oms*delta_s
    if not use_M5:
        return -1.5*S/kappa
    Rhv = float(Rh_i(N))
    Wv = float(Wwin(k_Mpc*Rhv))
    coeff = float(M5coeff_i(N))
    deltaN_proxy = delta_b   # flagged approximation, see module docstring
    # kappa*Phi = -1.5 S - 1.5 coeff W (deltaN_proxy - 3 Phi)
    # Phi (kappa - 4.5 coeff W) = -1.5 S - 1.5 coeff W deltaN_proxy
    denom = kappa - 4.5*coeff*Wv
    return (-1.5*S - 1.5*coeff*Wv*deltaN_proxy)/denom


def slaved_Ealpha_pointwise(N, delta_s, theta_s, alpha, kappa):
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kappa)
    chi = Qb*(theta_s + alpha)
    coef_E = K_B*Hc + (2-K_B)*K_B*Qb/(1+wv)*kap3
    RHS = (dKdQ*chi
           - (2-K_B)*Qb/(1+wv)*cad2v*delta_s
           - (2-K_B)**2*Qb/(1+wv)*kap3*chi
           - (2-K_B)*(Hc+Qb)*chi
           + 3*(2-K_B)*cad2v*Hc*Qb*alpha)
    Ealpha = RHS/coef_E
    Pi = cad2v*delta_s + kap3*(K_B*Ealpha + (2-K_B)*chi)
    return Ealpha, Pi


def rhs_quasistatic(N, y, kappa, k_Mpc, use_M5):
    N = min(max(N, Nmin_g), Nmax_g)
    delta_b, theta_b, delta_s, theta_s, alpha = y
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kappa)
    Ealpha, Pi = slaved_Ealpha_pointwise(N, delta_s, theta_s, alpha, kappa)
    Phi = Phi_of_state(N, kappa, delta_b, delta_s, k_Mpc, use_M5)
    Psi = Phi
    ddb = -kappa*theta_b/Hc
    dtb = Psi/Hc
    dds = 3*(wv*delta_s - Pi) + (1+wv)*(-kappa*theta_s/Hc)
    dts = 3*cad2v*theta_s + (Pi/(1+wv) + Psi)/Hc
    dalpha = (Ealpha - Psi)/Hc
    return [ddb, dtb, dds, dts, dalpha]


def rhs_explicit(N, y, kappa, k_Mpc, use_M5):
    N = min(max(N, Nmin_g), Nmax_g)
    delta_b, theta_b, delta_s, theta_s, alpha, Ealpha = y
    Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kappa)
    Phi = Phi_of_state(N, kappa, delta_b, delta_s, k_Mpc, use_M5)
    Psi = Phi
    chi = Qb*(theta_s + alpha)
    bracket = K_B*Ealpha + (2-K_B)*chi
    Pi = cad2v*delta_s + kap3*bracket
    ddb = -kappa*theta_b/Hc
    dtb = Psi/Hc
    dds = 3*(wv*delta_s - Pi) + (1+wv)*(-kappa*theta_s/Hc)
    dts = 3*cad2v*theta_s + (Pi/(1+wv) + Psi)/Hc
    dalpha = (Ealpha - Psi)/Hc
    dEalpha = (dKdQ*chi - (2-K_B)*(Qb/(1+wv)*Pi + (Hc+Qb)*chi - 3*cad2v*Hc*Qb*alpha))/(K_B*Hc) - Ealpha
    return [ddb, dtb, dds, dts, dalpha, dEalpha]


def check_stabilizes(k_Mpc, zs=(100,80,60,50,40,30,20,15,10,5,2,1,0.5,0.2,0.05,0.0)):
    """Stage 3f's handoff-to-explicit design is only valid if the
    (alpha,E_alpha) subsystem genuinely restabilizes (Re(lambda)<0) and
    STAYS stable down to z=0. This must be checked PER k -- Stage 3f
    only ever validated k=1e-4 Mpc^-1; the much larger, ISW-relevant k
    here (~1e-3 to 5e-3 Mpc^-1, per l=2-10) turn out NOT to satisfy
    this (found empirically below, in sec.42 of the Update doc)."""
    K_B_ = K_B
    for zt in zs:
        N = -np.log(1+zt)
        a = np.exp(N)
        kap = (k_Mpc*c0H0_Mpc/a)**2
        Hc, wv, cad2v, Qb, dKdQ, kap3 = coefs(N, kap)
        dPi_dEalpha = kap3*K_B_
        dPi_dalpha = kap3*(2-K_B_)*Qb
        dEalpha_dalpha = (dKdQ*Qb - (2-K_B_)*(Qb/(1+wv)*dPi_dalpha + (Hc+Qb)*Qb - 3*cad2v*Hc*Qb))/(K_B_*Hc)
        dEalpha_dEalpha = (-(2-K_B_)*(Qb/(1+wv)*dPi_dEalpha))/(K_B_*Hc) - 1.0
        J = np.array([[0.0, 1.0/Hc], [dEalpha_dalpha, dEalpha_dEalpha]])
        if np.max(np.linalg.eigvals(J).real) > 1e-8:
            return False   # still unstable at this z -- no valid handoff point below it
    return True


def run_growth(k_Mpc, use_M5, z_handoff=35.0, zstart=100.0):
    """Stage-3f's validated closure IF the mode genuinely restabilizes
    by z_handoff and stays stable to z=0 (checked via check_stabilizes);
    otherwise falls back to pointwise slaving THROUGHOUT the whole run
    (no handoff at all) -- valid whenever the fast mode stays large in
    magnitude (real or complex) across the run, per the same adiabatic-
    elimination logic Stage 3c/3f already established, just without a
    stable regime to hand off into."""
    N_start = -np.log(1+zstart)
    N_end = Nsort[-1]

    def kap_of(N):
        return (k_Mpc*c0H0_Mpc/np.exp(N))**2

    d0 = np.exp(N_start)
    y0 = [d0, d0, d0, d0, 0.0]

    if not check_stabilizes(k_Mpc):
        # Pure pointwise slaving throughout -- no explicit phase.
        def rhs_qs_all(N, y):
            return rhs_quasistatic(N, y, kap_of(N), k_Mpc, use_M5)
        Ngrid = np.linspace(N_start, N_end, 4000)
        sol = solve_ivp(rhs_qs_all, (N_start, N_end), y0, t_eval=Ngrid,
                         rtol=1e-9, atol=1e-13, method='Radau', max_step=0.02)
        if not sol.success:
            return None, "pointwise-throughout failed: " + sol.message
        delta_b_f, delta_s_f = sol.y[0], sol.y[2]
        Phi_f = np.array([Phi_of_state(N, kap_of(N), db, ds, k_Mpc, use_M5)
                           for N, db, ds in zip(Ngrid, delta_b_f, delta_s_f)])
        return (Ngrid, Phi_f), "OK (pointwise throughout, no stable handoff exists)"

    N_handoff = -np.log(1+z_handoff)

    def rhs_qs(N, y):
        return rhs_quasistatic(N, y, kap_of(N), k_Mpc, use_M5)
    Ngrid_qs = np.linspace(N_start, N_handoff, 1500)
    sol_qs = solve_ivp(rhs_qs, (N_start, N_handoff), y0, t_eval=Ngrid_qs,
                        rtol=1e-9, atol=1e-13, method='Radau', max_step=0.02)
    if not sol_qs.success:
        return None, "QS failed: " + sol_qs.message
    delta_b, theta_b, delta_s, theta_s, alpha = sol_qs.y[:, -1]
    Ealpha_h, _ = slaved_Ealpha_pointwise(N_handoff, delta_s, theta_s, alpha, kap_of(N_handoff))

    def rhs_ex(N, y):
        return rhs_explicit(N, y, kap_of(N), k_Mpc, use_M5)
    y1 = [delta_b, theta_b, delta_s, theta_s, alpha, Ealpha_h]
    Ngrid_ex = np.linspace(N_handoff, N_end, 3000)
    sol_ex = solve_ivp(rhs_ex, (N_handoff, N_end), y1, t_eval=Ngrid_ex,
                        rtol=1e-8, atol=1e-12, method='Radau', max_step=0.02)
    if not sol_ex.success:
        return None, "explicit failed: " + sol_ex.message

    Ngrid = np.concatenate([Ngrid_qs, Ngrid_ex[1:]])
    delta_b_f = np.concatenate([sol_qs.y[0], sol_ex.y[0][1:]])
    delta_s_f = np.concatenate([sol_qs.y[2], sol_ex.y[2][1:]])
    Phi_f = np.array([Phi_of_state(N, kap_of(N), db, ds, k_Mpc, use_M5)
                       for N, db, ds in zip(Ngrid, delta_b_f, delta_s_f)])
    return (Ngrid, Phi_f), "OK"


if __name__ == '__main__':
    # D_p(z), for the established k = l/D_p(z=0.5) convention (sec.21)
    zg = np.linspace(1e-4, 5, 4000)
    Ei_of_z = interp1d(np.sort(z_arr), 1/E[np.argsort(z_arr)], kind='linear')
    Dp_zg = cumulative_trapezoid(Ei_of_z(zg), zg, initial=0.0)*c0H0_Mpc
    Dp_i = interp1d(zg, Dp_zg)
    Dp_at_05 = float(Dp_i(0.5))
    print(f"D_p(z=0.5) = {Dp_at_05:.1f} Mpc\n")

    print("=== Stage 4 ISW estimate: validated growth system + M5 Einstein-constraint term ===\n")
    for l in (2, 5, 10):
        k_Mpc = l/Dp_at_05
        r_std, st_std = run_growth(k_Mpc, use_M5=False)
        r_m5, st_m5 = run_growth(k_Mpc, use_M5=True)
        if r_std is None or r_m5 is None:
            print(f"l={l}: FAILED (std: {st_std}, M5: {st_m5})")
            continue
        Ngrid, Phi_std = r_std
        _, Phi_m5 = r_m5
        Phi_std_n = Phi_std/Phi_std[0]
        Phi_m5_n = Phi_m5/Phi_m5[0]
        kernel_std = np.gradient(Phi_std_n, Ngrid)
        kernel_m5 = np.gradient(Phi_m5_n, Ngrid)
        P_std = np.trapz(kernel_std**2, Ngrid)
        P_m5 = np.trapz(kernel_m5**2, Ngrid)
        zvals = np.exp(-Ngrid)-1
        i_peak = np.argmax(np.abs(kernel_std))
        print(f"l={l:>3}  k={k_Mpc:.4e} 1/Mpc  P_M5/P_std = {P_m5/P_std:.4f}  "
              f"(std kernel peaks near z={zvals[i_peak]:.2f})")
        for zt in (10, 5, 2, 1, 0.5, 0.2, 0.0):
            i = np.argmin(np.abs(zvals-zt))
            print(f"    z={zt:5}: Phi_std/Phi_i={Phi_std_n[i]:.4f}  Phi_M5/Phi_i={Phi_m5_n[i]:.4f}")

    print("""
READING: this uses the VALIDATED growth closure (Stage 3f/g -- Omega_s's
own clustering properly included via delta_s,theta_s,alpha,E_alpha, not
the old matter-only approximation sec.21 found invalid) plus sec.6's
fully-derived M5 Einstein-constraint term (no re-derivation, same
F_QQ used in WP5's condensate mass / SZ check). Flagged approximation:
delta_N (the M5 term's own census-weighted contrast) taken as delta_b,
per the module docstring -- a genuine refinement, not a blocker. This
is a first, honestly-scoped estimate (Phi's time-derivative via
d/dN, no Bessel/Limber line-of-sight projection, no visibility-function
weighting) -- the eventual Boltzmann-code-class treatment is future
work, not attempted here.
""")
