#!/usr/bin/env python3
"""
closure_dynamics.py — cdot-7, session 2026-07-07 entry 7
AQUAL-consistent Machian closure: dynamical system, fixed point, instability,
Hubble-diagram fit, age, and forward runaway.
Companion to Update-ClosureRebuild-2026-07-07.md. Reproduces every number quoted there.

System (dimensionless; c0 = 1, R* = B*sqrt(mu*)*c0^{3/4}, T = R*/c0):
    dr/dt = a
    da/dt = a^2 / (kappa*lam * x * r)
    x     = mu^{-1}( mu* r^2 / a^{3/2} )
Fixed point: r = a^{3/4}, x* = 3/(4*kappa*lam). Redshift law: 1+z = a^{-3/2}.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import minimize_scalar, brentq

KAPPA = 1.0
INV_H0_GYR = 13.97          # 1/H0 for H0 = 70 km/s/Mpc


def setup(lam, muform):
    xs = 3.0 / (4 * KAPPA * lam)
    if muform == 'simple':                     # mu = x/(1+x)
        mu, xinv, nu = (lambda x: x/(1+x)), (lambda m: m/(1-m)), 1/(1+xs)
    elif muform == 'standard':                 # mu = x/sqrt(1+x^2)
        mu, xinv, nu = (lambda x: x/np.sqrt(1+x*x)), (lambda m: m/np.sqrt(1-m*m)), 1/(1+xs**2)
    else:
        raise ValueError(muform)
    return xs, mu(xs), xinv, nu


def integrate(eps0, lam, muform='simple', a_min=1e-5):
    """Backward in a from today (a=1, r=1+eps0). State: [r, tau_proper, t_coord]."""
    xs, mus, xinv, nus = setup(lam, muform)
    r0 = 1.0 + eps0

    def rhs(a, Y):
        r = Y[0]
        x = xinv(min(mus * r * r / a**1.5, 1 - 1e-13))
        dtda = KAPPA * lam * x * r / a**2
        return [KAPPA * lam * x * r / a, a**2.5 * dtda, dtda]

    sol = solve_ivp(rhs, [1.0, a_min], [r0, 0.0, 0.0], dense_output=True,
                    rtol=1e-11, atol=1e-13)
    x0 = xinv(min(mus * r0 * r0, 1 - 1e-13))
    H0 = 1.5 / (KAPPA * lam * x0 * r0)          # H0_obs = (3/2) (da/dt)|_0, units 1/T
    return sol, r0, H0


def DL_model(z, sol, r0, H0):
    a = (1.0 + z)**(-2.0 / 3.0)
    return H0 * (r0 - sol.sol(a)[0]) * (1.0 + z)      # units c0/H0_obs


def DL_EdS(z):
    return 2.0 * ((1 + z) - np.sqrt(1 + z))


def DL_LCDM(z, Om=0.3):
    E = lambda zz: 1.0 / np.sqrt(Om * (1 + zz)**3 + 1 - Om)
    zs = np.atleast_1d(z)
    out = np.array([(1 + zz) * quad(E, 0, zz)[0] for zz in zs])
    return out if np.ndim(z) else out[0]


def q0_numeric(eps0, lam, muform='simple', h=1e-6):
    """q0 = (4 - 2j)/3, j = a (df/dt)/f^2 by finite difference along the flow."""
    xs, mus, xinv, _ = setup(lam, muform)
    f = lambda a, r: a * a / (KAPPA * lam * xinv(min(mus * r * r / a**1.5, 1 - 1e-13)) * r)
    r0, a0 = 1 + eps0, 1.0
    f0 = f(a0, r0)
    j = a0 * (f(a0 + f0 * h, r0 + a0 * h) - f(a0 - f0 * h, r0 - a0 * h)) / (2 * h) / f0**2
    return (4 - 2 * j) / 3


def fit_eps0(lam, muform='simple', zmax=1.4, Om=0.3):
    zg = np.linspace(0.02, zmax, 60)
    dl_ref = DL_LCDM(zg, Om)
    def cost(e):
        sol, r0, H0 = integrate(e, lam, muform)
        return np.mean((5 * np.log10(DL_model(zg, sol, r0, H0) / dl_ref))**2)
    res = minimize_scalar(cost, bounds=(-0.12, -0.001), method='bounded',
                          options={'xatol': 1e-6})
    return res.x, np.sqrt(res.fun)


def forward_runaway(eps0, lam, muform='simple', a_stop=1e6):
    """Forward from today; returns proper-time (Gyr) to reach c = N*c0."""
    xs, mus, xinv, _ = setup(lam, muform)
    _, r0, H0 = integrate(eps0, lam, muform)
    def rhs(t, Y):
        r, a, tau = Y
        x = xinv(min(mus * r * r / a**1.5, 1 - 1e-13))
        return [a, a * a / (KAPPA * lam * x * r), a**2.5]
    ev = lambda t, Y: Y[1] - a_stop; ev.terminal, ev.direction = True, 1
    sol = solve_ivp(rhs, [0, 1e3], [r0, 1.0, 0.0], rtol=1e-10, atol=1e-12,
                    events=ev, dense_output=True)
    def tau_at(target):
        tt = brentq(lambda t: sol.sol(t)[1] - target, 0, sol.t[-1])
        return sol.sol(tt)[2] * H0 * INV_H0_GYR
    return tau_at, sol


if __name__ == '__main__':
    # -- validation: eps0 = 0 must be exactly EdS with age*H0 = 2/3
    sol, r0, H0 = integrate(0.0, 0.26)
    z = np.array([0.1, 0.5, 1.0, 2.0])
    assert np.allclose(DL_model(z, sol, r0, H0), DL_EdS(z), rtol=1e-8)
    assert abs(-sol.y[1, -1] * H0 - 2 / 3) < 1e-9
    print('validation: EdS fixed point + age*H0=2/3 reproduced')

    # -- instability exponent check vs 3/(2 nu*)
    xs, _, _, nus = setup(0.26, 'simple')
    sol, r0, H0 = integrate(-0.01, 0.26)
    av = np.array([0.9, 0.7, 0.5, 0.3])
    eps = sol.sol(av)[0] / av**0.75 - 1
    p = np.polyfit(np.log(av), np.log(-eps), 1)[0]
    print(f'instability: measured {p:.3f}  predicted {1.5/nus:.3f}')

    # -- survey table
    print(f"{'mu':>9} {'lam':>5} {'x*':>6} {'nu*':>6} {'eps0':>8} {'rms':>7} "
          f"{'q0':>7} {'ageH0':>7} {'Gyr':>6}")
    for muform in ('simple', 'standard'):
        for lam in (0.20, 0.26, 0.35):
            xs, _, _, nus = setup(lam, muform)
            e0, rms = fit_eps0(lam, muform)
            sol, r0, H0 = integrate(e0, lam, muform)
            print(f'{muform:>9} {lam:5.2f} {xs:6.2f} {nus:6.3f} {e0:8.4f} '
                  f'{rms:7.4f} {q0_numeric(e0, lam, muform):7.3f} '
                  f'{-sol.y[1,-1]*H0:7.3f} {-sol.y[1,-1]*H0*INV_H0_GYR:6.2f}')

    # -- fiducial forward runaway
    tau_at, _ = forward_runaway(-0.0627, 0.26)
    for N in (2, 10, 100, 1e4):
        print(f'  c = {N:>7.0f} c0  at proper time {tau_at(N):7.2f} Gyr')
    print(f'  proper time per e-fold (deep regime): '
          f'{(tau_at(1e4)-tau_at(100))/np.log(1e2):.1f} Gyr')
