# T3 — The Hubble Constant

## Observational Background

The Hubble constant $H_0$ quantifies the present-day rate of apparent recession of
distant galaxies: $v = H_0 D$ at low redshift, where $v = cz$ is the apparent
recession velocity and $D$ is the proper distance. It is among the most precisely
measured and most contested quantities in cosmology.

Current measurements fall into two groups with a $\sim 5\sigma$ tension:

- **Early-universe (CMB-based) methods:** Planck 2018 gives $H_0 = 67.4 \pm 0.5$
  km/s/Mpc. This is derived by fitting the acoustic structure of the CMB power spectrum
  within the ΛCDM framework; it is a model-dependent inference, not a direct
  measurement.

- **Late-universe (distance ladder) methods:** The SH0ES collaboration gives
  $H_0 = 73.04 \pm 1.04$ km/s/Mpc, anchored to Cepheid-calibrated Type Ia supernovae.
  This is a more direct geometric measurement but depends on calibration steps.

The discrepancy between these two values — the "Hubble tension" — is one of the most
discussed open problems in modern cosmology. It may indicate new physics, unresolved
systematic errors in one or both methods, or both.

---

## Two Hubble Constants in the Model

The model has **two distinct quantities** that both carry the label $H_0$, and
conflating them is a serious source of error.

### Horizon rate $H_0^{\text{hor}}$

This is the fractional growth rate of $c$:
$$H_0^{\text{hor}} \equiv \left.\frac{\dot c}{c}\right|_0 = 3kR_0^2.$$
It is the natural "internal" parameter of the horizon-evolution equation. In terms of
the present horizon radius $R_0$: $H_0^{\text{hor}} = 3c_0/R_0$.

### Observable Hubble constant $H_0^{\text{obs}}$

This is what an astronomer measures from the low-$z$ redshift–distance slope. Taylor-
expanding the distance formula at small $z$:
$$D_\text{p}(z) \approx \frac{c_0}{H_0^{\text{obs}}} z + \ldots$$
Working this out from the model's distance formula (Core Principles §4):
$$H_0^{\text{obs}} = P \cdot H_0^{\text{hor}}, \qquad P = s + 2$$
where $s$ is the mass scaling ($m \propto c^s$, $s = 0$ for invariant mass) and $P = 2$
in the preferred branch.

**The relation is $H_0^{\text{obs}} = 2\,H_0^{\text{hor}}$.** When one quotes
"$H_0 = 70$ km/s/Mpc," one is quoting $H_0^{\text{obs}}$. The horizon radius is then:
$$R_0 = \frac{3c_0}{H_0^{\text{hor}}} = \frac{3P\,c_0}{H_0^{\text{obs}}} = \frac{6c_0}{H_0^{\text{obs}}}.$$
Using $H_0^{\text{obs}} = 70$ km/s/Mpc: $R_0 = 6c_0/H_0^{\text{obs}} \approx 25.7$ Gpc.

This factor-$P$ difference is **not cosmetic** — using $H_0^{\text{obs}}$ directly in
$R_0 = 3c_0/H_0$ (as an earlier derivation did) understates $R_0$ by the factor $P$
and produces a spurious $\approx -1.8$ magnitude offset in the SN Hubble diagram.

### Physical meaning of $H$ in this model

In standard cosmology, $H$ is the rate of expansion of space: $H = \dot a/a$. In this
model, space is static; there is no $\dot a$. Instead,
$$H \equiv \frac{\dot c}{c}.$$
The Hubble "constant" is the fractional rate of increase of the speed of light. It is
not a constant in time. From $H^{\text{hor}} = \dot{c}/c = 3kR^2$, the horizon rate
grows as $R$ grows — it was smaller in the early universe and $H_0^{\text{hor}}$
is the present-day maximum:
$$H^{\text{hor}}(z) = \frac{H_0^{\text{hor}}}{(1+z)^{1/3}}\quad(P=2),
\qquad H^{\text{hor}}(u) = \frac{H_0^{\text{hor}}}{1 + 2kR_0^2\,u}.$$
The model is structurally **decelerating** ($q_0 = +1/6 > 0$, T4) — sources at high
$z$ appear closer than in dark-energy-dominated $\Lambda$CDM. See T4 for the SN
implications.

---

## The Hubble Tension and This Model

The Hubble tension is a discrepancy within the ΛCDM framework — between the value of
$H_0$ inferred from early-universe physics (CMB) and late-universe distance measurements
(distance ladder). This model offers a different conceptual framing, but it does not
automatically resolve the tension.

Within this model, the observable $H_0^{\text{obs}}$ is what the distance-ladder methods
measure directly from the redshift–distance slope. The CMB would need to be reinterpreted
within the model's framework (the CMB acoustic scale would map differently to $H_0$ because
the model's $H(z)$ history differs from ΛCDM's). A genuine comparison requires computing
the model's CMB power spectrum, which has not been done.

What is clear: **the model is structurally decelerating** ($q_0 = +1/6 > 0$, T4),
which is qualitatively different from ΛCDM's dark-energy-driven acceleration at late times. Whether this difference could account for the tension between early and
late $H_0$ measurements is an open and potentially interesting question, but no
quantitative answer is available.

---

## $H_0$ and the Proper Age

The proper age of the universe in the model is $\tau_\infty = \tfrac{3}{2}H_0^{-1}$
where $H_0 = H_0^{\text{obs}}$. The age–$H_0$ relation is therefore:
$$\tau_\infty H_0^{\text{obs}} = \tfrac{3}{2} = 1.5.$$
Compare to ΛCDM's $\tau_\infty H_0 \approx 0.96$ (for the concordance parameters).
This model's product is larger, meaning for the same $H_0$ the model predicts an
older universe ($\approx 21$ Gyr vs $\approx 13.8$ Gyr). See T1 for full discussion.

---

## $H(z)$: Comparison with ΛCDM

The evolution of the Hubble parameter with redshift is a direct observable from baryon
acoustic oscillations (BAO) and other probes.

| $z$ | $H(z)$ (model, $P=2$) / $H_0$ | $H(z)$ (ΛCDM) / $H_0$ |
|---:|---:|---:|
| 0 | 1 | 1 |
| 0.5 | $\approx 1.28$ | $\approx 1.32$ |
| 1 | $\approx 1.59$ | $\approx 1.72$ |
| 2 | $\approx 2.12$ | $\approx 2.60$ |

*(Model values use $H^{\text{obs}}(z) = H_0^{\text{obs}}(1+z)^{1/(3P)} \cdot 3kR_0^2/H_0^{\text{obs}} \cdot (1+z)^{2/(3P)}$
— the exact expression requires the coordinate-time conversion.)*

Both models give $H$ rising with $z$, but the model's rise is shallower at high $z$
due to deceleration rather than acceleration at late times. BAO data (which essentially
measure $H(z)/H_0$) could in principle distinguish the two.

---

## Open Questions

- A full BAO-data comparison: does the model's $H(z)$ evolution fit the observed
  $H(z)/H_0$ measurements (from SDSS, eBOSS, DESI) as well as ΛCDM?
- The Hubble tension: could the model's reinterpretation of the CMB acoustic scale
  reduce or eliminate the tension? This requires a full CMB power spectrum calculation
  within the model.
- The two-$H_0$ distinction is essential bookkeeping — it should be explicitly
  flagged in every numerical comparison with observational data.
