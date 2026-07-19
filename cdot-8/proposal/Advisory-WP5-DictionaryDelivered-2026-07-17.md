# Advisory — WP5 Dictionary Delivered: the Skordis–Złośnik Stability Paper Resolves All Three §6c Blockers — $Q_0$ Confirmed Verbatim, the Exact $\mu^2=-Q_0^2F_{QQ}/(2(2-K_B))$ Map, and the Sign That Looked Like a Tachyon Is the Sign Stability Requires (for `cdot-8/WP5/`)

*2026-07-17. Advisory in response to §6b–§6c of
`Update-WP5-WeakFieldStructure-2026-07-17.md`. The worker's §6c stop was
the right call and its recommendation (b) — a touch point with the advisor
before deriving the full second-order action from scratch — is answered
here. Source fetched in full: Skordis & Złośnik, "Aether scalar tensor
theory: Linear stability on Minkowski space," PRD 106, 104041
(arXiv:2109.13287v2) — the paper where the condensate mass, the $Q_0$
expansion point, and the stability conditions are all defined precisely.
Numerics in `meff_exact_dictionary.py`. Verdict up front: **all three
blockers dissolve against this one source. (i) The $Y$-vs-$Q$ map needs no
field-redefinition computation — SZ's $F(Y,Q)$ is sector-additive at
quadratic order, cdot-8's quadrature determines the $Q$-sector, the
imported MOND term is the $Y$-sector, and the mass formula is invariant
under $Q$-renormalization. (ii) $f_G$ enters $G_N$, not $\mu^2$; the mass
formula carries no $G$ factors at all. (iii) $F_{QQ}<0$ is not a tachyon —
SZ's stability condition $K_2>0$ *is* $F_{QQ}<0$ in cdot-8's convention;
the worrying sign is the required sign. The exact dictionary gives
$1/\mu\approx5$–$10$ Gpc across AeST's stable $K_B$ range, $r_c\approx
64$–$100$ Mpc — the skeleton's qualitative conclusion is now the exact
conclusion, and the worker's remaining verification shrinks to one item:
the $F$-slot sign convention against WP0's extraction.***

---

## 1. The $Q_0$ question — closed, verbatim

The worker's §6b was right not to accept my characterization on say-so,
and right that Mistele's paper alone doesn't state it. The companion
theory paper does, three times over: on FLRW, "$\phi\to\bar\phi(t)$
leading to $Q\to\bar Q=\dot{\bar\phi}$"; the free function's $Q$-sector
"$K(\bar Q)$ has a minimum at $Q_0$ (a constant)"; and the quasistatic
setup is "regions... in the late universe where the time derivative of the
background field has settled in its minimum $Q_0$, i.e.
$\dot{\bar\phi}\to Q_0$... we may expand $\phi=Q_0t+\varphi$." **Mistele's
$Q_0$ is the frozen cosmological background value of $\dot\phi$ — the
same object cdot-8 evolves as $Q(t)$ — exactly as characterized, now with
the primary-source anchor the worker's flag correctly demanded.** The
cdot-8-specific difference is real and worth one sentence in the write-up:
AeST's condensate *settles at* a minimum ($F_Q(Q_0)=0$), while cdot-8's
slides perpetually under M5 ($F_Q\neq0$ — it *is* the dust-like invoice);
the linear term in $\delta Q$ is the background equation of motion, and
the quadratic term — the mass — is unaffected.

## 2. The exact dictionary — three lines, no field redefinitions

SZ expand their free function around the condensate point (their Eq. 10):
$$F=(2-K_B)\lambda_sY-2K_2(Q-Q_0)^2+\dots$$
so the $Q$-sector curvature is $K_2=-\tfrac14F_{QQ}(Q_0)$, and the
condensate mass — their Eq. 58, *the* $\mu$ that MMH 2023 constrains,
with SZ's own cutoff formula $r_C\sim(r_M\mu^{-2})^{1/3}$ — is
$$\boxed{\ \mu^2=\frac{2K_2Q_0^2}{2-K_B}=-\frac{Q_0^2\,F_{QQ}(Q_0)}{2(2-K_B)}\ }$$
This dissolves the three §6c blockers in turn:

- **(i) No $Y$-map needed.** $F(Y,Q)$ is sector-additive at quadratic
  order: the $Y$-sector is the MOND interpolation cdot-8 imports unchanged
  (and the $|Y|^{3/2}$ term "does not contribute to the second order
  action" — SZ, explicitly — so cdot-8's evolving $a_0(Q)$ coefficient
  cannot leak into $\mu^2$); the $Q$-sector is exactly what cdot-8's
  quadrature determines. And the formula is **invariant under
  $Q$-renormalization** ($Q\to sQ$ gives $F_{QQ}\to F_{QQ}/s^2$, so
  $Q_0^2F_{QQ}$ is unchanged) — the "$Q_0=1$ today" convention is safe,
  and the only unit entering is $F$'s $H_0^2$ scale, fixed by the invoice.
- **(ii) No $f_G$ dictionary needed.** $f_G$ (SZ Eq. 2's
  $G_N$-vs-$\tilde G$ relation) renormalizes Newton's constant; $\mu^2$ is
  a dispersion-relation mass written directly in action parameters and
  carries no $G$ factor at all.
- **(iii) The sign is a passed stability check, not a tachyon.** SZ's
  scalar-sector stability condition is $K_2>0$ (their Eq. 62) — which in
  cdot-8's convention is precisely $F_{QQ}<0$. The quadrature's
  $F_{QQ}(1,\text{today})=-0.696$ gives $K_2=+0.174>0$: **the sign that
  triggered the ghost worry is the sign stability requires.** Cross-check
  that the dictionary is self-consistent across both papers: SZ's
  propagating-mode mass $M^2=(2-K_B)(1+\lambda_s)Q_0^2/K_B$ at
  $\lambda_s\to0$ equals $2m_\times^2$ in Mistele's notation ✓.

**One verification remains with the worker, and only one**: that cdot-8's
$F(Q)$ occupies SZ's $-F(Y,Q)$ action slot with matching sign — i.e., the
WP0/WP3 cross-check against the independently-extracted AeST Friedmann
equation, which the worker states "still holds," asserted with the sign
made explicit. Everything above is conditional on that one line.

## 3. The numbers, exact and $K_B$-bracketed

With $F_{QQ}=-0.696\,H_0^2$, $Q_0=1$, across AeST's stable range
$0<K_B<2$ (`meff_exact_dictionary.py`):

| $K_B$ | $\mu$ [$H_0/c$] | $1/\mu$ [Mpc] | $r_c(10^{11}M_\odot)$ [Mpc] |
|---:|---:|---:|---:|
| 0.1 | 0.428 | 10006 | 100 |
| 0.5 | 0.482 | 8890 | 92 |
| 1.0 | 0.590 | 7259 | 81 |
| 1.5 | 0.834 | 5133 | 64 |

**AeST must impose $\mu^{-1}\gtrsim$ Mpc by hand** (SZ's own words: "on
observational grounds $\mu^{-1}$ must be larger than $\sim$Mpc"); **cdot-8
gets $\mu^{-1}\approx5$–$10$ Gpc for free from the invoice** — three-plus
orders of magnitude above the requirement, immune to any $O(1)$ residue
in the one remaining sign verification. The condensate cutoff sits at
$r_c\approx64$–$100$ Mpc, far beyond the 1–3 Mpc of stacked lensing: MOND
persists at all survey radii, consistent with the MMH 2023 data that
pressures hand-tuned AeST. The skeleton's qualitative conclusion is now
the exact conclusion, and **the distinguishing advantage stands on the
primary sources' own formulas**. A bonus the skeleton couldn't see: SZ's
low-momentum unbounded-Hamiltonian window lives at $k<\mu$ — in AeST
that's sub-horizon ($\sim$Mpc); in cdot-8 it's pushed to *super-horizon*
scales ($\sim5$ Gpc), exactly where SZ's own caveat says the Minkowski
analysis yields to FLRW — the M5-governed background itself. Cleaner than
the parent theory, again by construction rather than choice.

## 4. Housekeeping — one stale section, one standing set

1. **§7 of the worker's document is stale**: it still routes the RAR curve
   behind the two-limit question ("once that's settled"), contradicting
   both the ScaleUnbundling advisory's §5 unblock (sub-percent $m_\times$
   at galaxy scales, per Mistele's own figures) and the worker's own §6b
   acceptance. §7 needs the rewrite; **the lensing-RAR-by-lens-redshift
   confrontation is now WP5's only remaining deliverable and nothing
   blocks it** — Brouwer et al. 2021 (KiDS-1000) and Mistele et al. 2024
   (2310.15248) as anchors, $E(z_\text{lens})$ backbone as delivered,
   $\mu(z)$ from this dictionary as the condensate-cutoff line if wanted.
2. Standing, unchanged: the author's Foundation §6 item 6 decision on WP4a
   (the gate — stable input, should not age out); WP4b adjudication
   confirmation and errata chain; consolidation batch (this round adds:
   the $\mu^2$ dictionary as an established program result, the $Q_0$
   closure, the §6c-restraint pattern as the worked example of the
   verify-then-trust rule operating in both directions); log repairs;
   KATRIN clock most time-critical.

## Companion

- `meff_exact_dictionary.py` — the exact map, the $K_B$ band, the
  stability check, the cross-paper $m_\times$ consistency check.
- This advisory: proposed location
  `cdot-8/WP5/Advisory-WP5-DictionaryDelivered-2026-07-17.md`.
