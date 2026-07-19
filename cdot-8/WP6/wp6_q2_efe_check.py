#!/usr/bin/env python3
"""
wp6_q2_efe_check_v2.py -- corrected: e_N is NOT a_e/a0 directly. e_N is
defined as the NEWTONIAN external field/a0 (a_e^N/a0); the OBSERVED
(Gaia) external field a_e relates to it via the MOND/QUMOND law
a_e = nu(e_N) * e_N * a0  (paper's own text: "e_N=|a_e^N|/a0", and
"it is customary to parametrize the predicted Q2 from the value of the
actual external field... a_e=nu(a_e^N/a0) a_e^N is not exact" -- i.e.
the STANDARD/leading approximation solves nu(e_N) e_N = a_e/a0 for e_N).
Solve this implicit equation (same structure as this program's own
"mu(u)u=y" force-law inversion, T22/Foundation's mu_force_inv), for
BOTH cdot-7's own Simple IF (n=1) and, as a validation check, the
paper's own delta=1 RAR IF against their quoted e_N=1.643, Q2=3.387e-26.
"""
import numpy as np
from scipy.integrate import dblquad
from scipy.optimize import brentq

G = 6.674e-11
Msun = 1.989e30
a_e = 2.32e-10   # Gaia external field (observed), as used in the paper

def nu_n(x, n=1):
    return (0.5*(1+(1+4*x**(-n))**0.5))**(1.0/n)
def nu_delta(x, delta=1.0):
    return (1-np.exp(-x**(delta/2)))**(-1.0/delta)

def solve_eN(y, nu_func):
    f = lambda x: nu_func(x)*x - y
    return brentq(f, 1e-6, 100)

def q_integral(e_N, nu_func):
    def integrand(xi, v):
        arg = np.sqrt(e_N**2 + v**4 + 2*e_N*v**2*xi)
        return (nu_func(arg)-1.0)*(e_N*(3*xi-5*xi**3) + v**2*(1-3*xi**2))
    q, err = dblquad(integrand, 0, 40, -1, 1, epsabs=1e-12, epsrel=1e-10)
    return 1.5*q

print("=== VALIDATION: paper's own delta=1 RAR IF, their a0=1.02e-10 ===")
a0_paper = 1.02e-10
y_paper = a_e/a0_paper
eN_paper = solve_eN(y_paper, lambda x: nu_delta(x,1.0))
print(f"y=a_e/a0={y_paper:.4f}  solved e_N={eN_paper:.4f}  (paper quotes e_N=1.643)")
q_paper = q_integral(eN_paper, lambda x: nu_delta(x,1.0))
Q2_paper = -3*a0_paper**1.5/(2*np.sqrt(G*Msun))*q_paper
print(f"q={q_paper:.6f}  Q2={Q2_paper:.4e} s^-2  (paper quotes Q2=3.387e-26 s^-2)")
print(f"ratio to paper's quoted value: {Q2_paper/3.387e-26:.4f}\n")

print("=== cdot-7's OWN established choice: Simple IF (n=1), a0=1.39e-10 ===")
a0_cdot7 = 1.39e-10
y_cdot7 = a_e/a0_cdot7
eN_cdot7 = solve_eN(y_cdot7, lambda x: nu_n(x,1))
print(f"y=a_e/a0={y_cdot7:.4f}  solved e_N={eN_cdot7:.4f}")
q_cdot7 = q_integral(eN_cdot7, lambda x: nu_n(x,1))
Q2_cdot7 = -3*a0_cdot7**1.5/(2*np.sqrt(G*Msun))*q_cdot7
print(f"q={q_cdot7:.6f}  Q2={Q2_cdot7:.4e} s^-2")
print(f"\nNew Cassini bound: Q2=(1.6+/-1.8)e-27 s^-2 (1-sigma)")
print(f"|Q2_cdot7|/|bound central| = {abs(Q2_cdot7)/1.6e-27:.1f}x")
print(f"|Q2_cdot7|/(1-sigma) = {abs(Q2_cdot7)/1.8e-27:.1f} sigma (naive)")
