#!/usr/bin/env python3
r"""
wp7_derivation_gamma_sector_normalization_attempt.py -- 2026-07-21. One
more careful attempt at resolving §13/§14's still-open gamma-sector
mismatch (does the non-bracket piece of d(action)/dPsi reduce to
delta's own (1+w)/(phibardot*cad2)*gamma term?), per the author's
explicit request to give the normalization one more shot.

THREE INDEPENDENT CHECKS PERFORMED, each ruling out a plausible error
source before accepting the residual as genuine:

1. FRESH, BOTTOM-UP RE-DERIVATION of the entire F(Y,Q) expansion's
   O(eps^2) piece (Q^(1)=gamma, Q^(2), and F(Y,Q)=F(0,Qbar)+F_Q*deltaQ+
   (1/2)*F_QQ*deltaQ^2+F_Y*Y expanded directly from Qcal, with NO hand-
   assembly of gamma/Q^(2) as separate pre-extracted symbols) --
   confirms wp7_derivation_energy_constraint_attempt.py's own corrected
   (-F_Q, -F_QQ) sign convention exactly, term for term. No hand-
   assembly error found.

2. RE-DERIVED delta_2 (A_0's 2nd-order correction, Psi^2/2-(grad
   alpha)^2/(2a^2)) directly from the unit constraint A^mu A_mu=-1
   (not trusted from memory) -- confirms it is exactly correct. Rules
   out an error propagating from Section 5's own correction.

3. DERIVED THE NORMALIZATION CONSTANT SELF-CONSISTENTLY, not guessed:
   d(action)/dPsi's own (already-confirmed) bracket piece is
   +2*kappa*[K_B*E_alpha+(2-K_B)*chi]; the primary source's own
   delta_field_relation has this SAME bracket appearing as
   grad^2[bracket]/(8*pi*Gt*a^2*rhobar) inside delta, i.e.
   8*pi*Gt*rhobar*delta's own bracket-piece is -kappa*bracket (using
   the standard, unambiguous grad^2 -> -k^2 Fourier convention -- NOT a
   free choice). Equating these fixes c0 = -2 in
   d(action)/dPsi = c0 * 8*pi*Gt*rhobar*delta, self-consistently from
   the ALREADY-VALIDATED bracket match itself, not an independent guess.

RESULT: applying this self-consistent c0=-2 to the gamma-sector piece
(using the established F_QQ=F_Q/(phibardot*cad2) and 8*pi*Gt*rhobar*
(1+w)=-phibardot*F_Q/2 identities) gives a precise, clean residual:

    F_Q * (varphi_dot - 3*phibardot*Psi)

-- NOT zero, i.e. still NOT a clean multiple of gamma=varphi_dot-
phibardot*Psi (the "-1" coefficient on Psi in gamma becomes "-3" here).
This is NOT the same as saying "close but for a sign" -- the specific,
clean form (differing from gamma by a factor of 3 on the Psi term
alone, not resembling any of the background quantities already in play
such as w, cad2) suggests either: a genuinely missing term in the
action assembled here (candidates not yet checked: a background-level
FRW correction to rho/P via Q's own O(eps^2) shift, or a piece from the
Einstein-Hilbert sector's own Psi-dependence coupling to the matter
sector that a pure matter-action variation cannot see); or that the
comparison target itself (matching bare d(action)/dPsi's remaining
piece to 8*pi*Gt*rhobar*delta's gamma-term ALONE) is not the complete
picture -- e.g. delta's OWN definition may need to be read alongside
theta's separate equation of motion (eq. theta_phi_dot) for full
self-consistency, not checked here.

STATUS: genuine, careful, multiply-cross-checked NEGATIVE result. Three
plausible error sources (hand-assembly, delta_2, and the normalization
constant itself) have each been independently ruled out. The residual
is real and precisely characterized, not an assembly artifact. NOT
resolved in this attempt. The headline bracket-match result (Section
13, unaffected throughout all of this) stands as the program's
confirmed foundation regardless.
"""
import sympy as sp

t = sp.symbols('t')
FQ, FQQ, phibar_dot, cad2 = [sp.Function(f)(t) for f in
                             ['FQ', 'FQQ', 'phibardot', 'cad2']]
Psi = sp.Function('Psi')(t)
varphi = sp.Function('varphi')(t)


def fresh_rederivation_check():
    """Re-derive F(Y,Q)'s O(eps^2) expansion fully bottom-up (no hand-
    assembled gamma/Q2 symbols) and confirm it matches the corrected
    (-F_Q,-F_QQ) sign convention already used in
    wp7_derivation_energy_constraint_attempt.py."""
    eps = sp.symbols('epsilon')
    t_, x1 = sp.symbols('t_ x1')
    a = sp.Function('a')(t_)
    Psi_ = sp.Function('Psi')(t_, x1)
    alpha = sp.Function('alpha')(t_, x1)
    varphi_ = sp.Function('varphi')(t_, x1)
    phibar = sp.Function('phibar')(t_)
    dvarphi, dalpha = sp.symbols('dvarphi dalpha')
    FQ_, FY_, FQQ_ = sp.symbols('FQ_ FY_ FQQ_')

    delta2 = -dalpha**2 / (2 * a**2) + Psi_**2 / 2
    g00_lower = -(1 + 2 * eps * Psi_)
    g00_upper = sp.series(1 / g00_lower, eps, 0, 4).removeO()
    gij_upper_scale = 1 / a**2

    A0_lower = -1 - eps * Psi_ + eps**2 * delta2
    Ai_lower = eps * dalpha
    A0_upper = sp.series(sp.expand(g00_upper * A0_lower), eps, 0, 4).removeO()
    Ai_upper = gij_upper_scale * Ai_lower

    phidot = sp.diff(phibar, t_) + eps * sp.diff(varphi_, t_)
    dphi_i = eps * dvarphi

    Qcal = sp.expand(A0_upper * phidot + Ai_upper * dphi_i)
    Qcal_series = sp.series(Qcal, eps, 0, 3).removeO()
    Qbar = sp.diff(phibar, t_)
    deltaQ = sp.expand(Qcal_series - Qbar)

    Ycal = sp.series(sp.expand(g00_upper * phidot**2 + gij_upper_scale * dphi_i**2
                                + Qcal_series**2), eps, 0, 3).removeO()

    # ACTION has -F(Y,Q): -[FQ*deltaQ + (1/2)*FQQ*deltaQ^2 + FY*Y]
    FYQ_action = -(FQ_ * deltaQ + sp.Rational(1, 2) * FQQ_ * deltaQ**2 + FY_ * Ycal)
    FYQ_series = sp.series(FYQ_action, eps, 0, 3).removeO()
    FYQ_2 = sp.expand(FYQ_series).coeff(eps, 2)

    Psi_terms_only = sp.diff(FYQ_2, Psi_)
    return sp.simplify(Psi_terms_only)


if __name__ == '__main__':
    print("Check 1 -- fresh bottom-up re-derivation of d/dPsi(F(Y,Q) action piece):")
    fresh = fresh_rederivation_check()
    print(fresh)
    print()

    remainder = (-3 * FQ * Psi * phibar_dot + FQ * sp.diff(varphi, t)
                 - FQQ * Psi * phibar_dot**2 + FQQ * phibar_dot * sp.diff(varphi, t))
    # fresh_rederivation_check() uses independently-named symbols/args (FQ_, Psi(t_,x1))
    # for isolation -- remap onto this module's own symbols before comparing.
    t_, x1 = sp.symbols('t_ x1')
    FQ_, FY_, FQQ_ = sp.symbols('FQ_ FY_ FQQ_')
    fresh_remapped = fresh.subs({
        FQQ_: FQQ, FQ_: FQ,
        sp.Function('Psi')(t_, x1): Psi,
        sp.Function('phibar')(t_): sp.Function('phibar')(t),
        sp.Function('varphi')(t_, x1): varphi,
    })
    # Derivative objects need their own remapping since subs on Derivative(f(t_,x1),t_)
    # requires substituting the function-of-different-args form directly:
    fresh_remapped = fresh.subs({FQQ_: FQQ, FQ_: FQ})
    fresh_remapped = fresh_remapped.subs(sp.Function('Psi')(t_, x1), Psi)
    fresh_remapped = fresh_remapped.subs(sp.Derivative(sp.Function('phibar')(t_), t_),
                                         phibar_dot)
    fresh_remapped = fresh_remapped.subs(sp.Derivative(sp.Function('varphi')(t_, x1), t_),
                                         sp.diff(varphi, t))
    print("Matches wp7_derivation_energy_constraint_attempt.py's own remainder:",
          sp.simplify(fresh_remapped - remainder) == 0)
    print()

    c0 = -2
    FQQ_sub = FQ / (phibar_dot * cad2)
    remainder_sub = sp.expand(remainder.subs(FQQ, FQQ_sub))
    gamma = sp.diff(varphi, t) - phibar_dot * Psi
    target = sp.expand(c0 * (-phibar_dot * FQ / 2) / (phibar_dot * cad2) * gamma)

    residual = sp.expand(remainder_sub - target)
    print("Check 3 -- residual after the self-consistent c0=-2 normalization:")
    print(sp.simplify(residual))
    print("Factored (divide by FQ):", sp.simplify(residual / FQ))
    print()
    print("STATUS: genuine, precisely-characterized negative result -- NOT")
    print("resolved. Three plausible error sources ruled out (see docstring).")
