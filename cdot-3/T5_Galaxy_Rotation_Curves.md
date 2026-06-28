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

### Why No Counting Law Variant Rescues the Mechanism

The $10^6$ failure is **geometric**, not law-dependent. The retardation smallness is:
$$\frac{\dot{c}}{c}\cdot\frac{d}{c} = \frac{H_0\,d}{c} = \frac{d}{c/H_0}
= \frac{\text{galaxy size}}{\text{Hubble radius}} \approx 2\times10^{-6}.$$
This ratio contains no horizon exponent. A different counting law
$c^a \propto N$ (i.e.\ $c \propto R^{3/a}$) only shuffles $O(1)$ coefficients — the
power $P$, source-strength drift — none of which touch the $10^6$. Getting order unity
from a retardation mechanism would require $\dot{c}/c \sim 10^6 H_0$ locally, i.e.\
$c$ changing on a $\sim10$ Myr timescale, which would destroy redshift and ages.

**General conclusion:** *No retardation or light-travel-time mechanism can solve
galactic rotation curves for any counting law*, because all carry the $d/(c/H_0)$
suppression. Do not pursue volume-law tweaks or retardation variants for rotation
curves.

### Structural Diagnostic: Distance-Keyed vs. Acceleration-Keyed

The RAR (T15) sharpens this into a structural statement. Observed galaxy dynamics
transition from Newtonian to MOND behaviour when the **local gravitational
acceleration** crosses $g_\dagger \sim cH_0$ — Newtonian above that threshold,
modified below it. The $\dot{c}/c$ retardation effect is keyed to a **distance ratio**
($H_0 r/c$ or $H_0 d/c$), not to local acceleration. These are structurally different
types of correction:

- A distance-keyed mechanism varies smoothly across a galaxy as $r$ changes, but
  cannot produce a universal acceleration threshold that is independent of galaxy
  size or distance from the observer.
- An acceleration-keyed mechanism switches on wherever the local field drops below
  $g_\dagger$, regardless of location — exactly what is observed.

**Conclusion:** retardation-type effects are ruled out not just quantitatively (factor
$10^6$ too small) but structurally (wrong functional dependence). Any viable
dark-matter-free mechanism must be **acceleration-keyed**: it must modify gravity
below a universal $\sim cH_0$ threshold, independently of where in the galaxy that
threshold is crossed.

The connecton foam-sea (T14) is the right *type* — steady-state diffusion carries no
$d/(c/H_0)$ suppression — and robustly delivers Newtonian $1/r$ gravity. But every
MOND mechanism attempted within the foam-sea picture (linear diffusion, additive GEM,
catalytic cycle, pilot-wave/broad-spectrum interference) gives Newton, not MOND; the
eikonal calculation closed the last live attempt. The acceleration-keyed requirement
is satisfied but the MOND challenge is unresolved. See T14 for the full analysis and
T15 for the RAR diagnostic.

---

## What Survives: The Dimensional Coincidence

Even with the mechanism failed, one observation remains: the MOND acceleration scale
$a_0 \approx 1.2 \times 10^{-10}$ m/s$^2$ is numerically close to $cH_0/2\pi$. The
model "knows" this scale via $H_0$, even though it cannot produce an order-one
galactic force from $\dot{c}/c$. This coincidence, and its sharpest form (the Radial
Acceleration Relation), are discussed in T6 and T15.

---

## Possible Paths Forward

Four options, in order of current plausibility:

**1. Primordial black hole dark matter (current leading candidate).** The project has
shifted toward accepting dark matter — but as a specific primordial component, not
an unspecified particle. PBHs formed at genesis through relic freeze-out (T13,
Reading 2) are gravitating, pressureless, and clustered by construction — the right
properties for galactic rotation curves and for the CMB higher-peak wells (T16).
The same PBH population would also seed supermassive black holes (T16). This reframes
the question from "what particle is dark matter?" to "did genesis produce PBHs at
$\Omega_\text{PBH} \sim 0.25$?" — gated by the unproven $r_s/R \sim 1$ formation
check of T13.

**2. Dynamical selection — flatness as an evolutionary attractor (most promising
mechanism-based direction).** Rather than demanding the force law produce flat curves
as a static solution, the dynamical selection picture (T14) notes that orbits expand
as $c$ grows ($r \propto c^2$, T9). A velocity-dependent Lorentz-type force acts as
a velocity selector: rings whose speed makes the term too strong are ejected; the
flat rotation curve is the marginally-bound surviving population — an evolutionary
attractor, not a force-balance solution. This dissolves the "static wall" and
requires no fine-tuning for flatness. The Tully-Fisher normalization ($v_f^4 = GM\,a_0$)
remains open (it requires a non-analytic $B_c$ source), but flatness itself is
explained. See T14 for the derivation and T17 for its connection to the M-σ relation
and galaxy morphology.

**3. A genuinely new MOND mechanism.** The foam-sea has been exhausted as a MOND
source: five mechanism classes (retardation, linear diffusion, additive GEM, catalytic
cycle, pilot-wave) all give Newton. Any further attempt must be conceptually new —
not a variant of the mechanisms tried. The structural diagnostic constrains it
severely: it must be acceleration-keyed, nonlinear in the source mass ($\sqrt{M}$
coupling for Tully-Fisher), and produce a universal $\sim cH_0$ scale. No current
candidate satisfies all three. See T14 for what has been ruled out and why, and T15
for the observational bar (the RAR).

**4. A Liénard-Wiechert / cosmologically-corrected GEM treatment.** A fully rigorous
treatment of gravitational radiation in a varying-$c$ background may reveal
corrections of a structurally different *type* (velocity-dependent, not
distance-dependent) that go beyond the $\dot{c}/c$ retardation terms already computed.
The structural diagnostic requires such corrections to be acceleration-keyed; the
Lorentz-form $v \times B_c$ (T14) is the natural candidate structure, but its source
has not been derived microscopically.

---

## Relationship to Mass Budget

With the rotation-curve mechanism failed, the model requires dark matter as an
ingredient — but the project has a concrete candidate: **primordial black holes from
genesis** (T13, T16).

PBH dark matter in this model differs from particle dark matter in ΛCDM:
- PBHs are gravitating and pressureless — correct properties for galactic rotation
  curves.
- They form at genesis through relic freeze-out (Reading 2, T13), not by late-time
  collapse, so their abundance is set by initial conditions at the $r_s/R \sim 1$
  crossover.
- They are clustered from the start (they are the overdense relics), giving them the
  spatial distribution needed to sit in galactic halos.
- The same population serves triple duty: CMB higher-peak gravitational wells (T16),
  galactic dark matter (here and T15), and seeds for supermassive black holes via
  early-universe PBH mergers (T16).

For cosmological accounting: spatial flatness is a **premise** (premise 1), not a
consequence of $\Omega = 1$. The model has no Friedmann constraint ($H_0$ and matter
density are decoupled free inputs), so $\Omega_b \approx 0.05$ is not a geometry
crisis. The question becomes purely structural: does the PBH mass function from
genesis give $\Omega_\text{PBH} \sim 0.25$ at galactic scales? This is gated by
the unproven $r_s/R \sim 1$ formation check (T13 open questions).

---

## Open Questions

**On the MOND challenge** (see T14 for full analysis, T15 for observational bar):
- All five mechanism classes in the connecton foam-sea (retardation, linear diffusion,
  additive GEM, catalytic cycle, pilot-wave/eikonal) give Newton, not MOND. The next
  attempt requires a genuinely new mechanism satisfying the structural constraint:
  acceleration-keyed, $\sqrt{M}$ coupling, universal $\sim cH_0$ scale (T14).
- A full Liénard-Wiechert treatment in a varying-$c$ background: does it produce any
  galactic-scale correction beyond the $\dot{c}/c$ terms already computed? The
  Lorentz-form $v \times B_c$ (T14) is the candidate structure.

**On PBH dark matter** (see T13 for formation, T16 for CMB consequences):
- Does the $r_s/R \sim 1$ crossover at genesis produce a PBH mass function compatible
  with $\Omega_\text{PBH} \sim 0.25$? (T13 load-bearing open question)
- What is the spatial clustering of genesis PBHs, and does it match galactic halo
  profiles at scales $\sim 1$–$100$ kpc?
- Can the same PBH population simultaneously explain CMB higher peaks (T16) and
  galactic rotation curves — or do the two constraints pull toward different PBH masses?

**On dynamical selection** (see T14 for derivation, T17 for morphology consequences):
- The Lorentz-type force produces flatness as an evolutionary attractor (T14). What
  is the predicted stripping timescale, and does it match the observed disk-to-elliptical
  ratio across galaxy masses? (T17 falsifiability handles)
- Can the Tully-Fisher normalization $v_f^4 = GM\,a_0$ be derived from a microscopically
  computed $B_c$ source, or does it remain a phenomenological input?

**On halo structure**:
- If PBH dark matter is accepted, how does the model's PBH halo structure and merger
  history differ from ΛCDM's NFW halos? (relevant to T16 SMBH seeds)
- Does the RAR (T15) survive in a PBH dark matter model, or is its tight baryonic
  correlation evidence against a purely PBH explanation?
