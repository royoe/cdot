# T14 — Connecton Gravity

*This document inherits the $R_0$ gap flagged in T6 and T12, and this is where it
actually needs resolving — T14 is where "the sea's kinematic acceleration" and "the
holographic saturation of the horizon" are *derived* (or were, under occupancy
counting). **Reconciled (2026-07-04) against two later developments, both checked
independently rather than taken on faith:**

1. **The particle horizon is finite after all — the "infinite horizon" finding below
   was correct for the pure, single-phase exponential law, but that law has since been
   superseded.** A percolation transition (`percolation_break/`, forthcoming T23 —
   Autocatalytic Counting) splits premise 2 into two regimes: connectivity counting
   ($c\propto e^{R/L}$) below a break redshift $z_*\approx1.2$, occupancy counting
   above it. Because the high-$z$ (subcritical) branch's $D_H\propto(1+z)^{-q}$ has
   $q\approx1.37>1$, its contribution to the distance integral converges, giving a
   **finite** particle horizon, $D_p(z\to\infty)\approx116.7\,r_d$ — re-derived
   independently below, not merely quoted. Holographic saturation is back in play; it
   needs recalibrating against this new, different finite horizon, not rebuilding from
   nothing.
2. **The connecton-sink premise relaxation is reverted.** A concrete test
   (`cz_inversion/`, "Fork A": excluding BH-confined mass from the count while keeping
   connectons themselves conserved) failed by 2–4 orders of magnitude against the real
   cosmic black-hole budget; genuine sinks were considered and not pursued. Connectons
   are conserved, exactly as in cdot-4 — restored below wherever the earlier draft
   assumed otherwise.

Sections not touching $R_0$ or connecton conservation (the Le Sage scorecard, the
foam-diffusion mechanism, the RAR closure's functional-form derivation, the
dynamical-selection mechanism) were already confirmed unaffected and are unchanged by
this reconciliation.*

---

## The Idea

Gravity may share the same substrate that drives $c(t)$. The proposal is to posit a
**connecton** that embodies the relational principle (T12) physically: it is the
carrier of the "connection" between particles that the counting rule requires.
*(What kind of thing a connecton is — not a standard field quantum, per T12 §"What Is
a Connecton?" — is addressed there; the properties below are unaffected by that
discussion, only their interpretation is.)*

A connecton has the following properties:
- **Massless**, zero rest energy.
- **Near-zero but finite energy**: cdot-4 characterized this as "of order the horizon
  distance $R_0=6c/H_0$, energy of order $\hbar H_0/6$." **Reopened, not closed off**:
  the particle horizon is finite again under the percolation-broken counting law
  (§"Energy Scale" below), but its value is not the old clean $R_0=6c/H_0$ — three
  candidate finite lengths are now in play, and which one (if any) plays $R_0$'s role
  is the open question, not whether a finite length exists at all.
- **Propagates at the local speed of light** $c(t)$ at the time of propagation —
  unaffected by the counting law.
- **Conserved in number**: never destroyed. Momentarily absorbed by a massive particle
  (in a brief virtual $e^+e^-$ pair creation and re-emission), then re-emitted. **This
  is unqualified, exactly as in cdot-4**: a concrete attempt to relax it (excluding
  BH-confined mass from the count while keeping connectons conserved) was tested
  against the real cosmic black-hole budget and failed by 2–4 orders of magnitude
  (`cz_inversion/`); genuine sinks were considered and not pursued. No amendment to
  this premise is needed or retained.
- **Emitted continuously by massive particles**: the emission rate is negligible in
  energy ($\sim10^{-39}$ of rest energy per Hubble time) but ensures the
  counting-Mach relation holds at all epochs — unaffected by the counting law, since
  this rate is evaluated locally and today.

The horizon is the dominant source: horizon-scale connectons permeate the universe
from the first moments. The global termination/turnover rate of connectons sets
$\dot c/c=H$ (the cosmology, premise 2, now connectivity counting); local structure in
the connecton field is gravity.

---

## One Sea, Two Descriptions: Density and Flow

The connecton sea is a **single** physical population, described — like any medium —
by a local number-density field $n(\mathbf x,t)$ and a local bulk-velocity field
$\mathbf u(\mathbf x,t)$. Both the cosmological role (premise 2) and the local
gravitational role (this document) are properties of this one field, not two different
mechanisms:

- **Global background.** Far from any mass, $n$ is spatially uniform and $\mathbf
  u=0$ in the cosmological rest frame. **Updated for cdot-5**: the slow, secular
  growth of the total reach $N\propto e^{R/L}$ (Core premise 2, connectivity counting —
  cdot-4 said $N\propto R^3$, occupancy counting) sets the cosmological signal speed
  $c(t)$ — a property of the network's *global* structure, not of any local value.
- **Local perturbation.** Near a mass, continuous net emission perturbs the same field
  in two ways: a density perturbation $\delta n\propto1/r$ (short-mean-free-path,
  "diffusive" fraction) sources the Newtonian potential $\phi=-GM/r$; a
  distinguishable, long-mean-free-path ("ballistic") fraction of the *same* sea
  develops a nonzero coherent bulk velocity $w(r)$ toward the mass, free-falling under
  that same $\phi$ — this is the **river**, derived in T22 §2. **This local mechanism
  is galactic-scale physics (diffusion, Poisson's equation, a free-fall velocity
  profile) and does not reference the cosmological counting law's functional form at
  all — confirmed unaffected.**

**There is one $c$, set once, globally.** The connectons' propagation speed relative
to the sea's own local rest frame is always $c(t)$ — it is not separately modulated by
local density perturbations (T22's uniqueness theorem: the index/density-coupling
channel is forced to zero, $A=0$, once $m$ and $G$ are required to stay strictly
invariant). This is what the design intuition behind "light travels slower in a well"
actually means: not a second, locally-varying value of $c$ itself, but ordinary
advection — the *coordinate* speed of light in the static map is $c(t)\mp
w(\mathbf x)$, the cosmological and local-flow effects composing exactly as
originally intended. **Unaffected by the counting-law change** — this is about local
vs. cosmological composition, not about which law drives $c(t)$'s cosmic history. See
T22 for the full derivation and its open items.

**The unresolved two-population tension, carried forward unchanged.** "Resolving the
Dilemma" below states that foam-scattering gives a sub-Compton mean free path and
hence diffusion "everywhere, including empty space." The river needs a *non*-
scattering, long-mean-free-path fraction to exist alongside that diffusive
population. This tension, and its two quantified (not yet derived) candidate
resolutions — endpoint-only interaction ($\propto1/L_\text{link}$, a *different* $L$
from Core Principles' recruitment length; unfortunate shared symbol, no relation) and
an illustrative Rayleigh-type cross-section — are local, sub-galactic microphysics
questions, unaffected by the cosmological counting-law change. Still open, exactly as
in cdot-4.

---

## Energy Scale: The Minimal Quantum — Reopened, Then Partly Recovered

*cdot-4's entire construction here uses $R_0$ as **the current physical size of the
observable universe** — a finite radius whose surface bounds a finite holographic
capacity. An earlier pass on this rewrite found that construct entirely unavailable
under a single-phase connectivity-counting law (infinite particle horizon). A later
development (the percolation transition, `percolation_break/`, forthcoming T23) changed
that finding — reworked below, independently re-derived rather than just quoted.*

### The particle horizon is finite again — under the two-phase law

The single-phase law, $D_p(z)=(L/2)\ln(1+z)$, does diverge as $z\to\infty$ — that
part of the earlier analysis was arithmetically correct. But premise 2 is no longer
single-phase: above a percolation break $z_*\approx1.2$, the network is subcritical and
reverts to occupancy counting, with $D_H\propto(1+z)^{-q}$, $q\approx1.37$. Re-deriving
the resulting horizon independently (matching $D_H$ continuously across $z_*$ and
integrating the subcritical tail):
$$D_p(z\to\infty)=D_p(z_*)+\frac{B}{q-1},\qquad B\equiv L/2,$$
which is **finite** because $q>1$ makes the subcritical tail integrable. Using the
fitted parameters ($B=33.55\,r_d$, $z_*=1.201$, $D_0=-0.46\,r_d$): $D_p(z_*)=26.0\,r_d$,
giving
$$D_p(\infty)=26.0+\frac{33.55}{0.37}\approx116.7\,r_d.$$
(Independently verified — this matches the value obtained by direct numerical
integration of the broken $D_H(z)$, not merely algebraic substitution.) Holographic
saturation is back in play: there is a finite boundary again, just not the old clean
$R_0=6c/H_0$.

### Three candidate lengths, and what they give for $g_\dagger$

The percolation construction actually supplies **three** distinct finite lengths, not
one, and it is not yet settled which (if any) plays the crossing-rate role $R_0$ played
under occupancy counting:

| Length | Meaning | Value ($r_d$) | $g_\dagger=c_0^2/\ell$ | vs. observed $a_0$ |
|---|---|---:|---:|---:|
| $L$ | Recruitment length $=R_*$, the correlation length at percolation | $67.1$ | $3.40\times10^{-10}$ m/s$^2$ | $2.83\times$ too large |
| $R_\text{now}$ | Present horizon, $=L+D_p(z_*)$ (T23's closed internal relation) | $93.1$ | $2.45\times10^{-10}$ m/s$^2$ | $2.04\times$ too large |
| $D_p(\infty)$ | Full particle horizon (occupancy-branch tail included) | $116.7$ | $1.96\times10^{-10}$ m/s$^2$ | $1.63\times$ too large |

(All three $g_\dagger$ values computed independently from the $g_\dagger^\text{naive}=c_0^2/L$
figure in T6, rescaled by the length ratios above; not merely copied from elsewhere.)
**None of the three closes the gap to cdot-4's $\sim6\%$ standard**, but $D_p(\infty)$
gets substantially closer than the naive $L$-substitution did, and the exercise is now
a finite-arithmetic-plus-one-conceptual-choice problem, not a search for a missing
length. The conceptual choice: $g_\dagger$ was read as a *crossing-rate* acceleration,
$c\cdot(c/\ell)$ — is the relevant crossing distance the recruitment length $L$ (the
scale over which the local node's reach turns over — arguably the right notion of
"crossing" for a connectivity-counted network) or the particle horizon $D_p(\infty)$
(a light-travel distance, which is what $R_0$ actually was under occupancy counting)?
**This is the genuine, narrower open question** — not "does a finite length exist,"
which is resolved (yes), but "which finite length sets the turnover rate."

### What survives, unaffected by either finding

The cascade slope ($n(k)\propto1/k$, $P_\rho(k)\propto k^{-2}$, steady-state
conserved-number transport) does not reference $R_0$ or any horizon size — it is about
the shape of a cascade in wavenumber space — and stands unaffected regardless of which
particle-horizon story is current. The RAR closure's functional form (below) and the
foam-diffusion mechanism for Newtonian gravity do not use $\rho_\text{bg}$ or the
holographic count — $\rho_\text{bg}$ "does not enter $g_\dagger$," per cdot-4's own
note, preserved here. Those results were never at risk either way.

### What needs recomputing, now that a finite horizon exists again

1. **The holographic count and sea density**, $N_\text{hor}=4\pi R_0^2/(4L_p^2)$,
   $\rho_\text{bg}=n_\text{holo}m_c=(\pi/6)\rho_\text{crit}$ — recomputable in principle
   against whichever of $D_p(\infty)$, $R_\text{now}$, or $L$ turns out to be the
   physically correct boundary, once the conceptual choice above is resolved. Not
   attempted here.
2. **The factor-3 ambiguity in the connecton's quantum mass definition**
   ($m_c=\hbar H^\text{hor}/c^2$ vs. $\hbar c/\ell$ for whichever $\ell$ is chosen) —
   unchanged in kind from cdot-4, now with three candidate $\ell$ values instead of
   one $R_0$.
3. **Deriving $R_*=L$ from the percolation condition** $n_\text{node}\ell_\text{link}^3\sim1$
   using the foam density evolution — T23's own item 1, "gating." Until this is done,
   $L$'s absolute value (hence all three lengths above) is fit to DESI, not derived.

---

## Scorecard Against Le Sage Objections

*Confirmed unaffected — every item here is local, sub-galactic microphysics
(conservation, momentum, composition-independence, diffusion geometry), none of it
referencing the cosmological counting law.*

The connecton hypothesis is a variant of Le Sage gravity (Le Sage 1748). Le Sage
theories face four standard objections.

### 1. Thermal catastrophe — SOLVED

**Le Sage problem:** a particle absorbing a constant flux of corpuscles heats up
without limit. **Connecton resolution:** connectons are conserved — absorbed and
immediately re-emitted (after a virtual $e^+e^-$ pair, uncertainty time
$\sim\hbar/mc^2$). No energy is permanently absorbed.

### 2. Drag — SOLVED

**Le Sage problem:** a moving body sweeps up more corpuscles from the front.
**Connecton resolution:** gravity is a field-gradient/delay effect, not a
momentum-transfer effect. Because the connecton energy is near zero, the momentum per
connecton ($p=E/c\sim\hbar H_0/c$) is negligible.

### 3. Equivalence principle — CLEAN

**Le Sage problem:** different materials might have different "opacity" to
corpuscles. **Connecton resolution:** source strength $\propto$ particle count
$\propto$ mass (invariant mass, premise 3), composition-independent.

### 4. Distance law ($1/r$) — CONDITIONAL; the central open problem, resolved below

**Le Sage problem:** geometric shadowing gives a $1/r^2$ flux deficit → $1/r^3$
force. **Connecton resolution attempt:** if connectons diffuse (captured and
re-emitted with randomized directions, conserved), the steady-state density
perturbation around a mass obeys Poisson's equation, whose Green's function gives
$\phi\propto1/r$ — Newtonian gravity, $S\propto M$. **The obstacle (natural case):**
$1/r$ needs diffusion; long-range gravity needs transparency. Resolved next.

---

## Resolving the Dilemma: The Connecton Sea = Quantum Foam

*Confirmed unaffected — local microphysics (the foam's Compton-scale density and mean
free path), no reference to the cosmological counting law.*

The resolution came from identifying the "dense self-interacting connecton sea" with
the **quantum foam** — the vacuum's virtual $e^+e^-$ pair population. Connectons
scatter off the quantum foam. The foam density $\sim1/\lambda_\text{Compton}^3\sim
10^{37}\ \text{m}^{-3}$ gives a sub-Compton mean free path → diffusion everywhere,
including "empty" space, while ordinary matter is only a weak perturbation (gravity
remains weak and EP-clean).

**Consequences, unaffected:**
- The diffusion equation holds in "empty" space → Newtonian $1/r$ gravity restored.
- Because this is a **steady-state diffusion profile**, not a light-travel-time
  effect, it carries **no $d/(c/H_0)$ suppression** — this uses $H_0$ at its present
  value only (confirmed counting-law-independent, T5), so it dodges the geometric
  $10^6$ that killed the retardation family exactly as before.

---

## Toward the RAR: The Natural Acceleration Scale — Reopened, Narrowed

*This is T6's finding, in its home derivation. Presented in full here since T14 is
where the derivation actually lives, not merely referenced. Updated for the
percolation-break reconciliation — see "Energy Scale" above for the finite-horizon
finding this section now relies on.*

cdot-4 fixed the transition scale via the horizon radius:
$$R_0=\frac{3Pc_0}{H_0^\text{obs}}=\frac{6c_0}{H_0^\text{obs}},\qquad
g_\dagger=\frac{c^2}{R_0}=\frac{cH_0^\text{obs}}{6}\approx1.13\times10^{-10}\ \text{m/s}^2,$$
matching the observed $a_0\approx1.2\times10^{-10}$ m/s$^2$ to within $\sim6\%$ — read
as "the sea re-randomizes connectons at the horizon crossing rate $c/R_0$; the
associated acceleration is $g_\dagger=c\cdot(c/R_0)$."

**Under connectivity counting, $R_0$'s single, clean referent splits into three
candidates** (Energy Scale, above): $L$ (recruitment length, $g_\dagger$ off by
$2.83\times$), $R_\text{now}$ ($2.04\times$), $D_p(\infty)$ ($1.63\times$). None matches
cdot-4's $\sim6\%$, but the best of the three ($D_p(\infty)$) is not far off being
within a factor of $\sqrt2$–$2$ — arguably close enough that resolving *which* length is
the correct crossing scale, rather than continuing to search for one, might close most
of the remaining gap. This is a real, still-open re-derivation, not a foreclosed one.

**Status, precisely:** the dimensional coincidence ($a_0\sim cH_0$) survives (forced by
dimensional analysis alone, T6) — that was never in question. What's open is which of
$L$, $R_\text{now}$, or $D_p(\infty)$ correctly represents "the crossing distance" for a
connectivity-counted, two-phase network, and whether that choice is itself derivable
(from the percolation condition, T23 item 1) rather than a modeling decision.
**This remains the single highest-priority open item in this document** — narrower and
more tractable than it looked in the previous reconciliation pass (three concrete
numbers to choose between and a well-posed conceptual question, not an open-ended
search for a missing concept), but not resolved.

---

## MOND/RAR: From Structural Obstruction to Partial Derivation

*The functional-form results here are unaffected by the counting-law change; the
numerical predictions inherit the $g_\dagger$ gap above and cannot currently be
evaluated with confidence.*

Five mechanisms were examined for reproducing the RAR interpolating function under
occupancy counting (additive GEM, catalytic cycle, criticality-as-license, pilot-wave
broad-spectrum, retardation). All give Newton — a structural result for *direct-source*
mechanisms (deep MOND needs $g\propto\sqrt M/r$, a nonlinear source coupling; every
mechanism this framework naturally produces from a linear source gives the wrong
Tully-Fisher slope). **This structural obstruction is local/galactic mechanics,
unaffected by the counting-law change.**

### Quarter power as a transition-radius geometric mean

Two accelerations, both independent of the connecton:
- **Mass-sourced:** $g_\text{mass}(r)=GM/r^2$.
- **Cosmological background:** $g_\dagger$ — whatever its correct value turns out to
  be (see above); mass-independent by construction regardless.

Transition radius: $r_t=\sqrt{GM/g_\dagger}$. Evaluating circular-orbit balance at
$r_t$:
$$v_f^4=GM\,g_\dagger,\qquad a_0\equiv g_\dagger.$$
**This functional relationship is unaffected by the counting-law change** — it holds
for *any* value of $g_\dagger$, mass-independent and cosmological in origin. What
changed is that the specific numerical prediction this produces for any given galaxy's
$v_f$ cannot currently be computed with confidence, since $g_\dagger$'s value is open
(above). The $M^{1/4}$ amplitude $B_c=v_f/r=(GM g_\dagger)^{1/4}/r$ as a geometric mean
of two linear quantities is likewise a functional statement, unaffected in form.

**M-σ as a derived consequence.** Since $M_\text{BH}\propto\sigma^4\propto
v_f^4=GM_\text{bary}\,g_\dagger$ (T17), the M-σ relation is the BTFR read through two
masses that the shared $a_0$ locks together — a functional/structural statement,
unaffected; its numerical zero-point inherits the same open $g_\dagger$ value.

**The river connection (hint, not yet derived, unaffected in status).** T22's ballistic
population, evaluated at $r_t$, satisfies $w(r_t)=\sqrt2\,v_f$ — an algebraic identity
independent of $g_\dagger$'s numerical value (it holds for whatever $g_\dagger$ is,
since both sides are expressed in terms of it consistently). Still suggestive, still
not a derivation that the two populations are the same.

### RAR Crossover: Derived from Connecton Indistinguishability

*Confirmed unaffected — this derives the closure's shape with $g_\dagger$ entering as
an external parameter, not something the derivation itself fixes.*

Write $g_\text{obs}=g_\text{bar}+g_x$. The closure
$$g_x(g_x+g_\text{bar})=g_\text{bar}\,g_\dagger$$
is derived from: **(1) Generalized-Poisson reduction** — for a diffusive connecton
field, spherical steady state reduces to $D(g)g=g_\text{bar}$; deriving the closure is
equivalent to deriving $D(g)=g/(g+g_\dagger)$. **(2) Steady-state balance** — production
of excess connectons $\propto g_\text{bar}$ balanced by relaxation $\nu g_x$ gives
$g_\text{bar}=\nu g_x$. **(3) Indistinguishability** — an excess connecton relaxes
against the *total* ambient population, $\nu\propto(g_x+g_\text{bar})/g_\dagger$.
**(4) Closure** — substituting (3) into (2) gives the boxed relation. None of steps
1–4 reference $R_0$, $L$, or the counting law's history — $g_\dagger$ enters purely as
a parameter. Solving gives exactly MOND's "simple" interpolating function, matching
McGaugh-Lelli-Schombert to $0.020$ dex with the three alternative relaxation laws
data-excluded — **this shape-level result is fully intact.** Only the numerical value
of $g_\dagger$ that goes into evaluating the closure for any specific galaxy is open.

---

## Dynamical Selection: Flatness as an Attractor

*Confirmed unaffected in mechanism; one already-open modeling question (how $B_c$
evolves with cosmic time) now explicitly inherits the new $c(z)$ relation whenever it
is eventually pinned down.*

For a disk star on a circular orbit at radius $r$ with tangential velocity $v_\phi$,
taking $\mathbf B_c=B_c\hat z$:
$$\frac{GM}{r^2}=\frac{v_\phi^2}{r}+v_\phi B_c.$$
Stars satisfying $v_\phi B_c>GM/r^2-v_\phi^2/r$ experience a net outward force and
spiral out on a dynamical timescale — a continuous, time-steady velocity selector, no
orbital expansion needed (consistent with T9's static orbits, a premise-3 result
unaffected by cdot-5). The flat rotation curve is the marginally-bound surviving
population: survivors satisfy $B_c(r)=v_f/r$ automatically, with no fine-tuning. None
of this mechanism references the cosmological counting law.

**Cosmic evolution — status unchanged, not newly resolved.** "$B_c$ grows with $c$
(specific scaling depends on the microphysical model)" was already unspecified in
cdot-4 — this remains an open modeling question in cdot-5, not newly broken, just
noted that whenever a specific $B_c(c)$ scaling is proposed, evaluating its
redshift-dependence will need the new $c(z)$ relation (still the same
$c(z)=c_0(1+z)^{-1/2}$, T2, unaffected) composed with whatever functional dependence on
$c$ is eventually derived for $B_c$ itself.

---

## The Inertia No-Go Result

*Confirmed unaffected in conclusion; the ram-pressure budget's exact numbers use
$\rho_\text{bg}$, whose value is now open (above) — but the conclusion is robust to
that uncertainty given how large the safety margin is.*

Gravity (in the connecton picture) is a gradient/sink/delay effect requiring
momentum-neutral connectons. A zero-momentum field cannot deliver a momentum-reaction
force. This explains at a mechanism level why inertial mass must be axiomatic
(premise 3) rather than emergent — consistent with the failure of Sciama-type inertia
(T11, T12; both confirmed unaffected by the counting-law change independently).

**The ram-pressure budget.** The maximum momentum flux the flow could deliver by full
absorption, relative to gravity, for a body of mass $m$ and radius $R_b$ at distance
$r$ from mass $M$:
$$\frac{F_\text{ram}}{F_\text{grav}}=2\pi\,\rho_\text{bg}\,\frac{R_b^2r}{m}$$
— independent of $M$. Using cdot-4's $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$: for
Earth at 1 AU, $3.1\times10^{-26}$; for Mercury, $3.2\times10^{-26}$; a 1 km comet at
$10^5$ AU, $9\times10^{-19}$. **This specific $\rho_\text{bg}$ value is exactly what
"Energy Scale" above found does not survive connectivity counting** — but the
conclusion (comoving is necessarily geometric, not a disguised collisional push) is
safe by such an enormous margin ($10^{-19}$ to $10^{-26}$) that essentially any
plausible revision of $\rho_\text{bg}$ — even one that changed by many orders of
magnitude — would leave this conclusion intact. Flagged as a place where the open
$\rho_\text{bg}$ question does not, in practice, threaten the result built on it.

**Cross-link to T16 (CMB):** unaffected in substance — the connecton field is
pressureless (momentum-neutral), correct for driving CMB peaks gravitationally without
oscillating, but horizon-smooth, not clustered, so PBHs remain needed for the higher
peaks. (T16's own cdot-5 rewrite separately found the CMB first-peak *position*
question resolves differently under $D_A\equiv D_p$ — see cdot-4's T16/T23 for that
distinct thread, not revisited here.)

---

## Verdict (Honest Summary)

| Result | Status |
|---|---|
| Newtonian $1/r$ gravity from foam diffusion | **Confirmed unaffected** — local microphysics, dodges the geometric $10^6$, EP-clean |
| All MOND mechanisms (5), direct-source couplings | **Confirmed unaffected** — structural $\sqrt M$ obstruction is local/galactic, not cosmological |
| RAR closure functional form | **Confirmed unaffected** — derived from connecton indistinguishability with $g_\dagger$ as an external parameter, 0.020 dex vs. McGaugh |
| BTFR/RAR *numerical* scale ($g_\dagger$'s value) | **Open, narrowed.** Three candidate finite lengths (percolation break, `percolation_break/`); best candidate ($D_p(\infty)$) misses $a_0$ by $1.63\times$, down from a naive $2.83\times$ — a finite-arithmetic-plus-one-conceptual-choice problem now, not a search for a missing concept |
| Holographic saturation / $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ dark-energy identity | **Reopened, not closed off.** A finite horizon exists again ($D_p(\infty)\approx117\,r_d$); the identity needs recomputing against it once the correct length is chosen, not rebuilding from nothing |
| Dynamical selection / Lorentz filter | **Confirmed unaffected** — flatness-as-attractor mechanism is local; $B_c(c)$ evolution remains an open modeling question, as in cdot-4 |
| Inertia No-Go / ram-pressure budget | **Conclusion confirmed robust** despite $\rho_\text{bg}$'s value being open — the safety margin is too large for this to matter |
| Local gravity as coherent flow (the river, T22) | **Confirmed unaffected** — local mechanism, does not reference the cosmological counting law |
| Connecton conservation | **Tested and restored** — a BH-confined-mass sink (Fork A) failed by 2–4 orders of magnitude (`cz_inversion/`); connectons are conserved, exactly as in cdot-4 |

**Bottom line.** The local-gravity program's *mechanisms* — foam diffusion, the RAR
closure's shape, the dynamical-selection attractor, the river — are exactly as
separable from the cosmological counting law as T23 predicted when it recommended this
program survive cdot-4's BAO exclusion intact. The program's two places where a
cosmological length scale was plugged in for a *number* — the MOND acceleration
$g_\dagger$ and the holographic sea density $\rho_\text{bg}$ — lost their old clean
referent ($R_0=6c/H_0$) when the counting law changed, but the percolation transition
restores a finite horizon (three candidate lengths, not one), turning "rebuild from
nothing" into "recalibrate against a specific, computable number, and decide which one
is physically correct." This is still the single most important open task in the
connecton program, but it is now a narrower one than the previous reconciliation pass
found.

---

## Open Items, In Priority

1. **Decide which finite length sets the crossing-rate/holographic scale, and
   recompute $g_\dagger$ and $\rho_\text{bg}$ against it.** Superseding both cdot-4's
   item 1 (force-law confirmation of a kinematic guess) and this document's own
   previous framing (no finite length exists): three candidates are now in hand ($L$,
   $R_\text{now}$, $D_p(\infty)$), the best gets within $1.63\times$ of $a_0$, and the
   remaining task is a specific recalibration plus a conceptual choice, not an
   open-ended search. See "Energy Scale" and "Toward the RAR" above.
2. **Attractor convergence** — unaffected, unchanged from cdot-4: does the Lorentz
   filter genuinely concentrate the surviving population at $r_t$ at all radii? A
   dynamical-systems proof is the binding constraint.
3. **$G$-normalization** — unaffected in framing, but now depends on item 1's outcome:
   reconciling the sea density with the $G$-setting condition requires first knowing
   what the sea density is.
4. **Global bookkeeping** — is $\dot c/c=H$ from the connecton network's growth
   consistent with the same field giving local Newtonian gravity? Unaffected question,
   now asked of the connectivity-counting network rather than the occupancy count.
5. **Derive the frame-flow profile $w=\sqrt{2GM/r}$ from connecton dynamics** —
   unaffected, unchanged from cdot-4; see T22. The single highest-priority *local*
   calculation, distinct from item 1's cosmological one.
6. **Two-population coexistence** — unaffected, unchanged from cdot-4; two quantified,
   undecided candidates (endpoint-only interaction, illustrative Rayleigh
   cross-section).
7. **Momentum/inertia consistency of the river** — resolved in cdot-4 via the
   ram-pressure budget; the conclusion is confirmed robust here despite $\rho_\text{bg}$
   now being open (see "The Inertia No-Go Result" above).
8. **Reconcile the river's derivation with the connecton ontology** — resolved in
   cdot-4 (category distinction, collective-mode vs. link velocity); unaffected.
9. **De-double-counting** — resolved in cdot-4 (Bernoulli identity); unaffected.
10. **Continuous emission** — unaffected, unchanged from cdot-4; whether emission only
    at creation is allowed remains open. (The connecton-sink question raised against
    this item in an earlier reconciliation pass is retired: conservation is restored,
    see the top note and "The Idea" above — there is no sink for continuous emission to
    interact with.)
