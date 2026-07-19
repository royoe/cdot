#!/usr/bin/env python3
"""
pulsar_basis_resolution.py — 2026-07-18. Resolution of the c_V^2
discrepancy flagged in wp6_pulsar_basis_discrepancy.py.

THE ERROR: one dictionary entry. c_a = c4 is wrong; the standard (and
here re-derived) identification is  c_a = c1 + c4  (= c14 — the
combination the ae-theory literature writes everywhere, BECAUSE it is
the acceleration coefficient).

THE MECHANISM: the covariant derivative of the aether decomposes as
  nabla_a u_m = [theta/sigma/omega projected part] - u_a a_m,
so the c1 structure  nabla_a u_m nabla^a u^m  contains an INDUCED
acceleration-squared piece through the (u_a a_m) term — in the
ae-literature's mostly-minus convention (u^2=+1):
  c1-term = c1*[sigma^2 + omega^2 + theta^2/3]  +  c1*a^2.
The worker matched only the EXPLICIT u^a u^b (c4) term — the same
induced-vs-explicit blindness class as the earlier 'even metric
contractions' c4 slip. c2 (pure trace) and c3 (the a-part is (u.a)^2 = 0)
induce nothing.

Verification below: with c_a = c1+c4, Vaglio's own c_V^2 formula gives
EXACTLY 1 at AeST's point — identical to Foster-Jacobson's independently
verified spin-1 result. Both primary sources are right; the discrepancy
was the dictionary's.
"""
import sympy as sp

c1, c2, c3, c4, KB = sp.symbols('c1 c2 c3 c4 K_B')
sub = {c1: KB, c2: 0, c3: -KB, c4: 0}

print("=== induced-a^2 audit, structure by structure (u^2=+1 convention) ===")
print("""c1: nabla_a u_m nabla^a u^m = P^2 + (u.u)(a.a) = P^2 + a^2 -> induces +c1*a^2
c2: theta^2 (trace only; trace of -u_a a_m is -(u.a) = 0)   -> no a^2
c3: nabla_a u_m nabla^m u^a: a-part = (u.a)^2 = 0            -> no a^2
c4: explicit (u^a nabla_a u^m)(u^b nabla_b u_m) = a^2        -> +c4*a^2
=> c_a = c1 + c4  (= c14, the ae-literature's ubiquitous combination)""")

c_sigma, c_omega, c_theta = c1+c3, c1-c3, c1+3*c2+c3
c_a_corr = c1 + c4
print("\n=== corrected dictionary at AeST's point ===")
for name, expr in [("c_sigma", c_sigma), ("c_omega", c_omega),
                   ("c_theta", c_theta), ("c_a (corrected)", c_a_corr)]:
    print(f"{name:>16} = {sp.simplify(expr.subs(sub))}")
print("=> NOT pure vorticity: VORTICITY (2K_B) + ACCELERATION (K_B).")

print("\n=== the discrepancy dissolves ===")
cT2 = 1/(1-c_sigma)
cV2 = (c_sigma + c_omega - c_sigma*c_omega)/(2*c_a_corr*(1-c_sigma))
s1_sq = (2*c1 - c1**2 + c3**2)/(2*(c1+c4)*(1-(c1+c3)))
print(f"Vaglio c_T^2 at AeST's point: {sp.simplify(cT2.subs(sub))}")
print(f"Vaglio c_V^2 (corrected c_a): {sp.simplify(cV2.subs(sub))}")
print(f"Foster-Jacobson spin-1:       {sp.simplify(s1_sq.subs(sub))}")
print("""THREE-WAY AGREEMENT: c_T^2 = c_V^2 = FJ spin-1 = 1 exactly.
Both primary sources correct; one dictionary entry was the whole story.
BONUS COHERENCE: c14 = c_a means the earlier alpha_1 = -4*K_B reads as
alpha_1 = -4*c_a — preferred-frame effects couple to the ACCELERATION
coefficient, exactly as they physically should. AeST's line in Vaglio's
{alpha_1, alpha_2, c_omega} space is (c_omega, c_a) = (2K_B, K_B).""")
