
# T17 — Galaxy Morphology and the M-σ Relation

*Note: this topic is qualitative and speculative. The four observational links
below each have a sign-level check that passes, but no quantitative derivation
of magnitudes, timescales, or functional forms has been done. The BTFR and RAR
crossover follow from $g_\dagger = c^2/R_0 = cH_0^{\text{obs}}/6$ (horizon radius, Core
§4a) plus Newtonian gravity; the RAR closure is derived from connecton
indistinguishability (T14). The morphology chain and M-σ account additionally depend
on the dynamical-selection / Lorentz-term mechanism of T14 for the attractor. The
$B_c \propto M_\text{bary}^{1/4}/r$ amplitude is conditionally derived as a geometric
mean sourced by the baryonic mass, not the BH; $B_c$'s axis comes from the galaxy's
bulk circulation (§"What Sources $B_c$"); attractor convergence remains open. The same
coherence factor $f$ that gates the disk/bulge Lorentz stripping here also gates
vertical disk thinning — see T19.*

---

## Observational Background

### The M-σ Relation

The M-σ relation (Ferrarese & Merritt 2000; Gebhardt et al. 2000) states that the
mass of the central supermassive black hole $M_\text{BH}$ correlates tightly with
the **velocity dispersion $\sigma$ of the host bulge** (not the disk):
$$M_\text{BH} \propto \sigma^4.$$

The same relation connects to the Baryonic Tully-Fisher Relation (T6) through the
derived BTFR $v_f^4 = GM_\text{bary}\,a_0$ (T14):
$$M_\text{BH} \propto v_f^4 = GM_\text{bary}\,a_0.$$
The M-σ relation is a **derived consequence** — the same equation read through two masses
that the shared $a_0$ locks together — rather than an independent empirical coincidence.

The disk and bulge normalizations differ by a computed geometric factor. For the disk
($f\to1$), the BTFR gives $v_f^4 = GM_\text{bary}\,a_0$ directly. For the bulge
(coherence factor $f\approx0.627\,v_\text{rot}/\sigma$, §"What Sources $B_c$"), the
effective acceleration scale is $a_0^\text{eff}=f^2 a_0 = (\pi/8)\beta^2 a_0$ where
$\beta = v_\text{rot}/\sigma$. The deep-MOND balance in the bulge gives:
$$\boxed{M_\text{bulge} \sim \frac{8}{\pi\beta^2}\,\frac{\sigma^4}{G\,a_0}.}$$
The exponent 4 is preserved. The prefactor $8/(\pi\beta^2)$ varies with rotational
support ($\beta\sim0.3$–$1.0$ → prefactor $\sim28$–$2.5$), which explains the
disk/bulge normalization offset and predicts that **M-σ scatter tracks $v_\text{rot}/\sigma$**
(§"Falsifiable Handles").

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
where $\mathbf{B}_c$ is a magnetic-like component of the $c$-field, with dimensions of
an angular frequency. For a flat rotation curve the surviving population requires
$B_c \sim v_f/r$. The amplitude is sourced by the **baryonic** mass through the
transition-radius construction (T14):
$$B_c = \frac{(GM_\text{bary}\,g_\dagger)^{1/4}}{r},\qquad g_\dagger = \frac{c^2}{R_0} = \frac{cH_0^{\text{obs}}}{6},$$
conditionally derived as a geometric mean (attractor convergence assumed). The quarter
power sits on the baryonic mass, not on $M_\text{BH}$. Because $M_\text{BH}$ also tracks
$GM_\text{bary}\,a_0$ (the derived M-σ relation, §above), $B_c$ correlates observationally
with central BH mass — but the BH does not source it.

### What Sources $B_c$

$B_c$ is sourced by the baryonic mass distribution coupled to the cosmological
acceleration scale $g_\dagger = c^2/R_0 = cH_0^{\text{obs}}/6$ (T14) — the same two
ingredients as the RAR. It is **not** sourced by the central black hole (which would
break the universality of $a_0$ and the RAR's 0.13 dex tightness). The black hole mass
*correlates* with $B_c$ — both track $GM_\text{bary}\,a_0$ — but is a correlate, not
a cause. Throughout the morphology chain below, "high-$M_\text{BH}$ galaxy" means
"galaxy high on the shared $GM_\text{bary}\,a_0$ normalization, hence high $B_c$ and
high $M_\text{BH}$ together."

**$B_c$ is a vector: amplitude from the sea, axis from bulk circulation.** An isotropic
connecton sea supplies the amplitude but no preferred direction. $B_c$'s axis is set by
the galaxy's coherent mass current — the net circulation of baryons:

- **Disk** (ordered rotation): coherent current is strong, $f\to1$ → $B_c$ axis is
  well-defined and aligned → Lorentz filter acts at full strength.
- **Bulge** (dispersion-dominated, small net drift $v_\text{rot}$): the coherent
  fraction is
  $$f \approx \sqrt{\tfrac{\pi}{8}}\,\frac{v_\text{rot}}{\sigma} \approx 0.627\,\frac{v_\text{rot}}{\sigma}$$
  (from Monte-Carlo of a drifting Maxwellian). Effective $B_c\to fB_c$, so
  $a_0^\text{eff} = f^2 a_0$ for the bulge.

### Flatness as a Dynamical Attractor

In the **dynamical selection** picture (T14), rotation curves are not a static
force-balance solution. Under invariant G (cdot-4), the mechanism is a direct,
time-steady Lorentz velocity filter rather than the expansion-triggered ejection of
cdot-3 (see T14 for the full derivation).

For a disk star with tangential velocity $v_\phi$ at radius $r$, the Lorentz term
$\mathbf{v}\times\mathbf{B}_c = v_\phi B_c\,\hat{r}$ is directed radially outward.
Stars where this term exceeds the gravitational binding margin experience a net
outward force and are continuously expelled. The flat rotation curve is the
**marginally-bound surviving population** — an evolutionary attractor rather than
a static equilibrium. Survivors satisfy $B_c(r) = v_f/r$ automatically, with no
fine-tuning. As the cosmological acceleration scale evolves and the stripping threshold shifts,
progressively more disk stars are stripped over cosmic time — driving morphological
evolution toward ellipticals at low $z$. (The sign of this trend depends on the joint
evolution of $c$ and $H$ in $g_\dagger = c^2/R_0 \propto cH_0$, Core §5; T14 hedges the $B_c$-vs-$c$
scaling explicitly and that check should be done before this link is claimed as firm.)

### Ordered vs. Random Orbits: Disk Stripping

The Lorentz term $\mathbf{v} \times \mathbf{B}_c$ is large when $\mathbf{v}$ is
large and ordered (coherent rotation), and small when $\mathbf{v}$ is random
(pressure support).

- **Disk stars (rotation-dominated, high ordered $v$):** the Lorentz term is large
  → strong ejection force → disk stars are selectively stripped over cosmic time.
- **Bulge/spheroid stars (pressure-dominated, random $v$):** the Lorentz term
  averages to near zero (random directions, low ordered component) → weak ejection
  → spheroid stars are retained.

A galaxy high on the shared $GM_\text{bary}\,a_0$ normalization has both a stronger
$B_c$ field and a more massive central BH. Its strong $B_c$ sheds the disk most
rapidly, ending as a pure spheroid — an **elliptical galaxy** — while also hosting a
massive SMBH. A galaxy low on the normalization has weak $B_c$ and a small BH, and
keeps its disk. The disk/elliptical dichotomy thus correlates with BH mass without
the BH sourcing the stripping field: both are downstream of the same baryonic
normalization.

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
A galaxy high on the $GM_\text{bary}\,a_0$ normalization (strong $B_c$, and a high-mass
BH as a co-tracer) → fast disk stripping → ends as a pure elliptical.
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
- The derived M-σ consequence $M_\text{BH} \propto v_f^4 = GM_\text{bary}\,a_0$
  (T14) then becomes a *statement about the PBH mass distribution*, not an
  independent relation. Equivalently, the $B_c$ amplitude
  $B_c \sim (GM_\text{bary}\,a_0)^{1/4}/r$ sourced by the baryonic distribution
  encodes the same normalization.

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
the shared $GM_\text{bary}\,a_0$ normalization sets the stripping strength (with BH mass
as a co-tracer, not the source), and the top-end M-σ break is the evaporation ceiling.
This is a single mechanism for three real observed facts.

However, the entire chain is:
1. **Qualitative / sign-level only.** No quantitative derivation of the
   evaporation timescale, the disk-vs-spheroid Lorentz contrast, the M-σ slope,
   or the break location.
2. **Dependent on the $v \times B_c$ force** with $B_c \sim M_\text{bary}^{1/4}/r$
   (baryon-sourced, not BH-sourced) — conditionally derived from the transition-radius
   geometric mean (T14); remaining debts are attractor convergence and the PDE derivation
   of the closure. The non-analytic wall is reclassified as an artifact of demanding a
   direct-source coupling.
3. **Dependent on PBH formation** (T16, T13) for the SMBH seed thread.

It is recorded because the four observations are checked and the mechanism is
coherent, not because a working force law has been derived.

---

## Falsifiable Handles (To Compute Later)

- **M-σ scatter tracks rotational support:** The prefactor $8/(\pi\beta^2)$ in
  $M_\text{bulge}\sim(8/\pi\beta^2)\sigma^4/(Ga_0)$ varies with $\beta=v_\text{rot}/\sigma$
  (typical range $\sim0.3$–$1.0$, prefactor $\sim28$–$2.5$). Slow-rotating
  (dispersion-dominated) bulges sit *above* the mean M-σ line; fast-rotating ones sit
  *below*. This explains why M-σ scatter (~0.3 dex) exceeds BTFR scatter (~0.1 dex) — the
  disk has no $\beta$ freedom ($f=1$ always), the bulge does. *Testable against
  resolved-kinematics samples (e.g. ATLAS3D-type $v/\sigma$ vs M-σ residuals; predicted
  sign: lower $\beta$ → higher $M/\sigma^4$). Not yet checked against data.*

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
- **Epoch co-evolution test (Path 4, parameter-free):** Since $a_0 \sim c(t)H(t)$,
  both the BTFR zero-point and the M-σ normalization must co-evolve in lockstep,
  computable with no free parameters from the model's own $c(u)$ and $H^\text{hor}(u)$
  scalings (Core §5). A locked co-evolution tracking $c(t)H(t)$ is a signature no
  ΛCDM+DM model predicts; absence falsifies the shared-$a_0$ premise. Testable now
  with JWST/ALMA high-$z$ dynamical masses paired with high-$z$ AGN masses.
- **Exponent from survival statistics (Path 5):** The M-σ exponent 4 may emerge as a
  *survival-statistics* exponent — derivable from the $\sigma$-distribution of the
  marginally-bound population selected by the Lorentz filter ($GM/r = v^2 + vB_c r$),
  without assuming the exponent in a force law. Connects Link 4 (evaporation ceiling)
  to a computable $\sigma$-saturation mass scale.

---

## Open Questions

- The $B_c \propto M_\text{bary}^{1/4}/r$ amplitude (baryon-sourced) is conditionally
  derived from the transition-radius geometric mean (T14) — the quarter power is analytic
  once the attractor is assumed. The remaining open question is **attractor convergence**:
  does the Lorentz filter genuinely concentrate survivors at $r_t$ at all radii, and does
  a dynamical-systems analysis confirm this? The criticality-as-license mechanism (T14)
  may facilitate the convergence, but is no longer required to produce the exponent.
- Does the PBH seed channel (T16) naturally produce the M-σ normalization, given
  the primordial PBH mass distribution?
- Is the $c$-evolution-driven disk stripping distinguishable from tidal stripping
  by its kinematic signature (ejected stars have specific angular-momentum
  distribution predicted by the Lorentz-selection picture)?
- The M-σ relation holds over $\sim 5$ orders of magnitude in $M_\text{BH}$.
  Does the evaporation-ceiling picture predict the correct functional form and
  scatter over this range?
