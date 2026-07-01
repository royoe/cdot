# Session Log — T4 Deceleration Parameter / SN Observable

**Topic:** T4 — Supernovae and Cosmic Acceleration (deceleration parameter $q_0$)
**Date:** 2026-06-28
**Outcome:** Negative-but-sharpening result. The conjectured route to apparent
acceleration was found and explicitly closed. T4's standard-candle assertion is
upgraded to a derived result. $q_0 = +1/6$ stands and is strengthened.

*(Timestamps are session-relative; absolute wall-clock not recorded.)*

---

## Prompt 1 — User

> The files stored in this project are a snapshot from a github repository. There is a
> Core Principles document that should always be kept in context, as well as a series of
> numbered Topic documents... [project framing] ... I want to discuss the issue of the
> deceleration parameter, included in T4. Is there any hints in the project context from
> where we could conceivably expect a sign change that would produce the observed
> accelerating expansion?

### Result 1
Read Core Principles, T4, T11, T9. Established:
- $q_0 = 1/(nP)$ is structurally positive; the two parameter routes ($n<0$, $P<0$) are
  correctly closed by T4.
- $q_0$ describes the curvature of the redshift–coordinate-distance relation fed through
  the *kinematic* $D_L=(1+z)D_\text{p}$. The real SN observable is flux vs. redshift.
- Candidate loophole identified: T4's "standard-candle" paragraph **asserts** that the
  map-frame $L\propto c^4$ brightening (T9) is a coordinate artifact. This is the one
  place a non-structural sign could hide. Flagged tension with T9, which treats
  $L\propto c^4$ as physically real (faint-young-Sun) and invokes a gravity-vs-EM
  non-cancellation principle to argue orbital expansion is observable.
- Caution noted: any candidate dimming must come from the emission side only, not
  in-flight (premise 4), to avoid double-counting the redshift.
- Proposed the explicit flux-integral calculation as the test.

## Prompt 2 — User

> Very good! This is my understanding of T9 too. Please do the integrals explicitly and
> carefully and see where we land before we continue.

### Result 2
Performed symbolic flux integral (sympy). Derived proper-time stretch
$d\tau_\text{obs}/d\tau_\text{emit}=(1+z)$ via photon counting + clock-rate scaling.
Assembled bolometric flux:
$$F_\text{bol} = \frac{L_p}{4\pi D_\text{p}^2 (1+z)^2}, \qquad D_L=(1+z)D_\text{p}.$$
Found this is *identical* to T4's kinematic $D_L$. Traced the $L\propto c^4$ term:
$L_\text{map}/L_p=(c/c_0)^4$ is a units rescaling fully absorbed into the $(1+z)$
factors; no leftover dimming. **Conjecture fails cleanly.** Identified the disanalogy
with T9: faint-young-Sun has two competing couplings (gravity vs EM) → non-cancellation;
the SN chain is photon-sector-only → clean collapse. Flagged the calorimetric energy
factor (step B) as the one place an alternative bookkeeping could be argued.

## Prompt 3 — User

> Let's just double-check that we didn't mess up the observable. What is measured is the
> peak magnitude of the observed SN, isn't it? It does not really involve any time
> dilation. And the observed survey magnitudes are corrected for redshift since
> observations have to correct the SN flux to the observed bandpass, which is redshifted
> with respect to the emitted bandpass. Let's go through the details here so that we're
> sure we haven't overlooked anything.

### Result 3
Recomputed the **actual** observable: peak specific flux $F_\nu$ + K-correction, not
bolometric fluence.
- Surfaced and resolved a genuine bookkeeping ambiguity (two conventions gave
  $D_L=D_\text{p}$ vs $D_L=(1+z)D_\text{p}$).
- **Resolution (premise 4):** the conserved absolute photon energy is $h\nu_o$ (measured
  now), not $h\nu_e$; $\nu_e$ is the proper emission-clock label. A self-correction was
  recorded: an intermediate step wrongly claimed premise 4 forbids the energy factor and
  pushed $D_L\to(1+z)^{1/2}D_\text{p}$; this was mistaken. Correct reading restores
  $D_L=(1+z)D_\text{p}$.
- **Spectral:** $F_\nu(\nu_o)=L_{\nu_e}^\text{proper}/[4\pi D_\text{p}^2 (1+z)]$ — single
  power of $(1+z)$, matching FRW structure.
- **Peak magnitude:** user correct that time dilation does not lower the peak; at peak the
  rate-dilation $1/(1+z)$ and bandwidth $(1+z)$ cancel, leaving one $(1+z)$ from
  per-photon energy. Peak $F_\nu$ has the same single power; magnitude structure unchanged.
- **K-correction:** depends only on the $\nu_e=(1+z)\nu_o$ mapping and SED shape, both
  identical to FRW → same function of $z$, no model-specific factor. FRW-calibrated
  pipelines (SALT2, Pantheon+) apply unchanged in $(1+z)$ structure.
- **Conclusion:** observable maps to $\mu=5\log_{10}(D_L/10\,\text{pc})$ with
  $D_L=(1+z)D_\text{p}$. No overlooked factor, no hidden sign. $q_0=+1/6$ stands and is
  strengthened.

## Prompt 4 — User

> [Selected: packaging as] update/addendum doc only ... Please continue to produce the docs.

### Result 4
Produced `T4_UPDATE_standard_candle_observable.md` (addendum for merge) and this session
log.

---

## Deliverables
- `T4_UPDATE_standard_candle_observable.md` — proposed addendum to T4.
- `SESSION_LOG_T4_SN_observable.md` — this log.

## Net change to the repository (proposed)
- T4 "Standard-Candle Assumption" section: assertion → derivation (peak $F_\nu$ + K-corr).
- T4: add subsection on why T9's gravity-vs-EM non-cancellation does not transfer.
- Core Principles status table: note SN observable now derived end-to-end; Pantheon+
  model-native fit remains the outstanding empirical task.

## Outstanding / unchanged
- Highest-priority empirical test still open: direct Pantheon+ fit in model-native
  framework with proper covariance.
- Model still cannot mimic acceleration; viability hinges on whether acceleration is
  robust independent of an FRW prior.
