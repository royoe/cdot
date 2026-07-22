#!/usr/bin/env python3
"""
wp7_r1_gradient_completion_feasibility.py -- 2026-07-21. R1 (per
Advisory-WP7-InstabilityRecourses-2026-07-21.md): a feasibility scan
for the F_Y(0,Q) small-gradient completion recourse, NOT a from-scratch
derivation -- see the honest caveat below before treating any number
here as validated.

WHAT IS RIGOROUS: the founding paper's own Minkowski-background
stability analysis (newRMONDLett.tex, "Stability and waves" section)
explicitly parametrizes F_Y = (2-K_B)*lambda_s (its own free parameter,
already named "additional free parameter to LCDM" in the paper's own
cosmology discussion), and states the vector/scalar sector is healthy
there iff 0<K_B<2 and lambda_s>-1, with the vector's own mass
M^2 = (2-K_B)(1+lambda_s)Q_0^2/K_B -- vanishing exactly at lambda_s=-1.

WHAT IS NOT YET DERIVED (the honest gap): the founding paper's own
COSMOLOGICAL (FRW, Newtonian-gauge) perturbation equations -- the
chi,gamma,alpha,E_alpha/delta,theta,Pi system this entire WP7 arc has
used -- were derived with Y=0 built in (Y is exactly zero on the FRW
background and was never carried as a free completion in the imported
equations). There is no existing primary-source derivation of how a
nonzero F_Y modifies THIS system. This script tests a STRUCTURAL
HYPOTHESIS, motivated by (not derived from) the Minkowski dispersion
relation's own lambda_s-dependence: that (2-K_B) -> (2-K_B)(1+lambda_s)
uniformly, wherever (2-K_B) appears in the E_alpha evolution equation's
own bracket (which is where R0(b) already isolated the destabilizing
term). A genuine action-level re-derivation of the FRW system with a
general F(Y,Q) is the necessary next step before this is more than a
plausibility/feasibility demonstration.

RESULT: under this hypothesis, moving lambda_s from 0 (bare AeST
default, i.e. cdot-8's current implicit assumption) toward -1 (but
staying STRICTLY inside the paper's own lambda_s>-1 healthy range)
suppresses the instability continuously and by many orders of
magnitude; lambda_s=-0.999 already stabilizes most of the tested
redshift range and lambda_s=-1 EXACTLY gives clean, k-independent
stability (Re(lambda)=-0.5) everywhere -- but lambda_s=-1 sits exactly
at the theory's own stated healthy-range BOUNDARY (vector mass -> 0
there), a real tension flagged, not resolved, here.
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


def aEE_aEalpha_lam(N, kappa, lam_s):
    """Structural hypothesis: (2-K_B) -> (2-K_B)*(1+lambda_s), matching
    the founding paper's own F_Y=(2-K_B)*lambda_s convention, applied
    uniformly within the E_alpha equation's own (2-K_B)[...] bracket
    (where R0(b) isolated the destabilizing Pi-feedback term)."""
    N = min(max(N, m.Nmin_g), m.Nmax_g)
    Hc, wv, cad2v, Qb, dKdQ, kap3 = m.coefs(N, kappa)
    KBg = (2 - K_B) * (1 + lam_s)
    dchi_dalpha = Qb
    dPi_dEalpha = kap3 * K_B
    dPi_dalpha = kap3 * KBg * dchi_dalpha
    a_EE = (-(KBg) * (Qb / (1 + wv) * dPi_dEalpha)) / (K_B * Hc) - 1.0
    a_Ealpha = (dKdQ * dchi_dalpha - KBg * (Qb / (1 + wv) * dPi_dalpha
                + (Hc + Qb) * dchi_dalpha - 3 * cad2v * Hc * Qb)) / (K_B * Hc)
    return Hc, a_EE, a_Ealpha


if __name__ == '__main__':
    k_Mpc = 2.71e-3
    zs = [1090, 100, 10, 1, 0.0]
    print(f"{'lambda_s':>10}  " + "  ".join(f"z={zt:>6}" for zt in zs)
          + "   [(2-K_B)(1+lambda_s)]")
    for lam_s in (0.0, -0.5, -0.9, -0.99, -0.999, -1.0, -1.001, -1.5, 1.0, 10.0):
        row = []
        for zt in zs:
            N = -np.log(1 + zt)
            kap = (k_Mpc * m.c0H0_Mpc / np.exp(N))**2
            Hc, a_EE, a_Ea = aEE_aEalpha_lam(N, kap, lam_s)
            J = np.array([[0.0, 1.0 / Hc], [a_Ea, a_EE]])
            row.append(np.max(np.linalg.eigvals(J).real))
        print(f"{lam_s:>10.3f}  " + "  ".join(f"{v:8.3f}" for v in row)
              + f"   [{(2 - K_B) * (1 + lam_s):.4f}]")

    print("""
VERDICT (feasibility only, not a validated fix -- see module docstring):
under the stated structural hypothesis, lambda_s safely inside the
founding paper's own healthy range (lambda_s>-1) but close to -1
(e.g. -0.999) suppresses the instability by 3-6 orders of magnitude and
fully stabilizes most of the tested range; lambda_s=-1 exactly gives
clean stability everywhere but sits exactly at the paper's own stated
healthy-range BOUNDARY (vector mass M^2 -> 0 there) -- a real tension,
flagged not resolved. Genuine next step: derive, from the action, how
F_Y(0,Q) actually enters the FRW cosmological system (not yet done
anywhere in the primary literature or this program) before treating any
specific lambda_s choice as a validated recourse.
""")
