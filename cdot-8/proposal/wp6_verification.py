#!/usr/bin/env python3
"""
wp6_verification.py — 2026-07-18. Independent verification of the worker's
§4 (Cassini table) and §5 (PPN degeneracy) claims.
"""
import numpy as np, sympy as sp

print("=== §4: Saturn anomaly for three completions, mu(u)*u = y ===")
gdag, cassini = 1.13e-10, 4e-14
y = 755.0**2
# naked simple: u^2/(1+u) = y -> u = [y+sqrt(y^2+4y)]/2 ; anomaly a0*(u-y)
u = (y+np.sqrt(y*y+4*y))/2
print(f"simple:      anomaly = {gdag*(u-y):.3e} m/s^2  ratio = {gdag*(u-y)/cassini:.0f}x  (worker: 1.13e-10, 2825x)")
# standard: u^2/sqrt(1+u^2) = y  -> solve numerically
from scipy.optimize import brentq
us = brentq(lambda u: u*u/np.sqrt(1+u*u)-y, y, y+10)
print(f"standard:    anomaly = {gdag*(us-y):.3e} m/s^2  ratio = {gdag*(us-y)/cassini:.2e}  (worker: 9.9e-17, 2.5e-3)")
# exponential: u(1-e^-u) = y -> anomaly ~ a0*y*e^-y level
print(f"exponential: anomaly ~ a0*u*exp(-u) at u~755 = {gdag*755*np.exp(-755):.1e}  (worker: ~0)")

print("\n=== §5: Foster-Jacobson alpha_1, alpha_2 at AeST's corner ===")
c1, c2, c3, c4 = sp.symbols('c1 c2 c3 c4')
c13, c14, c123 = c1+c3, c1+c4, c1+c2+c3
a1 = -8*(c3**2+c1*c4)/(2*c1-c1**2+c3**2)
a2_first_den = c123*(2-c14)   # the term the worker reports divergent
sub = {c2:0, c4:0, c3:-c1}
print(f"alpha_1 at (c2=c4=0, c3=-c1): {sp.simplify(a1.subs(sub))}   (worker: -4*c1; known post-GW170817 form -4*c14 with c14=c1: match)")
print(f"c13 = {sp.simplify(c13.subs(sub))}  (tensor-speed condition c13=0: EXACT, by the same Maxwell form)")
print(f"c123 = {sp.simplify(c123.subs(sub))}  -> alpha_2 first-term denominator = {sp.simplify(a2_first_den.subs(sub))}  -> DIVERGES for c1!=0 (worker confirmed)")
print("""
Both sections verify. Notes for the advisory:
- simple-mu constant-anomaly asymptote a0*(u-y) -> a0*(1-1/y): confirmed
  analytically (u = y+1-1/y+...), the structural reason for the clean kill.
- The SAME Maxwell-only choice produces c13=0 (tensor speed = c, exactly)
  AND c123=0 (no aether spin-0 mode -> PPN formula singular): one design
  choice, two consequences — requirement (v) and the PPN gap are the same
  fact seen from two sides.""")
