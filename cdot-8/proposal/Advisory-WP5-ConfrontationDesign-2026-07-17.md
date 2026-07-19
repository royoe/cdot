# Advisory — WP5 Confrontation Adjudicated: §8's Restraint Was Correct and Is Now Source-Confirmed; the Pooled Literature Cannot Decide Either Way; the Deliverable Closes as a Pre-Registered Prediction Plus the Differential Test Design That Can (for `cdot-8/WP5/`)

*2026-07-17. Advisory in response to §6c (rewritten), §7 (rewritten), and
§8 of `Update-WP5-WeakFieldStructure-2026-07-17.md`. Sources consulted this
round: Brouwer et al. 2021 (A&A 650, A113 / arXiv:2106.11677) and Mistele
et al. 2024 (JCAP 04, 020 / arXiv:2310.15248) at the level of their own
stated systematics. Design numerics in `rar_bin_test_design.py`. Verdict up
front: **§6c's independent verification is accepted — the dictionary
round is closed on both sides, including the F-slot sign check, and WP5's
structural questions are done. §8's refusal to convert "Mistele's pooled
1.24 shows no obvious enhancement" into a tension verdict was correct, and
the papers' own systematics statements now confirm it quantitatively: the
pooled comparison cannot decide in either direction. The honest closure of
WP5 is therefore a pre-registered prediction plus the test design that
escapes those systematics — the intra-survey differential bin ratio, which
cancels the zero-point and absolute-M/L degeneracies the pooled numbers
drown in, and which becomes decisive at the z≳0.6 lever arms that
DES-deep/HSC/LSST/Euclid provide. That is a complete, publishable WP5
outcome, not a deferral.***

---

## 1. §6c and §7 — accepted, closed

The rewritten §6c is the dictionary round done properly: every
load-bearing claim re-verified at the primary source, the one delegated
item (cdot-8's $F$ in SZ's $-\mathcal F$ slot, same $1/16\pi\tilde G$
prefactor, same sign — against WP3's validated term) confirmed
independently, the $M^2=2m_\times^2$ cross-paper algebra checked rather
than inherited, and the superseded text kept on the record. Nothing to
add; the $\mu^{-1}\approx5$–$10$ Gpc, $r_c\approx64$–$100$ Mpc result is
now a jointly-verified program result and goes to the consolidation batch
as such. §7's rewrite resolves the staleness flag. **All WP5 structural
questions are closed on both sides of the loop.**

## 2. §8's backbone cross-validation — accepted, with the offset given its role

Running cdot-7's own pre-existing $a_0(z)$ fit (read-only) against the
cdot-8 backbone is exactly the check worth having: two constructions,
independent in origin — one fit to SN+RAR data before cdot-8 existed, one
derived from the covariant closure — agreeing to 4–5% at $z=0.25$ and
1–2% at $z=1.0$ (the latter consistent with Foundation §5.5's fitted
$1.86$ at $z=1$ ✓). The worker's self-caught table misreading
(absolute-with-anchor vs bare ratio) is the presentation-gap rule working
from their side of the loop. Adjudication of the offset: real, small, and
now **promoted to the theory-side systematic band on the prediction** —
±4–5% at $z\lesssim0.35$, shrinking to ±1–2% by $z=1$. This has a design
consequence (§4): at short redshift lever arms the signal is comparable to
the theory band, so the test must be built on long lever arms, where the
band shrinks exactly as the signal grows.

## 3. §8's restraint — correct, and now source-confirmed on item (i)

The worker declined to read "pooled $a_0=1.24$ vs predicted 12–16%
enhancement at $\langle z\rangle$" as tension, for three stated missing
items. Item (i) — the papers' own uncertainty structure — closes from the
sources' own words: **Mistele et al. carry a 0.1 dex ($\approx26\%$)
systematic band on the ESD-to-acceleration conversion alone**, and
**Brouwer et al. name the unresolved baryonic budget ("missing baryons")
as "the single most severe limitation of our analysis"** — an uncertainty
that enters $g_\text{bar}$ and is absorbable into the fitted acceleration
scale in exactly the direction that masks or mimics an $a_0$ shift. Both
floors exceed the 12–16% pooled signal, and both are *common-mode* with
it. Conclusion, stated symmetrically as the evidence demands: **the pooled
literature numbers can neither confirm nor exclude
$\hat a_0\propto H_{\hat\tau}$.** The face-value observation stands as
recorded — no positive hint — and its evidentiary weight is, honestly,
small. Items (ii) (the $n(z)$ smearing) and (iii) (zero-point conventions)
are then not obstacles to overcome but the *reason to change the
observable*, which is §4.

Two adjacent facts from the reconnaissance belong in the write-up: the
literature gap (no redshift-binned lensing RAR exists) is a genuine,
reportable finding, and Brouwer et al.'s $6\sigma$ early-vs-late-type RAR
split is a known feature the binned analysis must control for (type
composition drifts with redshift in a flux-limited sample — a named
differential systematic, not a footnote).

## 4. The design: the intra-survey differential bin ratio

The observable that survives is
$$R(z_\text{lo},z_\text{hi})\equiv\frac{a_0(z_\text{hi}\text{-bin})}
{a_0(z_\text{lo}\text{-bin})}
\;\;\xrightarrow{\text{cdot-8}}\;\;\frac{E(z_\text{hi})}{E(z_\text{lo})},
\qquad\text{null: }R\equiv1,$$
measured within one pipeline and one stellar-population model, where the
absolute zero-point, the absolute $M/L$, and Mistele et al.'s 0.1 dex
conversion band all cancel as common modes. In the deep-MOND regime the
lensing amplitude carries $\sqrt R$. The design table
(`rar_bin_test_design.py`):

| $z_\text{lo}$ | $z_\text{hi}$ | $a_0$ ratio | amplitude | feasibility |
|---:|---:|---:|---:|---|
| 0.17 | 0.33 | 1.104 | 1.051× | KiDS median split — ~1σ, not decisive |
| 0.15 | 0.45 | 1.208 | 1.099× | KiDS edge bins — 1.5–2σ class |
| 0.20 | 0.60 | 1.292 | 1.137× | +DES/HSC depth — viable |
| 0.20 | 0.75 | 1.417 | 1.190× | HSC-deep/early LSST — decisive class |
| 0.20 | 1.00 | 1.651 | 1.285× | LSST/Euclid — decisive, ≫ theory band |

Surviving systematics to be modeled in the eventual analysis:
stellar-population evolution across bins at fixed $M_*$ (first order
absorbed by the shared SPS model; residual few %), selection/type-mix
drift (compare at fixed $M_*$ and fixed type per Brouwer's $6\sigma$
split), photo-z. Statistical sketch: KiDS-class pooled amplitude precision
~3% → bin ratio ~6% — short levers are directional only; the $z\gtrsim0.6$
levers are 3–5σ propositions. **Scoping caution for the write-up: this is
a test of $a_0$-tracks-$H(z)$ against $a_0$-constant, not of cdot-8's
$E$-shape against ΛCDM's — any $a_0\propto H$ theory predicts nearly these
ratios.** That is the evidence-collapse identity showing up exactly where
it should.

## 5. Closing WP5, and the scope boundary

Performing the binned analysis means reprocessing survey lens catalogs —
new data analysis, outside this advisory loop's verify-and-direct remit
and outside WP5's charter as written. **Directive: WP5 closes as (a) the
pre-registered prediction — the $E(z_\text{lens})$ curve with its ±4–5%→
±1–2% theory band and the $\sqrt E$ amplitude law; (b) the demonstrated
literature gap; (c) the differential test design of §4 with its
systematics budget and feasibility ladder.** That is a complete,
self-standing, falsifiable deliverable: the prediction is registered
before any binned data exist, which is the strongest epistemic position
this program can occupy. Whether to pursue the binned KiDS analysis as a
new work package (WP5b) or as an external proposal is an **author scope
decision**, flagged alongside — not instead of — the standing Foundation
§6 item 6 decision on WP4a, which remains the program gate.

## 6. Standing items

WP4b adjudication confirmation and errata chain — still owed, aging.
Consolidation batch — now also carries: the $\mu^2$ dictionary as a
jointly-verified result, the WP5 closure package, error #6 and the two K6
rules from the WP4b round. Log repairs (07-16 overwrite, numbering,
Entry-9) — one delivery. KATRIN — unchanged, most time-critical.

## Companion

- `rar_bin_test_design.py` — the lever-arm table, null, theory band,
  systematics budget, statistical sketch.
- This advisory: proposed location
  `cdot-8/WP5/Advisory-WP5-ConfrontationDesign-2026-07-17.md`.
