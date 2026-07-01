# UPDATE — Exploration Paths for the M-σ Consistency Condition and the $M^{1/4}$ Relation

*Proposed update spanning T16, T17, T14, T6. Status: research-program scoping, not a
result. To be cross-checked and merged. Author session: 2026-06-30.*

---

## 1. Sharpened Statement of the Problem

T16 and T17 both point at a "consistency condition" without isolating exactly what new
physics it demands. This update fixes the statement so the candidate paths can be judged
against it.

Two independent empirical facts are being fused:

1. **BTFR / deep-MOND scaling (T6, T15).** A flat rotation curve requires an effective
   force $g_\text{eff} = \sqrt{GM_\text{bary}\,a_0}/r$ — carrying $\sqrt{M_\text{bary}}$.
   In the Lorentz framing $\mathbf g = \mathbf g_N + \mathbf v\times\mathbf B_c$ with
   $v\times B_c = v_f B_c$, flatness requires
   $$B_c = \frac{v_f}{r} \propto \frac{(GM_\text{bary}\,a_0)^{1/4}}{r}.$$

2. **M-σ relation (T17).** $M_\text{BH}\propto\sigma^4\propto v_f^4\propto GM_\text{bary}a_0$,
   hence $M_\text{BH}^{1/4}\propto (GM_\text{bary}a_0)^{1/4}$ — *the same quarter power*,
   expressed through the central BH mass.

**The consistency condition is that these are one equation read two ways:**
$$B_c \sim \frac{M_\text{BH}^{1/4}}{r} \sim \frac{(GM_\text{bary}\,a_0)^{1/4}}{r}.$$

**The non-analytic wall (T14).** $M^{1/4}$ is *more* singular than the $\sqrt M$ that
already defeated all five linear gravitomagnetic mechanisms. No analytic source coupling
produces a quarter power. This is the precise debt.

**Reframed target.** The problem is *not* "explain MOND" or "explain M-σ" separately. It
is: **what structure makes the same quarter power appear in both the galaxy-scale force
and the BH–baryon relation, with a universal coefficient $a_0\sim cH_0$?** This framing
is what discriminates the paths below.

---

## 2. Candidate Paths (ordered by new-physics cost)

### Path 1 — The quarter power as a *geometric mean*, not a direct source (cheapest)

Force the algebra before invoking new physics:
$$B_c \sim \frac{(GM_\text{bary}\,a_0)^{1/4}}{r}
= \frac{1}{r}\sqrt{\,\sqrt{GM_\text{bary}}\cdot\sqrt{a_0}\,},
\qquad\Longleftrightarrow\qquad
B_c^2 \;\propto\; g_N \cdot g_\dagger ,$$
i.e. $(rB_c)^2 \propto (GM_\text{bary}/r)\cdot(a_0 r) = GM_\text{bary}\,a_0$.

A quarter power is the geometric mean of two square-root quantities. Both inputs already
exist in the model:
- $g_N\propto M$ (linear) — available from foam-diffusion Newtonian $1/r$ (T14).
- $g_\dagger\sim cH_0$ (mass-independent) — the cosmological background gradient
  $|\nabla\rho_\text{bg}|\sim\rho_\text{bg}H_0/c$ already derived in T14.

**The claim to test:** does a coupled steady state of (foreground mass-sourced connecton
field) and (cosmological background gradient) produce an observable that is the *geometric
mean* of the two — as happens generically at a marginal/critical layer where the two
balance? If so, the quarter power is **analytic and automatic**, and the "wall" is an
artifact of demanding a *direct* $M^{1/4}$ source. This is essentially the
dynamical-selection attractor (T14) re-expressed as an impedance / balance condition, and
it is consonant with the RAR being a *smooth crossover* between exactly these two regimes.

*Highest leverage, lowest cost. Exhaust first.*

### Path 2 — Make criticality-as-license quantitative (T6 Role 2, T14)

Critical surfaces are the one place in physics where fractional-power (non-integer)
exponents are *natural* rather than forbidden. Two computable sub-directions:

- **Critical-exponent route.** Treat the connecton-sea response near the central BH's
  critical surface as an order parameter; ask whether its susceptibility scales as
  $M_\text{BH}^{1/4}$. Non-analytic response near criticality is exactly the regime that
  hosts quarter-power exponents.
- **Holographic / mode-counting route.** Horizon area $\propto M_\text{BH}^2$. A field
  amplitude set by entropy-per-mode counting on the horizon, combined with the connecton
  minimal quantum $\hbar H_0$ (T14), may deliver $M^{1/4}$ as a bookkeeping result. Check
  whether area-density counting reproduces the quarter power.

Role 1 (BH *sources* the amplitude) remains correctly ruled out (T6) — it would make the
amplitude $\propto M_\text{BH}$ and destroy the universality of $a_0$. Only the *license*
(existence-condition) reading survives.

### Path 3 — Dissolve the wall via PBH statistics (T16)

If both the central SMBH and the halo wells are remnants of one primordial PBH population
(T16 triple-duty), then $M_\text{BH}\propto v_f^4$ is a statement about the **initial PBH
mass function**, not about gravity. There is then *no force-law non-analyticity at all*.

**Path:** derive the PBH mass function from the Reading-2 freezeout (T16's load-bearing
gate) and test whether the seed-mass→halo-mass ratio reproduces $M_\text{BH}\propto
GM_\text{halo}a_0$ at the right normalization.

**Discriminant from Paths 1/2:** if PBH statistics carry the relation, galaxies with
anomalous merger histories should scatter *off* M-σ; if a force law carries it, the
relation is tight regardless of merger history. The observed scatter contrast
(M-σ ≈ 0.3 dex vs. BTFR ≈ 0.1 dex) is itself a modelling target and a discriminant.

### Path 4 — Epoch co-evolution: the decisive, parameter-free observational test

Unique to this model: $a_0\sim c(t)H(t)$ must **drift with epoch** (T6 already flags this).
Using the model's own $c(u)$ and $H^\text{hor}(u)$ scalings (Core §5), $a_0$ at a galaxy's
redshift is computable with **no free parameters**. Then:

- the BTFR zero-point and the M-σ normalization must **co-evolve in lockstep**, because
  both are tied to the same $a_0(t)$;
- a locked co-evolution tracking $c(t)H(t)$ is a signature no $\Lambda$CDM+DM model
  predicts; its absence falsifies the shared-$a_0$ premise.

Testable now with JWST/ALMA high-$z$ dynamical masses and high-$z$ AGN masses. **Develop
in parallel regardless of microphysics** — it can confirm or kill the program independent
of whether a force law is ever derived.

### Path 5 — Derive the exponent 4 from survival statistics, not the force law (T17 cross-check)

T17 leaves the exponent in $M_\text{BH}\propto\sigma^4$ unexplained. Orthogonal route: in
dynamical selection, $\sigma$ is the dispersion of the *surviving marginally-bound
population*, fixed by the same attractor as $B_c$ via $GM/r = v^2 + vB_c r$. Derive the
survivor $\sigma$-distribution directly from the Lorentz filter and check whether the
fourth power emerges as a **survival-statistics exponent** rather than a force-law
exponent. Connects T17 Link 4 (evaporation ceiling) to a computable σ-saturation mass.

---

## 3. Recommended Priority

1. **Path 1** — cheapest; may show the wall is an artifact of demanding a direct source
   rather than a geometric mean of two already-derived linear quantities.
2. **Path 4** — most decisive empirically; no-free-parameter test; pursue in parallel.
3. **Paths 2 & 3** — the two genuine homes for quarter-powers (critical exponents; PBH
   statistics). They make *opposite* predictions on scatter and merger-history dependence,
   so pursuing both sharpens a real discriminant.
4. **Path 5** — self-consistency check on the T17 morphology story.

---

## 4. Suggested Document Edits (on merge)

- **T14** — add Path 1 as an explicit reformulation of the non-analytic wall:
  "$M^{1/4}$ as geometric mean $B_c^2\propto g_N g_\dagger$ from coupled foreground/
  background steady state." Reclassify the wall as *conditional on direct-source
  assumption*.
- **T16 / T17** — record the discriminant (scatter and merger-history dependence)
  distinguishing the force-law route (Paths 1/2) from the PBH-statistics route (Path 3).
- **T6** — add the epoch co-evolution test (Path 4) to Open Questions as a parameter-free
  falsifiable handle, noting the locked BTFR-zeropoint / M-σ-normalization prediction.
- **T17** — add Path 5 (exponent-from-survival-statistics) to "Falsifiable Handles."
- **Core Principles §7** — no status change yet; these are paths, not results. Consider a
  note that the M-σ / $M^{1/4}$ debt now has a scoped research program with one cheap
  analytic route (Path 1) and one decisive observational route (Path 4).
