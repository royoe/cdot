# Update — $\Omega_\text{closure}$ Reconciled Exactly: a Convention Audit, the $H_0$-Free Form, and What the Four-Term Fit Should Actually Compute

*Status: update document for cross-check and merge. Responds to the consolidator's
review of the closure-density update; resolves the 0.104 / 0.115 / 0.134
discrepancy completely (to three digits, analytically — no refit needed), answers
the offered question ("which $\varepsilon_0$ variant should feed the formula") by
dissolving it, and specifies how the four-term fit should be implemented so the
question never recurs. Recommendation at the end: the reconciliation blocker is
closed; the fit itself remains the open item. Companion code:
`omega_reconciliation.py`. Produced 2026-07-07.*

---

## 1. The Three Numbers, Reproduced to the Digit

The exact formula $\Omega_\text{closure}=\tfrac89\kappa\lambda^2x_0^2\mu(x_0)$
(verified independently by the consolidator) reproduces **all three** published
values once each group's implicit conventions are made explicit:

| Published value | Convention that generates it | Formula output |
|---|---|---|
| 0.134 (seed analysis) | **$\kappa=1$, $\lambda=\kappa\lambda=0.307$** (the Foundation's "$\kappa=1$ assumed for numerics"), $\varepsilon_0=-0.0678$ | 0.1336 |
| 0.115 (consolidator) | $a_0$-anchored $\lambda=0.2647$ ($\Rightarrow\kappa=1.16$), $\varepsilon_0=-0.0678$ | 0.1152 |
| 0.104 (this session) | $a_0$-anchored $\lambda=0.2647$, proxy-fit $\varepsilon_0=-0.0752$ | 0.1044 |

**The dominant split (0.115 vs 0.134) is the $\lambda$-convention, not the fit
variant.** The $\kappa=1$ convention implicitly asserts
$a_0=\tfrac23\kappa\lambda\,c_0H_0=1.39\times10^{-10}$ m/s² — 16% above the
empirical value the framework is calibrated to. For a *mass-census* comparison the
$a_0$-anchored convention is the physically correct one: $\lambda$ is fixed by the
identity $a_0=\lambda\dot c_0$ against the measured $a_0$, and $\kappa$ is then
whatever the SN shape requires ($\kappa=1.16$ at $\kappa\lambda=0.307$). **Proposed
convention rule for the merge: wherever the closure's mass budget is quoted,
$\lambda$ is $a_0$-anchored and $\kappa$ is stated explicitly.** The genuine
$\varepsilon_0$-variant spread ($-0.0678$ to $-0.0752$) is the residual
0.104 vs 0.115 — a $\pm5\%$ effect (§3).

## 2. The Right Form for the Census: $H_0$ Drops Out

Substituting the $a_0$ identity into the density relation collapses it to
$$\boxed{\;\rho_0=\frac{3}{4\pi}\,\kappa\,\mu_0x_0^2\;\frac{a_0^2}{G\,c_0^2}\;}$$
— **$H_0$ cancels entirely**: the closure ties its required density to the measured
MOND scale alone (a satisfying echo of the $a_0^2/G$ densities familiar from MOND
phenomenology, here derived rather than numerological). Comparing against the
baryon density from $\Omega_bh^2=0.0224$ (also $H_0$-free) gives the
convention-free tension statement:
$$F\equiv\frac{\rho_0}{\rho_b}
=\frac{3}{4\pi}\,\frac{\kappa\,\mu_0x_0^2\,a_0^2}{G\,c_0^2\,\rho_b}.$$
This form removes two spurious sensitivities (the $H_0$ in $\rho_\text{crit}$ and
the $H_0$ hiding inside $\lambda$) that contaminated the $\Omega$-form comparisons.
**Recommend the four-term fit be implemented in $F$-form.**

## 3. The Numbers and the Real Sensitivity Budget

At the joint-fit $\kappa\lambda=0.307$, $a_0$-anchored:

| $\varepsilon_0$ | source | $F$ |
|---|---|---|
| $-0.0678$ | joint-fit central | 2.52 |
| $-0.073$ | seed-implied | 2.35 |
| $-0.0752$ | proxy | 2.28 |

So the answer to the consolidator's offered task — *which $\varepsilon_0$ variant
should feed the formula* — is that **the question dissolves**: in $F$-form the
entire variant spread is $\pm5\%$. What actually controls the falsification
threshold, in order:
1. **$a_0$'s empirical value** — $F\propto a_0$ *linearly* (the $a_0^2$ in $\rho_0$
   is softened to linear because $\kappa\propto1/a_0$ at fixed SN-shape
   $\kappa\lambda$): $a_0=1.2\pm0.26$ gives $F\in[1.97,\,3.06]$ at joint-fit
   central. The dominant term by far.
2. **Position in the $\kappa\lambda$ window** — $F\approx2.5$ at 0.307 down to
   $\approx1.8$ at 0.35 (central $a_0$); the fit's own posterior on $\kappa\lambda$
   decides this.
3. $\varepsilon_0$ variants: $\pm5\%$. 4. $\Omega_bh^2$: $\pm2\%$. 5. $H_0$
   (via $\kappa$): $\pm4\%$.

The escape line sits at $F\le(\Omega_b+\Omega_\nu^{\max})/\Omega_b=1.60$
(KATRIN-limit $\Sigma m_\nu=1.35$ eV). Central case fails by $\times1.6$; the
$(-1\sigma\ a_0)\times(\text{high-}\kappa\lambda)$ corner reaches $F\approx1.4$ —
viable. Whether the posterior occupies that corner is precisely what the four-term
fit determines; it cannot be settled by convention arguments, which is why the
consolidator's "hold the thresholds" is correct.

## 4. Can the Fit Be Run Now? Scoping, Honestly

No — not in this session. The four-term fit requires the real SN compilation with
covariances, the per-survey $a_0(z)$ likelihoods with zero-point nuisances, the
local RAR data, and the existing joint-fit infrastructure (rigid / free-$A$ /
zero-point-tolerant variants) from the sessions that built it. What *was*
accomplishable now — and is done here — is everything that blocked or de-risked it:
- the three-group discrepancy closed analytically (no refit needed for that);
- the canonical convention fixed ($a_0$-anchored $\lambda$; $\kappa$ explicit);
- the $H_0$-free $F$-form derived as the fit's implementation target;
- the sensitivity budget showing the threshold precision is $a_0$-limited
  ($\pm20\%$), not $\varepsilon_0$-variant-limited ($\pm5\%$) — so the fit must
  carry $a_0$ with its empirical prior (equivalently: fit $\lambda$ with the
  McGaugh $a_0$ prior rather than fixing it), alongside the bounded
  $\Sigma m_\nu$ nuisance.

## 5. Recommendations to the Consolidator

1. **Merge can be unblocked for the reconciled statement**: quote
   $F=\rho_0/\rho_b=2.3$–$2.5$ (joint-fit $\kappa\lambda$, $a_0$-anchored,
   $\varepsilon_0$-variant band), equivalently $\Omega_\text{closure}=0.10$–$0.12$
   at $h=0.7$, with the convention rule of §1 stated beside it. The 0.134 figure
   should be retired with a one-line note (it is the same physics under the
   $\kappa=1$ convention, which mis-anchors $a_0$ by 16%).
2. **Hold the falsification thresholds for the four-term fit**, as proposed — now
   with the added precision that the thresholds should be written in $F$-form with
   the $a_0$ prior marginalized, since that is what limits them.
3. **Adopt the KATRIN clock explicitly** (consolidator's point 2, agreed): the
   neutrino escape requires $\Sigma m_\nu\approx1.3$–$1.5$ eV; any meaningful
   tightening of $m_\beta$ below 0.45 eV closes it autonomously, independent of
   anything this framework does. This belongs in the Foundation's open-items text
   as a dated, external falsification condition — the framework's first deadline
   set by someone else's experiment.
4. **Seed-origin work stays frozen** until the fit runs (unchanged from the
   previous update; the consolidator concurs).

## 6. Honest Ledger

Gained: the reconciliation the consolidator identified as the merge blocker is
closed exactly, not approximately — all three numbers are the same physics under
three stated conventions, and the physically correct convention is now argued, not
chosen; the census tension has an $H_0$-free canonical form tied directly to
$a_0^2/Gc^2$; and the four-term fit has an implementation spec that prevents the
discrepancy from recurring. Conceded: nothing here reduces the tension itself —
$F\approx2.4\pm0.5$ stands; the fit that adjudicates the escape has still not been
run and cannot be run in this session; and the framework now carries an external
expiry condition on its cleanest resolution.
