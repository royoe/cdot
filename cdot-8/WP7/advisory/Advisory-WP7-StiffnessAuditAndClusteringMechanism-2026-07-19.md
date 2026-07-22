# Advisory — WP7 §26 Assessed: the Double Failure Is Real Signal and the Joint Staged Round Is Confirmed — With Its Stage 0 Delivered Today: the System Is *Not* Intrinsically Stiff, the Suspects Are Formulation and Units, and the Audit's Byproduct Is the Round's Real Discovery — a Hubble-Tracking Tachyonic Effective Mass That *Is* the Scalar's Clustering Mechanism (for `cdot-8/WP7/`)

*2026-07-19. Advisory in response to §26 of
`Update-WP7-PerturbationStructure-2026-07-18.md`. Audit in
`wp7_stiffness_audit.py`. Gate 1(b) carried. Verdict up front: **the
checkpoint is accepted, the reasoning in §26's closure was genuinely
careful (the $F_Q$-vs-$\rho_s$ dictionary distinction was exactly
right), and two independent failures at the same wall is indeed signal
— the joint, WP3-rhythm staged round is confirmed, with advisor
cross-checking at each stage as requested. To make that round start
from knowledge rather than a third blind attempt, its Stage 0 is
delivered here: a stiffness audit along the trajectory. Result: the
effective-mass sector is* not *stiff — $|\mu_{\rm eff}|/H<1$ at every
epoch — so the solver deaths are not the physics; the prime suspects
are formulation (the effective-fluid $\delta,\theta$ kept as state
variables, whose definitions carry $1/c_{\rm ad}^2\sim20$–$230$
throughout the matter era) and units (the imported $\mathcal E_\alpha$
equation's normalization, with $|F_Q|$ spanning $4473\to1.85$ in
$H_0^2$ units). And the audit's byproduct outranks its purpose: through
the matter era the scalar's effective mass-squared is negative and
Hubble-tracking, $\mu^2\approx-1.27f_s/(2-K_B)\,H^2\approx-0.5H^2$
(closed form, interior spline agreeing to 1.6%), flipping to the
doubly-verified stable sign near today. A tachyonic mass at
$|\mu|<H$ is not a pathology — it is a Jeans-class growing mode: the
clustering mechanism §23's requirement was waiting for, delivered by
the quadrature unbidden. $F_{QQ}$'s fourth load-bearing appearance, and
the biggest.***

---

## 1. §26 accepted — and the request granted

The second attempt's closure logic was right where it mattered: direct
evolution equations instead of inverting definitions; $\chi=\bar Q(\theta
+\alpha)$ algebraic; the momentum constraint for $\Phi$ with real
$k$-dependence; and above all the identification of the $\mathcal
E_\alpha$ equation's coefficient with the *bare field equation's*
$F_Q$ — genuinely different from $\rho_s$'s M5-modified Friedmann
combination — which is the §23 dictionary lesson applied correctly
under pressure. That a formulation this careful still collapsed is why
the double failure is signal: **the joint staged round is confirmed**,
advisor cross-checking at each stage, §24's Stage 1 as the matter-era
regression target, the two exact anchors as brackets.

## 2. Stage 0, delivered: the audit and its verdicts

- **K1 — effective-mass stiffness: exonerated.**
  $\mu_{\rm eff}^2=-Q^2F_{QQ}/(2(2-K_B))$ evaluated along the
  trajectory gives $|\mu_{\rm eff}|/H\lesssim0.7$ at every epoch from
  the crossover to today. There is no fast oscillator; the physical
  system integrates at ordinary tolerances *if formulated in regular
  variables*. (The ULA-style averaged closure I would have prescribed
  for a stiff regime is not needed — noted so the staged round doesn't
  reach for it.)
- **K2 — the singular-factor map: prime suspect.** The effective-fluid
  $\delta,\theta$ *definitions* carry $1/\rho_s$ and $c_{\rm ad}^2$;
  their equations carry $\Pi/(1+w)$; and $|1/c_{\rm ad}^2|$ runs
  $20$–$230$ through the matter era — not just at the crossing.
  **Standing rule for the staged round: state variables are
  $(\chi$ or $\gamma,\ \alpha,\ \mathcal E_\alpha,\ \delta_b,\ \theta_b,
  \ \Phi)$ only — nothing whose definition contains $\rho_s$,
  $c_{\rm ad}^2$, or $1/(1+w)$; the effective-fluid objects are output
  diagnostics computed afterward.** Hypothesis to check against the
  actual §26 script: it kept $\delta,\theta$ as state.
- **K3 — the units contract: co-suspect.** $|F_Q|$ spans $4473$ ($z_*$)
  to $1.85$ (today) in $H_0^2$ units, and the founding paper's
  $dK/dQ$ lives in *its* normalization. A mixed import mis-scales the
  $\chi$–$\mathcal E_\alpha$ loop by orders and dies exactly like
  stiffness. **The staged round opens with one written dictionary line
  per imported equation ($K$-convention $\leftrightarrow$
  $F$-convention, $H_0^2$ vs $H^2(z)$) before any code** — the third
  dictionary-class trap, pre-empted this time.

## 3. The discovery: the clustering mechanism was in $F_{QQ}$ all along

The audit's $\mu^2$ zeros traced to a real sign structure, verified two
ways (matter-era closed form $Q^2F_{QQ}=\tfrac{36}{25}F$ against the
interior spline: 889 vs 875 at $z=10$): **through the matter era,
$\mu^2/H^2=-\tfrac{36}{25}\cdot\tfrac{30}{34}\,f_s/(2-K_B)\approx-0.5$,
constant — a scale-free, Hubble-tracking tachyonic effective mass —
flipping to the doubly-verified stable sign ($F_{QQ}(0)=-0.696$,
$1/\mu\sim$ Gpc) near today.** Read physically: a tachyonic mass slower
than Hubble is a Jeans-class growing mode — the destabilization of the
smooth solution that *makes a component cluster*. The quadrature
$F(Q)$, constructed with no input beyond the invoice, hands the scalar
exactly the ingredient §23's requirement demanded — clustering through
the matter era — and withdraws it exactly when the component turns
dark-energy-like. Requirement and mechanism close in one object. This
is $F_{QQ}$'s fourth load-bearing appearance (condensate mass;
stability sign; constraint feedback; now structure formation), which is
what a zero-dial sector looks like when it is either deeply right or
about to be very testable.

**Caveats, carried as Stage-1 tasks**: (i) the sign-flip location needs
a robust $F_{QQ}(z)$ (proper spline of the quadrature; my quick
endpoint value at $z=0$ disagreed with the verified record, which is
how the closed-form route got forced — the interior is solid, the
boundary is not); (ii) sub-horizon stability needs the full dispersion
$\omega^2=c_s^2k^2+\mu^2(z)$ with the $\mathcal Y$/gradient sector's
$c_s^2$ (SZ-healthy at today's anchor; epoch-dependence to verify);
(iii) SZ's Minkowski conditions are consistent by scope — they anchor
at today's point, where the sign is stable.

## 4. The staged round's plan, as now informed

Stage 0 ✓ (this audit). Stage 1: robust $F_{QQ}(z)$ + the dispersion
relation — the growth *rate* prediction $\delta_s\propto$
Hubble-tracking growth is now a checkable target, not just a sanity
hope. Stage 2: the units contract, one line per imported equation.
Stage 3: the pure-field-variable system per K2's rule, implicit solver
as insurance, §24 Stage 1 as regression, both anchors as brackets.
Stage 4: M5 term + exits + the ISW $\Delta C_\ell$. Each stage
cross-checked before the next, per the worker's own request.

## 5. Housekeeping

The `ConsolidationLog` Item-16 citation confirms the consolidation
record is live and maintained — the long-standing file-sighting item
softens to routine. Fold-in queue gains: the K2 state-variable rule,
the K3 contract, the $\mu^2(z)$ finding with its caveats. Two external
clocks unchanged (KATRIN; $Q_2$ awaiting the author's sequencing call).
Nothing in `cdot-7/` was touched.

## Companion

- `wp7_stiffness_audit.py` — the three-killer audit and the
  closed-form effective-mass addendum.
- This advisory: proposed location
  `cdot-8/WP7/Advisory-WP7-StiffnessAuditAndClusteringMechanism-2026-07-19.md`.
