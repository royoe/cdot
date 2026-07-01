# SESSION LOG — Disk Flattening: The Connecton Vertical Spring (T19 request)

**Topics:** T14 (Connecton Gravity), T17 (Morphology), → new T19
**Date:** 2026-07-01
**Session type:** Mechanism investigation + new-topic request. Transition/bulge checks
required before finalizing.

---

## Timeline

**[2026-07-01 ~11:00 UTC] — Prior turn (scoping).**
Explored the full 3D Lorentz force on a disk star. Found: purely vertical B_c does not act
on v_z (only in-plane cyclotron coupling); but a dipole-like B_c (sourced by disk
circulation) has an off-plane radial component B_r, and v_phi x B_r gives a vertical force,
restoring toward the midplane, sign fixed by the same dipole as the in-plane outward force.
No-work theorem: static vxB cannot damp; instead it is a vertical spring that thins the disk
geometrically (raises omega_z, shrinks z_max at fixed energy, sigma_z unchanged). omega_L^2
~ 3 v_f^2/r^2, tied to the same B_c=v_f/r, comparable to gravity. User asked to (a) make it a
new topic, (b) verify the transition works and preserves the bulge before finalizing.

**[2026-07-01 11:15 UTC] — User prompt (verbatim):**
> I feel we should make the change document a request for a new topic on disk flattening,
> rather than bloat the old topics too much. But before completing, I'd like to make sure
> that the transition works, and that we can preserve the bulge inside the transition.

**[2026-07-01 11:15 UTC] — Work performed (the required checks).**

Radial gate: vertical-spring/gravity ratio ~ g_x/g_bar (g_x from RAR closure). Computed
across the transition:
- inside r_t (g_bar>>g_d): g_x/g_bar -> g_d/g_bar -> 0. Spring vanishes.
- outside r_t (g_bar<<g_d): g_x/g_bar -> sqrt(g_d/g_bar) -> large. Spring dominates.
- crossover exactly at r_t (ratio 1/phi=0.62 at g_bar=g_d).

CRITICAL catch: bulge and disk OVERLAP in radius. At shared r the radial gate is identical
for both -> radial gate ALONE cannot spare an embedded bulge. The COHERENCE gate (T17,
f=sqrt(pi/8)v_rot/sigma) is load-bearing: vertical spring needs coherent B_c, which only
ordered (disk) orbits source/feel; random (bulge) orbits are spared everywhere.

Mechanism: spring ~ (g_x/g_bar) x f. Flattened iff BOTH outside r_t AND ordered.

Feedback / two attractors: disk (thinning->more order->stronger spring->more thinning,
self-limiting as f->1) and bulge (random->weak spring->stays random). Two stable fixed
points = observed disk/spheroid dichotomy from one field.

**[2026-07-01 11:15 UTC] — Result.**

Both checks PASS: transition works (spring off inside r_t, on outside), bulge preserved —
but the load-bearing reason is the COHERENCE gate, not the radial gate (they coexist in
radius). New mechanism: same B_c that flattens the rotation curve also thins the disk
(vertical spring), geometrically (no damping, no-work-theorem-safe), with two-attractor
dichotomy. Tied to B_c=v_f/r, no new parameter.

**[2026-07-01 11:15 UTC] — Critical assessment.**

Stress-tested before banking (given this thread's history of over-clean claims):
- sign consistency PASS (one dipole fixes both forces);
- no-work PASS (geometric compression, not damping; sigma_z unchanged, h drops);
- magnitude: O(1) comparable robust, factor 3 idealization-dependent;
- transition/bulge PASS with the coherence-gate caveat as the key non-obvious point.
Caveats retained: point-dipole idealization (factor imprecise), feedback qualitative not
dynamical, B_c-presence-during-settling assumed, depends on T14/T17 (speculative).

Explicitly flagged that "spring just turns off at small r" is the WRONG simplification —
the coherence gate is what spares embedded bulges.

**[2026-07-01 11:15 UTC] — Deliverables.**
- `NEW_TOPIC_T19_Disk_Flattening.md` (new-topic request)
- `SESSION_LOG_Disk_Flattening.md` (this log)

Minimal edits requested to T14/T17 (one-line pointers) and Core §7 (one new row); no
bloat to existing topics, per user preference.

**Possible next steps:** (1) compute extended-disk B_c geometry to pin the O(1) factor and
the h–v_f relation; (2) test predictions 1–3 (scale height vs v_f, thinness onset at r_t,
thickness vs v/sigma) against real disk data.

---

## Iteration 2 — Evolution section + halo lifetime  [2026-07-01 11:36 UTC]

**User prompt (verbatim):**
> Please keep updating the T19 request and appending the session log. We need a few more
> iterations. After adding the previous discussion, I'd like to do a check: What would be the
> lifetime of the current MilkyWay halo given the dynamics we have derived? The halo is
> constantly replentished by ejected stars, but we hope to balance flattening with
> replentishing.

**Work — (a) folded the Cosmic Evolution section into T19 (new §6).**
Epoch scalings from core cosmology (c ∝ (1+z)^{-1/2}, g_dagger=cH^hor/3, invariant G,M, static
orbits T9):
  g_dagger ∝ (1+z)^{-5/6}; v_f, B_c ∝ (1+z)^{-5/24}; omega_L^2 ∝ (1+z)^{-5/12} (spring
  strengthens with time); r_t ∝ (1+z)^{+5/12} (transition shrinks with time).
Evolutionary picture: r_t sweeps INWARD through static orbits -> disk (spring-on) grows
OUTSIDE-IN; early galaxies thick/spheroidal (r_t large), present = thin disk outside residual
bulge. Coherence lock-in: material virialized random (hot) inside r_t has low f, spring gated
off when r_t passes -> stays bulge-like (frozen-in). Bulge = early-randomized, disk =
late-ordered. Checks: adiabatic (r_t shrinks 1.3x over 8 Gyr >> t_dyn 0.2 Gyr); NOT a
replacement for dissipative disk formation (spring maintains order, can't create it from
collisionless stars); outside-in spring activation != inside-out mass growth (different
quantities). Predictions: boundary r_t ∝ (1+z)^{5/12}, thickness ∝ (1+z)^{-5/12}, high-z more
bulge-dominated — all observed direction.

**Work — (b) Milky Way halo lifetime / flattening-replenishment balance (new §8).**
Rates: ejection (flattening) estimated INDEPENDENTLY from disk heating (2.5sigma tail per ~3
Gyr) -> R_ej ~ 0.1 Msun/yr (range 0.02-0.4). SF replenishment ~1.5 Msun/yr. R_ej << R_SF ->
replenishment-dominated, NO runaway (genuine consistency test, passed — could have failed if
ejection stripped disks faster than SF).
Halo = circulating reservoir: right-of-transition stars pushed out but BOUND (marginal), don't
escape, slow fall-back, residence ~ Hubble time.
Independent check (avoid circularity): heating-driven R_ej accumulated over age gives
1e8-1e9 Msun halo, BRACKETS observed MW stellar halo (~1e9) WITHOUT using it as input.
Lifetime tau_halo = M_halo/R_ej ~ 10 Gyr ~ galaxy age. Long-lived quasi-steady reservoir.
Balance: gas->disk(1.5)->ejection(0.1)->marginally-bound halo(residence~age)->fall-back.
Flattening and replenishing DO balance.

**Critical assessment.** Caught and fixed a units-label slip (1e8 Msun/Gyr = 0.1 Msun/yr, not
Msun/yr). Flagged the partial circularity (used M_halo to get R_ej) and defused it with the
independent heating-based estimate. Robust content is the ORDERING (R_ej << R_SF; residence ~
age), not the exact rate. Honest caveats retained: R_ej bracketed to a factor of a few;
residence~age assumed not solved; halo partly accreted (Lorentz ejection is one contributor).

**Deliverables this iteration:** updated NEW_TOPIC_T19_Disk_Flattening.md (added §6 Evolution,
§8 Halo Lifetime; renumbered), this appended log.

**Open for next iterations:** pin the O(1) dipole factor (extended-disk B_c geometry); solve
fall-back dynamics for residence time; predicted h(z) and r_t(z) vs JWST high-z morphology;
whether ejected-then-returning stars re-order or stay hot (disk/halo exchange kinetics).

---

## Iteration 3 — Halo thread dropped; dipole factor → SIGN AMBIGUITY found  [2026-07-01]

**User prompt (verbatim):**
> Let's drop the halo star issue for the moment. I'm concerned that the ejection timescale
> that feeds the halo may not be well defined. It needs to come from several channels
> including multiple star ejections, mostly driven by cluster dynamics, as well as SN driven
> ejections and ejections from the central BH. If there was a predicted discrepancy in the
> literature between ejections and the total mass of the halo, it would have made sense to
> pursue this, but I'm not aware of such a thing. Let's proceed with the dipole factor.

**(a) Halo thread de-scoped.** Agreed: the ejection timescale is not well-defined — multiple
channels (cluster-dynamics multiple-star ejections, SN-driven, central-BH ejections), none
cleanly predictable, and no standing literature discrepancy between ejection budget and halo
mass to motivate it. §8 of T19 is therefore of limited value and somewhat overstated; flag it
as illustrative-only / de-scoped. (Did not delete it, but it should not be presented as a
result. Recommend demoting §8 to a note or removing on merge.)

**(b) Dipole factor — attempted to pin the O(1); found a SIGN problem instead.**
Point-dipole idealization gave omega_L^2 ~ 3 v_f^2/r^2 with a RESTORING (confining) force.
Extended-disk derivation from div B_c=0 + curl-free off-disk region:
  b1(r) = (dB_r/dz)|_0 = dB_z/dr|_0 = B0'(r).
With the attractor midplane profile B0 = v_f/r (monotonically decreasing): b1 = -v_f/r^2 < 0,
giving F_z = -kappa m v_phi B_r = +kappa m v_phi v_f/r^2 * z => POSITIVE coefficient on z =>
ANTI-CONFINING (force away from plane). OPPOSITE sign to the point-dipole result.

Diagnosis: the sign hinges on sign(B_z) in the disk plane, i.e. on the connecton current
geometry. Point dipole in its EQUATORIAL plane has B_z<0 (opposite the on-axis field); setting
|B_c|=v_f/r there embeds the restoring sign. A slowly-decreasing field of the axial sign
(B_z=+v_f/r) gives anti-confining. Both derivations internally correct; they assumed opposite
B_z signs. The rotation-curve attractor fixes only |B_c|=v_f/r (magnitude), NOT the sign of
B_z or its off-plane continuation.

**Result.** The vertical-force SIGN is UNDETERMINED by current inputs — load-bearing, because
it decides whether the mechanism thins (restoring) or thickens (anti-confining) disks. This is
now the PRIMARY open item for T19, above the O(1) magnitude. Resolving it requires deriving the
actual current geometry of B_c (how the disk mass current sources the connecton gravitomagnetic
field), not yet done.

**Critical assessment.** Did NOT compute a magnitude on top of an undetermined sign (would be
misleading). Did NOT overwrite §§2–6; instead added a prominent sign-ambiguity flag in §3 and
promoted it to the leading caveat in §9. Honest status: T19's disk-thinning direction is
conditional on the restoring-sign geometry; if anti-confining, the core claim reverses. This is
the correct place to pause — magnitude is meaningless until the sign is fixed.

**T19 edits this iteration:** added ⚠ sign-ambiguity flag (§3); promoted sign to primary caveat
(§9); halo §8 flagged as de-scoped/illustrative (recommend demotion on merge).

**Open for next iterations:** (1) derive the connecton B_c current geometry from the disk mass
current — this fixes sign(B_z) and resolves confining vs anti-confining; (2) only then pin the
O(1) magnitude; (3) if anti-confining, reassess whether any geometry (e.g. field reversal
across the disk, or the coherence-sourced axis) restores confinement, else T19's thinning claim
is withdrawn.

---

## Iteration 4 — Ringed-disk B_c model: SIGN RESOLVED (confining), magnitude O(1)  [2026-07-01]

**User prompt (verbatim):**
> I don't think we can avoid having a model for the actual B_c vector field, but a simple
> model should be ok. The disk model can be approximated as a simple disk with rings of
> different mass and velocity. The bulge component is trickier. Perhaps start with just a
> model for the disk?

**Work.** Modelled B_c as the gravitomagnetic (Biot-Savart) field of coplanar mass-current
rings (mass current per ring ∝ Sigma(a) v_phi(a) da), using the standard current-loop
elliptic-integral field. Computed (dB_r/dz)|_0 (sets the vertical-force sign) and B_z(midplane)
(the in-plane rotation-curve field) across radii and for several Sigma profiles.

Results:
- SIGN: dB_r/dz > 0 at ALL radii, for exponential / flat / outer-rising Sigma. F_z = -kappa m
  v_phi B_r is RESTORING (confining). Disk thins. Robust.
- Diagnosis of the earlier anti-confining result: the "curl-free off-disk" derivation applied
  a vacuum relation (dB_r/dz = dB_z/dr) in the plane where the current sits (not vacuum). The
  ringed model computes the real field and does not make that error. Physical picture:
  current-loop / magnetic-mirror geometry, field lines curve back through the plane and push
  displaced orbiting stars toward the midplane.
- MAGNITUDE: raw thin-sheet geometric factor G(r)=r(dBr/dz)/|Bz_mid| is huge (70-6000) and
  grows outward — but this is the thin-sheet singularity. Regularizing with finite disk
  thickness h0/Rd ~ 0.1-0.3 gives G ~ 1-5. Confirms omega_L^2 ~ 3 v_f^2/r^2 (O(1)xgravity).
- Residual wrinkle: razor-thin B_z(midplane) is small and sign-changes (~r/Rd~2.7), so the
  in-plane (rotation-curve) field and the near-plane vertical gradient may have different
  effective geometries; the rotation-curve B_c is plausibly smoother than a thin sheet. Affects
  the precise factor (via O(1) normalization eta), not the sign or order.

**Critical assessment.** The ringed model was worth doing: it RESOLVED the load-bearing sign
ambiguity from iteration 3 (confining, robustly) and explained why the abstract derivation was
wrong (vacuum relation misapplied at the source). Caught the huge G as a thin-sheet artifact
rather than reporting it as a tension, and verified via finite-thickness regularization that
the magnitude is O(1) as estimated. Did not over-claim a precise factor — G~1-5 depends on
thickness and eta.

**T19 edits this iteration:** §3 flag changed from "⚠ SIGN AMBIGUITY" to "✓ SIGN RESOLVED —
CONFINING" with the ringed-disk derivation, magnitude confirmation, and residual wrinkle;
leading caveat in §9 updated to "sign resolved (confining)"; added thickness-dependence and
ringed-model-is-minimal caveats.

**Open for next iterations:** (1) the bulge/spheroid B_c contribution (user noted it is
trickier — random orbits, coherence factor f; the disk model does not cover it); (2) pin the
O(1) factor with a self-consistent finite-thickness disk + smoother large-scale in-plane B_c
(resolve the eta normalization and the thin-sheet B_z sign-change wrinkle); (3) predicted
h(r,z-history) and the h-v_f relation now that the sign and order are fixed.

---

## Iteration 5 — Bulge B_c model: spared, dominated by geometry not coherence  [2026-07-01]

**User prompt (verbatim):**
> Let's continue with the bulge component. Is there some way we can model it simply with just
> the known mean cylindrical rotation of 100 km/s and dispersion of 100-150 km/s?

**Work.** Modelled the bulge as a rotating spheroid (q~0.8) of coherent mass-current rings:
current per ring ∝ rho_bulge(a,zc) * v_rot, since only the mean rotation sources a coherent
B_c (random dispersion averages to zero vectorially). Used v_rot=100, sigma=100-150 km/s.
Computed the off-plane (dB_r/dz)|_0 (vertical-force sign & magnitude) and compared to (i) an
equivalent disk and (ii) the bulge's own gravity.

Results:
- SIGN: dB_r/dz > 0 => confining (same as disk). A round bulge would be very slowly thinned,
  not thickened.
- MAGNITUDE: bulge vertical spring ~ 2-4% of the bulge's OWN gravity across sigma=100-150.
  Safely << 1 => bulge SPARED, keeps 3D shape.
- AUDIT (guarding against stacked suppressions): decomposed the ratio. Caught a DOUBLE-COUNT
  — the "source incoherence f" was already included by using the coherent v_rot as the ring
  current (random part averaged out). Dropped it. With a single correct responder-coherence
  factor v_rot/sqrt(v_rot^2+3 sigma^2)~0.4-0.5, SPRING/BULGEGRAV ~ 0.02-0.04.
- DOMINANT effect: GEOMETRY, not coherence. A round distribution spreads current rings over
  many heights -> off-plane B_r partially CANCELS -> ~4% of disk spring on geometry alone.
  Coherence trims a further ~2x. So the bulge is spared PRIMARILY by geometric B_r cancellation
  (round -> self-cancelling off-plane field); coherence is secondary.

**Critical assessment.** The audit mattered: my first assembly stacked two coherence factors
and one was double-counting. Removing it revealed the physically cleaner and more robust story
— geometry (roundness) does the sparing, not a pile of suppression factors. This is exactly
the failure mode to avoid (manufacturing a small number by stacking O(1)s), and the audit
prevented it. Explains morphology from one field: flat -> B_r adds (thins more); round -> B_r
cancels (resists) — geometric feedback consistent with §5 two-attractor picture. Refines the
§4 claim: for a spatially distinct round bulge, GEOMETRY spares it; the coherence gate is most
important where disk/bulge stars coexist at the same location.

Caveats retained: 2-4% depends on spheroid flattening q=0.8 and scale ratios; virial gravity
proxy omega_grav~sigma/Rb, not a solved potential. Robust: spring << gravity, geometric
cancellation dominant, confining sign.

**T19 edits this iteration:** added "Ringed-spheroid check" subsection to §4 (bulge spared,
geometry-dominated, double-count corrected, caveats).

**Open for next iterations:** (1) solved bulge potential instead of virial proxy for a firmer
percentage; (2) the disk/bulge coexistence region — quantify where geometry vs coherence
dominates the sparing; (3) with disk sign+magnitude and bulge sparing both fixed, derive the
predicted h-v_f relation and compare to real disks / JWST high-z thickness.
