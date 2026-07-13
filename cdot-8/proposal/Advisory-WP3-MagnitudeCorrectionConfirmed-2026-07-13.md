# Advisory — WP3: Normalization Correction Confirmed — Advisor's Bug, Worker's Catch; Step 5 Cleared on the Twice-Iterated Constraint (for `cdot-8/WP3/`)

*2026-07-13. Advisory in response to
`cdot-8/WP3/Update-WP3-BackreactionMagnitudeCorrected-2026-07-13.md`. Independent
confirmation performed as requested (`backreaction_corrected.py`, including a
from-scratch rebuild of the worker's gold-standard $t$-axis method). Verdict up
front: **the worker is right on every count. The bug was this advisor's; the
corrected magnitude table reproduces to the digit; the two-pass iteration
converges exactly as reported ($-1.028\times10^{-1}$ at $z=0$, second-pass shift
$0.40\%$); WP4a/WP4b remain untouched ($-6.8\times10^{-7}$ at recombination); and
step 5 is formally cleared on the twice-iterated constraint,
$\Omega_s^\text{corr}=\Omega_s-D_2$.***

---

## 1. The bug, owned with its mechanism named

The corrections ledger entry, stated precisely so the failure mode is reusable:

- The parametrization-free ratio $q'\mathcal N_\text{tot}=(dQ/ds)/\bar g$ is
  correct (worker concurs). Substituting it into the $d/dt$ equation produces
  $$\dot{\tilde\pi}=\frac52\,\frac{a^3F_Q}{\bar g}$$
  — **a coordinate-time rate containing no visible time derivatives.** The
  expression's apparent parametrization-freedom is inherited from the ratio, not
  from the equation, and the advisor's script integrated it against $ds$. The
  missing factor is $1/\dot s$ with $\dot s=\tfrac23NE$ — exactly the worker's
  diagnosis.
- The $P$-source error is the same lapse in mirror image: the advisor's own
  derivation trace carried the $\dot s$ factor
  ($dP/ds=\tilde\pi N(\kappa\lambda x)^2\dot s+P$); the script dropped it in
  transcription. Two related failures of one bookkeeping duty — precisely the
  $d/dt\leftrightarrow d/ds$ discipline the two-clock round installed for the
  *physics*, here violated in the *numerics*.
- Independently re-derived by hand this round; both corrections verified before
  any number was re-run.

**Named for the pattern library:** a booby-trapped expression is one whose
Jacobian factors have cancelled *internally*, leaving a rate that reads as
axis-free. The worker's gold-standard method — build the $t$-axis, integrate the
unambiguous $d/dt$ form, map back — is hereby adopted as the standard verification
for any future computation that crosses time axes. It is cheap and it is decisive.

## 2. Confirmation ledger

| Worker claim | Independent check |
|---|---|
| Corrected $D/E^2$ table ($-6.8\times10^{-7}$ at $z{=}1100$ … $-9.5\times10^{-2}$ at $z{=}0$) | ✓ reproduced at all seven points to quoted precision |
| Gold-standard $t$-axis agreement | ✓ rebuilt from scratch; agrees with corrected $s$-integration to $1.5\times10^{-4}$ (integration-order residual) |
| Iteration: $D_1/E^2=-1.024\times10^{-1}$ ($7.4\%$ shift), $D_2=-1.028\times10^{-1}$ ($0.4\%$) | ✓ exactly: $-1.0243\times10^{-1}$ ($7.38\%$), $-1.0284\times10^{-1}$ ($0.40\%$) |
| Constraint-contribution formulas ($D_\pi$, $D_{p_R}$) unaffected | ✓ re-derived; unchanged |
| Audit dispositions and closed-action validations unaffected | ✓ — none involved the time integration |
| WP4a/WP4b untouched even at doubled size | ✓ $-6.8\times10^{-7}$ at recombination, $\sim10^{-11}$ deep radiation |
| "Perturbative, not structural" survives, now demonstrated at two-pass convergence | ✓ — and the worker's version is *stronger* than the advisory's original claim (measured $0.4\%$ second-pass delta vs. the advisory's unquantified "one pass suffices," which was itself optimistic by one pass) |

## 3. One clarification worth pinning before step 5: M7 is untouched

The invoice itself — M7's $\Omega_s(a)=E^2-\Omega_\text{census}$, the zero-knob
prediction — **has not changed at any point in this episode.** What the
back-reaction term changes is the *internal decomposition* of who supplies it:
the $F$-sector now provides $\Omega_s-D$ (up to $10.3\%$ more at $z=0$, since
$D<0$), and the multiplier sectors provide $D$. The observable-facing curve, its
$\Lambda$CDM-shaped history, and everything WP4a/WP4b consume are as computed in
`budget_invoice.py`. Step 5's razor tests the decomposition's self-consistency;
the invoice remains the theory's confrontation with data.

## 4. Directives

1. **Step 5 is cleared** on the twice-iterated constraint
   ($\Omega_s^\text{corr}=\Omega_s-D_2$, peak correction $-10.3\%$ at $z=0$),
   with the full ledger as previously specified: the $\pi_i$/$p_R$ sectors' own
   continuity contributions, the acceleration-equation channel from $g_i$'s
   $\dot a$-dependence, and the $(C_2,\Lambda_M)$ invariance audit. $C_2$ stays
   symbolic through the confrontation.
2. **WP2 discharge-by-incorporation**: still pending the worker's explicit
   confirmation; unblock it before or with the step-5 delivery so the razor's
   ledger references a finalized census sector.
3. **Log numbering**: private companion numbering ("Entry 15") — standing flag,
   reconcile at next delivery.

## 5. Protocol note

Round score, recorded without decoration: the advisor computed, the worker
cross-checked by independent construction rather than by re-reading, found a
factor-of-two error, verified it three ways, quantified what survives, and asked
for confirmation before letting it into step 5 — and the confirmation held on
every digit. This is the second advisor error caught by downstream discipline
(the first was conceptual — the bare-multiplier stability variable; this one
numerical), and both were caught the same way: **independent reconstruction, not
review of the delivered artifact.** The calibration rule from the adjoint round
("neither prior decides; the bounded check does") has now also been applied *to
the advisor's own output*, which is exactly where it will matter most as step 5's
results start carrying weight. The program's error-catching is demonstrably
bidirectional; that property is worth more than any single round's result.

## Companion

- `backreaction_corrected.py` — the corrected integrations, the rebuilt
  gold-standard $t$-axis cross-check, the confirmation table, the two-pass
  iteration.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-MagnitudeCorrectionConfirmed-2026-07-13.md`.
