#!/usr/bin/env python3
r"""
wp7_derivation_Y_identity.py -- 2026-07-21. First step of the commissioned
action-level FRW derivation (Advisory-WP7-RecourseRoundAssessed-2026-07-21.md,
item 1 of the target list): work out Y = q^{mu nu} nabla_mu phi nabla_nu phi
to quadratic order in Newtonian-gauge cosmological perturbations, as the
prerequisite for tracing how a general F(Y,Q) modifies the already-derived
(F_Y=0) perturbation system.

RESULT (symbolically verified, see below):

    Y = (1/a^2) * (nabla_i chi)^2      [to quadratic order in perturbations]

where chi = varphi + phibar_dot * alpha is EXACTLY the combination already
used throughout this program's imported perturbation system (chi, gamma,
E_alpha). This is not a coincidence: chi IS the A-orthogonal projection of
nabla_mu phi (D_i phi = nabla_i phi + A_i * Q = partial_i chi, an exact
identity used in the derivation), so it is the natural object to appear in
Y's own quadratic expansion.

DIRECT ACTION-LEVEL CONSEQUENCE: expanding F(Y,Q) = F(0,Q) + F_Y(0,Q)*Y + ...
around Y=0 (exact on the background), the quadratic-in-perturbations action
picks up

    S superset -\int d^4x (a/16 pi Gtilde) [(2-K_B) + F_Y(0, Qbar)] (nabla chi)^2

i.e. (2-K_B) -> (2-K_B) + F_Y(0,Qbar) as the coefficient of chi's own
gradient-squared term IN THE ISOLATED F(Y,Q)-SECTOR OF THE ACTION. This
confirms the R1 structural hypothesis' core claim for this specific,
isolated piece.

A GENUINE BUG CAUGHT AND FIXED ALONG THE WAY (recorded for the record,
not swept under the rug): a first attempt at this derivation used the
paper's own STATED linear-order ansatz A_mu = (-1-Psi, nabla_i alpha)
literally, deriving A^0 (upper) from the unit constraint while treating
A_0 (lower) as exactly -1-Psi with no further correction. This is
INCONSISTENT once quadratic-order accuracy is needed: the unit-timelike
constraint A^mu A_mu = -1, combined with metric-consistent index raising,
requires a genuine SECOND-ORDER correction to A_0 itself (delta_2 =
Psi^2/2 - (nabla alpha)^2/(2a^2), matching the expected A_0 = -sqrt(-g_00)
generalization) that the paper's own linear-order-only quoted ansatz never
needed to state. Omitting it broke the Y = g^{mu nu} D_mu D_nu identity by
a term ~ (dalpha^2 - Psi^2 a^2) phibar_dot^2 / a^2 -- caught by computing Y
two independent ways (direct sum vs. the D_mu-projection identity) and
finding they disagreed, then tracing the disagreement to its root cause
rather than picking whichever answer looked more plausible.

STILL OPEN (not yet done, the harder remaining piece of item 1): tracing
this action-level coefficient through the FULL coupled Einstein + scalar +
vector field equations to determine whether -- and how -- it modifies
Pi's own already-established formula and the E_alpha equation specifically
(where (2-K_B) also appears, but possibly sourced by the SEPARATE
J^mu nabla_mu phi term in the base action, which does NOT receive an F_Y
correction). This requires either redoing that full variation, or finding
a valid shortcut using the linearity of the variation (the F_Y-sourced
correction to the equations of motion should be computable by varying
-F_Y(0,Qbar)*Y ALONE and adding it to the founding paper's own already-
derived equations, without redoing the entire derivation from scratch) --
not yet attempted, checkpointed here.
"""
import sympy as sp

eps = sp.symbols('epsilon')       # formal perturbation-counting parameter
t = sp.symbols('t')
a = sp.Function('a')(t)
Psi, phibar, varphi = [sp.Function(f)(t) for f in ['Psi', 'phibar', 'varphi']]
dvarphi, dalpha = sp.symbols('dvarphi dalpha')  # stand-ins for partial_i(varphi), partial_i(alpha)

# --- self-consistent A_0 (lower), including the necessary 2nd-order correction ---
delta2 = -dalpha**2 / (2 * a**2) + Psi**2 / 2

g00_lower = -(1 + 2 * eps * Psi)
g00_upper = sp.series(1 / g00_lower, eps, 0, 4).removeO()
gij_upper_scale = 1 / a**2

A0_lower = -1 - eps * Psi + eps**2 * delta2
Ai_lower = eps * dalpha
A0_upper = sp.series(sp.expand(g00_upper * A0_lower), eps, 0, 4).removeO()
Ai_upper = gij_upper_scale * Ai_lower

phidot = sp.diff(phibar, t) + eps * sp.diff(varphi, t)
dphi_i = eps * dvarphi

Qcal = sp.expand(A0_upper * phidot + Ai_upper * dphi_i)

D0 = sp.expand(phidot + A0_lower * Qcal)
Di = sp.expand(dphi_i + Ai_lower * Qcal)

Y_via_D = sp.expand(g00_upper * D0**2 + gij_upper_scale * Di**2)
Y_direct = sp.expand(g00_upper * phidot**2 + gij_upper_scale * dphi_i**2 + Qcal**2)

c_viaD = sp.expand(Y_via_D).coeff(eps, 2)
c_direct = sp.expand(Y_direct).coeff(eps, 2)

chi_grad = dvarphi + sp.diff(phibar, t) * dalpha
predicted = chi_grad**2 / a**2

if __name__ == '__main__':
    print("Y via D_mu-projection identity, eps^2 coefficient:")
    print(sp.simplify(c_viaD))
    print("\nY via direct sum (g^{mu nu} grad grad + Q^2), eps^2 coefficient:")
    print(sp.simplify(c_direct))
    print("\nBoth methods agree:", sp.simplify(c_viaD - c_direct) == 0)
    print("\nPredicted (1/a^2)(d_i chi)^2, chi = varphi + phibar_dot*alpha:")
    print(sp.simplify(predicted))
    print("Matches exactly:", sp.simplify(c_direct - predicted) == 0)
