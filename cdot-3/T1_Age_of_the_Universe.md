# T1 — The Age of the Universe

## Observational Background

The age of the universe is one of the most directly constrained quantities in cosmology.
The oldest stellar populations set a firm lower bound: globular clusters in the Milky Way
have ages measured at $12$–$13$ Gyr, with several determinations clustering near
$13$ Gyr. The CMB-based ΛCDM fit gives a total age of $\approx 13.8$ Gyr, consistent
with this bound and leaving a comfortable margin of $\sim 1$ Gyr for structure
formation before the oldest stars.

The key observational constraint is therefore a lower bound: **the universe must be at
least $\sim 13$ Gyr old** in whatever time measure is physically meaningful for atomic
clocks. There is no strong independent upper bound from stellar ages alone.

---

## Two Time Frames in the Model

The model has two distinct clocks, and conflating them leads to large errors.

**Coordinate (map) time $t$** is the GPS-style time of the static map: a shared "now"
in which the horizon grows as $dR/dt = c(t)$. The coordinate age is **infinite** —
$c \to 0$ only as $t \to -\infty$, with no finite-time origin in the volume law. There
is no Big Bang in coordinate time.

**Proper (atomic) time $\tau$** is what a physical clock governed by atomic transition
frequencies actually measures. Because atomic frequencies scale as $\nu \propto c^2$
(Core Principles §5a), clocks ran slower in the past (lower $c$) and accumulated fewer
ticks per unit of coordinate time. The rate of proper time relative to coordinate time
is:
$$\frac{d\tau}{dt} = \left(\frac{c(t)}{c_0}\right)^2,$$
where $c_0 \equiv c(t_\text{now})$ is the present speed of light.

---

## Derivation of the Proper Age

**Notation.** Define the coordinate lookback time $u \equiv t_\text{now} - t \geq 0$
($u = 0$ is now; $u \to \infty$ is the infinite coordinate past). From the horizon-ODE
solution (Core Principles §3), with $k$ the proportionality constant in $c = kR^3$ and
$R_0$ the present horizon radius:
$$c(u) = \frac{c_0}{(1 + 2kR_0^2\,u)^{3/2}}.$$

The total proper age since $c = 0$ (i.e., the integral over all coordinate time) is:
$$\tau_\text{total} = \int_0^\infty \frac{d\tau}{dt}\,du
= \int_0^\infty \left(\frac{c(u)}{c_0}\right)^2 du
= \int_0^\infty \frac{du}{(1 + 2kR_0^2\,u)^3}.$$

Substituting $x = 1 + 2kR_0^2 u$ ($dx = 2kR_0^2\,du$, integration limit $x:1\to\infty$):
$$\tau_\text{total}
= \frac{1}{2kR_0^2}\int_1^\infty x^{-3}\,dx
= \frac{1}{2kR_0^2}\cdot\frac{1}{2}
= \frac{1}{4kR_0^2}.$$

**Expressing through the two Hubble constants** (Core Principles §4a):
- Horizon rate: $H_0^{\text{hor}} \equiv \dot{c}/c\big|_0 = 3kR_0^2$, so $kR_0^2 = H_0^{\text{hor}}/3$.
- Observable Hubble constant: $H_0^{\text{obs}} = P\,H_0^{\text{hor}}$, where $P = s+2$
  and $s$ is the mass scaling ($m \propto c^s$; invariant mass gives $s=0$, $P=2$).

Therefore:
$$\tau_\text{total}
= \frac{1}{4kR_0^2}
= \frac{3}{4\,H_0^{\text{hor}}}
= \frac{3}{4} \cdot \frac{P}{H_0^{\text{obs}}}
= \frac{3P}{4\,H_0^{\text{obs}}}.$$

For the preferred invariant-mass branch ($s=0$, $P=2$):
$$\boxed{\tau_\text{total} = \frac{3}{2\,H_0^{\text{obs}}} \approx 21\ \text{Gyr}}
\qquad (H_0^{\text{obs}} = 70\ \text{km/s/Mpc},\ H_0^{-1} \approx 13.97\ \text{Gyr}).$$

**Note on the earlier 10.5 Gyr value.** Previous versions of this document and of the
Core Principles used $\tau = (3/4)H_0^{-1} \approx 10.5$ Gyr, which implicitly set
$H_0 = H_0^{\text{hor}} = 35$ km/s/Mpc (i.e., confused $H_0^{\text{hor}}$ with
$H_0^{\text{obs}}$). The derivation above is correct; the factor-2 error entered when
the two-$H_0$ distinction was introduced for distances (§4a of Core Principles) but
the time formula was not simultaneously updated.

### General mass scaling

For a general mass scaling $m \propto c^s$ (clock frequency $\nu \propto c^P$,
$P = s+2$), the same substitution gives:
$$\tau_\text{total} = \frac{3P}{(3P-2)\,H_0^{\text{obs}}},\quad P = s+2.$$
This converges only for $P > 2/3$ (equivalently $s > -4/3$). For $P \leq 2/3$ the
integral diverges and the proper age is infinite.

**Invariant mass** ($s=0$, $P=2$): $\tau = 3\cdot2/(4\,H_0^{\text{obs}}) = 3/(2H_0^{\text{obs}}) \approx 21$ Gyr.

**PV mass** ($s=-3/2$, $P=1/2 < 2/3$): the integral
$\int_0^\infty (1+2kR_0^2 u)^{-3/4}\,du$ diverges (the integrand decays only as
$u^{-3/4}$, which is not integrable). $\tau_\text{total} = \infty$ for PV mass.

**Old Machian mass** ($s=1$, $P=3$): $\tau = 9/(7H_0^{\text{obs}}) \approx 18$ Gyr
(this branch was discarded for other reasons — T4, T8).

---

## Lookback Time at Redshift $z$

The proper lookback time to a source at redshift $z$ follows the same integral with
upper limit $u(z)$. Using $(1+2kR_0^2 u(z)) = (1+z)^{2/(3P)}$ (from Core Principles
§4a):
$$\tau(z) = \frac{3}{4\,H_0^{\text{hor}}}\left[1-(1+z)^{-4/(3P)}\right]
= \frac{3P}{4\,H_0^{\text{obs}}}\left[1-(1+z)^{-4/(3P)}\right].$$

For $P=2$: $4/(3P) = 2/3$, so:
$$\tau(z) = \frac{3}{2\,H_0^{\text{obs}}}\left[1 - (1+z)^{-2/3}\right].$$

Representative values for $H_0^{\text{obs}} = 70$ km/s/Mpc ($\tau_\infty \approx 20.95$ Gyr):

| $z$ | $\tau(z)$ (Gyr) | fraction of $\tau_\infty$ | ΛCDM $\tau$ (Gyr) |
|---:|---:|---:|---:|
| 0.1 | 1.29 | 6% | 1.30 |
| 0.5 | 4.96 | 24% | 5.04 |
| 1 | 7.75 | 37% | 7.72 |
| 2 | 10.88 | 52% | 10.24 |
| 5 | 14.60 | 70% | 12.31 |
| 10 | 16.72 | 80% | 13.00 |
| $\infty$ | 20.95 | 100% | 13.80 |

A striking feature: at $z \leq 1$ the model's lookback times agree with ΛCDM to within
1%. The models diverge significantly only beyond $z \approx 2$, where the model
predicts older lookback times. This is a consequence of the corrected total age being
larger, with the difference concentrated at high redshift.

---

## Fit with the Model

The model predicts a proper age of $\approx 21$ Gyr for $H_0^{\text{obs}} = 70$
km/s/Mpc. This is **above** the age of the oldest globular clusters ($\sim 12$–$13$
Gyr), so the stellar-age lower bound is satisfied with a comfortable margin.

The model age is also **$\sim 7$ Gyr older than ΛCDM**. This is not constrained from
below by stellar ages, but raises the question of whether other observations independently
bound the age from above:

1. **High-$z$ structure formation.** At $z = 10$, the lookback time in this model is
   $\sim 16.7$ Gyr — considerably more than ΛCDM's $\sim 13$ Gyr. Galaxies and quasars
   observed at $z \sim 6$–$10$ formed when the universe was already several Gyr old
   by the model's clock. This gives more time for early structure to form (easing some
   ΛCDM tensions with JWST observations), but the dynamics of structure formation in
   a variable-$c$ background have not been computed.

2. **BAO and $H(z)$ measurements.** At $z \leq 1$ the model's lookback times almost
   exactly match ΛCDM, so BAO-derived $H(z)$ measurements at $z \lesssim 1$ would not
   strongly distinguish the two models on the basis of timing.

3. **The $H_0$ dependence.** The age scales as $(H_0^{\text{obs}})^{-1}$. With the
   local distance-ladder value $H_0 = 73$ km/s/Mpc: $\tau \approx 3/2 \times 13.4
   \approx 20$ Gyr — still well above the stellar lower bound.

The corrected age is thus **not in tension with stellar ages** and does not require
a resolution. The relevant open question is whether a 21 Gyr universe is consistent
with all other observational inputs, particularly at high $z$.

---

## Coordinate vs. Proper Age: No Big Bang in Map Time

The model's infinite coordinate past does not mean the universe is infinitely old in
any physical sense. Atomic clocks barely ticked during epochs of very low $c$. The
21 Gyr proper age is finite, computable, and represents the total accumulated clock
time available for physical processes.

The variant S′ of premise 2 ($c \propto R^{2/3}$) gives a **finite coordinate-time
origin** — a genuine Big Bang in map time. The S′ proper age has not been computed
and may differ from the volume-law value. See T4 for the S′ discussion.

---

## Open Questions

- The factor-2 correction to the age propagates into the comparison table in Core
  Principles §4a (the $\tau$ column). Both documents have been updated consistently.
- Is there a direct observational constraint on the age from above (independent of
  ΛCDM)? White dwarf cooling curves and metal-poor star ages set lower bounds, not
  upper bounds.
- Is there a self-consistent value of $H_0^{\text{obs}}$ and $P = s+2$ that fits
  both the supernova Hubble diagram (T4) and the lookback-time structure simultaneously?
  This is the natural joint constraint from the full redshift–distance–time relation.
- The S′ finite-origin variant: what is its proper age?
