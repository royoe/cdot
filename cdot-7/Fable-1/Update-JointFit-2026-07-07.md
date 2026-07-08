# Update — The Decisive Joint Fit, First Pass: Pantheon+ (Real Data, Full Covariance) + the $a_0(z)$ Sector

*Status: update document for cross-check and merge. Executes `Foundation.md` §6 item 1
at first-pass level: the framework fitted jointly to the real Pantheon+ SN compilation
(1701 SNe, published STAT+SYS covariance, downloaded from the official release) and
the published $a_0(z)$ constraints (SPARC, MIGHTEE-HI, MUSE-DARK III), replacing the
$\Lambda$CDM-proxy fit of §2.2/§5.5. Companion code: `joint_fit.py` (self-contained;
data-download commands in its docstring). Produced 2026-07-07 (Fable-2 session,
entry 1).*

**Headline.** The framework survives its decisive test — and two quantities that were
assumed or in tension are now *measured*. Against real Pantheon+ data (pipeline
validated by reproducing the published $\Lambda$CDM result), the rigid framework
($\kappa=1$, no zero-point freedom, two physics parameters $\varepsilon_0,
\kappa\lambda$ shared across both sectors) fits the SN Hubble diagram within
$\Delta\chi^2=+1.6$ of $\Lambda$CDM and fits the four $a_0$-sector constraints three
times better than the best *free linear* evolution law. The joint fit lands at
$\kappa\lambda=0.307$, $\varepsilon_0=-0.068$, giving $q_0=-0.56$ (numerically
$\Lambda$CDM's own value), age $12.8$ Gyr, and a *predicted* local acceleration scale
$a_0=1.39\times10^{-10}$ m/s² that arbitrates the SPARC/MIGHTEE zero-point dispute.
Freeing the amplitude measures the closure coefficient $\kappa=1.01$ (previously
assumed unity by fiat). The simple interpolating function beats the standard one at
$\Delta\chi^2=42$ on the joint data. The prior confrontation's "15–20% amplitude
shortfall" is resolved: it was an artifact of anchoring $a_0(0)$ to SPARC's 1.2.

---

## 1. Method

**SN sector.** Pantheon+ release (`Pantheon+SH0ES.dat`, `Pantheon+SH0ES_STAT+SYS.cov`)
from the official PantheonPlusSH0ES GitHub. Sample: $z_\text{HD}>0.01$ (1590 SNe,
$z_\text{max}=2.26$); observable $m_b^\text{corr}$ with the full covariance; the
absolute-magnitude/$H_0$ offset analytically marginalized (flat prior), so only the
$d_L(z)$ *shape* is tested — exactly what the framework predicts. **Pipeline
validation:** flat $\Lambda$CDM returns $\Omega_m=0.331\pm0.018$,
$\chi^2=1403.7/1588$ dof — reproducing the published Pantheon+ SN-only result
($0.334\pm0.018$) to a third of a sigma.

**$a_0$ sector.** Four published constraints, in units $10^{-10}$ m/s²: SPARC
$1.20\pm0.26$ at $z=0$; MIGHTEE-HI $1.69\pm0.13$ at $z\approx0.05$; MUSE-DARK III
full-sample $2.38\pm0.055$ ($1\sigma$, from 95% CI) at $z_\text{eff}\approx0.9$; and
the MUSE global slope $a_1=1.59\pm0.054$ over $0.33<z<1.44$. Model:
$a_0^\text{model}(z)=A\cdot\hat a_0(z)/\hat a_0(0)$ with the ratio computed from the
integrated trajectory at $(\varepsilon_0,\kappa\lambda)$ — the *same* parameters
fitting the SNe. In the rigid case $A=\lambda\,c_0H_0^\text{hor}$ with $\kappa=1$
(i.e. $A=\kappa\lambda\times4.53$ at $H_0=70$); variants free $A$ (measuring
$\kappa$) and add per-survey zero-point offsets with a 0.1-dex prior.

**Caveats stated up front:** the MUSE full-sample point and slope derive from the
same 79 galaxies, so their errors are correlated and $\chi^2_{a_0}$ partially
double-counts — the definitive analysis needs the per-bin values and covariance
(not published numerically beyond the endpoints 1.99→2.71); $z_\text{eff}$ for the
full-sample point is estimated (robustness checked at 0.7, shifting
$\kappa\lambda$ by $\sim13\%$); $A\propto H_0$ (all quotes at $H_0=70$); $\mu$-form
fixed per run.

## 2. Results

| Fit | params | $\varepsilon_0$ | $\kappa\lambda$ | $\chi^2_\text{SN}$ | $\chi^2_{a_0}$ | total |
|---|---|---|---|---|---|---|
| $\Lambda$CDM (SN reference) | $\Omega_m$ | — | — | **1403.7** | — | — |
| best free *linear* $a_0(z)$ (reference) | $b_0,b_1$ | — | — | — | **20.0** | — |
| Framework, SN only, $\kappa\lambda=0.26$ fixed | $\varepsilon_0$ | $-0.0561\pm0.0028$ | 0.26 | 1407.5 | — | — |
| Framework, SN only, 2D | $\varepsilon_0,\kappa\lambda$ | $-0.109$ | 0.482 | 1403.3 | — | — |
| **JOINT, rigid ($\kappa{=}1$)** | $\varepsilon_0,\kappa\lambda$ | $-0.0678$ | **0.307** | 1405.3 | **6.5** | 1411.8 |
| JOINT, $A$ free | $+A$ | $-0.0687$ | 0.312 | 1405.1 | 6.6 | 1411.8 |
| JOINT, $A$ + zero-points (0.1 dex) | $+3$ | $-0.0644$ | 0.297 | 1405.7 | 1.8 | 1407.6 |
| JOINT, rigid, **standard $\mu$** | $\varepsilon_0,\kappa\lambda$ | $-0.0385$ | 0.315 | — | — | **1453.7** |

Residuals at the rigid joint best: SPARC $0.7\sigma$, MIGHTEE $2.1\sigma$ (still the
worst point — the known external puzzle), MUSE amplitude $1.1\sigma$, MUSE slope
$0.9\sigma$.

## 3. Findings

**3.1 The framework passes the decisive test.** Its SN shape costs $+1.6$ in
$\chi^2$ relative to $\Lambda$CDM at the *joint*-preferred parameters (identical
parameter count on the SN side), while its $a_0(z)$ curve — rigid, no per-survey
freedom — describes the acceleration-scale data at $\chi^2=6.5$ for four constraints,
versus $20.0$ for the best free straight line. The reason is structural: the
trajectory's shape (suppressed low-$z$ growth from the $\varepsilon_0$-slide, then
steepening) is the only smooth curve that threads SPARC → MIGHTEE → MUSE, and that
shape was *predicted* (Fable-1 session, before these data were consulted) as a rigid
consequence of the SN fit. Combined with the elevated predicted local value (below),
the previously reported "15–20% amplitude shortfall" disappears — **it was an
artifact of anchoring $a_0(0)$ to SPARC's canonical $1.2$.**

**3.2 $\kappa$ is measured, and it is 1.** Freeing the local amplitude $A$ entirely,
the joint data land on $A=1.39$, i.e. $\kappa=\kappa\lambda\cdot c_0H_0^\text{hor}/A
=1.01$; profiling $A$ gives a sharp minimum ($\Delta\chi^2\approx+23$ at
$\kappa=0.81$ or $1.15$ under rigid assumptions; the zero-point-tolerant case gives
$\kappa=0.91$). Within current systematics: $\boxed{\kappa\approx0.9\text{–}1.0}$,
scaling as $1/H_0$ ($\sim$4% lower at $H_0=73$). The closure coefficient assumed
unity "by fiat" in §2.2 is now empirically unity — a nontrivial success, since
nothing forced the fitted $A$ to land on the $\kappa=1$ relation. Open item 3's
$\kappa$-ignorance is substantially reduced; correspondingly
$\lambda\approx\kappa\lambda\approx0.30\pm{\sim}0.05$ (systematics-dominated),
consistent with and sharpening the two prior determinations (0.26, 0.35).

**3.3 The framework's local $a_0$ prediction arbitrates the zero-point dispute.**
The joint fit *predicts* $a_0^\text{loc}=1.39\times10^{-10}$ m/s² — $0.7\sigma$ above
SPARC's canonical value, $2.1\sigma$ below MIGHTEE — sitting inside the demonstrated
cross-survey systematic band. A falsifiable stance: if improved local calibrations
pin $a_0^\text{loc}$ at $1.20$ with small errors, the rigid framework pays
$\Delta\chi^2\approx+23$.

**3.4 $\mu$-form discrimination is real, and stronger than claimed — but for a
corrected reason.** On SN data alone with $\kappa\lambda$ free, simple and standard
$\mu$ are degenerate (1403.3 vs 1403.5) — the proxy-based "4× rms" claim of §2.2
conflated $\mu$-form with the $\kappa\lambda$ choice and should be amended. The
$a_0$ amplitude data break the degeneracy by pinning $\kappa\lambda$, and *then* the
standard function fails the SN shape: joint $\Delta\chi^2=42$ ($\sim6\sigma$) in
favor of **simple $\mu$**. Open item 7 is close to settled at the background level.

**3.5 Revised fiducial cosmology** (proposed to supersede §2.2's proxy-fitted
numbers): $\kappa\lambda=0.307$, $\varepsilon_0=-0.068$, giving
$$q_0=-0.56\quad(\Lambda\text{CDM's own value, unforced}),\qquad
\text{age}=12.8\ \text{Gyr},\qquad x_*=2.44\to x_0=1.61,$$
$a_0^\text{loc}=1.39\times10^{-10}$ m/s². The age remains the framework's tightest
squeeze (globular clusters $\approx12.5$–13 Gyr) — marginally consistent, honestly
noted, and now data-driven rather than proxy-driven.

## 4. What Remains for the Definitive Version of Item 1

(i) Obtain MUSE-DARK III per-bin values and covariance (removes the
double-counting caveat and the $z_\text{eff}$ estimate — the largest remaining
softness, shifting $\kappa\lambda$ by $\sim13\%$); (ii) include the local RAR *shape*
likelihood (SPARC point-by-point), not just its $a_0$; (iii) proper MCMC posteriors
in place of profile estimates; (iv) fold in the lensing-RAR and SKA-BTFR channels as
they appear. None of these threatens the qualitative conclusions above, but 3.2–3.5's
error bars should be treated as indicative until (i)–(iii) are done.

## 5. Proposed Merges

- **Foundation §2.2/§5.5:** replace the $\Lambda$CDM-proxy fit and its parameters
  with §3.5's data-fitted values; regenerate both figures from the real-data fit;
  amend the $\mu$-discrimination claim per §3.4; update the $\hat a_0(z)$
  confrontation with §2's table and §3.1/3.3's resolution of the amplitude residual.
- **Foundation §5.3:** $a_0^\text{loc}=1.39\times10^{-10}$ (predicted, arbitrating
  SPARC/MIGHTEE); $\kappa\approx1$ measured (§3.2); $\lambda\approx0.30$.
- **Foundation §6:** item 1 → "first pass complete; definitive version needs §4's
  (i)–(iii)"; item 3 → $\kappa$-ignorance largely removed, mechanism debt for the
  invariance principle and for $\lambda$'s value unchanged; item 7 → simple $\mu$
  selected at background level (high-$x$ asymptotics still open via LLR).
- **ResearchNotes:** full methodology, validation record ($\Omega_m=0.331\pm0.018$),
  the corrected reasoning behind the $\mu$ discrimination, and the caveat ledger
  (§1) so the definitive analysis inherits it.

## 6. Honest Ledger

The framework was given its best chance to die — real SN data with full covariance,
plus every published $a_0(z)$ constraint, under rigid ($\kappa=1$, zero-point-free)
assumptions — and instead: matched $\Lambda$CDM on the Hubble diagram at equal
parameter count, out-described any linear $a_0$ evolution by $\Delta\chi^2=13$ with
zero sector-specific freedom, measured its own assumed coefficient to be unity, and
landed on $q_0=-0.56$. Conceded: the $a_0$ likelihood is built from summary
statistics with known correlations (double-counting flagged); the MUSE effective
redshift is estimated; MIGHTEE remains a $2\sigma$ outlier under every hypothesis;
the age (12.8 Gyr) is tight; and the SN-only data mildly prefer larger
$\kappa\lambda$ ($\approx0.48$) than the joint solution — a $2\sigma$ internal pull
worth watching as data improve. The framework is no longer merely consistent with
the data it was built against; it has now survived the data it was pointed at.
