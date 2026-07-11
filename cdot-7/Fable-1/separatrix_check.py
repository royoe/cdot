#!/usr/bin/env python3
"""
separatrix_check.py — cdot-7, main-session verification, 2026-07-11
Checks the sign-selection candidate result of Update-SeedOriginAndNotation-2026-07-07.md
§2: is the delta>0 (Newtonian-ward) branch of closure_dynamics.py's dynamical system
globally irregular, hitting mu(x)->1 (x->infinity) at finite coordinate (and hence,
since r,a stay finite throughout, finite proper) time -- while delta<0 (observed) is not?

Reuses closure_dynamics.py's exact system (dr/dt=a, da/dt=a^2/(kappa*lam*x*r),
x=mu^{-1}(mu* r^2/a^{3/2})), forward in coordinate time t from today (r=1+eps0, a=1),
for both interpolating-function forms already in use in Foundation.md.

Analytic cross-check (also verified by hand, see ResearchNotes.md §17): along the flow,
    d(ln mu)/dt = d(ln[mu* r^2 a^{-3/2}])/dt = 2(a/r) - (3/2)(da/dt)/a
                = (2a/r)(1 - x*/x)   [using x* = 3/(4*kappa*lam)]
                -> 2a/r > 0 as x -> infinity,
matching the update's dot(mu)/mu = (a/r)[2 - 2x*/x) exactly.
"""
import numpy as np
from scipy.integrate import solve_ivp

KAPPA = 1.0


def setup(lam, muform):
    xs = 3.0 / (4 * KAPPA * lam)
    if muform == 'simple':
        mu, xinv = (lambda x: x / (1 + x)), (lambda m: m / (1 - m))
    elif muform == 'standard':
        mu, xinv = (lambda x: x / np.sqrt(1 + x * x)), (lambda m: m / np.sqrt(1 - m * m))
    else:
        raise ValueError(muform)
    return xs, mu(xs), xinv


def forward_to_breakdown(eps0, lam, muform, t_max=5.0):
    """Integrate forward in coordinate time t; returns (sol, blew_up)."""
    xs, mus, xinv = setup(lam, muform)
    r0 = 1.0 + eps0

    def rhs(t, Y):
        r, a = Y
        if not np.isfinite(r) or not np.isfinite(a) or a <= 0:
            return [np.nan, np.nan]
        m = min(mus * r * r / a**1.5, 1 - 1e-13)   # clamp only to avoid xinv's exact pole
        x = xinv(m)
        return [a, a * a / (KAPPA * lam * x * r)]

    def event_blowup(t, Y):
        r, a = Y
        m = mus * r * r / a**1.5
        return 1.0 - m
    event_blowup.terminal = True
    event_blowup.direction = -1

    sol = solve_ivp(rhs, [0, t_max], [r0, 1.0], rtol=1e-11, atol=1e-13,
                     events=event_blowup, dense_output=True, max_step=0.01)
    # Only a genuine crossing of the mu->1 event counts as "breakdown" here.
    # Integration can also fail (status -1) for the unrelated, already-known
    # forward coordinate-time singularity where a=c/c0 itself diverges
    # (Foundation.md Sec2.2's future de Sitter runaway) -- that is NOT this check.
    mu_breakdown = len(sol.t_events[0]) > 0
    return sol, mu_breakdown


if __name__ == '__main__':
    lam = 0.26
    print(f"kappa=1, lambda={lam}  (fiducial); checking both interpolating functions\n")
    for muform in ('simple', 'standard'):
        print(f"-- mu = '{muform}' --")
        print("  delta0>0 (Newtonian-ward): expect mu->1 breakdown at finite t, r,a still finite")
        for eps0 in (0.005, 0.01, 0.02, 0.05):
            sol, mu_breakdown = forward_to_breakdown(eps0, lam, muform, t_max=3.0)
            r, a = sol.y[:, -1]
            print(f"    delta0={eps0:+.3f}  mu->1 breakdown: {mu_breakdown}  "
                  f"at coordinate t={sol.t[-1]:.4f}  (r,a still finite: {r:.3f},{a:.3f})")
        print("  delta0<0 (observed): expect NO mu->1 breakdown -- integration instead runs")
        print("  toward the OTHER, already-known singularity (a=c/c0 -> large; harmless, see Sec2.2)")
        for eps0 in (-0.005, -0.01, -0.0627):
            sol, mu_breakdown = forward_to_breakdown(eps0, lam, muform, t_max=0.5)
            r, a = sol.y[:, -1]
            print(f"    delta0={eps0:+.4f}  mu->1 breakdown: {mu_breakdown}  "
                  f"reached t={sol.t[-1]:.3f}  (r,a: {r:.3f}, {a:.1f})")
        print()
