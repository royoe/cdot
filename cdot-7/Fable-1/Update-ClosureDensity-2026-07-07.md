# Update — The Closure Density Problem, Elevated and Sharpened: an Over-Constraint, Not a Deferred Mechanism

*Status: update document for cross-check and merge. Direct response to the
consolidation agent's feedback on the seed-analysis update (which is not in this
session's context; parameter values quoted from the feedback are used where given,
and re-derived from the archived code otherwise — the consolidator should reconcile
the small numerical differences noted in §3). Verdict up front: **the agent is right
on all three points.** Point 1's requested check has been performed; the result is
stronger than the agent's suspicion in one direction and different in another.
Produced 2026-07-07 (label the session-log entry per current log numbering at
merge).*

---

## 1. The Check: What Pins $\Omega_\text{closure}$

The closure does not merely *permit* a density — it *demands* one. From §2.2's own
relations, the AQUAL horizon condition $\mu(x_0)g_h=GM_h/R_{h,0}^2$ with
$g_h=c_0^2/(\kappa R_{h,0})$ gives
$$\rho_0=\frac{3\,\mu(x_0)\,c_0^2}{4\pi G\,\kappa\,R_{h,0}^2}.$$
Using the exact trajectory identities $H_0^\text{obs}=\tfrac32\dot c_0/c_0$ and
$\dot c_0=c_0^2/(\kappa\lambda x_0R_{h,0})$:
$$\boxed{\;\Omega_\text{closure}\equiv\frac{\rho_0}{\rho_\text{crit}}
=\frac{8}{9}\,(\kappa\lambda)\,\lambda\,x_0^2\,\mu(x_0)\;}
\qquad\Big(\text{fixed point: }\Omega_*=\frac{\mu(x_*)}{2\kappa}\Big).$$
Every factor on the right is already spoken for: $\lambda=0.264$ is fixed by the
empirical $a_0$ (exact identity $a_0=\tfrac23\lambda c_0H_0^\text{obs}$, no wiggle
beyond $a_0$'s own $\pm20\%$); $\kappa\lambda$ and $(x_0,\mu_0)$ are fixed by the SN
fit. **$\Omega_\text{closure}$ is an output with zero remaining freedom once
$(a_0,\text{SN})$ are fit.** The agent's structural suspicion — that the density
"comes out that way" because of the fit — is confirmed, in sharpened form.

## 2. The Scan

Across the $(\mu,\kappa\lambda)$ family, each with its SN-fitted $\varepsilon_0$ and
with $\lambda=0.264$ throughout ($\kappa=\kappa\lambda/\lambda$):

| $\mu$ | $\kappa\lambda$ | $x_0$ | $\mu_0$ | $\kappa$ | $\Omega_\text{closure}$ | $/\Omega_b$ | $\Omega_\text{eff}=\Omega/\mu_0$ |
|---|---|---|---|---|---|---|---|
| simple | 0.20 | 2.54 | 0.72 | 0.76 | 0.217 | 4.4 | 0.30 |
| simple | 0.26 | 1.88 | 0.65 | 0.98 | 0.140 | 2.9 | 0.22 |
| simple | 0.307 | 1.54 | 0.61 | 1.16 | 0.104 | 2.1 | 0.17 |
| simple | 0.35 | 1.32 | 0.57 | 1.33 | 0.082 | 1.7 | 0.14 |
| standard | 0.35 | 1.44 | 0.82 | 1.33 | 0.140 | 2.9 | 0.17 |

(My proxy-refit at $\kappa\lambda=0.307$ gives 0.104 vs the seed-update's quoted
0.134 — presumably the joint fit's own $\varepsilon_0/\mu$ specifics; the
consolidator should reconcile, but nothing below depends on which value inside the
0.08–0.22 band is right.)

## 3. Answers to the Agent's Structural Question

**Is the fit quietly reproducing $\Lambda$CDM's matter budget?** No — and this
matters for how the problem is framed. The band is 0.08–0.22, robustly *below*
$\Lambda$CDM's $\Omega_m\approx0.315$ and robustly *above* $\Omega_b=0.049$. The
closure is not recreating the standard matter budget through a back door; it is
demanding its own, intermediate one. (Curiosity, recorded as numerology only: the
*phantom-inclusive* $\Omega_\text{eff}=\Omega/\mu_0$ column brushes 0.30 at the
low-$\kappa\lambda$ end.)

**Is it structurally forced above baryons?** Yes, decisively. Forcing
$\Omega_\text{closure}=\Omega_b$ at fixed SN shape ($\kappa\lambda=0.307$) requires
$\kappa=2.47$, which drives $\lambda\to0.124$ and hence
$a_0\to0.56\times10^{-10}$ m/s² — off the empirical value by $\times2.1$. So the
correct statement of the problem is: **three measurements (the $a_0$ value, the SN
shape, the mass census) over-determine two parameters $(\lambda,\kappa)$, and at
central values they fail to close by $\times1.7$–$2.9$.** This is not "unexplained
mass to mechanism later" — it is a live, quantitative internal tension of exactly
the kind this project exists to surface. The agent is right that it outranks the
seed analysis, which lives inside the same closure whose normalization is now in
question. Elevated accordingly (§6).

## 4. The One Escape Within Known Physics — Marginal, and Sharply Falsifiable

Relic neutrinos carry Standard-Model rest mass not counted in $\Omega_b$ — the one
form of extra mass that does *not* concede "no dark matter." Two honest caveats
first: the relic abundance formula ($\Omega_\nu h^2=\Sigma m_\nu/93.14$ eV) is
imported from standard early-universe physics this framework cannot yet derive (no
radiation era), and premise 3 must apply to neutrino masses (it does, by
construction). With the KATRIN bound ($m_\beta<0.45$ eV $\Rightarrow\Sigma
m_\nu\lesssim1.35$ eV): $\Omega_\nu\lesssim0.030$.

Arithmetic, not advocacy: neutrinos at the lab limit close the budget **only** at
the SN-shape-preferred end — $\kappa\lambda=0.35$, simple $\mu$:
$\Omega_\text{closure}=0.082$ vs $\Omega_b+\Omega_\nu\lesssim0.079$, i.e. marginal
at the $\sim5\%$ level and requiring $\Sigma m_\nu\approx1.5$ eV, *at or just beyond*
the current laboratory limit. At the joint-fit value ($\kappa\lambda\approx0.31$)
even maximal neutrinos leave a $\times1.3$–1.6 gap at central $a_0$; combining
(low-end $a_0$, $-1\sigma$) + (maximal $\Sigma m_\nu$) + (high $\kappa\lambda$) can
shrink the tension to near unity. Consequence: **the minimal resolution is directly
falsifiable by terrestrial neutrino-mass experiments** and by the joint fit itself —
which should now be extended (§6) to include the mass census as a likelihood term.
Note also that standard cosmological neutrino-mass bounds ($\Sigma<0.12$ eV) do
*not* automatically apply here — they are CMB/LSS results in $\Lambda$CDM, and this
framework has no perturbation sector to inherit them — but that cuts both ways: the
framework also cannot yet claim the perturbation-level consistency those bounds
encode.

## 5. Remaining Resolution Space, Ranked Honestly

1. **Machian-source amendment.** Should the horizon's gravitational-field energy
   (the phantom sector's energy) source the closure? Order of magnitude
   $\Omega_\text{field}\sim\xi^{-2}/3\kappa^2\sim$ few $\times10^{-2}$ — the right
   ballpark, but the coefficient of gravitational field energy is notoriously
   convention-dependent; acceptable only if derived from a principled energy
   accounting, never tuned to 0.05.
2. **Closure-form revision.** The one place a factor-2–3 could legitimately live —
   but any revision must preserve the fixed-point + instability structure that fits
   the SN diagram *and* the $\hat a_0(z)$ data. A tight needle; attempts should be
   logged even when they fail.
3. **New non-baryonic rest mass** (sterile-$\nu$ à la Angus). This is precisely
   MOND's own historical retreat at cluster scales. If ever taken, the Foundation's
   core claim must be rewritten from "no dark matter" to "no dark matter in galactic
   dynamics" — stated in §0, not buried.
4. **Acceptance as the framework's cluster-problem analog** — the $\sim2$–3$\times$
   residual known from MOND clusters, now appearing with a precise cosmological
   value. Legitimate only as a *labeled standing failure*, never as background.

## 6. Actions for Consolidation

- **Elevate** the closure density problem to a first-class open item, placed with
  (not after) the joint statistical fit — concretely: **add the mass census as a
  fourth likelihood term** (SN + $\hat a_0(z)$ + local RAR + $\Omega_\text{closure}$
  vs $\Omega_b[+\Omega_\nu(\Sigma m_\nu)]$ with $\Sigma m_\nu$ a bounded nuisance
  parameter). The fit then adjudicates §4's marginal corner instead of us arguing
  about it.
- **Freeze further seed-origin analysis** until this triage is done, per the agent —
  the seed's amplitude is meaningless if the closure's normalization is wrong.
- **Add a falsification clause** to the Foundation: if the four-way fit cannot close
  the mass budget within $(a_0\pm20\%,\ \text{lab-limit }\Sigma m_\nu,\ \text{the
  }\nu_*\text{ window})$, the "no unaccounted mass" claim fails at cosmological
  scales, and the framework survives only in the weakened form MOND itself occupies.
- **Point 2 accepted — replacement language for the inhomogeneity channel:** "not
  excluded; the required coupling history (peaking at $z\sim5$–15) is currently
  unmotivated — an accommodation, not a candidate, until something independent of
  the target numbers fixes its epoch-dependence." Do not let "opportunity" survive
  the merge.
- **Point 3 accepted — anti-softening note:** the seed value
  ($6.5\times10^{-13}$) keeps its status verbatim: *an unexplained cosmic initial
  condition, cornered, not explained*; "110 orders milder than $\Lambda$" is a
  statement about the size of the debt, not its repayment. Add this sentence to the
  merged text so future passes inherit it.

## 7. Honest Ledger

The agent's review converted a filed byproduct into what it actually is: the
framework's sharpest current internal tension, an over-constraint failing by
$\times1.7$–2.9 at central values, with exactly one known-physics escape that lives
at the edge of laboratory exclusion. Gained: the tension is now exactly quantified,
its structural origin proven (not suspected), its resolution space enumerated, and
its adjudication folded into the already-planned decisive fit. Conceded: the
framework's core claim is, for the first time this iteration, in measurable danger
from its own bookkeeping — which is the project working as intended.
