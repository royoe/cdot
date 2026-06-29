# Change Document — Adoption of Invariant $G$ (LLR-forced)

**Date:** 2026-06-29
**Scope:** Replaces the selected scaling $G\propto c^{-2}$ with **invariant $G$
($G\propto c^{0}$)** as the recommended core choice, on empirical grounds (Lunar Laser
Ranging). Affects: Core Principles, T8, T9, T10/OP-13, OP-8, and parts of OP-14. The
redshift law, two-$H_0$ structure, age, $\alpha$-invariance, and $q_0$ are **unaffected**
($G$-independent).

---

## 1. Motivation (the LLR refutation)

Detailed LLR analysis (T8, June 2026) shows $G\propto c^{-2}$ fails strongly:
- $\dot G/G = -2\dot c/c = -2H_0^{\text{hor}} \approx -7\times10^{-11}\,\text{yr}^{-1}$,
  vs the LLR bound $|\dot G/G| < 1.5\times10^{-13}\,\text{yr}^{-1}$ — a factor $\sim$500
  on $\dot G$ alone.
- The self-consistent ranging calculation (orbital expansion $r\propto c^2$ + varying
  $c$ in the range formula + atomic clock $\nu\propto c^2$) gives a predicted LLR range
  rate of **79.6 mm/yr vs observed 38.2 mm/yr**, a $\times720$ tension in $\dot G/G$-
  equivalent terms — the self-consistent treatment *worsens* the naive estimate by ~50%.
- **Orbital expansion $r\propto c^2$ is directly refuted** by LLR.

## 2. Key finding: $G\propto c^{-2}$ was *selected*, not premised

From T8 and Core Principles §1: $G\propto c^{-2}$ was always flagged as "selected by
agreeing constraints, not derived from a first principle" — a fifth scaling noted as a
*standing debt*, explicitly **not a premise**. It was chosen because it simultaneously:
1. reproduces GR weak-field as the PV/Dicke-native value;
2. gives orbital expansion $r\propto c^2$ → constant stellar flux;
3. keeps the SN Hubble diagram self-consistent;
4. passes through the Dicke (1957) natural-units value.

Reasons (1) and (4) are **PV-framework** features. The model **already abandoned PV** for
the mass scaling (it takes invariant mass $s=0$, not PV's $m\propto c^{-3/2}$, on
empirical grounds — T8, T11). Once PV is abandoned for mass, the PV-native value of $G$
loses its privileged status. Adopting invariant $G$ makes mass-invariance and
$G$-invariance **both** breaks from PV in the same direction — more internally
consistent, not less.

## 3. What invariant $G$ resolves

- **Orbital-expansion refutation removed at the root.** Expansion was a *consequence* of
  $G\propto c^{-2}$: from $L=mvr$ (conserved) and $v^2=GM/r$, $r\propto 1/G$. With $G$
  invariant, $v^2 r = GM$ = const and $vr$ = const ⟹ $r$ = const. **Orbits do not
  expand.** The $\times720$ LLR tension disappears.
- **$\dot G/G$ tension removed.** $G$ constant ⟹ $\dot G = 0$, trivially consistent with
  LLR, pulsar timing, and BBN $G$-variation bounds.

## 4. Costs (aesthetic, not empirical)

- **Loses orbital expansion $r\propto c^2$**, hence the OP-13 / T10 "galaxy size
  evolution $\propto(1+z)^{-1}$" consistency success. This was a soft check (high-$z$
  galaxy compactness is conventionally explained by formation/merging), not a core
  prediction.
- **Loses "constant stellar flux."** With expansion, $L\propto c^4$ and $r\propto c^2$
  gave received flux $F=L/4\pi r^2\propto c^0$ (constant). With static orbits,
  $F\propto c^4$ — but $\dot F/F\sim4H_0\sim4\times10^{-10}\,\text{yr}^{-1}$, locally
  unobservable; order-unity only over $\sim$Gyr (a weak paleoclimate/habitability
  consideration, not a sharp constraint). This was an anthropic *niceness*, never an
  observational requirement. (Note: $L\propto c^4$ itself is a separable modelling
  choice and may be revisited.)
- **SN Hubble diagram backbone is $G$-independent and survives.** The redshift law
  $1+z=(c_{\text{now}}/c_{\text{emit}})^2$ (from $\nu\propto c^2$, atomic) and the
  distance–redshift relation (from $c\propto R^3$ horizon kinematics) do not involve $G$.
  Only the standard-candle luminosity calibration is recomputed; $q_0>0$ is purely
  kinematic and unchanged.

## 5. Unaffected (explicitly $G$-independent — no change needed)

Squared redshift law; two-$H_0$ structure ($H_0^{\text{hor}}$, $H_0^{\text{obs}}$,
$P=2$); proper age $\approx21$ Gyr; $\alpha$ invariant to all orders; $\nu\propto c^2$;
$\epsilon_0\propto c^{-1}$; $q_0=1/(nP)>0$; the relational principle; conservation/
symmetric-flip structure; the count-vs-mass fork (OP-16).

---

## 6. Per-file edits for the repo

### Core_Principles.md
- **§1, the "fifth scaling" paragraph:** change $G\propto c^{-2}$ to **invariant $G$
  ($G\propto c^0$)** as the recommended choice. State that the PV-native $c^{-2}$ value
  is refuted by LLR ($\dot G/G$ and orbital-expansion ranging), and that invariant $G$
  parallels the invariant-mass break from PV. Remove the "makes stellar flux constant
  under orbital expansion" justification (no longer operative).
- **§1, premise list intro:** the lead sentence "all cosmological dynamics are carried by
  a time-varying speed of light $c(t)$ **and a time-varying gravitational coupling
  $G(t)$**" → strike "and a time-varying gravitational coupling $G(t)$"; $G$ is now
  constant. Cosmological dynamics are carried by $c(t)$ alone.
- **§7 status table:** 
  - Row "$G\propto c^{-2}$ scaling | PV/Dicke-native; selected by constraints (T8)"
    → "**$G$ invariant ($G\propto c^0$) | adopted; $c^{-2}$ refuted by LLR (T8)**".
  - Row "Orbital expansion $r\propto c^2$ = constant stellar flux | Core, given
    $G\propto c^{-2}$ (T9)" → "**Orbits static ($r$ const) under invariant $G$;
    no expansion (T9)**".
  - Row "Galaxy size evolution $r\propto(1+z)^{-1}$ | Consistency success (T10)"
    → "**Withdrawn — relied on orbital expansion, now dropped (T10)**".

### T8_Gravitational_Constant.md
- Reframe "The Model's Prediction: $G\propto c^{-2}$" → "The Model's Choice: invariant
  $G$." Keep the PV $c^{-2}$ derivation as **historical/legacy**, now superseded.
- Record the LLR result as **decisive against $c^{-2}$** (the $\times720$ / 79.6 vs
  38.2 mm/yr computation), and state invariant $G$ as the resolution (orbits static,
  $\dot G=0$).
- The "local screening" escape route for $c^{-2}$ becomes **moot** (no variation to
  screen). Note this.
- The "$G\propto c^{-2}\propto(1+z)$, larger in past" and BBN-tension subsections:
  mark as **resolved by invariant $G$** (no $G$ variation → no BBN-$G$ tension).
- Add a new standing debt: invariant $G$ is now itself a *choice* needing a
  first-principle justification from the relational framework (as $c^{-2}$ was) — the
  theoretical-debt note transfers, it does not disappear.

### T9_Orbital_Dynamics.md
- The orbital-expansion derivation $r\propto c^2$ is **superseded**: under invariant $G$,
  $v^2 r=GM$=const and $vr$=const ⟹ $r$=const. Orbits are static on the map.
- Recompute "constant stellar flux": now $F\propto c^4$ (drifts), locally unobservable;
  reframe as a minor habitability note, not a success.

### T10_Galaxy_Size_Evolution.md (and OP-13 in Open_Problems)
- The $(1+z)^{-1}$ size-evolution result **withdrawn** (it rested on orbital expansion).
  Note the observational compactness of high-$z$ galaxies is conventionally explained
  and is no longer claimed as model support.

### Open_Problems.md
- **OP-8:** update — invariant $G$ adopted; $c^{-2}$ refuted by LLR; the invariant-mass
  + invariant-$G$ pairing is the recommended non-PV core.
- **OP-13:** mark the orbital-expansion / galaxy-size consistency result **withdrawn**
  under invariant $G$ (cross-ref T9/T10). Note the dynamical-selection ring-ejection
  prediction (OP-14/OP-19) **must be re-examined**: it assumed orbits expand
  ($r\propto c^2$) as the driver of ring loss — see OP-14 note below.
- **Header status line / "Consistency success: OP-13":** remove OP-13 from consistency
  successes.

### OP-14 (connecton) and OP-19 (M–σ) — re-derivation flagged (do NOT silently keep)
$G\propto c^{-2}$ was baked into several OP-14 results. Under invariant $G$:
- **Foam-sea Newtonian $1/r$:** likely fine (present-epoch normalization of $G$), but the
  normalization argument should be re-stated with $G$ constant.
- **Genesis $r_s/R\propto R^{2-4n}$ (OP-6 Reading 2):** used firm $G\propto c^{-2}$.
  With $G$ constant, $r_s=2GM/c^2$ gives $r_s/R\propto$ (recompute: $M\propto R^3$,
  $r_s\propto R^3/c^2\propto R^3/R^{2n}=R^{3-2n}$, so $r_s/R\propto R^{2-2n}$) — **the
  exponent changes from $2-4n$ to $2-2n$.** Re-examine whether the super-Schwarzschild-
  reservoir (Reading 2) PBH picture still holds for the chosen $n$. *(For volume $n=3$:
  $2-2n=-4$, still $\to\infty$ as $R\to0$, so the generic early super-Schwarzschild phase
  survives qualitatively — but verify.)*
- **Dynamical selection / ring ejection (OP-14, OP-19):** the mechanism was driven by
  orbital expansion ($r\propto c^2$) as $c$ grows. With static orbits this driver is
  **gone** — the ejection picture must be re-derived from whatever residual $c$-dependent
  force remains (the $v\times B_c$ Lorentz term still exists, but the "orbits expand,
  outer rings unbind" narrative no longer applies as stated). **This is the most
  significant downstream casualty and needs a fresh look.** The M–σ / disk-elliptical
  chain (OP-19) inherits this dependency.
- **$a_0\sim cH_0$ scale:** $G$-independent (kinematic), unaffected.

### T-files for CMB/PBH (T13, T16) and OP-18
- PBH genesis inherits the OP-6 exponent change ($2-4n\to2-2n$); re-verify the
  freeze-out crossover. The CMB first-peak translation is $G$-independent (atomic
  $c^2$-scaling) and unaffected.

---

## 7. Summary

Invariant $G$ is **empirically forced by LLR** and **available** because $G\propto c^{-2}$
was a selected convenience with PV-inherited justification the model had already begun
shedding (via invariant mass). It removes both LLR tensions at the root, leaves the entire
$G$-independent backbone (redshift, age, $\alpha$, $q_0$, two-$H_0$) intact, and costs only
two soft aesthetic features (orbital expansion / galaxy-size evolution, and constant
stellar flux). The principal downstream work is re-deriving the OP-14/OP-19 gravity
results that assumed $G\propto c^{-2}$ — especially the **dynamical-selection ring-ejection
mechanism, whose orbital-expansion driver is removed** and must be reconstructed or
withdrawn. Invariant $G$ also transfers (does not erase) the standing theoretical debt: it
now needs its own first-principle justification from the relational framework.
