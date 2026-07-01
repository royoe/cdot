# UPDATE — T14: $g_\dagger$ Is Kinematic ($c^2/R_0$), Not Gravitational — PROFILE Retired

*Resolving update to T14 (§"Toward the RAR", §"Energy Scale", Open Items). Status: the
consistency-with-$G$ approach resolves the coefficient question by showing it was mis-posed.
$g_\dagger$ is the sea's **kinematic** acceleration scale $c^2/R_0 = cH_0/6$, set by horizon
kinematics alone — **not** a gravitational acceleration sourced by the sea density. The entire
"sea density → $a_0$" route (floor integral, $1/r$ profile, $G\rho_\text{bg}R_0/\text{PROFILE}$)
was the wrong physics. PROFILE is retired: no such factor is needed. The coefficient **6** is
derived from the horizon radius; the remaining assumption is the kinematic identification.
Session: 2026-07-01.*

---

## 1. The Resolution

Pursuing "derive PROFILE from consistency with the Newtonian coupling" led to the realization
that PROFILE was never the right object. The key physical fact:

**A test mass embedded in a uniform sea feels no net gravitational force from it** (symmetry —
the enclosed-mass pull cancels). This is why the enclosed-sea-mass estimate
$(4\pi/3)G\rho_\text{bg}R_0$ overcounts by $\sim9\times$, and why all three "sea density → $a_0$"
routes failed: they tried to make $g_\dagger$ a **gravitational** acceleration sourced by the
sea, but a uniform sea exerts no such net force.

What the closure's relaxation scale actually requires is the sea's **kinematic** acceleration —
the scale at which the sea's own dynamics operate. The sea re-randomizes connectons at the
horizon crossing rate $c/R_0$; the associated acceleration is
$$\boxed{\,g_\dagger = c\cdot\frac{c}{R_0} = \frac{c^2}{R_0} = \frac{cH_0^{\text{obs}}}{6}.\,}$$
This uses **only** $c$ and $R_0$ — horizon kinematics. No sea density, no $G$, no PROFILE.
Numerically $c^2/R_0 = cH_0/6$ identically (it is the same $R_0=6c/H_0$).

---

## 2. What This Retires

- **PROFILE** — the profile-amplitude O(1). Not needed; there is no "sea density → force"
  map in the coefficient. Retired.
- **The "sea density → $a_0$" route** ($G\rho_\text{bg}R_0/\text{PROFILE}$) — wrong physics
  (treats a uniform sea as exerting a net gravitational pull). Dropped.
- **The floor integral as a coefficient-fixer** — already demoted (dimensionally a
  frequency²); now also unnecessary, since $g_\dagger$ is kinematic.
- **The $1/r$ "profile" → constant acceleration argument** — was the autocorrelation $\xi(r)$
  mis-identified as a density; not needed for the coefficient.
- **The $9/8$ and the $(3/16)cH_0$** — artefacts of the abandoned gravitational route.

## 3. What Survives / Is Now Cleaner

- **Coefficient $a_0 = cH_0/6$** — the **6** is derived from the horizon radius
  $R_0 = 6c/H_0 = 3P\,c/H_0$ (Core §4a, solid). $g_\dagger = c^2/R_0$ then gives $cH_0/6$
  with the coefficient fixed, no free O(1).
- **Holographic sea density** $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ — remains a true,
  $\hbar$-free identity about the connecton sea, but it is **not on the path to $a_0$**
  (does not enter $g_\dagger$). Keep it as a standalone result / dark-energy connection, not
  as the coefficient source.
- **RAR closure and functional form** — unchanged (uses $g_\dagger$ as a scale).

---

## 4. Honest Caveat (where it could still be too clean)

The step "$g_\dagger$ = (crossing rate $c/R_0$) × $c$" is a **kinematic/dimensional**
argument, not a derivation from the connecton equations of motion. It asserts that the sea's
characteristic acceleration is built from its only kinematic ingredients — $c$ and the horizon
crossing rate — giving $c^2/R_0$. This is close to the long-standing T6/T15 observation that
"$a_0\sim cH_0$ is the only acceleration one can form." **What is genuinely new and stronger:**
the specific factor. The horizon geometry fixes $R_0 = 6c/H_0$ exactly, so $c^2/R_0 = cH_0/6$
is a definite coefficient, not a free $cH_0/(\text{O}(1))$.

So the honest status: **the coefficient $cH_0/6$ is derived at the level of horizon geometry
(the 6) plus a kinematic identification of $g_\dagger$ with the sea's crossing acceleration.**
The identification is well-motivated (it is the only acceleration the sea's kinematics
provide, and it correctly rejects the gravitational routes that overcounted) but is not a
force-law derivation. This is a materially stronger and cleaner position than the abandoned
gravitational route with its unbounded O(1) PROFILE.

---

## 5. Suggested Document Edits (on merge)

- **T14 §"Toward the RAR"** — lead with: $g_\dagger = c^2/R_0 = cH_0/6$ is the sea's kinematic
  acceleration scale (crossing rate × $c$); the 6 is from the horizon radius. State plainly
  that a uniform sea exerts no net gravitational force, so $g_\dagger$ is kinematic, not
  gravitational — retiring the density/profile route. Remove PROFILE, $9/8$, $(3/16)cH_0$.
- **T14 §"Energy Scale"** — demote the $q=2$-floor-integral-fixes-the-coefficient claim
  entirely; keep the $q=2$ slope as a spectral result only. Keep $\rho_\text{bg}=(\pi/6)
  \rho_\text{crit}$ as a standalone $\hbar$-free identity (dark-energy connection), explicitly
  noting it does **not** enter $g_\dagger$.
- **T14 Open Items** — the coefficient item becomes: "the $cH_0/6$ coefficient follows from
  horizon geometry ($R_0=6c/H_0$) + the kinematic identification $g_\dagger=c^2/R_0$; the open
  task is to **derive $g_\dagger=c^2/R_0$ from the connecton equations of motion** (confirm the
  crossing-rate acceleration is the closure's relaxation scale), rather than assert it
  kinematically."
- **Core §7 / T6 / T15** — $a_0$ status: "$a_0 = cH_0/6$; the **6 derived from horizon
  geometry**, $g_\dagger = c^2/R_0$ identified as the sea's kinematic scale (not gravitational);
  MOND form from the closure. Coefficient no longer O(1)-open at the scale level; the open item
  is a force-law derivation of the kinematic identification." This supersedes both the
  "$cH_0/2\pi$" (old) and the "$(3/16)cH_0$ / O(1)-open" (recent) wordings.
- **Supersedes:** `UPDATE_T14_Profile_Amplitude_Correction.md` (PROFILE is not just open — it
  is retired as the wrong object), `UPDATE_T14_9over8_Artefact.md`, and the coefficient parts
  of `UPDATE_T14_Holographic_Sea_Density.md`. The holographic identity itself stands (§3).

---

## 6. Net Arc of the Coefficient Saga

- $2\pi$ (guessed) → **6** (horizon geometry, derived).
- Coefficient route: gravitational (sea density × $G$ × PROFILE) → **kinematic** ($c^2/R_0$).
- The gravitational route's failures (floor integral frequency², $1/r$-as-$\xi$, enclosed-mass
  overcount, unbounded PROFILE) were all symptoms of forcing $g_\dagger$ to be gravitational.
- Resolution: $g_\dagger$ is kinematic; the sea density and PROFILE never belonged in it.
- **Firm:** $a_0 = cH_0/6$, the 6 from $R_0=6c/H_0$. **Open:** a force-law derivation that the
  closure's relaxation scale equals the kinematic $c^2/R_0$ (replacing the dimensional
  argument).

The "no surprises — we always needed the PROFILE" framing was right that the coefficient hinged
on one unresolved link; the resolution is that the link was mis-identified as gravitational,
and once kinematic, PROFILE is not needed at all.
