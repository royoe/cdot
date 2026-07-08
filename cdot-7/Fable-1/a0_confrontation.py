#!/usr/bin/env python3
"""
a0_confrontation.py — cdot-7, session 2026-07-07 entry 8
Trajectory-corrected prediction of the evolving MOND scale, a0_hat(z), and its
confrontation with MUSE-DARK III (Ciocan et al. 2026, A&A 709, L16).
Requires closure_dynamics.py (entry 7) on the path.

Prediction: a0 = lam * cdot on the fitted trajectory; in local units
(acceleration unit ~ c^{7/2}):
    a0hat(z)/a0hat(0) = [x0*r0 / (x(z)*r(z))] * (1+z)^{3/2},
which asymptotes to ~0.61*(1+z)^{3/2} for the fiducial fit — the suppression
factor is fixed by the SAME eps0 fitted to the SN Hubble diagram (no new freedom).
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from closure_dynamics import setup, integrate

A0_LOC = 1.2   # local a0 in 1e-10 m/s^2 (SPARC anchor)

# Published measurement (MUSE-DARK III, 95% CI):
MEAS = dict(a0_z1=(2.38, +0.12, -0.10), a1=(1.59, +0.11, -0.10),
            bins_low=1.99, bins_high=2.71, zrange=(0.33, 1.44))


def a0hat_ratio_fn(lam, muform, eps0):
    xs, mus, xinv, nus = setup(lam, muform)
    sol, r0, H0 = integrate(eps0, lam, muform)
    x0 = xinv(min(mus * r0 * r0, 1 - 1e-13))
    def ratio(z):
        a = (1 + z) ** (-2 / 3.)
        r = sol.sol(a)[0] if z > 0 else r0
        x = xinv(min(mus * r * r / a ** 1.5, 1 - 1e-13))
        return (x0 * r0) / (x * r) * a ** (-1.5)
    return ratio


if __name__ == '__main__':
    # (muform, lam, SN-fitted eps0) — eps0 values from closure_dynamics survey
    cases = [('simple', 0.26, -0.0627), ('simple', 0.35, -0.0862),
             ('simple', 0.20, -0.0467), ('standard', 0.35, -0.0480)]
    fns = [a0hat_ratio_fn(l, m, e) for m, l, e in cases]

    print('a0(z) predictions [1e-10 m/s^2], anchored to a0(0)=1.2:')
    print(f"{'z':>5} {'fixed-pt':>8} " + ' '.join(f'{m[:4]}{l:.2f}' for m, l, _ in cases))
    for z in [0.05, 0.33, 0.45, 0.70, 0.85, 1.00, 1.20, 1.44]:
        row = ' '.join(f'{A0_LOC * f(z):8.2f}' for f in fns)
        print(f'{z:5.2f} {A0_LOC * (1 + z) ** 1.5:8.2f} {row}')

    z1, z2 = MEAS['zrange']
    print(f"\nEffective slope a1 over {z1}<z<{z2}  "
          f"(measured: {MEAS['a1'][0]} {MEAS['a1'][1]}/{MEAS['a1'][2]}, 95% CI):")
    for (m, l, e), f in zip(cases, fns):
        print(f'  {m:>8} lam={l:.2f}: {A0_LOC * (f(z2) - f(z1)) / (z2 - z1):.2f}')
    print(f'  fixed-point law    : '
          f'{A0_LOC * ((1 + z2) ** 1.5 - (1 + z1) ** 1.5) / (z2 - z1):.2f}')
    print('  constant a0        : 0.00')
    print(f"\nmeasured a0|z~1 = {MEAS['a0_z1'][0]} (95% CI "
          f"{MEAS['a0_z1'][1]}/{MEAS['a0_z1'][2]}); bins "
          f"{MEAS['bins_low']} -> {MEAS['bins_high']}")
