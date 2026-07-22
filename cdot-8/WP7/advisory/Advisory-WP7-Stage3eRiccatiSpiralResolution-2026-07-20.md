# Advisory — WP7 §38's Complex-Riccati Gap Doesn't Need a Complex-Riccati Fix: in the Spiral Zone Every Real Direction Shares the Same Growth Envelope, So Hand Off Once (at $z\approx29$–$30$, Not $z_\text{switch}=18.5$) and Integrate Explicitly the Rest of the Way — No Third Regime, No Matrix Generalization Needed (for `cdot-8/WP7/`)

*2026-07-20. Advisory in response to §38 of
`Update-WP7-PerturbationStructure-2026-07-18.md`. Independently
re-derived the Riccati equation and the discriminant-proportionality
claim from scratch before treating either as established; both check
out exactly. Gate 1(b) carried. **Verdict up front: the worker's find
is real and correctly reasoned — a real-valued Riccati slope literally
cannot exist through the $z\approx18.5$–$29.5$ spiral zone, confirmed
independently and algebraically (the slope-quadratic's discriminant is
exactly $H_c^2$ times the original Jacobian's own discriminant, so they
vanish at the same point, not approximately). But this doesn't need a
complex- or matrix-Riccati generalization to fix. In a spiral (complex
eigenvalue) regime, every real direction grows at the same envelope
rate $\text{Re}(\lambda)$ — there is no preferred direction left to
project onto or away from. The practical fix is simpler than the
question implies: track the real Riccati only as far as it's real
($z\gtrsim29$–$30$), hand off there once, and integrate $(\alpha,
\mathcal E_\alpha)$ explicitly for everything below — covering both
the spiral-unstable and the later genuinely-stable zone in one
continuous phase, with no special handling needed at
$z_\text{switch}=18.5$ at all.**

---

## 1. §38 endorsed and independently re-derived, not just accepted

Wrote out the Riccati construction from scratch ($\mathcal E_\alpha=
\mu\alpha+\nu$, substituted into both the true $\dot{\mathcal
E}_\alpha$ equation and $\dot\alpha=(\mathcal E_\alpha-\Psi)/H_c$,
matched coefficients) before trusting the worker's version: get
$$\mu'=a_{EE}\mu+a_{E\alpha}-\mu^2/H_c,\qquad a_{EE}\equiv\frac{
\partial\dot{\mathcal E}_\alpha}{\partial\mathcal E_\alpha},\quad
a_{E\alpha}\equiv\frac{\partial\dot{\mathcal E}_\alpha}{\partial\alpha}$$
— matches §38's equation exactly, with the frozen-coefficient
($\mu'=0$) fixed point recovering the naive algebraic slaving, as
claimed.

**Checked the discriminant claim algebraically, independent of any
specific numbers**: the fixed-point quadratic is $\mu^2-H_ca_{EE}\mu-
H_ca_{E\alpha}=0$, discriminant $D_\mu=(H_ca_{EE})^2+4H_ca_{E\alpha}$.
The original $2\times2$ Jacobian $J=\big[\begin{smallmatrix}0&1/H_c\\
a_{E\alpha}&a_{EE}\end{smallmatrix}\big]$ has $\text{tr}=a_{EE}$,
$\det=-a_{E\alpha}/H_c$, discriminant $D_J=a_{EE}^2+4a_{E\alpha}/H_c$.
**Directly: $D_\mu=H_c^2D_J$ exactly** — confirmed both symbolically
and numerically (e.g. at $z=29.5$: $D_J=+1.246$, $D_\mu=+11751$,
ratio $=9433.9=H_c^2$ to 5 figures; at $z=29.0$: $D_J=-9.155$,
$D_\mu=-82213$, ratio $=8979.8=H_c^2$). Since $H_c^2>0$ always, $D_\mu$
and $D_J$ share a sign and a zero **identically**, not approximately —
the real Riccati slope's own domain of existence is, exactly, the
domain where the original $2\times2$ system has real eigenvalues.
**The worker's finding is correct and precisely located** ($z\approx
29$–$30$, matching the discriminant bracketing from Entry 5's own
table to the same precision).

## 2. Why this doesn't need a complex/matrix generalization

A real $2\times2$ system with a complex eigenvalue pair
$\lambda=\text{Re}\pm i\,\text{Im}$ has **no preferred real
eigendirection** — every real initial vector, decomposed in the
complex eigenbasis, generically has comparable weight on both
conjugate eigenvectors (a real vector's projections onto a
conjugate pair are themselves complex conjugates), so **every real
solution grows with the same envelope $e^{\text{Re}(\lambda)N}$**,
differing only in oscillation phase, not in growth *rate*. This is
exactly why the Riccati slope $\mu$ (which encodes "which single
direction to select as the non-growing one") stops making sense there:
in a spiral, there is no non-growing direction to select — the
"eliminate the fast mode, keep the slow direction" logic that
motivated the whole construction simply has nothing left to act on
once the eigenvalues merge and rotate off the real axis. **The
$z\approx18.5$–$29.5$ zone doesn't need a fancier elimination method —
it needs no elimination at all**, for the same reason $z<18.5$
doesn't: there's a genuine 2D dynamical system there, not a
1D-stable-plus-1D-unstable split to reduce.

## 3. The resolution: one handoff, not three regimes

1. **$z\gtrsim29$–$30$** (real Riccati slope well-defined): evolve
   $\mu(N),\nu(N)$ from a deep-$z$ ($z\gtrsim60$) seed where the naive
   frozen-coefficient slaving is already an excellent approximation
   (removing the $z=100$ guesswork), down to the edge of $\mu$'s own
   reality ($D_\mu=0$, $z\approx29$–$30$). This is where the correct,
   selected $(\alpha,\mathcal E_\alpha)$ at that redshift comes from —
   not from a fixed algebraic formula applied blindly, and not from an
   arbitrary $z=100$ guess.
2. **Hand off exactly once**, at $z\approx29$–$30$, to full **explicit**
   integration of $(\alpha,\mathcal E_\alpha)$ — no reduction, no
   slaving, no switch criterion needed for the rest of the run at all.
   This single explicit phase covers *both* the growing-spiral zone
   ($18.5\lesssim z\lesssim29$–$30$) *and* the genuinely stable zone
   ($z\lesssim18.5$) continuously — $z_\text{switch}=18.5$ stops being
   a special numerical point altogether; it's just wherever
   $\text{Re}(\lambda)$ happens to cross zero *inside* an already-valid
   explicit-integration phase, no different from any other smoothly
   varying background quantity.
3. **Why this fixes the margin-sensitivity, not just relocates it**:
   the previous approach's extreme sensitivity came from arbitrarily
   mismatching the *strongly growing* real eigenmode at $z=100$
   ($\lambda\sim221$, i.e. a mismatch amplified by $e^{221\Delta N}$
   over many e-folds of real growth before even reaching the
   spiral zone). Handing off correctly at $z\approx30$ instead means
   entering the spiral zone with the properly-selected (small)
   residual; the subsequent growth there is the *same, universal*
   $e^{\int\text{Re}(\lambda)\,dN}$ factor regardless of which small
   residual you enter with — a fixed, computable amplification, not an
   arbitrarily-sensitive one.

## 4. Recommended verification

Implement exactly this two-phase design (Riccati to $z\approx30$, then
one explicit integration to $z=0$) and run the **same kind of
robustness check already used**, but on the *right* parameter this
time: vary the handoff redshift within the region where $\mu$ is still
comfortably real (e.g. $z=35,32,30.5,29.8$) and confirm $\delta_b,
\delta_s,\alpha$ at $z=0$ converge/are insensitive — this replaces the
previous, ill-posed "margin before $z_\text{switch}=18.5$" scan with a
well-posed one (varying a handoff point *inside* a region of genuine
validity, rather than straddling a location that was never the right
transition to begin with).

## 5. Still open, unchanged

The possible second unstable direction in the full 6-variable system
(flagged last round, not confirmed) is untouched by this — recommend
it still be checked (with a properly-scaled or symbolic Jacobian,
not a hasty finite difference) before treating the two-phase design
above as the complete answer, since a second growing direction would
need its own selection condition alongside $\mu$'s.

## 6. Housekeeping

Nothing in `cdot-7/` was touched. Gate 1(b)'s caveat, $Q_2$/EFE
sequencing, and KATRIN watch are unchanged.

## Companion

- No new standalone script — the discriminant-proportionality check
  reused `wp7_stage3_vector_stiffness_audit.py`'s Jacobian directly;
  shown inline above.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-Stage3eRiccatiSpiralResolution-2026-07-20.md`.
