#!/usr/bin/env python3
"""
m5_separate_universe_check.py — 2026-07-18. Running the k->0 consistency
check the worker's §5 correctly flagged as the next verification step —
before the next step, as requested.

THE CHECK: at k->0 (W->1), a uniform density perturbation is a shifted
background (separate-universe limit). The perturbed equation's M5 source
must therefore equal the derivative of the BACKGROUND M5+scalar
contribution to H^2 along the constraint:
    background:  H^2 ⊃ -F/3 + Q F_Q/2,   with  Q = q(N_tot)  enforced.
    response to dN:  dQ = q' dN, then
    d[-F/3 + Q F_Q/2] = [ -F_Q/3 + (F_Q + Q F_QQ)/2 ] dQ
                      = [ F_Q/6 + Q F_QQ/2 ] q' dN.       (*)

THE WORKER'S ASSEMBLED TERM: 8πG Λ_M q' W [δ_tot - 3Φ] with
Λ_M = N a^3 F_Q / 16π G̃  ->  in H^2-units the coefficient is (F_Q/2) q'.

VERDICT: (F_Q/2) q'  !=  (F_Q/6 + Q F_QQ/2) q'   — the check FIRES.
"""
import sympy as sp

FQ, FQQ, Q, qp, dN = sp.symbols('F_Q F_QQ Q qprime deltaN', real=True)

background_response = (FQ/6 + Q*FQQ/2)*qp*dN          # (*) the required k->0 value
worker_term        = (FQ/2)*qp*dN                      # Lambda_M q' channel alone
missing            = sp.simplify(background_response - worker_term)
print(f"required k->0 coefficient : (F_Q/6 + Q F_QQ/2) q'")
print(f"worker's assembled term   : (F_Q/2) q'")
print(f"MISSING                   : {sp.factor(missing/dN/qp)} * q' * deltaN")
print("""
DIAGNOSIS — where the missing pieces live:
 1. dΛ_M channel: Λ_M = N a^3 F_Q/16πG̃ is FIELD-DEPENDENT through F_Q(Q).
    The perturbed constraint drags the windowed Q: dQ = q' dN — so
    dΛ_M ∝ a^3 F_QQ dQ. Varying at fixed Λ_M gives a legitimate PARTIAL
    contribution; the ASSEMBLED equation must carry dΛ_M too:
      supplies  +(Q F_QQ/2) q' dN.
 2. dF channel: the -F/3 term in H^2 responds as -F_Q/3 dQ:
      supplies  -(F_Q/3) q' dN,  and  F_Q/2 - F_Q/3 = F_Q/6. ✓
 Together: (F_Q/2 - F_Q/3 + Q F_QQ/2) q' dN = (F_Q/6 + Q F_QQ/2) q' dN — 
 exactly (*). The worker's direct term is one of three channels; the other
 two are the SAME dQ = q' dN propagating through F and F_Q everywhere
 they appear. Nothing new is needed — only the propagation carried
 consistently.

NOTABLE: F_QQ appears — the SAME quadrature curvature that gave WP5's
m_eff and passed SZ's stability sign check. Third appearance of one
object: the condensate mass, the perturbed-constraint feedback, and (per
WP5) the sign stability all draw on F_QQ(Q0). Numerically today:
F_QQ = -0.696, F_Q from the trajectory — the Q F_QQ/2 piece is NOT
small relative to F_Q/6; omitting it is an O(1) error in the new term,
not a refinement.

BOOKKEEPING FLAG (second, smaller): dN = N̄_tot-weighted — the assembled
equation as written carries Λ_M q' W [δ_tot - 3Φ] with the N̄_i factors
folded into 'species weights'; make the N̄_tot factor explicit so the
k->0 check can be run numerically without ambiguity:
    δN_tot = Σ_i N̄_i W(kR_h) [δ_i - 3Φ].
""")
