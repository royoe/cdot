# T10 — Galaxy Size Evolution

## Observational Background

High-redshift galaxies observed in deep imaging surveys (HST, JWST, and ground-based
adaptive optics) are systematically **smaller** than local galaxies of the same stellar
mass. This size evolution is one of the most striking and robustly established results
in observational galaxy evolution.

### The observed scaling

For early-type (elliptical/lenticular) galaxies:
$$r_e \propto (1+z)^{-1.5 \pm 0.3}$$
(effective radius shrinks by a factor of $\sim (1+2)^{1.5} = 2.6^{1.5} \approx 4$ from
$z = 2$ to today for early types).

For late-type (spiral/disk) galaxies:
$$r_e \propto (1+z)^{-0.75 \pm 0.2}$$
(less extreme evolution; spirals at $z = 2$ are roughly $(1+2)^{0.75} \approx 2.3$
times smaller than today).

These results are from large surveys (COSMOS, CANDELS, 3D-HST, UltraVISTA, EGS) and
are generally agreed upon, though the precise exponent depends on the selection
criterion (fixed stellar mass, fixed number density, fixed luminosity).

### Interpretation in ΛCDM

In the standard picture, galaxy size evolution is driven by:
1. **Mergers:** dry (gas-poor) major and minor mergers deposit material in the outskirts
   of galaxies, puffing them up.
2. **Adiabatic expansion** (mass loss from stellar winds and supernovae).
3. **Initial conditions:** high-$z$ galaxies formed from higher-density environments
   when the universe was smaller.

The ΛCDM picture can reproduce the observed trends with simulations (IllustrisTNG,
EAGLE, etc.) but the physical mechanisms, their relative contributions, and their
comparison to the data are still actively discussed.

---

## The Model's Prediction

### From orbital expansion

In this model, orbits expand as $r \propto c^2$ (Core Principles §6, T9). The same
argument applies to any gravitationally bound system: a galaxy's stellar orbits all
expand together as $c$ increases.

Since $c/c_0 = (1+z)^{-1/2}$ (from the squared redshift law):
$$r \propto c^2 \propto (1+z)^{-1},$$
so the effective radius of a galaxy scales as:
$$\boxed{r_e \propto (1+z)^{-1}.}$$

At $z = 2$: galaxies are $(1+2)^1 = 3$ times smaller than today. This is a definite,
parameter-free prediction of the model.

### Comparison with observations

The model's exponent $-1$ lies between the observed values for late-type ($-0.75$)
and early-type ($-1.5$) galaxies. It is:
- **Consistent** with late-type galaxies to within $\sim 1.5\sigma$.
- **Lower** than early-type galaxies (model predicts less size evolution than observed
  for ellipticals).

This bracketing of the observed range by a single theoretical prediction — with no
free parameters — is a **consistency success** of the model. It is not a perfect
fit, but it captures the right order of magnitude and the right direction.

### No mergers required

In ΛCDM, a factor of $\sim 4$ size evolution from $z = 2$ to today for early-type
galaxies requires a significant merger history, which is computationally challenging
to produce at the right rate with the right zero-point. In this model, the size
evolution is driven by the cosmological expansion of orbits — it happens passively, in
all galaxies, at the rate set by $H_0^{\text{hor}}$. No mergers are needed; mergers
would be an additional effect on top of the baseline cosmological expansion.

---

## Caveats and the Model-Type Dependence

The model predicts a universal exponent $-1$, but the observations show different
exponents for different morphological types. Several explanations are possible:

1. **Initial conditions:** the model gives the cosmological baseline. Additional
   processes (mergers, gas inflow, quenching) can add or subtract from this baseline
   differently for early vs. late types.

2. **Selection effects:** early-type galaxies are preferentially selected at fixed
   stellar mass (which is itself evolving); late-type galaxies may be selected at
   fixed luminosity or fixed number density, introducing different systematic offsets.

3. **Half-light vs. half-mass radius:** sizes are typically measured as half-light
   (effective) radii. If the stellar mass-to-light ratio changes with redshift (as
   stellar populations age), the half-light and half-mass radii evolve differently.

4. **The model's exponent is for adiabatic orbital expansion.** If galaxies form with
   a range of dynamical structures (extended disks vs. compact spheroids), the rate
   of adiabatic expansion could differ.

None of these effects has been quantitatively computed within this model. The
prediction $r \propto (1+z)^{-1}$ is the baseline; realistic evolution would require
detailed modelling.

---

## JWST and the Compact Galaxy Puzzle

JWST observations have revealed large numbers of massive, compact galaxies at $z > 3$
(and even $z > 6$), some with stellar masses comparable to modern ellipticals but sizes
$\sim 5$–$10$ times smaller. In ΛCDM, forming such massive compact systems so early
requires very high star-formation efficiencies and is challenging for standard models.

In this model:
- The prediction $r \propto (1+z)^{-1}$ means that at $z = 5$, galaxies should be
  $6\times$ smaller than today (at the same stellar mass). This is consistent with
  JWST observations without requiring any special early star formation efficiency.
- The model's smaller horizon at early epochs also means fewer particles within the
  causal radius, so the gravitational dynamics of early galaxy formation would be
  qualitatively different (faster $c$ growth, different cooling times, etc.).

JWST's ability to resolve compact galaxies at very high $z$ makes this one of the
most powerful near-term tests of the model's size-evolution prediction.

---

## Open Questions

- A quantitative comparison with galaxy size–redshift data at $0 < z < 10$ from HST
  and JWST, using the model's prediction $r_e \propto (1+z)^{-1}$ as the null hypothesis.
  What is the fit quality compared to ΛCDM with mergers?
- The observed scatter in size evolution: is the intrinsic scatter consistent with
  the model's prediction (where $r/r_0$ is universal at fixed $z$) or does it
  require additional mechanisms?
- The morphology dependence: can the model's baseline $r \propto (1+z)^{-1}$ account
  for early-type evolution ($-1.5$) if mergers add an additional $\sim (1+z)^{-0.5}$
  factor on top?
- Surface brightness evolution: since $r \propto c^2$ and luminosities scale as
  $L \propto c^4$, the surface brightness $\Sigma \propto L/r^2 \propto c^4/c^4 = \text{const}$.
  This predicts **no surface-brightness evolution at fixed stellar mass** — a
  potentially strong observational test.
