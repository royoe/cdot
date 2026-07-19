#!/usr/bin/env python3
"""
q_definition_adjudication.py — 2026-07-18. Adjudication of §9's ambiguity:
what does Q in the M5 constraint mean at perturbative order?

READING (A) — all-space zero mode: RULED OUT, three grounds.
 (i) Non-Machian: an all-space average is acausal; the charter's founding
     principle is local c set by the HORIZON census. (ii) Incoherent
     pairing: one equation relating an all-space average to a horizon-ball
     integral mixes two domains. (iii) Internally inconsistent with
     §4-§6: the SAME S_M5, varied w.r.t. the metric/densities, produced a
     windowed delta-N term — varying it w.r.t. phi cannot consistently see
     a windowless Q.

READING (B) — horizon-ball average, same ball as N: ADOPTED. Both sides
of the constraint are integrals of local fields over the SAME domain, so
every mode's contribution to EACH side carries the same W(kR_h). One
caveat carried: a ball needs a center — at perturbative order the
constraint is fiducial-observer-anchored (operationally OUR ball for OUR
observables); translation-invariance at perturbative order joins the
census gauge flag as a named covariant-completion open item.

CONSEQUENCE — §7's cancellation is exact ONLY at k -> 0.
The bulk phi-current carries the LOCAL term -F_Q A^mu (windowless).
The M5 contribution to delta-phi_k's equation is +F_Q W(kR_h) (A-structure)
[Lambda_M = a^3 N F_Q/16pi G-tilde is extensive over the fiducial ball, so
Lambda_M x (W/V_ball) = F_Q-density x W — the WP5 mechanism at finite k].
NET term in phi_k's equation:   -F_Q (1 - W(kR_h)) x (A-structure).
  k -> 0:  W -> 1, exact cancellation — reproduces the background
           identity (the constraint absorbs the background F_Q current,
           which IS WP3's Lambda_M = a^3 N F_Q relation). CHECK.
  k finite: the sliding-condensate term SURVIVES, weighted (1-W).
Magnitude vs the mode's own gradient term (k/a)^2 chi:
  ratio ~ F_Q (1-W) / (k/a)^2  ~  (aH/k)^2 (1-W)   [F_Q ~ H0^2-class]
"""
import numpy as np
W = lambda x: 3*(np.sin(x)-x*np.cos(x))/x**3
print(f"{'kR_h':>8} {'1-W':>9} {'(aH/k)^2(1-W) ~ term ratio':>28}")
for x in [0.3, 1.0, 3.0, 6.0, 20.0, 1e3]:
    ratio = (1/x**2)*(1-W(x))   # aH ~ 1/R_h-class at horizon scales
    print(f"{x:>8} {1-W(x):>9.3f} {ratio:>28.2e}")
print("""
READING OF THE TABLE:
 sub-horizon (kR_h >> 1): the surviving term is (aH/k)^2-suppressed —
   the SAME (H l)^2-class sliding-condensate suppression already
   established in the PPN sector (WP6 Step 2's -F_Q A^mu term): local
   physics is untouched, consistent with WP5. The founding-paper system
   imports unmodified SUB-HORIZON — §7's practical conclusion survives
   there.
 horizon scales (kR_h ~ 1-6): the term is O(0.1-1) relative to the
   gradient terms — M5 touches the FIELD equation too, not only the
   Einstein constraint, in exactly the low-l window, with the same
   W-architecture and the same F_Q/F_QQ-class coefficients as §6's term.
   The low-l sector now has BOTH halves of its M5 structure.
CORRECTED §7 STATEMENT: 'phi's equation is unmodified by M5' holds
sub-horizon (to (aH/k)^2) and at k=0 exactly; at kR_h <~ few it is
modified by -F_Q(1-W)(A-structure) — required, not optional, for the
low-l derivation.
ONE MORE CHANNEL FLAGGED for the assembly: N's census weights (E_P,
the p_i^sp exponents) may themselves depend on the local Q — a
delta-Q-proportional piece of delta-N that renormalizes coefficients
within the same window architecture. To be included or excluded
explicitly in the assembly, not silently.
""")
