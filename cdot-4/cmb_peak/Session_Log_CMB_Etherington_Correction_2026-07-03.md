# Session Log — Etherington Reciprocity Correction to the CMB First-Peak Calculation

**Date:** 2026-07-03 (continuation of the same day's CMB first-peak session)
**Scope:** Re-examine the angular-diameter-distance assumption behind the just-completed
first-peak calculation, prompted by the author questioning whether Etherington
reciprocity even applies to a non-expanding cosmology.
**Outputs:** Update_2026-07-03_CMB_Etherington_Correction.md; this log; edits to T16,
T4, Core Principles
**Session classification:** Corrective, then constructive — a user challenge to a
borrowed assumption overturns the numeric verdict of the prior session for the model's
preferred branch.

---

## User Prompts

> I don't see this in T22, but check in T4. D_p is presumably 'proper' distance? Is
> that defined anywhere?

Checked: $D_p$ is defined in Core Principles §4 as the proper path length the photon
travelled, $D=\int c\,dt=R_\text{now}-R_\text{emit}$. Confirmed $D_A$ appears in T4
exactly once (Open Questions), as an asserted consequence of Etherington reciprocity,
not derived or used in the actual SN flux calculation.

> I never understood why we needed The Etherington reciprocity relation in a
> non-expanding cosmology. Isn't its usage strictly limited to the case of an
> expanding universe?

This was the pivotal question. My own earlier framing (in the prior session's update)
had argued the $(1+z)^2$ suppression was suspect "because the model doesn't expand" —
checking the actual theorem showed this framing was imprecise. Etherington reciprocity
is proven for *any* spacetime with photons on null geodesics and conserved photon
number, independent of expansion history — it's used routinely as a model-independent
consistency test across arbitrary (including static or inhomogeneous) spacetimes for
exactly that reason. The real, narrower requirement is that the observed redshift be a
*null-geodesic effect* (whatever produces it — expansion, gravity, motion — must be
encoded in the metric's null-cone structure, since that's what the geodesic-deviation/
focusing-theorem proof acts on). This model's redshift is explicitly not that: premise 4
states photon frequency is *literally conserved in flight*; the $(1+z)$ comes from
comparing that unchanged frequency to a drifting local atomic reference standard — a
bookkeeping effect, not a propagation effect. That is the correct, sharper reason
Etherington's relation has no license here, and it applies regardless of whether the
space expands.

> Yes, please. [fold the correction in]

---

## Session Activity

- Corrected the theoretical framing: replaced "no expansion → no Etherington
  suppression" with "redshift isn't a null-geodesic effect here → Etherington's proof
  hypotheses aren't met, independent of expansion."
- Re-derived $D_A$ from first principles for this model's static Euclidean space:
  $D_A\equiv(\text{proper transverse size})/(\text{angle})=D_p$ directly, with no
  $(1+z)$ suppression, since (a) lengths don't drift with epoch in this model (unlike
  energies) and (b) two closely-separated edge-photons share the same $c(t)$ history
  to leading order, so no independent distortion is introduced.
- Recomputed $\theta_s=r_s/D_p(z_\text{rec})$ (in place of $r_s/D_A(z_\text{rec})$) for
  all three premise-2 branches at $z_\text{rec}=1090$, holding the previous session's
  $R\approx680$ fixed. Result: volume law (preferred branch) $\ell_1=313.6$, only
  $1.4\times$ above 220 — a near miss, reversed from $765\times$ short. Surface law
  and S$'$ now overshoot (3.1$\times$, 122$\times$).
- Verified numerically that $\theta_s(z)$ using $D_p$ is monotonically decreasing over
  $z=1$ to $10^9$ (no interior floor), unlike the $D_A$-based version — so the
  $z_\text{rec}=1090$ result is now the operative, meaningful number rather than one
  point on a U-shaped curve.
- Checked for consistency risk: confirmed T22 (gravitational lensing) does not
  currently use $D_A=D_L/(1+z)^2$ anywhere, so no immediate conflict from retracting
  that identity there. Flagged T4's own Etherington citation (Open Questions) as
  likely wrong, not merely unconfirmed.
- Wrote up the correction, the re-derivation, the recomputed table, and an honest
  caveat list (peak-height/baryon-loading problem unaffected; $z_\text{rec}$ still an
  external input; leading-order $\ell_1\approx\pi/\theta_s$ approximation not corrected
  for the $O(1)$ phase shift).

## Results Summary

1. **The user's challenge was correct and sharper than my own initial framing.**
   Etherington reciprocity's generality (it doesn't require expansion) is real, but
   its actual requirement — a null-geodesic redshift mechanism — is exactly what this
   model's premise-4 redshift mechanism is not.
2. **Numeric reversal for the preferred branch**: first-peak position goes from
   765$\times$ too small to 1.4$\times$ too large — a near miss rather than a decisive
   failure, using only the model's own already-defined $D_p$ and no new free
   parameters.
3. **Branch-dependent outcome**: only the volume law lands close; surface law and S$'$
   now overshoot, mild secondary evidence favoring the model's already-preferred
   branch.
4. **Two problems remain, unaffected by this fix**: the baryon-loading/peak-height
   issue ($R\approx680$ throughout, from the earlier session), and the undetermined
   $z_\text{rec}$ (T16 item A) — this calculation uses $1090$ as an observational
   anchor, not a derived quantity.
5. **General lesson flagged for the program**: any place the model imports a
   standard-cosmology distance/redshift/angle relation by analogy should be checked
   against whether that relation's proof survives the model's specific
   (non-geodesic) redshift mechanism, rather than assumed to transfer.

## Merge Recommendation

Merge as a correction layered on top of (not a full revert of) the previous update:
keep the baryon-loading finding, keep the Etherington-inapplicability argument (now
correctly framed), replace the position-failure numbers with the position-near-miss
numbers. Update T4's Etherington bullet to flag it as likely wrong. Recommended next
sessions, in priority order: (a) derive $z_\text{rec}$ within the model (T16 item A) to
remove the last external input from this calculation and turn the 1.4$\times$ near
miss into an actual prediction; (b) check the $O(1)$ $\ell_1\approx\pi/\theta_s$
phase-shift correction; (c) return to the still-unresolved baryon-loading/peak-height
problem, now the clear single remaining blocker on the first peak.
