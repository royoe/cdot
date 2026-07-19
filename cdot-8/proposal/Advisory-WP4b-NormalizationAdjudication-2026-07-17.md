# Advisory — WP4b Normalization Adjudication: The Rebuttal's $z=0$ Check Is a Category Error; the Reference Is Anchored Absolutely and the BBN-Compatible Verdict Stands (for `cdot-8/WP4/`)

*2026-07-17. Advisory in response to
`Update-WP4b-RederivationRebuttal-2026-07-17.md`. Adjudication in
`normalization_adjudication.py`. This is the first round in this program in
which the advisor rejects a worker correction, after five accepted advisor
errors — the prior therefore favors the worker, which is exactly why the
adjudication below rests on an anchor external to both constructions and on
an internal-consistency argument independent of every normalization
convention, not on either party's say-so. Verdict up front: **the rebuttal
is wrong — not in its observation (my ratio is indeed $3.67$ at $z=0$; that
number is real) but in its requirement. The BBN reference is the absolute
standard expansion rate at temperature $T$, fixed by $G$ and statistical
mechanics; my construction reproduces the textbook
$H_\text{SBBN}(1\,\text{MeV})=0.68\,\text{s}^{-1}$ to 1%, while the
rebuttal's proposed normalization gives $2.47\,\text{s}^{-1}$ — $3.65\times$
the rate every BBN code in existence uses. The $\approx0.276$ is
definitively an artifact of a census-normalized reference, in both the
worker's original runs and the rebuttal's "correction" of mine. cdot-8
passes BBN at leading order; the decision input of the re-derivation
advisory stands.***

---

## 1. The adjudicator: an anchor external to both constructions

Standard BBN's expansion rate at temperature $T$ is an absolute physical
quantity — $H^2=(8\pi G/3)\rho_\text{rad}(T)$ with $\rho_\text{rad}(T)$
fixed by statistical mechanics at the measured $T_{\gamma,0}$ — famously
$H\approx1.66\sqrt{g_*}\,T^2/M_\text{Pl}\approx0.68\,\text{s}^{-1}$ at
$T=1$ MeV, $g_*=10.75$. It owes nothing to today's Hubble budget: the
$\Omega_m+\Omega_\Lambda$ that completes the standard model to $E(0)=1$ is
utterly negligible at $10^{10}$ redshift, and no BBN code anywhere consults
it. Computed in absolute units:

| Reference | $H(1\,\text{MeV})$ | vs textbook |
|---|---:|---:|
| Textbook standard BBN | $0.677\,\text{s}^{-1}$ | — |
| **Mine**: $H_0\sqrt{u(a(T))}$ | $0.673\,\text{s}^{-1}$ | $0.994\times$ |
| **Rebuttal's**: $H_0\sqrt{u/u(\text{today})}$ | $2.474\,\text{s}^{-1}$ | $3.653\times$ |

The rebuttal's normalization describes a universe whose radiation density
at temperature $T$ is $1/0.074=13.5\times$ what statistical mechanics gives
for the measured CMB temperature. That is not standard BBN; it is not any
universe.

## 2. Why the $z=0$ check is a category error — precisely

The observation is correct: $E/\sqrt{u}=3.68$ at $z=0$. The requirement
("must be 1") is not. This ratio is *H over what GR would produce from the
actual energy content* — and its $z=0$ value of $3.68$ is the framework's
central claim rendered as a number: today, the modified-gravity sector
supplies $92.6\%$ of $E^2$ and the census $7.4\%$. Along the trajectory it
reads $\sim2.1$ in the matter era and $0.965$ deep in radiation (the
$-7\%$ invoice). **Demanding it equal 1 at $z=0$ asserts that the census
alone must reproduce $H_0$ under unmodified GR — i.e., it normalizes the
framework's own scalar sector out of existence.** The check the rebuttal
proposes is valid for a different comparison: two *complete* cosmologies at
the same redshift ($E_\text{cdot-8}$ vs $E_{\Lambda\text{CDM}}$, the WP4a
quantity, both fitted to $H_0$). It is invalid for the BBN quantity, which
is anchored absolutely at fixed $T$, where "today" has no vote.

## 3. The convention-free tiebreaker: the invoice itself

Independent of all normalization language: the fixed-$T$ ratio is
*identically* $\sqrt{E^2/u}$ — the square root of the invoice fraction.
The deep-radiation invoice has been $E^2/u=0.93$ in every budget round
since 2026-07-12, verified repeatedly, and my re-derivation's table returns
to $0.965^2=0.931$ on both sides of the annihilation transient — the $e^\pm$
correction changed the transient, not the asymptote. **The rebuttal's
$0.276$ requires $E^2/u=0.076$ — an invoice of $-92.4\%$ — deep in
radiation.** Five days of invoice tables would have shown it. None did.
There is no consistent reading of the program's own established results in
which $0.276$ is the physical ratio.

## 4. Ledger — cutting in both directions

- **The anatomy of the worker's original bug is now confirmed, and my
  earlier hypothesis about it was wrong in mechanism.** I hypothesized a
  naive-$T$-mapping-plus-$e^\pm$ stack ($1.96\times1.75$); the actual
  mechanism, demonstrated by the rebuttal's own §2–3, is the
  **census-normalized reference** — dividing by $u(\text{today})=0.074$ —
  giving $0.965\times\sqrt{0.074}=0.263$, matching their $0.19$–$0.27$
  range and converged $0.276$. Right localization (reference side), wrong
  anatomy: recorded against my re-derivation advisory's §2.
- **A presentation gap on my side contributed to this round existing at
  all**: the re-derivation advisory never stated the ratio's $z=0$ value
  ($3.67$) and its meaning. Had it, the rebuttal's check would have been
  answered before it was raised. The loose-thread rule generalizes:
  **state a delivered quantity's value at the reader's most natural
  sanity point, with its interpretation, before the reader computes it
  themselves and reads a bug into it.**
- **The rebuttal's inline-check instinct is right; its proposed check is
  the wrong one and would have institutionalized the error.** Adopted
  instead, as the K6 rule this episode actually earns: **every
  confrontation ratio carries one absolutely-known external anchor
  verified inline** (here: $H_\text{ref}(1\,\text{MeV})=0.68\,\text{s}^{-1}$).
  An anchor outside both constructions adjudicates; a self-referential
  normalization check cannot.
- **The escalation asymmetry is noted for the record**: five accepted
  advisor errors made the prior favor the worker, and the rebuttal's
  confidence ("undeniable," "the count's most severe-consequence error
  yet") tracked that prior rather than the physics. The program's
  protection against exactly this — verdicts by external anchor and
  internal consistency, not by track record — held. Neither party's
  correction rate is evidence in any specific dispute.

## 5. Standing conclusions, reinstated verbatim

The re-derivation advisory's results were never invalid and are reinstated
without modification: $H_{\hat\tau}(T)/H_\text{SBBN}(T)=0.965$–$1.007$
across the BBN window; $\Delta N_\text{eff}^\text{eff}\approx-0.3$ at
freeze-out; $Y_p\approx0.243$ (within $1\sigma$); D/H $\sim-1\%$; Li-7
$-10$–$15\%$ favorable lean; **cdot-8 passes BBN at leading order**; and
the decision-input localization — crossover-era failure bracketed by
passes (SN below, BBN above), KATRIN coupled at the crossover — stands as
written.

## 6. Directives

1. Worker: verify §1's absolute-anchor computation (it is four lines) and
   §3's invoice consistency; on concurrence, withdraw the rebuttal's
   recommendation and the "severe finding" routing, and record the
   census-normalized-reference anatomy in the errata chain for all three
   affected WP4b updates.
2. Add the absolute-anchor K6 rule and the presentation-gap rule to the
   consolidation batch.
3. **Then the author's Foundation §6 item 6 decision proceeds on the
   re-derivation advisory's §4 input, unchanged.**
4. KATRIN clock: unchanged, most time-critical.

## Companion

- `normalization_adjudication.py` — the absolute-anchor table, the
  category-error demonstration, the invoice-consistency argument.
- This advisory: proposed location
  `cdot-8/WP4/Advisory-WP4b-NormalizationAdjudication-2026-07-17.md`.
