# T7 — The Fine-Structure Constant

## Observational Background

The fine-structure constant $\alpha$ characterizes the strength of the electromagnetic
interaction:
$$\alpha = \frac{e^2}{4\pi\epsilon_0\hbar c} \approx \frac{1}{137.036}.$$
It is dimensionless and appears in the splittings of atomic spectral lines, the
Lamb shift, the electron's anomalous magnetic moment, and the opacity of atoms to
electromagnetic radiation.

Because $\alpha$ is dimensionless, its value is independent of unit conventions. Any
change in $\alpha$ over cosmic time would alter the pattern of atomic spectra in a way
distinguishable from a simple Doppler or cosmological redshift — it would change
*line ratios*, not just line positions. This makes $\alpha$ variation a unique probe:
it can be measured from absorption-line spectra of quasars at high redshift without
needing an independent distance calibration.

### Current observational bounds

The most precise measurements use the Many Multiplet (MM) method applied to
high-resolution quasar absorption spectra. Key results:

- **ESPRESSO (VLT):** $\Delta\alpha/\alpha = 1.3 \pm 1.3$ ppm at $z \sim 1.15$
  (Martins et al. 2022). Consistent with zero variation.
- **Earlier Webb et al. (2011) claims** of a spatial dipole variation (at ~$5\sigma$,
  with $|\Delta\alpha/\alpha| \lesssim 10$ ppm) remain controversial and have not
  been confirmed by independent groups.
- **Overall constraint:** $|\Delta\alpha/\alpha| \lesssim$ a few ppm over $0 < z < 2$,
  and $\lesssim 10^{-5}$ on laboratory timescales (optical clock comparisons).

Any model predicting $|\Delta\alpha/\alpha| > 1$–$2$ ppm at $z \sim 1$ is in tension
with ESPRESSO.

---

## The Model's Prediction: Classical $\alpha$ Invariance

### Why $\alpha$ is invariant at tree level

The fine-structure constant is:
$$\alpha = \frac{e^2}{4\pi\epsilon_0\hbar c}.$$
In this model:
- $e$ is invariant (premise 4).
- $\hbar = h/(2\pi)$ is invariant (premise 4).
- $\epsilon_0 \propto c^{-1}$ (forced by electromagnetism — Core Principles §2).
- $c$ varies as $c(t)$.

Substituting $\epsilon_0 \propto c^{-1}$:
$$\alpha \propto \frac{e^2}{\epsilon_0 \hbar c} \propto \frac{e^2}{c^{-1} \cdot \hbar \cdot c} = \frac{e^2}{\hbar} = \text{const}.$$
The factors of $c$ and $c^{-1}$ cancel identically. **Classical $\alpha$ is exactly
invariant in this model.** This is not fine-tuned — it is forced by the same argument
that makes $\epsilon_0 \propto c^{-1}$: the electromagnetic relation $c = 1/\sqrt{\epsilon_0\mu_0}$
fixes the product $\epsilon_0 c$ once $c$ is chosen and $\mu_0 \propto c^{-1}$
(which follows from the symmetric PV split preserving $Z_0 = \sqrt{\mu_0/\epsilon_0}$).

### The Bohr radius and atomic sizes

As a consequence, the Bohr radius
$$a_B = \frac{4\pi\epsilon_0\hbar^2}{m_e e^2} \propto \epsilon_0 \propto c^{-1}$$
scales inversely with $c$. Atoms were physically **larger** when $c$ was smaller.
At $z = 1$ (where $c_\text{emit} = c_\text{now}/\sqrt{2}$), atoms were $\sqrt{2} \approx 1.41$
times larger than today.

This does not affect the fine-structure constant (it cancels in $\alpha$), but it does
affect lengths and cross-sections. It is consistent with the general scaling of all
length scales with $c^{-1}$ in the model.

---

## The Open Question: QED Corrections

The classical ($\alpha$-invariant) result is robust. However, the actual value of $\alpha$
at any epoch includes radiative corrections from quantum electrodynamics (QED) — the
Uehling potential, vacuum polarization, and higher-order loops.

The leading vacuum-polarization correction to the effective coupling at a momentum
scale $q$ is of order $\alpha/(3\pi) \ln(q^2/m_e^2c^4/\hbar^2)$. If the
electron's Compton wavelength $\lambda_C = h/(m_e c)$ changes with $c$ (it does:
$\lambda_C \propto c^{-1}$), then the renormalization group running of $\alpha$ between
two epochs could introduce a small drift.

The relevant question: **does the QED effective coupling $\alpha(q^2)$, evaluated at
the atomic momentum scale $q \sim m_e c$, drift with cosmic time due to the changing
Compton wavelength?**

Multiple derivation attempts in earlier sessions produced inconsistent magnitudes,
due to errors in distinguishing additive from multiplicative perturbations. A clean
first-order calculation has not been completed.

**What is needed:** a systematic QED treatment in the background of varying $c$, keeping
track of which quantities are physical observables (transition energies, cross-sections)
and which are artifacts of the renormalization scheme. The drift, if any, must be
compared to the ESPRESSO bound of $|\Delta\alpha/\alpha| \lesssim 1$–$2$ ppm at $z \sim 1$.

With $c$ changing by a factor of $\sqrt{2}$ from $z = 1$ to today
($(1+z)^{-1/2} = 1/\sqrt{2}$, so $c_\text{now}/c_\text{emit} = \sqrt{2} \approx 1.41$,
a $\sim 41\%$ increase), the relevant log-change at the atomic scale $q \sim m_e c$ is:
$$\Delta\ln\!\left(\frac{m_e^2 c^4}{q^2}\right) = \Delta\ln(c^2) = \ln 2 \approx 0.69.$$
A naive QED correction of order $\alpha/(3\pi) \sim 7.7 \times 10^{-4}$ then gives:
$$\frac{\Delta\alpha}{\alpha} \sim \frac{\alpha}{3\pi}\,\ln 2 \approx 5 \times 10^{-4},
\quad \text{or } \sim 500\ \text{ppm}$$
— far above the ESPRESSO bound if correct. However, this estimate is speculative; the
actual QED correction in this framework needs careful treatment.

---

## Observational Implications

If the model's QED correction is large ($\gg 1$ ppm), it would be **excluded by
ESPRESSO**. This would be a clean, model-independent falsification.

If the QED correction is small ($\ll 1$ ppm), the model is safe and in fact makes a
clean prediction: $\alpha$ is exactly invariant at the classical level, and any
future detection of $\alpha$ variation would challenge the model's premises.

The ESPRESSO constraint applies at $z \sim 1.15$. More distant measurements (e.g., from
ALMA spectra at $z > 3$) would probe larger changes in $c$ and therefore larger
potential QED corrections.

---

## Open Questions

- A clean first-order QED calculation of the running of $\alpha$ in a variable-$c$
  background. Specifically: does the Compton wavelength's change with $c$ feed into
  the renormalization group running in a way observable in atomic spectra?
- The ESPRESSO bound is the most stringent test currently available. A predicted
  $\Delta\alpha/\alpha$ as a function of $z$ would allow direct comparison.
- The Bohr radius $\propto c^{-1}$: are there observational consequences for atomic
  cross-sections or opacities at high redshift that could test this scaling?
- The symmetric PV split ($\epsilon_0 = \mu_0 = K\epsilon_0^{(0)}$) is the assumption
  that enforces $Z_0 = $ const and hence $\alpha = $ const classically. An asymmetric
  split (e.g., only $\epsilon_0$ varying) would break $\alpha$-invariance at tree level.
  The polarization-alignment observational argument for the symmetric split should be
  examined more carefully.
