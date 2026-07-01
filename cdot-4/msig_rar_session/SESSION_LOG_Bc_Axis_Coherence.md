# SESSION LOG — $B_c$ Axis from Bulk Motion; Orbital Coherence Factor

**Topics:** T14 (Connecton Gravity), T17 (Galaxy Morphology & M-σ), T6
**Date:** 2026-06-30
**Session type:** Reframing + computation, prompted by user physical insight, following the
negative background-density result.

---

## Timeline

**[2026-06-30 14:43 UTC] — Prior session.**
Background-density derivation failed to close the $a_0$ coefficient; exposed an internal
T14 inconsistency (floor wavelength = $R_0$ vs $c/H_0$, differing by $3P$).

**[2026-06-30 15:54 UTC] — User prompt (verbatim):**
> I'm not discouraged by this. I did not expect the 1/6 to come out so neatly as it did in
> the first attempt. As we have established before, the connectons are not just a pure
> Horizon connection. They have to be reemitted at each interaction point as currently
> interpreted, that means that the horizon is just the longest possible wavelength in the
> spectrum. The connection spectrum is still something to be determined. And I also expect a
> factor to come from the galaxy geometry itself. We have worked with Lorentz forces in that
> act along the tangent, as would be the case for near circular orbits in the disk. But the
> bulge component have random orbits, and the contribution to B_c from that should be a
> geometrical average of the thermalised orbits representative of the residual rotation. B_c
> cannot be sourced only from the horizon, it must get its direction from the bulk motions
> in the galaxy.

**[2026-06-30 15:54 UTC] — Analysis (two threads).**

Thread A (spectrum): re-emission at every interaction point ⇒ horizon = IR cutoff only;
floor wavelength is not a single line but a spectral integral. The prior $R_0$-vs-$c/H_0$
clash was a false dichotomy (two endpoints of one spectrum). Resolves the T14 inconsistency
as "undetermined spectral shape," not a contradiction.

Thread B (axis): $B_c$ is a vector; isotropic sea has no direction; the axis comes from the
galaxy's coherent mass current. Disk (aligned) vs bulge (random + small drift) differ
geometrically.

**[2026-06-30 15:54 UTC] — Computation (Thread B).**

Monte-Carlo of a drifting Maxwellian (N=2e6): coherent fraction f = J_coh/J_tot:
- J_coh = v_rot; J_tot → sqrt(8/pi) sigma as v_rot→0.
- f ≈ sqrt(pi/8) v_rot/sigma (bulge), f→1 (disk). Crossover confirmed numerically.

Consequence: bulge sees a0_eff = f^2 a0; deep-MOND balance gives
M_bulge ~ (8/pi beta^2) sigma^4/(G a0), beta = v_rot/sigma.
- Exponent 4 PRESERVED (M-σ not broken).
- Geometric prefactor 8/(pi beta^2) on the M-σ normalization, absent from disk BTFR.
- Resolves the under-justified v_f≈sigma bridge: disk/bulge offset = sqrt(8/pi beta^2),
  a computed factor.

Bonus falsifiable prediction: beta varies (0.3–1.0) ⇒ prefactor 28→2.5 ⇒ M-σ scatter
tracks rotational support; explains M-σ scatter (~0.3 dex) > BTFR (~0.1 dex). Disk has no
beta freedom (f=1). Not yet checked against data.

**[2026-06-30 15:54 UTC] — Result.**

The $a_0$ coefficient now has two identified geometric contributions:
1. spectral integral (amplitude floor) — undetermined, correctly located (spectral shape);
2. orbital-coherence factor f (per-system projection) — computed.
Disk-vs-bulge RELATIVE normalization: derived. Absolute disk normalization: still open, now
a spectral-integral problem (not a single-wavelength choice).

**[2026-06-30 15:54 UTC] — Critical assessment.**

DERIVED: coherence factor f and the disk/bulge normalization offset (modulo Maxwellian
ellipsoid + gravitomagnetic-analogy sourcing).
ASSUMED: virial closure v_rot=beta sigma with roughly constant beta (idealization; the
spread is the predicted scatter); gravitomagnetic sourcing by analogy; Maxwellian (sets the
0.627). Spectral integral NOT done — absolute a0 still open.

This builds constructively on the prior negative result: same conclusion (single-wavelength
coefficient not derivable) + the user's reframing (spectrum + coherence) that turns it into
two well-posed sub-problems, one solved.

**[2026-06-30 15:54 UTC] — Visual produced.**
SVG: disk (aligned orbits, f≈1, strong coherent B_c axis) vs bulge (random orbits, small
drift, f≈sqrt(pi/8) v_rot/sigma, weak B_c).

**[2026-06-30 15:54 UTC] — Deliverables.**
- `UPDATE_T14_T17_Bc_Axis_Coherence.md`
- `SESSION_LOG_Bc_Axis_Coherence.md` (this log)

**Next computations flagged:** (1) posit a connecton re-emission spectrum and compute the
fluctuation-floor integral fixing the absolute disk a0; (2) test the M-σ scatter-vs-(v/σ)
prediction against resolved-kinematics data (predicted sign: lower beta → higher M/σ^4).
