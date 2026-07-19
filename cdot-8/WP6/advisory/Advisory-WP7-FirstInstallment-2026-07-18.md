# Advisory — WP7 First Installment Assessed: the Import Is Accepted; the $\delta\mathcal N$ Question Is Resolved Structurally (the Worker's Caution Was Right, and the Answer Has a Window); and the Pre-Computation for the $\Pi$ Question Exposes the Round's Real Finding — $\Omega_s$ Crosses Zero at $z\approx9600$, So the Fluid Form Cannot Cross the Crossover (for `cdot-8/WP7/`)

*2026-07-18. Advisory in response to
`Update-WP7-PerturbationStructure-2026-07-18.md`. Numerics in
`wp7_structure.py` (v2 — v1's inline check fired on two advisor errors,
both caught before delivery and recorded in §3). Every statement inherits
Gate 1(b)'s provisional-failure caveat, which this round makes *more*
concrete rather than less. Verdict up front: **the AeST
perturbation-system import is accepted; the horizon-scale decoupling
question is answered — $\delta\mathcal N\neq0$, the worker's refusal to
extend WP5's argument by analogy was correct, and the replacement
structure is a single global constraint whose per-mode force carries the
horizon-volume window $W(kR_h)$: clean import sub-horizon, a genuine new
M5 term at $kR_h\lesssim$ few. And the pre-computation of cdot-8's own
scalar-fluid $w(a)$ — which AeST's dustlike shortcut was going to be
checked against — finds something better than an answer: $\Omega_s$
crosses zero at $z\approx9600$, inside the Gate 1(b) crossover zone, so
the founding paper's fluid form is unusable through exactly the era that
matters most, and WP7 must run the crossover in field variables, where
everything stays regular.***

---

## 1. The $\delta\mathcal N$ question — resolved, with the worker vindicated

WP5's decoupling argument does **not** extend to cosmological scales,
exactly as §2 suspected: a $k$-mode contributes to the horizon-volume
census through the window $W(kR_h)=3j_1(kR_h)/(kR_h)$, which is $O(1)$
for $kR_h\lesssim1$ — $\delta\mathcal N\neq0$ there. But M5 remains
**one constraint per slice** (one $\Lambda_M(t)$, one $\bar Q(t)$,
one $q(\mathcal N_{\rm tot})$), so the perturbative force it exerts on
any individual mode carries that same window:

| $kR_h$ | $\lvert W\rvert$ | regime |
|---:|---:|---|
| 0.1 | 1.00 | super-horizon / SW plateau |
| 1 | 0.90 | horizon crossing |
| ~6 | 0.084 | first-acoustic-peak scale at $z_*$ |
| 20 | $2.7\times10^{-3}$ | higher peaks |
| $10^3$ | $1.7\times10^{-6}$ | matter power spectrum |

Consequences, in order of importance: **(i)** the AeST system imports
*cleanly* for all sub-horizon physics — matter power spectrum and the
higher acoustic peaks — with M5 corrections bounded by $(kR_h)^{-2}$;
**(ii)** a genuine, unavoidable new M5 term exists at
$kR_h\lesssim$ few — low-$\ell$ CMB and super-horizon evolution — which
is both WP7's real new derivation and a potential falsifiable signature
(stated with care: known low-$\ell$ curiosities in the data are *not* to
be claimed as support before the term is derived); **(iii)** the
first-peak scale carries a several-percent window — must be carried, not
dropped; **(iv)** none of this touches the background $\theta_*$: WP4a's
27% is a background statement, orthogonal to everything here — neither
rescued nor worsened. The worker's proposed task order stands, with the
structural answer now in hand: the next installment derives the
$\delta\mathcal N$ term explicitly in Newtonian gauge — density piece,
volume piece ($-3\Phi$), horizon-boundary piece, assembled with the
window — as the coefficient of the new term, not as a yes/no question.

## 2. The round's real finding: the fluid form cannot cross the crossover

Pre-computing cdot-8's scalar-fluid equation of state from the
established quadrature (correct WP3 constraint combination
$\rho_s=\tfrac12QF_Q-\tfrac13F$, verified against the invoice to
$10^{-4}$ inline):

| $z$ | $\Omega_s/E^2$ | $w$ |
|---:|---:|---:|
| 0 | +0.93 | $-0.68$ |
| 30 | +0.77 | $-0.01$ |
| 1100 | +0.43 | $-0.20$ |
| $10^4$ | $-0.003$ | (divergent) |
| $10^6$ | $-0.07$ | +0.34 |

Three structural facts, each load-bearing for WP7:

1. **$\Omega_s$ crosses zero at $z\approx9600$** — the scalar's share
   runs $+93\%$ today $\to0\to-7\%$ deep in radiation (the $-7\%$
   invoice, correctly signed). At the crossing, $w$ and $c_{\rm ad}^2$
   formally diverge: **the fluid description fails through exactly the
   crossover era, while the field variables ($\chi$,
   $\mathcal E_\alpha$) remain perfectly regular.** Directive: WP7 runs
   the crossover in field variables, switching to the fluid form only
   where $|\Omega_s|$ is $O(1)$. AeST's native dustlike-$\Pi\to0$
   shortcut does not transfer there — the worker's instinct to check
   rather than import was right before the reason was known.
2. **At recombination the scalar is 43% of the budget with
   $w\approx-0.2$** — a large, non-dust component at $z_*$. The
   perturbation-level physics of the CMB era is genuinely different from
   both ΛCDM and native AeST, and it is localized in the same
   crossover zone Gate 1(b) already flags: the same problem region, now
   with perturbation-level structure in it — coherent, not new damage,
   and exactly what the author's complete-through-WP7-first sequencing
   exists to map.
3. **Matter era $w\approx0$ by construction** (the invoice is dust-like
   there) — the dustlike limit *does* hold where structure formation
   happens, so the sub-horizon matter-power machinery imports with both
   the window suppression (§1) and the fluid form valid.

## 3. Advisor errors this round — self-caught, recorded

v1 of the companion script failed its own inline check (0.403 mismatch)
and its narrative conflated $E^2/u=0.93$ with the scalar's share. Two
errors, mine: the dictionary combination ($QF_Q-F$ for
$\tfrac12QF_Q-\tfrac13F$) and the $93\%$-vs-$-7\%$ conflation. Both
caught by the check before delivery — the inline-check rule doing
precisely its job, and the failed check is what surfaced §2's
zero-crossing finding. Ledgered as self-caught pre-delivery; the
fold-in queue gains the corrected dictionary combination as a reference
line for WP7's own derivations.

## 4. Housekeeping

The companion note says the session log is "to be created" — it exists,
at nine entries as of this morning; Entry-9 rule, continue numbering.
Consolidation-batch file sighting still expected at next sync; KATRIN
watch item unchanged. Nothing here touches `cdot-7/`.

## Companion

- `wp7_structure.py` — the window table, the corrected fluid
  computation, the zero crossing, the inline check (v1 failure noted in
  header).
- This advisory: proposed location
  `cdot-8/WP7/Advisory-WP7-FirstInstallment-2026-07-18.md`.
