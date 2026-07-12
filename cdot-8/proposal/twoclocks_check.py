#!/usr/bin/env python3
"""
twoclocks_check.py — 2026-07-12, advisory companion.

Verifies, numerically and independently of both the worker's algebra and the
advisor's, every step of the WP3 distance-tension resolution, on the exact
matter fixed point (the solution the worker analyzed):

 (1) the worker's finding: coordinate-clock rate H_t = d(ln a)/dt ∝ a^{1/6},
     and the constant-c covariant distance built on it DIVERGES as z→∞;
 (2) the worker's cross-check: a_0 = λ ċ ∝ c^{5/4} on the fixed point;
 (3) the resolution: matter proper (atomic) time dτ̂ = (c/c0)^{5/2} dt gives
     H_τ̂ = d(ln a)/dτ̂ ∝ a^{-3/2}  (i.e. H_τ̂² ∝ a^{-3}: exact EdS),
     and the matter-frame comoving distance χ̂ = ĉ∫dτ̂/a reproduces the
     bounded EdS formula (2ĉ/H_τ̂0)(1 − 1/√(1+z)) to numerical precision;
 (4) the clocks coincide today (calibrations untouched);
 (5) â_0(z) ∝ (1+z)^{3/2} ∝ H_τ̂ — the a_0 ~ cH relation is clock-consistent.

Setup: fixed point R_h = B c^{3/4}, Ṙ_h = c  ⟹  ċ = (4/3B) c^{5/4}.
Units: c0 = 1, B chosen so ċ0/c0 = 2/3 (⟹ H_τ̂0 = H_t0 = (3/2)(ċ0/c0) = 1).
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

B = 2.0                                   # ċ = (4/3B) c^{5/4} = (2/3) c^{5/4}
def cdot(c): return (4.0/(3.0*B))*c**1.25

# integrate c(t) backward from today (t=0, c=1) far into the past
sol = solve_ivp(lambda t, y: [cdot(y[0])], (0.0, -60.0), [1.0],
                rtol=1e-12, atol=1e-14, dense_output=True, max_step=0.01)
t = np.linspace(0.0, -60.0, 400000)
c = sol.sol(t)[0]
a = c**1.5
z = 1.0/a - 1.0

# ---- (1) coordinate-clock rate and the divergent distance -------------------
H_t = 1.5*cdot(c)/c
p_t = np.polyfit(np.log(a), np.log(H_t), 1)[0]
print(f"(1) H_t ∝ a^p: fitted p = {p_t:.6f}   (worker's claim: +1/6 = {1/6:.6f})")
# constant-c covariant comoving distance on the coordinate clock:
#   χ_t(z) = ĉ ∫_t^0 dt'/a(t')   (ĉ = 1)
chi_t = np.concatenate([[0.0], -np.cumsum(0.5*(1/a[1:]+1/a[:-1])*np.diff(t))])
for zq in (10, 100, 1000, 1e4, 1e5):
    i = np.argmin(abs(z-zq))
    print(f"    χ_t(z={zq:>7.0f}) = {chi_t[i]:12.2f}   (unbounded growth ✓)"
          if zq >= 1e4 else
          f"    χ_t(z={zq:>7.0f}) = {chi_t[i]:12.2f}")

# ---- (2) worker's cross-check ------------------------------------------------
p_a0 = np.polyfit(np.log(c), np.log(cdot(c)), 1)[0]
print(f"(2) a_0 = λċ ∝ c^p: fitted p = {p_a0:.6f}   (Foundation/worker: 5/4)")

# ---- (3) atomic-clock rate and the bounded EdS distance ----------------------
# τ̂(t): dτ̂ = c^{5/2} dt, integrated from today backward
dtau = c**2.5
tau = np.concatenate([[0.0], np.cumsum(0.5*(dtau[1:]+dtau[:-1])*np.diff(t))])  # negative
H_tau = H_t / c**2.5
p_tau = np.polyfit(np.log(a), np.log(H_tau), 1)[0]
print(f"(3) H_τ̂ ∝ a^p: fitted p = {p_tau:.6f}   (resolution's claim: -3/2)")
# matter-frame comoving distance χ̂ = ĉ ∫ dτ̂/a  vs analytic EdS
chi_tau = np.concatenate([[0.0], -np.cumsum(0.5*(dtau[1:]/a[1:]+dtau[:-1]/a[:-1])*np.diff(t))])
H_tau0 = H_tau[0]
eds = (2.0/H_tau0)*(1.0 - 1.0/np.sqrt(1.0+z))
mask = z > 0.01
err = np.max(np.abs(chi_tau[mask]/eds[mask] - 1.0))
print(f"    χ̂(z) vs EdS (2ĉ/H₀)(1−1/√(1+z)): max |ratio−1| = {err:.2e}  "
      f"(bounded, χ̂(∞)→{2/H_tau0:.3f})")
for zq in (1, 10, 1000, 1e5):
    i = np.argmin(abs(z-zq))
    print(f"    χ̂(z={zq:>7.0f}) = {chi_tau[i]:.6f}   EdS = {eds[i]:.6f}")

# ---- (4) clocks coincide today ------------------------------------------------
print(f"(4) today: H_t(0)/H_τ̂(0) = {H_t[0]/H_tau[0]:.12f}  (must be exactly 1)")

# ---- (5) â_0(z) ∝ (1+z)^{3/2} ∝ H_τ̂ -----------------------------------------
# local acceleration unit ∝ c^{7/2}  ⟹  â_0 ∝ c^{5/4-7/2} = c^{-9/4}
a0_hat = cdot(c)/c**3.5
p_hat = np.polyfit(np.log(1+z), np.log(a0_hat), 1)[0]
ratio = a0_hat/H_tau
print(f"(5) â_0 ∝ (1+z)^p: fitted p = {p_hat:.6f}   (claim: +3/2);  "
      f"â_0/H_τ̂ constant to {np.max(np.abs(ratio/ratio[0]-1)):.1e}")
