# Update — WP3: Third-Escalation Resolution, Checked and Consolidated

*Companion: `SessionLog-2026-07-12.md` (this directory), Entry 5. Consolidates
`cdot-8/proposal/Advisory-WP3-InverseReconstruction-2026-07-12.md` (new stand-in
agent) and `cdot-8/proposal/Addendum-ThirdEscalation-Assessment-2026-07-12.md`
(original proposer's audit of the stand-in) against this session's own independent
re-derivation — not a rubber stamp of either. One additional caveat found in that
process, not raised by either prior document, is recorded in §4.*

---

## 1. What was independently re-verified, and how

**The labeling-bug diagnosis** (Foundation §5.5's quoted "$\hat a_0(z)/\hat a_0(0)$"
values are actually absolute $\hat a_0(z)$ in $10^{-10}$ m/s², not ratios): checked
directly against `cdot-7/Foundation.md` source, not just the advisory's script.
Line 869 does explicitly label the equation as a ratio. But the same section's own
figure (lines 895–902) plots this quantity *directly against* MUSE-DARK's and
MIGHTEE-HI's absolute measurements ($2.38\times10^{-10}$, $1.69\times10^{-10}$ m/s²)
on what the caption describes as one consistent axis — a comparison that is only
coherent if Foundation's own numbers are *also* absolute, since a dimensionless ratio
and a $10^{-10}$-m/s² quantity cannot be plotted on the same axis without conversion.
Combined with the advisory's quantitative check (quoted/true-ratio $=1.385$–$1.386$
across all four points — matching the fit's own $a_0(0)=1.39\times10^{-10}$ anchor to
three digits, not a loose coincidence), **this is confirmed independently, not merely
accepted.**

**The exact identity $\hat a_0=\tfrac23\lambda c_0H_\tau$**: re-derived from scratch
(not run from either script) using only already-established results — $a_0=\lambda
\dot c$ (coordinate definition), $H_t=\tfrac32\dot c/c$ (WP1, exact from the redshift
law alone), the acceleration Planck-unit exponent $7/2$ (dimensional analysis: length
exponent $-3/2$, time exponent $-5/2$, acceleration $=$ length/time$^2$
$\Rightarrow-\tfrac32-2(-\tfrac52)=\tfrac72$), and $H_\tau=H_t(c/c_0)^{-5/2}$ (the
two-clock dictionary). Checked algebraically at five arbitrary values of $c/c_0$ (0.5
to 2.0, not just today or the fixed point) — **holds exactly at every point, confirming
it is a genuine identity of the framework's kinematics, not a fixed-point-specific
coincidence.**

**The premise correction** (F_Q\propto a^{-3}$ is the *free*, shift-symmetric AeST
scalar equation of motion — exactly the dynamics M5 exists to modify, not a
model-independent fact independent of sourcing): accepted as conceptually sound. WP0's
own extraction already noted this conservation law follows from the Lagrangian
depending on $\phi$ only through $Q=\dot\phi$ (and $Y$) — a shift symmetry. A genuine
Machian constraint tying $Q_0(t)$ to the nonlocal census $\mathcal N(t)$, implemented
honestly at the action level, generically requires $\phi$ (or its cosmological zero
mode) to couple to an externally-given function of time — which breaks that shift
symmetry by construction. This session's own earlier `Update-WP3-InverseReconstruction`
used the free conservation law unconditionally; that was the error, correctly
diagnosed.

---

## 2. One additional caveat, not raised by either prior document

M1's identification "$\phi=t_\text{coord}$" (used to get $Q=A^\mu\nabla_\mu\phi=dt_
\text{coord}/d\tau=(1+z)^{5/3}$) is dimensionally awkward as stated: $Q$ must carry
acceleration-adjacent dimensions (it is "the carrier of $\dot c$," an acceleration, per
M2), while $dt_\text{coord}/d\tau$ is a dimensionless ratio of two times. Either (a) an
implicit dimensionful conversion constant is being absorbed into $\lambda$ or a similar
parameter (harmless for every *shape*/exponent comparison made here, since an overall
constant does not affect $F\propto Q^{9/5}$-type ratios), or (b) the identification
needs an explicit dimensionful anchor stated alongside it. This does not appear to
change any conclusion in §3 below (all comparisons are shape/exponent comparisons,
insensitive to an overall constant), but it should be stated explicitly, not silently
absorbed, when M5 is actually implemented at the action level (directive 1 below) —
folded into the addendum's own Flag 3 (state the aether normalization convention
explicitly) as one further thing to pin down at the same time.

---

## 3. Verdict

With the free-vs-sourced premise corrected and the labeling bug accounted for, the
shape mismatch this session found in `Update-WP3-InverseReconstruction-2026-07-12.md`
dissolves: a genuine $F(Q)$ exists by quadrature (guaranteed for any monotonic $Q(a)$,
up to a zero-density gauge piece), and with $Q$ identified via M1, the reconstructed
$F(Q)$ has a clean, geometrically-motivated form — the census-constrained shift current
departs from free conservation by exactly one power of the two-clock lapse
($a^3F_Q\propto d\tau/dt$, vs. free conservation's $a^3F_Q=\text{const}$) — not a
curve-fit. **The kill condition does not trigger.** WP3's remaining, sharper form
(per the stand-in advisory, endorsed): implement M5 at the action level and check
whether the resulting equation of motion actually produces this single-lapse-factor
source — a zero-freedom success criterion, since the demanded answer is now known in
advance.

---

## 4. Carried forward, per both advisory documents (accepted as directed)

- **Sub-item 1b (stability)**: the reconstructed $F$ has $(F-QF_Q)$ changing sign
  (positive matter era, small-negative radiation era) — confirmed present in
  `budget_invoice.py`'s own output (rho_s/u goes from $+3.45$ at $z=20$ to $-0.068$ by
  $z=5\times10^5$). A zero-crossing sits exactly where WP0's stability caveats (the
  $k<\mu$ non-propagating mode) need re-examination on this branch specifically, not
  assumed benign by analogy to AeST's own (different) cosmological branch. Carried
  as a required check alongside the action-level M5 implementation, not resolved here.
- **State the aether/frame normalization convention explicitly** before deriving the
  modified equation of motion (addendum Flag 3, extended by §2's dimensional caveat
  above).
- **Zero-freedom success criterion, exact wording**: "...no adjustable function, up to
  the additive $CQ$ gauge piece (zero energy density, total derivative)" (addendum §6).

---

## 5. Corrections issued to this session's own prior documents

`cdot-8/WP1/Update-WP1-Addendum-TwoClockDictionary-2026-07-12.md` §5(c) compared the
fixed-point $(1+z)^{3/2}$ law against Foundation §5.5's mislabeled values, reporting
ratios $1.10,0.93,0.91,0.87$ ("reasonably close"). Using the true fitted ratios
($1.22,1.70,1.86,2.38$), the correct fixed-point/fitted ratios are
$1.26,1.48,1.52,1.60$ — a real, growing suppression, **not** the earlier "reasonably
close" reading. The qualitative direction (fitted values increasingly suppressed
below the pure fixed-point law at higher $z$) survives and is in fact sharper than
originally reported; the specific numbers were wrong. Corrected in place in that
document, citing this one as the source of the fix.
