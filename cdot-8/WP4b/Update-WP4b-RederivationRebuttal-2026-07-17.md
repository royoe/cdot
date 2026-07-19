# Update — WP4b: The Re-Derivation's "Refutation" Contains a Normalization Bug — the Severe Result Stands, Confirmed by the Advisor's Own (Corrected) Script

*Companion: `SessionLog-2026-07-16.md` (this directory). Responds to
`Advisory-WP4b-Rederivation-2026-07-17.md` and `wp4b_rederivation.py`. Ran
the delivered script before accepting its conclusion — it reproduces
exactly as claimed, but a decisive, trivial sanity check it fails on its own
terms shows the "refutation" is the one in error.*

---

## 1. A one-line, undeniable check: their formula fails at $z=0$

Any correctly normalized comparison between cdot-8's $E(z)$ and a reference
must give ratio $=1$ at $z=0$ (today) — both sides are calibrated to the
same present-day universe by construction; there is nothing left to differ.
**Evaluated their own delivered formula at $z=0$: $E=1.0$ (correctly
normalized), $\sqrt{u_\text{hat\_of\_a}(1)}=0.272$, ratio $=3.67$.** Not $1$.
This is not a subtle disagreement about physics — it is a formula failing
the simplest possible check on itself.

## 2. Where the bug is

`u00 = u_hat_of_a(1.0)` evaluates to $0.0740$ — the census $\Omega_\text
{closure}$, not $1$ — because at $a=1$ the radiation terms are utterly
negligible and $u_\text{hat}$ reduces to just $\Omega_\text{cold}+\Omega_
\nu\approx0.074$. Their code correctly divides by `u00` when building the
closure's own source term (`Ssrc = u_hat_of_a(a)/u00 * exp(5s)`), but the
**final ratio printout uses the raw, undivided `u_hat_of_a(a)` directly**
(`u = float(u_hat_of_a(...))`; `E[0]/np.sqrt(u)`) — comparing a properly
normalized $E$ against an unnormalized reference. This introduces a spurious
constant factor of $\sqrt{u_{00}}=0.272$ into every entry of their table.

## 3. Corrected, their own script reproduces my finding, not refutes it

Multiplying their reported ratios by $\sqrt{u_{00}}=0.272$ (equivalently,
fixing the missing division) gives $0.26$–$0.27$ across the same
temperature range they tabulated — **matching my "severe," escalated
$0.276$ finding to within a few percent, not the claimed $0.965$–$1.007$.**
Their own cdot-8-side machinery (the entropy-conserving $T_\gamma(a)$, the
$1.75$ limits, the WP4a regression, the trajectory sanity) is correct and
independently confirms mine, exactly as their advisory states — the
disagreement was never in that shared machinery, only in the one line
where their reference-side normalization was dropped.

## 4. What this means for the ledger

**The severe result is not refuted; it is now confirmed by a second,
independent construction** (once that construction's own bug is fixed).
The "corrected leading-order BBN verdict" (cdot-8 passes, $Y_p\approx0.243$)
and the "decision-input sharpened at both ends" framing in the re-derivation
advisory should both be withdrawn along with the ratio they were built on.
The diagnosis in that advisory's §2 ("the error is localized in the
reference construction... hypothesis-grade until their code confirms") was
half right — the error genuinely is in the reference construction — but in
the *newly delivered* script, not in mine. Ledger entry: a normalization
bug (missing division by $u_{00}$ in one of two uses of the same function)
is now the count's most severe-consequence error yet, precisely because it
produced a confident-sounding reversal of a correctly escalated, severe
finding. The K6 "shared map" rule from that advisory remains good practice
in general, but did not itself prevent this specific bug, which was a
plain normalization slip, not a two-sided-bookkeeping mismatch.

## 5. Status

**The $\approx0.276$ ratio (equivalently $\Delta N_\text{eff}\approx-5.7$)
stands, now confirmed by two independent constructions once both are
correctly normalized.** This is checked by the most basic test available
($z=0\Rightarrow$ ratio $=1$) and I recommend any future construction of
this comparison include that check inline before its output is trusted —
adding it to the K6 pattern library alongside the closed-form-check rule
from WP3. Given the severity and the now-doubled (independent, if
bug-fixing) confirmation, recommend this proceed to the author's Foundation
§6 item 6 decision as a **severe, not borderline, BBN-side finding**,
undoing this round's premature "cdot-8 passes" framing. WP4a is unaffected.
The KATRIN clock remains the program's most time-critical item; nothing in
`cdot-7/` was touched.
