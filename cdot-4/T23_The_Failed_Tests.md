# T23 — The Failed Tests

*This document is the honest ledger of cdot-4's ending. It exists because the project's
own stated ethos (Core Principles, "Why") is to pursue falsification, not just
consistency — and two independent, decisive tests (BAO, and the deeper structure the
CMB and Machian-mass investigation exposed underneath it) came back against the model's
cosmological sector. This is not a T-document in the usual sense: it does not propose a
mechanism. It consolidates (a) results already scattered across `desi_bao/` and
`cmb_peak/` that never made it into the numbered topics, (b) material from `new_tests/`
that was superseded, dropped, or walked back on the way into T12/T14/T22 and would
otherwise be lost, and (c) the final round of testing — whether a Machian mass-counting
model could rescue the cosmological sector — that closes out cdot-4. cdot-5 starts from
here.*

---

## Part I — The Cosmological Distance Sector: Decisive Failure

### 1.1 The DESI DR2 BAO Confrontation

The sharpest candle-free geometric test available was run against the model's core
distance relation, $D_p(z)=R_\text{now}[1-(1+z)^{-\alpha}]$, $\alpha=1/(nP)$ (Core §4/§4a).

**Full 13-point fit** (DESI DR2, 7 tracers, $0.295\le z\le2.330$, per-tracer $2\times2$
covariances): static model $\chi^2=150.9$ (13 pts, 1 param, best-fit ruler
$r_d=121.7$ Mpc) vs. flat $\Lambda$CDM $\chi^2=10.5$ (13 pts, 2 params, $\Omega_m=0.297$,
matching DESI's own published value — pipeline validated). **$\Delta\chi^2=+140$ with
one fewer parameter, a $\sim12\sigma$-equivalent exclusion.** Per-bin pulls show a
$z$-dependent, sign-rotating anisotropy no normalization can absorb: $D_M$ pulled high
at low $z$, $D_H$ pulled hard low near $z\approx0.9$–$1.3$, signs flipping by $z=2.33$.

**Parameter-free Alcock–Paczyński test**, $F_\text{AP}=D_M/D_H$ (immune to $r_d$, $H_0$,
and, in this model, to $R_\text{now}$ — every overall normalization cancels): six DESI
DR2 bins, **zero free parameters**, $\chi^2=67.8$ (first pass) / **93.9** (corrected,
forced $A=1$ — see §1.3). Worst single pull $+7.9\sigma$ at $z\approx0.93$. Matching
$D_M$ alone wants $r_d=119$–126 Mpc; matching $D_H$ alone wants $112$–122 Mpc — a 10%
disagreement *at the same redshift*, which no ruler evolution $L(z)$ can repair (a
transverse and a radial ruler must be the same physical object).

**Family-level result — the exclusion reaches the premises, not a parameter.** Letting
the counting exponent $\alpha=1/(nP)$ float freely across *every* member of the family
(any $n$, i.e. any horizon-counting law, not just the volume law): best fit
$\alpha=0.095\pm0.010$, $\chi^2=102.8$ (11 dof) — **still hopeless**. The model's actual
$\alpha=1/6$ sits $7.1\sigma$ from even this least-bad member, and the least-bad member
requires $nP\approx10.5$, incompatible with $P=2$ (pinned by the squared redshift law,
mass invariance, T2/T4) and $n=3$ (volume counting, premise 2). **No member of the
family fits, and the least-bad member contradicts the rest of the model.** The general
theorem behind this: in any static model, $F_\text{AP}(z)$ determines the mapping
completely via $D(z)\propto\exp\int dz/F_\text{AP}(z)$; DESI's $F_\text{AP}$ run dictates
a redshift–distance mapping that is $\Lambda$CDM's comoving-distance shape, which no
$R_0[1-(1+z)^{-\alpha}]$ solution reproduces, for any $\alpha$.

**Escape routes, assessed and foreclosed:**
1. RSD/template systematics — would need a coherent $+10\%$ bias in $F_\text{AP}$ peak
   position at $z\approx0.93$, 20–100$\times$ DESI's actual systematic budget
   (0.1–0.5%). Formally open; not credible as stated; would require the model to build
   its own full anisotropic clustering pipeline (it has none).
2. Ruler evolution $L(z)$ — foreclosed by the radial/transverse required-ruler split at
   fixed $z$ (above).
3. Different counting exponents — foreclosed by the family-level result (above).
4. Abandon the horizon-counting mapping — the only route that fits the data, and *not*
   an escape: a falsification of the cosmological sector as constituted.

### 1.2 Assumptions Audit: the Early Universe Cannot Be Blamed

Prompted by the challenge "did the test assume different initial conditions than the
model's own genesis physics?" — audited and confirmed: the failing quantity,
$dz/dD=(H_0^\text{obs}/c_0)(1+z)^{7/6}$, contains **no plasma-era quantity whatsoever** —
only late-time kinematics (the counting law's horizon rate, light propagation through
the static map). The test's only three assumptions about the pre-recombination era were
(i) one intrinsic scale, (ii) statistical isotropy (a symmetry theorem, not a modeling
choice — the AP channel is insulated from *any* imprint physics by construction), and
(iii) a frozen proper length post-recombination (forced by staticity). The sound-horizon
value itself was left fully free (marginalized).

**The "identical initial conditions" intuition, taken literally, is worse, not better.**
$\Lambda$CDM's $r_d=147.1$ Mpc comoving is a $0.134$ Mpc *proper* length at
recombination; identical local physics would imprint that same $0.134$ Mpc, which the
static model then *freezes* — $\sim900\times$ smaller than the $\sim122$ Mpc the data
need. Marginalizing $r_d$ away, as the main test did, was maximal charity, not an
oversight.

**By-product: the model's first quantitative genesis constraint.** Using
$L_s=(R_\text{rec}-R_\text{gen})/\sqrt3$ (sound horizon as frozen proper distance from
genesis to recombination): perturbations seeded at the BBN epoch ($z\sim10^{10}$) give
$L_s=4.3$ Gpc — $\sim35\times$ too large. Matching the required $122$ Mpc forces
$z_\text{gen}\approx1290$, i.e. the perturbation/PBH-seeding epoch would have to sit
**just before recombination** ($z\approx1290\to1100$), remarkably late and a sharp,
falsifiable target for T13's genesis gate — independent confirmation that the model's
plasma era cannot be a relabeled $\Lambda$CDM plasma era.

### 1.3 The Alcock–Paczyński Shape Test: Naming the Structural Fault

A second, independent AP run (DESI DR2 Table IV values, six bins) sharpened the
diagnosis from "any exponential law fits poorly" to a precise structural statement.

Pipeline validated first: flat $\Lambda$CDM ($\Omega_m=0.31$) gives $\chi^2\approx9$
(pass); the $R_h=ct$ toy model gives $\chi^2\approx53$ (correctly fails) — confirming the
test machinery before use.

**Corrected result.** An initial free-normalization fit gave a misleadingly good
$\chi^2\approx28$; recognizing that $D_M=D_p$ and $D_H=dD_p/dz$ share the same prefactor
$R_\text{now}$ **forces** $A=1$ — not a fit choice — raising the honest, parameter-free
value to $\chi^2=93.9$ (volume law), $175.9$ (surface law), with the S-shaped residual
(over-predicting $F_\text{AP}$ across $z\approx0.5$–$1.3$, worst $+7.9\sigma$ near
$z=0.93$, swinging under by $z=2.33$) unfixable by any single exponent — even the
unphysical free-exponent optimum ($nP\approx27$) still gives $\chi^2=49.6$.

**The fault, precisely.** Not normalization (the AP ratio removes $r_d$, $H_0$,
$R_\text{now}$ identically). Not a clock-choice artifact (T3's open $H_\tau$-vs-$H^\text{hor}$
ambiguity does not arise here — $D_H$ is *derived* as $dD_p/dz$, not chosen; two-clock
variants were tested separately and fare far worse, $\chi^2\gtrsim300$). **The real
culprit: because $D_M$ and $D_H$ both descend from the single function $c(t)$ that also
fixes redshift, the model has only one free function.** The AP ratio collapses to a
one-parameter shape too rigid to track the data at any exponent. This is the
**$D_H=dD_p/dz$ lock**: redshift clock and distance ruler are fused into one object by
the horizon-counting premise. Any surviving alternative must break exactly this lock —
make the ruler depend on the counted content independently of the horizon-growth
integral ($M_u\not\propto R^3$), via an epoch-dependent counted density fixed by
independent physics, not tuned.

### 1.4 The Frozen-Large Cross-Checks

Clarified per the author's own picture (structures imprinted large, frozen ever
since — exactly what the DESI fit's marginalized $r_d$ already implements): inverting
each DESI point for its implied frozen size gives a **directional** failure, vivid in
this framing — the same frozen object would need to be up to **10% longer across the
sky than along the line of sight** ($L_\text{transverse}/L_\text{radial}$ ranging
0.982–1.103 across the six tracers), with the anisotropy itself varying systematically
in $z$. No single frozen size at any value repairs a directional mismatch.

**New adverse cross-probe check.** The same frozen acoustic feature must serve both the
galaxy BAO and the CMB peak. Matter BAO (this fit): $L=121.7$ Mpc. CMB acoustic angle,
using $D_p(z{=}1100)=17{,}702$ Mpc and $\theta_*=1.0411\times10^{-2}$ rad:
$L_\text{CMB}=\theta_* D_p=\mathbf{184}$ Mpc. $L_\text{CMB}/L_\text{BAO}=1.51$ — a
**51% cross-probe split**, where $\Lambda$CDM serves both with one $r_d=147$ Mpc because
its mapping stretches both consistently. This is the same audit that first flagged, in
passing, that T16's "first peak translates" claim needed independent re-examination —
which Part I.5 below and the `cmb_peak/` sessions then carried out.

### 1.5 The CMB First Peak: A Partial, Incomplete Rescue

Two sessions (`cmb_peak/`) worked out T16's own open question — does the self-similar
acoustic plasma's peak land near the observed $\ell_1\approx220$?

**First pass (failure).** Using the model's Etherington-derived $D_A=D_L/(1+z)^2$ (Core
§4a, "exact"), the predicted angular scale $\theta_s=r_s/D_A(z_\text{rec})$ fell short of
$\ell_1\approx220$ by **9$\times$ (S$'$) to 765$\times$ (volume law)** at
$z_\text{rec}\approx1090$, and the shortfall survived granting the model total freedom
over $z_\text{rec}$ (best achievable $\ell_1$: 9.5–67, at unphysical $z\sim2$–5).
Separately, the invariant baryon-loading parameter $R\equiv3\rho_b/4\rho_\gamma$, taken
literally, is pinned at today's value ($\approx680$) for *all* epochs — not the
$\Lambda$CDM-like $\approx0.6$ needed at recombination for realistic peak heights,
because this static model has no differential $a^{-3}$/$a^{-4}$ dilution to shrink it
going backward.

**Second pass (partial correction, then a real limitation).** The Etherington relation
was then found to be an unjustified import: it requires the observed redshift to be a
genuine null-geodesic effect, which this model's redshift explicitly is not (premise 4:
photon frequency literally conserved in flight; $(1+z)$ is a comparison against a
drifting atomic reference, not a propagation effect). Rebuilding $D_A\equiv D_p$
directly from the model's static geometry (no $(1+z)$ suppression — nothing was ever
closer, because nothing expanded) and recomputing: volume law now gives
$\ell_1\approx313.6$, only **1.4$\times$ high** — a near miss, not a $765\times$ failure.
Surface law and S$'$ overshoot instead (3.1$\times$, 122$\times$).

**What this does and does not settle.** The correction is real and should stand (T4's
own citation of Etherington reciprocity was flagged as likely wrong for the same
reason). But it does not rescue the sector: the $1.4\times$ residual leans on
$z_\text{rec}\approx1090$ as an external, unresolved input (T16 item A), not a model
prediction; the baryon-loading problem above is untouched; and — most importantly for
this document's purpose — **the $D_A\equiv D_p$ correction is a fix to how a single
$c(t)$ history is *projected into an angle*, not a fix to the $c(t)$ history itself.**
The BAO failure (§1.1–1.3) is about the *history* — the single-function lock — and a
better projection cannot repair a wrong history. The frozen-large cross-check (§1.4)
still stands: $L_\text{CMB}\ne L_\text{BAO}$ by 51% on the model's own mapping.

### 1.6 This Session's Test: Can a Machian Mass-Count Escape the Lock?

The premise-2 fork (T12: particle count $c\propto N$ vs. classical Mach $c\propto M_u$)
was the standing candidate for breaking the $D_H=dD_p/dz$ lock. Tested directly and
found, in its literal forms, **not to escape it**:

- **As currently formulated, both readings give the same family.** $M_u$
  "mass-within-a-horizon-growing-at-$c$" under uniform density is still
  $M_u\propto R^n$ for some $n$ — a member of the *already-excluded* family (§1.1); it
  changes only $k$'s normalization, not the shape. This was independently reconfirmed:
  reverse-engineering the $c(\tau)$ history DESI's own preferred shape would require
  (using the model's fixed redshift law, $c_e=c_0(1+z)^{-1/2}$, as the only
  unquestioned ingredient) and fitting a power law in *proper* time, rather than
  coordinate time, gave what looked like a stunning sub-percent match — but checking it
  honestly (computing $F_\text{AP}$ from that law and $\chi^2$-fitting the real six
  points, not a smooth proxy curve) gave $\chi^2=3067$: catastrophic. It reduces
  algebraically to the *same* one-parameter family already excluded ($\beta$-reparametrized
  best fit $\chi^2\approx34.7$, matching §1.3's family-level $35.7$ almost exactly). **A
  single-mechanism bootstrap — count or mass, coordinate time or proper time — cannot
  escape this exclusion; the escape has to be structural, not a relabeling.** (This
  itself is a useful, generalizable lesson, and a documented self-correction: the first,
  encouraging-looking fit was an artifact of an insufficiently sensitive test metric.)
- **A genuinely two-component structure shows real promise.** $D_p(z)\propto
  [1-(1+z)^{-\alpha_1}]+w[1-(1+z)^{-\alpha_2}]$ (three shape parameters, two
  independently-scaling contributions) fit to the six AP points: $\chi^2=10.9$ —
  competitive with $\Lambda$CDM's channel-comparable $\approx9$–$10.5$, and a
  non-cosmetic improvement over the single-power-law family's best of 35–94. This is
  curve-fitting, not yet a mechanism, but it is structurally suggestive: $\Lambda$CDM
  itself only fits because it sums two terms (matter + $\Lambda$) inside the Friedmann
  equation; a single power law was never going to match a genuinely two-regime target.
- **A candidate physical mechanism for a second channel was tried: PBHs/BHs as pure
  connecton sinks** (motivated by "connectons propagate at $c$, so they cannot escape a
  horizon" — a consequence of existing premises, not a new one). Two directions tested:
  - *Locked fraction growing over time* (e.g. via ongoing PBH accretion of ambient
    baryons): makes the fit monotonically **worse** ($\chi^2$: 93.9 → 400 → 4800 → tens
    of thousands as the effect grows). Ruled out.
  - *Locked fraction shrinking over time* — using T13's own existing genesis picture
    with **no new assumption**: PBH mass fixed at genesis, "raw" sea grows $\propto R^3$,
    so the fraction $f_\bullet(R)=M_\text{BH,fixed}/M_\text{raw}(R)\propto(R_\text{now}/R)^{-3}$
    necessarily shrinks with time (capped at $f_\bullet\to1$ deep in the past — T13's own
    super-Schwarzschild statement, not a patch). This is the right direction: nearly
    parameter-free ($f_0\approx$ today's residual fraction as the one number), it gives
    $\chi^2:93.9\to25.0$ (best fit $f_0\approx0.019$, $p=3$; letting the exponent float
    only helps marginally, $\chi^2=24.2$ at $p\approx4.9$). **Real improvement, but not
    sufficient alone** — still $\sim2.5\times$ short of $\Lambda$CDM, with the worst
    residual pulls at $z\approx0.5$ and $z\approx0.93$ ($\sim2.7$–$2.9\sigma$) suggesting
    a generic power-law crossover is only an approximation to T13's actual $r_s/R\sim1$
    freeze-out shape.
  - **A flagged tension, not yet resolved:** the AP-preferred residual locked fraction
    ($f_0\approx0.02$) is far smaller than the $\Omega_\text{PBH}\sim0.25$ figure T13/T16
    use for the dark-matter-replacement role. Either these are different normalizations
    needing a careful mapping (fraction of the *counting sea* vs. fraction of *matter
    density* are not obviously the same number), or the AP shape wants a much smaller
    effect than the dark-matter role needs.

**Conclusion of this test.** The Machian mass-count route, as a simple substitution
within the existing horizon-ODE structure, is foreclosed by the same family-level
theorem that already excludes the count reading. A structurally different, multi-channel
mechanism is required, and the connecton-sink idea (using content already in T13, no new
physics) is the first candidate in this entire investigation that moves in the right
direction using existing model content rather than an ad hoc fit — but it is not, on its
own and in the simple form tested here, sufficient to close the gap to $\Lambda$CDM.
This is exactly the open, unresolved state in which cdot-4 ends on its cosmological
sector.

---

## Part II — The Local-Gravity Program: Superseded Machinery and Live Tensions

*Separable from Part I (per §1.1's own escape-route analysis: the connecton
diffusion/river/RAR-closure program requires a sea and a horizon scale, not the specific
$z(D)$ mapping). This survives cdot-4 and should carry into cdot-5. But its road to the
present T14/T22 formulation passed through machinery, branches, and claims that were
superseded, dropped, or overclaimed — recorded here so cdot-5 does not silently lose
them or re-walk the same dead ends.*

### 2.1 The Withdrawn Two-Regime Dictionary and Its Two Excluded Branches

Before the river/flow derivation, local gravity was modeled via a **matter-response
dictionary**: $\epsilon_0,\mu_0\propto K$; $m\propto K^{3/2}$ (PV-style local mass
dressing); $E,\nu_\text{atomic}\propto K^{-1/2}$; lengths $a_B\propto K^{+1}$, tied to a
local vacuum index $K$ via redshift/bending pincer constraints. This produced the
now-withdrawn premise: *matter responds to spatial/gravitational vacuum-index variation
with PV exponents ($m\propto K_\text{grav}^{3/2}$...), and to cosmological temporal
variation with invariant mass* — a **seam** between two regimes, motivated relationally
(local $K_\text{grav}$ as redistribution at fixed global count vs. cosmological
$K_\text{cosmo}$ as the count level itself) but never derived, only fit to two data
points.

**Two specific branches were tried and decisively excluded — worth keeping as a record
of what doesn't work, not just that something was withdrawn:**
- Keeping the invariant-mass dictionary locally ($\sigma=0$) predicts gravitational
  redshift **4$\times$ GR** — excluded by GPS and the Galileo GREAT eccentric-orbit test
  ($(0.19\pm2.48)\times10^{-5}$ fractional accuracy on GR) at $\sim10^4\sigma$.
- Renormalizing the $K$-field instead ($A=1/2,\sigma=0$) predicts light bending
  **$\tfrac14\times$ GR** ($0.44''$ instead of $1.75''$) — excluded by VLBI
  ($\gamma-1\sim10^{-4}$) and Cassini ($\gamma-1=(2.1\pm2.3)\times10^{-5}$).

The eventual $(A,\sigma)=(2,3/2)$ solution survives only as the *other* branch of the
later flow-derivation's uniqueness theorem ($\xi=0$) — the dictionary itself, as an
independent premise requiring a physical seam rationale, is dead. An intermediate
reframing (splitting the local sector's redshift power as $P=1/2$, "both branches") was
also tried and separately retired as no longer needed once the flow derivation
superseded the whole approach.

### 2.2 The GEM+PV-Dictionary Hybrid Architecture

A transitional model held the force sector (GEM: mass currents, $\mathbf B_c$,
Lense–Thirring, quadrupole radiation) and the clock/light sector (the PV dictionary
above) as **two separate mechanisms under one $\delta n_c$ field** — a four-row
consistency requirement (force via $g_{0i}$, light bending via $g_{00}$, clock rate via
$g_{00}$, spatial curvature via $g_{ij}$) demanding all four be simultaneously
GR-locked. This entire hybrid stage is **superseded** by the river/flow derivation
(single potential, single coupling, no seam) but is not recorded anywhere in T22 as
having existed — worth preserving so a future session doesn't propose reconstructing it
as if new.

**A dropped alternate resolution path for the ephemeris crisis, not carried into T22:**
"Environmental saturation" (an EFE-analog escape) — since the Sun already sits in a
trans-critical Galactic field ($2.15\times10^{-10}$ m/s² $=1.9\,g_\dagger$), if the RAR
closure's anomalous component depends on the *total local flux environment* rather than
purely the isolated point-mass field, the Sun's own increment could be purely Newtonian
without needing the entrainment-suppression law to do all the work. Flagged in the
source as likely needing to operate *together with* the entrainment path, not instead
of it — this combination was never followed up.

### 2.3 The Superfluid/Madelung Derivation: Superseded, but One Tension Survives Underneath

The river result $w=\sqrt{2GM/r}$ was originally derived through a full quantum-
hydrodynamic treatment (condensate order parameter, Madelung velocity, Bernoulli
equation with quantum potential) — premises C1 (condensate), C2 (universal coupling
$\delta\mu=m_c\phi$), C3 (stationarity + cosmological zero-energy boundary). T22 now
derives the same result classically and states this machinery "is not needed" — true for
the *result*, but the machinery produced one genuinely new technical finding not
preserved anywhere else: the **harmonic miracle** — the density profile the diffusion
mechanism itself generates, $\delta n\propto1/r$, is exactly harmonic
($\nabla^2\sqrt n\propto\nabla^2(1/r)=0$), so the quantum potential $Q\equiv0$
*identically* for precisely this profile, not approximately. T22's classical argument
(no quantum pressure term exists in the first place, for a pressureless population) is a
*different* argument reaching the same place — the harmonic-miracle result itself is
real and worth keeping on record independent of which route is preferred.

**A live tension the switch to a classical framing sidesteps rather than resolves.**
Quantized circulation in the superfluid picture, $\kappa=h/m_c\approx5\times10^{35}$
m²/s, sits **29 orders of magnitude above** the Sun's actual frame-dragging circulation
($\Gamma\sim10^6$ m²/s). Three candidate resolutions were proposed: (i) rotation carried
by the *normal* (diffusive) component via two-fluid angular-momentum entrainment
(rotating-helium analogy); (ii) the relevant circulation mass isn't $m_c$; (iii) frame
dragging is genuinely suppressed below the vortex threshold — **which would conflict
with the LAGEOS 2% measurement and falsify the pure-condensate reading.** T22 notes the
29-order mismatch but, by adopting the classical (non-superfluid) framing, does not
actually resolve which of (i)–(iii) is true — it sidesteps the question rather than
answering it. Since T22's own open items (§5) still list the two-population
ballistic/diffusive split as undetermined, this specific falsification risk (iii) is not
retired and should not be treated as such.

### 2.4 Failed Naive Attempts at $w(r)$ — Preserved So They Aren't Re-Walked

Before the successful Bernoulli/harmonic-miracle route, two direct estimates for the
frame-flow profile were tried and failed outright:
- **Le Sage shadow-drift anisotropy**: gives $w\sim|\Phi|/c$, evaluated numerically at
  **0.21 m/s at Earth's surface vs. the required 11.2 km/s** — short by $5\times10^4$,
  and wrong order in $\Phi$ for the redshift besides.
- **Material continuity for a steady sink**: gives $w\propto r^{-2}$ — the wrong radial
  profile entirely (needed $w\propto r^{-1/2}$).

Neither is mentioned in T22's open-items list, which states the derivation as
outstanding without this history. A related, still-unexecuted premise-language proposal
from the same thread: sharpening premise 2 to *"$c$ is set by the global count within
the horizon (relational anchor); local density perturbations move the sea's rest frame
and carry momentum flux, but do not change $c$"*, and premise 4 to *"stationary, not
static."* T22 acknowledges these edits are deferred but does not quote the proposed
wording; recorded here for whenever that edit is actually made.

### 2.5 Connecton Ontology: One Overclaim Walked Back

The claim that T14's holographic saturation count ($n_\text{holo}=3/(4L_p^2R_0)$)
exactly, independently matches the Freedman–Headrick "bit thread" density was originally
presented as "the exact identity that clinches it" — i.e. independent confirmation that
the connecton is a holographic degree of freedom. This was a **tautology**: both use the
same standard one-bit-per-$4L_p^2$ holographic count, so of course they agree. The claim
was walked back on the same day it was made, downgraded to "consistent with standard
holographic counting," and is recorded here as a documented instance of the project's
own rhetoric outrunning its result — worth remembering as a pattern to watch for, not
just this one instance. A "Convergences With Established Programs" section (links to
Jacobson 1995, Verlinde entropic gravity, holographic dark energy, ER=EPR) was dropped
entirely on merge into T12 and was never evaluated for whether those convergences are
substantive or superficial.

---

## Part III — The Deferred Test Battery

*An entire proposed observational program (`Update_2026-07-02_Observational_Test_Battery.md`)
was never merged into any topic document — confirmed by direct search: no T-document
contains "redshift drift," "Alcock," "Sandage-Loeb," "Bullet Cluster," "1E 0657,"
"quasar dipole," or "FRB." Only one item (a T15 sign correction) made it in. The T22
slot this document proposed creating was later taken by an unrelated topic
(gravitational lensing), and the rest of the battery was simply never revisited. Listed
here so cdot-5 starts with the full list, not a fragment.*

### 3.1 Already Run, Since This Was Written — and Failed

**The effective radial expansion rate / Alcock–Paczyński test** proposed here
($H_\text{eff}(z)=H_0^\text{obs}(1+z)^{7/6}$, predicted AP deviations of 2–9% vs. DESI's
1–2% precision, called "the sharpest currently-available geometric test") is exactly the
test that was subsequently run for real (§1.1, §1.3) and failed decisively
($\chi^2=93.9$/6 points, zero parameters). This is worth flagging explicitly: a test this
document predicted would be sharp and diagnostic *was* sharp and diagnostic — just not in
the model's favor.

### 3.2 Not Yet Run

- **Redshift drift (Sandage–Loeb).** $\dot z=H_0^\text{obs}(1+z)[1-(1+z)^{1/6}]$ predicts
  $\dot z<0$ at *all* $z$, no zero crossing — vs. $\Lambda$CDM's sign flip near
  $z\approx2.5$. Exact sign flip in $\dot v$ at $z=1$ ($-0.26$ vs $+0.26$ cm/s/yr). Called
  "arguably the single best future test of the model"; instruments: ELT-ANDES
  (2030s–2040s), CHIME/HIRAX 21cm ($z\lesssim2$).
- **CMB temperature–redshift relation.** The model predicts $T(z)=T_0(1+z)$ exactly
  ($\beta=0$) via an absorber-transition-frequency argument, consistent with the
  observational bound $\beta=0.022\pm0.018$ — a pass, conditional on an unverified
  sub-check (the Compton-scattering/SZ channel giving the same law has not been
  confirmed).
- **Bullet Cluster (1E 0657-56) lensing–baryon offset.** Requires the PBH component to
  dominate cluster potentials — creating a forced division of labor with the RAR
  closure's baryon-only fit (T15) that is **not reconciled anywhere** in T5/T6/T15/T16.
  This is the same structural tension already flagged in project memory as the
  PBH-halo-vs-baryon-only-RAR problem, now with a specific, checkable observational
  target attached.
- **BBN D/H priority.** Using T21's weak-rate ($\Gamma\propto c^4$) and deuteron-binding
  ($\propto c^2$) scalings as inputs to an actual light-element-yield calculation — T13
  still lacks this; the calculation remains undone.
- **Growth of structure** ($f\sigma_8$, RSD, cluster counts) — flagged as "entirely
  unworked," possibly fatal, possibly a discovery channel. No T-document addresses it at
  all.
- **Cosmic chronometers vs. BAO — a distinctive, falsifiable split.** The model predicts
  chronometer-$H$ and BAO-$H$ must disagree by exactly $(1+z)^{1/2}$ (they agree in
  $\Lambda$CDM). This directly resolves T3's still-open "which $H(z)$" ambiguity, but the
  resolution was never written into T3, which still lists the ambiguity as unconfirmed.
- **$\mu=m_p/m_e$ invariance** — passes existing ammonia/methanol and optical-clock
  bounds automatically; not recorded anywhere as a passed test.
- **Cosmic dipole / preferred-frame test.** Secrest et al.'s reported $\sim4$–$5\sigma$
  quasar-dipole excess over kinematic expectation — flagged as "a rare place the model
  could outperform $\Lambda$CDM." Not followed up.
- **The 21 Gyr age's two-sided test.** Any single object robustly dated $>14.5$ Gyr would
  falsify $\Lambda$CDM while confirming this model — "the only probe where the model
  predicts a positive anomaly rather than defending against one." Not connected to T1 or
  T20's existing white-dwarf age work.
- **FRB dispersion measures** (Macquart relation) — not evaluated.
- **Explicitly non-discriminating tests**, flagged in the source specifically so future
  sessions don't waste time re-deriving them: SN light-curve time dilation, Tolman
  surface-brightness/duality (passed by construction, since Etherington holds exactly —
  modulo §1.5/§1.6's finding that Etherington may not actually apply here, which
  reopens this closure and should be revisited), laboratory $\dot c$-drift searches. This
  closing-off list itself was never written into Core or elsewhere.

---

## Part IV — Conclusion: What Cannot Stand, What Survives

**What cannot stand.** Core Principles premises 1 (static geometry), 2 (horizon
counting, $c\propto N\propto R^n$), and 4 (photon frequency conserved in flight),
**taken together as currently formulated**, are excluded as the mechanism for the
cosmological redshift–distance relation. This is not a parameter problem: the
family-level result (§1.1, §1.6) shows no exponent, no counting-law variant, and no
simple single-channel Machian reformulation (count or mass, coordinate or proper time)
escapes the exclusion, because all of them share the same structural defect — a single
function $c(t)$ is forced to fix both the redshift clock and the distance ruler
simultaneously (the $D_H=dD_p/dz$ lock, §1.3), and DESI's Alcock–Paczyński ratio shows
directly that no one-function model can reproduce the data's shape. The CMB first-peak
correction (§1.5) fixes a *separate*, real error (an inapplicable borrowed Etherington
relation) but cannot repair this — it corrects the projection, not the history. The one
mechanism that moved in the right direction using only content already in the model
(PBH mass fixed at genesis, shrinking as a fraction of an ever-growing raw sea, §1.6)
gives real improvement but is not sufficient alone, and a genuinely two-channel
structure is what the data seem to want.

**What survives.** The connecton local-gravity program (T14, T22) — diffusion-sourced
Newtonian gravity, the river/flow derivation of $w=\sqrt{2GM/r}$, the RAR closure, the
MOND-scale identification $g_\dagger=c^2/R_0$ — is logically separable from the
cosmological counting law (it needs a sea and a horizon scale, not the specific $z(D)$
mapping) and is untouched by this exclusion. It carries its own open debts (§2: the
circulation-quantization tension, the un-derived entrainment law, the amplitude
normalization) but is not falsified by anything in this document.

**For cdot-5.** The cosmological sector needs a structurally different mechanism for
$c(t)$'s history — most likely a genuine multi-channel one, not a relabeling of the
existing single-channel counting law — that independently produces a redshift clock and
a distance ruler capable of tracking DESI's Alcock–Paczyński shape, while remaining
consistent with the local-gravity program's horizon scale $g_\dagger$, T1's age
constraint, and T4's Pantheon+ residual. The connecton-sink direction (§1.6) is the most
promising lead in hand and the recommended starting point, not a finished answer. The
deferred test battery (Part III) should be treated as the standing observational
to-do list for whatever replaces the counting law, evaluated fresh rather than assumed
to still apply.
