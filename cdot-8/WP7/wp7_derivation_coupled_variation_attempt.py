#!/usr/bin/env python3
r"""
wp7_derivation_coupled_variation_attempt.py -- 2026-07-21. First attempt
at the actual coupled Euler-Lagrange variation (the commissioned
derivation's harder remaining step, per Advisory-WP7-
JhatIdentityConfirmed-2026-07-21.md and the two advisories before it):
vary the alpha-dependent pieces of the action (bare Y term, the new
F_Y(0,Qbar)*Y completion, the J^mu*nabla_mu-phi term, the Maxwell-like
F_hat^mu-nu F_hat_mu-nu term, and F(Y,Q)'s own Q-dependence) directly
w.r.t. alpha, to obtain the vector (E_alpha) equation's new terms
without guessing an attribution.

BUILDING BLOCKS USED (all previously, independently established):
  - Y = (1/a^2)(grad chi)^2                    (wp7_derivation_Y_identity.py)
  - J_i = partial_i(E_alpha), J_0 = 0          (wp7_derivation_Jhat_identity.py)
  - Q's own second-order perturbation, computed here for the first time
    from Qcal in wp7_derivation_Y_identity.py: Q^(1) = gamma (no alpha-
    dependence, as expected), Q^(2) = [dalpha^2*phibardot + 2*dalpha*
    dvarphi + Psi-only terms]/(2a^2) -- a genuine alpha-varphi CROSS
    term inside Q itself, not previously computed in this program.

A GENUINE METHODOLOGICAL BUG CAUGHT AND FIXED before trusting anything:
the first attempt treated kappa=k^2/a^2 as a CONSTANT symbol in the
Euler-Lagrange derivative w.r.t. time -- this is wrong, since a(t) is
manifestly time-dependent, and produced a spurious 3H friction
coefficient for the Maxwell term alone (matching a canonical SCALAR
field's kinetic-term dilution rate, not a vector potential's). Fixed by
keeping kappa = k^2/a(t)^2 explicit; re-running the Maxwell term ALONE
then exactly reproduces the published K_B*(Ealpha_dot + H*Ealpha)
friction structure -- a clean, validating cross-check, not assumed.

RESULT WITH THE FULL ALPHA-DEPENDENT LAGRANGIAN (Y + F_Y*Y + J + Maxwell
+ F_Q*Q^(2)_alpha-part): the leading terms of the resulting
Euler-Lagrange equation DO match the published vector equation's
structure -- K_B*(Ealpha_dot+H*Ealpha) reproduced exactly; the chi
coefficient's leading (2-K_B)*H and dKdQ pieces reproduced. BUT TWO
RESIDUAL MISMATCHES REMAIN, not yet resolved:
  (1) the published chi coefficient has an additional (2-K_B)*phibardot
      piece this derivation does not produce;
  (2) the alpha coefficient here comes out proportional to
      dKdQ*phibardot and phibardot_dot (background Q-acceleration), not
      to cad^2*H*phibardot as in the published -3*(2-K_B)*cad^2*H*
      phibardot*alpha term.
Both are PRECISELY LOCATED, not vague: (1) is plausibly the point where
Pi/Psi's own separate origin (the 0i Einstein/momentum constraint, NOT
a raw field-variation object -- flagged as a structural concern before
this attempt even started) re-enters; (2) is plausibly resolved by
substituting the background scalar's OWN equation of motion (Qbar_dot
in terms of F_Q, F_QQ, H, via a^3*F_Q=const) to convert this
F_Q/F_QQ-parametrized raw result into the paper's compact cad^2
notation -- NOT yet attempted, a concrete, bounded next step.

STATUS: genuine, verified partial progress (the Maxwell-friction fix is
a real, validated result on its own); the two residual mismatches are
honestly reported as open, not resolved by guessing or forced through.
Checkpointing here per this program's standing discipline, given how
much this specific derivation (the coupled Y/J variation) has already
surfaced across five consecutive rounds (Sections 5-9 of
Update-WP7-InstabilityRecourses-2026-07-21.md).
"""
import sympy as sp

t = sp.symbols('t')
a = sp.Function('a')(t)
H = sp.Function('H')(t)
K_B, k2 = sp.symbols('K_B k2', positive=True)
FQ, FY, phibar_dot, cad2 = [sp.Function(f)(t) for f in ['FQ', 'FY', 'phibardot', 'cad2']]
Psi = sp.Function('Psi')(t)
CHI = sp.Function('CHI')(t)   # chi, treated as independent of alpha (paper's own convention)
alpha = sp.Function('alpha')(t)

kappa = k2 / a**2              # MUST stay a(t)-dependent -- see docstring bug note
chi = CHI
Ealpha = sp.diff(alpha, t) + Psi


def assemble_lagrangian():
    """Alpha-dependent quadratic action density (a^3 measure, kappa folded
    in), built from: bare Y term + F_Y(0,Qbar)*Y completion, the J-term
    (using J_i=partial_i(E_alpha) exactly), F_Q(Qbar)*Q^(2)'s alpha-part
    (derived from Qcal in wp7_derivation_Y_identity.py), and the Maxwell
    term (F_hat_01 = partial_1(E_alpha), same identity as J_1 in this
    1+1D reduction)."""
    L_YJ = a**3 * (
        -(2 - K_B + FY) * kappa * chi**2
        - FQ * kappa * alpha * chi
        + (FQ * phibar_dot / 2) * kappa * alpha**2
        + 2 * (2 - K_B) * kappa * Ealpha * chi
        - 2 * (2 - K_B) * phibar_dot * kappa * Ealpha * alpha
    )
    L_Maxwell = a**3 * K_B * kappa * Ealpha**2
    return L_YJ + L_Maxwell


def euler_lagrange(L):
    dL_dalphadot = sp.diff(L, sp.diff(alpha, t))
    dL_dalpha = sp.diff(L, alpha)
    EL = sp.expand(sp.diff(dL_dalphadot, t) - dL_dalpha)
    EL = EL.subs(sp.Derivative(a, t), a * H)
    return sp.expand(EL)


if __name__ == '__main__':
    print("=== Sanity check: Maxwell term ALONE, kappa=k^2/a(t)^2 kept explicit ===")
    L_M = a**3 * K_B * kappa * Ealpha**2
    EL_M = euler_lagrange(L_M)
    print(sp.expand(EL_M / (2 * a * k2)))
    print("(Should read exactly H*Psi + H*alpha_dot + Psi_dot + alpha_ddot")
    print(" = Ealpha_dot + H*Ealpha -- confirms kappa(t) fix, not asserted.)\n")

    print("=== Full alpha-dependent Lagrangian (Y+F_Y*Y+J+Maxwell+F_Q*Q^(2)) ===")
    L = assemble_lagrangian()
    EL = euler_lagrange(L)
    EL2 = sp.expand(sp.simplify(EL / (2 * a * k2)))
    collected = sp.collect(EL2, [CHI, alpha, Psi, sp.diff(alpha, t)])
    print(collected)
    print()
    print("Published (moved to '=0' form): K_B*(Ealphadot+H*Ealpha)")
    print("  - dKdQ*chi + (2-K_B)*phibardot/(1+w)*Pi")
    print("  + (2-K_B)*(H+phibardot)*chi - 3*(2-K_B)*cad2*H*phibardot*alpha = 0")
    print()
    print("STATUS: leading K_B*(Ealphadot+H*Ealpha) and (2-K_B)*H*chi + dKdQ*chi")
    print("terms match. Two residual mismatches remain open -- see module")
    print("docstring for the precise, non-vague diagnosis of each. NOT resolved")
    print("here; checkpointed for review.")
