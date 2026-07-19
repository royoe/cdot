# Mistele et al. (2024) — "Radial acceleration relation of galaxies with joint kinematic and weak-lensing data"

**Citation:** D. Mistele, F. Lelli, S. McGaugh, JCAP 04, 020 (2024); arXiv:2310.15248.
**Source stored:** `arXiv.2310.15248/lensing-RAR.tex` (+ `.bbl`, `jcappub.sty`, `plots/`).

## What this is, for cdot-8

WP5's second literature anchor for the lensing-RAR confrontation. Joins
kinematic (SPARC-type) and weak-lensing RAR data with a new, exact
deprojection formula converting excess surface density (ESD) profiles to
radial accelerations.

## Aspects load-bearing for cdot-8

- **Lens data**: KiDS-1000 SOM-gold source catalog + KiDS-bright lenses,
  $0.1<z<0.5$ — again **pooled, not binned by redshift** (confirmed
  independently of the Brouwer paper's own pooling — the two papers share
  the same underlying limitation for WP5's purposes).
- **$a_0=1.24\times10^{-10}$ m/s²**, applied as a **universal constant**
  across the whole sample — no redshift dependence reported or tested.
  This is the number WP5 §8 compared (at face value, then explicitly
  declined to over-interpret) against cdot-8's predicted 12–16% growth
  by the sample's own mean lens redshift.
- **$\approx0.1$ dex ($\approx26\%$) systematic band**, confirmed
  verbatim: "we translate this 0.2 dex uncertainty [in stellar mass] into
  a $\sim0.1$ dex uncertainty on $g_\text{obs}$" — the key uncertainty
  floor used in WP5's final adjudication that the pooled literature
  cannot decide the $a_0$-tracks-$H(z)$ question either way.
- New exact deprojection method explicitly stated to give **smaller**
  systematic uncertainties than older SIS/PPL approaches (confirmed
  "0.05 dex is indeed a reasonable estimate" for the older methods'
  error) — relevant context for why this paper's own error budget is
  taken as closer to a floor than a loose bound.
- Result: "the RAR inferred from weak-lensing data smoothly continues
  that inferred from kinematic data by about 2.5 dex in acceleration" —
  the core positive result of the paper, not itself disputed by cdot-8's
  work (WP5's interest is specifically in redshift-dependence, which this
  paper doesn't test).

## Status in cdot-8's record

Central to WP5 §8–9, alongside Brouwer et al. 2021. The 0.1 dex figure is
directly load-bearing for the "pooled data cannot decide" adjudication in
`Advisory-WP5-ConfrontationDesign-2026-07-17.md`, confirmed independently
before being accepted into the record.
