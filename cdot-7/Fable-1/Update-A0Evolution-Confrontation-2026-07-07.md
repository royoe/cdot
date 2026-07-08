# Update — Confronting the Evolving $a_0$ with Observation: the Trajectory Prediction vs the Measured Redshift Evolution of the RAR

*Status: update document for cross-check and merge. Responds to the author's request to
confront the framework's $c$-dependent $a_0$ (alignment update §2.1; closure-rebuild
update) with observations. Contains: the trajectory-corrected prediction (which
supersedes the fixed-point $(1+z)^{3/2}$ law quoted in the alignment update), a
quantitative comparison against a May 2026 measurement of exactly this quantity, and
the identification of the framework's decisive joint test. Companion code:
`a0_confrontation.py`. Produced 2026-07-07 (cdot-7, session entry 8).*

**Headline.** The prediction must be evaluated on the *fitted trajectory*, not the
fixed point: the same slide ($\varepsilon_0=-0.063$) that produces the apparent
acceleration boosts today's $\dot c$, suppressing the past evolution of
$\hat a_0(z)$ from $(1+z)^{3/2}$ to $\approx0.61\,(1+z)^{3/2}$ asymptotically — only
$1.82\times$ at $z=1$ instead of $2.83\times$. A measurement of precisely this
quantity now exists: MUSE-DARK III (Ciocan et al. 2026, A&A 709, L16) finds the RAR
acceleration scale rising with redshift, $a_0|_{z\sim1}=2.38^{+0.12}_{-0.10}
\times10^{-10}$ m/s² and $a_0(z)=a_0(0)+a_1z$ with $a_1=1.59^{+0.11}_{-0.10}$ (95% CI).
The framework's trajectory predicts $a_0(z{=}1)\approx2.2\times10^{-10}$ and
$a_1^\text{eff}\approx1.3$ — about 85% of the measured evolution, with **no parameter
tuned for this observable** — while both rival hypotheses fail badly: constant $a_0$
(standard MOND) is excluded by the data, and the naive fixed-point law
($a_1^\text{eff}=2.46$, $a_0(1)=3.4$) is excluded at high significance. Formal
face-value residuals are at the 3–5σ level, but demonstrably within current
cross-survey zero-point systematics (§3.3).

---

## 1. The Prediction, Stated Precisely

On the fitted trajectory of the closure-rebuild update, $a_0(t)=\lambda\dot c(t)$ with
$\dot c=c^2/(\kappa\lambda xR_h)$, so in local units (acceleration unit
$\propto c^{7/2}$):
$$\frac{\hat a_0(z)}{\hat a_0(0)}
=\frac{x_0\,r_0}{x(z)\,r(z)}\,(1+z)^{3/2},$$
computed directly from the integrated trajectory. Fiducial values (simple $\mu$,
$\lambda=0.26$, $\varepsilon_0=-0.0627$):

| $z$ | 0.05 | 0.33 | 0.45 | 0.70 | 0.85 | 1.00 | 1.20 | 1.44 |
|---|---|---|---|---|---|---|---|---|
| $\hat a_0(z)/\hat a_0(0)$ | 1.02 | 1.18 | 1.27 | 1.49 | 1.65 | 1.82 | 2.07 | 2.38 |
| fixed-point $(1+z)^{3/2}$ | 1.08 | 1.53 | 1.75 | 2.22 | 2.51 | 2.83 | 3.27 | 3.81 |

Asymptotically $\hat a_0(z)\to0.61\,(1+z)^{3/2}$. Three structural points:

1. **The suppression is not a new parameter.** It is fixed by the *same*
   $\varepsilon_0$ fitted to the SN Hubble diagram — the framework predicts a rigid
   consistency relation between the expansion history and the RAR evolution.
2. **The prediction is nearly parameter-free across the family.** Recomputing with
   $(\mu,\lambda)\in\{$simple 0.20/0.26/0.35, standard 0.35$\}$ (each with its own
   SN-fitted $\varepsilon_0$) changes $a_0(z{=}1)$ by only $\pm3\%$ (2.13–2.25, in
   units of $10^{-10}$ m/s² with $a_0(0)=1.2$) and the effective slope by
   $\pm10\%$ (1.19–1.43). The SN fit locks the curve.
3. **Chronology, for the record:** the trajectory numbers above were computed in this
   session *before* the literature search below; the fixed-point law they correct was
   Entry 6's stated prediction. Same-day, but genuinely blind.

## 2. The Measurement

**MUSE-DARK III** (Ciocan et al. 2026, A&A 709, L16; received 2026-01-30, published
2026-05-19): 79 star-forming galaxies, $0.33<z<1.44$, MUSE Hubble UDF, 3D
forward-modelled disk–halo decompositions with pressure-support corrections, RAR
fitted with the McGaugh interpolating form. Results:
- Full sample: $a_0|_{z\sim1}=2.38^{+0.12}_{-0.10}\times10^{-10}$ m/s² (95% CI),
  reported as $\sim19\sigma$ above the SPARC $z=0$ value
  ($1.2\times10^{-10}$).
- Quantile $z$-bins: $a_0$ rises monotonically from $\approx1.99$ (lowest bin) to
  $\approx2.71\times10^{-10}$ (highest).
- Global parametrization $a_0(z)=a_0(0)+a_1z$: $a_1=1.59^{+0.11}_{-0.10}
  \times10^{-10}$ m/s² (95% CI) — statistically significant evolution.
- Robustness: consistent $a_0|_{z\sim1}$ across DM halo profiles *and* from a
  self-consistent MOND-framework refit.
- Context: **Vărăşteanu et al. (2025)**, MIGHTEE-HI, find
  $a_0|_{z<0.08}=1.69\pm0.13\times10^{-10}$ — already elevated at nearly zero
  redshift (relevant to §3.3).

## 3. The Confrontation

### 3.1 Three-way discrimination

| Hypothesis | $a_0(z{\sim}0.9)$ [$10^{-10}$] | $a_1^\text{eff}$ (0.33–1.44) | Verdict vs data |
|---|---|---|---|
| Constant $a_0$ (standard MOND) | 1.20 | 0.00 | excluded (evolution detected) |
| Fixed-point $(1+z)^{3/2}$ (alignment update) | 3.2 | 2.46 | excluded ($\gg5\sigma$ high) |
| **Fitted trajectory (this framework)** | **2.0–2.2** | **1.19–1.43** | ≈85% of measured; see §3.2–3.3 |
| Measured (MUSE-DARK III) | $2.38^{+0.12}_{-0.10}$ | $1.59^{+0.11}_{-0.10}$ | — |

The framework's curve lands *between* the two excluded alternatives and close to the
measurement, with the suppression factor supplied by the SN fit. Notably, the data
simultaneously reject the hypothesis class ("$a_0$ never evolves") that standard MOND
occupies and the naive $a_0\propto cH(z)$ scaling — while an evolving-$a_0$ of
roughly this framework's *shape and amplitude* is what the measurement shows.

### 3.2 Face-value residuals

Taking the published statistics at face value (95% CI $\to1\sigma\approx0.055$): the
trajectory is low by $\sim0.2$–$0.4\times10^{-10}$ in $a_0|_{z\sim1}$ ($\sim3$–$7\sigma$
depending on the sample's effective redshift) and by $\sim0.2$–$0.3$ in $a_1$
($\sim3$–$5\sigma$). A real residual at the 15–20% level, honestly reported.

### 3.3 The systematic floor

The face-value statistics overstate the decisiveness, for a reason visible inside the
data themselves: the MIGHTEE-HI point ($1.69\pm0.13$ at $z<0.08$) is inconsistent with
*any* smooth cosmological evolution anchored to SPARC's $1.2$ — including MUSE-DARK's
own linear fit extrapolated to $z\sim0.05$ — demonstrating cross-survey/methodology
zero-point offsets of order $0.3$–$0.5\times10^{-10}$ between HI, IFU, and SPARC
analyses. The framework's residual sits inside that demonstrated systematic envelope.
Additional interpretation caveats: the $a_0$ extraction is partly framework-dependent
(disk–halo decomposition in $\Lambda$CDM; mitigated by their consistent MOND-framework
refit); the sample is massive SFGs with pressure-support corrections; and stellar
$M/L$ evolution enters $a_\text{bar}$ directly. Also consistent qualitatively: their
intrinsic scatter grows in wide $z$-bins (0.11→0.17 dex), which *any* evolving-$a_0$
model predicts as bin-mixing (the framework contributes $\sim0.03$ dex per
$\Delta z\sim0.25$ in the deep regime), on top of their data-quality explanation.

**Verdict:** the framework's rigid SN↔RAR consistency relation currently *holds at
the level the data can test it* — agreement in kind and in approximate magnitude,
a 15–20% amplitude residual within cross-survey systematics, and decisive superiority
over both constant-$a_0$ and the unsuppressed scaling.

## 4. The Decisive Test, Now Defined

Because the $\hat a_0(z)$ curve is locked by the SN fit, the right analysis is a
**joint statistical fit**: SN compilation + binned $a_0(z)$ (MUSE-DARK III,
MIGHTEE-HI, SPARC) + local RAR shape, with survey zero-point nuisance parameters,
fitting $(\varepsilon_0,\kappa\lambda,\mu)$ globally. The framework has essentially
one shape degree of freedom left after the SN fit, so this test can genuinely fail.
Sharper future channels, in order of cleanliness:
- **Low-acceleration lensing RAR by lens redshift** (KiDS/Euclid-type stacking):
  deep-MOND regime, where $\Delta\log g_\text{obs}=\tfrac12\Delta\log\hat a_0$
  ($+0.03$ dex at $z\sim0.3$, $+0.06$ at $z\sim0.5$) — small but statistically cheap,
  and free of rotation-curve pressure-support systematics.
- **BTFR zero-point evolution** with genuinely flat outer velocities (SKA-era HI at
  $z\sim0.5$–1): predicted $\Delta\log M_b$ at fixed $v_\text{flat}$ of $-0.12$ dex
  ($z{=}0.5$), $-0.26$ dex ($z{=}1$). Caveat carried from the analysis: current
  high-$z$ TFR samples measure $v(\sim2R_e)$ in quasi-Newtonian regions, which
  dilutes the predicted shift — the clean test needs the deep-MOND asymptote.
- **Early structure formation** (qualitative, needs the missing perturbation sector):
  $\hat a_0$ larger by $\times3$–7 at $z=2$–4 strengthens effective gravity at low
  accelerations, in the helpful direction for JWST's early massive galaxies — noted
  as motivation for the perturbation-sector open item, not claimed as a result.

## 5. Proposed Merges

- **Foundation §5.5/§4:** replace the alignment update's $(1+z)^{3/2}$ prediction
  with the trajectory-corrected curve (table in §1) and its parameter-robustness;
  record the SN↔RAR rigidity as the framework's primary falsifiable consistency
  relation.
- **Foundation §6:** upgrade the "compare with high-$z$ RAR literature" item to:
  *joint statistical fit of SN + $a_0(z)$ + RAR with zero-point nuisances* (§4);
  add the lensing-RAR and SKA-BTFR channels; strike the item's "murky/hedged" status
  — data now exist and are quantitatively engaged.
- **ResearchNotes:** record the confrontation table, the chronology note (§1.3), the
  face-value residuals, and the MIGHTEE zero-point puzzle as an external open issue
  the framework inherits but did not create.

## 6. Honest Ledger

For: the framework's most exotic-seeming feature — a cosmologically evolving MOND
scale — is not only *not* excluded, it matches the sign, approximate magnitude, and
existence of a newly measured effect that falsifies the constant-$a_0$ alternative;
the suppression relative to naive scaling was forced by the SN fit before the
measurement was consulted; and the prediction is essentially rigid across the
remaining parameter freedom. Against: a real 15–20% amplitude shortfall
($\sim3$–$5\sigma$ on face-value statistics) that only cross-survey systematics
currently excuse; the measurement's $a_0$ extraction is partly framework-laden; one
external dataset (MIGHTEE-HI) fits no smooth-evolution model including this one; and
the strongest version of the test (the joint fit of §4) has not yet been run — it is
now the framework's most important piece of outstanding work, and its most credible
opportunity to be killed.
