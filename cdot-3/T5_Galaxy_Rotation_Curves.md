# T5 — Galaxy Rotation Curves

## Observational Background

The rotation curves of spiral galaxies are among the most important observational
inputs in modern cosmology and galactic dynamics. The orbital velocity $v(r)$ of
stars and gas as a function of galactocentric radius $r$ is measured via Doppler
shifts of spectral lines (H$\alpha$, HI 21 cm).

For a galaxy where the visible mass $M(r)$ is concentrated in a central bulge and
disk, Newtonian dynamics predicts:
$$v(r) = \sqrt{\frac{GM(r)}{r}}.$$
At large radii, beyond the visible disk, $M(r) \approx \text{const}$, so one expects a
Keplerian fall-off $v \propto r^{-1/2}$.

**What is observed:** rotation curves are approximately **flat** beyond the optical
disk. The velocity $v(r)$ stays roughly constant out to the largest measurable radii
($\sim 10$–$50$ kpc), rather than falling as Keplerian.

This discrepancy — a factor of several in $v$, or an order of magnitude in enclosed
mass — is one of the most robust and precisely measured anomalies in astronomy. It
is observed in essentially all well-measured spiral galaxies and is correlated with
baryonic content via the Baryonic Tully-Fisher Relation (BTFR):
$$v_\text{flat}^4 = G M_\text{bar} a_0,$$
where $M_\text{bar}$ is the total baryonic mass and $a_0 \approx 1.2 \times 10^{-10}$
m/s$^2$. This tight empirical relation connecting rotation to baryons, with no scatter
related to galaxy size or dark matter content, is the central challenge for any
dark-matter model (see T6).

### Standard explanation: dark matter

In ΛCDM, galaxies are embedded in extended halos of dark matter (non-baryonic,
weakly interacting). The dark matter extends far beyond the optical disk and
provides the additional gravitational pull that keeps rotation curves flat. The NFW
profile (Navarro-Frenk-White) is the standard halo model. Dark matter comprises
$\sim 85\%$ of the matter budget of the universe and $\sim 6\%$ of the total
energy budget (with dark energy at $\sim 68\%$, baryons at $\sim 5\%$).

---

## The Model's Attempts and Their Failure

### The original rotation-curve claim

Earlier versions of the model claimed a rotation-curve solution through a
**retardation mechanism**: the finite travel time of gravity means that the effective
gravitational field at a test mass is sourced by emitters at retarded positions. In a
rotating disk, the near side of a ring rotates towards the observer while the far side
rotates away, creating a near/far asymmetry in the retarded source positions. The
model also considered a term from $\dot{c}/c$: the gravitational "signal" from a ring
element changes as $c$ changes over the transit time, giving a correction of order
$(1 + 2H_0 d/c)$ to the ring's contribution, where $d$ is the emitter-to-emitter
distance within the galaxy.

The claimed result was a "flat floor" $v^2 = 2GMH_0/c$, which at first appeared to
give the correct MOND-like scale.

### Why the mechanism fails: three routes

**1. Scale bug in the floor derivation.** The floor $v^2 = 2GMH_0/c$ was obtained by
taking $r \to \infty$ in the expression $(1 + H_0 r/c)$. But at galactic radii
$r \sim 10$ kpc, the dimensionless ratio is:
$$\frac{H_0 r}{c} \approx \frac{70 \times 10\,\text{kpc}}{c} \approx 2 \times 10^{-6}.$$
The $H_0 r/c$ term only dominates the Keplerian term at $r > c/(2H_0) \sim 4.3$ Gpc —
thousands of times the size of any galaxy. The $r \to \infty$ limit is never
approached within a galaxy.

**2. The local rotation mechanism is real but tiny.** Honest ring integration (using
emitter-to-emitter distances $d$ within the galaxy, not observer distance) shows:
- The strength correction $(1 + 2H_0 d/c)$ at $d \sim 10$ kpc: factor $\sim 4 \times 10^{-6}$.
- The rotation-retardation azimuthal shift ($\omega d/c$ for $v_\text{rot} \sim 200$ km/s):
  factor $\sim 10^{-3}$.
Neither gives the order-unity ($\sim \times 3$) boost needed to flatten rotation curves.
The gap is $10^3$–$10^6$ — a fundamental barrier, not a numerical issue.

**3. The apparent amplification was dimensional sleight-of-hand.** Dividing the bare
retardation effect by the Newtonian well depth produces a ratio that *must* equal
$cH_0$ by dimensional analysis alone — it is the only combination formable from $c$
and $H_0$ with the dimensions of acceleration, regardless of the physics. Explicitly
computing the force from this ratio produces MOND-scale acceleration, but the
computation has no physical content: the "amplification" never appears in the actual
force integral.

Also noted: the original derivation was tied to the galaxy–observer line of sight,
predicting different rotation curves for face-on vs. edge-on galaxies. This is
observationally false — rotation curves are independent of inclination (after
deprojection).

### Current status

**Rotation curves are an unsolved problem in this model.** The $\dot{c}/c$ retardation
route is closed at galactic scales. The model does not currently provide a mechanism
for dark-matter-free flat rotation curves.

---

## What Survives: The Dimensional Coincidence

Even with the mechanism failed, one observation remains: the MOND acceleration scale
$a_0 \approx 1.2 \times 10^{-10}$ m/s$^2$ is numerically close to $cH_0/2\pi$. The
model "knows" this scale via $H_0$, even though it cannot produce an order-one
galactic force from $\dot{c}/c$. This coincidence is discussed in detail in T6.

---

## Possible Paths Forward

Three honest options:

**1. Accept a limitation.** The model may simply need dark matter, like ΛCDM. Rotation
curves would then be explained by dark matter, and the model's distinctiveness would
lie elsewhere (redshift, SN distances, orbital dynamics, etc.). This is an honest
position and not necessarily fatal to the model.

**2. Seek a different mechanism.** A full Liénard-Wiechert / cosmologically-corrected
gravitoelectromagnetic (GEM) treatment — going beyond the $\dot{c}/c$ approximation
to include all retardation terms and the full field structure in a time-varying-$c$
background — is the natural next attempt. This has not been done. Such a treatment
might reveal corrections at a different scale or of a different type than the $\dot{c}/c$
mechanism.

**3. MOND as an emergent phenomenon.** MOND works extremely well phenomenologically
(T6). If the model can eventually derive MOND from its fundamental premises — even if
the specific $\dot{c}/c$ mechanism failed — that would be a success. The model knows
the scale $cH_0$; the challenge is to produce an order-unity force from it at galactic
radii.

---

## Relationship to Mass Budget

With the rotation-curve mechanism failed, the model currently has no mechanism to
replace dark matter. Removing dark matter from the cosmological mass budget leaves
$\Omega_b \approx 0.05$. In ΛCDM this would be catastrophic (no flat space, no
structure formation). In this model:
- Spatial flatness is a **premise** (premise 1), not a consequence of $\Omega = 1$.
  So low density is not a crisis for geometry.
- The model has no Friedmann constraint (there is no scale factor evolution to
  constrain by $\rho$), so $H_0$ and matter density $n$ are decoupled free inputs.
- Structure formation in a static, variable-$c$ universe with only baryonic matter
  has not been computed.

The absence of a dark-matter-free rotation-curve mechanism means the model, in its
current form, likely requires dark matter as an ingredient.

---

## Open Questions

- A full Liénard-Wiechert treatment of gravity in a variable-$c$ background: does it
  produce any galactic-scale correction beyond the $\dot{c}/c$ terms already computed?
- If dark matter is retained, how does the model's halo structure and formation history
  differ from ΛCDM's NFW halos?
- Is there a genuinely different mechanism — e.g., involving the connecton field (T14),
  vacuum polarization in the varying-$K$ background, or modified dispersion relations
  for gravitons — that could produce MOND-like behaviour?
