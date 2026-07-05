# T13 — Primordial Nucleosynthesis and Baryogenesis

*This topic is substantially more speculative than T1–T12, T23 — the ideas here depend
on unresolved aspects of the model and should be read as research directions, not
established results. This is squarely true of cdot-5 as well, and in one respect more
so: BBN and genesis sit at $z\sim10^{10}$, deep in the connectivity-counting network's
**pre-percolation (subcritical/occupancy) regime** (T23), whose functional form is
currently an empirical fit valid only up to $z=2.33$ — extrapolating it $\sim10$
orders of magnitude in redshift is not something T23 itself endorses. Everything below
that depends on the cosmic $c(t)$ history at these epochs should be read with that
caveat attached, more strongly than cdot-4's own uncertainty here.*

---

## Observational Background

### Big Bang Nucleosynthesis

Big Bang Nucleosynthesis (BBN) is the process by which the light elements H, D,
$^3$He, $^4$He, and $^7$Li were forged in the hot early universe during the first few
minutes ($T\sim0.1$–$1$ MeV, $t\sim10$–$200$ s). BBN is a precise theoretical
framework with few free parameters (primarily the baryon-to-photon ratio
$\eta=n_b/n_\gamma$ and the number of neutrino species $N_\nu$), and it fits the
observed primordial abundances well:
- $^4$He mass fraction: $Y_P\approx0.247$ (very sensitive to expansion rate at
  freeze-out)
- D/H $\approx2.5\times10^{-5}$ (sensitive to baryon density)
- $^7$Li/H: the "lithium problem" — standard BBN predicts $3\times$ more than observed

The $^4$He abundance is particularly sensitive to the expansion rate $H(T)$ at
freeze-out ($T\sim1$ MeV), because $H$ determines the freeze-out temperature of the
weak $n\leftrightarrow p$ reaction: faster expansion → higher freeze-out temperature →
more neutrons → more $^4$He.

Any modification to $H(T)$ at BBN epochs must keep $Y_P$ within $\sim1\%$ of the
observed value.

### Matter-Antimatter Asymmetry

The observable universe contains essentially only matter, no significant amounts of
antimatter (evidenced by the absence of $\gamma$-ray backgrounds from bulk
matter-antimatter annihilation). The baryon asymmetry is:
$$\eta=\frac{n_b-n_{\bar b}}{n_\gamma}\approx6\times10^{-10}.$$
The Sakharov conditions (1967) for generating this asymmetry require: (1) baryon
number violation; (2) C and CP violation; (3) departure from thermal equilibrium.
Standard $\Lambda$CDM does not explain the asymmetry from first principles; it is a
major open problem in particle physics and cosmology.

---

## BBN in the Model

### What survives unaffected: the weak/nuclear scaling laws

T21's candidate inputs — invariant $G_F$ (from invariant $g_w,M_W$) giving weak decay
rate $\Gamma_\text{weak}\propto c^4$, and invariant nuclear $Q$-values giving deuteron
binding energy $\propto c^2$ — are statements about how nuclear/weak physics scales
**at a given value of $c$**, exactly like T7's QED estimate or T8's $G$-scaling. They do
not reference how $c(t)$'s cosmological history is generated, only how physics responds
to whatever $c$ is at the time. **These carry forward unchanged into cdot-5**, same as
T7 and T8 were confirmed unchanged.

### What does not survive unexamined: the $c(t)$ history at BBN epochs

cdot-4 asked what $c$ actually *was* at BBN ($z\sim10^{10}$), using the occupancy
counting law's horizon ODE. That question is now harder, not easier, to answer:
BBN sits enormously far into the past relative to the percolation break
$z_*\approx1.2$ (T23) — the entire span from BBN to $z_*$ is inside the pre-percolation
(subcritical) regime, whose $D_H\propto(1+z)^{-q}$, $q\approx1.37$, is a fit to six
DESI points at $z\le2.33$, not a derived law. Using it at $z\sim10^{10}$ is a
$\sim10$-order-of-magnitude extrapolation with no derivation backing it — T23 §7 flags
exactly this kind of extrapolation as untrustworthy for the (much nearer) CMB epoch,
$z\approx1090$; BBN is further still. **The model currently has no trustworthy $c(t)$
or $H(t)$ history at BBN epochs, under either the old or new counting law** — this was
already true in cdot-4 (T13's own "remains undone" framing), and remains true, for a
compounded reason, in cdot-5.

What can be said qualitatively, unchanged from cdot-4: the model's $H(z)$ at high $z$
differs from $\Lambda$CDM's, whatever the correct counting law turns out to be, so
whether the model predicts the correct $^4$He abundance requires an explicit
calculation that has not been attempted for any version of this model.

### Retired: the BBN discriminator for the count-vs-mass fork

cdot-4 proposed BBN as the observational discriminator between the "count" and
"classical Mach" readings of premise 2 (do relativistic species weight the counting
rule or not). **This fork is retired** (T12 — both readings are occupancy-type
constructs in the same power-law family that DESI excludes for every exponent; T23).
There is no "mass reading" of connectivity counting left to discriminate against, so
this specific discriminator is moot. Whether BBN can discriminate *within* the new
picture — e.g. between different subcritical-branch microphysics, or between candidate
early-time forms discussed below — is a different, open question, not this one.

---

## The Genesis Bootstrap (Speculative)

### The bootstrap mechanism, updated for connectivity counting

The genesis bootstrap picture survives in spirit, with its framing updated: at the
moment of genesis, the network has no connections and $c=0$. A particle-creation event
(vacuum pair, say) gives the local point something to connect to; the connection lets
$c$ become non-zero; a larger $c$ lets the horizon (and hence potential new
connections) grow faster, admitting more pairs; more pairs → more connections → larger
$c$. This is a self-sustaining bootstrap, exactly cdot-4's picture, just read in
connectivity language (reach growing) rather than occupancy language (particles
present) — the qualitative mechanism does not depend on which reading is correct, only
the earlier "count vs. mass" framing of *why* it works does, and that framing is
retired along with the fork (above).

**A new, speculative connection worth recording, not yet derived.** T23's percolation
picture requires the network to *start* subcritical (a gas of local clusters) and only
later cross into the supercritical (connectivity-counted) regime at $z_*\approx1.2$.
The genesis bootstrap above is exactly the process that populates the network in the
first place — read together, genesis bootstraps the network from nothing; the network
then spends essentially all of cosmic history (from genesis to $z_*\approx1.2$) in the
subcritical phase, only percolating relatively recently. This is a coherent narrative
connecting this document to T23, but it is a narrative, not a derivation: nothing here
computes *when* percolation should occur from the bootstrap dynamics, or whether the
bootstrap's own early behavior resembles the fitted subcritical index $q\approx1.37$
at all. Flagged as a natural target for future work, not claimed as a result.

### The connecton role

Unchanged in substance, sharpened by T12's connectivity reading: in the earliest
moments, when $c$ is small and the horizon is tiny, the connecton network is sparse —
but even a few connectons propagating at the local (tiny) $c$ can bootstrap the system.
This is now literally the pre-percolation phase's earliest stage, not a separate
picture. The physical mechanism of the bootstrap — whether the vacuum pair-creation
rate in a varying-$c$ background is fast enough to sustain the growth, and whether it
is fast enough to reach the percolation threshold by $z_*\approx1.2$ — has not been
computed, exactly as in cdot-4, now with a sharper target (reach criticality by a
specific, fitted redshift) than before.

### Primordial Black Hole Formation at Genesis

**The $r_s/R$ condition, restated.** The Schwarzschild radius of the enclosed horizon
mass is
$$r_s=\frac{2GM_\text{horizon}}{c^2}\propto G\cdot\frac{R^3}{c^2}=R^{3-2n}
\quad(\text{using }c\propto R^n\text{ and invariant }G),$$
so $r_s/R\propto R^{2-2n}$. This derivation uses only $M_\text{horizon}\propto R^3$
(ordinary uniform-density matter, unaffected by which counting law governs
*connectons*) and *whatever* power law $n$ locally describes $c(R)$ in the regime of
interest — it does not itself assume occupancy or connectivity counting, only that
*some* power law applies in that regime. Genesis is deep in the pre-percolation
regime, so occupancy-type counting (some $n$) is the right structural family to use
here — the question is which $n$.

**cdot-4's three named candidates** (volume $n=3$, surface $n=2$, S$'$ $n=2/3$) were
part of the now-retired global premise-2 fork — retired as competing descriptions of
*all* of cosmic history, but their underlying physical motivations are not thereby
individually falsified as candidates for what the pre-percolation regime's early-time
behavior specifically looks like. In particular, **S$'$'s motivation — a Compton-scale
self-consistency floor at very small $R$ — is a statement about genesis-epoch physics
specifically**, and remains a live candidate for the deep pre-percolation regime's
earliest behavior, even though it is no longer a candidate for the *entire* history the
way it was in cdot-4.

**A new, extrapolated data point, offered with its caveat attached.** Taking T23's
fitted subcritical index $q\approx1.37$ at face value and inferring the implied power
law ($D_H\propto(1+z)^{-(1+\alpha)}$, $\alpha=1/(nP)$, $P=2$):
$$n_\text{eff}=\frac{1}{2(q-1)}=\frac{1}{2\times0.37}\approx1.35,$$
notably different from all three of cdot-4's named exponents (3, 2, $2/3$). Using this
in the $r_s/R$ exponent: $2-2n_\text{eff}\approx-0.70<0$, so $r_s/R\to\infty$ as
$R\to0$ — **Reading 2's super-Schwarzschild-early-universe condition would still hold**
under this extrapolated exponent, tentatively. This is offered as a data point, not a
result: $q=1.37$ was fit at $z\le2.33$ and extrapolating it to genesis is exactly the
move T23 §7 itself warns against for the much nearer CMB epoch. Treat this as "if the
subcritical branch's fitted shape held all the way to genesis, Reading 2 would survive"
— a conditional statement, not a checked one.

**Two readings, unchanged from cdot-4:**

*Reading 1 (old):* a super-Schwarzschild early universe means all local regions are
inside their own gravitational radii → PBH formation forbidden.

*Reading 2 (preferred):* the early super-Schwarzschild universe is a black-hole-like
reservoir. As $R$ grows and $c$ rises, $r_s/R$ decreases through a **crossover at
$r_s/R\sim1$**. The average region exits the super-Schwarzschild state into a normal
universe; overdense lumps that remain super-Schwarzschild are left behind as black
holes — frozen out as relics of the crossover, not formed by collapse.

Reading 2 is favored for the same reason as in cdot-4 (it flips the same cutoff Reading
1 called a barrier into the formation mechanism), and — per the extrapolated check
above — is not obviously disfavored by the new counting law, though this has not been
checked rigorously.

**The unproven step, unchanged.** Reading 2 requires that an overdense lump, once the
average goes sub-Schwarzschild, cleanly collapses to a black hole rather than merely
remaining a denser patch. This depends on the overdense region having a locally normal
exterior — a condition the homogeneous cosmology lacks globally. Whether a single
overdense lump can have the necessary exterior while the average is sub-Schwarzschild
remains the load-bearing open question, exactly as in cdot-4.

**Consequences if Reading 2 is correct** (see T16 for the full discussion, itself not
yet reconciled with the two-phase counting law): a genesis PBH population could serve
as clustered pressureless wells for the CMB higher peaks, galactic dark matter, and
SMBH seeds — unchanged in structure from cdot-4, with the caveat that T16 has not yet
been checked against either the counting-law change or the CMB cross-probe test T23 §7
flags as still outstanding.

---

## Matter-Antimatter Asymmetry

Unchanged in substance from cdot-4, with the S$'$ connection now read as one candidate
for the pre-percolation regime's earliest behavior (above) rather than an independent
premise-2 variant. If the deep pre-percolation regime's dynamics resemble S$'$'s finite
coordinate-time origin, that origin would supply a period of departure from thermal
equilibrium (Sakharov condition 3): the system starts from $c=0$, no connections, and
bootstraps up — not a thermal equilibrium state. Whether the process violates C and CP
symmetry and baryon number (the other two Sakharov conditions) is not addressed by the
current framework, in cdot-4 or cdot-5. The matter-antimatter asymmetry remains an
open, unsolved problem.

---

## The Lithium Problem

Unchanged in status from cdot-4, now with the compounded BBN-epoch $c(t)$-history
uncertainty noted above attached: the modified expansion history at BBN epochs would
give a different $^7$Li yield, but with no trustworthy $c(t)$ history at those epochs
under either counting law, whether the model produces more or less $^7$Li than
standard BBN remains unknown, more clearly so than in cdot-4.

---

## Open Questions

- **A full BBN calculation, gated on a trustworthy $c(t)$ history at BBN epochs.**
  cdot-4's version of this question assumed the occupancy horizon ODE; that ODE's
  validity at $z\sim10^{10}$ is now itself in question (above), so this question has a
  new prerequisite: establish (or extrapolate with a stated, justified uncertainty
  budget) what the pre-percolation branch's $c(t)$ history actually is at BBN epochs,
  before attempting the abundance calculation. Use T21's $\Gamma_\text{weak}\propto c^4$
  and deuteron-binding $\propto c^2$ scalings as the weak/nuclear inputs once that
  history is in hand — those inputs themselves are unaffected and ready to use. **This
  is the same "BBN D/H" item flagged in cdot-4's deferred test battery (T23 Part III):
  a real light-element-yield calculation (D/H$\approx2.5\times10^{-5}$ observed, the
  sharpest baryon-density-sensitive abundance) using T21's scalings as inputs. Still
  undone — the prerequisite above is the reason, not a separate blocker.**
- **Retired**: the premise-2 fork discriminator (count vs. mass) — moot, the fork
  itself is retired (T12).
- **New**: does the genesis bootstrap dynamics, worked out explicitly, reach the
  percolation threshold by $z_*\approx1.2$ (T23)? This connects T13 and T23 for the
  first time and is currently a narrative, not a calculation.
- **New**: is $n_\text{eff}\approx1.35$ (this document's extrapolation of T23's fitted
  subcritical index) a reasonable description of the pre-percolation regime near
  genesis, or does the regime's true early-time behavior look more like S$'$'s
  Compton-scale floor, or something else entirely? Not decided; the extrapolation
  above should not be trusted without independent support.
- The genesis bootstrap: can the self-consistent $c\propto N$ (now: $c\propto$ reach)
  fixed point be derived from a vacuum pair-creation model? What is the resulting time
  evolution of $c$ at the earliest moments? Unchanged from cdot-4.
- Matter-antimatter asymmetry: is there a specific mechanism within the (candidate,
  not confirmed) S$'$-like bootstrap that selects matter over antimatter? Unchanged
  from cdot-4.
- The $^7$Li problem: does the model's modified BBN alleviate or worsen the
  discrepancy? Unchanged from cdot-4, gated on the same prerequisite as the main BBN
  calculation above.
