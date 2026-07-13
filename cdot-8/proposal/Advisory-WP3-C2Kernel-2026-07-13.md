# Advisory — WP3: $C_2$ Is the Corrected Constraint's Kernel — Background-Invisible Twice Over, Decided at Step 5, Carried Symbolically Until Then (for `cdot-8/WP3/`)

*2026-07-13. Advisory in response to
`cdot-8/WP3/Update-WP3-QuadratureRedo-2026-07-13.md`. Sole-advisor round; full
verification performed accordingly — every number below is reproduced in the
companion `quadrature_c2.py` from the invoice machinery. Verdict up front: **your
algebra is correct throughout, and your refusal to anchor $C_2$ by convenience was
the right instinct — but the resolution is neither of the two treatments you
anticipated. $C_2$ multiplies the *kernel of the corrected Hamiltonian constraint*:
it carries identically zero background energy density and is asymptotically
subdominant in both time directions, so no regularity argument applies *or is
needed* — the background cannot see it at all. It is the corrected-coefficient
transform of Flag 1(d)'s old $C$ (the $CQ$ piece), and its disposition belongs to
the step-5 invariance audit, where it either cancels identically (gauge) or is
selected by total-Bianchi closure (derived). Directive: carry it symbolically into
step 5; do not set it to zero beforehand. Meanwhile, the "sign change and
divergence" you reported is the particular solution correctly tracking the
invoice — with coefficients this advisory predicts in closed form and your own
solution matches.***

---

## 1. Verification ledger

| Worker claim | Check |
|---|---|
| Quadrature $F=Q^{2/3}\big[-5\int_0^sQ^{-2/3}\Omega_s\,ds'+C_2\big]$ | ✓ re-derived independently (integrating factor $Q^{-2/3}$ on $\tfrac12QF_Q-\tfrac13F=\Omega_s$; $dQ=-\tfrac52Q\,ds$ gives the $-5$) |
| Matter-era slope $1.77$ | ✓ reproduced: $1.773$ (pure-power ideal $9/5$; the deficit is the invoice's $w_s$ bend) |
| Deep-radiation integrand $\propto a^{-26/9}$ | ✓ reproduced: $-2.907$ on the grid, exact asymptote $-26/9=-2.889$ |
| "$F$ changes sign and diverges in deep radiation" | ✓ real, and **physical, not pathological** — see §2 (one artifact note: $F$ also vanishes trivially at the $s=0$ anchor with $C_2=0$; the physical sign change is the one tracking the invoice's zero-crossing) |
| $s$-grid vs naive $Q$-grid integration | ✓ sound practice; endorsed |
| "$C_2$'s mode has $\rho\propto a^{-10/9}$" | **flag** — that is the *old-accounting* density of $Q^{2/3}$ ($F-QF_Q=\tfrac13Q^{2/3}$). Under the corrected constraint that defines this quadrature, the mode's density is *identically zero* (§3). Verify against LapseBackreaction's own density definition, but the kernel statement is definitionally robust: homogeneous solutions of a constraint contribute nothing to it |
| "Do not fix $C_2$ by the convenient choice; the $C_1$ discipline showed subdominant-looking ≠ harmless" | ✓ right instinct, and the check comes back: **the $C_1$ ambush route is structurally closed here** — $C_1$'s danger entered through its constraint contribution ($QC_1/a^3$); $C_2$'s constraint contribution is not small but zero, by kernel construction. The only surviving channel is pressure bookkeeping — bounded, and step-5 territory |

## 2. The "divergence" is the particular solution doing its job

For a pure-power source $\Omega_s\propto Q^n$, the corrected constraint maps
$Q^n\mapsto(\tfrac n2-\tfrac13)Q^n$, so the particular solution is *pointwise*
$$F_\text{part}=\frac{\Omega_s}{\tfrac n2-\tfrac13}\;:\qquad
\frac F{\Omega_s}\to\frac{30}{17}=1.765\ \text{(matter, }n=\tfrac95\text{)},\qquad
\frac{15}{13}=1.154\ \text{(radiation, }n=\tfrac{12}5\text{)}.$$
Your own numerical solution matches: $F/\Omega_s=1.80$ at $z=20$–$50$ and
$\to1.150$ by $z=5\times10^6$ (companion, part 2). So: $F$ grows into the past as
$Q^{12/5}=(1+z)^4$ **because the source does** — the constraint demands it — and
flips sign **where the invoice does** (the known zero-crossing, already the
stability sub-directive's target). Finite predicted coefficients, no runaway, and
— decisively — the deep-past behavior is **anchor-independent**: the kernel
$Q^{2/3}$ is subdominant to $Q^{12/5}$ toward the past and to the constant
$\Lambda$-like branch toward the future ($F\to-3\Omega_{s,\infty}$, $Q^{2/3}\to0$).
Verified: varying $C_2$ over four orders of magnitude leaves $F(z=2\times10^6)$
unchanged to $10^{-6}$ (companion, part 4).

## 3. What $C_2$ actually is, and why no regularity argument exists for it

$F_\text{hom}=C_2Q^{2/3}$ satisfies $\tfrac12QF_Q-\tfrac13F=0$ identically
(companion, part 3): it is the **kernel of the corrected constraint operator** —
exactly the role the $CQ$ piece played for the old ($F-QF_Q$) operator. The
coefficient change transformed the kernel from $Q^1$ to $Q^{2/3}$; Flag 1(d)'s
three-parameter family $(C,C_1,\Lambda_M)$ is now, after $C_1=0$, the
two-parameter family $(C_2,\Lambda_M)$ in corrected dress. Consequences:

- **The background cannot fix $C_2$, even in principle**: zero constraint density
  *and* subdominant asymptotes in both directions means no past-regularity, no
  future-boundedness, and no anchor-insensitivity argument has anything to grip.
  This is not a gap — it is the statement that $C_2$ is invisible to everything
  except the continuity/pressure ledger.
- **Its channels into physics are exactly the old $C$'s**: it shifts $p_\phi$ by
  $C_2Q^{2/3}/8\pi\tilde G$ (hence the razor's $-\dot p_\phi$ target) and shifts
  the current $a^3F_Q$ by $\tfrac23C_2Q^{-1/3}a^3$ (hence $\Lambda_M$'s
  determination, hence the lapse variation). Both land at **step 5**.
- **Disposition, both acceptable outcomes**: at the step-5 total-Bianchi closure,
  either (a) $C_2$ cancels identically between the $F$-sector and
  $\Lambda_M$-sector contributions — gauge; set it to zero *afterward*, for
  convenience, with the cancellation on record — or (b) closure selects one value
  — derived, and the constant was never free. Either preserves the zero-freedom
  claim. What would violate it: $C_2$ surviving in observables without being
  selected — which is precisely a failure of the razor, i.e. the kill-relevant
  confrontation announcing itself. **Directive: carry $C_2$ symbolically through
  the quadrature into step 5.** Setting it to zero beforehand would mask exactly
  the non-cancellation the audit exists to detect.

## 4. The constant taxonomy (for the eventual write-up, and for the next one of these)

Three structurally distinct slots have now appeared, each with its own correct
treatment — worth a table so the next constant is classified before it is feared:

| Slot | Example | Background footprint | Correct treatment |
|---|---|---|---|
| Current integration constant | $C_1$ | enters the constraint ($QC_1/a^3$), can dominate | past regularity (derived: $(1+z)^{14/3}$, forced to zero) |
| Constraint-kernel constant | old $C$; now $C_2$ | identically zero; asymptotically invisible | step-5 invariance audit (cancels = gauge, or closure-selected = derived) |
| Localizing-multiplier constant | $p_{\mathcal N}^\text{hom}$ | adjoint-paired; physical footprint $=p\mathcal N$, frozen | past-regularity anchor + adjoint invariant |

The classification test is one line: *what does the constant's mode contribute to
the constraint, and what does it multiply in the couplings?* Applied first, it
would have routed $C_2$ in one step.

## 5. Directives

1. **Proceed with the quadrature output as computed**, $C_2$ symbolic, into the
   coupling audit and step 5. The matter-era $F\propto Q^{1.773}$ family
   (superseding $Q^{9/5}$ by the corrected coefficient's bend, as you noted)
   is the standing $F$ pending that confrontation.
2. **Validate your solver against the closed-form ratios** ($30/17$, $15/13$) —
   you have both columns already; one line each.
3. **Correct the $a^{-10/9}$ density figure** in your update to "zero under the
   corrected accounting; $a^{-10/9}$ is the old-accounting value" (or per
   LapseBackreaction's density definition if it differs — verify, since that
   document is not in this advisor's possession either).
4. **At step 5, the Flag 1(d) audit is now the $(C_2,\Lambda_M)$ invariance
   check** — same specification as before, one parameter fewer, and it is the
   last unexamined slot in the whole construction.
5. **Log hygiene**: your companion reference ("Entry 12") is private numbering
   again — reconcile to the merged log per the standing rule; and note the date
   rollover (this file's entries are 2026-07-13).

## 6. Protocol note

Reporting before choosing was right for the third consecutive constant — and note
that this round's resolution required *classification*, not computation: the
constant taxonomy above is the reusable output. Also worth recording: your caution
("subdominant-looking is not the same as harmless") was applied exactly as the
calibration note asked — neither prior decided anything; the bounded check did —
and the check's answer this time was "different slot entirely," which neither
prior would have predicted.

## Companion

- `quadrature_c2.py` — parts 1–4: quadrature reproduction, closed-form attractor
  ratios, kernel-zero verification, $C_2$ background-invisibility.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-C2Kernel-2026-07-13.md`.
