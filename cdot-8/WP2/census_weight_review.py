#!/usr/bin/env python3
"""
census_weight_review.py — 2026-07-19. Review of the WP2 addendum
(census weights' Q-dependence: decided No, on the definitions as written).

VERIFICATION of the addendum's claims:
 * E_P = sqrt(hbar c^5/G): standard, c-dependence c^{5/2}.        OK
 * c(t) = c0 (a/a0)^{2/3}  <=>  1+z = (c0/c)^{3/2}: kinematic,
   pre-Q, background-only in WP1 as written.                      OK
 * p_matter = 5/2 (m ~ c^{1/2} times c^2), p_radiation = 1:
   match the g_i = (p-5/2) cdot/c + 3c/R_h structure on record.   OK
 * Textual reading: E_P(t), p_i^sp carry no argument that could
   hold local Q — decision-on-the-record is sound.                OK

THE AMENDMENT: 'does not bear on the covariantization-freedom item' is
one notch too separate. The ALTERNATIVE the addendum correctly declines
to adopt — a locally-normalized census, E_P(x,t) built from the
ball-smoothed local c — is not excluded by physics, only by the
definitions as built: it is FACET 4 of the census-sector
covariantization freedom (gauge status, center, volume convention, and
now normalization locality), renormalizing coefficients within the same
window architecture.

THE SHARPENING — how big can facet 4 be? The census integrand is
rho_E,coord/E_P ~ c^{p_i - 5/2} per species. Under the local-c
alternative, a smoothed delta-c enters each species' census as
(p_i - 5/2) * (delta c / c):
"""
for name, p in [("matter", 2.5), ("radiation", 1.0), ("neutrino (rel.)", 1.0)]:
    print(f"  {name:>16}: p - 5/2 = {p-2.5:+.1f}  ->  delta-c coupling {'ZERO — IMMUNE' if abs(p-2.5)<1e-12 else f'{p-2.5:+.1f} x (dc/c)'}")
print("""
=> the MATTER census is IMMUNE to the normalization-locality choice —
the same p_m = 5/2 cancellation that makes g_matter's cdot/c term vanish
on the background kills the delta-c piece at perturbative order too.
Facet 4 can touch RADIATION-ERA census coefficients only (p - 5/2 =
-3/2), i.e. the deep-radiation/crossover end of the low-l term — the
matter-era low-l structure is convention-free on this facet. A genuinely
useful bound: the freedom item shrinks where it matters most for the
late-time CMB.""")
