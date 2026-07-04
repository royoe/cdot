# T10 — Galaxy Size Evolution

*Checked carefully against the counting-law change (Core Principles §1). Result: this
document's prediction was already **withdrawn in cdot-4**, and for a premise-3 reason
(invariant $G$ removes the orbital-expansion driver, T8/T9) entirely unrelated to
premise 2's counting law. cdot-5's counting-law revision gives no route to revive it —
verified below, not merely assumed by carrying the withdrawal forward unexamined.*

## Observational Background

High-redshift galaxies observed in deep imaging surveys (HST, JWST, and ground-based
adaptive optics) are systematically **smaller** than local galaxies of the same
stellar mass. This size evolution is one of the most striking and robustly established
results in observational galaxy evolution.

### The observed scaling

For early-type (elliptical/lenticular) galaxies:
$$r_e\propto(1+z)^{-1.5\pm0.3}$$
(effective radius shrinks by a factor of $\sim(1+2)^{1.5}=2.6^{1.5}\approx4$ from $z=2$
to today for early types).

For late-type (spiral/disk) galaxies:
$$r_e\propto(1+z)^{-0.75\pm0.2}$$
(less extreme evolution; spirals at $z=2$ are roughly $(1+2)^{0.75}\approx2.3$ times
smaller than today).

These results are from large surveys (COSMOS, CANDELS, 3D-HST, UltraVISTA, EGS) and are
generally agreed upon, though the precise exponent depends on the selection criterion
(fixed stellar mass, fixed number density, fixed luminosity).

### Interpretation in $\Lambda$CDM

In the standard picture, galaxy size evolution is driven by:
1. **Mergers:** dry (gas-poor) major and minor mergers deposit material in the
   outskirts of galaxies, puffing them up.
2. **Adiabatic expansion** (mass loss from stellar winds and supernovae).
3. **Initial conditions:** high-$z$ galaxies formed from higher-density environments
   when the universe was smaller.

The $\Lambda$CDM picture can reproduce the observed trends with simulations
(IllustrisTNG, EAGLE, etc.) but the physical mechanisms, their relative contributions,
and their comparison to the data are still actively discussed.

---

## The Former Prediction, and Why It Is Withdrawn

### The historical derivation (cdot-3, superseded)

The original version of this model (cdot-3) predicted galaxy size evolution from
orbital expansion: with $G\propto c^{-2}$, orbits were claimed to expand as
$r\propto c^2$ (cdot-3 Core Principles §6, T9), and the same argument was applied to
any gravitationally bound system, including a galaxy's stellar orbits. Since
$c/c_0=(1+z)^{-1/2}$ (squared redshift law): $r\propto c^2\propto(1+z)^{-1}$, giving
$r_e\propto(1+z)^{-1}$ — a parameter-free prediction bracketing the observed range
between late types ($-0.75$) and early types ($-1.5$).

### Why it is withdrawn (T8/T9, premise 3 — not premise 2)

The withdrawal has nothing to do with the cosmological counting law. It follows
directly from T8's central result: Lunar Laser Ranging refutes $G\propto c^{-2}$ by a
factor of $\times720$ (self-consistent computation, T8), forcing the adoption of
**invariant $G$** ($G\propto c^0$) from cdot-4 onward. Under invariant $G$ with
invariant mass, T9 derives $r=L^2/(m^2GM)=\text{const}$: orbits are static, full stop —
there is no $c$-dependence left in the orbital radius formula at all, for *any*
gravitationally bound system, galaxies included. The prediction $r_e\propto(1+z)^{-1}$
is not weakened or revised; its entire mechanism (orbits expanding as $c$ grows) is
removed at the root. **No advantage is claimed**: the observed compactness of
high-$z$ galaxies is not offered as model support, and is left to $\Lambda$CDM's own
explanations (mergers, formation conditions, adiabatic expansion).

### Verified: cdot-5's counting-law change does not revive this

T8 and T9 were independently re-examined for cdot-5 (see those documents) and both
confirmed **fully unaffected** by the premise-2 revision — the LLR $\times720$ result
and the static-orbit derivation depend only on premise 3 (invariant $G$, invariant
mass) and a present-day rate ($H_0^\text{hor}$) that is identical under both counting
laws. There is no route by which replacing occupancy counting with connectivity
counting reopens orbital expansion: the driver was always $G\propto c^{-2}$, which
remains refuted for reasons entirely independent of how $c(t)$'s cosmological history
is generated. This prediction stays withdrawn in cdot-5, for exactly the reason it was
withdrawn in cdot-4.

### No mergers required — advantage not claimed

As in cdot-4: the "no mergers required" feature that cdot-3 claimed as an advantage
(passive, universal size evolution driven by orbital expansion, no need for a
merger-rate model) is not available in either cdot-4 or cdot-5, since the underlying
mechanism does not exist under invariant $G$.

---

## JWST and the Compact Galaxy Puzzle

JWST observations have revealed large numbers of massive, compact galaxies at $z>3$
(and even $z>6$), some with stellar masses comparable to modern ellipticals but sizes
$\sim5$–$10$ times smaller. In $\Lambda$CDM, forming such massive compact systems so
early requires very high star-formation efficiencies and is challenging for standard
models. The withdrawn cdot-3 prediction ($6\times$ smaller at $z=5$) is **not** claimed
as an explanation for this in either cdot-4 or cdot-5 — it would require the
now-refuted orbital-expansion mechanism. JWST compact galaxies are not evidence for or
against this model on this front.

---

## Caveats

The primary issue is not any of the secondary caveats below — the prediction itself is
withdrawn because its $G\propto c^{-2}$ foundation is ruled out (T8), independent of
the counting law. The five secondary caveats from cdot-3 (morphological transformation
via dynamical selection T17; initial conditions; selection effects at fixed mass vs.
luminosity vs. number density; half-light vs. half-mass radius; range of dynamical
structures at formation) are retained here for historical completeness only — none is
live in cdot-4 or cdot-5, since there is no baseline orbital-expansion prediction left
for them to modify.

---

## Open Questions

All four questions, as in cdot-4, reduce to one: **what, if anything, does this model
predict for galaxy size evolution without an orbital-expansion mechanism?**
1. No quantitative comparison is possible without a mechanism; this is the standing
   gap, unaffected by cdot-5's premise-2 change.
2. Scatter in $r_e$: whether the model has anything to say about it without orbital
   expansion — no, not currently, under either counting law.
3. Morphology dependence: T17's disk-stripping consequences (dynamical selection) do
   not need a cosmological orbital-expansion baseline to operate — they are a separate,
   premise-3-and-T14-based mechanism (velocity-threshold ejection) that could in
   principle speak to morphology-dependent compactness on its own, independent of this
   document's now-dead baseline. Not computed.
4. Surface brightness: the $\Sigma=\text{const}$ prediction depended on both
   $r\propto c^2$ and the old $L_\text{lum}\propto c^4$ luminosity scaling (T18, since
   corrected to $L_\text{lum}\propto c^0$) — both ingredients are gone, so this
   prediction is withdrawn along with the rest, for the same premise-3 reasons.
