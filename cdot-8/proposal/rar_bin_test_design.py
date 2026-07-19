#!/usr/bin/env python3
"""
rar_bin_test_design.py — 2026-07-17. Design numbers for the differential,
intra-survey lensing-RAR redshift test — the form of the WP5 confrontation
that survives the systematics the pooled literature cannot:
  * absolute zero-point and absolute M/L cancel in a BIN RATIO within one
    pipeline + one SPS model (kills worker item iii and the absolute-Upsilon
    degeneracy; Mistele et al.'s 0.1 dex ESD-conversion band is common-mode);
  * what survives is DIFFERENTIAL systematics (stellar-population evolution
    across bins, selection drift at fixed M*) — percent-level, not 26%.
Observable: deep-MOND lensing amplitude g_obs = sqrt(a0 g_bar), so an a0
ratio R_a0 = E(z_hi)/E(z_lo) appears as sqrt(R_a0) in amplitude.
Theory-side band: +-4-5% at low z (cdot-7 fit-variant spread vs cdot-8
backbone, worker §8 cross-validation) -> demand signal >> band: maximize
the redshift lever arm rather than median-splitting.
"""
import numpy as np
# E(z) backbone (delivered, verified): interpolate
zs  = np.array([0.0, 0.10, 0.25, 0.35, 0.50, 0.75, 1.00])
Es  = np.array([1.0, 1.059, 1.161, 1.237, 1.362, 1.597, 1.861])
E = lambda z: np.interp(z, zs, Es)

print("DIFFERENTIAL BIN-RATIO DESIGN: a0(z_hi)/a0(z_lo) = E(z_hi)/E(z_lo)")
print("amplitude effect in deep-MOND lensing = sqrt of that ratio\n")
print(f"{'z_lo':>5} {'z_hi':>5} {'a0 ratio':>9} {'amp. effect':>12}  feasibility")
cases = [
 (0.17, 0.33, "KiDS-bright median split — signal ~ theory band, ~1 sigma: NOT decisive"),
 (0.15, 0.45, "KiDS-bright edge bins — marginal, 1.5-2 sigma class"),
 (0.20, 0.60, "KiDS+deeper (DES/HSC) — signal 2x theory band: viable"),
 (0.20, 0.75, "HSC-deep / early LSST — decisive class"),
 (0.20, 1.00, "LSST/Euclid full — decisive, >3x theory band"),
]
for zlo, zhi, note in cases:
    R = E(zhi)/E(zlo)
    print(f"{zlo:>5} {zhi:>5} {R:>9.3f} {np.sqrt(R):>11.3f}x  {note}")

print("""
NULL HYPOTHESIS: constant a0 -> ratio = 1.000 at every lever arm.
LCDM-mimic caution: any a0 ~ H(z) theory predicts nearly the same ratios
(this is a test of a0-tracks-H versus a0-constant, not of cdot-8 vs LCDM
E-shape — state this scoping in the write-up).
THEORY BAND: +-4-5% on E at z<~0.35 (fit-variant spread, worker §8),
shrinking to +-1-2% by z=1.0 — another reason the lever arm wins.
DIFFERENTIAL SYSTEMATICS BUDGET (to be modeled in the analysis, not here):
stellar-population evolution across bins at fixed M* (SPS handles first
order; residual few %), selection drift (compare at fixed M*), photo-z.
STATISTICAL SKETCH: pooled stacked amplitude precision ~3% (KiDS-class)
-> per-bin ~4%, ratio ~6%: the 5-10% short-lever signals are ~1 sigma,
the 15-30% long-lever signals are 3-5 sigma IF depth supports z_hi bins.
CONCLUSION: the decisive test needs the z~0.6-1.0 lens bins that only
DES/HSC-deep/LSST/Euclid provide; with KiDS alone the test is directional,
not decisive. The WP5 deliverable therefore closes as a PRE-REGISTERED
prediction + test design, not a pass/fail verdict on current data.""")
