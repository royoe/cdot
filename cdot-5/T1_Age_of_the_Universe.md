# T1 — The Age of the Universe

## Observational Background

The age of the universe is one of the most directly constrained quantities in cosmology.
The oldest stellar populations set a firm lower bound: globular clusters in the Milky Way
have ages measured at $12$–$13$ Gyr, with several determinations clustering near
$13$ Gyr. The CMB-based $\Lambda$CDM fit gives a total age of $\approx13.8$ Gyr,
consistent with this bound and leaving a comfortable margin of $\sim1$ Gyr for structure
formation before the oldest stars.

The key observational constraint is therefore a lower bound: **the universe must be at
least $\sim13$ Gyr old** in whatever time measure is physically meaningful for atomic
clocks. There is no strong independent upper bound from stellar ages alone.

---

## Two Time Frames in the Model

The model has two distinct clocks, and conflating them leads to large errors.

**Coordinate (map) time $t$** is the GPS-style time of the static map: a shared "now"
in which the horizon grows as $dR/dt=c(t)$ (Core Principles §3). Under the connectivity
counting law, the coordinate age is **infinite in the past** — $c\to0$ only as
$t\to-\infty$ — but, unlike the earlier occupancy-counting law, the coordinate future is
**finite**: $c\to\infty$ at a finite future coordinate time $t_*$. Whether that matters
physically is exactly the question the rest of this document, and Core Principles §3,
answers: no, once the right clock is used.

**Proper (atomic) time $\tau$** is what a physical clock governed by atomic transition
frequencies actually measures. Because atomic frequencies scale as $\nu\propto c^2$
(Core Principles §5a — this scaling follows from invariant mass and $e,h$ and the
EM-forced $\epsilon_0\propto c^{-1}$, none of which depend on how $c$'s cosmological
history is generated), clocks ran slower in the past (lower $c$) and accumulated fewer
ticks per unit of coordinate time. The rate of proper time relative to coordinate time
is:
$$\frac{d\tau}{dt}=\left(\frac{c(t)}{c_0}\right)^2,$$
where $c_0\equiv c(t_\text{now})$ is the present speed of light. This relation is
unchanged from every earlier iteration of the model — it is a statement about atomic
physics, not about the cosmological counting law.

---

## Derivation of the Proper Age

**Notation.** Define the coordinate lookback time $u\equiv t_\text{now}-t\ge0$ ($u=0$ is
now; $u\to\infty$ is the infinite coordinate past). The horizon-law solution for
connectivity counting (Core Principles §3), with $L$ the fixed recruitment length in
$c(R)=c_0e^{(R-R_\text{now})/L}$, is
$$c(u)=\frac{c_0}{1+c_0u/L}.$$

The total proper age since $c=0$ (the integral over all coordinate time) is:
$$\tau_\text{total}=\int_0^\infty\frac{d\tau}{dt}\,du
=\int_0^\infty\left(\frac{c(u)}{c_0}\right)^2du
=\int_0^\infty\frac{du}{(1+c_0u/L)^2}.$$
Substituting $w=1+c_0u/L$ ($dw=(c_0/L)\,du$, limits $w:1\to\infty$):
$$\tau_\text{total}=\frac{L}{c_0}\int_1^\infty w^{-2}\,dw=\frac{L}{c_0}.$$

**Expressing through the observable Hubble constant** (Core Principles §4a): the
horizon rate is $H_0^\text{hor}\equiv(\dot c/c)_0=c_0/L$, and the relation between the
two Hubble constants, $H_0^\text{obs}=P\,H_0^\text{hor}$ ($P=s+2$, the mass-scaling
exponent), holds exactly as it always has — it comes from the redshift law (T2), not
from the counting law, and survives the counting-law change unchanged. For invariant
mass ($s=0$, $P=2$): $L=2c_0/H_0^\text{obs}$, so
$$\boxed{\,\tau_\text{total}=\frac{L}{c_0}=\frac{2}{H_0^\text{obs}}\approx27.9\ \text{Gyr}\,}
\qquad(H_0^\text{obs}=70\ \text{km/s/Mpc},\ H_0^{-1}\approx13.97\ \text{Gyr}).$$

### General mass scaling

For a general mass scaling $m\propto c^s$ (clock frequency $\nu\propto c^P$, $P=s+2$),
the same substitution gives
$$\tau_\text{total}=\frac{L}{c_0}\int_1^\infty w^{-P}\,dw=\frac{L}{c_0(P-1)}
=\frac{P}{(P-1)\,H_0^\text{obs}},$$
using $L=Pc_0/H_0^\text{obs}$ (the general form of the boundary condition above). This
converges only for $P>1$ (equivalently $s>-1$). For $P\le1$ the integral diverges and
the proper age is infinite.

**Invariant mass** ($s=0$, $P=2$): $\tau=2/(1\cdot H_0^\text{obs})=2/H_0^\text{obs}\approx27.9$ Gyr.

**PV mass** ($s=-3/2$, $P=1/2<1$): the integral $\int_1^\infty w^{-1/2}\,dw$ diverges
(the integrand decays only as $w^{-1/2}$, not integrable). $\tau_\text{total}=\infty$
for PV mass — the same conclusion as under the old occupancy-counting law, though that
law's convergence threshold was $P>2/3$ rather than $P>1$; PV mass fails both.

**Old Machian mass** ($s=1$, $P=3$): $\tau=3/(2H_0^\text{obs})\approx21$ Gyr (this branch
was discarded for other reasons unrelated to the age — see T4, T8) — numerically the
same expression as the *invariant-mass* result under the old occupancy-counting law,
a coincidence of these two particular numbers rather than any structural connection
between the two branches.

---

## Lookback Time at Redshift $z$

The proper lookback time to a source at redshift $z$ follows the same integral with
upper limit $u(z)$. Using $1+c_0u(z)/L=(1+z)^{1/2}$ (from the redshift law, T2, combined
with the horizon-law solution above):
$$\tau(z)=\frac{L}{c_0}\left[1-(1+z)^{-1/2}\right]=\tau_\infty\left[1-(1+z)^{-1/2}\right].$$
(General $P$: $\tau(z)=\tau_\infty\left[1-(1+z)^{-(P-1)/P}\right]$.) Verified by direct
numerical integration of the exact $c(u)$ history to better than four significant
figures.

Representative values for $H_0^\text{obs}=70$ km/s/Mpc ($\tau_\infty\approx27.94$ Gyr):

| $z$ | $\tau(z)$ (Gyr) | fraction of $\tau_\infty$ | $\Lambda$CDM $\tau$ (Gyr) |
|---:|---:|---:|---:|
| 0.1 | 1.30 | 4.7% | 1.30 |
| 0.5 | 5.13 | 18.4% | 5.04 |
| 1 | 8.18 | 29.3% | 7.72 |
| 2 | 11.81 | 42.3% | 10.24 |
| 5 | 16.53 | 59.2% | 12.31 |
| 10 | 19.51 | 69.8% | 13.00 |
| $\infty$ | 27.94 | 100% | 13.80 |

At $z=0.1$ the model's lookback time matches $\Lambda$CDM to better than $0.1\%$, but
the two diverge earlier than a naive "matches at low $z$" reading would suggest: already
$\sim6\%$ high by $z=1$, $\sim15\%$ high by $z=2$, growing to $\sim2\times$ $\Lambda$CDM's
total age in the infinite-redshift limit. The divergence is a direct, mechanical
consequence of the connectivity law's $\ln(1+z)$ distance shape (Core Principles §4)
replacing the older, shallower root-law shape — it is not a new tension, just a
different quantitative profile of the same qualitative feature (the model is
systematically older, with the gap widening at higher $z$) that the occupancy-counting
model also had.

---

## Fit with the Model

The model predicts a proper age of $\approx27.9$ Gyr for $H_0^\text{obs}=70$ km/s/Mpc.
This is **above** the age of the oldest globular clusters ($\sim12$–$13$ Gyr), so the
stellar-age lower bound is satisfied with a comfortable margin — larger than the
occupancy-counting model's $21$ Gyr margin.

The model age is also **$\sim14$ Gyr older than $\Lambda$CDM** (roughly double). This is
not constrained from below by stellar ages, but raises the same question cdot-4 asked,
now with a larger gap to account for:

1. **High-$z$ structure formation.** At $z=10$, the lookback time in this model is
   $\sim19.5$ Gyr — considerably more than $\Lambda$CDM's $\sim13.0$ Gyr, and more than
   the occupancy-counting model's own $\sim16.7$ Gyr. Galaxies and quasars observed at
   $z\sim6$–$10$ formed when the universe was already many Gyr old by the model's clock,
   giving more time for early structure to form (easing some $\Lambda$CDM tensions with
   JWST observations, at least in principle) — but the dynamics of structure formation
   in a variable-$c$ background remain uncomputed in either counting law.
2. **BAO and $H(z)$ measurements.** Unlike the occupancy-counting model, this model's
   lookback times no longer track $\Lambda$CDM's closely out to $z\sim1$ — the agreement
   is now confined to $z\lesssim0.1$ before drifting noticeably. BAO-derived $H(z)$
   measurements at $z\gtrsim0.5$ would distinguish the two models on timing grounds more
   readily than the earlier version of this model would have predicted.
3. **The $H_0$ dependence.** The age still scales as $(H_0^\text{obs})^{-1}$ (unchanged
   functional form). With the local distance-ladder value $H_0=73$ km/s/Mpc:
   $\tau\approx2/13.4\cdot13.97\approx26.8$ Gyr — still well above the stellar lower
   bound.

The larger age is thus **still not in tension with stellar ages** and does not itself
require a resolution. The open question, sharpened relative to cdot-4, is whether a
$\sim28$ Gyr universe remains consistent with every other observational input, given
that the gap to $\Lambda$CDM's $13.8$ Gyr has grown rather than shrunk.

---

## Coordinate vs. Proper Age: A Beginning, but No End

The model's infinite coordinate past does not mean the universe is infinitely old in
any physical sense: atomic clocks barely ticked during epochs of very low $c$, and the
$27.9$ Gyr proper age derived above is finite, computable, and represents the total
accumulated clock time available for physical processes — this much is unchanged from
every earlier version of the model.

**What is new under connectivity counting is a finite coordinate future**,
$t_*=t_\text{now}+L/c_0$, at which the horizon law formally gives $c\to\infty$. Taken
literally in coordinate time, this reads as the map itself ending at a finite time —
a genuinely new feature absent from the occupancy-counting model, which had no boundary
in either time direction beyond the asymptotic past. But coordinate time is not what
any clock measures; proper time is, and proper time is exactly a clock-cycle count
($d\tau=(c/c_0)^2dt$, a clock ticking at rate $\nu\propto c^2$). Counting cycles forward
from today: let $v\equiv t_*-t$ (remaining coordinate time, so $c=L/v$ and $v_0\equiv
L/c_0$ is today's value). The proper time elapsed reaching a future $v$ is
$$\Delta\tau(v)=\int_v^{v_0}\left(\frac{c}{c_0}\right)^2dv'
=\left(\frac{L}{c_0}\right)^2\left(\frac1v-\frac1{v_0}\right)
\ \xrightarrow[v\to0^+]{}\ \infty.$$
**A clock never reaches $t_*$ — it ticks infinitely many times first.** This is the
exact mirror of the past-side result above: the same integral, $\int(c/c_0)^2dt\sim\int
dv'/v'^2$, converges toward $v'\to\infty$ (the past tail, giving the finite $27.9$ Gyr
age) and diverges toward $v'\to0$ (the future tail, giving an infinite remaining proper
time) — a property of the power in the integrand, not a coincidence or an approximation
(verified in closed form and by direct numerical integration).

So: in coordinate time, this model has an infinite past and a finite future — the
opposite of how it first appears. In the only physically meaningful time (what a clock
actually counts), it is the reverse: a **finite proper past** (a genuine beginning,
$27.9$ Gyr ago) and an **infinite proper future** (no end is ever reached). This matches
the "no Big Bang, no Big Crunch" character the model has always claimed for its proper
time, and confirms that character survives the counting-law change rather than being
threatened by the new coordinate-time singularity.

The variant of the old occupancy-counting fork with a finite coordinate-time *origin*
(rather than the finite coordinate *future* found here) is no longer part of this
model — that whole exponent fork (volume/surface/finite-origin counting laws) is
superseded by the connectivity counting law (Core Principles §1).

---

## Open Questions

- **Is a $\sim28$ Gyr universe still consistent with every other observational input?**
  An upper-bound check independent of $\Lambda$CDM remains open, and is now a somewhat
  sharper question than before, given the age grew further from $\Lambda$CDM's $13.8$ Gyr
  rather than closer to it. White dwarf cooling curves and metal-poor star ages remain
  lower-bound-only probes and do not resolve this by themselves.
- **Is there a self-consistent value of $H_0^\text{obs}$ and $P=s+2$ that fits both the
  supernova Hubble diagram and the lookback-time structure simultaneously?** This is the
  natural joint constraint from the full redshift–distance–time relation, and is
  compounded here by the deceleration parameter's marginal $q_0=0$ result (Core
  Principles §4a) — both need checking together against the data, not yet done.
- **T20's white-dwarf-population argument** used the earlier $21$ Gyr figure as an input
  to its own age-ceiling consistency check and needs re-running against $27.9$ Gyr — not
  yet done.
- What is the proper age under a network that is *not* purely exponential above
  $z\sim1.3$ (the high-$z$/QSO-Ly$\alpha$ deferral flagged in the counting-law update
  itself)? If $L$ runs or a second component enters at high $z$, the age integral above
  would need revisiting for its high-$z$ contribution, which is currently the dominant
  share of the total.
- **The "old-object" two-sided test (from cdot-4's deferred test battery, T23 Part
  III), updated.** Any single object robustly dated older than $\Lambda$CDM's $13.8$
  Gyr total age would falsify $\Lambda$CDM while remaining consistent with this model —
  the only probe in the program where the model predicts a positive anomaly rather
  than defending against one. cdot-4 quoted this against its own $21$ Gyr ceiling;
  cdot-5's ceiling is **$27.9$ Gyr**, an even larger margin. Not yet connected to T20's
  actual white-dwarf age-ceiling work (a different, unrelated use of "age" in this
  model — T20 bounds how *young* a massive white dwarf must be; this item is about
  whether any object is *older* than $\Lambda$CDM allows). No candidate object
  identified or checked.
