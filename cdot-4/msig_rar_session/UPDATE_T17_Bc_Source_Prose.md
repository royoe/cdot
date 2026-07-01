# UPDATE — T17 Prose Correction: What Sources $B_c$

*Targeted prose fixes to T17. Resolves the dimensional error (Issue 1) and the
BH-as-source contradiction (Issue 2) found in the consistency check. All four sign-level
links are preserved — the edits remove a false causal arrow, they do not weaken the
mechanism. Session: 2026-06-30.*

---

## 1. The Conceptual Fix (read first)

The merged result (T14 §"Quarter Power as a Transition-Radius Geometric Mean";
T17 line 29) establishes that the M-σ relation is a **derived consequence** of the shared
acceleration scale: $M_\text{BH}$ and $v_f$ each independently track $GM_\text{bary}\,a_0$,
so they correlate **without one causing the other**.

But three passages in T17 (lines 66, 98, 127) still carry the older causal story in which
the central black hole *sources* $B_c$. That is the previously-discarded "Role 1":
if $B_c$'s amplitude scaled with $M_\text{BH}$, then $a_0$ would vary galaxy-to-galaxy with
central BH mass — destroying the universality of $a_0$ that the RAR's 0.13 dex tightness
over six decades directly evidences. The BH therefore **cannot** be the source.

**What actually sources $B_c$:** the baryonic mass distribution, through the same
transition-radius / selection-junction physics that produces the RAR:
$$B_c = \frac{(GM_\text{bary}\,g_\dagger)^{1/4}}{r}, \qquad g_\dagger = \dot{c} = cH_0.$$
The quarter power is on the **baryonic** mass, not the BH mass. $M_\text{BH}$ enters only
because it *also* tracks $GM_\text{bary}\,a_0$ (the derived M-σ relation). The black hole
is a **correlate of $B_c$, not its cause.**

This makes the morphology chain *stronger*: disk-stripping strength is set by the galaxy's
own baryonic $B_c$ field, which correlates observationally with $M_\text{BH}$, so all four
sign-level checks survive — they simply no longer assert a false causal arrow.

---

## 2. Surgical Replacements

### Fix A — Issue 1 (dimensional error), §"The Two-Component Force Law", lines 64–68

REPLACE:
> where $\mathbf{B}_c$ is a magnetic-like component of the $c$-field. For a flat
> rotation curve this requires $B_c \sim v_f/r$ — i.e. $B_c$ has dimensions of an
> angular frequency and, from the M-σ connection, $B_c \sim M_\text{BH}^{1/4}/r$
> (conditionally derived from the transition-radius geometric mean construction, T14;
> attractor convergence assumed).

WITH:
> where $\mathbf{B}_c$ is a magnetic-like component of the $c$-field, with dimensions of
> an angular frequency. For a flat rotation curve the surviving population requires
> $B_c \sim v_f/r$. The amplitude is sourced by the **baryonic** mass through the
> transition-radius construction (T14),
> $$B_c = \frac{(GM_\text{bary}\,g_\dagger)^{1/4}}{r},\qquad g_\dagger=\dot{c}=cH_0,$$
> conditionally derived as a geometric mean (attractor convergence assumed). The quarter
> power sits on the baryonic mass, not on $M_\text{BH}$. Because $M_\text{BH}$ also tracks
> $GM_\text{bary}\,a_0$ (the derived M-σ relation, below), $B_c$ correlates observationally
> with central BH mass — but the BH does not source it.

*(Removes the dimensionally-broken $M_\text{BH}^{1/4}/r$ on the LHS of a mass; states the
correct baryonic source explicitly.)*

### Fix B — new subsection, inserted immediately after §"The Two-Component Force Law"

INSERT:
> ### What Sources $B_c$
>
> $B_c$ is sourced by the baryonic mass distribution coupled to the cosmological
> acceleration scale $g_\dagger = \dot{c} = cH_0$ — the same two ingredients as the RAR
> (T14). It is **not** sourced by the central black hole. This matters for the universality
> of $a_0$: if $B_c$ scaled with $M_\text{BH}$, the acceleration scale would vary with
> central BH mass and the RAR would not hold to 0.13 dex across six decades. The black hole
> mass *correlates* with $B_c$ — both track $GM_\text{bary}\,a_0$ — but is a correlate, not
> a cause. Throughout the morphology chain below, "high-$M_\text{BH}$ galaxy" should be read
> as "galaxy high on the shared $GM_\text{bary}\,a_0$ normalization, hence high $B_c$ *and*
> high $M_\text{BH}$ together."

### Fix C — §"Flatness as a Dynamical Attractor", lines 83–84

REPLACE:
> As $c$ grows and $B_c$ strengthens, progressively more disk stars are
> stripped — driving morphological evolution toward ellipticals at low $z$.

WITH:
> As the cosmological acceleration scale evolves and the stripping threshold shifts,
> progressively more disk stars are stripped over cosmic time — driving morphological
> evolution toward ellipticals at low $z$. (The sign of this trend depends on the joint
> evolution of $c$ and $H$ in $g_\dagger = cH$, Core §5, and should be checked against
> those scalings rather than assumed; see T14, which hedges the $B_c$-vs-$c$ scaling
> explicitly. This is Issue 3 of the consistency check.)

### Fix D — §"Ordered vs. Random Orbits", lines 98–101

REPLACE:
> A galaxy with a very massive central BH (sources a stronger $B_c$) sheds its disk
> most rapidly and ends as a pure spheroid — an **elliptical galaxy**. A galaxy with
> a small BH keeps its disk. This is a qualitative account of the disk/elliptical
> dichotomy tied to BH mass.

WITH:
> A galaxy high on the shared $GM_\text{bary}\,a_0$ normalization has both a stronger $B_c$
> field and a more massive central BH. Its strong $B_c$ sheds the disk most rapidly,
> ending as a pure spheroid — an **elliptical galaxy** — while also hosting a massive SMBH.
> A galaxy low on the normalization has weak $B_c$ and a small BH, and keeps its disk. The
> disk/elliptical dichotomy thus correlates with BH mass without the BH sourcing the
> stripping field: both are downstream of the same baryonic normalization.

### Fix E — Link 3, line 127 (within the existing bullet)

REPLACE:
> A high-mass BH (strong $B_c$) → fast disk stripping → ends as a pure elliptical.

WITH:
> A galaxy high on the $GM_\text{bary}\,a_0$ normalization (strong $B_c$, and a high-mass
> BH as a co-tracer) → fast disk stripping → ends as a pure elliptical.

---

## 3. Consistency Notes (for the merge cross-check)

- After these edits, T17 lines 27, 29 (M-σ as derived consequence) and the mechanism
  sections tell **one** causal story: baryonic mass + $g_\dagger$ → $B_c$ → stripping;
  $M_\text{BH}$ co-tracks the same normalization. No remaining BH-as-source language.
- Fix A also resolves Issue 1: the only place a quarter-power appeared on a mass with a
  stray $/r$ (line 66) is replaced by the correct $B_c$ amplitude (a frequency) with the
  quarter power on $M_\text{bary}$.
- The "consistency condition" at T17 line 152 (Connection to PBH, §) carries the **same**
  dimensional error as old line 66 ($M_\text{BH}^{1/4}\sim(GM_\text{bary}a_0)^{1/4}/r$).
  Recommend the same fix there: state it as the $B_c$ amplitude
  $B_c\sim(GM_\text{bary}a_0)^{1/4}/r$ **or** as the mass relation
  $M_\text{BH}\sim GM_\text{bary}a_0$ — not the two fused. Flagged here; not rewritten
  above because it sits in the PBH section, which may want its own framing.
- Issue 4 (evaporation-ceiling break) is *not* edited here. With M-σ now derived, the
  top-end break is a **departure** from the derived relation (BH grows by mergers/accretion
  while $\sigma$ saturates), not a feature of it. Suggest one clarifying sentence in Link 4;
  left for a separate pass to keep this update focused on the $B_c$-source fix.

---

## 4. Suggested T14 Touch (optional, for symmetry)

T14 is internally correct on the source ($B_c=(GM_\text{bary}g_\dagger)^{1/4}/r$, baryonic).
No fix required. Optionally add one sentence to the "M-σ as a derived consequence" paragraph
(T14 line 201) stating explicitly that $B_c$ is baryon-sourced and the BH is a co-tracer, so
the point is stated in both files rather than only inferable from T14.
