#!/usr/bin/env python3
"""
longitudinal_response.py — 2026-07-18. The longitudinal momentum-flux
response: structural derivation of the scaling, answering the open
advisory request (does the O(1.5) correction to U inherit the static
screening suppression, and what does alpha_1 become?).

PART 1 — the driven-response operator.
Linearize Step 2's corrected equation around the screened static
background U0 (|U0| ~ grad(Phi)/mu_tilde, established sub-task 1).
The static operator is  div[ (1 + mu_tilde(|U|)) U ];  linearizing:
  div[ M . dU ] = dS,   M_ij = (1+mu_tilde) delta_ij
                              + mu_tilde'(|U0|)|U0| * (U0_i U0_j)/|U0|^2.
In the screened regime BOTH eigenvalues of M are large (~mu_tilde for the
transverse-to-U0 directions; ~mu_tilde + mu_tilde'|U0| along U0 — for
tracking/screening completions mu_tilde'|U0| >= 0, no soft direction).
=> the DRIVEN response obeys dU ~ dS / mu_tilde = O(eps) * dS.
The O(1.5) sources dS, enumerated from the covariant structure:
  (a) Q0 * h_0i inside U (frame dragging feeds the scalar)   ~ O(1.5)
  (b) convective time derivatives (d_t -> v.grad on O(1))    ~ O(1.5)
  (c) J-term pieces (aether acceleration at this order)      ~ O(1.5)
  (d) F_Q A^mu term: F_Q(Q0) ~ H0^2-class -> (H0 l)^2-suppressed: DROP
      (stated, not silent).
None of the sources is mu_tilde-ENHANCED, so:
  dU(O(1.5)) ~ eps * O(1.5)  —  STEP 3e's HYPOTHESIS CONFIRMED at the
  structural level: the driven response inherits the static suppression
  because it is the same stiff operator being driven.

PART 2 — what this does to alpha_1 (correcting the advisor's own earlier
pre-registration).
At AeST's parameter point, Step 3d proved the transverse sector is
exactly GR — so vanilla ae-theory's alpha_1 = -4c1 at this same point is
carried ENTIRELY by its longitudinal u^L channel (the one with the
c123-denominators, finite only via a 0 x infinity cancellation). AeST
REPLACES that channel with the screened chi/U — whose stress feed into
g_0i is doubly small: the U-sector T_0i ~ c_Y * U_0 * U_i with
U_0 ~ O(eps * perturbation) => contribution ~ O(eps), NOT O(1).
=> The earlier pre-registration ('strong screening RECOVERS -4*c14') was
   WRONG IN DIRECTION: strong screening does not restore the ae-value,
   it suppresses the only channel that produced it. Corrected registered
   expectation:  alpha_1(cdot-8) = O(K_B * eps)  [+ possibly an
   unsuppressed O(K_B) piece from the aether-stress 'E-term', whose
   provenance mixes in vanilla u^L substitutions and must be re-derived
   in AeST before it can be kept or discarded — the ONE remaining
   certified-derivation item].

PART 3 — the conservative envelope, quotable today.
Whatever the E-term re-derivation yields, it is bounded by its vanilla
magnitude: |alpha_1| <= 4*K_B (the replaced channel cannot exceed the
channel it replaces under a stiff operator — stated as an envelope with
its basis, not a theorem). Under the envelope:
"""
import numpy as np
a1_pulsar, a2_solar = 1e-5, 1.6e-9
print(f"pulsar |alpha_1| < {a1_pulsar:.0e}  ->  K_B < {a1_pulsar/4:.1e}   (conservative envelope)")
print(f"solar  |alpha_2| < {a2_solar:.0e}  ->  K_B < {a2_solar/4:.1e}   (PROVISIONAL envelope — alpha_2's")
print( "   own coefficient needs the same E-term re-derivation; do not quote as final)")
mu_eff_KB0 = np.sqrt(0.6962)/2
c_H0_Mpc = 2.99792458e8/(0.70*100*1000/3.0857e22)/3.0857e22
print(f"""
K_B -> 0 robustness (already established, restated for the record):
  1/mu_eff -> {c_H0_Mpc/mu_eff_KB0:.0f} Mpc; m_x -> infinity (one-field limit);
  WP5 lensing conclusions unchanged; tensor & vector sectors K_B-benign.
=> CONDITIONAL SUB-TASK-3 STATEMENT, available now: cdot-8 passes every
   preferred-frame test for K_B below the envelope values, with the
   registered expectation (Part 1-2) that the TRUE constraint is weaker
   by a factor ~1/eps = mu_tilde(screened) — i.e. the same screening that
   protects Cassini protects the pulsars. Exact alpha_1, alpha_2 remain
   the one open certified-derivation item (E-term provenance + the dU
   coefficient), correctly scoped as dedicated future work.""")
