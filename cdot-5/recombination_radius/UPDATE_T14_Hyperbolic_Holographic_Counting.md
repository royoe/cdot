# UPDATE — Hyperbolic-Holographic Counting Law: Deriving the Form from Boundary DOF

*Status: proposed update, for cross-check and merge. Session 2026-07-05.*
*Targets: T14 (holographic saturation, $g_\dagger$, finite horizon); T12 (connecton as holographic DOF); T23 (counting-law origin — see companion T23 review note).*
*Depends on: T23 (Autocatalytic Counting), cdot-5; the hyperbolic-relation-space and holographic-DOF tests of this session.*

---

## 0. Summary

Holographic saturation — already in T14 ("one bit per $4L_p^2$" on the horizon) —
evaluated on a **hyperbolic** relation-space boundary **derives the functional
form** of the counting law that cdot-5's autocatalytic mechanism failed to
supply. The boundary area of a ball of radius $R$ in $H^d$ (curvature radius
$r_c$) is $A(R)\propto\sinh^{d-1}(R/r_c)$; the holographic count $N\sim A/4L_p^2$
therefore interpolates, in one expression, between the flat area count ($R^{d-1}$,
small $R$) and the exponential counting law ($e^{(d-1)R/r_c}$, large $R$). This
**unifies** T14's original flat-$R^2$ holographic count and cdot-5's exponential
law as two regimes of a single geometry, and replaces the (failed) autocatalytic
kinetics with geometry. It does **not** fix the geometry's dimension/curvature
from first principles — that remains one posited scale, and it is currently
**over-determined** (§4). This is a picture assembled from established holographic
ingredients on cdot's own premises, not a borrowing of dS/CFT dynamics (§5).

---

## 1. The construction

Take the relation space (the network whose node-count sets $c$; T12) to have
intrinsic hyperbolic geometry $H^d$ with curvature radius $r_c$:
$$ds^2=dR^2+r_c^2\sinh^2(R/r_c)\,d\Omega_{d-1}^2.$$
The boundary area of a ball of intrinsic radius $R$ is
$$A(R)\propto\sinh^{d-1}(R/r_c),$$
and T14's holographic saturation gives the count $N\sim A/4L_p^2\propto A(R)$, with
$c\propto N$.

**Two regimes of one expression:**
- $R\ll r_c$: $\sinh(x)\approx x$ ⟹ $A\propto R^{d-1}$ — the **flat holographic
  area count** (e.g. $R^2$ for $d=3$): T14's original occupancy-era count.
- $R\gg r_c$: $\sinh(x)\approx e^x/2$ ⟹ $A\propto e^{(d-1)R/r_c}$ — the
  **exponential counting law**, matching $c\propto e^{R/L}$ with $L=r_c/(d-1)$.

The crossover is at $R\sim r_c$.

## 2. What this fixes: the counting-law *form*, from geometry not kinetics

cdot-5 (T23) posited $dN/dR=N/L$ via an autocatalytic "transitive reachability"
argument. That mechanism was shown this session to fail: a short-range dense
network is space-filling and gives the volume law, not the exponential, and a
sparse multiplicative tree cannot embed in fixed-density 3-space (exponential
node-count outruns cubic volume within a few hops). The obstruction is that
**exponential growth vs a physical radius is geometrically impossible in flat 3D
at fixed density.**

The resolution is that the relation space is **not** flat 3D — its intrinsic
geometry is hyperbolic, where exponential volume/area growth is the *defining*
property. On $H^d$ the obstruction vanishes by construction, and the exponential
law is a **theorem of the geometry** rather than a posited kinetics. This is the
firmer footing the autocatalytic mechanism lacked.

## 3. What this unifies

Three previously-separate items collapse into one object $N\propto\sinh^{d-1}(R/r_c)$:
- T14's flat-$R^{d-1}$ holographic area count (small $R$);
- cdot-5's exponential connectivity law (large $R$);
- the "occupancy → connectivity transition."

The transition — for which two sessions found **no** mechanism (no local vacuum
saturation; no percolation control parameter) — is simply the **curvature
crossover** at $R\sim r_c$. There is no phase transition, nothing "saturates," and
T23's supercriticality assumption is not needed: it is one smooth geometric
crossover. (Consistency checks: boundary-area and bulk-volume counts become
proportional at large $R$ — the "everything near the boundary" property, with
$V/A\to r_c/(d-1)=L$ — so the holographic and connectivity readings agree; and the
count is finite at the finite physical horizon $D_p(\infty)$, so no infinite
horizon is reintroduced.)

## 4. Consequence for $g_\dagger$, and the honest over-determination of $d$

**A geometric scale for $g_\dagger$.** The count now carries an intrinsic length,
the curvature radius $r_c=(d-1)L$. This is a *geometric* candidate for the
crossing-rate scale in $g_\dagger\sim c^2/\ell$, replacing the earlier ambiguity
("which of $L$, $R_\text{now}$, $D_p(\infty)$?"). For $d=3$, $r_c=2L$, which
roughly **halves** T14's standing $2.8\times$ overshoot on $a_0$ to $\sim1.4\times$.
A concrete lever with a principled origin — not decisive, and not a fit.

**But $d$ is over-determined and does not perfectly reconcile.** Three features
pull on the one free parameter $d$ (equivalently $r_c$):

| feature | reading | implied $d$ |
|---|---|---|
| break location $R_*\approx L$ (crossover at $R\sim r_c$) | $r_c=L$ | $d=2$ |
| DESI subcritical index $n\approx1.35$, **if** $N=$ boundary area | $n=d-1$ | $d\approx2.35$ |
| DESI subcritical index $n\approx1.35$, **if** $N=$ bulk volume | $n=d$ | $d\approx1.35$ |

These do not coincide. A single $H^d$ cannot satisfy all three; $d$ sits somewhere
in $\sim1.35$–$2.35$ depending on the feature and on whether $c\propto N$ counts
the boundary area (holographic) or the bulk volume (connectivity). **This is the
one honest free parameter, and it is not yet pinned consistently.** The picture
fixes the *form* ($\sinh$) and unifies the regimes; it does not yet predict the
dimension.

## 5. Relation to dS/CFT — similarities and differences, stated plainly

The "horizon matrix" / dS-CFT picture (information stored as microstates on an
observer's cosmic horizon, capacity set by boundary area) is the established model
this most resembles. What cdot **shares**: the horizon as a holographic screen;
the boundary DOF count as the fundamental quantity; capacity $\propto$ boundary
area. What cdot does **not** take (correctly, since cdot has no $\Lambda$ and no
expansion): dS/CFT's $\Lambda$-driven horizon dynamics — the cdot horizon grows
because $c(t)$ grows, not because space expands. And cdot's horizon is a **finite,
real, reachable** radius rather than dS/CFT's boundary at unreachable future
timelike infinity, which sidesteps dS/CFT's hardest feature (a non-unitary
Euclidean boundary CFT). The transferable content is kinematic/holographic, not
dynamical. Framing: cdot borrows the *picture*, not the *equations of motion*.

## 6. Proposed edits to T14

- **Holographic-saturation section:** add §1's construction — the count is
  $N\propto\sinh^{d-1}(R/r_c)$ on a hyperbolic boundary, with the flat area count
  as its small-$R$ limit. State that this *derives* the counting-law form (§2) and
  *unifies* the flat and exponential counts (§3).
- **$g_\dagger$ / "which finite length" open item:** update with §4 — the natural
  scale is $r_c=(d-1)L$; $d=3$ halves the overshoot; flag $d$ as over-determined.
- **Finite-horizon row:** note the holographic count is finite at $D_p(\infty)$;
  no infinite horizon.
- **New open item:** pin $d$ (equivalently $r_c$) and resolve the area-vs-volume
  reading of $c\propto N$ (§4). Until then $d\in\sim[1.35,2.35]$ is the one free
  geometric parameter.
- **Add a "relation to dS/CFT" note** (§5) for context, clearly marking what is
  and is not borrowed.

## 7. Caveats

- $d$/$r_c$ unfixed and over-determined (§4) — the central open item.
- Whether $c\propto N$ counts boundary area or bulk volume is unresolved and
  changes the $d$↔$n$ relation; the two agree only asymptotically (large $R$).
- This addresses the counting-law **form**; it does **not** resolve the CMB
  $\ell_1$ bracket, which is about horizon **size** (separate axis).
- "Hyperbolic relation space" is itself still a posited structure — more
  principled and better-connected to established holography than the autocatalytic
  kinetics, but not derived from the connecton foundations.
