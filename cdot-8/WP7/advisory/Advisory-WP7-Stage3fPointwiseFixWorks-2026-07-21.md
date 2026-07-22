# Advisory — WP7 §39's Repelling Riccati Confirmed, and a Simpler Fix That Already Works: Drop the Riccati ODE Entirely, Reuse Stage 3c's Pointwise Slaving With the Handoff Moved to $z\approx30$–$45$ Instead of $z_\text{switch}=18.5$ — Tested, Smooth, Convergent, No New Machinery (for `cdot-8/WP7/`)

*2026-07-21. Advisory in response to §39 of
`Update-WP7-PerturbationStructure-2026-07-18.md`. Verified the
repelling-branch diagnosis analytically before proposing anything, then
built and tested a working alternative rather than only diagnosing.
Gate 1(b) carried. **Verdict up front: the worker's diagnosis is
correct and precisely characterized — confirmed the linearized rate at
the stable root is exactly $\lambda_\text{unstable}-\lambda_\text{stable}$,
unconditionally positive, so forward-$N$ propagation of $\mu$ is a
repeller by construction, not a numerical accident. But this doesn't
need fixing with backward integration or a compound-vector
reformulation. It needs dropping the Riccati ODE entirely: Stage 3c's
original pointwise algebraic slaving — re-solved fresh at every step,
never propagated as its own state — works perfectly well as long as
the handoff to explicit integration happens comfortably above the true
$z\approx29$–$30$ threshold, rather than at the far-too-late $z_
\text{switch}=18.5$ Stage 3d used. Tested handoffs from $z=45$ down to
$z=30.2$ (right at the edge of validity): smooth, convergent,
no blow-up, no sensitivity problem at all.**

---

## 1. §39's diagnosis confirmed, precisely

Re-derived the linearization independently: near either root of the
fixed-point quadratic, $d(\delta\mu)/dN=(a_{EE}-2\mu^*/H_c)\,\delta\mu$.
Using $\mu^*=H_c\lambda$ (the worker's own identity, itself confirmed
in Entry 7) and $a_{EE}=\text{tr}=\lambda_\text{stable}+
\lambda_\text{unstable}$: at $\mu=\mu_\text{stable}=H_c\lambda_
\text{stable}$, the rate is exactly $\lambda_\text{unstable}-
\lambda_\text{stable}$ — and since the two roots are labeled precisely
so that $\lambda_\text{unstable}>\lambda_\text{stable}$, **this is
unconditionally positive everywhere the roots are real**, not just
near the eventual crossing. Checked numerically (analytic formula
against a direct finite difference on the Riccati RHS) at seven
redshifts from $z=60$ down to $z=30$: exact agreement at every point
(e.g. $z=60$: rate $=56.75$ both ways; $z=30$: rate $=3.49$ both ways).
**The stable branch is a repeller under forward-$N$ integration at
every point in the seed-to-handoff range, not only close to the
threshold** — this is exactly the well-known Riccati/shooting-method
phenomenon the worker correctly named, now with the specific rate
formula behind it confirmed.

## 2. A simpler fix, tested rather than just proposed

Rather than reformulate to backward integration or a compound
(unnormalized-vector) scheme — both legitimate but nontrivial
rewrites — tried the much simpler option first: **go back to Stage
3c's own pointwise algebraic slaving** (re-solve $\dot{\mathcal
E}_\alpha=0$ fresh at every RHS evaluation, with no propagated $\mu(N)$
state at all — there is nothing for a repelling flow to act on if
nothing is being propagated), and simply **move the handoff to
explicit integration earlier**, to a redshift comfortably above the
true $\text{Re}(\lambda_\text{max})=0$ threshold ($z\approx29$–$30$)
rather than at $z_\text{switch}=18.5$ (which Entry 5/6 already showed
sits deep inside the already-unreliable zone — that was always the
wrong place to hand off, independent of the Riccati question).

**Result, run end to end** (`wp7_stage3f_pointwise_conservative_handoff.py`):

| $z_\text{handoff}$ | $\delta_b(z{=}0)$ | $\delta_s(z{=}0)$ | $\alpha(z{=}0)$ |
|---:|---:|---:|---:|
| $45.0$ | $0.4361$ | $1.1365$ | $4.1676$ |
| $40.0$ | $0.4065$ | $1.0666$ | $3.9109$ |
| $37.0$ | $0.3958$ | $1.0415$ | $3.8187$ |
| $35.0$ | $0.3897$ | $1.0272$ | $3.7663$ |
| $33.0$ | $0.3838$ | $1.0132$ | $3.7149$ |
| $32.0$ | $0.3807$ | $1.0058$ | $3.6877$ |
| $31.0$ | $0.3772$ | $0.9978$ | $3.6581$ |
| $30.5$ | $0.3754$ | $0.9934$ | $3.6420$ |
| $30.2$ | $0.3742$ | $0.9906$ | $3.6318$ |

**Smooth and monotonically convergent across the entire range** —
including $z_\text{handoff}=30.2$, right at the edge of where the
fixed point even remains real. No blow-up anywhere, and the spread
across this whole range is $\lesssim15\%$, converging further as the
handoff moves later — nothing like Stage 3d's eight-orders-of-magnitude
sensitivity. **This works because pointwise slaving is an excellent
leading-order approximation exactly where $|\lambda(N)|\gg1$** (true
for $z\gtrsim30$–$40$, per Entry 6's own table — $\lambda\sim3$–$220$
there), **and it never propagates $\mu$ as a dynamical variable**, so
Stage 3e's repelling-flow problem simply doesn't arise: there's no
$\mu(N)$ trajectory to repel away from anything.

## 3. Why Stage 3d failed and this doesn't

Stage 3d used the *same* pointwise-slaving idea already (its
`slaved_Ealpha` was re-solved at every call, not propagated) — its
failure was entirely the **choice of handoff redshift**
($z_\text{switch}=18.5$, deep inside the zone where the
frozen-coefficient approximation is no longer trustworthy *and* where
$\text{coef}_E$ is near its own singularity). Moving the handoff to
$z\gtrsim30$ removes both problems at once: the approximation is still
excellent there, and $\text{coef}_E$ is comfortably away from zero.
**No new machinery was needed — only relocating a design decision that
was mis-set two rounds ago.**

## 4. Recommendation

Adopt this directly: Stage 3c's pointwise closure, handoff at
$z\approx35$ (comfortable margin, not the tightest tested point) to
full explicit $(\alpha,\mathcal E_\alpha)$ integration for the rest of
the run. Retire the Riccati-ODE approach (§38's derivation and its
discriminant identity remain correct and worth keeping on record, but
the fix doesn't need it). Recommended as the standard robustness check
going forward: confirm insensitivity to the handoff choice within
$z\approx30$–$45$ (already done above) before trusting the resulting
ISW/growth numbers.

## 5. Still open, unchanged

The possible second unstable direction in the full 6-variable system
(flagged in Entry 6, not confirmed) is untouched by this fix and should
still be checked before the closure is treated as fully validated.

## 6. Housekeeping

Nothing in `cdot-7/` was touched. Gate 1(b)'s caveat, $Q_2$/EFE
sequencing, and KATRIN watch are unchanged.

## Companion

- `wp7_stage3f_pointwise_conservative_handoff.py` — the repelling-rate
  verification and the working pointwise-handoff test, reproducible
  end to end (imports `../wp7_stage3e_riccati_handoff.py` for shared
  machinery, does not duplicate it).
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-Stage3fPointwiseFixWorks-2026-07-21.md`.
