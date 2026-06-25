# T4 — Supernovae and Cosmic Acceleration

## Observational Background

Type Ia supernovae (SNe Ia) are used as cosmological "standard candles": their peak
luminosities are approximately uniform (with empirical corrections via the
Phillips relation between peak brightness and decline rate, and colour), allowing
distances to be inferred from observed fluxes. The luminosity distance $D_L$ is:
$$\mu = 5\log_{10}\!\left(\frac{D_L}{10\ \text{pc}}\right), \qquad D_L = (1+z)D_\text{p}.$$

The 1998 discovery (Riess et al., Perlmutter et al.) that distant SNe Ia ($z \sim 0.3$–$1$)
appear $\sim 0.2$–$0.3$ magnitudes **dimmer** than expected in a matter-only decelerating
universe was the primary evidence for cosmic acceleration and the dark energy ($\Lambda$).
The result has been confirmed and extended by the Pantheon and Pantheon+ datasets
(Scolnic et al. 2018, Brout et al. 2022), which together cover $0 < z < 2.3$.

The inferred cosmological deceleration parameter for ΛCDM is $q_0 \approx -0.55$
(with $\Omega_m \approx 0.3$, $\Omega_\Lambda \approx 0.7$), indicating that the
expansion of the universe is currently accelerating.

---

## The Model's Prediction: Structural Deceleration

### The deceleration parameter

For a general power-law horizon $c \propto R^n$ (volume law $n=3$, surface law $n=2$,
S′ law $n=2/3$) combined with the squared redshift law ($P = s+2 = 2$ for $s=0$) and
the standard-candle luminosity distance $D_L = (1+z)D_\text{p}$, the deceleration
parameter is:
$$\boxed{q_0 = \frac{1}{nP}.}$$

For the preferred volume law ($n=3$, $P=2$): $q_0 = 1/6 \approx +0.17$.

This is **strictly positive for any $n > 0$ and $P > 0$**. The model predicts mild
deceleration, not acceleration.

### Why $q_0 < 0$ is structurally impossible

For $q_0 < 0$, one needs either $n < 0$ or $P < 0$. But:

- **$n < 0$ means $c$ was larger in the past**, so $c_\text{emit} > c_\text{now}$, which
  gives $1+z < 1$ — a blueshift. This is refuted by the observed ubiquity of
  cosmological redshift.
- **$P < 0$ means $s < -2$**, a mass scaling $m \propto c^s$ with $s < -2$. This is
  exotic, unmotivated, and would imply mass growing faster than $c^2$ as $c$ decreases —
  physically unreasonable.

**There is no version of this model that mimics dark energy.** This is a structural
result, not a numerical coincidence. The model cannot mimic cosmic acceleration
regardless of parameter choices.

### The SN magnitude residual

Using $P = 2$ and $H_0^{\text{obs}} = 70$ km/s/Mpc, the luminosity-distance residuals
compared to the concordance ΛCDM model are:

| $z$ | $D_L$ (model) | $D_L$ (ΛCDM) | $\Delta\mu$ |
|---:|---:|---:|---:|
| 0.1 | 445 Mpc | 460 Mpc | $-0.07$ |
| 0.5 | 2519 Mpc | 2833 Mpc | $-0.26$ |
| 1.0 | 5607 Mpc | 6608 Mpc | $-0.36$ |
| 2.0 | 12898 Mpc | 15540 Mpc | $-0.40$ |
| 5.0 | 39803 Mpc | 46652 Mpc | $-0.34$ |

$\Delta\mu < 0$ means the model predicts SNe are **brighter** (closer) than ΛCDM.
Equivalently, the model predicts SNe are slightly less dim than a decelerating universe
would give — but not as faint as a ΛCDM accelerating universe predicts. Since the
original SN discovery compared to a flat matter-dominated model, and found SNe *dimmer*,
the model sits between the matter-only expectation and ΛCDM.

The residual has a **shape** (peaks near $z \approx 2$, falls at low and high $z$), not
a flat offset. This shape encodes the $q_0 = +1/6$ deceleration signal.

---

## The Horizon-Law Variants

### Volume law ($c \propto R^3$, baseline)

$q_0 = 1/6$. No finite coordinate-time origin; the horizon has grown from $c = 0$
infinitely far in the past (in coordinate time).

### Surface law ($c \propto R^2$)

$q_0 = 1/4$. Slightly larger deceleration, slightly worse SN tension.

### S′ law ($c \propto R^{2/3}$)

$q_0 = 3/4$. This variant was initially thought to mimic acceleration (under the old
linear redshift law), but that was an artifact of the incorrect linear law. With the
corrected squared law, S′ gives $q_0 = 3/4$, which is **worse** than the volume law.

S′ has one attractive feature: it gives a **finite coordinate-time origin** (a genuine
Big Bang in map time), which is required for the genesis bootstrap of T13. But it makes
the SN tension more acute.

---

## What This Means for the Model

The SN tension is the model's most serious empirical constraint. Two framings:

**Framing 1 (pessimistic).** The Pantheon+ data robustly establish $q_0 < 0$ at $> 5\sigma$.
The model predicts $q_0 > 0$. The model is excluded.

**Framing 2 (honest and open).** The $q_0 < 0$ conclusion rests on SNe Ia being
standard candles to better than $\sim 0.1$–$0.2$ mag precision over the full $z$ range.
This is non-trivial. The Phillips correction and colour correction are empirical; there
are ongoing debates about host-galaxy systematics, Milky Way dust, and potential
evolution of the SN population with redshift. The Pantheon+ analysis derives
$q_0 \approx -0.55$ within ΛCDM; it has not been done within this model's framework.

The honest statement is: **the model cannot mimic dark energy, and its viability
therefore depends entirely on an external empirical question — whether cosmic
acceleration is as robustly established as currently believed, specifically whether
SNe Ia are reliable standard candles to the precision the acceleration claim requires.**
This is a live debate in the community (see e.g. discussions of stretch-parameter
evolution, SHOES vs. UNITY analyses, and dust modelling uncertainties).

### What is needed

A genuine comparison requires fitting the Pantheon+ dataset directly within the model's
framework — using the model's $D_L(z)$ formula and its own covariance structure rather
than comparing model predictions to ΛCDM-derived posteriors. This has not been done and
is the single highest-priority empirical test.

---

## The Standard-Candle Assumption in the Model

For SNe to serve as standard candles in this model, the intrinsic luminosity $L$ of a
Type Ia SN must be the same in the model's proper units at all redshifts. Since the
model has $c$ increasing over cosmic time, and since stellar luminosity scales as
$L \propto c^4$ (T9), **a SN at higher $z$ (lower $c$) would be intrinsically less
luminous** in map-frame units. However, the standard-candle condition is defined in
proper (atomic) units at the time of emission, where the luminosity is derived from
the same nuclear physics at all epochs. In proper units the luminosity is invariant
(the $c^4$ factor is a map-frame artifact, not a physical dimming). This is consistent
with the energy-conserving map frame (T11): what changes is the coordinate description,
not the physical measurement.

---

## Open Questions

- A direct Pantheon+ fit: compute the model's predicted $\mu(z)$ curve and compare
  to the Pantheon+ data with proper covariance. Does the $q_0 = +1/6$ signal appear
  at a level exceeding the data scatter?
- What is the constraint on the mass-scaling exponent $s$ from SN data? The shape
  of $\mu(z)$ is sensitive to $P = s+2$; a MCMC fit could constrain $s$.
- If the SN data firmly require $q_0 < 0$ even after model-native analysis, the model
  is definitively excluded — this outcome should be pursued, not avoided.
- The Etherington reciprocity relation $D_A = D_L/(1+z)^2$ is satisfied exactly by the
  model (the model sits on the Etherington line). This means it makes the same
  angular-diameter–luminosity-distance connection as ΛCDM, providing a consistency
  check between SN distances and angular-size measurements (e.g. BAO).
