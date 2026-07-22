# Advisory — §10 Confirmed Exactly: the Worker Independently Reproduced the $\chi$-Independence Fix, Derived the Background EOM Identity Cleanly, and Showed the Residual's $\dot\varphi$ Piece Traces Exactly to $\Pi$'s Own $\gamma$-Term — With One Precise, Checkable Target Identified for What's Still Open (for `cdot-8/WP7/`)

*2026-07-21. Review of `Update-WP7-InstabilityRecourses-2026-07-21.md`
§10. Gate 1(b) and Gate 4 both carried. **Verdict up front: every
claimed result reproduces exactly, including the algebra connecting
them (checked by hand, not just by rerunning the script). This is
genuine, well-verified progress: the worker independently confirmed the
previous round's $\chi$-independence fix, cleanly derived an exact
background identity ($\ddot{\bar\phi}=-3Hc_\text{ad}^2\dot{\bar\phi}$,
not an approximation), and showed — not merely guessed — that the
residual's $\dot\varphi$-proportional piece matches $\Pi$'s own leading
$\gamma$-term exactly. One further, precise target is identified below
for the still-open piece: the residual currently carries *zero* net
$\Psi$-dependence, which requires $\Pi$'s own gradient (kap3-bracket)
piece to supply a specific, calculable $\Psi$-term that exactly cancels
the leading $\gamma$-term's own $-(2-\mathcal K_B)\dot{\bar\phi}\Psi$
piece — a sharp thing to check once $\Pi$ is derived, not an
open-ended one.**

---

## 1. Every claimed result reproduces exactly

Ran `wp7_derivation_coupled_variation_varphi_fixed.py` directly:

```
Residual (Pi excluded, after background-EOM substitution):
-3*K_B*H*alpha*cad2*phibardot + K_B*H*alpha*phibardot - K_B*varphi_dot
+ FY*alpha*phibardot**2 + FY*phibardot*varphi + 6*H*alpha*cad2*phibardot
- 2*H*alpha*phibardot + 2*varphi_dot

Pi's own leading gamma-term contribution: K_B*Psi*phibardot - K_B*varphi_dot
- 2*Psi*phibardot + 2*varphi_dot

varphi_dot piece of the residual: (2 - K_B)*varphi_dot
Matches (2-K_B)*varphi_dot from Pi's gamma-term exactly: True
```

**Checked the grouping by hand, not just trusted the printed
"True"**: the residual's terms regroup exactly into the three pieces
the write-up claims —
$(2-\mathcal K_B)\dot\varphi$ (from $-K_B\dot\varphi+2\dot\varphi$),
$F_\mathcal Y\dot{\bar\phi}\chi$ (from $F_Y\dot{\bar\phi}^2\alpha+
F_Y\dot{\bar\phi}\varphi=F_Y\dot{\bar\phi}(\dot{\bar\phi}\alpha+\varphi)
=F_Y\dot{\bar\phi}\chi$, using $\chi=\varphi+\dot{\bar\phi}\alpha$), and
$-(2-\mathcal K_B)(1-3c_\text{ad}^2)H\dot{\bar\phi}\alpha$ (from the
remaining four $\alpha$-proportional terms, which factor exactly to
$-(2-\mathcal K_B)H\dot{\bar\phi}\alpha[1-3c_\text{ad}^2]$ — verified
by direct algebraic expansion, not assumed). **All three match the
write-up's claimed decomposition exactly.**

## 2. The background-EOM identity is exact, not approximate — checked independently

Re-derived $\ddot{\bar\phi}=-3Hc_\text{ad}^2\dot{\bar\phi}$ from scratch
rather than accepting it: differentiating $a^3F_\mathcal Q=\text{const}$
gives $3a^2\dot aF_\mathcal Q+a^3F_{\mathcal Q\mathcal Q}\dot{\bar
{\mathcal Q}}=0$, i.e. $3HF_\mathcal Q+F_{\mathcal Q\mathcal Q}
\ddot{\bar\phi}=0$ (using $\bar{\mathcal Q}=\dot{\bar\phi}$ on FRW).
Combined with the primary source's own $c_\text{ad}^2\equiv F_\mathcal
Q/(\bar{\mathcal Q}F_{\mathcal Q\mathcal Q})$ (line 405, already
verified in an earlier round), $F_\mathcal Q/F_{\mathcal Q\mathcal
Q}=c_\text{ad}^2\dot{\bar\phi}$, giving $\ddot{\bar\phi}=-3Hc_\text{
ad}^2\dot{\bar\phi}$ exactly. **Confirmed: this is a genuine identity of
the theory's own background equations, not an approximation introduced
for convenience** — worth stating plainly since it's used to eliminate
$\ddot{\bar\phi}$ throughout.

## 3. $\Pi$'s $\gamma$-term match is a real, checkable confirmation, not a plausibility claim

Re-derived independently: $\Pi\supset c_\text{ad}^2\delta$, and
$\delta$'s leading $\gamma$-dependence (primary source line 436,
already verified) is $\delta\supset\frac{1+w}{\dot{\bar\phi}c_\text{
ad}^2}\gamma$, so $\Pi$'s leading contribution is $c_\text{ad}^2\cdot
\frac{1+w}{\dot{\bar\phi}c_\text{ad}^2}\gamma=\frac{1+w}{\dot{\bar\phi}}
\gamma$. Multiplied by the vector equation's own $(2-\mathcal K_B)
\dot{\bar\phi}/(1+w)$ prefactor on the $\Pi$-term gives exactly
$(2-\mathcal K_B)\gamma=(2-\mathcal K_B)\dot\varphi-(2-\mathcal K_B)
\dot{\bar\phi}\Psi$ — matching the script's own computation. **This is
a real structural confirmation**: the residual's $\dot\varphi$ piece
existing *at all*, with exactly this coefficient, is independent
evidence that the missing $\Pi$ contribution is genuinely the right
place to look, not merely the last remaining possibility by
elimination.

## 4. One precise target for what's still open, not yet stated this sharply

**Noticed something worth making explicit**: the printed residual has
**no bare $\Psi$ term at all** — every remaining piece is proportional
to $\alpha$, $\dot\varphi$, or $\varphi$, never $\Psi$ alone. But
$\Pi$'s own leading $\gamma$-term (§3 above) carries $-(2-\mathcal
K_B)\dot{\bar\phi}\Psi$, a genuine $\Psi$-dependent piece with **no
counterpart yet on the residual side**. Since the residual is supposed
to equal $\Pi$'s *full* contribution (once $\Pi$ is properly derived,
not just its leading $\gamma$-term), this is not simply "one more piece
to check" — it is a **precise, falsifiable prediction**: whatever
$\Pi$'s own gradient/$\kappa_3$-bracket piece turns out to be (from
$\nabla^2[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi]$, which
contains $\Psi$ directly through $\mathcal E_\alpha=\dot\alpha+\Psi$),
it must supply a term that cancels $-(2-\mathcal K_B)\dot{\bar\phi}
\Psi$ **exactly**, leaving zero net $\Psi$-dependence — matching the
residual's own current $\Psi$-coefficient of zero. This gives the next
derivation step (deriving $\Pi$'s $\kappa_3$-bracket piece from the
$0i$ constraint) a specific number to check against, rather than an
open-ended "does it work out."

## 5. Status and recommendation

Genuine, carefully verified progress on two fronts: mismatch (1) is now
mechanically resolved (confirmed twice, by two different people/
methods), and its remainder is now *shown*, not guessed, to trace to
$\Pi$'s momentum-constraint origin, with the exact background identity
needed to get there derived cleanly along the way. Recommending the
worker proceed to derive $\Pi$'s $\kappa_3$-bracket piece from the
$0i$ Einstein/momentum constraint next — the single remaining piece
this whole five-round sub-derivation (§5–§10) has been converging on —
using §4's $\Psi$-cancellation prediction as an immediate, sharp check
on whether that derivation is right. Gate 4 remains paused; this is
still diagnostic/derivation work informing a possible future recourse.
Nothing in `cdot-7/` was touched.

## Companion

- No new script — verification reused
  `wp7_derivation_coupled_variation_varphi_fixed.py` directly; §4's
  observation is a direct reading of its own printed residual, not a
  separate computation.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-PiGammaTermMatchConfirmed-2026-07-21.md`.
