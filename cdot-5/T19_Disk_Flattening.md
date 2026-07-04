# T19 — Disk Flattening from the Connecton Vertical Spring

*Speculative, within the connecton program (T14, T17), as in cdot-4. Checked against the
counting-law change: the mechanism itself (§1–5 below — the vertical spring, its sign
and magnitude, the bulge/disk dichotomy, the two-attractor feedback) is **local,
galactic-scale physics and is confirmed unaffected**, the same pattern already
established for T14's foam-diffusion result and T17's morphology chain. What changes is
§6, "Cosmic Evolution of the Mechanism" — this section propagates $g_\dagger(z)$'s
epoch-dependence, which **is** counting-law-dependent, and T15's cdot-5 rewrite gives a
different (though same-sign) result. §6 is **redone** below using T15's
$g_\dagger(z)\propto(1+z)^{-1}$ in place of cdot-4's $(1+z)^{-5/6}$, with T15's own
percolation-break caveat ($z<z_*\approx1.2$ only) carried through explicitly.*

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

None of this section references cosmic history, $N$, $R$, or the horizon law — it is a
static-geometry, fixed-epoch force calculation, and is unaffected by the counting-law
change exactly as T14's parent derivation is.

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
response from the RAR closure, $g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$, confirmed
unaffected by the counting-law change per T15), times the coherence factor $f$:
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

None of §4 references cosmic history — $r_t$, $g_x$, $g_\text{bar}$, and $f$ are all
evaluated at fixed epoch. Unaffected by the counting-law change.

## 5. Two Attractors (the morphological dichotomy)

The coherence gate creates feedback:
- **Disk:** thinning → more ordered → higher $f$ → stronger spring → more thinning.
  Self-limiting ($f$ caps at 1, $\omega_L$ saturates). Converges to ordered-thin.
- **Bulge:** random → low $f$ → weak spring → no thinning → stays random. Stable.

Two stable fixed points — **ordered-thin (disk)** and **random-round (bulge)** — of one
coherence-spring feedback, reproducing the observed disk/spheroid dichotomy from a single
field. This complements T17's Lorentz-selection morphology story (same $B_c$, now acting
vertically). Unaffected by the counting-law change — a statement about the feedback's fixed
points, not about how $B_c$'s overall amplitude evolves with cosmic epoch (that question is
§6, below).

---

## 6. Cosmic Evolution of the Mechanism — Redone

*This is the one section of the topic that depends on cosmic history rather than a
fixed-epoch force calculation, and therefore the one place the counting-law change bites.
Redone here using T15's cdot-5 result for $g_\dagger(z)$ in place of cdot-4's.*

The static picture above is a snapshot. Every ingredient depends on $c(t)$, so morphology
is the *history* of the mechanism, not a fixed state. The needed input is $g_\dagger(z)$,
which T15 derives (post-percolation branch, $z<z_*\approx1.2$ only) using the one candidate
length ($L$) that has an unambiguous meaning at earlier epochs:
$$g_\dagger(z)=g_\dagger(0)\,(1+z)^{-1}\qquad(z<z_*),$$
— a **different exponent from cdot-4's $(1+z)^{-5/6}$**, but the same sign and the same
qualitative conclusion (the MOND threshold was weaker in the past). Propagating this
through the same chain cdot-4 used, with $r=\text{const}$ (static orbits, T9, unaffected)
and $c(z)=c_0(1+z)^{-1/2}$ (T2, unaffected):
$$v_f\propto g_\dagger^{1/4}\propto(1+z)^{-1/4}\quad(\text{was }(1+z)^{-5/24}),\qquad
B_c=v_f/r\propto(1+z)^{-1/4}\quad(\text{was }(1+z)^{-5/24}),$$
$$\omega_L^2\propto v_f^2\propto(1+z)^{-1/2}\ \text{(spring strengthens with time; was
}(1+z)^{-5/12}),\qquad
r_t=\sqrt{GM/g_\dagger}\propto(1+z)^{+1/2}\ \text{(transition shrinks with time; was
}(1+z)^{+5/12}).$$
The new $r_t(z)$ exponent matches T15's own stated result exactly (T15, "The construction"),
as it must — both are the same calculation, restated here for the vertical-spring chain.

**The transition radius sweeps inward through static orbits.** Since orbits are static (T9)
and $r_t$ shrinks, a star at fixed radius crosses from *inside* $r_t$ (Newtonian, no spring)
to *outside* $r_t$ (MOND, spring on) as $r_t(t)$ shrinks past it. The disk (spring-on)
regime therefore grows **outside-in** — unaffected in direction, sharper in magnitude:
- **Early ($r_t$ large):** most radii sit inside $r_t$ → Newtonian, no vertical spring →
  thick / spheroidal.
- **Later ($r_t$ shrinks):** outer radii cross to $r>r_t$ → spring on → disk forms
  outside-in; inner radii join progressively.
- **Present ($r_t$ small):** extended thin disk outside a residual bulge (the material still
  inside today's $r_t$).

**Coherence lock-in (why the bulge is a fossil) — unaffected.** Material that virialized into
random, hot orbits while inside $r_t$ has low coherence $f$. When $r_t$ later sweeps past
it, the spring is coherence-gated *off* for that material, so it stays bulge-like. Only
material that remained ordered joins the thin disk. The bulge is therefore **frozen-in
early-randomized material**; the disk is **late-ordered material**. This argument is about
the *gating logic*, not the specific exponent, so it carries over unchanged.

**Consistency checks — redone with the new exponent.**
- *Adiabaticity:* at $z=1$ (inside the post-percolation regime, $z<z_*\approx1.2$),
  $r_t(z=1)/r_t(0)=2^{1/2}\approx1.41\times$ (was $2^{5/12}\approx1.30\times$ under
  cdot-4) — still far slower than a galactic dynamical time ($\sim0.2$ Gyr) over the
  $\sim8$ Gyr lookback to $z=1$, so treating orbits as static (T9) remains consistent, with
  slightly more shrinkage than cdot-4 found but nowhere near enough to threaten
  adiabaticity.
- *Not a replacement for dissipative disk formation* — unaffected: stars are collisionless;
  the spring *maintains and enhances* order but cannot create it. This mechanism is an
  **additional** thinning + morphology-locking channel **on top of** ordinary disk
  formation, not a substitute.
- *Outside-in ≠ inside-out contradiction* — unaffected: "outside-in" refers to where the
  vertical *spring activates* (thinning history), not where stars *form* (mass-assembly
  history). These are different quantities and do not conflict.

**Evolutionary predictions (parameter-free given the cosmology) — same direction, new
numbers, and now explicitly bounded to $z<z_*$.**
- Disk/bulge (or thin/thick) boundary radius scales as $r_t\propto(1+z)^{1/2}$ (was
  $(1+z)^{5/12}$).
- Disk thickness evolves with the spring, $\omega_L^2\propto(1+z)^{-1/2}$ (was
  $(1+z)^{-5/12}$): high-$z$ disks thicker and hotter, thin-disk fraction rising toward
  $z=0$.
- High-$z$ galaxies more bulge-dominated (larger $r_t$, smaller spring-on zone).
All in the observed direction (late emergence of settled thin disks; hotter high-$z$
disks), as in cdot-4 — but **only established for $z<z_*\approx1.2$**. Beyond the break,
the pre-percolation branch's own (undetermined) $g_\dagger(z)$ scaling would apply instead
— not derived, matching the same gap flagged in T15 and T17 for their own epoch-dependence
sections. Most direct morphology-evolution observations (disk settling out to $z\sim2$–3)
reach past this boundary, so the quantitative predictions above should be read as
established for the lower-redshift half of the relevant range and provisional beyond it.

**Unresolved competition with T17 — unaffected in substance, inherits the same $z_*$
caveat.** The same growing $B_c$ is credited in T17 with a *radial* effect (Lorentz-
stripping disks into ellipticals, more strongly toward $z=0$) — the opposite morphological
arrow from the vertical thinning/settling claimed here, also strengthening toward $z=0$.
Both are individually defensible (radial ejection of the fastest stars vs. vertical
compression of survivors) and may dominate in different regimes ($r/r_t$, $v_\phi/v_f$),
but the repository does not yet compute which channel wins where — unchanged from cdot-4,
now with the added wrinkle that both channels' evolution laws are themselves only
established below $z_*$. Treat the "thin-disk fraction rising toward $z=0$" claim above as
provisional until the stripping-vs-thinning timescale ratio (T17) is derived.

---

## 7. Falsifiable Predictions

1. **Scale height ↔ rotation-curve flatness** through the shared $B_c$: thinner disks where
   $v_f/r$ (hence $B_c$) is larger. A specific $h$–$v_f$ relation follows once the geometry
   factor is pinned. Unaffected by the counting-law change.
2. **Thinness onset at $r_t$:** disks should thin outside the RAR transition radius and
   thicken/round inward toward it. The disk/bulge structural boundary should coincide with
   $r_t$. Unaffected.
3. **Coherence dependence:** partially-ordered systems (low $v_\text{rot}/\sigma$) should be
   proportionally thicker at fixed $r$ and $v_f$ — a test via $v/\sigma$ vs scale height.
   Unaffected.
4. **Epoch-dependence exponent, redone:** $r_t\propto(1+z)^{1/2}$ and
   $\omega_L^2\propto(1+z)^{-1/2}$ for $z<z_*\approx1.2$ (§6) replace cdot-4's $5/12$ and
   $-5/12$ exponents — a genuinely different, falsifiable normalization for any future
   quantitative test of disk-thinning history, valid only over this restricted range.

---

## 8. Honest Caveats

- **Disk-thickness dependence of the factor.** The vertical-spring magnitude is O(1)×gravity
  ($G\sim1$–5) for realistic thickness $h_0/R_d\sim0.1$–0.3; the razor-thin limit diverges
  (sheet singularity), so the precise factor depends on disk thickness and the in-plane
  normalization $\eta$. Order confirmed; exact number not pinned. Unaffected by the
  counting-law change.
- **Ringed-current model is minimal.** $B_c$ is modelled as the Biot–Savart field of coplanar
  mass-current rings. Adequate to fix the sign and order of the vertical spring for both disk
  and bulge; a fully self-consistent finite-thickness treatment (resolving $\eta$ and the
  thin-sheet $B_z$ sign-change wrinkle, §2) remains open. Unaffected.
- **Feedback is qualitative.** The two-attractor argument (§5) establishes the fixed points
  exist and are stable in sign; it does not solve the settling dynamics quantitatively.
  Unaffected.
- **$B_c$ presence during settling.** The mechanism assumes the coherent $B_c$ is in place
  while the disk settles; the co-evolution of $B_c$ and disk order is not modelled.
  Unaffected.
- **Depends on the connecton program (T14)** and the coherence factor (T17), both speculative.
  Unaffected.
- **No-damping is exact.** The mechanism is geometric compression, not dissipation; it thins
  ($h$) without cooling ($\sigma_z$). Unaffected.
- **New: §6's epoch-dependence exponents are only established for $z<z_*\approx1.2$.**
  Beyond the percolation break, the pre-percolation branch's own $g_\dagger(z)$ scaling is
  undetermined (T15, T23) — the evolutionary predictions in §6/§7 item 4 should be read as
  bounded to this range, not extrapolated further.
- **Ejection/halo bookkeeping not pursued.** An earlier draft explored whether the flattening
  mechanism's ejected stars are balanced by star-formation replenishment (Milky Way halo
  lifetime). This was dropped as illustrative-only in cdot-4 and remains so here — not a
  result of this topic.

---

## Cross-References

- **T14** — the coherent $B_c$ that flattens the rotation curve also produces the vertical
  spring described here.
- **T15** — the epoch-dependence of $g_\dagger(z)$ used in §6, including its $z<z_*$
  validity boundary.
- **T17** — the coherence factor $f$ gates disk thinning as well as morphology; the
  two-attractor dichotomy (§5) complements T17's Lorentz-selection morphology story; the
  unresolved radial-vs-vertical competition (§6) is shared with T17.
- **T9** — the adiabaticity check (§6) relies on static orbits.
- **T23** — the percolation break itself, source of the $z_*$ boundary that now caps every
  epoch-dependence result in this document.
