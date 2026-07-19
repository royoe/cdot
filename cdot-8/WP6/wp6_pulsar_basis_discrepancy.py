#!/usr/bin/env python3
"""
wp6_pulsar_basis_discrepancy.py -- 2026-07-18. Companion script for
Update-WP6-BinaryPulsar-2026-07-18.md.

(1) Derives the (c_theta, c_sigma, c_omega, c_a) <-> (c1, c2, c3, c4)
    dictionary from the standard kinematic decomposition of nabla_mu U_nu
    (Vaglio et al. 2026, arXiv:2605.01436, Eq. 1-4), evaluated at AeST's
    aether point (c1=K_B, c2=0, c3=-K_B, c4=0).
(2) Reproduces the resulting c_sigma=c_theta=c_a=0, c_omega=2*K_B result
    ("AeST's aether is pure vorticity").
(3) Demonstrates the UNRESOLVED discrepancy: Vaglio's own c_V^2 formula
    is singular at this point, while Foster-Jacobson's own vector-mode
    formula (gr-qc/0509083, already verified twice this session --
    Advisory-WP6-DictionaryCrossCheck-2026-07-18.md Route B, and
    Update-WP6-TensorSpeedStructure-2026-07-18.md Step 3d) gives a
    finite, healthy speed^2 = 1 at the SAME physical point.

NOT YET RESOLVED. Flagging for advisor cross-check per
Update-WP6-BinaryPulsar-2026-07-18.md.
"""
import sympy as sp

c1, c2, c3, c4, KB = sp.symbols('c1 c2 c3 c4 K_B')
sub = {c1: KB, c2: 0, c3: -KB, c4: 0}

print("=== (1) Kinematic-decomposition dictionary ===")
c_sigma = c1 + c3
c_omega = c1 - c3
c_theta = c1 + 3*c2 + c3
c_a = c4
print(f"c_sigma = c1+c3 -> {sp.simplify(c_sigma.subs(sub))}")
print(f"c_omega = c1-c3 -> {sp.simplify(c_omega.subs(sub))}")
print(f"c_theta = c1+3c2+c3 -> {sp.simplify(c_theta.subs(sub))}")
print(f"c_a = c4 -> {sp.simplify(c_a.subs(sub))}")
print("=> AeST's aether kinetic term is PURE VORTICITY at this point.\n")

print("=== (2) Vaglio's own mode speeds (arXiv:2605.01436, Eqs. cT/cV/cS) ===")
cT2 = 1/(1 - c_sigma)
cV2 = (c_sigma + c_omega - c_sigma*c_omega) / (2*c_a*(1 - c_sigma))
print(f"c_T^2 at AeST's point: {sp.simplify(cT2.subs(sub))}  (matches c13=0 tensor-speed result)")
cV2_num = sp.simplify((c_sigma + c_omega - c_sigma*c_omega).subs(sub))
print(f"c_V^2 numerator at AeST's point: {cV2_num}  (nonzero)")
print(f"c_V^2 denominator (2*c_a*(1-c_sigma)) at AeST's point: {sp.simplify((2*c_a*(1-c_sigma)).subs(sub))}  (ZERO)")
print("=> c_V^2 is a GENUINE POLE -- Vaglio's own vector-mode formula diverges here.\n")

print("=== (3) Foster-Jacobson's own vector-mode formula (gr-qc/0509083, Eq. 15) ===")
print("(already independently verified twice this session; reproduced here for direct")
print(" side-by-side comparison against Vaglio's formula, same physical point)")
c13, c14 = c1 + c3, c1 + c4
s1_sq = (2*c1 - c1**2 + c3**2) / (2*c14*(1 - c13))
print(f"FJ speed^2 (their normalization) at AeST's point: {sp.simplify(s1_sq.subs(sub))}")
print("""
DISCREPANCY: Vaglio's c_V^2 -> pole;  FJ's own vector-mode speed^2 -> 1 (finite, healthy).
Same physical point (c1=K_B, c2=0, c3=-K_B, c4=0), same physical mode (transverse/
vector), two primary sources' formulas disagree. NOT resolved -- could be:
  (a) an error in the (c_theta,c_sigma,c_omega,c_a) <-> (c1,c2,c3,c4) dictionary
      derived here (the c_a=c4 identification is solid; c_sigma/c_omega/c_theta
      less certain -- worth an independent re-derivation of the kinematic split);
  (b) a genuine difference in normalization/definition between the two papers'
      "vector mode speed" (e.g. relative to a different residual gauge freedom);
  (c) something else not yet identified.
Flagged for advisor cross-check per Update-WP6-BinaryPulsar-2026-07-18.md Sec 2.
""")
