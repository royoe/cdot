#!/usr/bin/env python3
r"""
wp7_derivation_coupled_variation_varphi_fixed.py -- 2026-07-21. Adopts
the secondary advisor's correction to wp7_derivation_coupled_variation_
attempt.py (Advisory-WP7-CoupledVariationChiIndependenceCaught-2026-07-
21.md): chi = varphi + phibardot*alpha is NOT an independent field --
the genuinely independent fields are (varphi, alpha). Varying at fixed
chi (the original script's convention) silently forces varphi to
co-vary; varying at fixed varphi is the physically correct choice.
Independently reproduced the advisory's own correction exactly before
extending it further below.

FURTHER, NEW STEP (not in the advisory): substituted the background
scalar's own equation of motion, derived cleanly from a^3*F_Q=const:
differentiating gives 3*H*F_Q + F_QQ*phibar_ddot = 0, and using
cad2 = (dK/dQ)/(Qbar*d^2K/dQ^2) = F_Q/(Qbar*F_QQ) (paper's own
definition, line 405), this simplifies EXACTLY to

    phibar_ddot = -3*H*cad2*phibar_dot

-- a clean, exactly-derived identity, not an approximation.

RESULT: redoing the full Euler-Lagrange derivation directly in
(varphi, alpha) -- never introducing chi as a bookkeeping symbol, to
avoid the presentation ambiguity that made the advisory's "chi_dot
term" look like a new structure -- and substituting this background
identity, the residual (full derived vector-EOM minus the published
chi/alpha/Ealpha-explicit terms, which deliberately excludes Pi since
Pi is a separate momentum-constraint object, not a field-variation
one) comes out to EXACTLY:

    (2-K_B)*varphi_dot  +  F_Y*phibardot*chi  -  (2-K_B)*(1-3*cad2)*H*phibardot*alpha

The middle term (F_Y*phibardot*chi) is expected, genuine new physics
from the F_Y completion (absent in the published F_Y=0 equation, as it
should be). The other two pieces are checked against Pi's OWN
definition (eq. Pi_delta_E_alpha in the primary source, using
delta's leading gamma-dependence, gamma=varphi_dot-phibardot*Psi):

    (2-K_B)*phibardot/(1+w) * [Pi's leading gamma-term]
        = (2-K_B)*phibardot/(1+w) * [(1+w)/phibardot * gamma]
        = (2-K_B)*gamma = (2-K_B)*varphi_dot - (2-K_B)*phibardot*Psi

**The (2-K_B)*varphi_dot piece matches EXACTLY** -- confirmed
algebraically here, not just speculated as plausible (the advisory's
own framing). This is a genuine, positive confirmation that Pi's
momentum-constraint origin is precisely what completes the vector
equation's varphi_dot-dependence.

STILL OPEN, honestly reported: Pi's gamma-term also carries a
-(2-K_B)*phibardot*Psi piece not present in either side yet, and Pi's
own kap3*bracket piece has not been checked against the remaining
-(2-K_B)*(1-3*cad2)*H*phibardot*alpha residual -- both require actually
deriving Pi from the 0i Einstein/momentum constraint (not yet done
anywhere in this program), the single missing piece flagged since §8.
"""
import sympy as sp

t = sp.symbols('t')
H = sp.Function('H')(t)
K_B, k2 = sp.symbols('K_B k2', positive=True)
FQ, FY, phibar_dot, cad2, w = [sp.Function(f)(t) for f in
                                ['FQ', 'FY', 'phibardot', 'cad2', 'w']]
Psi = sp.Function('Psi')(t)
alpha = sp.Function('alpha')(t)
varphi = sp.Function('varphi')(t)
a = sp.Function('a')(t)

chi = varphi + phibar_dot * alpha
Ealpha = sp.diff(alpha, t) + Psi


def euler_lagrange_wrt_alpha():
    kappa = k2 / a**2
    L_YJ = a**3 * (
        -(2 - K_B + FY) * kappa * chi**2
        - FQ * kappa * alpha * chi
        + (FQ * phibar_dot / 2) * kappa * alpha**2
        + 2 * (2 - K_B) * kappa * Ealpha * chi
        - 2 * (2 - K_B) * phibar_dot * kappa * Ealpha * alpha
    )
    L_Maxwell = a**3 * K_B * kappa * Ealpha**2
    L = L_YJ + L_Maxwell
    dL_dalphadot = sp.diff(L, sp.diff(alpha, t))
    dL_dalpha = sp.diff(L, alpha)
    EL = sp.expand(sp.diff(dL_dalphadot, t) - dL_dalpha)
    EL = EL.subs(sp.Derivative(a, t), a * H)
    return sp.expand(EL)


if __name__ == '__main__':
    EL = euler_lagrange_wrt_alpha()
    EL2 = sp.expand(sp.simplify(EL / (2 * a * k2)))

    phibar_ddot_sym = sp.Derivative(phibar_dot, t)
    EL3 = sp.expand(EL2.subs(phibar_ddot_sym, -3 * H * cad2 * phibar_dot))

    target = (K_B * (sp.diff(alpha, t, 2) + sp.diff(Psi, t)
                      + H * (sp.diff(alpha, t) + Psi))
              + FQ / 2 * chi
              + (2 - K_B) * (H + phibar_dot) * chi
              - 3 * (2 - K_B) * cad2 * H * phibar_dot * alpha)
    target = sp.expand(target)

    residual = sp.expand(EL3 - target)
    print("Residual (derived vector-EOM minus published chi/alpha/Ealpha terms,")
    print("Pi deliberately excluded), after background-EOM substitution:")
    print(sp.simplify(residual))
    print()

    gamma = sp.diff(varphi, t) - phibar_dot * Psi
    Pi_leading_contribution = (2 - K_B) * phibar_dot / (1 + w) * ((1 + w) / phibar_dot * gamma)
    print("Pi's own leading gamma-term contribution, (2-K_B)*phibardot/(1+w)*[Pi_leading]:")
    print(sp.expand(Pi_leading_contribution))
    print()

    varphi_dot_piece = residual.coeff(sp.diff(varphi, t), 1) * sp.diff(varphi, t)
    print("varphi_dot piece of the residual:", varphi_dot_piece)
    print("Matches (2-K_B)*varphi_dot from Pi's gamma-term exactly:",
          sp.simplify(varphi_dot_piece - (2 - K_B) * sp.diff(varphi, t)) == 0)
    print()
    print("STATUS: varphi_dot piece confirmed to match Pi's momentum-constraint")
    print("contribution exactly. Remaining pieces (Pi's own -phibardot*Psi term,")
    print("and Pi's kap3*bracket vs. the alpha/cad2 residual) still require")
    print("deriving Pi from the actual 0i Einstein constraint -- not done here.")
