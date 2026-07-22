#!/usr/bin/env python3
r"""
wp7_r1_derived_completion.py -- 2026-07-21. The payoff of the
commissioned action-level derivation (Sections 5-15 of
Update-WP7-InstabilityRecourses-2026-07-21.md): re-tests R1's original
feasibility question (does an F_Y(0,Qbar) small-gradient completion
stabilize the vector sector at the ISW-relevant wavenumbers?) using the
ACTUALLY DERIVED modification, not either of the two earlier crude
attribution guesses (wp7_r1_gradient_completion_feasibility.py's
"uniform substitution," wp7_r1_refined_attribution.py's "refined
attribution").

WHAT WAS ACTUALLY DERIVED, and is used here directly (no guessing):

  - Section 10 (the coupled Euler-Lagrange variation, corrected to vary
    at fixed varphi, independently verified twice): the E_alpha
    equation's chi-coefficient gets EXACTLY one new term added,
    F_Y*phibardot*chi -- i.e. the modification is a clean ADDITIVE
    correction to the vector equation, confirmed to reproduce the
    published (F_Y=0) equation's leading structure exactly when this
    term is dropped.

  - Section 13 (the energy constraint, derived directly by varying the
    action w.r.t. Psi): Pi/delta's own bracket
    [K_B*E_alpha+(2-K_B)*chi] is CONFIRMED F_Y-INDEPENDENT -- Y has no
    Psi-dependence at all (Section 5), so F_Y*Y cannot contribute to
    the energy constraint. Pi's formula is therefore used UNMODIFIED
    here, exactly as coded in wp7_stage3e_riccati_handoff.py.

This means the actual, derived R1 completion is SURGICAL: it modifies
ONLY the E_alpha evolution equation (one new additive term), leaving
Pi, delta, theta all exactly as originally coded -- a sharp answer to
the program's original target-list item 1 ("does (2-K_B)->(2-K_B)(1+
lambda_s) hold in the FRW system?"): NO, not uniformly -- only the
E_alpha equation's chi-coefficient picks up the completion; Pi's own
bracket does not.

(A second, momentum-constraint-sourced F_Y term was found in Section 12
-- -2*F_Y*phibardot^2*partial_1(alpha) -- but its precise placement in
the coupled system was not pinned down there (unlike the vector
equation's own term, confirmed twice over). NOT included here; flagged
honestly as a possible second contribution this scan may be missing.)

METHOD: reuse the exact, already-validated aEE_aEalpha machinery
(coefs() from wp7_stage3e_riccati_handoff.py, unmodified), adding only
the new, derived a_Ealpha correction: -F_Y*Qbar^2/(K_B*Hc), using
F_Y=(2-K_B)*lambda_s (the founding paper's own parametrization,
Minkowski-background stability section, already verified).
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


def aEE_aEalpha_derived(N, kappa, lam_s):
    """The ACTUALLY-DERIVED R1 completion (Sections 10+13): Pi/delta's
    bracket is exactly the original, unmodified coefs()-based formula
    (a_EE and Pi's own alpha-dependence, dPi_dalpha, are UNCHANGED --
    Section 13 confirmed no F_Y-dependence there). The ONLY new piece
    is the vector equation's own additive F_Y*phibardot*chi term
    (Section 10), contributing -F_Y*Qbar^2/(K_B*Hc) to a_Ealpha."""
    N = min(max(N, m.Nmin_g), m.Nmax_g)
    Hc, wv, cad2v, Qb, dKdQ, kap3 = m.coefs(N, kappa)
    FY = (2 - K_B) * lam_s

    dPi_dEalpha = kap3 * K_B
    dPi_dalpha = kap3 * (2 - K_B) * Qb
    a_EE = (-(2 - K_B) * (Qb / (1 + wv) * dPi_dEalpha)) / (K_B * Hc) - 1.0
    a_Ealpha_base = (dKdQ * Qb - (2 - K_B) * (Qb / (1 + wv) * dPi_dalpha
                     + (Hc + Qb) * Qb - 3 * cad2v * Hc * Qb)) / (K_B * Hc)
    a_Ealpha = a_Ealpha_base - FY * Qb**2 / (K_B * Hc)
    return Hc, a_EE, a_Ealpha


if __name__ == '__main__':
    k_Mpc = 2.71e-3
    zs = [1090, 100, 10, 1, 0.0]
    print("Derived R1 completion -- vector equation only, Pi/delta UNCHANGED")
    print(f"{'lambda_s':>10}  " + "  ".join(f"z={zt:>6}" for zt in zs))
    for lam_s in (0.0, -0.5, -0.9, -0.99, -0.999, -1.0, -1.001, -1.5, 1.0, 10.0):
        row = []
        for zt in zs:
            N = -np.log(1 + zt)
            kap = (k_Mpc * m.c0H0_Mpc / np.exp(N))**2
            Hc, a_EE, a_Ealpha = aEE_aEalpha_derived(N, kap, lam_s)
            J = np.array([[0.0, 1.0 / Hc], [a_Ealpha, a_EE]])
            eig = np.linalg.eigvals(J)
            row.append(f"{max(eig.real):10.4g}")
        print(f"{lam_s:10.4g}  " + "  ".join(row))

    print()
    print("Comparison at z=1090, uniform substitution vs. refined attribution")
    print("vs. this derived completion, lambda_s=-1 (the previous rounds' most")
    print("favorable/most unfavorable test points):")
    for zt in [1090]:
        N = -np.log(1 + zt)
        kap = (k_Mpc * m.c0H0_Mpc / np.exp(N))**2
        for lam_s in (0.0, -1.0):
            Hc, a_EE, a_Ealpha = aEE_aEalpha_derived(N, kap, lam_s)
            J = np.array([[0.0, 1.0 / Hc], [a_Ealpha, a_EE]])
            eig = np.linalg.eigvals(J)
            print(f"  z={zt}, lambda_s={lam_s}: max Re(lambda) = {max(eig.real):.6g}")
