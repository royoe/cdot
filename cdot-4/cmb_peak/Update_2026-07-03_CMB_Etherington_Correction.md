# Update — Etherington Reciprocity Does Not Apply Here; Correcting the First-Peak Calculation (2026-07-03, continuation)

*Session type: corrective, then constructive. Follows directly from
`Update_2026-07-03_CMB_First_Peak_Angular_Scale.md`, which found the predicted
first-peak position short of $\ell_1\approx220$ by 9$\times$–765$\times$ using
$\theta_s = r_s/D_A(z_\text{rec})$ with $D_A\equiv D_L/(1+z)^2$ (T4's Etherington-based
definition). Prompted by the author questioning why Etherington reciprocity would apply
in a non-expanding cosmology at all. **Answer, refined through the discussion: the
theorem is not restricted to expanding universes — it is proven for any spacetime with
photons on true null geodesics and conserved photon number, independent of expansion
history — but it does require the observed redshift to be a genuine null-geodesic
effect. This model's redshift is explicitly not that (premise 4: photon frequency is
literally conserved in flight; the $(1+z)$ is a comparison against a drifting atomic
reference standard, not a propagation effect). That is the correct, sharper reason
Etherington's relation has no license here — not the absence of expansion.** Rebuilding
the angular-diameter distance from the model's own first-principles static geometry
($D_A \equiv D_p$, no $(1+z)$ suppression) and redoing the first-peak calculation
reverses the previous verdict for the model's preferred branch: volume law now lands
within 1.4$\times$ of $\ell_1\approx220$, down from 765$\times$ short.*

---

## 1. Why Etherington Reciprocity Does Not License $D_A = D_L/(1+z)^2$ Here

**The theorem is more general than "expanding universe," and that generality is not
the issue.** Etherington's reciprocity (distance-duality) relation is proven for
essentially any spacetime describable by a Lorentzian metric with photons propagating
on null geodesics and conserved photon number — it does not assume homogeneity,
isotropy, or any particular expansion history. Its derivation uses the reciprocity of
the geodesic-deviation (Sachs focusing) equation between a light bundle's cross-section
at emission and at observation. This generality is precisely why cosmologists use
$D_L=(1+z)^2D_A$ as a *model-independent* consistency test (distance-duality tests
against cluster gas fractions, strong-lensing statistics, inhomogeneous "Swiss cheese"
cosmologies) — a violation signals new physics (photon non-conservation, non-metric
gravity), specifically *because* the relation is expected to hold regardless of
expansion history. So "this model doesn't expand" is not, by itself, a valid reason to
doubt it — a genuine static GR spacetime (e.g. the Einstein static universe) would
still satisfy it.

**What the theorem actually requires is narrower: the redshift must be a null-geodesic
effect.** The proof ties the $(1+z)$ appearing in the frequency ratio to the *same*
$(1+z)$ that governs the beam's solid-angle transformation via the geodesic-deviation
equation — i.e. whatever produces the redshift (cosmological expansion, a gravitational
potential, peculiar motion) must be encoded in the metric's null-cone structure, because
that structure is what the focusing theorem acts on.

**This model's redshift is not that.** Premise 4 states photon frequency is *literally
conserved in flight* — there is no frequency shift along the null path at all, and
therefore nothing for a focusing theorem to act on in the way Etherington's proof
requires. The observed $(1+z)$ arises entirely from comparing the (unchanged) photon
frequency against a local atomic reference standard whose own natural frequency has
drifted, because $c(t)$ was different when that reference transition was set (Core §2,
T2). This is a bookkeeping/reference-frame redshift, not a propagation redshift. The
theorem's hypotheses are simply not met here — independent of whether the space
expands.

**Consequence:** T4's single citation of Etherington reciprocity (Open Questions,
"the model sits on the Etherington line... providing a consistency check") is an
unsupported import. It is not derived anywhere in the repository, is not used in any
actual T4 calculation (the SN flux/distance-modulus derivation, §"The Standard-Candle
Assumption," never invokes it), and — per the argument above — there is no reason to
expect it to hold in a model whose redshift mechanism is structurally different from
the null-geodesic effect the theorem is built around. This should be flagged as
**likely inapplicable**, not merely "unconfirmed."

## 2. Rebuilding $D_A$ from the Model's Own Static Geometry

Angular-diameter distance is defined, by its own physical meaning, as
$D_A \equiv (\text{proper transverse size})/(\text{subtended angle})$ — a purely
geometric/kinematic quantity, independent of flux or luminosity. In a flat, static,
Euclidean 3-space (premise 1: $\dot a=0$, no spatial curvature, no recessional motion),
with light travelling on straight lines, two photons emitted from the opposite edges of
an object of proper transverse size $s$ converge on the observer's position after
travelling the same physical path length — the model's own $D_p(z)$ (Core §4,
"the proper path length the photon traversed," $D=\int c\,dt = R_\text{now}-R_\text{emit}$).
Elementary Euclidean geometry then gives
$$\theta = \frac{s}{D_p},\qquad\text{i.e.}\qquad \boxed{D_A \equiv D_p}\ \text{(no $(1+z)$ suppression).}$$

Two supporting points:
- **Lengths don't drift with epoch in this model.** Unlike energies ($\propto c^2$
  throughout), physical/geometric lengths are absolute (premise 1; orbit radii are
  literally $r=\text{const}$, T9). So the sound horizon's physical size in meters, and
  the observer–source separation $D_p$, are both fixed, unambiguous lengths that don't
  need any epoch-dependent rescaling before comparing them.
- **The two edge-photons share the same $c(t)$ history to leading order.** They are
  emitted at essentially the same time from essentially the same place (separation
  $s\ll D_p$) and traverse essentially the same path through the (globally, not
  locally, varying) $c(t)$ background, so any distortion from $c(t)$'s time-variation
  along the way cancels between them at leading order — it does not introduce an
  independent suppression factor the way cosmological expansion does in FRW.

This does **not** touch the SN luminosity-distance result $D_L=(1+z)D_p$: that
derivation (T4, "The Standard-Candle Assumption") is a flux/energy-bookkeeping argument
(clock-rate time dilation + per-photon energy), entirely independent of the angular-size
geometry above, and untouched by this correction. It is only the *bridge* between $D_L$
and $D_A$ — which was never independently derived, only asserted via Etherington — that
is being replaced.

## 3. Recomputed First-Peak Position

Repeating the T16 calculation with $\theta_s = r_s/D_p(z_\text{rec})$ in place of
$r_s/D_A(z_\text{rec})$, at the observationally-labeled $z_\text{rec}\approx1090$ and
the model's self-similarity-implied $R\approx680$ (unchanged from the previous update):

| Branch | $D_p(z_\text{rec})$ | $r_s$ | $\theta_s$ | $\ell_1$ | vs. observed 220 |
|---|---:|---:|---:|---:|---:|
| Volume law $n=3$ (preferred) | 17,688 Mpc | 177 Mpc | 0.01002 rad | **313.6** | 1.4$\times$ too high |
| Surface law $n=2$ | 21,226 Mpc | 99 Mpc | 0.00466 rad | 674.1 | 3.1$\times$ too high |
| S$'$ $n=2/3$ | 25,562 Mpc | 3.0 Mpc | 0.000117 rad | 26,815 | 122$\times$ too high |

**This reverses the previous verdict for the preferred branch.** Where the
Etherington-based calculation was short by $765\times$, the first-principles static-space
calculation overshoots by only $1.4\times$ — arguably within the noise of everything
still approximate here (see caveats). Note also that with $D_p$, $\theta_s(z)$ decreases
*monotonically* with $z_\text{rec}$ (verified numerically, $z=1$ to $10^9$) rather than
having the interior floor the $D_A$ version had — so there is no structural ceiling on
$\ell_1$ any more, and the specific number at $z_\text{rec}=1090$ is now the operative,
meaningful check rather than an optimization exercise.

Surface law and S$'$ now *overshoot* rather than undershoot, and by a much larger
margin for S$'$ — mild, secondary evidence favoring the volume law (already the
model's preferred branch on other grounds: mildest $q_0$ tension, T4; retains the PBH
genesis argument, T13/T16) over the alternatives, purely from this new consistency
check.

## 4. What This Does and Does Not Fix

**Fixed (tentatively):** the first peak's *angular position*, for the preferred branch,
is no longer a many-orders-of-magnitude failure — it's a same-order-of-magnitude near
miss.

**Not fixed — still open:**
- The **baryon-loading problem** (§2 of the previous update) is untouched: self-similarity
  still pins $R\approx680$ at all epochs, not the $R\approx0.6$ needed for realistic
  peak *heights*/damping. This calculation only addresses peak *position*.
- $z_\text{rec}\approx1090$ is still not derived within the model (T16 item A) — it is
  used here as an observational anchor, not a first-principles prediction. Because
  $\theta_s(z)$ is now monotonic rather than floored, the specific 1.4$\times$ result is
  sensitive to this input in a way the previous (floored) calculation's qualitative
  verdict was not — a genuine derivation of $z_\text{rec}$ remains a priority.
- This is a **leading-order geometric estimate**: $\ell_1\approx\pi/\theta_s$ is the
  standard approximation, and the real first-peak location includes an $O(1)$
  phase shift from the baryon-drag physics not computed here (nor in $\Lambda$CDM
  is $\ell_1$ exactly $\pi/\theta_s$ — the true relation includes a driving-phase
  correction). A 1.4$\times$ discrepancy is well within the size such corrections can
  plausibly produce, but that has not been checked, only asserted as plausible.
- The $D_A\equiv D_p$ replacement is a **new proposal**, argued from first principles
  here but not yet cross-checked against every other place the model implicitly leans
  on distance-duality-type reasoning. It was checked that T22 (gravitational lensing)
  does not currently use $D_A=D_L/(1+z)^2$ anywhere, so no immediate conflict there.

## 5. Consolidated Edits (for merge)

| # | File | Edit | Type |
|---|------|------|------|
| 1 | T16 §(C) | Replace the 2026-07-03 "decisive quantitative failure" framing: the failure was an artifact of importing an inapplicable Etherington relation; using the model's own $D_A\equiv D_p$, the preferred (volume-law) branch is a 1.4$\times$ near-miss, not a 765$\times$ failure. Keep the baryon-loading ($R\approx680$) concern, which is unaffected. | **Reversal of the reversal** |
| 2 | T16 "Current Status" table | Update "(C) angular position" row from "decisive quantitative failure" to "near miss (1.4$\times$, preferred branch) under a first-principles static-space $D_A\equiv D_p$; decisive failure only under the (now-doubted) imported Etherington relation" | Status change |
| 3 | T16 Open Questions | Replace the "is there an appropriate static-space angle mapping" question (now answered: yes, $D_A\equiv D_p$) with: "derive $z_\text{rec}$ within the model (item A) to remove the last external input in this calculation"; "check the $O(1)$ phase-shift correction to $\ell_1\approx\pi/\theta_s$"; "the baryon-loading/peak-height problem remains, independent of this fix" | Resolution + new items |
| 4 | T4 Open Questions, Etherington bullet | Flag as likely inapplicable: the model's redshift is not a null-geodesic effect (photon frequency literally conserved in flight, premise 4), so Etherington's reciprocity theorem's hypotheses are not met, independent of the model's lack of expansion. Recommend removing $D_A=D_L/(1+z)^2$ as an assumed identity anywhere it might be relied on. | Correction |
| 5 | Core Principles §7 status table, CMB row | Update to reflect the near-miss result for the preferred branch and the still-open baryon-loading and $z_\text{rec}$ items | Status change |

**Bottom line.** The author's question — why would a reciprocity theorem tied to
geodesic light propagation apply in a model where photon frequency is stipulated not to
change in flight at all — was the right question, and it overturns the previous
session's numeric verdict for the model's preferred branch. The lesson generalizes:
anywhere this model imports a standard-cosmology relation between distances,
redshifts, or angles, it is worth checking whether that relation's proof actually
survives the model's specific (non-geodesic) redshift mechanism, rather than assuming
it transfers by analogy. The first peak's *position*, for the volume-law branch, now
looks like a near-miss rather than a falsification; the *height* problem (baryon
loading) and the *epoch* problem ($z_\text{rec}$ undetermined) remain the open,
load-bearing items.
