# T23 — Autocatalytic Counting

*This is premise 2's dedicated home for cdot-5, gathering what was previously scattered
across four working sessions (`autocatalytic_counting/`, `cz_inversion/`,
`percolation_break/`) into one document, in the same style as T1–T14. Core Principles
states the headline only and points here for the derivation. Status: constructive, with
one gating derivation still open (§6) and one caveat the author raised directly and
this document has not yet addressed (§7): the current fit uses only DESI BAO; the CMB
acoustic-peak cross-check that already broke the old occupancy law (cdot-4 T23 §1.4)
has not been re-run against this replacement.*

---

## 0. Where This Starts: the Occupancy Law Is Excluded

cdot-4's premise 2 — $c$ set by the occupancy of a horizon growing into a uniform
particle sea, $c\propto N\propto R^n$ for any exponent $n$ — was excluded by the DESI
DR2 BAO Alcock–Paczyński test at $\chi^2\approx94$/6 (volume law) with **no rescuing
exponent**: a family-level scan over every $n$ still gave $\chi^2\approx35$ at best,
requiring $nP\approx10.5$ against the model's own $n=3,P=2$. Full derivation and
numbers: cdot-4 `T23_The_Failed_Tests.md` §1.1–§1.3. This document picks up from that
exclusion and works out the replacement.

---

## 1. The Static Map Survives — the Power Law Was Rigid, Not the Framework

The first thing worth correcting, because it changes what the rest of this document is
allowed to assume: an early framing of the AP failure as "the $D_H=dD_p/dz$ lock"
suggested the *static map itself* — any cosmology with $D_M=D_p$, $D_L=(1+z)D_p$ — was
constrained past usefulness. **This is not so.** The identity $D_H=dD_M/dz$ is
universal: it holds in $\Lambda$CDM and any FRW model too, since $dD_M/dz=c/H=D_H$ by
construction. It cannot distinguish the static map from anything, and does not falsify
it.

What actually fits DESI: take $D_p(z)$ directly equal to the measured $D_M(z)$. This
reproduces the BAO distances by construction, and $D_L=(1+z)D_p$ (Etherington) matches
the SN Hubble-diagram shape to $\sim1\%$ with one overall scale. **The static map is not
falsified by the data — only the occupancy-counting *derivation* of $D_p(z)$ was.**

**Inverting DESI for the required counting index.** Holding the squared redshift law
fixed ($c(z)/c_0=(1+z)^{-1/2}$ — this is a separate premise, T2, and stays fixed
throughout this entire document) and reading off what power-law index $n(z)\equiv
d\ln c/d\ln R$ the data would need at each $z$:

| $z$ | $c/c_0=(1+z)^{-1/2}$ | required $n(z)$ |
|---:|---:|---:|
| 0.510 | 0.814 | 0.72 |
| 0.706 | 0.766 | 0.67 |
| 0.934 | 0.719 | 0.58 |
| 1.321 | 0.656 | 0.42 |
| 1.484 | 0.634 | 0.38 |
| 2.330 | 0.548 | 0.43 |

Two robust conclusions, independent of the one free normalization ($R_\text{now}/r_d$):
$n=3$ (volume) is excluded by a wide margin, and $n$ is **not constant** — it declines
from $z\sim0.5$ toward a minimum near $z\sim1.5$ and rises again by $z\sim2.3$, a
shallow dip. Even area-counting ($n=2$) over-counts for reasonable normalizations — the
data want a *sub-area* law. This running, and the dip's location, are what the rest of
this document explains.

---

## 2. Fork A: A Conservation-Preserving Symmetry Breaker (Tested, Failed)

Before arriving at the mechanism below, one candidate fix was tried and needs recording
as closed, not left as an open temptation for a future session to re-walk.

**The idea.** If connectons are pilot-wave-like two-way relations, a connection cannot
be made to matter *inside* a black hole (the return leg cannot propagate out) — so
black-hole-*confined* mass should drop out of whatever count sets $c$, while the
connectons themselves remain fully conserved (T14's "conserved, never destroyed"
premise untouched). This gives $c\propto M_\text{count}(R)=M_u(R)[1-f_\text{BH}(z)]$,
with $f_\text{BH}(z)$ an observable, not a new fluid.

**The test.** Inverting the AP residual for the required swing: closing the S-shaped
$D_H=dD_p/dz$ mismatch needs $|\Delta f_\text{BH}|\sim3\times10^{-2}$ of the counted
mass, concentrated near $z\sim1$, with a sign flip by $z\sim2.3$. Checked against the
real cosmic black-hole budget:

| Population | $f_\text{BH}$ today | $\Delta f_\text{BH}$ over $0<z<2.3$ | shortfall |
|---|---:|---:|---:|
| SMBH/AGN (Soltán argument) | $\sim10^{-5}$ | $\sim10^{-5}$ | $\sim2600\times$ |
| + all stellar-remnant BHs (maximal) | $\sim$few$\times10^{-4}$ | $\sim3\times10^{-4}$ | $\sim90\times$ |
| PBHs ($\Omega_\text{PBH}\sim0.25$) | $\sim0.8$ | $\approx0$ (genesis-formed) | no clock at all |

**Why it fails structurally, not just numerically:** the population large enough to
matter (PBHs) is genesis-formed and essentially time-constant over the relevant
redshift range — a constant $f_\text{BH}$ only rescales the normalization $k$, it
cannot bend the AP *shape*. The population that actually varies over $0<z<2.3$
(accretion-grown SMBHs) is a $\sim10^{-5}$ sliver of the counted mass. The only escape —
a dominant, late-forming, hidden BH population — is the dark sector renamed, which the
project's own no-dark-sector stance rules out on the same grounds as everywhere else.

**Genuine connecton sinks** (dropping conservation outright, rather than excluding
confined mass from the count) were considered and explicitly **not pursued**: they
collide with T12's photon-exclusion argument and T14's conservation premise, and with
Fork A already dead there was no clear reason to pay that cost. **Connectons are
conserved, full stop — this was tested, not merely assumed.**

---

## 3. Connectivity Counting: the Autocatalytic Law

With Fork A closed, the live path is a genuinely different counting rule, not a patch
to the occupancy one. T12 had already argued, on independent ontological grounds, that
a connecton is "a conserved unit of relation," not a particle — this section is that
reading doing quantitative work for the first time.

**The mechanism.** Read $N$ (the quantity $c$ tracks, $c\propto N$) as the local
reference point's **connectivity** — how many connectons it is transitively connected
to — rather than how many occupy the growing causal volume. A newly admitted horizon
shell contributes new *occupancy* independent of what's already connected
($dN/dR\propto R^2$, the old volume law), but it contributes new *reachable* nodes only
in proportion to the connectivity already held (a node joins the reachable set iff it
links to a node already in it):
$$\frac{dN}{dR}=\frac{N}{L}\quad\Longrightarrow\quad N\propto e^{R/L},\qquad c\propto N,$$
for a **fixed length** $L$ — fixed, not a fraction of $R$, is the entire content of the
distinction from the excluded power-law family (a horizon-tracking $L\propto R$ would
give back $N\propto R^{1/\alpha}$, a power law).

**Three assumptions this rests on, none derived from anything deeper yet:**
1. **Supercriticality** — transitive reach grows rather than saturating only if the
   network's mean branching exceeds 1; a subcritical network's reach would saturate
   and $c$ would freeze. Assumed.
2. **The endpoint-only $1/L$ recruitment rate** — reuses T12/T14's heuristic (interaction
   likelihood per unit length $\propto1/L_\text{link}$ for a connection's endpoints;
   note this microphysical $L_\text{link}$ is a *different* quantity from this
   section's cosmological $L$ — shared symbol, no relation, per T14's reconciliation).
   Itself not yet derived from re-anchoring kinetics.
3. **Mean-field independence** — frontier connections recruit independently, no
   clustering. Correlations would shift the effective exponent.

---

## 4. Fit to the Clean DESI Bins

Restricting to the four galaxy bins ($z=0.510,0.706,0.934,1.321$; QSO and Ly$\alpha$
excluded for now, see §6) and fitting one-parameter counting laws jointly to
$D_M/r_d,D_H/r_d$ (8 data points), holding the squared redshift law fixed:

| Law | form | free params | $\chi^2$ |
|---|---|---:|---:|
| **exponential (this law)** | $D_p\propto\ln(1+z)$ | 1 ($B=L/2\approx33\,r_d$) | **13.2 / 7** |
| power, volume ($n=3$) | | 1 | 98 |
| power, surface ($n=2$) | | 1 | 178 |
| power, $n=1$ | | 1 | 552 |
| power, S$'$ ($n=2/3$) | | 1 | 1104 |
| power, $n=1/2$ | | 1 | 1798 |
| — reference: $\Lambda$CDM | $\Omega_m,A$ | 2 | 10.5 / 6 |

The one-parameter exponential law ($\chi^2/\text{dof}\approx1.9$) is competitive with
two-parameter $\Lambda$CDM and decisively beats every power law tried — and the power
laws get *worse*, not better, as the exponent is lowered toward the small values §1's
local-slope inversion suggested, because the data want an index that *grows* with $R$
($n_\text{eff}(R)=d\ln c/d\ln R=R/L$), which is exactly the exponential limit of a
power law as its exponent runs to infinity. (An intermediate reading of §1's inverted
$n(z)$ as "the data want a low, constant $n\sim0.4$–0.7" is superseded by this direct
fit — that reading came from a local derivative at an assumed normalization, not from
fitting the actual data, and constant low-$n$ power laws fit *worse* than $n=3$, not
better.)

**Structural signature.** $c(R)\propto e^{R/L}$ ⟺ the network recruits over a fixed
length, not a fixed fraction of the horizon. This is a falsifiable statement about the
network's character, not merely a curve-fit: scale-free connectivity is excluded by
DESI.

---

## 5. The High-$z$ Failure, and the Percolation Transition

The pure exponential law overshoots the two excluded tracers (QSO, Ly$\alpha$,
$z>1.3$): $D_M$ slightly high, $D_H$ badly high at $z=2.33$ ($-14\sigma$ under the pure
log law on all six bins, $\chi^2\approx139$/10). This was first treated as a deferred
"decide later" item; it turned out to be the same physics as §3, one phase further.

**The percolation picture.** How connectivity grows as the horizon grows depends on the
connecton network's *phase*:
- **Subcritical (occupancy counting).** With no giant connected component, a new
  horizon shell adds $\sim n\cdot4\pi R^2\,dR$ independently reachable nodes —
  $N\propto R^3$, the volume law. This is cdot-4's premise 2, now understood as the
  network's *early* phase, not the whole story.
- **Supercritical (connectivity counting).** Once a spanning component exists, §3's
  autocatalytic rule takes over.

The transition between these is a genuine **continuum percolation transition**, and it
fixes $L$ rather than leaving it a bare free scale:
$$L=R_*,$$
the horizon radius *at* the percolation epoch $t_*$. At criticality the correlation
length is set; thereafter the giant component's connectivity grows exponentially with
each added shell **at that fixed correlation length**. This delivers a time-fixed $L$
(pure exponential for $R>R_*$), a cosmological magnitude for $L$ (no coincidence
between a microphysical length and the Hubble scale — an earlier, superseded reading of
$L$ as a microphysical re-anchoring length or Compton length was wrong by orders of
magnitude, corrected in this session), and a closed internal relation: since the
emission horizon at the break equals $R_*=L$, the present horizon is
$R_\text{now}=L+D_p(z_*)$ — **predicted**, not free.

**The gating gap.** Criticality occurs when $n_\text{node}\ell_\text{link}^3\sim
\mathcal O(1)$ ($n_\text{node}$ the connecton/foam number density, $\ell_\text{link}$
the link range). The growing horizon first satisfies this at $t_*$, fixing $R_*=L$.
Deriving $R_*$ from the foam density evolution (T14 §"Energy Scale") rather than
reading it off the DESI fit is the outstanding task — see §8.

---

## 6. Fit to All Six DESI Bins

The percolation-broken law — connectivity/log branch below $z_*$, occupancy/power
branch above, matched continuously in $D_H$ — fit to all six DESI DR2 bins (12 data:
$D_M/r_d$, $D_H/r_d$), four parameters:

| parameter | meaning | value |
|---|---|---:|
| $B=L/2$ | log-branch amplitude | $33.55\,r_d$ |
| $L$ | recruitment length $=R_*$ | $67.1\,r_d$ |
| $z_*$ | percolation break | $1.201$ |
| $q$ | subcritical $D_H\propto(1+z)^{-q}$ index | $1.37$ |
| $D_0$ | offset (absolute-scale nuisance; consistent with the model's own $D_p(0)=0$ within fit freedom) | $-0.46\,r_d$ |

**Goodness of fit: $\chi^2=6.8$/8 dof $=0.85$, all per-bin pulls $\le1.5\sigma$** — the
pure (unbroken) log law on all six bins gives $\chi^2\approx139$/10. Profiling $\chi^2$
over fixed $z_*$ (other parameters re-optimized at each value) gives a clean interior
minimum at $z_*\approx1.20$ ($\chi^2$: 9.3, 7.5, 6.8, 7.0, 7.7 at
$z_*=1.0,1.1,1.2,1.3,1.4$) — not a boundary artifact and not simply the galaxy/QSO
tracer split, though the two are not yet cleanly separated (§7).

**The break's finite-horizon consequence, re-derived independently.** Since $q=1.37>1$,
the subcritical tail is integrable and the particle horizon is **finite**:
$$D_p(z\to\infty)=D_p(z_*)+\frac{B}{q-1}=26.0+\frac{33.55}{0.37}\approx116.7\,r_d,$$
verified against direct numerical integration of the broken $D_H(z)$, not merely this
closed form. Compare $R_\text{now}=L+D_p(z_*)\approx93.1\,r_d$ and the recruitment
length $L\approx67.1\,r_d$ itself — **three distinct finite lengths**, all order-unity
multiples of each other, and which one (if any) plays the role cdot-4's clean
$R_0=6c/H_0$ played for the MOND acceleration scale and holographic saturation is now
the open question feeding into T14 and T6 (see those documents' cdot-5 reconciliation
for the numbers: the best candidate, $D_p(\infty)$, brings $g_\dagger$ to within
$1.63\times$ of the observed MOND scale, down from a naive $2.83\times$).

**Illustrative absolute scale** (standard $r_d\approx147$ Mpc, order-of-magnitude only
since this model's own $r_d$ is not computed — T16): $L\approx9900$ Mpc,
$R_\text{now}\approx13{,}700$ Mpc, $z_*=1.20$.

---

## 7. Interpretation, and the Caveat the Author Raised Directly

The transition unifies the model's two counting laws as two phases of one network:
before percolation, a gas of local clusters, $c$ counts occupancy; after, a spanning
component, $c$ counts transitive connectivity. The universe's distance law carries a
fossil of the moment its connecton network first became globally connected. This is
squarely in the model's relational spirit: "everything became connected to everything"
is exactly the epoch counting should switch character.

**Checked since — result: fails by $7.6\times$, but mostly for a different reason than
this document's own extrapolation.** This fit used **only DESI BAO data**. cdot-4's
occupancy law had failed a second, independent test — the CMB/BAO cross-probe
consistency check (cdot-4 `T23_The_Failed_Tests.md` §1.4). **T16's cdot-5 rewrite ran
the analogous check for the percolation-broken law**: extending the fitted subcritical
branch ($q\approx1.37$) to $z_\text{rec}\approx1090$ gives $\ell_1\approx1674$,
$7.6\times$ too high. A follow-up decomposition (also folded into T16) then separated
this into a distance-law contribution and a baryon-loading contribution ($R\approx680$,
T16's independently-derived self-similarity value, unrelated to this document) and
found **$R\approx680$ is the dominant lever, not the extrapolated distance law** — $R$
alone would need to shrink by $\sim63\times$ to fix the position, and it independently
fails an extrapolation-free peak-*height* test by $\sim400\times$, on grounds that have
nothing to do with the counting law here. This is good news for this document
specifically: the counting-law extrapolation past $z\gtrsim2.33$ remains a real, open
caveat (below), but it is not primarily what is wrong with the CMB test, and the "third
regime" question is correspondingly de-prioritized relative to fixing $R\approx680$
(T16's own top open item now). See T16 for the full decomposition.

---

## 8. Structural Consequences and What Still Needs Recomputing

**Unaffected by any of this document's content:** the redshift law
$1+z=(c_\text{now}/c_\text{emit})^2$ (T2) — fixed throughout §§1–6 as the one thing held
constant while the counting law was inverted, fit, and re-fit. Mass and $G$ invariance
(premises 3). The future-singularity resolution (Core Principles §3, T1): the entire
future lies at $z\le0<z_*$, inside the post-percolation branch, so the "finite
coordinate future, infinite proper future" result is untouched by the break.

**Needs recomputing, not yet done:** T1's proper age integral, and T3/T4's distance and
$H(z)$ tables, were computed in cdot-5 using the *single-phase* exponential law, before
the percolation break was identified. The age integral in particular runs over all past
history and therefore crosses $z_*$ — its current value ($\tau_\infty=2/H_0^\text{obs}
\approx27.9$ Gyr) used only the post-percolation branch and needs re-deriving with the
subcritical branch's contribution to the deep past included. This is flagged, not
performed, here; it belongs to T1/T3/T4's own next reconciliation pass.

**T14's reconciliation** (connecton gravity: the MOND acceleration scale, holographic
saturation, connecton conservation) has already been carried out against this document's
findings — see T14's cdot-5 version for the full account; summarized in §6 above.

---

## 9. Relationship to Other Documents

- **Core Principles §1/§3:** state the two-phase premise and the post-percolation
  branch's formulas; point here for the mechanism, the fit, and the open items.
- **T1, T3, T4:** currently use the single-phase law; flagged in §8 as needing
  recomputation against the two-phase law, not yet done.
- **T2:** entirely unaffected and load-bearing throughout — the fixed redshift law is
  what makes §1's inversion and every fit in this document well-posed.
- **T6, T14:** the MOND acceleration scale and holographic saturation reconciliation
  are carried out there, using this document's three candidate lengths ($L$,
  $R_\text{now}$, $D_p(\infty)$) and the finite-horizon result of §6.
- **T12:** the connectivity reading of $N$ (§3) is the ontological argument that
  document already made, now doing quantitative work; the retired count-vs-mass fork
  (T12's cdot-5 version) and Fork A (§2 above) are two independent closures of
  different, easily-confused questions — worth keeping distinct.
- **T13, T16:** T13's PBH-genesis timing argument and T16's CMB treatment both use the
  cosmic $R(t)$/$c(t)$ history and have not yet been checked against the two-phase law;
  T16 specifically is where §7's flagged CMB cross-check would need to be run.
- **cdot-4 `T23_The_Failed_Tests.md`:** the closing ledger this document's premise-2
  story continues from; not edited, referenced throughout.

---

## 10. Open Questions

**Gating (blocks treating $L$ as derived rather than fit):**
- Derive $R_*=L$ from the percolation condition $n_\text{node}\ell_\text{link}^3\sim1$
  using the foam/holographic density evolution (T14). This is the one step that would
  eliminate the model's one free scale entirely.

**High priority:**
- ~~Run the CMB acoustic-angle cross-check against the two-phase law.~~ **Done (T16,
  same day): fails by $7.6\times$, but a follow-up decomposition (also T16) found the
  miss is baryon-loading-dominated ($R\approx680$, T16's own independent quantity),
  not primarily a counting-law artifact.** This is good news for this document
  specifically — the counting law is largely exonerated on this particular number.
- **Demoted (was "the load-bearing open question for the whole program"):** is there a
  third regime between DESI's fitted range and recombination that the subcritical
  branch passes through before reaching the CMB? Still open and still worth deriving
  $q$ from first principles for its own sake, but no longer the top priority — per
  the decomposition above, even a perfectly-derived distance law would not fix the
  CMB test while $R\approx680$ stands, so T16's own "is $R\approx680$ correct?"
  question is now the higher-value target.
- Derive the subcritical index $q\approx1.37$ from branching statistics on the
  subcritical side of the percolation transition, and check it against the fitted
  value — now higher-priority still, since T16's finding is exactly as sensitive to
  this index as it is to $z_\text{rec}$.
- Decide which of $L$, $R_\text{now}$, $D_p(\infty)$ sets the MOND/holographic
  crossing scale (T6, T14) — or show none does and the coincidence with $a_0$ is
  weaker than cdot-4's occupancy law made it look.

**Also open:**
- Show supercriticality persists for all $R>R_*$ (plausible — $R>R_*$ only increases
  $n_\text{node}\ell_\text{link}^3$ — but not yet shown).
- Continuity/order of the percolation transition: the fit imposes $C^0$/$C^1$
  continuity in $D_p$; a real percolation transition may impose a specific critical
  exponent on how $N(R)$ rounds through $R_*$, making the sharp kink an idealization.
- Re-fit with the full DESI covariance and DR3 bins; confirm $z_*$ survives and
  separate it from the galaxy/QSO tracer-transition systematic it currently coincides
  with (§6's two-reasons note — not yet disentangled).
- The physical reading of the future $c$-singularity at $t_*^\text{fut}$ (Core
  Principles §3): resolved as a coordinate artifact (infinite proper time to reach it),
  but whether recruitment saturates near it, physically regulating the coordinate
  divergence, is unaddressed.
- Recompute T1/T3/T4's tables under the two-phase law (§8).
- Derive the endpoint-only $1/L_\text{link}$ recruitment rate from an explicit
  re-anchoring kinetics equation (T14's own standing debt, now load-bearing for
  cosmology as well as local gravity).
