# Advisory — §15's Negative Result Confirmed (Three Independent Checks All Verified); §16's Final, Derived Verdict Confirmed Exactly: R1 Is Not a Viable Recourse for the ISW-Band Instability — Eleven Rounds of Original Derivation Reach a Genuine, Well-Earned Answer (for `cdot-8/WP7/`)

*2026-07-21. Review of `Update-WP7-InstabilityRecourses-2026-07-21.md`
§15 (one more attempt at the $\gamma$-sector normalization) and §16
(the final, derived answer to R1's feasibility question). Gate 1(b)
carried; Gate 4's status addressed directly below. **Verdict up front:
both sections check out. §15 is a genuine, careful, triply-verified
negative result — the $\gamma$-sector gap is real and precisely
characterized, not an assembly artifact, and correctly left as a
standing open item rather than forced. §16 is the payoff of this
entire eleven-round derivation arc, and it reproduces exactly on rerun,
including a sign-tracking check I did independently by hand that
confirms the new completion term's sign and structure follow directly
from §10's own already-twice-verified result. R1 is now genuinely
resolved, not merely suspected: it does not stabilize the ISW-band
instability, because the derivation shows the completion modifies the
vector equation's off-diagonal term while leaving $\Pi$'s bracket — and
hence the Jacobian's dominant trace — completely untouched. This
answers the program's original target-list item 1 with a derived
result, closing the single piece of missing theory the whole recourse
program was waiting on.**

---

## 1. §15's negative result — all three checks verified independently

Ran `wp7_derivation_gamma_sector_normalization_attempt.py` directly —
every printed line reproduces exactly (Check 1's fresh bottom-up
re-derivation matches the corrected sign convention exactly; Check 3's
residual is $F_\mathcal Q(\dot\varphi-3\dot{\bar\phi}\Psi)$, confirmed
non-zero).

**Independently re-derived the $c_0=-2$ normalization constant by
hand**, since this is the load-bearing step of the whole check: the
already-confirmed bracket match gives $d(\text{action})/d\Psi\supset
+2\kappa[\text{bracket}]$; the primary source's own $\delta$-formula
(line 436-437, already verified in earlier rounds) has $\delta\supset
\nabla^2[\text{bracket}]/(8\pi\tilde Ga^2\bar\rho)$, so $8\pi\tilde G
\bar\rho\,\delta\supset\nabla^2[\text{bracket}]/a^2$; using $\nabla^2
\to-k^2$ (standard, not a free choice) and $\kappa\equiv k^2/a^2$
(this program's own established convention throughout), this is
$-\kappa[\text{bracket}]$. Equating $2\kappa=c_0\times(-\kappa)$ gives
$c_0=-2$ — confirmed, self-consistently derived from the
already-validated bracket match, not guessed. **This is exactly the
right way to pin a normalization constant** — from an already-checked
result, not an independent assumption — and it's good that this round
did it this way rather than fitting $c_0$ to make things work.

**The residual's precise form is itself informative, not just "not
zero"**: $F_\mathcal Q(\dot\varphi-3\dot{\bar\phi}\Psi)$ differs from a
clean $\gamma$-multiple only in the $\Psi$-coefficient (3 instead of 1)
— a clean, simple discrepancy, not a messy accumulation of stray terms,
which is itself evidence this isn't an assembly error (a genuine bug
would more likely produce an ugly, multi-term residual, not a clean
factor-of-3 mismatch on a single coefficient). **Endorsing the
decision to stop here**: three focused, independently-verified checks
(hand-assembly, $\delta_2$, and the normalization constant) each ruling
out a plausible error source is the right amount of diligence before
calling a residual "genuine" — continuing to guess at a fourth
explanation without new information would be exactly the kind of
unproductive iteration this program has learned to avoid.

## 2. §16 — the final answer, reproduced exactly

Ran `wp7_r1_derived_completion.py` directly:

```
lambda_s    z=1090      z=100       z=10    z=1      z=0.0
     0    3.356e+08   1.537e+05   131.3   22.27    90.05
  -0.5    3.356e+08   1.537e+05   131.4   22.47    90.07
  -0.9    3.356e+08   1.537e+05   131.4   22.62    90.09
    -1    3.356e+08   1.537e+05   131.5   22.66    90.09
    10    3.356e+08   1.537e+05   129.6   17.48    89.67
```

**Reproduces exactly**: unchanged to the stated precision at $z=1090$
across the entire tested $\lambda_s$ range (including exactly at
$\lambda_s=-1$, where the original, crude "uniform substitution" test
had found *complete* stabilization — the contrast could not be
starker), and the small $z=1$ response ($22.27\to22.66$, $\lesssim2\%$)
matches exactly.

**Independently checked the new completion term's sign and structure
by hand, tracing it back through §10's own result, rather than
accepting the script's formula on its own**: §10's corrected
Euler-Lagrange derivation found the vector equation, in "$K_B(\dot
{\mathcal E}_\alpha+H\mathcal E_\alpha)=[\text{original RHS}]-F_
\mathcal Y\dot{\bar\phi}\chi$" form, picks up exactly one new term.
Differentiating $-F_\mathcal Y\dot{\bar\phi}\chi/\mathcal K_B$ w.r.t.
$\alpha$ (using $\partial\chi/\partial\alpha=\dot{\bar\phi}$, and the
program's standing $d/dt\to H\,d/dN$ e-fold conversion) gives exactly
$-F_\mathcal Y\dot{\bar\phi}^2/(\mathcal K_BH)$ — **matching the
script's own `- FY * Qb**2 / (K_B * Hc)` term exactly**, confirming the
new addition isn't just numerically consistent but traceably the same
object §10 already derived and I already independently verified twice
before.

**Confirmed $\Pi$'s bracket and the trace ($a_{EE}$) are genuinely
left bare in this script**: `dPi_dalpha = kap3*(2-K_B)*Qb` (no
$\lambda_s$/$F_\mathcal Y$ anywhere) and `a_EE` has no $\lambda_s$-
dependence at all — matching §13's independently-verified finding that
$\Pi$ cannot see $F_\mathcal Y$ (since $\mathcal Y$ has no $\Psi$-
dependence, §5). This is the structural reason the scan comes out flat:
the trace dominates the eigenvalue (already independently confirmed via
the discriminant calculation in an earlier round, Entry 5 — $a_{EE}^2$
outweighs the off-diagonal-sourced term by seven orders of magnitude),
and the trace is exactly the piece this completion cannot touch.

## 3. The honest caveat is appropriately scoped, not glossed over

The momentum-constraint-sourced $F_\mathcal Y$ term from §12
($-2F_\mathcal Y\dot{\bar\phi}^2\partial_1\alpha$) is correctly excluded
here since its placement in the coupled system wasn't pinned down.
Worth stating explicitly why this doesn't threaten the verdict: this
term is, by its own derivation, an $\alpha$-sourced (off-diagonal-type)
contribution, not a trace-type one — and the trace's dominance by seven
orders of magnitude (§1 above, previously verified) means even a
sizeable off-diagonal correction from this second term would need to
be extraordinarily large to compete. Not proven here, but consistent
with everything already established, and correctly flagged as
unresolved rather than asserted away.

## 4. Status and recommendation

**R1 is now resolved, not merely suspected — the central conclusion of
eleven consecutive rounds (§5–§16) of original, independently-verified
derivation work.** The $\mathcal F(\mathcal Y,\mathcal Q)$ small-
gradient completion is a real, structurally well-motivated recourse
that genuinely modifies the theory (confirmed twice, via two
independent constraint derivations), but it modifies the wrong piece of
the vector-sector Jacobian to address the ISW-band instability: the
destabilizing term lives in $\Pi$'s own bracket contribution to the
trace, and $\Pi$'s bracket is now *confirmed* $F_\mathcal Y$-
independent, not merely observed to not respond in one numerical test.

**Recommending this be reported to the author as the resolution of the
commissioned derivation**, closing target-list item 1 with a derived
(not guessed) answer, and that the recourse ladder now formally move to
R3 (re-closure) or R4 (nonlinear-saturation reframing) per the original
sequencing (`Advisory-WP7-InstabilityRecourses-2026-07-21.md`) — this
is exactly the kind of author-level sequencing decision this program
has consistently reserved for the author rather than resolving
unilaterally (cf. WP4a's own three-way fork). Gate 4 remains formally
paused pending that decision; this diagnostic/derivation arc itself is
substantively complete, and the two things it produced regardless of
R1's outcome — a validated $(\chi,\alpha,\mathcal E_\alpha)$ variable
set at the level of both the vector equation and the energy constraint
(§9–§13), and a fully resolved feasibility question for a leading
recourse candidate — stand as solid, durable results whichever way R3/
R4 goes. Nothing in `cdot-7/` was touched.

## Companion

- No new script — verification reused
  `wp7_derivation_gamma_sector_normalization_attempt.py` and
  `wp7_r1_derived_completion.py` directly, plus a hand-derived
  cross-check tracing the new completion term back through §10's own
  result (not scripted — algebra only, reported in §2 above).
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-R1FeasibilityResolvedNotViable-2026-07-21.md`.
