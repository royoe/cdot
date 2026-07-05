# REVIEW NOTE (REWORKED) — T23: Mechanism Replacement, $R(z)$, and the Occupancy Index

*Status: review note, supersedes REVIEW_NOTE_T23_Rz_and_Occupancy_Index.md. To be folded into T23 (Autocatalytic Counting), toward cdot-6.*
*Date: 2026-07-05.*
*Targets: T23 title/§3 (mechanism), §5 (subcritical phase), §6 (lengths), §10 (open items).*
*Depends on: T23 cdot-5; UPDATE_T14_Hyperbolic_Holographic_Counting.md (companion, same session).*

---

## 0. Why this reworks the earlier note

The earlier review note sharpened T23 on two points ($R(z)$; occupancy index
$n\approx1.35$) but left T23's **autocatalytic mechanism** in place. This session
showed that mechanism **fails** (a flat-3D transitive-reachability network gives
the volume law or the wrong functional form; exponential growth vs a physical
radius is geometrically impossible in fixed-density flat 3-space). It is replaced
by a **hyperbolic-holographic** origin (companion T14 update). This reworked note
folds that replacement together with the two earlier clarifications, so the whole
of T23 §3, §5, §6, §10 is revised coherently. The parts of the earlier note that
survive unchanged (the $R(z)$ construction, the $n$↔$q$ relation) are retained
below.

---

## 1. Mechanism: replace autocatalysis with hyperbolic-holographic counting

**T23 §3 as written (retract):** $dN/dR=N/L$ from "transitive reachability"
(new nodes join the connected set in proportion to $N$). This session's finding:
- short-range dense links → space-filling → volume law, not exponential;
- diffusive spanning tree → $e^{R^2/L^2}$ (wrong form);
- sparse multiplicative tree → cannot embed in fixed-density 3-space (exponential
  node-count outruns cubic volume within a few hops).
The obstruction is general: **exponential $N$ vs physical $R$ is impossible in flat
3D at fixed density.** The autocatalytic mechanism does not hold.

**Replacement (T14 companion update):** the relation space has intrinsic
**hyperbolic** geometry $H^d$ (curvature radius $r_c$); holographic saturation on
its boundary gives $N\propto\sinh^{d-1}(R/r_c)$, which is $R^{d-1}$ (flat) for
$R\ll r_c$ and $e^{(d-1)R/r_c}$ for $R\gg r_c$, matching $c\propto e^{R/L}$ with
$L=r_c/(d-1)$. Exponential growth is now a theorem of the geometry, not a posited
kinetics. Recommend rewriting §3 around this, and **retitling** the document (it
is no longer "autocatalytic"; e.g. "Hyperbolic-Holographic Counting and the
Curvature Crossover").

## 2. The "transition" is a curvature crossover, not a phase transition

**T23 §5 as written:** an occupancy → connectivity **percolation transition**,
with the subcritical phase as "$N\propto R^3$, the volume law." Two corrections:

(a) **Not a percolation transition.** Two sessions found no mechanism for one — no
local vacuum saturation (the foam is scale- and $c$-rescaling-invariant, so no
local quantity crosses threshold at a cosmological epoch), and no percolation
control parameter. Under the hyperbolic picture the "transition" is the **smooth
curvature crossover at $R\sim r_c$** — occupancy-like ($R^{d-1}$) below, exponential
above. No critical phenomenon, nothing saturates, and **T23's supercriticality
assumption (§10 open item) is no longer needed** — it is dissolved, not answered.

(b) **The subcritical index is not the volume law.** The DESI high-$z$ bins give a
subcritical distance index $q=1.37$, hence a counting index
$n=1/(2(q-1))\approx1.35$ (derivation retained from the earlier note; $D_H$
continuity at the break checks exactly). This is **not** $N\propto R^3$ ($n=3$
would give $q=1.17$, missing the data). The subcritical phase is a *sub-volume,
near-sub-area* power law, $n\approx1.35$ — and in the hyperbolic picture this is
the small-$R$ area index $d-1$ (if $c\propto$ boundary area) or bulk index $d$ (if
$c\propto$ bulk volume). Recommend §5 replace "$N\propto R^3$ volume law" with the
$n\approx1.35$ statement and the $n=1/(2(q-1))$ relation.

## 3. The over-determination of the dimension $d$ (new, honest caveat)

The hyperbolic picture has one free parameter, $d$ (equivalently $r_c=(d-1)L$),
and it is currently **over-determined** by three features that do not coincide:

| feature | implied $d$ |
|---|---|
| break location $R_*\approx L$ (crossover $R\sim r_c$) | $2$ |
| $n\approx1.35$ if $c\propto$ boundary area ($n=d-1$) | $2.35$ |
| $n\approx1.35$ if $c\propto$ bulk volume ($n=d$) | $1.35$ |

$d\in\sim[1.35,2.35]$ depending on the feature and the area-vs-volume reading. The
picture fixes the *form* and *unifies* the regimes; it does **not** yet pin $d$.
Recommend §10 record this as the central open item, replacing "derive $q$ from
branching statistics" (branching statistics no longer apply — there is no
branching process; the task is now to pin the geometry's dimension/curvature and
resolve whether $c\propto N$ counts boundary area or bulk volume).

## 4. Retained from the earlier note: the epoch horizon $R(z)$

Unchanged and still recommended for §6. The horizon that sets the local $c$ is
obtained by **inverting the counting law**, not by $R_\text{now}-D_p(z)$ (which
goes negative at high $z$):
- percolated/exponential ($z\le z_*$): $R(z)=R_\text{now}-\tfrac{L}{2}\ln(1+z)$;
- subcritical/power ($z>z_*$): $R(z)=R_*\,[(1+z)/(1+z_*)]^{-1/(2n)}$.

Internal check: the crossover horizon $R_*$ from inversion ($66.6\,r_d$) matches
$L=67.1\,r_d$ to <1%. Epoch-horizon anchors (illustrative $r_d=147$ Mpc):

| epoch | $z$ | $R(z)$ [$r_d$] | $R(z)/R_\text{now}$ |
|---|---:|---:|---:|
| today | 0 | 93.1 | 1.00 |
| DESI Ly$\alpha$ | 2.33 | 57.2 | 0.61 |
| crossover $z_*$ | 1.20 | 66.6 | 0.72 |
| recombination | ~1090 | 6.7 | 0.07 |

Physical reading unchanged: $R(z)$ is literally the count that sets $c$; as
$z\to$ genesis, $R\to0$ and $c\to0$. Also retained for §6: the one-line
clarification that $D_p(\infty)=116.7\,r_d > R_\text{now}=93.1\,r_d$ because, on a
static map with a counting-law crossover, the integrated light path and the
present horizon radius are genuinely different lengths.

*(Note: the specific $R(z)$ values above use the cdot-5 broken-law fit with a
sharp break at $z_*=1.20$. Under the smooth hyperbolic crossover, and with the
QSO/Ly$\alpha$ points treated as possibly-revisable, the low-$z$ galaxy fit gives
the same slope $L\approx68\,r_d$ but places the crossover at extreme $z$; the
recombination-era $R(z)$ then differs. Flag both readings in §6 and mark the sharp
break as the aspect most sensitive to future QSO/Ly$\alpha$ revision.)*

## 5. Summary of recommended edits to T23

1. **Title/§3:** retire "autocatalytic"; replace the mechanism with
   hyperbolic-holographic counting $N\propto\sinh^{d-1}(R/r_c)$ (T14 companion).
2. **§5:** the "transition" is a curvature crossover, not percolation; the
   subcritical phase is $N\propto R^{1.35}$ (from $q=1.37$ via $n=1/(2(q-1))$),
   **not** the $R^3$ volume law.
3. **§6:** add the $R(z)$ inversion formulas, the epoch-horizon table, and the
   $D_p(\infty)\neq R_\text{now}$ clarification; note the sharp-break vs
   extreme-$z$-crossover ambiguity pending QSO/Ly$\alpha$ revision.
4. **§10:** replace "derive $q$/supercriticality" with "pin the geometric
   dimension $d$/curvature $r_c$ (currently over-determined, $d\sim1.35$–$2.35$)
   and resolve the area-vs-volume reading of $c\propto N$." The supercriticality
   item is dissolved (no critical phenomenon under the geometric picture).

## 6. Caveats

- The mechanism replacement is a *more principled posited structure* (hyperbolic
  relation space + established holographic saturation), not a first-principles
  derivation; $d$/$r_c$ remain unfixed and over-determined.
- $n\approx1.35$ inherits the fitted $q=1.37$ uncertainty (four bins, diagonal
  errors, $z_*$/tracer degeneracy); it moves if $q$ moves under full covariance/DR3.
- This note concerns the counting-law **form and origin**; it does not resolve the
  CMB $\ell_1$ bracket (horizon **size**, separate axis).
