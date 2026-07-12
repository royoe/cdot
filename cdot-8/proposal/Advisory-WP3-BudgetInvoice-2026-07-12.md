# Advisory — WP3 Budget Tension: The Invoice, Computed Along the Actual Trajectory (for `cdot-8/WP3/`)

*2026-07-12. Advisory in response to
`cdot-8/WP3/Update-WP3-BudgetTension-2026-07-12.md`. Author decision (SessionLog
2026-07-12 Entry 4): **option 3 endorsed** — the post-invoice claim language of §7
below is now cdot-8 policy. Companion: `budget_invoice.py` (every number below in
one pass). Verdict up front: **your arithmetic is correct; your severity estimate —
and the advisor's first-reply ratio — were both computed on the wrong solution; the
actual fitted trajectory's invoice is dramatically milder and has a shape nobody
ordered. Your escape route 1 was the right route, for a reason neither of us
identified.***

---

## 1. Corrections ledger, both directions

| Claim | Status |
|---|---|
| Worker: $\Omega_\text{closure}=\tfrac89\kappa\lambda\,\lambda x_0^2\mu(x_0)=0.0750$ | ✓ reproduced exactly |
| Worker: shortfall $13.3\times$ | ✓ *for the idealized fixed-point-through-today solution* — not the fitted cosmology |
| Advisor (first reply): grav-to-census ratio $\approx12.3$, "constant, a prediction" | **same idealization; superseded by §3** — recorded as a correction to the advisor, not only the worker |
| Advisor (first reply): "the invoice stands at high $z$" (route-1 dismissal) | **wrong in magnitude**: being *on* the fixed point at high $z$ fixes the slope, but the late-time departure rescales the *amplitude* of $E\equiv H_{\hat\tau}/H_{\hat\tau,0}$ everywhere. Route 1 helps enormously — your instinct to flag it as "the most promising unexplored escape route" (first escalation) was right both times |
| Worker §2: AQUAL's mechanism "structurally does not survive homogenization" | **incomplete** — see §2 |

## 2. Homogenization does not kill the mechanism — it rotates the gradient into time

Correct: $\nabla\Phi\equiv0$ on exact FRW, so the *spatial* branch of the free
function is inert there. Incomplete: in AeST's own FRW sector — the very Friedmann
equation you extracted — the free function is evaluated on the **temporal** gradient
$Q=\dot\phi$, and the $-\tfrac13(F-QF_Q)$ term you set aside *is* that mechanism's
homogeneous limit; it is exactly where AeST's dust-like scalar density comes from.
No non-additive construction (your option 4) is needed: the literature-standard
additive equation already contains a gravity-sector density whose form is dictated
by $F$ on $Q_0$. And note how cdot-7-flavored this is: the framework's own portal
was always $a_0=\lambda\dot c$ — a *time* derivative. "On FRW the free function
runs on $\dot\phi$" is mapping conjecture M2 saying itself back to us.

So WP3's correctly-posed question is: **does the census closure (M5), imposed on
AeST's FRW sector, fix $F$ and $Q_0(t)$ such that $-\tfrac13(F-QF_Q)$ reproduces
the demanded $\rho_s(a)$?** That demanded curve is what this advisory supplies.

## 3. The invoice, computed on the fitted cosmology

From the two-clock dictionary (first advisory) and the closure ODE:
$$E(s)\equiv\frac{H_{\hat\tau}}{H_{\hat\tau,0}}=e^{-3s/2}\,\frac{x_0}{x(s)\,r(s)},
\qquad a=e^{3s/2},$$
(check: matter fixed point $\Rightarrow E\propto a^{-3/2}$; radiation fixed point
$\Rightarrow E\propto a^{-2}$ — the closure's two attractors are *Friedmann-shaped*,
$H^2\propto a^{-3}$ and $a^{-4}$, before any invoice is written). Friedmann
accounting then defines the invoice:
$$\boxed{\ \Omega_s(a)\equiv E^2(a)-\Omega_\text{census}(a)\ }\qquad
(\text{M7 in the amended proposal}).$$

Along the **actual** three-component census trajectory (backward from $x_0=1.10$,
$\Omega_\text{closure}=0.074$, simple $\mu$):

| epoch | demanded total $E^2a^3$ | invoice $\rho_s a^3$ | $\rho_s/\rho_\text{census}$ | $w_s$ |
|---|---|---|---|---|
| $z=0$ | — | $\Omega_s=0.926$ | 12.5 (instantaneous) | $-0.68$ |
| $z=0.5$ | | | | $-0.41$ |
| $z=10$ | | | | $-0.006$ |
| $z=20$ | $0.334$ | $0.259$ | $3.45$ | $\approx0$ |
| $z=100$ | $0.321$ | $0.242$ | $3.04$ | $-0.03$ |
| $z=10^4$ | $E^2/u=0.997$ | $-0.003\,u$ | $-0.003$ | — |
| $z\gtrsim10^5$ | $E^2/u\to0.93$ | $-0.07\,u$ | $-0.07$ | — |

**Read that table slowly, because nobody tuned it:** the invoice component is
**dust-like precisely in the matter era** ($w_s\approx0$ for $z\sim10$–$100$) with
amplitude $\Omega_s^\text{dust}\approx0.26$; it **bends to $\Lambda$-like at late
times** ($w_s\to-0.68$ today) — the departure-from-dust *is* M6's $\Lambda$-analog,
now explicit as one continuous $w_s(a)$; and it **essentially vanishes in the
radiation era** (slightly negative, $-7\%$ of the census — a sign the
$(F-QF_Q)$ term or a $\tilde G\ne G$ renormalization can carry naturally). Compare
$\Lambda$CDM's $(\Omega_c,\Omega_\Lambda)\approx(0.265,0.685)$: **Friedmann
accounting of the fitted census trajectory spontaneously produces a dark sector of
$\Lambda$CDM-like shape and size.** Honest decomposition of that resemblance: the
$z\lesssim2$ agreement is partially guaranteed (the four-term fit was fit to
Pantheon+, which $\Lambda$CDM also fits); the matter-era plateau $\approx0.33$, the
dust-like $w_s$, and the near-zero radiation-era invoice are **not** guaranteed —
they are outputs of the closure, and they are the genuinely new content.

Two quantified confrontations fall out immediately:
- **Recombination:** $H_{\hat\tau}/H_{\Lambda\text{CDM}}\approx0.79$ at $z\simeq1090$
  (our census $z_\text{eq}\approx1080$ vs $\Lambda$CDM's $\approx3400$) — a real,
  21% background difference exactly where $\theta_*$ (0.03% precision) looks. This
  supersedes the advisor's earlier Stage-1 framing ("EdS-normalized, $\Omega=1$") —
  wrong for the actual trajectory; the true Stage-1 question is whether $r_s$ and
  $D_A$ shifts cancel in the ratio. **Stage-1 is hereby promoted to immediately
  after this advisory's adoption** — it is cheap and now decisive.
- **BBN:** deep-radiation $H_{\hat\tau}/H_\text{std}\approx0.966$, an effective
  $\Delta N_\text{eff}\approx-0.5$ — a $\sim3\sigma$-scale tension at face value,
  carried with two caveats: the trend value is read at $z=5\times10^5$ (grid edge),
  and the $e^+e^-$/QCD census re-weighting kinks (07-11 handoff, still uncomputed)
  sit exactly at the BBN epoch and now become **load-bearing** for this number.

## 4. Directives

1. **WP3, re-posed with the target curve in hand:** determine whether a census-
   constrained $F(Q)$ reproduces $\rho_s(a)$ of §3's table (dust-tracking plateau
   $\to$ late bend $\to$ small-negative radiation-era value). The demanded curve is
   in `budget_invoice.py`; your job is now inverse-function reconstruction plus the
   original constraint-propagation check — in that order, since a failed
   reconstruction moots the algebra.
2. **Insert WP4a (Stage-1 acoustic scale) and WP4b (BBN expansion rate)** before
   WP5, per the amended proposal. Both are background-level, both use machinery
   that now exists, both can kill or vindicate cheaply.
3. **Compute the $e^+e^-$/QCD census kinks** (was a 07-11 "well-posed, uncomputed"
   handoff; now prerequisite to trusting the $\Delta N_\text{eff}$ number).
4. **cdot-7 routing:** nothing in this advisory requires touching `cdot-7/`; the
   invoice is cdot-8 Friedmann accounting of a cdot-7 history that remains
   internally consistent. The $\Delta N_\text{eff}\approx-0.5$ marker, however,
   should be reported to the consolidator as a cdot-7-relevant external-confrontation
   flag (it is a statement about the shared background, not about the embedding).

## 5. Post-invoice claim language (author-endorsed, now policy)

cdot-8 does not claim "no dark matter" simpliciter. It claims: **no
freely-adjustable dark sector, and no particulate cold dark matter in halos.** The
gravitational sector carries energy — as every covariant theory's does, including
GR's $\Lambda$ — but its amplitude and history are census-determined, with the
$\rho_s(a)$ of §3 as a zero-knob prediction, and galaxy-scale phenomenology comes
from the MOND branch, not clustering particles. What is genuinely at risk, stated
plainly and kept in the risk register: if the census-locked component *perturbs*
dust-like as well, it is dark matter in all but provenance, and
provenance-plus-prediction is then the entire content of the claim. The perturbed
behavior is item-6/WP7 territory; the third-peak requirement identified on
2026-07-11 (something must gravitate without oscillating at recombination) now has
a named, amplitude-fixed candidate — which keeps the CMB a prediction, in both the
vindicating and the killing sense.

## 6. Protocol note

Second escalation, second correct call — including declining to read your own §2
homogenization argument as a kill when it felt like one. Note for calibration: both
you and the advisor independently computed on the idealized fixed point and both
overstated severity; the correction came from taking *your* escape route 1
seriously in amplitude rather than slope. Two-independent-checks caught the
arithmetic; it took the third pass to catch the solution-choice. That is the
pattern to remember: verify the *solution* is the physical one before verifying
the algebra on it.

## Companion files

- `budget_invoice.py` — the invoice along the actual trajectory: every table
  entry, the $w_s(a)$ curve, the $\Lambda$CDM comparison, the BBN marker.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-BudgetInvoice-2026-07-12.md`.
