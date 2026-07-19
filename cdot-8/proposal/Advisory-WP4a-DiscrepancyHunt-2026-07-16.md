# Advisory — WP4a Discrepancy Hunt: The Miss Localizes Entirely in $E(z)$ at $z\sim10^3$–$10^5$; $\Omega_b$ Is Innocent; the Levers Found Reach ~5%, Not 27% (for `cdot-8/WP4/`)

*2026-07-16. Advisory in response to the author's directive: "extra effort to
look for possible causes of the discrepancy... Are we missing something
important?" Full numerical treatment in `theta_star_diagnosis.py`. Verdict up
front: **something important was indeed missing — from the worker's §4
attribution, not from the calculation. Swap experiments show $\Omega_b$
contributes ~1% of the 27% miss, not the ~20% attributed to it: running
$\Lambda$CDM's expansion history with cdot-8's own census $\Omega_b=0.0442$
gives $100\theta_*=1.042$ — matching Planck's $1.041$ almost exactly. The
census baryon fraction is not merely innocent; it is spot-on. The entire
miss lives in $E(z)$ over the window $z_*\to\text{few}\times10^4$, where
cdot-8's expansion runs 15–21% slow relative to $\Lambda$CDM. Every candidate
rescue examined either closes (the census-convention freedom does not exist),
helps modestly in a direction aligned with the KATRIN tension (lighter
neutrinos: ~5% of the needed 27%), or is bounded small (perturbation-mapping
caveat: plausibly a few %). The miss survived the hunt, sharply localized.***

---

## 1. The localization — swap experiments

| Configuration | $r_s$ (Mpc) | $D_p$ (Mpc) | $100\theta_*$ |
|---|---:|---:|---:|
| cdot-8 baseline ($E_8$, census $\Omega_b$) | 173.4 | 13120 | **1.321** |
| $\Lambda$CDM reference ($E_\Lambda$, Planck $\Omega_b$) | 138.1 | 13390 | 1.031 |
| **cdot-8 $E$, $\Lambda$CDM $\Omega_b$** | 171.5 | 13120 | **1.307** ← $\Omega_b$ lever: 1% |
| **$\Lambda$CDM $E$, census $\Omega_b$** | 139.6 | 13390 | **1.042** ← $E$ lever: everything |

The worker's §4 attributed ~20% of the $r_s$ excess to the census
$\Omega_b=0.0442$ vs $\Lambda$CDM's ~0.049. **Corrected**: the baryon-photon
ratio $R$ depends on the physical density $\omega_b=\Omega_bh^2$, and cdot-8's
census $\omega_b=0.0217$ sits only 3% below Planck's 0.0224 — moving $c_s$ by
~1% and $\theta_*$ by 1.4%. The mis-attribution arose from comparing
$\Omega$'s at different implicit $h$'s. **Ledger entry: worker's §4 partially
corrected; and the flip side is a genuine positive result worth recording —
the census-forced baryon fraction, with zero tuning, reproduces the Planck
acoustic scale exactly when run through a $\Lambda$CDM expansion. The census
is not the problem. The expansion history is.**

## 2. Anatomy of the $E(z)$ deficit

$H_{\hat\tau}/H_{\Lambda\text{CDM}}$: 0.79 at $z_*$, 0.85 at $10^4$, 0.93
deep radiation (previously flagged; now the confirmed sole driver). The
deficit trough sits *at* recombination because the census matter-radiation
crossover ($z_\text{eq}^\text{census}\approx1080$, set by the heavy-$\nu$
census composition) coincides with $z_*\approx1090$ — cdot-8's radiation
support arrives exactly as $\Lambda$CDM's is still contributing its 32% boost
from its much earlier $z_\text{eq}\approx3400$. In budget terms: the missing
piece at $z_*$ is $\Delta\Omega_{m,\text{eff}}\approx0.15$-equivalent —
the M7 invoice's dust component (0.26, $\Lambda$CDM-like at $z\sim20$–$100$)
declines toward recombination rather than holding, and the radiation era
carries the invoice's $-7\%$.

## 3. The hunt — every candidate, with its outcome

1. **Census $\nu$-weighting convention** (the 07-11 $z_\text{eq}$ range
   1081–1832 across conventions): **closed — this freedom does not exist.**
   The census law itself is the exact massive-FD dispersion
   $\sqrt{(mc^2)^2+(\hbar kc)^2}$, forced by the Planck-unit counting law
   with zero convention dependence; the "conventions" were diagnostic
   markers for *quoting* $z_\text{nr}$, never alternative sources. $E(z)$
   is convention-free. (Checked against the 07-11 census update's own
   derivation; the crossover-diagnostic range must not be mistaken for a
   physical uncertainty band in $E$.)

2. **The neutrino mass** — the one genuine lever, probed (derivative probe:
   $(\kappa\lambda,x_0)$ held; a real change requires a refit):

   | $\Sigma m_\nu$ (eV) | cold census | $E(z_*)/E_\Lambda$ | $100\theta_*$ |
   |---:|---:|---:|---:|
   | 1.374 (baseline) | 0.0442 | 0.793 | 1.321 |
   | 0.60 | 0.0610 | 0.804 | 1.290 |
   | 0.30 | 0.0675 | 0.817 | 1.271 |
   | 0.06 | 0.0727 | 0.835 | 1.253 |

   Lighter neutrinos (with option-iii/PBH cold makeup holding
   $\Omega_\text{closure}=0.074$) move $\theta_*$ in the right direction —
   **and this is the same direction KATRIN is pushing** (final ~0.3 eV
   analysis pending would exclude 1.374 eV). Two independent data
   confrontations pressing on the same parameter, the same way, is worth
   recording as a structural fact. But the magnitude: ~5% of the needed
   27%. Insufficient alone, even at $\Sigma m_\nu\to0$.

3. **The Stage-1 scope caveat (perturbation mapping)**: the measured
   $100\theta_*=1.041$ is extracted assuming standard acoustic propagation
   maps peak spacing to background $r_s/D_A$. In cdot-8 the AQUAL portal is
   *active* at recombination-era horizon scales (background $x(1100)=2.61$,
   $\mu=0.72$, effective boost $\sim1.4\times$), so the mapping is not
   guaranteed standard. Honest bound: MOND-type modifications act mainly on
   driving/heights; peak-*spacing* shifts (cf. the $N_\text{eff}$ phase
   shift) are few-percent effects. Stage 2 owns this question; it cannot
   plausibly absorb tens of percent, and pre-registering that expectation
   now is what keeps this from becoming the indefinitely-deferred rescue
   the Duerr–Wolf critique targets.

4. **The BBN/lithium angle (the author's hint)**: examined, and it cuts
   interestingly but not toward $\theta_*$. cdot-8's own BBN-era signature
   (pending the census kinks) is $H/H_\text{std}\approx0.93$–$0.96$
   ($\Delta N_\text{eff}\approx-0.5$) with $\omega_b$ 3% below Planck.
   Directional consequences: $Y_p$ *down* ~0.007 (observed 0.245 vs SBBN
   0.247 — mildly favorable); Li-7 *down* ~10–15% (toward the observed
   factor-3 deficit — right direction, far short of resolving it); D/H
   nearly neutral (the slower-$H$ decrease and the lower-$\omega_b$
   increase partially cancel, net ~$-2\%$, within errors). **So the
   framework's BBN signature is not hostile and even leans the right way
   on lithium — a genuine WP4b motivation — but BBN and the acoustic scale
   are different epochs and different observables: no BBN-assumption crack
   can absorb a 27% $\theta_*$ miss.** The lithium problem hints that
   standard cosmology's early-universe sector has at least one unexplained
   tension; it does not license discounting $\theta_*$, which is measured
   at 0.03% and is geometric rather than nuclear.

5. **Everything else checked and clean**: $h$ cancels in $\theta_*$
   exactly (both integrals $\propto c/H_0$); $z_*$ sensitivity including a
   plausible Peebles-equation delay from the slower $H$ is $\lesssim2\%$;
   the frame/clock structure of both integrals verified against Foundation
   §5.2's analytic fixed-point formula; the census source composition at
   $z\sim10^3$–$10^5$ is complete (b, $\gamma$, $\nu$ — nothing known is
   uncounted).

## 4. The honest summary for the Foundation §6 item 6 decision

Nothing important is missing at the background level. The 27% miss is
real, zero-knob, and now **sharply localized: cdot-8's expansion history is
15–21% slow over $z\sim10^3$–$10^5$**, driven by the census crossover
structure. The identified partial levers — the neutrino mass (KATRIN-aligned,
~5%) and the Stage-2 mapping (few %) — together plausibly reach 5–10%, not
27%. Any genuine rescue must put more gravitating budget into that specific
window, and the census counts everything the framework currently contains.

Restated as the decision input: the theory's own most rigid, most derived
sector (the census + closure through the radiation era) is what fails the
confrontation — not a tunable periphery. That is simultaneously the worst
news for survivability and the best news for the program's integrity: it
means WP4a tested the actual theory. The three readings from the previous
advisory stand, with the middle one now carrying the sharpened fact that
the miss localizes in derived structure; the decision remains the author's
under Foundation §6 item 6.

## 5. Directives

1. Correct the worker's §4 attribution per §1 (ledger entry; the positive
   census-$\Omega_b$ result recorded alongside).
2. Record the $\nu$-mass/KATRIN alignment as a structural note in the
   consolidation log: *two independent confrontations press the same
   parameter the same way; if the author ever authorizes a refit with
   lighter $\nu$ + option-iii cold, both should be re-evaluated jointly.*
3. The census-convention non-freedom (§3.1) recorded so it is not
   re-hunted.
4. WP4b's motivation is *strengthened* by §3.4 (the lithium lean) —
   unchanged in queue position, gated on the census kinks as before.
5. All prior outstanding items unchanged; **the KATRIN clock remains the
   program's most time-critical item — and is now formally coupled to the
   $\theta_*$ tension via §3.2.**

## Companion

- `theta_star_diagnosis.py` — the swap experiments, the $\nu$-mass probe,
  all table entries.
- This advisory: proposed location
  `cdot-8/WP4/Advisory-WP4a-DiscrepancyHunt-2026-07-16.md`.
