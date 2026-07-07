# Research Notes — The Path to cdot-6's Foundation

*This document exists so `Foundation.md` can stay clean of history. Everything here is
context, motivation, and a record of dead ends — nothing here is load-bearing for the
Foundation itself, which is meant to stand alone. Cross-references to `cdot-1` through
`cdot-5` live here, not there.*

---

## 1. Why cdot-6 Starts Over, Rather Than Patching cdot-5

cdot-1 through cdot-3 explored variable-$G$ ($G\propto c^{-2}$) and PV-influenced mass
scaling; cdot-4 adopted invariant $G$ and invariant mass after the Lunar Laser Ranging
(LLR) test refuted $G\propto c^{-2}$ at $\times720$ (`cdot-4/T8_Gravitational_Constant.md`),
and built a full topic-document program (T1–T22) plus a horizon/occupancy counting law
for $c(t)$'s cosmological history. That counting law was excluded outright by the DESI
DR2 BAO Alcock–Paczyński test for every exponent (`cdot-4/T23_The_Failed_Tests.md`).

cdot-5 replaced it with, successively: autocatalytic connectivity counting (fit the
clean DESI galaxy bins, failed at high $z$); a percolation-broken two-phase law (fit all
six DESI bins at $\chi^2=6.8/8$, the best cdot-5 result); then failed the CMB first-peak
test, which led to a deep dive into the baryon-loading value $R\approx680$ and a
recombination-physics investigation that found no single photon-sector convention gives
both a sensible $R_\text{rec}$ and a sensible $z_\text{rec}$ simultaneously; and finally
a "hyperbolic-holographic" geometric replacement for the counting law's own mechanism,
which fit DESI far worse and still didn't fix the CMB. **The decisive diagnosis**
(`cdot-5/T24_The_Cosmological_Sector_Closed.md`): the CMB failure traces to premises 1
(static geometry), 3 (invariant mass), and 4 (photon-frequency conservation) — not to
premise 2, the counting law — meaning no further counting-law replacement could have
fixed it. T24 closed the cosmological (redshift–distance–CMB) sector and recommended
either focusing on the local connecton-gravity program (which survived all four
iterations unscathed) or, if cosmology were revisited, examining premise 1 or premise 4
directly rather than patching premise 2 a fifth time.

**cdot-6 is that direct examination.** Rather than keep cdot-5's static-space-plus-
connecton-counting structure and try yet another $c(t)$ law, cdot-6 starts from a
different geometric/kinematic foundation altogether (Atkinson's Euclidean reformulation
of GR, below) and asks what minimal Machian closure, built on it, could produce
MOND-like dynamics. The full cdot-4/cdot-5 topic-document apparatus (T1–T22, the
connecton ontology of T12/T14, the river derivation of T22) is not carried over into
cdot-6's Foundation — it is preserved, unedited, in its own directories, and may turn
out to be re-derivable from cdot-6's premises later, but nothing in `Foundation.md`
assumes it.

---

## 2. Two Independent Papers Checked and Rejected as Formalism Sources

Before settling on Atkinson, two papers proposing a modern "vacuum field" origin for the
MOND scale $a_0$ were checked in detail, since both were offered as possible sources of
formalism for a fresh attempt:

- **S. B. Thorwe, "Dynamic Vacuum Field Theory" (IJFMR, 2025) and "The Relationship
  Between the MOND Acceleration Scale ($a_0$) and the Hubble Constant ($H_0$) in
  Dynamic Vacuum Field Theory."** DVFT is ordinary GR (the action keeps the
  Einstein-Hilbert term) plus a nonlinear scalar field engineered to reproduce MOND via
  a Bekenstein-Milgrom-style $F(X)\propto X^{3/2}$ kinetic term — constant $c$,
  expanding space, standard redshift throughout. The specific $a_0=cH_0/2\pi$ claim was
  checked line by line: two intermediate proportionality constants are explicitly left
  undetermined ("model-dependent," "can be made explicit once... specified") and the
  final formula is simply asserted ("we therefore identify"), not derived from what
  precedes it. Rejected: wrong premises (constant $c$, expanding space) for this
  project, and unrigorous even on its own terms.
- **X. He, "Entropic Information Dynamics" (2025).** Different formalism (holographic
  bit-erasure/Landauer's principle instead of a scalar field) but the same target
  claim, $a_0=cH_0/2\pi$ — asserted via an unshown "cancellation," not derived, exactly
  as in the DVFT paper. The $\Omega_\Lambda=\ln2$ result elsewhere in the same paper has
  internally consistent algebra but rests on an unmotivated physical assumption (the
  entire holographic bit budget is erased and rewritten exactly once per Hubble time).
  Two independent numerical errors were found on inspection: a sign error in
  $V''(\psi)$, and an inflation-energy-scale claim ($2.1\times10^{16}$ GeV) inconsistent
  with the paper's own stated density ($10^{96}$ kg/m³) by a factor of several hundred.
  Rejected for the same premise mismatch as DVFT, plus these specific errors.

**The pattern worth remembering:** both papers, independently, converge on the same
decades-old $a_0\sim cH_0$ dimensional coincidence (Milgrom flagged this order-of-magnitude
relation himself) and dress it in elaborate, correctly-cited formalism (holographic
principle, Landauer's principle, Lagrangian field theory) that does not actually connect
to the final numerical claim when checked. Impressive-looking machinery around one
un-derived assertion is a recognizable failure mode, not a coincidence of two unrelated
authors — treat any future paper in this genre with the same suspicion.

---

## 3. Atkinson (1963): What It Actually Contains, and Why It Was Chosen

`R. d'E. Atkinson, "General Relativity in Euclidean Terms," Proc. Roy. Soc. Lond. A 272,
60–78 (1963)` — read in full (the scanned JSTOR copy, OCR'd via direct multimodal
reading since `pdftotext` failed on it). This is the founding paper of what became
Puthoff's "Polarizable Vacuum" (PV) program decades later, but Atkinson's own paper is
narrower and more honest than the later PV literature: it treats **only** a single
stationary mass and Einstein's vacuum equations ($G_{\mu\nu}=0$), and states explicitly
(p. 64): *"Nothing either new or even old is assumed (at least expressly) about
gravitation."* $\psi=fM/2rc^2$ is taken directly from the already-known Schwarzschild
solution, not derived from a mass-sourcing field equation. The two postulates
$c_r=c(1-\psi)/(1+\psi)^3$ and $\mu_r/\mu=(1+\psi)^5/(1-\psi)$ are explicitly labeled
*ad hoc* by Atkinson himself — adopted because they work, not derived from a deeper
principle — and checked, in the paper, to reproduce light deflection, gravitational
redshift, and the perihelion advance exactly, via a Lagrangian treatment (Pryce's,
per Atkinson's acknowledgment) and direct geodesic-equation matching.

**Why this, and not Puthoff's later extension:** Puthoff's PV program generalizes
Atkinson's single-mass ad hoc postulates into a field theory (a scalar $K$ sourced by
mass distributions generally, with $\epsilon_0,\mu_0\to K\epsilon_0,K\mu_0$) and commits
to specific cosmological consequences — $G\propto c^{-2}$ and $m\propto c^{-3/2}$ — that
this project has excluded (T8's LLR calculation; cdot-5's T4 via the SN Hubble diagram).
**Correction (2026-07-07): the LLR figure needs a precision caveat — see §3.2 below; the
conclusion survives, but T8 did not literally test PV's own combined package.**
Atkinson's own paper commits to neither: it has no time dependence at all, and says
nothing about how $G$ or the reference mass/light-speed scale should behave
cosmologically. Building on Atkinson directly, rather than on Puthoff's cosmological
extension, avoids reopening a question that's already been answered.

### 3.1 A gap this reading exposed in cdot-4/cdot-5's own reasoning

cdot-4's T22 (`cdot-4/T22_Gravitational_Lensing_and_Local_Gravity.md`) tried a PV-style
local approach first, found it required a "Two-Regime Dictionary" — local mass dressing
$m\propto K_\text{grav}^{3/2}$, i.e. Atkinson's own $\mu_r(\psi)$ structure in different
notation — and discarded it in favor of the Gullstrand–Painlevé "river" derivation,
specifically by imposing strict local mass invariance ($\sigma=0$ in T22's own
three-channel taxonomy), justified as *"already the model's standing commitment —
T8/T21."* Checking T8 directly: **T8's refutation is about $G\propto c^{-2}$ (tested
against mass already taken invariant, per T4) tracking the cosmologically-evolving
$c(t)$ over time** (the LLR calculation is explicitly a secular-drift test, $\dot
r_\text{LLR}/r_\text{LLR}\propto H_0^\text{hor}$; the mass-scaling rejection is a
*separate* test, citing the SN Hubble diagram's redshift power — see §3.2 for why these
being two separate tests, not one joint test, matters). Neither test says anything about
a purely **local, position-dependent, single-epoch** mass or light-speed variation near
an ordinary body — which is all Atkinson's $\mu_r(\psi)$, $c_r(\psi)$ actually claim.
T22's extension of cosmological mass invariance to local invariance was a
consistency/parsimony choice, not something T8 independently forced. This means
Atkinson-style local dressing was never actually refuted by anything in this project —
only set aside. cdot-6's Foundation §2 revives it deliberately, and §5 item 6 flags that
its compatibility with solar-system data (PPN, ephemerides) still needs an honest check,
not an assumption either way.

### 3.2 T8's LLR figure was for a hybrid, not literal PV — redone for real PV, it's worse

The author's objection (2026-07-07): T8's self-consistent LLR calculation runs
$G\propto c^{-2}$ with mass held invariant — but PV's own claim is $G\propto c^{-2}$
*and* $m\propto c^{-3/2}$ *together* (both are consequences of the same vacuum
polarizability $K$). T8's own text confirms this precisely: *"The model already
abandoned PV for the mass scaling: it takes invariant mass $s=0$, not PV's
$m\propto c^{-3/2}$, on empirical grounds. Once PV is abandoned for mass, the PV-native
value of $G$ loses its privileged status"* — i.e. invariant mass was adopted first
(from T4's SN Hubble diagram fit, a separate test), and the LLR calculation then tested
$G\propto c^{-2}$ *against that already-invariant mass*, not against PV's own paired
value. The $\times717$/$\times720$ figures are for this hybrid. Literal, self-consistent
PV was never actually run through T8's machinery. §3's claim above (and elsewhere in
this project) that T8 "refuted PV via LLR" overstates what was actually computed —
corrected here.

**Redone for genuine PV.** Generalizing T8's own derivation chain with $G\propto c^g$
and *all* rest mass (Earth, Moon, and the electron mass feeding the atomic clock's
Rydberg-type frequency — PV's self-energy scaling is universal, so it has to apply
there too, not just to gravitating bodies) scaling as $m\propto c^s$: the orbital
radius from $L=m\sqrt{GMr}=\text{const}$ goes as $r\propto c^{-(3s+g)}$, and the atomic
clock rate from $\nu\propto m_e\epsilon_0^{-2}\propto m_ec^2$ (invariant $e,h$,
$\epsilon_0\propto c^{-1}$ from an invariant fine-structure constant) goes as
$\nu\propto c^{s+2}$. Carrying both through T8's own ranging-formula steps gives a
single net exponent for the LLR range-rate:
$$\frac{\dot r_\text{LLR}}{r_\text{LLR}}=E\,H_0^\text{hor},\qquad E=-2s-g+1.$$
T8's actual test point ($g=-2,s=0$) gives $E=3$, exactly reproducing their $+41.4$
mm/yr, $\times717$ result — confirms the formula. PV's own point ($g=-2,s=-3/2$,
both together) gives $E=6$ — **twice T8's tested exponent**, i.e. $\approx82.8$ mm/yr,
a $\times1429$ exclusion. The softer clock-rate exponent under running mass
($\nu\propto c^{1/2}$ instead of $c^2$) is more than offset by the much steeper
orbital-radius exponent ($r\propto c^{6.5}$ instead of $c^2$, since angular-momentum
conservation now has three factors of $c^s$ working together instead of one factor of
$c^g$ alone). **Genuine PV is excluded more decisively than T8's own figure, not less —
the substantive conclusion survives; only the precision of "T8 refuted PV" needed
correcting.** (Same caveat as T8's own calculation: this uses the adiabatic-invariant
$L=\text{const}$ assumption without re-deriving it for the case where mass itself is
time-varying — a limitation inherited from the original, not introduced here.)

The formula also places cdot-6's own LLR check (§7.1) in the same frame: $g=0,s=0$
(invariant $G$, invariant $\mu$, borrowed $\nu\propto c^2$) gives $E=1$, exactly the
$\times238$ result found there.

---

## 4. The Cosmological Extension: Working Notes Behind Foundation §3

The idea of extending Atkinson's single-mass closure to the whole observable universe —
replacing $M,r$ with the horizon's own enclosed mass $M_h(t)$ and radius $R_h(t)$ — was
developed in two passes:

**Pass 1 (rejected outright; Foundation §3.3).** The direct substitution posits
$c=c_\text{ref}(1-\psi_h)/(1+\psi_h)^3$ (Atkinson's own rational function, reused
unchanged, with the $\psi_h=0$ reference value initially called $c_\infty$ — a label
retired once the author objected to it, §5 below, since it wrongly suggested "the value
at $z=\infty$" when it actually needed to be the value at $z=0$). This was killed by a
clean argument, prompted directly by the author questioning the $c_\infty$ notation:
genesis is $\psi_h=0$ (from $M_h\propto R_h^3$, so $\psi_h\propto R_h^2\to0$ as
$R_h\to0$), and the standard redshift convention requires $c\to0$ there — but the
rational function gives $c=c_\text{ref}\cdot1=c_\text{ref}$ at $\psi_h=0$, a fixed
nonzero value. Forcing $c_\text{ref}=0$ to fix the genesis point collapses $c(t)\equiv0$
for *all* $t$, since $c_\text{ref}$ multiplies the whole function. This is decisive on
its own — no numerics needed.

A second, independent line of evidence, found first (before the cleaner genesis
argument) and worth keeping as corroboration: solving the self-consistency equation
$\psi_hc^2=\kappa R_h^2$ (with $\kappa\equiv2\pi G\rho/3$) explicitly for $R_h(\psi_h)$
gives $R_h^2\propto f(\psi_h)\equiv\psi_h(1-\psi_h)^2/(1+\psi_h)^6$, and $f$ has a
**maximum at $\psi_h\approx0.13$** ($f_\text{max}\approx0.047$, checked numerically by
direct evaluation at $\psi=0.05,0.10,0.12,0.13,0.14,0.15,0.20$) — so $R_h$ cannot grow
monotonically under this closure at all, quite apart from the genesis-value problem.
Both findings point the same way: reusing Atkinson's single-mass rational function
directly for the cosmological closure is wrong, not merely incomplete.

**Pass 2 (Foundation §3.4, provisional fallback).** Dropping Atkinson's exact rational
functions and using only the leading Sciama-type scaling $c^2\propto GM_h/R_h$ (i.e.
$c\propto R_h$, given homogeneous $M_h\propto R_h^3$) gives a solvable, if less
rigorously grounded, cosmology: $\dot c/c=H_0^\text{hor}$ exactly constant (a
simplification not present in any cdot-4/cdot-5 counting law), $c(t)=c_0e^{H_0^\text{hor}
(t-t_0)}$ — which, unlike Pass 1, gives $c\to0$ at genesis correctly, by construction, not
by patching — a **finite** particle horizon $D_p(\infty)=c_0/H_0^\text{hor}$ with no
percolation break or hyperbolic geometry needed to get there, $\tau_\infty=1/H_0^\text{obs}
\approx13.97$ Gyr (strikingly close to $\Lambda$CDM's own 13.8 Gyr, tighter than any
cdot-4/cdot-5 iteration's margin over the oldest globular clusters), and $q_0=+1/2$ at
leading order (more decelerating than cdot-4's original $+1/6$, flagged as a concern for
the SN Hubble diagram once that's back in scope). All of this is explicitly provisional,
pending §3.3's actual resolution — Pass 2 sidesteps the closure question rather than
answering it, using only §3.2's mass-radius scaling directly.

**Note on $n=1$ and DESI.** $c\propto R_h$ is exactly the $n=1$ power law already in
cdot-5's own DESI fit table (`cdot-5/T23_Autocatalytic_Counting.md` §4), excluded at
$\chi^2=552$ — worse than the volume law's 98. Per the author's explicit direction
(2026-07-07), DESI-fit quality is deliberately out of scope while the local sector is
being rebuilt; this exclusion is recorded here so it isn't forgotten, not because it's
being ignored by accident.

---

## 5. The MOND Conjecture Behind Foundation §4

The idea that a MOND-like transition could emerge from comparing a *local* $\psi$ (near
an ordinary mass) against the *cosmological background* $\psi_h$ is new to cdot-6 — it
has no direct antecedent in cdot-4/cdot-5's connecton-diffusion account of the same
phenomenology (`cdot-4/T14_Connecton_Gravity.md`, `T15_Radial_Acceleration_Relation.md`),
though the dimensional shape of the crossover condition ($GM/r^2\sim g_\dagger$) is the
same one cdot-4/5 used throughout, and the cdot-4/5 program's three-candidate-length
problem for $g_\dagger$ (`cdot-5/T6_MOND_Acceleration_Scale.md`, `T14`) is the same kind
of question $\psi_h$'s value would need to answer here. Whether the connecton-diffusion
mechanism and this $\psi$-competition idea are two views of the same underlying physics,
or genuinely different mechanisms that happen to share a dimensional coincidence, is not
yet known. Nothing from the connecton program (T12/T14's foam-diffusion argument, T15's
indistinguishability-based RAR closure) has been imported into cdot-6's Foundation; if
the $\psi$-competition idea fails to produce MOND-like dynamics on its own, that
existing derivation is the natural fallback to revisit, not a source to blend in
prematurely.

---

## 6. Why $c_0,c_z$ Are Relational, Not Measured (and What This Does to §3.6 Item 3)

Prompted by the author questioning what "the value we measure" could even mean given
that, in an SI-convention world, $c$'s numerical value is fixed by definition (a
cycle-count second plus a light-travel-time metre), not by measurement — and that both
length and time standards trace back to the same local light-speed/atomic-transition
physics, so no self-consistently-calibrated local observer can ever measure their own
$c$ to differ from any other's. Foundation §3.1 now states this explicitly: $c_0,c_z$
are cross-epoch relational bookkeeping, the same role redshift $z$ itself plays, not
instrument readings. This is not a new premise — it is arguably what cdot-1 through
cdot-5's "redshift is a drifting local atomic reference standard, not a photon energy
loss" framing (used throughout that whole project's T2/T7/T18 lineage) already implied,
now stated as an explicit operational point for cdot-6 rather than left implicit.

**Consequence for §3.6 item 3.** The question "does an atomic clock's tick rate depend
on cosmological $c(t)$" was ambiguous in exactly the way this section clarifies: read as
"does a clock disagree with its own past self," the answer is tautologically no. The
question that actually matters, and the one item 3 now asks, is whether two
*independently-built* local clocks — one atomic, one gravitational/orbital — drift
*relative to each other* over cosmic time. This is, precisely, what cdot-4's T8 LLR
calculation tested (`ResearchNotes.md` §6, this document): the self-consistent
computation compared round-trip light time (an atomic-clock-timed quantity) against
orbital dynamics (a $G,M$-timed quantity) and found they would disagree at a rate LLR
already excludes, if $G\propto c^{-2}$. Framing §3.6 item 3 this way — relative drift
between two differently-sourced local clocks, not an absolute reading — is the correct,
checkable version of the question, and it's the version whoever picks up that item
should actually compute.

---

## 7. Why Foundation §3.6 Exists: the LLR Precedent

Foundation §3.6 (local systems are not automatically immune to cosmological drift) is
motivated directly by cdot-4's T8 episode
(`cdot-4/T8_Gravitational_Constant.md`), and is worth recording explicitly here even
though the Foundation itself states the principle without the history.

cdot-3 adopted $G\propto c^{-2}$ (a Polarizable-Vacuum-native choice). cdot-4's T8 ran
the *self-consistent* Lunar Laser Ranging calculation — not just a naive $\dot G/G$
estimate, but the full chain: orbital expansion ($r\propto c^2$, from angular-momentum
conservation with $G$ varying), the varying light-travel time in the ranging formula
itself, and the varying atomic clock rate ($\nu\propto c^2$, from cdot-4's premise 4 and
invariant charge/mass). All three effects turned out to be roughly the same order of
magnitude and to **add rather than cancel**, giving a predicted non-tidal range-rate of
$+41.4$ mm/yr against an observed bound of $<0.058$ mm/yr — a $\times717$ exclusion, and
an inferred $\dot G/G$ excluded by $\times720$ against the direct LLR bound. This is why
cdot-4 adopted strict, unconditional $G$ invariance from that point on, and it is the
single sharpest lesson of the entire cdot-1 through cdot-5 line: **a cosmological rate
that looks small ($H_0^\text{hor}\sim10^{-18}\,\text{s}^{-1}$) is not automatically safe
at solar-system scale** — several channels can each pick up a factor of the same rate
and add up to something high-precision instruments already rule out.

cdot-6's Foundation does not yet make any claim about whether $G$, the reference mass
$\mu$, or atomic clock rates track the cosmological $c(t)$ of §3 — this is a genuinely
open question for the new framework, not something inherited automatically from cdot-4's
resolution (cdot-6's premises are different enough that the old answer isn't guaranteed
to still apply, though it is the natural first thing to try: adopting strict $G$ and
cosmological-$\mu$ invariance, exactly mirroring cdot-4's own resolution, would most
likely reproduce the same safety cdot-4 found — but this needs to be checked for cdot-6's
own specific relations, not assumed by analogy). Whoever picks up Foundation §5 item 1
should redo T8's *style* of calculation (identify every channel that could carry a
$\dot c/c$-type rate into a local observable, check whether they cancel or add) for
cdot-6's own $c_r(\psi)$, $\mu_r(\psi)$, and whatever redshift/clock-rate relation
emerges from item 4 — not assume the old answer transfers.

### 7.1 This has now been done, and invariant $G$ turns out not to be enough

Redoing T8's calculation for cdot-6 (2026-07-07): take the natural first-try answer to
items 1–2 (strict $G$ and $\mu$ invariance, hence static orbits, $r_\text{EM}=$const —
removing T8's largest single contributor, orbital expansion), and use the redshift/clock
relation §3.4 already imports provisionally, $\nu(t)=\nu_0(c(t)/c_0)^2$, for item 3.
Tracking the actual round-trip proper time recorded by an atomic clock,
$\Delta\tau=(c(t)/c_0)^2\Delta t_\text{coord}$ with $\Delta t_\text{coord}=2r_\text{EM}/
c(t)$, against a data-reduction pipeline that assumes constant $c,\nu$: the inferred
range is $r_\text{LLR}(t)=r_\text{EM}\cdot(c(t)/c_0)$, giving $\dot r_\text{LLR}/
r_\text{LLR}=\dot c/c=H_0^\text{hor}$ — one power, from $-1$ (naive light-travel-time
bookkeeping) and $+2$ (clock rate) combining to $+1$, not zero. Numerically,
$\approx13.8$ mm/yr against the $<0.058$ mm/yr non-tidal LLR bound — a $\times238$
exclusion, from the clock-rate channel *alone*, with orbital expansion already removed.
This is a genuine subset of T8's own arithmetic, not a new estimate: T8's three-channel
sum was $-1+2+2=+3$ powers of $H_0^\text{hor}$, giving $3\times13.8\approx41.4$ mm/yr,
matching their quoted figure exactly; dropping the $+2$ orbital-expansion term (absent
here because $G$ is invariant) leaves $-1+2=+1$, i.e. this result.

**Retroactive note on cdot-4's own T8.** T8's text asserts that adopting invariant $G$
gives static orbits and therefore "the LLR ranging signal has no cosmological
component" — but that statement does not appear to have re-run the clock-rate-alone
channel to check it; it simply declared the problem solved once orbital expansion
vanished. The calculation above suggests that check would have failed even for cdot-4's
own premises, since cdot-4's own $\nu\propto c^2$ relation (its premise 4, invariant
charge/mass) is exactly what's used here. cdot-4 is closed and this document is not
editing it, but it's worth recording plainly: the residual channel identified here looks
like a real gap in that closed document's own reasoning, not something specific to
cdot-6's different premises.

**What this means for cdot-6.** Invariant $G$ (§5 item 1's natural first guess) is
necessary but not sufficient. The framework's survival now hinges entirely on whether
§5 item 4 — deriving the redshift/clock-rate mechanism from §2's own Atkinson closure,
rather than importing $\nu\propto c^2$ from cdot-4/5's separate premise 4 — produces
something other than $\nu\propto c^2$. If it reproduces the same relation, cdot-6 fails
this test the same way cdot-3's $G\propto c^{-2}$ did, just via a different channel. This
is now the single most urgent open item in the Foundation, not one among several.

### 7.2 The author's follow-up: is this really about which mass law, or something deeper?

Prompted directly by the author (2026-07-07): the exercise above only tried one
candidate for item 3 (the imported $\nu\propto c^2$). Two further checks close this out.

**First, does Atkinson's own $\mu_r(\psi)$, applied cosmologically, give something
different?** Tempting, but it runs into the same category error §3.3 already used to
reject reusing $c_r(\psi)$ cosmologically: Atkinson's $\psi$-dependence describes how
properties vary *across space, at one moment*, for one static system — not how a
reference value evolves *across cosmic time*. Taken at face value anyway, using
Foundation §3.4's adopted closure ($c\propto R_h$): since $M_h\propto R_h^3$ and
$c\propto R_h$, $\psi_h\equiv GM_h/(2R_hc^2)\propto R_h^3/(R_h\cdot R_h^2)=R_h^0=$
**constant** — Sciama-type scaling is, by construction, exactly the statement that
$\psi_h$ doesn't evolve. Plugging a constant into Atkinson's $\mu_r(\psi_h)$ formula
trivially gives a constant $\mu$ — i.e., invariant reference mass, not a new prediction.
But this doesn't resolve item 3 on its own: the $\nu\propto c^2$ relation comes from
$\nu\propto m_e\epsilon_0^{-2}$, and the $\epsilon_0\propto c^{-1}$ factor is an
electromagnetic-sector assumption inherited from cdot-4/5's premise 4 — Atkinson's paper
says nothing about electromagnetism at all. Invariant $\mu$ alone doesn't touch that
factor, so $\nu\propto c^2$ (and the $\times238$ exclusion) survives regardless.

**Second, is this fixable by choosing a different mass-scaling exponent, motivated or
not?** Generalizing §3.2's formula $E=-2s-g+1$ with $g=0$ (invariant $G$, effectively
forced by the separately very tight $\dot G/G$ bounds) and solving $E=0$: $s=+1/2$ is
the unique value that cancels the LLR signal exactly. It exists — the problem is not
mathematically unsolvable — but it is the opposite sign from every physically motivated
mass law considered (PV's $-3/2$, Atkinson's own implied $0$), is not implied by
anything in Atkinson's postulates, and has no independent motivation: its only property
is that it cancels the number. Adopting it would be exactly the "selected by agreeing
constraints, not derived" move T8 itself flagged as a standing debt for cdot-3's
$G\propto c^{-2}$ — repeating that move to patch cdot-6 would not be progress.

**The sharper finding: an irreducible floor, independent of any mass/clock assumption.**
Stripping the calculation to zero local coupling — invariant $G$, static orbit, and an
atomic clock rate held perfectly fixed ($\nu=\nu_0$, no $c$-dependence assumed at all —
not even Atkinson's own postulates invoked) — the light-travel-time bookkeeping alone
still gives $r_\text{LLR}(t)=r_\text{EM}\cdot(c_0/c(t))$, i.e. $\dot r_\text{LLR}/
r_\text{LLR}=-H_0^\text{hor}$, the same $\times238$-level signal with the opposite sign.
This is not a consequence of any assumption about $G$, mass, or atomic physics — it
follows purely from $c(t)$ genuinely differing from its value 50 years ago, which is
premise 3's entire content. Recorded in `Foundation.md` §3.6, since this is now a
load-bearing structural conclusion, not history.

**Resonance worth flagging, not a repetition:** a structure that insulates local
systems from a cosmologically-evolving background quantity is exactly the shape of
T22's withdrawn "Two-Regime Dictionary" (`cdot-4/T22_Gravitational_Lensing_and_Local_
Gravity.md`) — though T22's version was about whether *mass* dresses locally via
Atkinson's $\psi$, a narrower claim than what this floor requires (the *local value of
$c$ itself* not tracking the cosmological rate, at any order, through any channel). If
cdot-6 ends up needing a local/cosmological split, it should be built to answer this
specific, sharper requirement — not assumed to be the same fix T22 already tried and
walked back.

---

## 8. Open Threads Not Yet Reflected in the Foundation

- Whether the redshift mechanism itself (comparing a photon's frequency against a local
  atomic standard) can be derived from Foundation §2's own $\mu_r,c_r$ closure, rather
  than imported from cdot-4/cdot-5's separate premise 4 (photon frequency exactly
  conserved in flight) as §3.5 currently does implicitly.
- Whether the entire cdot-4/cdot-5 local-gravity program (T14's foam diffusion, T22's
  river) is recoverable as a special/approximate case of cdot-6's Foundation, once §3.4
  and §4 are resolved — or whether cdot-6 genuinely supersedes it.
- The connecton ontology (T12: "a conserved unit of relation, not a particle") has not
  been invoked anywhere in the Foundation. Whether cdot-6 needs an ontological
  commitment of this kind at all, or can remain agnostic about *what* mediates the
  Machian relation between mass and $c$ (matching the author's original instruction to
  keep connecton-specific assumptions to a minimum), is itself an open stylistic and
  substantive choice for future sessions.
