# Update — WP3 Step 5: The Razor Passes by Construction, but the $(C_2,\Lambda_M)$ Invariance Audit Finds a Genuine, Unfixed Free Parameter

*Companion: `SessionLog-2026-07-13.md` (this directory), Entry 17. Executes the
full step-5 ledger cleared by `Advisory-WP3-MagnitudeCorrectionConfirmed-
2026-07-13.md` §4: the acceleration-equation channel, total-Bianchi closure, the
razor, and the $(C_2,\Lambda_M)$ invariance audit — the item every round since
the fourth escalation has named as "the last unexamined slot." Three of four
close cleanly. The fourth does not, and the finding is reported precisely rather
than resolved by assumption, per this program's standing discipline.*

---

## 1. The acceleration-equation channel — derived and verified

Following the advisory's named ledger item (§1 of the confirmed-correction
advisory: $g_i$'s $\dot a$-dependence puts the census sector into the
acceleration equation, not just the Hamiltonian constraint), varied $S_{\mathcal
N}+S_{R_h}$ w.r.t. $a(t)$ via the standard "treat $a,\dot a$ as independent
inputs" Euler–Lagrange check (same style as the closed-action verification,
*not* hand algebra alone). Result:
$$\text{EL}_a^{(\mathcal N,R_h)}=\frac{d}{dt}\!\left[-\frac23\frac1a\sum_i
\Big(p_i^\text{sp}-\tfrac52\Big)\pi_i\right]-\left[-\frac23\frac{c}{aR_h}N
\sum_i\pi_i+\frac23\frac{\dot a}{a^2}\sum_i\Big(p_i^\text{sp}-\tfrac52\Big)\pi_i
-\frac23\frac ca Np_R\right],\quad\pi_i\equiv p_i\mathcal N_i.$$
Verified against a nested finite-difference check on synthetic (non-physical)
test functions, converging to $\sim10^{-7}$ relative residual as the step size
is refined (checked $h=10^{-3},10^{-4},10^{-5}$; the naive $h=10^{-6}$ single-pass
check showed $\sim10^{-4}$ noise from second-derivative amplification, resolved
by the convergence sweep — the same kind of care the $\dot s$-normalization
episode showed is necessary whenever a derivation crosses more than one
time-derivative). This closes the named ledger item.

## 2. Total-Bianchi closure — structural, not a new numerical result

Every individual equation of motion in the closed action ($N$-variation,
$R_h$-variation, $\mathcal N_i$-variation, the $a$-variation above, the
$\phi$/M5 sector) has now been independently derived and verified against a
solved or synthetic system. For a generally covariant (reparametrization
invariant) action, the Bianchi identity — equivalently, that the time-derivative
of the Hamiltonian constraint is implied by the other equations of motion — is a
mathematical consequence of that covariance, not a separate physical input.
**This is not claimed as a new, independently-checked result**: it is the
correct conclusion to draw from having verified every piece individually, and
is stated as such rather than manufactured into an additional numerical
"triumph" it would not be.

## 3. The razor — passes, but only in a sense that turns out not to be the real test

The razor's original form (form (i)/(ii)/(iii) of the TouchPoint advisory:
$a^3F_Q\propto N$, equivalently the corrected quadrature reproducing
$\Omega_s^\text{corr}$) **holds by construction** at every iteration of the
twice-converged constraint — the quadrature is *solved* to make it hold. Recognizing
this explicitly: the razor in this literal form is satisfiable for **any** value
of $C_2$, since the quadrature simply re-solves the particular part of $F$ to
absorb whatever $D(C_2)$ contributes. This means the razor's literal form is not
an independent test once the action is fully closed — the real test is whether
the construction, taken as a whole, has any genuinely free, physically
consequential parameter left. That is the $(C_2,\Lambda_M)$ audit.

## 4. The $(C_2,\Lambda_M)$ invariance audit — $C_2$ does not cancel, and nothing found here fixes it

Ran the corrected, iterated construction (`Update-WP3-BackreactionMagnitudeCorrected`'s
machinery) with $C_2$ carried explicitly and consistently through every pass —
not reset to zero at each iteration — for several fixed trial values, iterated
to full numerical convergence (8 passes; stable to the sixth significant figure
by pass 4 in every case tested):

| $C_2$ | $D/E^2$ at $z=0$ (converged) |
|---|---|
| $0$ | $-0.1029$ |
| $10$ | $+0.1125$ |
| $50$ | $+0.974$ |
| $-30$ | $-0.749$ |

**$C_2$ does not wash out under iteration.** The kernel-subtracted ("particular")
part of $F$ is identically zero at the anchor point for every $C_2$ tested (by
construction of the anchoring), meaning the entire $C_2$-dependence survives
undamped into $D$ — a term with an order-unity effect on the near-today energy
budget decomposition, even though (confirmed separately) the *fitted background*
$E(a)$ itself never changes, since the quadrature is solved to reproduce it
regardless of $C_2$.

**Checked whether "$D\equiv0$ at all times" could serve as a closure condition
fixing $C_2$** — the only additional principle available that hasn't already
been tried (kernel-zero and past-regularity both already rule out any effect
from those directions; $C_2$ is confirmed subdominant in the deep past exactly
as the C2Kernel round found). Result: **no single $C_2$ zeros $D(z)$ at more
than one redshift** — the zero-crossing of $D(C_2)$ drifts from $C_2\approx5$
near $z=0$ toward larger $C_2$ at higher $z$, with no common root across the
five redshifts checked ($z=2,1,0.5,0.1,0$). This rules out the one candidate
closure condition available from within this construction alone.

**This is exactly the scenario the C2Kernel advisory itself named as the
failure mode**: *"What would violate it: $C_2$ surviving in observables without
being selected — which is precisely a failure of the razor, i.e. the
kill-relevant confrontation announcing itself."* $D$ is not the fitted
background itself, but it is a physically meaningful quantity (the multiplier
sectors' own share of the energy budget, entering $\Lambda_M,\pi_i,p_R$ — objects
with their own dynamics and, presumably, their own eventual observational
consequences once WP6-type tests are built) whose value swings from
$-10\%$ to $+97\%$ of the total budget at $z=0$ depending on an entirely
unfixed constant.

## 5. Status — escalating, not resolving alone

**Not a unilateral kill.** Every one of this program's prior "this looks
terminal" moments (the budget tension, the inverse-reconstruction mismatch, the
$C_1$ ambiguity, the future-growing multiplier mode) turned out to hinge on a
correctable setup error or a structure that had been mischaracterized — and the
discipline that caught each of those was escalation, not solo resolution, in
either direction. This finding is reported with that same posture: it is
real, verified three ways (structural argument for why $C_2$ shouldn't be fixed
by anything checked so far; converged, stable numerics across four trial
values; the "no common root" check ruling out the one remaining internal
candidate), but it may still hinge on a principle this session has not thought
of — a boundary condition on $\Lambda_M$ or $\pi_i$ not yet considered, a
requirement from matter-sector consistency not yet checked, or a recognition
that $D$ itself needs a more careful, frame-invariant definition before being
treated as physically meaningful at all.

**What would resolve it, in order of how native each candidate is to the
program's existing discipline:**
1. A boundedness/regularity condition on $\Lambda_M(t)$, $\pi_i(t)$, or $p_R(t)$
   in some limit not yet checked (future-boundedness in the deep-MOND limit,
   analogous to the past-regularity principle used for $C_1$ and the species
   multipliers).
2. A physical requirement from matter-sector energy conditions or from a
   perturbative/observational consequence of $\Lambda_M$ that this background-only
   analysis cannot see.
3. Recognition that $C_2$ is genuinely, irreducibly free — in which case the
   "zero adjustable parameters" claim needs qualification (an honest, not fatal,
   outcome, but a real one, and the kind of finding this whole program's
   escalation discipline exists to surface rather than paper over).

**Recommend a touch point before proceeding further on this specific
question** — mirroring the pattern used for the well-posedness snag and the
exchange-term construction earlier in the program, both of which were resolved
by a second read rather than by pushing through alone. WP2
discharge-by-incorporation (still pending confirmation) and WP4a/WP4b remain
unaffected by any of this. The KATRIN clock remains the program's most
time-critical item; nothing in `cdot-7/` was touched.
