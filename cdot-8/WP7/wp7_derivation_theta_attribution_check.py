#!/usr/bin/env python3
r"""
wp7_derivation_theta_attribution_check.py -- 2026-07-21. Checks the
secondary advisor's testable hypothesis
(Advisory-WP7-MomentumConstraintAttemptAssessed-2026-07-21.md, sec.4):
does the "bare F_Q" piece of the §11 candidate T^0_1
(wp7_derivation_momentum_constraint_attempt.py) -- isolated there as
F_Q*(partial_1(varphi) - phibardot*partial_1(alpha)), NOT F_Q*partial_1
(chi) as the write-up's looser phrasing suggested (advisory's own
correction, confirmed here too) -- actually belong to the SCALAR
sector's own theta-equation (theta = varphi/phibardot, primary source
line 440) rather than to Pi's own bracket?

METHOD: use the already-established background identities (8 pi Gt
rhobar = Q dK/dQ - K; 8 pi Gt Pbar = K; dK/dQ = -F_Q/2, all verified in
earlier WP2/WP3/WP7 rounds) to check whether

    (1+w)*rhobar*16*pi*Gt  =?=  -phibardot*F_Q

-- the identity needed for the STANDARD fluid momentum source,
-(1+w)*rhobar*partial_i(theta), to reproduce F_Q*partial_1(varphi)
(using theta=varphi/phibardot, partial_1(theta)=partial_1(varphi)/
phibardot since phibardot depends on t only).

RESULT: the identity holds EXACTLY (symbolic difference zero) --
(1+w)*rhobar*16*pi*Gt = -Q*F_Q = -phibardot*F_Q. This confirms the
varphi-part of the isolated F_Q piece maps EXACTLY onto the standard
fluid momentum-constraint source, -(1+w)*rhobar*partial_1(theta) --
not an approximation, an exact background identity.

CONSEQUENCE: subtracting this theta-matched piece from the full §11
candidate T^0_1 leaves a clean remainder,

    2*(2-K_B)*phibardot*partial_1(E_alpha) - 2*(2-K_B+F_Y)*phibardot^2*partial_1(alpha)

-- purely alpha/E_alpha-dependent (no varphi at all), which must be
what maps onto Pi's own kap3-bracket contribution (in combination with
the vector equation already derived in Sections 5-10). Notably, this
remainder contains a genuine F_Y-proportional piece
(-2*F_Y*phibardot^2*partial_1(alpha)) -- an EXPECTED new-physics
contribution from the completion itself, structurally analogous to
the F_Y*phibardot*chi term already found in Section 10's vector
equation.

STATUS: genuine, confirmed partial resolution of the "bare F_Q" gap --
the theta-attribution hypothesis is correct for the varphi-part,
verified via an exact background identity, not merely plausible. The
remaining alpha/E_alpha-proportional piece is NOT yet matched against
Pi's own bracket structure -- that comparison (does this remainder,
after a further spatial derivative, reproduce k^2*[K_B*E_alpha+(2-K_B)*
chi] up to normalization?) is the next concrete, bounded step, not
attempted here.
"""
import sympy as sp

FQ, dKdQ, K, Q, rho, P, w, Gt = sp.symbols('FQ dKdQ K Q rho P w Gt')
K_B, FY, phibardot = sp.symbols('K_B FY phibardot')
alpha_1, varphi_1, Ealpha_1 = sp.symbols('alpha_1 varphi_1 Ealpha_1')

if __name__ == '__main__':
    rho_expr = (Q * dKdQ - K) / (8 * sp.pi * Gt)
    P_expr = K / (8 * sp.pi * Gt)
    w_expr = sp.simplify(P_expr / rho_expr)

    lhs = sp.simplify((1 + w_expr) * rho_expr * 16 * sp.pi * Gt).subs(dKdQ, -FQ / 2)
    rhs = -Q * FQ
    print("(1+w)*rhobar*16*pi*Gt =", lhs)
    print("-phibardot*FQ (Q=phibardot) =", rhs)
    print("Exact background identity confirmed:", sp.simplify(lhs - rhs) == 0)
    print()

    candidate = (FQ * (varphi_1 + phibardot * alpha_1)
                 + 2 * (2 - K_B) * phibardot * Ealpha_1
                 - 2 * phibardot * alpha_1 * ((2 - K_B + FY) * phibardot + FQ))
    theta_piece = FQ * (varphi_1 - phibardot * alpha_1)
    remainder = sp.expand(candidate - theta_piece)
    print("theta-matched piece (isolated F_Q term, varphi-alpha combination):")
    print(sp.expand(theta_piece))
    print()
    print("Remainder after subtracting the theta-matched piece:")
    print(sp.simplify(remainder))
    print()
    print("STATUS: theta-attribution confirmed exactly for the varphi-part.")
    print("Remainder (pure alpha/E_alpha) still needs comparison against Pi's")
    print("own bracket structure -- not attempted here.")
