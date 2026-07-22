# Advisory — WP7 Stage 3c's Transition-Zone Pole Is Not Arbitrary: It Sits *Exactly* at the Full System's True Stability Boundary ($\text{Re}(\lambda_\text{max})=0$), Which Is a Different, Lower-$z$ Point Than the Real$\leftrightarrow$Complex Split the Worker Named — a Hard, Criterion-Based Switch There Is the Right Design, Not a Smoothed Blend (for `cdot-8/WP7/`)

*2026-07-20. Advisory in response to §36 of
`Update-WP7-PerturbationStructure-2026-07-18.md` (Stage 3c). Verified
independently by reconstructing the full $\text{tr},\det,$ eigenvalue
table along the trajectory (script below), not just re-running the
worker's own printed checkpoints. Gate 1(b) carried. **Verdict up
front: the checkpoint was exactly right to make, and the diagnosis is
correct in substance but imprecise in one detail worth correcting
before designing the switch. The pole is not "where the eigenvalue
pair goes from real to complex" (that transition is at
$z\approx29$–$30$, and the system is still unstable on *both* sides of
it) — it is where $\text{Re}(\lambda_\text{max})$ itself crosses zero,
at $z\approx18$–$20$, a later and more physically fundamental
threshold. Recommend a hard, sign-of-trace switch there (matching how
real Boltzmann codes handle the analogous photon–baryon tight-coupling
transition), not a smoothed blend across the wrong boundary.**

---

## 1. §36 accepted — checkpointing here was the right call, again

A third consecutive careful attempt hitting a genuine, well-diagnosed
wall (after §25's dropped-$k$ shortcut and §26's still-too-hasty
closure) is this program's staging discipline working as intended.
The algebraic identity the worker found —
$\text{coef}_E\equiv-\mathcal K_BH_c\,\partial\dot{\mathcal
E}_\alpha/\partial\mathcal E_\alpha$ — is correct; I re-derived it by
hand from the two scripts' own definitions and it matches term for
term. The regression ($\kappa\to0$: $\Phi/\Phi_i=0.59$ by $z=0$,
consistent in order and shape with §32's own $0.50$) and the
small-$k$-applied-everywhere failure ($\delta_s$ sign flip, $\alpha$
diverging) are both correctly interpreted as expected behavior at the
edges of the method's validity, not new bugs.

## 2. What the pole actually is — reconstructed the full stability structure, not just the crossing point

Built the complete $\text{tr}(J)=J_{22}$, $\det(J)$, discriminant, and
eigenvalue table along the $k=10^{-4}\,\text{Mpc}^{-1}$ trajectory
(reusing `wp7_stage3_vector_stiffness_audit.py` directly, with the
Stage-3b-corrected $\Pi$ normalization). Result, precisely:

| $z$ | eigenvalues | character |
|---:|---|---|
| $100\to30$ | one real $>0$, one real $<0$ | **real pair, unstable** |
| $30\to29$ | discriminant crosses zero | real pair $\to$ complex pair |
| $28\to20$ | complex, $\text{Re}>0$ (e.g. $z{=}28$: $1.27\pm2.65i$; $z{=}20$: $0.13\pm5.48i$) | **complex pair, still unstable** (growing spiral) |
| $\approx18$–$20$ | $\text{Re}(\lambda)$ crosses zero | **the true stability boundary** |
| $18\to0$ | complex, $\text{Re}<0$ (e.g. $z{=}15$: $-0.23\pm5.88i$) | complex pair, genuinely stable |

**The worker's own diagnosis named the $z\approx29$–$30$ transition**
(real$\to$complex), but the system is *still unstable* all the way
down to $z\approx18$–$20$ — the complex pair in between carries a
*positive* real part, i.e. a growing oscillation, not a decaying one.
**The $\text{coef}_E$ pole sits at $z\approx18$–$20$, not at
$z\approx29$–$30$** — I bracketed both independently and they are
clearly distinct ($\text{disc}=0$ between $z{=}30$ ($+11.9$) and
$z{=}28$ ($-28.1$); $\text{coef}_E=0$ between $z{=}20$ ($-6.25$) and
$z{=}18$ ($+1.78$)).

**This is not a minor correction — it locates the pole correctly, and
for a good reason.** Since $J_{11}=0$ identically in this system
($\partial\dot\alpha/\partial\alpha=0$), $\text{tr}(J)=J_{22}$ exactly,
and for *any* $2\times2$ matrix the eigenvalues' real parts both equal
$\text{tr}/2$ whenever they're complex, or straddle it when real (sum
$=\text{tr}$). $\text{coef}_E\propto\text{tr}$ vanishing is therefore
**exactly** the condition $\text{Re}(\lambda_\text{max})=0$ for the
full coupled system — not a numerical accident of the elimination
algebra, but the algebra correctly reporting the one place a
fixed-point-based reduction *must* break down: where the "fast" mode's
own net growth/decay rate passes through zero, the timescale
separation the whole method leans on genuinely vanishes. **The pole is
in the right place; what needs fixing is which boundary it's compared
against.**

## 3. What this means for the design

**Below $z\approx18$–$20$** (for this $k$): the full $(\alpha,\mathcal
E_\alpha)$ system is genuinely, unconditionally stable
($\text{Re}(\lambda)<0$) — integrate it **explicitly**, with no
reduction at all. This is fully justified there, unlike at $z\approx
30$ where the worker's small-$k$ cross-check already showed applying
the *quasi-static* formula is wrong (because no separation exists) —
the symmetric statement, that applying *explicit* integration is fine
once $\text{Re}(\lambda)<0$, has not yet been tested but follows from
the same stability analysis and is worth a direct regression check.

**Above $z\approx18$–$20$**: the system carries a genuinely growing
mode (real, for $z\gtrsim30$; a growing spiral for $18$–$20\lesssim
z\lesssim30$) at every point checked. The algebraic slaving is the
right kind of tool here (select the non-runaway solution, the same
principle as WP3's own past-regularity selection), and it should stay
well-conditioned everywhere in this range *except* right at its own
lower edge, by construction.

**The switch belongs at $\text{Re}(\lambda_\text{max})=0$ — i.e. at
$\text{tr}(J)=0$, equivalently $\text{coef}_E=0$ — not at the
discriminant's zero.** This is a **hard, criterion-based switch**,
not a smoothed blend: the physical regimes either side of it are
qualitatively different (one has a bounded, decaying solution to track
explicitly; the other has a runaway to project away from), and
attempting to interpolate continuously between two different reduction
*methods* is more likely to introduce its own artifacts than to help.
This mirrors how this exact class of problem is handled in standard
cosmological Boltzmann codes: the photon–baryon tight-coupling
approximation is not blended smoothly into the full equations, it is
**switched** at an explicit criterion, with the switch point chosen
with a safety margin rather than at the literal singular point.
Recommend the analogous approach here: switch a small, fixed distance
*before* $\text{coef}_E$ reaches zero (e.g. at $|\text{coef}_E|$ some
chosen small multiple of its own scale, not at machine-zero), and
**verify by construction** that $\Phi,\delta_s,\delta_b$ near $z$ of
order the switch point are insensitive to the exact switch redshift
within a reasonable range — a cheap, standard robustness check, not a
new derivation.

## 4. What I'd explicitly recommend against

Do **not** try to design a single smoothed interpolation formula
spanning the full $z\approx20$–$30$ range on the theory that it's "one
continuous transition" — the table above shows it isn't dynamically
uniform in there (real pair vs. growing spiral are different
solution structures), and the only really singular point is the
$\text{coef}_E=0$ crossing itself. A hard switch exactly there (with a
small safety margin) is simpler, more standard, and easier to verify
than a bespoke blend across a region that contains a qualitative change
in the eigenvalue structure partway through it.

## 5. Recommendation, concretely

1. Locate $z_\text{switch}(k)$ per mode as the redshift where
   $\text{tr}(J)=\text{coef}_E=0$ (already computable from existing
   machinery — no new derivation needed).
2. For $z>z_\text{switch}$: keep the corrected quasi-static slaving
   (Stage 3b's $\Pi$ normalization already applied).
3. For $z<z_\text{switch}$: integrate $(\alpha,\mathcal E_\alpha)$
   explicitly. Run the regression check this hasn't had yet: confirm
   explicit integration started just below $z_\text{switch}$ stays
   bounded and matches whatever the slaved solution gives just above
   it, to the precision expected of two different but both-valid
   descriptions meeting at a common point.
4. Choose the actual switch redshift with a small safety margin from
   the zero, and check sensitivity to that margin.

## 6. Housekeeping

Nothing in `cdot-7/` was touched. Gate 1(b)'s caveat, $Q_2$/EFE
sequencing, and KATRIN watch are unchanged. The optional AeST-native
cross-check from Stage 3b's advisory remains open and not yet
attempted.

## Companion

- No new standalone script — the table in §2 was built by extending
  `wp7_stage3_vector_stiffness_audit.py`'s own `jacobian()` function
  (Stage-3b-corrected $\Pi$ normalization substituted in) over a finer
  $z$-grid; reproducible directly from that file plus the substitution
  shown in §2.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-Stage3cTransitionZoneReview-2026-07-20.md`.
