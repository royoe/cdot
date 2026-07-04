# UPDATE — BAO Alcock–Paczynski Shape Test (parameter-free)

*Status: proposed update, for cross-check and merge. Session 2026-07-04.*
*Targets: Core Principles §4, §4a; T3 (Hubble Constant / BAO); T4 (SN); T12 (premise-2 fork).*

---

## Summary

A **parameter-free** Alcock–Paczynski (AP) shape test against DESI DR2 BAO
confirms — and sharpens — the working diagnosis that the horizon-count
distance construction fails the BAO data. The failure is **not** a
normalisation issue, and **not** a clock-choice artifact. It is a structural
consequence of a single lock intrinsic to the horizon-count premise:

$$D_H(z) = \frac{dD_p}{dz},$$

which forces the AP ratio to a rigid one-parameter shape that cannot fit the
DESI data for any counting exponent.

---

## Method

The AP observable $F_\text{AP}(z)\equiv D_M(z)/D_H(z)$ is independent of the
sound horizon $r_d$, of $H_0$, and (in this model) of $R_\text{now}$ — every
overall normalisation cancels. It is therefore a **pure shape** test with no
free scale.

**Data.** DESI DR2 BAO, the six effective-redshift bins reporting both
$D_M/r_d$ and $D_H/r_d$ (DESI DR2 Table IV; values as tabulated in
arXiv:2511.12017 Table I):

| $z$ | $D_M/r_d$ | $D_H/r_d$ | $F_\text{AP}=D_M/D_H$ |
|---:|---:|---:|---:|
| 0.510 | $13.588\pm0.167$ | $21.863\pm0.425$ | $0.6215\pm0.0143$ |
| 0.706 | $17.351\pm0.177$ | $19.455\pm0.330$ | $0.8919\pm0.0177$ |
| 0.934 | $21.576\pm0.152$ | $17.641\pm0.193$ | $1.2231\pm0.0159$ |
| 1.321 | $27.601\pm0.318$ | $14.176\pm0.221$ | $1.9470\pm0.0377$ |
| 1.484 | $30.512\pm0.760$ | $12.817\pm0.516$ | $2.3806\pm0.1127$ |
| 2.330 | $38.988\pm0.531$ | $ 8.632\pm0.101$ | $4.5167\pm0.0811$ |

(AP errors propagated ignoring the $D_M$–$D_H$ correlation — conservative for a
shape test; folding in the reported correlation would only tighten the pulls.)

**Pipeline validation.** On these same six bins the AP ratio yields:
- flat ΛCDM ($\Omega_m=0.31$): $\chi^2\approx 9$, best normalisation $A\approx1.00$ — pass;
- $R_h=ct$: $\chi^2\approx 53$ — correctly fails.

This confirms the test machinery before applying it to the model.

---

## The parameter-free model prediction

In the static ($a=1$) horizon-count cosmology the transverse comoving distance
**is** the proper path length, $D_M=D_p$, and the radial BAO mode measures
$D_H=dD_\text{comoving}/dz=dD_p/dz$. With
$$D_p(z)=R_\text{now}\left[1-(1+z)^{-b}\right],\qquad b=\frac{1}{nP},$$
both distances share the prefactor $R_\text{now}$, so it cancels in the ratio,
leaving **no free constant** ($A=1$ is forced, not fitted):

$$\boxed{\,F_\text{AP}(z)=\frac{D_p}{dD_p/dz}
=\frac{1+z}{b}\left[(1+z)^{b}-1\right].\,}$$

This was verified numerically to be independent of $R_\text{now}$.

---

## Result

Parameter-free ($A=1$ forced), six data points:

| Counting law | $b=1/(nP)$ | $\chi^2$ (6 pts, 0 free) |
|---|---:|---:|
| Volume ($n=3,P=2$) | $1/6$ | **93.9** |
| Surface ($n=2,P=2$) | $1/4$ | 175.9 |
| Best single power law (unphysical) | $b=0.038$, $nP\approx27$ | 49.6 |
| — reference: flat ΛCDM | — | 9.0 |

Per-point pulls for the volume law:

| $z$ | obs | model (vol) | pull ($\sigma$) |
|---:|---:|---:|---:|
| 0.510 | 0.6215 | 0.6442 | $+1.6$ |
| 0.706 | 0.8919 | 0.9531 | $+3.5$ |
| 0.934 | 1.2231 | 1.3484 | $+7.9$ |
| 1.321 | 1.9470 | 2.0980 | $+4.0$ |
| 1.484 | 2.3806 | 2.4405 | $+0.5$ |
| 2.330 | 4.5167 | 4.4357 | $-1.0$ |

The residual is **S-shaped**: the model over-predicts $F_\text{AP}$ across
$z\approx0.5$–$1.3$ (worst, $+7.9\sigma$, at $z\approx0.93$) and swings toward
under-prediction by $z=2.33$. This is a genuine shape mismatch, not a constant
offset, and it cannot be removed by any single exponent — the free-exponent
optimum ($nP\approx27$) is both far from any motivated value (6 or 4) and still
a decisive fail ($\chi^2=50$).

---

## Interpretation — the fault is the $D_H=dD_p/dz$ lock

The sharpened conclusion, replacing the looser "any exponential law fits
poorly":

1. **Not a normalisation problem.** The AP ratio removes $r_d$, $H_0$,
   $R_\text{now}$. The model fails on shape alone.
2. **Not a clock-choice artifact.** T3's open question — which clock the BAO
   ruler lives in (atomic $H_\tau\propto(1+z)^{2/3}$ vs horizon
   $H_\text{hor}\propto(1+z)^{-1/3}$) — does not arise in the honest
   self-consistent construction: $D_H$ is *derived* as $dD_p/dz$, not chosen.
   (Two-clock variants were also tested and fare worse, $\chi^2\gtrsim300$.)
3. **The real culprit.** Because $D_M$ and $D_H$ both descend from the single
   $c(t)$ that also fixes redshift, the model has only one free function. The
   AP ratio collapses to the one-parameter form above and is too rigid to
   track the data at any exponent. The lock $D_H=dD_p/dz$ is the failure.

This is the structural rigidity the horizon-count premise imposes: it fuses the
redshift clock and the distance ruler into one object.

---

## Consequence for the Machian mass-count route

The test defines the target a surviving alternative must hit. To break the
$D_H=dD_p/dz$ lock, a Machian mass-count model ($c\propto M_u$) must make the
distance ruler depend on the enclosed mass $M_u(z)$ **independently** of the
horizon-growth integral — i.e. $M_u\not\propto R^3$. That requires an
epoch-dependent counted density $n(z)$, and to be a real test (not a tuned
fit) $n(z)$ must be fixed by independent physics already in the model:
- the radiation-vs-baryon counting fork (T12): does the relativistic sea count?
- PBH formation / freeze-out at the $r_s/R\sim1$ crossover (T13, T16),
  changing the counted population.

A mass-count variant earns its keep only if such a physically-fixed $n(z)$
bends $F_\text{AP}(z)$ onto the DESI data **while** preserving: the Pantheon+
SN residual (T4), the epoch-invariance of $R=3\rho_b/4\rho_\gamma$ that carries
the CMB first-peak self-similarity (T16 §C), and the ~21 Gyr proper age (T1).

---

## Proposed edits to existing documents

- **Core Principles §4/§4a and Status table:** the entries
  "Distance $D_{z=1}=0.1091\,R_\text{now}$" and the $D_p(z)$ working formula
  should carry a flag: *the derived $D_H=dD_p/dz$ makes the AP ratio
  parameter-free and it fails DESI DR2 at $\chi^2\approx94$/6 (volume law);
  see UPDATE_BAO.* Downgrade "Horizon law ... Core, stable" pending resolution.
- **T3:** the "$H(z)$ comparison with ΛCDM" section and its Open Questions
  should record that the BAO comparison has now been attempted via the AP
  ratio; the clock ambiguity is resolved *against* the two-clock reading in
  favour of the self-consistent $D_H=dD_p/dz$, which fails. Add the result
  table above.
- **T4:** cross-reference — the SN tension ($q_0>0$) and the BAO shape failure
  are now the two independent distance-sector problems; note they share the
  common origin (single-$c(t)$ rigidity).
- **T12:** elevate the premise-2 fork from "open" toward "load-bearing" — the
  mass-count variant is now the leading route to break the distance lock, with
  a concrete target ($M_u\not\propto R^3$ via physically-fixed $n(z)$).

---

## Caveats

- Six bins, AP errors propagated without the published $D_M$–$D_H$ correlation
  (conservative). A full fit should use the DESI covariance; it will not soften
  a $+7.9\sigma$ single-point pull into agreement.
- The ΛCDM validation ($\chi^2\approx9$) uses fixed $\Omega_m=0.31$, no fit; it
  is a sanity check on the pipeline, not a competitive comparison.
- The conclusion is about the *horizon-count distance construction*. It does
  not by itself refute the redshift law or the relational principle; it refutes
  the identification of the distance ruler with the horizon-growth integral.
