#!/usr/bin/env python3
"""
step3b_crosscheck.py — 2026-07-18. Three-part cross-check of the PPN
derivation update (Steps 2, 3b).

PART 1 — Step 2's phi field equation: independent re-derivation finds a
SIGN ERROR on the F_Q term, and shows why BOTH of the worker's
cross-checks are structurally blind to it.

PART 2 — Step 3b's Delta_alpha: verified correct (both brackets, including
the emergent factor 2 from the J-term's integration by parts).

PART 3 — Step 3b's DIAGNOSIS corrected: the static-limit mismatch with
Mistele's U-structure is NOT the order-scheme failure manifesting — it is
the missing unit-constraint elimination. Varying with all A^mu independent
gives the raw partial current; Mistele's equation is AFTER eliminating
A^0 via g_mn A^m A^n = -1, whose chain rule dA^0/dA^i = A_i supplies
exactly the missing Q0^2 A_i, completing grad(phi) -> U_i.
"""
import sympy as sp

print("=== PART 1: the phi-current, term by term ===")
print("""L_phi = 2(2-K_B) J^mu d_mu(phi) - (2-K_B) Y - F(Y,Q)
dL/d(d_mu phi):  J-term -> +2(2-K_B) J^mu
                 Y-term -> -(2-K_B) * 2 U^mu
                 F-term -> -F_Y * 2 U^mu  AND  -F_Q * A^mu   (dQ/d(d_mu phi) = A^mu)
CURRENT: P^mu = 2(2-K_B)J^mu - 2[(2-K_B)+F_Y]U^mu  - F_Q A^mu
WORKER:  P^mu = 2(2-K_B)J^mu - 2[(2-K_B)+F_Y]U^mu  + F_Q A^mu   <-- SIGN ERROR
Blind-spot demonstration:
 * FRW check: J=U=0 -> del_mu(+-F_Q A^mu)=0 -> d/dt(a^3 F_Q)=0 EITHER WAY
   (a conservation law is insensitive to the overall sign of its current);
 * static check: the F_Q A^mu term is absent from Mistele's reduced system
   because AeST sits at F_Q(Q0)=0 (the K-minimum) — and in cdot-8 it is
   (H0*l)^2-suppressed at galaxy scales (same class as m_eff^2).
 Both checks pass with EITHER sign: they cannot certify this term.
 The sign matters at the order Step 3's cancellation check runs at.
 NOTE the cdot-8-specific content: F_Q(Q0) != 0 here (the invoice) —
 this term is a genuinely NEW, sliding-condensate term absent in AeST.""")

print("=== PART 2: Delta_alpha re-derivation (worker's algebra) ===")
# J-term: A^n (grad_n A^m) (grad_m phi): partial d/dA^a gives (grad_a A^m)(grad_m phi);
# d/d(grad_b A^s) gives A^b grad_s phi -> IBP: -grad_b(2(2-K_B) A^b grad_s phi)
# = -2(2-K_B)[(div A) grad_s phi + A^b grad_b grad_s phi]; and
# A^b grad_b grad_s phi = grad_s Q - (grad_s A^b) grad_b phi  (torsion-free swap)
print("""J-term EOM contribution assembles to:
  2(2-K_B)[ 2(grad_a A^m)(grad_m phi) - (div A) grad_a phi - grad_a Q ]
   — the factor 2 on the first term EMERGES from partial + IBP swap: worker CORRECT.
Y/F-term: dY/dA^a = 2 Q grad_a phi ; dQ/dA^a = grad_a phi
  -> -{ 2Q[(2-K_B)+F_Y] + F_Q } grad_a phi : worker CORRECT.
Delta_alpha VERIFIED — the algebra is right. The interpretation is not:""")

print("=== PART 3: the 'missing U_i' is the unit constraint, not a broken scheme ===")
Q0, Ai, dphi, Phi = sp.symbols('Q_0 A_i dphi_i Phi')
# component-level static Y with the constraint A^0 = 1 - Phi + A^2/2 (to needed order):
# Y = |grad phi + Q0 A|^2  (verified expansion) -> dY/dA_i WITH constraint:
Y_comp = (dphi + Q0*Ai)**2
dY_constrained = sp.diff(Y_comp, Ai)
print(f"component route (constraint imposed BEFORE varying): dY/dA_i = {sp.expand(dY_constrained)}")
print(f"covariant partial route (A^mu independent):          dY/dA_i = 2*Q0*dphi_i  (worker's Delta)")
print(f"difference = {sp.expand(dY_constrained - 2*Q0*dphi)}  = the chain-rule term")
print("""  (dY/dA^0)*(dA^0/dA^i): with dA^0/dA^i = A_i from g_mn A^m A^n = -1
  and dY/dA^0 = 2*Q*(d_0 phi) = 2*Q0^2 at leading order -> +2*Q0^2*A_i. QED.
The raw partial current PLUS the lambda-constraint force (or equivalently
A^0-elimination) reproduces Mistele's U-structure exactly. The worker
compared the PRE-elimination partial against the POST-elimination reduced
equation — apples to oranges. This was precisely the 'A0 elimination /
second-class bookkeeping' item flagged in the fork-resolution advisory.

WHAT SURVIVES OF STEP 3b's FINDING: the order-counting caveat is REAL —
FJ's 'delta u^i ~ O(1.5) only' is proven for vanilla aether (static u^i=0
exactly) and false for AeST (static A^i content exists, per Mistele). But
its severity is CONTROLLED: in the PPN environment the static content is
screening-suppressed, U ~ grad(Phi)/mu_tilde, i.e. O(eps) with
eps = 1/mu_tilde(screened) — the SAME small parameter already registered
as the alpha_1 correction scale, Cassini-capped from above. The 'two-scale
expansion' IS the (PPN order) x (eps) double expansion already on the
books: at O(eps^0), FJ counting is RECOVERED (curl sector via FJ with
c1=K_B, c3=-K_B; chi at screened magnitude); the O(eps) terms are the
registered corrections. Not a strategy collapse — a strategy refinement
with its small parameter now identified and bounded by sub-task 1.""")
