
# T19 — Disk Flattening from the Connecton Vertical Spring

*Speculative, within the connecton program (T14, T17). The same coherent $B_c$ that
flattens the rotation curve also stiffens the vertical potential and thins the disk,
while sparing the bulge. Sign and order-of-magnitude of the vertical force are now
resolved via an explicit ringed-current model of $B_c$; the disk/bulge dichotomy
follows from the same coherence gate as T17's morphology chain. Session: 2026-07-01.*

---

## 1. The Mechanism (one line)

The coherent connecton Lorentz field $B_c$ — dipole-like, sourced by the disk's ordered
circulation — produces a **vertical restoring spring** off the midplane. It thins the disk
geometrically (no energy removal), is tied to the *same* $B_c = v_f/r$ that flattens the
rotation curve (no new parameter), and switches off for the bulge. Disk flatness and
rotation-curve flatness become two faces of one field.

## 2. The Vertical Force

For a disk star with velocity $\mathbf{v} = v_r\hat r + v_\phi\hat\phi + v_z\hat z$ and
$\mathbf{B}_c = B_c\hat z$ (vertical), $\mathbf{v}\times\mathbf{B}_c = v_\phi B_c\hat r -
v_r B_c\hat\phi$ — **no $z$-component**. A purely vertical $B_c$ cannot act on $v_z$; it is
a cyclotron field for the in-plane motion.

The vertical force appears because $B_c$ is **not** purely vertical. Sourced by the disk's
coherent circulation ($\mathbf{L}$ along $\hat z$), $B_c$ is dipole-like and off the
midplane acquires a cylindrical-radial component
$$B_{r} = 3C\,\frac{rz}{(r^2+z^2)^{5/2}} \xrightarrow{|z|\ll r} \frac{3C}{r^4}\,z,
\qquad \text{sign}(B_r) = \text{sign}(z).$$
The dominant orbital velocity crossing $B_r$ gives a vertical force
$$F_z = \kappa\,m\,(v_\phi\hat\phi\times B_r\hat r)_z = -\kappa\,m\,v_\phi B_r
= -K\,z,\qquad K = \frac{3\kappa m v_\phi C}{r^4}.$$

**Sign resolved — confining.** The sign of $F_z$ is fixed by the sign of $dB_r/dz$ at the
midplane, i.e. by the connecton current geometry, not by the rotation-curve attractor
(which fixes only $|B_c|=v_f/r$). This was checked explicitly by modelling $B_c$ as the
gravitomagnetic (Biot–Savart) field of coplanar mass-current rings — the disk's actual
circulation. Result: $(dB_r/dz)|_0>0$ at **every** radius, for **every** surface-density
profile tested (exponential, flat, outer-rising), giving $F_z$ **restoring** (toward the
midplane). The disk thins. Physically this is the standard current-loop / magnetic-mirror
geometry: field lines curving back through the plane push a displaced orbiting star back
toward the midplane. (An earlier abstract "curl-free off-disk" derivation had found the
opposite sign; that derivation wrongly applied a vacuum relation, $dB_r/dz=dB_z/dr$, in the
plane where the current actually sits — not vacuum. The ringed-current model computes the
real field and does not make that error.)

## 3. Flattening Without Damping (the no-work resolution)

A static $\mathbf{v}\times\mathbf{B}$ does no work, so it **cannot damp** $v_z$. The disk
thins by a different route: the spring raises the vertical frequency,
$$\omega_z^2 = \omega_\text{grav}^2 + \omega_L^2.$$
At fixed vertical energy, $v_{z,\max}=\sqrt{2E/m}$ is unchanged but the amplitude
$z_{\max}=v_{z,\max}/\omega_z$ **shrinks** as $\omega_z$ rises. Scale height $h\sim z_{\max}$
drops; velocity dispersion $\sigma_z$ is unchanged. **Geometric compression, not damping** —
this is how it evades the no-work theorem.

Magnitude (with $C$ fixed by $B_c(\text{midplane})=C/r^3=v_f/r \Rightarrow C=v_f r^2$):
$$\omega_L^2 = \frac{3\kappa v_\phi v_f}{r^2} \sim 3\,\frac{v_f^2}{r^2},\qquad
\frac{\omega_L^2}{\omega_\text{grav}^2}\sim O(1)\ (\approx3,\ \text{idealization-dependent}).$$
Comparable to gravity's vertical restoring force — a sizeable, not negligible, effect, tied
to the rotation-curve $B_c$ with **no new parameter**.

The ringed-current model confirms the order of magnitude directly: the raw thin-sheet
geometric factor $G(r)=r(dB_r/dz)/|B_z^\text{mid}|$ diverges (thin-sheet singularity), but
regularized at realistic disk thickness ($h_0/R_d\sim0.1$–0.3) it settles to $G\sim1$–5,
consistent with $\omega_L^2\sim3\,v_f^2/r^2$. *Residual wrinkle:* for a razor-thin sheet the
in-plane $B_z$ (rotation-curve field) is small and sign-changing ($\sim r/R_d\sim2.7$), so
the field an orbit feels in-plane and the vertical gradient near the plane may have somewhat
different effective geometries — the rotation-curve $B_c$ is plausibly a smoother
large-scale field than a thin sheet gives. This affects the precise O(1) normalization
$\eta$, not the two headline results: sign confining, magnitude O(1).

## 4. The Transition — Bulge Preserved (two gates, both required)

The vertical-spring-to-gravity ratio is $g_x/g_\text{bar}$ (with $g_x$ the connecton
response from the RAR closure, $g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$), times the
coherence factor $f$:
$$\frac{\omega_L^2}{\omega_\text{grav}^2} \sim \frac{g_x}{g_\text{bar}}\times f.$$

**Radial gate** ($g_x/g_\text{bar}$):
- Inside $r_t$ ($g_\text{bar}\gg g_\dagger$): $g_x/g_\text{bar}\to g_\dagger/g_\text{bar}\to0$.
  Spring vanishes.
- Outside $r_t$ ($g_\text{bar}\ll g_\dagger$): $g_x/g_\text{bar}\to\sqrt{g_\dagger/g_\text{bar}}$.
  Spring dominates.
- Crossover exactly at $r_t$ (ratio $=1/\varphi\approx0.62$ at $g_\text{bar}=g_\dagger$).

**Coherence gate** ($f$, from T17): $f=1$ (ordered disk), $f=\sqrt{\pi/8}\,v_\text{rot}/\sigma
\ll1$ (random bulge).

**Both gates are required.** The radial gate alone does *not* spare an embedded bulge: bulge
and disk overlap in radius, and at shared $r$ the radial gate treats them identically. The
**coherence gate is load-bearing** — the vertical spring needs the coherent $B_c$, which
only ordered (disk) orbits source and feel. A star is flattened iff it is **both** outside
$r_t$ **and** on an ordered orbit. A bulge star (random) is spared everywhere, even where it
overlaps the disk.

**Bulge modelled explicitly.** Modelling the bulge as a rotating spheroid of coherent
mass-current rings (current $\propto\rho_\text{bulge}\,v_\text{rot}$; the random dispersion
averages to zero vectorially, so only the mean rotation sources $B_c$), with Milky-Way-like
values $v_\text{rot}=100$ km/s, $\sigma=100$–150 km/s ($q\approx0.8$ spheroid): the bulge
vertical spring is **$\sim$2–4% of the bulge's own gravity** — safely $\ll1$. **The bulge
keeps its 3D shape.** The sign is the same as the disk's (confining) — a somewhat-flattened
bulge would be *very slowly* thinned, not thickened, consistent with the observed continuum
from round classical bulges to flatter pseudobulges rather than a sharp dichotomy.

The dominant suppression mechanism is **geometry, not coherence.** A round current
distribution spreads its rings over many heights, so their off-plane $B_r$ contributions
**partially cancel**, knocking the vertical spring to $\sim$4% of an equivalent disk on
geometry alone. A single correctly-applied responder-coherence factor
($v_\text{rot}/\sqrt{v_\text{rot}^2+3\sigma^2}\approx0.4$–0.5) trims it a further
$\sim2\times$. So the bulge is spared **primarily because a round current distribution
self-cancels its own off-plane field**; coherence is a secondary trim. This sharpens the
picture: for a *spatially distinct* round bulge, geometry does most of the sparing; the
coherence gate matters most where bulge and disk stars genuinely coexist at the same
location.

*Caveats:* the 2–4% figure depends on the assumed spheroid flattening ($q=0.8$) and scale
ratios, and uses a virial gravity proxy $\omega_\text{grav}\sim\sigma/R_b$, not a solved
potential. Robust content: bulge spring $\ll$ bulge gravity, dominated by geometric $B_r$
cancellation, same (confining) sign as the disk.

## 5. Two Attractors (the morphological dichotomy)

The coherence gate creates feedback:
- **Disk:** thinning → more ordered → higher $f$ → stronger spring → more thinning.
  Self-limiting ($f$ caps at 1, $\omega_L$ saturates). Converges to ordered-thin.
- **Bulge:** random → low $f$ → weak spring → no thinning → stays random. Stable.

Two stable fixed points — **ordered-thin (disk)** and **random-round (bulge)** — of one
coherence-spring feedback, reproducing the observed disk/spheroid dichotomy from a single
field. This complements T17's Lorentz-selection morphology story (same $B_c$, now acting
vertically).

## 6. Cosmic Evolution of the Mechanism

The static picture above is a snapshot. Every ingredient depends on $c(t)$, so morphology is
the *history* of the mechanism, not a fixed state. All scalings follow from the core
cosmology ($c\propto(1+z)^{-1/2}$, $g_\dagger = cH^\text{hor}/3$, invariant $G$, $M$, and
static orbits $r=\text{const}$, T9):
$$g_\dagger \propto (1+z)^{-5/6},\quad v_f\propto g_\dagger^{1/4}\propto(1+z)^{-5/24},\quad
B_c=v_f/r\propto(1+z)^{-5/24},$$
$$\omega_L^2\propto v_f^2\propto(1+z)^{-5/12}\ \text{(spring strengthens with time)},\quad
r_t=\sqrt{GM/g_\dagger}\propto(1+z)^{+5/12}\ \text{(transition shrinks with time)}.$$

**The transition radius sweeps inward through static orbits.** Since orbits are static (T9)
and $r_t$ shrinks, a star at fixed radius crosses from *inside* $r_t$ (Newtonian, no spring)
to *outside* $r_t$ (MOND, spring on) as $r_t(t)$ shrinks past it. The disk (spring-on)
regime therefore grows **outside-in**:
- **Early ($r_t$ large):** most radii sit inside $r_t$ → Newtonian, no vertical spring →
  thick / spheroidal.
- **Later ($r_t$ shrinks):** outer radii cross to $r>r_t$ → spring on → disk forms
  outside-in; inner radii join progressively.
- **Present ($r_t$ small):** extended thin disk outside a residual bulge (the material still
  inside today's $r_t$).

**Coherence lock-in (why the bulge is a fossil).** Material that virialized into random, hot
orbits while inside $r_t$ has low coherence $f$. When $r_t$ later sweeps past it, the spring
is coherence-gated *off* for that material, so it stays bulge-like. Only material that
remained ordered joins the thin disk. The bulge is therefore **frozen-in early-randomized
material**; the disk is **late-ordered material**. Morphology is a fossil of *when* and *in
what dynamical state* each parcel virialized relative to $r_t(t)$.

**Consistency checks.**
- *Adiabaticity:* $r_t$ shrinks by only $\sim1.3\times$ from $z=1$ to now ($\sim8$ Gyr),
  far slower than a galactic dynamical time ($\sim0.2$ Gyr) — consistent with treating
  orbits as static (T9).
- *Not a replacement for dissipative disk formation.* Stars are collisionless; the spring
  *maintains and enhances* order but cannot create it. The initial rotationally-supported
  state must come from dissipative gas settling (standard). This mechanism is an
  **additional** thinning + morphology-locking channel **on top of** ordinary disk
  formation, not a substitute.
- *Outside-in ≠ inside-out contradiction.* "Outside-in" here refers to where the vertical
  *spring activates* (thinning history), not where stars *form* (mass-assembly history).
  Inside-out mass growth and outside-in spring activation are about different quantities and
  do not conflict.

**Evolutionary predictions (parameter-free given the cosmology).**
- Disk/bulge (or thin/thick) boundary radius scales as $r_t\propto(1+z)^{5/12}$.
- Disk thickness evolves with the spring, $\omega_L^2\propto(1+z)^{-5/12}$: high-$z$ disks
  thicker and hotter, thin-disk fraction rising toward $z=0$.
- High-$z$ galaxies more bulge-dominated (larger $r_t$, smaller spring-on zone).
All in the observed direction (late emergence of settled thin disks; hotter high-$z$ disks).

## 7. Falsifiable Predictions

1. **Scale height ↔ rotation-curve flatness** through the shared $B_c$: thinner disks where
   $v_f/r$ (hence $B_c$) is larger. A specific $h$–$v_f$ relation follows once the geometry
   factor is pinned.
2. **Thinness onset at $r_t$:** disks should thin outside the RAR transition radius and
   thicken/round inward toward it. The disk/bulge structural boundary should coincide with
   $r_t$.
3. **Coherence dependence:** partially-ordered systems (low $v_\text{rot}/\sigma$) should be
   proportionally thicker at fixed $r$ and $v_f$ — a test via $v/\sigma$ vs scale height.

## 8. Honest Caveats

- **Disk-thickness dependence of the factor.** The vertical-spring magnitude is O(1)×gravity
  ($G\sim1$–5) for realistic thickness $h_0/R_d\sim0.1$–0.3; the razor-thin limit diverges
  (sheet singularity), so the precise factor depends on disk thickness and the in-plane
  normalization $\eta$. Order confirmed; exact number not pinned.
- **Ringed-current model is minimal.** $B_c$ is modelled as the Biot–Savart field of coplanar
  mass-current rings. Adequate to fix the sign and order of the vertical spring for both disk
  and bulge; a fully self-consistent finite-thickness treatment (resolving $\eta$ and the
  thin-sheet $B_z$ sign-change wrinkle, §2) remains open.
- **Feedback is qualitative.** The two-attractor argument (§5) establishes the fixed points
  exist and are stable in sign; it does not solve the settling dynamics quantitatively.
- **$B_c$ presence during settling.** The mechanism assumes the coherent $B_c$ is in place
  while the disk settles; the co-evolution of $B_c$ and disk order is not modelled.
- **Depends on the connecton program (T14)** and the coherence factor (T17), both speculative.
- **No-damping is exact.** The mechanism is geometric compression, not dissipation; it thins
  ($h$) without cooling ($\sigma_z$). This is a definite, checkable signature (thin but not
  necessarily kinematically cold) and distinguishes it from dissipative disk-settling.
- **Ejection/halo bookkeeping not pursued.** An earlier draft explored whether the flattening
  mechanism's ejected stars are balanced by star-formation replenishment (Milky Way halo
  lifetime). This was dropped as illustrative-only: the ejection timescale depends on several
  poorly-constrained channels (cluster-dynamics multi-body ejection, SN-driven ejection,
  central-BH ejection), none cleanly predictable from this model alone, and there is no
  standing literature discrepancy between ejection budgets and halo mass to motivate pursuing
  it further. Not a result of this topic.

---

## Cross-References

- **T14** — the coherent $B_c$ that flattens the rotation curve also produces the vertical
  spring described here.
- **T17** — the coherence factor $f$ gates disk thinning as well as morphology; the
  two-attractor dichotomy (§5) complements T17's Lorentz-selection morphology story.
- **T9** — the adiabaticity check (§6) relies on static orbits.
