# T5 — Galaxy Rotation Curves

*Checked carefully against the counting-law change (Core Principles §1): the
retardation-mechanism failure below is verified to be robust — it uses only
present-day $H_0$, $c_0$, and galactic scales, none of which reference the
cosmological counting law's functional form. The connecton/RAR program's *functional*
results (T14/T15) are likewise unaffected in form. But this document's own numerical
anchor — $g_\dagger\sim cH_0/6$, derived from the old law's horizon radius
$R_0=6c_0/H_0$ — does **not** survive intact; see "What Survives" below and T6 for the
full accounting. This is a genuine, load-bearing gap, not a formality, and is now the
top open item for T14's eventual cdot-5 rewrite.*

## Observational Background

The rotation curves of spiral galaxies are among the most important observational
inputs in modern cosmology and galactic dynamics. The orbital velocity $v(r)$ of stars
and gas as a function of galactocentric radius $r$ is measured via Doppler shifts of
spectral lines (H$\alpha$, HI 21 cm).

For a galaxy where the visible mass $M(r)$ is concentrated in a central bulge and disk,
Newtonian dynamics predicts:
$$v(r)=\sqrt{\frac{GM(r)}{r}}.$$
At large radii, beyond the visible disk, $M(r)\approx\text{const}$, so one expects a
Keplerian fall-off $v\propto r^{-1/2}$.

**What is observed:** rotation curves are approximately **flat** beyond the optical
disk. The velocity $v(r)$ stays roughly constant out to the largest measurable radii
($\sim10$–$50$ kpc), rather than falling as Keplerian.

This discrepancy — a factor of several in $v$, or an order of magnitude in enclosed
mass — is one of the most robust and precisely measured anomalies in astronomy. It is
observed in essentially all well-measured spiral galaxies and is correlated with
baryonic content via the Baryonic Tully-Fisher Relation (BTFR):
$$v_\text{flat}^4=GM_\text{bar}a_0,$$
where $M_\text{bar}$ is the total baryonic mass and $a_0\approx1.2\times10^{-10}$
m/s$^2$. This tight empirical relation connecting rotation to baryons, with no scatter
related to galaxy size or dark matter content, is the central challenge for any
dark-matter model (see T6).

### Standard explanation: dark matter

In $\Lambda$CDM, galaxies are embedded in extended halos of dark matter (non-baryonic,
weakly interacting). The dark matter extends far beyond the optical disk and provides
the additional gravitational pull that keeps rotation curves flat. The NFW profile
(Navarro-Frenk-White) is the standard halo model. Dark matter comprises $\sim85\%$ of
the matter budget of the universe and $\sim6\%$ of the total energy budget (with dark
energy at $\sim68\%$, baryons at $\sim5\%$).

---

## The Model's Attempts and Their Failure

### The original rotation-curve claim

Earlier versions of the model claimed a rotation-curve solution through a
**retardation mechanism**: the finite travel time of gravity means that the effective
gravitational field at a test mass is sourced by emitters at retarded positions. In a
rotating disk, the near side of a ring rotates towards the observer while the far side
rotates away, creating a near/far asymmetry in the retarded source positions. The model
also considered a term from $\dot c/c$: the gravitational "signal" from a ring element
changes as $c$ changes over the transit time, giving a correction of order
$(1+2H_0d/c)$ to the ring's contribution, where $d$ is the emitter-to-emitter distance
within the galaxy.

The claimed result was a "flat floor" $v^2=2GMH_0/c$, which at first appeared to give
the correct MOND-like scale.

### Why the mechanism fails: three routes

**1. Scale bug in the floor derivation.** The floor $v^2=2GMH_0/c$ was obtained by
taking $r\to\infty$ in the expression $(1+H_0r/c)$. But at galactic radii
$r\sim10$ kpc, the dimensionless ratio is:
$$\frac{H_0r}{c}\approx\frac{70\times10\,\text{kpc}}{c}\approx2\times10^{-6}.$$
The $H_0r/c$ term only dominates the Keplerian term at $r>c/(2H_0)\sim4.3$ Gpc —
thousands of times the size of any galaxy. The $r\to\infty$ limit is never approached
within a galaxy.

**2. The local rotation mechanism is real but tiny.** Honest ring integration (using
emitter-to-emitter distances $d$ within the galaxy, not observer distance) shows:
- The strength correction $(1+2H_0d/c)$ at $d\sim10$ kpc: factor $\sim4\times10^{-6}$.
- The rotation-retardation azimuthal shift ($\omega d/c$ for $v_\text{rot}\sim200$ km/s):
  factor $\sim10^{-3}$.
Neither gives the order-unity ($\sim\times3$) boost needed to flatten rotation curves.
The gap is $10^3$–$10^6$ — a fundamental barrier, not a numerical issue.

**3. The apparent amplification was dimensional sleight-of-hand.** Dividing the bare
retardation effect by the Newtonian well depth produces a ratio that *must* equal
$cH_0$ by dimensional analysis alone — it is the only combination formable from $c$ and
$H_0$ with the dimensions of acceleration, regardless of the physics. Explicitly
computing the force from this ratio produces MOND-scale acceleration, but the
computation has no physical content: the "amplification" never appears in the actual
force integral.

Also noted: the original derivation was tied to the galaxy–observer line of sight,
predicting different rotation curves for face-on vs. edge-on galaxies. This is
observationally false — rotation curves are independent of inclination (after
deprojection).

### Current status

**The retardation route is closed at galactic scales.** The $\dot c/c$ retardation
mechanism cannot produce flat rotation curves — that failure stands, unaffected by
which cosmological counting law is behind $c(t)$'s history (verified explicitly below).
The model is not without a mechanism, however: the connecton RAR closure (T14/T15)
derives the RAR functional form from selection-junction closure and reproduces it to
$0.020$ dex, parameter-free, with the BTFR as its deep-MOND limit — see T14/T15 for the
mechanism, and "What Survives" below for what changed and what didn't when the counting
law changed.

### Why No Counting Law Variant Rescues the Mechanism — Verified for Connectivity Counting

The $10^6$ failure is **geometric**, not law-dependent, and this is confirmed directly
for the new law, not merely asserted by analogy. The retardation smallness is:
$$\frac{\dot c}{c}\cdot\frac{d}{c}=\frac{H_0\,d}{c}=\frac{d}{c/H_0}
=\frac{\text{galaxy size}}{\text{Hubble radius}}\approx2\times10^{-6}.$$
This ratio uses only $H_0^\text{obs}$ (today's observed value, $70$ km/s/Mpc, unchanged
by the counting-law swap — it is a directly measured quantity, not a derived one) and
$c_0$ (today's speed of light, likewise fixed by definition) and $d$ (a galactic
distance, an astronomical fact). None of these three inputs reference the counting
law's functional form at all — the counting law only determines $c(t)$'s *history*
(what $c$ was at earlier cosmic epochs), and this ratio never looks at that history; it
is evaluated entirely at the present epoch. **The connectivity-counting law therefore
changes nothing about this conclusion, exactly as the occupancy-counting law's own
internal exponent changes ($n=2,3,2/3$) changed nothing about it in cdot-4.** Getting
order unity from a retardation mechanism would still require $\dot c/c\sim10^6H_0$
locally, i.e. $c$ changing on a $\sim10$ Myr timescale, which would destroy redshift
and ages regardless of which counting law governs the cosmological-scale history.

**General conclusion, unchanged:** *No retardation or light-travel-time mechanism can
solve galactic rotation curves for any counting law*, because all carry the
$d/(c/H_0)$ suppression evaluated at the present epoch. Do not pursue counting-law
tweaks or retardation variants for rotation curves — this remains true under cdot-5's
premise 2 exactly as it was under cdot-4's.

### Structural Diagnostic: Distance-Keyed vs. Acceleration-Keyed

The RAR (T15) sharpens this into a structural statement, unaffected by the
counting-law change since it is about mechanism *types*, not about cosmological
history. Observed galaxy dynamics transition from Newtonian to MOND behaviour when the
**local gravitational acceleration** crosses a universal threshold $g_\dagger$ —
Newtonian above that threshold, modified below it. The $\dot c/c$ retardation effect is
keyed to a **distance ratio** ($H_0r/c$ or $H_0d/c$), not to local acceleration. These
are structurally different types of correction:

- A distance-keyed mechanism varies smoothly across a galaxy as $r$ changes, but cannot
  produce a universal acceleration threshold that is independent of galaxy size or
  distance from the observer.
- An acceleration-keyed mechanism switches on wherever the local field drops below
  $g_\dagger$, regardless of location — exactly what is observed.

**Conclusion, unchanged:** retardation-type effects are ruled out not just
quantitatively (factor $10^6$ too small) but structurally (wrong functional
dependence). Any viable dark-matter-free mechanism must be **acceleration-keyed**: it
must modify gravity below a universal threshold, independently of where in the galaxy
that threshold is crossed.

The connecton foam-sea (T14) remains the right *type* — steady-state diffusion carries
no $d/(c/H_0)$ suppression — and robustly delivers Newtonian $1/r$ gravity, a result
that (like the RAR closure's functional form) does not depend on the specific
cosmological counting law, only on the sea existing and diffusing (T14).

---

## What Survives: The Dimensional Coincidence — Reopened, Not Confirmed

**This is the section that changes most under cdot-5, and the change is a genuine gap,
not a housekeeping update.** cdot-4 stated that the MOND acceleration scale
$a_0\approx1.2\times10^{-10}$ m/s$^2$ is matched by $g_\dagger=c^2/R_0=cH_0/6$, with the
coefficient "6" **derived** from the old occupancy-counting law's horizon radius
$R_0=6c_0/H_0^\text{obs}$ (Core Principles §4a in cdot-4) — itself a consequence of the
specific volume-law exponent $n=3$ entering $H_0^\text{hor}=nc_0/R_0$.

**Under connectivity counting, there is no horizon radius $R_0$ playing this role at
all.** $R$ is now only a bookkeeping coordinate (Core Principles §3, cdot-5) — only
differences $R-R_\text{now}$ enter anything physical, and there is no meaningful
"current size of the horizon." The natural candidate replacement is the one length
scale the new law actually provides, $L$ (the fixed recruitment length), giving
$$g_\dagger^{\,\text{naive}}\equiv\frac{c_0^2}{L}=\frac{c_0H_0^\text{obs}}{2}
\approx3.40\times10^{-10}\ \text{m/s}^2\qquad(H_0^\text{obs}=70\ \text{km/s/Mpc}),$$
using $L=2c_0/H_0^\text{obs}$ ($P=2$; Core Principles §4a). **This is $\sim2.8\times$
*too large* compared to the observed $a_0\approx1.2\times10^{-10}$ m/s$^2$** — a real,
quantitative failure, not a 5%-level near-miss the way cdot-4's $cH_0/6$ was. Verified
numerically (both coefficients recomputed independently: cdot-4's $cH_0/6\approx
1.13\times10^{-10}$ m/s$^2$, within $\sim6\%$ of the observed value as claimed; the
naive $cH_0/2$ replacement above is not close).

**Why the naive substitution is probably the wrong move, not just an unlucky number.**
The "$6$" in cdot-4's coefficient was not an arbitrary label on $R_0$ — it encoded the
specific relationship $H_0^\text{hor}=nc_0/R_0$ with $n=3$ (the volume-counting
exponent), baked into "the sea's kinematic acceleration (horizon crossing rate)" via a
physical picture (a photon/connecton takes time $\sim R_0/c$ to cross a horizon of
*size* $R_0$). Connectivity counting has no horizon of a given size to cross — what
grows is *reach*, not occupied volume — so the entire physical picture behind
"$g_\dagger=c^2/R_0$ as a crossing-rate acceleration" may simply not have a
connectivity-counting analogue, rather than having one that happens to need a different
coefficient. Substituting $L$ for $R_0$ mechanically (as done above, to get a number to
check) is not the same as re-deriving the concept, and the $2.8\times$ miss is exactly
the kind of result you'd expect from mechanically relabeling a concept that doesn't
actually transfer.

**This is now the single most important open item inherited by T14's eventual cdot-5
rewrite.** It is *not* resolved here — resolving it requires reconstructing what "the
sea's kinematic acceleration" should mean when the sea is counted by connectivity
rather than occupancy, which is squarely T14's derivation to redo, not something T5 or
T6 can patch by re-labeling a symbol. See T6 for the fuller accounting of what this
does and does not threaten (in particular: the RAR closure's *functional form*, fit
empirically to $g_\dagger\approx1.2\times10^{-10}$ m/s$^2$ as an input, is not directly
threatened by this gap — only the claim that $g_\dagger$'s specific *value* is derived
from $c$ and $H_0$ alone, parameter-free, is).

---

## Possible Paths Forward

Four options, carried forward from cdot-4 with the $g_\dagger$ caveat above now
attached to every one that leans on it:

**1. Primordial black hole dark matter.** The connecton/foam-diffusion route (item 2
below) remains the leading dark-matter-free direction; PBHs are a candidate for the
CMB/genesis mass budget and are potentially complementary rather than competing (T14) —
though the two programs are not yet reconciled at galactic scale (T5/T6's open question
on whether PBH halo mass would double-count the baryon-only RAR, unaffected by the
counting-law change since it is about spatial mass distribution, not cosmological
history). **New caveat:** T13's PBH-genesis argument ($r_s/R\sim1$ crossover) uses the
*same* $R(t)$ that the counting-law change altered the time-history of — the
crossover's timing (T13's own open question, $z_\text{gen}$) needs re-examination
under the new law, not yet done (T13's job for cdot-5).

**2. Dynamical selection — flatness as an evolutionary attractor (most promising
mechanism-based direction).** Rather than demanding the force law produce flat curves
as a static solution, the dynamical selection picture (T14) uses a direct, time-steady
Lorentz-type velocity filter ($v\times B_c$): stars whose tangential velocity makes the
term too strong are ejected outward on a dynamical timescale, with no orbital expansion
needed as an intermediate trigger (orbits are static under invariant $G$, T9 —
unaffected by the counting law). The flat rotation curve is the marginally-bound
surviving population — an evolutionary attractor, not a force-balance solution. The
Tully-Fisher normalization ($v_f^4=GMa_0$) is derived from the transition-radius
geometric mean of $g_\text{mass}$ and $g_\dagger$ — and therefore directly inherits the
$g_\dagger$ gap above: the *functional* derivation (quarter power from where
$r_t\propto\sqrt M$ places the surviving population) survives, but its normalization
depends on the same unresolved $g_\dagger$ value.

**3. A genuinely new MOND mechanism.** The foam-sea has been exhausted as a MOND
source under occupancy counting: five mechanism classes (retardation, linear
diffusion, additive GEM, catalytic cycle, pilot-wave) all give Newton. Whether
connectivity counting opens any qualitatively new door here is unexamined — the
mechanisms tried were about local force laws, not cosmological counting, so there is no
particular reason to expect a different answer, but this has not been checked
directly.

**4. A Liénard-Wiechert / cosmologically-corrected GEM treatment.** Unaffected in
substance by the counting-law change — this is about the local force law's structure,
not cosmological history.

---

## Relationship to Mass Budget

Unchanged from cdot-4: with the rotation-curve retardation mechanism failed, the model
requires dark matter as an ingredient, with primordial black holes from genesis as the
concrete candidate (T13, T16). PBHs are gravitating, pressureless, clustered from
formation, and serve triple duty (CMB wells, galactic dark matter, SMBH seeds) — none of
this depends on the cosmological counting law's functional form, only on the genesis
mechanism (T13), which does need its own re-examination for timing (see item 1 above).
Spatial flatness remains a premise (Core Principles §1, unchanged), not a consequence of
$\Omega=1$; the model still has no Friedmann constraint, so $\Omega_b\approx0.05$ is not
a geometry crisis.

---

## Open Questions

**New top item:**
- **Re-derive "the sea's kinematic acceleration" for connectivity counting.** The naive
  $R_0\to L$ substitution gives $g_\dagger\approx3.4\times10^{-10}$ m/s$^2$, $\sim2.8\times$
  too large — a real failure, not a relabeling exercise. Does connectivity counting
  supply *any* physically motivated acceleration scale close to $1.2\times10^{-10}$
  m/s$^2$, or does the coincidence that made $cH_0/6$ so suggestive under occupancy
  counting simply not carry over? This is squarely T14's derivation to redo (T6 for the
  fuller discussion).

**On the MOND challenge** (unchanged from cdot-4, see T14 for full analysis, T15 for
observational bar):
- All five mechanism classes in the connecton foam-sea give Newton, not MOND. The next
  attempt requires a genuinely new mechanism satisfying the structural constraint:
  acceleration-keyed, $\sqrt M$ coupling, universal scale.
- A full Liénard-Wiechert treatment in a varying-$c$ background: does it produce any
  galactic-scale correction beyond the $\dot c/c$ terms already computed?

**On PBH dark matter** (see T13 for formation, T16 for CMB consequences; timing now
flagged for re-examination above):
- Does the $r_s/R\sim1$ crossover at genesis, under connectivity counting's $R(t)$
  history, still produce a PBH mass function compatible with $\Omega_\text{PBH}\sim0.25$?
- What is the spatial clustering of genesis PBHs, and does it match galactic halo
  profiles at scales $\sim1$–$100$ kpc?
- Can the same PBH population simultaneously explain CMB higher peaks (T16) and
  galactic rotation curves?

**On dynamical selection** (see T14 for derivation, T17 for morphology consequences):
- What is the predicted stripping timescale, and does it match the observed
  disk-to-elliptical ratio across galaxy masses?
- Can the Tully-Fisher normalization be derived from a microscopically computed $B_c$
  source, independent of the now-unresolved $g_\dagger$ value?

**On halo structure** (unchanged):
- If PBH dark matter is accepted, how does the model's PBH halo structure and merger
  history differ from $\Lambda$CDM's NFW halos?
- Does the RAR (T15) survive in a PBH dark matter model, or is its tight baryonic
  correlation evidence against a purely PBH explanation?
