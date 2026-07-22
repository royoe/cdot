#!/usr/bin/env python3
r"""
wp7_derivation_momentum_constraint_attempt.py -- 2026-07-21. First
attempt at deriving Pi's own momentum-constraint (0i Einstein equation)
contribution directly from the action -- the single piece flagged as
missing since Update-WP7-InstabilityRecourses-2026-07-21.md's Section
8, and sharpened into a precise, checkable target by
Advisory-WP7-PiGammaTermMatchConfirmed-2026-07-21.md's Section 4 (the
residual's net-zero Psi-dependence must be matched by Pi's own
kap3-bracket piece).

METHOD: extend the perturbed-FRW metric with a genuine shift
perturbation g_01 = epsilon*B(t,x1) (temporarily nonzero, alongside the
existing Psi, Phi, alpha, varphi), extending the same Christoffel-symbol
machinery already validated in wp7_derivation_Jhat_identity.py. T^0_i
(the momentum-density source of the 0i Einstein/momentum constraint) is
obtained, in the standard GR sense, from d(quadratic action)/dB at
B=0 -- differentiating w.r.t. the metric's own shift component, not a
field variation.

RESULTS, each independently computed and checked:
  - J_hat_mu (LOWER index) has NO B-dependence at linear order -- a
    clean, verified structural fact (checked directly, not assumed).
  - J_hat^0 (UPPER index, via g^01 raising) DOES pick up a B-linear
    piece once contracted into J^mu*nabla_mu-phi: the O(eps^2)
    coefficient of J^mu*nabla_mu-phi contains a genuine new term,
    B*phibar_dot*partial_1(E_alpha)/a^2 -- not present in any prior
    round's (B=0) analysis, since B never appeared there.
  - Q's own B-linear piece: B*[partial_1(alpha)*phibar_dot -
    partial_1(varphi)]/a^2.
  - Y's own B-linear piece: 2*B*partial_1(alpha)*phibar_dot^2/a^2.
  - The Maxwell term (F^mu-nu F_mu-nu) has EXACTLY ZERO B-dependence at
    this order -- checked directly, not assumed (the (g^01)^2
    correction to F^01 is O(eps^3), too high to matter here).

ASSEMBLING these into a candidate T^0_1-type quantity (d/dB of the
total action, evaluated at B=0) gives, after simplification using
chi = varphi + phibardot*alpha:

    F_Q*partial_1(chi) + 2*(2-K_B)*phibardot*partial_1(E_alpha)
      - 2*phibardot*partial_1(alpha)*[(2-K_B+F_Y)*phibardot + F_Q]

This DOES contain the expected phibardot*partial_1(Psi) piece (inside
E_alpha = alpha_dot+Psi) that Advisory-WP7-PiGammaTermMatchConfirmed's
own Section 4 prediction needs -- encouraging, not yet a full
confirmation. But it ALSO contains a bare F_Q*partial_1(chi) piece
(equivalently -2*dK/dQ*partial_1(chi)) with NO direct counterpart in
the published delta/Pi bracket [K_B*E_alpha+(2-K_B)*chi] (eq.
delta_field_relation / Pi_delta_E_alpha in the primary source), which
carries no separate dK/dQ term at all.

STATUS: genuine, partial progress -- NOT a completed or fully verified
derivation of Pi. The clean sub-results (J_hat_mu's B-independence, the
specific B-linear pieces of Q/Y/J, Maxwell's exact zero) are each
independently checkable and are reported with confidence. The
assembled candidate T^0_1 does not yet cleanly reproduce the published
bracket -- a genuine, unresolved discrepancy (the bare F_Q term),
honestly left open rather than forced to match. Likely candidates for
the gap, NOT yet checked: (a) an overall-normalization/sign convention
not yet matched to eq. Pi_delta_E_alpha's own 8*pi*Gt*a^2*rhobar
factor; (b) a missing cross-term from the Einstein-Hilbert sector's own
B-dependence (not computed here -- assumed to reduce to the standard
GR G^0_i as the primary source states, but not independently verified
in this extended, B-perturbed setting); (c) the F(Y,Q) expansion's own
Q^(1)-squared (gamma^2) term's B-cross-contribution, not included here.
Checkpointing here rather than pushing to an unverified conclusion,
consistent with this program's standing discipline.
"""
import sympy as sp

eps = sp.symbols('epsilon')
t, x1 = sp.symbols('t x1')
a = sp.Function('a')(t)
Psi = sp.Function('Psi')(t, x1)
Phi = sp.Function('Phi')(t, x1)
alpha = sp.Function('alpha')(t, x1)
varphi = sp.Function('varphi')(t, x1)
phibar = sp.Function('phibar')(t)
Bfun = sp.Function('B')(t, x1)
K_B, FQ, FY = sp.symbols('K_B FQ FY')

g00 = -(1 + 2 * eps * Psi)
g01 = eps * Bfun
g11 = a**2 * (1 - 2 * eps * Phi)
coords = [t, x1]
g = sp.Matrix([[g00, g01], [g01, g11]])
ginv = sp.Matrix(2, 2, lambda i, j: sp.series(g.inv()[i, j], eps, 0, 3).removeO())


def christoffel(up_idx):
    Gamma = sp.zeros(2, 2)
    for b in range(2):
        for c in range(2):
            s = 0
            for d in range(2):
                s += ginv[up_idx, d] * (sp.diff(g[d, c], coords[b])
                                        + sp.diff(g[d, b], coords[c])
                                        - sp.diff(g[b, c], coords[d]))
            Gamma[b, c] = sp.expand(sp.series(s / 2, eps, 0, 2).removeO())
    return Gamma


A0_lower = -1 - eps * Psi
A1_lower = eps * sp.diff(alpha, x1)
A_lower = [A0_lower, A1_lower]
A_upper = [sp.series(sp.expand(sum(ginv[i, j] * A_lower[j] for j in range(2))),
                      eps, 0, 3).removeO() for i in range(2)]


def J_component(mu):
    s = 0
    for al in range(2):
        s += A_upper[al] * sp.diff(A_lower[mu], coords[al])
        for be in range(2):
            s -= A_upper[al] * christoffel(be)[al, mu] * A_lower[be]
    return sp.series(sp.expand(s), eps, 0, 2).removeO()


if __name__ == '__main__':
    J0 = J_component(0)
    J1 = J_component(1)
    print("J_0, J_1 (lower index) -- B-dependence check:")
    print("  J_0 =", sp.expand(J0), " (B-linear piece:",
          sp.expand(J0 - J0.subs(Bfun, 0)), ")")
    print("  J_1 =", sp.expand(J1), " (B-linear piece:",
          sp.expand(J1 - J1.subs(Bfun, 0)), ")")
    print()

    phibar_dot = sp.diff(phibar, t)
    phi_t = phibar_dot + eps * sp.diff(varphi, t)
    phi_1 = eps * sp.diff(varphi, x1)

    Jup0 = sp.series(sp.expand(ginv[0, 0] * J0 + ginv[0, 1] * J1), eps, 0, 3).removeO()
    Jup1 = sp.series(sp.expand(ginv[1, 0] * J0 + ginv[1, 1] * J1), eps, 0, 3).removeO()
    Jdotphi = sp.series(sp.expand(Jup0 * phi_t + Jup1 * phi_1), eps, 0, 3).removeO()
    c2_J = sp.expand(Jdotphi.coeff(eps, 2))
    print("J^mu*nabla_mu(phi), O(eps^2), B-linear piece:")
    print(sp.expand(c2_J - c2_J.subs(Bfun, 0)))
    print()

    Qcal = sp.series(sp.expand(A_upper[0] * phi_t + A_upper[1] * phi_1), eps, 0, 3).removeO()
    Q2 = sp.expand(Qcal.coeff(eps, 2))
    Q2_Blin = sp.expand(Q2 - Q2.subs(Bfun, 0)).coeff(Bfun, 1) * Bfun
    print("Q, O(eps^2), B-linear piece (B^2 term dropped):")
    print(Q2_Blin)
    print()

    gdphidphi = sp.series(sp.expand(sum(ginv[i, j] * [phi_t, phi_1][i] * [phi_t, phi_1][j]
                                        for i in range(2) for j in range(2))),
                           eps, 0, 3).removeO()
    Ycal = sp.series(sp.expand(gdphidphi + Qcal**2), eps, 0, 3).removeO()
    Y2 = sp.expand(Ycal.coeff(eps, 2))
    Y2_Blin = sp.expand(Y2 - Y2.subs(Bfun, 0)).coeff(Bfun, 1) * Bfun
    print("Y, O(eps^2), B-linear piece (B^2 term dropped):")
    print(Y2_Blin)
    print()

    F01 = sp.diff(A1_lower, t) - sp.diff(A0_lower, x1)
    F_lower = sp.Matrix([[0, F01], [-F01, 0]])
    Fup01 = sp.series(sp.expand(sum(ginv[0, a_] * ginv[1, b_] * F_lower[a_, b_]
                                    for a_ in range(2) for b_ in range(2))),
                       eps, 0, 3).removeO()
    FF = sp.series(sp.expand(2 * Fup01 * F01), eps, 0, 3).removeO()
    FF2_Blin = sp.expand(sp.expand(FF.coeff(eps, 2)) - sp.expand(FF.coeff(eps, 2)).subs(Bfun, 0))
    print("Maxwell F^mu-nu F_mu-nu, O(eps^2), B-linear piece:", FF2_Blin)
    print("(Confirms exactly zero -- no B-dependence from the Maxwell term here.)")
    print()

    print("STATUS: sub-results above are each independently checkable and")
    print("reported with confidence. Assembling them into a candidate T^0_1")
    print("does NOT yet cleanly reproduce the published delta/Pi bracket --")
    print("see module docstring for the honest accounting of what matches")
    print("(the expected phibardot*partial_1(Psi) piece) and what doesn't yet")
    print("(a bare F_Q*partial_1(chi) term with no published counterpart).")
