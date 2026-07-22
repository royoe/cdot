#!/usr/bin/env python3
"""
wp7_r1_refined_attribution.py -- 2026-07-21. Applies the secondary
advisor's sharpening (Advisory-WP7-YIdentityDerivationReviewed-2026-07-21.md,
sec.5) to R1's feasibility scan: since the new F_Y(0,Qbar)*Y term is
functionally identical to the bare -(2-K_B)*Y term already in the
action (same Y, different coefficient -- confirmed, wp7_derivation_Y_identity.py),
its contribution to the field equations must have EXACTLY the same
functional form as the bare Y-term's own contribution, scaled by
lambda_s alone. This narrows "does (2-K_B)->(2-K_B)(1+lambda_s) hold
uniformly" (R1's original, cruder hypothesis) to a bounded attribution
question: WHICH occurrences of (2-K_B) in Pi/E_alpha trace to the bare
Y-term (a pure spatial-gradient/Laplacian structure) versus the
separate J^mu*nabla_mu phi term (the aether's own covariant
ACCELERATION -- a Hubble-friction/mass-type structure, no spatial
Laplacian at all)?

CRITERION APPLIED: (2-K_B) occurrences INSIDE Pi's own
nabla^2[K_B*E_alpha+(2-K_B)*chi] bracket (a genuine Laplacian
structure) trace to the bare Y-term -> get the lambda_s correction.
The OUTER (2-K_B) in the E_alpha equation, multiplying a bracket built
from (H+phibar_dot)*chi and 3*c_ad^2*H*phibar_dot*alpha (no nabla^2
anywhere -- a friction/mass-type structure) traces to J^mu*nabla_mu phi
-> stays bare, uncorrected.

RESULT: under this refined attribution, the Pi-feedback term (R0(b)'s
"B") becomes LINEAR (not quadratic) in (1+lambda_s) -- but the
instability barely responds to lambda_s at all, because the Jacobian's
own TRACE (a_EE) is dominated by a DIFFERENT term (the K_B*E_alpha
piece of Pi, times the now-uncorrected OUTER (2-K_B)) that is NEVER
touched by lambda_s under this hypothesis. A large, fixed, positive
trace alone forces a large positive eigenvalue regardless of what the
off-diagonal (lambda_s-sensitive) entry does.

STATUS: this is a MUST-REPORT DIVERGENCE from the original "uniform
substitution" test (wp7_r1_gradient_completion_feasibility.py), not a
resolved answer -- both hypotheses are structurally motivated, neither
is rigorously derived from the action. See the write-up (Update-WP7-
InstabilityRecourses-2026-07-21.md sec.6) for the full honest framing.
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


def aEE_aEalpha_refined(N, kappa, lam_s):
    """Refined attribution: only the (2-K_B) INSIDE Pi's own nabla^2[...]
    bracket (source 1, the bare Y-term) gets (2-K_B)->(2-K_B)(1+lambda_s).
    The OUTER (2-K_B) multiplying the E_alpha equation's whole bracket
    (source 2, the J^mu nabla_mu phi friction/acceleration term) stays bare."""
    N = min(max(N, m.Nmin_g), m.Nmax_g)
    Hc, wv, cad2v, Qb, dKdQ, kap3 = m.coefs(N, kappa)
    KB2_inner = (2 - K_B) * (1 + lam_s)   # Y-sourced, corrected
    KB2_outer = (2 - K_B)                  # J-sourced, uncorrected
    dchi_dalpha = Qb
    dPi_dEalpha = kap3 * K_B               # the K_B*E_alpha piece of Pi -- no (2-K_B) at all
    dPi_dalpha = kap3 * KB2_inner * dchi_dalpha
    a_EE = (-(KB2_outer) * (Qb / (1 + wv) * dPi_dEalpha)) / (K_B * Hc) - 1.0
    a_Ealpha = (dKdQ * dchi_dalpha - KB2_outer * (Qb / (1 + wv) * dPi_dalpha
                + (Hc + Qb) * dchi_dalpha - 3 * cad2v * Hc * Qb)) / (K_B * Hc)
    return Hc, a_EE, a_Ealpha


if __name__ == '__main__':
    k_Mpc = 2.71e-3
    zs = [1090, 100, 10, 1, 0.0]
    print(f"{'lambda_s':>10}  " + "  ".join(f"z={zt:>6}" for zt in zs))
    for lam_s in (0.0, -0.5, -0.9, -0.99, -0.999, -1.0, -1.001, -1.01, -1.1, -1.5, -2.0):
        row = []
        for zt in zs:
            N = -np.log(1 + zt)
            kap = (k_Mpc * m.c0H0_Mpc / np.exp(N)) ** 2
            Hc, a_EE, a_Ea = aEE_aEalpha_refined(N, kap, lam_s)
            J = np.array([[0.0, 1.0 / Hc], [a_Ea, a_EE]])
            row.append(np.max(np.linalg.eigvals(J).real))
        print(f"{lam_s:>10.3f}  " + "  ".join(f"{v:14.3f}" for v in row))

    print("\n=== Diagnostic: a_EE (trace) vs a_Ealpha (off-diagonal) separately at z=1090 ===")
    N = -np.log(1091)
    kap = (k_Mpc * m.c0H0_Mpc / np.exp(N)) ** 2
    for lam_s in (0.0, -1.0, -2.0):
        Hc, a_EE, a_Ea = aEE_aEalpha_refined(N, kap, lam_s)
        print(f"  lambda_s={lam_s}: a_EE={a_EE:.4e} (trace, unaffected)  a_Ealpha={a_Ea:.4e} (responds strongly)")
    print("\nVerdict: a large, fixed, positive trace alone forces a large positive")
    print("eigenvalue regardless of lambda_s -- the dominant high-z driver, under")
    print("this refined attribution, is NOT the term R1 targets at all.")
