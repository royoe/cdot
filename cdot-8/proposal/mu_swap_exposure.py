#!/usr/bin/env python3
"""
mu_swap_exposure.py — 2026-07-18. Pre-registration numerics for WP6
sub-task 1 (Cassini/ephemeris test). The collision to defuse in advance:
cdot-7/cdot-8's closure machinery uses mu(x) = x/(1+x) — the SIMPLE
interpolating function, whose slow 1-mu ~ 1/x Newtonian return is exactly
what cdot-4/T22 (mirroring Hees et al. 2014/2016) excluded by ~2800x with
Cassini ranging. This is a KNOWN property of the naked simple function,
not a new cdot-8 kill. Two questions actually matter:
 (1) AeST-chassis framing: the quasistatic limit is AeST's, which has its
     own GR-restoration machinery (lambda_s screening / higher-Y terms,
     SZ's 'two ways GR can be restored') — the Cassini test constrains
     THAT sector, not the naked mu tail. Expected outcome: a LOWER BOUND
     on the screening sector, not an exclusion.
 (2) Closure exposure: if the effective mu must be Cassini-safe (fast
     high-x return), how much do closure-relevant mu values shift at the
     trajectory's moderate-x working points (fixed points 1.72 / 3.44,
     x(1100) = 2.61)? This sets the refit scale for kappa*lambda, x0 —
     which lands inside Gate 1(b)'s post-WP7 revisit anyway.
"""
import numpy as np
xs = np.array([1.10, 1.7222, 2.61, 3.4443])   # x0, matter FP, x(1100), radiation FP
mu_simple  = xs/(1+xs)
mu_standard = xs/np.sqrt(1+xs**2)             # fast tail: 1-mu ~ 1/(2x^2)
# RAR/MLS-family: nu(y)=1/(1-exp(-sqrt(y))) => effective mu = g_N/g = y/x mapping;
# use the exponential-return proxy mu_exp = 1 - exp(-x) family bracketing fast returns:
mu_exp = 1-np.exp(-xs)
print(f"{'x':>7} {'mu_simple':>10} {'mu_standard':>12} {'mu_exp':>8} {'std/simple':>11} {'exp/simple':>11}")
for i,x in enumerate(xs):
    print(f"{x:>7.3f} {mu_simple[i]:>10.4f} {mu_standard[i]:>12.4f} {mu_exp[i]:>8.4f}"
          f" {mu_standard[i]/mu_simple[i]:>11.3f} {mu_exp[i]/mu_simple[i]:>11.3f}")
print(f"""
High-x (Saturn, x ~ 1e8): 1-mu_simple = 1e-8 (EXCLUDED, ~2800x, T22/Hees);
1-mu_standard = 5e-17, 1-mu_exp = ~0 (both Cassini-safe by construction).
EXPOSURE VERDICT: at the closure's working points the Cassini-safe
families sit 24-41% above mu_simple — the closure quadrature uses mu only
through these moderate-x values, so a mu-swap forces a kappa*lambda / x0
refit at the tens-of-percent scale (direction: larger mu => less scalar
source per x => refit compensates). NOT free, NOT fatal — and it belongs
to the same post-WP7 revisit Gate 1(b) already mandates (the nu-mass
lever lives there too). MAGNITUDE COINCIDENCE, flagged for the revisit:
the mu-swap moves closure-era quantities at the same tens-of-percent
order as WP4a's 27% theta* miss — and the swap is EXTERNALLY FORCED
(Cassini), not invented to fix theta*. Direction unverified: the revisit
should test the mu-swap FIRST among discrepancy-resolution options, and
it may equally worsen theta* — pre-registered as a candidate, not a fix. Pre-registered expectations for sub-task 1:
 (a) AeST screened form passes Cassini; deliverable = lower bound on the
     screening sector (lambda_s / higher-Y terms), not pass/fail on mu;
 (b) if the naked-mu framing is used anyway, the 2800x number will
     reappear — it is T22's known result about mu_simple, not news;
 (c) closure refit exposure at the tens-of-percent scale in
     kappa*lambda / x0 — quantify, don't execute, until the post-WP7
     revisit, where the mu-swap is first in the options queue.""")
