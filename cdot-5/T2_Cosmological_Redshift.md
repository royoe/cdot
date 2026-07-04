# T2 — Cosmological Redshift

## Observational Background

Spectral lines from distant galaxies are systematically shifted to longer wavelengths
(redshifted). The shift is quantified by
$$1 + z = \frac{\lambda_\text{obs}}{\lambda_\text{emit}},$$
where $\lambda_\text{emit}$ is the rest-frame wavelength of the transition and
$\lambda_\text{obs}$ is the measured wavelength. Redshift is observed to be:
- Ubiquitous: all galaxies beyond the Local Group show $z > 0$.
- Systematic with distance: nearby galaxies have small $z$, distant galaxies large $z$
  (the Hubble relation $v = H_0 D$ at low $z$).
- Achromatic and line-ratio-preserving: all transitions from the same source shift by
  the same factor $1+z$, and the ratios of transition frequencies within a multiplet
  are unchanged to high precision.

The last point is particularly constraining — it means the *pattern* of atomic energy
levels is the same in distant sources as locally, even if overall energy scales differ.

In standard $\Lambda$CDM, redshift is a metric effect: space expands, stretching photon
wavelengths in transit. The photon loses energy proportionally to the scale factor;
$1+z = a_\text{now}/a_\text{emit}$.

---

## The Model's Mechanism

In this model, space is static (premise 1). There is no stretching of wavelengths in
transit. Instead, the redshift arises because **the atomic energy scale has changed**
between emission and observation.

### Why photon frequency is conserved in flight

Premise 4 states that $h$ and $e$ are invariant and that photon frequency $\nu$ is
constant from emission to observation. This is the "energy-conserving map frame": the
map was specifically constructed so that photons do not lose energy in transit. This
is the symmetric counterpart to standard cosmology, which conserves rest energy and
lets photon energy drop.

### How atomic frequencies change with epoch

The Rydberg (atomic transition) energy is
$$E_\text{Ryd} = \frac{m_e e^4}{8\epsilon_0^2 h^2}.$$
With $e$ and $h$ invariant (premise 4), $m_e$ invariant (premise 3), and
$\epsilon_0 \propto c^{-1}$ (forced by electromagnetism — $c=1/\sqrt{\epsilon_0\mu_0}$
must hold at every epoch, and $\epsilon_0,\mu_0$ must scale identically or the impedance
of free space would drift and polarization structure could not survive propagation):
$$E_\text{Ryd} \propto c^2, \qquad \nu_\text{atomic} = E_\text{Ryd}/h \propto c^2.$$
An atom at an earlier epoch, when $c$ was smaller, emitted transitions at genuinely
lower frequencies than the same atom today. This is not an energy loss by the photon;
it is a difference in the reference standard. **This scaling is fixed by premises 3 and
4 alone — it does not reference how $c$'s cosmological history is generated, so it is
identical in every counting-law variant this model has used, past or present.**

### The squared redshift law

A spectrograph measures the ratio of the incoming photon wavelength to a local
reference line for the same transition. Both are now in the same epoch (same
$c_\text{now}$), so the local $c$ cancels. What remains is the ratio of the emitted
atomic frequency (at $c_\text{emit}$) to the local atomic frequency (at $c_\text{now}$):
$$1 + z = \frac{\nu_\text{ref,now}}{\nu_\text{phot}}
= \frac{c_\text{now}^2/h}{c_\text{emit}^2/h}
= \left(\frac{c_\text{now}}{c_\text{emit}}\right)^2.$$
Equivalently:
$$\frac{c_\text{emit}}{c_\text{now}} = (1+z)^{-1/2}, \qquad K \equiv \frac{c_0}{c_z} = (1+z)^{1/2}.$$
For $z = 1$: $c_\text{emit} = c_\text{now}/\sqrt{2} \approx 0.707\,c_\text{now}$ (not
$0.5\,c_\text{now}$ as a naive linear law would give).

### Why "squared" and not something else

The power-2 law is not an independent assumption; it follows from:
- $m$ invariant ($s = 0$)
- $e, h$ invariant
- $\epsilon_0 \propto c^{-1}$ (EM-forced)

For a general mass scaling $m \propto c^s$, the result is $1+z = (c_\text{now}/c_\text{emit})^{s+2}$.
The redshift power $P = s+2$ and the mass scaling $s$ are the same degree of freedom.
Measuring the shape of the redshift–distance relation effectively measures $s$, making
the supernova Hubble diagram a direct test of the mass-scaling assumption (T4).

---

## Line Ratios and Fine Structure

The observation that line ratios within multiplets are unchanged at high $z$ is
automatically satisfied: the ratio of two atomic transition energies involves only the
same $E_\text{Ryd}$ scale, which cancels. The redshift shifts all lines by the same
factor $1+z$, which is exactly what the squared law delivers (it is a universal
multiplicative shift applied to all transitions from the same source).

The fine-structure constant $\alpha = e^2/(4\pi\epsilon_0\hbar c)$ is invariant
classically: with $e, h$ invariant and $\epsilon_0 \propto c^{-1}$, the factors of $c$
cancel identically. This is consistent with the tight observational bounds on $\alpha$
variation (T7).

---

## The Hubble Relation at Low $z$

For a source at small $z \ll 1$, expanding the proper-distance–redshift relation to
first order in $z$ gives, for *any* smooth static-map distance function $D_p(z)$
(regardless of the specific counting law behind it — this is a purely low-order
statement):
$$D_\text{p}(z) \approx \frac{c_0}{H_0^{\text{obs}}} z + O(z^2).$$
Defining the apparent recession velocity $v = cz$, this is Hubble's law $v = H_0 D$
with $H_0 = H_0^{\text{obs}}$. The Hubble relation emerges at low $z$ for any smooth
cosmology; it does not by itself test which model is correct, and it does not test
which counting law is behind the distance mapping either. The discriminating
information is in the curvature of $D_p(z)$ — the deceleration parameter $q_0$, and more
generally the full shape — which appears at order $z^2$ and above (T3, T4).

---

## Comparison with $\Lambda$CDM

| Property | $\Lambda$CDM | This model |
|---|---|---|
| Physical origin of redshift | Metric expansion, photon wavelength stretched | Changing atomic energy scale; photon frequency conserved |
| Redshift law | $1+z = a_\text{now}/a_\text{emit}$ | $1+z = (c_\text{now}/c_\text{emit})^2$ |
| What is "stretched" | The photon wavelength | Nothing — the reference changes |
| Energy conservation | Photon energy drops; rest energy conserved | Photon energy conserved; rest energy changes |
| Low-$z$ Hubble law | Yes (by construction) | Yes (by construction) |
| High-$z$ deviations | Acceleration in the standard fit | Model-dependent shape; currently under active revision (T3, T4) |
| $\alpha$ variation | Not directly predicted | Classically invariant (T7) |

The key observational difference is not in the existence of redshift but in the
**shape of the redshift–distance relation at $z \gtrsim 0.1$**. That shape is set by
the counting law (Core Principles §1, §3–§4a), not by anything in this document — this
document fixes only the *relationship* between $c_\text{emit}/c_\text{now}$ and the
observed $z$, which is independent of how $c$'s cosmological history is generated. This
is why this document required no rework when the counting law changed for cdot-5 (see
`Change_Document_cdot4_to_cdot5.md`): the redshift mechanism and the distance mapping
are genuinely separable pieces, and this is the mechanism piece.

---

## Open Questions

- The derivation assumes the spectrograph comparison is purely local (ratio of photon
  wavelength to local reference line). This is standard in observational astronomy, but
  the formal justification in a variable-$c$ spacetime — ensuring no path-dependent
  $c$ factors enter the instrument — deserves explicit treatment.
- The mass-scaling degree of freedom ($s$, hence $P=s+2$): $s=0$ is theoretically
  preferred (invariant rest mass), but a precise measurement of the redshift–luminosity
  relation (a Pantheon+ fit, T4) directly constrains $s$, independent of which counting
  law it is paired with.
- **Retired.** An earlier open question asked whether different counting-law exponents
  (volume/surface/S$'$) would give different $D_p(z)$ shapes with the same redshift
  mechanism, distinguishable via the SN Hubble diagram. That whole exponent family is
  now superseded by the connectivity-counting law (Core Principles §1); the underlying
  point survives as a demonstrated fact rather than an open question — the redshift
  mechanism above is untouched by the counting-law change, while $D_p(z)$'s shape
  changed completely, direct confirmation that the two are separable. See
  `cdot-4/T2_Cosmological_Redshift.md` for how this question was originally posed.
