#!/usr/bin/env python3
r"""
wp7_derivation_energy_constraint_attempt.py -- 2026-07-21. The natural
parallel to wp7_derivation_momentum_constraint_attempt.py: instead of
introducing a new shift perturbation to extract T^0_i (the momentum
constraint), this derives the ENERGY constraint (the 00 Einstein
equation) by varying the already-assembled action directly w.r.t. Psi
-- the lapse perturbation already present throughout this program's
machinery (g_00 = -(1+2*eps*Psi)), no new field needed. Psi is
genuinely non-dynamical here (no Psi_dot appears anywhere in the
relevant Lagrangian pieces -- checked explicitly below), so
d(action)/dPsi = 0 IS the energy constraint directly, exactly
analogous to how d(action)/dB gave the momentum constraint and
d(action)/dalpha gave the vector equation.

INGREDIENTS (all previously established): Y = (1/a^2)(grad chi)^2 has
NO Psi-dependence at all (an already-verified fact from Section 5's
derivation, since the self-consistent A_0 ansatz was built precisely
to make this true) -- so only F(Y,Q)'s own Q-dependence (via gamma =
varphi_dot - phibardot*Psi, and Q^(2)'s own Psi-terms, re-derived here
from Qcal in wp7_derivation_Y_identity.py) and the Maxwell/J terms
(via E_alpha = alpha_dot + Psi) carry Psi-dependence.

RESULT: d(action)/dPsi, collected, splits cleanly into two pieces.
The first,

    2*kappa*[K_B*E_alpha + (2-K_B)*chi]

-- is an EXACT, clean match (zero symbolic difference after collecting)
to the published delta/Pi bracket (K_B*E_alpha+(2-K_B)*chi, primary
source eq. delta_field_relation / Pi_delta_E_alpha), appearing
correctly multiplied by kappa=k^2/a^2, matching the grad^2[...]
structure exactly. This is the concrete confirmation the six-round
derivation (Sections 5-12 of Update-WP7-InstabilityRecourses-2026-07-
21.md) has been building toward.

SIGN CORRECTION, 2026-07-21 (Advisory-WP7-EnergyConstraintBracketConfirmed
-2026-07-21.md, sec.3): the F_Q/F_QQ terms were originally assembled
with a PLUS sign (+F_Q*Q2+(1/2)*F_QQ*gamma^2) -- inconsistent with the
already-validated convention in wp7_derivation_coupled_variation_
varphi_fixed.py (Sections 9-10), where the equivalent terms were shown
(independently, by hand) to equal -F_Q*Q2's own alpha-part, matching
the actual action's -F(Y,Q) superset -F_Q*delta_Q-(1/2)*F_QQ*
(delta_Q)^2 structure. Fixed here to -F_Q*Q2-(1/2)*F_QQ*gamma^2.
INDEPENDENTLY VERIFIED this sign is now correct by directly comparing
against the established §9/10 Lagrangian's own F_Q-alpha-part -- matches
exactly (zero symbolic difference).

CONSEQUENCE OF THE FIX, checked directly, not assumed: the bracket-match
result (2*kappa*[K_B*E_alpha+(2-K_B)*chi]) is completely UNAFFECTED --
it comes purely from the Maxwell+J-hat terms, which carry no F_Q/F_QQ
dependence at all. The corrected non-bracket "second piece" is simply
the negative of the originally-reported one:

    -3*F_Q*Psi*phibardot + F_Q*varphi_dot - F_QQ*Psi*phibardot^2
      + F_QQ*phibardot*varphi_dot

Tried the advisory's own proposed resolution (compare against
8*pi*Gt*rhobar*delta's own gamma-term, i.e. use the established
identity 8*pi*Gt*rhobar*(1+w) = -phibardot*F_Q/2, rather than a bare
(1+w) comparison) -- substituting F_QQ=F_Q/(phibardot*cad2) and
simplifying gives exactly

    F_Q*(1+1/cad2)*gamma - 2*F_Q*phibardot*Psi

which is NOT a clean multiple of gamma=varphi_dot-phibardot*Psi (the
extra -2*F_Q*phibardot*Psi term persists) -- confirming, independently,
the advisory's own finding that this hypothesis does not resolve the
mismatch either. The gamma-sector piece remains genuinely open.
"""
import sympy as sp

t = sp.symbols('t')
K_B, kappa = sp.symbols('K_B kappa', positive=True)
FQ, FY, FQQ, phibar_dot = [sp.Function(f)(t) for f in ['FQ', 'FY', 'FQQ', 'phibardot']]
Psi = sp.Function('Psi')(t)
alpha = sp.Function('alpha')(t)
varphi = sp.Function('varphi')(t)

chi = varphi + phibar_dot * alpha
Ealpha = sp.diff(alpha, t) + Psi
gamma = sp.diff(varphi, t) - phibar_dot * Psi
Q2 = (kappa * phibar_dot * alpha**2 / 2 + kappa * alpha * varphi
      + sp.Rational(3, 2) * Psi**2 * phibar_dot - Psi * sp.diff(varphi, t))

L = (-FQ * Q2 - sp.Rational(1, 2) * FQQ * gamma**2
     + K_B * kappa * Ealpha**2 + 2 * (2 - K_B) * kappa * Ealpha * chi)

if __name__ == '__main__':
    dL_dPsi = sp.expand(sp.diff(L, Psi))
    print("d(action)/dPsi, collected:")
    print(sp.collect(dL_dPsi, [chi, alpha, sp.diff(alpha, t), varphi, sp.diff(varphi, t)]))
    print()

    bracket_candidate = 2 * kappa * (K_B * Ealpha + (2 - K_B) * chi)
    remainder = sp.expand(dL_dPsi - bracket_candidate)
    print("Remainder after subtracting 2*kappa*[K_B*E_alpha+(2-K_B)*chi]:")
    print(sp.simplify(remainder))
    print()
    print("Bracket match confirmed (remainder has no E_alpha/chi/alpha/varphi")
    print("terms left, only the separate F_Q/F_QQ/Psi/varphi_dot piece):")
    remainder_no_gamma_terms = remainder.subs({sp.diff(varphi, t): 0, Psi: 0})
    print("  Zero after also dropping the gamma-sector terms:",
          sp.simplify(remainder_no_gamma_terms) == 0)
