#!/usr/bin/env python3
"""
wp7_stage3g_full_system_stability_audit.py -- 2026-07-20/21. Checks the
item both the secondary advisor and I have flagged repeatedly but never
confirmed: does the FULL 6-variable system
(delta_b, theta_b, delta_s, theta_s, alpha, E_alpha) have any growing
direction OTHER than the already-audited (alpha, E_alpha) one?

The advisor's own attempt (a rough finite-difference Jacobian on
wp7_stage3d_hybrid_closure.py's rhs_full) was explicitly flagged as not
precise enough to trust, given the huge range of coefficient magnitudes
in this system (Qbar ~ 10^3, kappa ~ 10^0-10^5, etc. -- finite
differences lose precision badly here).

This script instead builds the Jacobian ANALYTICALLY. The full system
(rhs_full in wp7_stage3e_riccati_handoff.py / wp7_stage3_field_variable.py)
is LINEAR in the 6 state variables at fixed N (all N-dependence is in
the background-trajectory coefficients, not in the state) -- so the
Jacobian can be written down exactly, term by term, with no finite-
difference error at all. This directly resolves the advisor's precision
concern.
"""
import numpy as np
import importlib.util
import sys

spec = importlib.util.spec_from_file_location(
    'm', 'wp7_stage3e_riccati_handoff.py')
m = importlib.util.module_from_spec(spec)
sys.modules['m'] = m
src = open('wp7_stage3e_riccati_handoff.py').read().split("if __name__")[0]
exec(compile(src, 'wp7_stage3e_riccati_handoff.py', 'exec'), m.__dict__)

K_B = m.K_B


def full_jacobian_analytic(N, kappa):
    """Exact 6x6 Jacobian of rhs_full, state order
    (delta_b, theta_b, delta_s, theta_s, alpha, E_alpha).
    Derived by hand from rhs_full's own linear structure (every term is
    linear in the state at fixed N) -- verified against a high-precision
    (mpmath-free, but rtol/atol-tight) finite difference below before
    trusting it for the scan."""
    N = min(max(N, m.Nmin_g), m.Nmax_g)
    Hc, wv, cad2v, Qb, dKdQ, kap3 = m.coefs(N, kappa)
    Omb = float(m.Omb_i(N)); Oms = float(m.Oms_i(N))

    J = np.zeros((6, 6))
    # index: 0=delta_b, 1=theta_b, 2=delta_s, 3=theta_s, 4=alpha, 5=E_alpha

    # Row 0: ddb/dN = -kappa*theta_b/Hc
    J[0, 1] = -kappa/Hc

    # Row 1: dtb/dN = Psi/Hc = -1.5*(Omb*delta_b+Oms*delta_s)/(kappa*Hc)
    J[1, 0] = -1.5*Omb/(kappa*Hc)
    J[1, 2] = -1.5*Oms/(kappa*Hc)

    # Row 2: dds/dN = 3*(wv*delta_s - Pi) + (1+wv)*(-kappa*theta_s/Hc)
    # Pi = cad2v*delta_s + kap3*K_B*Ealpha + kap3*(2-K_B)*Qb*theta_s + kap3*(2-K_B)*Qb*alpha
    J[2, 2] = 3*wv - 3*cad2v
    J[2, 3] = -3*kap3*(2-K_B)*Qb - (1+wv)*kappa/Hc
    J[2, 4] = -3*kap3*(2-K_B)*Qb
    J[2, 5] = -3*kap3*K_B

    # Row 3: dts/dN = 3*cad2v*theta_s + (Pi/(1+wv) + Psi)/Hc
    # NOTE: the coded rhs divides Pi/(1+wv) by Hc too (not just Psi) --
    # caught via finite-difference cross-check below after an initial
    # transcription slip here.
    J[3, 0] = -1.5*Omb/(kappa*Hc)
    J[3, 2] = cad2v/((1+wv)*Hc) - 1.5*Oms/(kappa*Hc)
    J[3, 3] = 3*cad2v + kap3*(2-K_B)*Qb/((1+wv)*Hc)
    J[3, 4] = kap3*(2-K_B)*Qb/((1+wv)*Hc)
    J[3, 5] = kap3*K_B/((1+wv)*Hc)

    # Row 4: dalpha/dN = (Ealpha - Psi)/Hc
    J[4, 0] = 1.5*Omb/(kappa*Hc)
    J[4, 2] = 1.5*Oms/(kappa*Hc)
    J[4, 5] = 1.0/Hc

    # Row 5: dEalpha/dN (matches aEE_aEalpha's a_EE, a_Ealpha for the
    # alpha/Ealpha columns exactly; theta_s and delta_s columns are new)
    J[5, 2] = -(2-K_B)*Qb/(1+wv)*cad2v/(K_B*Hc)
    J[5, 3] = (dKdQ*Qb - (2-K_B)**2*Qb**2/(1+wv)*kap3 - (2-K_B)*(Hc+Qb)*Qb)/(K_B*Hc)
    J[5, 4] = (dKdQ*Qb - (2-K_B)**2*Qb**2/(1+wv)*kap3 - (2-K_B)*(Hc+Qb)*Qb
               + 3*(2-K_B)*cad2v*Hc*Qb)/(K_B*Hc)
    J[5, 5] = -(2-K_B)*Qb*kap3/((1+wv)*Hc) - 1.0

    return J


def full_jacobian_complexstep(N, kappa):
    """Complex-step differentiation -- exact to machine precision, no
    cancellation error regardless of coefficient magnitude (avoids the
    real-finite-difference precision loss the advisor's own rough check
    ran into, given Qbar~10^3, kappa~10^0-10^5 in this system). Used
    ONLY to validate the analytic Jacobian above, not as the trusted
    scan result itself."""
    h = 1e-30
    n = 6
    J = np.zeros((n, n))
    for j in range(n):
        y0 = np.array([1.0]*6, dtype=complex)
        y0[j] += 1j*h
        f = m.rhs_full(N, y0, kappa)
        J[:, j] = [np.imag(fi)/h for fi in f]
    return J


if __name__ == '__main__':
    k_Mpc = 1e-4

    print("=== Validate the analytic Jacobian against complex-step differentiation (exact to machine precision) ===")
    for zt in (100, 60, 40, 20, 5, 0.0):
        N = -np.log(1+zt)
        kap = (k_Mpc*m.c0H0_Mpc/np.exp(N))**2
        Ja = full_jacobian_analytic(N, kap)
        Jc = full_jacobian_complexstep(N, kap)
        resid = np.max(np.abs(Ja-Jc)/(np.abs(Ja)+np.abs(Jc)+1e-30))
        print(f"  z={zt:5}: max relative residual (analytic vs complex-step) = {resid:.3e}")

    print("\n=== Full 6x6 eigenvalue scan: any growing direction beyond the known vector-sector one? ===")
    zs = [100, 90, 80, 70, 60, 50, 45, 40, 35, 32, 30, 29, 25, 20, 18.5, 15, 10, 5, 2, 1, 0.5, 0.0]
    for zt in zs:
        N = -np.log(1+zt)
        kap = (k_Mpc*m.c0H0_Mpc/np.exp(N))**2
        J = full_jacobian_analytic(N, kap)
        eigs = np.linalg.eigvals(J)
        max_re = np.max(eigs.real)
        n_growing = np.sum(eigs.real > 1e-8)
        print(f"  z={zt:7.2f}: max Re(lambda)={max_re:10.4f}  #growing={n_growing}  "
              f"eigs={np.round(eigs,3)}")
