# REVIEW NOTE — T16 Rewrite: The First-Peak Failure Is Baryon-Loading-Dominated

*Status: review note, to be folded into the T16 (cdot-5) rewrite before merge.*
*Date: 2026-07-04.*
*Targets: T16 draft §"Acoustic Peaks — (C)", opening paragraph, Status table, Open Questions.*
*Depends on: T23_Percolation_Transition.md; T16 cdot-5 draft under review.*

---

## 0. One-line summary

The rewrite's $\ell_1\approx1674$ calculation is **arithmetically correct** and
the flagged validation was rightly run. But the document attributes the failure
to the counting-law extrapolation, whereas decomposition shows the **dominant
lever is the assumed baryon loading $R\approx680$** (through the sound speed
$c_s$), not the distance law. The failure is a *compound* of two model inputs,
and the larger one — $R\approx680$ — is independently testable against peak
*heights* with **zero** counting-law extrapolation. The conclusion should be
reframed accordingly, and $R\approx680$ should be the first thing tested.

---

## 1. The calculation reproduces exactly

Using the T23 broken law ($B=33.55$, $z_*=1.201$, $q=1.37$, $D_0=-0.46$, $r_d$
units) and $R=680$: $D_p(\infty)=116.68$, $D_p(1090)=107.56$, $c_s/c=0.02212$,
$r_s=0.202\,r_d$, $\theta_s=1.88\times10^{-3}$, $\ell_1=1674$. Confirmed. No
arithmetic issue.

## 2. Decomposition — where the $7.6\times$ actually comes from

Write the acoustic scale as
$$\ell_1=\pi\,\frac{D_p^\text{rec}}{c_s/c\;\big(D_p^\infty-D_p^\text{rec}\big)}
=\pi\,\frac{[\,D_p^\text{rec}/(D_p^\infty-D_p^\text{rec})\,]}{c_s/c}.$$

Two model-specific inputs:

| input | value | role |
|---|---:|---|
| distance factor $D_p^\text{rec}/(D_p^\infty-D_p^\text{rec})$ | **11.8** | the counting-law / geometry contribution |
| $c_s/c=1/\sqrt{3(1+R)}$ at $R=680$ | **0.0221** | the baryon-loading contribution |

Sensitivity of $\ell_1$ to $R$ at **fixed** distance law:

| $R$ | $c_s/c$ | $\ell_1$ |
|---:|---:|---:|
| 0.6 (ΛCDM-like) | 0.456 | 81 |
| 6 | 0.218 | 170 |
| 68 | 0.070 | 533 |
| 680 (model) | 0.0221 | **1674** |

The two ways to hit the observed $\ell_1=220$:
- **hold the distance law, vary $R$** → need $R\approx10.8$ (not 680, not 0.6);
- **hold $R=680$, vary the distance** → need the distance factor $7.6\times$
  smaller (1.55 vs 11.8), i.e. the "no $z_\text{rec}$ saves it, would need
  $z_\text{rec}\approx13$" result.

**Reading:** the $z_\text{rec}\approx13$ absurdity in the draft is an artifact of
forcing the *distance* to absorb a discrepancy that is mostly in $c_s$. The
distance law is off by a factor ~7.6; the baryon loading is off by ~20 (relative
to ΛCDM-like $R$). They **compound**; $R\approx680$ is the larger lever.

## 3. Why this changes the conclusion, not just the wording

The draft quarantines $R\approx680$ to peak *heights* (ingredient C, higher
peaks) and treats the first-peak *position* as a clean counting-law test. But
$R$ enters the position too, through $c_s$, and dominates it. So "the counting
law extended to recombination fails by $7.6\times$" is not a clean verdict on
T23's law — it is a verdict on the *pair* (counting law, $R\approx680$), with the
second element carrying most of the weight and being the less-justified of the
two.

$R\approx680$ vs the standard plasma $R\approx0.6$ is a **thousandfold**
discrepancy. It is asserted in the draft from "both $\rho_b$ and $\rho_\gamma$
scale as $c^2$, so $R$ is epoch-invariant" — but epoch-invariance fixes only that
$R$ *doesn't change with $c$*, **not** its present value. The value $R\approx680$
comes from evaluating $3\rho_b/4\rho_\gamma$ with today's $\Omega_b h^2$ and
$T_0$; in a static-$a$ model the photon energy density is not diluted by
expansion, so $\rho_\gamma$ today is the *same* bath as at recombination — which
is exactly why $R$ comes out ~1000× the standard value. That is a real, sharp
consequence of the static-$a$ premise, and it deserves to be the headline
concern, because:

**If $R\approx680$ is correct, the model fails the CMB almost regardless of the
distance law. If $R\approx680$ is wrong, the counting-law verdict is premature.**
The document cannot currently tell these apart, and should say so.

## 4. The test to run first — $R\approx680$ against peak *heights* (no extrapolation)

$R\approx680$ is falsifiable **without any distance-law extrapolation to $z=1090$**,
using only the plasma physics the draft already accepts as self-similar:

- The odd/even (compression/rarefaction) peak-height modulation is driven by $R$;
  the baryon drag scales as $(1+R)$.
- Observed CMB: the first-to-second peak asymmetry corresponds to $(1+R)\approx1.6$.
- $R\approx680$ predicts $(1+R)\approx681$ — a **~400× stronger** odd/even
  asymmetry than observed, i.e. the higher peaks essentially annihilated and the
  first peak grotesquely boosted.

This is a clean, present-value-physics falsification test of $R\approx680$ that
touches neither the counting law nor recombination distance. **It should be run
before the first-peak-position result is presented as a counting-law verdict**,
because its outcome determines how to read that verdict:

- if $R\approx680$ fails the peak heights → the CMB problem is localized to
  baryon loading (the static-$a$ $\rho_\gamma$ issue), and T23's counting law is
  substantially exonerated on the position;
- if $R\approx680$ somehow survives → then, and only then, is the $7.6\times$
  position miss a genuine counting-law tension.

Either way it is more informative than "the whole cosmological sector now hinges
on an unspecified third regime between $z=2.33$ and $z=1090$."

## 5. Clarity notes (the draft is otherwise very clear)

1. **Opening paragraph does too much.** It states result, direction, magnitude,
   the $z_\text{rec}\approx13$ consequence, and the caveat before the reader has
   any footing. Cut to: the T23 §7 validation was flagged; it has been run; it
   fails conditionally, and (per this note) the failure is baryon-loading-
   dominated. Let §C carry the detail.
2. **Justify the sound-horizon formula.** $r_s=(c_s/c)\,[D_p(\infty)-D_p(z_\text{rec})]$
   is the load-bearing equation and is asserted, not derived. Add one line: the
   sound horizon is the sound-speed fraction of the proper distance sound could
   traverse between genesis (the horizon $D_p(\infty)$) and recombination.
3. **Separate the "92% of horizon" fact from the "tiny $r_s$" claim.** The 92% is
   real geometry (distance law). The tiny $r_s$ is *mostly* $c_s$ ($R=680$).
   Presenting them together reads as if the small sound horizon were a distance
   fact; it is dominantly a sound-speed fact. Keep them distinct in the prose to
   avoid the misattribution §3 corrects.

## 6. The new questions (§Open Questions)

- The "third regime between DESI and recombination" question is well-posed and
  honest, but it is **not** the highest-leverage new question. Demote it below:
- **New load-bearing question (replaces it):** *Is $R\approx680$ correct at
  recombination?* This is the larger lever on $\ell_1$, it is a direct
  consequence of the static-$a$ premise (undiluted $\rho_\gamma$), and it is
  testable against peak heights with no extrapolation (§4). It gates both the
  first-peak position and the higher-peak heights simultaneously — a genuinely
  unifying open question, unlike the third-regime hypothesis which nothing
  predicts.
- Keep the $z_\text{rec}$-derivation item, but reframe: the sensitivity of
  $\ell_1$ to $z_\text{rec}$ is real, but §2 shows $z_\text{rec}$ is being asked
  to absorb an $R$-driven discrepancy; deriving $z_\text{rec}$ will not help while
  $R\approx680$ stands.

## 7. What is unaffected and correct

The self-similarity of the plasma shape (invariance of $R$ *with respect to
epoch*), the finite-horizon precondition inherited from T23/T14 (correctly noted
as what makes the calculation possible at all), the $r_s/R\propto R^{2-2n}$
carry-over with $n_\text{eff}\approx1.35$ appropriately down-weighted, and the
PBH-candidate structure are all handled correctly and are not disturbed by this
note. The intellectual honesty of running the flagged test rather than deferring
it is exactly right; this note sharpens *what* the test result means, and does
not dispute that it was run correctly.

---

## 8. Recommended action

Before merge: (i) run the $R\approx680$ peak-height test (§4); (ii) reframe the
§C conclusion and Status-table row from "counting-law failure" to
"baryon-loading-dominated failure, counting-law contribution ~7.6×, $R$
contribution ~20×, compounding"; (iii) promote $R\approx680$ to the load-bearing
open question and demote the third-regime hypothesis; (iv) apply the three
clarity edits in §5. The net effect is to relocate most of the CMB tension from
T23's newly-fitted counting law (which this session invested heavily in) onto the
older, less-examined baryon-loading premise — which is both more accurate and a
more tractable target.
