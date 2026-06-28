# Static VSL Cosmology — Working Document v5 (compacted)

*Open points only, numbers preserved from v2. History and full derivations live in
the v2 archive (`Core_Principles_v2.md`, `Open_Problems_v2.md`). This document keeps
only what is currently considered open or live, plus a compact settled-foundation
header so it stands alone. OP-10 was proposed (unit/ontology consistency) but never
recorded as a separate entry — it was absorbed into OP-11 before being written; the
number is intentionally vacant.*

---

## Settled foundation (compact reference)

**Premises.** (1) Static flat space, $a=1$. (2) Horizon counting
$c\propto N\propto R^3$ (volume law, baseline) — *or equivalently the classical
Machian $c\propto M_u$ (rest mass of the universe); the two coincide for invariant $m$
in the present epoch but fork at the temporal extremes — see OP-16.* (3) Invariant rest
mass $m\propto c^0$. (4) Invariant $e,h$; photon frequency conserved in flight
(energy-conserving map frame).

**Forced scalings (from EM + premises).** $c=1/\sqrt{\epsilon_0\mu_0}$ exact at all
epochs, with $\epsilon_0\propto\mu_0\propto K\propto c^{-1}$ (polarization-alignment
argument). Hence $\alpha$ invariant, Bohr radius $\propto c^{-1}$, atomic frequency
$\nu\propto c^{2}$. $G\propto c^{-2}$ is the PV/Dicke-native value (reproduces GR
weak-field).

**Redshift law (squared).** $1+z=(c_\text{now}/c_\text{emit})^{s+2}$; for invariant
mass $s=0$, $1+z=(c_\text{now}/c_\text{emit})^2$, i.e.
$c_\text{emit}/c_\text{now}=(1+z)^{-1/2}$, $K=c_0/c_z=(1+z)^{1/2}$. The redshift power and mass scaling are one
degree of freedom; SN data effectively measure $s$.

**Two Hubble constants (avoid the trap).** Horizon rate
$H_0^{\text{hor}}=\dot c/c=3kR_0^2$ vs observable $H_0^{\text{obs}}=P\,H_0^{\text{hor}}$ ($P=s+2$). "$H_0=70$"
is $H_0^{\text{obs}}$; map horizon $R_0=3P\,c_0/H_0^{\text{obs}}$.

**Transformation formulae (volume law, $P=s+2$).**
$$D_\text{proper}(z)=R_0\big[1-(1+z)^{-1/(3P)}\big],\quad
D_L=(1+z)\,D_\text{proper},\quad D_A=D_L/(1+z)^2.$$
$$\tau(z)=\tfrac{3}{2H_0^{\text{obs}}}\big[1-(1+z)^{-2/3}\big]\ (P{=}2),\quad
\tau_\infty=\tfrac{3}{2}(H_0^{\text{obs}})^{-1}\approx 21\ \text{Gyr}.$$
SN standard candle: $L$ is epoch-invariant in proper units (map-frame
$L\propto c^{2P}$ is a units artifact, not dimming). Deceleration $q_0=1/(3P)>0$.

**Resolved (see v2 for derivations):** OP-1 (time frames; finite proper age
$\approx21$ Gyr — corrected from a two-$H_0$ slip that had halved it to 10.5; the
$3/4$ coefficient carries the *horizon* rate, $\tau=3/(4H_0^{\text{hor}})=3/(2H_0^{\text{obs}})$.
This uses the constant-density volume law and is a **lower bound** — the true
number-Machian age can be larger if the early count was relativistically enhanced,
bounded by $\sim84$ Gyr; OP-16), OP-7 (mass exponent; invariant mass favored),
OP-8 (invariant-mass branch is the recommended core), OP-4 ($\dot\alpha$: $\alpha$
invariant to all orders — every dimensionless QED quantity is $c$-invariant since
$\alpha\propto c^0$ and all lengths $\propto c^{-1}$ in lockstep; predicts zero drift,
consistent with ESPRESSO; tied to the invariant-mass branch). *(OP-3, formerly "rotation
curves resolved," has been **demoted** — see live entry below; the mechanism fails at
galactic scale.)*

**Consistency success:** OP-13 (galaxy size evolution $\propto(1+z)^{-2/P}=(1+z)^{-1}$
at $P=2$, between observed late-type $-0.75$ and early-type $-1.5$ exponents); OP-15
free-particle peculiar-velocity damping $\propto(1+z)^{1/2}$ (vs FLRW $(1+z)^1$ — right
direction, comparable rate).

**Inertia & conservation (OP-15):** the map is the **conjugate frame to standard
cosmology** — standard cosmology conserves rest energy and drops photon energy; the map
conserves photon energy and lets rest energy change (the symmetric flip). From
symmetry: momentum and angular momentum conserved (homogeneity/isotropy), energy **not**
conserved (time-translation broken by $c(t)$). Inertial mass invariant and axiomatic;
model is Machian about $c$, not mass. Free particles decelerate relative to $c$
(peculiar-velocity damping $\propto(1+z)^{1/2}$); bound orbits conserve angular momentum
→ $r\propto c^2$ expansion (OP-13 safe). Energy non-conservation is firm, but its
*interpretation* (connecton absorption vs pure $c$-scaling vs relational-to-$N$) is
open — the "energy reservoir" reading is not asserted.

**Partially withdrawn:** OP-9 (conformal-projection hypothesis — Etherington
refutation rested on the corrected units error; model sits on the Etherington line,
differs only in implied decelerating $H(z)$. Still a genuine rival to FLRW, mild
$q_0$-sign tension, not excluded).

**Speculative directions:** OP-6 (primordial genesis, needs S′), OP-14 (connecton —
candidate unification of gravity and the $c$-field; the **connecton sea = quantum foam**
gives diffusion everywhere → restores Newtonian $1/r$ and dodges the OP-3 geometric
$10^6$. On MOND: every mechanism tried (retardation, linear diffusion, additive GEM,
catalytic cycle, and the pilot-wave/broad-spectrum interference) gives **Newton, not
MOND**. The pilot-wave $\sqrt M$ looked promising but a proper eikonal integral overturned
it — coherent gravitational interference is just classical bending for the strongly-
coupled modes. So: **Newtonian gravity yes, MOND not reproduced**; the model most likely
needs dark matter for galaxies — plausibly the same PBH population as the CMB wells,
OP-18).

---

## Live open problems

### OP-3 — Galactic rotation curves — **DEMOTED: mechanism fails at galactic scale**

*Status reversal. Previously marked "largely resolved" (flat curves from retarded
gravity, no dark matter). Explicit ring integration (carrying $\dot c/c$ through the
intra-galactic emitter-to-emitter distance, per the intended local mechanism) shows
the effect is $\sim10^{-6}$ of what flat curves require. Rotation curves are now an
**open, unsolved problem** in the model.*

**What failed, three ways:**
1. **Original "flat floor" derivation has a scale bug.** The floor $v^2=2GMH_0/c$ was
   obtained by taking $r\to\infty$ in $(1+H_0 r/c)$ — but at galactic $r\sim10$ kpc,
   $H_0 r/c\approx2\times10^{-6}$. The floor only dominates the Keplerian term at
   $r>c/(2H_0)\sim$ Gpc, thousands of times any galaxy. The $r\to\infty$ limit is
   never reached. (Also: that derivation was tied to the Earth–galaxy line of sight,
   giving a tilt-dependent prediction, which is observationally false.)
2. **The intended local mechanism (rotation near/far asymmetry) is real but tiny.**
   Ring integration with the emitter-to-emitter distance $d$ (observer distance does
   not enter): the strength correction $(1+2H_0 d/c)$ contributes $\sim4\times10^{-6}$;
   the rotation-retardation azimuthal shift ($\omega d/c$) contributes $\sim10^{-3}$.
   Flat curves need an order-one ($\sim\times3$) boost. Gap of $10^3$–$10^6$.
3. **Central-well "amplification" was dimensional sleight-of-hand.** Dividing the bare
   effect by the well depth gave a crossover at galactic scale with acceleration
   exactly $cH_0$ — but that ratio has no force-law justification; it is the only
   combination that *must* give $cH_0$. The explicit integration shows the real
   amplification is absent. Withdrawn.

**What survives:** only the dimensional coincidence that the MOND scale $a_0\sim cH_0$
contains $H_0$ — the model "knows" the scale but cannot produce an order-one galactic
force from $\dot c/c$. *Open: either a genuinely different dark-matter-free mechanism,
or accept that the model does not solve rotation curves without dark matter (an honest
limitation, not necessarily fatal).* A full Liénard-Wiechert / cosmologically-corrected
GEM treatment (deferred) is the natural next attempt, but the $\dot c/c$ route is
closed at galactic scale.

**Why no volume-law change rescues it (the $10^6$ is geometric).** Tested whether a
different counting law — $c^a\propto N$, i.e. $c\propto R^{3/a}$ — could fix the factor.
It cannot, for a structural reason: the retardation smallness is
$\frac{\dot c}{c}\cdot\frac{d}{c}=\frac{H_0 d}{c}=\frac{d}{c/H_0}=$ (galaxy
size)/(Hubble radius) $\approx2\times10^{-6}$ — a purely **geometric** ratio that does
*not* contain the horizon exponent. Any counting power only shuffles $O(1)$
coefficients (the $P$ factor, the source-strength drift); none touches the $10^6$.
Getting order unity would require $\dot c/c$ to be $\sim10^6$ larger *locally* ($c$
changing on a $\sim$10 Myr timescale), which would wreck redshift and ages. **General
consequence:** *no retardation/light-travel-type mechanism can solve galactic rotation
curves for any counting law*, because all carry the $d/(c/H_0)$ suppression. A viable
mechanism must come from a different channel entirely — acceleration-keyed (OP-17), not
distance-keyed: e.g. OP-14 connecton/diffusion gravity (if the diffusive regime holds)
or a direct $c$-gradient force-law modification, both speculative. *Do not pursue
volume-law tweaks or any retardation variant for rotation curves.*

### OP-2 — MOND constant $a_0$: numerical value and the $2\pi$ factor

**Depends on OP-3, now demoted:** the floor $v_\text{edge}^4=4G^2M^2H_0^2/c^2$ this
entry rests on is the same one that fails the scale test (OP-3). So the $a_0$
derivation below inherits the scale problem — it is a *dimensional* relation, not a
working galactic prediction. Retained for the dimensional content only.

Rotation floor gives $v_\text{edge}^4=4G^2M^2H_0^2/c^2$ (coefficient 4 from $|g|=2$).
Matching Tully-Fisher $v^4=GMa_0$ and substituting $M_\text{univ}=\tfrac12 c^3/(GH_0)$
gives baseline $a_0=2cH_0$. With the (undetermined) $1/2\pi$ geometric factor,
$a_0=cH_0/\pi\approx2.17\times10^{-10}$ — an 80% **overshoot** of observed
$1.2\times10^{-10}$; matching needs $1/4\pi$. **Order of magnitude ($\sim cH_0$)
robust; precise coefficient undetermined** — the geometric factor was always
reverse-engineered. Redshift law does not affect $a_0$ (present-epoch quantities).
*Open: the dimensional $a_0\sim cH_0$ match is a hint, but with OP-3 demoted there is
no working derivation of the floor it rests on. Treat as unexplained coincidence
pending a real rotation-curve mechanism.*

### OP-17 — Radial Acceleration Relation (RAR) — note, not a result

The RAR (McGaugh–Lelli–Schombert 2016) is the sharpest, most theory-agnostic form of
the rotation-curve challenge: across ~150 galaxies, $g_\text{obs}$ is a tight
one-parameter function of the baryonic $g_\text{bar}$,
$g_\text{obs}=g_\text{bar}/[1-e^{-\sqrt{g_\text{bar}/g_\dagger}}]$, with a single
universal scale $g_\dagger\approx1.2\times10^{-10}$ m/s². Newtonian above $g_\dagger$,
$g_\text{obs}\to\sqrt{g_\text{bar}\,g_\dagger}$ below it. Tiny scatter (~0.13 dex).

**Status: dimensional match; a candidate mechanism now exists (OP-14, unproven).**
Three honest levels:
1. *Scale:* $g_\dagger\sim cH_0$ (specifically $\approx cH_0/2\pi$, also
   $\approx cH_0/6$) — a cosmological acceleration, and $cH_0$ is the model's one natural
   acceleration scale. The model "knows" the scale — but so does MOND and every
   cosmologically-motivated proposal; $cH_0$ is the *only* acceleration formable from
   the constants, so this is inevitability, not a distinctive prediction.
2. *Mechanism:* the $\dot c/c$ retardation route is **dead** (distance-keyed; OP-3). The
   **OP-14 connecton-sea = quantum-foam** picture is the best candidate: diffusion
   restores Newtonian $1/r$ and dodges the geometric $10^6$, and the $\sim cH_0$ scale is
   self-consistent. **But the functional form is the wall** — reproducing the RAR/MOND
   shape needs a low-gradient diffusion nonlinearity $D\propto|\nabla\rho|$ that is
   unmotivated and *disfavored* by the natural reading (which gives Newton, no
   enhancement). So: a candidate that delivers Newtonian gravity but **not demonstrably
   the RAR**. No mechanism currently produces the RAR functional form.
3. *Structural diagnostic (the useful content):* the RAR is keyed to **local
   acceleration** crossing $g_\dagger$ — Newtonian above, modified below. The
   $\dot c/c$ retardation effect is keyed to a **distance** ratio ($H_0 r/c$ or $H_0 d/c$),
   not acceleration. So retardation-type effects are ruled out structurally — which is
   precisely why the OP-14 gradient-keyed (acceleration-keyed) route is the right kind.

**Blocker (explicit):** the $\sim10^{-6}$ magnitude problem of OP-3 must be solved
before anything further is attempted on rotation curves, MOND ($a_0$, OP-2), or the
RAR. These three (OP-2, OP-3, OP-17) stand or fall together on finding an
acceleration-keyed, $cH_0$-scale, order-unity galactic mechanism — which the model
does not currently have. *Do not pursue the RAR connection until the $10^{-6}$ order
problem is resolved.*

### OP-18 — The CMB power spectrum — the hardest constraint, with a candidate path

The CMB angular power spectrum is $\Lambda$CDM's tightest success (a 6-parameter fit to
thousands of multipoles at sub-percent residuals) and the place alternative cosmologies
most often die. For a static $c(t)$ model with no metric expansion, it is the hardest
test on the table — harder than rotation curves, because there the foam-sea at least
gave Newtonian gravity. Broken into four physically distinct ingredients:

**(A) Thermal origin.** Does *not* translate directly: $\Lambda$CDM's CMB is hot from
*compression* (small $a$), but here $a=1$ always — no compression heating. Candidate: in
the low-$c$ genesis epoch (OP-6) all energies scale $\propto c^2$, so "recombination" is
a *$c$-threshold* (atomic binding $\sim$ bath energy, both $\propto c^2$) at a definite
epoch, not a temperature-drop event. Translatable in principle, mechanism unworked.

**(B) Blackbody to $10^{-5}$.** A real constraint: the near-perfect Planck spectrum
needs genuine thermalization in an optically thick early phase. The static model must
reach that optical depth from its genesis-set density rather than from $a^{-3}$
compression. Unworked; hard to fake without real thermalization.

**(C) Acoustic peaks — the crux.** The peak structure (esp. the third) is $\Lambda$CDM's
cleanest "DM exists" argument. **Two author connections substantially improve the
outlook:**
- *First peak translates (Connection 1).* The first peak is the least DM-dependent
  feature — the fundamental baryon-photon plasma mode. Its sound speed
  $c_s=c/\sqrt{3(1+R)}$ is ratio-based, and since every energy scales $\propto c^2$
  (relational principle), the plasma physics is **self-similar under the $c$-scaling**:
  the dimensionless acoustic structure up to the recombination $c$-threshold is the same
  physics, just scaled to the right epoch. So the first peak is reproduced **without
  dark matter**. This narrows the hard problem from "the whole spectrum" to "the
  *relative peak heights*" (the third-peak ratio).
- *PBHs as the DM-role wells (Connection 2).* The higher-peak driving needs *clustered,
  pressureless, non-oscillating* gravitational wells present before recombination — the
  one thing a smooth connecton sea (OP-14, pressureless but horizon-smooth) cannot
  supply. **Primordial black holes** can: gravitating ✓, pressureless ✓, present
  pre-recombination if formed at genesis ✓, and *localized wells by construction* ✓✓
  (no collapse needed). PBH-dark-matter is a mainstream (constrained) idea. **Big
  payoff:** if genesis (OP-6) produces PBHs, they could be *both* the CMB wells *and*
  the galactic dark matter the foam-sea couldn't give (OP-3/OP-17) — unifying the two
  hardest problems, and reframing the model from "no dark matter" to "**dark matter =
  primordial black holes**," a more defensible claim.

**(D) Primordial spectrum** ($n_s\approx0.96$): would come from genesis, not inflation.
Unworked, not obviously forbidden.

**Caveats / checks (honest):** (1) to drive the third peak like DM, PBHs need
$\Omega_\text{PBH}\sim0.25$; PBH-as-all-DM is observationally constrained (microlensing,
evaporation) but viable in specific mass windows (e.g. asteroid-mass
$\sim10^{17}$–$10^{23}$ g). Not free. (2) **Key internal check:** OP-6 carries an
$r_s>R$ cutoff that currently *forbids early localization* — PBH formation must be shown
to be *allowed* by the early dynamics, not forbidden by that same constraint. This is
load-bearing. (3) Origin (A) and blackbody (B) remain unworked and are now the
*secondary* problems; the acoustic-peak quantitative bar (matching relative heights at
$\Lambda$CDM precision) is the existential test regardless of origin story.

**Status:** the model's hardest constraint, but no longer plausibly fatal — the first
peak translates, and PBHs are a concrete candidate for the DM-role features that could
also address rotation curves. The path runs through OP-6: under the **preferred Reading
2**, the $r_s>R$ super-Schwarzschild early phase is the PBH *source* (relics frozen out
at the $r_s/R\sim1$ crossover), not a barrier — so genesis plausibly *does* make PBHs.
The unproven step is whether an overdense lump cleanly yields a black hole (vs. a denser
patch) as the average goes sub-Schwarzschild. Until a spectrum is actually computed,
this is a research program, not an answer.

**Sub-thread to investigate — PBH mergers → supermassive black holes (galaxy cores).**
If genesis produces a PBH population, early-universe PBH *mergers* could build the
supermassive black holes at galaxy cores. Worth investigating because: (i) it addresses
a *real mainstream puzzle* — JWST/quasar surveys find $\sim10^9\,M_\odot$ SMBHs at
$z>10$ that standard stellar-seed accretion struggles to grow so fast; a PBH-merger
seeding channel could turn that problem into a prediction. (ii) **Economy:** the *same*
PBH population would serve three roles — CMB DM-role wells (this OP), galactic dark
matter (OP-3/OP-17), and SMBH seeds. (iii) **Cross-link to OP-14's
criticality-as-license:** if the central SMBH and the halo wells share a common PBH
origin, then "every galaxy has a central critical surface licensing the MOND term while
the halo provides distributed wells" is one mechanism, not a coincidence — and may bear
on the observed M–$\sigma$ relation. *Caveats:* gated behind the same OP-6 $r_s>R$
formation check; the merger rate in a varying-$c$ early universe is unworked; and the
mass budget is severe (asteroid-mass PBHs $\sim10^{-16}M_\odot$ → $10^6$–$10^9\,M_\odot$
SMBHs needs $\sim10^{22}$–$10^{25}$ mergers each, requiring either a higher-mass PBH
spectrum or extended hierarchical merging). Firmly speculative (sits on OP-6 + OP-18);
flagged as a direction, not a result.

### OP-19 — The M–σ relation, bulges, and the disk/elliptical sequence (speculative)

A distinctive set of qualitative predictions that ties OP-14 (the velocity-dependent
Lorentz term + dynamical selection) to OP-18 (SMBH/PBH origin), built on the author's
observation that **bulges are the relevant component for M–σ**. The chain, with each
link checked against observation:

1. **M–σ is a bulge (spheroid) relation, and the bulge grows with BH mass.** Matches the
   mainstream view — M–σ correlates $M_\text{BH}$ with the *spheroid* velocity
   dispersion, not the disk. ✓
2. **Giant ellipticals are the edge of the bulge tail** (classical bulges → ellipticals
   as a sequence; ellipticals are "all bulge"). Consistent with observation. ✓
3. **The Lorentz term explains why giant ellipticals have no disk.** Disks are
   rotation-supported with high *ordered* velocity → large $v\times B_c$ → strong Lorentz
   ejection; spheroids are pressure-supported (random motions, low ordered $v$) → weak
   Lorentz → survive. A galaxy with a very massive BH (strong seed perturbation → strong
   $B_c$) sheds its disk fastest and ends as a pure spheroid (elliptical). This is a
   *distinctive* account of the disk/elliptical dichotomy tied to BH mass — standard MOND
   says nothing like it. ✓ (qualitatively coherent)
4. **Giant ellipticals deviate from the extended M–σ relation because evaporation caps
   galaxy size.** If the outer mass is evaporated (Lorentz ejection), $\sigma$ saturates
   at the remaining bound core while $M_\text{BH}$ keeps growing → $M_\text{BH}$ lies
   *above* the naive M–σ extrapolation. **This matches the observed sign:** giant
   ellipticals / BCGs do show over-massive BHs and a steepening/break at the top end. ✓

**Why it's worth a section:** the four links are *separable* and could have failed
independently, but the chain is internally coherent and matches three real facts (M–σ is
a bulge relation; ellipticals are disk-free; giant ellipticals break M–σ upward) under
*one* mechanism — disks evaporate (high ordered $v$ → strong Lorentz), spheroids survive,
BH mass sets the evaporation strength, and the top-end M–σ break is the evaporation
ceiling. It also unifies with the dynamical-selection prediction (OP-14): the same
ring-ejection that flattens rotation curves strips disks and caps galaxy size here.

**Honest caveat (foregrounded):** *entirely qualitative / sign-level.* No quantitative
derivation that the evaporation timescale, the disk-vs-spheroid Lorentz contrast, or the
M–σ slope and break location come out right; and it rests on the same unproven
$B_c\sim M^{1/4}$ normalization (OP-14, the non-analytic-source wall). So: a striking set
of pre/post-dictions resting on an unproven force law. Falsifiable handles to compute
later: the predicted disk-stripping timescale vs. the observed disk/elliptical fractions
with redshift; the σ-saturation mass scale vs. the observed M–σ break; and whether the
disk/spheroid Lorentz contrast quantitatively tracks the observed morphology–$M_\text{BH}$
correlation.

### OP-4 — Fine-structure drift $\dot\alpha$ — **now resolved: invariant to all orders**

*Redone carefully outside pure PV theory (using the model's own forced scalings, not the
PV $K$-cancellation), at the author's request.*

**Zeroth order.** $\alpha=e^2/(4\pi\epsilon_0\hbar c)$. With $e,\hbar$ invariant
(premise 4) and $\epsilon_0\propto c^{-1}$ (EM-forced), the $1/\epsilon_0$ gives $c^{+1}$
that exactly cancels the explicit $c^{-1}$: $\alpha\propto c^0$, **invariant** — same
result as PV but from the model's *own* scalings.

**First order (Uehling / vacuum polarization) — the part the old entry worried about.**
The worry was that the one-loop correction depends on the Compton wavelength
$\lambda_C\propto c^{-1}$ and so might drift. Treating it carefully dissolves the worry:
the correction depends on the *ratio* of the atomic scale to $\lambda_C$, and in this
model the Bohr radius $a_0\propto c^{-1}$ scales in **lockstep** with
$\lambda_C\propto c^{-1}$, so $a_0/\lambda_C$ is invariant. Cross-checked directly: the Uehling energy
shift $\sim\alpha^5 m_e c^2\propto c^2$ and the gross atomic energy
$\sim\alpha^2 m_e c^2\propto c^2$ scale *identically*, so the fractional shift
$\Delta E_\text{Uehling}/E_\text{gross}\propto c^0$ — invariant. Every atomic energy
(gross, fine-structure, vacuum-polarization) scales as $c^2$ in lockstep; the spectrum
scales **rigidly**, with all line ratios and splittings invariant. No differential
drift exists to measure.

**Robust to all orders.** The invariance rests on two facts:
$\alpha_\text{classical}\propto c^0$, and *every length* $\propto c^{-1}$. Any QED correction at any loop order
is built from powers of $\alpha$ (invariant) and ratios of lengths (invariant) — so
every dimensionless quantity is $c$-invariant to all orders. *This explains the old
"inconsistent magnitudes":* there was never a real drift; the residual was the
additive-vs-multiplicative perturbation error applied to a quantity that is structurally
zero.

**Tied to (the "not pure PV" caveats):** the result holds *given* (1) $e,\hbar$
invariant (premise 4); (2) $\epsilon_0\propto c^{-1}$ *exact* — this is the derived
EM-forced scaling, not a premise, so a correction to the polarization argument could
leave a residual $c$-dependence (the one thing to scrutinize); (3) **$m_e$ invariant
(premise 3).** Under the PV mass branch ($s=-3/2$), $\lambda_C\propto\hbar/(m c)$ no
longer scales as $c^{-1}$, the $a_0/\lambda_C$ lockstep breaks, and $\alpha$ *could*
drift — so $\alpha$-invariance is another discriminator favoring the invariant-mass
branch (joining the finite proper age, OP-1). **Cross-link to OP-18:** the CMB
first-peak translation needs atomic/binding energies to scale cleanly as $c^2$ so
recombination is a sharp $c$-threshold; OP-4 confirms that scaling is exact to all
orders, firming up the first-peak argument. Consistent with the modern bound (ESPRESSO
$\Delta\alpha/\alpha=1.3\pm1.3$ ppm at $z\sim1.15$): the model predicts *zero* drift.

### OP-5 — What sources $c$: the counting law (open) and the $q_0$ sign (resolved)

*This entry bundles two distinct questions; keeping them separate clarifies it. **(A) The
$q_0$ sign — RESOLVED** (below). **(B) Which counting law** $c\propto R^n$ (volume $n=3$,
surface $n=2$, S′ $n=2/3$) — the actual open problem.*

Baseline is volume law $c\propto N\propto R^3$.

**(B) The counting law — open, but now cross-constrained.** The $c\propto N$ rule and
the bulk-vs-surface exponent are an underived first principle. Variant **S′**
($c\propto R^{2/3}$, Compton-thickness self-consistent) uniquely restores a **finite
coordinate-time origin** (a real Big Bang in map time) and has the only internal
rationale of the three. Historically a "free choice," $n$ is now touched by several
this-session constraints:
- *$q_0$ pushes toward volume.* $q_0=1/(nP)$, so S′ gives the *worst* deceleration
  ($+3/4$ at $P=2$) and volume the mildest ($+1/6$) — most vs least SN tension. (Strength
  conditional on the standard-candle question, as in (A).)
- *Genesis/PBH was thought to pull toward S′* (finite origin for PBH formation) — **but
  this pull is now removed.** Under OP-6 Reading 2, PBH freeze-out at the $r_s/R\sim1$
  crossover is *generic to any counting law*, so PBHs do **not** require S′. **The
  tension dissolves: the volume law can have both the best $q_0$ and the PBHs.** S′'s
  remaining advantage is only the finite-coordinate-origin aesthetic, a weaker
  consideration.
- *New constraints to compute (not yet evaluated):* the proper-age count-branch bound
  (OP-1) and the CMB first-peak position (OP-18) both depend on $c(R)$ hence on $n$ —
  so the age and the CMB peak location are now *potential* discriminators of the
  counting law, to be calculated.

Net: the counting law remains open, but the balance has shifted **toward the volume
law** — it carries the mildest $q_0$ tension and (post-Reading-2) loses nothing on
genesis/PBH. S′ is no longer favored by the PBH program. This choice is unconstrained by
the SN result in (A) directly, but is now indirectly constrained by age and CMB.

**(A) The $q_0$ sign — RESOLVED (structural, negative).** Computed $q_0$ for a *general*
power-law horizon $c\propto R^n$ under the squared redshift law + standard-candle
treatment:
$$\boxed{\,q_0 = \frac{1}{nP}\,}\qquad (n>0,\ P=s+2).$$
Volume $q_0=1/(3P)$; surface $q_0=1/(2P)$; S′ $q_0=3/(2P)$ — all **strictly positive**.
S′ is in fact *worse* ($+3/4$ at $P=2$) than volume ($+1/6$). The decisive point is
why no choice escapes: $q_0<0$ requires $n<0$ (light *faster* in the past), but $n<0$
gives $c_\text{emit}>c_\text{now}\Rightarrow 1+z<1$, a **blueshift** — refuted by the
existence of cosmological redshift itself. (The only other escape, $P<0$ i.e. mass
$s<-2$, is exotic and unmotivated.)

**Conclusion: the model structurally cannot reproduce apparent cosmic acceleration.**
Any version with redshift-from-declining-$c$ and a sensible mass scaling is committed
to mild deceleration $q_0=1/(nP)>0$. This is a clean falsifiable prediction, not a
tuning problem; the prior "S′ mimics acceleration, $q_0=-3/2$" was a linear-law
artifact and does not survive.

**What this does / doesn't mean.** It does *not* by itself kill the model: the tension
is mild in magnitude ($+1/6$ for the volume law), and it hangs entirely on the
standard-candle assumption — if SNe Ia are not standard candles to the precision the
acceleration claim needs (a live debate, independent of this model), the
"$q_0\approx-0.55$" being contradicted is itself on softer ground. What it *does* mean:
the model
**cannot mimic dark energy**. It lives or dies on whether cosmic acceleration is real
and standard-candle-clean. *Remaining work:* a real Pantheon+ fit to test the $q_0>0$
prediction directly against the data (rather than a ΛCDM proxy), and a view on the
standard-candle question — though the latter is explicitly out of scope here.

### OP-6 — Primordial genesis and matter/antimatter asymmetry (speculative)

Depends on S′ (finite origin, diverging Compton wavelength at $t=0$). Proposes
$c\propto N$ is the fixed point of a self-consistent matter-creation bootstrap. The PBH
cutoff $r_s>R$ is reinterpreted below (Reading 2). Conjectural; flagged as such.
**Now load-bearing for OP-18 (CMB):** the proposal that primordial black holes supply
the CMB's DM-role wells (and possibly galactic dark matter, OP-3/OP-17, and SMBH seeds)
requires PBH formation *at genesis*.

**The $r_s>R$ cutoff — reinterpreted (Reading 2 preferred).** Computing $r_s/R$ with
firm $G\propto c^{-2}$ and horizon mass $M_u\propto R^3$ under $c\propto R^n$ gives
$r_s/R\propto R^{2-4n}$, which $\to\infty$ as $R\to0$ for *every* law with $n>1/2$
(volume, surface, S′ alike) — so the early super-Schwarzschild condition is **generic,
not S′-specific**. Two readings:
- *Reading 1 (old):* if everything early is super-Schwarzschild, no localized
  sub-horizon collapse is possible → PBH formation *forbidden*.
- *Reading 2 (preferred):* the early super-Schwarzschild universe is a black-hole-like
  *reservoir*; PBHs are not formed by collapse but **frozen out as relics**. As the
  horizon grows and $c$ rises, $r_s/R$ decreases through a crossover at $r_s/R\sim1$;
  the average region exits the super-Schwarzschild state into a normal universe while
  overdense lumps stay super-Schwarzschild and are left behind as black holes. **Generic
  for any counting law** (all cross $r_s/R\sim1$). This *flips the cutoff from a barrier
  into the PBH-formation mechanism.*

Under Reading 2, PBH genesis does **not** require S′ — it occurs at the crossover for
any $n$ — which dissolves the OP-5 counting-law tension (volume law can have both the
best $q_0$ *and* the PBHs). *Honest caveat:* Reading 2 is the favored picture but not
proven. The same "horizon inside its own $r_s$" holds in standard cosmology *without*
making the universe a black hole, because that needs an asymptotically flat exterior a
homogeneous cosmology lacks — so Reading 2's relic-freeze-out relies on the
*inhomogeneity* (an overdense lump acquiring a normal exterior once the average goes
sub-Schwarzschild) doing real work. Whether that cleanly yields a black hole rather than
merely a denser patch is the precise unproven step — and the single highest-leverage
check in the speculative program (it gates OP-18, OP-3/OP-17 PBH-DM, the SMBH thread,
*and* the OP-5 law choice).

**Matter/antimatter asymmetry unsolved** — the headline open problem here. BBN expected
normal pending an $H$-as-freeze-out-timer check (the $H$-substitution may smuggle
assumptions). Conjectural; flagged as such.

### OP-16 — Premise fork: particle count ($c\propto N$) vs. classical Mach ($c\propto M_u$)

*A genuine fork in premise 2, kept open. Both forms are stated; the model does not yet
commit.* Premise 2 has been written as **count** ($c\propto N$, number of particles in
the horizon). The classical Machian alternative is **rest mass** ($c\propto M_u$, total
rest mass of the universe). With invariant $m$ they are *related* by $M_u=Nm$, so the
distinction is only the mean rest mass per particle $\langle m\rangle=M_u/N$ — they
**agree wherever composition is fixed** and diverge only when $\langle m\rangle$
changes. (The author originally chose $N$ only because PV implied non-invariant $m$,
which would have made $N$ and $M_u$ scale differently; with $m$ now invariant that
specific reason is gone — but the fork is real for other reasons below.)

**Where they agree (the swap is free):** all present-epoch continuum cosmology —
redshift, distances, ages, the horizon law, OP-12's Machian content, OP-15's relational
principle. None involve $\langle m\rangle$.

**Where they diverge (the swap is NOT free) — both temporal extremes:**
- **Early universe.** The count is dominated ($\sim10^9$ over baryons) by *relativistic*
  species (relic photons, neutrinos). Whether these contribute is the controlling
  question: if only real massive particles count, $N_\text{massive}=M_u/m$ and the two
  premises coincide; if every quantum counts, they differ enormously in the
  radiation/pair-dominated era. The **genesis/connecton bootstrap (OP-6, OP-14) relies
  on the count reading** — the vast number of primordial pair-creation events boosts
  $c$ by count, not by the near-zero rest mass of transient relativistic pairs. Classical
  Mach would weaken or remove that engine.
- **Far future.** Under **count** (incl. relativistic sea), $N$ keeps growing as the
  horizon swallows more relic quanta → $c$-growth is **self-sustaining, open-ended**.
  Under **rest mass**, once baryogenesis and star formation cease the massive content is
  comoving-fixed → $c$-growth tied to horizon mass intake, and **could stall**. A
  profoundly different long-term cosmology.
- **Proper age.** The $\approx21$ Gyr age (OP-1) assumes constant density (the volume
  law $c\propto R^3$). Under the count branch, an enhanced early relativistic census
  made $c$ larger
  early → the proper age *increases* (bounded: $[21,\sim84]$ Gyr, ceiling at the
  $c\equiv c_0$ limit). Rest-mass branch keeps it near 21. So the fork affects the age
  of the universe too — $\approx21$ Gyr is a lower bound, not the exact value.

**Evidence gathered (bearing on the choice, not deciding it):**
- *Neutrino-runaway objection (against count) is quantitatively negligible.* If
  neutrinos counted, stellar production might inflate $N$ — but integrating the full
  stellar era ($\sim10^{14}$ yr) at today's rate reaches only $\sim10^{-5}$ of the relic
  neutrino sea. Stellar burning fizzles long before it matters. So there is **no
  pressure** to abandon the count premise on these grounds.
- *The count premise keeps a "leg" the model may need:* a two-ended self-sustaining
  engine — the primordial pair-sea bootstrap (genesis) and open-ended far-future
  $c$-growth. Reverting to classical Mach makes the theory more standard and anchors
  $c$ to known masses, but risks losing both.
- *Observable discriminator:* **BBN.** The two premises predict different $c$ during
  nucleosynthesis (full relativistic census vs rest mass only) → different light-element
  yields. The concrete in-principle test. (Full BBN calc deferred.)

**Status:** keep the fork open. Do not revert to classical Mach yet — it would gain
standardness but lose the genesis engine and the open-ended future. (Per the author,
the relativistic-contribution question is left open, not fixed as a premise.)

### OP-12 — Sciama relation fails; the mass-budget conundrum (clarifying)

With physical map quantities (particle horizon $R$, enclosed mass
$M_u=nm\tfrac43\pi R^3$), the Sciama relation $c^2\sim GM_u/R_u$ is violated as $R^{-10}$ — a present-epoch
coincidence, not preserved, and unrescuable with firm $G\propto c^{-2}$. The apparent
"exact identity" via Hubble radius + critical mass is just $\rho_c$'s definition
rearranged. **The model's Machianism is the counting rule $c\propto N$, which is
distinct from and incompatible with gravitational-potential (Sciama) Machianism.**

Mass budget: the static model has **no Friedmann constraint** — flatness is by
construction, so the total density is not fixed by a critical-density requirement and a
low value is **not** a crisis. Price: $H_0$ and matter density $n$ are decoupled free
inputs (no Sciama link), so the model has less explanatory economy than FLRW on this
point.

**The dark-matter stance has shifted this session — two positions, now leaning to the
second:**
1. *Baryons only* ($\Omega_b\sim0.05$, no dark matter). The original aspiration. With
   OP-3 demoted and OP-14's foam-sea giving Newtonian $1/r$ but not MOND, this requires
   either a weak-field cooperativity that has not been found, or living with unexplained
   rotation curves.
2. *Primordial-black-hole dark matter* ($\Omega\sim0.3$, the PBH population of OP-18 /
   OP-6). PBHs would do triple duty — CMB DM-role wells (OP-18), galactic dark matter
   (OP-3/OP-17), and SMBH seeds (OP-18 sub-thread) — a single primordial component
   rather than three separate fixes. This is *not* "no dark matter"; it is "dark matter
   is baryonic/primordial in origin," a different and arguably more defensible claim.
The model is currently leaning toward (2): it is more economical (one population, three
jobs) and rescues the CMB, at the cost of the pure no-DM aspiration. Both are gated
behind the OP-6 $r_s>R$ check (does genesis actually form PBHs?). So the honest current
budget is *either* $\Omega_b\sim0.05$ with no DM *or* $\Omega\sim0.3$ with PBH-DM — not
settled.

*Open: what pins $n$ (the baryon density)?* — now joined to *what sets the PBH abundance
$\Omega_\text{PBH}$?* (OP-18), since the two together set the total budget.

### OP-14 — The "connecton": a candidate unification of gravity and the $c$-field (speculative)

*Status: speculative, like OP-6, but with a real logical spine and several
quantitative checks. Produced a **specific negative result** at its center, which is
why it is worth recording. Not adopted into the core; a research direction.*

**The idea.** Gravity may share the same substrate that drives $c(t)$. Posit a field
quantum — the **connecton** — that represents a "connection" between points: massless,
near-zero energy, propagating at local $c$, **conserved in number** (never destroyed),
continuously emitted and momentarily captured/re-emitted by massive particles (a brief
virtual $e^+e^-$ pair, re-emitted after the uncertainty time). The horizon is the
dominant source. The global termination/turnover rate sets $\dot c/c = H$ (the
cosmology, premise 2); local structure in the field is gravity.

**Energy scale (non-tunable).** A connecton whose wavelength equals the horizon has
frequency exactly $H_0$ and energy $\hbar H_0 \approx 1.5\times10^{-33}$ eV — the
minimal quantum of the observable universe, a scale that independently appears in
holographic/IR-cutoff discussions. So "low but finite energy" is fixed by the horizon,
not a free knob. The connecton field has a **spectrum**: a dominant horizon-wavelength
population (primordial, permeating from the first moment) plus a short tail from matter
created at later (smaller-horizon) epochs. The volume law's weak $(1+z)^{-1/6}$ horizon
scaling makes the spectrum narrow (within ~3× of the horizon wavelength).

**Scorecard against the four classic Le Sage objections:**
- **Thermal catastrophe — SOLVED exactly.** Strict conservation (capture + re-emit, no
  destruction) means zero net energy absorbed. Poincaré's objection does not apply.
- **Drag — solved.** Force is a field/delay effect, not momentum transfer; the
  near-zero momentum that kills drag is built in.
- **Equivalence principle — clean.** Source strength $\propto$ particle count $\propto$
  mass (invariant mass), composition-independent.
- **Distance law ($1/r$) — CONDITIONAL; this is the central open problem.**

**The $1/r$ derivation and its obstacle.** If connectons *diffuse* (captured and
re-emitted with **randomized direction**, conserved), the steady-state parked-density
perturbation around a mass obeys Poisson's equation $\nabla^2\phi = -S\,\delta^3(x)$,
whose Green's function is exactly $\phi = S/(4\pi r)$ — Newtonian $1/r$, with
$S\propto M$. This is rigorous **in the diffusive regime**, and connects the mechanism
to
PV/Dicke gravity (the connecton capture-delay *is* the microscopic refractive index,
$g\propto\nabla c/c$).

**But the regime is wrong in the natural case.** $1/r$ needs diffusion (short mean free
path, matter opaque to connectons). Weak, long-range gravity needs transparency
(ballistic transport). A single isotropic re-emitter in transparent space produces a
**free-streaming $1/r^2$ density halo** → wrong force law ($1/r^3$). The two
requirements are linked by the same capture cross-section and pull opposite ways — a
cousin of the Le Sage dilemma, surviving in the distance law even though conservation
killed it for the thermal/drag problems. Author's refinements (vacuum doesn't
randomize but matter does; connectons numerous but matter transparent) do **not** break
this: matter-only randomization gives diffusion *inside* bodies but ballistic transport
in the empty gaps where long-range gravity acts.

**Escape evolved — the connecton sea = the quantum foam (promising).** Identify the
"dense self-interacting connecton sea" with the **quantum foam** (the vacuum's virtual
$e^+e^-$ pairs) — no new ontology, it already exists. Connectons scatter off the foam,
whose density $\sim1/\lambda_\text{Compton}^3\sim10^{37}\,\text{m}^{-3}$ gives a
sub-Compton mean free path → **diffusion everywhere, including "empty" space**, while
ordinary matter is only a weak perturbation (gravity stays weak). This **resolves the
ballistic/diffusive dilemma** and **dodges the geometric $10^6$** that killed the
retardation family (OP-3) — a steady-state diffusion profile is not a light-travel-time
effect, so it carries no $d/(c/H_0)$ suppression. The $1/r$ potential is restored
(point sink in a diffusive medium, $\nabla^2\rho=S\delta^3\Rightarrow\rho\propto1/r$),
weak and EP-clean. This is the first mechanism in the project that is both the right
*type* (not distance-keyed) and free of the geometric death.

**Toward the RAR (OP-17) — a gradient-keyed transition gives a universal $\sim cH_0$
scale.** Pure diffusion is just Newton ($1/r^2$) — no MOND. A transition keyed to
*density* (mass perturbation = background) fails: it gives a **mass-dependent** scale
$g_t\propto1/M$, wrong for the universal RAR. But keying it to *gradients* works: the
cosmic sea rises with horizon distance, carrying an intrinsic background gradient
$|\nabla\rho_\text{bg}|\sim\rho_\text{bg}H_0/c$ (mass-independent, cosmological). Where
the mass's connecton-density gradient drops to this background, the transition
acceleration is $g_t=\kappa\rho_\text{bg}H_0/c$ — **mass-independent**, and $\sim cH_0$
if $\kappa\rho_\text{bg}\sim c^2$ (the natural energy-density scale). This is the right
*structure* for the RAR (universal $\sim cH_0$ onset), and it avoids both failure modes
that sank earlier attempts (distance-keying and mass-dependence). **Open pieces (do not
overclaim):** (a) the scale rests on $\kappa\rho_\text{bg}\sim c^2$, now *sharpened*:
since $\kappa\rho_\text{bg}$ is dimensionally a velocity² (forced by the force law
$g=\kappa\nabla\rho$), this is the single physical statement $V=c$ — the sea's
characteristic velocity is the connecton propagation speed. Half of it is **structural**
(the diffusion constant $D=cL/3$ supplies one power of $c$, since connectons move at
$c$); the other power is a concrete **microphysical closure condition**
$4\pi G L\rho_\text{bg}/(3\sigma)=c$ (linking per-mass emission $\sigma$, mean free path
$L$, background density $\rho_\text{bg}$) — plausible, not yet derived, but a specific
target rather than a free fit. This is *not* the OP-3 dimensional sleight-of-hand:
there the "amplification" had no force-law backing; here $g=\kappa\nabla\rho$ is the
actual force law and $V=c$ has definite physical meaning (the sea's signal speed).
(b) this gives the *scale*, not the *functional form* — whether the nonlinear diffusion
yields the deep-MOND $\sqrt{g_\text{bar}a_0}$ law and the RAR interpolating function is
unproven and needs the nonlinear diffusion solved; **(caveat 2, examined — the wall.)**
The deep-MOND law requires the low-gradient diffusion to take the *specific* form
$D\propto|\nabla\rho|$ (equivalently Bekenstein-Milgrom $\mu(x)\to x$). *If* it does,
everything closes beautifully: $g\propto1/r$ (flat curves), $v^4=GM\,a_0$ (Baryonic
Tully-Fisher), and $a_0=\kappa\rho_\text{bg}H_0/c=cH_0$ — the **same** $V=c$ condition
fixing the scale in *both* regimes (a real self-consistency). **But** no independent
physical reason for $D\propto|\nabla\rho|$ was found; worse, the natural reading
("a small mass-gradient riding on the large cosmic background gradient") gives back
*linear* response — Newton-on-a-background, **no MOND enhancement** — and the obvious
nonlinearity (flux saturation) pushes the wrong way. So the honest status: the foam-sea
robustly delivers **Newtonian $1/r$ gravity** (real progress — dodges the $10^6$, gives
EP), but the **MOND/RAR functional form does not fall out** and is currently *disfavored*
by the natural reading. The scale self-consistency says only "if MOND, then $a_0=cH_0$,"
not "therefore MOND."
(c) the background-gradient estimate assumes isotropic horizon-tracking (local
overdensities would add scatter but not shift the trend — acceptable).

**The obstruction, pinned (additive/GEM route examined).** An *additive* two-component
force $g=g_N+g_\text{cosmo}$ (GEM-inspired: leave Newton intact, add a cosmological
piece) is the right *framing* — it avoids wrecking Newton and shows the second term must
go as $1/r$ (a constant gives rising curves, the old failed floor; $1/r^2$ just rescales
$G$). **But it relocates the wall precisely onto the mass scaling:** the MOND term must
be $g_\text{cosmo}\propto\sqrt{M}/r$ (this $\sqrt M$ is what gives Tully-Fisher
$v^4=GM\,a_0$ and is MOND's irreducible signature). A *linear* additive term — the
literal GEM analogue, since GEM is a linear theory ($g_\text{magnetic}\propto$ mass
current $\propto M$) — gives $M/r$, hence $v^4\propto M^2$, the **wrong** Tully-Fisher
slope. **General diagnosis:** every mechanism the model naturally produces (retardation,
linear diffusion, additive GEM-like terms) is *linear in the source mass*, and MOND's
$\sqrt M$ demands a **nonlinear source coupling**. This is why the *scale* keeps matching
(dimensional, linear-friendly) while the *functional form* keeps failing (needs
nonlinearity). The one genuine nonlinearity the model has is the **self-interacting**
connecton sea (connectons scatter off each other, not just off matter). Whether that
self-interaction can generate a $\sqrt M$ coupling — the mass's perturbation modulated
by the background sea it is embedded in — is unproven (the naive cross-term
$|\nabla\rho_\text{tot}|^2$ stays linear in $M$) but is the **one concrete place a
$\sqrt M$ could hide**, and the live next target.

**Catalytic-cycle calculation (attempted, negative — informative).** Tested the
specific self-interaction the author favors: connectons *catalyze* transient virtual
$e^+e^-$ pairs (conserved on re-emission), with the pair as the localized intermediate
resolving the wavelength objection (horizon-scale connectons can't elastically scatter,
but they can co-catalyze a Compton-sized pair). Three stages: (1) the threshold density
of states for pair creation gives a *real* non-analytic $\sqrt{E_\text{exc}}$ — exactly
the kind of $\sqrt{}$ MOND needs. (2) **But** $E_\text{exc}$ is set by the pair's own
energy ($\sim2m_ec^2$, MeV), which swamps the galactic field-gradient energy
($|\nabla\phi|\lambda_C$) by $\sim10^{33}$ — so the $\sqrt{}$ is a *constant* prefactor,
not $\sqrt{|\nabla\phi|}$. (3) The collective/coarse-grained version gives *linear* drift
(Einstein relation $v_\text{drift}\propto F$) → Newton; the only route to a *sublinear*
($\sqrt{}$) collective response is **cooperativity** (one pair's formation enhancing
neighbors') — i.e. criticality, which belongs at the strong-field (black-hole) end, not
the weak-field MOND end. **Verdict:** the catalytic cycle robustly gives Newtonian
gravity but **not MOND** — the $\sqrt M$ requires a *weak-field cooperative/non-analytic*
coupling that this mechanism (like retardation, linear diffusion, additive terms) does
not supply. Not a proof the model can't do MOND, but a precise statement of what is
missing: a weak-field cooperativity in the foam, unmotivated so far, that criticality
supplies only at the strong end.

**Author's note — criticality as a *license*, and the Lorentz-force target structure.**
Two refinements worth keeping for future tries:
*(i) Two roles for criticality.* Every galaxy has a central black hole = a strong-field
critical surface. **Role 1** (BH critical region *sources* the effect) is ruled out — it
would make the flat-curve amplitude scale with $M_\text{BH}$, killing the universal
$a_0$. **Role 2** (criticality is an *existence condition* that *licenses* the
non-analytic term, while the *scale* is horizon-set, $a_0\sim cH_0$) survives that
objection: $a_0$ stays universal. This dissolves the catalytic-calc dead end (which
needed "weak-field cooperativity = strong-field criticality"): the criticality need only
*exist somewhere* to license the term, not *operate* in the weak field. **Open:** a
localized BH critical surface ($\sim$AU) licensing a coupling that acts at $\sim$10 kpc
requires *licensing-at-a-distance* — a global boundary/topological condition, not a
local source. Conceivable, unproven.
*(ii) The target equation (GEM/Lorentz form).* The two-component law sought is
$\mathbf g = \mathbf g_\text{Newton} + \mathbf v_\text{star}\times\mathbf B_c$, with
$\mathbf B_c$ a magnetic-like component of the $c$-field — a *velocity-dependent*
cross-product term (genuinely different from the density/gradient couplings tested; it
is the natural gravitomagnetic structure). Worked through: a flat curve needs
$B_c\sim v/r$, i.e. $B_c\propto(GM\,a_0)^{1/4}/r$, and then $v\times B_c=\sqrt{GM\,a_0}/r$
**does carry the correct $\sqrt M$** (deep-MOND + Tully-Fisher). So the $v\times B_c$
form *accommodates* the MOND signature — but it **repackages** the difficulty: $B_c$ must
then be sourced $\propto M^{1/4}$, an even more non-analytic source scaling than
$\sqrt M$. *Conjecture (connecting (i) and (ii), unproven):* criticality-as-license may
be exactly what permits a non-analytic $B_c$ source, with the $v\times B_c$ structure
then delivering a velocity-dependent force carrying $\sqrt M$ and a horizon-set $a_0$.
This is the first framing where velocity-dependence, the $\sqrt M$ requirement, and a
universal $a_0$ coexist without immediate contradiction — a direction for the next try,
not a result.

**Lorentz route revisited in detail (after the eikonal reversal) — same wall, but a real
M–σ connection.** The eikonal result killed the *interference* route but is silent on a
genuinely *velocity-dependent* force, so the two-component law
$\mathbf g=\mathbf g_N+\mathbf v\times\mathbf B_c$ was re-examined. Findings: (1) a *standard* gravitomagnetic $B_c\sim a_0/c$ is
$v/c$-suppressed ($\sim10^{-3}a_0$) — fails, as in the Session-3 GEM digression. (2) The
$B_c$ actually needed is $B_c=\sqrt{g_N a_0}/v=(GM a_0)^{1/4}/r=v_\text{flat}/r=\omega_\text{flat}$ — the orbital angular frequency (so it must be sourced independently
and *checked* to equal $\omega$, else it is circular). (3) **Striking consistency:** the
observed **M–σ relation** $M_\text{BH}\sim\sigma^4\sim v_\text{flat}^4\sim GM a_0$ gives
$(M_\text{BH})^{1/4}\sim(GM a_0)^{1/4}$ — *exactly* the needed amplitude. So *if* $B_c$ is
sourced by the central black hole as $B_c\sim M_\text{BH}^{1/4}/r$, the Lorentz route
yields MOND + Tully-Fisher **and** M–σ emerges as the BH↔flat-curve consistency
condition — the concrete realization of the criticality-as-license idea (strong-field BH
sets the field that produces the weak-field curve). **But the wall is only relocated, not
breached:** $B_c\sim M^{1/4}/r$ is a *non-analytic quarter-power source*, which no linear
gravitomagnetic mechanism provides (linear gives $M^1$) — the same non-analyticity as the
$\sqrt M$. And per the eikonal lesson, this was reached by *scaling arguments*:
$B_c\sim M_\text{BH}^{1/4}/r$ is **not derived**. So $v\times B_c$ *accommodates* MOND, does not
*produce* it. **What is genuinely new:** the M–σ relation as a falsifiable consistency
prediction linking BH mass to the flat-curve velocity — worth keeping even though the
mechanism is undishown. Net: consistent with the program's conclusion (no derived MOND;
model likely needs PBH dark matter, OP-12/OP-18), but the $v\times B_c$/M–σ thread is a
real checkable structure, not a dead remnant.

**Pilot-wave interference + the broad connecton spectrum — the first surviving MOND
mechanism (staged calculation).** Triggered by two corrections: (i) the catalytic calc
missed the *interference* aspect (transaction amplitude depends on the path bundle from
the horizon, double-slit style; a mass *shadows* part of the horizon); (ii) the
horizon-only spectrum was an $N$-argument artifact — with $m$-dependence allowed,
connectons are created at the horizon but absorbed/reemitted at every vacuum point,
building a broad spectrum from $\lambda_C$ to $c/H_0$. Done in stages (both recorded, to
locate the nonlinearity):
- *Stage 1 (uniform vacuum):* detailed balance + number conservation + scale-invariance
  → cascade index $p=1$ (equal connectons per octave); pair-creation **cutoff** at
  $\lambda_C\propto c^{-1}$ (moves with local $c$ — author's point); null force
  (validated). $p=1$ also gives the $c$-feeding rate $\propto c$ via the trigger-
  frequency weighting — the closure is satisfied, not imposed.
- *Stage 2 (perturbative gradient on uniform background):* **null for MOND**, as the
  author predicted. $c$-feeding is dominated by the shortest connectons, which track
  local $c$ smoothly → Newton; the cutoff-shift channel carries no weight. A uniform-
  vacuum perturbative treatment cannot produce MOND.
- *Stage 3 (black holes in the background, nonlinearity ab initio):* black holes
  resonantly absorb/scatter connectons at $\lambda\sim r_{s}$ — *exactly* the coherent
  sweet spot $\lambda^*=2\pi GM/c^2\sim r_s$ (a clean, distance-independent result: the
  wavelength that interferes coherently with a well is the well's own gravitational
  radius). The BH population thus *injects spectral weight at the MOND scale* — the
  ingredient Stage 2 lacked. With it, the coherent coupling scales as **$M^{-1/2}$ →
  $v^4\propto GM\,a_0$, the $\sqrt M$ Tully-Fisher signature appears for the first time
  in the project.** This concretely *links the criticality-as-license note to a
  mechanism*: the strong-field BHs shape the spectrum that produces the weak-field term.

**Status — the coherence factor was derived properly, and it OVERTURNS the $\sqrt M$:
the mechanism gives Newton, not MOND.** The Stage-3 $\sqrt M$ rested on a *scaling
estimate* of the coherence factor $f$ (flagged at the time as the least-rigorous step).
Doing the actual eikonal interference integral: a connecton crossing the well at impact
parameter $b$ has eikonal phase $\Phi(b)=(2\pi/\lambda)(GM/c^2)\cdot2\ln(L/b)$, giving a
deflection $\theta=2GM/(c^2 b)$ that is **wavelength-independent** — ordinary classical
gravitational bending. The spectrum washes out; there is no special enhancement at
$\lambda^*$. Checked the one escape (the diffraction regime, where the eikonal fails,
$\lambda>r$): the sweet spot $\lambda^*\sim r_s\sim10^{15}$ m is strongly coupled
($\delta\phi\sim1$) but sits at $\lambda^*\ll r$ (eikonal → Newton), while the only
modes in the diffraction regime ($\lambda\sim c/H_0\sim10^{26}$ m) have
$\delta\phi\sim10^{-12}$ (negligible). **No wavelength is both strongly coupled and
diffractive**, so $f\to0$ (Newton). The $r^{1/2}$ discrepancy was the symptom of the
scaling estimate being wrong, not a small fixable gap. *Lesson (recurring this
project): a scaling estimate yielding a clean $\sqrt M$ is the classic artifact pattern
here; only the real integral distinguishes mechanism from coincidence, and it dissolved
the enhancement.*

**Net for the whole MOND program (honest).** Every mechanism tried — retardation,
linear diffusion, additive GEM terms, the catalytic cycle, and the pilot-wave/broad-
spectrum interference — gives **Newton** (or a linear-in-$M$ term), never the $\sqrt M$
Tully-Fisher signature. The eikonal result explains *why* they keep failing: coherent
gravitational interference is just classical bending for all strongly-coupled modes, and
the diffractive modes are too weakly coupled to matter. The connecton foam-sea robustly
gives **Newtonian $1/r$** (real progress — dodges the geometric $10^6$ and the
ballistic/diffusive dilemma), but **MOND/RAR is not reproduced.** The model most likely
**needs dark matter for galaxies** — not fatal, since the PBH thread (OP-18) supplies a
candidate: PBH dark matter would give rotation curves the same way it gives the CMB
wells (one population, OP-12 stance (2)). The criticality-as-license and $v\times B_c$
notes remain mechanism-less for *deriving* MOND, but the detailed Lorentz revisit (below)
found that they connect to the observed **M–σ relation** as a consistency condition —
a falsifiable structure worth keeping, even though no mechanism is shown. So: not dead
remnants, but checkable leads without a derivation.

**Dynamical-selection reframing (author) — flatness as an attractor, not a static
solution.** A correction to the whole approach above: every attempt demanded that
$\mathbf g_N+\mathbf v\times\mathbf B_c$ produce a flat curve as its *static equilibrium*,
which forced a non-analytic $B_c$. But a galaxy is a *dynamical* object on the map —
orbits expand as $c$ grows ($r\propto c^2$, OP-13). The central BH only *seeds* the
initial $c$-field perturbation; the bulk $B_c$ is sourced by the whole disk (each ring
weighted by its horizon-distance factor $\sim H_0 r/c$). A velocity-dependent Lorentz
force is a **velocity selector**: rings whose speed makes the Lorentz term too strong
become unbound and are *ejected to intergalactic space* as the system evolves. The flat
curve is then the **marginally-bound surviving population** — an attractor of the
evolution, not a solution the force law must yield. *This dissolves the static-solution
wall:* the math no longer has to produce flatness, only to eject over-supported rings;
survivors satisfy $B_c(r)=v_f/r$, which *is* flat, with **no fine-tuning**.
Result of the (scaling-level) test — a clean split:
- *Flatness:* explained as an attractor — robust, needs no fine-tuned $B_c$. Genuine
  progress; the author's central point stands. The static wall does not apply.
- *Tully-Fisher normalization* ($v_f^4=GM\,a_0$): **still open** — pinning the flat
  *value* requires the disk-sourced $B_c$ to carry $W\propto M^{-3/4}R$, the same
  non-analytic-source issue relocated into the normalization.
- *New falsifiable prediction:* galaxies should **lose outer rings to intergalactic
  space** over cosmic time as $c$ grows (ties to OP-13). Potentially observable
  (intracluster light, intergalactic stars, tidal-looking streams without a tidal
  cause) — a consequence distinct from flat curves, which is what a rival theory needs.
  The *same* ejection mechanism strips disks and caps galaxy size in **OP-19** (the
  M–σ / disk-vs-elliptical predictions).
- *Dark-matter implication:* flatness being partly dynamical means the model may need
  *less* dark matter than $\Lambda$CDM (selection does some of the work), even if
  PBH-DM (OP-12/OP-18) still sets the normalization.
**Honest status:** a scaling sketch, not a derived calculation. Flatness-as-attractor is
structurally sound, but the dynamical *convergence* (does Lorentz ejection from a
realistic disk, through $c$-evolution, actually reach $B_c=v_f/r$?) is unproven, and the
TF normalization is unsolved. **This is now the most promising rotation-curve direction**
— a new, well-posed dynamical-ejection calculation not yet done properly.

**Inertia no-go (a clean by-product).** The connecton **cannot** source inertia: a
momentumless field gives no momentum-reaction force. Gravity (a sink/gradient/delay
effect) and inertia (a momentum-reaction effect) require opposite momentum properties
of the same field. This explains *why* invariant mass (premise 3) must be **axiomatic**
rather than emergent — and is independently consistent with OP-12 (routing inertia
through the cosmic potential would drift as $c^{-10/3}$).

**Open items, in priority:** (1) **the RAR functional form** — solve the nonlinear
diffusion in the foam-sea picture and check whether it yields the deep-MOND law and the
RAR interpolating function, not just the $\sim cH_0$ scale (this is now the make-or-break,
and the most promising route to the OP-3/OP-17 rotation-curve problem). (2) Prove the
closure condition $4\pi G L\rho_\text{bg}/(3\sigma)=c$ (equivalently $V=c$) that pins
the transition to $cH_0$ — one power of $c$ is already structural ($D=cL/3$).
(3) Derive the *coefficient* — does it yield $G\propto c^{-2}$ with the right magnitude,
not just the $1/r$ form? (4) Light bending and the global $c$-growth bookkeeping
($\dot c/c=H$ from the same termination field) must be shown mutually consistent.
(5) Whether matter must continuously emit (preferred: clean EP, energy drain
$\sim10^{-39}$ of rest energy per Hubble time, negligible) or emit only at creation.

### OP-15 — Inertia, conservation laws, and the symmetric flip from standard cosmology

*Status: resolved in structure. Establishes what is conserved (momentum/angular
momentum yes, energy no), resolves "where does invariant mass leave inertia?", the
free-particle puzzle, and confirms orbital expansion (OP-13) survives. One accepted
ontological commitment; one flagged subtlety.*

**The map is the conjugate frame to standard cosmology — the symmetric flip.**
Standard cosmology: **rest energy conserved, photon energy drops** (cosmological
redshift = energy loss). The map's purpose is the mirror image: **photon energy
conserved, rest energy changes.** This is not an add-on; it is the defining property
of the map frame. The two descriptions are related by the map↔observer transformation;
neither is "more true," but the map is the frame in which photons lose no energy in
flight (premise 4) — the feature the model was built to have.

**What is conserved (from symmetry, the decisive argument).** The static map is
spatially **homogeneous** and **isotropic**, but $c=c(t)$ breaks time-translation.
By Noether, unambiguously:
- **Linear momentum conserved** (space homogeneity, exact).
- **Angular momentum conserved** (isotropy, exact — no torque available).
- **Energy NOT conserved** (time-translation broken by $c(t)$).

This is the symmetric flip made precise: energy is exactly the quantity that is
allowed to change, while momentum is exactly preserved.

**Cross-link (now load-bearing for OP-18).** The connecton field is *momentumless* —
hence **pressureless** — which is why it cannot source inertia (no momentum-reaction;
see the OP-14 inertia no-go) and why it gravitates without a pressure term. That same
pressureless property is exactly the trait the CMB analysis (OP-18) leans on: a
pressureless gravitating component is what is needed to drive the acoustic peaks without
oscillating. The smooth connecton sea has it but does not *cluster* (so cannot drive the
higher peaks); PBHs are pressureless *and* clustered (OP-18). So the momentumless result
established here is the property that makes the PBH/CMB parallel work — recorded so the
two entries stay connected.

**The model is Machian about $c$, not about inertial mass.** Sciama makes inertial
*mass* relational ($GM_u/R_uc^2\sim1$); this model makes the *speed of light*
relational ($c\propto N$, $c\to0$ for a lone particle). Inertial mass is invariant
(premise 3); what requires other matter is the kinematic *arena* ($c>0$). "$c\to0$
when alone" means dynamics become **vacuous**, not that inertia vanishes — arguably
cleaner than Sciama (no "zero-inertia particle in a normal spacetime"). Sciama's ratio
$GM_u/(R_uc^2)=\tfrac12$ **today** but **drifts as $c^{-10/3}$** (OP-12), so literal
Sciama-induced inertia is *incompatible* with invariant mass — confirmed from three
routes (OP-12, OP-14, here). $m$ is invariant and **axiomatic**; the model does not
derive its magnitude (a limitation Sciama aspired to fill).

**Free unbound particle as $c$ grows.** Momentum conserved $p=p_0$, $m$ invariant:
$$\frac{u}{c}=\frac{p_0}{\sqrt{p_0^2+m^2c^2}}\ \ (\text{decreases as }c\text{ grows}),
\qquad E=c\sqrt{p_0^2+m^2c^2}\ \ (\text{grows}).$$
So rest/total energy **grows** with $c$ (the flip — standard cosmology would hold it
fixed), while the particle **decelerates relative to $c$**. This is the model's
**peculiar-velocity damping**: $u/c\propto(1+z)^{1/2}$ vs standard FLRW $(1+z)^1$ —
same direction, comparable rate, **no scale catastrophe** (contrast OP-3). A genuine,
testable difference on the right side.

**Bound orbit — orbital expansion CONFIRMED, OP-13 safe.** For a bound orbit the
vacuum is isotropic, so **angular momentum is conserved** (no torque). With
$L=mvr$ const, $m$ invariant, and $v^2=GM/r$ ($G\propto c^{-2}$):
$$r\propto c^{2},\qquad v\propto c^{-2}.$$
Orbits **expand** as $r\propto c^2$ — the original OP-8 result stands. This is what
OP-13 (galaxy size evolution $\propto(1+z)^{-1}$, matching observations) rests on, so
the new inertia physics **does not** overturn it. (Energy is *not* conserved for the
orbit — it is the quantity the vacuum exchanges — consistent with the symmetric flip.)

**On the energy non-conservation — interpretation is OPEN (do not overstate).** The
firm result is only that energy is *not a conserved quantity* on the map (time-
translation broken by $c(t)$); momentum and angular momentum are conserved. The math
does **not** by itself say energy physically flows into or out of a vacuum reservoir.
At least three distinct readings are compatible with what we have, and we cannot yet
distinguish them:
1. **Connecton absorption (real exchange):** a moving particle gains effective energy
   by absorbing connectons; because each carries only $\sim\hbar H_0$, vast numbers
   can boost it with no thermal catastrophe. The only reading positing a mechanism;
   ties to OP-14. A stronger claim than the math requires.
2. **Pure $c$-scaling (units):** nothing flows; the quantity called energy simply
   carries a factor of $c$, so it grows as $c$ grows — a bookkeeping/units effect,
   like redshift being a measurement artifact. **Corollary: rest energy is less
   fundamental than usually assumed** — $mc^2$ growing is not the particle acquiring a
   store of energy, but rest energy being a $c$-dependent quantity, not an invariant.
3. **Relational (Machian):** it is the addition of particles to the universe (more
   $N$ raises $c$, premise 2) that boosts a moving particle's effective
   energy. Energy is referred to the global matter content, not traded with a local
   reservoir. Arguably the most consistent with premise 2; distinct from both above.
   **Author's preferred reading.** This is not a new postulate — it is the model's
   counting-Machianism (OP-12, $c\propto N$) extended from the arena ($c$) to energy.
   See the unifying note below.

The "energy reservoir" phrasing is withdrawn as over-committed. What is safe to say:
energy is non-conserved on the map (the intended mirror of standard cosmology's photon
energy loss), momentum/angular momentum are conserved, and *how* to interpret the
energy change is an open modelling choice.

**Flagged subtlety (open):** photons and massive particles conserve *different*
invariants under the same vacuum — photons conserve frequency/energy (redshift
evidence from atomic lines requires it; momentum $p=E/c$ then drops), massive particles
conserve momentum (energy grows). This is *plausibly* consistent — a photon has no rest
frame and $E=pc$ locks the two so only one (frequency, its topological phase invariant)
can be conserved, while a massive particle's robust invariant is momentum from space
homogeneity — but it has not been proven consistent from a single action. *Open: a VSL
Lagrangian showing one vacuum conserves a photon's frequency and a massive particle's
momentum simultaneously, without contradiction.*

---

## Unifying note — the relational (counting-Machian) principle

*The single principle the model most nearly reduces to.* Premise 2 ($c\propto N$) is
usually stated as "the speed of light is set by the cosmic particle count." The
relational reading of OP-15 recognizes that this governs not just $c$ but **everything
$c$ scales** — so the principle is broader: **the global matter count $N$ sets $c$, and
$c$ sets every energy, length, time, and coupling; therefore all physical scales are
referred to $N$.** Energy is relational because $c$ is relational. This is *counting*-
Machianism (distinct from Sciama's *potential*-Machianism, which the model fails —
OP-12), now seen to run through the whole structure:

- **OP-12:** $N$ sets $c$ (the arena). The root statement.
- **OP-15:** $c$ sets particle energy → energy is referred to $N$ (the contents).
- **OP-11:** redshift = a photon's fixed energy compared to a *now-larger* ($N$-grown)
  atomic reference. The relational principle already in observable action.
- **OP-1:** clock rates / atomic frequencies $\propto c^2$ → time is referred to $N$.
- **OP-13:** orbital energy referred to $N$ (grows, non-conserved) while angular
  momentum is locally protected — explains the split.
- **OP-6:** at genesis $N\to$small, so all scales $\to$small together; the energy
  scale of the universe bootstraps with the matter count.

So the model's Machian content is **one principle in many arenas**, not several
separate premises. This is the cleanest candidate for the model's foundational
statement, and the natural organizing idea if/when v5 is promoted to the core
document. (Caveat: it is the *interpretation* of energy non-conservation, not a new
derived result; the firm results are unchanged. But it costs no new ontology and
follows from premise 2.)

---

## Cross-cutting threads / next-session priorities

1. **(RESOLVED this session)** OP-5 $q_0$ sign: $q_0=1/(nP)>0$ for *all* power-law
   horizons — no variant gives acceleration; $n<0$ is barred by the existence of
   redshift. The model structurally cannot mimic dark energy. **New framing of the
   central question:** the model's viability now hinges on an *external* question —
   whether cosmic acceleration is real and standard-candle-clean. If it is, the model
   is in genuine tension; if SNe-as-standard-candles is as uncertain as the author
   suspects, the tension softens. Either way there is no internal fix to pursue.
2. **(highest remaining priority) Real data:** a genuine Pantheon+ fit (with
   covariance) to test the clean prediction $q_0=1/(nP)>0$ directly against SN data,
   replacing the ΛCDM-proxy comparison. This is now the decisive empirical test.
3. **Minor cleanups (cosmetic):** OP-7's $s$-fit and the OP-9 "fork" section still cite
   superseded linear-law results; their conclusions are corrected inline but the body
   text predates the fix.
4. **Open theory debts:** why mass is invariant ($s=0$) and not PV ($s=-3/2$) — the
   one remaining premise the author holds provisionally (now with *more* riding on it:
   the finite proper age, OP-1, and $\alpha$-invariance, OP-4, both require it); and what
   pins the number density $n$ (OP-12) / the PBH abundance (OP-18). *(OP-4 $\dot\alpha$
   itself is now resolved — $\alpha$ invariant to all orders.)*
5. **(major reopened problem — BLOCKER) Rotation curves (OP-3):** the $\dot c/c$
   mechanism fails at galactic scale by $\sim10^3$–$10^6$ (ring integration).
   Dark-matter-free flat curves are now **unsolved**. The RAR (OP-17) sharpens the bar:
   any viable mechanism must be **acceleration-keyed**
   (modify gravity below $g_\dagger \sim cH_0$), not distance-keyed — which rules out retardation-type effects
   structurally. Either find such a mechanism (cosmologically-corrected GEM /
   Liénard-Wiechert, or OP-14 connecton gravity), or accept the model needs dark matter.
   **The $\sim10^{-6}$ order problem must be solved before any further work on rotation
   curves, MOND (OP-2), or the RAR (OP-17) — these stand or fall together.**
6. **Foundational (independent of SN):** the volume-vs-surface-vs-S′ choice (OP-5) is
   still open and is *not* constrained by the $q_0$ result — all give $q_0>0$. S′
   remains attractive for its finite origin (OP-6).
7. **Speculative (OP-14, connecton gravity) — best gravity mechanism yet, but MOND
   unproven:** the connecton-sea = quantum-foam identification gives diffusion
   everywhere (restores Newtonian $1/r$, dodges the geometric $10^6$, gives EP) — this
   is real progress on *gravity*. But the **RAR/MOND functional form is the wall
   (caveat 2):** it needs a low-gradient diffusion nonlinearity $D\propto|\nabla\rho|$
   that has no independent motivation and is *disfavored* by the natural reading (small
   perturbation on the cosmic background gradient gives linear response = Newton, no
   enhancement). The $a_0=cH_0$ scale is self-consistent across regimes but does not
   force the MOND form. **Obstruction pinned:** MOND's $\sqrt M$ scaling (Tully-Fisher)
   needs a *nonlinear source coupling*; every natural mechanism (retardation, linear
   diffusion, additive GEM-like terms) is *linear* in $M$ — hence the scale matches but
   the form fails. **The catalytic-cycle attempt (connectons co-catalyzing transient
   pairs) was worked through and gives Newton, not MOND:** the real threshold $\sqrt{}$
   is keyed to the pair's MeV energy (not the field gradient), and the collective version
   gives linear drift unless cooperativity (criticality) is invoked — which belongs at
   the strong-field end. **Sharpened obstruction:** MOND needs a *weak-field
   cooperative/non-analytic* coupling in the foam; no linear mechanism supplies it.
   **UPDATE — pilot-wave mechanism examined and overturned.** Allowing $m$-dependence
   gave a broad spectrum (index $p=1$) with BH resonant shaping at $\lambda\sim r_s$;
   a scaling estimate suggested $\sqrt M$ Tully-Fisher, but the proper **eikonal
   integral** for the coherence factor shows coherent gravitational interference is just
   classical bending (wavelength-independent) → **Newton, not MOND**. No wavelength is
   both strongly coupled and in the diffraction regime. So every connecton mechanism
   (retardation, linear diffusion, additive GEM, catalytic cycle, pilot-wave) gives
   Newton; the $\sqrt M$ is not reproduced. **Conclusion: the model most likely needs
   dark matter for galaxies — plausibly the PBH population of OP-18** (one component for
   rotation curves *and* CMB wells *and* SMBH seeds; OP-12 stance 2). MOND-from-connectons
   is not a live lead pending a genuinely new idea for a weak-field nonlinearity.
8. **(new — hardest constraint) The CMB power spectrum (OP-18):** $\Lambda$CDM's tightest
   success and where rival cosmologies usually die. Two author connections give a path:
   the **first peak translates** (baryon-photon acoustic physics is self-similar under
   the $c^2$-energy scaling — no DM needed), narrowing the problem to the *higher-peak
   heights*; and **primordial black holes** are a concrete candidate for the clustered
   pressureless wells the third peak needs — and could *also* be the galactic dark
   matter (OP-3/OP-17), reframing the model as "DM = PBHs" rather than "no DM." The path
   runs through OP-6: **does genesis produce PBHs, and is that consistent with the
   $r_s>R$ cutoff that currently forbids early localization?** That is the load-bearing
   check. Origin and blackbody (ingredients A, B) remain unworked secondary problems.
   Until a spectrum is computed, a research program, not an answer.

*Pattern worth remembering: this session's corrections (redshift law, standard-candle
treatment) repeatedly made the model look better by removing artifacts. But two
headline "successes" did NOT survive scrutiny: the SN "mimics acceleration" result
(linear-law artifact, OP-5/OP-9) and the rotation-curve mechanism (scale bug + a
dimensional sleight-of-hand, OP-3). The discipline cuts both ways — removing errors
sometimes reveals a real result was illusory. Honest current headlines: the model
cannot produce apparent acceleration ($q_0=1/nP>0$), and it does not (yet) solve
rotation curves without dark matter.*
