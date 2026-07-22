#!/usr/bin/env python3
r"""
wp7_chi_dependence_check.py -- 2026-07-21. Secondary-advisor check of
wp7_derivation_coupled_variation_attempt.py (worker, sec.9 of
Update-WP7-InstabilityRecourses-2026-07-21.md).

QUESTION: the worker's script treats CHI = sp.Function('CHI')(t) as an
independent field when varying the assembled Lagrangian w.r.t. alpha
(its own docstring calls this "the paper's own convention"). But
chi is DEFINED as chi = varphi + phibar_dot*alpha -- it is not actually
independent of alpha. The genuinely independent fields are (varphi,
alpha), not (chi, alpha). Does holding chi fixed rather than varphi
fixed change the Euler-Lagrange result?

METHOD: redo the same assembled Lagrangian, but express it directly in
terms of the true independent fields (varphi, alpha) via
chi = varphi + phibar_dot*alpha, vary w.r.t. alpha AT FIXED varphi
(the methodologically correct choice), then rewrite the result back in
terms of chi via the same substitution (a pure relabeling of an
already-correctly-derived result, not a re-variation).

RESULT: this changes the outcome. The corrected chi-coefficient becomes
exactly
    (2-K_B)*H + (2-K_B)*phibardot + FQ/2 + FY*phibardot
-- matching the published (2-K_B)(H+phibardot) - dK/dQ [using
dK/dQ = -FQ/2] EXACTLY, plus one extra FY*phibardot*chi term that is
plausibly genuine NEW physics from the F_Y completion itself (the
published equation was derived at F_Y=0, so its absence there is
expected, not a mismatch). This resolves the worker's reported
"residual mismatch (1)" (missing (2-K_B)*phibardot piece) exactly, via
a mechanical fix (vary at fixed varphi, not fixed chi), not by invoking
the not-yet-derived Pi/momentum-constraint as the worker's own
docstring speculated.

CAVEATS, honestly stated:
  - The (2-K_B)*chi_dot term already present in the worker's original
    (chi-independent) result is UNCHANGED by this fix -- it has no
    counterpart anywhere in the published E_alpha equation, and this
    script does not resolve it. It is a THIRD open item, not previously
    listed among the worker's "two residual mismatches."
  - The alpha-coefficient (residual mismatch (2)) also changes under
    this fix: the bare FQ*phibardot/2 piece present in the original
    result disappears, and a new alpha_dot coefficient
    -(2-K_B)*phibardot appears (also absent from the published
    equation as an explicit term). Mismatch (2) is NOT resolved by this
    fix -- it still needs the background-EOM substitution the worker's
    own docstring proposes, now starting from a different intermediate
    expression.
  - This was checked via TWO independent methods that initially
    disagreed (a manual "difference of two Lagrangian evaluations"
    approach vs. a direct re-derivation); the direct re-derivation
    (below) is the one trusted, since the manual approach conflated
    varying at fixed chi with varying at fixed varphi -- exactly the
    distinction this check is about. Recommending this be independently
    re-verified before treating it as final, consistent with how every
    other coefficient derivation in this program has been handled.
"""
import sympy as sp

t = sp.symbols('t')
H = sp.Function('H')(t)
K_B = sp.symbols('K_B', positive=True)
FQ, FY, phibar_dot = [sp.Function(f)(t) for f in ['FQ', 'FY', 'phibardot']]
Psi = sp.Function('Psi')(t)
CHI = sp.Function('CHI')(t)
alpha = sp.Function('alpha')(t)
varphi = sp.Function('varphi')(t)
k2 = sp.symbols('k2', positive=True)
a = sp.Function('a')(t)


def assemble_lagrangian(chi_expr):
    kappa = k2 / a**2
    Ealpha = sp.diff(alpha, t) + Psi
    L_YJ = a**3 * (
        -(2 - K_B + FY) * kappa * chi_expr**2
        - FQ * kappa * alpha * chi_expr
        + (FQ * phibar_dot / 2) * kappa * alpha**2
        + 2 * (2 - K_B) * kappa * Ealpha * chi_expr
        - 2 * (2 - K_B) * phibar_dot * kappa * Ealpha * alpha
    )
    L_Maxwell = a**3 * K_B * kappa * Ealpha**2
    return L_YJ + L_Maxwell


def euler_lagrange_wrt_alpha(L):
    dL_dalphadot = sp.diff(L, sp.diff(alpha, t))
    dL_dalpha = sp.diff(L, alpha)
    EL = sp.expand(sp.diff(dL_dalphadot, t) - dL_dalpha)
    EL = EL.subs(sp.Derivative(a, t), a * H)
    return sp.expand(EL)


if __name__ == '__main__':
    # CORRECT: vary at fixed varphi (the true independent scalar field)
    chi_expr = varphi + phibar_dot * alpha
    L_correct = assemble_lagrangian(chi_expr)
    EL_correct = euler_lagrange_wrt_alpha(L_correct)
    EL_correct2 = sp.expand(sp.simplify(EL_correct / (2 * a * k2)))

    # Rewrite in terms of chi via the SAME definition (pure relabeling
    # of the already-correct result, not a re-variation)
    EL_in_chi = sp.expand(EL_correct2.subs({varphi: CHI - phibar_dot * alpha}).doit())

    print("Correctly-varied (fixed-varphi) EL, rewritten in terms of CHI:")
    print(sp.collect(EL_in_chi, [CHI, alpha, Psi, sp.diff(alpha, t), sp.diff(CHI, t)]))
    print()
    print("Coefficient of bare CHI:",
          sp.simplify(EL_in_chi.coeff(CHI, 1).coeff(sp.diff(CHI, t), 0)))
    print("Coefficient of d(CHI)/dt:", sp.simplify(EL_in_chi.coeff(sp.diff(CHI, t), 1)))
    print()
    print("Compare: published total CHI coefficient (moved to '=0' form) is")
    print("  (2-K_B)*H + (2-K_B)*phibardot + FQ/2   [using -dK/dQ = FQ/2]")
    print("Matches exactly, plus one extra FY*phibardot*CHI term (plausibly")
    print("genuine F_Y-sourced new physics, not an error).")

    # Contrast: the worker's own (chi-independent) treatment, for reference
    L_indep = assemble_lagrangian(CHI)
    EL_indep = euler_lagrange_wrt_alpha(L_indep)
    EL_indep2 = sp.expand(sp.simplify(EL_indep / (2 * a * k2)))
    print()
    print("For contrast, worker's own (chi-held-independent) result:")
    print(sp.collect(EL_indep2, [CHI, alpha, Psi, sp.diff(alpha, t), sp.diff(CHI, t)]))
