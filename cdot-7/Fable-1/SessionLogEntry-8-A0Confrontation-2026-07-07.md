# Session Log Entry — 2026-07-07 (for merge as Entry 8 of `cdot-7/SessionLog-2026-07-07.md`)

## Entry 8 — Evolving $a_0$ confronted with observation: trajectory prediction vs MUSE-DARK III

**Prompt (verbatim):**
> The c-dependency on a_0 is surprising. Can it be confronted with observations?

**Summary:** Confronted the framework's evolving MOND scale with data. Two steps:

1. **Prediction corrected to the fitted trajectory** (computed *before* the literature
   search — same-day but genuinely blind; the fixed-point $(1+z)^{3/2}$ law of Entry 6
   is superseded): $\hat a_0(z)/\hat a_0(0)=[x_0r_0/(x(z)r(z))](1+z)^{3/2}$, since the
   slide that produces the acceleration also boosts today's $\dot c$. Fiducial values:
   1.31 at $z=0.5$, 1.82 at $z=1$, asymptote $0.61(1+z)^{3/2}$. The suppression is
   fixed by the *same* $\varepsilon_0$ fitted to the SN Hubble diagram — a rigid
   SN↔RAR consistency relation — and the curve is nearly parameter-free across the
   $(\mu,\lambda)$ family once $\varepsilon_0$ is SN-fitted ($a_0(z{=}1)$ varies
   $\pm3\%$, slope $\pm10\%$).
2. **The measurement exists** (found via search; postdates training data): MUSE-DARK
   III (Ciocan et al. 2026, A&A 709, L16), 79 SFGs at $0.33<z<1.44$, MUSE HUDF, 3D
   forward modelling with pressure support: $a_0|_{z\sim1}=2.38^{+0.12}_{-0.10}
   \times10^{-10}$ m/s² (95% CI, $\sim19\sigma$ above SPARC's 1.2); binned $a_0$ rises
   monotonically 1.99→2.71; linear evolution $a_1=1.59^{+0.11}_{-0.10}$; robust across
   halo profiles and in a self-consistent MOND refit. Context: Vărăşteanu et al. 2025
   (MIGHTEE-HI) report $a_0=1.69\pm0.13$ already at $z<0.08$.

**Confrontation (three-way):** constant $a_0$ (standard MOND) — excluded by the
detected evolution; naive fixed-point $(1+z)^{3/2}$ — $a_1^\text{eff}=2.46$,
$a_0(1)=3.4$, excluded at high significance; **fitted trajectory** —
$a_0(z{\sim}0.9)\approx2.0$–2.2, $a_1^\text{eff}=1.19$–1.43: sign, existence, and
$\approx85\%$ of the measured amplitude, with no parameter tuned for this observable.
Face-value residual: 15–20% low ($\sim3$–$5\sigma$ on published statistics) — but the
MIGHTEE point is inconsistent with *any* smooth evolution anchored to SPARC (including
MUSE-DARK's own fit), demonstrating cross-survey zero-point systematics of
0.3–0.5$\times10^{-10}$ that cover the residual. Also noted: wide-$z$-bin scatter
inflation (0.11→0.17 dex) is qualitatively predicted by any evolving-$a_0$ model.

**Decisive test defined:** a joint statistical fit — SN compilation + binned
$a_0(z)$ (SPARC/MIGHTEE/MUSE-DARK, with zero-point nuisances) + local RAR — over
$(\varepsilon_0,\kappa\lambda,\mu)$; after the SN fit the framework has essentially
one shape degree of freedom, so this can genuinely fail. Future channels ranked:
lensing RAR by lens redshift ($+0.03$–0.06 dex, systematics-clean), SKA-era BTFR
zero point at $z\sim0.5$–1 ($-0.12$ to $-0.26$ dex in $M_b$ at fixed $v_\text{flat}$;
current TFR samples diluted by quasi-Newtonian radii), early structure formation
(qualitative, awaits perturbation sector).

**Files produced:** `Update-A0Evolution-Confrontation-2026-07-07.md`,
`a0_confrontation.py` (verified; reproduces the prediction table and slope
comparison), this log entry.
