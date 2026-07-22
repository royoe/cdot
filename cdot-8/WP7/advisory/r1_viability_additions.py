#!/usr/bin/env python3
"""
r1_viability_additions.py — 2026-07-21. Three additions to the R0/R1/R2
record before advising on how to proceed.

ADDITION 1 — the physical reading of lambda_s -> -1: it is NOT an
arbitrary suppression trick. At lambda_s = -1 the hypothesized total
small-gradient coefficient (2-K_B)(1+lambda_s) vanishes — the scalar
sector becomes ULTRALOCAL (c_s^2 -> 0) at cosmological gradients.
A zero-sound-speed component is precisely what 'dust' means:
R1's endpoint is the completion under which the scalar is HONEST DUST
at linear cosmological order — while the census-fixed mu^2 ~ -0.5 H^2
driver (untouched by lambda_s) keeps supplying the scale-free,
CDM-like growth. The pathology was c_eff^2 < 0; CDM has c_s^2 = 0;
the fix drives c_eff^2 -> 0+ from the wrong side. Principled, not
epicyclic.

ADDITION 2 — the lambda_s > 0 tension has a scale structure worth
recording: the flagged Hamiltonian condition concerns the omega=0
vector mode with the boundary at momenta ~ mu. Where is mu relative to
the band we need stabilized?
"""
import numpy as np
mu_inv_Gpc = 10.3            # 1/mu_eff today (K_B->0 end, WP5 record)
mu_Mpc = 1.0/(mu_inv_Gpc*1000)
isw_band = (1.1e-3, 5.4e-3)  # ell = 2-10 at D_p(z=0.5), the unstable band
print(f"mu (today) ~ {mu_Mpc:.2e} /Mpc;  ISW instability band: {isw_band[0]:.1e}-{isw_band[1]:.1e} /Mpc")
print(f"band sits {isw_band[0]/mu_Mpc:.0f}-{isw_band[1]/mu_Mpc:.0f} x ABOVE mu")
print("""=> the negative-Hamiltonian zone (k below ~mu, per the quoted text's
first clause) and the zone needing stabilization (k = 10-55 x mu) are
ADJACENT BUT DISTINCT — and the paper's own reading of the low-k
negativity is 'likely akin to Jeans-type instabilities' (i.e. the
clustering sector, arguably a feature in a DM-mimicking theory, and
Hubble-frictioned on FRW). The compact PRL phrasing leaves ambiguous
whether lambda_s < 0 also threatens the k > mu region — exactly the
question the action-level FRW derivation must settle, now with the
scale map in hand. NOT dissolved; located.\n""")

print("""ADDITION 3 — the 'dangerous corner' (vector mass M^2 ~ (1+lambda_s))
is parametrically PROTECTED by WP6's own K_B squeeze:
   M^2 = (2-K_B)(1+lambda_s) Q0^2 / K_B   [founding paper, quoted]
— the 1/K_B blows the mass back up as K_B shrinks:""")
Q0 = 1.0  # in its own units; ratios below are what matter
for lam, KB in [(-0.999, 1.0), (-0.999, 2.5e-6), (-0.9999, 2.5e-6), (-0.99999, 2.5e-6)]:
    M2 = (2-KB)*(1+lam)/KB
    print(f"  lambda_s={lam:>9}, K_B={KB:<8}: M^2/Q0^2 = {M2:>12.3g}")
print("""At the pulsar-squeezed K_B <~ 2.5e-6 (WP6's conservative envelope),
even (1+lambda_s) = 1e-5 leaves M^2/Q0^2 ~ 8 — the vector stays HEAVY.
The corner is only dangerous at O(1) K_B; the same squeeze that looked
like pure constraint in WP6 is load-bearing FOR the recourse. (The
proper mass-vs-Hubble comparison along the trajectory belongs to the
derivation round; the parametric structure is the point here.)""")
