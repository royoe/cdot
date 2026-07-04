# T6 — The MOND Acceleration Scale

*This document's numerical anchor changed under the counting-law transition
(Core Principles §1). Checked carefully rather than assumed: cdot-4's derivation of
$g_\dagger=c^2/R_0=cH_0/6\approx1.13\times10^{-10}$ m/s$^2$ (within $\sim6\%$ of the
observed $a_0$) leaned specifically on the old occupancy-counting horizon radius
$R_0=6c_0/H_0^\text{obs}$. Connectivity counting has no analogous "current horizon
size." The naive replacement ($R_0\to L$) gives $g_\dagger\approx3.4\times10^{-10}$
m/s$^2$ — $\sim2.8\times$ too large, not a near-miss. This document works through why,
and what is and is not threatened by it.*

## Observational Background

Modified Newtonian Dynamics (MOND), proposed by Milgrom (1983), is an empirical
modification of Newtonian gravity that reproduces flat rotation curves without dark
matter. In its simplest form, the effective gravitational acceleration $g$ felt by a
test particle transitions between Newtonian behaviour ($g=g_N$ when $g_N\gg a_0$) and
modified behaviour ($g=\sqrt{g_Na_0}$ when $g_N\ll a_0$), where $g_N=GM/r^2$ is the
standard Newtonian acceleration.

The critical acceleration is:
$$a_0\approx1.2\times10^{-10}\ \text{m/s}^2.$$
This value is empirically determined from galaxy rotation curves and is remarkably
universal — it is the same constant across galaxies spanning orders of magnitude in
mass, surface brightness, and morphology.

### The Baryonic Tully-Fisher Relation

The most precise statement of MOND's success is the **Baryonic Tully-Fisher Relation**
(BTFR), the empirical correlation
$$v_\text{flat}^4=GM_\text{bar}a_0.$$
This arises naturally in MOND: in the low-acceleration regime ($g\ll a_0$), circular
orbit equilibrium gives $v^2/r=\sqrt{GMa_0}/r\Rightarrow v^4=GMa_0$. The relation holds
over five decades in baryonic mass with remarkably small scatter ($\lesssim0.1$ dex),
far tighter than predicted by dark-matter models without fine-tuning.

### The numerical coincidence — cdot-4's version

The MOND acceleration is numerically very close to several combinations of fundamental
constants. Under cdot-4's occupancy-counting law:
$$a_0\approx\frac{cH_0}{6}\approx1.2\times10^{-10}\ \text{m/s}^2,$$
using $H_0=70$ km/s/Mpc: $cH_0/6\approx1.13\times10^{-10}$ m/s$^2$, within $\sim6\%$ of
observed. The coefficient $6$ was not fitted: it came from $R_0=6c_0/H_0^\text{obs}$
(cdot-4 Core §4a), itself a consequence of the volume-law exponent $n=3$ entering
$H_0^\text{hor}=nc_0/R_0$. In the connecton picture (T14), $g_\dagger=c^2/R_0$ was
identified as the sea's kinematic acceleration (a horizon-crossing rate) — the
coefficient fixed by horizon geometry alone, not tuned to match $a_0$. This
cosmological–galactic connection has been noted since Milgrom (1983); cdot-4 made it
structural, not just numerological, via this derivation.

---

## The Numerical Coincidence — Reopened Under Connectivity Counting

**This is the crux of what changed.** Connectivity counting (Core Principles §1) has
no horizon of a fixed *size* $R_0$ at all — $R$ is a bookkeeping coordinate, and only
differences $R-R_\text{now}$ enter any physical formula (Core Principles §3). The
concept behind cdot-4's derivation — "a photon/connecton takes time $\sim R_0/c$ to
cross a horizon of size $R_0$, and $g_\dagger$ is the acceleration associated with that
crossing rate" — has no obvious referent when what grows with the horizon is *reach*,
not occupied volume.

**The naive substitution, computed explicitly (not just asserted to fail).** The one
length scale connectivity counting actually supplies is $L$ (the fixed recruitment
length, Core Principles §1/§3). Mechanically replacing $R_0\to L$:
$$g_\dagger^\text{naive}=\frac{c_0^2}{L}=\frac{c_0H_0^\text{obs}}{2}
\approx3.40\times10^{-10}\ \text{m/s}^2\qquad(H_0^\text{obs}=70\ \text{km/s/Mpc}),$$
using $L=2c_0/H_0^\text{obs}$. This is $\sim2.8\times$ the observed
$a_0\approx1.2\times10^{-10}$ m/s$^2$ — a real quantitative failure. (Both this number
and cdot-4's $1.13\times10^{-10}$ m/s$^2$ were independently recomputed for this
document, confirming cdot-4's own $\sim6\%$ claim and the new mismatch alike.)

**Why the mismatch is a real physics problem, not an artifact of which symbol was
substituted.** The old coefficient "$6$" encoded $H_0^\text{hor}=n\,c_0/R_0$ with
$n=3$ — a relationship specific to the *power-law* structure ($c\propto R^n$, whose
logarithmic derivative is the constant $n$). Connectivity counting's horizon law,
$c(R)=c_0e^{(R-R_\text{now})/L}$, gives $H_0^\text{hor}=c_0/L$ with no analogous
integer multiplying it — effectively "$n=1$" in the old language, and no version of
the old counting-law family had $n=1$ available to check against (the family ran
$n=2/3,2,3$). So the coefficient genuinely changes structure, not just value, when the
counting law changes — there is no reason to expect $R_0\to L$ to preserve a
coefficient that was doing real work encoding $n=3$ specifically.

**What this does and does not threaten.** Three separable claims were bundled together
in cdot-4 and need to be pulled apart now:
1. *"$a_0$ is dimensionally of order $cH_0$."* Survives — this is forced by dimensional
   analysis alone (the only acceleration formable from $c$ and $H_0$) and is
   independent of any counting law.
2. *"$g_\dagger$'s specific numerical coefficient is derived, parameter-free, from
   horizon kinematics."* **Does not survive intact.** cdot-4's specific derivation
   leaned on the volume-law horizon radius; the connectivity-counting analogue, worked
   out above, misses by $\sim2.8\times$. Whether *some* connectivity-counting-native
   construction gets close to $1.2\times10^{-10}$ m/s$^2$ is open and unproven — not
   claimed to be impossible, just not currently in hand.
3. *"The RAR's functional form (the interpolation shape between Newtonian and MOND
   regimes) is derived from connecton indistinguishability, matching McGaugh to
   0.020 dex."* **Survives**, because that derivation (T14) fits the *shape* of
   $g_\text{obs}(g_\text{bar})$ with $g_\dagger$ entering as an empirically-set
   normalization, not something whose absolute value the shape-derivation itself
   fixes. The 0.020 dex agreement is a statement about functional form; it does not, by
   itself, certify where $g_\dagger$'s numerical value comes from.

So: the RAR closure's shape is intact; the specific, celebrated "parameter-free" claim
about $g_\dagger$'s numerical origin is not, and needs a genuine re-derivation (not a
relabeling) from T14, using connectivity counting's actual structure — most plausibly
by returning to first principles (what physical process sets the network's recruitment
length $L$, and does *that* process, rather than a crossing-time picture built for
occupied volumes, generate an acceleration scale close to $a_0$?) rather than
substituting symbols into cdot-4's formula.

---

## The Model's Relationship to MOND

### What the model has

This model naturally contains the scale $c_0H_0^\text{obs}$, regardless of counting
law — the two Hubble constants (Core Principles §4a) still give two natural
accelerations:
$$c_0H_0^\text{hor}=\frac{c_0^2}{L}\approx3.40\times10^{-10}\ \text{m/s}^2,\qquad
c_0H_0^\text{obs}\approx6.80\times10^{-10}\ \text{m/s}^2.$$
The observed MOND scale $a_0\approx1.2\times10^{-10}$ m/s$^2$ is of the same *order* as
both — the dimensional coincidence that motivated the whole program survives — but,
unlike cdot-4, there is currently no derived combination of these two numbers that
lands within a few percent of $a_0$ rather than a factor of a few away. The model
"knows" the MOND scale dimensionally; it no longer visibly "knows" it quantitatively,
pending T14's re-derivation.

### What the model does not have

Unchanged from cdot-4: the model does not currently have a **working force law** that
produces MOND-like behaviour at galactic scales from first principles. The retardation
mechanism (T5) fails by $\sim10^3$–$10^6$ at galactic radii regardless of counting law
(T5, verified explicitly) — not merely quantitatively but structurally (distance-keyed,
not acceleration-keyed). The RAR closure's functional form is derived from connecton
indistinguishability (T14) independent of this gap; the *coefficient* gap above is the
new, additional item.

---

## The Sharpest Statement: The Radial Acceleration Relation (T15)

Unchanged in structure from cdot-4. The RAR (McGaugh, Lelli, Schombert 2016) is the
sharpest, most theory-neutral form of the rotation-curve challenge. Across $\sim150$
galaxies, the observed gravitational acceleration $g_\text{obs}$ is a **tight
one-parameter function** of the Newtonian baryonic acceleration $g_\text{bar}$:
$$g_\text{obs}=\frac{g_\text{bar}}{1-e^{-\sqrt{g_\text{bar}/g_\dagger}}},
\qquad g_\dagger\approx1.2\times10^{-10}\ \text{m/s}^2.$$
Scatter is $\sim0.13$ dex; there is **no residual dependence** on galaxy size,
environment, or morphology. The BTFR is the deep-MOND limit of this relation. The
closure is derived from connecton indistinguishability (T14), matching McGaugh to
$0.020$ dex — a *shape* statement, unaffected by the counting-law change (per the
previous section's point 3). See T15 for the full discussion.

---

## The $\sqrt{M}$ Signature: Why Linear Mechanisms Fail

Unchanged from cdot-4 — this is about the local force law's mathematical structure, not
about cosmological history. The key structural feature of MOND is the Baryonic
Tully-Fisher Relation $v^4=GMa_0$. In the deep-MOND regime this requires the force at
radius $r$ to go as $g_\text{MOND}\propto\sqrt M/r$ — note the $\sqrt M$, not the
$M/r^2$ of Newton. This is MOND's **irreducible nonlinear signature**. Every natural
mechanism the model produces from a *linear* source (retardation terms, linear
diffusion, additive GEM-like fields) gives $M/r$, hence $v^4\propto M^2$ — the wrong
Tully-Fisher slope. The resolution (T14): the quarter power emerges from *where the
surviving population sits* ($r_t\propto\sqrt M$, a geometric-mean transition-radius
argument), not from a non-analytic source coupling — the field equations remain
linear. This survives the counting-law change; its normalization inherits the
$g_\dagger$ gap above.

---

## Physical Interpretation of the Coincidence

Unchanged from cdot-4 — these are literature interpretations, not specific to either
counting law:

1. **Cosmological boundary condition.** Gravity modifies when centripetal acceleration
   equals a "cosmic acceleration" set by $H_0$ — phenomenological, no microphysical
   mechanism.
2. **Vacuum energy / dark energy.** $a_0\sim(c^4\Lambda/3)^{1/2}$; the model has no
   $\Lambda$, so this route is not available.
3. **Gravitational polarization of the vacuum.** The connecton foam-sea (T14) is the
   best candidate from this model: Newtonian $1/r$ from diffusion, with the transition
   scale ideally coming from horizon/network geometry (not a background gradient — the
   homogeneous sea has no net directional force) — this is exactly the piece now
   reopened above.
4. **Inertia modification.** Not this model's framing; not excluded.

---

## The Connecton Sea: The Derived Mechanism, and Where the Gap Sits

The connecton sea = quantum foam (T14) remains the leading mechanism from this model
for rotation curves. Unaffected by the counting-law change:
- Resolves the ballistic/diffusive dilemma, restoring Newtonian $1/r$.
- Is not distance-keyed — free of the geometric $10^6$ suppression (T5).
- The Lorentz-form force law $\mathbf g=\mathbf g_\text{Newton}+\mathbf v_\text{star}\times\mathbf B_c$,
  with $B_c=(GM_\text{bary}\,g_\dagger)^{1/4}/r$, carries the correct $\sqrt M$ in the
  deep-MOND limit; the constitutive interpolation law is derived from connecton
  indistinguishability, matching McGaugh to $0.020$ dex.

**Directly affected:** "Sets the acceleration floor $g_\dagger=c^2/R_0=cH_0/6$ as the
sea's kinematic acceleration" — this specific identification is exactly what no longer
holds under connectivity counting (see above). The background connecton sea's
holographic-standing-population density result, $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$
($\hbar$-free, T14), is a *separate*, standalone identity linking the sea to dark
energy — not the source of $g_\dagger$ — and is not directly addressed by this
document; whether it survives connectivity counting is T14's question, not examined
here.

**BH role, unchanged:** the BH is a co-tracer of the baryonic normalization
$GM_\text{bary}\,a_0$, not a source of $B_c$.

---

## Relation to the BTFR

Unchanged from cdot-4. If the model eventually produces a force law with a MOND-like
regime, the BTFR emerges automatically as the deep-MOND limit. The tight observed
scatter ($\lesssim0.1$ dex, no residual dependence on galaxy size or surface
brightness) strongly constrains the mechanism: it must be baryonic mass alone that
enters. With PBH dark matter as a live candidate (T5, T13, T16), the BTFR becomes a
constraint on that dark component being gravitationally inert with respect to the MOND
interpolation — a required constraint, not a demonstrated mechanism, exactly as in
cdot-4. Quantifying the maximum $\Omega_\text{PBH}(r\lesssim30\,\text{kpc})$ compatible
with the observed RAR scatter remains open (T5).

---

## Open Questions

- **Re-derive $g_\dagger$ for connectivity counting from first principles, not by
  relabeling.** The naive substitution misses by $\sim2.8\times$. Is there a
  connectivity-native construction (perhaps involving the recruitment rate $1/L$
  itself, or the supercriticality condition — both already flagged as open in Core
  Principles §7 for unrelated reasons) that lands closer to $1.2\times10^{-10}$ m/s$^2$?
  This is now the top open item for T14's cdot-5 rewrite, and this document's central
  open question, replacing cdot-4's "confirming the crossing-rate acceleration equals
  the closure's relaxation scale" (which presupposed the crossing-rate picture that no
  longer applies).
- **Transport kernel:** unchanged from cdot-4 — the RAR closure shape is derived from a
  relaxation-time ansatz; a full Boltzmann derivation remains the deepening task (T14).
- **Attractor convergence:** unchanged — does the Lorentz filter genuinely concentrate
  the surviving population at $r_t$ at all radii? Still open (T14, T17).
- **Epoch dependence:** if $a_0\propto c(t)H_0(t)$ under whatever the correct
  connectivity-counting $g_\dagger$ construction turns out to be, galaxy rotation
  curves at high $z$ should show a different MOND threshold than cdot-4 predicted —
  testable with JWST/IFU kinematic surveys, but not computable until the first open
  item above is resolved.
- Does $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ (the holographic sea-density identity,
  separate from $g_\dagger$) survive connectivity counting? Not examined here — T14's
  question.
