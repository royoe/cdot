# Static VSL Cosmology — Working Document v3 (compacted)

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
$$\tau(z)=\tfrac{3}{4H_0}\big[1-(1+z)^{-2/3}\big]\ (P{=}2),\quad
\tau_\infty=\tfrac34 H_0^{-1}\approx 10.5\ \text{Gyr}.$$
SN standard candle: $L$ is epoch-invariant in proper units (map-frame
$L\propto c^{2P}$ is a units artifact, not dimming). Deceleration $q_0=1/(3P)>0$.

**Resolved (see v2 for derivations):** OP-1 (time frames; finite proper age
$\approx10.5$ Gyr), OP-7 (mass exponent; invariant mass favored),
OP-8 (invariant-mass branch is the recommended core). *(OP-3, formerly "rotation
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
candidate unification of gravity and the $c$-field; solves thermal/drag/EP but the
Newtonian $1/r$ at range is unresolved).

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

### OP-4 — Fine-structure drift $\dot\alpha$ (never converged)

Classical $\alpha$ invariant (the $K$'s cancel). Open question: does the first-order
QED vacuum-polarization (Uehling) correction, which depends on the Compton wavelength
$\propto c^{-2}$, drift over cosmic time? Multiple derivation attempts in v2 produced
inconsistent magnitudes (the additive-vs-multiplicative perturbation error was caught
but not cleanly resolved). Modern bound: ESPRESSO $\Delta\alpha/\alpha=1.3\pm1.3$ ppm
at $z\sim1.15$ — any predicted drift above ~1 ppm is excluded. *Open: a clean,
correct first-order loop calculation of $\dot\alpha/\alpha$, then compare to ESPRESSO.
Currently unresolved.*

### OP-5 — What sources $c$: volume vs. surface law, and the $q_0$ sign

Baseline is volume law $c\propto N\propto R^3$.

**Foundational (still open):** the $c\propto N$ rule and the bulk-vs-surface counting
are an underived first principle. Variant **S′** ($c\propto R^{2/3}$, Compton-thickness
self-consistent) is the leading alternative and uniquely restores a **finite
coordinate-time origin** (a real Big Bang in map time). This choice is unconstrained by
the SN result below.

**The $q_0$ sign — RESOLVED (structural, negative).** Computed $q_0$ for a *general*
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
$c\propto N$ is the fixed point of a self-consistent matter-creation bootstrap; PBH
cutoff $r_s>R$ forbids early localization. **Matter/antimatter asymmetry unsolved** —
the headline open problem here. BBN expected normal pending an $H$-as-freeze-out-timer
check (the $H$-substitution may smuggle assumptions). Conjectural; flagged as such.

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

Mass budget: removing dark matter (OP-3) leaves $\Omega_b\sim0.05$. But the static
model has **no Friedmann constraint** — flatness is by construction, so low density is
**not** a crisis. Price: $H_0$ and matter density $n$ are decoupled free inputs (no
Sciama link), so the model has less explanatory economy than FLRW on this point.
*Open: what pins $n$?*

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

**Flagged escape (speculative, unproven):** if connectons scatter mainly off **each
other or the vacuum pair-field** — a dense, self-interacting connecton *sea* — the mean
free path is set by the sea (diffusive everywhere, including "empty" space) while
ordinary matter only lightly perturbs it (gravity stays weak). This would restore
diffusion and the $1/r$, but it is a substantially different, more speculative model
(connectons as a self-interacting medium, not a thin gas) and has not been derived.

**Inertia no-go (a clean by-product).** The connecton **cannot** source inertia: a
momentumless field gives no momentum-reaction force. Gravity (a sink/gradient/delay
effect) and inertia (a momentum-reaction effect) require opposite momentum properties
of the same field. This explains *why* invariant mass (premise 3) must be **axiomatic**
rather than emergent — and is independently consistent with OP-12 (routing inertia
through the cosmic potential would drift as $c^{-10/3}$).

**Open items, in priority:** (1) the ballistic/diffusive dilemma — does the
connecton-sea picture give diffusion at range without making gravity strong/short? This
is make-or-break. (2) If diffusion holds, derive the *coefficient* — does it yield
$G\propto c^{-2}$ with the right magnitude, not just the $1/r$ form? (3) Light bending
and the global $c$-growth bookkeeping ($\dot c/c=H$ from the same termination field)
must be shown mutually consistent. (4) Whether matter must continuously emit (preferred:
gives clean EP, energy drain $\sim10^{-39}$ of rest energy per Hubble time, negligible)
or emit only at creation.

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
statement, and the natural organizing idea if/when v3 is promoted to the core
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
   one remaining premise the author holds provisionally; OP-4 $\dot\alpha$; what pins
   the number density $n$ (OP-12).
5. **(major reopened problem) Rotation curves (OP-3):** the $\dot c/c$ mechanism fails
   at galactic scale by $\sim10^3$–$10^6$ (ring integration). Dark-matter-free flat
   curves are now **unsolved**. Either find a genuinely different mechanism (a full
   cosmologically-corrected GEM / Liénard-Wiechert treatment is the natural next try),
   or accept that the model needs dark matter — an honest limitation. This was a
   headline "success"; it is now a headline open problem.
6. **Foundational (independent of SN):** the volume-vs-surface-vs-S′ choice (OP-5) is
   still open and is *not* constrained by the $q_0$ result — all give $q_0>0$. S′
   remains attractive for its finite origin (OP-6).
7. **Speculative (OP-14, connecton gravity):** resolve the ballistic/diffusive dilemma
   — does a self-interacting connecton *sea* give diffusion (hence Newtonian $1/r$) at
   range without making gravity strong/short? Make-or-break for the mechanism. The
   author intends to return to this.

*Pattern worth remembering: this session's corrections (redshift law, standard-candle
treatment) repeatedly made the model look better by removing artifacts. But two
headline "successes" did NOT survive scrutiny: the SN "mimics acceleration" result
(linear-law artifact, OP-5/OP-9) and the rotation-curve mechanism (scale bug + a
dimensional sleight-of-hand, OP-3). The discipline cuts both ways — removing errors
sometimes reveals a real result was illusory. Honest current headlines: the model
cannot produce apparent acceleration ($q_0=1/nP>0$), and it does not (yet) solve
rotation curves without dark matter.*
