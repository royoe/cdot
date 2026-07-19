#!/usr/bin/env python3
"""
ppn_fork_resolution.py — 2026-07-18. Structural resolution of the §5b fork:
does delta-phi participate at the momentum-flux-sourced PPN order?

THE CHANNEL IS DIRECT, NOT INDIRECT. Expand AeST's own Y-invariant,
Y = (g^mn + A^m A^n) d_m phi d_n phi, on the aligned background
(A = dt + perturbation, phi = Q0*t + dphi) to quadratic order in
{dphi, A_i, g_0i}. The longitudinal-sector gradient terms assemble into
ONE object: U_i = d_i(dphi) + Q0*(A_i + g_0i-part) — exactly the static
U = grad(phi) + Q0*A the worker already quoted from Mistele Eq.(1) in §4,
now seen as the momentum-flux-order carrier. The metric's g_0i (the
worker's conjectured indirect channel) enters INSIDE the same combination.

Below: (1) the rank structure that makes the vanilla singularity an
artifact; (2) the invertibility statement; (3) the screening-regime
check for pulsar systems; (4) the pre-registered value structure.
"""
import numpy as np, sympy as sp

print("=== (1) Longitudinal gradient sector from the Y-term: rank check ===")
Q0, cY = sp.symbols('Q_0 c_Y', positive=True)
# quadratic form in (d_i dphi, A_i^long) from c_Y * U_i U^i:
M = cY*sp.Matrix([[1, Q0],[Q0, Q0**2]])
print(f"gradient matrix (dphi, A_long) = c_Y * [[1, Q0],[Q0, Q0^2]];  det = {sp.simplify(M.det())}, rank = {M.rank()}")
print("""rank 1: ONLY the combination U (equivalently chi = dphi + Q0*alpha,
SZ's own healthy-mode variable) has a gradient operator; the orthogonal
combination is eliminated by the unit-timelike constraint / second-class
sector, NOT solved by inverting a gradient operator. Vanilla ae-theory's
c_123-denominator solution inverts an operator for a mode that, in AeST,
does not exist as a separate degree of freedom -> the singularity at
c_123 = 0 is an artifact of integrating out a non-mode.""")

print("=== (2) Invertibility of what actually carries the source ===")
print("""U's stationary operator is c_Y * div(...grad) with c_Y = the Y-sector
coefficient: (2-K_B)*lambda_s-type in the screened/tracking regime,
J'(Y) in the MOND regime — nonzero everywhere except the Y->0 point.
Rigor anchor (no new derivation needed): SZ's Minkowski stability
spectrum (PRD 106, 104041 — fetched, already load-bearing in WP5) is
non-degenerate for K_B in (0,2) and admissible lambda_s: an invertible
quadratic form on Minkowski IS the statement that the stationary PPN
elliptic system has unique solutions for generic momentum-flux sources.
=> alpha_1, alpha_2 EXIST AND ARE FINITE. Fork resolves in the
pre-registered direction — by construction, not by luck.""")

print("=== (3) Pulsar systems sit deep in the screened regime ===")
G, Msun = 6.674e-11, 1.989e30
a_orb = G*1.5*Msun/(1.0e9)**2   # PSR-class: ~1.5 Msun companion, r ~ 1e6 km
print(f"orbital acceleration ~ {a_orb:.0f} m/s^2  vs  a0 ~ 1.2e-10 m/s^2:"
      f"  x ~ {a_orb/1.2e-10:.1e} -> deeply screened;")
print("the c_Y entering alpha_1's completion is the SCREENED coefficient —")
print("sub-task 1's Cassini lower bound on screening and sub-task 2's PPN")
print("values are COUPLED through the same object.\n")

print("=== (4) Pre-registered value structure (hedged; derivation still owed) ===")
print("""alpha_1 = -4*c_14(K_B) + O(Q0^2/c_Y_screened) corrections:
 - strong-screening limit: chi is stiff, its alpha_1 contribution
   suppressed ~ 1/lambda_s -> ae-theory form recovered with c_14 ~ K_B
   (normalization c_1 <-> K_B still unpinned — worker's flag stands;
   the staged derivation must pin it before any number is quoted);
 - alpha_2: finite by (2); value requires the full anisotropic sector.
ENDGAME SHAPE: |alpha_1| <~ 1e-5 (pulsar/LLR class) would then bound K_B
at ~1e-5-ish IF the leading form survives — survivable for cdot-8
(mu_eff depends on K_B only through 2-K_B; m_x -> infinity is Mistele's
phenomenologically-quiet limit except wide binaries) but a REAL
constraint. Pre-registered as shape, not asserted as value.""")
