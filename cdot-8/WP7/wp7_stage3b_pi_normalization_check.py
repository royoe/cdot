#!/usr/bin/env python3
"""
wp7_stage3b_pi_normalization_check.py -- worker, 2026-07-20.

Stage 3b: resolve the Pi-formula's own Fourier/Laplacian normalization,
the one sub-term Stage 2's units contract never itemized (flagged by
the secondary advisor in Advisory-WP7-Stage3VectorInstabilityDiagnosed-
2026-07-20.md).

Primary-source re-derivation (newRMONDLett.tex line 456):
    Pi = cad2*delta - [cad2/(8 pi Gt a^2 rhobar)] grad^2[K_B*E_alpha + (2-K_B)*chi]

Fourier: grad^2 -> -k^2 (universal minus sign; the open question is only
whether an EXTRA 1/a^2 belongs inside grad^2 itself, i.e. "physical"
vs "comoving" Laplacian). Argument for the comoving reading: the
formula already carries an EXPLICIT a^2 multiplying rhobar in its own
prefactor (8 pi Gt a^2 rhobar) -- if grad^2 itself already meant the
physical (1/a^2-including) Laplacian, this explicit a^2 would double-
count the conversion factor the operator already supplies. The paper's
own minimal-notation convention (no redundant factors elsewhere in this
same PRL) favors NOT double counting: grad^2 -> -k^2 (bare comoving k),
with 8 pi Gt rhobar_s(a) = 3 H0^2 Om_s(a) (density definition, no extra
a^2 folded in separately). This gives:

    Pi_vec_term = + cad2 * kappa / (3 Om_s(a)) * bracket

where kappa = (k/(a H0))^2, matching this program's own established
Poisson-equation convention (Phi = -1.5*Om*delta/kappa, cross-checked
against the same paper's delta G^0_0 = 8 pi G rhobar delta relation).

This is DIFFERENT from the code currently in wp7_stage3_field_variable.py,
which uses a bare kappa (no Om_s division at all) -- a real, separate
normalization gap, regardless of which Laplacian convention is right.

Tested here: does fixing this (three candidates: current bare-kappa code,
the "comoving" reading kappa/(3*Om_s), and the "physical" reading
kappa/(3*a^2*Om_s), the second candidate the advisor also tried)
change the qualitative stability verdict from
wp7_stage3_vector_stiffness_audit.py?

Result: NO. All three readings give a growing real eigenvalue at high z
for k=1e-4 Mpc^-1 (the comoving reading roughly HALVES the eigenvalue's
magnitude at fixed z but does not remove it; the physical reading makes
it dramatically WORSE). The instability's existence is robust to this
normalization choice -- it is not resolved by nailing down the Pi-term's
Fourier convention. This is evidence (not proof) that the instability is
a genuine physical feature of the theory (sourced by the same negative
c_ad^2 that already made the scalar sector tachyonic/clustering per
Sec 23/27/28), not a units artifact.
"""
import numpy as np
import importlib.util
import sys

spec = importlib.util.spec_from_file_location(
    'audit', 'WP7/advisory/wp7_stage3_vector_stiffness_audit.py')
audit = importlib.util.module_from_spec(spec)
sys.modules['audit'] = audit
spec.loader.exec_module(audit)


def jacobian_normalized(N, kappa, reading):
    """reading in {'bare', 'comoving', 'physical'} -- see module docstring."""
    Ev2 = float(audit.E2_i(N)); Hc = np.sqrt(Ev2)
    wv = float(audit.w_i(N)); cad2v = float(audit.cad2_i(N))
    Qb = float(audit.Q_i(N)); FQv = float(audit.FQ_i(N))
    Oms = float(audit.Oms_i(N))
    a = np.exp(N)
    dKdQ = -0.5 * FQv
    KB = audit.K_B
    if reading == 'bare':
        kap_eff = kappa
    elif reading == 'comoving':
        kap_eff = kappa / (3 * Oms)
    elif reading == 'physical':
        kap_eff = kappa / (3 * a * a * Oms)
    else:
        raise ValueError(reading)
    dchi_dalpha = Qb
    dPi_dEalpha = cad2v * kap_eff * KB
    dPi_dalpha = cad2v * kap_eff * (2 - KB) * dchi_dalpha
    dalpha_dEalpha = 1.0 / Hc
    dEalpha_dalpha = (dKdQ * dchi_dalpha
                       - (2 - KB) * (Qb / (1 + wv) * dPi_dalpha + (Hc + Qb) * dchi_dalpha
                                     - 3 * cad2v * Hc * Qb)) / (KB * Hc)
    dEalpha_dEalpha = (-(2 - KB) * (Qb / (1 + wv) * dPi_dEalpha)) / (KB * Hc) - 1.0
    return np.array([[0.0, dalpha_dEalpha], [dEalpha_dalpha, dEalpha_dEalpha]])


if __name__ == '__main__':
    print(f"{'z':>6} {'Om_s':>8}   {'bare (current code)':>28}   "
          f"{'comoving k^2 (recommended)':>32}   {'physical k^2/a^2':>28}")
    k_Mpc = 1e-4
    for zt in (1090, 300, 100, 90, 70, 50, 10, 1, 0):
        i = np.argmin(np.abs(audit.z_arr - zt))
        Nv = audit.Nax[i]; a = np.exp(Nv)
        kap = (k_Mpc * audit.c0H0_Mpc / a) ** 2
        Oms = float(audit.Oms_i(Nv))
        e_bare = np.linalg.eigvals(jacobian_normalized(Nv, kap, 'bare'))
        e_com = np.linalg.eigvals(jacobian_normalized(Nv, kap, 'comoving'))
        e_phys = np.linalg.eigvals(jacobian_normalized(Nv, kap, 'physical'))
        print(f"{zt:6} {Oms:8.4f}   {str(e_bare):>28}   {str(e_com):>32}   {str(e_phys):>28}")

    print("\nVerdict: the growing real eigenvalue survives under all three")
    print("readings -- the Pi-normalization ambiguity changes the threshold's")
    print("exact scale but not its qualitative existence. Recommend treating")
    print("the instability as a real physical feature (quasi-static/slaved")
    print("closure for kappa above threshold), while still fixing the")
    print("separately-identified missing 1/(3*Om_s) factor in the coded Pi")
    print("term for its own sake (it is wrong regardless of which Laplacian")
    print("convention is adopted).")
