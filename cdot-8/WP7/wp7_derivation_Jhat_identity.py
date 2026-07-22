#!/usr/bin/env python3
r"""
wp7_derivation_Jhat_identity.py -- 2026-07-21. Checks the secondary
advisor's "weak point" concern (Advisory-WP7-RefinedAttributionAssessed-
2026-07-21.md, sec.3): does the aether's own covariant acceleration
J_mu = A^alpha nabla_alpha A_mu have a spatial component that is ITSELF
gradient-structured (undermining the "friction/mass, no Laplacian"
half of Stage-6's refined attribution)?

RESULT (symbolically verified via the actual perturbed-FRW Christoffel
symbols, not asserted): to linear order,

    J_i = partial_i(Psi + alpha_dot) = partial_i E_alpha

exactly -- J_i IS the spatial gradient of E_alpha (the already-
established variable E_alpha = alpha_dot + Psi), confirming and
sharpening the advisory's concern precisely (not just "some gradient
of alpha", but exactly this combination). This means the term
2(2-K_B) J^mu nabla_mu phi's spatial piece,

    J^i nabla_i phi ~ (1/a^2) partial_i(E_alpha) partial_i(varphi)

is a genuine gradient-CROSS-term between E_alpha and varphi -- a
DIFFERENT structure from Y = (1/a^2)(partial chi)^2 (which is chi
dotted with itself), not simply "no gradient at all" as the naive
friction/mass half of the refined-attribution criterion assumed, but
also not identical in structure to Y itself. Its own contribution to
the field equations (via integration by parts) would plausibly source
BOTH a nabla^2(E_alpha)-type term in the scalar equation and a
nabla^2(varphi)-type term in the E_alpha equation -- a genuinely
separate coupling, not capturable by either of Stage 6's two crude
"uniform substitution" / "refined attribution" hypotheses.

STATUS: this precisely locates what the actual coupled-variation
derivation (the advisor's own recommended next step, sidestepping the
attribution guess entirely) needs to account for -- not yet carried
through to the modified Pi/E_alpha equations themselves. Checkpointed
here per this program's standing discipline, given how much genuine,
easy-to-miss structure this single sub-problem keeps surfacing.
"""
import sympy as sp

t, x1 = sp.symbols('t x1')
eps = sp.symbols('epsilon')
a = sp.Function('a')(t)
Psi = sp.Function('Psi')(t, x1)
Phi = sp.Function('Phi')(t, x1)
alpha = sp.Function('alpha')(t, x1)

g00 = -(1 + 2 * eps * Psi)
g11 = a**2 * (1 - 2 * eps * Phi)
coords = [t, x1]
g = sp.diag(g00, g11)
ginv = sp.Matrix(2, 2, lambda i, j: sp.series(g.inv()[i, j], eps, 0, 2).removeO())


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


A0 = -1 - eps * Psi
A1 = eps * sp.diff(alpha, x1)
A_lower = [A0, A1]
A_upper = [sp.series(sp.expand(sum(ginv[i, j] * A_lower[j] for j in range(2))),
                      eps, 0, 2).removeO() for i in range(2)]


def J_component(mu):
    s = 0
    for al in range(2):
        s += A_upper[al] * sp.diff(A_lower[mu], coords[al])
        for be in range(2):
            s -= A_upper[al] * christoffel(be)[al, mu] * A_lower[be]
    return sp.series(sp.expand(s), eps, 0, 2).removeO()


def J_time_component_check():
    """J_0 = 0 to linear order (verified separately, added to this module
    for completeness -- see the printed output below)."""
    J0 = J_component(0)
    return J0


def orthogonality_check():
    """A^mu J_mu = 0 identically (independent consistency check on J_0, J_1
    and A_upper/A_lower together)."""
    s = sum(A_upper[mu] * J_component(mu) for mu in range(2))
    return sp.series(sp.expand(s), eps, 0, 2).removeO()


if __name__ == '__main__':
    J1 = J_component(1)
    print("J_1 (spatial component), to O(eps):")
    print(sp.simplify(J1))
    predicted = eps * sp.diff(Psi + sp.diff(alpha, t), x1)
    print("\nPredicted eps*d/dx1(Psi + alpha_dot) = eps*d/dx1(E_alpha):")
    print(sp.simplify(predicted))
    print("\nMatches exactly:", sp.simplify(J1 - predicted) == 0)

    J0 = J_time_component_check()
    print("\nJ_0 (time component), to O(eps):")
    print(sp.simplify(J0))
    print("\nJ_0 = 0 exactly:", sp.simplify(J0) == 0)

    orth = orthogonality_check()
    print("\nOrthogonality check A^mu J_mu, to O(eps):")
    print(sp.simplify(orth))
    print("\nA^mu J_mu = 0 exactly:", sp.simplify(orth) == 0)
