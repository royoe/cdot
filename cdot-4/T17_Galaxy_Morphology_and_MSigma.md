
# T17 — Galaxy Morphology and the M-σ Relation

*Note: this topic is qualitative and speculative. The four observational links
below each have a sign-level check that passes, but no quantitative derivation
of magnitudes, timescales, or functional forms has been done. The content depends
on the unproven dynamical-selection / Lorentz-term mechanism of T14.*

**Note (cdot-4):** In addition to the unproven T14 Lorentz mechanism, this topic
depends on orbital expansion r∝c² (T9, cdot-3) as the driver of dynamical
selection. Under invariant G (cdot-4), orbits are static and the orbital-expansion
driver is removed. The 'Flatness as a Dynamical Attractor' picture must be
re-derived without this driver (see T14 flag). The four-link observational chain
and its qualitative checks remain on record, but the underlying mechanism needs
reconstruction. The qualitative morphological observations themselves are
unaffected.

---

## Observational Background

### The M-σ Relation

The M-σ relation (Ferrarese & Merritt 2000; Gebhardt et al. 2000) states that the
mass of the central supermassive black hole $M_\text{BH}$ correlates tightly with
the **velocity dispersion $\sigma$ of the host bulge** (not the disk):
$$M_\text{BH} \propto \sigma^4.$$

The same relation, written using flat-curve velocity $v_f \approx \sigma$, connects
to the Baryonic Tully-Fisher Relation (T6):
$$M_\text{BH} \sim \sigma^4 \sim v_f^4 \sim GM_\text{bary}\,a_0,$$
i.e. BH mass tracks the galactic Tully-Fisher normalization.

**Key observational facts:**
- M-σ correlates with the *spheroid* (bulge or elliptical body), not the disk.
  Pure disk galaxies with small or absent bulges have correspondingly small or
  absent SMBHs.
- Giant ellipticals and brightest cluster galaxies (BCGs) show **over-massive BHs**
  relative to the naive M-σ extrapolation — the relation steepens or breaks
  upward at the top end.
- Elliptical galaxies have no disk component; their stars are on
  pressure-supported (random-motion) orbits rather than rotation-supported
  (ordered) orbits.

### The Disk-vs-Elliptical Dichotomy

Spiral galaxies are rotation-dominated (disk + bulge); ellipticals are
pressure-dominated (no disk). Intermediate morphologies exist (lenticulars, S0s),
but the two extremes are well-defined. The correlation with BH mass is striking:
the most massive SMBHs are found in giant ellipticals.

---

## The Model's Account: Dynamical Selection

The mechanism connecting these observations in this model is the
**Lorentz-force / dynamical-selection picture** of T14. This section translates
that mechanism into morphological predictions.

### The Two-Component Force Law

The model (T14, speculative) proposes that in addition to Newtonian gravity, there
is a velocity-dependent term:
$$\mathbf{g} = \mathbf{g}_\text{Newton} + \mathbf{v} \times \mathbf{B}_c,$$
where $\mathbf{B}_c$ is a magnetic-like component of the $c$-field. For a flat
rotation curve this requires $B_c \sim v_f/r$ — i.e. $B_c$ has dimensions of an
angular frequency and, from the M-σ connection, $B_c \sim M_\text{BH}^{1/4}/r$
(dimensional argument; not derived from a microscopic model).

### Flatness as a Dynamical Attractor

In the **dynamical selection** picture (T14), rotation curves are not a static
force-balance solution. **[FLAG — orbital expansion driver removed, cdot-4]** The
following picture assumes orbital expansion r∝c² as the primary driver (T9,
cdot-3). Under invariant G, this expansion is absent. The mechanism must be
reconstructed — the Lorentz term v×B_c still exists but the trigger ('orbits
expand, outer rings unbind') is gone. Pending re-derivation, the following text is
preserved for record. As $c$ grows, orbits expand ($r \propto c^2$, T9). A
Lorentz-type velocity-dependent force acts as a **velocity selector**: stars in
rings whose orbital speed makes the Lorentz term too strong become unbound and
are ejected to intergalactic space. The flat rotation curve is the **marginally
bound surviving population** — an evolutionary attractor rather than a solution
forced by the force law.

This dissolves the "static wall" discussed in T5 and T14: the force law does not
need to produce flatness at every instant; it only needs to eject over-supported
rings, and survivors satisfy $B_c(r) = v_f/r$, which is the flat condition.

### Ordered vs. Random Orbits: Disk Stripping

The Lorentz term $\mathbf{v} \times \mathbf{B}_c$ is large when $\mathbf{v}$ is
large and ordered (coherent rotation), and small when $\mathbf{v}$ is random
(pressure support).

- **Disk stars (rotation-dominated, high ordered $v$):** the Lorentz term is large
  → strong ejection force → disk stars are selectively stripped over cosmic time.
- **Bulge/spheroid stars (pressure-dominated, random $v$):** the Lorentz term
  averages to near zero (random directions, low ordered component) → weak ejection
  → spheroid stars are retained.

A galaxy with a very massive central BH (sources a stronger $B_c$) sheds its disk
most rapidly and ends as a pure spheroid — an **elliptical galaxy**. A galaxy with
a small BH keeps its disk. This is a qualitative account of the disk/elliptical
dichotomy tied to BH mass.

---

## The Four-Link Chain (OP-19)

The model makes four qualitative predictions about the M-σ / morphology connection.
Each link is checked against observation.

### Link 1: M-σ Is a Bulge (Spheroid) Relation

The model predicts M-σ should correlate with the *spheroid* component, since the
spheroid is what survives the Lorentz stripping. **Observation:** M-σ indeed
correlates with spheroid velocity dispersion, not disk kinematics. ✓

### Link 2: Giant Ellipticals Are the End of the Bulge Sequence

Classical bulges → ellipticals is a continuous sequence; giant ellipticals are
"all bulge" (the disk is entirely stripped). **Observation:** this matches the
standard morphological classification — ellipticals are pressure-supported systems
with no disk, consistent with being a bulge-only remnant. ✓

### Link 3: Disks Are Stripped by the Lorentz Term (Velocity Selectivity)

Disks are rotation-supported (high ordered $v$) → strong Lorentz ejection.
Spheroids are pressure-supported (low ordered $v$) → weak Lorentz retention.
A high-mass BH (strong $B_c$) → fast disk stripping → ends as a pure elliptical.
**Observation:** the most massive SMBHs are hosted by ellipticals, not spirals;
disk galaxies have comparatively smaller BHs. ✓ (qualitatively)

### Link 4: Giant Ellipticals Show Over-Massive BHs (Evaporation Ceiling)

If outer mass is ejected by Lorentz stripping, the stellar velocity dispersion
$\sigma$ saturates at the remaining bound core while $M_\text{BH}$ keeps growing
(if BH growth continues, e.g. through mergers or accretion). This makes
$M_\text{BH}$ lie *above* the naive M-σ extrapolation at the top end.
**Observation:** giant ellipticals and BCGs do show over-massive BHs and a
steepening or break in the M-σ relation at the top end. ✓

---

## Connection to PBH Formation (T16)

If central SMBHs are built by PBH mergers (T16), and the galactic dark matter halo
is also a PBH remnant, then the M-σ relation has a common origin in the primordial
PBH mass distribution:

- The central SMBH mass $M_\text{BH}$ is set by the merger history of the central
  PBH seed.
- The halo PBH population sets the galactic dark matter and hence the flat-curve
  velocity $v_f$.
- The M-σ consistency condition $M_\text{BH}^{1/4} \sim (GM_\text{bary}\,a_0)^{1/4}/r$
  (T14) then becomes a *statement about the PBH mass distribution*, not an
  independent relation.

Whether the primordial PBH population from genesis naturally produces the observed
M-σ normalization is unworked.

---

## Connection to T14's Dynamical Selection Prediction

The dynamical selection picture (T14) makes an independent prediction: galaxies
should **lose outer rings to intergalactic space** over cosmic time as $c$ grows.
This is distinct from the rotation-curve flatness claim:

- **Intracluster light (ICL):** stripped disk stars should populate the
  intracluster medium. ICL is observed and growing with time — consistent
  qualitatively with Lorentz stripping, though tidal stripping also contributes.
- **Intergalactic stars:** stray stellar populations far from any galaxy, with
  streams that look tidal but have no obvious tidal cause, would be a
  distinctive prediction.
- **Morphological evolution:** the disk/elliptical fraction should evolve with
  redshift in a specific way — more disks at high $z$ (when $c$ was smaller,
  Lorentz term weaker), fewer at low $z$ (more stripping accumulated).
  **Observation:** indeed, high-$z$ galaxies are more disky (blue irregular and
  spiral-rich); the elliptical fraction rises toward $z = 0$. ✓ (qualitatively,
  though environment and mergers also contribute)

---

## Honest Assessment

The four links are separable, could have failed independently, and are internally
coherent: disks evaporate (high ordered $v$ → strong Lorentz), spheroids survive,
BH mass sets the evaporation strength, and the top-end M-σ break is the
evaporation ceiling. This is a single mechanism for three real observed facts.

However, the entire chain is:
1. **Qualitative / sign-level only.** No quantitative derivation of the
   evaporation timescale, the disk-vs-spheroid Lorentz contrast, the M-σ slope,
   or the break location.
2. **Dependent on the unproven $v \times B_c$ force** with $B_c \sim M^{1/4}/r$
   — a non-analytic source scaling that no linear gravitomagnetic mechanism provides
   (T14, the non-analytic source wall).
3. **Dependent on PBH formation** (T16, T13) for the SMBH seed thread.

It is recorded because the four observations are checked and the mechanism is
coherent, not because a working force law has been derived.

---

## Falsifiable Handles (To Compute Later)

- **Disk-stripping timescale:** does the predicted stripping rate, given a
  plausible $B_c$ normalization, match the observed disk/elliptical fractions as
  a function of redshift and BH mass?
- **σ-saturation mass scale:** at what BH mass does the Lorentz stripping remove
  enough of the stellar envelope to cause σ to saturate? Does this match the
  observed M-σ break location?
- **Disk/spheroid Lorentz contrast:** the ratio of (ordered velocity)/(velocity
  dispersion) between disk and spheroid stars quantitatively determines how much
  more effective stripping is in disks. Does this ratio track the observed
  morphology-$M_\text{BH}$ correlation?
- **ICL growth rate:** the rate at which intergalactic stars are added to the ICL
  should track the Lorentz ejection rate — faster in galaxies with higher $v_f$
  and higher $M_\text{BH}$. This is observationally testable with deep surface
  photometry.

---

## Open Questions

- Can the $v \times B_c$ force law be derived from the connecton sea (T14) with
  a non-analytic source coupling $B_c \propto M^{1/4}$? The criticality-as-license
  mechanism (T14) is the best candidate; it requires a black-hole critical surface
  to license the non-analytic term globally.
- Does the PBH seed channel (T16) naturally produce the M-σ normalization, given
  the primordial PBH mass distribution?
- Is the $c$-evolution-driven disk stripping distinguishable from tidal stripping
  by its kinematic signature (ejected stars have specific angular-momentum
  distribution predicted by the Lorentz-selection picture)?
- The M-σ relation holds over $\sim 5$ orders of magnitude in $M_\text{BH}$.
  Does the evaporation-ceiling picture predict the correct functional form and
  scatter over this range?
