# Addendum — Fifth-Round Assessment: The $C_1$ Row Is Exact and Era-Independent; Strike Directive 3's Contingency (for `cdot-8/WP3/`)

*2026-07-12. Addendum to `Advisory-WP3-AnchorAndC1-2026-07-12.md` (stand-in),
following assessment of it and of `Update-WP3-MMPrimarySource-2026-07-12.md`
(worker). Verdict of record: **both endorsed without reversal.** The worker's
primary-source discipline closed directive 6 in full and surfaced a usable method
plus its counter-example; the stand-in's two corrections — the anchor as an
*implementation* of past regularity, not a replacement, and the non-transfer of
MM's source-smallness leg — are both correct and important, and the §4 ordering
(exponent table first, triple duty) stands. This addendum contributes one
sharpening in the good direction, two honesty caveats, and one struck contingency.*

---

## 1. Sharpening — the $C_1$ scaling is an exact identity, on every trajectory, in every era

The stand-in's §3 derives $Q\propto(1+z)^{5/3}$ "in the matter era" and asks for
the radiation/crossover exponents from the dictionary, with directive 3's
escalation trigger guarding the case where the radiation-era clock exponent comes
out $\le1$. The guard is unnecessary, because the relation is exact everywhere:
$$Q=\frac1N=\Big(\frac{c_0}{c}\Big)^{5/2},\qquad 1+z=\Big(\frac{c_0}{c}\Big)^{3/2}
\ \Longrightarrow\ \boxed{\,Q=(1+z)^{5/3}\ \text{identically, on any trajectory}\,}$$
— both sides are exact functions of $c$; no fixed point, era, or trajectory
assumption enters. With $a^3=(1+z)^{-3}$ (also exact), the $C_1$ mode's density
scales as
$$\rho_{C_1}\propto\frac{Q}{a^3}\propto(1+z)^{14/3}
\quad\text{exactly, always.}$$

**Independent verification through the $F$-sector route, including the integral
piece the two-line argument omits** (worker to re-verify): the $C_1$ piece of the
current gives $\Delta F_Q=C_1/a^3$; on the matter fixed point $a^3=Q^{-9/5}$, so
$\Delta F=\int(C_1/a^3)dQ=\tfrac5{14}C_1Q^{14/5}$ and
$Q\Delta F_Q=C_1Q^{14/5}$, hence
$$\Delta(F-QF_Q)=-\tfrac9{14}\,C_1\,Q^{14/5}\ \propto\ (1+z)^{14/3}$$
— same power as the constraint-route estimate: the $\Delta F$ integral does not
soften the scaling. (Off the fixed point the $Q/a^3$ factor is exact regardless;
only the $O(1)$ coefficient shifts.)

**Consequences:**
- **The $C_1$ row of the §4 exponent table is a one-liner, not a per-era
  computation.** The mode dominates any background component with
  $d\ln\rho_\text{bg}/d\ln(1+z)<\tfrac{14}3$ toward the past — and every era in
  the entire history sits below that: matter ($3$), radiation ($4$), the
  crossover (between), and the deep-past radiation attractor ($4$). **Past
  regularity therefore forces $C_1=0$ unconditionally** — Flag 1(c) option 1,
  closed derived, no census-exhaustiveness axiom, no K6 mechanism-debt entry —
  pending only the worker's verification pass and the coefficient audit of §2.
- **Directive 3's escalation contingency is struck**: "if the radiation-era clock
  exponent comes out $\le1$, escalate" cannot fire; the clock exponent is $5/3$
  identically. The eternal-past row *for the $C_1$ mode* is likewise covered by
  the exactness (the deep past is the radiation attractor, stiffness $4<14/3$).
- The forward prong sharpens the same way: $\rho_{C_1}$ decays *fastest* of all
  components toward the future, exactly, so the finite-anchor implementation with
  $C_1(t_*)=0$ is $t_*$-insensitive as a matter of identity, not estimate.

## 2. Two honesty caveats

- **The coefficient is unaudited by this advisor.** The stand-in's
  $\Delta(H_{\hat\tau}^2)=-QC_1/6a^3$ rests on the boxed coefficient-$\tfrac12$
  constraint of `Update-WP3-LapseBackreaction-2026-07-12.md`, which was not among
  this round's uploads. The **scaling** is confirmed two independent ways
  (constraint route and $F$-sector route share the exact $Q/a^3$); the
  **coefficient** remains on the worker's §3-verification list, unchanged.
- **The exactness shortcut covers the $C_1$ row only.** The
  $p_{\mathcal N}$ and $p_R$ homogeneous-mode rows depend on $g$'s
  trajectory-dependent coefficients; they are *not* era-independent, their
  eternal-past entries remain genuinely open, and MM's inflationary
  counter-example remains the standing warning for exactly those rows. Do not let
  the $C_1$ one-liner leak onto them: the species-resolved, per-era table of the
  stand-in's §4 step 1 is still required in full for the localizing sector.

## 3. Standing order of work, restated with the closure folded in

Stand-in directives 1–5 remain in force with one strike (the directive-3
contingency) and one closure (Flag 1(c), derived, pending worker verification):
(1) exponent table for $p_{\mathcal N}$/$p_R$, species-resolved, eternal-past row
included; (2) anchor-insensitivity demonstration; (3) quadrature redo against the
coefficient-$\tfrac12$ constraint with $C_1=0$; (4) the razor and the Flag 1(d)
$(C,C_1,\Lambda_M)$ invariance audit at step 5 — noting that with $C_1$ derived
away, that audit's role narrows to confirming the implementation respects it and
that the $C$-cancellation closes, which is now the last place a hidden knob could
hide. WP2 finalization still hard-blocks; all cdot-7 consolidation-log handoffs
unchanged.

## 4. Protocol note

Five rounds on WP3, and the pattern has now fully inverted from where the budget
tension started the day: each escalation has *removed* freedom from the
construction rather than added it. The confrontation the worker is walking toward
has, at this point, exactly zero adjustable elements pending two bounded
verifications — which is the position every prior advisory promised and none
could yet deliver. If step 5 passes, it will mean something; if it fails, it will
mean something. That is the whole point of the program, and it is now actually
true rather than aspirational.

*Proposed location: `cdot-8/WP3/Addendum-FifthRound-C1RowExact-2026-07-12.md`.*
